#!/usr/bin/env python3
"""Keep the files Claude must read at session start small. History is moved, never deleted.

Usage: python3 scripts/tidy.py <lang> [<lang> ...] | --all   [--date YYYY-MM-DD] [--dry-run]

What it does, per language (languages/<lang>/progress/):
  review-queue.md   rows whose next due date is more than 14 days away -> review-later.md
                    (rows in review-later.md that come within 14 days move back). status.py reads both files.
  mistakes.md       rows with status "fixed" -> archive/mistakes.md
  grammar.md        rows marked "superseded", or mastery 4 and last reviewed >= 14 days ago -> archive/grammar.md
  vocabulary.md     same rule -> archive/vocabulary.md   (export_anki.py reads the archive too)
  long cells (> 170 chars) in mistakes.md / grammar.md / vocabulary.md are compacted to "start … latest";
  the full original row is saved in archive/<file>.md first (so nothing is lost).
Idempotent: running it twice changes nothing the second time.
Sessions do NOT read archive/ or review-later.md at start; grep them when you need history.
"""
import datetime as dt, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LANGS = ROOT / "languages"
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
HORIZON = 14        # days: queue rows due later than this live in review-later.md
MASTERED_AGE = 14   # days since last review before a mastery-4 row is archived
MAXCELL = 170
SEP = " … "


def split_table(text):
    """-> (before_lines, header_cells, sep_line, rows(raw lines), after_lines) for the first table, or None."""
    lines = text.split("\n")
    start = next((i for i, l in enumerate(lines) if l.lstrip().startswith("|")), None)
    if start is None or start + 1 >= len(lines):
        return None
    end = start
    while end < len(lines) and lines[end].lstrip().startswith("|"):
        end += 1
    header = [c.strip().lower() for c in lines[start].strip().strip("|").split("|")]
    return lines[:start], header, lines[start], lines[start + 1], lines[start + 2:end], lines[end:]


def cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]


def colidx(header, prefix):
    return next((i for i, h in enumerate(header) if h.startswith(prefix)), None)


def compact_cell(c):
    if len(c) <= MAXCELL or SEP in c:
        return c
    head = c[:70].rsplit(" ", 1)[0]
    tail = c[-80:]
    tail = tail.split(" ", 1)[1] if " " in tail else tail
    return head + SEP + tail


def archive_append(path, header_line, sep_line, rows, dry):
    """Append rows not already present to an archive table (creates it with the same header)."""
    if not rows or dry:
        return
    path.parent.mkdir(exist_ok=True)
    old = path.read_text(encoding="utf-8") if path.exists() else (
        f"# Archive — {path.stem}\n\n_Moved here by scripts/tidy.py. Not read at session start; grep when you need history._\n\n{header_line}\n{sep_line}\n")
    have = set(old.split("\n"))
    new = [r for r in rows if r not in have]
    if new:
        path.write_text(old.rstrip("\n") + "\n" + "\n".join(new) + "\n", encoding="utf-8")


def tidy_file(path, archive, keep_rule, dry, compact=True):
    """keep_rule(header, cells) -> True to archive the row. Returns (n_archived, n_compacted)."""
    if not path.exists():
        return 0, 0
    parts = split_table(path.read_text(encoding="utf-8"))
    if not parts:
        return 0, 0
    before, header, hline, sline, rows, after = parts
    keep, moved, full, nc = [], [], [], 0
    for r in rows:
        cs = cells(r)
        if keep_rule and keep_rule(header, cs):
            moved.append(r)
            continue
        if compact:
            new = [cs[0]] + [compact_cell(c) for c in cs[1:]]
            if new != cs:
                nc += 1
                full.append(r)
                r = "| " + " | ".join(new) + " |"
        keep.append(r)
    if (moved or full) and not dry:
        archive_append(archive, hline, sline, moved + full, dry)
        path.write_text("\n".join(before + [hline, sline] + keep + after), encoding="utf-8")
    return len(moved), nc


def is_mastered(today):
    def rule(header, cs):
        row = " ".join(cs).lower()
        if "superseded" in row:
            return True
        mi, li = colidx(header, "mastery"), colidx(header, "last reviewed")
        if mi is None or mi >= len(cs) or not cs[mi].startswith("4"):
            return False
        m = DATE.search(cs[li]) if li is not None and li < len(cs) else None
        return bool(m) and (today - dt.date.fromisoformat(m.group())).days >= MASTERED_AGE
    return rule


def is_fixed(header, cs):
    si = colidx(header, "status")
    return si is not None and si < len(cs) and cs[si].lower().startswith("fixed")


def split_queue(d, today, dry):
    qp, lp = d / "progress" / "review-queue.md", d / "progress" / "review-later.md"
    if not qp.exists():
        return 0, 0
    qparts = split_table(qp.read_text(encoding="utf-8"))
    if not qparts:
        return 0, 0
    before, header, hline, sline, rows, after = qparts
    di = colidx(header, "next due")
    lrows = []
    if lp.exists():
        lparts = split_table(lp.read_text(encoding="utf-8"))
        lrows = lparts[4] if lparts else []
    limit = today + dt.timedelta(days=HORIZON)

    def due(r):
        m = DATE.search(cells(r)[di]) if di is not None and di < len(cells(r)) else None
        return dt.date.fromisoformat(m.group()) if m else None

    go_later = [r for r in rows if due(r) and due(r) > limit]
    come_back = [r for r in lrows if due(r) and due(r) <= limit]
    if not (go_later or come_back):
        return 0, 0
    if dry:
        return len(go_later), len(come_back)
    new_q = [r for r in rows if r not in go_later] + come_back
    new_l = [r for r in lrows if r not in come_back] + go_later
    new_q.sort(key=lambda r: due(r) or dt.date.max)
    new_l.sort(key=lambda r: due(r) or dt.date.max)
    qp.write_text("\n".join(before + [hline, sline] + new_q + after), encoding="utf-8")
    ltxt = ("# Review Queue — later (not due within %d days)\n\n_Moved by scripts/tidy.py; moves back into review-queue.md when it comes within %d days. "
            "status.py counts these too. Not read at session start._\n\n" % (HORIZON, HORIZON))
    lp.write_text(ltxt + "\n".join([hline, sline] + new_l) + "\n", encoding="utf-8")
    return len(go_later), len(come_back)


def tidy(lang, today, dry):
    d = LANGS / lang
    p = d / "progress"
    a = p / "archive"
    out = []
    g, b = split_queue(d, today, dry)
    out.append(f"queue: {g} -> later, {b} back")
    for name, rule in (("mistakes", is_fixed), ("grammar", is_mastered(today)), ("vocabulary", is_mastered(today))):
        n, c = tidy_file(p / f"{name}.md", a / f"{name}.md", rule, dry)
        out.append(f"{name}: {n} archived, {c} compacted")
    print(f"{lang}: " + "; ".join(out) + (" (dry run)" if dry else ""))


def main():
    args = sys.argv[1:]
    dry = "--dry-run" in args
    today = dt.date.today()
    if "--date" in args:
        i = args.index("--date")
        today = dt.date.fromisoformat(args[i + 1])
        del args[i:i + 2]
    args = [a for a in args if a != "--dry-run"]
    if not args:
        sys.exit(__doc__)
    langs = sorted(p.name for p in LANGS.iterdir() if (p / "LANGUAGE.md").exists()) if args == ["--all"] else [a.lower() for a in args]
    for lang in langs:
        tidy(lang, today, dry)


if __name__ == "__main__":
    main()
