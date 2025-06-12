import streamlit as st
import subprocess
import os

st.set_page_config(page_title="📡 Telecom Project Launcher", layout="wide")

col1, col2 = st.columns(2)
with col2:
    st.image("my_streamlit_app/bsnl-B5FLGLPP.png")
with col1:
    st.image("my_streamlit_app/rttc-logo.png")

st.title("RTTC BSNL HYD INTERNSHIP PROJECT")
st.title("🚀 Unified Telecom + AI Projects")

# List of project names and their launch script paths
project_paths = {
    "🛡️ MAJOR PROJECT(i-TADS)": "i-tads_1",
    "📶 Telecom Network Simulator ": "telecom_dhcp_simulator_2",
    "📞 Telecom Switching Simulator ": "telecom_switching_simulator_3y",
    "🎧 VoIP Simulator": "telecom_network_simulator_5",
    "📟 Call Flow + IMS + PCM Visual Simulator": "telecom_network_simulator_4"

}

# Dropdown for selecting project
selected_project = st.selectbox("Select a project to launch:", list(project_paths.keys()))

# Launch button
if st.button("🔗 Launch Project"):
    script_path = project_paths[selected_project]
    full_command = f"streamlit run {script_path}"
    
    st.success(f"Launching: {selected_project}")
    
    # Launch in a new terminal
    subprocess.Popen(full_command, shell=True)
    
