# Claude-native skills

This is where Claude discovers CreativeEngine's skills automatically. Each skill lives in its own folder: `.claude/skills/<skill-name>/SKILL.md`.

| Skill | Owner | Record |
|---|---|---|
| `humanizer` | WordSmither | `WordSmither/skills/humanizer.md` (calibrated for advertising copy) |
| `format-copywriting` | WordSmither | `WordSmither/skills/format-copywriting.md` (in-house) |
| `format-prototyping` | DesignChamp | `DesignChamp/skills/format-prototyping.md` (in-house) |
| `ad-reference` | DesignChamp (used by WordSmither and CreativeDirector) | `DesignChamp/skills/ad-reference.md` (in-house) · reads Ads of the World; links and our analysis only, never copies |
| `artlist-production` | DesignChamp (WordSmither supplies scripts, voiceover, hooks and lyrics) | `DesignChamp/skills/artlist-production.md` (in-house) · drives the Artlist MCP; inspiration and pitch only, never commercial; every call spends credits: quote and confirm each batch |
| `instapage-production` | DesignChamp (WordSmither's copy, BriefMachine's ask and CreativeDirector's approval are inputs) | `DesignChamp/skills/instapage-production.md` (in-house) · native Instapage production through the Instapage MCP; Native Authorability; client-agnostic; never publishes without explicit approval |
| `frontend-slides` | DesignChamp | `DesignChamp/skills/frontend-slides.md` |
| `ui-ux-pro-max` | DesignChamp | `DesignChamp/skills/ui-ux-pro-max.md` |
| `banner-design` | DesignChamp | `DesignChamp/skills/ui-ux-pro-max.md` |
| `slides` | DesignChamp | `DesignChamp/skills/ui-ux-pro-max.md` (depends on `design-system`) |
| `design-system` | DesignChamp | `DesignChamp/skills/ui-ux-pro-max.md` |
| `identity-design` (upstream `design`, renamed) | DesignChamp | `DesignChamp/skills/ui-ux-pro-max.md`. Sends prompts and logos to Gemini, Atlas Cloud or MuAPI: confirm per client job |
| `design-taste-frontend` | DesignChamp | `DesignChamp/skills/taste-skill.md` (Taste-Skill pack) · runs package installs when building a site: confirm them |
| `design-taste-frontend-v1` | DesignChamp | `DesignChamp/skills/taste-skill.md` (Taste-Skill pack) |
| `gpt-taste` | DesignChamp | `DesignChamp/skills/taste-skill.md` (Taste-Skill pack) · prefer real divergent exploration over its simulated randomness |
| `image-to-code` | DesignChamp | `DesignChamp/skills/taste-skill.md` (Taste-Skill pack) |
| `imagegen-frontend-web` | DesignChamp | `DesignChamp/skills/taste-skill.md` (Taste-Skill pack) |
| `imagegen-frontend-mobile` | DesignChamp | `DesignChamp/skills/taste-skill.md` (Taste-Skill pack) |
| `brandkit` | DesignChamp | `DesignChamp/skills/taste-skill.md` (Taste-Skill pack) |
| `redesign-existing-projects` | DesignChamp | `DesignChamp/skills/taste-skill.md` (Taste-Skill pack) |
| `high-end-visual-design` | DesignChamp | `DesignChamp/skills/taste-skill.md` (Taste-Skill pack) |
| `full-output-enforcement` | DesignChamp | `DesignChamp/skills/taste-skill.md` (Taste-Skill pack) |
| `minimalist-ui` | DesignChamp | `DesignChamp/skills/taste-skill.md` (Taste-Skill pack) |
| `industrial-brutalist-ui` | DesignChamp | `DesignChamp/skills/taste-skill.md` (Taste-Skill pack) |
| `stitch-design-taste` | DesignChamp | `DesignChamp/skills/taste-skill.md` (Taste-Skill pack) · ships `DESIGN.md` |
| `apple-design` | DesignChamp | `DesignChamp/skills/emil-kowalski-skills.md` (Emil Kowalski) · interface interaction, not ad typography |
| `animate` | DesignChamp | `DesignChamp/skills/emil-kowalski-skills.md` (Emil Kowalski) · interface motion inside prototypes, not ad motion |
| `review-animations` | DesignChamp | `DesignChamp/skills/emil-kowalski-skills.md` (Emil Kowalski) · manual only |
| `animation-vocabulary` | DesignChamp | `DesignChamp/skills/emil-kowalski-skills.md` (Emil Kowalski) |
| `prototype` | DesignChamp | `DesignChamp/skills/emil-kowalski-skills.md` (Emil Kowalski) · manual only; skip Phase 6 (promote to production) |
| `marketing-ideas` | BriefMachine | `BriefMachine/skills/marketing-ideas.md` (coreyhaines31/marketingskills) · manual only; tactics, not ideas; SaaS-centric, translate for other clients |
| `wait-what` | WordSmither (any role) | `WordSmither/skills/wait-what.md` (mattpocock/skills) · manual only; re-pitch the last message plainly; uses CLAUDE.md vocabulary, no GLOSSARY.md |

## Before adding a skill

1. Audit its `SKILL.md`.
2. Inspect its scripts and executable components.
3. Check what permissions and actions it expects.
4. Check for credential access.
5. Check for destructive commands.
6. Check for overlap with existing skills, including installed plugin skills.
7. Assign an owning CreativeEngine department.
8. Get the user's approval.

The full review policy is in the root `CLAUDE.md`.

## Department skills folders

`BriefMachine/skills/`, `DesignChamp/skills/` and `WordSmither/skills/` are organizational and registry areas. They record which department owns a skill and hold evaluation notes. Claude does not discover skills from them.

When we approve an executable Claude skill, we will decide how to expose it here without creating confusing duplicate copies.
