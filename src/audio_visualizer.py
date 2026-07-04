import time
import numpy as np
import audio_recorder as audio
import fourier_transform as fft




def visualizer():

    try:
        print("🎙️ Initializing microphone stream...\n")
        stream = audio.start_audio_stream()
    except:
        print("[ERROR!]: Coud not initialize microphone")
        exit()

    try:
        while True:

            data = audio.get_audio()
            data_amplitude, _ = fft.process_audio(data, audio.SAMPLE_RATE)


            volumen = np.mean(data_amplitude[:100]) * 10
            length = int(min(volumen, 50))

            audio_bar = "█" * length

            if length < 30:
                color = "\033[92m"
            elif length < 45:
                color = "\033[93m"
            else:
                color = "\033[91m"

            reset = "\033[0m"

            print(f"Volum: {color}{audio_bar:50}{reset}", end="\r")
            time.sleep(0.05)


    except KeyboardInterrupt:
        print("\nShutting down the audio system safely...")
        stream.stop()
        stream.close()
        print("Bye!!!")


if __name__ == "__main__":
    visualizer()
