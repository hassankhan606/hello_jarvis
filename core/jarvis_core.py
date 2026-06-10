"""core/jarvis_core.py — JARVIS brain: UI loop + command dispatcher."""

import os, time, datetime, threading
from rich.console import Console
from rich.panel   import Panel
from rich.text    import Text
from rich.live    import Live
from rich.layout  import Layout
from rich.table   import Table
from rich         import box

# ── module imports ───────────────────────────────────────
from modules.voice      import VoiceEngine
from modules.weather    import get_weather
from modules.news       import get_news
from modules.search     import wiki_search, web_search_ddg
from modules.system_info import sys_stats
from modules.jokes      import tell_joke
from modules.facts      import random_fact
from modules.person     import search_person
from modules.places     import search_place
from modules.calculator import calculate
from modules.reminder   import ReminderManager
from modules.notes      import NotesManager
from modules.ai_brain   import AIBrain
from modules.crypto     import crypto_prices
from modules.movies     import search_movie
from modules.translator import translate_text
from modules.dictionary import define_word
from modules.github_search import github_search
from modules.ip_info    import get_ip_info

con = Console()

BANNER = """
[bold cyan]
     ██╗ █████╗ ██████╗ ██╗   ██╗██╗███████╗
     ██║██╔══██╗██╔══██╗██║   ██║██║██╔════╝
     ██║███████║██████╔╝██║   ██║██║███████╗
██   ██║██╔══██║██╔══██╗╚██╗ ██╔╝██║╚════██║
╚█████╔╝██║  ██║██║  ██║ ╚████╔╝ ██║███████║
 ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚═╝╚══════╝
[/bold cyan]
[dim]Just A Rather Very Intelligent System  •  v2.0 MEGA[/dim]
"""

HELP_TABLE = [
    ("⏰  time / date",        "Current time & date"),
    ("🌤  weather <city>",     "Live weather (wttr.in)"),
    ("📰  news [topic]",       "Top headlines (GNews API)"),
    ("🔍  search <query>",     "Wikipedia summary"),
    ("🌐  web <query>",        "DuckDuckGo instant answers"),
    ("👤  person <name>",      "Wikipedia bio of any person"),
    ("📍  place <name>",       "Info about any place"),
    ("🎬  movie <name>",       "Movie details (OMDb API)"),
    ("📖  define <word>",      "Dictionary definition"),
    ("🌍  translate <text>",   "Translate to English (MyMemory)"),
    ("🧮  calc <expr>",        "Safe expression evaluator"),
    ("😂  joke",               "Random programming/dad joke"),
    ("💡  fact",               "Random interesting fact"),
    ("💻  system",             "CPU / RAM / Disk / Network"),
    ("💰  crypto [coin]",      "Live crypto prices"),
    ("📝  note <text>",        "Save a note"),
    ("📋  notes",              "View all notes"),
    ("⏰  remind <s> <msg>",   "Set a reminder (seconds)"),
    ("🐙  github <query>",     "Search GitHub repos"),
    ("🌐  myip",               "Your IP & geolocation"),
    ("🤖  ask <question>",     "AI answer (GPT-4o-mini / free)"),
    ("🔊  voice on/off",       "Toggle text-to-speech"),
    ("❓  help",               "Show this menu"),
    ("👋  quit / exit",        "Goodbye"),
]


