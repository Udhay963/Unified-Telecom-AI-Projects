# Unified Telecom Switching Network Simulator

This project simulates various telecom switching technologies learned during a 2-week offline internship at BSNL RTTC.  
Built using Python, Streamlit, NetworkX, and Matplotlib.

## Features

- PSTN Circuit Switching simulation
- PSDN Packet Switching simulation (HTTP data transfer)
- PLMN Hybrid voice + data simulation
- SIP-based VoIP call simulation
- Visualization of MDF and SPC switching network graphs
- Unified Streamlit UI dashboard for interactive simulations

## How to Run

1. Install dependencies:
   ```
   pip install streamlit networkx matplotlib
   ```

2. Run the Streamlit app:
   ```
   streamlit run streamlit_app.py
   ```

3. Select the simulation type and click the button to start.

## Project Structure

```
telecom_switching_simulator/
├── __init__.py
├── pstn_simulator.py
├── psdn_simulator.py
├── plmn_simulator.py
├── sip_simulator.py
├── mdf_spc_visual.py
└── streamlit_app.py
```

---

**Author:** BSNL Internship Project - YERRA UDHAY (CSE AIML Student)