# components/rtp_simulator.py
import time

class RTPSimulator:
    def __init__(self, caller="UserA", callee="UserB", packet_count=10):
        self.caller = caller
        self.callee = callee
        self.packet_count = packet_count
        self.packets_sent = []

    def generate_packet(self, i):
        timestamp = time.strftime("%H:%M:%S", time.localtime())
        return f"[{timestamp}] RTP Packet {i} sent from {self.caller} to {self.callee}"

    def generate_packets(self):
        self.packets_sent = []
        for i in range(1, self.packet_count + 1):
            self.packets_sent.append(self.generate_packet(i))

    def get_packets(self):
        return self.packets_sent
