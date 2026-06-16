def commentary_agent(state):

    player_data = state.get(
        "player_findings",
        []
    )

    team_data = state.get(
        "team_findings",
        []
    )

    commentary = f"""

Key Players:
{player_data}

Teams:
{team_data}

AI Commentary:
Strong performance indicators detected.
"""

    state["commentary"] = commentary

    return state