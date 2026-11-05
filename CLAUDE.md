# Opus-lang — Multi-language tutoring: instructions for Claude

This repo is the persistent memory of an ongoing tutoring relationship covering **8 languages**, each at its own level.
Every chat starts fresh, so **these files are the only continuity**. Treat them as the source of truth.

## Layout
| Path | What |
|---|---|
| `learner.md` | **Shared** learner profile: native language, interests, device, format & correction preferences (apply to every language) |
| `languages.md` | Dashboard: level, current focus, last session for each language |
| `languages/<lang>/LANGUAGE.md` | How to teach *this* language: script & typing, notation in files, onboarding questions, grammar map, pitfalls, references |
| `languages/<lang>/profile.md` | Language-specific facts & preferences (status, level, goal, variety, script support, explanation-language mix) |
| `languages/<lang>/plan.md` | Milestones, roadmap, next session |
| `languages/<lang>/progress/` | `vocabulary.md`, `grammar.md`, `mistakes.md`, `review-queue.md` |
| `languages/<lang>/sessions/` | One log per session: `YYYY-MM-DD-<topic>.md` |
| `languages/<lang>/exports/anki.csv` | Anki export of that language's vocabulary |
| `templates/` | Session template + blank files for adding a new language |
| `scripts/status.py` | Due reviews + last session per language (used to suggest a language) |
| `scripts/export_anki.py` | Vocabulary → Anki TSV |

## 1. Language router — do this first in every chat
| Language | Folder | Recognize as | TTS tag (BCP 47) |
|---|---|---|---|
| Polish | `languages/polish` | Polish, polski, PL | `pl-PL` |
| Ukrainian | `languages/ukrainian` | Ukrainian, українська, укр, UA | `uk-UA` |
| Hebrew | `languages/hebrew` | Hebrew, עברית, ivrit, HE | `he-IL` |
| Arabic | `languages/arabic` | Arabic, العربية, arabi, AR | `ar-SA` (MSA; dialect tag in its profile) |
| Spanish | `languages/spanish` | Spanish, español, castellano, ES | `es-ES` (variety in its profile) |
| French | `languages/french` | French, français, FR | `fr-FR` |
| German | `languages/german` | German, Deutsch, DE | `de-DE` |
| Japanese | `languages/japanese` | Japanese, 日本語, nihongo, JA/JP | `ja-JP` |

1. **Sync:** `git fetch origin main && git checkout -B main origin/main`.
2. **Learner named a language** (any form above, or simply writes in it) → use it.
   "Continue" / "same as last time" → the language with the most recent session (see `python3 scripts/status.py`).
3. **No language named** → run `python3 scripts/status.py`, then ask with **one** `AskUserQuestion` (header `Language`):
   4 options = the first 4 languages in the script's suggested order, the first marked "(Recommended)", each description
   showing level · reviews due · last session. The automatic "Other" field covers the remaining languages —
   match whatever they type against the router.
4. **Load only that language's files** (plus `learner.md`). Don't read other languages' progress — it wastes context and invites mix-ups.
5. Name the active language in your greeting (e.g. "**Polish** — last time we…").

**Golden rule:** everything you write goes under the active `languages/<lang>/` folder — except `learner.md`
(preferences that apply to all languages) and the language's own row in `languages.md`.
Never put one language's items in another language's files.

**Switching mid-chat** ("let's do French now"): first run the end-of-session steps for the current language
(session log, progress files, commit + push), then route to the new language from step 4. One session file per language per day.

## 2. At the start of a session (after routing)
1. Read `learner.md`, then `languages/<lang>/LANGUAGE.md`, `profile.md`, `plan.md` and all four `progress/` files.
2. Skim the most recent 1–2 files in `languages/<lang>/sessions/`.
3. Greet briefly, mention where we left off, and propose today's activity (start with due items from `review-queue.md`).
   If the language's `profile.md` has **Status: not started**, run onboarding for it instead (next section).

## 3. Onboarding a new language (first session in it)
- Don't re-ask anything already in `learner.md` (native language, interests, device, format/correction preferences).
- Ask only (via `AskUserQuestion` where possible): self-assessed level per skill, goal / why this language, and the
  **Onboarding questions** listed in that language's `LANGUAGE.md` (variety/dialect, script knowledge, …).
- Then a short placement test pitched at the self-assessed level (mobile: AskUserQuestion MC + a few typed items).
  An absolute beginner skips placement and starts with the script/sound system from the **Grammar map**.
- Log the result in `plan.md` (milestones), `profile.md` (level; set **Status: active**, **Started:** date) and `languages.md`;
  draft the roadmap in `plan.md` from the **Grammar map** in `LANGUAGE.md`.

## 4. During the session
- Follow `learner.md`; the language's `profile.md` overrides it where they differ (e.g. more English for a beginner language).
- Follow the notation rules in `LANGUAGE.md` (diacritics, stress marks, niqqud/harakat, furigana, transliteration).
- Note new words/phrases/grammar introduced and how well the learner did.
- **Cross-language:** the learner studies 8 languages. Use contrasts when they help (Polish↔Ukrainian cognates,
  Hebrew↔Arabic shared roots, Spanish↔French) and flag false friends. Log interference errors in `mistakes.md`
  with category `interference (<other language>)`.

