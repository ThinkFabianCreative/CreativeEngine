# Trello gap, borrowable libraries, type scale, theme and a11y

```
CLIENT:   Traffik (internal)
PROJECT:  Task Hub board
SOURCE:   Leo's mockup v2 (work/reviews/leo-mockup-2026-10-20/), our prototype, Andres's direction 2026-10-20
METHOD:   Code inspection of both files; axe-core 4.10 (WCAG 2.0/2.1/2.2 A+AA) in headless Chrome, light and dark,
          on Weekly, Status and Home; computed-style type census of the Weekly view. Trello comparison from
          product knowledge, not a fresh test of Trello
```

Direction from Andres: the app should be based mainly on Trello. Theme belongs in user profile settings. Must pass a11y.

## 1. Gap to Trello

Trello's model is simple: **board → lists → cards**, everything else on the back of the card. Leo's build already has the board. The gap is mostly on the card and in interaction speed, not views.

| Trello pattern | Leo v2 | Our prototype | Gap |
|---|---|---|---|
| Lists as columns, cards move by drag | ✅ Status board, drag + `[` `]` keys | ✅ | None. Keyboard move is better than Trello's |
| **Card front: title, then small badges** (due, checklist 2/5, comments, members) | 🟠 Client, title, parent, status chip, avatar+name, age, due pill | 🟠 Closer (4 things) | **Medium.** Trello's front is title-first with icon badges, no status chip (the list says it) |
| Labels (coloured, optional text) | ❌ Client colour does this job, unlabelled | ❌ | **Medium.** Use labels for client *or* type, one meaning only (see DesignChamp colour pass) |
| **Card back** as one panel: description, checklist, activity/comments, members, dates | 🟠 Modal with 3 statuses, agency-wide people chips | ✅ Side sheet | **Medium.** Fix status + roles (audit #16–18) |
| **Checklists** with progress on the card front | ❌ (QC is a column) | ✅ QC checklist | **Large for Leo.** This is Trello's most-used feature and our QC rule |
| Add card inline at the bottom of a list | ❌ "+ New Task" form only | ❌ | **Medium.** Quick add (title only, lands in Intake) cuts PM load |
| Quick edit (`E`), shortcuts (`Q` my cards, `F` filter, `?` help) | 🟠 Some keys | 🟠 | **Small-medium** |
| Filter: my cards, member, label, due | ✅ Team/Person/Client + scope | ✅ | Role default missing (audit #1) |
| WIP limits / card aging | 🟠 Age pill on every card | ❌ | Show age only past threshold |
| Collapse a list | ❌ | ❌ | Small. Useful for Complete and On hold |
| Views: Table, Calendar, Timeline, Dashboard | ✅ List, Calendar (bars), Executive | ✅ List, Calendar, Workload, Leadership | **Ahead of Trello** |
| Automation (Butler) | ❌ | ❌ | Later. Rules like "moved to With client → notify AM" |
| Standup | ✅ | ✅ | **Ahead of Trello** |

**Size of the gap:** views and workflow are ahead of Trello. The gap is the **card** (front and back) and **speed** (inline add, quick edit, checklists). Roughly: card front 1–2 days, checklist + card back 3–5 days, inline add + shortcuts 2 days. The biggest Trello lesson is subtraction: the list tells you the status, so the card doesn't.

## 2. Libraries worth borrowing from

Leo's mockup is **vanilla JS with string templates, not React**. So either borrow patterns and tokens now, or adopt packages if the production app is (or moves to) React. Check what the live Task Hub runs before choosing. All below are open source (MIT or Apache 2.0); confirm the licence of the exact version before shipping.

| Need | Library | Why | Works without React? |
|---|---|---|---|
| Board drag and drop | **Pragmatic drag and drop** (Atlassian) | Built for and used by Trello and Jira; accessible-drop guidance included | **Yes**, framework-agnostic. Leo already has drag + keyboard; adopt only if his drag fails on touch or with long lists |
| Board drag and drop (React) | dnd-kit | Mature, keyboard sensors, sortable lists | No |
| Dialog, side sheet, menus, popovers, tooltips | **Radix UI primitives** / **shadcn/ui** (copy-paste components on Radix) | Focus trapping, Escape, ARIA done right; shadcn's Sheet = our side sheet | No |
| Accessible grids, lists with drag, date pickers | **React Aria** (Adobe) | Strongest a11y of the lot; GridList with keyboard drag | No |
| Dashboard KPIs, bars, donuts (Executive) | **Tremor** | Ready KPI cards, bar lists, charts on Tailwind | No |
| List view | **TanStack Table** (+ TanStack Virtual) | Sorting, column visibility, virtualised rows | Core is framework-agnostic |
| Command palette (`⌘K` jump to client/task) | cmdk | Linear/Vercel-style quick find | No |
| Toasts ("Moved to Internal review · Undo") | Sonner | Small, accessible | No |
| **Tokens: type, colour, spacing** | **Atlassian Design System tokens** | Trello's own system: 14px body, 12px small, tested light/dark colour roles | Yes (CSS variables) |

Recommendation: **take Atlassian's tokens as the reference for the type scale and colour roles now** (no new dependency; DesignChamp's changes are CSS and templates). Keep Pragmatic drag and drop in reserve. Use Radix/shadcn and Tremor as the reference for dialog/sheet and Executive patterns, and as the stack if the app goes React.

## 3. Typography for scannability

**Measured (Weekly view, light):** 18 different size/weight combinations on one screen. Across the file's CSS, sizes run 8–42px, including half-pixel steps (10.5, 11.5, 12.5, 13.5). KPI numerals render at 30px. Three families: Urbanist (display), Manrope (UI), Geist Mono. The most frequent label style is **11px, weight 800, uppercase, letter-spaced** (35 instances: client names, KPI labels, column meta), which is the least legible setting for scanning.

*Skills note:* `impeccable` is not installed (blocked 2026-10-03; see `DesignChamp/skills/awwwards-stack.md`). The Taste pack is built for landing pages, not dense product UI. So this uses `shared/frameworks/typography.md` (§4 hierarchy as reading order, §5 scale, §8 legibility) and Atlassian's product scale as the reference.

**Proposed scale: five steps, one family (Manrope), mono only for job numbers.**

| Role | Size / weight / line height | Used for |
|---|---|---|
| Page title | 28 / 600 / 36 | "Workspace", "Home". Down from 42px |
| Section and column heading | 14 / 600 / 20, sentence case | Column names, panel titles |
| **Card title** | 15 / 500 / 20, max 2 lines | The thing people scan. Brightest, largest on the card |
| Body | 14 / 400 / 20 | Dialog text, comments |
| Meta | 12 / 500 / 16, secondary colour, ≥4.5:1. Client name 12 / 600 | Client, due, assignee, counts |

Rules:
- No uppercase tracked labels under 12px. Client name becomes 12/500 sentence case, coloured text or a label, not shouted.
- `font-variant-numeric: tabular-nums` on dates, counts and hours.
- Drop Urbanist; one sans family is calmer and loads faster.
- Counts are meta, not headlines: no 30px KPI numerals on working views.
- Values match DesignChamp's card anatomy (§3.2 of its pass), which owns this call.

## 4. Load by role (seat)

| Seat | Opens on | Card shows | Summary row shows | Hidden by default |
|---|---|---|---|---|
| Designer / maker | **Mine**, Weekly | Title · client · due · one badge | Nothing, or "2 due today" | Executive, Resourcing, counts |
| Creative Director / lead | **My team**, Board, avatars as filter | Title · client · assignee · one badge | Blocked · In review/QC | Executive |
| PM / account | **Everyone**, Status board with On hold on top ("My clients" is a later option; that scope doesn't exist yet) | Title · client · assignee · due · one badge | Overdue · Needs a date · Unassigned · Blocked | — |
| Leadership | Executive | — | Full counts | — |

Plus a profile setting for **density** (Comfortable / Compact), next to theme.

## 5. Theme in the user profile

*Superseded by the personal settings panel in `leo-v2-handoff_READ-FIRST_2026-10-20.md` (Decision 2).*

Leo already has "Light or dark" in the user menu. It saves to `localStorage` (this browser only). With nothing saved, the CSS appears to follow the OS setting; not confirmed.

Change: store it on the **user profile** (server-side), with three options **System (default) · Light · Dark**, applied before first paint so there's no flash. Keep the OS media query as the System behaviour. Put Density in the same settings panel.

## 6. Accessibility result

| Check | Result |
|---|---|
| axe-core, WCAG 2.0/2.1/2.2 A+AA, light and dark, Weekly / Status / Home | **0 violations** on all six runs |
| Colour contrast (axe) | 312 text nodes pass per view; **22 could not be verified** (text on tinted cards, where the tint is a pseudo-element). Needs a manual check, especially dark theme |
| Keyboard move on board | ✅ `[` / `]` plus drag |
| Not covered | Screen-reader pass, target sizes (WCAG 2.2 2.5.8), focus order in the dialog, reduced motion, 200% zoom |

Leo's base is solid. The legibility problems are within WCAG (11px uppercase is legal) but hurt scanning, which is why the type scale above matters more than contrast fixes.
