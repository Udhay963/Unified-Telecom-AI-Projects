import networkx as nx

class RoutingSimulator:
    def __init__(self):
        self.graph = nx.Graph()
        # Add nodes
        access_nodes = [f"Access_{i}" for i in range(1, 6)]
        dist_nodes = [f"Distribution_{i}" for i in range(1, 4)]
        core_node = "Core"

        self.graph.add_nodes_from(access_nodes + dist_nodes + [core_node])

        # Add edges Access -> Distribution
        for i, access in enumerate(access_nodes):
            dist = dist_nodes[i // 2]  # Each dist node connects 2 access nodes approx
            self.graph.add_edge(access, dist)

        # Add edges Distribution -> Core
        for dist in dist_nodes:
            self.graph.add_edge(dist, core_node)

    def get_path(self, start_node):
        return nx.shortest_path(self.graph, start_node, "Core")

    def get_graph(self):
        return self.graph
