import time
import random

class TrafficSimulator:
    def __init__(self):
        self.events = []
        self.call_count = 0
        self.packet_count = 0
        self.call_durations = []
        self.packet_delays = []

    def simulate_pstn_call(self):
        self.call_count += 1
        duration = random.uniform(3, 6)  # seconds
        self.call_durations.append(duration)
        self.events.append("[Establishing] Setting up call from User A to User B...")
        time.sleep(1)
        self.events.append("[Establishing] Ringing...")
        time.sleep(1)
        self.events.append("[Established] Call accepted by User B")
        time.sleep(duration / 3)
        self.events.append("[Transfer] Voice data being transferred...")
        for i in range(1, 4):
            self.packet_count += 1
            self.packet_delays.append(random.uniform(0.2, 0.6))
            self.events.append(f"→ Voice packet {i}")
            time.sleep(0.5)
        self.events.append("[Disconnecting] Terminating call between User A and User B...")
        time.sleep(1)
        self.events.append("[Disconnected] Call ended.")

    def simulate_psdn_data(self):
        self.events.append("[HTTP Request] Client Browser sending GET request to http://bsnl.co.in...")
        time.sleep(1)
        self.events.append("[Packet Switching] Breaking data into packets...")
        for i in range(1, 6):
            self.packet_count += 1
            delay = round(random.uniform(0.25, 0.6), 2)
            self.packet_delays.append(delay)
            self.events.append(f"→ Packet {i} sent (delay: {delay}s)")
            time.sleep(0.5)
        self.events.append("[Complete] All packets received at server.")

    def simulate_plmn_session(self):
        self.call_count += 1
        duration = random.uniform(4, 8)
        self.call_durations.append(duration)
        self.events.append("--- Simulating PLMN for Mobile User: User C ---")
        self.events.append("[Voice Call] User C initiating voice connection (Circuit Switching)...")
        time.sleep(1)
        self.events.append("[Data Session] User C accessing internet (Packet Switching)...")
        time.sleep(1)
        for i in range(1, 6):
            if i % 2 == 0:
                self.packet_count += 1
                delay = round(random.uniform(0.25,0.6), 2)
                self.packet_delays.append(delay)
                self.events.append(f"→ Data packet {i} transmitted (delay: {delay}s)")
            else:
                self.packet_count += 1
                self.packet_delays.append(random.uniform(0.2, 0.5))
                self.events.append(f"→ Voice packet {i // 2 + 1}")
            time.sleep(0.5)
        self.events.append("[Data Session] Browsing session completed.")
        self.events.append("[Voice Call] Call ended.")
        self.events.append("[PLMN] Hybrid session completed for User C.")
