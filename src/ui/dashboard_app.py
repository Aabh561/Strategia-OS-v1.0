import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import streamlit as st
from src.agents.data_agent import run_data_agent
from src.agents.compare_strategies_agent import compare_strategies
from src.rag.rag_pipeline import build_vectorstore
from langchain.chains import RetrievalQA
from langchain.llms import Ollama

st.set_page_config(layout="wide")
st.title("Cognify AI OS – Dashboard")

tab1, tab2, tab3 = st.tabs(["CSV Insights", "Compare Strategies", "Ask a PDF"])

with tab1:
    file = st.file_uploader("Upload CSV", type="csv")
    if file:
        insights = run_data_agent(file)
        st.json(insights)

with tab2:
    if file:
        results = compare_strategies(insights)
        st.code(results["conservative_strategy"])
        st.code(results["aggressive_strategy"])

with tab3:
    pdf = st.file_uploader("Upload PDF", type="pdf")
    if pdf:
        with open("docs/enterprise_policy.pdf", "wb") as f:
            f.write(pdf.read())  # save uploaded file

        vectordb = build_vectorstore("docs/enterprise_policy.pdf")
        question = st.text_input("Ask something from the policy:")

        if question:
            llm = Ollama(model="mistral")
            qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())
            answer = qa.run(question)
            st.write("Answer:", answer)
