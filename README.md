<div align="center">

# 🎧 Real-Time Audio Visualizer

**Live microphone input → FFT analysis → terminal visualization**

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=ffdd54&labelColor=1a1a2e)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-2.4.1-013243?style=flat&logo=numpy&logoColor=white&labelColor=1a1a2e)](https://numpy.org/)
[![SciPy](https://img.shields.io/badge/SciPy-1.15.2-8CAAE6?style=flat&logo=scipy&logoColor=white&labelColor=1a1a2e)](https://scipy.org/)
[![sounddevice](https://img.shields.io/badge/sounddevice-0.5.5-FF6F00?style=flat&labelColor=1a1a2e)](https://python-sounddevice.readthedocs.io/)
[![License](https://img.shields.io/badge/License-GPLv3-2ea44f?style=flat&labelColor=1a1a2e)](#license)

*Turn your microphone into a live, color-coded frequency meter — right in your terminal.*

</div>

---

## ✨ What is this?

Listens to your microphone in real time, runs the audio through an **FFT**,
and prints the result as a volume bar in your terminal.

## 🧠 How it works

1. **`audio.py`** opens a mic input stream and pushes audio chunks into a queue.
2. **`fft.py`** takes each chunk, applies a Hanning window, and runs a Real FFT to get the frequency magnitudes.
3. **`audio_terminal.py`** turns that data into a bar length + color and prints it live.

```mermaid
flowchart LR
    A[Microphone] --> B[audio.py]
    B --> C[fft.py]
    C --> D[Terminal]
```

## 🚀 Quick start

```bash
git clone https://github.com/MiquelEstMo/Audio-Visualizer.git
cd Audio-Visualizer
mise install
pip install -r requirements.txt
python audio_terminal.py
```

Press **Ctrl+C** to stop.

## 🛠️ Structure

```
.
├── audio_terminal.py   # Entry point
├── src/
│   ├── audio.py        # Mic capture
│   └── fft.py          # FFT processing
└── requirements.txt
```

## 📄 License

This project is licensed under the **[GNU General Public License v3.0](LICENSE)**.

<div align="center">

</div>
