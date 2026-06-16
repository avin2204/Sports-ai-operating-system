def team_agent(state):

    chunks = state.get(
        "retrieved_chunks",
        []
    )

    findings = []

    teams = [

        "india",
        "australia",
        "england",
        "pakistan",

        "rcb",
        "csk",
        "mi",

        "real madrid",
        "barcelona",
        "arsenal",
        "liverpool",
        "manchester city"
    ]

    for chunk in chunks:

        text = chunk.lower()

        for team in teams:

            if team in text:

                findings.append(team)

    state["team_findings"] = list(
        set(findings)
    )

    return state