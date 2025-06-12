import streamlit as st
import time
import random

class PLMNSimulator:
    def __init__(self, user):
        self.user = user

    def run_simulation(self):
        st.text(f"--- Simulating PLMN for Mobile User: {self.user} ---")
        st.text("[Voice Call] User C initiating voice connection (Circuit Switching)...")
        time.sleep(0.5)
        st.text("[Data Session] User C accessing internet (Packet Switching)...")
        for i in range(1, 6):
            delay = round(random.uniform(0.25, 0.6), 2)
            st.text(f"→ Data packet {i} transmitted (delay: {delay}s)")
            time.sleep(delay)
            if i == 3:
                st.text("[Voice Call] Call in progress...")
        st.text("[Data Session] Browsing session completed.")
        st.text("[Voice Call] Call ended.")
        st.text("[PLMN] Hybrid session completed for User C.")