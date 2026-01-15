# 🧠 Strategia OS – Local AI Operating System for Enterprises

> ⚙️ An offline-ready, modular AI system that simulates executive-level strategy, analyzes support operations, and answers complex policy questions — all using private, explainable LLM agents

---

## 🏢 Why Strategia OS?

Traditional dashboards show charts.  
**Strategia OS tells you what to do next.**

This project simulates what companies like Siemens, Google, or Microsoft might use *internally* to:

- 🔍 Diagnose customer service inefficiencies from CSVs
- 🤖 Simulate conservative vs aggressive business strategies
- 📚 Query internal policy documents locally using Retrieval-Augmented Generation (RAG)
- 🔒 All using **no APIs, no cloud — only local LLMs via Ollama**

---

## 💡 Key Capabilities

| Feature                          | What It Does |
|----------------------------------|--------------|
| 🔍 CSV Insight Agent             | Extracts total tickets, avg. response time, and top issues from support data |
| 🤖 Strategy Simulation Agent     | Compares conservative vs. aggressive AI-generated strategies based on CSV insight |
| 📚 RAG Q&A Agent (PDF)           | Answers deep questions from policy docs using LangChain + FAISS + LLaMA |
| 🔐 Fully Local + Offline         | No OpenAI/Anthropic — powered by Ollama + LangChain Community |
| 🧪 Modular & Tested              | FAANG-style codebase with test cases and clean structure |

---

## 🧠 Architecture (Multi-Agent AI OS)

```ascii
+------------------------+
|  sample_support_chats |
+------------------------+
           ↓
  [ CSV Insight Agent ]
           ↓
  [ Conservative Agent ]     [ Aggressive Agent ]
           ↓                      ↓
      Business Plan ←─────────────┘

  [ PDF Policy Doc ]
           ↓
   [ RAG + FAISS + Ollama ]
           ↓
    Answer to HR/IT/Legal Questions
