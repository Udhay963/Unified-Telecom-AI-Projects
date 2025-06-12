# File: components/rtp_simulator.py
import threading
import time

class RTPSimulator:
    def __init__(self):
        self.running = False

    def start_rtp_stream(self):
        if self.running:
            return

        self.running = True

        def stream():
            for i in range(1, 11):
                if not self.running:
                    break
                time.sleep(0.5)
                msg = f"[RTP] Packet {i} sent from UserA to UserB"
                print(msg)
                if 'call_log' in globals():
                    call_log.append(msg)
                import streamlit as st
                if 'call_log' in st.session_state:
                    st.session_state.call_log.append(msg)

            self.running = False

        threading.Thread(target=stream, daemon=True).start()
