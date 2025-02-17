
## Code Explanation

### Backend (FastAPI)

-   **`main.py`**: Contains the FastAPI application logic.
    -   `/upload-pdf`: Endpoint for uploading and processing PDF files.
    -   `/query`: Endpoint for receiving questions and returning answers.
    -   `/set-settings`: Endpoint for updating API keys and model configurations.
    -   Uses `PyPDF2` to extract text from PDFs.
    -   Uses `SentenceTransformer` to generate embeddings.
    -   Uses `QdrantClient` to interact with the Qdrant vector database.
    -   Uses `ChatGroq` to generate answers.

### Frontend (Streamlit)

-   **`app.py`**: Contains the Streamlit application logic.
    -   Provides a user interface for uploading PDFs, asking questions, and configuring settings.
    -   Uses `streamlit_option_menu` for navigation.
    -   Uses `requests` to communicate with the backend.
    -   Implements a dark theme using custom CSS.

## Deployment

The AI PDF Chatbot can be deployed on various platforms, including:

-   **Cloud Platforms**: AWS, Google Cloud, Azure.
-   **Containerization**: Docker, Kubernetes.

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch.
3.  Implement your changes.
4.  Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
