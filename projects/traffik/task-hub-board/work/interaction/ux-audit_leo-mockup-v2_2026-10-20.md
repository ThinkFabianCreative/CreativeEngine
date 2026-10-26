# UX audit: Leo's mockup v2 (Status · Calendar · Standup)

```
CLIENT:    Traffik
PROJECT:   Task Hub board
SOURCE:    taskhub-mockup-status-calendar-standup.html, from Leo M, supplied by Andres 2026-10-20
           (copy: work/reviews/leo-mockup-2026-10-20/)
COMPARED:  taskhub-board-prototype.html (our hi-fi) and ux-audit_hot-sheet-weekly_2026-10-14.md
METHOD:    Clicked through at 1440×900: Weekly, Day view, Calendar, Status board, Standup (Creative,
           all 12 steps), task dialog, Home, Executive, "Viewing as" Leo (Account/PM) and Matt (Creative).
           No screen reader pass; New Task form, Resourcing and Clients only glanced at
LENS:      Cognitive load for CDs, designers and PMs
```

> **Severity note (2026-10-20):** read 🔴 High as **Major** and 🟠 Medium / 🟡 Low as **Minor**, the scale used in `designchamp-review_leo-v2_2026-10-20.md`. Nothing here blocks the primary task.

## Verdict

Big step. Leo has closed most of the Oct 14 list: side nav, a stage board, a guided standup, blockers with reason/owner/follow-up date, brief links, "My team's work / Everyone", and a role switcher. The standup is now close to ours and in places better (per-person "What moves today / Will it make the promised date / What's blocking you", a wrap-up with "Copy summary").

What's left is mostly **load at the top of every view** and **who sees what by default**. The tool now shows the right things; it shows too many of them at once.

## Scorecard against the Oct 14 audit

