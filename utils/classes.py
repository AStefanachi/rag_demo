# utils\classes.py
"""
This module provides a class for loading and processing PDF documents.
"""

from langchain.document_loaders import PyPDFLoader


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
class ChromaDBLoader:
    """
    A class to handle the loading of data into ChromaDB.

    Attributes:
        collection_name (str): The name of the collection in ChromaDB.
        home_dir (str): The home directory where ChromaDB data is stored.
        client (chromadb.PersistentClient): The ChromaDB client instance.
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
        self.client = None

    def load_data(self, data_list):
        """
        Loads data into the specified ChromaDB collection.

        Args:
            data_list (list): A list of data to be loaded into ChromaDB.

        Returns:
            bool: True if the data was loaded successfully, False otherwise.
        """
        # The logic for loading data into ChromaDB will be implemented here.
        # This will include the code from utils\example.txt that handles the
        # ChromaDB loading process, adapted to use the class attributes and
        # parameters.
        pass  # Placeholder for the actual implementation.

# Add the rest of the code from utils\example.txt that is relevant to the
# ChromaDB loading process, adapted to fit within the ChromaDBLoader class.
