# Deck designer

| | |
|---|---|
| Source | CreativeEngine (in-house), adapted from an outside "Presentation Engine" package supplied by the user (`CREATIVE_ENGINE_CLAUDE_SKILL_INSTALL.zip`, reviewed 2026-11-17) |
| Owner | DesignChamp (used by WordSmither for titles and CreativeDirector for review; `art-teacher` advises on style) |
| Status | Built and installed in `.claude/skills/deck-designer/` 2026-11-17 at the user's request |
| Invocation | Automatic when a deck is to be designed or laid out |

## What it does

Plans and art-directs a deck: discuss → story → style → layout → build → check → ship. It does not generate files itself; it hands the build to Figma components, `figma-use-slides`, `frontend-slides` or `pptx`.

## What changed from the package

- No fixed house style. Style comes from client brand standards, then the user's request (any graphic design movement, from `ArtTeacher/knowledge/graphic-design-styles.md`), then Swiss for Andres's own and internal decks, otherwise two proposed directions.
- Layout data lives in `shared/knowledge/deck-layout-archetypes.md`; deck craft in `editorial-presentation.md`. The skill points to them and doesn't repeat them.
- Unverified material from the package (pixel geometries, Figma Community and MAD Decks mappings) is kept as candidate structure only.
- Review: text only, no scripts, no credential access.

## Rules that govern its use

- Client brand standards win over any style.
- Internal TRAFFIK decks use the Figma Presentation_template and Campaign slides components.
- Aesthetic "elevate" jobs: no text changes.
- MAD Decks material needs the actual permission on file before anything leaves the team.
