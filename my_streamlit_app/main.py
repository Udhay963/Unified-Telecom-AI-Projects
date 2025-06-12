import streamlit as st

st.set_page_config(page_title="📡 Telecom Project Launcher", layout="wide")

col1, col2 = st.columns(2)
with col2:
    st.image("bsnl-B5FLGLPP.png")
with col1:
    st.image("rttc-logo.png")

st.title("RTTC BSNL HYD INTERNSHIP PROJECT")
st.title("🚀 Unified Telecom + AI Projects")

# Define your 5 app names and URLs
apps = {
     "🛡️ MAJOR PROJECT(i-TADS)": "https://telecomitads.streamlit.app/" ,
    "📶 Telecom Network Simulator ": "https://telecomntwsimulator.streamlit.app/",
    "📞 Telecom Switching Simulator ": "https://telecomswitchsimulator.streamlit.app/",
    "🎧 VoIP Simulator": "https://telecomvoip.streamlit.app/",
}

# Dropdown for user to choose an app
selected_app = st.selectbox("Choose an App to Launch:", list(apps.keys()))

# Button to open selected app
if st.button("🚀 Open Selected App"):
    st.markdown(f"[👉 Click here to open {selected_app}]({apps[selected_app]})", unsafe_allow_html=True)
