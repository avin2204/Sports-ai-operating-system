from functools import lru_cache

from fastapi import APIRouter

from app.rag.embeddings.local_embedding import (
    LocalEmbedding
)

from app.rag.vectorstores.qdrant_vector_store import (
    QdrantVectorStore
)

from app.providers.gemini_provider import (
    GeminiProvider
)

router = APIRouter()


@lru_cache
def get_embedding_model():

    return LocalEmbedding()


@lru_cache
def get_vector_store():

    return QdrantVectorStore()


@lru_cache
def get_llm():

    return GeminiProvider()


@router.post("/ask")
def ask(
    question: str
):

    embedding_model = (
        get_embedding_model()
    )

    vector_store = (
        get_vector_store()
    )

    llm = (
        get_llm()
    )

    query_vector = (
        embedding_model.embed(
            question
        )
    )

    results = (
        vector_store.search(
            embedding=query_vector,
            top_k=3
        )
    )

    context = "\n".join(
        hit.payload["text"]
        for hit in results
    )

    prompt = f"""
Context:
{context}

Question:
{question}

Answer:
"""

    answer = (
        llm.generate(
            prompt
        )
    )

    return {

        "question":
        question,

        "answer":
        answer,

        "context":
        context
    }