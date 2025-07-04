# Placeholder content for test_agents.py
from src.agents.data_agent import run_data_agent

def test_data_agent_output():
    result = run_data_agent("data/raw/sample_support_chats.csv")
    assert "total_tickets" in result
    assert result["total_tickets"] > 0
