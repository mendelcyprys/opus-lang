# Large-type practice page (Arabic)

`arabic-practice.html` is a self-contained Artifact page: big Arabic text with an A−/A+ control (the learner finds Arabic too small in chat and in
`AskUserQuestion` modals — see `profile.md`), 6 multiple-choice + 6 typed items, instant checking (spelling slips in hamza / ى / ة are flagged separately),
and three Claude hooks.

| Feature | Capability | Notes |
|---|---|---|
| "Ask Claude why" (per miss) and "Get feedback from Claude" (summary) | `sample` | page asks Claude directly; first use asks the viewer for consent |
| "Send results to Claude" | `comments` (full form) | `sendToClaude` posts the result text as a comment and wakes this session; the learner must be an editor of the artifact. Fallback: "Copy results" → paste into chat |

## Using it in a session
1. Edit the `ITEMS` array (and `MODEL`, the vowelled answers shown for typed items) for today's focus: due items in `review-queue.md` + top active patterns in `progress/mistakes.md`.
   `type:'mc'`: `opts[0]` is always the correct one in the source (the page shuffles at runtime); `type:'type'`: `a` = accepted answers, unvowelled.
2. Publish with the Artifact tool, **same file path / URL** (keeps the link), always passing `capabilities: {"sample": {}, "comments": {}}`
   (omitting keeps the stored declaration; passing a different set revokes the rest). URL: https://claude.ai/artifact/9Gp267NvKwq2c8Eff6GuhV
3. When the results arrive (comment from the page, or pasted text): log the round as usual (session file, progress files, review queue, commit).
4. Other languages have their own pages (`languages/<lang>/tools/`): Polish (Latin), Japanese (romaji → kana, tile building), Hebrew (RTL, Mac-layout keyboard, tile building), Ukrainian + French (shared code with a CONFIG block: Cyrillic Mac keyboard / accent bar, tile building). Port from the closest one for a new language.

## Notes from the 2026-11-07 code audit
- **Text size:** the A−/A+ buttons set `--ar-size`; *all* text (prompts, glosses, notes, feedback, summary, Claude's answers) is sized from it, since Arabic also appears in English lines.
  Only the A−/A+ buttons themselves stay fixed. Storage key `arSize2`.
- **Matching:** `strict()` strips harakat/tatweel and punctuation; `loose()` also merges hamza seats, ى/ي, ة/ه — equal under `loose` but not `strict` = "spelling slip".
  Persian ی/ک are mapped to Arabic ي/ك (some phone keyboards). The old harakat regex accidentally covered Arabic-Indic digits and ٮ ٯ; now explicit escapes.
- **Fixes:** multi-line prompts keep their line breaks (`white-space:pre-line`); Arabic glyphs inside English text use Amiri (font stack); `aria-live` moved from the whole card to the feedback box (`role="status"`).
- Known limits: no persistence (results leave only via Send/Copy); a typed answer with a different but valid word order is marked wrong (add alternatives to `a:[...]`).

## Grading goes in the chat
When a round arrives, give the full grading in the session chat (see `learner.md`); the thread reply is a short pointer. Re-check marks the page got wrong and add valid alternatives to `a:[...]`.

## Fast path (since 2026-11-07): round.json instead of editing JS
1. Write the round in `tools/round.json` (format: header of `scripts/build_round.py`; `python3 scripts/build_round.py arabic --extract` shows the current one).
2. `python3 scripts/build_round.py arabic` validates and rewrites the ITEMS/MODEL blocks of `arabic-practice.html`.
3. Publish that file with the Artifact tool (same path, capabilities `{"sample":{},"comments":{}}`). Commit `round.json` + the page.
