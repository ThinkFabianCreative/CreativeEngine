# Task Hub: Stage board and quality rules (spec for Leo)

From: Andres Fabian, Creative Director · Draft v0.8, Oct 10 2026
Prototype: `taskhub-board-prototype.html` (open it in a browser and drag the cards)

## Summary

The Task Hub already has the hard parts: plans built from steps, planned hours from standard times, delivery dates, free hours per person, a Blocked step status, a time-logged field and the Hot Sheet views. This spec builds on those. It asks for four things:

1. A **stage board**: the same tasks, grouped by the step they're on instead of by date.
2. **Three existing steps turned into rules**: Internal review, Pre-launch QA, Send / present.
3. **A few fields made required**: one owner per role and the due-date driver.
4. **Time logging people actually use**, so capacity stops reading 35h free for everyone.

Nothing here replaces existing views or data.

## What the prototype demonstrates

Open `taskhub-board-prototype.html`. The tabs are Board, Weekly load, Leadership and Completed, plus **+ New Task**.

| Spec item | In the prototype |
|---|---|
| Stage board as a Hot Sheet view, with person and client filters | Board tab, with columns mapped to existing steps |
| Blocked lane: reason, owner, date | "Block" on any card asks for a reason and owner; "Clear" removes it |
| WIP limit 3 (warning) | A warning when a 4th card goes In progress; "Over WIP" counter |
| One account lead, creative lead, reviewer | Shown on every card; "none" in red when missing |
| Maker is never checker | Can't move to Internal review if the reviewer is the assignee |
| Quality Control checklist | "QC checklist" on cards in Quality Control: 5 yes/no questions with signers, and an ACD override needing a reason |
| Send / present only after QC | Can't move to With client or Done without QC passed |
| Rounds and change orders | Moving into Feedback adds a round; past the contracted rounds it's flagged "Change order" |
| Plan before date | "Promised before plan" tag and counter when the promised date is earlier than the plan's delivery date |
| HIGH needs a reason | The reason shows on hover over the HIGH tag |
| Time logging | "+0.5h" on each card; Weekly load shows planned vs. logged, and "nothing logged" in red |
| Reworked intake form | + New Task requires a title, client, one account lead, creative lead, assignee and a standard timeline; a driver if a date is requested; a reason if HIGH. A brief link puts the task in Ready, otherwise Intake |
| Ticket detail (click a card) | A side panel showing the parent ticket, the plan (current step highlighted, RULE steps marked), roles, dates vs. plan vs. driver, the QC status, blockers and other tasks on the same parent |
| Parent ticket | Click the parent name: all its tasks grouped by stage, with overdue, blocked and hours totals |
| Completed view | Real export data, Apr 28 – Oct 9 2026, by client and department |

## What exists today (as seen in the hub-fork build)

| Feature | Status |
|---|---|
| Plans with steps (e.g. Digital, social & video ads, 12 steps) | ✅ Exists |
| Step names: Internal review, Send / present, Client feedback R1, Revisions R1, Client final approval, Exports & spec check, Pre-launch QA, Campaign launch | ✅ Exists |
| Planned hours per step, from standard times | ✅ Exists |
| "Delivers" vs "promised" date per plan | ✅ Exists |
| Step status: New / Active / Complete / Blocked | ✅ Exists |
| Free hours per person when assigning | ✅ Exists, but based on 0 logged hours |
| Time logged per task and step | ✅ Field exists, unused (0h) |
| Due-date driver field | ✅ Field exists, empty |
| Hot Sheet: Weekly, Day view, Flow & capacity | ✅ Exists |
| Agency counters: overdue, needs a date, on hold, due on the weekend | ✅ Exists |
| View by stage (where work is waiting) | ❌ Missing |
| Rules on review, QC and send steps | ❌ Missing (steps are optional) |
| One named owner per role | ❌ Shared ("Darcey/Brad/Ky", "Amanda/Hunter") |
| Brief link and QC checklist on the task | ❌ Missing |
| Completed-work history with on-time and rework rates | ❌ Missing |

## 1. Stage board (new view)

Add **Board** as a fourth Hot Sheet view (next to Weekly, Day view, Flow & capacity), with the same Team, Person and Client filters.

Each task appears once, in the column of its **current step**. Columns group the existing step names:

| Column | Existing steps that map here |
|---|---|
| Intake | Task in the queue, no plan yet, or "Needs a date" |
| Ready | Plan exists, first step not started |
| In progress | Any work step that is Active (design, copy, build, edits, revisions) |
| Internal review | "Internal review", "Internal check-in", "Due for internal" |
| Quality Control | "Pre-launch QA", "Exports & spec check" |
| With client | "Send / present", "Present to client", "R1/R2 due" (sent) |
| Feedback | "Client feedback R1/R2", "Revisions R1/R2" |
| Done | "Client final approval", "Campaign launch", or task Complete |

