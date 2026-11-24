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


def main() -> None:
    # Exactly one character, no trailing newline: the gate requires
    # /output/entry.txt to be UTF-8 text of 1 to 1 characters.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(CHOICE)
    assert os.path.getsize(OUTPUT_PATH) == 1


if __name__ == "__main__":
    main()
