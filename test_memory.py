# test_memory.py

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
        "My favorite team is Arsenal"
    },
    config=config
)

print("\nMEMORY HISTORY\n")

for state in graph.get_state_history(
    config
):
    print(state.values)