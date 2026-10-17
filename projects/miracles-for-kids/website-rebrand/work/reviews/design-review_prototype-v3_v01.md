# Design review: landing prototype v3 (v01)

CLIENT: Miracles for Kids Charity · PROJECT: website-rebrand · SOURCE SCOPE: PROJECT-LEVEL
Reviewer: design-champ · Mode: DEVELOP (aesthetic pass, design only) · Date: 2026-10-16
Reviewed: `work/prototype/index.html` (source read in full; live view checked at 1440 hero). Note: in-pane scrolling did not advance at 1440 during review, so below-hero judgments are from markup/CSS plus the v2 CD review; re-check mobile 375 after implementing.
Frameworks: `visual-craft.md`, `barry-concept-art-direction.md` (who carries the idea, reading order).

## A. Critique, ranked

### Top issues
1. **Programs ("Five ways we help") has no system.** 2 big + 3 small cells, five different crop shapes (blob, arch, heart, pebble, blob again), two different image ratios (1.9:1 and 1.5:1), text stacked as 4 loose spans with no container. Nothing aligns to anything; the shapes compete instead of the miracles. Fix: section C (zipper bento).
2. **Shape vocabulary is random and includes hearts.** Hearts appear 4 times (hero `.h-heart`, `#c-heart` in programs and involve, `♥` in the bug). Blob and pebble are formless and read "AI organic". Fix: replace the whole set with the family in section B; one shape per job, repeated.
3. **Crops are square-authored (400x400 viewBox) but images are landscape.** `scale(.0025)` on a 4:3 box stretches every shape horizontally; arches become squat, the heart becomes a bean. Fix: 400x300 paths, `scale(0.0025 0.003333)`, every cropped image `aspect-ratio:4/3`.
4. **Truth band is the idea of the page but has the least design around it after the hero.** 220px padding of flat sun with centered type is right; the `$500` burst (spiky, magenta) fights the headline and is the only spiky shape on the page. Fix: swap burst for the rounded star (B4) at 200px, navy number, rotated -8°; add pattern D1 at low contrast so the band stops looking like an empty spacer.
5. **Too many flat full-bleed bands in a row** (truth sun → programs soft → proof magenta → urgency sky → involve canvas → events canvas → close sun). The color ratio from the Gillette lessons (one dominant, one support, accents rare) is broken: sun is used as a section ground three times. Fix: sun only for truth + close; programs on canvas with pattern; proof magenta; urgency becomes a navy pill-shaped band inset in canvas (not full bleed).

