# Practice page (Japanese)

`japanese-practice.html` — Artifact page for Japanese rounds, same relay/grading rules as the Arabic and Polish pages (see `languages/arabic/tools/README.md`).
URL: https://claude.ai/artifact/5GvuSvki7avC4WWs5tWJBA · always republish with `capabilities: {"sample": {}, "comments": {}}`.

## What is different
- **Three exercise types:** `mc` (kana + romaji under each option: `"すし\nsushi"`), `build` (tap word tiles in order — for sentence building before free typing), `type`.
- **Typing without a Japanese keyboard:** typed answers convert romaji → kana live (`toKana`): lowercase = ひらがな, UPPERCASE = カタカナ, `ha` = は, `wo` = を, `nn` = ん, `-` = ー, double consonant = っ.
  Switchable off (checkbox); skipped automatically when a real IME is composing.
- **Checking:** `strict()` ignores spaces and punctuation; `loose()` also folds katakana → hiragana, so a right word in the wrong script is "Right words, wrong script".
- Kanji are not used yet; when they are, give furigana in the prompt.

## Per session
Edit `ITEMS`/`MODEL` (6 mc, 3 build, 3 type works well), republish the same file path, grade the round in the chat when it arrives, and add valid variants to `a:[...]`.
