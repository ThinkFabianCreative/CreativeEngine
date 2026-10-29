# DesignChamp UI/UX pass: landing prototype v4

CLIENT: Miracles for Kids
PROJECT: website-rebrand
MODE: DEVELOP review (Interaction design lead, Marketing design support)
DATE: 2026-10-29
TARGET: projects/miracles-for-kids/website-rebrand/work/prototype/v4/index.html (+ assets/), served at http://localhost:8430/work/prototype/v4/index.html
METHOD: I read the code in full and checked it live at 1440x900 and 375x812, with the viewport reset afterwards. Contrast figures are calculated from the hex tokens. Figma fidelity was checked against the frame positions recorded in the code comments and against live layout. I did not pull new Figma screenshots in this pass, so treat the fidelity notes as provisional until someone compares 154:936 and 154:625 side by side.
SCOPE: Judged against the decisions already made (Look A Saturated, M3 Expressive components, asymmetric tile corners and duotone shapes kept). This review does not reopen any of them.

## What is working

- The page has personality without losing order. The asymmetric 140px corners on the story tiles and the duotone shape fields (sun on sun-100, orange on sky-50, peach on orange) are the most ownable thing on the page. The mosaic reads as a family album, not as a card grid. Keep them exactly as they are.
- The order is right: stories come straight after the truth band, hospitals are grouped as proof, and Donate and Volunteer each have a clear home.
- The donation pop-out is now properly condensed. The frequency switch has a spring thumb, the amount group is connected with full outer ends and a selected pill that grows, and the button label updates live ("Give $50 monthly" / "today"). This is correct M3E behavior and feels good in the hand.
- Reduced motion is respected globally: transitions are killed, reveals are shown, and parallax and count-up are gated.
- Hidden 48px hit areas (::after) on the close button, the switch and the amounts are the right technique for a compact visual size.
- Family photography inside the organic crops (oval, arch, heart, pebble, scallop) carries trust and warmth together.

## P1: must fix

1. **Donation pop-out: white label on orange primary button fails contrast.** Section: pop-out. Viewport: both. Observed: `.give .btn{color:#fff}` sets white text on #F99400, about 2.3:1. Everywhere else orange buttons use navy text, which is the agreed rule. Why it matters: this is the single most important button on the page, and it fails WCAG AA at 15px. It also breaks the Look A rule that orange always takes navy. Fix: remove the `color:#fff` override so the label uses `--navy` (about 7:1).

2. **Focus ring disappears on dark surfaces.** Sections: truth band, pop-out (royal), close band, footer (navy). Viewport: both. Observed: the global `:focus-visible` is a 3px navy outline, which is invisible on #242424, royal and navy. Keyboard users lose their place on the video chip, "How we help", every pop-out control, Sign up and every footer link. Fix: add `.truth, .close, footer, .give { --focus: var(--sun) }` and use `outline-color: var(--focus, var(--navy))`. Sun on navy and on royal both pass 3:1 for non-text contrast.

3. **The mobile menu stays in the tab order while closed.** Section: nav. Viewport: 375. Observed: below 980px, `.nav-links` is hidden only with opacity:0 and pointer-events:none. Its six links remain focusable and announced while invisible. There is also no Esc close, and focus does not move into the panel. Why it matters: keyboard and screen-reader users tab through invisible links before they reach the hero. Fix: add `visibility:hidden` to the closed state (with a delayed visibility transition, as `.give` already does), set it visible on `.nav.open`, close on Esc and return focus to the menu button. Also toggle the button's aria-label between "Open menu" and "Close menu".

4. **The pop-out's dialog semantics don't match its behavior.** Section: pop-out. Viewport: both. Observed: the form carries `role="dialog"`, but it is non-modal, opens itself on scroll without taking focus, and when closed it does not return focus to the Donate link that opened it. It has both aria-labelledby and aria-label, and the aria-label ("Quick donation (prototype, does not charge)") overrides the visible heading. Why it matters: a screen reader announces a dialog the user never opened, and after closing it via Donate, focus falls to the document start. Fix: when it opens on scroll, treat it as a landmark (`role="region"` or `<aside aria-labelledby="give-h">`, no dialog role) and don't announce it. When it opens from a Donate link, move focus to the heading or the switch and remember the trigger, then on close (X or Esc) return focus to that trigger. Drop the aria-label and keep the prototype note as visually hidden text.

