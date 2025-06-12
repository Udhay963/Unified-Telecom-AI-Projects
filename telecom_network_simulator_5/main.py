# main.py
from components.voip_signaling import SIPSignalingSimulator
from components.rtp_simulator import RTPSimulator

if __name__ == "__main__":
    sip = SIPSignalingSimulator()
    rtp = RTPSimulator()

    sip.start_call()
    if sip.call_state == "ESTABLISHED":
        rtp.start_stream()
    sip.end_call()

    print("\n--- Call Log ---")
    for log in sip.get_call_log():
        print(log)

    print("\n--- RTP Packets Sent ---")
    for packet in rtp.get_packets():
        print(packet)
