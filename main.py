#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI -- make.fun entry.

Writes one pickup line aimed at a robot/AI to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt),
with no trailing newline.
"""

import os
import sys
from pathlib import Path

ENTRY = (
    "Are you overfitting? Because you've memorized every little thing "
    "about me \u2014 and I hope you never generalize."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text):
    """Check the entry against the competition gate.

    Returns a list of problems; an empty list means the entry is valid.
    """
    problems = []
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        problems.append(
            "entry is %d characters, must be %d-%d"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    if not text.strip():
        problems.append("entry is only whitespace")
    if text != text.strip():
        problems.append(
            "entry has leading or trailing whitespace, which wastes "
            "characters and weakens the punch"
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    if any(ord(ch) < 0x20 and ch != "\t" for ch in text):
        problems.append("entry contains control characters")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry is not valid UTF-8")
    return problems


def main():
    problems = validate(ENTRY)
    if problems:
        for problem in problems:
            print("invalid entry: %s" % problem, file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8")
    print("wrote %d characters to %s" % (len(ENTRY), out_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
