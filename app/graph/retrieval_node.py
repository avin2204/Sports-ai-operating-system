from app.rag.rag_service import RAGService


def retrieval_node(state):

    rag = RAGService()

    context = rag.retrieve(
        state["question"]
    )

    return {
        "context": context
    }