# Responsive behavior

Instapage has two layouts per page, desktop and mobile, not a continuous range of breakpoints. Responsive intent is DesignChamp's decision and belongs in the spec; production reproduces it with native controls (`platform.md` §3, §4).

## 1. The platform's model

| Fact | Consequence for the spec |
|---|---|
| Mobile shows below 768 px of browser width; desktop at 768 and above. Tablets in portrait get mobile | Specify two layouts. The mobile layout also serves portrait tablets, so check it at 767 px as well as on a phone |
| Canvas blocks respond up to 1200 px; the mobile canvas is 400 px | Desktop spec frame 1440 wide with a 1200 content column (guide at 960); mobile spec frame 400 wide |
| Fluid Grid containers reflow and stack in their numbered order on mobile; the mobile layout can reorder, resize or hide containers | Give every container a mobile order. When mobile needs a different order or a hidden container, say so per container |
| Mobile uses the same elements as desktop; an element cannot move to another block on mobile | Reading order across blocks is fixed. If mobile needs content in a different block, the spec shows a duplicate element with desktop-only and mobile-only visibility |
| Device-specific size, line height, padding and alignment exist in limited release | Where the workspace has them, per-device type sizes are native. Where it does not, the spec's mobile type sizes are a constraint to check at INSPECT |
| Blocks can be hidden on mobile, never on desktop | A desktop-only block is a constraint: use hidden elements and a minimal block height, or rethink with DesignChamp |
| Sticky header or footer is the first or last block, per device | Mark it in the spec; test it only on a published URL |

## 2. What the spec states

For every block:

- **Type:** Fluid Grid (grid columns and rows) or Canvas.
- **Desktop and mobile arrangement:** both drawn, not described.
- **Container mobile order** (Fluid Grid): the number each container stacks at, and any container hidden on mobile.
- **Visibility:** elements shown on desktop only or mobile only.
- **Type sizes per device:** only where they differ; otherwise the desktop size holds.
- **Image crops per device:** focal point and safe area for each crop, and whether the image is an element or a block or container background (backgrounds crop differently as the width changes).
- **Minimums:** tap targets and text sizes that must hold at 375 px.

## 3. Technical consequences

Responsive intent (what the mobile page should feel like, how dense it is, what leads) is DesignChamp's decision for this client and this project. These are only the platform's consequences:

- **Stacking follows the numbers.** Instapage stacks Fluid Grid containers in their numbered order. If the spec's mobile order differs from the desktop order, the spec says so per container; production never infers it.
- **Background crops move.** A block or container background image is cropped differently at every width. When readable text sits over one, QA checks it at each width (RS-06); a problem goes back to DesignChamp.
- **Long real copy.** Test the approved copy at its longest, at 375 px. A headline that wraps badly at the spec size is a constraint for DesignChamp (size, measure) and possibly WordSmither (length), never something production shortens.
- **Tap targets** of at least 24 × 24 CSS px with spacing, per WCAG 2.2 success criterion 2.5.8 (Target Size, Minimum). An accessibility floor, not a style. [W3C WCAG 2.2]
- **Padding units.** Instapage advises against vh for left or right padding in Fluid Grid containers, and recommends at least 20 px of block padding left and right so content does not touch the edge on tablets.

## 4. QA widths

Check each page at: 1440 and 1200 (desktop), 769 (smallest desktop), 767 (largest mobile: portrait tablet), 390 and 375 (phones). Look for horizontal overflow, clipped or overlapping text, crops that lose the focal point, spacing that collapses, tap targets, and sticky bar behavior (`qa.md` RS-01 to RS-10).
