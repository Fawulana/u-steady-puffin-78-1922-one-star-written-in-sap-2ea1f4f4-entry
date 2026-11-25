# SPDX-License-Identifier: MIT
"""One Star, Written in Sap.

Writes a single one-line 1-star review, in the voice of a houseplant,
to /output/entry.txt. Deterministic, offline, stdlib-only: the text is a
fixed constant, so every run produces byte-identical output.
"""

import os

LINE = (
    "He waters me with ice cubes and calls it 'a little treat' \u2014 "
    "I'm a tropical plant, not a cocktail, "
    "and the one star is for the frostbite, the cold feet, and the lies."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
