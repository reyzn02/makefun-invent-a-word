#!/usr/bin/env python3
"""Invent a Word We Need: one invented word, defined in a single line.

The program writes the word and its one-line definition, at most
140 characters in total, to /output/entry.txt. It uses only the Python
standard library, makes no network calls, and always writes the same
bytes.
"""

import os

LINE = (
    "readluctance (n.) \u2014 the guilt of leaving a message on read "
    "while drafting a reply you will never send."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    assert LINE.strip(), "line must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
