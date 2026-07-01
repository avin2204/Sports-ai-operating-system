from app.graph.workflow import (
    build_graph
)

graph = build_graph()

result = graph.invoke(
    {
        "question":
        "Who scored most runs in IPL 2016?"
    }
)

print("\nANSWER:\n")

print(
    result["answer"]
)