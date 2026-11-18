# MFK reference-based refinement and gap register

Date: October 18, 2026. Target: work/prototype/adobe-type.html?pair=anago. Shared refinements also apply to index.html. Scope: local prototype. No live deployment or Figma design changes in this pass.

## Method and evidence

Used the installed Taste Skill for a preserve-and-refine review. Read actual DESIGN.md documents from VoltAgent/awesome-design-md, pinned to revision 3b605329240ce735b510037cca322f1831fdd7f8. These are independent website analyses, not official brand systems. Compare design relationships and component behavior rather than copying colors, fonts or page structure.

MFK governing choices: retain all five program hues, neutral reading text, Anago/Playpen proposal, Feather icons, friendly crop shapes and existing destinations. The project-root DESIGN.md records the adopted system rules.

Fresh before/after browser evidence captured on the Anago variant at 1280 × 720 and 390 × 844. Dimensions below are one observed state at those viewports, not user research, conversion evidence or accessibility certification.

## Reference decisions

| Repository document | Adopted principle | Rejected for MFK |
|---|---|---|
| Airbnb | Four-pixel spacing relationships; modest elevation; legible controls; mobile navigation preserves access | Marketplace density, Cereal typography, brand coral, property/search layouts |
| Figma | Neutral reading across expressive surfaces; purposeful radius roles; one clear primary-action treatment | Its fonts, color palette, product screenshots, pricing architecture |
| Mastercard | Deliberate rounded geometry and a coherent spacing scale | Extreme editorial empty space, orbit decorations, brand/proprietary fonts |

These comparisons supplement the actual MFK brief. None establishes that one layout will increase giving.

## Findings and dispositions

| Priority | Gap and before evidence | Reference relationship | Refinement | State |
|---|---|---|---|---|
| P0 | Mobile logo measured0px wide at 390px. Flex navigation compressed the image out of view | Airbnb responsive navigation preserves entry points | Reserve 99px for phone logo, 112px desktop. Add native Menu disclosure for existing links | Fixed, measured99px |
| P0 | Fixed prototype stamp covered navigation; comparison toolbar obscured hero; floating Donate duplicated the primary action | Figma clear primary-action hierarchy | Review controls moved to collapsed Preview settings in document flow. Remove automatic donation interruption and floating duplicate | Fixed |
| P1 | Desktop hero940px high; first hero CTA began at824px in a720px viewport | Figma/Mastercard hierarchy and intentional composition | Separate neutral text from the family photograph. Reduce hero to about 549px; CTA now begins around 501px | Fixed in observed desktop state |
| P1 | Mobile programs consumed 2931px with image-heavy stacked cards | Airbnb relationship between section and card density | Consistent 88px thumbnails with compact adjacent body hierarchy and retained program tints | Fixed, about 1254px |
| P1 | Filter chips changed pressed state without filtering stories | Consistent control state and result relationship | Client-side format/update filtering. Read shows Michelle only; All restores 4 story links | Fixed and exercised |
| P1 | Handwritten line and mixed display weights lacked a restrained hierarchy; body measures varied | Airbnb restrained type, Figma distinct type roles | Hero 40–60px desktop and 34–40px phone; handwritten line at1.16 line-height. Lead 19px desktop / 17px mobile | Applied, visually checked; not a readability study |
| P1 | Program hover changed radius and heading weight, shifting labels and geometry | Stable component roles in repository analyses | Shared 24px card radius, 700 button/card weight, small transform feedback | Fixed |
| P1 | Section padding ranged from 24px to 220px; large closing/bills sections added empty scrolling | Shared spacing relationships across all 3 references |4px-based scale. Major sections 80px desktop / 48px mobile with explicit divider exceptions | Fixed |
| P1 | Mobile family stories stacked vertically and mixed a quote into the sequence | Photo-first browsing and clear content hierarchy | Native horizontal story rail. Move existing quotation outside it. Preserve visible placeholder disclosures | Applied; touch/keyboard testing beyond observed filtering remains |
| P1 | Feather Play inherited dark stroke on magenta, which did not give sufficient non-text contrast | Contrast check rather than copying reference appearance | Reversed white stroke on magenta; retain24px/2px library geometry | Fixed |
| P2 | Multiple shape/radius conventions had no role documentation | Figma/Mastercard radius roles | Document16px utility,24px card and pill actions. Keep meaningful existing photo masks | Documented and applied |
| P2 | No project-specific design contract connected the references to implementation | Repository DESIGN.md approach | Add project-root DESIGN.md with source links, roles, tokens, layout and guardrails | Complete |

## Observed measurements

| Check | Before | After |
|---|---:|---:|
| Phone logo width |0px|99px|
| Desktop hero height |940px|about 549px|
| Desktop hero CTA top |824px|about 501px|
| Phone programs height |2931px|about 1254px|
| Phone total page height |13636px|about 8027px|
| Desktop total page height |8037px|about 6920px|

Page-height reductions reflect layout changes at the measured viewport. They do not measure task success or user preference. All copy, program routes and image sources remain available except removing duplicate/interruptive prototype UI. The child-drawing placeholder stays in desktop review and is omitted from the compact mobile rail.

## Remaining gaps

1. Content readiness: borrowed family photographs and bracketed claims remain internal-review placeholders. Obtain consented MFK images and validate every metric before release.
2. Newsletter: remains design-only, with no backend or success/error journey. This pass does not imply subscription handling.
3. Donation: links route to the existing MFK destination. No checkout or conversion evaluation occurred.
4. Accessibility: keyboard focus, zoom/reflow, screen-reader behavior and all interactive states need a broader test. Earlier 89-node/5.55:1 result applies only to the older Figma mobile frame 39:136.
5. Logo: restored display space does not resolve the signature's small-scale optical complexity. Obtain approved vector art and test an approved small-use lockup separately.
6. Architecture: styles are layered on a prototype. Consolidating legacy rules, bundling dependencies and production font delivery remain implementation work.
7. Source references are third-party analyses, some marked alpha. Their measurements are not accessibility guidance. Do not inherit weak contrast pairs or unsupported compliance claims from them.

## Sources

- https://github.com/VoltAgent/awesome-design-md/blob/3b605329240ce735b510037cca322f1831fdd7f8/design-md/airbnb/DESIGN.md
- https://github.com/VoltAgent/awesome-design-md/blob/3b605329240ce735b510037cca322f1831fdd7f8/design-md/figma/DESIGN.md
- https://github.com/VoltAgent/awesome-design-md/blob/3b605329240ce735b510037cca322f1831fdd7f8/design-md/mastercard/DESIGN.md
- Internal constraints: normalized-brief.md, latest user instructions, project discovery-2026-10-18/DISCOVERY.md
- WCAG: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html and https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html

## Screenshots

01-before-desktop.jpg /02-before-mobile.jpg /03-after-desktop.jpg /04-after-mobile.jpg. Additional verified menu/program screenshots may accompany these.

Final measurements use document-top coordinates at scrollY=0. At390px the hero actions end around593px, including the36px review disclosure above navigation. Tablet768px also showed no horizontal page overflow.

## User-directed correction: expressive surface contrast

The first reference pass over-muted the surfaces. At the user's request, saturated program fills and stronger section blocks have been restored. Neutral text does not require pastel backgrounds: charcoal on green/teal/orange/sky and white on magenta retain strong text contrast. The bills section and quote use yellow; trust uses magenta with a white logo panel; closing uses sky. Selected filters use magenta against blue options. Keep the repaired layout and control behavior. Screenshot05-expressive-surfaces.jpg records the corrected direction. Earlier pastel screenshots remain historical evidence of the first pass, not the final color direction.
