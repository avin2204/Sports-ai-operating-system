from app.services.retrieval_service import (
    RetrievalService
)

from app.providers.gemini_provider import (
    GeminiProvider
)


class AskService:

    def __init__(self):

        self.retrieval_service = (
            RetrievalService()
        )

        self.llm = (
            GeminiProvider()
        )

    def ask(
        self,
        question: str
    ):

        chunks = (

            self.retrieval_service.retrieve(
                question
            )
        )

        context = "\n\n".join(
            chunks
        )

        prompt = f"""
Context:
{context}

Question:
{question}

Answer:
"""

        answer = (
            self.llm.generate(
                prompt
            )
        )

        return {

            "question":
            question,

            "answer":
            answer,

            "retrieved_chunks":
            len(chunks)
        }