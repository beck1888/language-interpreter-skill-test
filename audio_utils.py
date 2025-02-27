from playsound import playsound
import sounddevice as sd
import soundfile as sf
import numpy as np
import librosa
import time
import os

def record_audio(seconds: float, save_as: str = 'mic.mp3') -> None:
    sd.default.device = (0, 1)
    time.sleep(0.5)
    sample_rate: int = 44_100
    
    recording = sd.rec(
        int(seconds * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype=np.float32,
        device=0,
        blocking=True
    )
    
    recording = np.squeeze(recording)
    if recording.max() != 0:
        recording = recording * (32767 / max(abs(recording.max()), abs(recording.min())))
    
    recording = recording.astype(np.int16)
    
    temp_wav = 'temp.wav'
    sf.write(temp_wav, recording, sample_rate)
    
    audio_data, _ = sf.read(temp_wav)
    sf.write(save_as, audio_data, sample_rate, format='MP3')
    
    os.remove(temp_wav)

def play_audio_from_file(file_path: str) -> None:
    playsound(
        sound=file_path,
        block=True
    )

if __name__ == '__main__':
    print("This file is not meant to be ran directly. Please run main.py instead.")
    raise SystemExit(1)
