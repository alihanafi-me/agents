# AI Agent Rankings

![Decorative abstract chart with glowing curves; no real data is represented.](assets/ai-agent-rankings.png)

Compare user-selected AI models and agents for light and heavy tasks.

## Heavy Tasks

Current exponent: `10`

| Rank | Model / Agent | Intelligence | Cost per task | Score |
| ---: | --- | ---: | ---: | ---: |
| 🥇 1 | gpt 6.1 sol medium | 48 | 0.21 | 309.2m |
| 🥈 2 | gpt 6.1 sol high | 50 | 0.32 | 305.2m |
| 🥉 3 | gpt 6.1 sol max | 52 | 0.72 | 200.8m |
| 4 | kimi k3.1 pro | 55 | 2.11 | 120m |
| 5 | opus 5.5 high | 54 | 1.82 | 115.8m |
| 6 | haiku 5.5 max | 43 | 0.21 | 102.9m |
| 7 | gpt 6 luna max | 38 | 0.07 | 89.7m |
| 8 | opus 5.5 medium | 51 | 1.34 | 88.8m |
| 9 | gemini 4 argon high | 53 | 1.99 | 87.9m |
| 10 | haiku 5.5 high | 38 | 0.08 | 78.5m |
| 11 | opus 5.5 max | 58 | 5.98 | 72m |
| 12 | gpt 6 astra high | 51 | 1.73 | 68.8m |
| 13 | gpt 6 astra medium | 50 | 1.54 | 63.4m |
| 14 | sonnet 5.5 high | 47 | 0.88 | 59.8m |
| 15 | sonnet 5.5 max | 56 | 5.46 | 55.6m |
| 16 | gpt 6 astra max | 53 | 3.26 | 53.6m |
| 17 | gpt 6 luna high | 33 | 0.03 | 51.1m |
| 18 | haiku 5.5 medium | 34 | 0.05 | 41.3m |
| 19 | muse wonder max | 52 | 4.52 | 32m |
| 20 | fable 5.1 high | 51 | 3.91 | 30.4m |
| 21 | gpt 6 luna medium | 30 | 0.02 | 29.5m |
| 22 | sonnet 5.5 medium | 41 | 0.48 | 28m |
| 23 | fable 5.1 medium | 49 | 2.98 | 26.8m |
| 24 | fable 5.1 max | 53 | 7.63 | 22.9m |
| 25 | grok 4.7 xhigh | 46 | 3.74 | 11.3m |

## Light Tasks

Current exponent: `2`

| Rank | Model / Agent | Intelligence | Cost per task | Score |
| ---: | --- | ---: | ---: | ---: |
| 🥇 1 | gpt 6 luna medium | 30 | 0.02 | 45k |
| 🥈 2 | gpt 6 luna high | 33 | 0.03 | 36.3k |
| 🥉 3 | haiku 5.5 medium | 34 | 0.05 | 23.1k |
| 4 | gpt 6 luna max | 38 | 0.07 | 20.6k |
| 5 | haiku 5.5 high | 38 | 0.08 | 18.1k |
| 6 | gpt 6.1 sol medium | 48 | 0.21 | 11k |
| 7 | haiku 5.5 max | 43 | 0.21 | 8.8k |
| 8 | gpt 6.1 sol high | 50 | 0.32 | 7.8k |
| 9 | gpt 6.1 sol max | 52 | 0.72 | 3.8k |
| 10 | sonnet 5.5 medium | 41 | 0.48 | 3.5k |
| 11 | sonnet 5.5 high | 47 | 0.88 | 2.5k |
| 12 | opus 5.5 medium | 51 | 1.34 | 1.9k |
| 13 | gpt 6 astra medium | 50 | 1.54 | 1.6k |
| 14 | opus 5.5 high | 54 | 1.82 | 1.6k |
| 15 | gpt 6 astra high | 51 | 1.73 | 1.5k |
| 16 | kimi k3.1 pro | 55 | 2.11 | 1.4k |
| 17 | gemini 4 argon high | 53 | 1.99 | 1.4k |
| 18 | gpt 6 astra max | 53 | 3.26 | 862 |
| 19 | fable 5.1 medium | 49 | 2.98 | 806 |
| 20 | fable 5.1 high | 51 | 3.91 | 665 |
| 21 | muse wonder max | 52 | 4.52 | 598 |
| 22 | sonnet 5.5 max | 56 | 5.46 | 574 |
| 23 | grok 4.7 xhigh | 46 | 3.74 | 566 |
| 24 | opus 5.5 max | 58 | 5.98 | 563 |
| 25 | fable 5.1 max | 53 | 7.63 | 368 |

## Where the Numbers Come From

[Artificial Analysis](https://artificialanalysis.ai/) is the source of the Intelligence and Cost per task inputs in these tables.
It benchmarks AI models and reports measures such as intelligence, speed, and cost.
Its Intelligence Index combines multiple evaluations into a weighted measure of model capability;
see its [intelligence benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) for the benchmark definitions and weighting.

We manually supply the selected model names and source values in `data.json`.
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

1. Edit the `models` array in `data.json`. Each entry contains `name` (text), `intelligence` (a nonnegative number), and `cost_per_task` (a positive number).
2. Adjust `exponents.light` and `exponents.heavy` as needed. Their defaults are 2 and 10. Heavy-task scores are additionally divided by one billion.
3. Regenerate README.md:

```bash
python3 generate_readme.py
```

Rankings use unrounded scores. Scores below 1000 are displayed without decimal places.
Thousands, millions, and billions use `k`, `m`, and `b`, respectively, with up to one decimal place
(for example, 1500 becomes 1.5k, 1350000 becomes 1.4m, and 2300000000 becomes 2.3b).
Equal scores are ordered by model name for deterministic output.
README.md is generated. Edit `generate_readme.py` to change its static text.

## License

This project is licensed under the [MIT License](LICENSE).
