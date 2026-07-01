from pydantic import (
    BaseModel
)


class ChatMessage(
    BaseModel
):

    session_id: str

    question: str
    