def transfer_agent(state):

    chunks = state.get(
        "retrieved_chunks",
        []
    )

    findings = []

    transfer_words = [

        "transfer",

        "signed",

        "contract",

        "auction",

        "retained",

        "released"
    ]

    for chunk in chunks:

        text = chunk.lower()

        for word in transfer_words:

            if word in text:

                findings.append(word)

    state["transfer_findings"] = list(
        set(findings)
    )

    return state