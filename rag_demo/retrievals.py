# /llm/retrievals.py
# This module defines functions to perform retrieval operations for the RAG demo.

# Relative imports from within the rag_demo package
from .prompt_templates import rag_prompt_custom  # Custom prompt templates for RAG
from .retrieval_from_chromadb import run_qa_chromadb  # Function to run QA on ChromaDB

def query_LG_DRYER_DEMO(prompt: str, collection_name: str) -> str:
    """
    Queries the LG_DRYER_DEMO collection from the vectorstore and returns the context.

    Args:
        prompt (str): The question to query the vectorstore with.

    Returns:
        str: The retrieved context from the vectorstore.
    """
    return run_qa_chromadb(question=prompt, collection_name=collection_name, template=rag_prompt_custom)
