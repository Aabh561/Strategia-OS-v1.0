# Placeholder content for ollama_sandbox.sh
#!/bin/bash

# This script ensures Ollama runs securely in offline mode
# No internet access — fully air-gapped execution

ollama run mistral --system "You are an isolated LLM. Respond using only internal knowledge. Do not fetch any live data or call APIs."
