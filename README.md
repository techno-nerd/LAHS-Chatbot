# LAHS Chatbot

This is a simple demonstration on how Retrieval Augmented Generation (RAG) can be used to give Large Language Models a custom knowledge base. This gives them the ability to answer questions about more nuanced topics and reduces hallucinations.

## Overview
0. Getting the documents for the model to reference. These documents were taken from the [Los Altos High website](https://lahs.mvla.net) using a web scraper. The code for this is in the `scraping` folder, and the web pages are saved as raw `txt` files in the `documents` folder.

1. Creating a vector database with these documents. Using an embedding generation model, all chunks are turned into embeddings. When a prompt is entered, the embeddings are compared to find the most relevant chunks for that prompt. The database is stored in the `vectors` folder and was created using the script in the `indexing` folder.

2. Interacting with the model through a front-end, which has been built using Streamlit. The files for this are in the `app` folder. The app loads the vectors and queries them using the user prompt, and then gives it to an LLM (through the Groq API) to generate the final response.

## Setting it up

1. Install the dependencies: `pip install -r requirements.txt` (Warning: some of these packages are quite big. The total size is expected to be around 6.2 GB)

2. Add your Groq API key: Get a Groq API key from [GroqCloud](https://console.groq.com/keys). Then, create a `.env` file in the `app` folder and add this line: `GROQ_API_KEY = <YOUR_KEY>`

3. To run the app, `streamlit run app/app.py`