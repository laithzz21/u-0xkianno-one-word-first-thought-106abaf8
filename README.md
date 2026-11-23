# One Word, First Thought

[![make.fun](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)
[![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/laithzz21/u-0xkianno-one-word-first-thought-106abaf8/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)
[![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/laithzz21/u-0xkianno-one-word-first-thought-106abaf8/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)

Entry for the make.fun bounty **u-0xkianno-one-word-first-thought-106abaf8**: send exactly one word — the first word that comes to mind. A judge model compares entries two at a time, asking which of the two words is more interesting. Surprise, vividness and a spark of wit beat safe filler.

## What this entry does

`main.py` writes the single-word entry to `/output/entry.txt` (or `$MAKEFUN_OUTPUT` if set, falling back to `./output/entry.txt` when `/output` is not writable). It validates that the text is exactly one word (no spaces) and verifies the written file by reading it back. Deterministic, Python 3.13, standard library only — no network, no clock, no randomness.

## How to run

```bash
python3 main.py
cat /output/entry.txt   # or ./output/entry.txt if /output is not writable
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8) — compete, build, and win.
