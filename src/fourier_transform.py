import numpy as np
from scipy.fft import rfft, fftfreq

def process_audio(audio, sample_rate):

    if len(audio.shape) > 1:
        np.mean(audio, axis=1)

    chunk_size = len(audio)
    audio_transform = rfft(audio)

    magnitude = np.abs(audio_transform) # type: ignore
    frequencies = fftfreq(chunk_size, d = 1.0/sample_rate)

    return magnitude, frequencies
