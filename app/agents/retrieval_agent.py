def retrieval_agent(state):

    question = state.get(
        "rewritten_question",
        state["question"]
    )

    docs = rag_service.retrieve(
        question
    )

    context = "\n".join(
        [
            doc.payload["text"]
            for doc in docs
        ]
    )

    return {
        "context": context
    }