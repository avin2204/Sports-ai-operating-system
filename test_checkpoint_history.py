from app.graph.workflow import (
    build_graph
)

graph = build_graph()

config = {
    "configurable": {
        "thread_id": "avin"
    }
}

graph.invoke(
    {
        "question":
        "Who scored most runs in IPL 2016?"
    },
    config=config
)

print("\nCHECKPOINTS\n")

for state in graph.get_state_history(
    config
):
    print(state)