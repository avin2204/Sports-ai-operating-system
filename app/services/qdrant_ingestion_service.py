from app.rag.vectorstores.qdrant_vector_store import (
    QdrantVectorStore
)


class QdrantIngestionService:

    def __init__(self):

        self.vector_store = (
            QdrantVectorStore()
        )

    def store_chunk(
        self,
        chunk: str,
        embedding: list[float]
    ):

        self.vector_store.add(
            text=chunk,
            embedding=embedding
        )