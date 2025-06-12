import networkx as nx

class DSLPathSimulator:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.create_pipeline()

    def create_pipeline(self):
        self.graph.add_node("Device", layer="Access")
        self.graph.add_node("DSL Modem", layer="Access")
        self.graph.add_node("DSLAM", layer="Access")
        self.graph.add_node("Primary MUX", layer="Distribution")
        self.graph.add_node("Secondary MUX", layer="Distribution")
        self.graph.add_node("Gateway Router", layer="Core")
        self.graph.add_node("Internet", layer="Cloud")

        self.graph.add_edges_from([
            ("Device", "DSL Modem"),
            ("DSL Modem", "DSLAM"),
            ("DSLAM", "Primary MUX"),
            ("Primary MUX", "Secondary MUX"),
            ("Secondary MUX", "Gateway Router"),
            ("Gateway Router", "Internet")
        ])

    def get_graph(self):
        return self.graph

    def get_path(self):
        return ["Device", "DSL Modem", "DSLAM", "Primary MUX", "Secondary MUX", "Gateway Router", "Internet"]
