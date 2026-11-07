# Practice page (Ukrainian)

`ukrainian-practice.html` — Artifact page for Ukrainian rounds (relay/grading rules as in `languages/arabic/tools/README.md`).
URL: https://claude.ai/artifact/SKjrYxv7nzVoxyAbbypS9i · always republish with `capabilities: {"sample": {}, "comments": {}}`.
Built 2026-11-07. **Shares its code with `languages/french/tools/french-practice.html`**: the only differences are the `CONFIG` block
(between `CONFIG:BEGIN` / `CONFIG:END`), the `<title>` and the accent colours. Fix bugs in both.

## Keyboard
- Clickable keyboard in the **macOS "Ukrainian" layout** (Apple's current default = the Windows/PC arrangement; called "Ukrainian – PC" before):
  ЙЦУКЕН letters, ґ on the `` ` `` key (ISO keyboards: between left Shift and Z — `IntlBackslash` is mapped too), apostrophe **ʼ** (U+02BC) on `\`,
  full stop on `/` (Shift = comma). "Ukrainian – Legacy" swaps ґ and the apostrophe; "Ukrainian – QWERTY" is phonetic.
- **Laptop keys → Ukrainian:** with the Mac still on English, physical keys are mapped by `KeyboardEvent.code`; the letter case follows what the OS produced
  (Shift or Caps Lock). If the OS is already in a Cyrillic layout the native input is left alone; phone keyboards (no key code) are never touched.
- Shown by default on laptops, hidden on touch (toggle). Toggles + text size remembered in localStorage (`ukKbOpen`, `ukKbLatin`, `ukMapKeys`, `ukSize`).

## Checking
- `strict()`: case-insensitive, **stress marks (U+0301) ignored**, all apostrophe variants (' ’ ‘ ʼ `) equal, punctuation ignored.
- `loose()` (= "Right words, spelling slip"): also folds і/и/ї, е/є, г/ґ, drops the apostrophe, maps Latin look-alikes (i, a, o, c …) and Russian ы э ё ъ.
  So *овочи*, *пять*, a Latin *i* or a Russian *ы* show as spelling slips, not as wrong words — still count as misses; log them.
- Prompt lines containing Cyrillic are shown large automatically.

## Per session (round.json fast path)
1. Write `tools/round.json` (format: header of `scripts/build_round.py`; 6 mc, 3 build, 3 type). Stress-mark new words in prompts (вокза́л).
2. `python3 scripts/build_round.py ukrainian` → rewrites ITEMS/MODEL.
3. Publish the same file path (`capabilities: {"sample":{},"comments":{}}`), grade the relayed round in the chat, add valid variants
   (word order, та/і/й, -ся/-сь) to `a:[...]` / `alt:[...]`. Commit `round.json` + the page.
