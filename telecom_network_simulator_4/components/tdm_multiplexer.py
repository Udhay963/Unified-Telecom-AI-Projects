# File: components/tdm_multiplexer.py
import matplotlib.pyplot as plt

class TDMMultiplexer:
    def __init__(self):
        self.user_streams = {}

    def load_user_streams(self, user_pcm_files):
        """
        user_pcm_files: dict like {'UserA': 'assets/pcm_userA.txt', ...}
        """
        for user, file in user_pcm_files.items():
            with open(file, 'r') as f:
                self.user_streams[user] = f.read().splitlines()

    def multiplex(self, output_file="assets/tdm_output.txt", visual_path="assets/tdm_visual.png"):
        tdm_stream = []
        max_length = max(len(stream) for stream in self.user_streams.values())

        for i in range(max_length):
            for user in sorted(self.user_streams.keys()):
                stream = self.user_streams[user]
                if i < len(stream):
                    tdm_stream.append(f"{user}:{stream[i]}")

        with open(output_file, 'w') as f:
            for frame in tdm_stream:
                f.write(frame + '\n')

        print(f"[✔] TDM Multiplexed stream saved to {output_file}")

        # Visualization
        user_labels = list(sorted(self.user_streams.keys()))
        symbols = {label: i for i, label in enumerate(user_labels)}
        signal_labels = [symbols[line.split(":")[0]] for line in tdm_stream[:1000]]
        plt.figure(figsize=(12, 2))
        plt.plot(signal_labels, drawstyle='steps-post')
        plt.yticks(range(len(user_labels)), user_labels)
        plt.title("TDM Stream User Sequence (First 1000 frames)")
        plt.xlabel("Frame Index")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(visual_path)
        plt.close()

        return output_file, visual_path