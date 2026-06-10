"""modules/movies.py — Movie details via OMDb free API.

Free key: https://www.omdbapi.com/apikey.aspx  (1,000 req/day free)
Set OMDB_API_KEY env var or replace below.
"""

import os, requests

OMDB_KEY = os.getenv("OMDB_API_KEY", "trilogy")   # 'trilogy' is a demo key

def search_movie(title: str) -> str:
    if not title:
        return "Please provide a movie title."
    try:
        url  = "http://www.omdbapi.com/"
        params = {"t": title, "apikey": OMDB_KEY, "plot": "short"}
        d    = requests.get(url, params=params, timeout=8).json()
        if d.get("Response") == "False":
            return f"Movie '{title}' not found. {d.get('Error','')}"
        lines = [
            f"🎬 {d.get('Title')} ({d.get('Year')})",
            f"⭐ IMDb: {d.get('imdbRating')}  |  {d.get('Genre')}",
            f"🎭 {d.get('Actors')}",
            f"🌍 {d.get('Country')}  •  {d.get('Runtime')}",
            f"📝 {d.get('Plot')}",
            f"🏆 {d.get('Awards','No awards info')}",
        ]
        return "\n".join(lines)
    except Exception as e:
        return f"Movie search error: {e}"
