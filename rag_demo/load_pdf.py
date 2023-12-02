
# rag_demo\load_pdf.py
# Import necessary modules and classes
from utils.classes import PDFLoader
from utils.constants import SAMPLE_SOURCES_PDF
import os

def load_pdfloader(name: str):
    """
    Load a PDF file and split it into manageable parts.

    Args:
        name (str): The name of the PDF file to be loaded.

    Returns:
        list: A list of parts into which the PDF has been split.
    """
    # Create a PDFLoader instance with the path to the PDF file
    pdf_loader = PDFLoader(os.path.join(SAMPLE_SOURCES_PDF, name))
    # Load the PDF file and split it
    return pdf_loader.load_and_split()
