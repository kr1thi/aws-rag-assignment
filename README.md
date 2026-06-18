# AWS Customer Agreement Chatbot 🤖

An AI-powered chatbot that answers user queries related to the AWS Customer Agreement document using NLP, embeddings, and Retrieval-Augmented Generation (RAG).

## 📌 Project Overview

This project allows users to ask questions about the AWS Customer Agreement PDF and get relevant answers from the document.

The system processes the PDF, extracts text, converts the content into vector embeddings, stores them in a vector database, and retrieves the most relevant information to generate accurate responses.

## 🚀 Features

- Upload and process AWS Customer Agreement PDF
- Extract text from documents
- Split documents into smaller chunks
- Generate text embeddings
- Store embeddings using FAISS Vector Database
- Query-based document retrieval
- AI chatbot response generation
- REST API using FastAPI
- Interactive chatbot interface

## 🛠️ Technologies Used

- Python
- FastAPI
- React.js
- LangChain
- FAISS
- Hugging Face Embeddings
- Uvicorn
- NLP
- RAG Architecture

## 📂 Project Structure

```
AWS-Customer-Agreement-Chatbot/
│
├── backend/
│   ├── main.py
│   ├── ingest.py
│   ├── requirements.txt
│
├── frontend/
│   ├── app.js
|
│
├── data/
│   └── aws_customer_agreement.pdf
│
└── README.md
```

## ▶️ Run Application

### Backend Setup

Navigate to backend folder:

```bash
cd backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI server:

```bash
uvicorn main:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

---

### Frontend Setup

Open another terminal:

```bash
cd frontend
```
Frontend URL:

```
http://localhost:3000
```

## 📌 API Endpoints

### Ingest Document

```
POST /ingest
```

Processes AWS Customer Agreement PDF and creates embeddings.

### Ask Question

```
POST /ask
```

Example:

```
What is AWS Confidential Information?
```

## 🔮 Future Enhancements

- Add authentication
- Deploy using AWS services
- Support multiple documents
- Improve chatbot accuracy
- Add voice assistant support

## 👩‍💻 Author

**Kiruthika J**
