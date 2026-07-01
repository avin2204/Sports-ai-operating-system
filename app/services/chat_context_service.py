from app.memory.query_rewriter import (
    QueryRewriter
)

from app.services.memory_service import (
    MemoryService
)


class ChatContextService:

    def __init__(self):

        self.rewriter = (
            QueryRewriter()
        )

        self.memory = (
            MemoryService()
        )

    def build_query(

        self,

        session_id: str,

        question: str
    ):

        history = (
            self.memory.history(
                session_id
            )
        )

        return self.rewriter.rewrite(
            question,
            history
        )