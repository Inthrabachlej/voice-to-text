#!/usr/bin/env python3
import whisper
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import subprocess
import os

print("\n🎤 Press ENTER to start recording...")
input()

fs = 16000
recording = []

def callback(indata, frames, time, status):
    recording.append(indata.copy())

print("🔴 RECORDING... (press ENTER to stop)")

stream = sd.InputStream(samplerate=fs, channels=1, dtype='int16', callback=callback)
stream.start()
input()
stream.stop()
stream.close()
print("✅ Stopped")

audio = np.concatenate(recording, axis=0)
write("/tmp/voice.wav", fs, audio)

print("⏳ Processing...")
model = whisper.load_model("base")
result = model.transcribe("/tmp/voice.wav", language="en", fp16=False)

text = result["text"].strip()
subprocess.run(['xclip', '-selection', 'clipboard'], input=text.encode('utf-8'))

print("\n" + "="*60)
print(text)
print("="*60)
print("\n✅ IN CLIPBOARD - paste with Ctrl+V\n")

os.remove("/tmp/voice.wav")
