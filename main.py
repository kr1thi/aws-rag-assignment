from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag import ingest_document, ask_question
from database import SessionLocal, Interaction

from sqlalchemy import func
import time

app = FastAPI(title="AWS RAG System")


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {"message": "AWS RAG API Running"}


@app.post("/ingest")
def ingest():
    try:
        chunks = ingest_document()

        return {
            "message": "Document processed successfully",
            "chunks": chunks
        }

    except Exception as e:
        return {
            "error": str(e)
        }


@app.post("/ask")
def ask(request: QueryRequest):

    if not request.query.strip():
        raise HTTPException(
            status_code=400,
            detail="Query cannot be empty"
        )

    start_time = time.time()

    try:

        answer, source = ask_question(
            request.query
        )

        response_time = time.time() - start_time

        db = SessionLocal()

        interaction = Interaction(
            query=request.query,
            answer=answer,
            source_chunk=source,
            response_time=response_time,
            no_answer="Answer not found" in answer
        )

        db.add(interaction)
        db.commit()
        db.close()

        return {
            "answer": answer,
            "source": source
        }

    except Exception as e:
        return {
            "error": str(e)
        }


@app.get("/analytics")
def analytics():

    db = SessionLocal()

    most_frequent = (
        db.query(
            Interaction.query,
            func.count(
                Interaction.id
            ).label("count")
        )
        .group_by(
            Interaction.query
        )
        .order_by(
            func.count(
                Interaction.id
            ).desc()
        )
        .all()
    )

    no_answer = (
        db.query(
            Interaction
        )
        .filter(
            Interaction.no_answer == True
        )
        .all()
    )

    avg_latency = (
        db.query(
            func.avg(
                Interaction.response_time
            )
        ).scalar()
    )

    db.close()

    return {
        "most_frequent_questions": [
            {
                "query": item.query,
                "count": item.count
            }
            for item in most_frequent
        ],

        "no_answer_queries": [
            item.query
            for item in no_answer
        ],

        "avg_response_time":
            round(avg_latency, 4)
            if avg_latency
            else 0
    }