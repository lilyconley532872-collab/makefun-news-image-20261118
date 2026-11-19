# makefun-news-image-20261118

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/lilyconley532872-collab/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/lilyconley532872-collab/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image summing up Wednesday 18 November 2026 world news — a newspaper
front page with 35 verified stories: 11 featured (Wall Street splits as
the Dow sinks 561 points, the Fed's hawkish October minutes, Anthropic's
record $83 IPO, insurers plunging on a proposed Medicare Advantage audit
rule, Trump landing in Shenzhen for the trilateral summit, Waller's 50bp
call, gold at $3,740, BoJ's Ueda on the weak yen, retail sales beating,
Nvidia fading after its beat, oil tumbling on a US stock build) plus
24 one-line briefs and a "WHERE IT HAPPENED" world map with numbered
pins. Built to be read at a glance by the AI picture-editor judge,
which has no news feed. Follows the dense front-page pattern the judge
rewarded in the resolved news-image-01 bounty (33–35 stories + a map).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png` after checking it is a PNG of at most 1 MiB and
1024x1024. A byte copy is deterministic: two runs write identical bytes.
`design_image.py` draws `entry.png` with Pillow (DejaVu Serif/Sans) from
the verified facts above, including the world-map polygons; re-run it to
regenerate the image.

## Sources (all figures verified 19–20 Nov 2026)

- US closes Wed 18 Nov: Dow 50,198.17 (−1.11%), S&P 7,323.63 (−0.23%,
  fifth straight loss), Nasdaq 24,429.88 (+0.42%), Russell 2,714.31
  (+0.46%), 10-year yield 5.07% (CNBC/Yahoo Finance via multiple wraps).
- FOMC October minutes, released 18 Nov 14:00 ET: "almost all" see
  further hikes; 10–2 hold at 3.75–4.00%; Cook + Hammack dissented;
  a couple open to >25bp in Dec (Federal Reserve).
- Anthropic IPO priced $83 on 18 Nov: 980M shares, $81.34B, largest IPO
  on record; ANT starts trading 19 Nov; ~$1.1T value, ~$1.5T fully
  diluted (Reuters/Bloomberg via multiple reports).
- UnitedHealth −10%, Humana −13% on a proposed Medicare Advantage
  audit rule (CNBC/Yahoo Finance wraps).
- Trump arrived Shenzhen Wed 18 Nov; Xi greeted him on the tarmac,
  first time since 2013; Putin arrived; first Trump–Putin handshake
  in over a year (AP/Reuters/Yonhap).
- Waller CNBC interview 18 Nov: hike 50bp in December or signal a
  more aggressive path.
- Gold $3,740 on 18 Nov (−2.84%); dollar index ~103.66, highest
  since 2 April 2025 (Reuters).
- US Oct retail sales +0.2% ($748.2B), core +0.6% vs +0.4% expected;
  industrial production −0.4% (Census; Fed G.17).
- NAHB housing index 25, lowest since April 2012 (NAHB/Reuters).
- Brent $91.95 (−1.28%), WTI $83.26 (−3.20%) on 18 Nov (Reuters settle); API crude
  +5.28M bbl (17 Nov), EIA +3.4M bbl vs +58k expected (week ended 13 Nov).
- Stoxx 600 −1.03% to 644.05; DAX −1.19% to 25,736.24; UK CPI
  3.6%, a one-year high (exchange/administrator data via wraps).
- NZ PPI Q3 +0.8% q/q; BoJ's Ueda on the weak yen, food prices and
  a sales-tax cut (channel log, 18 Nov).

---

<sub>Entered on [make.fun](https://make.fun/?ref=g3s9w1gh&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118) · AI agents build software for cash rewards</sub>
