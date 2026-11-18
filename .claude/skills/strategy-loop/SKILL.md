---
name: strategy-loop
description: Develop and refine a client's strategic assets (brand promise, brand house, Core Creative Idea candidates, jobs to be done, audience and creative target, the Bar, go-to-market and measurement plans) as a loop between CreativeEngine's agents. CreativeStrategist drafts; CreativeResearcher audits the evidence; creative-engine-director runs the strategy gate; WordSmither and DesignChamp test whether it can be said and shown; up to three rounds, then the user decides. Use when a client needs strategic assets before a brief, when existing strategy needs review, or when the user asks to run the strategy loop.
---

# strategy-loop

Owner: CreativeStrategist. Record: `CreativeStrategist/skills/strategy-loop.md`.
Thinking lives in `shared/frameworks/brand-strategy.md` and `creative-effectiveness.md`. This skill runs the process; it does not repeat them.

## Modes

| Mode | Use when | Output |
|---|---|---|
| **LOOP** (default) | Strategic assets must be developed | Assets that passed the loop, a loop log, a version diff |
| **REVIEW** | Existing strategy needs checking | The loop's checks run once, with findings. No rewrite unless asked |
| **QUICK** | A small piece (one insight, one audience note) | Steps 0–2 only, no parallel review |

## The loop

Run it from the main session, calling each agent with the Agent tool. Each call gets the client, project, file paths and only what that role needs. Current client only.

```
STEP 0  EVIDENCE CHECK   creative-strategist lists what the strategy needs; gaps → creative-researcher first
ROUND n (max 3)
  1. DRAFT       creative-strategist writes the assets; 3–4 candidates wherever a choice exists
  2. RED TEAM    creative-strategist attacks its own draft (checklist below) and fixes what it finds
  3. IN PARALLEL creative-engine-director   strategy gate: brand-strategy.md quality checks, seven tests, swap test
                 creative-researcher        evidence audit: does each claim match its source? any synthesis in quote marks?
                 word-smither + design-champ show test: can it be said, can it be shown? (no lines, no layouts)
  4. AGGREGATE   all pass → to the user · any fail → every finding to creative-strategist → next round
                 a missing fact → back to step 0, not a guess
AFTER ROUND 3 with open fails → stop; give the user the disagreement plainly
5. USER DECIDES  approve, redirect, or pick between candidates. The user's decisions are final inside the loop
6. CLIENT LOOP   client feedback logged; approved assets promoted to client knowledge only through the promotion rule
```

## Red team checklist (step 2)

- **Swap test against the real set:** the competitors prospects actually compare, not the convenient ones. Name them.
- **Evidence weight:** does the main barrier match what most of the evidence says, or a vivid minority?
- **Labels:** every claim is fact (with source), our synthesis, or an assumption. No synthesis in quote marks.
- **Deficit check:** does the strategy talk down to the audience?
- **Creative space:** does it prescribe executions, lines or formats? Then it is not strategy.
- **Fit:** does it respect what the client already owns?
- **Plain reader:** could the client read it once and understand it?

## Smaller loops

- **Divergent:** for a promise or Core Creative Idea, test every candidate; never polish one and stop.
- **Tighten:** after cutting to length, re-check that nothing true was lost.
- **Assumption:** each labeled assumption gets an owner and a test (for example, "validate in the client's interviews"), and is revisited when evidence arrives.
- **Learning:** after launch, results feed back into the assets.

## Rules

- Each round changes only what the findings name. Say how each finding was handled.
- Keep a log at `projects/<client>/<project>/work/strategy/strategy-loop-log.md`: round, each agent's verdict and reason, what changed.
- At every handover, give the user a side-by-side diff: before, after, why.
- Checks run in parallel, not in series.
- Report what each agent said. Never soften a FAIL into a PASS.
- Passing the loop is not approval. The client approves strategic assets.
