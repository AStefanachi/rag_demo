# utils\classes.py

from langchain.document_loaders import PyPDFLoader

class PDFLoader:

    def __init__(self, path):
        self.path = path
        self.loader = None

    def load_and_split(self):
        self.loader = PyPDFLoader(self.path)
        return self.loader.load_and_split()
