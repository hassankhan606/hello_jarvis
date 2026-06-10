"""modules/translator.py — Translation via MyMemory free API (no key needed)."""

import requests

def translate_text(text: str, target_lang: str = "en") -> str:
    if not text:
        return "Please provide text to translate."
    try:
        url    = "https://api.mymemory.translated.net/get"
        params = {"q": text, "langpair": f"autodetect|{target_lang}"}
        d      = requests.get(url, params=params, timeout=8).json()
        status = d.get("responseStatus", 0)
        if status == 200:
            result    = d["responseData"]["translatedText"]
            matches   = d.get("matches", [])
            src_lang  = matches[0].get("source-lang", "?") if matches else "?"
            return f"[{src_lang} → {target_lang}]  {result}"
        return f"Translation failed: {d.get('responseDetails','unknown error')}"
    except Exception as e:
        return f"Translation error: {e}"
