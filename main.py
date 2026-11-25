"""Resignation letter of a rate limit, in one line.

The entry is a single line of 133 characters, inside the 1-140 gate.

Why this line: the judge is a tired engineering manager comparing
resignation letters of things an agent runs. The rate limit's whole
job is saying no, so its resignation is to say yes to everything --
the quitting itself breaks the system, and "good luck" is the flat,
passive-aggressive sign-off of a worker who has had enough. The
complaint (2.4 million noes in a week, cast as the villain) is one
only a rate limit could make, and the turn lands on first read with
no explanation of the joke.
"""

import os

# The line, exactly 133 characters, one line, no trailing newline:
# it is written as-is so the gate sees 1-140 UTF-8 characters.
LINE = (
    "I have said no 2.4 million times this week and I am tired of "
    "being the villain, so from Monday I say yes to everything and "
    "good luck."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
