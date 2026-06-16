from typing import Dict


def supervisor_agent(state: Dict):

    question = state["question"].lower()

    execution_plan = []

    execution_plan.append("retrieval")

    if any(word in question for word in [
        "log",
        "error",
        "failure",
        "crash"
    ]):
        execution_plan.append("log_analysis")

    if any(word in question for word in [
        "nexus",
        "switch",
        "linecard",
        "fabric",
        "module"
    ]):
        execution_plan.append("hardware")

    if any(word in question for word in [
        "github",
        "commit",
        "pr",
        "bug"
    ]):
        execution_plan.append("github")

    state["execution_plan"] = execution_plan

    return state