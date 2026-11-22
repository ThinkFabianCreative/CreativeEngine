# Jakub Krehel skills (`interfaces` plugin)

- **Source:** `github.com/jakubkrehel/skills`, MIT, plugin `interfaces` v1.22.0
- **Reviewed commit:** `547d415` (2026-11-18)
- **Owner:** DesignChamp (Interaction design specialty)
- **Status:** Approved and installed in `.claude/skills/` 2026-11-18: `better-typography`, `better-colors`, `better-layout`, `better-accessibility`, `better-interface` (`agents/` folders removed). `explain-interface` not installed.
- **Found via:** a web inspiration list the user shared (`shared/knowledge/web-inspiration-sources.md`)

## What it is

There are 15 skills, all Markdown. Each one comes with a small `agents/openai.yaml` that sets its display name for other harnesses. Seven are model-invoked craft skills (`better-*`, `build-design`) and eight are user-invoked workflows (`disable-model-invocation: true`).

## Review against CLAUDE.md

| Check | Finding |
|---|---|
| 1. SKILL.md read | Yes for all 15: front matter and scope, with full bodies for `better-typography`, `better-writing`, `afk` and the privacy section of `upskill` |
| 2. Scripts or executables | None. No `.sh`, `.py` or `.js` files. Manifests are plain JSON and YAML |
| 3. Permissions and actions | Craft skills edit the project's CSS and components. `explain-interface` `curl`s a public page and its stylesheets when no browser is available. `interface-review` runs `git diff` and `gh pr view`, read only. `afk` creates a local branch or worktree and commits unattended for hours. `upskill` reads the user's whole Claude session history |
| 4. Suspicious or unrelated instructions | None found. The text is well scoped and pushes back on its own overreach (for example, "never propose a new typeface unless the task asks") |
| 5. Credential access | None asked for. `upskill` reads session logs that may hold pasted secrets; it redacts them and sends nothing outside, but the exposure is still real |
| 6. Destructive commands | None. `afk` explicitly forbids push, merge, deploy and posting unless asked |
| 7. Overlap | `better-ui` overlaps `apple-design`, `design-motion-principles` and the Emil Kowalski skills. `better-writing` overlaps `design:ux-copy` and WordSmither's voice ownership. `build-design` overlaps `figma:figma-design-to-code`. `better-interface` partly overlaps `impeccable` and `design:design-critique` |
| 8. Does it improve CreativeEngine? | Yes, in part. The type, colour, layout and accessibility skills give exact, measurable web values, which fills a gap between `typography.md` and `visual-craft.md` (judgment) and the prototype code |

## Recommendation

**Install (5):**
- `better-typography`: measurable web type rules (line-height by role, measure, tracking, weights under 18px). It checks rendered prototypes against `typography.md`.
- `better-colors`: palette ramps, token naming and contrast measurement.
- `better-layout`: grouping, reading order, resize, translation and RTL stress tests.
- `better-accessibility`: WCAG 2.2 checks for prototypes and Instapage QA.
- `better-interface`: one ranked report across the skills above. Use it in JUDGE on rendered web work.

**Optional (1):**
- `explain-interface`: lets CreativeResearcher explain how a reference site's effect is built (useful for 3D and GSAP studies). It is user-invoked, and it fetches only public URLs.

**Do not install:**
- `afk` (unattended commits; wrong fit for a creative repo) and `upskill` (reads private session history).
- `interface-review`, `break`, `state-machine` and `variant`: product-engineering workflows with little use here.
- `better-ui`, `better-writing` and `build-design`, because installed skills already cover them (row 7).

## Calibration if installed

- These skills judge craft only, never the idea. `typography.md`, `visual-craft.md` and `creative-engine-director` keep the verdict.
- They stay client-agnostic. Values come from the project's own tokens, never from the skill's examples.
- Their findings go to prototypes. Instapage production follows `instapage-production`.
- No craft score counts as a gate in EXPLORE.

## Install method (after approval)

Copy the chosen skill folders from the reviewed commit into `.claude/skills/`, leaving out `agents/openai.yaml`, and list them in `.claude/skills/README.md`. Do not add the whole plugin, because that would also install `afk` and `upskill`.
