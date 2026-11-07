# Practice page (Polish)

`polish-practice.html` — Artifact page derived from `languages/arabic/tools/arabic-practice.html` (see its README for the capabilities, relay and grading rules).
URL: https://claude.ai/artifact/5sJJsNkwBdeCJsFHEPMSpq · always republish with `capabilities: {"sample": {}, "comments": {}}`.

## Differences from the Arabic page
- LTR Latin text, one font (Source Sans 3); A−/A+ still scales all text.
- Answer check: `strict()` lower-cases and ignores punctuation but **keeps diacritics**; `loose()` folds ą ę ó ł ś ć ń ź ż. Equal under `loose` only = "Right words, spelling slip" (learner drops diacritics on the phone).
- Feedback prompts (`LEARNER`, weak spots) are Polish-specific: B1, simple Polish + English, masculine forms.

## Per session
Edit the `ITEMS` array (6 multiple choice with the correct option first in the source, 6 typed with every valid variant in `a:[...]`) and `MODEL` (displayed answers),
then republish the same file path. When results arrive, grade them in the chat (see `learner.md`), and add any valid alternative the page rejected.

## Porting to another language
Copy the page, change: title/h1, fonts and `direction`, `lang` on the input, `strict/loose`, the `LEARNER` prompt, the weak-spots sentence, the "spelling slip" hint, `ITEMS`/`MODEL`.
