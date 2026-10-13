# Task Hub board: handoff for Leo

From Andres Fabian, Creative Director · October 12, 2026

Leo, this is everything for the board and workflow changes we want in the Task Hub. The prototype shows the behavior; the notes explain what to build and in what order. It isn't production code, so please build it in the Hub your way, on your data.

## Start here

| Order | File | Why |
|---|---|---|
| 1 | `taskhub-v1-spec.md` | **What we need first (month 1).** One page, five items |
| 2 | `taskhub-board-prototype.html` | Open it in Chrome and click around. Notes for each item are in `IMPLEMENTATION.md` |
| 3 | `IMPLEMENTATION.md` | How the prototype works: data model, rules, views, and where each one lives in the code |
| 4 | `ACCEPTANCE.md` | How we'll check each v1 item is done |
| 5 | `taskhub-board-spec.md` | The full picture, including what comes in months 2–3. Reference only |

## Running the prototype

It's a single HTML file. Open it in Chrome (double-click, or `open -a "Google Chrome" taskhub-board-prototype.html`). It needs internet for the font (Instrument Sans) and icons (Feather). Nothing is saved: a reload resets it.

## Scope of v1

1. A **Board** view by stage
2. **One owner per role:** account lead, creative lead, reviewer
3. A **Quality Control** checklist with five yes/no questions
4. **Blockers** with a reason and an owner
5. A **brief link** field

Everything else in the prototype (List, Calendar, Workload, Leadership, Completed, stand-up mode, nudges, the new intake form, time logging) is for later. It's in the prototype so you can see where we're heading, not because it's needed now.

## What we need back from you

1. Can the board read each task's current step from existing data?
2. A rough effort estimate for each v1 item.
3. Anything in the prototype that fights how the Hub is built. Tell us, and we'll adjust the spec rather than force it.

## Data note

The Completed view embeds the Hub's own task export (Apr 28 – Oct 9 2026), and the sample cards use real names and clients. Treat the file as internal.
