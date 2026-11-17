# Bento family stories: plan, v01

```
CLIENT:       Miracles for Kids Charity
PROJECT:      website-rebrand
PAGE:         /family-stories (Webflow)
SOURCE BRIEF: ~/Downloads/Webflow Expressive Bento collection .txt (build handover v1.0, Nov 2026)
DECIDED BY:   Andres (CD), in chat, 2026-11-01
STATUS:       Planning. Not building yet. Not client-approved.
```

## Decisions

| # | Topic | Decision | Changes to the source brief |
|---|---|---|---|
| 1 | Shapes | Use the brief's five: circle, arch, hexagon, triangle, rounded star | None. Overrides the MFK-mark-derived shapes for this component |
| 2 | Color | Look A Saturated. Cards use every palette color at different saturation levels, each paired with its own shape | Replaces "flat pastel duotone" |
| 3 | Photos | Add a photo card variant: photo as full cover, title overlaid | Adds a variant; brief had no card image |
| 4 | CTA | "Learn more" | Replaces "View project ↗" |
| 5 | Filters | Program tags as filter categories. Untagged stories take the guessed tags. Finsweet Attributes filter | Categories = the five Programs |
| 6 | Volume | Finsweet pagination with load more | Brief stopped at 12 cards |
| 7 | Empty fields | Any optional field can be hidden; a card with a blank field must still render cleanly | New |
| 8 | Process | Build locally with the 36 scraped stories, validate, then implement in Webflow | — |

## What each decision needs

**1. Shapes.** One SVG per shape, built for the bottom-left crop (260px, about 75% hidden). Per-shape crop offsets for triangle, arch and star, as the brief warns.

**2. Color.** Look A core: royal #1B5FBF, orange #F99400 (action, navy text), sun #FFD23F, orange-700 #BB6F00 (display sizes only), white canvas.
- Need: the full Look A tonal scale (light / mid / saturated per hue) from Figma MFK-Andres v2, frame 26:6, color mode "A Saturated". Not yet in the repo.
- Rule to define: a card color set = background tone + shape tone of the same or a paired hue, and the text color that passes contrast on it (navy or white).
- Rule to define: neighbouring cards never repeat the same color set.
- Flag: `website-rebrand/DESIGN.md` describes a different system (five program hues, Anago type, magenta Donate). It predates Look A; confirm it is not the source for these cards.

**3. Photo variant.** Image covers the card; title on top with a scrim or solid color band for contrast; the expressive corner and 20px padding still apply. Shape: none or small, so it doesn't fight the photo. Uses `main_image_url` (all 36 have one). Crops: check faces against the card shapes in every grid span (3, 4, 5, 6 columns). Consent for every photo used.

**4. CTA.** "Learn more" across all variants. A visual label inside the card link, not its own link.

**5. Filters.** Chips from the Programs collection (Lifeline, Safe Haven, Balance, Boost, Pillars). Multi-select, OR logic, filter by slug.
- Tags for the 12 untagged stories come from `program_tags_guess` in `../research/webflow-family-stories.csv`. Label them as guesses until MFK confirms.
- Open: Abraham matched no program in the guess. Needs a tag before he can be filtered.
- Verify the Finsweet v2 filter setup and its after-render event against the installed version.

**6. Pagination.** Finsweet list load-more on 36 items.
- Define the page size so each page composes cleanly (e.g. 10 = 3+3+4, or 12 = 4+4+4).
- The composition engine recomposes all visible cards after each load and each filter change, in CMS order.
- Check how Finsweet filter and load-more interact (filter across all items, not just loaded ones).
- Rows past 12: define the repeat pattern so later rows don't drift into two-card rows.

**7. Hidden fields.** Each optional element (badge, description, index, photo, shape) collapses when empty or toggled off, without leaving gaps or breaking the card height. Webflow side: conditional visibility per field, plus an on/off switch where the editor should choose.

**8. Local build.** Static prototype using `../research/webflow-family-stories.json`, Finsweet loaded from CDN with the same attributes Webflow will use, and the composition script as a separate file so it moves to Webflow unchanged. Validated against the brief's §10 acceptance criteria plus decisions 2–7. Then a builder handover v1.1.

## CMS fields (planned)

Existing (from the scrape): name, slug, headline, preview, main image, gallery, body, program tags (multi-reference).

To add: Color set (option), Shape (option: circle, arch, hexagon, triangle, star), Card variant (option: shape, photo), Expressive corner (option: top-left, top-right, bottom-right; or assigned by the script), Sort order (number), show/hide switches for optional elements, and the video fields from `story-video-cms-fields_v01.md`.

## Resolved 2026-11-01

