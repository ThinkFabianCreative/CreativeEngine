# Homepage, better-interface review (DEVELOP r1)

CLIENT: Traffik · PROJECT: website-d2c · SOURCE SCOPE: PROJECT-LEVEL · design-champ via `better-interface`, 2026-11-18
This is a craft check on measurable interface rules. It is not a verdict on the idea; that stays with `creative-engine-director` (see `2026-11-18_director_develop-r1-review.md`).

## Scope and coverage

- **Scope:** Figma file `eLfndwoXdZ0nURgxN8VIhn`, Page 12, inspected read-only:
  - Route 1 at 1440 (`679:431`)
  - Route 2 at 1440 (`680:431`), seen only through its 390 first screen and its motion notes
  - The 390 first screens of both routes (`680:606`, `680:623`)
  - Motion notes `679:597`, `679:598` and `680:603`
- **Stack:** a Figma design with no code. The motion notes name the build target: Webflow Interactions with GSAP SplitText and ScrollTrigger.
  - Tokens: the variable collection "Traffik · site tokens" (10 color roles).
  - Text styles: Traffik/Display, H1, H2, H3, Body, Small, Label and Figure.
- **Conventions found:** `2026-11-18_homepage-build-note_v01.md` (one red per page, yellow only on figures, Caslon has one job per page). The root `CLAUDE.md` holds CreativeEngine method only and has no interface rules.
- **Boundary:**
  - **Not inspected:** Route 2's desktop sections below the fold, motion notes `679:599`, `679:600`, `680:604` and `680:605`, mobile beyond the first screen (it isn't designed yet), and every hover, focus and menu-open state (none are drawn).
  - **Placeholders not judged:** grey image boxes, the logo box and the stand-in Caslon.

| Domain | Evidence inspected | Result |
|---|---|---|
| Accessibility | Measured token contrast pairs; motion notes 679:597, 679:598, 680:603; both 390 first screens | 2 findings |
| Layout | Route 1 at 1440, both 390 first screens, CTA hierarchy | Clear |
| Writing | Not reviewed: `better-writing` is not installed. WordSmither owns the copy | Not reviewed |
| Typography | Text styles from `get_variable_defs`, Route 1 at 1440, both 390 first screens | 2 findings |
| Colors | All 10 color tokens, contrast computed per pair | Merged into the Accessibility contrast finding (one root cause) |
| UI polish | Not reviewed: `better-ui` is not installed. Motion is covered by `design-motion-principles` and `apple-design` | Not reviewed |

## Findings

| Severity | Domain | Location | Before | After | Why |
|---|---|---|---|---|---|
| HIGH | Accessibility | Token `color/accent-red` `#d91f1f`. Used on: R1 "Ideas that survive review." (679:431 hero; 680:606 at about 20px Semibold); the R1 sign-off; R2 "Some rules are real." | Red text measures **4.17:1** on `color/bg` #000, **3.75:1** on `color/surface` #111 and **4.24:1** on `color/paper` #F1EBDD | Cheapest fix: set every red text line at 24px or larger (H3 or above), so it counts as large text (3:1); it then passes on black and paper. On #111 it still needs ≥24px. Otherwise add a lighter text-only red role and keep #d91f1f for fills. The color itself is the team's call | Contrast trigger (WCAG 1.4.3). Red below 24px fails 4.5:1. The 390 hero line renders under 24px and does not count as bold (Semibold, 600) |
| MEDIUM | Accessibility | Motion note `679:597`, Route 1 rule → idea | "Rule letters break apart and rebuild as the hero line (SplitText chars)". Nothing says how assistive tech reads the split | Keep the full sentence as the accessible name of the parent (`aria-label` with the visible text) and hide the character spans with `aria-hidden="true"`. The reduced-motion end state is already specified | Character-split text is read letter by letter by several screen readers. The hero line is the H1 |
| MEDIUM | Typography | Motion note `679:598`; Route 1 figures 77%, 9.4% and 45,000+ (style Traffik/Figure, 72px) | Count-up 0 → value over 1.2s, with no numeric setting | `font-variant-numeric: tabular-nums` on the figure element | A changing value with proportional digits changes width every frame, so the "unv" mark and the source line beside it jitter |
| LOW | Typography | 680:606 rule panel, Caslon at the Small size (14px) | "STAND-IN: Adobe Caslon Pro" is Libre Caslon **Display** set at 14px | Check it again with Adobe Caslon Pro, which is a text cut. If a Display stand-in stays, keep it at 28px or larger | A display cut has hairlines drawn for large sizes, so at 14px they break up. This repeats build-note open item 4; it goes away once the real face is in |

No findings were cut by the cap.

## Verification

**Passed**
- The other contrast pairs, computed from token hex with the WCAG relative-luminance formula:

  | Pair | Contrast |
  |---|---|
  | `text-muted` on #000 | 7.84 |
  | `text-muted` on #111 | 7.05 |
  | `evidence-yellow` on #000 | 14.67 |
  | `text-on-paper` on paper | 15.89 |
  | white on #000 | 21 |

- **Text styles:**
  - Body 18/1.5 at weight 400.
  - Small 14/1.45 at weight 400.
  - Headings descend in size: H1 64, H2 40, H3 24.
  - Nothing under 18px is lighter than 400.
- **Primary actions:** each page view has one filled action. "Start a project" is filled; "See the work" and "Book a call" are outlined.
- **Reduced motion:** specified in all three notes inspected (final value only, end state without the split, and a 0.2s crossfade).

**Not verified**
- **Focus indicators and keyboard paths:** no focus or menu-open states are drawn. They need specifying before the build, because a missing focus ring is a blocker on sight.
- **Secondary-button outline contrast:** the border token wasn't confirmed. If it's `color/line` #333, it measures **1.66:1** on black, under the 3:1 that WCAG 1.4.11 requires for a component boundary.
- **The rest of the page:** reflow at 320px and 200% zoom, mobile below the first screen, Route 2 desktop below the hero, and the four motion notes I didn't open (including the 3D poster).
- **Label tracking:** `letterSpacing: 4` on the 12px label couldn't be confirmed as px or %.

## Verdict

**Block** at the time of review. Writing and UI polish were not reviewed.

## Fixes applied in Figma (2026-11-18, after review)

A read-back of every red text node narrowed the HIGH finding to one node. Desktop R1 "Ideas that survive review." (679:456) is already H3 at 24px, and R2 "Some rules are real." (680:521) is H2 at 40px. Both count as large text and pass 3:1 on black. No red text was found on paper.

| Finding | Change | Node |
|---|---|---|
| HIGH contrast | Mobile "Ideas that survive review." went from a hand-set 20px Semibold to the `Traffik/H3` style (24px). Copy and color are unchanged. The rule is now: red text is never set below H3 | 680:620 |
| MEDIUM SplitText | Added a line to the motion note: "Accessibility: parent keeps the full line as aria-label; char spans aria-hidden" | 679:597 |
| MEDIUM count-up | Added a line to the motion note: "Numerals: font-variant-numeric: tabular-nums" | 679:598 |
| LOW Caslon stand-in | Not changed; it resolves when Adobe Caslon Pro goes in | — |

I took a screenshot of 680:606 after the fix. The red line now sits at 24px with no clipping or overlap, and the button below moved down 5px.

**Verdict after fixes: Approve.** No HIGH findings remain in the domains inspected. Focus states and the secondary-button outline are still **Not verified**. Writing and UI polish were not reviewed.
