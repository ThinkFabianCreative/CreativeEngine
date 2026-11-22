# Homepage build note, DEVELOP r1 (v01)

CLIENT: Traffik · PROJECT: website-d2c · SOURCE SCOPE: PROJECT-LEVEL · design-champ, 2026-11-18
Figma file eLfndwoXdZ0nURgxN8VIhn, page "Page 12" (670:5146). Frames sit at y=7615, 400 px below the board (673:343). Existing frames 670:5147 and 673:343 were not touched.

## Frames
| Frame | ID | Position |
|---|---|---|
| Home · Route 1 · The rule, first · 1440 · v1 | 679:431 | x 1840, h 7025 |
| Route 1 MOTION NOTEs (rule→idea, count-up, case Flip, doc stack) | 679:597–679:600 | x 3320 |
| Route 1 3D POSTER (document stack) | inside 679:431, section "Case stack · 3D POSTER (optional)" | |
| Home · Route 2 · Work first · 1440 · v1 | 680:431 | x 3880, h 8111 |
| Route 2 MOTION NOTEs (hero Flip, count-up, PIH rule→idea) | 680:603–680:605 | x 5360 |
| Route 1 · 390 · first screen | 680:606 | x 5880 |
| Route 2 · 390 · first screen | 680:623 | x 6370 |

Tokens: variable collection "Traffik · site tokens" (VariableCollectionId:677:431, 10 color roles, all fills bound). Text styles "Traffik/Display, H1, H2, H3, Body, Small, Label, Figure".

## Copy
WordSmither deck `2026-11-18_homepage-copy_route1-route2_v01.md` used word for word (main lines, no alts). Primary CTA "Start a project" also in the nav.

## Director fixes applied
- Route 1: the PIH shipped work (904×600) outsizes the rule panel (392 wide) on the first screen; the motion note scales it up further by the end of the first scroll.
- Route 2: plain who-we-are line above the full-bleed image; PIH sits lower as rule > idea > result; no stop/go devices.
- One red per page (R1 sign-off, R2 "Some rules are real."). Yellow only on figures. Caslon has one job per page (R1 rule; R2 hero line).

## Placeholders
- Every image is a labelled grey box (PIH shipped work, CMU Featherstone, the 6 case visuals). Logo is a labelled box.
- Caslon is Libre Caslon Display, layers named "STAND-IN: Adobe Caslon Pro". Acumin Pro is live.
- All figures carry "unv" and "Source: [source] · Year: [year]". PIH seminar attendance stays "[number needed]".

## Open items
1. Sources and years for 77%, 9.4% and 45,000+; the benchmark for PIH's 77%.
2. Featherstone cleared as the Route 2 hero; PIH rule wording (A8) approved for showing at category level.
3. 3D POSTER is built for Route 1 only; Route 2 has no stack (optional by direction).
4. Mobile: only first screens. The rule panel at 390 is small (Small style); check legibility with real Caslon.
5. Cream paper (#F1EBDD) is a site-direction panel, not a brand color; confirm along with Q10 (white).
6. No case components yet: the case cards are repeated frames, not a CMS "Tier" component.

---

# v02 · DEVELOP r2 · Combined on Route 2's skeleton (design-champ, 2026-11-18)

Andres decision 2026-11-18: combine both routes on Route 2's skeleton. v1 frames (679:431, 680:431, 680:606, 680:623), 670:5147 and board 673:343 untouched; v2 frames are duplicates of 680:431 / 680:623.

## Frames
| Frame | ID | Position |
|---|---|---|
| Home · Combined · Route 2 base · 1440 · v2 | 686:431 | x 7160, y 7615, h 9604 |
| MOTION NOTE · Rule → work (PIH section) | 687:475 | x 8680, beside the PIH section |
| Home · Combined · Route 2 base · 390 · v2 | 686:603 | x 9120, y 7615 |
| Hero line panel (over image) | 687:431 | inside 686:431 |
| Rule → work · scroll sequence (State A, State B, 3D POSTER) | 687:438 | inside PIH section 686:520 |
| How we work · new Step 4 (from Route 1) | 687:456 | inside 686:555 |
| CTA section · VARIANT B (Route 1 line) | 687:460 | after VARIANT A (686:577) |

## What changed
- Hero: image cut to 1440×796 so the first screen is 900 px with nav. Who line sits on the image top-left; the Caslon hero line (72 px) and both CTAs sit on a dark panel over the bottom of the image; Featherstone caption is a small card above it on the right. At 1440×900: who line, hero line, See the work, Start a project all visible.
- 390: "Start a project" added beside "See the work" in the first screen (both inside 844).
- Cases: each tile has two text levels, the habit (16 px, text-muted) over the work's move (Bold, 30–48 px). Lead case unchanged in size; the 2×2 grid became asymmetric (784/472, then 472/784) with different image heights.
- PIH section is the authored moment: State A (rule fills the screen on the paper panel, work enters as a sliver) → State B (rule shrinks to 392, IDEA line appears, the shipped work fills the rest), plus the 3D document stack as this section's optional 3D, as a poster frame. The rule / idea / result grid stays below as the reduced-motion frame and indexable copy. Route 1's separate stack section is not carried over.
- How we work: Route 1's "Take it through review with you. We sit with your legal and compliance team…" added as step 4 of 5.
- Closing CTA: A/B labelled. A = "What hasn't your category said yet?", B = "Got a rule you think kills the idea?" (Route 1 copy).
- Footer: "SIGN-OFF · pending decision" label + "Ideas that survive review." placeholder line.
- Kept: one red (kicker "Some rules are real."), one Caslon job (hero line), yellow only on figures with "unv", Featherstone as a labelled placeholder "clearance pending". Copy verbatim from the v01 deck; motion-state labels are design annotations, not page copy. No new connective page copy was written, so nothing is in [brackets].

## Open items
1. Featherstone clearance and the 9.4% source (hero depends on it; WellCare is the fallback).
2. How-we-work step 3 (R2 "We work it through with your team") and step 4 (R1 "We sit with your legal…") overlap. WordSmither to merge or cut one; 5 columns are narrow (237 px).
3. State labels repeat the rule text in A, B and the static grid; on the live page only one state shows at a time. Confirm the static grid stays as the reduced-motion version.
4. Hero buttons on the panel are both white; primary vs secondary weight not distinct (carried from v1). Fix with the button component next round.
5. Proof row and the services divisions are still three equal columns; they are no longer adjacent, but services could take the asymmetric treatment next.
6. Mobile: only the first screen; the PIH sequence at 390 is not designed.
7. Rule panels bound to color/paper and color/text-on-paper; Caslon remains the Libre Caslon Display stand-in; all figures still unv.
8. Sixth best-practice move from the deck slide 12 ("content relevancy") not yet checked by name on the render.
