import re


def statistics_agent(state):

    chunks = state.get(
        "retrieved_chunks",
        []
    )

    goals = 0
    wickets = 0
    runs = 0

    for chunk in chunks:

        goals += len(
            re.findall(
                r"\bgoal\b",
                chunk.lower()
            )
        )

        wickets += len(
            re.findall(
                r"\bwicket\b",
                chunk.lower()
            )
        )

        runs += len(
            re.findall(
                r"\bruns\b",
                chunk.lower()
            )
        )

    state["statistics_findings"] = {

        "goals": goals,
        "wickets": wickets,
        "runs": runs
    }

    return state