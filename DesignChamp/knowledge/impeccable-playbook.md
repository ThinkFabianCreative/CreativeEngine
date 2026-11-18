# impeccable playbook

How DesignChamp uses `impeccable` (`pbakaus/impeccable`) on CreativeEngine web design projects. Method only: no client facts. The record and approval are in `DesignChamp/skills/awwwards-stack.md`; where this playbook and that record disagree, the record wins until it is updated.

Written 2026-11-18 from the installed skill (`.claude/skills/impeccable/`, skill **4.9.1**, engine pin **0.1.24** in `scripts/VERSION`) and the docs at impeccable.style (latest published: skill 4.9.1 and CLI 4.9.2 with engine 0.1.25, both 2026-11-15). Nothing was run to write it. Points marked **(unverified)** could not be confirmed from the docs or the installed files.

## 1. What it is

An agent skill with a local engine binary. It plans, builds, critiques and refines web interfaces (and native iOS/Android screens). Its model:

- **Two records.** `PRODUCT.md` holds product truth (users, purpose, positioning, constraints, evidence, brand commitments, platform). `DESIGN.md` holds the visual system (tokens in YAML frontmatter, prose sections, Google's DESIGN.md format) with a generated sidecar `.impeccable/design.json`. A per-page **surface brief** in `.impeccable/surfaces/` holds one page's purpose, mode and **direction contract**.
- **Four surface modes** decide how much expression the page gets: **Persuade** (landing, campaign, pricing), **Operate** (app UI, dashboards), **Read** (docs, articles), **Experience** (portfolios, showcases). Mode comes from the surface, not the product.
- **Refinement preserves, redesign replaces.** Refinement keeps the incumbent world, copy and behavior. Redesign replaces the visual world through the new-work flow, never by polishing the old look.
- **Anti-default machinery.** For a new visual world it "rolls" directions (`concept-seed`, a call to impeccable.style) so the model does not converge on the category default, deals catalog "challenger" worlds, and shows the choice on a localhost decision page. A craft floor (`reference/craft-floor.md`) carries bans and checks loaded before every UI edit. A detector flags slop patterns, contrast, overflow and drift from `DESIGN.md`.
- **Finish is part of the build.** A new surface is not done until a fresh-context finish reviewer has judged it and a documenter has written `DESIGN.md` from what was actually built.

## 2. Commands

`/impeccable <command> [target]`. With no argument it shows a context-aware menu and runs nothing.

| Command | Does | Use in CreativeEngine | Writes or changes |
|---|---|---|---|
| `init` (alias `teach`) | Interviews for product truth; asks build path (comp-first or code-first) when image generation exists | Start of DEVELOP, once a direction is approved. Answers come from the normalized brief, work packet and client knowledge, not a fresh interview | `PRODUCT.md`; `.impeccable/config.json` (`buildPath`); maybe `.impeccable/live/config.json` |
| `shape` | Discovery interview, then a confirmed design brief. Never writes code | Optional. Only to turn an approved concept into a page-level brief (states, ranges, layout intent). Never instead of BriefMachine | Nothing durable; returns a brief |
| new work (plain request; `craft` is a deprecated alias) | Full flow: scope, direction round or pin, contract, build, inspect, finish review, documenter | DEVELOP build of the approved direction, pinned (section 4) | Surface brief; source; `.impeccable/mocks/`, `review/`, `build/`; `DESIGN.md` + `design.json` at finish |
| `document` | Records an existing visual system as `DESIGN.md` from code | When a built prototype or a client's existing site needs its system recorded. Client brand sources override what it infers | `DESIGN.md`, `.impeccable/design.json` (asks refresh / overwrite / merge if one exists) |
| `extract` | Pulls repeated patterns (3+ uses) into shared components and tokens | DEVELOP, multi-page prototypes only | Source refactor |
| `critique` | Design review (Nielsen 0-4, cognitive load, personas, design-specificity verdict) run in a subagent isolated from a detector + browser-overlay subagent, then merged | DEVELOP and JUDGE, on a rendered page | Report in chat; snapshot in `.impeccable/critique/` |
| `audit` | Technical checks: accessibility, performance, theming, responsive, implementation integrity; scored /20, P0-P3. Does not fix | JUDGE, before presentation | Report in chat; saved report |
| `polish` | Final refinement pass; reads the latest critique snapshot as its backlog and closes it when cleared | End of DEVELOP and after JUDGE fixes | Source |
| `bolder` / `quieter` | Amplify a timid design / calm a loud one | DEVELOP, when the critique names it | Source |
| `distill` / `clarify` / `layout` / `typeset` / `colorize` | Strip complexity / UX microcopy / spacing and hierarchy / type / strategic color | DEVELOP, one per named defect. `clarify` only on interface microcopy | Source |
| `animate` / `delight` / `overdrive` | Purposeful motion / personality touches / push past convention | DEVELOP, when motion or a signature moment is part of the concept | Source |
| `adapt` | Rework for another device or breakpoint | DEVELOP, responsive pass | Source |
| `harden` / `onboard` / `optimize` | Errors, i18n, edge cases / first-run and empty states / UI performance | Only the parts a prototype needs to show (states, empty, error). We do not ship production code | Source |
| `live` | Browser overlay: pick an element, generate variants, accept one into source via HMR | DEVELOP, local prototype with a dev server or static file | `.impeccable/live/`; temporary injection, removed on exit; may ask to change CSP |
| `generate [n] [action] [element]` | One-sentence fast lane into live: n variants of one element | DEVELOP, comparing variants of a hero, card or CTA block | As `live` |
| `hooks on/off/status/...` | Manages the post-edit detector hook | Not on by default here (installed `--no-hooks`). `status` is safe; `on` needs the user | `.claude/settings.local.json`, `.impeccable/config*.json` |
| `doctor` | Reports and repairs schema drift in its own artifacts | Maintenance, on request | `--fix` moves or rewrites its own files |
| `foundations` | Product-launch roadmap (secrets, 404, icons, CI, legal pages, error tracking) | **Do not use.** Production concerns; we build prototypes | Source, if run |
| `pin` | Creates a standalone `/<command>` shortcut | Only if the user asks | Skill files |

Shipped subagents (in `.claude/agents/`, tooling, not department agents): `impeccable-finish-reviewer` (read-only, judges a build against its contract and comp), `impeccable-documenter` (writes `DESIGN.md` from the built code), `impeccable-asset-producer` (raster plates from approved comps), `impeccable-manual-edit-applier` (applies live-mode copy edits). They are spawned by the flow; do not call them directly.

## 3. Files and where they must go

| File | Holds | CreativeEngine location |
|---|---|---|
| `PRODUCT.md` | Product truth | `projects/<client>/<project>/` (or the prototype folder inside it). Never the repo root |
| `DESIGN.md` | Visual system tokens and rules | Same folder. Never the repo root |
| `.impeccable/config.json` | `buildPath`, `projectRoots`, detector ignores, hook settings, `telemetry` | Project folder; a repo-root copy only for `projectRoots` and `telemetry`, with the user's approval |
| `.impeccable/config.local.json` | Per-developer overrides, hook consent | Gitignored by impeccable |
| `.impeccable/surfaces/*.md` | Surface brief and direction contract | Project folder |
| `.impeccable/mocks/`, `review/`, `build/`, `critique/`, `live/` | Comps, captures, diff reports, critique snapshots, live session journal | Project folder. Generated images follow the project's `work/generated/` rule; do not commit large rasters |

**Root resolution is the main risk.** Impeccable writes new files at the resolved project root and looks for context at that root, then `.agents/context/`, then `docs/`. In a monorepo, a folder without its own file falls back to the repository root. CreativeEngine is one git repo with no package workspaces, so by default the root is the repo root. Consequences and rules:

1. Never let a `PRODUCT.md` or `DESIGN.md` exist at the repo root, in `/docs/` or in `/.agents/context/`. Every client project would silently inherit it, which breaks client isolation.
2. Make each project its own root. Two ways: a repo-root `.impeccable/config.json` with `"projectRoots": ["projects/*/*"]` (persistent configuration: ask the user first), or always passing `--target projects/<client>/<project>/...` and checking where it resolved. **(unverified)** that `--target` alone changes where `init` writes; the docs describe `projectRoots` as the boundary mechanism.
3. After `impeccable context` runs, read the resolved `PRODUCT.md` / `DESIGN.md` paths it prints. If they point outside `projects/<client>/<project>/`, stop before any write.
4. **Client brand sources win.** Identity, palette, type, voice and mandatories come from `projects/<client>/client/`. `init` records them under Brand Commitments with their source paths; `document` and the documenter record what was built, and where that conflicts with an approved client source, the client source is right and the build is the defect. An inferred `DESIGN.md` is never a client brand source.
5. **One `DESIGN.md` per project.** `design-superpowers:/map-design` also writes `DESIGN.md` into the client project folder. Whichever runs second must merge, never overwrite (impeccable's `document` asks refresh / overwrite / merge; choose merge and show the user).
6. Provenance: `PRODUCT.md` is a derived project record. Facts carry their source (brief, packet, client file); open items are labeled open or proposed, never invented. It never feeds back into client knowledge without the normal promotion step.

## 4. A web design project end to end

### EXPLORE: concept first, impeccable mostly off

- The concept sentence (`barry-concept-art-direction.md` §1) and territories come first, with WordSmither. Impeccable does not generate ideas.
- Do not run `init`, new work or the direction roll on an undecided concept. The roll picks a **visual world**, not an idea; treated as the idea it replaces the concept with a catalog look.
- Permitted: `critique` or the detector on a competitor or current client site as **evidence** (findings are observations, not verdicts). The roll may be run once as labeled stimulus for one territory if the user wants it; it calls impeccable.style (section 6).
- Interaction risks are surfaced here as notes, not run through `audit`.

### DEVELOP: build, refine, critique

1. **Set the root** (section 3), confirm the engine is available (section 6).
2. **`init`** from the normalized brief, work packet and `projects/<client>/client/`. Platform `web`. Stack: plain HTML/CSS unless the format calls for more (prototypes, not production). Build path: **code-first** by default (`buildPath: "code"`); comp-first only for a flagship hero page, with the user's approval of the image-generation route and cost.
3. **Pin the direction.** Impeccable skips the roll and the decision page when the user or brief "pins whole" a direction: the world **and** the first-surface experience, in quotable words. Write the approved DesignChamp direction that way (concept sentence, visual world from client sources, first viewport) and confirm it with the user. The surface brief then records `seed: none (pinned)` with the quoted pin. Mode is usually Persuade for campaign and landing pages.
4. **Build.** It loads the craft floor before edits and writes the direction contract (THESIS, OWN-WORLD, STORY, FIRST VIEWPORT, FORM, FINISH) into the surface brief. Approved WordSmither copy goes in verbatim; it is told to ask before replacing factual copy or adding claims.
5. **Inspect and finish.** It captures desktop and mobile into `.impeccable/review/`, runs the detector once (no hook is wired), spawns the finish reviewer, acts on its disposition (`ship` / `fix` / `rebuild` / `recapture`), then the documenter writes `DESIGN.md`. Let it finish; an unreviewed build is unfinished by its own contract.
6. **Refine** with one command per named defect (`layout`, `typeset`, `clarify` for microcopy, `bolder`/`quieter`, `animate`, `adapt`), or `live` / `generate` for element variants on a running prototype.
7. **`critique`** on the rendered page, then `polish`, which consumes the critique snapshot. Judge whether the craft lands the idea with `visual-craft.md` and `typography.md` alongside, not instead.

### JUDGE: audit and finish review

- `audit` for accessibility, performance, theming, responsive and integrity (/20, P0-P3). P0 and P1 go back to DEVELOP.
- `critique` again if layout or flow changed materially. Its design-specificity verdict ("could an unrelated product use this unchanged?") is the useful brand-blind test; add our cross-client check: does it look like the last impeccable or unslop run on another client?
- Report the finish reviewer's disposition at its actual scope ("three fixes scored resolved", not "no issues remain"). Unverified behavior is listed as such (AGENT.md, Interaction design).
- CreativeDirector judges the idea and selection. Impeccable's scores are decision aids, like ours.

## 5. Division of labour

One tool per job; the most specific wins.

| Job | Use | Not |
|---|---|---|
| Whether the idea exists and reads | Barry, `pricken-idea-mechanisms.md`, CreativeDirector | impeccable roll, any skill |
| Whether craft lands the idea (focal point, grid, color jobs, imagery) | `visual-craft.md` | impeccable scores alone |
| Type job and face choice | `typography.md` decides; `typeset` executes | impeccable's font avoid-list overriding a client face |
| Build a web page from an approved direction, with a finish review and recorded system | impeccable new work | `frontend-design` and `design-taste-frontend` on the same page |
| Quick one-off component or artifact with no project records | `frontend-design` | impeccable (too heavy) |
| Anti-generic landing page or redesign without the records and gates | `design-taste-frontend` (taste-skill record; confirm its package installs) | impeccable on the same page |
| Clean up AI-looking or vibecoded UI | `unslop` (audit, five-line direction, nine passes) | impeccable `polish`, unless the page was built by impeccable |
| Broader interface work: critique with heuristics, bolder/quieter, harden, motion, live variants | impeccable | `unslop` |
| P0-P3 interface health and WCAG report for a deliverable | `design-superpowers:design-review` **or** impeccable `audit`/`critique`: pick one per review | both on one page |
| Recording a design language into `DESIGN.md` | impeccable `document` for code it built or a site with code; `/map-design` otherwise. One file, merged | two competing `DESIGN.md` files |
| Production landing page | `instapage-production` | impeccable (prototype only) |

## 6. Guardrails

**Needs the user's confirmation first** (CreativeEngine rules plus what the tool actually does):

| Action | Why |
|---|---|
| First `impeccable context` on a machine without the engine | The launcher downloads a binary from GitHub Releases (checksum-verified against `engine-checksums.txt`) into `~/.impeccable/bin/<version>/`. On this machine no engine was found on 2026-11-18, despite the record |
| `npx impeccable install` / `update`, `link`, `agents`, `telemetry` | Installs or changes tooling and settings |
| `/impeccable hooks on` (and `reset`) | Writes `.claude/settings.local.json`; the hook runs the engine unsandboxed with the agent's environment and network on every UI edit |
| Writing a repo-root `.impeccable/config.json` (`projectRoots`, `telemetry: false`) | Persistent configuration |
| `concept-seed` / direction roll | Calls `impeccable.style/api/roll`. Per the privacy page it sends a roll key, round, scope, mode and filters, not project names, paths or briefs. Optional choice reporting adds card type, position and catalog id. Recommend `"telemetry": false` or `IMPECCABLE_NO_TELEMETRY=1` |
| Comp-first or any `generate-image` call | Uses the harness image tool or `OPENAI_API_KEY`; prompts and reference images (screenshots of client pages) go to OpenAI and cost money. Follow the `artlist-production` rules: quote, confirm, label AI-drafted, pitch only, no client facts without approval |
| `live` CSP change | It asks before editing a Content Security Policy; still confirm |
| Signing in to impeccable.style, or opting into saved critique reports, health counts or `DESIGN.md` (changelog 4.9.0) | Would send client work to a third party. Do not opt in on client work. Details **(unverified)**: the privacy page does not cover this feature |
| Anything that publishes or deploys | Standard rule |

Background network with no confirmation step: a daily version check to `impeccable.style/api/version` (no project content; disable with `IMPECCABLE_NO_UPDATE_CHECK=1`).

**Working rules:**

- **Copy.** `clarify` and the craft floor may fix labels, button text, errors, empty states and status messages. Headlines, value propositions, chapter lines and any line carrying the idea go to `word-smither`. Comp prompts and builds use approved copy verbatim.
- **Client identity beats the craft floor.** The floor bans eyebrows/kickers outright, discourages hard offset shadows, glyph icons, gradient text and a list of "training-data default" faces (Inter as display, DM Sans, Space Grotesk, IBM Plex, Playfair and others). Where a client's approved system uses one, the client wins; record a narrow detector ignore with the reason `"user confirmed: client brand source <path>"` via `hooks ignore-value`, and never `ignore-rule` or `ignore-file` without the user.
- **Andres's own design work stays** (`WORKING-PREFERENCES.md`), even if a critique, detector or polish pass flags it. Flag and propose.
- **Prototypes, not production.** Its language is "ship" and "production-grade". Ours: hi-fi prototype in its real format. Skip `foundations`; use `harden` and `optimize` only for what the prototype must show.
- **No fake proof.** Impeccable already forbids invented customers, prices and benchmarks and labels synthetic demo data. Ours is stricter: claims come from the claim ledger or are labeled placeholder.
- **Never rerun context mid-session or repair drift unasked.** `CONTEXT_STALE` is reported, not acted on.
- **Raw is immutable.** A captured client site used as input is a raw source: work on a copy.

## 7. Worked example (generic)

Assignment: a campaign landing page prototype for a new service. A normalized brief and a landing-page work packet exist; client brand sources exist in `projects/<client>/client/`.

1. **EXPLORE.** DesignChamp and WordSmither produce three territories, each with a concept sentence. CreativeDirector advances one. Impeccable not used, apart from a detector scan of two competitor pages, filed as evidence.
2. **Set-up (DEVELOP).** Ask the user: engine download on first run, repo-root `.impeccable/config.json` with `projectRoots: ["projects/*/*"]` and `telemetry: false`. Then `impeccable context --target projects/<client>/<project>/work/prototype/`; confirm the resolved paths sit inside the project.
3. **`init`.** Users, purpose, positioning and evidence from the work packet; Brand Commitments from the client folder with paths; open items labeled. Platform web, stack static HTML/CSS, `buildPath: code`.
4. **New work, pinned.** Request names the world (client palette and type, the concept's one visual device) and the first viewport ("full-bleed product moment, approved headline over it, booking form visible without scroll"). User confirms the pin; no roll. Mode Persuade. Build with WordSmither's approved copy.
5. **Finish.** Desktop and mobile captures, one detector run, finish reviewer returns `fix` with three items; one batch, recapture, verdict scores all three resolved. Documenter writes `DESIGN.md`, merged with any existing `/map-design` file after the user chooses merge.
6. **Refine.** `critique` (dual-agent) gives 26/32 with a P1 on form error recovery and a weak secondary CTA. `clarify` on the form errors; WordSmither rewrites the CTA line; `generate 3 quieter variants of the benefits block` in live mode; `polish` closes the critique snapshot. `visual-craft.md` check confirms the focal point still carries the concept.
7. **JUDGE.** `audit` scores 17/20; one P1 contrast issue on the hero overlay fixed in DEVELOP. Report to CreativeDirector: audit and critique scores, the reviewer's verdict at its scope, unverified behavior (no real-device touch test), taste fit reported separately.
