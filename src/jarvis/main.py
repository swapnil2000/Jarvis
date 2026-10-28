"""Minimal terminal chat loop against a local Ollama model."""

import os

import ollama
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
    model = os.getenv("JARVIS_MODEL", "llama3.1:8b")
    system = os.getenv(
        "JARVIS_SYSTEM_PROMPT",
        "You are Jarvis, a concise and helpful personal assistant.",
    )

    client = ollama.Client(host=host)
    messages = [{"role": "system", "content": system}]
    print(f"Jarvis ready ({model}). Type 'exit' to quit.")

    while True:
        try:
            user = input("you> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if user.lower() in {"exit", "quit"}:
            break
        if not user:
            continue

        messages.append({"role": "user", "content": user})
        reply = ""
        print("jarvis> ", end="", flush=True)
        for chunk in client.chat(model=model, messages=messages, stream=True):
            piece = chunk["message"]["content"]
            reply += piece
            print(piece, end="", flush=True)
        print()
        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
