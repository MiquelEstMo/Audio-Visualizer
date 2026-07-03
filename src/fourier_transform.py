import numpy as np
from scipy.fft import rfft, fftfreq

def process_audio(audio, sample_rate):
    if len(audio.Shape):
        np.mean(audio, axis=1)

    audio_transform = rfft(audio)

    magnitude = np.abs(audio_transform) # type: ignore
    frequencies = fftfreq(audio_transform, d = 1.0/sample_rate)

    return magnitude, frequencies
