# WordSmither skills

Skills owned by WordSmither.

Third-party skills must pass the review in the root `CLAUDE.md` before they are added here.

| Skill | Source | Status | Record |
|---|---|---|---|
| `humanizer` | `blader/humanizer` | Approved and installed in `.claude/skills/` 2026-09-14 | [humanizer.md](humanizer.md) |
| `format-copywriting` | CreativeEngine (in-house) | Approved and installed in `.claude/skills/` 2026-09-17. Covers social and paid in English | [format-copywriting.md](format-copywriting.md) |
| `wait-what` | `mattpocock/skills` | Approved and installed in `.claude/skills/` 2026-10-03. Manual only; session utility for any role | [wait-what.md](wait-what.md) |

## Reviewed, not installed

| Skill | Source | Decision |
|---|---|---|
| `storybrand-messaging` | `wondelai/skills` (v1.5.0) | Reviewed 2026-10-03. Safe (Markdown only), but auto-triggers on everyday copy requests, imposes its own 10/10 score and fill-in copy patterns. Method adopted instead: conversion clarity in `format-copywriting` and the messaging lens in `brief-normalization.md` §12. Do not re-review unless the need changes |
