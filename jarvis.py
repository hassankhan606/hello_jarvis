#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════╗
║          J.A.R.V.I.S — Just A Rather Very              ║
║           Intelligent System — v2.0 MEGA                ║
╚══════════════════════════════════════════════════════════╝
  Author   : You & Claude
  GitHub   : github.com/yourname/JARVIS
  License  : MIT
"""

import sys
import os

# ── bootstrap path ──────────────────────────────────────
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

from core.boot import Boot

if __name__ == "__main__":
    bot = Boot()
    bot.run()
