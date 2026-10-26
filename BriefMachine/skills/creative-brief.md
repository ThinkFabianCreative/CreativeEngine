# creative-brief

| | |
|---|---|
| Source | In-house, built 2026-10-26 |
| Owner | BriefMachine |
| Status | Built at the user's request 2026-10-26 ("we need agents in our system to do this as a loop") |
| Installed | `.claude/skills/creative-brief/` |
| Scope | Write, review and render TRAFFIK creative briefs through a loop: brief-machine writes; creative-engine-director runs the strategy gate and USP tests; word-smither and design-champ run the show test; max three rounds, then the user decides |

## Contents

- `SKILL.md`: the loop and modes.
- `assets/creative-brief-template.md`, `assets/judging-card.md`: copies of `projects/traffik/templates/`. When the template changes there, update these copies.
- `scripts/brief2docx.py`: renders the red TRAFFIK .docx. Needs `python-docx`, installed in a scratchpad virtualenv. Reads and writes local files only; no network, no credentials.

## Use

- The thinking is in `shared/frameworks/brand-strategy.md` (§6a USP, §7 brief) and `creative-effectiveness.md`. The skill must not grow its own version of them.
- The show test is not EXPLORE. Agents judge whether the brief gives them material; they don't produce concepts.
- Test 4 (true and provable) stays with the client. The loop never clears a ⚑.
