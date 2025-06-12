import streamlit as st
import time
from components.voip_signaling import SIPSignalingSimulator
from components.rtp_simulator import RTPSimulator

st.title("📞 Real-Time VoIP Call Simulator")

if "sip" not in st.session_state:
    st.session_state.sip = SIPSignalingSimulator()

if "rtp" not in st.session_state:
    st.session_state.rtp = RTPSimulator()

if "call_in_progress" not in st.session_state:
    st.session_state.call_in_progress = False

if "call_log" not in st.session_state:
    st.session_state.call_log = []

if "rtp_packets" not in st.session_state:
    st.session_state.rtp_packets = []

call_log_placeholder = st.empty()
rtp_log_placeholder = st.empty()

import uuid

def display_logs():
    unique_id = str(uuid.uuid4())  # Generate a truly unique ID

    call_log_placeholder.text_area(
        "📋 Call Signaling Log",
        value="\n".join(st.session_state.call_log),
        height=200,
        key=f"call_log_area_{unique_id}"
    )

    rtp_log_placeholder.text_area(
        "📡 RTP Packets Sent",
        value="\n".join(st.session_state.rtp_packets),
        height=200,
        key=f"rtp_log_area_{unique_id}"
    )


def run_call_simulation():
    st.session_state.call_log = []
    st.session_state.rtp_packets = []
    sip = st.session_state.sip
    rtp = st.session_state.rtp

    # Stepwise SIP signaling with delay
    steps = [
        f"{sip.caller} → {sip.callee}: INVITE",
        f"{sip.callee} → {sip.caller}: 180 RINGING",
        f"{sip.callee} → {sip.caller}: 200 OK",
        f"{sip.caller} → {sip.callee}: ACK",
        "Call Established - RTP stream started"
    ]

    st.session_state.call_in_progress = True
    sip.call_state = "CALLING"

    for step in steps:
        timestamp = time.strftime("%H:%M:%S", time.localtime())
        st.session_state.call_log.append(f"[{timestamp}] {step}")
        display_logs()
        time.sleep(1)

    sip.call_state = "ESTABLISHED"

    # RTP streaming packets incrementally
    for i in range(1, rtp.packet_count + 1):
        timestamp = time.strftime("%H:%M:%S", time.localtime())
        packet = f"[{timestamp}] RTP Packet {i} sent from {rtp.caller} to {rtp.callee}"
        st.session_state.rtp_packets.append(packet)
        display_logs()
        time.sleep(0.5)

def run_end_call():
    sip = st.session_state.sip
    st.session_state.call_log.append(f"[{time.strftime('%H:%M:%S')}] {sip.caller} → {sip.callee}: BYE")
    display_logs()
    time.sleep(1)
    st.session_state.call_log.append(f"[{time.strftime('%H:%M:%S')}] {sip.callee} → {sip.caller}: 200 OK")
    display_logs()
    time.sleep(1)
    st.session_state.call_log.append(f"[{time.strftime('%H:%M:%S')}] Call ended")
    st.session_state.call_in_progress = False
    display_logs()

if "call_active" not in st.session_state:
    st.session_state.call_active = False

if not st.session_state.call_active:
    if st.button("Start Call"):
        st.session_state.call_active = True  # Mark call as active
        run_call_simulation()
else:
    st.button("Start Call", disabled=True)

if st.button("End Call"):
    st.session_state.call_active = False  # Reset call state
    run_end_call()


display_logs()
