from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import HuggingFaceHub
from .embeddings import get_embeddings

def build_vectorstore(text: str):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)
    embeddings = get_embeddings()
    vectorstore = FAISS.from_texts(chunks, embeddings)
    return vectorstore

def get_llm():
    return HuggingFaceHub(
        repo_id="google/flan-t5-base",  # lightweight free model
        model_kwargs={"temperature": 0.3, "max_length": 512}
    )

def ask_question(vectorstore, query: str):
    retriever = vectorstore.as_retriever()
    docs = retriever.get_relevant_documents(query)
    context = " ".join([doc.page_content for doc in docs])
    llm = get_llm()
    prompt = f"Answer based on context:\n\n{context}\n\nQuestion: {query}\nAnswer:"
    return llm(prompt)
