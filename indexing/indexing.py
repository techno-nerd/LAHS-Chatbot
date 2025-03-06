from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS


def load_docs(directory):
  loader = DirectoryLoader(directory)
  documents = loader.load()
  return documents

def split_docs(documents,text_splitter):
  docs = text_splitter.split_documents(documents[:])
  return docs

raw_docs = load_docs("documents/")

print(f"{len(raw_docs)} documents loaded")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100, separators=["\n\n","\n","."," ",""])
docs = split_docs(raw_docs, text_splitter)
print(f"Documents split into {len(docs)} chunks")

embedding_model = SentenceTransformerEmbeddings(model_name="all-mpnet-base-v2")
vectorstore = FAISS.from_documents(docs, embedding_model)
print("Vector database made")
vectorstore.save_local("vectors")