def analysis_agent(state):

    context = state["context"]

    analysis = f"""
    Analysis:

    Retrieved Context:
    {context}

    Confidence: High
    """

    return {
        "analysis": analysis
    }