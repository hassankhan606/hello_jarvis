"""modules/github_search.py — Search GitHub repos via public API (no key needed)."""

import requests

def github_search(query: str, limit: int = 5) -> str:
    if not query:
        return "Please provide a search query."
    try:
        url    = "https://api.github.com/search/repositories"
        params = {"q": query, "sort": "stars", "order": "desc", "per_page": limit}
        headers= {"Accept": "application/vnd.github.v3+json"}
        data   = requests.get(url, params=params, headers=headers, timeout=8).json()
        items  = data.get("items", [])
        if not items:
            return f"No GitHub repositories found for '{query}'."
        lines = [f"🐙 Top GitHub results for '{query}':\n"]
        for r in items:
            lines.append(
                f"  ⭐ {r['stargazers_count']:>6,}  "
                f"[{r['language'] or '?':12}]  "
                f"{r['full_name']}\n"
                f"           {r['description'] or 'No description'}\n"
                f"           🔗 {r['html_url']}\n"
            )
        return "\n".join(lines)
    except Exception as e:
        return f"GitHub search error: {e}"
