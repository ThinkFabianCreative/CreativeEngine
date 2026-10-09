# Refero Design

| | |
|---|---|
| Source | `github.com/referodesign/refero_skill` (MIT), commit `a9b54a3` (2026-09-05), version 1.0.2 |
| Owner | DesignChamp. WordSmither, CreativeDirector and SprintFacilitator may use it as described below |
| Status | Approved by the user 2026-10-05 |
| Exposure | `.claude/skills/refero-design/`, copied from the repo (`SKILL.md`, `references/`, `agents/openai.yaml`) with the repo `LICENSE` added. No edits. Installed with `npx skills add`; its `.agents/` symlink layout was replaced with a plain copy to match the other installed skills |
| MCP | Refero MCP (`https://api.refero.design/mcp`, HTTP) added to the user's local Claude config for this project 2026-10-05. The user signs in to Refero through `/mcp`. Until then, the skill runs on its bundled craft references only |
| Scripts | `scripts/check-release` (package validator) is not installed. Nothing executable ships in the skill |
| Invocation | Automatic |
| Reviewed | 2026-10-05 |

## What it is for

A reference library and method. Refero's MCP searches curated real-world work in three layers:

- **Styles**: extracted art-direction systems from real sites: visual thesis, tokens, type, layout, imagery treatment, do/don't rules.
- **Screens**: concrete UI patterns, states, copy and CTA patterns.
- **Flows**: multi-step journeys.

The method around it is sound and is adopted: study several references, **lock one dominant direction**, borrow only specific details, **don't average references into a safe middle**, **preserve token and media roles**, keep a **decision ledger**, and check the build against the lock.

## Use beyond UI/UX

A style is an art-direction system, not only a web pattern. Use it for pitch and credentials decks, key visuals, campaign art direction, OOH and social systems, identity mood work, motion languages and image-generation prompts (its visual thesis and imagery treatment translate directly). Its library is web-sourced: it supplies taste and craft evidence, not advertising mechanisms. For ad precedents use `ad-reference`.

## CreativeEngine rules (these override the skill)

1. **References are welcome from the first EXPLORE round.** Pitch work runs on references: they are what the client needs to see. Use Refero to build territories, mood boards and visual directions early, and to remix and combine proven work (see the user's remix method).
2. **Remix, don't clone.** Combine references into something new for this client; Refero's own lock-and-borrow rule is the mechanism. Every territory still needs a reason to exist: a truth or concept sentence, even a rough one.
3. **Not the default design authority.** The skill calls itself the primary design skill and tells the agent to prefer it over other design skills. Ignore that. DesignChamp's judgment and the frameworks govern (`barry-concept-art-direction.md`, `visual-craft.md`, `typography.md`, `editorial-presentation.md`). Refero composes with the Awwwards stack, Taste-Skill and UI/UX Pro Max; it does not replace them.
4. **"Research is mandatory" is advice, not a gate.** Skip it for small fixes or when the client's own brand layer is the reference.
5. **Copy belongs to WordSmither.** `references/copywriting.md` is background only.
6. **No client facts in queries.** Queries go to Refero's server. Search with aesthetic, category and brand-name terms ("warm trustworthy medical device marketing"), never confidential client or project detail.
7. **Credit sources in pitch materials** where references are shown.
8. **Client look stays in client knowledge.** Style locks chosen for a client are project records, never global method.

## Overlap

- `anti-ai-slop.md` overlaps Taste-Skill and Impeccable checks; adds useful tells (token-role drift, "calm editorial" cream canvases and serif word swaps).
- `typography.md`, `color.md`, `motion.md` overlap our frameworks and the Awwwards stack. Ours win on conflict.
- Screens and flows are new to the department: use them for landing pages, Instapage specs and sprint prototypes.
