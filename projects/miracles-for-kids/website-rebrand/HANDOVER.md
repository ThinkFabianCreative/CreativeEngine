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

## Prototype images included

All 25 images used by the current prototype are versioned in `work/prototype/assets/` (about 5.6 MB total). The HTML references these portable copies, so no separate image transfer is needed to view the prototype on another computer.

The larger original folders `raw/MiraclesForKids/` and `raw/production-site/` remain excluded. `work/prototype/local-assets-manifest.json` lists the included assets. Gillette placeholder photos remain labeled in the prototype and still need replacement before publication.

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

1. Open the repository prototype over HTTP and verify image rendering. All referenced images are now included; the old Claude file preview showed broken images before portable copies were added.
2. Complete a visual review at 1440 and 375 pixels, including every section, crops, contrast, overflow, story filtering and donation dialog behavior. Claude was interrupted during its browser check; final visual acceptance is outstanding.
3. Replace clearly labeled Gillette Children's placeholder story photos with approved MFK family stills. Do not publish the stand-ins as MFK families.
4. Resolve bracketed claims and dates against MFK sources; newsletter is design-only. Preserve existing project approval questions in the brief/README.
5. Review soft-blob buttons and organic dividers with Andres before expanding that styling.

## Also in the repository

- `work/reviews/mobile-m3e-audit/`: mobile Material 3 Expressive molecule audit of Figma frame 39:136 (contrast repairs, hierarchy, elevation), with before/after captures.
- `work/reviews/cd-review_v2-landing_v01.md` and `work/reviews/design-review_prototype-v3_v01.md`: the Creative Director and designer reviews that drove v3.
- `.claude/launch.json` is not committed (it points at a machine-specific temporary folder). On a new computer, serve from the repository root as described above.

## Handover verification

The save task checked local image-path existence and versioned the source, documentation, token files and review artifacts. It did not perform a full visual or functional acceptance review and did not publish the website.
