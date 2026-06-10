"""modules/places.py — Search info about any place via Wikipedia + wttr."""

import wikipedia, requests

def search_place(place: str) -> str:
    if not place:
        return "Please provide a place name."
    try:
        wikipedia.set_lang("en")
        summary = wikipedia.summary(place, sentences=5, auto_suggest=True)
        page    = wikipedia.page(place, auto_suggest=True)
        # bonus: current weather
        try:
            w = requests.get(f"https://wttr.in/{requests.utils.quote(place)}?format=3",
                             timeout=5).text.strip()
        except Exception:
            w = "weather unavailable"
        return f"📍 {page.title}\n\n{summary}\n\n🌤 {w}\n\n🔗 {page.url}"
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Ambiguous: {', '.join(e.options[:5])}"
    except wikipedia.exceptions.PageError:
        return f"No info found for '{place}'."
    except Exception as e:
        return f"Place search error: {e}"
