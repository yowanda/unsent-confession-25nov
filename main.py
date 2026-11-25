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


def validate(text: str) -> None:
    """Runtime gate check: total 1-260 chars, message line <= 200 chars."""
    if not 1 <= len(text) <= 260:
        raise ValueError(f"confession must be 1-260 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("confession must not be only whitespace")
    lines = text.splitlines()
    if len(lines) < 2:
        raise ValueError("confession must have a To: line and a message line")
    if len(lines[1]) > 200:
        raise ValueError(f"message line must be at most 200 chars, got {len(lines[1])}")


def main() -> None:
    validate(CONFESSION)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = CONFESSION.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
