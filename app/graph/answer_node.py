from app.providers.gemini_provider import (
    GeminiProvider
)


def answer_node(
    state
):

    llm = (
        GeminiProvider()
    )

    context = "\n".join(

        state[
            "retrieved_chunks"
        ]
    )

    prompt = f"""
Context:
{context}

Question:
{state['question']}

Answer:
"""

    state[
        "answer"
    ] = llm.generate(
        prompt
    )

    return state
