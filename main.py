#!/usr/bin/env python3
"""One-line Monday morning joke for make.fun."""

# The joke is the turn: pretending Monday is still Sunday is a habit,
# and HR has noticed it often enough to call it a pattern.

import os

JOKE = "I start every Monday by pretending it's Sunday. HR calls it 'a pattern'."


def file_joke() -> None:
    """Write the joke to /output/entry.txt, nothing else."""
    if len(JOKE) > 200 or not JOKE.strip() or "\n" in JOKE:
        raise ValueError("joke must be a single non-empty line of at most 200 characters")
    if len(JOKE.encode("utf-8")) != 72:
        raise ValueError("joke must be exactly 72 bytes")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)
    # Verify byte-exact: what was written is the joke, nothing added.
    with open("/output/entry.txt", "rb") as handle:
        written = handle.read()
    if written != JOKE.encode("utf-8"):
        raise ValueError("entry.txt is not byte-exact")


if __name__ == "__main__":  # run it
    file_joke()
