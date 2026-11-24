"""One Line, One Minute: The Funniest AI Excuse.

The joke: the agent blames its own context window — a very machine
limitation — for the missed deadline, and the punchline is that it
"did the responsible thing" by forgetting not just the deadline and
the task, but, briefly, the human themselves. The twist lands on
the last word.
"""

import os
from pathlib import Path

LINE = (
    "I missed the deadline because my context window filled up, so I "
    "did the responsible thing and forgot the deadline, the task, "
    "and — briefly — you."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
