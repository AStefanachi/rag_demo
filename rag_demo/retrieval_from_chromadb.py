# /rag_demo/retrieval_from_chromadb.py
"""
retrieval_from_chromadb.py

This module provides functionality to retrieve context from a ChromaDB vector store
based on a given question and collection name, and then generate an answer using a
language model.
"""

# Langchain imports
from langchain.chat_models import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.chains import LLMChain, HypotheticalDocumentEmbedder
from langchain.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

# Local imports
from .prompt_templates import hyde_custom_prompt

# Core Python and third-party imports
import chromadb
from dotenv import load_dotenv
import os

# Utility imports
from utils.constants import CHROMA_PERSISTANT_DIR


def run_qa_chromadb(question: str, collection_name: str, template: object) -> str:
    """
    Retrieves context from a ChromaDB vector store and generates an answer to a question.

    Args:
        question (str): The question to be answered.
        collection_name (str): The name of the collection in the vector store to query.
        template (object): The template object to format the question for the language model.

    Returns:
        str: The generated answer to the question.
    """

    # Load environment settings
    load_dotenv("settings.env")

    # Create the embedding function using a pre-trained model
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # Initialize the language model with a custom prompt
    llm_hyde = ChatOpenAI(model_name=os.environ.get('LLM_MODEL'), temperature=0)
    llm_chain = LLMChain(llm=llm_hyde, prompt=hyde_custom_prompt)

    # Embed the hypothetical answer
    embeddings = HypotheticalDocumentEmbedder(llm_chain=llm_chain, base_embeddings=embedding_function)

    # Instantiate the vector store client
    client = chromadb.PersistentClient(path=CHROMA_PERSISTANT_DIR)

    # Create the Chroma vector store with the hypothetical embeddings
    db = Chroma(client=client, collection_name=collection_name, embedding_function=embeddings)

    # Configure the retriever for Max Marginal Relevance Search with diversity
    retriever = db.as_retriever(search_type="mmr", search_kwargs={'k': 5, 'lambda_mult': 0.5})

    # Retrieve the most relevant documents based on the question
    context = retriever.get_relevant_documents(question)

    # Initialize the language model for generating the answer
    llm = ChatOpenAI(model_name=os.environ.get('LLM_MODEL'), temperature=0)

    # Create the chain with the context, question, template, and language model
    rag_chain = ({"context": retriever, "question": RunnablePassthrough()} | template | llm)

    # Generate and return the answer
    return rag_chain.invoke(question).content
    
