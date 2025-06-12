import streamlit as st
import time

class SIPSimulator:
    def __init__(self, caller, callee):
        self.caller = caller
        self.callee = callee

    def run_simulation(self):
        st.text("--- Simulating SIP VoIP Session ---")
        st.text(f"[SIP] {self.caller} → INVITE → {self.callee} via sip.bsnl.co.in")
        time.sleep(0.5)
        st.text("[SIP] Proxy → TRYING → Callee")
        time.sleep(0.5)
        st.text("[SIP] Callee → RINGING → Proxy → Caller")
        time.sleep(0.5)
        st.text("[SIP] Callee → OK → Proxy → Caller")
        time.sleep(0.5)
        st.text("[SIP] Caller → ACK → Callee")
        time.sleep(0.5)
        st.text("[SIP] Session Established. VoIP Call in Progress...")
        time.sleep(1)
        st.text("[SIP] Caller → BYE → Callee")
        time.sleep(0.5)
        st.text("[SIP] Callee → OK → Caller")
        time.sleep(0.5)
        st.text("[SIP] Session Terminated.")