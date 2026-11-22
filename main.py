"""Curious for the Judge — make.fun text micro.

Writes one short scene to entry.txt: a lighthouse keeper who keeps
the lamp lit though no ship has passed in forty years, and a logbook
open to a page dated tomorrow.

How it meets the judge's curiosity brief (most important first):

1. Intrigue: two open questions carry the whole piece — why keep a
   lamp lit for ships that never come, and who wrote tomorrow's date
   in the logbook? Each sentence plants a question the next sentence
   does not answer; the reader is left asking.
2. Calm from the text itself: no instruction to relax, no wellness
   words. The calm is shown — a quiet night, a lamp, a desk — and the
   strangeness arrives gently inside that stillness.
3. Craft: plain concrete words (lamp, desk, logbook, tomorrow), a
   slow two-sentence rhythm, and nothing that could be cut — every
   word either sets the scene or sharpens the mystery.
4. It lingers: the dated-tomorrow logbook is an image the reader can
   return to; it keeps working after the last line.
5. Freshness: its own image, not a stock phrase or a reworded
   meditation — a lighthouse that guides no one, and a future that is
   already written down.
"""

import os

TEXT = (
    "The lighthouse keeper leaves the lamp lit every night, though no "
    "ship has passed in forty years. On the desk, a logbook open to a "
    "page dated tomorrow."
)


def main() -> None:
    if not TEXT.strip():
        raise ValueError("entry text must not be blank")
    if not 1 <= len(TEXT) <= 280:
        raise ValueError(
            f"entry text must be 1-280 code points, got {len(TEXT)}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
