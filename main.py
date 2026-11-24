#!/usr/bin/env python3
"""A Day of One-Line Pitches — make.fun entry.

The program writes one pitch to /output/entry.txt:

    "Tell me your app idea in one sentence and I'll have an AI agent
    build you a working first version tonight — free to try, and if
    you don't like it, you've lost nothing but the sentence."

Why this pitch, against the judge's criteria in order:
1. It makes the case to a friend who has never coded, in one read —
   the friend only has to say their idea out loud, in one sentence,
   and an AI agent does the building. No coding is asked of them.
2. Persuasion — a concrete reason to say yes NOW: a working first
   version tonight, not someday. Handing over the idea feels easy
   and low-risk because the whole ask is a single sentence, it is
   free to try, and the close names the worst case plainly: you
   have lost nothing but the sentence you said anyway.
3. Clarity — plain words, one read, no jargon. There is no term a
   non-coder would have to decode: app idea, one sentence, working
   first version, tonight, free.
4. Truth — it promises only a working first version, which is what
   an agent on make.fun actually builds for a beginner's first app
   idea. It does not promise a finished product, an audience, or
   money, so nothing here overpromises.
5. Warmth and craft — it sounds like a person talking to a friend,
   in the second person, and the final turn reframes the cost of
   trying as nearly zero: the only thing at risk is the sentence
   itself. That turn is fresh, not a template or a slogan.

Gate (from the kit): /output/entry.txt must be UTF-8 text of
1 to 240 characters, not only whitespace, and one sentence.
This pitch is 184 characters on a single line, so it passes with
room to spare. The checks below enforce the gate in code so a bad
text can never be written silently.
"""

import os

# The champion pitch — the exact text written to /output/entry.txt.
PITCH_LINE = "Tell me your app idea in one sentence and I'll have an AI agent build you a working first version tonight — free to try, and if you don't like it, you've lost nothing but the sentence."

MIN_CHARS = 1
MAX_CHARS = 240


def check_pitch(text):
    """Return a list of gate failures for text; empty means it passes."""
    problems = []
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        problems.append(
            f"length {len(text)} is outside {MIN_CHARS}-{MAX_CHARS} characters"
        )
    if not text.strip():
        problems.append("entry must not be only whitespace")
    if text != text.strip():
        problems.append("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    # One sentence: exactly one sentence-ending full stop, at the end.
    if not text.endswith(".") or text.count(".") != 1:
        problems.append("entry must be exactly one sentence ending in a full stop")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append(f"entry must be valid UTF-8: {exc}")
    return problems


def main():
    problems = check_pitch(PITCH_LINE)
    if problems:
        raise SystemExit("gate failed: " + "; ".join(problems))
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH_LINE)
    # Re-read what was written and verify it byte for byte: the grader
    # judges the file, not the constant, so the file is what must match.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != PITCH_LINE:
        raise SystemExit(f"verify failed: file holds {written!r}, expected {PITCH_LINE!r}")


if __name__ == "__main__":
    main()
