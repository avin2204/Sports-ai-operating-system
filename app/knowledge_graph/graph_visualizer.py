import networkx as nx


class GraphVisualizer:

    def build(self):

        graph = nx.Graph()

        graph.add_edge(
            "Virat Kohli",
            "RCB"
        )

        graph.add_edge(
            "RCB",
            "IPL"
        )

        graph.add_edge(
            "Messi",
            "Inter Miami"
        )

        graph.add_edge(
            "Inter Miami",
            "MLS"
        )

        return graph