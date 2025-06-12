# File: streamlit_app.py
import streamlit as st
from utils.audio_utils import record_audio, generate_test_wave, plot_waveform
from components.pcm_encoder import PCMEncoder
from components.tdm_multiplexer import TDMMultiplexer
import os
from PIL import Image

st.title("📡 Telecom Network Simulator — PCM + TDM with Visualization")
os.makedirs("assets", exist_ok=True)

if st.button("🎤 Record Mic (UserA)"):
    signal, rate = record_audio("assets/userA.wav", duration=3)
    plot_waveform(signal, rate, "UserA Audio Waveform", "assets/waveform_userA.png")
    st.success("Recorded UserA.wav and waveform plotted")
    st.image("assets/waveform_userA.png")

if st.button("🎼 Generate Test Tone (UserB)"):
    signal, rate = generate_test_wave("assets/userB.wav", freq=880)
    plot_waveform(signal, rate, "UserB Test Tone Waveform", "assets/waveform_userB.png")
    st.success("Generated UserB.wav and waveform plotted")
    st.image("assets/waveform_userB.png")

if st.button("🔄 Encode to PCM"):
    pcm = PCMEncoder()
    pcm.encode("assets/userA.wav", "assets/pcm_userA.txt", "assets/pcm_visual.png")
    pcm.encode("assets/userB.wav", "assets/pcm_userB.txt", "assets/pcm_visual.png")
    st.success("PCM Encoding done")
    st.image("assets/pcm_visual.png")

if st.button("🔀 TDM Multiplex"):
    tdm = TDMMultiplexer()
    tdm.load_user_streams({
        "UserA": "assets/pcm_userA.txt",
        "UserB": "assets/pcm_userB.txt"
    })
    path, visual_path = tdm.multiplex("assets/tdm_output.txt", "assets/tdm_visual.png")
    st.success("TDM stream saved and visualized")
    with open(path) as f:
        data = f.read()
    st.text_area("🧾 TDM Output", data, height=300)
    st.image(visual_path)