| Oct 14 item | Status in v2 |
|---|---|
| B1.0 Side navigation | ✅ Done, collapsible, with Viewing as + user |
| B1.1 Board by stage | ✅ Status → Board (8 columns) and List |
| B1.2 Scope, role default | 🟠 Toggle exists; **no role default** (see #1) |
| B1.3 Avatar person filter | 🟡 Dropdown only |
| B2.5–7 Four things per card | 🟠 Parent line still on every card; Weekly cards add a due-date pill |
| B2.6 One badge | 🟠 Status chip + Overdue chip still stack (Weekly, Mon) |
| B3.10 Red only for problems | ✅ Mostly; status colours are calm |
| B3.12 Secondary text ≥12 px | 🔴 Client tag, due pill, avatars, KPI labels are 11–11.5 px |
| B4.14 One summary row | 🔴 Now **two** rows: 7 KPI tiles + 6 filter chips |
| B5.17–18 One account lead, creative lead, reviewer | ✅ On the full task page (Ownership: Account manager, Project manager, Creative lead, Reviewer, Account team). 🟠 Not in the quick dialog |
| B5.19 Blocker reason/owner/since | ✅ On hold shows reason, owner, follow-up date |
| B5.20 QC checklist | 🟠 Five-item checklist on the full task page, **advisory by design** (Settings: "never blocks a status change"). v1 spec said sending waits on it |
| B5.21 Brief link | ✅ "Open the brief document"; standup Intake step checks "No brief yet" |
| B6 Side sheet detail | 🟠 Centered modal that covers the board; "Open full page" exists |
| B7 Run stand-up | ✅ Done, strong |

## Findings (🔴 high · 🟠 medium · 🟡 low)

| # | Finding | Sev | Who it hurts | Fix |
|---|---|---|---|---|
| 1 | **Everyone sees Everyone.** Viewing as Matt (Creative) the Workspace still opens on "Everyone", 34 open, all clients. "My team's work" is one click away but never the default | 🔴 | Designers most | Default Mine for makers, My team for CDs/leads, Everyone for PMs/leadership. Remember last choice |
| 2 | **Two summary rows doing one job.** 7 KPI tiles (Total open, Active, In the queue, On hold, Overdue, Due this week, With the client) then 6 chips (Overdue 1, Due on the weekend 1, Needs a date 1, In the queue 1, On hold 1, Unassigned 1). Overdue, On hold and In the queue appear in both, with different numbers (In the queue: 14 vs 1) | 🔴 | Everyone: ~13 numbers before the first card | One row of 4: **Overdue · Blocked/On hold · Needs someone · Needs a date**. Clickable as filters. Hide zeros. Move Total/Active/Due this week to Executive |
| 3 | **Same row repeats on every view.** Weekly, Day, Calendar and Status each carry the KPI tiles + chips; on Home they reappear as a third variant | 🟠 | Everyone | Put the summary once per page, in the header band **below** the view switcher (DesignChamp §3.3) |
| 4 | **Two status layers in one dialog.** "Upload to trade portals" shows *In the queue* in the header, a Status select (*In the queue*) and "Project status: Quality Control" | 🔴 | PMs, designers | Steps don't need their own stage. Show one status (the project's) and the step as "current step". This is B2.9 from Oct 14: one card per task |
| 5 | **"In the queue" sits before Intake** on the board. Work flows right to left at the start | 🟠 | PMs | Order as in the v1 spec: Intake → Ready (rename "In the queue") → In progress → Internal review → Quality Control → With client → Feedback → Done. Leo has no Feedback column yet. On hold as a lane above, not a column between With client and Complete |
| 6 | **Age pill unexplained.** Yellow "1d / 5d / 7d" boxes on every board card, all the same warning colour; meaning only in a hover tooltip ("7 days in In the queue") | 🟠 | Everyone | Show only past a threshold (e.g. >3 days in stage), neutral grey; amber only when it threatens the date. Label "7d in stage" |
| 7 | **Parent line on every card** ("FY26-27 webinar promo video, cut 2", "Q4 trade ad resize set") | 🟠 | Scanning speed | Drop on the Status board. On Weekly and Day keep it as one truncated secondary line (DesignChamp: it lets a CD group scattered steps) |
| 8 | **Quick dialog assigns from the whole agency.** 11 people as chips under Creative/Media/Account. The roles exist on the full task page but not here | 🟠 | PMs | Bring the full page's Ownership rows into the dialog: Account manager, Creative lead, Maker, Reviewer (≠ maker). Picker, not a wall of chips |
| 9 | **QC checklist is hidden and advisory.** It lives only on the full task page, the card doesn't show progress, and it never blocks moving to With client | 🟠 | CDs | Show "QC 3/5" on the card and in the dialog. Stays advisory; sending under 5/5 asks for a logged reason (READ-FIRST, Decision 3) |
| 10 | **Modal hides the board.** Detail opens centered over everything | 🟡 | PMs in standup | Right-side sheet so the column stays visible; keep "Open full page" |
| 11 | **Home "My work today: Nothing on your list"** while the KPI row says 7 open, 5 due this week | 🟠 | Everyone, first thing in the morning | Empty today → show "Next up" (next 3 by date) instead of an empty panel |
| 12 | **Standup is 12 steps** and opens on Internal review, not Blocked/On hold | 🟡 | CDs running it | Start with On hold/blocked (the call to action), then With client, Review/QC, people. Skip empty steps automatically. Intake step with 10 items × 3 buttons is heavy; show only items missing a brief |
| 13 | **Small secondary text.** 11 px on client tag, avatars, KPI labels, due pills | 🟡 | Readability, WCAG 1.4.3 | 12 px min, ≥4.5:1 |
| 14 | **Executive visible to everyone** in the nav, including Matt | 🟡 | Designers (noise) | Show by role |

## What Leo did that we should copy back

- **Standup per-person prompts** and the **"Also watch"** column (On hold items the person is tied to).
- **Wrap-up with marks count + "Copy summary"** — ready for Slack.
- **On hold card**: reason · owner (client-side) · follow-up date, in one line.
- **Calendar as project bars** with "+N more" per day; better than our Calendar for spanning work.
- **"Viewing as"** switcher: excellent for demos and QA of role defaults.

> Superseded by `leo-v2-handoff_READ-FIRST_2026-10-20.md`, which merges this list with the DesignChamp pass.

## Top 5 for Leo next (in order)

1. Role-based default scope (#1).
2. Collapse KPI tiles + chips into one 4-number row, once per page (#2, #3).
3. One status per card/dialog; steps live under their project (#4, #7).
4. Board order + On hold as a top lane (#5) and a quiet age pill (#6).
5. Roles in the dialog (account lead, creative lead, maker, reviewer) and the QC checklist (#8, #9).

Items 1, 2 and 6/7 are a day or less each; 3 and 5 are the real build.

## Visual markup

- Live: `../reviews/leo-mockup-2026-10-20/taskhub-mockup_v2_MARKUP.html` (Leo's file plus `markup-overlay.js`). Click a pin for its note; press M to toggle.
- PDF: `../reviews/TaskHub_Leo-v2_audit-markup_2026-10-20.pdf`. Pin numbers there are the markup's own numbering (#1–21), not the table above.

*Correction, same day: an earlier draft said "Start standup" was not a button. It is a `<button>`; the finding is removed.*
