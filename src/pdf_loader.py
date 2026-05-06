import os
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

def save_uploaded_files(uploaded_files) -> List[str]:
    """
    Saves Streamlit UploadedFile objects to temporary files so PyPDFLoader can read them.
    Returns a list of file paths.
    """
    file_paths = []
    # Create the data directory if it doesn't exist
    os.makedirs("data/uploaded_pdfs", exist_ok=True)
    
    for uploaded_file in uploaded_files:
        # Save to a temporary file, or to data/uploaded_pdfs
        file_path = os.path.join("data/uploaded_pdfs", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        file_paths.append(file_path)
    return file_paths

def load_pdf_documents(file_paths: List[str]) -> List[Document]:
    """
    Loads text from PDF files using LangChain's PyPDFLoader.
    """
    documents = []
    for path in file_paths:
        try:
            loader = PyPDFLoader(path)
            docs = loader.load()
            documents.extend(docs)
        except Exception as e:
            print(f"Error loading {path}: {e}")
    return documents
