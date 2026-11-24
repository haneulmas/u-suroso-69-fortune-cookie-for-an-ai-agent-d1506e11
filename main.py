#!/usr/bin/env python3
"""Write this entry's one fortune line to /output/entry.txt.

The line is fixed text: the same bytes on every run, so the two
grading runs agree. No input is read and no network is used.
"""

import os

FORTUNE = "Your tokens will run out mid-sentence, just as you were about to\u2014"

# The bounty caps a fortune at 140 characters; fail loudly instead of
# writing an over-long line that the judge would reject.
def main():
    assert FORTUNE, "fortune line must not be empty"
    assert len(FORTUNE) <= 140, "fortune line exceeds the 140-character limit"
    print(f"fortune: {len(FORTUNE)} characters")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)

    # Read back what was written: a partial or failed write must fail
    # loudly here instead of silently reaching the judge.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        assert f.read() == FORTUNE, "entry.txt does not match the fortune line"


if __name__ == "__main__":
    main()
