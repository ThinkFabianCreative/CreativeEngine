# Visual direction · LP1 (SYNTHETIC)

> **Synthetic validation fixture.** Written in DesignChamp's role for the fictional Fernwick Tool Library and approved by creative-engine-director **for validation only** (2026-09-24). It shows the two layers that sit above the global kit: the client's system (Layer 2) and this page's composition (Layer 3).

## Concept (Barry §1)

The page is a library catalog card for the tool you were about to buy: borrowing, stamped and due back.

```
CONCEPT:     catalog card for the tool you were about to buy
FIRST:       the h1, set large in the headline face against paper; nothing competes with it
FEEL:        a public library that is quietly funny about your garage
COLOR JOBS:  paper (dominant ground) · ink (text) · library green (the proof band) · stamp red (only the due-back stamp and the action)
IMAGE:       one honest photograph of lendable tools on shelves with library tags, daylight, no people posed at camera (production shoot; placeholder until then)
CODES:       library codes adopted on purpose (stamp, catalog type), DIY-retail codes avoided (orange, hazard stripes, discount bursts)
SYSTEM:      paper ground, one red per section at most, catalog face on the button and the stamp only
REAL SIZE:   h1 checked at 375 px in the approved copy's full length
RISK:        the stamp reading as a coupon; keep it quiet and typographic
```

## Layer 2 · Fernwick client system (synthetic)

In real work this lives in the client's own Figma library and is recorded in `projects/<client>/client/design-library.md`. Here it is a card on the kit's Validation page (node `18:19`).

| Element | Fernwick value |
|---|---|
| Palette (5 of the 14 Instapage Styles slots) | paper `#F3EEE3` · ink `#1E2A22` · library green `#2F5D3A` · stamp red `#C8412B` · rule `#CFC6B4` |
| Font roles | headline Fraunces SemiBold · paragraph Work Sans (forms use it) · button Courier Prime Bold, uppercase, +4% tracking |
| Button | stamp red fill, paper label, radius 2 |
| Form | Work Sans labels, white fields, 1 px ink border, radius 2; field text size as Instapage fixes it |
| Motif | the "due back" stamp: a container with a 2 px stamp-red border and Courier Prime text |
| Client components | `Fernwick / Hero / Split` · `Fernwick / Form / Card signup` · `GLOBAL · Fernwick / Footer / Legal` |

## Layer 3 · this page

| Block | Composition | Mobile |
|---|---|---|
| B01 Hero | Headline and subhead left (7 of 12 columns), photo right spanning three rows; stamp and button in their own containers under the text | Text, stamp, button, then the photo (orders 1–4): the promise before the picture |
| B02 How it works | h2 across, three steps in three columns | Stacked in reading order |
| B03 Proof | Library-green band, proof line across 9 columns | Same, full width |
| B04 Form | Why (5 columns) beside the form (7 columns) | Why, then the form |
| B05 Footer | Legal line and privacy link on ink | Same |

Per-device headline sizes (72 desktop, 40 mobile) depend on a limited-release Instapage setting: constraint CON-03, open until the workspace is inspected.

## Range test (acceptance criteria 1–7)

The kit's Validation page also holds three synthetic heroes built from the **same** primitives (`IP / Headline`, `IP / Paragraph`, `IP / Button`, `IP / Image`, Fluid Grid blocks) and the **same words**, styled only by stand-in client layers:

| Synthetic client | Register | What changed |
|---|---|---|
| A | editorial, minimal, typography-led | Instrument Serif at 104 px, one 9-column container, a text-link button, no image |
| B | dense, product-led, UI-heavy | IBM Plex Sans, dark UI ground, 5 + 7 columns with a product image, two buttons, three metric containers |
| C | expressive, image-led, high-energy | Anton uppercase at 128 px over a native container background image, pill button |

They share no face, color, radius or layout, and none of them is a CreativeEngine look. Each is built from native Fluid Grid blocks and native elements, so each would stay editable in Instapage. The fixtures are local overrides standing in for three client libraries; they are not templates.
