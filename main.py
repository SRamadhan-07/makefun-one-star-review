#!/usr/bin/env python3
"""Entry for make.fun's "One-Star Review of Something Essential".

Writes one line to /output/entry.txt: a deadpan one-star review of
Sleep, an everyday essential. The line is 117 characters (129 UTF-8
bytes), inside the gate of 1 to 160 characters. Standard library
only; no network.
"""

import os

REVIEW = (
    "★☆☆☆☆ — Sleep: advertised as eight free hours; "
    "mine arrived in 40-minute instalments, with dreams as "
    "unskippable ads."
)


def main() -> None:
    # Gate guard: one line of 1 to 160 characters — the count is in
    # characters, not bytes, which matters with the star glyphs.
    if not 1 <= len(REVIEW) <= 160 or "\n" in REVIEW:
        raise ValueError("review must be one line of 1 to 160 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # One line only: the review is written with no trailing newline.
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(REVIEW)


if __name__ == "__main__":
    main()
