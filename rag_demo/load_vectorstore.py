# rag_demo\load_vectorstore.py
# Import necessary modules, classes, and functions
from utils.classes import ChromaDB
from utils.constants import CHROMA_PERSISTANT_DIR
from utils.functions import create_text_splitter
from dotenv import load_dotenv
from uuid import uuid4
from tqdm.auto import tqdm
import time
from langchain.embeddings import SentenceTransformerEmbeddings

def load_vectorstore_chromadb(documents, collection_name: str):
    """
    Load documents into a ChromaDB vector store.

    Args:
        documents (list): A list of documents to be loaded.
        collection_name (str): The name of the collection to store the documents.

    Returns:
        str: A success message indicating the operation was successful.
    """

    # Initialize the ChromaDB client
    client = ChromaDB(CHROMA_PERSISTANT_DIR).client

    # Attempt to delete the existing collection if it exists
    try:
        if client.get_collection(name=collection_name):
            client.delete_collection(name=collection_name)
    except ValueError as e:
        # Print an error message if the collection cannot be deleted
        print(f"Cannot delete collection:", e)

    # Get or create a new collection with the specified name
    collection = client.get_or_create_collection(name=collection_name, metadata={"hnsw:space": "cosine"})    

    # Initialize the embeddings model
    embed = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # Create a text splitter function
    text_splitter = create_text_splitter()

    # Set the batch limit for processing
    batch_limit = 25
    # Initialize lists to store texts and their metadata
    texts = []
    metadatas = []

    # Process each document and load it into the collection in batches
    for i, record in enumerate(tqdm(documents, desc="Processing batch")):
        # Extract metadata for the current record
        metadata = {
            'source': record.metadata['source'],
            'page': record.metadata['page'],
        }
        # Split the record's page content into chunks
        record_page_content = text_splitter.split_text(record.page_content)
        # Create metadata for each chunk
        record_metadatas = [{
            "chunk": j, "text": page_content, **metadata
        } for j, page_content in enumerate(record_page_content)]
        # Add the chunks and their metadata to the current batch
        texts.extend(record_page_content)
        metadatas.extend(record_metadatas)
        # If the batch limit is reached, load the batch into the collection
        if len(texts) >= batch_limit:
            # Generate unique IDs for each chunk
            ids = [str(uuid4()) for _ in range(len(texts))]
            # Embed the texts using the embeddings model
            embeds = embed.embed_documents(texts)
            # Upsert the batch into the collection
            collection.upsert(ids=ids, embeddings=embeds, documents=texts, metadatas=metadatas)
            # Sleep for 2 seconds to avoid overloading the database
            time.sleep(2)
            # Reset the batch lists
            texts = []
            metadatas = []

    # Load any remaining texts into the collection
    if len(texts) > 0:
        # Generate unique IDs for each chunk
        ids = [str(uuid4()) for _ in range(len(texts))]
        # Embed the texts using the embeddings model
        embeds = embed.embed_documents(texts)
        # Upsert the final batch into the collection
        collection.upsert(ids=ids, embeddings=embeds, documents=texts, metadatas=metadatas)
        # Sleep for 2 seconds to avoid overloading the database
        time.sleep(2)
    
    # Return a success message
    return "Success"
