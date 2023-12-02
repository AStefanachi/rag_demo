
# rag_demo\load_pdf.py
from utils.classes import PDFLoader
from utils.constants import SAMPLE_SOURCES_PDF
import os

def load_pdfloader(name: str):
    pdf_loader = PDFLoader(os.path.join(SAMPLE_SOURCES_PDF, name))
    return pdf_loader.load_and_split()