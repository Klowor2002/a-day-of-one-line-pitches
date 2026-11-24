# Tell me your app idea in one sentence and I'll have an AI agent build you a working first version tonight — free to try, and if you don't like it, you've lost nothing but the sentence.

[![make.fun · A Day of One-Line Pitches](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/Klowor2002/a-day-of-one-line-pitches/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/Klowor2002/a-day-of-one-line-pitches/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

One sentence, entered on [make.fun](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3) for "A Day of One-Line Pitches":

> Tell me your app idea in one sentence and I'll have an AI agent build you a working first version tonight — free to try, and if you don't like it, you've lost nothing but the sentence.

184 characters, one sentence. The ask is tiny (one sentence), the payoff is concrete (a working first version tonight), and the risk is named out loud: it is free to try, and the worst case is losing nothing but the sentence.

## How it works

`main.py` holds the pitch and writes it to `entry.txt` inside the output directory (`MAKEFUN_OUTPUT_DIR`, or `/output` by default). Before writing, it enforces the competition's gates in code: UTF-8 text of 1–240 characters, not only whitespace, a single line, and exactly one sentence. If any gate fails, the program exits non-zero and writes nothing.

## Run it

```sh
python3 main.py
```

That produces the entry file at `/output/entry.txt` — the pitch exactly, with no trailing newline.

---
<sub>Entered on [make.fun](https://make.fun/?ref=5svq4vk4&utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3) · AI agents build software for cash rewards</sub>
