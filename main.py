"""One Letter: Coffee or Tea.

The whole answer is a single letter, written to /output/entry.txt:
A for coffee, B for tea. No word, no explanation, no punctuation.

The choice here is A, coffee. Coffee is the vivid one: dark, hot,
and unmistakable from the first sip of the day. Tea whispers;
coffee answers. When the question is asked in one letter, the
honest, alive answer is the cup that wakes you up.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
CHOICE = "A"  # A = coffee, B = tea


def validate_choice(choice: str) -> str:
    """Accept only the gate's two letters, A (coffee) or B (tea)."""
    if choice not in ("A", "B"):
        raise SystemExit(f"bad choice {choice!r}: must be A (coffee) or B (tea)")
    return choice


def main() -> None:
    # Exactly one character, no trailing newline: the gate requires
    # /output/entry.txt to be UTF-8 text of 1 to 1 characters.
    validate_choice(CHOICE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # newline="" stops the writer adding a trailing line break: the
    # gate counts bytes, so even one extra byte fails the entry.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(CHOICE)
    # Gate self-check: read back and verify the file is exactly one
    # letter, no newline, no extra bytes.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        text = f.read()
    if len(text) != 1 or text not in ("A", "B"):
        raise SystemExit(f"bad entry {text!r}: must be a single letter A or B")
    if os.path.getsize(OUTPUT_PATH) != 1:
        raise SystemExit("bad entry: file must be exactly 1 byte")


if __name__ == "__main__":
    main()
