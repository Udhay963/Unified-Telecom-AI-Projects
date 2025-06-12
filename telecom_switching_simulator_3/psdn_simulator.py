import streamlit as st
import time
import random

class PSDNSimulator:
    def __init__(self, client, server_url):
        self.client = client
        self.server_url = server_url

    def run_simulation(self):
        st.text(f"[HTTP Request] Client {self.client} sending GET request to {self.server_url}...")
        st.text("[Packet Switching] Breaking data into packets...")
        for i in range(1, 6):
            delay = round(random.uniform(0.25, 0.6), 2)
            st.text(f"→ Packet {i} sent (delay: {delay}s)")
            time.sleep(delay)
        st.text("[Complete] All packets received at server.")