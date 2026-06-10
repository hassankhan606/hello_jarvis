"""config.py — Centralised API key & settings configuration for JARVIS.

Edit this file OR set environment variables (env vars take priority).
Free tiers & sign-up links are listed beside each key.
"""

import os

# ─────────────────────────────────────────────────────────
#  REQUIRED  (everything works without these — they just
#  enable richer / higher-quota responses)
# ─────────────────────────────────────────────────────────

# OpenAI — GPT-4o-mini AI answers
# Free $5 credit on new accounts: https://platform.openai.com
OPENAI_API_KEY      = os.getenv("OPENAI_API_KEY",  "")

# GNews — real-time news headlines
# 10 req/hr free: https://gnews.io
GNEWS_API_KEY       = os.getenv("GNEWS_API_KEY",   "")

# OMDb — movie database
# 1,000 req/day free: https://www.omdbapi.com/apikey.aspx
OMDB_API_KEY        = os.getenv("OMDB_API_KEY",    "trilogy")

# ─────────────────────────────────────────────────────────
#  ALWAYS FREE (no key needed)
# ─────────────────────────────────────────────────────────
# • wttr.in          → weather
# • DuckDuckGo API   → instant web answers
# • Wikipedia API    → search / person / place
# • CoinGecko API    → crypto prices
# • ip-api.com       → IP geolocation
# • Free Dictionary  → word definitions
# • MyMemory API     → translation (1,000 words/day)
# • uselessfacts API → random facts
# • official-joke-api → jokes
# • GitHub REST API  → repo search
# • BBC RSS feeds    → news fallback

# ─────────────────────────────────────────────────────────
#  JARVIS BEHAVIOUR SETTINGS
# ─────────────────────────────────────────────────────────
VOICE_ENABLED       = True    # set False to disable TTS at startup
VOICE_RATE          = 165     # words per minute
VOICE_VOLUME        = 0.95    # 0.0 – 1.0
AI_MAX_TOKENS       = 300
NEWS_MAX_HEADLINES  = 5
