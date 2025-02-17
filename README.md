# 🤖✨ AI PDF Chatbot: Unlock the Power of Your Documents with AI! 🚀📚

## 🎉 Overview

Tired of manually searching through lengthy PDFs? This project revolutionizes how you interact with your documents! Imagine effortlessly asking questions in natural language and receiving instant, insightful answers powered by AI. This AI PDF Chatbot leverages a robust FastAPI backend for lightning-fast processing and a sleek Streamlit frontend for a delightful user experience. 
**Unleash the power of your PDFs!** ✨

**Demo in Action:**  [AI PDF Chatbot Demo](https://drive.google.com/file/d/14h4WgRom1I24yrrQ7XVxeRVAJByDl4VY/view?usp=drive_link) 
*Note: Embedding is not supported; the link will take you to the demo video.*

## 🌟 Key Features

-   📄 **Effortless PDF Processing**: Extracts text from your PDFs with speed and precision.
-   🗣️ **Natural Language Interaction**: Engage in conversations with your documents using everyday language.
-   🧠 **Intelligent AI**: Powered by Groq's cutting-edge LLMs for accurate and relevant answers.
-   ⚡️ **Blazing Fast**: Utilizes a Qdrant vector database for near-instant retrieval of information.
-   🎨 **Beautiful Interface**: A user-friendly Streamlit frontend with a stylish dark theme.
-   🎛️ **LLM Selection**: **Pick your perfect LLM** from a curated list of high-performing models.
-   🛠️ **Customizable Settings**: Fine-tune LLM, embedding model, and database parameters to your liking.

## ⚙️ Technologies Used

-   **Backend**:
    -   FastAPI: The modern, high-performance web framework.
    -   Uvicorn: An ASGI server for running the FastAPI application.
    -   Qdrant Client: The official client for interacting with the Qdrant vector database.
    -   Sentence Transformers: Library for generating meaningful sentence embeddings.
    -   PyPDF2: A powerful PDF manipulation library.
    -   NLTK: Natural Language Toolkit for text processing.
    -   Langchain-Groq: Integration for using Groq's LLMs.
-   **Frontend**:
    -   Streamlit: The fastest way to build and share data apps.
    -   Streamlit Option Menu: Elegant sidebar navigation.
    -   Requests: Simple HTTP requests for seamless communication with the backend.
-   **Vector Database**:
    -   Qdrant: The vector database that powers similarity search.
-   **LLMs**:
    -   Groq: Provides the Large Language Models for generating conversational responses.
    -   **Available LLMs:** `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, `deepseek-r1-distill-qwen-32b`, `mixtral-8x7b-32768`, `gemma2-9b-it`

## 🏗️ System Architecture

1.  **User Interface (Streamlit)**: Provides an intuitive interface for uploading PDFs, asking questions, and viewing responses.
2.  **API Layer (FastAPI)**:
    -   Handles PDF uploads and queries from the frontend.
    -   Extracts text from PDFs using PyPDF2.
    -   Generates embeddings using Sentence Transformers.
    -   Stores embeddings in Qdrant.
    -   Queries Qdrant to find relevant context.
    -   Uses a LLM to generate answers.
3.  **Vector Database (Qdrant)**: Stores and indexes PDF embeddings for efficient similarity search.
4.  **LLMs (Groq)**: Generates conversational responses based on the context retrieved from the vector database.

## 🚀 Prerequisites

Before you get started, ensure you have:

-   Python 3.9+
-   Pip (Python package installer)
-   Qdrant Cloud Account
-   Groq API Key

## 🛠️ Setup Instructions

### Backend Setup

1.  **Clone the Repository**

    ```
    git clone <repository_url>
    cd <backend_directory>
    ```

2.  **Create and Activate a Virtual Environment**

    ```
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies**

    ```
    pip install -r requirements.txt
    ```

4.  **The backend does not require environment variables. Configuration is handled through the Streamlit frontend.**

5.  **Run the Backend**

    ```
    uvicorn main:app --reload
    ```

    The backend will start at `http://127.0.0.1:8001`.

### Frontend Setup

1.  **Navigate to the Frontend Directory**

    ```
    cd <frontend_directory>
    ```

2.  **Create and Activate a Virtual Environment**

    ```
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install Dependencies**

    ```
    pip install -r requirements.txt
    ```

4.  **Run the Frontend**

    ```
    streamlit run app.py
    ```

    The frontend will open in your web browser.

## ⚙️ Configuration

### 🔑 API Keys and Cloud URL

-   **Critical**: Set up your API keys and Cloud URL in the Streamlit app's "Settings" page.

#### 🔑 Obtaining a Groq API Key

1.  Go to the [GroqCloud website](https://console.groq.com/).
2.  Sign up for an account or log in.
3.  Navigate to the API Keys section in your dashboard.
4.  Create a new API key.
5.  Copy the API key and save it. You'll need to paste this into the Settings page.

#### ☁️ Obtaining a Qdrant API Key and Cloud URL

1.  Go to the [Qdrant Cloud website](https://cloud.qdrant.io/).
2.  Sign up for an account or log in.
3.  Create a new cluster.
4.  Once the cluster is created, go to the API Keys section.
5.  Create a new API key.
6.  Copy the API key.
7.  Find the Cloud URL for your cluster (it will be displayed in the cluster details).

### 🧠 Selecting Your LLM

1.  The user can select LLM as per the need
2.  The available llm are : llama-3.3-70b-versatile, llama-3.1-8b-instant, deepseek-r1-distill-qwen-32b, mixtral-8x7b-32768, gemma2-9b-it

## ⚡ Usage

### 🚀 Initial Setup (Important!)

1.  **Navigate to the "Settings" page** in the sidebar. This is a must for the application to run correctly.
2.  **Configure LLM Settings**:
    -   Enter your Groq API Key.
    -   **Select your preferred LLM** from the available options.
3.  **Configure Database Settings**:
    -   Enter your Qdrant Cloud URL.
    -   Enter your Qdrant API Key.
    -   Select your desired Embedding Model.
4.  **Save Settings**: Click the "Save Settings" button.

### 📤 Uploading PDFs

1.  Go to the "Chat" page.
2.  Click "Choose a PDF" and select a PDF file.
3.  The file will be uploaded to the backend.

### 💬 Asking Questions

1.  After uploading a PDF, type your question in the "Ask a Question" input box.
2.  Click the "Get Answer" button.
3.  The AI will process your question and show the answer.

### ⚙️ Settings

1.  Navigate to the "Settings" page in the sidebar.
2.  Configure the following:
    -   **LLM Settings**:
        -   Groq API Key: Enter your Groq API key.
        -   Select LLM: **Choose your preferred LLM** from the dropdown menu.  Available options include: `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, `deepseek-r1-distill-qwen-32b`, `mixtral-8x7b-32768`, `gemma2-9b-it`.
    -   **Database Settings**:
        -   Qdrant Cloud URL: Enter the URL of your Qdrant Cloud instance.
        -   Qdrant API Key: Enter your Qdrant API key.
        -   Embedding Model: Select the desired embedding model from the dropdown menu.
3.  Click the "Save Settings" button.
