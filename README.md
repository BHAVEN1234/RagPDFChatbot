# AI PDF Chatbot: Interact with Your Documents Using AI

## [Overview](pplx://action/followup)

This project creates an AI-powered PDF chatbot that allows users to upload PDF documents and ask questions about their content in natural language. The system features a FastAPI backend for PDF processing, embedding generation, and querying a Qdrant vector database. The Streamlit frontend offers an intuitive interface with a sleek dark theme. The chat functionality utilizes Groq's LLMs for fast and efficient responses. **You have the power to select your preferred LLM!**

**[Watch the Demo](pplx://action/followup):**  [AI PDF Chatbot Demo](https://drive.google.com/file/d/14h4WgRom1I24yrrQ7XVxeRVAJByDl4VY/view?usp=drive_link)

## [Table of Contents](pplx://action/followup)

-   [Features](#features)
-   [Technologies Used](#technologies-used)
-   [System Architecture](#system-architecture)
-   [Prerequisites](#prerequisites)
-   [Setup Instructions](#setup-instructions)
    -   [Backend Setup](#backend-setup)
    -   [Frontend Setup](#frontend-setup)
-   [Configuration](#configuration)
    -   [API Keys and Cloud URL](#api-keys-and-cloud-url)
        -   [Obtaining a Groq API Key](#obtaining-a-groq-api-key)
        -   [Obtaining a Qdrant API Key and Cloud URL](#obtaining-a-qdrant-api-key-and-cloud-url)
    - [Selecting your own LLM](#selecting-your-own-llm)
-   [Usage](#usage)
    -   [Initial Setup (Important!)](#initial-setup-important)
    -   [Uploading PDFs](#uploading-pdfs)
    -   [Asking Questions](#asking-questions)
    -   [Settings](#settings)
-   [Project Structure](#project-structure)
-   [Code Explanation](#code-explanation)
    -   [Backend (FastAPI)](#backend-fastapi)
    -   [Frontend (Streamlit)](#frontend-streamlit)
-   [Deployment](#deployment)
-   [Contributing](#contributing)
-   [License](#license)

## [Features](pplx://action/followup)

-   **[PDF Document Processing](pplx://action/followup)**: Extracts text from PDFs efficiently.
-   **[Natural Language Interaction](pplx://action/followup)**: Ask questions in natural language about your PDFs.
-   **[Powered by AI](pplx://action/followup)**: Uses Groq's LLMs for accurate and speedy answers.
-   **[Vector Database](pplx://action/followup)**: Stores PDF embeddings in a Qdrant vector database for quick retrieval.
-   **[User-Friendly Interface](pplx://action/followup)**: Streamlit frontend with a dark theme for enhanced usability.
-   **[LLM Selection](pplx://action/followup)**: **Choose your preferred LLM** from a list of powerful models.
-   **[Customizable Settings](pplx://action/followup)**: Configure LLM, embedding model, and database parameters.

## [Technologies Used](pplx://action/followup)

-   **[Backend](pplx://action/followup)**:
    -   FastAPI
    -   Uvicorn
    -   Qdrant Client
    -   Sentence Transformers
    -   PyPDF2
    -   NLTK
    -   Langchain-Groq
-   **[Frontend](pplx://action/followup)**:
    -   Streamlit
    -   Streamlit Option Menu
    -   Requests
-   **[Vector Database](pplx://action/followup)**:
    -   Qdrant
-   **[LLMs](pplx://action/followup)**:
    -   Groq
    -   **[Available LLMs](pplx://action/followup):** `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, `deepseek-r1-distill-qwen-32b`, `mixtral-8x7b-32768`, `gemma2-9b-it`

## [System Architecture](pplx://action/followup)

1.  **[User Interface (Streamlit)](pplx://action/followup)**: Provides an interface for users to upload PDFs, ask questions, and view responses.
2.  **[API Layer (FastAPI)](pplx://action/followup)**:
    -   Handles PDF uploads and queries from the frontend.
    -   Extracts text from PDFs using PyPDF2.
    -   Generates embeddings using Sentence Transformers.
    -   Stores embeddings in Qdrant.
    -   Queries Qdrant to find relevant context.
    -   Uses a LLM to generate answers.
3.  **[Vector Database (Qdrant)](pplx://action/followup)**: Stores and indexes PDF embeddings for efficient similarity search.
4.  **[LLMs (Groq)](pplx://action/followup)**: Generates conversational responses based on the context retrieved from the vector database.

## [Prerequisites](pplx://action/followup)

Before you begin, make sure you have the following:

-   **[Python 3.9+](pplx://action/followup)**
-   **[Pip](pplx://action/followup)** (Python package installer)
-   **[Qdrant Cloud Account](pplx://action/followup)**
-   **[Groq API Key](pplx://action/followup)**

## [Setup Instructions](pplx://action/followup)

### [Backend Setup](pplx://action/followup)

1.  **[Clone the Repository](pplx://action/followup)**

    ```
    git clone <repository_url>
    cd <backend_directory>
    ```

2.  **[Create and Activate a Virtual Environment](pplx://action/followup)**

    ```
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **[Install Dependencies](pplx://action/followup)**

    ```
    pip install -r requirements.txt
    ```

4.  **[The backend does not require environment variables. Configuration is handled through the Streamlit frontend.](pplx://action/followup)**

5.  **[Run the Backend](pplx://action/followup)**

    ```
    uvicorn main:app --reload
    ```

    The backend will start at `http://127.0.0.1:8001`.

### [Frontend Setup](pplx://action/followup)

1.  **[Navigate to the Frontend Directory](pplx://action/followup)**

    ```
    cd <frontend_directory>
    ```

2.  **[Create and Activate a Virtual Environment](pplx://action/followup)**

    ```
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **[Install Dependencies](pplx://action/followup)**

    ```
    pip install -r requirements.txt
    ```

4.  **[Run the Frontend](pplx://action/followup)**

    ```
    streamlit run app.py
    ```

    The frontend will open in your web browser.

## [Configuration](pplx://action/followup)

### [API Keys and Cloud URL](pplx://action/followup)

-   **[Important](pplx://action/followup)**: Before using the application, you'll need to set up your API keys and Cloud URL within the Streamlit app's "Settings" page. Follow the instructions below.

#### [Obtaining a Groq API Key](pplx://action/followup)

1.  Go to the [GroqCloud website](https://console.groq.com/).
2.  Sign up for an account or log in if you already have one.
3.  Navigate to the API Keys section in your dashboard.
4.  Create a new API key.
5.  Copy the API key and save it. You'll need to paste this into the Settings page of the application.

#### [Obtaining a Qdrant API Key and Cloud URL](pplx://action/followup)

1.  Go to the [Qdrant Cloud website](https://cloud.qdrant.io/).
2.  Sign up for an account or log in.
3.  Create a new cluster.
4.  Once the cluster is created, go to the API Keys section.
5.  Create a new API key.
6.  Copy the API key.
7.  Find the Cloud URL for your cluster (it will be displayed in the cluster details).

### [Selecting your own LLM](pplx://action/followup)
1. The user can select LLM as per the need
2. The available llm are : llama-3.3-70b-versatile, llama-3.1-8b-instant, deepseek-r1-distill-qwen-32b, mixtral-8x7b-32768, gemma2-9b-it

## [Usage](pplx://action/followup)

### [Initial Setup (Important!)](pplx://action/followup)

1.  **[Navigate to the "Settings" page](pplx://action/followup)** in the sidebar. This is crucial for the application to function correctly.
2.  **[Configure LLM Settings](pplx://action/followup)**:
    -   Enter your Groq API Key.
    -   **[Select your preferred LLM](pplx://action/followup)** from the available options. You can choose the model that best suits your needs.
3.  **[Configure Database Settings](pplx://action/followup)**:
    -   Enter your Qdrant Cloud URL.
    -   Enter your Qdrant API Key.
    -   Select your desired Embedding Model.
4.  **[Save Settings](pplx://action/followup)**: Click the "Save Settings" button to store your configuration.

### [Uploading PDFs](pplx://action/followup)

1.  Go to the "Chat" page.
2.  Click on "Choose a PDF" and select a PDF file from your computer.
3.  The file will be uploaded to the backend.

### [Asking Questions](pplx://action/followup)

1.  After uploading a PDF, type your question in the "Ask a Question" input box.
2.  Click the "Get Answer" button.
3.  The AI will process your question and display the answer in the chat window.

### [Settings](pplx://action/followup)

1.  Navigate to the "Settings" page in the sidebar.
2.  Configure the following:
    -   **[LLM Settings](pplx://action/followup)**:
        -   Groq API Key: Enter your Groq API key.
        -   Select LLM: **Choose your preferred LLM** from the dropdown menu.  Available options include: `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, `deepseek-r1-distill-qwen-32b`, `mixtral-8x7b-32768`, `gemma2-9b-it`.
    -   **[Database Settings](pplx://action/followup)**:
        -   Qdrant Cloud URL: Enter the URL of your Qdrant Cloud instance.
        -   Qdrant API Key: Enter your Qdrant API key.
        -   Embedding Model: Select the desired embedding model from the dropdown menu.
3.  Click the "Save Settings" button to save your configuration.

## [Project Structure](pplx://action/followup)
