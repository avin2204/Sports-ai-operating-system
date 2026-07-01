from app.services.retrieval_service import (
    RetrievalService
)


def retrieve_node(
    state
):

    retrieval = (
        RetrievalService()
    )

    state[
        "retrieved_chunks"
    ] = retrieval.retrieve(

        state[
            "rewritten_question"
        ]
    )

    return state