Leo knows the full step library, so the mapping above should be checked and completed against it.

**Blocked** is a lane across the top, showing any task with a Blocked step. Each one shows its reason, an owner (a person, or "Client") and the date it was blocked. All three are required when setting Blocked.

**Clicking a card** opens the task's existing detail view as a side panel, so the board stays visible. It adds:
- A breadcrumb to the **parent ticket** (job #, parent name). Clicking it opens the parent with all its tasks **grouped by stage**.
- The **plan's steps**, with the current step highlighted and the three rule steps marked.
- Plan date vs. promised date vs. due-date driver, side by side.
- Roles: account lead, PM, creative lead, reviewer, assignee, QC owner. Missing ones are shown in red.
- The QC checklist status, the blocker (if any), and the **other tasks on the same parent**, each opening in place.

**WIP limit:** flag anyone with more than 3 Active work steps at once. Show it as a warning, not a hard block, to start.

## 2. Three steps become rules

| Step | Rule |
|---|---|
| **Internal review** | Required in every creative plan. It must have an assigned reviewer, and **the reviewer can't be anyone assigned to the work steps** (maker is never checker). |
| **Pre-launch QA** (rename to **Quality Control**) | Required before Send / present. Opens a five-section yes/no checklist (below). The step can't be marked Complete until every answer is Yes, or the ACD records an override with a reason. |
| **Send / present** | Can't start until Quality Control is complete. For G1 and G2 work, the assignee must be an ACD or CD (creative is presented, not just sent). |

**Quality Control checklist** (stored on the task, with who answered and when):

1. **Meets the brief?** Answers the proposition, speaks to the one person, right fidelity. *Signed by: Account lead + ACD*
2. **On brand?** Logo, colors, type, imagery, tone, licenses. *Signed by: AD on the job*
3. **Delivers what was asked?** Every change-log item done, nothing extra changed, all sizes and specs. *Signed by: QC owner*
4. **Any mistakes?** Claims and numbers confirmed with the client in writing *(Account lead)*; spelling, names, links, CTAs, legal lines *(QC owner)*
5. **Presentation ready?** Agency format, decisions needed, round count shown. *Signed by: ACD*

## 3. Fields

| Field | Change |
|---|---|
| Account lead | **One person**, required. Others can be added as "Account team" |
| Creative lead | New field: the ACD or CD accountable for the work. Required on creative tasks |
| QC owner | New field. Defaults to the QC team (Judy, Katie) |
| Brief link | New field. Required before the first work step goes Active |
| Due-date driver | Existing field, **made required** before a date can be locked (printer, launch, media start, client event) |
| Requested by | Should be the client contact or account lead, not the PM by default |
| Round | Shown on the task: "Round 1 of 2". Entering Feedback past the contracted rounds flags the task as **Change order** |

## 3b. Intake form (New task): what drives the gaps

What we saw in the New task form:
- **Account manager** is a dropdown of fixed *pairs and trios* (Amanda/Hunter, Darcey/Brad/Ky, Savannah/Leo). The shared ownership is built into the form. Change it to a single-person picker plus an optional "Account team".
- **Requested due date is required, and Standard timeline is optional.** The requester sets the date before any plan exists. Reverse this: make the timeline required for creative work, and show the requested date next to the plan's "delivers" date.
- **"Info / meeting driving due date" is optional.** Make it required whenever the requested date is earlier than the plan.
- **"High priority = needed today/tomorrow AM"** is a yes/no anyone can tick (17% of completed tasks). Require a reason and the account lead's name.
- **A "Creative Brief" template exists.** Make it the default for creative requests, and add a required brief-link field.
- **No step for the creative brief or Concept Card** in campaign timelines. Add one to "Campaign concepts", "Integrated campaign", "Brand identity" and "GTM plan & creative brief".

## 4. Time logging

- **A daily prompt:** "Log today's hours", grouped by the steps you're assigned to, with a 0.5h step. Pre-filled from planned hours, so most days it's one click to confirm.
- **Categories:** new work, rework (Feedback or Revisions steps), QC, waiting or blocked.
- **Free hours, planned vs. logged, and the capacity grid then use real data.**
- **Extend the capacity grid** to Account, PM, Strategy and QA/QC. These roles are outside it today, so only Creative and Digital look either slow or idle.

## 5. Completed view (new)

A history of finished work, filterable by client, department and person. Per client:
- The on-time rate against the **original** promised date
- Median days late
- Rework share
- The share of tasks requested with ≤1 day of turnaround
- The HIGH share
- Planned vs. logged hours (once logging is live)
- Rounds used vs. contracted

The prototype's Completed view already runs on the Task Hub's own CSV export from Oct 10.

## 6. Dates

- The **default date** is the plan's own "delivers" date (start + planned steps + client review time: 3 business days, or 5 for medical or regulated work). Asking a designer "when will this be done?" is no longer the source of dates.
- A PM can override the date, but has to give a reason. A date earlier than the plan's appears as **"Promised earlier than planned"** on the task and on the board.
- **Weekends:** steps can't be scheduled on a Saturday or Sunday without a CD-approved exception. This builds on the existing "Due on the weekend" counter.
- **Standard times:** add QA/QC standard times (only 2 exist today), and review the time for "Concept & big idea" with Creative.

## 7. Behavioral design principles

Source: Jakob Nielsen, "Behavioral Economics & UX: Design for Irrational Humans" (Oct 7 2026), 50 numbered guidelines. The numbers below refer to his list. Applied where they change how people use the board:

| Guideline | Applied as |
|---|---|
| #1 Summarize before detailing · #11 Curate a shortlist | A "Start here" strip above the board: the top 3 items needing attention (blocked, waiting on QC or review, no brief), one per task. With a person selected it becomes "Their next 3" |
| #7 Reduce competing signals | 4 counters by default (Open, Blocked, Waiting on review/QC, Promised before plan); "More counts" reveals the rest |
| #2 Defensible recommendations · #4 Safe paths | Every rule that blocks a move offers the fix in one click ("Assign Jeremy as reviewer", "Add brief link", "Open QC checklist") |
| #9 Spend reminders like money | The WIP warning fires once per person per session, not on every move |
| #5 Make automation reviewable | Every plan date explains how it was calculated (timeline, business days, review days, regulated-client days) |
| #16–#18 Anchor with defensible benchmarks · show ranges | New Task shows the plan date first, with a likely range, before any requested date. Hours show a likely range in the ticket |
| #26 Show final states alongside changes | A requested date earlier than the plan shows the consequence before submitting. Starting a round past the contract shows "change order" before confirming |
| #22 Publish base rates · #35 Pick the honest frame | The HIGH choice shows the real base rate from the Hub's own data: 17% of completed tasks were HIGH; HIGH finished on time 49% vs 43% for normal |
| #44 Active choice | Priority has no default: Normal or HIGH must be chosen; HIGH requires a reason |
| #8 Design for interruption · #36 Preserve what users built | The New Task form autosaves a draft and restores it; Cancel keeps the draft |
| #46 Shrink the immediate cost · #47 Bring some benefit forward | "Confirm today" logs a day's hours in one click, pre-filled from the plan |
| #28 Losses weigh about twice gains (honest frame) | The weekly view states plainly that unlogged hours don't count when workload and staffing are decided |
| #48 Break distant goals into near-term steps | The parent ticket shows a progress bar, tasks done of total, and the next milestone |

Not used, on purpose: urgency tricks, streaks, or guilt messages. Per the article's ethics section, nudges here only make the honest path the easy one.

## 8. Visual system (for the new views)

**Update v0.6: Jira look and feel, remixed with the Traffik brand.**
- **Layout:**
  - Left sidebar: For you, Resourcing, the Creative department, and clients as spaces that filter the views.
  - Top bar: search, a red Create button, the user avatar.
  - A space header with breadcrumb and title.
  - Underline tabs: Board, List, Calendar, Workload, Leadership, Completed.
  - A toolbar with an avatar stack that filters by person.
- **Views added:**
  - **List:** a sortable table with search and group-by (client, stage, assignee, account lead).
  - **Calendar:** a Monday–Friday month view; bars run from planned start to promised date and are color-coded by stage.
- **Atlassian-style details:**
  - Flat uppercase status labels: blue in progress, purple review/QC, yellow with client, green done, red blocked or overdue.
  - Cards with Jira's subtle shadow.
  - Grey secondary buttons.
- **Brand:** Traffik red replaces Jira blue for Create, selected tabs and the selected nav item.

The token list below still applies, apart from these overrides.

**Update v0.7: scannability.**
- **Icons:** Feather icons throughout, at 16px with a 1.75 stroke.
- **Column headers:** each stage has its own icon, and the column rules move into a tooltip on the header.
- **One summary row of chips:** open · need someone · blocked · promised before plan.
  - "Need someone" and "blocked" expand on click.
  - The "Next up" list and the Blocked lane are collapsed by default.
- **Cards show four things:**
  - Title.
  - Client and round.
  - Assignee.
  - One status badge.
  - Icons appear only for a problem (no brief) or a pass (QC done).
  - Hours live in the task panel.
- **List:** 5 columns by default (Task, Client, Assignee, Stage, Promised); "More columns" adds the rest.
- **Scope switch:** Mine / My team / Everyone, defaulting to My team.

A shadcn/ui design language in plain HTML/CSS, so it works in a vanilla build:
- **Tokens:** zinc neutrals (background #fafafa, card #fff, border #e4e4e7, muted #f4f4f5, muted text #71717a), 8px radius, 1px borders, light shadows only on cards and overlays.
- **Identity:** the Traffik dark header (#1d1d1d) and red (#c8202f), used only for the header, the New Task button and real problems (blocked, overdue). Red is not decoration.
- **Type:** Instrument Sans, one variable family (weight 400–700, width 75–100%). Condensed width for headings, column labels and numbers; normal width for text; tabular figures for hours and dates. No monospace.
- **Components:** Tabs (view switcher), Card (task), Badge (one status per card, most important first), Button (primary, outline), Sheet (task detail, right side), Dialog (QC checklist, New Task), Toast (bottom right, with an action).
- **Icons:** inline SVG (Lucide shapes), never emoji or text symbols.
- **Accessibility:** cards are focusable and open with Enter; Escape closes the sheet and dialogs; focus returns to the card; visible focus rings; a "Move to" control in the sheet as the non-drag alternative (WCAG 2.2 dragging movements); reduced motion respected.

## 9. What the Hub should stop showing

The Hub shows nearly everything it knows at once, and some of it isn't reliable. Seen in the hub-fork build on Oct 10 2026:

| Screen | What it shows today | Change |
|---|---|---|
| **Home** | Every open task, with about 12 details per row (job #, status, overdue flag, type, account pair, people, subtask progress, "Your subtasks" list, PM, due date, counter), all at the same visual weight | Lead with exceptions (blocked, overdue, waiting on someone). Rows show title, client, owner, one status, due date. The rest goes in the task panel |
| **Home counters** | Total open, Active, In the queue, On hold, Overdue, Due this week, plus the out-of-office strip | One summary row. Hide counters at zero. Show out-of-office only for people on the current scope |
| **Hot Sheet** | Five alert chips plus every deadline and step per day; Flow lists 71 assignments | Default to the user's scope (Mine / My team). Collapse steps under their task. Keep the alert chips and drop the duplicate counts |
| **Task detail** | A 12-step plan where every step repeats the full list of ~30 people with "35h free" | Assign people once at task level; steps inherit them, with a per-step override. Show the people list only when "Assign" is clicked, filtered to the task's team |
| **Resourcing** | Four big stats plus a 20 people × 6 weeks heatmap with numbers in every cell | Hide free hours, % booked and the heatmap numbers until time logging has run 4–6 weeks, or label them "Estimate (no hours logged)". Colour only, numbers on hover |
| **Every task** | 13 columns × 710 rows | Default to 5 columns and open tasks only. Finished tasks go in the Completed view, with rates instead of rows |
| **New task** | About 25 fields, plus four people checklists (Digital, Creative, Account, Assign team members) | A template plus about 8 required fields (title, client, account lead, creative lead, assignee, brief link, timeline, priority). "Quick capture" (already in the Hub) for everything else. One people picker, not four lists |

**Principles**
1. **Exceptions first.** Lead with what's blocked, overdue or waiting on someone. Everything else is one click away.
2. **Scope by role.** Designers default to Mine, PMs and creative leads to My team, leadership to Everyone with stage totals.
3. **One main number per view.** Hide zero counters.
4. **Progressive disclosure.** Subtasks, plan steps and extra columns stay collapsed until asked for.
5. **No metric before its data is real.** A number built on 0 logged hours is false precision, and it misleads staffing decisions. Hide it or label it as an estimate.
6. **Enter once.** People are assigned at task level; dates come from the plan; templates pre-fill the rest.
7. **One visual system.** The Hub mixes several fonts and a monospace. Use one variable family (Instrument Sans in the prototype) and the tokens in §8.

## Suggested build order

1. Required fields: one account lead, creative lead, QC owner, due-date driver, brief link
2. The stage board view, read-only
3. The rules on the three steps, plus the QC checklist
4. The daily time-log prompt
5. The Completed view
6. Date defaults and the weekend rule

## Questions for Leo

1. Is there a single step library, so the board mapping can live in one place?
2. Can existing plans be backfilled with Internal review and Quality Control steps without breaking history?
3. Should the rules be hard blocks or warnings during a 6-week pilot? Our suggestion is warnings first, with overrides logged, then hard blocks.
4. Effort estimate per item above.
