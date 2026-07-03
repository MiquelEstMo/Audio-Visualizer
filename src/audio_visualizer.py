import time
import numpy as np
import audio_recorder as audio
import fourier_transform as fft

stream = audio.start_audio_stream()

def visualizer():
    try:
        while True:

            data = audio.get_audio()
            data_amplitude, _ = fft.process_audio(data, audio.SAMPLE_RATE)

            volumen = np.mean(data_amplitude[:50]) * 100
            length = int(min(volumen, 50))

            audio_bar = "█" * length

            print(f"Volum: {audio_bar:<50}", end="\r")


    except KeyboardInterrupt:
        print(" Bye!")
        stream.stop()
        stream.close()


if __name__ == "__main__":
    visualizer()
