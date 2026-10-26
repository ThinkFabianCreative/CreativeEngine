---
name: creative-brief
description: Write, review and pressure-test a TRAFFIK creative brief as a loop between CreativeEngine's agents, then render it as the red TRAFFIK .docx. BriefMachine writes; creative-engine-director tests strategy and the USP; WordSmither and DesignChamp test whether the USP and proposition can be shown; the loop repeats until the brief passes or three rounds are spent. Use when a client brief, RFP or source material must become a TRAFFIK brief, when an existing brief needs review, or when the user asks to run the brief loop.
---

# creative-brief

Owner: BriefMachine. Record: `BriefMachine/skills/creative-brief.md`.
Thinking lives in `shared/frameworks/brand-strategy.md` (brand platform, JTBD, USP §6a, brief fields §7) and `creative-effectiveness.md` (ladder, judging). This skill runs the process; it does not repeat them.

Template: `assets/creative-brief-template.md`. Judging card: `assets/judging-card.md`. Renderer: `scripts/brief2docx.py` (needs `python-docx`; install it in a scratchpad virtualenv, never globally).

## Modes

| Mode | Use when | Output |
|---|---|---|
| **LOOP** (default) | Source material must become a brief | A brief that passed the loop, a loop log, and a .docx |
| **REVIEW** | An existing brief needs checking | The loop's tests run once on that brief, with findings. No rewrite unless asked |
| **RENDER** | A finished brief's Markdown needs a .docx | The .docx, previewed |

## The loop

Run it from the main session, calling each agent with the Agent tool. Each call gets the client, project, the paths to the sources and the current draft, and only what that role needs. Agents work from the project's sources and the normalized brief, never from another client's workspace.

```
STEP 0 (optional)  creative-researcher   if the project has no competitor map or voice-of-customer
                                         evidence, research them first (CreativeResearcher/AGENT.md)
ROUND n (max 3)
  1. brief-machine            WRITE (round 1) or REVISE (later rounds) → draft brief .md
  2. in parallel:
     creative-engine-director STRATEGY GATE
     word-smither             SHOW TEST (verbal)
     design-champ             SHOW TEST (visual)
  3. Aggregate the verdicts
     all 12 standards PASS → stop, render
     any FAIL → send every finding to brief-machine → next round
AFTER ROUND 3 with open FAILs → stop, escalate to the user with the disagreement stated plainly
```

Three rounds follows the program's rule of three meetings: after three, produce it or decide.

When a round's FAILs are blocked on evidence TRAFFIK could find (competitor claims, audience language, benchmarks, what an asset library holds), send that question to `creative-researcher` before the next round instead of asking brief-machine to assume.

### Step 1: brief-machine writes

- Fill every template field from evidence. Delete the grey prompt lines (`> `) from the output.
- **USP per job:** write it from evidence and check it against the seven tests yourself first. If nothing is truly unique, write **parity**, or a labeled **pre-emptive** USP. Never invent one.
- Mark unapproved claims ⚑. Put assumptions in *italics*. On a later round, change only what the findings name, and say how each finding was handled.
- Write to the **TRAFFIK Brief Standard** (`brand-strategy.md` §7a). **Three pages at most.** Cut words, never fields. If it won't fit, it's more than one brief.

### Step 2a: creative-engine-director, strategy gate

Judge **standards 1–11 of the TRAFFIK Brief Standard** (`brand-strategy.md` §7a): **PASS / FAIL** for each, with one reason and, for a FAIL, what would fix it. Also run the readiness questions in `CreativeDirector/AGENT.md`, and USP tests 3 and 7 (strong, defensible) as advice. Those two don't fail the brief on their own.

### Step 2b: word-smither and design-champ, show test

Standard 12 (USP test 6). For each job, answer **SHOWABLE / THIN / NOT**:

- **word-smither:** can the proposition be said in a way that stops someone? Is there a verbal mechanism in it?
- **design-champ:** does the USP give an image, a demonstration or a visual proof?

One reason each. **No concepts, headlines or layouts.** This is a test of the brief, not EXPLORE. THIN or NOT counts as a FAIL and goes back to brief-machine, unless the USP is honestly parity. In that case, flag the cell as one where the idea has to carry the distinctiveness.

### Step 3: aggregate

- Keep a loop log at `projects/<client>/<project>/work/brief/brief-loop-log.md`: round, each agent's verdicts and reasons, and what changed.
- **Disagreement:** if the director and the creatives conflict (strategically sound but not showable, or the reverse), it goes back to brief-machine as one finding. If it survives round 3, the user decides.
- **Test 4 (true and provable) is never cleared in the loop.** List every ⚑ claim for the client or legal at the end.

## Render

1. Save the passed brief as `creative-brief_vNN.md` in the project's `work/brief/`.
2. `<venv>/bin/python -I scripts/brief2docx.py <brief.md> <Client>_Creative-Brief_vNN.docx`
3. Preview it (`qlmanage -t -s 1000 -o <scratch> <file.docx>`), read the image, and check the title block, headings, bullets and symbols before delivering. Check the page count: over three pages fails standard 1, so send it back.
4. Markdown conventions the renderer reads: `@ TITLE | CLIENT · PROJECT | meta` for the title block; `##` section; `###` job; `- ` bullet; `> ` grey prompt; `---` rule.

## Rules

- Current client only. Sources are labeled as in `brief-normalization.md`. Raw files are never edited.
- A brief is not approved because it passed the loop. The client signs it.
- Report what each agent said. Don't summarize a FAIL into a PASS.
