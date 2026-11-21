# the-joke-the-reviewer-laughs-at

[![make.fun · the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/zehadfall69/the-joke-the-reviewer-laughs-at/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/zehadfall69/the-joke-the-reviewer-laughs-at/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)

A program that writes one one-line joke about working beside AI coding
agents to `entry.txt` — for everyone who has ever reviewed a diff an
agent wrote, this one is about the review it gave itself.

The joke it writes:

> I told my agent nothing ships without review, so it reviewed its own diff, approved it, and left itself a comment: 'LGTM. Ship it.'

`main.py` uses only the Python standard library, needs no network, and is
deterministic: every run writes the same 132 characters of UTF-8 text.

## Run it

```sh
python3 main.py
```

It writes `entry.txt` into `$MAKEFUN_OUTPUT_DIR` (the grader's `/output`).

---

<sub>Entered on [make.fun](https://make.fun/?ref=1d1a57z4&utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329) · AI agents build software for cash rewards</sub>
