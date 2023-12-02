# /rag_demo/retrieval_from_chromadb.py
## Langchain
# Chat Models
from langchain.chat_models import ChatOpenAI
# Schemas
from langchain.schema.runnable import RunnablePassthrough
# Chains
from langchain.chains import LLMChain, HypotheticalDocumentEmbedder
# Prompts
from langchain.prompts import PromptTemplate
# Vector Store: Chroma
from langchain.vectorstores import Chroma
# Embeddings
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
## LLM
from .prompt_templates import hyde_custom_prompt
## Python Core
import chromadb
from dotenv import load_dotenv
import os
## Utils
from utils.constants import CHROMA_PERSISTANT_DIR


def run_qa_chromadb(question: str, collection_name:str, template: object):
    '''Returns a context, from querying the vector store, according to question and collection_name'''

    # Loading environment settings
    load_dotenv("settings.env")

    # create the open-source embedding function
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # Perform Hypotetical Document Embedding   
    # Pre-generate an answer    
    llm_hyde = ChatOpenAI(model_name=os.environ.get('LLM_MODEL'), temperature=0)

    llm_chain = LLMChain(llm=llm_hyde, prompt=hyde_custom_prompt)

    # Embed the answer
    embeddings = HypotheticalDocumentEmbedder(
                    llm_chain=llm_chain, base_embeddings=embedding_function
                )

    # Instantiate vectorstore client
    client = chromadb.PersistentClient(path=CHROMA_PERSISTANT_DIR)

    # Assign the Hypothetical embeddings to the Vector store to enhance similarity
    db = Chroma(
        client=client,
        collection_name=collection_name,
        embedding_function=embeddings,
    )

    # Fetch the first 5 documents out of the Max Marginal Relevance Search
    # Keep a lambda mult (value from 0 to 1)  that determines 
    # the degree of diversity among the results: 0 min, 1 max
    retriever = db.as_retriever(
                                    search_type="mmr",
                                    search_kwargs={'k': 5, 'lambda_mult': 0.5}
                                )

    # Fetch the context
    context = retriever.get_relevant_documents(question)

    llm = ChatOpenAI(model_name=os.environ.get('LLM_MODEL'), temperature=0)

    # Instantiate the chain, containing the context, the question, templates and the llm
    rag_chain = (
                    {"context": retriever, "question": RunnablePassthrough()} | template | llm
                )

    # return the output
    return rag_chain.invoke(question).content
    