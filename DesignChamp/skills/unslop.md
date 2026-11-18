# unslop (plugin)

| | |
|---|---|
| Source | `github.com/heydamir/unslop` (CC BY 4.0), by Damir Sokolovsky |
| Owner | DesignChamp (Interaction design specialty) |
| Status | Installed by the user as a Claude plugin 2026-11-18 (user scope, marketplace `heydamir`). Reviewed the same day against the eight steps (commit `620163e`). Approved with the calibration below |
| Exposure | Plugin, outside the repo. Appears as `unslop:unslop` and is invoked as `/unslop`, or picked up automatically from trigger phrases ("unslop", "polish", "stop looking AI-generated") |
| Upstream after review | Plugin updates come through the plugin manager. Any new version counts as unreviewed until someone checks it against the eight steps again |
| Reviewed | 2026-11-18 |

## What it is

A one-skill plugin that takes vibecoded, AI-looking UI and turns it into a designed interface. It runs in this order:

1. Audit the screen against a list of slop signs (`references/signs.md`).
2. Choose how much to change: heavy slop, light slop (polish mode) or no slop.
3. Write a five-line direction (Product, Character, World, Moments, Signature) and **stop for approval**.
4. Fix the screen in nine ordered passes: spacing, color, icons, copy, type, layout, details, visuals, motion.
5. Run a checklist, including a template check.

It can also do two optional things. It can snapshot a live site into one HTML file when no code is available, and it can render a "story video" of the screen unslopping itself.

## Use in CreativeEngine

| Use | Verdict |
|---|---|
| Cleaning up AI-generated or vibecoded web UI: prototypes, landing pages, dashboards, `format-prototyping` and `awwwards` output that has drifted into slop | **Approve.** This is its job |
| Client asset audits of a live site, through `snapshot.mjs` plus the slop audit | **Approve.** The audit list works as evidence: a sourced observation, not a verdict |
| Quick self-check in DEVELOP on any interface DesignChamp builds | **Approve.** Run the audit and the template check only, with no passes |
| Ad layouts, OOH, print, social statics, editorial decks, identity | **Do not use.** Its rules are product-UI defaults. `visual-craft.md`, `typography.md` and `editorial-presentation.md` govern these |
| Story video | **Manual only.** Use it for internal demos or case-study material, when asked |

## Calibration for DesignChamp

- **The direction is not the idea.** Its five lines are a design-language brief, and "World" and "Signature" make useful prompts. They never replace Barry's concept sentence (`shared/frameworks/barry-concept-art-direction.md` §1) or EXPLORE work. When a concept already exists, the direction comes from that concept, not from scratch.
- **The client's brand wins.** unslop already keeps a real brand. In CreativeEngine, "real brand" means the approved sources in `projects/<client>/client/`. Its claim that a violet gradient or sparkle in a logo is slop "unless the user says they do" does not override an approved client identity. Raise it as an observation instead.
- **Copy belongs to WordSmither.** The copy pass may fix interface microcopy on its own: labels, button text, empty states, exclamation marks, trailing periods. Headlines, subheads, value propositions and any line that carries the idea go to `word-smither`. Its rules on unverifiable claims already match CreativeEngine's rule: list them and never invent facts.
- **The fixed rules are interface defaults, not law.** Weights 400 to 600, no italic, no uppercase tracked labels, the 4px grid and the hero "scene" recipe all fit product UI. A client system that deliberately uses uppercase tracked labels or a heavy display weight is not slop. `typography.md` decides type, and the brand decides identity.
- **Its "what good looks like" is a house look.** Quiet chrome, one bright element and a scene hero make a strong pattern. Used on every client, they become the next template. Run its own template check, and in JUDGE also check that the result does not look like the last unslop run on another client's work.
- **Always stop at the direction.** Keep step 4 (show the audit and direction, then wait). Skip the wait only when the user says to.
- **Image generation follows CreativeEngine's rules.** When the Visuals pass offers to generate a scene or object, route it through `artlist-production` or the image rules in `DesignChamp/AGENT.md` (quote, confirm, label as AI-drafted, pitch only). Prompts must contain no client facts unless the user has approved sending them to that service.
- **Outputs go in the project folder.** `snapshot.mjs` writes `unslop/original.html` and `original.live.png`, and the story writes `unslop-story/`, all relative to the working folder. In CreativeEngine, run them from `projects/<client>/<project>/` or give that path. Never write them at the repo root.
- **Snapshots are raw sources.** A saved copy of a client's live site is raw evidence. Work on a copy and leave the snapshot untouched (raw is immutable).
- **Credit.** Every story video carries `unslop by @heydamir`. Keep the credit on internal use. Before a story video goes into client-facing material, flag it to the user.
- **Overlap.** Use `unslop` when the input is AI-generated UI with the usual tells. Use `impeccable` for broader interface work (critique, bolder, quieter, harden, motion) and `design-superpowers:design-review` for a P0 to P3 health and accessibility report. `redesign-existing-projects` and `design-taste-frontend` overlap with its redesign passes; use one per job, not several.

## Security review

1. **SKILL.md read:** yes, plus `references/signs.md` and `visuals.md`. `tokens.md`, `effects.md`, `rtl.md` and `refs.md` are reference values and image examples.
2. **Executables:** three Node scripts.
   - `snapshot.mjs` launches Playwright, preferring the system Chrome or `CHROME_PATH`. It loads the URL or file you give it, scrolls, inlines that page's own images and stylesheets with `fetch`, and writes one HTML file and one PNG to the output path you give.
   - `story.mjs` serves the story folder on `127.0.0.1` with a random port. `story-path.mjs` guards it against path traversal and symlink escape. It records frames with Playwright, encodes them with `ffmpeg` through `execFileSync` (fixed arguments, no shell), and deletes only its own temporary frames folder.
   - Tests in `test/` are repository CI only.
   - There are no hooks, no MCP server and no `.mcp.json`.
3. **Actions expected:** read and edit the project's UI files, take screenshots, run the two scripts, and optionally call an image generation tool if one is connected.
4. **Suspicious instructions:** none. It promotes the author through a credit line only.
5. **Credentials:** none accessed. The only environment variable read is `CHROME_PATH`.
6. **Destructive commands:** none outside its own temporary frames folder. `snapshot.mjs` overwrites the output file you name.
7. **Dependencies:** Playwright and `ffmpeg` are needed only for the scripts. They aren't installed by the skill; it tells the user the install command. Confirm before installing either.
8. **Improves CreativeEngine:** yes. No other installed skill covers cleaning up AI-looking UI with an ordered audit list, and the slop signs list is a useful checklist for reviewing any prototype the department generates.
