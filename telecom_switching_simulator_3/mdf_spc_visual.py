import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st

class MDFSPCVisualizer:
    def __init__(self):
        self.graph = nx.DiGraph()

    def build_network(self):
        self.graph.add_node("MDF", label="Main Distribution Frame")
        self.graph.add_node("SPC", label="SPC Exchange Logic")
        self.graph.add_nodes_from(["Subscriber A", "Subscriber B", "Trunk 1", "Trunk 2"])

        self.graph.add_edges_from([
            ("Subscriber A", "MDF"),
            ("Subscriber B", "MDF"),
            ("MDF", "SPC"),
            ("SPC", "Trunk 1"),
            ("SPC", "Trunk 2"),
            ("Trunk 1", "Subscriber B")
        ])

    def visualize(self):
        pos = nx.spring_layout(self.graph, seed=42)
        labels = {n: n for n in self.graph.nodes()}

        nx.draw(self.graph, pos, with_labels=True, node_color="skyblue", node_size=2000, font_size=10, font_weight='bold', arrows=True)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels={(u, v): " " for u, v in self.graph.edges()}, font_size=8)

        plt.title("MDF ↔ SPC ↔ Switching Network")
        plt.tight_layout()
        fig = plt.gcf()
        st.pyplot(fig)

    def run_visualization(self):
        self.build_network()
        self.visualize()