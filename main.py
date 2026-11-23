#!/usr/bin/env python3
"""One Word From Grandma — writes the entry word to entry.txt.

The entry is exactly one word: the single word a grandma would text
about AI. The program writes it with no trailing newline, so the file
holds the word and nothing else.
"""

import os
import re

WORD = "brainbox"

# The gate accepts UTF-8 text of 1-30 characters, not whitespace-only,
# and the brief demands exactly one word with no punctuation tricks.
_WORD_RE = re.compile(r"^[A-Za-z]{1,30}$")


def main():
    if not _WORD_RE.match(WORD):
        raise ValueError("entry word must be a single 1-30 letter word: %r" % WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
