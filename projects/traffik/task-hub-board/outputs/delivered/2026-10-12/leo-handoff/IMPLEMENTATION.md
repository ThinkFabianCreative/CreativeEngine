# Implementation notes

How the prototype works, so it can be rebuilt inside the Task Hub on real data. Function names refer to the `<script>` in `taskhub-board-prototype.html` (one file, vanilla JS, no framework). All state is in memory.

## 1. Data model

### Task (prototype: `cards[]`)

| Field | Type | Meaning | Hub equivalent / change |
|---|---|---|---|
| `id` | number | Task ID | Existing |
| `t` | string | Title | Existing |
| `c` | string | Client | Existing |
| `who` | string | Assignee (the maker) | Existing "Assigned to" |
| `am` | string | **Account lead: one person** | Replace the shared pairs ("Darcey/Brad/Ky") with a single-person field, plus an optional "Account team" list |
| `lead` | string | **Creative lead** (ACD/CD) | New |
| `rev` | string | **Reviewer.** Must not be the maker | New |
| `col` | enum | Current stage (see §2) | Derived from the current plan step |
| `brief` | 0/1 | Brief linked | New field: `brief_url` |
| `qcOK` | 0/1 | Quality Control passed | Derived from the QC checklist (§4) |
| `high` | string | Reason for HIGH (empty = normal) | Existing HIGH flag, plus a required reason |
| `late` | 0/1 | Overdue | Existing |
| `round` / `rounds` | number | Current client round / contracted rounds | Later (month 3) |
| `plan` / `log` | number | Planned hours (standard times) / logged hours | Existing planned effort; logging later (month 2) |
| `del` / `prom` | date | Plan "delivers" date / promised date | Existing |
| `driver` | string | Due-date driver | Existing field; required later |
| `track` | "Light" / "Full" | Process track | Later (month 2) |

### Blocker (prototype: `blocked[]`)

`{ id: taskId, why: string, owner: string, since: date }`

In the Hub this belongs on the step that's Blocked: when a step is set to Blocked, ask for `reason` and `owner` (a person or "Client"), and stamp `since`.

### QC answers (prototype: `qcAns[taskId]`)

An array of five booleans. In the Hub, store each answer with `answered_by` and `answered_at`, plus `override_reason` if the ACD overrides a No.

## 2. Stages (board columns)

`COLS` and `ORDER` define the columns. The board places a task in the column of its **current step**. Map the Hub's step names like this (Leo: check against the full step library):

| Column (`col`) | Hub steps |
|---|---|
| `intake` | In the queue · no plan · "Needs a date" |
| `ready` | Plan exists, first step not started |
| `prog` | Any active work step (design, copy, build, edits) |
| `review` | Internal review · Internal check-in · Due for internal |
| `qc` | Pre-launch QA (rename to **Quality Control**) · Exports & spec check |
| `client` | Send / present · Present to client · R1/R2 due |
| `fb` | Client feedback R1/R2 · Revisions R1/R2 |
| `done` | Client final approval · Campaign launch · task Complete |

Moving a card on the board = completing the current step and starting the next step that maps to the target column. If that's awkward in the Hub's model, a read-only board (v1) is fine; moves can happen in the task detail.

## 3. Rules (v1)

All in `rule(card, toColumn)`, which returns a message when a move is blocked, and `fix()`, which offers a one-click fix.

| Rule | Prototype logic | Hub behavior |
|---|---|---|
| No brief, no work | Leaving `intake` needs `brief` and `am` | The first work step can't go Active without `brief_url` and an account lead (Full track) |
| Maker is never checker | `review` blocked if `rev === who` | The Internal review step's assignee can't be anyone assigned to the work steps |
| QC before the client | `client`/`done` blocked unless `qcOK` | "Send / present" can't start until Quality Control is complete |
| Blocked means blocked | Can't move forward while in `blocked[]` | A blocked task can't advance until the blocker is cleared |

Start with **warnings plus a logged override** for a 6-week pilot, then make them hard blocks.

## 4. Quality Control checklist

