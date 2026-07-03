import queue
import sys
import numpy as np
import sounddevice as sd

SAMPLE_RATE = 44100
CHUNK_SIZE = 1024

audio_queue = queue.Queue()

def audio_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    audio_queue.put(indata.copy())

def start_audio_stream():
    stream = sd.InputStream(channels=1, blocksize=CHUNK_SIZE, callback=audio_callback)
    stream.start()
    return stream

def get_audio():
    data = None

    while not audio_queue.empty():
        try:
            data = audio_queue.get_nowait()
        except queue.Empty:
            break

    if data is not None:
        return data
    else:
        return np.zeros((CHUNK_SIZE, 1), dtype=np.float32)
