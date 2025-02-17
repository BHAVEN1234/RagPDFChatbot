# AI PDF Chatbot

## Overview

This project implements an AI-powered PDF chatbot, allowing users to upload PDF documents and ask questions about their content using natural language. The system leverages a FastAPI backend for processing PDFs, generating embeddings, and querying a vector database (Qdrant), and a Streamlit frontend for user interaction. The chat functionality is powered by Groq's LLM, offering quick inference and minimal latency.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [System Architecture](#system-architecture)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Configuration](#configuration)
  - [Environment Variables](#environment-variables)
  - [API Keys](#api-keys)
- [Usage](#usage)
  - [Uploading PDFs](#uploading-pdfs)
  - [Asking Questions](#asking-questions)
  - [Settings](#settings)
- [Project Structure](#project-structure)
- [Code Explanation](#code-explanation)
  - [Backend (FastAPI)](#backend-fastapi)
  - [Frontend (Streamlit)](#frontend-streamlit)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- **PDF Document Processing**: Extracts text from uploaded PDFs.
- **Natural Language Interaction**: Allows users to ask questions about PDF content using natural language.
- **AI-Powered**: Uses a LLM (Groq) to generate relevant answers.
- **Vector Database**: Stores PDF embeddings in a Qdrant vector database for efficient similarity search.
- **Customizable Settings**: Configurable LLM, embedding model, and database settings.
- **User-Friendly Interface**: Clean and intuitive Streamlit frontend.
- **Dark Theme**: Aesthetically pleasing dark theme for improved user experience.

## Technologies Used

- **Backend**:
    - FastAPI
    - Uvicorn
    - Qdrant Client
    - Sentence Transformers
    - PyPDF2
    - NLTK
    - Langchain-Groq
- **Frontend**:
    - Streamlit
    - Streamlit Option Menu
    - Requests
- **Vector Database**:
    - Qdrant
- **LLM**:
    - Groq

## System Architecture

1.  **User Interface (Streamlit)**: Provides an interface for users to upload PDFs, ask questions, and view responses.
2.  **API Layer (FastAPI)**:
    - Receives PDF uploads and queries from the frontend.
    - Extracts text from PDFs using PyPDF2.
    - Generates embeddings using Sentence Transformers.
    - Stores embeddings in Qdrant.
    - Queries Qdrant to find relevant context.
    - Uses a LLM to generate answers.
3.  **Vector Database (Qdrant)**: Stores and indexes PDF embeddings for efficient similarity search.
4.  **LLM (Groq)**: Generates conversational responses based on the context retrieved from the vector database.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9+**
- **Pip** (Python package installer)
- **Qdrant Cloud Account**
- **Groq API Key**

## Setup Instructions

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

4.  **Set Environment Variables**

    Create a `.env` file in the backend directory and add the following:

    ```
    QDRANT_API_KEY=<your_qdrant_api_key>
    QDRANT_CLOUD_URL=<your_qdrant_cloud_url>
    GROQ_API_KEY=<your_groq_api_key>
    ```

    Replace the placeholders with your actual API keys and Qdrant Cloud URL.

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

## Configuration

### Environment Variables

The following environment variables are used to configure the application:

-   `QDRANT_API_KEY`: API key for accessing the Qdrant vector database.
-   `QDRANT_CLOUD_URL`: URL of the Qdrant Cloud instance.
-   `GROQ_API_KEY`: API key for accessing the Groq LLM.

### API Keys

-   **Qdrant API Key**: Obtain this from your Qdrant Cloud account.
-   **Groq API Key**: Obtain this from your Groq account.

## Usage

### Uploading PDFs

1.  Open the Streamlit frontend in your web browser.
2.  Navigate to the "Chat" page.
3.  Click on "Choose a PDF" and select a PDF file from your local machine.
4.  The file will be uploaded to the backend for processing.

### Asking Questions

1.  After uploading a PDF, type your question in the "Ask a Question" input box.
2.  Click the "Get Answer" button.
3.  The AI will process your question and display the answer in the chat window.

### Settings

1.  Navigate to the "Settings" page in the sidebar.
2.  Configure the following:
    -   **LLM Settings**:
        -   Groq API Key: Enter your Groq API key.
        -   Select LLM: Choose the desired LLM from the dropdown menu.
    -   **Database Settings**:
        -   Qdrant Cloud URL: Enter the URL of your Qdrant Cloud instance.
        -   Qdrant API Key: Enter your Qdrant API key.
        -   Embedding Model: Select the desired embedding model from the dropdown menu.
3.  Click the "Save Settings" button to save your configuration.

## Project Structure
