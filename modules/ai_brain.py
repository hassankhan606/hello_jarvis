"""modules/ai_brain.py — AI question answering.

Priority chain:
  1. OpenAI GPT-4o-mini  (if OPENAI_API_KEY env var is set — free $5 credit on new accounts)
  2. Ollama local model   (if running locally)
  3. DuckDuckGo instant + Wikipedia fallback (always free, no key)
"""

import os, requests

OPENAI_KEY = os.getenv("OPENAI_API_KEY", "")
OLLAMA_URL = "http://localhost:11434/api/generate"

class AIBrain:
    def ask(self, question: str) -> str:
        if not question:
            return "Please ask a question."

        # ── 1. OpenAI ───────────────────────────────────
        if OPENAI_KEY:
            try:
                import openai
                openai.api_key = OPENAI_KEY
                resp = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system",
                         "content": "You are JARVIS, a helpful AI assistant. Be concise but insightful."},
                        {"role": "user", "content": question}
                    ],
                    max_tokens=300,
                )
                return resp.choices[0].message.content.strip()
            except Exception as e:
                pass  # fall through

        # ── 2. Ollama (local LLM) ────────────────────────
        try:
            payload = {"model": "llama3", "prompt": question, "stream": False}
            r       = requests.post(OLLAMA_URL, json=payload, timeout=30)
            if r.status_code == 200:
                return r.json().get("response", "").strip()
        except Exception:
            pass

        # ── 3. Free fallback: DDG + Wikipedia ───────────
        try:
            from modules.search import web_search_ddg
            return web_search_ddg(question)
        except Exception as e:
            return (f"AI brain unavailable. Set OPENAI_API_KEY or install Ollama. "
                    f"({e})")
