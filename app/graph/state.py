from typing import TypedDict


class GraphState(
    TypedDict
):

    session_id: str

    question: str

    rewritten_question: str

    retrieved_chunks: list[str]

    selected_agent: str

    answer: str