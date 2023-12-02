from langchain.document_loaders import UnstructuredPDFLoader

loader = UnstructuredPDFLoader(r"C:\PRIVATE\rag_demo\sample_sources\pdf\DR_EUS_MFL70442678_00_221121_00_WEB_EN.pdf")

data = loader.load()

print(data)