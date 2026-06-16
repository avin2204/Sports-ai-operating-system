def scouting_agent(state):

    chunks = state.get(
        "retrieved_chunks",
        []
    )

    scouting_notes = []

    skills = [

        "finishing",

        "pace",

        "passing",

        "dribbling",

        "batting",

        "bowling",

        "fielding"
    ]

    for chunk in chunks:

        text = chunk.lower()

        for skill in skills:

            if skill in text:

                scouting_notes.append(skill)

    state["scouting_findings"] = list(
        set(scouting_notes)
    )

    return state