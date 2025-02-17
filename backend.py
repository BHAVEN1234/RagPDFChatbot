import os
import shutil
import logging
import asyncio
from concurrent.futures import ThreadPoolExecutor
import pickle
from typing import List
import numpy as np
import hashlib

from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer
from langchain_groq import ChatGroq
from PyPDF2 import PdfReader
from pydantic import BaseModel
import json
from nltk.tokenize import sent_tokenize
import nltk
import sqlite3

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')  # Ensure the punkt_tab resource is available

# Initialize FastAPI app
app = FastAPI()

# Initialize storage dictionaries
API_KEYS = {}
MODEL_CONFIG = {}

# Constants
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Pydantic models
class QueryRequest(BaseModel):
    query: str
    collection_name: str

class SettingsData(BaseModel):
    qdrant_api_key: str
    qdrant_cloud_url: str
    embedding_model: str
    groq_api_key: str

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for optimized chunking and batching
MAX_CHUNK_SIZE = 512  # maximum words per chunk
CHUNK_OVERLAP = 50
BATCH_SIZE = 10       # number of chunks processed per batch

def compute_md5(text: str) -> str:
    """Compute an MD5 hash of the given text."""
    return hashlib.md5(text.encode("utf-8")).hexdigest()

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from PDF file page by page to reduce memory overhead."""
    try:
        logging.info(f"Extracting text from PDF: {pdf_path}")
        reader = PdfReader(pdf_path)
        text_parts = []
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text_parts.append(page_text)
        full_text = "\n".join(text_parts)
        logging.info(f"Successfully extracted text from PDF: {pdf_path}")  # Corrected log message
        return full_text
    except Exception as e:
        logging.error(f"Error extracting text from PDF {pdf_path}: {e}")
        raise

def split_text_into_sentences(text: str) -> List[str]:
    """Splits a large text into sentences using NLTK."""
    try:
        sentences = sent_tokenize(text)
        return sentences
    except Exception as e:
        logging.error(f"Error splitting text into sentences: {e}")
        raise

def chunk_text(sentences: List[str], max_chunk_size: int = MAX_CHUNK_SIZE, chunk_overlap: int = CHUNK_OVERLAP) -> List[str]:
    """Chunks the text into smaller parts based on token count and overlap."""
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        # Estimate words in the sentence
        word_count = len(sentence.split())
        if len(current_chunk.split()) + word_count > max_chunk_size:
            chunks.append(current_chunk)
            # Implement overlap by taking the last 'chunk_overlap' words
            overlap_words = current_chunk.split()[-chunk_overlap:]
            current_chunk = " ".join(overlap_words) + " " + sentence
        else:
            current_chunk += " " + sentence
    if current_chunk:
        chunks.append(current_chunk)
    return chunks

def get_embedding(text: str, embedding_model_name: str) -> List[float]:
    """Generate embeddings for the given text using SentenceTransformer."""
    try:
        model = SentenceTransformer(embedding_model_name)
        embedding = model.encode(text).tolist()
        return embedding
    except Exception as e:
        logging.error(f"Error generating embedding for text: {e}")
        raise

def initialize_qdrant_client(qdrant_cloud_url: str, qdrant_api_key: str):
    """Initialize and return a Qdrant client."""
    try:
        client = QdrantClient(
            url=qdrant_cloud_url,
            api_key=qdrant_api_key,
        )
        return client
    except Exception as e:
        logging.error(f"Error initializing Qdrant client: {e}")
        raise

def create_collection(client: QdrantClient, collection_name: str, embedding_size: int):
    """Create a collection in Qdrant if it doesn't exist."""
    try:
        client.recreate_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=embedding_size, distance=Distance.COSINE),
        )
        logging.info(f"Collection '{collection_name}' created or already exists.")
    except Exception as e:
        logging.error(f"Error creating Qdrant collection: {e}")
        raise

