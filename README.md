# SQL Question Answering Bot

## Description

This SQL Question Answering Bot is designed to offer users an interactive way to retrieve information and answer questions directly from a PDF document. Leveraging the power of state-of-the-art language models and vector storage solutions, the application provides a seamless chatbot experience. The key features of this bot include:

- **Document-Based Knowledge**: The bot is initialized with information extracted from a specified PDF document, allowing it to answer questions based on the content of the document.
- **Interactive Chat Interface**: Users can interact with the bot through a simple text-based interface, asking questions and receiving answers in real-time.
- **Advanced Retrieval Mechanism**: Utilizes a combination of OpenAI's embeddings for document understanding and FAISS vector storage for efficient information retrieval.
- **Conversation Context Awareness**: Employs a conversation buffer memory to maintain the context of the conversation, enhancing the relevance of responses.

## User Instructions

### Installation and Setup

1. Ensure Python 3.8 or newer is installed on your system.
2. Clone this repository to your local machine.
3. Install the required dependencies by running `pip install -r requirements.txt` in your terminal.
4. Place the PDF document you wish to use as the knowledge base in the same directory as the application and rename it to `INFO.pdf`.

### Interacting with the Bot

- **Via Command Line (CLI):**
  - Run `python cli.py` in your terminal.
  - When prompted, enter your question and press Enter.
  - To exit, type "exit" and press Enter.

- **Via Web Interface:**
  - Run `streamlit run app.py` in your terminal.
  - Access the web interface by navigating to the URL provided by Streamlit (usually `http://localhost:8501`).
  - Use the chat input box to ask questions and interact with the bot.

## Technical Innovations

The application integrates Retrieval-Augmented Generation (RAG) or Language Model (LLM) techniques with state-of-the-art tools for a sophisticated chatbot experience:

- **PyPDFLoader**: Extracts text from the specified PDF document to serve as the knowledge base for the bot.
- **OpenAIEmbeddings**: Utilizes embeddings from OpenAI to understand and interpret the content of the PDF document.
- **FAISS Vector Store**: Implements a fast and efficient vector storage solution to facilitate quick retrieval of information based on the query.
- **ConversationalRetrievalChain**: Combines the language model, vector storage, and conversation context to provide accurate and context-aware responses to user queries.

## Acknowledgments

- **OpenAI**: For providing the language model embeddings used for document understanding and conversation generation.
- **FAISS**: For the vector storage solution that enables efficient information retrieval.
- **Streamlit**: For the web framework that makes it easy to create and share beautiful, custom web apps for machine learning and data science.
- **PyPDF2**: For the PDF reading capabilities that allow extracting text from PDF documents.

This project is a demonstration of how advanced natural language processing and information retrieval techniques can be combined to create a powerful and user-friendly chatbot. 
Whether for educational purposes, customer support, or interactive exploration of documents, this bot showcases the potential of AI in enhancing our interaction with digital content.

streamlit link ---> https://datax-manasvi.streamlit.app/
