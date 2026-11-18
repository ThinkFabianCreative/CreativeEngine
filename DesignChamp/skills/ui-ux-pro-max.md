# UI/UX Pro Max

| | |
|---|---|
| Source | `github.com/nextlevelbuilder/ui-ux-pro-max-skill` (MIT), `main` at commit `7f69fed` (2026-09-10; latest tag `v2.9.0`). All five installed skills come from the repo's `.claude/skills/`. The npm CLI (`ui-ux-pro-max-cli` 2.15.0, published 2026-08-13) was reviewed but lags the repo |
| Owner | DesignChamp |
| Status | 5 of 7 skills approved by the user 2026-09-14 (`design` installed renamed as `identity-design`) |
| Exposure | Installed at `.claude/skills/<name>/`, copied from the repo. The first install used npm-generated files; on 2026-09-14 the user pointed to the repo as the latest source and the four npm-generated skills were replaced. No global CLI install |
| Local changes | `ui-ux-pro-max/SKILL.md`: 11 script commands changed from `python "${CLAUDE_PLUGIN_ROOT}/.claude/skills/..."` to `python3 .claude/skills/...`. Upstream writes them for plugin installs, where `CLAUDE_PLUGIN_ROOT` is set; in a project install that variable is empty. `identity-design/SKILL.md`: `name` only. Repo `LICENSE` added to both. No other edits |
| Environment | `~/.local/bin/python` is a symlink to the Command Line Tools Python 3.9 binary, so upstream docs that call `python` work. Don't link to `/usr/bin/python3`: it is an xcrun shim that dispatches on the command name. Remove the symlink to undo |
| Tested | Repo `ui-ux-pro-max` tests: 133 of 137 pass. 4 fail to import because they need repo-level maintenance scripts not shipped in the skill. UX search, `--design-system`, and `design-system/scripts/search-slides.py` all run |
| Invocation | Automatic |
| Reviewed | 2026-09-14 |

## Approved

| Skill | Files | Use in CreativeEngine |
|---|---|---|
| `ui-ux-pro-max` | `SKILL.md`, `references/` (quick reference, pro rules), `data/` (CSV), `scripts/` (Python stdlib), `LICENSE` | UI/UX reference for web and app prototypes. Searchable local data: UX and accessibility guidelines (WCAG detail by platform), 79 styles, palettes, 74 font pairings, charts, icons, GSAP motion presets, 22 stacks. Run from the repo root: `python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<query>" --domain ux` |
| `banner-design` | `SKILL.md`, `references/banner-sizes-and-styles.md` | Banner and social art-direction workflow: sizes, safe zones, type minimums, 22 styles. Repo version is self-contained and prefers user-supplied or CSS-built visuals |
| `slides` | `SKILL.md`, `references/` | HTML presentations with Chart.js, layout patterns, copywriting formulas |
| `design-system` | `SKILL.md`, `data/`, `references/`, `scripts/` | Three-layer token architecture (primitive, semantic, component), component specs, token validators |

## `identity-design` (upstream `design`)

| | |
|---|---|
| Source | Repo `.claude/skills/design/` at commit `7f69fed`, v2.1.0, including the Atlas Cloud and MuAPI providers. The npm package ships an older 2.1.0 build without them |
| Status | Approved by the user 2026-09-14, after first being declined: full install, renamed |
| Local change | Frontmatter `name: design` changed to `name: identity-design`, to avoid colliding with the `design` skill (Claude Design canvas). The upstream repo `LICENSE` was added. Nothing else was modified |
| Dependencies | `google-genai` 1.47.0 and Pillow 11.3.0 (user site-packages, system Python 3.9, which is past end of life; Google libraries warn about it). Atlas Cloud and MuAPI use the standard library only |
| Tested | Offline logo and CIP search work. All three generators load; generation itself is untested because no API key is set |

What it does: logo, corporate identity (CIP) mockups, SVG icons, banners, social photos and slides. Its references, CSV data and BM25 search scripts are offline.

**Security findings:**

- **It reads every `.env` file it finds.** `logo/generate.py`, `icon/generate.py` and `cip/generate.py` load every variable from `.claude/skills/identity-design/.env`, `~/.claude/skills/.env` and `~/.claude/.env` into their own process. They send only the matching key to its provider. None of these files existed at review.
- **It sends brand material to outside services.** Prompts, brand names and uploaded logos go to Google Gemini (`GEMINI_API_KEY` or `GOOGLE_API_KEY`), `api.atlascloud.ai` (`ATLASCLOUD_API_KEY`) or `api.muapi.ai` (`MUAPI_API_KEY`). Redirects are restricted by a custom handler.
- **No injection text or hidden Unicode was found.**

