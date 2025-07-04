# Placeholder content for fastapi_app.py
from fastapi import FastAPI, UploadFile
from src.agents.data_agent import run_data_agent
from src.rag.rag_pipeline import build_vectorstore
from langchain.llms import Ollama
from langchain.chains import RetrievalQA

app = FastAPI()

@app.post("/analyze_csv")
async def analyze(file: UploadFile):
    with open("temp.csv", "wb") as f:
        f.write(await file.read())
    return run_data_agent("temp.csv")

@app.post("/rag_pdf")
async def rag_qa(file: UploadFile, question: str):
    with open("docs/enterprise_policy.pdf", "wb") as f:
        f.write(await file.read())

    vectordb = build_vectorstore("docs/enterprise_policy.pdf")
    llm = Ollama(model="mistral")
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())
    return {"answer": qa.run(question)}
