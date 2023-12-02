# /llm/retrievals.py
from .prompt_templates import rag_prompt_custom
from .retrieval_from_chromadb import run_qa_chromadb

def query_LG_DRYER_DEMO(prompt: str):
    '''Returns a context from a question regarding the LG_DRYER_DEMO collection from the vectorstore'''
    return run_qa_chromadb(question=prompt, collection_name="LG_DRYER_DEMO", template=rag_prompt_custom)