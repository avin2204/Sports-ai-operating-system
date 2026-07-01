from app.graph.workflow import (
    build_graph
)

graph = build_graph()

config = {
    "configurable": {
        "thread_id": "avin"
    }
}

print(
    "\nSAVE MEMORY\n"
)

graph.invoke(
    {
        "user_id":
        "avin",

        "question":
        "My favorite team is Arsenal"
    },
    config=config
)

print(
    "\nTEST MEMORY QUERY\n"
)

result = graph.invoke(
    {
        "user_id":
        "avin",

        "question":
        "How did they perform?"
    },
    config=config
)

print(
    "\nFINAL STATE\n"
)

print(result)