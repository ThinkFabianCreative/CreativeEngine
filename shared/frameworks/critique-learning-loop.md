# Critique Learning Loop

> CreativeEngine shared framework. Owner `creative-engine-director`. Used by `design-champ` and `word-smither` when they receive or give critique on rendered work, and by any role proposing a reusable rule.

## Provenance

Mined on 2026-11-17 from an outside "Art Teacher" agent package supplied by the user (`CREATIVE_ENGINE_ART_TEACHER_LEARNING_LOOP.zip`, files `art-teacher.md`, `agent-learning-loop.md`, `critique-rubric.md`). The package was not installed: its proposed agent duplicated existing roles, routed work to agents CreativeEngine does not have, and imposed a fixed house style. Only its critique-to-lesson method is kept here, rewritten for CreativeEngine's roles and verdicts.

## Purpose

Critique fixes one piece of work. This framework covers what happens next: how a fix is checked, and how a fix that keeps recurring becomes a reusable rule, without anyone claiming the department "learned" something it only wrote down.

```
DID THE FIX ACTUALLY FIX THE DEFECT, ON THE RENDERED WORK?
DID IT BREAK ANYTHING ELSE?
HAS THIS LESSON EARNED A PLACE IN SHARED METHOD, OR IS IT ONE JOB'S TASTE?
```

## What this framework does not cover

| Judgment | Where it lives |
|---|---|
| Whether the idea is good; verdicts | `CreativeDirector/AGENT.md`, `creative-direction-audit.md`, `creative-effectiveness.md` |
| Visual, type and deck craft criteria | `visual-craft.md`, `typography.md`, `editorial-presentation.md` |
| Copy craft criteria | `hey-whipple-copycraft.md` |
| How ideas improved across rounds | `creative-trajectory-evaluation.md` |
| Client-specific preferences | `projects/<client>/client/` (never promoted to shared method) |

## 1. The loop

Runs in DEVELOP and JUDGE on rendered work. Never in EXPLORE.

| Step | What happens | Who |
|---|---|---|
| **Diagnose** | Name observable defects in the actual render: what is visibly there, not what is imagined | Critic (usually `creative-engine-director`; any role may critique) |
| **Teach** | For each consequential defect: the principle it breaks, why it matters for this piece's job, a one-line before/after rule | Critic |
| **Prescribe** | At most three prioritized, testable changes, each addressed to the role that owns it. Preserve the idea | Critic |
| **Practice** | The owning role makes the revised version and states what changed | `design-champ` / `word-smither` |
| **Compare** | Look at v1 and v2 side by side. Did the target defect improve? Did anything regress? If the render can't be seen, mark it pending, never passed | Critic |
| **Calibrate** | Andres accepts, rejects or revises each lesson, with a reason | User |
| **Codify** | Only a lesson with repeat evidence or explicit approval becomes a candidate rule (§4) | Owner of the target framework |
| **Regression test** | Run the candidate rule against at least three different past pieces, including one where the rule should not apply | Owner of the target framework |

**Stop conditions.** Two iterations per issue by default. Stop on no measurable improvement, a regression, no visual access, a brand conflict or a human rejection, and escalate. No endless self-critique, no two roles approving each other in circles.

## 2. Severity

| Severity | Means |
|---|---|
| **Critical** | Factual or claim error, rights problem, illegible, distorted or wrong asset |
| **Major** | Communication or hierarchy broken; the idea doesn't land |
| **Minor** | Polish |

A craft score never outranks a critical defect. Record each dimension as `pass`, `needs revision` or `not verifiable`; no invented numeric scores.

## 3. Critique record

One record per issue, kept with the project's work (`projects/<client>/<project>/work/`), not in shared files.

```
artifact / version / owner role
issue / severity / visible evidence / principle / why it matters
correction / acceptance test (what we'd see if fixed)
reference (or "none") / confidence / verification status
after revision: before-after observation / regressions / Andres's decision / lesson candidate (yes/no)
```

## 4. Promoting a lesson

- A lesson starts as a **candidate** in the project record.
- It becomes shared method only when: it recurred on independent work, or Andres explicitly approves; it passed the regression test including a counterexample; and it is stated no more broadly than its evidence.
- It is written into the most specific existing framework or skill record as a proposed edit, reviewed in a diff. Never into memory alone, never as a silent change to an `AGENT.md`, never mid-deliverable without approval.
- Lessons drawn from one client's work stay client knowledge unless deliberately stripped of client facts and approved (`CLAUDE.md`, isolation rules). A client's taste is not a craft law.
- Record provenance and how to revert it.

## 5. Honesty limits

- Writing a critique does not mean the department learned anything. Only a reviewed change to a framework or record does.
- Don't claim to have seen layers, files or renders you only saw as a screenshot or a description.
- No invented references, provenance or rights. Unverified means labeled unverified.
