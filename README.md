# 🚀 DocuMind AI

An end-to-end Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask natural language questions. The system retrieves the most relevant document content using semantic search and generates accurate answers using a locally hosted Llama 3.2 model through Ollama.

---

## ✨ Features

- 📄 Upload PDF documents
- 🔍 Extract text from PDFs
- ✂️ Intelligent text chunking
- 🧠 Generate embeddings using Sentence Transformers
- 📦 Store embeddings in FAISS
- 🔎 Semantic document retrieval
- 🤖 Local LLM inference with Ollama (Llama 3.2)
- ⚡ FastAPI REST APIs
- 📝 Modular service-oriented architecture
- 📊 Interactive Swagger API documentation

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Python 3.11+
- Uvicorn

### AI / RAG
- Sentence Transformers
- FAISS
- Ollama
- Llama 3.2

### PDF Processing
- PyMuPDF (fitz)

### Other Libraries
- NumPy
- Pydantic
- python-dotenv

---

## 🏗️ Architecture

```text
                    User
                      │
                      ▼
             FastAPI Backend
          ┌───────────────────┐
          │                   │
          ▼                   ▼
     Upload API          Chat API
          │                   │
          ▼                   ▼
 Document Pipeline      Retriever
          │                   │
          ▼                   ▼
   PDF Extraction      FAISS Search
          │                   │
          ▼                   ▼
 Text Chunking       Relevant Context
          │                   │
          ▼                   ▼
 Sentence Embeddings  Ollama (Llama 3.2)
          │                   │
          └──────────► AI Response
```

---

## 📂 Project Structure

```text
DocuMind-AI/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── exceptions/
│   │   ├── rag/
│   │   ├── services/
│   │   ├── config.py
│   │   ├── logger.py
│   │   ├── schemas.py
│   │   └── main.py
│   │
│   ├── uploads/
│   ├── requirements.txt
│   └── .env
│
└── frontend/   (Coming Soon)
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd DocuMind-AI
```

---

### 2. Create a virtual environment

```bash
cd backend

python -m venv venv
```

Activate:

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Install Ollama

Download and install Ollama.

Pull the model:

```bash
ollama pull llama3.2
```

---

### 5. Configure environment variables

Create a `.env` file inside the `backend` folder:

```env
APP_NAME=DocuMind AI
LLM_MODEL=llama3.2
EMBEDDING_MODEL=all-MiniLM-L6-v2
TOP_K=3
UPLOAD_DIR=uploads
```

---

### 6. Run the application

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### Upload PDF

```
POST /upload
```

Uploads a PDF, extracts text, generates embeddings and stores them in FAISS.

---

### Chat

```
POST /chat
```

Example request

```json
{
  "question": "What services does Beetle provide?"
}
```

Example response

```json
{
  "question": "What services does Beetle provide?",
  "answer": "Beetle provides Sales, Rental, AMC and Spare Parts."
}
```

---

## 🚀 Current Features

- ✅ PDF Upload
- ✅ PDF Text Extraction
- ✅ Text Chunking
- ✅ Sentence Embeddings
- ✅ FAISS Vector Search
- ✅ Semantic Retrieval
- ✅ Ollama Integration
- ✅ Llama 3.2
- ✅ Chat API
- ✅ Logging
- ✅ Custom Exceptions
- ✅ Environment Configuration

---

## 🔮 Future Enhancements

- React Frontend
- Multiple PDF Support
- Conversation Memory
- Persistent FAISS Index
- Docker Support
- User Authentication
- Cloud Deployment

---

## 👩‍💻 Author

**Varshitha H**

Built as a portfolio project to demonstrate modern AI application development using Retrieval-Augmented Generation (RAG), FastAPI, FAISS, and Ollama.