async def process_and_upsert_pdf(file_path: str, collection_name: str, qdrant_cloud_url: str, qdrant_api_key: str, embedding_model: str):
    """Process the PDF, chunk text, generate embeddings, and upsert to Qdrant."""
    try:
        logging.info(f"Processing PDF: {file_path}, Collection: {collection_name}")

        # Extract text
        text = extract_text_from_pdf(file_path)

        # Split into sentences
        sentences = split_text_into_sentences(text)

        # Chunk the sentences
        chunks = chunk_text(sentences)

        # Initialize Qdrant client
        client = initialize_qdrant_client(qdrant_cloud_url, qdrant_api_key)

        # Determine embedding size
        sample_embedding = get_embedding(chunks[0], embedding_model)  # Get one sample embedding
        embedding_size = len(sample_embedding)

        # Create collection
        create_collection(client, collection_name, embedding_size)

        # Prepare points for Qdrant
        points = []
        for chunk in chunks:
            chunk_id = compute_md5(chunk)
            embedding = get_embedding(chunk, embedding_model)
            point = PointStruct(id=chunk_id, vector=embedding, payload={"content": chunk})
            points.append(point)

        # Upsert points in batches
        for i in range(0, len(points), BATCH_SIZE):
            batch = points[i:i + BATCH_SIZE]
            client.upsert(collection_name=collection_name, points=batch, wait=True)  # Ensure upsert completes
            logging.info(f"Upserted batch {i // BATCH_SIZE + 1} of {len(points) // BATCH_SIZE + 1} to Qdrant.")

        logging.info(f"PDF processing and upsert completed for: {file_path}")

    except Exception as e:
        logging.error(f"Error processing and upserting PDF: {e}")
        raise

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok"}

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    """Upload a PDF file, process it, and store it in Qdrant."""
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        collection_name = os.path.splitext(file.filename)[0]
        settings = MODEL_CONFIG.get("settings")
        if not settings:
            raise HTTPException(status_code=500, detail="Settings not configured.")

        qdrant_cloud_url = settings.get("qdrant_cloud_url")
        qdrant_api_key = settings.get("qdrant_api_key")
        embedding_model = settings.get("embedding_model")

        if not all([qdrant_cloud_url, qdrant_api_key, embedding_model]):
            raise HTTPException(status_code=500, detail="Missing Qdrant or embedding settings.")

        # Use BackgroundTasks to avoid blocking the response
        background_tasks.add_task(process_and_upsert_pdf, file_path, collection_name, qdrant_cloud_url, qdrant_api_key, embedding_model)

        return JSONResponse(content={"message": "File uploaded. PDF processing started in the background."})

    except Exception as e:
        logging.error(f"Error during file upload and processing setup: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query")
async def query_qdrant(query_request: QueryRequest):
    """Query Qdrant database and get an answer using LLM."""
    try:
        query = query_request.query
        collection_name = query_request.collection_name

        settings = MODEL_CONFIG.get("settings")
        if not settings:
            raise HTTPException(status_code=500, detail="Settings not configured.")

        qdrant_cloud_url = settings.get("qdrant_cloud_url")
        qdrant_api_key = settings.get("qdrant_api_key")
        embedding_model = settings.get("embedding_model")
        groq_api_key = settings.get("groq_api_key")

        if not all([qdrant_cloud_url, qdrant_api_key, embedding_model, groq_api_key]):
            raise HTTPException(status_code=500, detail="Missing Qdrant, embedding, or Groq settings.")

        client = initialize_qdrant_client(qdrant_cloud_url, qdrant_api_key)

        # Generate embedding for the query
        query_embedding = get_embedding(query, embedding_model)

        # Search Qdrant
        search_result = client.search(
            collection_name=collection_name,
            query_vector=query_embedding,
            limit=5  # Adjust the limit as needed
        )

        # Extract context from search results
        context = "\n".join([hit.payload["content"] for hit in search_result])

        # Initialize Groq LLM
        llm = ChatGroq(temperature=0.0, groq_api_key=groq_api_key)

        # Create prompt
        prompt = f"You are a helpful AI assistant. Use the following context to answer the question. \nContext: {context}\nQuestion: {query}"

        # Get answer from LLM
        answer = llm.invoke(prompt).content

        return JSONResponse(content={"answer": answer})

    except Exception as e:
        logging.error(f"Error during query and LLM inference: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/set-settings")
async def set_settings(settings_data: SettingsData):
    """Set Qdrant and embedding settings."""
    try:
        settings = settings_data.dict()
        MODEL_CONFIG["settings"] = settings
        return {"message": "Settings saved successfully."}
    except Exception as e:
        logging.error(f"Error saving settings: {e}")
        raise HTTPException(status_code=500, detail=str(e))
