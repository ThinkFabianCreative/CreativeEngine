# Miracles for Kids: website rebranding and pivot

```
CLIENT:   Miracles for Kids Charity
PROJECT:  Website rebranding and pivot. "Rebranding" = Jordan's rebrand landing page (round 1, then a round 2 refinement), which got pushback. "Pivot" = CreativeEngine's new approach to it
OPENED:   2026-10-16
```

- Figma working file (where the new design lives): https://www.figma.com/design/9tYtPFq2Nek4tzaz5NOVq8/MFK-Andres
  - node 1:4 production homepage capture, node 1:3 Jordan's Webflow homepage, node 1:6 mission close-up, frames 7:2–7:5 empty 1440x800 frames
- Reference folder supplied by Andres: website-rebrand/raw/MiraclesForKids (MFK site images, logos, icons, 2026 events calendar, Gillette Children's brand guidelines as an outside reference, Adobe Stock .ait templates). Not yet copied into raw/.
- Jordan's live prototype: https://miracles-for-kids-8843ee.webflow.io/
- Jordan round 2 (Figma): https://www.figma.com/design/JHMKRTXVYdvl5p58mvRQwT/MFK-Refinement?node-id=2175-387
- Client profile: ../client/knowledge/organization-profile.md
- Reviews: work/reviews/production-homepage-audit_v01.md, work/reviews/jordan-homepage-audit_v01.md, work/reviews/jordan-homepage-audit_v02-round2.md

- Normalized brief: normalized-brief.md (DRAFT, 2026-10-16)
- Packets: packets/P1_voice-and-homepage-copy.md, packets/P2_brand-system-and-homepage-design.md

Next: creative-engine-director readiness check, then P1 copy exploration.

## Figma tokens (MFK-Andres)

- **MFK Copy**: 209 string variables, mode "T5 Everyday miracles v01". Source: work/copy/landing-copy_T5_v01.json (flat: .figma-strings.json)
- **MFK Type Primitives**: 60 raw values (families, styles, sizes, line heights, letter spacing), hidden from pickers
- **MFK Type**: 65 semantic type tokens aliasing primitives, 4 modes = looks: A Saturated (Outfit + Caveat), B Blocks (Fredoka/Nunito + Caveat Brush), C Pastel (Nunito + Dancing Script), D System (Lexend + Kalam). Source: work/design/tokens/mfk-type-tokens_v01.json
- **Text styles**: MFK/Display, Heading 1–3, Stat, Eyebrow, Body Large, Body, Caption, Button, Highlight / Display, Highlight / Heading 1, Highlight / Heading 2, all bound to MFK Type
- **MFK Color Primitives**: 53 colors (ramps 50–900 of MFK navy, sky, orange, teal, magenta from the live site and logo, plus royal, sun, lavender and neutrals), hidden from pickers
- **MFK Color**: 20 semantic roles (bg canvas/primary/secondary/accent/soft, text on-each, text primary/secondary/highlight, action, shapes 1–3, border), 4 modes matching MFK Type. Ratio rules + contrast report: work/design/tokens/mfk-color-tokens_v01.json
- **Specimens**: "MFK Type Specimen v01" (16:142), "MFK Color Specimen v01" (17:77)

## Landing page designs (MFK-Andres, desktop 1440)

| Look | Node | Fonts | Palette |
|---|---|---|---|
| A Saturated | 19:52 | Outfit + Caveat | royal blue, orange, sun |
| B Blocks | 22:355 | Fredoka/Nunito + Caveat Brush | sun, magenta, sky on cream |
| C Pastel | 22:707 | Nunito + Dancing Script | lavender, sky, magenta on cream |
| D System | 22:1059 | Lexend + Kalam | navy, sky, orange on white |

Same layout, fully bound to MFK Copy / MFK Color / MFK Type. Switching a frame's modes swaps the look. Photos: real MFK family photos (Campbell family hero, Kiara, Michelle, Miracle Manor) plus MFK-folder stock as fillers. Story video posters are empty slots (YouTube thumbnails not pulled). Mobile 375 not built yet.

## Landing page v2 batch (organic shapes + image-led), desktop 1440

| Look | Node |
|---|---|
| A Saturated | 26:6 |
| B Blocks | 28:733 |
| C Pastel | 28:1067 |
| D System | 28:1401 |

New in v2: MFK Shape components (Blob, Pebble, Swoosh, Arch, Heart, Wave Top, Wave Bottom; frame "MFK Shapes v01", 25:2) with fills bound to color tokens; hero photo cropped in a large organic blob; wave section dividers; photo-backed Truth and Close sections with a token overlay; Starlight-style story mosaic (video, photo and quote tiles with asymmetric corners; real quotes from MFK's site: Maribel, the Madrid family); program and get-involved photos cropped in organic shapes. v1 batch kept unchanged.

## Landing page v3: Color B + Type A, CD edits (node 30:94)

Built from cd-review_v2-landing_v01.md plus Material 3 Expressive tactics (Andres, 2026-10-16: "material 3 expressive with variable fonts").
- Copy: new MFK Copy mode "T5 Everyday miracles v02" (v01 untouched). Hero "Miracles look like a *normal Tuesday.*"; "miracle" cut to hero/truth/close + program names; "There's a waitlist." replaces "[6+] families are waiting".
- Script highlight only in Hero, Truth, Close; elsewhere the highlight word is color-only.
- Truth is a second hero: flat block, display type, "$500 up to, every month" burst (claim C2).
- Stories: 4 filters; child-drawing placeholder tile; video posters still placeholders (need real stills).
- Proof: sentence blocks, readable hospital chips, badges; 88¢ and 2,100+ removed.
- Events: two cards for the next events. One hero video entry point.
- New M3-Expressive-style shapes drawn for MFK: Cookie, Clover, Flower, Burst (in "MFK Shapes v01").
- Variable fonts: Outfit, Nunito, Fredoka and Lexend are all variable on Google Fonts; the web build can use custom weights for emphasized type. Figma tokens hold named styles only.

## HTML prototype (v3)

`work/prototype/index.html`: browser build of v3 (Color B + Type A, Copy v02). Design only.
- Framework: Material 3 Expressive tactics: shape variety + shape morph (play buttons, chips and buttons morph on hover/press), shaped containers, emphasized variable-font type (Outfit wght 100–900, Caveat 400–700: weight contrast 340/900 in headlines, weight shifts on hover, one load animation), spring easing, reduced-motion respected.
- Hero (Andres, 2026-10-16): full-bleed production-site photo (raw/production-site/Homepage_Desktop_EDIT_2-2.jpg, a stock family). Note: this reverses the earlier "no stock heroes" rule at Andres's request; the Campbell family photo is the real-family alternative.
- Mobile: hero stacks (photo, then navy text, then donation card). No horizontal scroll at 375 or 1440.
- Preview: the app's sandbox can't serve from Documents, so a copy is served from the session scratchpad on localhost:8430. Images live in gitignored raw/ folders, so a clone won't show them.
- Donation (Andres, 2026-10-16): the form left the hero. It's now a dismissible interstitial (`<dialog>`) that opens once after the visitor scrolls past the family stories. "Maybe later", the close button, a backdrop click or Esc minimize it to a sticky "Donate" bug, which reopens it. Remembered per browser.
- Story-first order: Hero → Family stories → Truth → Programs → Proof → Urgency → Get involved → Events → Close.
- CTAs: Donate and Volunteer only (nav, hero, close; urgency is Donate).
- Trust (Andres, 2026-10-16: "recognizable logos are key"): the 9 hospital logos from the live site (raw/production-site/logos/, gitignored) in a white logo wall inside Proof, full color. Logo use still needs each hospital's permission (Q7).
- Story tiles: William, Willow and Jeremiah use photos from raw/MiraclesForKids/more_images as labeled placeholders. Those are Gillette Children's patients from its brand guide, not MFK families: never ship or present them as MFK families.
