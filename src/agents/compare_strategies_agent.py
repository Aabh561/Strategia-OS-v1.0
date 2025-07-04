from langchain_community.llms import Ollama


def compare_strategies(insight_dict):
    llm = Ollama(model="mistral")
    
    conservative = llm(f"As a cautious consultant, suggest strategies based on: {insight_dict}")
    aggressive = llm(f"As a bold growth hacker, suggest win-back strategies based on: {insight_dict}")
    
    return {
        "conservative_strategy": conservative,
        "aggressive_strategy": aggressive
    }