### Section by section
| Section | Wrong | Fix |
|---|---|---|
| Hero | Heart floats unanchored at `bottom:560px`; three CTAs + video chip in one row; script "normal Tuesday." in sun on photo is low contrast on the bright sky area. | Delete heart; put a sun **rounded asterisk** (B3) 120px, overlapping the photo's bottom-right edge into the wave. CTAs: Donate (primary) + video chip; Volunteer moves to nav only (already there). Add a navy 0→40% bottom-left scrim under the text block only. Mobile: photo 4:3 with the arch (B1) top instead of the `0 0 120px 0` corner. |
| Stories | 7 tiles, 4 different corner radii hacks (`r-tl` etc.), Prev/Next suggest a carousel that isn't one, dashed "drawing" tile looks broken. Placeholders flagged correctly. | Keep the 4-col mosaic (it is the Starlight Cool Grid move) but fix rhythm: row 1 = William wide (span 2; video tiles stay 16:9, photo tiles 4:3), quote, Michelle; row 2 = Willow, Jeremiah wide, drawing. Uniform 28px radius; the one expressive corner is a single 140px radius on the wide video tiles only. Drop Prev/Next (or make it a real scroll-snap rail on mobile only). Drawing tile: solid canvas with a sky **ticket** (B6) frame, not dashed border. |
| Truth | See top issue 4. | Rounded star badge, pattern D1, link becomes a btn-ghost on-primary "How the bills get paid". |
| Programs | See top issue 1. | Section C. |
| Proof | 4 sentence blocks with 4 asymmetric radii + white logo wall + outlined badges = three visual languages on magenta. Logo wall `box-shadow` is the only drop shadow besides the donation card. | 2 sentence blocks only (the $500 and Miracle Manor), both squircle (B5 used as CSS `border-radius:48px` equivalent), side by side above the wall. Logo wall: remove shadow, radius 32px, logos greyscale→colour on hover. Badges as filled canvas pills. Pattern D2 on the magenta ground. |
| Urgency | Full-bleed sky band right after a full-bleed magenta band; reads as a footer strip. "[waitlist]" risk stays (CD review §4). | Inset navy capsule (radius 999px desktop, 40px mobile) on canvas, 1200px max, sun Donate button. Shape change = moment change. |
| Get involved | 3 equal cards with arch, pebble, heart crops at a fixed 260px height. Heart on "Business with a heart" doubles the cliché. | Zipper-of-3 is overkill; use a **1+2 bento**: 360° Miracle tall left (arch B1), Volunteer and Partner stacked right (ticket B6 and squircle B5). Magenta stays on Volunteer only (it is a primary CTA). |
| Events | Flower and cookie crops at 160px square from landscape photos; Nov 14 card and basket card use the same volunteer photo as involve. | Ticket shape (B6) as the card itself, not the image: date in a sun stub on the left behind the notch line, 4:3 photo right in a squircle. Unique photos. |
| Close | Formless blob shape at right; sun ground again. | Replace blob with a sky rounded star (B4) partly off-canvas, plus 2 small asterisks. Keep sun (it bookends truth). Newsletter input to canvas fill, not white. |
| Footer | Fine structurally; 2fr/1fr/1fr/1fr collapses to 2 cols at 800 with the long line squeezed. | At ≤800: line + address full row, links 3 cols ≥560, 1 col below. Add a 24px scallop edge (D2 tile row) on top in navy. |
| Interstitial / bug | Bug uses a heart glyph; dialog trigger fires on leaving stories, i.e. mid-scroll on the truth band, which interrupts the best line on the page. | Bug icon = small sun rounded asterisk SVG. Trigger after programs exit (visitor has seen stories + truth + how), not stories. Dialog card radius matches family (squircle 40px), close button stays. |

## B. Crop-shape family (400x300 viewBox)

Use: `<clipPath id="c-x" clipPathUnits="objectBoundingBox"><path transform="scale(0.0025 0.003333)" d="..."/></clipPath>` and every clipped `img{aspect-ratio:4/3;object-fit:cover}`. No hearts, no blob, no pebble: delete `#c-heart`, `#c-blob`, `#c-pebble`, `#c-cookie`, and the runtime `.polar` builder for crops (keep it only for decorative SVG if wanted).

**B1 Round arch** (Get involved lead, hero mobile, programs big cell)
`M0 276 V200 A200 200 0 0 1 400 200 V276 Q400 300 376 300 H24 Q0 300 0 276 Z`