- **Consent:** all photo consent is provided (Andres).
- **Versions:** latest of everything: Finsweet Attributes v2 current release, current Webflow. Pin the exact version numbers at build time and record them in the handover.
- **Corner (recommended):** the script assigns it, with an optional CMS override.

### Corner rule (recommendation)

A fixed CMS corner can't work, because filtering and load-more move every card to a new grid position, and the expressive corner reads as part of the composition, not of the story. So the script decides from the position, after each recompose:

1. Never bottom-left: the shape sits there.
2. First card in a row: top-left. Last card in a row: top-right. Middle cards: bottom-right. The row reads as one framed unit, with corners pointing outward.
3. A single full-width card: top-right.
4. Vertical neighbours never share the same corner; if they would, the lower card swaps to bottom-right.
5. Photo variant: always a top corner, because the overlaid title sits at the bottom.
6. Override: CMS option "Corner" = Auto (default) / Top-left / Top-right / Bottom-right. Anything other than Auto wins over rules 2–4, never over 1 or 5.

Implement as a data attribute set by the script (`data-corner="tl|tr|br"`) and styled in CSS, so the rule is testable in the local build and editors never have to think about it.

### Look A palette (pulled from Figma MFK-Andres v2, file 9tYtPFq2Nek4tzaz5NOVq8, frame 26:6, 2026-11-01)

| Token | Value | Tier |
|---|---|---|
| `--mfk-color-bg-primary` | #1B5FBF royal | saturated |
| `--mfk-color-bg-accent` / `action-bg` / `shape-1` | #F99400 orange | saturated |
| `--mfk-color-shape-2` / `text-highlight-on-primary` | #FFD23F sun | saturated |
| `--mfk-color-text-primary` / `focus-ring` | #002855 navy | deep |
| `--mfk-color-text-highlight` | #BB6F00 orange-700 | deep, display sizes only |
| `--mfk-color-bg-soft` | #FFF5D5 sun-soft | soft |
| `--mfk-color-bg-secondary` | #F2F8FD sky-soft | soft |
| `--mfk-color-bg-canvas` | #FFFFFF | page |
| `--mfk-color-border-subtle` | #C7D0DA | line |
| `--mfk-color-text-secondary` | #5B6474 | text |

Figma has no mid tier. The file holds saturated and soft tones only.

**Card color sets** (background / shape / text). Each set gets its own shape so color and shape travel together:

| Set | Background | Shape | Text | Shape type |
|---|---|---|---|---|
| royal | #1B5FBF | #FFD23F | #FFFFFF | rounded star |
| orange | #F99400 | #FFD23F | #002855 | circle |
| sun | #FFD23F | #F99400 | #002855 | arch |
| navy | #002855 | #1B5FBF | #FFFFFF | hexagon |
| sun-soft | #FFF5D5 | #FFD23F | #002855 | triangle |
| sky-soft | #F2F8FD | #1B5FBF | #002855 | circle |
| royal-mid *(derived, not in Figma)* | #8DB0E2 | #1B5FBF | #002855 | arch |
| orange-mid *(derived, not in Figma)* | #FCC97F | #F99400 | #002855 | rounded star |

The mid sets are 50% tints of royal and orange onto white, labelled as proposals; add them to Figma if they pass review. Contrast is checked in the local build. Text colors follow Figma's `text-on-*` tokens.

Figma also shows the story filters as **All, Video, Read, Where Are They Now?** plus the five programs. That adds a story-format filter beside the program filter; confirm whether it's in scope.

