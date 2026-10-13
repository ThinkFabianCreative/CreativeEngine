# v1 acceptance checks

Each item is done when every check passes on real Hub data.

## 1. Board view

- [ ] "Board" appears as a view next to Weekly, Day view and Flow & capacity
- [ ] Eight columns in order: Intake, Ready, In progress, Internal review, Quality Control, With client, Feedback, Done
- [ ] Each open task appears exactly once, in the column of its current step
- [ ] Team, Person and Client filters work, plus Mine / My team / Everyone
- [ ] Cards show only: title, client, assignee, and at most one status badge
- [ ] Clicking a card opens the existing task detail
- [ ] Task detail has a "Move to" control (the non-drag alternative)
- [ ] Usable by keyboard: Tab to a card, Enter opens it, Escape closes it

## 2. One owner per role

- [ ] Account lead accepts exactly one person; pairs like "Darcey/Brad/Ky" are gone from the picker
- [ ] An optional "Account team" field holds anyone else
- [ ] New "Creative lead" field
- [ ] New "Reviewer" field; the person assigned to the work can't be chosen as reviewer
- [ ] Existing tasks are migrated: the first name in each pair becomes the account lead, the rest go into the team (confirm the mapping with Darcey)

## 3. Quality Control checklist

- [ ] "Pre-launch QA" is renamed "Quality Control"
- [ ] It shows five yes/no questions: brief, brand, delivered as asked, mistakes, presentation ready
- [ ] Each answer records who answered and when
- [ ] "Send / present" can't start until all five are Yes
- [ ] A No can be overridden only by an ACD, with a reason, and the override is logged

## 4. Blockers

- [ ] Setting a step to Blocked requires a reason and an owner (a person or "Client")
- [ ] The "since" date is set automatically
- [ ] Blocked tasks appear in a lane at the top of the board, showing reason, owner and since
- [ ] Clearing the blocker returns the task to its column

## 5. Brief link

- [ ] Every task has a brief link field
- [ ] The first work step can't go Active without it (Full-track work), or shows a warning during the pilot

## Pilot mode

- [ ] Rules 2–5 can run as warnings with a logged override for the first 6 weeks, then be switched to hard blocks
