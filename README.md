# Document_Intelligence_Chatbot_using_Retrieval_Augmented_Generation-
Document-centric conversational AI system using Retrieval-Augmented Generation (RAG) to enable accurate, context-aware question answering over large PDF datasets.
# 📄 RAG-Based Document Chatbot (LangChain + OpenAI)

A **Retrieval-Augmented Generation (RAG)** based conversational AI system that enables users to query large collections of PDF documents and receive **context-aware, grounded answers** using OpenAI LLMs.

This project demonstrates a **production-style GenAI pipeline** combining document ingestion, semantic search, and conversational AI.

---

## 🚀 Features

* Conversational question answering over **multiple PDF documents**
* **Retrieval-Augmented Generation (RAG)** to reduce hallucinations
* Semantic search using **vector embeddings**
* Maintains **chat history** for follow-up questions
* Web interface powered by **Flask**
* Modular, extensible, and easy to scale

---

## 🧠 Architecture Overview

```
User Query
   ↓
Retriever (FAISS Vector Store)
   ↓
Relevant Document Chunks
   ↓
LLM (OpenAI)
   ↓
Context-Aware Answer
```

**Key Idea:**
Instead of relying only on an LLM, the system retrieves relevant document context at runtime and grounds the response in actual source content.

---

## 🛠️ Tech Stack

* **Language:** Python
* **GenAI / NLP:** LangChain, OpenAI API
* **Vector Database:** FAISS
* **Backend:** Flask
* **Document Processing:** PyPDF
* **Environment Management:** Conda, pip

---

## 📂 Project Structure

```
GenAI/
│── gen_ai.py              # RAG pipeline logic
│── gen_ai_chatbot.py      # Flask application
│── data/                 # PDF documents
│── templates/             # HTML templates
│── static/                # CSS / assets
│── requirements.txt
│── README.md
```

---

## ⚙️ Environment Setup

### 1️⃣ Create Conda Environment

```bash
conda create -n rag_env python=3.10 -y
conda activate rag_env
```

### 2️⃣ Install Dependencies

```bash
pip install flask langchain langchain-community langchain-core \
            langchain-openai langchain-text-splitters \
            faiss-cpu pypdf openai
```

> ⚠️ **Note:** LangChain versions are pinned to avoid Pydantic v2 compatibility issues.

---

## 🔐 OpenAI API Key Setup

Set your API key as an environment variable:

**Windows (PowerShell)**

```powershell
setx OPENAI_API_KEY "your_openai_api_key"
```

**Linux / macOS**

```bash
export OPENAI_API_KEY="your_openai_api_key"
```

The application automatically reads the key from the environment.

---

## ▶️ Running the Application

```bash
python gen_ai_chatbot.py
```

Open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

## 📌 Example Use Cases

* Internal knowledge base chatbot
* Policy and compliance document Q&A
* Research paper summarization
* Technical documentation assistant

---

## 🔍 Key Design Decisions

* **RAG over fine-tuning:** Allows dynamic document updates without retraining
* **Chunk overlap:** Preserves semantic continuity across document sections
* **FAISS:** Fast, local similarity search for embeddings
* **Environment isolation:** Prevents dependency conflicts

---

## 📈 Future Enhancements

* Replace FAISS with Pinecone / Weaviate for large-scale deployments
* Add source citations in responses
* Implement user authentication and access control
* Enable streaming responses
* Dockerize the application

---

## 👤 Author

**Senthil**
Senior Python & GenAI Engineer

* LinkedIn: [https://linkedin.com/in/yourprofile](www.linkedin.com/in/senthil-prabhu-aa287964 )
* GitHub: [https://github.com/yourprofile](https://github.com/Senthil1794/)

---

## ⭐ Why This Project Matters

This project showcases **real-world GenAI engineering skills**, including:

* Designing RAG architectures
* Handling LLM limitations and hallucinations
* Managing evolving AI tooling ecosystems
* Building production-ready AI-backed applications

---

⭐ *If you find this project useful, consider starring the repository!*
