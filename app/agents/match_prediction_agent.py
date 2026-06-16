def match_prediction_agent(state):

    confidence = state.get(
        "prediction_result",
        {}
    ).get(
        "confidence",
        50
    )

    if confidence > 70:

        result = "High confidence"

    elif confidence > 50:

        result = "Moderate confidence"

    else:

        result = "Low confidence"

    state["match_prediction"] = result

    return state