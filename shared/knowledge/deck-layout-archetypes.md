# Deck Layout Archetypes

> Shared reference for `editorial-presentation.md`. Owner `design-champ`. A menu of slide structures chosen by content and asset format. Not a framework, not a style, not a template.

## Provenance and limits

Mined on 2026-11-17 from an outside "Presentation Engine" skill package supplied by the user (`CREATIVE_ENGINE_CLAUDE_SKILL_INSTALL.zip`). The package was not installed: it hard-coded one house look (Swiss style, Inter, white backgrounds) that conflicts with CreativeEngine's client-agnostic rule, and duplicated `editorial-presentation.md`, `typography.md`, `visual-craft.md` and the deck-building skills.

What is kept here is **structure only**: which slide shapes suit which content, content limits and fallbacks. Look, typefaces, colors and spacing tokens come from the client's brand or the project's art direction, never from this file. The package's own authors marked its archetypes as unvalidated proposals; the MAD Decks sequences are their hypotheses from a public product page, not reproductions. For internal TRAFFIK decks, the Figma Presentation_template and Campaign slides components still come first.

## 1. Pick by content, not variety

1. List the assets: format, aspect ratio, count, role.
2. Name each slide's job: setup, tension, evidence, reveal, demonstration, ask.
3. Keep only archetypes that hold the assets at native ratio and readable size.
4. Choose for meaning first, then rhythm (no three of the same shape in a row).
5. Overflow means split the slide or change archetype. Never shrink or crop critical content to fit.

## 2. Asset → archetype

| Input | Archetypes | Constraint |
|---|---|---|
| Desktop web page | Browser hero; long-scroll chapters (2–4 crops of one tall capture) | Never scale a full page to illegibility; slice by content region |
| Responsive UI | Desktop + mobile split; 3-breakpoint lineup | Label breakpoints; honest relative scale |
| Mobile flow | 3–5 screen sequence, numbered | Keep order and screen fidelity |
| 9:16 social | Vertical triptych | Avoid tiny unreadable verticals |
| 4:5 social | Portrait quartet | Keep 4:5 unless a crop is approved |
| 1:1 social / carousel | Square matrix; carousel sequence | Keep sequence order |
| Mixed placements | Mixed-ratio family | Every asset at its own native ratio |
| Film hero still | Cinematic 16:9 frame + director note | Restrained metadata |
| Storyboard | 3×2 six-up; film sequence | Shot order and labels kept |
| Script | A/V two-column | Exact approved script text; picture and audio matched by scene |
| Moodboard | Hero + satellites; contact sheet; territory comparison | Don't mix unrelated directions on one slide |
| Strategy | Manifesto; insight + proof; problem/opportunity; three pillars; quote; single metric | One claim per slide; a metric needs a verified number and a source |
| Feedback | Before/after two-up (same scale); annotated creative; action sheet | Every note points to an exact location, priority and owner |
| Production | Brief sheet; deliverable matrix; production sheet; non-negotiables | Tables over decoration |

## 3. Content limits and fallbacks (starting points)

| Archetype | Limit | Fallback |
|---|---|---|
| Manifesto / big idea | Headline 3–10 words, max 3 lines | Shorten, or move to insight + proof |
| Insight + proof | Headline ≤16 words; proof ≤45 words, one chart | Follow-on evidence slide |
| Problem / opportunity | Two statements ≤22 words each | Split; no bullet cramming |
| Three pillars | Three titles, ≤24 words each | More than three: stage across slides |
| Quote | ≤24 words plus attribution | Edit or split; don't shrink the quote |
| Metric hero | One verified number, label, source | More than three metrics: data slide |

## 4. Narrative sequences (candidate shapes)

From the package's reading of the four public MAD Decks modes. Planning aids, not slide quotas; `narrative-craft.md` and `editorial-presentation.md` §3–§4 decide the actual shape.

- **Quick pitch (~7):** cover → tension → insight → idea reveal → hero visual → executions → ask.
- **Full pitch (~19):** cover → agenda → situation → audience → cultural context → tension → insight → proposition → territory → idea reveal → articulation → film → storyboard → social → web → responsive → OOH → rollout → ask.
- **Vendor / production (~14):** cover → assignment → intent → tone → references → cinematography → light and color → casting → locations → script → storyboard → non-negotiables → deliverables → timing.
- **Feedback (~6):** cover → summary → before/after → callouts → frame corrections → action list.
- **Director treatment:** emotional promise → interpretation → story → characters → world → camera → light → edit and sound → execution confidence.
- **Brand transformation:** past → pressure → principle → identity → system → applications → governance.
- **UX / product concept:** human problem → evidence → principle → experience → flow → responsive proof → outcomes → decision.

## 5. Render check

Render every slide at full size and at 50%. Check clipping, overflow, stretched media, unreadable captions, source fidelity (script text, storyboard order, data) and slide-to-slide rhythm. A checklist is not a substitute for looking.
