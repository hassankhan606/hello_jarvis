"""modules/person.py — Search info about any person via Wikipedia."""

import wikipedia

def search_person(name: str) -> str:
    if not name:
        return "Please provide a person's name."
    try:
        wikipedia.set_lang("en")
        page    = wikipedia.page(name, auto_suggest=True)
        summary = wikipedia.summary(name, sentences=5)
        return f"📌 {page.title}\n\n{summary}\n\n🔗 {page.url}"
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple matches found: {', '.join(e.options[:6])}. Be more specific."
    except wikipedia.exceptions.PageError:
        return f"Could not find information about '{name}'."
    except Exception as e:
        return f"Person search error: {e}"
