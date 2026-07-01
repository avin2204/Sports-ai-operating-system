from fastapi import APIRouter

from app.graph.workflows.rag_workflow import (
    build_graph
)

from app.models.chat_message import (
    ChatMessage
)

router = APIRouter(

    prefix="/agent",

    tags=["Agent Chat"]
)

graph = (
    build_graph()
)


@router.post("/chat")
def chat(
    request: ChatMessage
):

    result = graph.invoke(

        {
            "session_id":
            request.session_id,

            "question":
            request.question
        }
    )

    return result