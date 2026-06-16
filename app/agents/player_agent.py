def player_agent(state):

    chunks = state.get(
        "retrieved_chunks",
        []
    )

    findings = []

    player_keywords = [
        "virat kohli",
        "rohit sharma",
        "ms dhoni",
        "sachin",
        "messi",
        "ronaldo",
        "mbappe",
        "haaland",
        "salah"
    ]

    for chunk in chunks:

        text = chunk.lower()

        for player in player_keywords:

            if player in text:

                findings.append(player)

    state["player_findings"] = list(
        set(findings)
    )

    return state