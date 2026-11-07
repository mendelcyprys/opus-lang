# opus-lang — learning 8 languages with Claude
Persistent state for a multi-language tutoring course: Polish, Ukrainian, Hebrew, Arabic, Spanish, French, German, Japanese.
See `CLAUDE.md` for how sessions work.

**How to start a chat:** name the language ("Polish", "let's do Hebrew", "日本語") — or just say hi and Claude
offers the languages with the most reviews due.

- `learner.md` – who I am & preferences shared by all languages · `languages.md` – level & focus per language
- `languages/<lang>/` – everything for one language: `LANGUAGE.md` (teaching notes), `profile.md`, `plan.md`,
  `progress/` (vocabulary, grammar, mistakes, review queue; `review-later.md` + `archive/` hold far-off and finished items),
  `sessions/`, `exports/anki.csv`, and `tools/` (practice page + `round.json`; Polish, Arabic, Japanese, Hebrew so far)
- `scripts/status.py` – reviews due per language · `scripts/export_anki.py <lang>|--all` – Anki export
- `scripts/tidy.py <lang>|--all` – keeps the start-of-session files small (archives, never deletes)
- `scripts/build_round.py <lang>` – `tools/round.json` → the exercises in that language's practice page
- `templates/` – blank files (session log, new language)
