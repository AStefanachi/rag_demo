# RAG Demo Application

This application demonstrates the capabilities of a Retrieval-Augmented Generation (RAG) system using Flask for the web backend and ChromaDB for document storage and retrieval.

## Author

Andrea Stefanachi <andrea@stefanachi.com>

## Installation

Before installing the necessary dependencies, you need to create a `settings.env` file in the project root with the following contents as an example:

```env
FLASK_APP=main.py
FLASK_ENV=development
LLM_MODEL=gpt-3.5-turbo-1106
OPENAI_API_KEY=YOUROPENAIAPIKEY
```

Additionally, create a folder to store your ChromaDB persistent client data.

To install the necessary dependencies for this application, run the following command:

```bash
poetry install
```

Make sure you have Poetry installed on your system. If not, you can install it by following the instructions on the [Poetry website](https://python-poetry.org/docs/).

## Usage

To run the application, use the following command:

```bash
flask run
```

Navigate to `http://127.0.0.1:5000/` in your web browser to access the application.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
