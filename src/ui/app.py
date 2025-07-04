# Placeholder content for app.py
import streamlit as st
from src.agents.data_agent import run_data_agent

st.title("🧠 Cognify AI OS")
file = st.file_uploader("Upload CSV", type="csv")

if file:
    insights = run_data_agent(file)
    st.json(insights)
    st.image("outputs/plots/sentiment_distribution.png")
