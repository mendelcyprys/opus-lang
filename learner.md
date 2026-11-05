# Learner (shared across all languages)

_Facts and preferences that apply to **every** language. Language-specific info lives in `languages/<lang>/profile.md`,
which wins where the two differ. Mostly gathered during Polish onboarding (2026-11-04) — when starting a new language,
assume these hold and don't re-interview; adjust if the learner says otherwise._

- **Native language:** English
- **Studying (8):** Polish, Ukrainian, Hebrew, Arabic, Spanish, French, German, Japanese — at different levels (see `languages.md`).
  Only Slavic pair: Polish (stronger) + Ukrainian (lower level).
- **Goals (general):** hobby / interest in languages & culture (stated for Polish; check per language).
- **Interests (for examples & texts):** food & cooking, travel & places, tech & work, books/film/music
- **Time per session / frequency:** longer sessions now (~20–30 min; changed 2026-11-05, was ~10 min bursts) → several rounds per session, not 1–2
- **Gender for 1st/2nd-person forms:** masculine (used *będę czekał* in Polish, 2026-11-04) — assume masculine unless told otherwise.
  Matters for Hebrew/Arabic addressing ("you"), Slavic past tense, Romance adjective agreement.

## Device & format
- Mostly uses the Claude **mobile app** — quiz widgets don't render. Claude can't detect the device: assume mobile unless the learner
  says "desktop" in that chat. Use `AskUserQuestion` for MC and translation (with Hint/Skip options;
  learner types answers via "Other"). Plain text only for longer items. Answers compactly.
- **Round length — DEFAULT for every language: 12 questions = 3 AskUserQuestion modals back to back, one after another** (4 + 4 + 4, no feedback in between),
  then feedback on all 12 (raised from 8 on 2026-11-05: learner wants longer rounds). Don't stop at a single modal of 4.
- **Variation within a round (2026-11-05):** mix exercise types in each round — e.g. MC fill-in, pick-the-translation, error-spotting
  ("which sentence is wrong?"), odd-one-out, matching a form to its use, reading snippet, typed answer via "Other" — instead of 8 near-identical items.
  Mix review + mistake drill + new material in one round; vary the topic and sentence frames.
- Likes reading comprehension: short text + AskUserQuestion MC — with the text **inside** question 1 (see the last bullet).

## Teaching preferences
- Correction style: correct **every** mistake, with a brief explanation.
- Favourite exercise types: short, structured exercises (fill-in-the-blank, translation, sentence building, multiple choice).
- Dislikes: open-ended/creative writing ("write about X") — always give concrete prompts or sentences to translate/transform instead.
- Stretch: every so often (~1 in 3–4 rounds) set an exercise one level up for challenge (requested in Polish, 2026-11-04).
- Explanation language: depends on level → set per language in its `profile.md` (Polish: mix of simple Polish + English).
- Typing: occasionally drops diacritics/letters — correct every time; suggest long-press / the right keyboard layout.
- **Reading texts on mobile (2026-11-05):** chat text printed before an AskUserQuestion dialog is NOT visible. Put the whole text inside question 1 (and quote the relevant sentence in later questions).
