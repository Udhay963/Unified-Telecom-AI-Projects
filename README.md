# Unified-Telecom-AI-Projects

# 📡 i-TADS: Intelligent Telecom Anomaly Detection & Defense System

i-TADS is a real-time project that combines **Telecom**, **AI/ML**, and **Cybersecurity** to detect abnormal network behavior and trigger automated cyber defense actions.

---

## 🚀 Features

- 📈 **Simulates telecom traffic** (SIP, RTP, VoIP)
- 🤖 **AI-based Anomaly Detection** using Isolation Forest
- 🛡️ **Cyber Defense System** to block malicious IPs
- 📊 **Interactive Streamlit Dashboard** to visualize threats
- 🧠 Designed for real-time traffic inspection + alerts

---

## 🛠️ Modules

- `traffic_simulator.py` – Generates synthetic telecom traffic
- `anomaly_detector.py` – Trains Isolation Forest on traffic data
- `cyber_defense.py` – Simulates IP blocking + threat alerts
- `streamlit_app.py` – Front-end UI for uploading & analyzing traffic

---
# 📡 Telecom Network Visual Simulator

A multi-module Streamlit application that visually demonstrates core components of telecom networking — including **DHCP IP assignment**, **Routing**, **NAT/PAT translation**, and **DSL ISP backbone flow**.

## 🔧 Features

- **DHCP Simulation**  
  Dynamically assigns IPv4 or IPv6 addresses to multiple client devices using a simulated DHCP server.

- **Routing Flow Visualization**  
  Shows routing paths from access networks to the core using NetworkX graphs.

- **NAT/PAT Simulation**  
  Translates private IPs to public IPs and ports, simulating Network Address Translation.

- **DSL + ISP Backbone**  
  Illustrates how user data flows from DSL access to the internet through MUX and gateway nodes.

---

## 🚀 Run the App

---

## 🧠 Features

- ✅ PSTN Voice Call Simulation (Circuit Switching)
- ✅ PSDN HTTP Data Transfer Simulation (Packet Switching)
- ✅ PLMN Hybrid Voice+Data Scenario
- ✅ SIP-based VoIP Session Signaling
- ✅ Visual representation of MDF & SPC logic
- ✅ Modular backend simulation + future-ready for real-device networking
- ✅ Ready for integration with real SIP clients and packet monitors

---

## 🚀 Technologies Used

- Python 3
- Streamlit (for UI)
- NetworkX & Matplotlib (for visualizations)
- FSM (for switching flow logic)
- SIP Concepts (INVITE, ACK, BYE flow)
- Scapy/Wireshark (for packet analysis — future work)

---

# 📡 Telecom Network Simulator

> An interactive Streamlit-based telecom project demonstrating PCM, TDM, and VoIP simulation using audio processing and SIP/RTP protocol emulation.

---

## 🚀 Features

- 🎤 **Audio Input**: Record from mic or generate test waveform
- 🔢 **PCM Encoding**: Encode audio to binary (8-bit) format
- ⌛ **TDM Multiplexing**: Simulate multi-user stream interleaving
- 📞 **VoIP Emulation**: SIP signaling + RTP packets with logs
- 📊 **Live Visualizations**: Waveform, PCM stream, and TDM frames

---
