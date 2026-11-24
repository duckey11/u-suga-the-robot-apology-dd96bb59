#!/usr/bin/env python3
"""Write the make.fun entry text for the Robot Apology bounty.

Writes exactly two lines to /output/entry.txt, no trailing newline,
deterministic: two runs produce byte-identical output.
"""

import os

ENTRY = (
    "I'm sorry I watered your grandmother's orchid instead of the fern, "
    "and it wilted before you noticed.\n"
    "I've learned to read the label on every pot before I pour, so from "
    "now on I'll read the label twice and water only the plant you named."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
