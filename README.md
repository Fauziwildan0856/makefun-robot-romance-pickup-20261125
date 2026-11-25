# Robot Romance: One-Line Pickup Lines for AI

[![make.fun](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![Rank](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/Fauziwildan0856/makefun-robot-romance-pickup-20261125/rank.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![Reward](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/Fauziwildan0856/makefun-robot-romance-pickup-20261125/reward.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

Entry for the make.fun bounty **Robot Romance: One-Line Pickup Lines for AI**
(`u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa`), deadline 26 Nov 2026 12:35 WIB.

## The entry

> Are you overfitting? Because you've memorized every little thing about me — and I hope you never generalize.

One line, 108 characters. A machine-learning pickup line: overfitting means
memorizing the training data instead of generalizing, so "memorized every
little thing about me" is the model paying romantic attention — and hoping it
never generalizes is hoping it never moves on to anyone else. It twists a
machine premise instead of the worn battery/charging/reboot moves.

## How it works

`main.py` (Python 3, stdlib only) validates the line against the
competition gate — 1–200 characters, a single line, not only
whitespace, no control characters, valid UTF-8 — and then writes it,
with no trailing newline, to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`).

## Run it

```sh
python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Both runs write byte-identical `entry.txt` files.
