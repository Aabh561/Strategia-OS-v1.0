# Placeholder content for rag_pipeline.py
from langchain.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

def build_vectorstore(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    chunks = CharacterTextSplitter(chunk_size=500, chunk_overlap=100).split_documents(documents)
    embeddings = OllamaEmbeddings()
    return FAISS.from_documents(chunks, embeddings)
