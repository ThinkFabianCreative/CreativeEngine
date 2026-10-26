# Task Hub board

## Identity

```
CLIENT:           Traffik
PROJECT:          Task Hub board (changes to the internal Task Hub tool)
FOLDER:           projects/traffik/task-hub-board/
IDENTITY SOURCE:  Andres Fabian, filed as a Traffik project, 2026-10-12
BRIEF:            NOT YET NORMALIZED. The specs below carry the requirements
```

## Scope *(summary)*

Proposed updates to Traffik's in-house Task Hub (built and maintained by Leo M) so the culture-reset workflow can run on it. The changes are a stage board (kanban), one owner per role, a Quality Control checklist, blockers with reasons, brief links, then time logging, dates from standard times and lighter screens.

This is a hi-fi prototype and a spec for Leo, not production code.

## Deliverables

| File | What it is |
|---|---|
| `work/interaction/taskhub-v1-spec.md` | One-page month-1 scope for Leo: start here |
| `work/interaction/taskhub-board-spec.md` | Full spec v0.8, and the "later" list |
| `work/interaction/taskhub-board-prototype.html` | Clickable prototype (open in Chrome): Board with stand-up mode, List, Calendar, Workload, Leadership, Completed |

The prototype's Completed view embeds Traffik's own Task Hub export (Apr 28 – Oct 9 2026). It names Traffik's clients, so treat the file as internal and don't publish it.

## Delivered

| Date | To | What |
|---|---|---|
| 2026-10-12 | Leo M | `outputs/delivered/2026-10-12/leo-handoff/`: prototype, v1 and full specs, implementation notes, acceptance checks. A zip of it sits beside the folder (local only, not in git) |
| 2026-10-20 | Leo M (ready, not sent) | `outputs/delivered/2026-10-20/leo-v2-feedback/`: feedback on his mockup v2. Read-first decisions, marked-up mockup + PDF, acceptance checks in three batches, Claude prompt. Zip beside it (local only); message draft in `message-to-leo.md` |

## Related

- [Culture reset playbook](../culture-reset-playbook/README.md): the workflow these changes support.
- Live Task Hub (requires sign-in): https://taskhub-resourcing-demo.pages.dev/

## Ownership

| Responsibility | Person |
|---|---|
| Requirements | Andres Fabian |
| Build | Leo M |
| Daily users | PMs (Mikayla, Dee, Jeff) and the design team |
