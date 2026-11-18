# References

Use these as patterns and sources. Build in the Hub's own code; don't add frameworks. Links checked by name only on 2026-10-20: confirm each before relying on it.

## In this folder

| File | Use it for |
|---|---|
| `references/tokens-v2.css` | Colour roles, surfaces, status, type scale, card spacing, icon sizes, light / dark / system. Map onto the Hub's existing variables |
| `screenshots/1-weekly.png` … `6-home.png` | Your mockup with numbered markup pins |
| `screenshots/7-phone-status.png` | The phone problem: clipped tiles, no cards above the fold |
| `screenshots/8-new-task-errors-keep.png` | **The error pattern to reuse** for every new prompt |
| `taskhub-mockup_v2_MARKUP.html` | All pins and notes, live. Press M to toggle |

From the Oct 12 handoff you already have: `taskhub-board-prototype.html` (our prototype; the standup and side sheet patterns) and `taskhub-v1-spec.md` (column order).

## Icons

**Lucide** (lucide.dev), the maintained successor to Feather, which the Oct 12 spec named. ISC licence. Use the static SVGs (`lucide-static` on npm) inline or as a sprite; no React needed. Pin the version you install and note it in the code.

| Rule | Value |
|---|---|
| Grid / stroke | 24 / 1.75 |
| Size | 16px in UI, 20px in nav and the bottom bar |
| Colour | `currentColor` |
| Accessibility | Decorative icons `aria-hidden="true"` beside a text label; icon-only buttons get `aria-label` and a tooltip |
| Suggested names | home, layout-grid, users, briefcase, building-2 (nav); plus, calendar, clock, lock (blocked), circle-check (QC passed), file-text (brief), undo-2, search, settings, x |

Keep the Traffik logo as it is.

## Patterns

| Pattern | Reference |
|---|---|
| Board, card front, card back, checklists, inline add, shortcuts | Trello (trello.com; shortcuts at trello.com/shortcuts) |
| Type and colour roles for a dense work tool | Atlassian Design System: atlassian.design/foundations (typography, color, tokens) |
| Drag and drop if yours struggles on touch or long lists | Pragmatic drag and drop: atlassian.design/components/pragmatic-drag-and-drop (framework-agnostic) |
| Side sheet for task detail | shadcn/ui Sheet: ui.shadcn.com/docs/components/sheet |
| Move toast with Undo | Sonner: sonner.emilkowal.ski (pattern only) |
| Modal dialog focus rules | WAI-ARIA APG, Dialog (Modal): w3.org/WAI/ARIA/apg/patterns/dialog-modal |
| Accessibility bar | WCAG 2.2 AA: w3.org/TR/WCAG22; target size 2.5.8 |
| Automated check | axe-core (github.com/dequelabs/axe-core), run in light and dark |
