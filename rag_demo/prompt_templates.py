# /llm/prompt_templates.py
# This module is responsible for loading custom prompt templates for the RAG demo.

# External imports
from langchain.prompts import load_prompt  # Langchain library to load prompts
import os  # Python Core library for OS interface

# Internal imports
from utils.constants import PROMPT_YAML_DIR  # Utility constants for the project

# Load custom RAG prompt template from YAML file
rag_prompt_custom = load_prompt(os.path.join(PROMPT_YAML_DIR, "rag_custom_prompt.yaml"))

# Load custom Hyde prompt template from YAML file
hyde_custom_prompt = load_prompt(os.path.join(PROMPT_YAML_DIR, "hyde_custom_prompt.yaml"))
