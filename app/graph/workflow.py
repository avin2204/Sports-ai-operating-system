from langgraph.graph import (
    StateGraph,
    START,
    END
)

from langgraph.checkpoint.memory import (
    InMemorySaver
)

from app.graph.state import SportsState

from app.agents.supervisor_agent import (
    supervisor_agent
)

from app.agents.router_agent import (
    router_agent
)

from app.agents.cricket_agent import (
    cricket_agent
)

from app.agents.football_agent import (
    football_agent
)

from app.agents.analysis_agent import (
    analysis_agent
)

from app.agents.answer_agent import (
    answer_agent
)

from app.agents.router_logic import (
    route_question
)
from app.agents.memory_agent import (
    memory_agent
)

from app.agents.query_rewriter_agent import (
    query_rewriter_agent
)


def build_graph():

    graph = StateGraph(
        SportsState
    )

    graph.add_node(
        "supervisor",
        supervisor_agent
    )

    graph.add_node(
        "router",
        router_agent
    )

    graph.add_node(
        "cricket",
        cricket_agent
    )

    graph.add_node(
        "football",
        football_agent
    )

    graph.add_node(
        "analyze",
        analysis_agent
    )

    graph.add_node(
        "answer",
        answer_agent
    )

    graph.add_node(
        "memory",
        memory_agent
    )

    graph.add_node(
        "rewriter",
        query_rewriter_agent
    )
    graph.add_edge(
        START,
        "memory"
    )

    graph.add_edge(
        "memory",
        "rewriter"
    )

    graph.add_edge(
    "rewriter",
    "supervisor"
    )

    graph.add_edge(
        "supervisor",
        "router"
    )

    graph.add_conditional_edges(
        "router",
        route_question,
        {
            "cricket": "cricket",
            "football": "football"
        }
    )

    graph.add_edge(
        "cricket",
        "analyze"
    )

    graph.add_edge(
        "football",
        "analyze"
    )

    graph.add_edge(
        "analyze",
        "answer"
    )

    graph.add_edge(
        "answer",
        END
    )

    memory = InMemorySaver()

    return graph.compile(
        checkpointer=memory
    )