def review_agent(state):

    evidence = "\n".join(
        state.get(
            "retrieved_chunks",
            []
        )
    )

    root_cause = state.get(
        "root_cause",
        ""
    )

    issues = []

    if len(evidence) < 50:
        issues.append(
            "Insufficient evidence"
        )

    if len(root_cause) < 50:
        issues.append(
            "Weak RCA"
        )

    state["review_notes"] = issues

    state["review_passed"] = (
        len(issues) == 0
    )

    return state