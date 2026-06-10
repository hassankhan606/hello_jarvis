"""modules/reminder.py — Thread-based reminder manager."""

import threading, time
from rich.console import Console

con = Console()

class ReminderManager:
    def __init__(self):
        self._count = 0

    def set(self, seconds: int, message: str) -> str:
        self._count += 1
        n = self._count

        def _fire():
            time.sleep(seconds)
            con.print(f"\n[bold red]⏰ REMINDER #{n}:[/bold red] {message}\n")

        t = threading.Thread(target=_fire, daemon=True)
        t.start()
        m, s = divmod(seconds, 60)
        label = f"{m}m {s}s" if m else f"{s}s"
        return f"Reminder #{n} set for {label}: '{message}'"