`QC` holds the five questions and their signers. `openQC(id)` renders the dialog.

1. Meets the brief? (account lead + ACD)
2. On brand? (an AD who didn't make it)
3. Delivers what was asked? (QC team: Judy, Katie)
4. Any mistakes? (account lead for claims and numbers; QC team for language and details)
5. Presentation ready? (ACD)

Pass = five Yes. A No is allowed only with an ACD override and a reason.

## 5. Views

| View | Function | v1? |
|---|---|---|
| Board | `board()`, `cardHTML()`, `flag()` | **Yes** |
| Task detail sheet | `openDrawer()`, `openParent()`, `showSheet()` / `hideSheet()` | Use the Hub's existing task detail; add the fields in §1 and the QC section |
| List | `list()` | Later |
| Calendar | `cal()`, `span()` | Later |
| Workload | `week()` | Later (needs logged hours) |
| Leadership | `lead()` | Later |
| Completed | `comp()`, `sum()` over `DONE[]` (the export) | Later |
| Stand-up mode | `suSteps()`, `suPanel()` | Later; it runs on top of the board |
| New task form | `#newBtn` handler, `TL`, `addBiz()`, `baseHigh()` | Later (intake rework) |

**Scope filter:** `scope` (`mine` / `team` / `all`), `MY_TEAM`, `inScope()` and `vis()`. Andres's team is: Andres, Umair, Michael, Jordan, Debbie, Damba, Andrea, Aaron, Matt. In the Hub, "My team" should come from reporting lines.

**Card content (keep it this light):** title · client · round · assignee avatar · one status badge chosen by `flag()` in priority order (Blocked → Change order → Overdue → Self-review → Before plan → High) · icons only for "no brief" and "QC passed".

## 5b. Side navigation (must-have)

Markup: `<aside class="side" id="side">`. Client entries render in `chrome()` into `#spaces`, each with a `data-sp` client filter. The rail toggle is `#sideT`; `applyRail()` sets the `.rail` class (64 px, labels hidden via `.lbl`) and remembers the choice in `localStorage` (`th_rail`). Narrow screens (<900 px) default to the rail. Every nav item carries a `title` for the rail tooltip.

## 6. Design tokens

The prototype uses a Jira-style layout with the Traffik brand. Tokens (CSS variables in the "Jira look & feel" block):

| Token | Value | Use |
|---|---|---|
| `--fg` | #172B4D | Text |
| `--sub` | #44546F | Secondary text |
| `--mfg` | #626F86 | Muted text |
| `--border` | #DCDFE4 | Borders |
| `--muted` | #F7F8F9 | Column background |
| `--hov` | #F1F2F4 | Hover |
| `--sel` | #FDECEE | Selected nav / tab background |
| `--brand` | #C8202F | Traffik red: Create, selected tab, problems only |
| `--ok` | #216E4E | Done / passed |
| Header | #1d1d1d | Traffik dark (earlier header variant) |

- **Type:** Instrument Sans, variable (width 75–100, weight 400–700). Condensed width for headings and numbers; tabular figures. One family, no monospace.
- **Icons:** Feather, 16px, stroke 1.75. Each column has its own icon (`COLICON`).
- **Status labels:** flat, uppercase, Atlassian-style (`.lz`, `.tag`).
- **Red only for problems** (blocked, overdue) and the primary action. Not decoration.

## 7. Accessibility (keep these)

- Cards are focusable (`tabindex="0"`) and open with Enter or Space.
- The detail sheet traps focus loosely, closes with Escape, and returns focus to the card (`showSheet` / `hideSheet`).
- **"Move to"** in the detail sheet is the non-drag alternative (WCAG 2.2 dragging movements).
- Visible focus rings; `prefers-reduced-motion` respected.

## 8. Not to copy

- The sample cards, plan templates (`TPL`), parent names (`PARENT`) and hour ranges are placeholders.
- The prototype computes stages from a `col` field. The Hub should derive them from real plan steps.
- `DONE[]` is a static export. In the Hub, the Completed view should query live data.
