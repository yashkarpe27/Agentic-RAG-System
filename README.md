# Agentic-RAG-System

# 🧠 Agentic RAG System using OpenRouter

## 🚀 Overview

This project implements an **Agentic Retrieval-Augmented Generation (RAG) System** using OpenRouter as the LLM provider.

The system intelligently decides how to respond to user queries by:

* Retrieving relevant knowledge from documents
* Calling external APIs (e.g., weather)
* Generating responses using LLM

---

## 🎯 Features

* ✅ Agent-based decision making
* ✅ Multi-retrieval strategies:

  * Cosine Similarity (FAISS)
  * Euclidean Distance
  * BM25 (Keyword search)
* ✅ Reranking using Cross-Encoder
* ✅ OpenRouter LLM integration
* ✅ External API support (Weather)
* ✅ FastAPI backend
* ✅ Fallback mechanism (no crashes)

---

## 🏗️ Architecture

User Query → Agent → Retrieval → Reranker → LLM → Response

---

## 🧩 Components

### 1. Data Ingestion

* Loads documents from text files

### 2. Embedding Generator

* Uses HuggingFace embeddings

### 3. Vector Store

* FAISS for efficient similarity search

### 4. Retrieval Layer

* Cosine Similarity
* Euclidean Distance
* BM25 Keyword Search

### 5. Reranking Module

* Cross-encoder improves relevance

### 6. Agent Layer

Decides:

* RAG (knowledge queries)
* API (real-time queries)
* Hybrid (both)

### 7. LLM Layer

* OpenRouter API (with fallback)

### 8. External API

* Weather API placeholder

---

## ⚙️ Installation

```bash
pip install fastapi uvicorn langchain langchain-community sentence-transformers rank-bm25 requests
```

---

## ▶️ Run the Project

```bash
uvicorn app:app --reload
```

---

## 🌐 API Usage

### Home:

```
http://127.0.0.1:8000/
```

### Query:

```
http://127.0.0.1:8000/query?q=What is AI?
```

---

## 🧠 Example Output

```json
{
  "decision": "rag",
  "response": "Artificial Intelligence is the simulation..."
}
```

---

## ⚠️ Note on OpenRouter Free Models

Free models may:

* Be rate-limited
* Be temporarily unavailable

✅ To handle this, the system includes:

* Retry logic
* Model fallback
* RAG-only fallback (guaranteed response)

---

## 🎓 Key Concepts

* RAG improves accuracy by grounding responses in data
* Agent enables dynamic decision-making
* Reranking improves retrieval quality

---

## 🚀 Future Improvements

* UI dashboard
* Streaming responses
* Multi-agent orchestration
* Caching layer

---

## 👨‍💻 Author

Yash Karpe
