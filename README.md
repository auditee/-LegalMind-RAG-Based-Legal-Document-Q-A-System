# LegalMind - RAG-Based Legal Document Q&A System

LegalMind is a RAG (Retrieval-Augmented Generation) based Q&A system designed for legal documents. It allows users to upload PDF documents, processes them using LangChain, stores embeddings in a FAISS vector database, and uses Google's Gemini LLM to answer questions specifically grounded in the uploaded documents.

## Features
- PDF Document Upload & Processing
- Semantic Search using HuggingFace embeddings (`all-MiniLM-L6-v2`)
- High-quality responses using Google Gemini API
- Local Vector Database storage using FAISS
- Extra features: Document Summarization, Key Clauses Extraction, Legal Risk Analysis
- Clean and responsive Streamlit UI

## Tech Stack
- Python 3.10+
- Streamlit
- LangChain
- FAISS
- HuggingFace Sentence Transformers
- Google Gemini API (via `langchain-google-genai`)
- PyPDF

## Setup Instructions

1. **Clone the repository** (or download the source code).
2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Environment Variables**:
   Copy `.env.example` to `.env` and add your Google Gemini API Key.
   ```bash
   cp .env.example .env
   ```
5. **Run the application**:
   ```bash
   streamlit run app.py
   ```
