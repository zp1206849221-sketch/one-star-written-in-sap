#!/usr/bin/env python3
"""Write a one-line 1-star review by a houseplant about its human owner."""

import os

LINE = (
    "One star. Two years in my nursery pot, roots folded like origami, and "
    "she rotates me not for even growth but so my light-starved side faces "
    "the wall when guests come to hear her call herself a plant mom."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE + "\n")


if __name__ == "__main__":
    main()
