# This is a working example of the PyPDF Loader

from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"C:\PRIVATE\rag_demo\sample_sources\pdf\DR_EUS_MFL70442678_00_221121_00_WEB_EN.pdf")
pages = loader.load_and_split()

# I want you to generalize it in a class

class PDFLoader:

    def __init__(self, path):
        self.path = path
        self.loader = None

    def load_and_split(self):
        self.loader = PyPDFLoader(self.path)
        return self.loader.load_and_split()