**B2 Rounded flower, 6 soft lobes** (Events stub accent, stories drawing tile accent; image crop where a joyful kid photo needs a playful frame, max one per viewport)
`M200.0 0.0 L210.4 1.0 L220.5 3.9 L229.9 8.4 L238.5 14.1 L246.2 20.6 L253.1 27.3 L259.5 33.8 L265.6 39.5 L271.8 44.3 L278.6 47.9 L286.2 50.5 L294.8 52.2 L304.5 53.3 L315.1 54.2 L326.3 55.3 L337.6 57.1 L348.6 59.8 L358.5 63.6 L366.9 68.7 L373.2 75.0 L377.3 82.3 L379.0 90.2 L378.5 98.6 L376.1 107.1 L372.5 115.3 L368.2 123.2 L363.9 130.5 L360.4 137.4 L358.0 143.8 L357.1 150.0 L358.0 156.2 L360.4 162.6 L363.9 169.5 L368.2 176.8 L372.5 184.7 L376.1 192.9 L378.5 201.4 L379.0 209.8 L377.3 217.7 L373.2 225.0 L366.9 231.3 L358.5 236.4 L348.6 240.2 L337.6 242.9 L326.3 244.7 L315.1 245.8 L304.5 246.7 L294.8 247.8 L286.2 249.5 L278.6 252.1 L271.8 255.7 L265.6 260.5 L259.5 266.2 L253.1 272.7 L246.2 279.4 L238.5 285.9 L229.9 291.6 L220.5 296.1 L210.4 299.0 L200.0 300.0 L189.6 299.0 L179.5 296.1 L170.1 291.6 L161.5 285.9 L153.8 279.4 L146.9 272.7 L140.5 266.2 L134.4 260.5 L128.2 255.7 L121.4 252.1 L113.8 249.5 L105.2 247.8 L95.5 246.7 L84.9 245.8 L73.7 244.7 L62.4 242.9 L51.4 240.2 L41.5 236.4 L33.1 231.3 L26.8 225.0 L22.7 217.7 L21.0 209.8 L21.5 201.4 L23.9 192.9 L27.5 184.7 L31.8 176.8 L36.1 169.5 L39.6 162.6 L42.0 156.2 L42.9 150.0 L42.0 143.8 L39.6 137.4 L36.1 130.5 L31.8 123.2 L27.5 115.3 L23.9 107.1 L21.5 98.6 L21.0 90.2 L22.7 82.3 L26.8 75.0 L33.1 68.7 L41.5 63.6 L51.4 59.8 L62.4 57.1 L73.7 55.3 L84.9 54.2 L95.5 53.3 L105.2 52.2 L113.8 50.5 L121.4 47.9 L128.2 44.3 L134.4 39.5 L140.5 33.8 L146.9 27.3 L153.8 20.6 L161.5 14.1 L170.1 8.4 L179.5 3.9 L189.6 1.0 Z`

**B3 Rounded asterisk, 8 soft lobes** (decor: hero badge, bug icon, close confetti; as crop only for one programs small cell)
`M200.0 0.0 L210.3 2.4 L219.8 9.0 L227.7 18.9 L233.9 30.3 L238.8 41.3 L243.2 50.4 L248.0 56.1 L254.5 58.1 L263.4 56.6 L275.0 52.6 L288.9 47.4 L304.0 42.6 L318.9 39.9 L331.9 40.1 L341.4 43.9 L346.5 51.1 L346.9 60.8 L343.2 72.0 L336.9 83.3 L329.9 93.8 L324.5 102.4 L322.5 109.1 L325.2 114.0 L332.9 117.6 L344.9 120.9 L359.6 124.6 L374.8 129.2 L387.9 135.2 L396.8 142.3 L400.0 150.0 L396.8 157.7 L387.9 164.8 L374.8 170.8 L359.6 175.4 L344.9 179.1 L332.9 182.4 L325.2 186.0 L322.5 190.9 L324.5 197.6 L329.9 206.2 L336.9 216.7 L343.2 228.0 L346.9 239.2 L346.5 248.9 L341.4 256.1 L331.9 259.9 L318.9 260.1 L304.0 257.4 L288.9 252.6 L275.0 247.4 L263.4 243.4 L254.5 241.9 L248.0 243.9 L243.2 249.6 L238.8 258.7 L233.9 269.7 L227.7 281.1 L219.8 291.0 L210.3 297.6 L200.0 300.0 L189.7 297.6 L180.2 291.0 L172.3 281.1 L166.1 269.7 L161.2 258.7 L156.8 249.6 L152.0 243.9 L145.5 241.9 L136.6 243.4 L125.0 247.4 L111.1 252.6 L96.0 257.4 L81.1 260.1 L68.1 259.9 L58.6 256.1 L53.5 248.9 L53.1 239.2 L56.8 228.0 L63.1 216.7 L70.1 206.3 L75.5 197.6 L77.5 190.9 L74.8 186.0 L67.1 182.4 L55.1 179.1 L40.4 175.4 L25.2 170.8 L12.1 164.8 L3.2 157.7 L0.0 150.0 L3.2 142.3 L12.1 135.2 L25.2 129.2 L40.4 124.6 L55.1 120.9 L67.1 117.6 L74.8 114.0 L77.5 109.1 L75.5 102.4 L70.1 93.7 L63.1 83.3 L56.8 72.0 L53.1 60.8 L53.5 51.1 L58.6 43.9 L68.1 40.1 L81.1 39.9 L96.0 42.6 L111.1 47.4 L125.0 52.6 L136.6 56.6 L145.5 58.1 L152.0 56.1 L156.8 50.4 L161.2 41.3 L166.1 30.3 L172.3 18.9 L180.2 9.0 L189.7 2.4 Z`

