from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

TXT_PATH = "../data/aws_customer_agreement.txt"
VECTOR_DB_PATH = "../vectorstore"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def ingest_document():

    with open(TXT_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    documents = [
        Document(page_content=text)
    ]

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    vectorstore.save_local(VECTOR_DB_PATH)

    return len(chunks)


def ask_question(query):

    vectorstore = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = vectorstore.similarity_search(
        query,
        k=3
    )

    if not docs:
        return (
            "Answer not found in document.",
            ""
        )

    source = docs[0].page_content

    answer = (
        "Based on AWS Customer Agreement:\n\n"
        + source[:500]
    )

    return answer, source[:500]