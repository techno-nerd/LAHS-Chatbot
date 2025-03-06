import streamlit as st
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from groq import Groq
import os


CHUNKS = 3
MODEL_NAME = "llama-3.3-70b-versatile"

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


@st.cache_resource(show_spinner=False) #Only runs once
def get_retriever():
    # Loading the saved embeddings 
    embedding_model = SentenceTransformerEmbeddings(model_name="all-mpnet-base-v2")
    loaded_vectors = FAISS.load_local("vectors", embedding_model, allow_dangerous_deserialization=True)

    faiss_retriever = loaded_vectors.as_retriever(search_kwargs={"k":CHUNKS})
    return faiss_retriever


def rewrite_prompt(prompt, chunks):
    """Adds the context to the prompt"""
    prompt = prompt + "Context: " + " ".join([chunk.page_content for chunk in chunks])
    return prompt

def get_response(prompt):
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    return completion.choices[0].message.content