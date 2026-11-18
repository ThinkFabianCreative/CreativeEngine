---
name: deck-designer
description: Plan and art-direct a CreativeEngine presentation - pitch, credentials, concept presentation, director treatment, vendor/production brief, creative review or feedback deck - before and while it is built. Chooses the narrative sequence, gives every slide one job, picks a layout archetype by asset format and content, sets a style direction (from the client brand, the user's request, or a named graphic design movement), then renders and checks every slide. Use when the user asks for a deck, slides or a presentation to be designed or laid out. Builds through existing tools (Figma Presentation_template components, frontend-slides, pptx, figma-use-slides); it is not a file generator itself.
---

# Deck designer

Adapted 2026-11-17 from an outside "Presentation Engine" package supplied by the user. The package's fixed Swiss/Inter house style is replaced by a style step: the look comes from the client, the request, or a chosen movement. Andres's own preference for Swiss design is used for his and TRAFFIK's internal decks.

This skill is method. DesignChamp owns the design judgment, WordSmither the slide titles and chapter lines, CreativeDirector the call on whether the deck is ready. `art-teacher` advises on style.

## Read first

- `shared/frameworks/editorial-presentation.md`: what makes a deck authored, not templated (rhythm, chapters, the turn, case studies, specificity).
- `shared/knowledge/deck-layout-archetypes.md`: slide shapes by asset format, content limits, fallbacks, candidate sequences.
- `ArtTeacher/knowledge/graphic-design-styles.md`: when a style or movement is requested or needs choosing.
- Inside a client workspace: `projects/README.md` and the client's `client/knowledge/` (brand standards win).
- For internal TRAFFIK decks: the Figma Presentation_template and Campaign slides components come first.

Load `typography.md`, `visual-craft.md` and `narrative-craft.md` only when the step needs them.

## Workflow

### 1. Discuss
Audience, the decision we want, the single takeaway, deck type (quick pitch, full pitch, credentials, concept, treatment, vendor, review, feedback), presented or read, format (Figma, HTML, PPTX), deadline, assets on hand. Ask only for what's missing.

### 2. Story
Pick a sequence from `deck-layout-archetypes.md` §4 as a starting point and bend it to the story (`narrative-craft.md`, `editorial-presentation.md` §3–§4). Write a slide list where every slide has one job and a title that states the point (WordSmither writes or approves titles).

### 3. Style
Decide the look before laying anything out, in this order:
1. **Client brand standards**, if it's a client deck. Never override them silently.
2. **The user's request**: if a movement or style is named ("make it Bauhaus", "Japanese poster feel", "Y2K"), use it, by principle not pastiche.
3. **Internal or Andres's own deck** with no other direction: start from Swiss / International Typographic Style (his preference).
4. Otherwise, propose two directions with reasons, from `graphic-design-styles.md`, matched to the audience, category and medium. Ask `art-teacher` when the choice is non-obvious.

Write the direction down as a short spec: movement or brand source, the principle taken, type roles (display, text, labels), grid, color jobs, image treatment, what to avoid.

### 4. Layout
For each slide: list its assets (format, ratio, count), choose an archetype from `deck-layout-archetypes.md` §2 that holds them at native ratio and readable size, respect the content limits in §3. Overflow means split or switch archetype; never shrink or crop critical content. Vary rhythm: no three identical shapes in a row; alternate quiet type moments, hero visuals and organized evidence.

### 5. Build
Hand to the build tool: Figma components (internal), `figma-use-slides`, `frontend-slides` (HTML; read its record), or `anthropic-skills:pptx`. Keep text and media editable. Use real screenshots and licensed or approved imagery; label placeholders. No invented data, quotes or results (`selling-the-work.md`).

### 6. Check
Render every slide at full size and at 50%. Check: hierarchy, alignment, clipping, overflow, stretched or distorted media, unreadable captions, fidelity to source (script text, storyboard order, data), rhythm across slides, attribution. Fix and re-render. Then CreativeDirector reviews; for craft issues use `critique-learning-loop.md` (max three fixes per round).

### 7. Ship
The editable file, a preview, and a short note of anything still placeholder or unverified.

## Never
- One layout repeated for the whole deck.
- Decoration that doesn't carry meaning: gratuitous gradients, glass, blobs, stock icons, device mockups that don't explain the work.
- Stretching, distorting or silently cropping someone's work.
- Reusing one client's look for another.
- Changing text on an "elevate" or aesthetic job: zero text changes; suggestions go in notes.
- Removing design elements Andres added; propose instead.
