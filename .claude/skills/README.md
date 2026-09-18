# Claude-native skills

This is where Claude discovers CreativeEngine's skills automatically. Each skill lives in its own folder: `.claude/skills/<skill-name>/SKILL.md`.

| Skill | Owner | Record |
|---|---|---|
| `humanizer` | WordSmither | `WordSmither/skills/humanizer.md` (calibrated for advertising copy) |
| `frontend-slides` | DesignChamp | `DesignChamp/skills/frontend-slides.md` |
| `ui-ux-pro-max` | DesignChamp | `DesignChamp/skills/ui-ux-pro-max.md` |
| `banner-design` | DesignChamp | `DesignChamp/skills/ui-ux-pro-max.md` |
| `slides` | DesignChamp | `DesignChamp/skills/ui-ux-pro-max.md` (depends on `design-system`) |
| `design-system` | DesignChamp | `DesignChamp/skills/ui-ux-pro-max.md` |
| `identity-design` (upstream `design`, renamed) | DesignChamp | `DesignChamp/skills/ui-ux-pro-max.md`. Sends prompts and logos to Gemini, Atlas Cloud or MuAPI: confirm per client job |

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
