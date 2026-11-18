# Taste-Skill pack

| | |
|---|---|
| Source | `github.com/Leonxlnx/taste-skill` (MIT), repo state of 2026-08-24 |
| Owner | DesignChamp |
| Status | Approved by the user 2026-09-13 as a full pack |
| Exposure | Installed 2026-09-17 in `.claude/skills/<install name>/`: 14 files copied unchanged from commit `ccbc15639c` (the reviewed 2026-08-24 state), fetched file by file from GitHub raw URLs. Nothing executed. Sizes matched GitHub's tree listing; security scan repeated with the same result |
| Upstream after review | HEAD `e79ca9e` (2026-09-16) changes only README.md and a sponsor image; no skill file differs from the installed copy |
| Reviewed | 2026-09-13 |

## Skills

| Install name | Repo folder | Job |
|---|---|---|
| `design-taste-frontend` | `taste-skill` | Default anti-generic frontend skill for landing pages, portfolios and redesigns (v2 experimental) |
| `design-taste-frontend-v1` | `taste-skill-v1` | Original v1, kept for backward compatibility |
| `gpt-taste` | `gpt-tasteskill` | GSAP-heavy "Awwwards" frontend with simulated random layout selection |
| `image-to-code` | `image-to-code-skill` | Generate design images first, then implement code to match |
| `imagegen-frontend-web` | `imagegen-frontend-web` | Website design reference images, one per section. No code |
| `imagegen-frontend-mobile` | `imagegen-frontend-mobile` | Mobile app screen concept images. No code |
| `brandkit` | `brandkit` | Brand-kit boards: logo concepts, identity systems, palettes, typography, mockups. No code |
| `redesign-existing-projects` | `redesign-skill` | Audit and upgrade an existing site's design |
| `high-end-visual-design` | `soft-skill` | Soft, "expensive" UI look |
| `full-output-enforcement` | `output-skill` | Bans truncation and placeholder code |
| `minimalist-ui` | `minimalist-skill` | Editorial monochrome minimalism |
| `industrial-brutalist-ui` | `brutalist-skill` | Swiss / terminal brutalism (beta) |
| `stitch-design-taste` | `stitch-skill` | DESIGN.md rules for Google Stitch (ships a `DESIGN.md` alongside `SKILL.md`) |

## Security review

- All skills are Markdown instructions. No bundled executables. `skill.sh` only prints a path; `scripts/*.mjs` process README images and are not part of any skill.
- No credential access, destructive commands, hidden characters or prompt-injection text found.
- `design-taste-frontend` and `design-taste-frontend-v1` instruct running package installs (`npm install`, `npx shadcn`) when building a site. Treat those as normal dependency actions needing the usual confirmation.
- External URLs are design-system documentation and placeholder image hosts only.
- Full text was pattern-scanned; not every file was read line by line.

## Fit notes for DesignChamp

- Most of the pack is web UI engineering (React, Tailwind, GSAP). Closest to CreativeEngine's visual work: `brandkit`, `imagegen-frontend-web`, `imagegen-frontend-mobile`.
- The skills carry house aesthetics (em-dash ban, spring-only motion, bento grids, "Awwwards-tier" polish). Use them as methods, not taste. DesignChamp keeps judgment on distinctiveness (CLAUDE.md principles 1, 2, 10, 11) and should not let a skill's preset look replace a concept.
- `gpt-taste` relies on simulated randomness to force layout variety; prefer real divergent exploration.
- Overlaps DesignChamp's own visual-criteria role; watch for duplication as DesignChamp's `AGENT.md` is designed.
