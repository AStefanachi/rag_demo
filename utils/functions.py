# utils\functions.py

# Text Splitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
## Tiktoken
import tiktoken

tokenizer = tiktoken.get_encoding('cl100k_base')
def tiktoken_len(text):
    '''Returns the tiktoken len'''
    tokens = tokenizer.encode(
        text,
        disallowed_special=()
    )
    return len(tokens)


def create_text_splitter():
    '''Creates a RecursiveCharacterTextSplitter'''
    return RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=20,
        length_function=tiktoken_len,
        separators=["\n\n", "\n", " ", ""]
    )  