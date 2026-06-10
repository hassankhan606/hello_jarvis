"""modules/notes.py — Persistent notes saved to a local JSON file."""

import json, os, datetime
from rich.table import Table
from rich       import box

NOTES_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                          "data", "notes.json")

class NotesManager:
    def __init__(self):
        os.makedirs(os.path.dirname(NOTES_FILE), exist_ok=True)
        self._notes: list[dict] = []
        self._load()

    def _load(self):
        try:
            with open(NOTES_FILE) as f:
                self._notes = json.load(f)
        except Exception:
            self._notes = []

    def _save(self):
        with open(NOTES_FILE, "w") as f:
            json.dump(self._notes, f, indent=2)

    def add(self, text: str) -> str:
        if not text:
            return "Please provide note text."
        entry = {"id": len(self._notes)+1,
                 "text": text,
                 "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}
        self._notes.append(entry)
        self._save()
        return f"Note #{entry['id']} saved."

    def view(self):
        if not self._notes:
            return "No notes saved."
        t = Table(title="My Notes", box=box.SIMPLE, border_style="yellow")
        t.add_column("#",    style="cyan",  no_wrap=True)
        t.add_column("Time", style="dim",   no_wrap=True)
        t.add_column("Note", style="white")
        for n in self._notes:
            t.add_row(str(n["id"]), n["time"], n["text"])
        return t
