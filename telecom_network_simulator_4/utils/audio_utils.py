# File: utils/audio_utils.py
import numpy as np
import wave
import sounddevice as sd
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import os

def generate_test_wave(filename="assets/sample_audio.wav", duration=2, freq=440, rate=8000):
    t = np.linspace(0, duration, int(rate * duration), endpoint=False)
    signal = (np.sin(2 * np.pi * freq * t) * 32767).astype(np.int16)

    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        wf.writeframes(signal.tobytes())

    print(f"[✔] Dummy audio generated at {filename}")
    return signal, rate

def record_audio(filename="assets/userA.wav", duration=3, rate=8000):
    print("[🎤] Recording from mic...")
    recording = sd.rec(int(duration * rate), samplerate=rate, channels=1, dtype='int16')
    sd.wait()
    write(filename, rate, recording)
    print(f"[✔] Recording saved to {filename}")
    return recording.flatten(), rate

def plot_waveform(signal, rate, title, save_path):
    plt.figure(figsize=(10, 3))
    t = np.linspace(0, len(signal) / rate, num=len(signal))
    plt.plot(t, signal)
    plt.title(title)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()
