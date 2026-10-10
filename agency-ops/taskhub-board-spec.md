# Task Hub: Board view spec (draft for Leo)

From: Andres Fabian, Creative Director · Draft v0.1, Oct 2026
Prototype: `taskhub-board-prototype.html` (open it in a browser; drag the cards around)

## Why

Designers and PMs have no single view of daily and weekly workload. Dates are set by asking designers "when will this be done?", nobody logs hours, and the capacity view shows the agency at 10% booked. Blockers and QC waits are invisible, so all delay reads as Creative delay.

## 1. Columns

The columns map to the statuses that already exist (New, Active, Ready for Review, Sent to Client, Round 1 Edits, On Hold, Complete).

| Column | Entry rule (enforced) | Owner |
|---|---|---|
| Intake | Request logged | PM |
| Ready | Signed brief linked, change log, due date from standard time, due-date driver filled | PM + Accounts |
| In progress | Assigned designer. WIP limit: 3 cards per person | Designer |
| Internal review | Reviewer is not the maker | ACD / CD |
| QC | Five-section QC gate | QC owner + Accounts |
| With client | QC passed | Accounts |
| Feedback | Client notes entered as numbered tasks; round number increments | PM + Accounts |
| Done | QC passed, delivered | PM |

**Blocked** is a lane across all columns, not a status. It requires a reason, an owner (person or "Client") and a since date.

## 2. New ticket fields

- Account lead: one person, not "Darcey/Brad/Ky"
- Creative lead (ACD/CD) and QC owner
- Brief link (required to leave Intake)
- Gate and round, e.g. "G3 · Round 1 of 2"
- Due-date driver (required; there's no locked date without one)
- Standard time (picked from the existing 593 standard times: simple, standard or complex)
- Hours logged: daily, rounded to 0.5h, by category: new work, rework, QC, waiting
- QC gate: five yes/no sections with a signer per section (brief, brand, delivered as asked, mistakes, presentation)

## 3. Rules the tool enforces

1. A card can't leave Intake without a brief link.
2. A person can't have more than 3 cards In progress.
3. A card can't move to With client or Done unless QC passed.
4. The Internal review signer can't be the card's assignee.
5. The due date defaults to start date + standard time + client review days (3, or 5 for medical/regulated). A PM can override it, but the override needs a reason.
6. Moving to Feedback increments the round. Going past the contracted rounds flags the card as "change order".

## 4. Views

- **Daily board:** filter by person. Used in the daily PM check-in. Blocked and over-WIP cards are shown first.
- **Weekly load:** each person's open cards × standard time (logged hours once they exist) against 35h capacity. Over 85% shows amber, over 100% red.
- **Leadership:** card counts per column. A pile-up in Internal review, QC, With client or Feedback shows where the time actually goes.

## 5. Also extend

- Include Account, PM, QA/QC and Strategy in the capacity grid (they're excluded today).
- Add QA/QC standard times. There are only 2 today.

## Open questions for Leo

- Effort and order: suggested order is fields → board → rules → weekly view.
- Can the existing status values be mapped onto these columns without breaking history?
