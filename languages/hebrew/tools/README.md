# Practice page (Hebrew)

`hebrew-practice.html` — Artifact page for Hebrew rounds, ported from `languages/japanese/tools/japanese-practice.html`
(same relay/grading rules as the Arabic page — see `languages/arabic/tools/README.md`).
URL: https://claude.ai/artifact/5wQf8mza4uZNkHhT7tKJh8 · always republish with `capabilities: {"sample": {}, "comments": {}}`.

## What is different
- **RTL:** each prompt line gets its own block (`dir=auto`), so English and Hebrew lines don't scramble; Hebrew options/tiles/input are `dir=rtl`.
  An mc option starting with a Latin letter is shown LTR (English answers, e.g. reading comprehension). `"עברית\ngloss"` puts a small gloss under an option —
  don't add glosses that give the answer away.
- **Keyboard (requested 2026-11-07; learner forgets the Hebrew mapping on the laptop):**
  - Clickable on-screen keyboard in the **macOS "Hebrew" layout** (letter keys identical to SI-1452: e→ק r→ר t→א y→ט u→ו i→ן o→ם p→פ /
    a→ש s→ד d→ג f→כ g→ע h→י j→ח k→ל l→ך ;→ף / z→ז x→ס c→ב v→ה b→נ n→מ m→צ ,→ת .→ץ; q→/ w→' '→, /→.).
    Small Latin labels show the physical key (toggle "Latin key labels") so the layout gets learned; final-form keys have a bottom shadow.
  - **Laptop keys → Hebrew:** with the Mac still set to English, physical keys are mapped by `KeyboardEvent.code` to that layout; the pressed key flashes on the
    on-screen keyboard. If the OS is already in Hebrew the native input is left alone. Phone keyboards send no key code → untouched.
  - Keyboard shown by default on pointer:fine devices, hidden on touch (toggle "Show keyboard"). Toggles remembered in localStorage (`heKbOpen`, `heKbLatin`, `heMapKeys`).
- **Checking:** `strict()` strips niqqud/cantillation, spaces and punctuation (incl. geresh/gershayim, maqaf); `loose()` also folds final letters ך ם ן ף ץ →
  "Right words, final-letter slip". Plene vs defective spelling is NOT folded (it's a tracked mistake) — add accepted variants to `a:[...]` if needed.

## Per session (round.json fast path)
1. Write `tools/round.json` (format: header of `scripts/build_round.py`; 6 mc, 3 build, 3 type works well).
2. `python3 scripts/build_round.py hebrew` → rewrites the ITEMS/MODEL blocks.
3. Publish the same file path with the Artifact tool (`capabilities: {"sample":{},"comments":{}}`), grade the round in the chat when it arrives,
   add valid variants (word order, synonyms) to `a:[...]` / `alt:[...]`. Commit `round.json` + the page.
