# rag_demo\load_vectorstore.py
## Utils
from utils.classes import ChromaDB
from utils.constants import CHROMA_PERSISTANT_DIR
from utils.functions import create_text_splitter
## Python Core
from dotenv import load_dotenv
from uuid import uuid4
from tqdm.auto import tqdm
import time
## Langchain
from langchain.embeddings import SentenceTransformerEmbeddings


def load_vectorstore_chromadb(documents, collection_name: str):
    load_dotenv('settings.env')

    client = ChromaDB(CHROMA_PERSISTANT_DIR).client

    # If the collection exists, we drop it and add new data
    try:
        if client.get_collection(name=collection_name):
            client.delete_collection(name=collection_name)
    except ValueError as e:
        print(f"Cannot delete collection:", e)

    # Get or create the collection
    collection = client.get_or_create_collection(name=collection_name, metadata={"hnsw:space": "cosine"})    

    embed = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    text_splitter = create_text_splitter()

    # Preparing the load in batches of 25 to ChromaDB
    batch_limit = 25   
    texts = []
    metadatas = []

    for i, record in enumerate(tqdm(documents, desc="Processing batch")):
        # first get metadata fields for this record
        metadata = {
            'source': record.metadata['source'],
            'page': record.metadata['page'],
        }
        # now we create chunks from the record text
        record_page_content = text_splitter.split_text(record.page_content)
        # create individual metadata dicts for each chunk
        record_metadatas = [{
            "chunk": j, "text": page_content, **metadata
        } for j, page_content in enumerate(record_page_content)]
        # append these to current batches
        texts.extend(record_page_content)
        metadatas.extend(record_metadatas)
        # if we have reached the batch_limit we can add texts
        if len(texts) >= batch_limit:
            ids = [str(uuid4()) for _ in range(len(texts))]
            embeds = embed.embed_documents(texts)
            collection.upsert(ids=ids, embeddings=embeds, documents=texts, metadatas=metadatas)
            time.sleep(2)
            texts = []
            metadatas = []

    if len(texts) > 0:
        ids = [str(uuid4()) for _ in range(len(texts))]
        embeds = embed.embed_documents(texts)
        collection.upsert(ids=ids, embeddings=embeds, documents=texts, metadatas=metadatas)
        time.sleep(2)
    
    return "Success"