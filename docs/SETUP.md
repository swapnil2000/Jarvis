# Setup and open items

## Steps on the laptop

1. Install Python 3.11+ and Git.
2. Install Ollama from https://ollama.com and confirm `ollama --version` works.
3. Pull a model: `ollama pull llama3.1:8b` (fits in 8 GB VRAM).
4. Create a virtual environment and install dependencies (see README quick start).
5. Copy `.env.example` to `.env` and adjust the model if needed.
6. Run `python -m jarvis.main` from the project root with `src` on the path
   (e.g. `set PYTHONPATH=src` on Windows).

## Planned next

| Stage | Item | Needs |
|-------|------|-------|
| 1 | Terminal chat with local model | Done (skeleton) |
| 2 | Speech to text | Choose engine (e.g. faster-whisper) |
| 3 | Text to speech | Choose engine (e.g. Piper) |
| 4 | Social media post drafting | Decide platforms and tone examples |
| 5 | Home automation | List of devices and protocol (MQTT, Home Assistant, etc.) |
| 6 | Hardware node | Arduino Nano ESP32 or Raspberry Pi; on hold |

## Needed from me

- Which devices to automate first
- Which social platforms to draft for, plus a few sample posts for tone
- Wake word or push-to-talk preference
- Decision on Home Assistant vs direct integrations
