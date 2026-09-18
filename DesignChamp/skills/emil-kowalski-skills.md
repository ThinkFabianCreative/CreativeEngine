# Emil Kowalski skills

| | |
|---|---|
| Source | `github.com/emilkowalski/skills` (MIT), repo state of 2026-08-21 |
| Owner | DesignChamp |
| Status | 5 of 12 approved by the user 2026-09-13 |
| Exposure | Installed 2026-09-17 in `.claude/skills/<name>/` with supporting files (8 files) copied unchanged from commit `d23d7f88a2` (the reviewed 2026-08-21 state), fetched file by file from GitHub raw URLs. Nothing executed. Sizes matched GitHub's tree listing; security scan repeated with the same result |
| Upstream after review | HEAD `85e8e23` (2026-09-15) modifies all five approved SKILL.md files and adds `mobile-native`. Those changes are **unreviewed and not installed**. Updating requires a new review against the eight steps and user approval |
| Reviewed | 2026-09-13 |

## Approved

| Skill | Files | Use in CreativeEngine | Invocation |
|---|---|---|---|
| `apple-design` | `SKILL.md` | Interaction principles for interactive prototypes (response, direct manipulation, interruptibility, gestures, feedback, wayfinding), materials and depth, screen micro-typography | Automatic |
| `animate` | `SKILL.md`, `RECIPES.md` | Building interface motion inside HTML prototypes | Automatic |
| `review-animations` | `SKILL.md`, `STANDARDS.md` | Strict critique of interface motion | Manual only |
| `animation-vocabulary` | `SKILL.md` | Naming motion precisely when directing, briefing or prompting | Automatic |
| `prototype` | `SKILL.md`, `PICKER.md` | EXPLORE: 3 to 5 genuinely divergent variants on named axes, full size in context, behind a live picker | Manual only |

## Not approved

`emil-design-eng` (largely duplicated by `animate` and `review-animations`, code-heavy, opens with a course promotion), `find-animation-opportunities` and `improve-animations` (codebase audits), `animate-expo`, `write-swift`, `ask-sonner`, `pick-ui-library` (native-app and production code).

## Security review

- Markdown only. No bundled executables.
- Only commands: `npx expo install` in `animate-expo` (not approved).
- Zero-width spaces in `improve-animations/PLAN-TEMPLATE.md` escape nested code fences; benign.
- No credential access, destructive commands or prompt-injection text. Two skills explicitly treat repository content as data.
- External URLs are the author's sites, easing tools and library documentation.

## Calibration for DesignChamp

- **Interface motion is not advertising motion.** Rules such as "UI animations stay under 300ms", "never ease-in on UI" and the frequency-of-use gate apply to interactive elements inside prototypes: buttons, menus, sheets, form states. They do not govern storytelling motion in rich media sequences, Reels, film, DOOH loops or scroll narratives. That belongs to `shared/frameworks/animation-craft.md` (planned).
- **`prototype`:** skip Phase 6 (promote into a production codebase) and its prototype-surface deletion; CreativeEngine builds prototypes only. Its no-project default look (neutral grays, one accent, system font) is a placeholder, not a direction: variants take their look from the brief and the brand.
- **`apple-design` typography** says to default to the system font. That fits product UI, not distinctive advertising or brand work, where typeface choice is a creative decision (`shared/frameworks/typography.md`).
- `apple-design`'s materials guidance supports translucency as an option, consistent with `ANDRES_CREATIVE_OS.md`: it must earn its place and preserve readability.
