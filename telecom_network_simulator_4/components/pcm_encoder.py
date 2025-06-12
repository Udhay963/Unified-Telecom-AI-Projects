# File: components/pcm_encoder.py
import wave
import matplotlib.pyplot as plt

class PCMEncoder:
    def encode(self, input_file, output_file="assets/pcm_output.txt", visual_path="assets/pcm_visual.png"):
        print(f"[PCM] Encoding {input_file} to {output_file}")
        with wave.open(input_file, 'rb') as wf:
            frames = wf.readframes(wf.getnframes())
            pcm_data = [format(b, '08b') for b in frames]

        with open(output_file, 'w') as f:
            f.write('\n'.join(pcm_data))

        # Visualization
        plt.figure(figsize=(12, 4))
        plt.plot([int(bits, 2) for bits in pcm_data[:500]])
        plt.title("PCM Bitstream (First 500 samples)")
        plt.xlabel("Sample Index")
        plt.ylabel("8-bit Value")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(visual_path)
        plt.close()

        print(f"[✔] PCM encoded data saved to {output_file}, visual at {visual_path}")