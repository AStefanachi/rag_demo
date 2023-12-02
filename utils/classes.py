# utils\classes.py
"""
This module provides a class for loading and processing PDF documents.
"""

from langchain.document_loaders import PyPDFLoader
import chromadb


class PDFLoader:
    """
    A class that wraps the PyPDFLoader to load and split PDF documents.

    Attributes:
        path (str): The file path to the PDF document.
        loader (PyPDFLoader): An instance of PyPDFLoader for loading the document.
    """

    def __init__(self, path):
        """
        Initializes the PDFLoader with the given file path.

        Args:
            path (str): The file path to the PDF document.
        """
        self.path = path
        self.loader = None

    def load_and_split(self):
        """
        Loads the PDF document and splits it into pages.

        Returns:
            list: A list of pages from the PDF document.
        """
        self.loader = PyPDFLoader(self.path)
        return self.loader.load_and_split()


class ChromaDB:
    """
    Write some proper documentation here
    """

    def __init__(self, collection_name, home_dir):
        """
        Initializes the ChromaDBLoader with the given collection name and home directory.

        Args:
            collection_name (str): The name of the collection in ChromaDB.
            home_dir (str): The home directory where ChromaDB data is stored.
        """
        self.collection_name = collection_name
        self.home_dir = home_dir
        self.client = chromadb.PersistentClient(path=home_dir)
        return self.client
