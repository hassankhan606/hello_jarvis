"""modules/facts.py — Random interesting facts via uselessfacts API."""

import requests, random

BACKUP_FACTS = [
    "Honey never spoils — archaeologists found 3,000-year-old honey in Egyptian tombs.",
    "A group of flamingos is called a flamboyance.",
    "Octopuses have three hearts and blue blood.",
    "The Eiffel Tower grows 15 cm taller in summer due to thermal expansion.",
    "Bananas are berries, but strawberries are not.",
    "A day on Venus is longer than a year on Venus.",
    "The human brain generates about 20 watts of electrical power.",
]

def random_fact() -> str:
    try:
        r = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random?language=en",
                         timeout=6)
        return r.json().get("text", random.choice(BACKUP_FACTS))
    except Exception:
        return random.choice(BACKUP_FACTS)
