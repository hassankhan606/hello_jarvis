# J.A.R.V.I.S — AI Assistant v2.0

> **Just A Rather Very Intelligent System**  
> A real-world, feature-rich, voice-enabled AI assistant built in Python — inspired by Tony Stark's JARVIS.

---

## Features

| Feature | Command | API Used |
|---|---|---|
| 🕐 Live Time & Date | `time` / `date` | Built-in |
| 🌤 Live Weather | `weather London` | wttr.in (free) |
| 📰 Real-time News | `news technology` | BBC RSS / GNews |
| 🔍 Wikipedia Search | `search black holes` | Wikipedia API |
| 🌐 Web Instant Answers | `web who is Elon Musk` | DuckDuckGo API |
| 👤 Person Lookup | `person Albert Einstein` | Wikipedia |
| 📍 Place Info | `place Tokyo` | Wikipedia + wttr |
| 🎬 Movie Details | `movie Inception` | OMDb API |
| 📖 Dictionary | `define serendipity` | Free Dictionary API |
| 🌍 Translator | `translate Hola mundo` | MyMemory API |
| 🧮 Calculator | `calc sin(45)*pi^2` | Built-in (safe eval) |
| 😂 Jokes | `joke` | Official Joke API |
| 💡 Random Facts | `fact` | uselessfacts API |
| 💻 System Stats | `system` | psutil |
| 💰 Crypto Prices | `crypto bitcoin,eth` | CoinGecko API |
| 📝 Notes | `note Buy milk` | Local JSON |
| ⏰ Reminders | `remind 60 Take a break` | Threading |
| 🐙 GitHub Search | `github python AI` | GitHub REST API |
| 🌐 IP / Location | `myip` | ip-api.com |
| 🤖 AI Brain | `ask Why is the sky blue?` | OpenAI / Ollama / DDG |
| 🔊 Voice Toggle | `voice on` / `voice off` | pyttsx3 |

---

## 🚀 Quick Start

### 1. Clone

```bash
git clone https://github.com/hassankhan606/hello_jarvis.git
cd JARVIS
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> **Windows users**: If SpeechRecognition fails, install PyAudio separately:  
> `pip install pipwin && pipwin install pyaudio`

### 3. (Optional) Set API keys

```bash
# Free — only needed for AI answers and premium news
export OPENAI_API_KEY="sk-..."
export GNEWS_API_KEY="your_gnews_key"
export OMDB_API_KEY="your_omdb_key"
```

Or edit `config.py` directly.

### 4. Run JARVIS

```bash
python jarvis.py
```

---

## 🔑 Free API Keys

| API | Free Tier | Sign-up |
|---|---|---|
| OpenAI | $5 credit (new accounts) | https://platform.openai.com |
| GNews | 10 req/hr | https://gnews.io |
| OMDb | 1,000 req/day | https://www.omdbapi.com/apikey.aspx |
| All others | **No key needed** | — |

---

## 🏗 Project Structure

```
JARVIS/
├── jarvis.py              # Entry point
├── config.py              # API keys & settings
├── requirements.txt
├── core/
│   ├── boot.py            # Startup / dependency checker
│   └── jarvis_core.py     # Main brain & command dispatcher
├── modules/
│   ├── voice.py           # TTS + STT (pyttsx3 / SpeechRecognition)
│   ├── weather.py         # Live weather (wttr.in)
│   ├── news.py            # Headlines (BBC RSS / GNews)
│   ├── search.py          # Wikipedia + DuckDuckGo
│   ├── person.py          # Person biography
│   ├── places.py          # Place information
│   ├── movies.py          # Movie database (OMDb)
│   ├── dictionary.py      # Word definitions
│   ├── translator.py      # Language translation
│   ├── calculator.py      # Safe expression evaluator
│   ├── jokes.py           # Programming & dad jokes
│   ├── facts.py           # Random interesting facts
│   ├── system_info.py     # CPU / RAM / Disk stats
│   ├── crypto.py          # Crypto prices (CoinGecko)
│   ├── notes.py           # Persistent notes
│   ├── reminder.py        # Thread-based reminders
│   ├── github_search.py   # GitHub repository search
│   ├── ip_info.py         # IP geolocation
│   └── ai_brain.py        # AI Q&A (OpenAI / Ollama / DDG)
├── data/
│   └── notes.json         # Auto-created note storage
└── logs/                  # Reserved for future logging
```

---

## 🎙 Voice Commands (Speech-to-Text)

```bash
# Inside JARVIS, switch to mic input:
You ▸ voice on
# Then speak your command — JARVIS will listen and respond!
```

Requires a working microphone. Uses Google Speech Recognition (free, internet needed).

---

## 🤖 AI Brain Priority

1. **OpenAI GPT-4o-mini** — if `OPENAI_API_KEY` is set  
2. **Ollama local LLM** — if Ollama is running locally (`ollama run llama3`)  
3. **DuckDuckGo + Wikipedia** — always free, no key needed  

---

## 🔮 Roadmap / Coming Soon

- [ ] Wake-word detection ("Hey JARVIS") via Porcupine
- [ ] Face recognition via OpenCV
- [ ] Home automation (MQTT / Home Assistant)
- [ ] Gmail / Calendar integration
- [ ] Spotify music control
- [ ] Custom plugin system

---

## 📄 License

MIT — free to use, modify, and distribute.

---

*Built with ❤️ by Hassan.*
