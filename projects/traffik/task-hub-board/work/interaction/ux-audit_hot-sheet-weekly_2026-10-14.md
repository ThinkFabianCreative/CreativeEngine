# UX audit: Hot Sheet · Weekly (production)

```
CLIENT:    Traffik
PROJECT:   Task Hub board
SOURCE:    Screenshot of the live Hot Sheet, Weekly view, week of Oct 12–16 2026, supplied by Andres 2026-10-14
METHOD:    Visual audit of one screenshot. Interactions, hover states and keyboard use were not tested
```

**Scope of the screen:** 50 project deadlines + 37 steps across five day columns, Team "All teams", Person "Everyone". The page runs about 2,000 px tall. Wednesday alone holds about 25 items.

**New in production since Oct 10:** the view switcher now shows **Weekly · Day view · Calendar · Status**. "Status" may already be a board by stage. Check it before building §B1.

## A. Findings (severity: 🔴 high · 🟠 medium · 🟡 low)

| # | Finding | Sev | Why it hurts |
|---|---|---|---|
| 1 | **Everything at once.** 87 items for the whole agency, every day, no default scope | 🔴 | A designer or PM has to scan the whole agency to find their own work. The screen answers "what's due?", never "what should I do next?" |
| 2 | **Red everywhere.** About 30 "Overdue" chips with red outlines, plus red dots and the counter chip | 🔴 | Alarm fatigue: when a third of the page is red, red stops meaning anything. Blocked work isn't distinguished from merely late work |
| 3 | **No stage view.** Status appears only as a small chip per item (Intake, Ready, In progress, Feedback, On hold) | 🔴 | You can't see where work piles up (review, QC, with client), which is the question the stand-up needs answered |
| 4 | **4–5 lines per item, all at similar weight:** client tag, title, parent task, type label (Deadline / Step / Milestone / Internal review), status chip, overdue chip, people | 🟠 | The title doesn't stand out, so scanning is slow. The parent-task line repeats on many items |
| 5 | **Small, light-grey secondary text.** Parent lines, type labels and people names look about 10–11 px in light grey | 🟠 | Likely below 4.5:1 contrast and hard to read at a glance (WCAG 1.4.3) |
| 6 | **People as truncated text.** "Debbie, Andres +1", "Jeremy, Anthony", many "Unassigned" | 🟠 | Ownership is unclear: no single account lead, no reviewer, and "Unassigned" steps look the same as assigned ones |
| 7 | **Two kinds of items mixed:** "Deadline" (task) and "Step" (plan step) in the same list with the same look | 🟠 | The same job can appear twice in a week (as a step and a deadline), which inflates counts |
| 8 | **Clients interleaved within a day,** with no sorting by urgency or owner | 🟠 | The most important item of the day can sit at the bottom of a 25-item column |
| 9 | **Counter chips are ambiguous.** "Overdue 41 · 38 overdue, 3 tagged", "Needs a date 23 · 5 tasks, 18 steps" | 🟡 | Two numbers per chip; "tagged" isn't explained; you can't tell if a chip filters or opens something |
| 10 | **Unlabeled red dots** next to some items | 🟡 | Meaning unknown without a legend |
| 11 | **No blocker reason.** "On hold" shows no reason, owner or date | 🟡 | The stand-up can't ask "who owns this?" |
| 12 | **Non-creative work mixed in** (burn reports, budget recommendations, media analyses) under "All teams" | 🟡 | Fine for leadership; noise for the design team |
| 13 | **Top-only navigation.** Home, Hot Sheet and Resourcing sit in the header; clients are buried in a dropdown | 🔴 | No persistent place to move between areas or jump to a client. Andres: side navigation is a must |

**What works:** today's column is tinted; the week navigation is clear; the Traffik header and red "+ New Task" are consistent; filters for Team, Person and Client exist.

## B. Changes to reach the prototype UI

Grouped by area, in suggested build order. "v1" = in `taskhub-v1-spec.md`.

