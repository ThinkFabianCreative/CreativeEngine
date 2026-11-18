# DesignChamp pass: Leo's Task Hub mockup v2

```
CLIENT:   Traffik (internal). Mockup names real clients: internal only, do not publish
PROJECT:  Task Hub board
INPUTS:   markup-shots 1–4 (Weekly, Status board, task dialog, standup person), markup-overlay.js,
          ux-audit_leo-mockup-v2_2026-10-20.md
MODE:     JUDGE on existing UI, DEVELOP-style recommendations
LIMITS:   Judged from screenshots at 1440×900 (2x). Calendar and Home shots not re-read; contrast
          values are by eye, not measured. Leo's CSS not inspected line by line
```

> **Severity note (2026-10-20):** read 🔴 High as **Major** and 🟠 Medium / 🟡 Low as **Minor**, the scale used in `designchamp-review_leo-v2_2026-10-20.md`. Nothing here blocks the primary task.

## Verdict

The audit is right about the direction and right that load sits at the top of the page. It under-calls the biggest visual problem: **colour has three jobs and no rules.** Client tints on cards, status tints on columns and chips, and red for severity all draw from the same saturated range, so nothing reads as "this is the problem". Fix the colour roles and the card anatomy, and half the audit's density findings get easier, because people can then skip what is calm.

## 1. Challenging the audit

