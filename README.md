# ⚖️ LegalMind — RAG-Based Legal Document Q&A System

> An AI-powered Legal Document Assistant built using Retrieval-Augmented Generation (RAG), FAISS Vector Search, LangChain, Streamlit, and Google Gemini.

---

# 🚀 Live Demo

🔗 Add your deployed Streamlit URL here after deployment:

```txt
https://your-app-name.streamlit.app
```

---

# 📌 Project Overview

LegalMind is a Generative AI application that allows users to upload legal PDF documents and interact with them using natural language queries.

The system uses a Retrieval-Augmented Generation (RAG) pipeline to:

* Extract text from uploaded legal PDFs
* Split documents into semantic chunks
* Generate vector embeddings
* Store embeddings using FAISS vector database
* Retrieve contextually relevant chunks
* Generate AI-powered legal answers using Google Gemini

The goal of this project is to reduce hallucination and improve answer reliability by grounding responses in retrieved document context.

---

# ✨ Features

## 📄 Legal PDF Upload

Upload one or multiple legal documents.

## 🔍 Semantic Search

Uses vector similarity search to retrieve relevant clauses and sections.

## 🤖 AI-Powered Question Answering

Ask legal questions in natural language.

## 🧠 RAG Pipeline

Combines retrieval + LLM generation for accurate contextual answers.

## 📑 Document Summarization

Generate concise summaries of uploaded legal documents.

## 📌 Key Clause Extraction

Extract important legal clauses automatically.

## ⚠️ Legal Risk Analysis

Identify potential legal risks and obligations.

## 🎨 Interactive Streamlit UI

Clean and responsive user interface.

---

# 🏗️ System Architecture

```txt
                ┌──────────────────────┐
                │   Upload Legal PDF   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   PDF Text Extraction │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │   Text Chunking       │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Embedding Generation  │
                │ Sentence Transformers │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │  FAISS Vector Store   │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Semantic Retrieval    │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ Google Gemini LLM     │
                └──────────┬───────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │ AI Generated Response │
                └──────────────────────┘
```

---

# 🛠️ Tech Stack

| Category               | Technology            |
| ---------------------- | --------------------- |
| Frontend               | Streamlit             |
| Backend                | Python                |
| RAG Framework          | LangChain             |
| Vector Database        | FAISS                 |
| Embeddings             | Sentence Transformers |
| LLM                    | Google Gemini API     |
| PDF Parsing            | PyPDF / PyPDFLoader   |
| Environment Management | Python venv           |

---

# 📂 Project Structure

```txt
LegalMind/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── data/
│   └── uploaded_pdfs/
│
├── vectorstore/
│
└── src/
    ├── pdf_loader.py
    ├── text_splitter.py
    ├── vector_store.py
    └── qa_chain.py
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/LegalMind.git
cd LegalMind
```

---

## 2️⃣ Create Virtual Environment

```bash
py -3.11 -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key
```

---

## 5️⃣ Run Application

```bash
python -m streamlit run app.py
```

---

# 💡 Example Queries

```txt
Summarize this document.

What are the key clauses in this agreement?

What legal risks are mentioned?

What is the termination policy?

What obligations does the first party have?
```

---

# 📸 Screenshots

## 🖥️ Home Page

Add screenshot here.

## 📄 PDF Upload

Add screenshot here.

## 🤖 AI Generated Answer

Add screenshot here.

## 📌 Key Clause Extraction

Add screenshot here.

---

# 🎯 Challenges Solved

* Dependency conflicts in LangChain ecosystem
* Python environment management
* FAISS compatibility setup
* Gemini API integration
* Retrieval-Augmented Generation pipeline implementation
* Semantic document search
* Hallucination reduction using grounded context

---

# 🔮 Future Improvements

* Multi-document comparison
* Chat history
* Authentication system
* Citation highlighting
* ChromaDB/PostgreSQL integration
* Cloud deployment
* Docker containerization
* AWS/GCP deployment
* OCR support for scanned PDFs

---

# 📈 Resume Highlights

```txt
• Built a RAG-powered Legal Document Q&A system using Streamlit, LangChain, FAISS, and Gemini API to enable semantic search and AI-driven querying over legal PDFs.

• Implemented document ingestion, text chunking, embedding generation, vector similarity retrieval, and LLM-based answer generation.

• Added legal document summarization, key clause extraction, and legal risk analysis features using Retrieval-Augmented Generation (RAG).
```

---

# 🧑💻 Author

## Auditee Chowdhury

AI/ML | Generative AI | Data Science | Full Stack Development

LinkedIn: Add your LinkedIn link
GitHub: Add your GitHub link

---

# ⭐ If you like this project

Give this repository a star ⭐ and share your feedback.
