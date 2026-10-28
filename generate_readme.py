"""Generate README.md from manually supplied data; no external dependencies."""

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def number(value, label, *, allow_zero=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be a number")
    if not math.isfinite(value) or value < 0 or (value == 0 and not allow_zero):
        raise ValueError(f"{label} must be finite and {'nonnegative' if allow_zero else 'positive'}")
    return value


def cell(value):
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("|", "&#124;").replace("\n", " ").replace("\r", " ")


def format_score(score):
    for threshold, suffix in ((1_000_000_000, "b"), (1_000_000, "m"), (1_000, "k")):
        if score >= threshold:
            value = f"{score / threshold:.1f}".rstrip("0").rstrip(".")
            return f"{value}{suffix}"
    return f"{score:.0f}"


def generate(data):
    exponents = {
        kind: number(data["exponents"][kind], f"exponents.{kind}")
        for kind in ("light", "heavy")
    }
    models = data["models"]
    if not isinstance(models, list):
        raise ValueError("models must be a list")
    names = set()
    for model in models:
        name = model["name"]
        if not isinstance(name, str) or not name.strip() or name in names:
            raise ValueError("Model names must be nonempty, unique strings")
        names.add(name)
        number(model["intelligence"], f"{name}.intelligence", allow_zero=True)
        number(model["cost_per_task"], f"{name}.cost_per_task")

    intelligence_medals = dict(zip(
        sorted({model["intelligence"] for model in models}, reverse=True)[:3],
        ("🥇 ", "🥈 ", "🥉 "),
    ))
    cost_medals = dict(zip(
        sorted({model["cost_per_task"] for model in models})[:3],
        ("🥇 ", "🥈 ", "🥉 "),
    ))

    source = data.get("source")
    snapshot_note = (
        f"Data snapshot: Artificial Analysis Intelligence Index **v{cell(source['intelligence_index_version'])}**, "
        f"verified on **{cell(source['verified_on'])}**.\n\n"
        if source else ""
    )

    sections = ["""# AI Agent Rankings

![Decorative abstract chart with glowing curves; no real data is represented.](assets/ai-agent-rankings.png)

Compare user-selected AI models and agents for light and heavy tasks.

"""]
    for kind, title in (("heavy", "Heavy Tasks"), ("light", "Light Tasks")):
        exponent = exponents[kind]
        rows = []
        for model in models:
            score = model["intelligence"] ** exponent / model["cost_per_task"]
            if kind == "heavy":
                score /= 1_000_000_000
            if not math.isfinite(score):
                raise ValueError(f"Score overflow for {model['name']}")
            rows.append((model, score))
        rows.sort(key=lambda item: (-item[1], item[0]["name"].casefold(), item[0]["name"]))
        lines = [f"## {title}", "", f"Current exponent: `{exponent:g}`", ""]
        if rows:
            lines.extend([
                "| Rank | Model / Agent | Intelligence | Cost per task | Score |",
                "| ---: | --- | ---: | ---: | ---: |",
            ])
            for rank, (model, score) in enumerate(rows, 1):
                medal = {1: "🥇 ", 2: "🥈 ", 3: "🥉 "}.get(rank, "")
                intelligence = f"{intelligence_medals.get(model['intelligence'], '')}{model['intelligence']}"
                cost = f"{cost_medals.get(model['cost_per_task'], '')}{model['cost_per_task']}"
                lines.append(f"| {medal}{rank} | {cell(model['name'])} | {intelligence} | {cost} | {format_score(score)} |")
        else:
            lines.extend([
                "| Rank | Model / Agent | Intelligence | Cost per task | Score |",
                "| ---: | --- | ---: | ---: | ---: |",
                "", "No data has been supplied yet.",
            ])
        sections.append("\n".join(lines))
    sections.append(f"""## Where the Numbers Come From

[Artificial Analysis](https://artificialanalysis.ai/models) is the source of the Intelligence and Cost per task inputs in these tables.
It benchmarks AI models and reports measures such as intelligence, speed, and cost.
Its Intelligence Index combines multiple evaluations into a weighted measure of model capability;
see its [intelligence benchmarking methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking) for the benchmark definitions and weighting.

{snapshot_note}Intelligence is recorded at the source's displayed precision (a whole number), and Cost per task is recorded in **USD**, rounded to two decimal places.
Cost per task is the weighted average cost of running one Intelligence Index task, not a price per million tokens or a quote for your own workload.
When the index changes its evaluations or weights, both Intelligence and Cost per task can change even if API token prices stay the same.
Compare models within the same index version; scores from different versions are not directly comparable.

The selected model variants and their verified Artificial Analysis values are stored in `data.json`.
Model names are shortened for readability. Reasoning settings such as `medium`, `high`, `xhigh`, and `max` identify separate variants;
the Claude Opus 5.5, Sonnet 5.5, and Fable 5.1 entries use the source's default fallback configuration.
This project does not run those benchmarks or automatically refresh the inputs from the source.
""")
    sections.append("""## How This Project Ranks Models

The **Score** column and the resulting ranks are calculated by this project's own formulas, using the supplied Intelligence and Cost per task values.
These formulas combine capability and cost into a single score to help compare value for different task priorities.
They are project-defined metrics, not official Artificial Analysis scores or rankings.

Higher Intelligence increases the score; higher Cost per task decreases it. Higher scores rank better:

```text
heavy_score = intelligence ** heavy_exponent / cost_per_task / 1_000_000_000
light_score = intelligence ** light_exponent / cost_per_task
```

Medals in the Intelligence column mark the three highest distinct values; medals in Cost per task mark the three lowest distinct values.
Equal values share a medal. These column medals are independent of the overall Rank.

`**` means exponentiation. The default light-task exponent of 2 gives cost more influence relative to intelligence
than the heavy-task exponent of 10, which rewards increases in intelligence much more strongly.
Dividing the heavy-task score by one billion only changes its scale, not the ranking.
The exponents are configurable preferences, not benchmark-derived weights.
"Light" and "heavy" describe these scoring priorities; they are not separate task benchmarks run by this project.

Intelligence and Cost per task are source inputs; Score is a calculated comparison metric, not an accuracy percentage or a prediction of performance on every task.
Use comparable Intelligence benchmarks and consistent currency units and task definitions for Cost per task.
Cost per task must be positive. Exponents must be positive and may be fractional.
""")
    sections.append("""## Updating the Rankings

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
""")
    return "\n\n".join(section.strip() for section in sections) + "\n"


def main():
    try:
        data = json.loads((ROOT / "data.json").read_text(encoding="utf-8"))
        output = generate(data)
    except (ValueError, KeyError, TypeError, OverflowError) as error:
        raise SystemExit(f"Invalid data.json: {error}") from error
    (ROOT / "README.md").write_text(output, encoding="utf-8")


if __name__ == "__main__":
    main()
