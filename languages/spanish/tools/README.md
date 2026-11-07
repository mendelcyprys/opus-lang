# Practice page (Spanish)

`spanish-practice.html` — Artifact page for Spanish rounds (relay/grading rules as in `languages/arabic/tools/README.md`).
URL: https://claude.ai/artifact/VDBDuAjK6nQpxjnCBfNpeY · always republish with `capabilities: {"sample": {}, "comments": {}}`.
Built 2026-11-07 from the French page: **same code**, only `<title>`, accent colours and the `CONFIG` block differ.

## Per session (round.json fast path)
1. Write `tools/round.json` (6 mc, 3 build, 3 type; prompt lines in Spanish start with `> ` to show large).
2. `python3 scripts/build_round.py spanish` → rewrites ITEMS/MODEL.
3. Publish the same file path, grade the relayed round in the chat, add valid variants to `a:[...]`. Commit.
