from app.memory.redis_memory import (
    RedisMemory
)


class ConversationMemory:

    def __init__(self):

        self.memory = (
            RedisMemory()
        )

    def save_user_message(
        self,
        session_id,
        message
    ):

        self.memory.save(
            session_id,
            "user",
            message
        )

    def save_ai_message(
        self,
        session_id,
        message
    ):

        self.memory.save(
            session_id,
            "assistant",
            message
        )

    def history(
        self,
        session_id
    ):

        return self.memory.get_history(
            session_id
        )