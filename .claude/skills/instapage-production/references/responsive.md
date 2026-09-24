# Responsive behavior

Instapage has two layouts per page, desktop and mobile, not a continuous range of breakpoints. Responsive intent is DesignChamp's decision and belongs in the spec; production reproduces it with native controls (`platform.md` §3, §4).

## 1. The platform's model

| Fact | Consequence for the spec |
|---|---|
| Documentation says mobile below 768 px and desktop above 768 px; exactly 768 is unspecified. Check actual builder output | Specify two layouts. The mobile layout also serves portrait tablets, so check it at 767 px as well as on a phone |
| Canvas blocks respond up to 1200 px; the mobile canvas is 400 px | 1440/400 are replaceable spec preview widths; Canvas guides do not mandate a universal client grid or Fluid Grid content width |
| Fluid Grid containers reflow and stack in their numbered order on mobile; the mobile layout can reorder, resize or hide containers | Give every container a mobile order. When mobile needs a different order or a hidden container, say so per container |
| Mobile shares page structure. The current mobile guide documents reparenting that also changes desktop; workspace availability must be checked | Specify shared parent changes explicitly and recheck both views. For independent placement, document device visibility and duplicated content if approved |
| Device-specific size, line height, padding and alignment exist in limited release | Where the workspace has them, per-device type sizes are native. Where it does not, the spec's mobile type sizes are a constraint to check at INSPECT |
| Blocks can be hidden on mobile, never on desktop | A mobile-only block is a constraint if desktop block hiding is unavailable; route native alternatives to DesignChamp |
| Sticky header or footer is the first or last block, per device | Mark it in the spec; test what the unpublished environment supports and record unsupported runtime checks as NOT_RUN |

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

Responsive intent (what the mobile page should feel like, how dense it is, what leads) is DesignChamp's decision for this client and this project. The following distinguish platform behavior, project decisions and recommendations:

- **Stacking follows the numbers.** Instapage stacks Fluid Grid containers in their numbered order. If the spec's mobile order differs from the desktop order, the spec says so per container; production never infers it.
- **Background crops move.** A block or container background image is cropped differently at every width. When readable text sits over one, QA checks it at each width (RS-06); a problem goes back to DesignChamp.
- **Long real copy.** Test the approved copy at its longest, at 375 px. A headline that wraps badly at the spec size is a constraint for DesignChamp (size, measure) and possibly WordSmither (length), never something production shortens.
- **Accessibility, not an Instapage limit.** WCAG 2.2 SC 2.5.8 uses 24 × 24 CSS px targets or qualifying spacing/other exceptions. Record the applicable criterion and test it; a fixture’s 48 px button is not a universal requirement. [W3C](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- **Vendor recommendation, not a hard limit.** Instapage advises against vh for left or right padding in Fluid Grid containers, and recommends at least 20 px of block padding left and right so content does not touch the edge on tablets.

## 4. QA widths

Check each page at: 1440 and 1200 (desktop), 769 and exactly 768 (record observed layout), 767 (largest mobile: portrait tablet), 390 and 375 (phones). Look for horizontal overflow, clipped or overlapping text, crops that lose the focal point, spacing that collapses, tap targets, and sticky bar behavior (`qa.md` RS-01 to RS-10).
