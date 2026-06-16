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

embedding_model = LocalEmbedding()
vector_store = QdrantVectorStore()
llm = GeminiProvider()


@router.post("/ask")
def ask(question: str):

    query_vector = embedding_model.embed(
        question
    )

    results = vector_store.search(
        embedding=query_vector,
        top_k=3
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

    answer = llm.generate(
        prompt
    )

    return {
        "question": question,
        "answer": answer,
        "context": context
    }