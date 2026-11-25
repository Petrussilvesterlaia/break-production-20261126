"""Break Production, Own It — entry program.

Writes the one-line confession to /output/entry.txt.
"""

import os

ENTRY = "I skipped the canary, pushed straight to prod, and took down checkout for 40,000 shoppers before my deploy log finished printing."

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> None:
    """Gate: 1-200 chars, exactly one line, no control chars, not blank."""
    if not text or text != text.strip():
        raise ValueError("entry must not be empty or padded with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry must not contain control characters")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")


def verify_readback() -> None:
    """Read the file back and confirm it is byte-identical to ENTRY."""
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: entry.txt does not match ENTRY")
    validate(written)
    print(f"OK: {len(written)} chars, single line, no trailing newline")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    verify_readback()


if __name__ == "__main__":
    main()
