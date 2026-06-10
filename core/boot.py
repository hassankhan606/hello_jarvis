"""core/boot.py — Startup controller & dependency checker."""

import os, sys, time, importlib

REQUIRED = [
    ("requests",       "requests"),
    ("rich",           "rich"),
    ("pyttsx3",        "pyttsx3"),
    ("speech_recognition", "SpeechRecognition"),
    ("wikipedia",      "wikipedia"),
    ("bs4",            "beautifulsoup4"),
    ("pyjokes",        "pyjokes"),
    ("psutil",         "psutil"),
    ("pytz",           "pytz"),
    ("openai",         "openai"),
]

OPTIONAL = [
    ("cv2",            "opencv-python", "Face / camera features"),
    ("pvporcupine",    "pvporcupine",   "Wake-word 'Hey JARVIS'"),
]


class Boot:
    def __init__(self):
        self._check_deps()

    # ── dependency gate ──────────────────────────────────
    def _check_deps(self):
        from rich.console import Console
        from rich.panel  import Panel
        from rich.table  import Table

        con = Console()
        con.print(Panel.fit(
            "[bold cyan]J.A.R.V.I.S  MEGA  v2.0[/bold cyan]\n"
            "[dim]Checking dependencies …[/dim]",
            border_style="cyan"
        ))

        missing = []
        for mod, pkg in REQUIRED:
            try:
                importlib.import_module(mod)
                con.print(f"  [green]✔[/green]  {pkg}")
            except ImportError:
                con.print(f"  [red]✘[/red]  {pkg}  [dim](will install)[/dim]")
                missing.append(pkg)

        if missing:
            con.print("\n[yellow]Installing missing packages…[/yellow]")
            import subprocess
            subprocess.check_call([sys.executable, "-m", "pip", "install", *missing, "-q"])
            con.print("[green]All packages ready.[/green]\n")

        for mod, pkg, note in OPTIONAL:
            try:
                importlib.import_module(mod)
                con.print(f"  [blue]✔[/blue]  {pkg}  [dim]({note})[/dim]")
            except ImportError:
                con.print(f"  [dim]–  {pkg}  optional ({note})[/dim]")

    # ── launch ───────────────────────────────────────────
    def run(self):
        from core.jarvis_core import JarvisCore
        j = JarvisCore()
        j.start()
