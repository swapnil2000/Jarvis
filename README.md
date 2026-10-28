# Jarvis

A personal, local-first JARVIS-style assistant for home automation and social media drafting. It runs on my laptop and uses local models through [Ollama](https://ollama.com), so it can work offline.

## Status

Early stage. Software side first, on the laptop. The hardware node (Arduino Nano ESP32 or Raspberry Pi acting as mic/speaker) is on hold until the software works.

## Goals

- Talk to a local LLM from the terminal, then by voice
- Home automation commands (hardware node comes later)
- Draft social media posts
- Run offline wherever possible

## Quick start

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
copy .env.example .env
ollama pull llama3.1:8b
python -m jarvis.main
```

See [docs/SETUP.md](docs/SETUP.md) for the full setup steps and what is still needed.

## Layout

```
src/jarvis/     application code
docs/           setup notes and roadmap
.env.example    configuration template (copy to .env, never commit .env)
```

## Dev machine

i7-14700HX, 16 GB DDR5, 1 TB NVMe, RTX 4070 8 GB. 7-8B parameter models run comfortably on the GPU.

## License

Not chosen yet.
