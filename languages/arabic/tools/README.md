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
4. The same page works for other scripts (Hebrew, Japanese): change the font (`--ar`), `dir`, `lang`, and the item list.
