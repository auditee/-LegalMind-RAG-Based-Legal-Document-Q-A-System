import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA

load_dotenv()


def generate_answer(vector_store, question):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.2,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )

    result = qa_chain.invoke({"query": question})

    answer = result["result"]
    sources = result["source_documents"]

    return answer, sources


def summarize_document(vector_store):
    return generate_answer(
        vector_store,
        "Summarize this legal document in simple language."
    )


def extract_key_clauses(vector_store):
    return generate_answer(
        vector_store,
        "Extract the key legal clauses from this document."
    )


def analyze_legal_risks(vector_store):
    return generate_answer(
        vector_store,
        "Analyze the possible legal risks mentioned in this document."
    )