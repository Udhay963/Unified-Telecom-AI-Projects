import streamlit as st
import time
import pandas as pd
from pstn_simulator import PSTNSimulator
from psdn_simulator import PSDNSimulator
from plmn_simulator import PLMNSimulator
from sip_simulator import SIPSimulator
from mdf_spc_visual import MDFSPCVisualizer
from traffic_simulator import TrafficSimulator

# ------------------------------
# App Configuration
# ------------------------------
st.set_page_config(page_title="Telecom Switching Simulator", layout="centered")


# ------------------------------
# Core Telecom Simulation UI
# ------------------------------
def show_simulation_ui():
    st.title("📡 Unified Telecom Switching Network Simulator")
    st.markdown("Simulate telecom technologies learned during BSNL Internship.")

    sim_type = st.selectbox(
        "Choose a Simulation Type",
        ("Select", "PSTN (Circuit Switching)", "PSDN (Packet Switching)", "PLMN (Hybrid)", "SIP (VoIP)", "Visualize MDF + SPC")
    )

    if sim_type == "PSTN (Circuit Switching)":
        if st.button("Start PSTN Simulation"):
            with st.spinner("Running PSTN simulation..."):
                sim = PSTNSimulator("User A", "User B")
                sim.run_simulation()

    elif sim_type == "PSDN (Packet Switching)":
        if st.button("Start PSDN Simulation"):
            with st.spinner("Running PSDN simulation..."):
                sim = PSDNSimulator("Client Browser", "http://bsnl.co.in")
                sim.run_simulation()

    elif sim_type == "PLMN (Hybrid)":
        if st.button("Start PLMN Simulation"):
            with st.spinner("Running PLMN simulation..."):
                sim = PLMNSimulator("User C")
                sim.run_simulation()

    elif sim_type == "SIP (VoIP)":
        if st.button("Start SIP Session"):
            with st.spinner("Running SIP session..."):
                sim = SIPSimulator("VoIP_User_1", "VoIP_User_2")
                sim.run_simulation()

    elif sim_type == "Visualize MDF + SPC":
        if st.button("Show Network Graph"):
            with st.spinner("Rendering network topology..."):
                vis = MDFSPCVisualizer()
                vis.run_visualization()

# ------------------------------
# Interactive Traffic Simulation
# ------------------------------
def show_traffic_dashboard():
    st.title("📊 Interactive Telecom Traffic Dashboard")
    sim = TrafficSimulator()

    choice = st.selectbox("Select Simulation Type:", ["PSTN Call", "PSDN Data", "PLMN Session"])
    run_sim = st.button("Run Simulation")

    placeholder = st.empty()
    col1, col2, col3 = st.columns(3)
    progress = st.progress(0)

    if run_sim:
        sim.events.clear()
        sim.call_count = 0
        sim.packet_count = 0
        sim.call_durations.clear()
        sim.packet_delays.clear()

        sim_func = {
            "PSTN Call": sim.simulate_pstn_call,
            "PSDN Data": sim.simulate_psdn_data,
            "PLMN Session": sim.simulate_plmn_session
        }.get(choice)

        if sim_func:
            sim_func()
            for i, event in enumerate(sim.events):
                placeholder.text(event)
                progress.progress(min((i + 1) / len(sim.events), 1.0))
                time.sleep(0.5)

            col1.metric("Total Calls", sim.call_count)
            col2.metric("Total Packets", sim.packet_count)
            avg_dur = round(sum(sim.call_durations)/len(sim.call_durations), 2) if sim.call_durations else 0
            col3.metric("Avg Call Duration (s)", avg_dur)

            if sim.packet_delays:
                st.subheader("📈 Packet Delay Distribution")
                df = pd.DataFrame(sim.packet_delays, columns=["Delay"])
                st.bar_chart(df)

# ------------------------------
# Sidebar Navigation
# ------------------------------
st.sidebar.title("🔎 Navigation")
page = st.sidebar.radio("Go to", ["Simulation", "Traffic Dashboard"])

if page == "Simulation":
    show_simulation_ui()
elif page == "Traffic Dashboard":
    show_traffic_dashboard()
