def fantasy_team_agent(state):

    players = state.get(
        "player_findings",
        []
    )

    selected = players[:11]

    state["fantasy_team"] = selected

    return state