from app.providers.gemini_provider import (
    GeminiProvider
)


def answer_agent(state):

    provider = GeminiProvider()

    prompt = f"""
    Context:
    {state['context']}

    Analysis:
    {state['analysis']}

    Question:
    {state['question']}
    """

    answer = provider.generate(
        prompt
    )

    return {
        "answer": answer
    }