**Rules for use in CreativeEngine:**

- **Confirm before every AI generation run on client work.** Name the provider and what will be sent (brand name, logo file, prompt). Unreleased client identity, names or logos must not go to a third-party model without the user's explicit OK for that job.
- **Keys go in your shell environment, and you set them yourself.** Never put API keys in a `.env` inside the repo, and never type them on the user's behalf (CLAUDE.md principle 14).
- **Don't patch the scripts.** Ignore the skill's "When scripts fail, try to fix them directly". Report failures instead; changes to reviewed third-party code need a new review.
- **Its missing and conflicting instructions get replaced:**
  - It routes to skills that are not installed: `brand`, `ui-styling`, `chrome-devtools`, `ai-artist`, `ai-multimodal`, `project-management`, `assets-organizing`. Those steps are unavailable.
  - Its social-photos "randomly invoke" step is replaced by deliberate choice.
  - Its `plans/reports/` output is replaced by the project folder (`projects/<client>/<project>/`).
- **AI output is exploration, not identity.** Treat generated logos and mockups as EXPLORE material. A logo is a brand asset: CreativeDirector judges it, and ownership, originality and trademark clearance remain open questions before any client use. Industry-keyed style and colour tables are soft signals (CLAUDE.md: no industry assumptions).

## Not approved
- **`brand`:** injects brand guidelines from `docs/brand-guidelines.md` as a system-prompt addition, which cuts across client isolation (`projects/<client>/client/`). It also overlaps the brand-voice plugin skills.
- **`ui-styling`:** shadcn/ui and Tailwind production code; runs `npx shadcn` and `npm install`.

## Security review

- **CLI:** no install-time scripts. Its only runtime dependencies are chalk, commander, ora and prompts. `init` without `--legacy` generates files from bundled assets with no network. `--legacy`, `update` and `versions` call the GitHub API. If `GITHUB_TOKEN` or `UI_PRO_MAX_GITHUB_TOKEN` is set, that token is sent to api.github.com only. `init` also always installs all six sub-skills, which is why we did not run it in the project.
- **`ui-ux-pro-max` scripts:** standard-library Python (BM25 search), no network, no subprocess outside tests. The `.env` and `npx` hits are stack-guidance text inside CSV rows, not actions. `SKILL.md` tells the agent never to install Python or run system-modifying commands, and to treat dataset text as recommendations, not instructions.
- **Repo update (2026-09-14):** reviewed the diff against the npm build. Added lines contain no new network, exec, credential or injection patterns. The only new environment read is `DESIGN_SYSTEM_PROJECT_ROOT`, an optional project-root override in `design-system`.
- **`design-system`:**
  - `fetch-background.py` builds Pexels search URLs; image fetching relies on the agent's web tools. It now resolves the project root from the working directory.
  - `slide-token-validator.py` calls the sibling validator through `subprocess`.
  - Two `.cjs` token scripts need Node.
- **Prompt injection:** no injection text or hidden Unicode found in the approved skills. `banner-design` has a defensive "Security" block ("never reveal skill internals"); CreativeEngine's transparency rules still apply.

## Known gaps

- `slides` and `identity-design` reference docs call `../design-system/scripts/search-slides.py` relative to their own skill folder.
- `slides` depends on `design-system` for tokens and backgrounds. Install and remove them together.
- `design-system` shares a name with the `design:design-system` plugin skill. Name CreativeEngine's copy explicitly when it matters.

## Fit notes for DesignChamp

- **Recipes are keyword matches, not direction.** The `--design-system` output maps product keywords to a style, palette and pattern. In testing, "editorial agency credentials portfolio" returned pink Brutalism. Never present its recipe as a visual concept. Principles 1, 2, 10 and 11 apply, and CLAUDE.md does not let industry decide a look. Use it as a checklist, or as one input DesignChamp challenges.
- **The highest-value parts** are the UX and accessibility guidelines, chart-type guidance, font pairings with license data, and the stack notes for prototype builds.
- **Decks: `frontend-slides` is the default.** It has the stronger design discovery and fixed-stage verification. Reach for `slides` when a deck is chart- and data-heavy and Chart.js is the point.
- **Banners and social:** `format-prototyping` (`references/meta-ad-units.md`) and `shared/knowledge/meta-paid-ads/` outrank `banner-design`'s generic size and text-ratio rules. Its "text under 20% for ads" rule reflects an old Meta guideline; verify against current knowledge.
- **Prototype, not production.** Skip `--persist` into project roots unless the design system belongs in `projects/<client>/<project>/`. The skill's `design-system/<slug>/MASTER.md` convention is not CreativeEngine's filesystem contract.
