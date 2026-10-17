# MFK website rebrand — resume on another computer

Saved 2026-10-17 after Claude reached its session limit.

## Resume

Repository: https://github.com/ThinkFabianCreative/CreativeEngine
Branch: `handoff`

Clone the repository and check out `handoff`, or pull that branch in your existing checkout. Start with this file and the project README.

The current editable prototype is `work/prototype/index.html`. It is standalone HTML/CSS/JavaScript, not a React application. No build or package installation is required. From the repository root run:

```sh
python3 -m http.server 8430
```

Then open:
http://localhost:8430/projects/miracles-for-kids/website-rebrand/work/prototype/index.html

The old Claude scratchpad preview is a temporary copy; use the repository version as the source of truth.

## Transfer images separately

These folders are deliberately excluded from Git and must be copied from the original computer into the same project-relative locations:

- `raw/MiraclesForKids/`
- `raw/production-site/` (including `logos/`)

`work/prototype/local-assets-manifest.json` lists the 25 unique image paths used by the prototype. All exist on the source computer at handover. A Git-only clone will have missing images until these folders are transferred. No shared cloud asset location has been confirmed.

## Current state

- Prototype v3 implements Color B + Type A and Copy v02, with friendly 4:3 image crops, rounded arch/star/asterisk geometry, program bento/zipper layout, pattern backgrounds, full-color hospital logos, inset urgency capsule, and shaped event cards.
- Latest design review: `work/reviews/design-review_prototype-v3_v01.md`. Its checklist was not updated after implementation; verify the page rather than assuming every item is finished.
- Figma working file: https://www.figma.com/design/9tYtPFq2Nek4tzaz5NOVq8/MFK-Andres ; v3 node `30:94`. HTML received subsequent changes and may differ from Figma.
- Fonts and color token sources are in `work/design/tokens/`. Copy and strategy sources are under `work/copy/` and `work/strategy/`.
- Current HTML includes donation dialog, story filters, hover/press effects and reduced-motion styles. This remains a design prototype, not a completed production site.

## Latest design direction from Andres

- Organic button exploration: the **soft blob** is closer than straight geometric buttons or a ragged paint swash. See `work/design/button-exploration/handmade-buttons.svg` (middle option). These are separate studies, not applied to the prototype.
- Section dividers should use custom SVGs like Elementor: soft, asymmetrical organic curves, matching adjacent background colors, responsive heights, no seams or overflow. This direction has not been newly implemented by the handover task.
- Prior requests: critique every section; 4:3-friendly image masks; rounded arches, rounded asterisks and stars, friendly geometry; avoid heart-shaped masks; improve “Five ways we help”; explore bento, carousel and zipper layouts and background patterns.

## Next work

1. Transfer the ignored image folders and verify all images load over HTTP. The supplied Claude screenshot showed broken images in its file preview; source image paths exist locally, but that does not confirm browser rendering.
2. Complete a visual review at 1440 and 375 pixels, including every section, crops, contrast, overflow, story filtering and donation dialog behavior. Claude was interrupted during its browser check; final visual acceptance is outstanding.
3. Replace clearly labeled Gillette Children's placeholder story photos with approved MFK family stills. Do not publish the stand-ins as MFK families.
4. Resolve bracketed claims and dates against MFK sources; newsletter is design-only. Preserve existing project approval questions in the brief/README.
5. Review soft-blob buttons and organic dividers with Andres before expanding that styling.

## Handover verification

The save task checked local image-path existence and versioned the source, documentation, token files and review artifacts. It did not perform a full visual or functional acceptance review and did not publish the website.
