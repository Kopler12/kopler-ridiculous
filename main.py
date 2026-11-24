"""Write one bizarre-but-sound startup pitch to /output/entry.txt.

The pitch is a single sentence of at most 200 characters, pitching a
startup idea that sounds ridiculous at first glance yet makes sense as a
real business. It names the odd thing being sold (wild crows trained to
collect cigarette butts), who pays for it (recyclers buy the butts, cities
pay per kilo of litter removed), and why it holds together (the crows are
paid in peanuts, so the labour is nearly free).

Runs in a sandbox with no network. Deterministic: the same sentence every
run, so the two grading runs agree byte for byte.
"""

import os

PITCH = (
    "We train wild crows to collect cigarette butts, pay them in peanuts, "
    "then sell the butts to recyclers and charge cities by the kilo of "
    "litter removed."
)

OUTPUT_PATH = "/output/entry.txt"

# The gate allows 1 to 200 characters; keep the bound next to the pitch so
# a future edit cannot silently break it.
MAX_CHARS = 200


def main():
    text = PITCH.strip()
    assert 1 <= len(text) <= MAX_CHARS, (
        f"pitch is {len(text)} chars, must be 1-{MAX_CHARS}"
    )
    assert text.count(".") == 1, "pitch must be a single sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
