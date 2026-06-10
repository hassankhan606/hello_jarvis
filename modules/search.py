"""modules/search.py — Wikipedia summaries + DuckDuckGo instant answers."""

import requests, wikipedia

def wiki_search(query: str) -> str:
    if not query:
        return "Please provide a search term."
    try:
        wikipedia.set_lang("en")
        summary = wikipedia.summary(query, sentences=4, auto_suggest=True)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Ambiguous query. Did you mean: {', '.join(e.options[:5])}?"
    except wikipedia.exceptions.PageError:
        return f"No Wikipedia page found for '{query}'."
    except Exception as e:
        return f"Search error: {e}"

def web_search_ddg(query: str) -> str:
    if not query:
        return "Please provide a search term."
    try:
        url    = "https://api.duckduckgo.com/"
        params = {"q": query, "format": "json", "no_html": 1, "skip_disambig": 1}
        data   = requests.get(url, params=params, timeout=8).json()
        if data.get("AbstractText"):
            return data["AbstractText"]
        if data.get("Answer"):
            return data["Answer"]
        if data.get("RelatedTopics"):
            for t in data["RelatedTopics"]:
                if isinstance(t, dict) and t.get("Text"):
                    return t["Text"]
        return wiki_search(query)
    except Exception as e:
        return f"Web search error: {e}"
