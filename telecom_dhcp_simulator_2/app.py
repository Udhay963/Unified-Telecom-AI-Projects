import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt
import networkx as nx

from dhcp_server import DHCPServer, ClientDevice
from nat_simulator import NATSimulator
from routing_simulator import RoutingSimulator
from dsl_path_simulator import DSLPathSimulator
from utils import generate_ipv4_pool, generate_ipv6_pool

st.set_page_config(page_title="Telecom Network Visual Simulator", layout="wide")
st.title("📡 Telecom Network Visual Simulator")

tabs = st.tabs(["DHCP Simulation", "Routing Flow", "NAT/PAT", "DSL & ISP Backbone"])

# ────────────────────────────────────────────────
with tabs[0]:
    st.title("📡 DHCP IP Assignment Simulator")

    mode = st.radio("Select Addressing Mode:", ["IPv4", "IPv6"])
    device_count = st.slider("Number of Devices", 1, 20, 5)
    lease_time = st.slider("Lease Time (seconds)", 30, 300, 60)

    if mode == "IPv4":
        ip_pool = generate_ipv4_pool("192.168.1.100", 50)
    else:
        ip_pool = generate_ipv6_pool("2001:db8:abcd", 50)

    server = DHCPServer(ip_pool, lease_time)
    clients = [ClientDevice(f"Device_{i+1}") for i in range(device_count)]

    if st.button("Assign IPs"):
        assigned = []
        for client in clients:
            ip, status = server.assign_ip(client.device_id)
            assigned.append((client.device_id, ip, status))
        
        df = pd.DataFrame(assigned, columns=["Device ID", "Assigned IP", "Status"])
        st.success("IP Assignment Completed")
        st.dataframe(df, use_container_width=True)

        lease_data = []
        for cid, lease in server.leases.items():
            lease_data.append((cid, lease["ip"], lease["expiry"].strftime("%H:%M:%S")))
        lease_df = pd.DataFrame(lease_data, columns=["Client ID", "IP Address", "Lease Expires At"])
        st.subheader("📋 Current Lease Table")
        st.dataframe(lease_df, use_container_width=True)

# ────────────────────────────────────────────────
with tabs[1]:
    st.header("🛰️ Routing Path Visualization")

    sim = RoutingSimulator()
    access_node = st.selectbox("Select Access Node (Client's Entry Point)", [f"Access_{i}" for i in range(1, 6)])

    if st.button("Show Route to Core"):
        path = sim.get_path(access_node)
        st.write(f"📍 Path from {access_node} to Core:", " ➡️ ".join(path))

        graph = sim.get_graph()
        pos = nx.spring_layout(graph, seed=42)
        color_map = []

        for node in graph:
            if node.startswith("Access"):
                color_map.append("lightgreen")
            elif node.startswith("Distribution"):
                color_map.append("skyblue")
            else:
                color_map.append("orange")

        nx.draw(graph, pos, with_labels=True, node_color=color_map, node_size=800, font_size=10)
        nx.draw_networkx_edges(graph, pos, edgelist=[(path[i], path[i+1]) for i in range(len(path)-1)], edge_color="red", width=3)
        
        st.pyplot(plt.gcf())
        plt.clf()

# ────────────────────────────────────────────────
with tabs[2]:
    st.header("🌍 NAT & PAT Simulation")

    nat = NATSimulator("115.99.251.10")  # Simulated public IP
    device_count = st.slider("Private Devices Sending Data", 1, 10, 5)
    private_ips = generate_ipv4_pool("192.168.0.10", device_count)

    if st.button("Translate Private IPs"):
        translation_data = []

        for ip in private_ips:
            private_port = random.randint(3000, 9000)
            public_ip, public_port = nat.translate(ip, private_port)
            translation_data.append((f"{ip}:{private_port}", f"{public_ip}:{public_port}"))

        st.subheader("🔁 NAT Translation Table")
        df = pd.DataFrame(translation_data, columns=["Private Address", "Public Address"])
        st.dataframe(df, use_container_width=True)

# ────────────────────────────────────────────────
with tabs[3]:
    st.header("🔌 DSL + ISP Backbone Simulation")

    dsl_sim = DSLPathSimulator()
    path = dsl_sim.get_path()
    graph = dsl_sim.get_graph()
    pos = nx.spring_layout(graph, seed=42)

    color_map = []
    for node in graph.nodes():
        if "MUX" in node:
            color_map.append("skyblue")
        elif "Gateway" in node:
            color_map.append("orange")
        elif node == "Internet":
            color_map.append("green")
        else:
            color_map.append("lightgray")

    nx.draw(graph, pos, with_labels=True, node_color=color_map, node_size=1200, font_size=10)
    nx.draw_networkx_edges(graph, pos, edgelist=[(path[i], path[i+1]) for i in range(len(path)-1)], edge_color="red", width=3)

    st.pyplot(plt.gcf())
    plt.clf()

    st.markdown("### 🌐 Path Flow:")
    st.write(" ➡️ ".join(path))
