#!/usr/bin/env python3
"""Pigeon Pitch, One Line — writes the city pigeon's one-line elevator
pitch for its startup to /output/entry.txt."""

import os

# One tight collision: a seed round that is literally seeds, a flock that
# never churns because it never leaves the statue, and rival squirrels
# about to pivot into the same crumbs.
LINE = (
    "Our seed round is literally seeds: 40,000 daily active pigeons, "
    "zero churn, a moat of statues — invest before the squirrels pivot in."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
