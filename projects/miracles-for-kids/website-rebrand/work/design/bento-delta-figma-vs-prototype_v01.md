# Bento delta: Figma reusable grids vs local prototype, v01

```
CLIENT:   Miracles for Kids Charity
PROJECT:  website-rebrand
FIGMA:    MFK-Andres, node 193:1305 "MFK / System refinement / Review" (sections 03–06)
PROTO:    ../prototype/bento-stories/ (localhost:8450)
DATE:     2026-11-02
STATUS:   Comparison only. Nothing changed in either.
```

Figma read through the Figma MCP (metadata + screenshots). Measurements below are frame sizes from metadata; radii, type sizes and colors are read off screenshots and need confirming with design context before build.

## Grid

| | Figma | Prototype | Delta |
|---|---|---|---|
| Structure | 4 equal columns (282 / 270 wide in 1200), double span = 588–612 | 12 columns, spans 2–12 | Figma is a 4-col system expressed as fixed compositions; prototype computes 12-col spans. 4 cols = spans of 3 / 6 in a 12-col grid, so Figma fits inside ours, but our 5/4/3, 3/6/3, 4/2/3/3 variety does not exist in Figma |
| Gutter | 24px | 16px | Change to 24 |
| Row height | Fixed 320px (one stray card at 324/328) | Content height, min 320 | Figma rows are uniform; fix 320 |
| Tall card | Feature spans 2 cols × 2 rows (612×664) beside a 2×2 stack (§04) | None | Missing: tall feature |
| Two-card rows | Allowed: Photo + Quote at 588 + 588 (§04), 2-col compositions (§05) | Forbidden on desktop (brief rule) | **Conflict** with the build brief's "no two-card rows" |
| Row mixes | 4 singles; 1 double + 2 singles; tall + 2×2; 2 doubles | Table-driven 1–12 | Figma compositions are named, reusable layouts, not a count table |
| Responsive | Explicit 2-col (744) and 1-col (342) compositions (§05) | CSS fallback 2 / 1 col | Figma designs the narrow versions; ours only reflows |

## Card variants

| Figma component | Content | Prototype equivalent | Delta |
|---|---|---|---|
| Story Card / **Video Warm** (cream bg, yellow flood) | Play button top-right, "Video Story" badge, title, duration pill | none | Missing (no video data yet; wait for video field) |
| Story Card / **Video Cool** (sky-soft bg, orange flood) | same as above | none | Missing |
| Story Card / **Quote Blue** (royal bg, white text) | Quote + attribution, no title, no badge | none | Missing; needs a Quote field in CMS |
| Story Card / **Quote Cream** (cream bg, navy text) | Quote + attribution | none | Missing |
| Story Card / **Photo** | Full-bleed photo, white badge, white title + one-line description directly on photo | Photo variant | Ours puts title on a solid color panel; Figma sets white text straight on the photo (check contrast) |
| Story Card / **Feature** (orange, peach quarter-circle flood) | Big play button, badge, large title (~36px), description | none | Missing: large feature card |
| — | — | Shape card (color set + bottom-left SVG shape) | **Not in Figma.** Figma has no circle/hexagon/star cards |

## Card anatomy

| | Figma | Prototype |
|---|---|---|
| Expressive corner | One large corner, mostly top-left or top-right (~100–150px); small corners ~24px | 88px expressive, 16px standard |
| Decorative shape | Large flat flood blocks (rectangle, quarter-circle) behind badge/title at bottom-left, part of the card fill | 260px SVG shape, 75% cropped, behind a reserved band |
| Badge | White pill, navy text | Translucent pill |
| Title | Outfit Bold ~24px (Feature ~36px) | Outfit Bold 20–26px |
| Description | Only on Photo / Feature, 1–2 lines | Every card, 1 line ellipsis |
| CTA | None (whole card is the link; play button on video) | "Learn more →" |
| Index number | None | 01–36 |
| Play button | Orange circle (white on Feature), ~80px, top-right | none |
| Duration pill | White pill, e.g. "1:43" | none |
| Title wrap test | Boundary note + "Title wrap test" (§06) | Balanced wrap, no line cap |

## Color

Figma cards use: cream #FFF5D5-ish, sky-soft #F2F8FD, royal #1B5FBF, orange #F99400, sun #FFD23F, a peach tint (not in the token list we pulled). No navy card, no royal-mid / orange-mid. Our 8 sets include navy plus two derived mids that Figma doesn't use; Figma uses a peach that our sets don't.

## Filters / content model

Figma's variants imply CMS fields we haven't planned: **quote text, quote attribution, video duration** (and video link). Badge text in Figma is the format ("Video Story", "Where Are They Now?", "Story") or a program ("Lifeline"); ours is always the first program.

## What lines up

- Look A palette and Outfit type
- One expressive corner per card, bottom-left kept standard
- Photo variant, badge, left-aligned content
- Filter vocabulary (Video, Read, Where Are They Now?, programs)

## Decisions this delta needs

1. **Source of truth for the grid:** Figma's named compositions (4-col, fixed 320 rows, tall feature, two-card rows allowed) or the brief's count-driven 12-col engine. Ours can host Figma's patterns, but the brief's "no two-card rows" has to go if Figma wins.
2. **Shape cards:** drop them for Figma's flood-block cards, or keep both.
3. **CTA, index, description on every card:** Figma has none of these.
4. **Quote and Feature cards:** add, with Quote fields in the CMS.
