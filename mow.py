#!/usr/bin/env python3
import whisper
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import subprocess
import os

print("\n🎤 Naciśnij ENTER aby zacząć nagrywać...")
input()

fs = 16000
recording = []

def callback(indata, frames, time, status):
    recording.append(indata.copy())

print("🔴 NAGRYWAM... (naciśnij ENTER aby zakończyć)")

stream = sd.InputStream(samplerate=fs, channels=1, dtype='int16', callback=callback)
stream.start()
input()
stream.stop()
stream.close()
print("✅ Zatrzymałem")

audio = np.concatenate(recording, axis=0)
write("/tmp/voice.wav", fs, audio)

print("⏳ Przetwarzam...")
model = whisper.load_model("base")
result = model.transcribe("/tmp/voice.wav", language="pl", fp16=False)

text = result["text"].strip()
subprocess.run(['xclip', '-selection', 'clipboard'], input=text.encode('utf-8'))

print("\n" + "="*60)
print(text)
print("="*60)
print("\n✅ W SCHOWKU - wklej Ctrl+V\n")

os.remove("/tmp/voice.wav")
