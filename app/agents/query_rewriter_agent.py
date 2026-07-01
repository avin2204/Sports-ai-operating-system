def query_rewriter_agent(state):

    question = state["question"]

    memory = state.get(
        "memory",
        {}
    )

    rewritten = question

    favorite_team = memory.get(
        "favorite_team"
    )

    if (
        favorite_team
        and "they" in question.lower()
    ):

        rewritten = question.replace(
            "they",
            favorite_team
        )

        print(
            f"\nQUERY REWRITTEN:"
            f"\n{rewritten}"
        )

    return {
        "rewritten_question":
        rewritten
    }