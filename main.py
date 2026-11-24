#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the sun with a face (U+1F31E).
Chosen as the single character most likely to make a stranger smile:
a smiling face plus literal sunshine warmth, universal, and a deliberate
pick rather than the first smiley that comes to mind.
"""

import os
import sys

EMOJI = "\U0001F31E"  # SUN WITH FACE


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    # Gate: exactly one emoji, 1-8 characters, not whitespace only.
    # The task demands a single emoji, so require exactly one code point.
    text = EMOJI
    if len(text) != 1:
        print(f"gate fail: entry must be exactly one emoji, got {len(text)} chars", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 8):
        print(f"gate fail: length {len(text)} not in 1..8", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate fail: entry is whitespace only", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Verify after write: read back and require byte-identical content.
    with open(path, "r", encoding="utf-8", newline="") as f:
        back = f.read()
    if back != text:
        print(f"verify fail: read back {back!r} != {text!r}", file=sys.stderr)
        return 1

    print(f"wrote {path}: {text!r} ({len(text.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
