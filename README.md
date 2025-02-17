
## [Code Explanation](pplx://action/followup)

### [Backend (FastAPI)](pplx://action/followup)

-   **[`main.py`](pplx://action/followup)**: Contains the FastAPI application logic.
    -   `/upload-pdf`: Endpoint for uploading and processing PDF files.
    -   `/query`: Endpoint for receiving questions and returning answers.
    -   `/set-settings`: Endpoint for updating API keys and model configurations.
    -   Uses `PyPDF2` to extract text from PDFs.
    -   Uses `SentenceTransformer` to generate embeddings.
    -   Uses `QdrantClient` to interact with the vector database.
    -   Uses `ChatGroq` to generate answers.

### [Frontend (Streamlit)](pplx://action/followup)

-   **[`app.py`](pplx://action/followup)**: Contains the Streamlit application logic.
    -   Provides a user interface for uploading PDFs, asking questions, and configuring settings.
    -   Uses `streamlit_option_menu` for navigation.
    -   Uses `requests` to communicate with the backend.
    -   Implements a dark theme using custom CSS.

## [Deployment](pplx://action/followup)

The AI PDF Chatbot can be deployed on various platforms, including:

-   **[Cloud Platforms](pplx://action/followup)**: AWS, Google Cloud, Azure.
-   **[Containerization](pplx://action/followup)**: Docker, Kubernetes.

## [Contributing](pplx://action/followup)

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch.
3.  Implement your changes.
4.  Submit a pull request.

## [License](pplx://action/followup)

This project is licensed under the [MIT License](LICENSE).