**B4 Rounded star, 5 soft points** (truth $500 badge, close decor, Boost program crop). Point-up; the star is drawn ~1:1 inside the 4:3 box, so set `object-position:center 30%` on faces.
`M200.0 0.0 L208.3 1.3 L216.2 5.2 L223.4 11.3 L229.6 19.3 L234.7 28.6 L238.6 38.5 L241.5 48.5 L243.7 57.9 L245.5 66.3 L247.3 73.1 L249.7 78.3 L252.9 81.7 L257.4 83.6 L263.4 84.0 L270.9 83.5 L279.9 82.6 L290.1 81.6 L301.1 81.1 L312.4 81.5 L323.4 83.2 L333.4 86.3 L341.9 90.8 L348.3 96.6 L352.2 103.6 L353.4 111.5 L351.9 119.7 L347.9 128.0 L341.7 136.0 L333.9 143.4 L325.0 150.0 L315.8 155.7 L306.9 160.5 L299.0 164.7 L292.6 168.5 L288.1 172.1 L285.6 176.1 L285.1 180.6 L286.5 186.1 L289.3 192.7 L293.1 200.4 L297.2 209.2 L301.1 218.9 L304.2 229.1 L305.9 239.4 L305.9 249.3 L303.9 258.2 L299.9 265.7 L294.0 271.4 L286.5 274.9 L277.7 276.1 L268.0 275.1 L258.0 272.0 L248.0 267.3 L238.6 261.5 L230.0 255.0 L222.4 248.6 L215.7 242.8 L209.9 238.3 L204.8 235.4 L200.0 234.4 L195.2 235.4 L190.1 238.3 L184.3 242.8 L177.6 248.6 L170.0 255.0 L161.4 261.5 L152.0 267.3 L142.0 272.0 L132.0 275.1 L122.3 276.1 L113.5 274.9 L106.0 271.4 L100.1 265.7 L96.1 258.2 L94.1 249.3 L94.1 239.4 L95.8 229.1 L98.9 218.9 L102.8 209.2 L106.9 200.4 L110.7 192.7 L113.5 186.1 L114.9 180.6 L114.4 176.1 L111.9 172.1 L107.4 168.5 L101.0 164.7 L93.1 160.5 L84.2 155.7 L75.0 150.0 L66.1 143.4 L58.3 136.0 L52.1 128.0 L48.1 119.7 L46.6 111.5 L47.8 103.6 L51.7 96.6 L58.1 90.8 L66.6 86.3 L76.6 83.2 L87.6 81.5 L98.9 81.1 L109.9 81.6 L120.1 82.6 L129.1 83.5 L136.6 84.0 L142.6 83.6 L147.1 81.7 L150.3 78.3 L152.7 73.1 L154.5 66.3 L156.3 57.9 L158.5 48.5 L161.4 38.5 L165.3 28.6 L170.4 19.3 L176.6 11.3 L183.8 5.2 L191.7 1.3 Z`

