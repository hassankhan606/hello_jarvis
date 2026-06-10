"""modules/ip_info.py — Public IP address + geolocation via ip-api.com (free)."""

import requests

def get_ip_info() -> str:
    try:
        d = requests.get("http://ip-api.com/json/", timeout=8).json()
        if d.get("status") != "success":
            return "Could not retrieve IP info."
        return (
            f"🌐 IP:      {d.get('query')}\n"
            f"📍 Location: {d.get('city')}, {d.get('regionName')}, {d.get('country')}\n"
            f"🕐 Timezone: {d.get('timezone')}\n"
            f"📡 ISP:     {d.get('isp')}\n"
            f"🔢 Lat/Lon:  {d.get('lat')}, {d.get('lon')}"
        )
    except Exception as e:
        return f"IP lookup error: {e}"
