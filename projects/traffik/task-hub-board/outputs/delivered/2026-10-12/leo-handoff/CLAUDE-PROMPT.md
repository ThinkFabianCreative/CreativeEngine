# Prompt for Claude (Leo's builder)

Copy everything below the line into Claude Code (or your Claude builder) from the root of the Task Hub codebase. Put this handoff folder somewhere Claude can read it, and replace `<path-to-leo-handoff>` with that location.

---

You're helping me implement v1 of a set of changes to our in-house Task Hub (Traffik's project and resourcing tool). The creative director, Andres, has supplied a clickable prototype and specs. Your job is to build the v1 scope **inside our existing app, on our real data**, following its current architecture. Don't port the prototype's code.

## Read first, in this order

1. `<path-to-leo-handoff>/README.md`: overview and scope
2. `<path-to-leo-handoff>/taskhub-v1-spec.md`: **the scope you're building**
3. `<path-to-leo-handoff>/ACCEPTANCE.md`: the checks that define "done"
4. `<path-to-leo-handoff>/IMPLEMENTATION.md`: how the prototype models data, rules and views, and how they map to our app
5. `<path-to-leo-handoff>/ux-audit_hot-sheet-weekly_2026-10-14.md`: why each change matters
6. `<path-to-leo-handoff>/taskhub-board-prototype.html`: the reference for behavior and look (open it in a browser; read the code only to understand behavior)

`taskhub-board-spec.md` is the full long-term spec. Use it for context only: **nothing outside v1 is in scope.**

## Then, before writing any code

1. Explore our codebase and summarize how it currently models tasks, plan steps, step statuses (including Blocked), account managers, assignees, and the Hot Sheet views (Weekly, Day view, Calendar, Status).
2. Tell me whether the existing **Status** view is already a board by stage, and whether we should extend it or add a new Board view.
3. Propose a plan for the v1 items, in the order below, listing every schema change, migration and file you'll touch.
4. List anything in the specs that conflicts with how the app is built, with a suggested adjustment.

**Wait for my approval of the plan before changing anything.**

## v1 scope, in build order

0. **Side navigation (must-have).** A persistent left sidebar on every page: For you · Hot Sheet · Resourcing · Department · Clients (each client filters every view; "All clients" first). It collapses to a 64 px icon rail with a remembered toggle; narrow screens show the rail and never hide it. Tooltips and accessible names in rail mode.
1. **Board view.** Eight columns by each task's **current plan step**: Intake, Ready, In progress, Internal review, Quality Control, With client, Feedback, Done (step mapping in IMPLEMENTATION.md §2; confirm it against our step library). One card per task. Mine / My team / Everyone scope plus the existing Team, Person and Client filters. Cards show title, client, assignee avatar and **one** status badge. Clicking a card opens the existing task detail, which gets a "Move to" control.
2. **One owner per role.** The account lead is a single person (replace the shared pairs like "Darcey/Brad/Ky"), plus an optional Account team field. New fields: creative lead, and reviewer (can't be anyone assigned to the work).
3. **Quality Control checklist.** Rename "Pre-launch QA" to "Quality Control". Five yes/no questions (brief, brand, delivered as asked, mistakes, presentation ready), each storing who answered and when. "Send / present" can't start until all five are Yes; an ACD override needs a reason and is logged.
4. **Blockers with a reason.** Setting a step to Blocked requires a reason and an owner (a person or "Client"); "since" is stamped automatically. Blocked tasks show in a lane at the top of the board.
5. **Brief link.** A field on the task, required before the first work step goes active on Full-track work.

## Constraints

- **Don't break existing views or data.** Weekly, Day view, Calendar, Resourcing and Every task must keep working.
- **Migrations are reversible.** Back up before migrating. For account managers, migrate the first name in each existing pair to account lead and the rest to Account team, and **show me the mapping before running it.**
- **Rules start as warnings with a logged override** (a 6-week pilot), behind a single switch, so they can become hard blocks later.
- **Accessibility:** cards are keyboard-focusable and open with Enter; Escape closes the detail and returns focus; "Move to" is the non-drag alternative; visible focus rings; respect reduced motion; secondary text at least 12 px at 4.5:1 contrast.
- **Visual rules:** one variable font family with tabular figures; Feather icons at 16 px; red (#C8202F) only for problems (blocked, overdue) and the primary action; flat status labels (blue in progress, purple review/QC, yellow with client, green done, grey intake/ready); no emoji as icons. Tokens are in IMPLEMENTATION.md §6.
- **Out of scope for now:** time logging, dates from standard times, Light/Full track logic, rounds and change orders, WIP warnings, List, Leadership and Completed views, stand-up mode, the new intake form. Don't build them, even partially.
- Don't copy the prototype's sample data, plan templates or the embedded task export.

## Work in small steps

Build one v1 item at a time. After each:
- Show me what changed.
- Run the relevant ACCEPTANCE.md checks and report pass/fail.
- Wait for my go-ahead before the next item.

Ask me rather than guess about anything the specs don't settle.
