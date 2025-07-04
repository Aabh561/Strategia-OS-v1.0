# Placeholder content for data_agent.py
from src.utils.data_loader import load_support_data
from src.utils.visualizer import generate_sentiment_plot

def run_data_agent(path):
    df = load_support_data(path)
    generate_sentiment_plot(df)
    return {
        "total_tickets": len(df),
        "avg_response_time": df["response_time"].mean(),
        "top_issues": df["issue"].value_counts().head(3).to_dict()
    }
