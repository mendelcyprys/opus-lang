#!/usr/bin/env python3
"""Show, per language: status, level, review items due, last session — and a suggested order.

Usage: python3 scripts/status.py [--date YYYY-MM-DD]
Used by Claude at session start to suggest which language to study (see CLAUDE.md → Language router).
"""
import datetime as dt, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LANGS = ROOT / "languages"
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


def table(path):
    """Yield dict rows (lower-cased headers) from the first markdown table in a file."""
    header = None
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("|"):
            if header:
                return
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if header is None:
            header = [h.lower() for h in cells]
        elif not set("".join(cells)) <= set("-: "):
            yield dict(zip(header, cells))


def col(row, prefix):
    return next((v for k, v in row.items() if k.startswith(prefix)), "")


def main():
    today = dt.date.today()
    if "--date" in sys.argv:
        today = dt.date.fromisoformat(sys.argv[sys.argv.index("--date") + 1])
    dash = {col(r, "language").lower(): r for r in table(ROOT / "languages.md")}
    out = []
    for d in sorted(p for p in LANGS.iterdir() if (p / "LANGUAGE.md").exists()):
        due = 0
        for r in table(d / "progress" / "review-queue.md"):
            m = DATE.search(col(r, "next due"))
            if m and dt.date.fromisoformat(m.group()) <= today:
                due += 1
        dates = sorted(f.name[:10] for f in (d / "sessions").glob("*.md") if DATE.match(f.name))
        r = dash.get(d.name, {})
        out.append(dict(lang=d.name, status=col(r, "status") or "?", level=col(r, "level") or "?",
                        due=due, last=dates[-1] if dates else "—", n=len(dates)))
    # Suggested order: active languages by most due, then most recent; then the rest (not started/paused).
    active = sorted((o for o in out if o["status"] == "active"),
                    key=lambda o: (o["due"], o["last"] if o["n"] else ""), reverse=True)
    rest = [o for o in out if o["status"] != "active"]
    print(f"Today: {today}")
    print(f"{'Language':<11} {'Status':<12} {'Due':>3}  {'Last':<10} {'#':>3}  Level")
    for o in active + rest:
        print(f"{o['lang']:<11} {o['status']:<12} {o['due']:>3}  {o['last']:<10} {o['n']:>3}  {o['level']}")
    print("Suggested order:", ", ".join(o["lang"] for o in active + rest))


if __name__ == "__main__":
    main()
