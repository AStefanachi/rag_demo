# utils\functions.py
# This module provides utility functions for text tokenization and splitting.

# External imports
from langchain.text_splitter import RecursiveCharacterTextSplitter  # Langchain library for text splitting
import tiktoken  # Library for tokenization

# Initialize the tokenizer with a specific encoding
tokenizer = tiktoken.get_encoding('cl100k_base')

def tiktoken_len(text: str) -> int:
    """
    Calculates the length of the text in terms of tiktoken tokens.

    Args:
        text (str): The text to be tokenized.

    Returns:
        int: The number of tokens.
    """
    tokens = tokenizer.encode(text, disallowed_special=())
    return len(tokens)

def create_text_splitter() -> RecursiveCharacterTextSplitter:
    """
    Creates and returns a RecursiveCharacterTextSplitter instance.

    Returns:
        RecursiveCharacterTextSplitter: An instance of RecursiveCharacterTextSplitter configured for use.
    """
    return RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=20,
        length_function=tiktoken_len,
        separators=["\n\n", "\n", " ", ""]
    )
