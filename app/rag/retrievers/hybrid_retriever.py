from rank_bm25 import BM25Okapi

from app.rag.vectorstores.qdrant_vector_store import (
    QdrantVectorStore
)

from app.services.embedding_service import (
    EmbeddingService
)


class HybridRetriever:

    def __init__(self):

        self.qdrant = (
            QdrantVectorStore()
        )

        self.embedding_service = (
            EmbeddingService()
        )

    def retrieve(
        self,
        question: str,
        top_k: int = 5
    ):

        query_vector = (
            self.embedding_service.embed(
                question
            )
        )

        vector_results = (
            self.qdrant.search(
                embedding=query_vector,
                top_k=top_k
            )
        )

        documents = [

            hit.payload["text"]

            for hit in vector_results
        ]

        if not documents:

            return []

        bm25 = BM25Okapi(

            [
                doc.split()
                for doc in documents
            ]
        )

        scores = bm25.get_scores(
            question.split()
        )

        ranked = sorted(

            zip(
                documents,
                scores
            ),

            key=lambda x: x[1],

            reverse=True
        )

        return [

            item[0]

            for item in ranked
        ]