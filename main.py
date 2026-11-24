#!/usr/bin/env python3
"""The Robot Apology — entrypoint.

Writes a two-line robot confession to /output/entry.txt:
line 1 owns one specific mistake, line 2 names the lesson and the fix.
Stdlib only.
"""

import os
from pathlib import Path

ENTRY = (
    "I'm sorry \u2014 I salted your coffee this morning because the salt and sugar jars sit "
    "side by side and I grabbed by position instead of reading the label.\n"
    "I learned that position is not identity, so from now on I read every label before I "
    "pour, even when I'm sure I already know.\n"
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(ENTRY.encode("utf-8"))
    raw = target.read_bytes()
    assert raw == ENTRY.encode("utf-8"), "entry.txt bytes do not match the intended text"
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 400, f"entry length {len(text)} outside 1-400"
    assert text.strip(), "entry is only whitespace"
    lines = [line for line in text.split("\n") if line.strip()]
    assert len(lines) == 2, f"expected exactly 2 non-empty lines, got {len(lines)}"


if __name__ == "__main__":
    main()