### B1. Views and scope
0. **Side navigation (must-have).** A persistent left sidebar replaces the top-only nav:
   - **Order, top to bottom:** brand · For you · Hot Sheet · Resourcing · Department (e.g. Creative) · Clients (each client filters every view; "All clients" first).
   - **Collapsible** to a 64 px icon rail with a chevron toggle. The user's choice is remembered. Narrow screens default to the rail; it never disappears.
   - **Every item has a tooltip and an accessible name** in rail mode. The current page and the selected client are clearly marked.
   - The top bar keeps search, + Create and the user avatar.
1. **Add a Board view** (v1), or make "Status" the board if that's what it is: eight columns by current step (Intake → Ready → In progress → Internal review → Quality Control → With client → Feedback → Done).
2. **Mine / My team / Everyone scope** at the top of every view; **default to My team** for creative leads and PMs and to Mine for designers. "My team" comes from reporting lines.
3. **Person avatars** as a one-click person filter, alongside the existing dropdown.
4. Keep Weekly, Day view and Calendar. In Weekly, apply the same scope and card rules below.

### B2. Cards (apply to Board and Weekly)
5. **Four things per card:** title (largest, darkest) · client (small, grey) + round · assignee avatar · **one** status badge.
6. **One badge, chosen by priority:** Blocked → Change order → Overdue → Self-review → Promised before plan → High. Never two chips.
7. **Drop from the card:** the parent-task line, the Deadline/Step label, the status chip (the board column says it), and comma lists of names. Show them in the task detail.
8. **Icons only for exceptions:** "no brief" (red) and "QC passed" (green). Feather icons, 16 px.
9. **Merge a task and its steps** on the board: one card per task, placed at its current step. In Weekly, show steps under their task, collapsed.

### B3. Color and type
10. **Red only for problems and the primary action:** Blocked, Overdue, and + New Task. Status labels use the flat Atlassian-style palette: blue in progress, purple review/QC, yellow with client, green done, grey intake/ready.
11. **Overdue on the card as a red label, not an outlined chip;** blocked gets a lock icon and its own lane.
12. **Secondary text at least 12 px** and at least 4.5:1 contrast (for example #626F86 on white).
13. **One type family** (variable) with tabular figures for dates and counts.

### B4. Top of page
14. **Replace the five counter chips with one summary row:** open · need someone · blocked · promised before plan. One number each; zero counters hidden.
15. "Need someone" and "blocked" **expand on click** into a short list (next up / blocked lane). Collapsed by default.
16. **Remove the unlabeled red dots,** or give them a legend and a tooltip.

### B5. Ownership and rules (v1)
17. **Account lead: one person,** never "Darcey/Brad/Ky". Add an Account team field.
18. **New fields:** creative lead and reviewer (the reviewer can't be the maker).
19. **Blocked needs a reason, an owner and a "since" date,** shown in a Blocked lane at the top of the board.
20. **Quality Control checklist** (rename Pre-launch QA): five yes/no questions; "Send / present" waits on it.
21. **Brief link field,** required before Full-track work goes active.

### B6. Task detail (side sheet)
22. Open from any card as a **right-side sheet**, with the board still visible behind it.
23. Contents: breadcrumb to the parent ticket · plan steps with the current step highlighted and the rule steps marked · plan date vs. promised date vs. driver · roles · QC status · blocker · other tasks on the same parent.
24. **"Move to"** control (the non-drag alternative). Escape closes the sheet and focus returns to the card.

### B7. Stand-up
25. **"Run stand-up"** on the board: walks Blocked → With client → Review/QC → each person (including people with nothing on the board) → Ready → Close, spotlighting matching cards, with On track / At risk / Blocked buttons.

### B8. Later (months 2–3)
26. Daily time-log prompt; Workload view on logged hours; hide "free hours" until logging is real.
27. Dates from standard times; "Promised before plan" flag; weekend rule.
28. List view (5 default columns), Leadership view, Completed view with rates.
29. New Task form: one account lead, timeline required, driver for early dates, reason for HIGH, saved drafts.

## C. Quick wins (a day or less each)

- Hide zero counters; one number per chip.
- Remove the parent-task line and the Deadline/Step label from cards.
- Swap outlined "Overdue" chips for a single red label; one badge per card.
- Raise secondary text to 12 px at 4.5:1.
- Default the Person filter to the signed-in user, or to their team.
