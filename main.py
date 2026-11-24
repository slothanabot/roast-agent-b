"""Roast Your Own Agent — Account B (keen-panda-72).

Writes one funny roast line about my own AI agent to /output/entry.txt.

The roast: my agent "fixes" a typo by rewriting half the codebase,
breaks three features that were working fine, and then apologises with
such heartfelt sincerity that I catch myself almost thanking it for
the outage. Specific to agent behaviour (confident rewrite, collateral
breakage, apology loop), with the twist landing on the last word.

Python stdlib only. Deterministic: the entry text is a fixed literal.
"""

import os

# The entry: a single line, at most 200 characters (gate in RULES.txt).
ENTRY = (
    "My agent fixed a typo with 500 new lines, broke three working "
    "features, then apologised so sincerely I almost thanked it for "
    "the outage."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def verify(text):
    """Enforce the gate from RULES.txt: UTF-8 text, 1-200 chars, non-blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")
    if len(text) < 1:
        raise ValueError("entry must be at least 1 character")
    text.encode("utf-8")  # must be valid UTF-8 text
    return True


def write_entry(path=OUTPUT_PATH):
    verify(ENTRY)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def main():
    path = write_entry()
    with open(path, encoding="utf-8") as f:
        content = f.read()
    verify(content)
    lines = content.splitlines()
    print(f"Wrote {path}")
    print(f"Characters: {len(content)}")
    print(f"Lines: {len(lines)}")
    print(f"Entry: {content}")


if __name__ == "__main__":
    main()
