import os
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from src.pdf_loader import save_uploaded_files, load_pdf_documents
from src.text_splitter import split_documents
from src.vector_store import create_and_save_vector_store, load_vector_store
from src.qa_chain import generate_answer, summarize_document, extract_key_clauses, analyze_legal_risks

# Page configuration
st.set_page_config(
    page_title="LegalMind - RAG Legal Q&A",
    page_icon="⚖️",
    layout="wide"
)

# Sidebar for configuration and uploads
with st.sidebar:
    st.title("⚖️ LegalMind")
    st.markdown("Upload legal documents and ask questions based on their content.")
    
    # API Key handling
    api_key = st.text_input("Google Gemini API Key", type="password", value=os.environ.get("GOOGLE_API_KEY", ""))
    if api_key:
        os.environ["GOOGLE_API_KEY"] = api_key
    
    st.divider()
    st.subheader("1. Upload Documents")
    uploaded_files = st.file_uploader(
        "Upload Legal PDFs", 
        type="pdf", 
        accept_multiple_files=True,
        help="Select one or more PDF files to analyze."
    )
    
    process_button = st.button("Process Documents", use_container_width=True)

# Main Application logic
st.title("RAG-Based Legal Document Q&A System")
st.markdown("Ask questions about your uploaded legal documents. The system uses AI to find relevant context and formulate accurate answers without hallucinating.")

# State initialization
if "vector_store" not in st.session_state:
    st.session_state.vector_store = load_vector_store()
    
# Processing Documents
if process_button:
    if not api_key:
        st.error("Please enter your Google Gemini API Key in the sidebar.")
    elif not uploaded_files:
        st.warning("Please upload at least one PDF document.")
    else:
        with st.spinner("Processing documents... This might take a few moments."):
            try:
                # 1. Save uploaded files
                file_paths = save_uploaded_files(uploaded_files)
                
                # 2. Load PDF documents
                documents = load_pdf_documents(file_paths)
                
                # 3. Split documents into chunks
                chunks = split_documents(documents)
                st.info(f"Created {len(chunks)} chunks from {len(uploaded_files)} document(s).")
                
                # 4 & 5. Generate embeddings and create vector store
                vector_store = create_and_save_vector_store(chunks)
                st.session_state.vector_store = vector_store
                
                st.success("Documents processed and indexed successfully! You can now ask questions.")
            except Exception as e:
                st.error(f"An error occurred while processing the documents: {e}")

# Q&A Section
st.divider()

if st.session_state.vector_store is not None:
    st.subheader("2. Ask a Question")
    query = st.text_input("Enter your legal query here:")
    
    col1, col2 = st.columns([4, 1])
    with col1:
        ask_button = st.button("Ask", type="primary")
    
    st.subheader("Quick Actions (Bonus Features)")
    bcol1, bcol2, bcol3 = st.columns(3)
    with bcol1:
        summarize_btn = st.button("Summarize Document", use_container_width=True)
    with bcol2:
        clauses_btn = st.button("Key Clauses Extraction", use_container_width=True)
    with bcol3:
        risk_btn = st.button("Legal Risk Analysis", use_container_width=True)

    # Handle standard question
    if ask_button and query:
        if not api_key:
            st.error("API Key is missing. Please provide it in the sidebar.")
        else:
            with st.spinner("Searching for answers..."):
                try:
                    answer, sources = generate_answer(st.session_state.vector_store, query)
                    
                    st.markdown("### Answer")
                    st.info(answer)
                    
                    with st.expander("Show Source References"):
                        st.markdown("#### Retrieved Context Chunks")
                        for i, doc in enumerate(sources):
                            st.markdown(f"**Source {i+1}** (Page: {doc.metadata.get('page', 'Unknown')}, File: {os.path.basename(doc.metadata.get('source', 'Unknown'))})")
                            st.text(doc.page_content)
                            st.divider()
                except Exception as e:
                    st.error(f"Error during answering: {e}")

    # Handle quick actions explicitly
    vector_store = st.session_state.vector_store

    if summarize_btn:
        if not api_key:
            st.error("API Key is missing. Please provide it in the sidebar.")
        else:
            with st.spinner("Generating document summary..."):
                try:
                    answer, sources = summarize_document(vector_store)
                    st.markdown("### Document Summary")
                    st.info(answer)
                except Exception as e:
                    st.error(f"Error during document summary: {e}")

    if clauses_btn:
        if not api_key:
            st.error("API Key is missing. Please provide it in the sidebar.")
        else:
            with st.spinner("Generating key clauses..."):
                try:
                    answer, sources = extract_key_clauses(vector_store)
                    st.markdown("### Key Clauses")
                    st.info(answer)
                except Exception as e:
                    st.error(f"Error during key clauses: {e}")

    if risk_btn:
        if not api_key:
            st.error("API Key is missing. Please provide it in the sidebar.")
        else:
            with st.spinner("Generating legal risk analysis..."):
                try:
                    answer, sources = analyze_legal_risks(vector_store)
                    st.markdown("### Legal Risk Analysis")
                    st.info(answer)
                except Exception as e:
                    st.error(f"Error during legal risk analysis: {e}")

else:
    st.info("Please upload and process documents before asking questions.")
