# rag_demo\orchestration.py

from utils.classes import Orchestrator
from .load_pdf import load_pdfloader
from .load_vectorstore import load_vectorstore_chromadb

def load_chromadb(document_name: str, collection_name: str):

    orchestrator = Orchestrator()
    orchestrator.load_function(load_pdfloader, document_name)
    orchestrator.load_function(lambda result: load_vectorstore_chromadb(documents=result, collection_name=collection_name))
    # Execute the loaded functions sequentially and return the results
    results = orchestrator.run()
    return [output for output in results] if results else False