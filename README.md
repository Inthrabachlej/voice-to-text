# voice-to-text

Local voice-to-text workflow tools for transcription and clipboard output. Offline, privacy-first, supports Polish and English.

## Features
- 🎤 Press-to-talk interface (Enter to start/stop)
- 📋 Auto-copy to clipboard
- 🔒 100% offline (privacy-first)
- 🇵🇱 Polish support (mow.py)
- 🇬🇧 English support (speak.py)

## Installation
```bash
# Install dependencies
pip install openai-whisper sounddevice scipy --break-system-packages
sudo apt install xclip portaudio19-dev python3-pyaudio -y

# Clone repository
git clone https://github.com/Inthrabachlej/voice-to-text.git
cd voice-to-text

# Make executable
chmod +x mow.py speak.py

# Optional: Add aliases to ~/.bashrc
echo "alias mow='python3 \"$HOME/Projects/voice-to-text/mow.py\"'" >> ~/.bashrc
echo "alias speak='python3 \"$HOME/Projects/voice-to-text/speak.py\"'" >> ~/.bashrc
source ~/.bashrc
```

## Usage

**Polish:**
```bash
python3 mow.py
# or with alias: mow
```

**English:**
```bash
python3 speak.py
# or with alias: speak
```

## How it works
1. Press Enter to start recording
2. Speak
3. Press Enter to stop
4. Text automatically in clipboard (Ctrl+V to paste)

## Requirements
- Linux (tested on Linux Mint)
- Python 3.12+
- Microphone
- ~150MB disk space (for Whisper model)

## Model
Uses Whisper `base` model - good balance between speed and accuracy on CPU.

## License
MIT
