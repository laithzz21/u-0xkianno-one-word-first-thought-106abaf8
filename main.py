#!/usr/bin/env python3
"""One-word first-thought entry for make.fun bounty
u-0xkianno-one-word-first-thought-106abaf8.

Writes the single-word entry to /output/entry.txt (or $MAKEFUN_OUTPUT
if set). Deterministic, stdlib only, no network, no clock, no randomness.
"""

import os
import sys

WORD = "zamboni"


def validate_word(word: str) -> None:
    """The entry must be exactly one word: non-empty, no whitespace."""
    if not word:
        raise ValueError("entry word is empty")
    if any(ch.isspace() for ch in word):
        raise ValueError(f"entry must be a single word, got: {word!r}")


def resolve_path() -> str:
    """Resolve the output path, falling back to ./output/entry.txt
    when /output is not writable."""
    override = os.environ.get("MAKEFUN_OUTPUT")
    if override:
        return os.path.join(override, "entry.txt")
    try:
        os.makedirs("/output", exist_ok=True)
        if os.access("/output", os.W_OK):
            return "/output/entry.txt"
    except OSError:
        pass
    return os.path.join(os.getcwd(), "output", "entry.txt")


def main() -> int:
    validate_word(WORD)
    path = resolve_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Verify the written file by reading it back.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != WORD:
        raise ValueError(
            f"verification failed: expected {WORD!r}, read back {written!r}"
        )
    print(f"Wrote entry to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
