# DesignChamp skills

Skills owned by DesignChamp.

Third-party skills must pass the review in the root `CLAUDE.md` before they are added here.

| Skill | Source | Status | Record |
|---|---|---|---|
| Taste-Skill pack (13 skills) | `Leonxlnx/taste-skill` | Approved 2026-09-13; installed in `.claude/skills/` 2026-09-17 (reviewed commit `ccbc156`) | [taste-skill.md](taste-skill.md) |
| Emil Kowalski skills (5 of 12) | `emilkowalski/skills` | Approved 2026-09-13; installed in `.claude/skills/` 2026-09-17 (reviewed commit `d23d7f8`) | [emil-kowalski-skills.md](emil-kowalski-skills.md) |
| `frontend-slides` | `zarazhangrui/frontend-slides` | Approved and installed in `.claude/skills/` 2026-09-14 | [frontend-slides.md](frontend-slides.md) |
| UI/UX Pro Max (5 of 7: `ui-ux-pro-max`, `banner-design`, `slides`, `design-system`, `identity-design`) | `nextlevelbuilder/ui-ux-pro-max-skill` | Approved and installed in `.claude/skills/` 2026-09-14 | [ui-ux-pro-max.md](ui-ux-pro-max.md) |
| `format-prototyping` | CreativeEngine (in-house) | Approved and installed in `.claude/skills/` 2026-09-17 | [format-prototyping.md](format-prototyping.md) |
| `hyperframes` | `heygen-com/hyperframes` | Approved and installed globally (`~/.agents/skills/`) 2026-10-28 (reviewed commit `8e63faf`) | [hyperframes.md](hyperframes.md) |
| `ad-reference` | CreativeEngine (in-house) | Built at the user's request and installed in `.claude/skills/` 2026-09-24 | [ad-reference.md](ad-reference.md) |
| `artlist-production` | CreativeEngine (in-house), for the Artlist MCP connector | Built at the user's request and installed in `.claude/skills/` 2026-09-24. Connector not yet connected | [artlist-production.md](artlist-production.md) |
| `instapage-production` | CreativeEngine (in-house), for the Instapage MCP and Public API | Built at the user's request and installed in `.claude/skills/` 2026-09-24. Instapage MCP not yet connected; Figma Native Kit built | [instapage-production.md](instapage-production.md) |
| Awwwards stack (`awwwards`, `frontend-design`, `color-expert`, `color-palette-extractor`, `design-motion-principles`, `remotion-best-practices`; `impeccable` installed by the user 2026-11-16, playbook in `../knowledge/impeccable-playbook.md`) | `ga14ctic/awwwards-skill` and upstreams listed in the record | Approved and installed in `.claude/skills/` 2026-10-03. Automatic; DesignChamp uses as needed | [awwwards-stack.md](awwwards-stack.md) |
| `refero-design` + Refero MCP | `referodesign/refero_skill` | Approved and installed in `.claude/skills/` 2026-10-05 (reviewed commit `a9b54a3`). MCP added; user sign-in pending | [refero-design.md](refero-design.md) |
| `ad-library` MCP server | `at-dan/ad-library-mcp` | Approved and installed outside the repo 2026-10-08 (reviewed commit `2da03c1`). Localhost only; user adds ScrapeCreators key and starts server | [ad-library-mcp.md](ad-library-mcp.md) |
| design-superpowers plugin (`/map-design`, `/design-review`, `/creative`, `/design`, `/ds-make` approved; `/ds-consumer`, `/ds-producer`, `/ds-manage`, `/figma-setup` on hold) | `LSDimi/design-superpowers` v1.0.0 | Approved 2026-10-26. Installed as a Claude plugin, outside the repo | [design-superpowers.md](design-superpowers.md) |
| `deck-designer` | CreativeEngine (in-house), adapted from the Presentation Engine package | Built at the user's request and installed in `.claude/skills/` 2026-11-17 | [deck-designer.md](deck-designer.md) |
| `unslop` plugin | `heydamir/unslop` (CC BY 4.0) | Installed by the user as a Claude plugin 2026-11-18 (user scope, outside the repo); reviewed and approved with calibration the same day (commit `620163e`) | [unslop.md](unslop.md) |

## Reviewed and not installed

| Package | Source | Decision | Where its useful parts went |
|---|---|---|---|
| Art Teacher agent + `art-style-intelligence` skill (agent later adapted and installed as `art-teacher`, 2026-11-17, see `ArtTeacher/AGENT.md`) | Outside package supplied by the user (`CREATIVE_ENGINE_ART_TEACHER_LEARNING_LOOP.zip`), reviewed 2026-11-17 | Not installed: duplicated DesignChamp and `creative-engine-director` critique, routed to agents CreativeEngine lacks, and imposed a fixed Swiss/Inter house style. Text only; no scripts or credential access | `shared/frameworks/critique-learning-loop.md`; archive list in `CreativeResearcher/knowledge/design-history-and-deck-sources.md` |
| `presentation-engine` skill (later adapted and installed as `deck-designer`, 2026-11-17) | Outside package supplied by the user (`CREATIVE_ENGINE_CLAUDE_SKILL_INSTALL.zip`), reviewed 2026-11-17 | Not installed: self-described specification, not a working generator; fixed house look conflicts with client-agnostic rule; overlaps `editorial-presentation.md`, `typography.md`, `visual-craft.md`, `frontend-slides`, `slides`. Text only | Structure in `shared/knowledge/deck-layout-archetypes.md`; MAD Decks and Figma sources in `CreativeResearcher/knowledge/design-history-and-deck-sources.md` |
