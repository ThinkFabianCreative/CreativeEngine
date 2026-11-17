# Awwwards stack

`awwwards` and the skills it composes. One record for the pack.

| Skill | Source | Installed | Runs code |
|---|---|---|---|
| `awwwards` | `ga14ctic/awwwards-skill` (MIT) | `.claude/skills/awwwards/` | No. Its pages load React, Framer Motion, Three.js and anime.js from a CDN |
| `frontend-design` | `anthropics/claude-code` plugin (official) | `.claude/skills/frontend-design/` | No |
| `color-expert` | `meodai/skill.color-expert` | `.claude/skills/color-expert/` (SKILL.md, references, licences) | No |
| `color-palette-extractor` | `onewave-ai/claude-skills` | `.claude/skills/color-palette-extractor/` | No |
| `design-motion-principles` | `kylezantos/design-motion-principles` | `.claude/skills/design-motion-principles/` | No |
| `remotion-best-practices` | `remotion-dev/skills` (official) | `.claude/skills/remotion-best-practices/` | No. Example `.tsx` only |
| `impeccable` | `pbakaus/impeccable` v4.5 | `.claude/skills/impeccable/` (installed by the user 2026-11-16, `--no-hooks`; engine v0.1.24 in `~/.impeccable/bin/`). Installer also added 4 `impeccable-*` agents to `.claude/agents/`: tooling, not CreativeEngine department agents | Yes: launcher downloads a binary from GitHub releases (checksum-verified); writes `PRODUCT.md` / `DESIGN.md`; optional edit hook |

| | |
|---|---|
| Owner | DesignChamp |
| Status | Approved by the user 2026-10-03 after review |
| Invocation | Automatic. DesignChamp uses them as needed; no manual-only flag |
| Local changes | `awwwards`: description rescoped to DesignChamp work after a concept exists; CreativeEngine note added at the top |

## Review (2026-10-03)

- No credentials, destructive commands or suspicious instructions in any installed skill.
- `awwwards` is the author's personal pipeline: Sam, Switchyard, Railyard, `~/CLAUDE.md`, `~/skills-showcase`, `switchyard-video` and its pricing language are his private setup. Ignore them.
- Not adopted: `agent-browser` (global npm install plus Chromium; the built-in browser pane does the job), the 21st.dev Magic MCP (needs the user's own account and key), `vercel:*` (Next.js; not our path), `switchyard-video` (private).
- Overlap: `design-motion-principles` with the Emil Kowalski skills (it adds Krehel's polish and Tompkins' play lenses); `frontend-design` with the Taste-Skill pack; `awwwards` phase 3 with `ui-ux-pro-max`. Use the most specific one for the job.

## Use

**When.** Whenever the craft bar is high and the medium is digital:

| Job | Use |
|---|---|
| Campaign digital executions (hero pages, microsites, interactive or animated key visuals) | `awwwards` pipeline |
| Slide decks | `frontend-slides` or `slides` still own deck structure; `awwwards` for showcase decks and single hero slides. `editorial-presentation.md` judges the deck |
| Prototypes | `format-prototyping` owns the format and context; `awwwards` raises the build. Prototypes only |
| Email | `frontend-design` and `color-expert` only. Email clients do not run JS, WebGL or most CSS motion; no Three.js, Framer Motion or anime.js in email |
| Video and motion pieces | `remotion-best-practices` (phase 7) |
| Color | `color-palette-extractor` for a client's real colors from their assets or site screenshots; `color-expert` for building or checking a palette |

**Rules.**

1. **Concept first.** Run `awwwards` only once a concept sentence exists (`barry-concept-art-direction.md` §1). Its phase 1 "pick one aesthetic extreme" chooses the execution's look, never the idea. Phase 1's brief inherits the normalized brief or work packet.
2. **Client look comes from client knowledge.** On client work, the palette, type and visual rules come from `projects/<client>/client/`. Phase 2 branch A (extract from the real brand) applies; never invent a client palette.
3. **Prototypes, not production.** Production landing pages are native Instapage (`instapage-production`). Nothing built here ships as production code.
4. **Artifacts load from jsDelivr.** The single-HTML recipe imports from `esm.sh`, which published Artifacts block. Swap to `cdn.jsdelivr.net/npm/` (or cdnjs / unpkg) for anything published as an Artifact.
5. **Verification uses the built-in browser** in place of `agent-browser`: 320 / 768 / 1280 / 1920 screenshots, tab order, interactions.
6. **Without `impeccable`**, phase 8 runs as DesignChamp's own audit against `visual-craft.md` and `typography.md`, plus the accessibility checks it lists (contrast, 44px targets, focus, reduced motion).
7. **Phase 3 without Magic MCP** uses `ui-ux-pro-max` and `ad-reference`. Remix references, never copy.
8. **No fake proof.** Logos, testimonials and metrics come from the claim ledger or are labeled placeholder. Upstream rule; also ours.
