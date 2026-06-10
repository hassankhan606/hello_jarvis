"""modules/crypto.py — Live crypto prices via CoinGecko free API."""

import requests

def crypto_prices(coins: str = "bitcoin,ethereum,dogecoin") -> str:
    ids = coins.lower().replace(" ", "").strip()
    try:
        url    = "https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": ids, "vs_currencies": "usd,eur", "include_24hr_change": "true"}
        data   = requests.get(url, params=params, timeout=8).json()
        if not data:
            return "No crypto data returned."
        lines = []
        for coin, vals in data.items():
            usd    = vals.get("usd", "?")
            chg    = vals.get("usd_24h_change", 0)
            arrow  = "📈" if chg >= 0 else "📉"
            lines.append(f"{arrow}  {coin.capitalize()}: ${usd:,.2f}  ({chg:+.2f}% 24h)")
        return "\n".join(lines)
    except Exception as e:
        return f"Crypto error: {e}"
