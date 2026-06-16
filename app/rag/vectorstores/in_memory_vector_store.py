from app.rag.vectorstores.base_vector_store import BaseVectorStore
from app.rag.utils.similarity import (
    cosine_similarity
)   


class InMemoryVectorStore(
    BaseVectorStore
):

    def __init__(self):

        self.data = []

    def add(
        self,
        text: str,
        embedding: list[float]
    ):

        self.data.append(
            {
                "text": text,
                "embedding": embedding
            }
        )

    def search(
    self,
    embedding,
    top_k=3
):

    scored_results = []

    for item in self.data:

        score = cosine_similarity(
            embedding,
            item["embedding"]
        )

        scored_results.append(
            {
                "text": item["text"],
                "embedding": item["embedding"],
                "score": score
            }
        )

    scored_results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return scored_results[:top_k]