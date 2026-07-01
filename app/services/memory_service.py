from app.memory.conversation_memory import (
    ConversationMemory
)


class MemoryService:

    def __init__(self):

        self.memory = (
            ConversationMemory()
        )

    def save_user(
        self,
        session_id,
        text
    ):

        self.memory.save_user_message(
            session_id,
            text
        )

    def save_ai(
        self,
        session_id,
        text
    ):

        self.memory.save_ai_message(
            session_id,
            text
        )

    def history(
        self,
        session_id
    ):

        return self.memory.history(
            session_id
        )