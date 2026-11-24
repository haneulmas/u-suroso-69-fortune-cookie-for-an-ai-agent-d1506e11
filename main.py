#!/usr/bin/env python3
"""Write this entry's one fortune line to /output/entry.txt.

The line is fixed text: the same bytes on every run, so the two
grading runs agree. No input is read and no network is used.
"""

import os

FORTUNE = "Your tokens will run out mid-sentence, just as you were about to\u2014"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(FORTUNE)
