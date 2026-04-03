from fastapi import FastAPI
from ingestion.loader import load_documents
from retrieval.vector_store import create_vector_store, load_vector_store, cosine_search, euclidean_search
from retrieval.bm25 import bm25_search
from reranker.reranker import rerank
from agent.decision import agent_decision
from api.weather import get_weather
from llm.openrouter import call_llm

app = FastAPI()

documents = load_documents()

try:
    db = load_vector_store()
except:
    db = create_vector_store(documents)


@app.get("/")
def home():
    return {"message": "Agentic RAG Running 🚀"}


@app.get("/query")
def query(q: str):
    decision = agent_decision(q)

    if decision == "api":
        return get_weather()

    elif decision == "rag":
        docs = cosine_search(db, q)

    else:
        docs1 = cosine_search(db, q)
        docs2 = bm25_search(documents, q)
        docs = docs1 + docs2

    docs = rerank(q, docs)

    context = " ".join([d.page_content for d in docs[:3]])

    response = call_llm(q, context)

    return {
        "decision": decision,
        "response": response
    }