- **Abraham:** placeholder tag **Lifeline** (his story describes the financial strain of a single mother with medical bills). Labelled PLACEHOLDER until MFK confirms.
- **Pagination:** Finsweet pagination, **12 cards per page**. 36 stories = 3 full pages, each composing as three rows of 4 cards (the brief's 12-card pattern). A filtered last page that isn't full composes from the table.

### Story-format filter (Andres, 2026-11-01: in scope)

Chips, as in Figma: **All · Video · Read · Where Are They Now?** then the five programs.

- **CMS:** new multi-reference or multi-option field "Format" (Video, Read, Where Are They Now?). A story can be more than one (a Read story that later gets a video).
- **Video** is driven by the Story video field: a story counts as Video once its video link is set, so the chip fills as the video rollout happens. Today it matches 0 stories; hide the chip until at least one video is live, so it never returns an empty grid.
- **Logic:** OR inside a group, AND across groups (Video + Lifeline = Lifeline stories that have a video). Verify the Finsweet v2 group setup for this.
- **All** clears every chip in both groups.
- **Data:** `format_guess` in `../research/webflow-family-stories.csv`. Every story is Read; Where Are They Now? is guessed from the story text and needs MFK confirmation.

## Local prototype (2026-11-02)

`../prototype/bento-stories/` (`build.py` renders `index.html` from the scraped JSON; serve on localhost:8450). Finsweet Attributes **2.7.1** (latest on npm) from jsDelivr.

What the build proved about Finsweet 2.7.1, for the Webflow handover:
- `fs-list-load="pagination"` and `fs-list-itemsperpage="12"` go on the **Collection List Wrapper** (`w-dyn-list`), not the list.
- Don't turn on Webflow's native pagination (`w-pagination-*`): Finsweet then fetches the next CMS page, and on a single page it duplicated every item. Set the Collection List to show all items (36, under the 100 limit) and let Finsweet paginate, so filters always search every story.
- Multi-reference values (programs, format) must render as a **nested Collection List** inside each item, each value an element with `fs-list-field`. Plain sibling elements only register the first value.
- Filter checkboxes need a `name` (Webflow adds one) plus `fs-list-field` and `fs-list-value`.
- Leave `fs-list-filtermatch` unset: default gives OR within a field and AND across fields. Setting it to `and` made chips inside a group require every value.
- Layout script recomposes from the items passed to the `render` hook, not from the DOM (the DOM still holds outgoing cards mid-animation).
- Local page needs a `window.Webflow` stand-in; real Webflow pages don't.

**Update 2026-11-02 (Andres):**
- **Quotes are their own item type in the same collection** (`type: "quote"` in `../research/webflow-family-stories.json`, with quote text, attribution, tone and source). 7 quotes: 6 real testimonials (Maribel, the Madrid family, Miranda M. ×2, Diego O., Denise M.; sources recorded) and 1 Figma content-test quote marked UNVERIFIED. In Webflow: a "Type" option (Story / Quote) plus a Sort Order field to place quotes between stories. No collection merge needed.
- **No nested tag lists inside cards.** Each card shows one badge. Programs and formats are hidden plain-text fields ("Lifeline, Boost"), and chips use `fs-list-operator="contain"`. Verified: every chip count matches the data (e.g. Safe Haven or Pillars 26, + Video 7). This removes the Webflow nested-list limit risk. Plain-text tags supersede the nested-list note above.
- Webflow code hosted as one external file (agreed).
- **Merged direction built (2026-11-02):** look from Figma Story Bento (193:1305) and Netlify v4; behaviour from this prototype. Card types: Photo (all read stories), Video Warm / Cool, Feature (double), Quote Blue / Cream. 4 columns as 3-spans on a 12-column track, 24px gap, 320px rows, 28px / 140px corners, v4 colour blocks, play button and hover. Rows fill in CMS order; a double that doesn't fit starts the next row. Cards with a play button never take the top-right corner. Shape cards, "Learn more" and card numbers removed.
- **Open items checked (2026-11-02):**
  - Jeremiah's video is 2:25 (YouTube lengthSeconds 145).
  - Quotes checked against miraclesforkids.org/families-weve-helped: Miranda M., Denise M., Diego O. VERIFIED (Miranda's two cards are one testimonial split in two; Denise's is an excerpt). Both Maribel quotes and the Figma content-test quote are NOT on the site: UNVERIFIED, need MFK's source. Status recorded per quote in the JSON (`verification`).
  - Tablet and phone: the script now lays out per breakpoint on the same 12-column track (4 / 2 / 1 per row) and re-runs on breakpoint change, so rows and corners match what's on screen. No overflow, no horizontal scroll, no clipped play buttons.
  - Motion: filter results rise in through Finsweet's `is-list-starting` class with `fs-list-stagger="35"` on items; page turns slide in from the side you're heading to (render hook, Web Animations). Reduced motion turns both off. Verified: Next +32px, Previous −32px, jump to page 4 +32px, filtering uses no slide.
  - Floating filter bar (v4) on phones ≤700px: chips become one sideways-scrolling row and dock at the bottom while the stories are on screen; they undock at the top.
  - Finsweet 2.7.1 does run its render hooks on page changes. Testing note: a background browser tab pauses requestAnimationFrame, which Finsweet waits on, so paging looks stuck. Test with the tab in front.
- **Real videos in the JSON:** William (1:43), Willow (3:01), Jeremiah (Feature, Where Are They Now?; no duration in v4), from the v4 deploy. Video chip: 3; Video or Where Are They Now?: 6.

Checked in the browser: 36 stories, 3 pages of 12; Safe Haven 7 (5/4/3 + 3/3/3/3); Safe Haven or Pillars 10 (5/4/3, 3/6/3, 3/3/3/3); one result spans 12; All clears; no shape overlaps text on any page at desktop width; tablet 2 columns, phone 1 column, no horizontal scroll.

## Open

- Mid-tier colors: approve or replace (decision 2)
- Which stories are Where Are They Now? (MFK to confirm)
- Webflow plan field limits
