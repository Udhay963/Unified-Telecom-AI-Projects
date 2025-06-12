# components/voip_signaling.py
import time

class SIPSignalingSimulator:
    def __init__(self, caller="UserA", callee="UserB"):
        self.caller = caller
        self.callee = callee
        self.call_state = "IDLE"
        self.call_log = []

    def log(self, message):
        timestamp = time.strftime("%H:%M:%S", time.localtime())
        log_entry = f"[{timestamp}] {message}"
        self.call_log.append(log_entry)

    def start_call(self):
        self.call_state = "CALLING"
        self.log(f"{self.caller} → {self.callee}: INVITE")
        self.log(f"{self.callee} → {self.caller}: 180 RINGING")
        self.log(f"{self.callee} → {self.caller}: 200 OK")
        self.log(f"{self.caller} → {self.callee}: ACK")
        self.call_state = "ESTABLISHED"
        self.log("Call Established - RTP stream started")

    def end_call(self):
        if self.call_state == "ESTABLISHED":
            self.log(f"{self.caller} → {self.callee}: BYE")
            self.log(f"{self.callee} → {self.caller}: 200 OK")
            self.call_state = "IDLE"
            self.log("Call ended")
        else:
            self.log("No active call to end")

    def get_call_log(self):
        return self.call_log
