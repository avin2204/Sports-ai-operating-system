from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)

from app.rag.vectorstores.base_vector_store import (
    BaseVectorStore
)


class QdrantVectorStore(BaseVectorStore):

    def __init__(self):

        self.client = QdrantClient(
            host="localhost",
            port=6333
        )

        self.collection_name = "sports_docs"

        collections = [
            c.name
            for c in self.client.get_collections().collections
        ]

        if self.collection_name not in collections:

            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE
                )
            )

    def add(
        self,
        text: str,
        embedding: list[float]
    ):

        point_id = abs(hash(text))

        self.client.upsert(
            collection_name=self.collection_name,
            points=[
                PointStruct(
                    id=point_id,
                    vector=embedding,
                    payload={
                        "text": text
                    }
                )
            ]
        )

    def search(
        self,
        embedding: list[float],
        top_k: int = 5
    ):

        results = self.client.query_points(
            collection_name=self.collection_name,
            query=embedding,
            limit=top_k
        )

        return results.points