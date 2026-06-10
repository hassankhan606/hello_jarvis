"""modules/voice.py — Text-to-speech + speech-to-text engine."""

import threading

class VoiceEngine:
    def __init__(self):
        self._enabled = True
        self._engine  = None
        self._init_tts()

    def _init_tts(self):
        try:
            import pyttsx3
            self._engine = pyttsx3.init()
            self._engine.setProperty("rate",   165)
            self._engine.setProperty("volume", 0.95)
            # prefer a male British-ish voice if available
            voices = self._engine.getProperty("voices")
            for v in voices:
                if "david" in v.name.lower() or "daniel" in v.name.lower():
                    self._engine.setProperty("voice", v.id)
                    break
        except Exception:
            self._engine = None

    def speak(self, text: str):
        if not self._enabled or not self._engine:
            return
        def _run():
            try:
                self._engine.say(text)
                self._engine.runAndWait()
            except Exception:
                pass
        t = threading.Thread(target=_run, daemon=True)
        t.start()

    def toggle(self) -> bool:
        self._enabled = not self._enabled
        return self._enabled

    # ── optional STT ────────────────────────────────────
    def listen(self) -> str:
        try:
            import speech_recognition as sr
            r  = sr.Recognizer()
            with sr.Microphone() as src:
                r.adjust_for_ambient_noise(src, duration=0.5)
                audio = r.listen(src, timeout=5, phrase_time_limit=8)
            return r.recognize_google(audio)
        except Exception as e:
            return f"[voice error: {e}]"
