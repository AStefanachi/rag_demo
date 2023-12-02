# utils\classes.py
"""
This module provides a class for loading and processing PDF documents.
"""

from langchain.document_loaders import PyPDFLoader
import chromadb
from functools import partial
import traceback


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
    ChromaDB is a class for interacting with a ChromaDB database.

    It provides an interface to connect to a ChromaDB collection and perform
    operations such as querying and updating records.

    Attributes:
        collection_name (str): The name of the collection in ChromaDB.
        home_dir (str): The home directory where ChromaDB data is stored.
        client (PersistentClient): A client instance for database operations.
    """

    def __init__(self, home_dir):
        """
        Initializes a new instance of the ChromaDB class.

        Args:
            home_dir (str): The home directory where ChromaDB data is stored.
        """
        self.home_dir = home_dir
        self.client = chromadb.PersistentClient(path=home_dir)


class Orchestrator:
    """
    Manages and executes a sequence of functions sequentially.

    Functions are loaded with their arguments, and when run, each function's output
    is passed as input to the next function in the sequence.
    """
    
    def __init__(self):
        """Initializes the Orchestrator with an empty list to store functions."""
        self.functions = []
    
    def load_function(self, function, *args, **kwargs):
        """Loads a function into the orchestrator with its arguments.

        Args:
            function: The function to be loaded into the orchestrator.
            args: Positional arguments to be passed to the function.
            kwargs: Keyword arguments to be passed to the function.
        """
        self.functions.append(partial(function, *args, **kwargs))
        
    def run(self):
        # Runner function to execute each loaded function, passing the result of the
        # previous function as its argument.
        def runner(func, previous_result):
            # Pass the previous result into the function if it exists; otherwise, call without arguments.
            result = func(previous_result) if previous_result is not None else func()
            # Yield the function's result back to the caller
            yield result
            # Return the result to be used as input for the next function
            return result

        # Initialize the result variable to None
        result = None
        try:
            # Execute each loaded function sequentially
            for function in self.functions:
                # Obtain a generator from the runner function
                result_generator = runner(function, result)
                # Retrieve the result from the generator and update the result variable
                result = next(result_generator)
        except Exception as e:
            # Yield an error message and stop execution if an exception occurs
            yield f"Error: {e}\n{traceback.format_exc()}"
            return
        # Yield a final message indicating completion and the final result after all functions are executed
        yield result