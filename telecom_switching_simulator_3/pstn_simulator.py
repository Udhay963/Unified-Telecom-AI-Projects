import streamlit as st
import time

class PSTNSimulator:
    def __init__(self, caller, callee):
        self.caller = caller
        self.callee = callee

    def run_simulation(self):
        st.text(f"[Establishing] Setting up call from {self.caller} to {self.callee}...")
        st.text("[Establishing] Ringing...")
        time.sleep(0.5)
        st.text(f"[Established] Call accepted by {self.callee}")
        st.text("[Transfer] Voice data being transferred...")
        for i in range(1, 4):
            st.text(f"→ Voice packet {i}")
            time.sleep(0.3)
        st.text(f"[Disconnecting] Terminating call between {self.caller} and {self.callee}...")
        time.sleep(0.5)
        st.text("[Disconnected] Call ended.")