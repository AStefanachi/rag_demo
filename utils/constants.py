# utils\constants.py
"""
Constants used throughout the utils package.

This module defines path constants that are used across different modules
within the utils package for file and directory management.
"""

import os
import sys

# Define the home directory based on the system path
HOME_DIR = sys.path[0]

# Define the path to the sample sources PDF directory
SAMPLE_SOURCES_PDF = os.path.join(HOME_DIR, "sample_sources", "pdf")

# Define the path to the ChromaDB persistent directory
CHROMA_PERSISTANT_DIR = os.path.join(HOME_DIR, "chromadb")

# Define the path to the directory containing prompt YAML files
PROMPT_YAML_DIR = os.path.join(HOME_DIR, "prompt_yaml")
