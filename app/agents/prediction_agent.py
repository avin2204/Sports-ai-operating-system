def prediction_agent(state):

    player_score = len(
        state.get(
            "player_findings",
            []
        )
    )

    team_score = len(
        state.get(
            "team_findings",
            []
        )
    )

    confidence = min(
        (
            player_score * 10
            +
            team_score * 10
        ),
        100
    )

    state["prediction_result"] = {

        "confidence": confidence,

        "prediction":

        "Evidence available for analysis"
    }

    return state