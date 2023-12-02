# from rag_demo.orchestration import load_chromadb
from utils.classes import ChromaDB
from utils.constants import CHROMA_PERSISTANT_DIR

# print(load_chromadb(document_name="DR_EUS_MFL70442678_00_221121_00_WEB_EN.pdf", collection_name="LG_DRYER_DEMO"))

from rag_demo.retrievals import query_tech_news_feed_chromadb

print(query_tech_news_feed_chromadb("What is the brand of this object?"))