class JarvisCore:
    def __init__(self):
        self.voice   = VoiceEngine()
        self.remind  = ReminderManager()
        self.notes   = NotesManager()
        self.ai      = AIBrain()
        self.running = True

    # ── greeting ─────────────────────────────────────────
    def _greet(self):
        hour = datetime.datetime.now().hour
        if   hour < 12: g = "Good morning"
        elif hour < 17: g = "Good afternoon"
        else:           g = "Good evening"
        msg = f"{g}, boss. JARVIS is online. How can I assist you today?"
        con.print(Panel(BANNER, border_style="cyan", expand=False))
        con.print(f"\n[bold green]JARVIS ▸[/bold green] {msg}\n")
        self.voice.speak(msg)

    # ── prompt ───────────────────────────────────────────
    def _prompt(self) -> str:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return con.input(f"[dim]{now}[/dim] [bold cyan]You ▸[/bold cyan] ").strip()

    # ── respond helper ───────────────────────────────────
    def _say(self, text: str, style: str = "bold green"):
        con.print(f"\n[{style}]JARVIS ▸[/{style}] {text}\n")
        self.voice.speak(text)

    # ── help ─────────────────────────────────────────────
    def _show_help(self):
        t = Table(title="JARVIS Command Menu", box=box.ROUNDED,
                  border_style="cyan", show_header=True,
                  header_style="bold cyan")
        t.add_column("Command",     style="yellow", no_wrap=True)
        t.add_column("Description", style="white")
        for cmd, desc in HELP_TABLE:
            t.add_row(cmd, desc)
        con.print(t)

    # ── main dispatcher ──────────────────────────────────
    def _handle(self, raw: str):
        cmd   = raw.lower().strip()
        parts = raw.strip().split(maxsplit=1)
        kw    = parts[0].lower() if parts else ""
        arg   = parts[1].strip() if len(parts) > 1 else ""

        # ── time / date ──────────────────────────────────
        if kw in ("time",):
            self._say(datetime.datetime.now().strftime("It is %I:%M %p."))

        elif kw in ("date",):
            self._say(datetime.datetime.now().strftime("Today is %A, %B %d %Y."))

        elif kw in ("datetime", "now"):
            self._say(datetime.datetime.now().strftime("%A %B %d %Y — %I:%M:%S %p"))

        # ── weather ──────────────────────────────────────
        elif kw == "weather":
            city = arg or "London"
            self._say(get_weather(city))

        # ── news ─────────────────────────────────────────
        elif kw == "news":
            stories = get_news(arg or "world")
            for i, s in enumerate(stories[:5], 1):
                con.print(f"  [cyan]{i}.[/cyan] {s}")
            self.voice.speak(f"Here are the top {min(5,len(stories))} headlines.")

        # ── wikipedia search ─────────────────────────────
        elif kw == "search":
            self._say(wiki_search(arg))

        # ── web / ddg ────────────────────────────────────
        elif kw == "web":
            self._say(web_search_ddg(arg))

        # ── person bio ───────────────────────────────────
        elif kw == "person":
            self._say(search_person(arg))

        # ── place info ───────────────────────────────────
        elif kw == "place":
            self._say(search_place(arg))

        # ── movie ────────────────────────────────────────
        elif kw == "movie":
            self._say(search_movie(arg))

        # ── dictionary ───────────────────────────────────
        elif kw == "define":
            self._say(define_word(arg))

        # ── translate ────────────────────────────────────
        elif kw == "translate":
            self._say(translate_text(arg))

        # ── calculator ───────────────────────────────────
        elif kw in ("calc", "calculate"):
            self._say(calculate(arg))

        # ── joke ─────────────────────────────────────────
        elif kw in ("joke", "jokes"):
            self._say(tell_joke())

        # ── fact ─────────────────────────────────────────
        elif kw in ("fact", "facts"):
            self._say(random_fact())

        # ── system stats ─────────────────────────────────
        elif kw in ("system", "sysinfo", "stats"):
            con.print(sys_stats())

        # ── crypto ───────────────────────────────────────
        elif kw == "crypto":
            self._say(crypto_prices(arg or "bitcoin,ethereum,dogecoin"))

        # ── notes ────────────────────────────────────────
        elif kw == "note":
            self._say(self.notes.add(arg))

        elif kw == "notes":
            con.print(self.notes.view())

        # ── reminder ─────────────────────────────────────
        elif kw == "remind":
            try:
                p2 = arg.split(maxsplit=1)
                secs, msg = int(p2[0]), p2[1]
                self._say(self.remind.set(secs, msg))
            except Exception:
                self._say("Usage: remind <seconds> <message>", "red")

        # ── github ───────────────────────────────────────
        elif kw == "github":
            self._say(github_search(arg))

        # ── my ip ────────────────────────────────────────
        elif kw == "myip":
            self._say(get_ip_info())

        # ── AI brain ─────────────────────────────────────
        elif kw == "ask":
            self._say(self.ai.ask(arg), "bold magenta")

        # ── voice toggle ─────────────────────────────────
        elif kw == "voice":
            state = self.voice.toggle()
            self._say(f"Voice {'enabled' if state else 'disabled'}.")

        # ── help ─────────────────────────────────────────
        elif kw in ("help", "?", "commands"):
            self._show_help()

        # ── exit ─────────────────────────────────────────
        elif kw in ("quit", "exit", "bye", "goodbye"):
            msg = "Shutting down. Stay awesome, boss."
            self._say(msg)
            self.running = False

        # ── empty / unknown ──────────────────────────────
        elif cmd == "":
            pass
        else:
            # fallback: ask AI
            answer = self.ai.ask(raw)
            self._say(answer, "bold magenta")

    # ── main loop ────────────────────────────────────────
    def start(self):
        self._greet()
        self._show_help()
        while self.running:
            try:
                raw = self._prompt()
                self._handle(raw)
            except KeyboardInterrupt:
                self._say("Interrupted. Type 'quit' to exit.")
            except Exception as e:
                con.print_exception()
