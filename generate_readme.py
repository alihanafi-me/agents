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

    sections = ["""# AI Agent Rankings

Compare user-selected AI models and agents for light and heavy tasks.
Model names, Intelligence scores, and Cost per task values are supplied manually by the project owner from Artificial Analysis.

Higher scores rank better:

```text
heavy_score = intelligence ** heavy_exponent / cost_per_task / 1_000_000_000
light_score = intelligence ** light_exponent / cost_per_task
```

Use comparable Intelligence benchmarks and consistent currency units and task definitions for Cost per task.
Cost per task must be positive. Exponents must be positive and may be fractional.
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
                medal = {1: " 🥇", 2: " 🥈", 3: " 🥉"}.get(rank, "")
                lines.append(f"| {rank}{medal} | {cell(model['name'])} | {model['intelligence']} | {model['cost_per_task']} | {format_score(score)} |")
        else:
            lines.extend([
                "| Rank | Model / Agent | Intelligence | Cost per task | Score |",
                "| ---: | --- | ---: | ---: | ---: |",
                "", "No data has been supplied yet.",
            ])
        sections.append("\n".join(lines))
    sections.append("""## Updating the Rankings

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
