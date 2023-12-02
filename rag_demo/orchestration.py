# rag_demo\orchestration.py
"""
rag_demo.orchestration
~~~~~~~~~~~~~~~~~~~~~~

This module provides orchestration for loading documents into a ChromaDB vector store.
"""

from utils.classes import Orchestrator
from .load_pdf import load_pdfloader
from .load_vectorstore import load_vectorstore_chromadb

def load_chromadb(document_name: str, collection_name: str):
    """
    Orchestrates the loading of a document into a ChromaDB vector store.

    Args:
        document_name (str): The name of the document to be loaded.
        collection_name (str): The name of the collection where the document will be stored.

    Returns:
        list: A list of outputs from the loaded functions or False if no results.
    """
    # Initialize the orchestrator
    orchestrator = Orchestrator()
    # Load the PDF loader function with the document name
    orchestrator.load_function(load_pdfloader, document_name)
    # Load the vector store function with the result of the PDF loader and collection name
    orchestrator.load_function(lambda result: load_vectorstore_chromadb(documents=result, collection_name=collection_name))
    # Execute the loaded functions sequentially and return the results
    results = orchestrator.run()
    # Return the results as a list if there are any, otherwise return False
    return [output for output in results] if results else False
