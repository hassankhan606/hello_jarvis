"""modules/jokes.py — Programming & dad jokes via pyjokes + official joke API."""

import requests, random

def tell_joke() -> str:
    # try official joke API first
    try:
        r = requests.get("https://official-joke-api.appspot.com/random_joke", timeout=5)
        d = r.json()
        return f"{d['setup']} ... {d['punchline']}"
    except Exception:
        pass
    # fallback: pyjokes
    try:
        import pyjokes
        return pyjokes.get_joke()
    except Exception:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"