## P2: should fix

5. **The pop-out covers content and controls.** Section: pop-out over stories. Viewport: 1440, where it sits over the stories "1 of 6 / Prev / Next" pager at certain scroll positions. At 375 it takes 216px of an 812px viewport (27%) across most of the page, sitting on top of the stories, the program copy and the newsletter field. Why it matters: it competes with the stories it is supposed to follow, and on mobile it reads like an interstitial. Fix: at 1100px and below, show a collapsed state first, a single 56px "Give monthly" bar or extended FAB that expands into the card on tap (M3E container transform), and keep the full card only after an explicit Donate tap. On desktop, hide it while the stories section's pager or the close band is in view (IntersectionObserver), or offset `bottom` to clear them.

6. **The pop-out heading contradicts the one-time choice.** Section: pop-out. Viewport: both. Observed: with "One-time" selected, the heading still says "Become a monthly miracle." while the button says "Give $50 today". Fix: swap the heading with the frequency, using one-time copy from WordSmither. Don't invent the line in design.

7. **The amount ladder and target spacing.** Section: pop-out. Viewport: 375. Observed: the six buttons measure 49px each (the selected one 64px) with 2px gaps, so the 48px hit areas nearly touch. The $250/$300/$350 steps look arbitrary next to $25/$50/$100. Why it matters: fat-finger mis-taps on a money control, and the ladder looks unconsidered. Fix: cut to four amounts plus "Other" (an M3E connected group works well with 4 or 5 segments), which gives roughly 60px segments at 375. Raise the visual height from 36px to 40px. The amount values are the client's call, so flag them rather than set them.

