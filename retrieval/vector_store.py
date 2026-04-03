from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embeddings():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def create_vector_store(documents):
    db = FAISS.from_documents(documents, get_embeddings())
    db.save_local("vector_store")
    return db

def load_vector_store():
    return FAISS.load_local("vector_store", get_embeddings())

def cosine_search(db, query):
    return db.similarity_search(query)

def euclidean_search(db, query):
    return db.similarity_search(query, metric="l2")
