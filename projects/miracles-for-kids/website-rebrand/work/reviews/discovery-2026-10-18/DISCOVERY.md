# MFK live discovery and proposed evolution

Observed October 18, 2026 in the in-app browser. Sources: https://miraclesforkids.org/ and https://miraclesforkids.org/how-we-help-2/.

## Live style inventory

- Body: Open Sans, 16px, weight 300. Sampled headings: 32 or 42px, weight 300. Accent face: jennasue (Jenna Sue).
- Program headings: 19px, colored script name and black category. Buttons sampled on homepage: 24px radius, 16px/700. Compact action buttons also use 12px type.
- Current program hues: Lifeline #31B744; Safe Haven #A92061; Balance #27BBC9; Boost #F99400; Pillars #79BDE9.
- Navy #002855 footer; white main surfaces; grey #B1B0B0 footer text. This is an observed inventory, not a published brand token spec.
- Logo in desktop navigation: approximately99x60CSSpx. Source logo_mfks.png has natural dimensions240x146px. Qualitative visual assessment: thin script, overlapping forms and small vertical FOR become delicate as size reduces. No user recognition study has been performed.

## Palette recommendation

Retain all five program hues, including Boost orange. Magenta already exists for Safe Haven and Ways to Give. Keep navy for structural surfaces. Introduce #FFD23F yellow only as a supporting accent, with #FFF4D0 as a light optional surface. White/light surfaces do most of the work. Program tints: #EAF7EC, #F8E9F0, #E8F7F9, #FFF0DB and #EBF5FC.

Text: #242424 primary, #595959 secondary on tested light surfaces, white for reversal. Names and categories remain visible alongside program color. Greyscale is a design preference, not a WCAG requirement.

## Contrast calculations

WCAG relative-luminance formula on the observed solid color pairs, rounded to two decimals:

| Background | White text | Charcoal #242424 |
|---|---:|---:|
| Green #31B744 |2.63:1|5.90:1|
| Magenta #A92061 |6.85:1|2.27:1|
| Teal #27BBC9 |2.32:1|6.68:1|
| Orange #F99400 |2.27:1|6.85:1|
| Sky #79BDE9 |2.05:1|7.59:1|
| Yellow #FFD23F |1.44:1|10.75:1|

Normal text threshold4.5:1; large text3:1. Source: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html. Color must not act as the only signal: https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html. This is not a full accessibility audit. Prior89node/5.55minimum result belongs only to Figma frame39:136.

## React Feather implementation

index.html and adobe-type.html share icons-react.js and brand-evolution.css. Uses actual react-feather2.0.10 React components with React18.3.1 through a pinned import map. Native24px grid, strokeWidth2, round caps/joins, currentColor. Decorative icons have aria-hidden and retain visible text labels.

Program mapping: CreditCard/Lifeline, Home/Safe Haven, Sun/Balance, ShoppingBag/Boost, TrendingUp/Pillars. Shared actions: Gift, Users, Play, ArrowUpRight, Video, BookOpen, Clock, Mail, Send and X.

Verified26/26icons rendered, all program text/linescharcoal, no horizontal overflow at390px or desktop, no browser console errors observed. External font/icon delivery requires network access. Screenshot03records the narrow program layout. No production deployment occurred.

## Evidence

01-current-homepage.jpg and02-current-programs.jpg are fresh browser captures accepted after visual inspection.03-mobile-feather-programs.jpg shows the updated local program card at390px. Figma page52:3232 contains24editable presentation frames, with the current screenshots embedded and clearly marked before/after studies. Official logo art and before screenshots retain original colors. No logo redraw has been approved.