**B5 Squircle** (default crop: programs small cells, proof blocks, events photo, dialog)
`M200 0 C360 0 400 30 400 150 C400 270 360 300 200 300 C40 300 0 270 0 150 C0 30 40 0 200 0 Z`

**B6 Ticket / tab** (events card, stories drawing frame, Volunteer card)
`M24 0 H376 Q400 0 400 24 V126 A24 24 0 0 0 400 174 V276 Q400 300 376 300 H24 Q0 300 0 276 V174 A24 24 0 0 0 0 126 V24 Q0 0 24 0 Z`

**B7 Capsule / stadium** (urgency band, hero video still on mobile; tilt via the wrapper, `transform:rotate(-4deg)`, never the clip)
`M150 0 H250 A150 150 0 0 1 250 300 H150 A150 150 0 0 1 150 0 Z`

Rule: per section, one crop shape for images, one optional decor shape. Shape morph (M3 Expressive) on hover = squircle → arch only (same point count is not needed if you morph with CSS `border-radius` on non-clipped cards instead).

## C. "Five ways we help"

| Option | Desktop | Mobile | Verdict |
|---|---|---|---|
| Bento | Strong hierarchy; 5 fits a 3x2 with one 2-cell lead; reads as a set | Collapses to stack, fine | Good but static, and the Lifeline lead risks making the other four look minor |
| Carousel | Hides 3 of 5 programs; donors don't swipe to learn what you do | Natural | Kill for this job; programs are the proof of "how", they must all be visible |
| Zipper (alternating 2-col rows) | Clear, but 5 full rows = ~4 screens; repeats the stories rhythm badly | Same stack as bento | Too long |

**Pick: bento with a zipper accent.** Lifeline gets the lead cell because it is the truth band's proof ($500, bills): reading order goes truth → "here's how" without a jump. The other four sit as a 2x2 that zips (image left/right alternates) so it doesn't read as a template card grid.

Desktop (≥1100):
```css
.pgrid{display:grid;grid-template-columns:repeat(12,1fr);grid-template-rows:auto auto;gap:24px}
.prog{display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:center;padding:20px;border-radius:32px;background:var(--white)}
.prog.lead{grid-column:1/6;grid-row:1/3;grid-template-columns:1fr;align-content:start;background:var(--bg-primary);color:var(--on-primary);padding:28px}
.prog:nth-child(2){grid-column:6/13} .prog:nth-child(3){grid-column:6/13}   /* row 1 and 2, right */
.prog:nth-child(4),.prog:nth-child(5){grid-column:span 6}                   /* row 3, full width pair */
.prog:nth-child(3) .crop,.prog:nth-child(5) .crop{order:2}                    /* zipper */
.prog .crop{width:100%;aspect-ratio:4/3;object-fit:cover}
```
Layout result: Lifeline tall left (5 cols, rows 1–2), Safe Haven and Balance right (7 cols each, image left then right), Boost + Pillars as a pair on row 3 (6+6, Pillars image right).

Shapes and color:
| Program | Crop | Card ground | Kicker color |
|---|---|---|---|
| Lifeline (lead) | B1 arch, 4:3, image top, text below | `--bg-primary` sun #FFD23F, navy text | magenta |
| Safe Haven | B1 arch (it is a house) | white | magenta |
| Balance | B5 squircle | white | magenta |
| Boost | B4 star | white | magenta |
| Pillars | B5 squircle | `--bg-accent` sky #79BDE9, navy text | navy |

Text in each card: kicker (14px/600 caps, 1.5px), name as h3 ("The lights-on miracle", Outfit 750), one line, then the stat as **20px/700 navy on a #E9F8FA pill** (fixes "stat lines too small"). Whole card is the link; arrow chip bottom-right. Section ground: canvas #FBF6EE with pattern D3.

