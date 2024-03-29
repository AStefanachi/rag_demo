import os
import os
from flask import Flask, render_template, request, jsonify
from rag_demo.orchestration import load_chromadb
from rag_demo.retrievals import query_LG_DRYER_DEMO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list_documents', methods=['GET'])
def list_documents():
    directory = 'sample_sources/pdf'
    files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    return jsonify(files)

@app.route('/load_vectorstore', methods=['POST'])
def load_vectorstore():
    directory = 'sample_sources/pdf'
    files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
    if not files:
        return jsonify({'error': 'No documents found'}), 404
    document_name = request.form['document_name']
    collection_name = request.form['collection_name']
    result = load_chromadb(document_name, collection_name)
    return jsonify(result)

@app.route('/query', methods=['POST'])
def query():
    prompt = request.form['prompt']
    collection_name = request.form['collection_name']
    result = query_LG_DRYER_DEMO(prompt, collection_name)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
