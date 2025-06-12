import streamlit as st

st.title("📁 Project Hub - App Launcher")

# Define your 5 app names and URLs
apps = {
    "📡 i-TADS - Telecom Anomaly Detection": "https://telecomitads.streamlit.app/",
    "📶 Internet Speed Tester": "https://your-speedtest-app-url",
    "🔐 File Encryptor & Decryptor": "https://your-file-encryption-app-url",
    "📞 Call Simulation": "https://your-call-sim-app-url",
    "📊 Network Routing Visualizer": "https://your-routing-app-url"
}

# Dropdown for user to choose an app
selected_app = st.selectbox("Choose an App to Launch:", list(apps.keys()))

# Button to open selected app
if st.button("🚀 Open Selected App"):
    st.markdown(f"[👉 Click here to open {selected_app}]({apps[selected_app]})", unsafe_allow_html=True)
