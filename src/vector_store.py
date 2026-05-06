import os
from typing import List
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Specify the directory to save the FAISS index locally
VECTOR_STORE_DIR = "vectorstore/faiss_index"

def get_embeddings_model() -> HuggingFaceEmbeddings:
    """
    Initializes and returns the HuggingFace embeddings model.
    Using 'all-MiniLM-L6-v2' which is fast and effective for semantic search.
    """
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def create_and_save_vector_store(documents: List[Document]) -> FAISS:
    """
    Generates embeddings for the document chunks and stores them in a FAISS vector database.
    Saves the FAISS index locally for future reuse.
    """
    embeddings = get_embeddings_model()
    
    # Create FAISS vector store from documents
    vector_store = FAISS.from_documents(documents, embeddings)
    
    # Ensure directory exists
    os.makedirs("vectorstore", exist_ok=True)
    
    # Save the vector store locally
    vector_store.save_local(VECTOR_STORE_DIR)
    
    return vector_store

def load_vector_store() -> FAISS | None:
    """
    Loads the previously saved FAISS vector database from local storage.
    Returns None if the directory doesn't exist.
    """
    if os.path.exists(VECTOR_STORE_DIR):
        embeddings = get_embeddings_model()
        # Enable dangerous deserialization as we created this index locally
        return FAISS.load_local(VECTOR_STORE_DIR, embeddings, allow_dangerous_deserialization=True)
    return None