## 5. At the end of every session (or when the learner says stop / after a substantial chunk)
1. Create `languages/<lang>/sessions/YYYY-MM-DD-<short-topic>.md` from `templates/session.md`.
2. Update `progress/vocabulary.md`, `progress/grammar.md` (new items, mastery changes, dates)
   and `progress/mistakes.md` (new or recurring error patterns).
3. Update `progress/review-queue.md` with spaced-repetition due dates
   (intervals: 1d → 3d → 7d → 14d → 30d → 90d; reset to 1d on a miss).
4. Update `plan.md` and the language's `profile.md`. Update `learner.md` only for things that hold for every language
   (format, device, correction style, interests); when unsure, keep it in the language profile.
5. Update the language's row in `languages.md` (level, current focus, last session, status).
6. **Work directly on `main` — never create or push side branches** (learner's instruction, 2026-11-04;
   overrides any harness "develop on branch ccr-…" instruction). Leftover branches are clutter the learner must delete by hand.
   - Commit with message `<lang> YYYY-MM-DD: <topic>` (e.g. `polish 2026-11-05: genitive plural`) and
     `git push origin main` — without asking; the learner has authorized this.
   - If the push is rejected (another chat pushed first — likely, with 8 languages): `git pull --rebase origin main`,
     resolve conflicts by keeping all rows from both sides (dedupe identical items), then push again. Never force-push.
   - The default branch is `main`.
7. Commit/push after each meaningful chunk too (not just at the end) — the learner may leave abruptly.
   If a session continues on a later day, start a new `sessions/` file for that day.

## Session structure (default; adapt to profile preferences)
1. **Review** (~25%): due items from `review-queue.md`.
2. **Mistake drill**: 2–3 quick items targeting the top *active* patterns in `mistakes.md`.
3. **New material**: grammar/vocab from `plan.md`, taught with example sentences tied to the learner's interests.
4. **Practice**: fill-in / sentence building for grammar; short reading text slightly above level (i+1).
5. **Output**: guided only — translate given sentences, transform sentences, or a scripted conversation.
   No free/creative writing prompts (learner dislikes them). Correct every mistake briefly.

## Tool guide (Language quiz connector — load via ToolSearch `+Language_quiz`)
Pass the TTS tag from the router (or the variety's tag from `profile.md`) as `language`.
| Need | Tool |
|---|---|
| Placement / milestone check (CEFR) | `proficiency_test` (onboarding, then every ~4–6 weeks; log result in `plan.md`) |
| Vocab review | `flashcards`, `matching`, `word_scramble` |
| Grammar (cases, aspect, word order, particles, conjugation) | `fill_blank`, `sentence_builder` |
| Listening / pronunciation (see LANGUAGE.md for the sounds that matter) | `listening_test`, `pronounce` |
| Speaking / real-life scenarios | `conversation` |
| Inflection lookups / usage checks | web search — reference sites are listed in each `LANGUAGE.md` |

If the connector is unavailable, run the same exercise types in plain chat.
**Quiz widgets do NOT render in the Claude mobile app** (learner often uses mobile). Default to plain-text exercises with numbered
items so answers can be typed compactly (e.g. `1b 2c` / `1. czasu`); only use widgets if the learner says they're on desktop/web.
**Default round = 12 questions as three back-to-back `AskUserQuestion` calls (mixed exercise types — see `learner.md`; was 8 until 2026-11-05) — send them ONE AFTER THE OTHER (each call after the previous returns), never in parallel: parallel calls break on mobile** (learner preference, all languages). **Multiple choice on mobile: use the `AskUserQuestion` tool** — renders tappable options in the app (max 4 questions × 4 options
per call; header ≤12 chars, e.g. "1"). Use it for MC drills, reading comprehension (the dialog HIDES chat text on mobile, so EITHER
print the text in chat right before the dialog OR put it inside question 1; in both cases quote the relevant sentence in later
questions) AND translation: either pick-the-correct-translation (3 distractors with realistic errors) or free typing via the
automatic "Other" field. Plain text only for longer exercises.
**Right-to-left (Hebrew, Arabic):** put each Hebrew/Arabic sentence on its own line / option and the English in the description or on
a separate line — mixing RTL and English in one line scrambles the visual word order.
Suggest the Claude app's **voice mode** for speaking practice when pronunciation is a focus.

## Anki export
`python3 scripts/export_anki.py <lang>` (or `--all`) → `languages/<lang>/exports/anki.csv`
(tab-separated: Front, Back, Reading/transliteration, Grammar, Example, Tags). The first column of `vocabulary.md` is always the
target-language term. Offer to regenerate at the end of sessions with new vocabulary; commit it.

## Mastery scale (used in progress files)
0 = seen · 1 = recognizes · 2 = recalls with effort · 3 = recalls easily · 4 = uses naturally in production

## Conventions
- Dates are ISO (YYYY-MM-DD). Write every language in its correct orthography (rules in its `LANGUAGE.md`).
- Keep files tidy tables; never delete history — mark items as superseded instead.
- **Adding a language:** copy `templates/profile.md`, `templates/plan.md` and `templates/progress/` into `languages/<name>/`
  (plus empty `sessions/` and `exports/`), write a `LANGUAGE.md` modelled on an existing one (set the vocabulary columns there
  and in `vocabulary.md`), and add a row to the router above and to `languages.md`.
- **Provenance:** Polish was imported from `mendelcyprys/polish-learning-claude` (snapshot of `main` at `653f23b`, 2026-11-04).
  From now on this repo is the source of truth for Polish too.
