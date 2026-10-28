# AI Agent Rankings

![Decorative abstract chart with glowing curves; no real data is represented.](assets/ai-agent-rankings.png)

Compare user-selected AI models and agents for light and heavy tasks.

## Heavy Tasks

Current exponent: `10`

| Rank | Model / Agent | Intelligence | Cost per task | Score |
| ---: | --- | ---: | ---: | ---: |
| 🥇 1 | gpt 6.1 sol max | 55 | 1.27 | 199.4m |
| 🥈 2 | gpt 6.1 sol high | 50 | 0.59 | 165.5m |
| 🥉 3 | gpt 6.1 terra max | 51 | 0.96 | 124m |
| 4 | gpt 6.1 sol medium | 46 | 0.36 | 117.8m |
| 5 | gpt 6 astra high | 55 | 3.24 | 78.2m |
| 6 | gpt 6.1 terra high | 42 | 0.26 | 65.7m |
| 7 | gpt 6 astra max | 57 | 6.24 | 58m |
| 8 | gpt 6 astra medium | 51 | 2.73 | 43.6m |
| 9 | opus 5.5 max | 58 | 10.04 | 42.9m |
| 10 | opus 5.5 high | 52 | 3.46 | 41.8m |
| 11 | gpt 6.1 terra medium | 38 | 0.17 | 36.9m |
| 12 | opus 5.5 medium | 48 | 2.45 | 26.5m |
| 13 | gemini 4 argon high | 50 | 3.84 | 25.4m |
| 14 | sonnet 5.5 max | 54 | 10.02 | 21m |
| 15 | kimi k3.1 pro | 46 | 3.68 | 11.5m |
| 16 | haiku 5.5 max | 36 | 0.41 | 8.9m |
| 17 | sonnet 5.5 high | 41 | 1.64 | 8.2m |
| 18 | fable 5.1 high | 47 | 7.56 | 7m |
| 19 | fable 5.1 max | 49 | 13.04 | 6.1m |
| 20 | fable 5.1 medium | 43 | 5.58 | 3.9m |
| 21 | haiku 5.5 high | 30 | 0.16 | 3.7m |
| 22 | muse wonder max | 43 | 6.95 | 3.1m |
| 23 | gpt 6 luna max | 28 | 0.15 | 2m |
| 24 | haiku 5.5 medium | 25 | 0.09 | 1.1m |
| 25 | sonnet 5.5 medium | 30 | 0.78 | 757k |
| 26 | grok 4.7 xhigh | 34 | 7.51 | 274.9k |
| 27 | gpt 6 luna high | 21 | 0.07 | 238.3k |
| 28 | gpt 6 luna medium | 18 | 0.04 | 89.3k |

## Light Tasks

Current exponent: `2`

| Rank | Model / Agent | Intelligence | Cost per task | Score |
| ---: | --- | ---: | ---: | ---: |
| 🥇 1 | gpt 6.1 terra medium | 38 | 0.17 | 8.5k |
| 🥈 2 | gpt 6 luna medium | 18 | 0.04 | 8.1k |
| 🥉 3 | haiku 5.5 medium | 25 | 0.09 | 6.9k |
| 4 | gpt 6.1 terra high | 42 | 0.26 | 6.8k |
| 5 | gpt 6 luna high | 21 | 0.07 | 6.3k |
| 6 | gpt 6.1 sol medium | 46 | 0.36 | 5.9k |
| 7 | haiku 5.5 high | 30 | 0.16 | 5.6k |
| 8 | gpt 6 luna max | 28 | 0.15 | 5.2k |
| 9 | gpt 6.1 sol high | 50 | 0.59 | 4.2k |
| 10 | haiku 5.5 max | 36 | 0.41 | 3.2k |
| 11 | gpt 6.1 terra max | 51 | 0.96 | 2.7k |
| 12 | gpt 6.1 sol max | 55 | 1.27 | 2.4k |
| 13 | sonnet 5.5 medium | 30 | 0.78 | 1.2k |
| 14 | sonnet 5.5 high | 41 | 1.64 | 1k |
| 15 | gpt 6 astra medium | 51 | 2.73 | 953 |
| 16 | opus 5.5 medium | 48 | 2.45 | 940 |
| 17 | gpt 6 astra high | 55 | 3.24 | 934 |
| 18 | opus 5.5 high | 52 | 3.46 | 782 |
| 19 | gemini 4 argon high | 50 | 3.84 | 651 |
| 20 | kimi k3.1 pro | 46 | 3.68 | 575 |
| 21 | gpt 6 astra max | 57 | 6.24 | 521 |
| 22 | opus 5.5 max | 58 | 10.04 | 335 |
| 23 | fable 5.1 medium | 43 | 5.58 | 331 |
| 24 | fable 5.1 high | 47 | 7.56 | 292 |
| 25 | sonnet 5.5 max | 54 | 10.02 | 291 |
| 26 | muse wonder max | 43 | 6.95 | 266 |
| 27 | fable 5.1 max | 49 | 13.04 | 184 |
| 28 | grok 4.7 xhigh | 34 | 7.51 | 154 |

