#!/usr/bin/env python3
"""Write one code-review comment: a single line approving a pull request
while carrying quiet existential dread. Python standard library only."""

import os

COMMENT = (
    "LGTM. The refactor is clean, the tests pass, and I can already hear "
    "the 3am page this code is quietly scheduling."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(COMMENT + "\n")


if __name__ == "__main__":
    main()
