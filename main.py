"""Unsent micro-confession entry.

Writes one original two-part micro-confession to entry.txt inside
$MAKEFUN_OUTPUT_DIR (or /output when unset). Deterministic: the same
bytes on every run, no network, no input read.
"""

import os

CONFESSION = (
    "To: the girl who sat next to me in maths for three years\n"
    "i still have the note i wrote you the day you moved away, folded "
    "inside my old maths book, and i never found out if you'd have "
    "laughed or just said thanks\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