## Where the Numbers Come From

[Artificial Analysis](https://artificialanalysis.ai/models) is the source of the Intelligence and Cost per task inputs in these tables.
It benchmarks AI models and reports measures such as intelligence, speed, and cost.
Its Intelligence Index combines multiple evaluations into a weighted measure of model capability;
see its [intelligence benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) for the benchmark definitions and weighting.

Data snapshot: Artificial Analysis Intelligence Index **v5.0**, verified on **2026-10-28**.

Intelligence is recorded at the source's displayed precision (a whole number), and Cost per task is recorded in **USD**, rounded to two decimal places.
Cost per task is the weighted average cost of running one Intelligence Index task, not a price per million tokens or a quote for your own workload.
When the index changes its evaluations or weights, both Intelligence and Cost per task can change even if API token prices stay the same.
Compare models within the same index version; scores from different versions are not directly comparable.

The selected model variants and their verified Artificial Analysis values are stored in `data.json`.
Model names are shortened for readability. Reasoning settings such as `medium`, `high`, `xhigh`, and `max` identify separate variants;
the Claude Opus 5.5, Sonnet 5.5, and Fable 5.1 entries use the source's default fallback configuration.
This project does not run those benchmarks or automatically refresh the inputs from the source.

## How This Project Ranks Models

The **Score** column and the resulting ranks are calculated by this project's own formulas, using the supplied Intelligence and Cost per task values.
These formulas combine capability and cost into a single score to help compare value for different task priorities.
They are project-defined metrics, not official Artificial Analysis scores or rankings.

Higher Intelligence increases the score; higher Cost per task decreases it. Higher scores rank better:

```text
heavy_score = intelligence ** heavy_exponent / cost_per_task / 1_000_000_000
light_score = intelligence ** light_exponent / cost_per_task
```

`**` means exponentiation. The default light-task exponent of 2 gives cost more influence relative to intelligence
than the heavy-task exponent of 10, which rewards increases in intelligence much more strongly.
Dividing the heavy-task score by one billion only changes its scale, not the ranking.
The exponents are configurable preferences, not benchmark-derived weights.
"Light" and "heavy" describe these scoring priorities; they are not separate task benchmarks run by this project.

Intelligence and Cost per task are source inputs; Score is a calculated comparison metric, not an accuracy percentage or a prediction of performance on every task.
Use comparable Intelligence benchmarks and consistent currency units and task definitions for Cost per task.
Cost per task must be positive. Exponents must be positive and may be fractional.

## Updating the Rankings

Requires Python 3.10 or later, with no external packages.

1. Check each exact model variant on Artificial Analysis and use the same Intelligence Index version for all entries. Record the displayed Intelligence and Cost per task in USD; do not substitute token pricing for Cost per task.
2. Edit the `models` array in `data.json`. Each entry contains `name` (text), `intelligence` (a nonnegative number), and `cost_per_task` (a positive number). Update `source.intelligence_index_version` and `source.verified_on` (YYYY-MM-DD) after verifying the complete snapshot.
3. Adjust `exponents.light` and `exponents.heavy` as needed. Their defaults are 2 and 10. Heavy-task scores are additionally divided by one billion.
4. Regenerate README.md, then inspect both tables:

```bash
python3 generate_readme.py
```

Rankings use unrounded calculated scores based on the stored inputs; source precision is limited as described above.
Scores below 1000 are displayed without decimal places.
Thousands, millions, and billions use `k`, `m`, and `b`, respectively, with up to one decimal place
(for example, 1500 becomes 1.5k, 1350000 becomes 1.4m, and 2300000000 becomes 2.3b).
Equal scores are ordered by model name for deterministic output.
README.md is generated. Edit `generate_readme.py` to change its static text.

## License

This project is licensed under the [MIT License](LICENSE).
