from flask import Flask, render_template, request, jsonify
from rag_demo.orchestration import load_chromadb
from rag_demo.retrievals import query_LG_DRYER_DEMO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load_vectorstore', methods=['POST'])
def load_vectorstore():
    document_name = request.form['document_name']
    collection_name = request.form['collection_name']
    result = load_chromadb(document_name, collection_name)
    return jsonify(result)

@app.route('/query', methods=['POST'])
def query():
    prompt = request.form['prompt']
    result = query_LG_DRYER_DEMO(prompt)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
