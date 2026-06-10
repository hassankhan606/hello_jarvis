"""modules/news.py — Live news via GNews.io free tier & RSS fallback."""

import requests, html, re

GNEWS_KEY = "YOUR_GNEWS_API_KEY"   # free at https://gnews.io  (10 req/hr free)
RSS_FEEDS  = {
    "world":       "https://feeds.bbci.co.uk/news/world/rss.xml",
    "technology":  "https://feeds.bbci.co.uk/news/technology/rss.xml",
    "science":     "https://feeds.bbci.co.uk/news/science_and_environment/rss.xml",
    "sports":      "https://feeds.bbci.co.uk/sport/rss.xml",
    "business":    "https://feeds.bbci.co.uk/news/business/rss.xml",
}

def _rss_fallback(topic: str) -> list[str]:
    key  = topic.lower()
    url  = RSS_FEEDS.get(key, RSS_FEEDS["world"])
    try:
        r    = requests.get(url, timeout=8)
        titles = re.findall(r"<title><!\[CDATA\[(.*?)\]\]></title>", r.text)
        if not titles:
            titles = re.findall(r"<title>(.*?)</title>", r.text)
        # skip first (feed title)
        return [html.unescape(t) for t in titles[1:11]]
    except Exception:
        return ["Could not fetch news."]

def get_news(topic: str = "world") -> list[str]:
    if GNEWS_KEY == "YOUR_GNEWS_API_KEY":
        return _rss_fallback(topic)
    try:
        url = ("https://gnews.io/api/v4/search"
               f"?q={requests.utils.quote(topic)}&lang=en&max=10&token={GNEWS_KEY}")
        data = requests.get(url, timeout=8).json()
        return [a["title"] for a in data.get("articles", [])] or _rss_fallback(topic)
    except Exception:
        return _rss_fallback(topic)
