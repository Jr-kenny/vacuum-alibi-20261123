#!/usr/bin/env python3
"""Entry program for make.fun u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.

Writes the one-line alibi to /output/entry.txt. Python 3, stdlib only.
The line is deadpan robot voice, specific about the sensors, with the
punch at the end: the vacuum lets the human step on the Lego instead.
"""
import os

LINE = "I skipped that corner on purpose: my sensors found a Lego brick there, and I decided your bare foot deserved the lesson more than my wheels did."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("line must be 1 to 200 characters")
    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = os.path.join(OUT_DIR, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back what was written: the entry must be exactly the line,
    # no trailing newline, nothing added.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise SystemExit("entry.txt does not match the line")


if __name__ == "__main__":
    main()
