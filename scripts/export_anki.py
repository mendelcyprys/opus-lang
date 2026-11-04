#!/usr/bin/env python3
"""Export languages/<lang>/progress/vocabulary.md to an Anki-importable TSV.

Usage:  python3 scripts/export_anki.py <lang> [<lang> ...]   |   python3 scripts/export_anki.py --all
Output: languages/<lang>/exports/anki.csv
Anki:   File → Import, separator = Tab, fields: Front, Back, Reading, Grammar, Example, Tags.

The first column of the vocabulary table is the target-language term whatever its header
(Polish, Hebrew (with niqqud), Japanese, …). Optional "Reading"/"Transliteration" column → Reading field.
Rows marked "superseded" are skipped.
"""
import csv, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LANGS = ROOT / "languages"


def rows(src):
    header = None
    for line in src.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if header is None:
            header = [h.lower() for h in cells]
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        if cells and cells[0] and "superseded" not in line.lower():
            yield header, cells


def export(lang):
    src = LANGS / lang / "progress" / "vocabulary.md"
    if not src.exists():
        sys.exit(f"No vocabulary file for '{lang}' ({src.relative_to(ROOT)})")
    out = LANGS / lang / "exports" / "anki.csv"
    cards = []
    for header, cells in rows(src):
        rec = dict(zip(header, cells))
        g = lambda *keys: next((v for h, v in rec.items() if any(h.startswith(k) for k in keys)), "")
        mastery = g("mastery") or "0"
        cards.append([cells[0], g("english"), g("reading", "translit"), g("grammar"), g("example"),
                      f"{lang} mastery::{mastery}"])
    if not cards:
        print(f"{lang}: no vocabulary yet — skipped")
        return
    out.parent.mkdir(exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        csv.writer(f, delimiter="\t").writerows(cards)
    print(f"{lang}: wrote {len(cards)} cards to {out.relative_to(ROOT)}")


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    langs = sorted(p.name for p in LANGS.iterdir() if p.is_dir()) if args == ["--all"] else [a.lower() for a in args]
    for lang in langs:
        export(lang)


if __name__ == "__main__":
    main()
