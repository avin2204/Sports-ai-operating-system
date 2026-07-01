def route_question(state):

    question = state["question"].lower()

    cricket_keywords = [
        "ipl",
        "cricket",
        "virat",
        "dhoni",
        "rohit"
    ]

    for keyword in cricket_keywords:

        if keyword in question:
            return "cricket"

    return "football"