| Audit item | DesignChamp view |
|---|---|
| Missing: **colour roles** | Not in the audit. Weekly cards are tinted by client (CSUN card in dark red, Calveba blue, Champlain teal, Alignment olive). A red client tint sits next to the red "Overdue" chip and the red-pink New Task button. On the board, columns are tinted by status *and* cards keep client-coloured labels. Three colour systems in one view. This is the root of "everything looks equally important". Raise to 🔴 |
| Missing: **primary action colour** | New Task is the only filled red element at rest, so the eye lands on it before any work. Red is a severity colour; the primary button should be the neutral-light fill Leo already uses for selected tabs |
| #2 KPI + chips (🔴) | Agree, and go further: the tiles use 30px numbers (measured; first draft said 44px), the largest type on the page after "Workspace". The page's typographic hierarchy currently says *counts matter more than work*. Shrink, don't just merge |
| #3 summary repeats per view | Agree, but put it **once in the header band, not per view**. Below the view switcher, not above it, so the switcher stays the first decision |
| #6 age pill (🟠) | Agree, and note it reuses the yellow of the "With client" chip and the On hold number. One more reason yellow means nothing |
| #7 parent line (🟠) | Partly disagree. On Weekly, where steps from one project scatter across days, the parent line is what lets a CD group mentally. Keep it on Weekly at secondary weight, single line, truncated; drop it on the Status board, where the column already gives context |
| #9 two badges on late card | Agree, but the cleaner fix is structural (anatomy below): status lives in one slot, lateness lives on the due date, not as a second chip |
| #10 modal vs side sheet (🟡) | Agree it is low. Raise the dialog's real problem instead: 11 people as equal chips is the heaviest block in it (see #8, keep 🟠) |
| #13 11px text (🟡) | Agree, and add **letter-spaced uppercase** on client tags and KPI labels. Tracked caps at 11px on dark is the hardest text on the page to read. Use 12px, sentence-case client name at 600 weight instead |
| Missing: **dark theme contrast** | Card fills (~#15191f) on page (~#0d0f12) are barely separated; cards rely on coloured borders, which is why client tints crept in. Raise card surface one step lighter and drop the coloured borders |
| Missing: **two "Today" signals** | Tuesday column has a pink tint plus a pink "Today" word. Fine, but it uses the same red family as Overdue. Use a neutral lighter column fill and a white underline under the date |
| #12 standup 12 steps | Agree. Visually the standup is the best screen in the build; don't let step logic changes bloat it |

## 2. Keep (do not let Leo lose these)

- **Standup person screen**: big name, three numbered prompts, "Due today or in progress" with On track / At risk / Blocked segmented control, "Done yesterday", "Also watch". Clear two-column hierarchy, honest empty states. This is the reference for the rest of the app.
- **Segmented controls** (view switcher, Board/List, scope): consistent, readable, right weight.
- **Day header pattern** on Weekly: big date numeral + day + "2 deadlines, 3 steps". Good, glanceable.
- **Avatar initials + first name** on cards. Names beat initials-only for a 12-person team.
- **Dialog footer line** "Status, dates and people save as you change them…" Tells people the rule. Keep that tone everywhere.
- **The type family and dark palette base** themselves. The problem is colour roles, not the theme.
- "Viewing as", "How to move cards", "Open full page".

## 3. The five changes that cut most load

All achievable in Leo's existing CSS/JS; no new libraries.

### 3.1 Colour roles (do first; it makes everything else work)

| Role | Colour | Used for | Never used for |
|---|---|---|---|
| Problem | Red, one value (e.g. #ff5a5f) | Overdue date text, Blocked/On hold marker, problem count numbers | Buttons, client identity, Today, column fills |
| Warning | Amber, one value | At risk, age past threshold | Status chips, client labels |
| Status | Desaturated, low-contrast chips (fill at ~12% opacity, text ~70%) | Status chip on card, column header dot | Card borders, card fills |
| Client | **Text colour only** on the client name, or a 3px dot. No card fill, no card border | Recognising the client | Anything else |
| Primary action | Dark theme: off-white fill, dark text. Light theme: ink fill, white text (approved 2026-10-20) | New Task, Next, Save | — |
| Neutral surfaces | Page #0d0f12, card one step up (~#1b1f26), 1px neutral border (~#2a2f38) | All cards, all columns | — |

Columns on the board: neutral fill, status shown by a small coloured dot before the column name. Remove the per-status column tints.

### 3.2 Card anatomy (one card, everywhere)

Width as now. Padding 14px. Vertical gap 6px. Max four rows.

| Row | Content | Type |
|---|---|---|
| 1 | Client name (sentence case, client text colour) · right: single badge only if Blocked/Overdue/High | 12px / 600, no tracking |
| 2 | Task title, max 2 lines | 15px / 500, white |
| 3 | Parent project, 1 line truncated (**Weekly and Day only**) | 12px / 400, ~60% white |
| 4 | Due date (left) · status chip (middle, omit on Status board) · avatar + first name (right) | 12px / 500 |

Rules: overdue turns the **due date text red** ("Due Oct 12 · 1d late"), no extra chip. Age shows only past 3 days in stage, as grey "7d in stage" on row 4; amber when it threatens the date. "Complete" cards drop to 50% opacity on Weekly. One badge maximum per card.

### 3.3 Header pattern (one band, once per page)

```
Workspace                          [Weekly | Day | Calendar | Status]   [Start standup]   [Mine | My team | Everyone]
Oct 12–16  ‹ ›  This week          Overdue 1 · On hold 1 · Needs someone 1 · Needs a date 1       Team ▾ Person ▾ Client ▾
```

- Second line holds the four problem counts as inline text buttons: 14px, number in 600, red number only when >0, hidden when 0. No tiles, no big numerals. Clicking filters the view.
- "Workspace" title down from ~48px to 28px. The page title shouldn't outweigh the work.
- Total, Active, Due this week, With the client move to Executive.
- Filter selects sit at the right of line 2, same height as the counts (32px), so the header is two rows, ~96px total instead of ~330px. That alone puts a full extra row of cards above the fold.

### 3.4 Dialog: one status, people by role

- Header: client · title · one status chip (the project's). Step shown as "Current step: Upload to trade portals" text, not a second status.
- Remove "Project status" block and the step Status select.
- Replace the 11-chip wall with four rows: Account lead, Creative lead, Maker, Reviewer. Each shows one avatar+name and a "Change" link that opens a searchable picker.
- *Correction 2026-10-20: Leo already has these roles and a five-item QC checklist on the full task page; the change is to surface them in the quick dialog.*
- QC: five checkboxes in a block above Comments, only when stage is QC; "Send to client" button disabled until all ticked.

### 3.5 Remove

- KPI tile row and the chip row (replaced by 3.3).
- Coloured card borders and fills.
- Uppercase tracked labels on cards and counts (keep caps only for section labels inside dialogs/standup, at 12px).
- Executive nav item for non-leadership roles.
- Pink/red fill on Today column.

## 4. Per-role check: Workspace on open

| Role | Sees first now | Should see first |
|---|---|---|
| CD | Red New Task button, then 34/19/14/19 tile numerals, then 6 chips. Work starts ~40% down the screen | Scope "My team", the problem line (what's overdue/on hold/in review for my people), then Status board with Internal review and QC columns in view. Review queue is the CD's job |
| Designer | Same: all agency counts, Everyone scope, every client's work | Scope "Mine", Weekly, own cards only, today's column highlighted. The problem line shows only their own overdue/blocked. Ideally no counts at all if zero |
| PM | Counts they can't act on directly ("Total open 34"), then the chips, which are the useful part but look secondary | Scope "Everyone", the problem line as the hero (Needs someone, Needs a date are PM actions), Status board with On hold lane on top |

## How close Leo can get to our prototype

Close. His structure, components and standup already match or beat ours. The gap is styling discipline, not architecture: colour roles, card anatomy and the header band are CSS and template changes, roughly a day each. The dialog roles and QC gating are the real build, as the audit says.
