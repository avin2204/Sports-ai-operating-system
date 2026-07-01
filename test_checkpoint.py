from app.graph.workflow import (
    build_graph
)

graph = build_graph()

config = {
    "configurable": {
        "thread_id": "avin"
    }
}

result = graph.invoke(
    {
        "question":
        "Who scored most runs in IPL 2016?"
    },
    config=config
)

print("\nRESULT\n")

print(result)