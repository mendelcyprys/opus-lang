# Practice page (French)

`french-practice.html` — Artifact page for French rounds (relay/grading rules as in `languages/arabic/tools/README.md`).
URL: https://claude.ai/artifact/QHy2s14qAEZrCqeF1GWgFu · always republish with `capabilities: {"sample": {}, "comments": {}}`.
Built 2026-11-07. **Shares its code with `languages/ukrainian/tools/ukrainian-practice.html`**: only the `CONFIG` block, `<title>` and accent colours differ.

## Typing accents
- No full keyboard (Latin script): an **accent bar** é è ê ë à â ç î ï ô û ù œ inserts at the cursor, plus a reminder of the Mac US-keyboard dead keys
  (⌥e é · ⌥` à è ù · ⌥i â ê î ô û · ⌥u ë ï · ⌥c ç · ⌥q œ). Phone: long-press.

## Checking
- `strict()`: case-insensitive, punctuation/apostrophes/hyphens ignored (j'habite = j habite, est-ce = est ce), œ = oe; **accents kept**.
- `loose()` strips accents → "Right words, accent slip" (still a miss; log it in `mistakes.md` as spelling).
- **Prompt lines in French:** start the line with `> ` in round.json to show it large (French can't be detected by script).

## Per session (round.json fast path)
1. Write `tools/round.json` (format: header of `scripts/build_round.py`; 6 mc, 3 build, 3 type).
2. `python3 scripts/build_round.py french` → rewrites ITEMS/MODEL.
3. Publish the same file path (`capabilities: {"sample":{},"comments":{}}`), grade the relayed round in the chat, add valid variants to `a:[...]`. Commit.
