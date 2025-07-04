# Placeholder content for strategy_agent.py
from langchain.llms import Ollama

def generate_strategy(insight_dict):
    llm = Ollama(model="mistral")
    prompt = f"Based on these insights: {insight_dict}, suggest 3 improvements to reduce negative sentiment."
    return llm(prompt)
