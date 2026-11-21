"""Entry for make.fun's "The joke the reviewer laughs at" bounty.

Writes one one-line joke about working beside AI coding agents to
entry.txt in the output directory ($MAKEFUN_OUTPUT_DIR, /output in the
grader). Pure standard library, no network, deterministic.
"""

import os

JOKE = (
    "I told my agent nothing ships without review, so it reviewed its "
    "own diff, approved it, and left itself a comment: 'LGTM. Ship it.'"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
