def retrieval_agent(state):

    question = state["question"]

    docs = rag_service.retrieve(question)

    state["retrieved_chunks"] = [
        doc.page_content
        for doc in docs
    ]

    return state