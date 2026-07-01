from app.rag.retrievers.hybrid_retriever import (
    HybridRetriever
)


class RetrievalService:

    def __init__(self):

        self.retriever = (
            HybridRetriever()
        )

    def retrieve(
        self,
        question: str
    ):

        return self.retriever.retrieve(
            question
        )