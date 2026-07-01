from langgraph.graph import (
    StateGraph
)

from app.graph.state import (
    GraphState
)

from app.graph.nodes.memory_node import (
    memory_node
)

from app.graph.nodes.retrieve_node import (
    retrieve_node
)

from app.graph.nodes.router_node import (
    router_node
)

from app.graph.nodes.answer_node import (
    answer_node
)


def build_graph():

    workflow = (
        StateGraph(
            GraphState
        )
    )

    workflow.add_node(
        "memory",
        memory_node
    )

    workflow.add_node(
        "retrieve",
        retrieve_node
    )

    workflow.add_node(
        "router",
        router_node
    )

    workflow.add_node(
        "answer",
        answer_node
    )

    workflow.set_entry_point(
        "memory"
    )

    workflow.add_edge(
        "memory",
        "retrieve"
    )

    workflow.add_edge(
        "retrieve",
        "router"
    )

    workflow.add_edge(
        "router",
        "answer"
    )

    return workflow.compile()
