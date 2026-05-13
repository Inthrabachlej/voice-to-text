# voice-to-text — Runbook

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
sudo apt install ffmpeg
```

## Uruchomienie

```bash
# Nagrywanie i transkrypcja (Polski + Angielski)
source .venv/bin/activate
python speak.py

# Alias systemowy (jeśli skonfigurowany)
mow
```

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Brak mikrofonu | sprawdź `arecord -l` |
| `whisper` błąd | `pip install openai-whisper` |
| `ffmpeg not found` | `sudo apt install ffmpeg` |
