# /llm/prompt_templates.py
## Langchain
from langchain.prompts import load_prompt
## Utilities
from utils.constants import PROMPT_YAML_DIR
## Python Core
import os

# Define here your prompt templates load_prompt(os.path.join(PROMPT_YAML_DIR, "yourprompt.yaml"))

rag_prompt_custom = load_prompt(os.path.join(PROMPT_YAML_DIR, "rag_custom_prompt.yaml"))
  
hyde_custom_prompt = load_prompt(os.path.join(PROMPT_YAML_DIR, "hyde_custom_prompt.yaml"))