def router_node(
    state
):

    question = (

        state[
            "rewritten_question"
        ]

        .lower()
    )

    if any(

        word in question

        for word in

        [
            "football",
            "fifa",
            "world cup",
            "premier league"
        ]
    ):

        state[
            "selected_agent"
        ] = "football"

    elif any(

        word in question

        for word in

        [
            "cricket",
            "ipl",
            "odi",
            "t20"
        ]
    ):

        state[
            "selected_agent"
        ] = "cricket"

    else:

        state[
            "selected_agent"
        ] = "rag"

    return state