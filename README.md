# AWS Customer Agreement Chatbot 🤖

An AI-powered chatbot that answers user queries related to the AWS Customer Agreement document using NLP, embeddings, and Retrieval-Augmented Generation (RAG).

## 📌 Project Overview

This project allows users to ask questions about the AWS Customer Agreement PDF and get relevant answers from the document.

The system processes the PDF, converts the content into vector embeddings, stores them in a vector database, and retrieves the most relevant information to generate responses.

## 🚀 Features

- Upload and process AWS Customer Agreement PDF
- Extract text from documents
- Split documents into smaller chunks
- Generate text embeddings
- Store embeddings using FAISS Vector Database
- Query-based document retrieval
- AI chatbot response generation
- REST API using FastAPI

## 🛠️ Technologies Used

- Python
- FastAPI
- LangChain
- FAISS
- Hugging Face Embeddings
- Uvicorn
- NLP / RAG Architecture
- 
## ▶️ Run Application

### 1. Navigate to Backend Folder

```bash
cd backend
uvicorn main:app --reload

### 1. Navigate to Frontend Folder

```bash
cd frontend
