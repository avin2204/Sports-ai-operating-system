def injury_agent(state):

    chunks = state.get(
        "retrieved_chunks",
        []
    )

    injuries = []

    keywords = [

        "injury",
        "hamstring",
        "ankle",
        "knee",
        "shoulder",
        "fracture",
        "out injured"
    ]

    for chunk in chunks:

        text = chunk.lower()

        for keyword in keywords:

            if keyword in text:

                injuries.append(keyword)

    state["injury_findings"] = list(
        set(injuries)
    )

    return state