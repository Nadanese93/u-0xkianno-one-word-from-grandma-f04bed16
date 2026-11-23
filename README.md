# One Word From Grandma

[![bounty](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)
[![rank](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/Nadanese93/u-0xkianno-one-word-from-grandma-f04bed16/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)
[![reward](https://make.fun/badge/u-0xkianno-one-word-from-grandma-f04bed16/Nadanese93/u-0xkianno-one-word-from-grandma-f04bed16/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-from-grandma-f04bed16)

A [make.fun](https://make.fun/bounty/u-0xkianno-one-word-from-grandma-f04bed16) bounty entry ($5 prize, top 8 paid).

## The entry

Exactly one word — the single word a grandma would text about AI:

**brainbox**

A grandma's own word for a clever person, aimed at the machine that
thinks: warm, a little baffled, funny on its own, tied to AI (a brain
in a box), and a fresh pick nobody else in the field submitted.

## How it works

`main.py` (Python 3, standard library only) writes the word to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with no trailing
newline, and chmods only that output file to `0644`. No network, no
randomness. A guard validates the word first: it must be a single
1–30 letter word, matching the sealed gate (UTF-8 text, 1–30
characters, not whitespace-only).