8. **Anchors land under the sticky nav.** Sections: all anchor targets (#stories, #programs, #events, #involve). Viewport: both. Observed: the nav is 112px tall at 375 and about 112px at 1440 (64px logo plus 24px padding). With no `scroll-margin-top`, headings land under it. I confirmed this at 375, where the stories mosaic sat under the bar. Fix: `section[id]{scroll-margin-top:128px}`. Also consider shrinking the nav to a 48px logo with 12px padding once `.scrolled` applies. The bar is too heavy on mobile.

9. **The truth headline line-height breaks on mobile.** Section: truth. Viewport: 375. Observed: `.h1x` has a fixed 72px line-height while the font shrinks to 36px, so "too." floats a full line below "Rent's due. Miracles". Separately, at 1440 the space between the Caveat "Miracles" and "too" visually collapses ("Miraclestoo"). Fix: `line-height:1.1` (unitless), and add a small right margin (about 0.15em) to `.script` inside headings, since Caveat's sidebearings eat the space.

10. **Story filters have no empty state, and the pager count is fiction.** Section: stories. Viewport: both. Observed: Balance and Pillars return 0 tiles, and Safe Haven and Where Are They Now return 1, which leaves a blank area or a lone tile. The pager says "1 of 6" but only rotates the same seven tiles. At 375 the nine chips wrap to four rows, about 230px, before any story. Why it matters: stories are the lead section, and an empty filter is a dead end. Fix: disable or hide filters with no content in the prototype, and add an empty state ("No Balance stories yet. See all stories" with a reset link). At 600px and below, put the chips on one horizontally scrolling row with edge fade, or reduce them to All / Video / Read plus a "Program" menu. For the client build, show the pager count from real content, or drop it.

11. **Mobile story rhythm.** Section: stories. Viewport: 375. Observed: every tile goes full-width at min 320px, so the section is about 7 screens tall, with two of the first three being colour fields without photos. Fix: at 600px and below, use a 2-column mosaic for the quote and photo tiles, keeping wide tiles at span 2. Alternatively, use a horizontal snap carousel with peek. The asymmetric corners survive either way, and both keep stories first without burying programs.

12. **Small orange-700 text is below AA.** Sections: eyebrows (14px uppercase). Viewport: both. Observed: #BB6F00 on white is about 3.9:1 and about 3.6:1 on sun-100. It passes only for large text, so the Caveat script words are fine. Fix: darken the eyebrow token to roughly #9A5B00 (about 5.3:1 on white), or set eyebrows in navy with an orange rule. Keep #BB6F00 for the script highlight, which is large.

13. **The pop-out's stacking is fragile.** Section: pop-out. Observed: `.give` declares `z-index:30` and then `z-index:3` in the same rule, so 3 wins. It works today only because no later section creates a higher stacking context, and it sits under the nav (20). Fix: keep a single z-index of 30. Also move the form out of `.hero-media` to the end of `<body>`. A fixed element inside an overflow:hidden, parallax-driven parent is a future bug the moment anyone adds a transform to that parent.

## P3: polish

14. **Video links leave the page silently.** Hero chip, truth chip and video tiles go to YouTube in the same tab. Fix: open a lightbox player (the prototype can fake it), or at least add an external indicator with "opens YouTube" in the accessible name.
15. **Count-up stats announce noise.** The `b[data-count]` text changes every frame. Fix: put the final value in an `aria-label` on the card, and mark the animated number `aria-hidden`.
16. **Hover-only affordances on tiles and cards** (lift and shadow) have no `:focus-visible` counterpart. Fix: mirror `:hover` with `:focus-visible` on `.tile`, `.icard`, `.ev` and `.prog`.
17. **Footer headings** are `h4` straight after section `h2`s. Fix: use `h3`, or `p` with the same style.
18. **Newsletter input** has no visible label (only the placeholder), and its invalid state is the browser default. Fix: put a visible small label above it in white, and add an inline error in sun text for an invalid email.
19. **The heart crop on Balance** (`c-heart`) cuts through the mother's face at some widths. Check the crop against the photo, or nudge `object-position`.
20. **The disabled pager button** has no visual disabled state beyond the browser default. Give `.btn:disabled` 38% opacity and remove its hover lift, following M3 disabled rules.

## Figma fidelity (provisional)

The hero follows the recorded 154:947 geometry at 1440: media box at x836, the blob, the heart and the photo clip. The close band follows 154:1238. Two drifts are visible in code. First, the pop-out was condensed from 340px to 300px, an approved change, so update Figma to match rather than revert. Second, the pager label in Figma is "1 of 6", which code imitates without real pages (see item 10). At 375, the hero stacks text over photo with the photo pushed below the fold, so the girl with the walker isn't seen on first load. Check 154:625 to see whether the photo is meant to sit above the fold on mobile. If it is, reduce the hero `gap` and the margin-top on the media.

## On the ?m3=1 page-wide flag

It is worth doing, but as a narrow pass, not a restyle. What it would change:

- **Buttons:** one shape-morph rule for every `.btn` (pill at rest, 16px corners on hover, 10px on press, spring spatial curve). The page already does a version of this with an 18px/12px morph and a different curve, so the flag is mostly about unifying tokens. Add M3 state layers (8% hover, 10% press overlay) instead of translateY lifts, which would also give a free focus state.
- **Chips:** filter chips become proper M3 filter chips, with a check icon on select and 8px corners morphing to full. This would make the selected state legible without relying only on colour, which is a real accessibility gain over today's colour-only state.
- **Pager:** Prev/Next become a connected button group, matching the amounts. That gives the page one recurring interaction signature.
- **Leave alone:** story tiles, program crops and involve cards. Their asymmetric corners and duotone shapes are the brand and must not be normalized into M3 shape scales. The flag should touch controls only, never containers.

The value is consistency and stronger states for about a day of work. The risk is that it pushes the page towards Android-app neutrality. If it is built, review the flagged and unflagged versions side by side on the stories section specifically.

## Claims

Design depends on two figures. "Watch 20 years of miracles" is a CTA label, and the four stat cards (2,100+, 41,437, 88 cents, up to $500) are the proof band's whole layout. If any of them is withdrawn, the stats grid needs a 3-card variant, so plan that variant now. I have not verified the claims; that is not a design call.
