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
    "\nFIRST QUESTION\n"
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
    "\nSECOND QUESTION\n"
)

graph.invoke(
    {
        "user_id":
        "avin",

        "question":
        "What is my favorite team?"
    },
    config=config
)