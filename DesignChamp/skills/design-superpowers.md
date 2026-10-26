# design-superpowers (plugin)

| | |
|---|---|
| Source | `github.com/LSDimi/design-superpowers` (MIT), plugin v1.0.0 by Dimitrios Arapis |
| Owner | DesignChamp |
| Status | Reviewed 2026-10-26; approved by the user 2026-10-26 with the calibration below |
| Exposure | Installed as a Claude plugin (outside the repo), not copied into `.claude/skills/`. Skills appear namespaced: `design-superpowers:<name>`, invoked as `/creative`, `/design-review` and so on, or picked up automatically from their trigger phrases |
| Upstream after review | Plugin updates arrive through the plugin manager. A new version is unreviewed until it is checked again against the eight steps |
| Reviewed | 2026-10-26 |

## What it is

Nine router skills that split design work into sub-agents ("Moodboard Generator", "A11y Auditor" and so on), with a shared knowledge base (`skills/shared/knowledge/*.md`) and CSV lookup tables (styles, typography, psychological principles, usability guidelines). Every skill first detects a "maturity level": L0 no design language, L1 a `DESIGN.md` exists, L2 a design system exists, L3 an enterprise design system described in `.ds-context.md`. CreativeEngine work is almost always L0 or L1.

## Use in CreativeEngine

| Skill | Verdict | Use | Invocation |
|---|---|---|---|
| `/map-design` | **Approve** | Pull a design language out of a client's live site, screenshots, Figma file or prototype into a `DESIGN.md`. Best use: client asset audits and the MFK-style `DESIGN.md` per project. Its "Reconcile" mode diffs two sources (Figma against code) without picking a winner, which fits our divergence rule | Automatic |
| `/design-review` | **Approve** | Interface review in DEVELOP and JUDGE: visual quality, Nielsen heuristics, WCAG 2.1 AA, motion. Report is P0 to P3 with a required "what's working" section. Use on landing pages, prototypes and web builds | Automatic |
| `/creative` | **Approve, calibrated** | Palette Architect (OKLCH scales with WCAG pass/fail) and Typography Director (type scale and font availability check) are useful craft tools once a direction exists. Moodboard, Brand Architect and Refresh Strategist are secondary; see calibration | Automatic for palette, type and layout systems; manual for moodboards and brand direction |
| `/design` | **Approve, calibrated** | Composing pages and flows from an existing client design system or `DESIGN.md` (web rebrands, landing pages). Its hard rule against overrides suits client design-system work | Automatic |
| `/ds-make` | **Approve, narrow** | Token architecture when we are building a client design system (MFK Storybook tokens, design-system handover). Token Architect and Component Builder only | Manual only |
| `/ds-consumer` | Hold | Assumes an enterprise system with lint, Shortcut and squad libraries. Nothing in our work is L3. Revisit if a client hands us one | Do not use |
| `/ds-producer` | Hold | Enterprise production workflow built around Shortcut tickets, Figma branches, peer-review quotas and publish cascades. Not our process | Do not use |
| `/ds-manage` | Hold | Publishing cascades and adoption analytics for a design system team we do not run | Do not use |
| `/figma-setup` | Hold | Installs PluginOS, a second third-party plugin, plus a Figma Community bridge plugin. That is a separate review. We already use the official Figma MCP | Do not use |

## Calibration for DesignChamp

- **Concept before system.** `/creative` treats direction as a design-language problem: a theme statement ("calm precise instrument") and safe, balanced and bold variants. That is not a creative idea. It never replaces Barry's concept sentence (`shared/frameworks/barry-concept-art-direction.md` §1) or the EXPLORE work in `DesignChamp/AGENT.md`. Use it after the idea exists, to systematize color, type and layout.
- **Brand Architect is not brand strategy.** Its archetypes and "brand philosophy" stay below `shared/frameworks/brand-strategy.md` and BriefMachine. Use only its brand-to-product translation table, when a decided brand has to become UI tokens.
- **Its defaults are product-UI defaults.** Fixed type ratios, 8px t-shirt spacing, 100 to 500ms motion and "12-column for product UI" fit interfaces. They do not govern ad layouts, OOH, film or editorial decks. There, `typography.md`, `visual-craft.md` and `editorial-presentation.md` win.
- **Specificity wins on overlap.** For visual critique use `/design-review` for interface health and `visual-craft.md` for whether the craft lands the idea. For type choice, `typography.md` decides and `/creative` checks availability and builds the scale. For color, `color-expert` and `/creative` Palette Architect are interchangeable; use one, not both. For accessibility, `/design-review`'s A11y Auditor and `design:accessibility-review` are interchangeable.
- **`DESIGN.md` goes in the client workspace, never at the repo root.** `/map-design` writes to "project root" by default. In CreativeEngine that means `projects/<client>/<project>/DESIGN.md` (as with `projects/miracles-for-kids/website-rebrand/DESIGN.md`), or `projects/<client>/client/` only when the user confirms it as client knowledge. It asks to confirm before writing; state the path when it asks.
- **No `.ds-context.md` or `fonts-inventory.txt` at the repo root.** If a skill offers to write one, keep it in the project folder or decline. Skills fall back to the session when the file is absent.
- **Client isolation.** Its maturity check reads `DESIGN.md` and `.ds-context.md` from the working folder. Point it at the current project's `DESIGN.md` explicitly, so it never picks up another client's.
- **Imagery.** When `/creative` or `/design` offers to generate images, route through `artlist-production` or the image rules in `DesignChamp/AGENT.md` (quote, confirm, label as AI-drafted, pitch only).
- **Output style.** Its outputs are tables with no narrative. Fine for working files. For anything shown to a client, DesignChamp rewrites them into its own voice.

## Security review

1. **SKILL.md read:** all nine, plus `shared/figma-adapter.md`, `font-availability.md` and `ds-context-loader.md`.
2. **Executables:** `scripts/validate_plugin.py` and `scripts/aggregate_eval_results.py` are repository CI and evaluation tools; no skill calls them. No hooks, no MCP server, no `.mcp.json`.
3. **Actions expected:** Read, Grep on its own CSVs, Write (`DESIGN.md`, `.ds-context.md`, font inventory, each after confirmation), Figma reads through PluginOS or the Figma MCP, browser `getComputedStyle` reads in `/map-design`.
4. **Suspicious instructions:** none. `/figma-setup` steers users to the author's own PluginOS plugin and tells Claude not to offer the Figma MCP as an alternative. That is promotion of the author's product, not a hazard, but it is why that skill is on hold.
5. **Credentials:** none accessed.
6. **Destructive commands:** none. `/map-design` can overwrite an existing `DESIGN.md` after confirmation; in enrich mode it is told not to remove content unless contradicted.
7. **Overlap:** see calibration. Largest overlaps: `color-expert`, `ui-ux-pro-max` / `design-system`, `design:design-critique`, `design:accessibility-review`, `vectorlab-ux-skills:ux-audit`.
8. **Improves CreativeEngine:** yes for `/map-design` (fills a gap: no other installed skill extracts a design language into a file), `/design-review` (one structured interface report) and the craft parts of `/creative`. The enterprise design-system skills add nothing to current work.
