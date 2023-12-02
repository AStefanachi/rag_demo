# utils\constants.py
import os, sys

HOME_DIR = sys.path[0]
SAMPLE_SOURCES_PDF = os.path.join(HOME_DIR, "sample_sources", "pdf")
CHROMA_PERSISTANT_DIR = os.path.join(HOME_DIR, "chromadb")
PROMPT_YAML_DIR = os.path.join(HOME_DIR, "prompt_yaml")