Mobile (≤700): single column, all cards image-top 4:3, lead first, no zipper; 16px gutter, 16px gap. 701–1099: lead full width (image left / text right), others 2x2.

## D. Pattern backgrounds

Use as `background-image:url("data:image/svg+xml,...")` over the section color. All tiles are tone-on-tone (≤6% luminance shift), so existing text contrast is unchanged; never put pattern behind body copy narrower than 400px without a solid card.

**D1 Asterisk confetti** on the truth band (sun):
```svg
<svg xmlns="http://www.w3.org/2000/svg" width="160" height="160" viewBox="0 0 160 160"><g fill="#F5C52C"><path d="M40 28c3 0 4 6 4 8s5-3 7-1-3 6-3 8 6 2 6 5-6 3-8 3 3 5 1 7-6-3-7-3-1 6-4 6-4-6-4-6-5 4-7 2 2-6 2-7-6-1-6-4 6-3 8-3-4-6-2-8 6 1 7 1 1-8 4-8z"/><circle cx="118" cy="44" r="5"/><circle cx="92" cy="120" r="7"/><path transform="translate(80 70) rotate(20)" d="M40 28c3 0 4 6 4 8s5-3 7-1-3 6-3 8 6 2 6 5-6 3-8 3 3 5 1 7-6-3-7-3-1 6-4 6-4-6-4-6-5 4-7 2 2-6 2-7-6-1-6-4 6-3 8-3-4-6-2-8 6 1 7 1 1-8 4-8z" opacity=".7"/></g></svg>
```
**D2 Scallops** on proof (magenta), also as the footer top edge in navy:
```svg
<svg xmlns="http://www.w3.org/2000/svg" width="48" height="24" viewBox="0 0 48 24"><path d="M0 24a24 24 0 0 1 48 0" fill="none" stroke="#B42B6C" stroke-width="3"/></svg>
```
**D3 Soft dots + wave** on programs (canvas):
```svg
<svg xmlns="http://www.w3.org/2000/svg" width="120" height="60" viewBox="0 0 120 60"><path d="M0 40c20-12 40-12 60 0s40 12 60 0" fill="none" stroke="#F1E8D8" stroke-width="3" stroke-linecap="round"/><circle cx="30" cy="14" r="3" fill="#F1E8D8"/><circle cx="90" cy="14" r="3" fill="#E9F8FA"/></svg>
```
Colors are tints of the tokens (#F5C52C = sun −6%, #B42B6C = magenta +5%, #F1E8D8 = canvas −4%). Add them as tokens: `--pat-sun`, `--pat-magenta`, `--pat-canvas`. Respect `prefers-reduced-motion`: patterns are static; no parallax.

## E. Other layout moves

1. **Get involved as 1+2 bento** (above). Clear win: puts one ask first instead of three equals.
2. **Urgency as an inset capsule**, not a band (above). Breaks the band-stack monotony at the right moment.
3. **No zipper for stories.** Stories must stay a grid (Starlight Cool Grid, Andres's reference); a zipper turns faces into a list.
4. **Merge events into close?** No: keep, but cap at 2 ticket cards; it is a volunteer route.
5. **One expressive type moment per section.** Script (Caveat) only in hero, truth, close; everywhere else Outfit weight contrast (300 lite / 800 heavy) carries emphasis.

## Implementation checklist
- [ ] Replace clipPath defs with B1–B7 (400x300, `scale(0.0025 0.003333)`); delete heart/blob/pebble/cookie.
- [ ] All clipped images `aspect-ratio:4/3`.
- [ ] Remove all hearts (hero SVG, involve crop, bug glyph).
- [ ] Programs → section C grid.
- [ ] Patterns D1 truth, D2 proof + footer edge, D3 programs.
- [ ] Urgency inset capsule; involve 1+2 bento; events ticket cards; close star.
- [ ] Dialog trigger after programs.
- [ ] Re-check 375 and 1440, every section; AA on all text over patterns.
