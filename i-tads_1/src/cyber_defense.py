class CyberDefense:
    def __init__(self):
        self.blocklist = set()
        self.alerts = []

    def block_ip(self, ip):
        if ip not in self.blocklist:
            self.blocklist.add(ip)
            alert = f"[ALERT] Blocked suspicious IP: {ip}"
            self.alerts.append(alert)
            print(alert)

    def analyze_traffic(self, df):
        anomalies = df[df["predicted_anomaly"] == 1]
        for ip in anomalies["src_ip"].unique():
            self.block_ip(ip)

    def get_alerts(self):
        return self.alerts

    def get_blocklist(self):
        return list(self.blocklist)
