from rag_demo.orchestration import load_chromadb
from rag_demo.retrievals import query_LG_DRYER_DEMO
import argparse

def main():
    parser = argparse.ArgumentParser(description="RAG Demo Orchestration")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Subparser for load_vectorstore
    parser_load = subparsers.add_parser('load_vectorstore', help='Load a document into ChromaDB vector store')
    parser_load.add_argument('document_name', type=str, help='The name of the document to be loaded')
    parser_load.add_argument('collection_name', type=str, help='The name of the collection where the document will be stored')

    # Subparser for query
    parser_query = subparsers.add_parser('query', help='Query the LG_DRYER_DEMO collection from the vectorstore')
    parser_query.add_argument('prompt', type=str, help='The question to query the vectorstore with')

    args = parser.parse_args()

    if args.command == 'load_vectorstore':
        result = load_chromadb(args.document_name, args.collection_name)
        print(result)
    elif args.command == 'query':
        result = query_LG_DRYER_DEMO(args.prompt)
        print(result)

if __name__ == '__main__':
    main()
