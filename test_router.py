from app.graph.workflow import (
    build_graph
)

graph = build_graph()

print("\n===== CRICKET TEST =====")

result = graph.invoke(
    {
        "question":
        "Who scored most runs in IPL 2016?"
    }
)

print(result)

print("\n===== FOOTBALL TEST =====")

result = graph.invoke(
    {
        "question":
        "Who won FIFA World Cup 2022?"
    }
)

print(result)