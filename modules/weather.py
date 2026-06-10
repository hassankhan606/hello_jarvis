"""modules/weather.py — Live weather via wttr.in (no API key needed)."""

import requests

def get_weather(city: str = "London") -> str:
    city = city.strip() or "London"
    try:
        url = f"https://wttr.in/{requests.utils.quote(city)}?format=3"
        r   = requests.get(url, timeout=8)
        if r.status_code == 200:
            return r.text.strip()
        # richer format fallback
        url2 = (f"https://wttr.in/{requests.utils.quote(city)}"
                "?format=%l:+%C+%t+feels+like+%f+💧%h+💨%w")
        r2 = requests.get(url2, timeout=8)
        return r2.text.strip() if r2.status_code == 200 else "Weather data unavailable."
    except Exception as e:
        return f"Weather error: {e}"
