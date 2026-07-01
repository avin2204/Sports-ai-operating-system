from app.services.chat_context_service import (
    ChatContextService
)


def memory_node(
    state
):

    service = (
        ChatContextService()
    )

    state[
        "rewritten_question"
    ] = service.build_query(

        session_id=
        state["session_id"],

        question=
        state["question"]
    )

    return state
