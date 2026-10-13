# Culture reset playbook

## Identity

```
CLIENT:           Traffik
PROJECT:          Culture reset playbook (The Standard, The Craft)
FOLDER:           projects/traffik/culture-reset-playbook/
IDENTITY SOURCE:  Andres Fabian, filed as a Traffik project, 2026-10-12
BRIEF:            NOT YET NORMALIZED. The working record is work/strategy/decisions.md
```

## Scope *(summary)*

Reset how Traffik's creative department and account team work together, and raise the standard of the design team's work. It changes the workflow (briefs, gates, review, QC, dates, stand-ups), not only the deliverables.

Pilot in Andres's group first. Accounts and PM rules are co-owned with Darcey O'Byrne; shared rules (QC, working hours, presentation) are offered to Jeremy Troutt's group.

## Audiences

- **The Standard:** Accounts, PMs and leadership.
- **The Craft:** the design team (week 1 designer reset session).

## Deliverables

| File | What it is | Status |
|---|---|---|
| `outputs/review/The_Standard_v0.2.pptx` | 10 presented slides plus an appendix | Draft for review |
| `outputs/review/The_Craft_v0.2.pptx` | 12 presented slides plus an appendix | Draft for review |
| `outputs/review/The_Standard_v0.1.pptx` · `The_Craft_v0.1.pptx` | Full masters the v0.2 decks are cut from | Working masters |

Rebuild: `python3 work/design/deck-build/build.py`, then `build_craft.py`, then `shorten.py`. Type is Libre Caslon (display) and Acumin Pro (text); Acumin Pro needs Adobe Fonts, so it falls back in Google Slides.

## Working files

| Location | Holds |
|---|---|
| `work/strategy/decisions.md` | Diagnosis, every decision made, open questions |
| `work/design/deck-build/` | Deck build scripts |

## Related

- [Task Hub board](../task-hub-board/README.md): the tool changes this workflow depends on.
- [Team and stakeholders](../client/knowledge/team.md).
- Andres's standing rules: [`WORKING-PREFERENCES.md`](../../../WORKING-PREFERENCES.md).

## Ownership and approvals

| Responsibility | Person |
|---|---|
| Owner | Andres Fabian, Creative Director |
| Accounts and PM rules | Andres + Darcey O'Byrne |
| RFPs, rates, new business | Brent Shoji |
| Final awareness | Anthony Trimino (after month 3) |
