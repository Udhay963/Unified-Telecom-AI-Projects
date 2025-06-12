import random
import pandas as pd
from datetime import datetime, timedelta

# Generate synthetic IPs
def generate_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

# Create normal and abnormal packet records
def generate_traffic_row(is_anomaly=False):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    src_ip = generate_ip()
    dst_ip = generate_ip()
    protocol = random.choice(["SIP", "RTP", "VoIP", "UDP", "TCP"]) if not is_anomaly else random.choice(["XXX", ""])
    packet_size = random.randint(60, 1500) if not is_anomaly else random.randint(2000, 5000)
    latency_ms = round(random.uniform(10, 100), 2) if not is_anomaly else round(random.uniform(300, 1000), 2)

    return {
        "timestamp": timestamp,
        "src_ip": src_ip,
        "dst_ip": dst_ip,
        "protocol": protocol,
        "packet_size": packet_size,
        "latency_ms": latency_ms,
        "is_anomaly": int(is_anomaly)
    }

# Main function to simulate traffic
def simulate_traffic(n_packets=1000, anomaly_rate=0.05):
    data = []
    n_anomalies = int(n_packets * anomaly_rate)

    for _ in range(n_packets - n_anomalies):
        data.append(generate_traffic_row(False))

    for _ in range(n_anomalies):
        data.append(generate_traffic_row(True))

    random.shuffle(data)
    df = pd.DataFrame(data)
    return df

# Save the generated traffic
if __name__ == "__main__":
    df = simulate_traffic(1000)
    df.to_csv("data/traffic_samples.csv", index=False)
    print("[✓] Generated synthetic telecom traffic in 'data/traffic_samples.csv'")
