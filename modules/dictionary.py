"""modules/dictionary.py — Word definitions via Free Dictionary API (no key)."""

import requests

def define_word(word: str) -> str:
    word = word.strip().split()[0] if word.strip() else ""
    if not word:
        return "Please provide a word."
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        r   = requests.get(url, timeout=8)
        if r.status_code != 200:
            return f"'{word}' not found in dictionary."
        data    = r.json()[0]
        title   = data.get("word", word)
        phonetic= data.get("phonetic", "")
        lines   = [f"📖 {title}  {phonetic}"]
        for meaning in data.get("meanings", [])[:3]:
            pos   = meaning.get("partOfSpeech", "")
            lines.append(f"\n[{pos}]")
            for defn in meaning.get("definitions", [])[:2]:
                lines.append(f"  • {defn['definition']}")
                if defn.get("example"):
                    lines.append(f'    "{defn["example"]}"')
        return "\n".join(lines)
    except Exception as e:
        return f"Dictionary error: {e}"
