# Design Sprint and Brand Workshop Method

> CreativeEngine shared framework. Owner `sprint-facilitator`. Consulted by `creative-engine-director` for routing and readiness, `brief-machine` when workshop output becomes a brief, and `design-champ` and `word-smither` when they build sprint prototypes.

## Provenance

Method summarized in our own words from public descriptions of the Design Sprint (Jake Knapp, John Zeratsky and Braden Kowitz, *Sprint*, 2016, developed at GV), the four-day Design Sprint 2.0 (AJ&Smart, with Knapp's approval) and GV's Three-Hour Brand Sprint (Knapp, Laura Melahn, Daniel Burka, John Zeratsky).

- Attribute the method to its authors. Do not reproduce the book's text, worksheets or templates; describe and adapt.
- Exercise names are the authors' labels. Use them so clients and teams can look them up.
- Anything not confirmed in a source we read is marked UNVERIFIED. Known gaps are in §9.

## Purpose

```
WHAT ARE WE TRYING TO ANSWER?
WHO DECIDES, AND WHO MUST BE IN THE ROOM?
WHAT DOES THE SMALLEST REAL TEST LOOK LIKE?
WHAT DID WE LEARN, AND WHAT DID WE ONLY BELIEVE?
```

A sprint compresses a long argument into a short structured one: map the problem, generate divergent solutions alone, decide, build a realistic prototype, test it with real people. Its value is speed to evidence, not consensus.

## What this framework is not

- **Not a creative engine.** A sprint produces sketches from the team, not CreativeEngine-grade concepts. Concept quality is still judged by `creative-engine-director`.
- **Not a substitute for research.** Five interviews reveal patterns and failures. They are not statistics.
- **Not always the right tool.** See §1.
- **Not client knowledge.** What a team says in a workshop is project-level, unverified until confirmed (§8).

## 1. Choose the format

| Situation | Format |
|---|---|
| Team disagrees on who the brand is; no shared language | **Brand Sprint** (3 hours) |
| Big website or landing-page question; stakeholders available; risk of building the wrong thing | **Design Sprint 2.0** (4 days) or original (5 days) |
| Small, well-understood change | No sprint. Just design it |
| Question needs statistical proof, or the audience cannot be reached in a week | Research, not a sprint |
| Decider cannot attend, or the challenge is too broad to test in one prototype | Fix that first, or do not run it |

Default for web design projects: **Brand Sprint first if identity is unresolved, then a Design Sprint on the one page or flow that matters most.**

## 2. Preconditions (check before scheduling)

1. **A challenge small enough to prototype and test in the time.** A homepage, a conversion flow, a service-page journey. Not "the whole website".
2. **A Decider** who can say yes and is in the room for the key decisions.
3. **A team of seven or fewer**, cross-functional, plus a Facilitator who does not also design.
4. **Target customers reachable** for test day (recruitment starts early).
5. **Blocked calendars** and a war room (physical or a shared board).
6. **A sprint brief** stating the challenge, context, known constraints and what happens with the outcome. Prepared with `brief-machine` when source material is raw.

If any fail, record it and either fix it or change the format. Running a sprint without a Decider is the most common way to produce a week of theatre.

## 3. Three-Hour Brand Sprint

Purpose: turn "our brand" into concrete, shared language so later decisions about visuals, voice and identity are easier. It defines the team's belief; it does not verify it.

| # | Exercise | Job |
|---|---|---|
| 1 | 20-Year Roadmap | Long-term vision and what the world looks like if the company succeeds |
| 2 | What, How, Why | Clarify why the company exists, what it does and how |
| 3 | Top 3 Values | Turn "why" into three specific, ownable values |
| 4 | Top 3 Audiences | Who the brand serves most |
| 5 | Personality Sliders | Place the brand on opposing traits (for example friendly to authoritative, playful to serious) |
| 6 | Competitive landscape | See where competitors sit and where the brand can differ. UNVERIFIED as the sixth item; one source lists Design Principles instead. Confirm against GV's original before quoting it |

Facilitation rules:
- Everyone works silently first, then shares, so the loudest voice does not set the answer.
- Timebox hard. The Why exercise runs long; cut it, do not extend it.
- Output is a one-page brand summary, not a brand strategy.
- Disagreement is data. Record it and mark it OPEN if it does not resolve.

Outputs go to `brief-machine` as PROJECT-LEVEL source material. Personality sliders and values become inputs to `design-champ` and `word-smither`, not conclusions.

## 4. Design Sprint 2.0 (four days)

The original five-day agenda (Map, Sketch, Decide, Prototype, Test) is compressed so the full team is needed for about two days.

| Day | Agenda | Who |
|---|---|---|
| **1. Define and sketch** | Expert interviews and How Might We notes. Long-term goal and sprint questions ("Can we...?"). Map the customer journey. Lightning Demos. Four-step sketch: notes, ideas, Crazy 8s, solution sketch | Full team, experts |
| **2. Decide and storyboard** | Art-museum display, heat map, speed critique, straw poll, Decider's supervote. User Test Flow storyboard | Full team; experts may leave after the vote |
| **3. Prototype** | Build a realistic facade. Two Decider check-ins. Stop at a fixed time | Makers, Stitcher, Writer, Facilitator |
| **4. Test** | Five customers plus one backup, one-on-one, five-act interview. Team watches and takes notes. End-of-day pattern review against the sprint questions | Facilitator, interviewer, observers, Decider |

Roles: **Decider**, **Facilitator**, **Makers**, **Stitcher** (assembles the prototype), **Writer** (real copy, no lorem ipsum), **Asset collector**, **Interviewer**, **Note-takers**.

Guardrails:
- **Sketch alone, decide with a structure.** No group brainstorming for ideas; no design by committee for the storyboard.
- **Goldilocks fidelity.** Real enough that customers react honestly, rough enough to build in a day.
- **Test the questions, not the taste.** Each sprint question needs an observable signal.
- **Interviews are not focus groups.** Never lead the customer; never sell them the prototype.

## 5. Adapting for web design projects

| Web deliverable | How the sprint is applied |
|---|---|
| Homepage or landing page | Challenge is the one job the page must do. Prototype is a clickable page in Figma or a hosted prototype. Test: can a visitor say what this is and what to do next? |
| Conversion flow (form, checkout, enrolment, booking) | Map the whole journey, pick the riskiest step, prototype that step realistically |
| Site architecture or navigation | Card-style tasks in the test; prototype the navigation, not every page |
| Rebrand of a site | Brand Sprint, then a Design Sprint on the highest-traffic template |

- **Prototype, then production.** A sprint prototype is a learning artifact. It is never promoted to production. Native builds follow the `instapage-production` skill when the client's route is Instapage, and the approved Figma spec, not the sprint prototype, is the source.
- **Real copy.** The Writer role writes real copy. Route through `word-smither` when the copy carries the idea.
- **Brand constraints.** A client's approved identity is a mandatory; the sprint does not reopen it unless that is the challenge.

## 6. Operating modes

| Sprint stage | Mode | Note |
|---|---|---|
| Brand Sprint, Map, expert interviews | Briefing input (BriefMachine territory) | Convert output to a normalized brief; do not treat it as strategy |
| Lightning Demos, Crazy 8s, sketches | EXPLORE | Divergence first, no critique until display |
| Critique, votes, storyboard | Decision inside the sprint | This is the team's and Decider's decision, not a KILL/ADVANCE verdict |
| Prototype | DEVELOP | Rough enough to be quick |
| Test and pattern review | Evidence | Feeds JUDGE; failing the test can return work to EXPLORE or the brief |

A sprint winner is not automatically ADVANCE. CreativeDirector may still judge it REWORK or KILL on originality or brand grounds, and must say what the sprint evidence does and does not show.

## 7. Facilitation craft

- **Timebox visibly.** Timer on screen; say what happens when time runs out.
- **Thick markers, short notes.** Forcing brevity forces clarity.
- **Silence is a tool.** Solo work first, discussion second.
- **Facilitator is neutral.** They run the process; the Decider decides; the team supplies content.
- **Remote sprints.** Add a co-facilitator who watches participation and chat; give each person a small logistics job; shorter sessions with breaks; a shared board (Miro, FigJam) as the wall.
- **Energy management.** Breaks, food, a hard stop. Protect Day 3 building time.
- **Re-centre on the questions.** When a debate drifts, return to the sprint questions.

## 8. Evidence and scope rules

- Workshop statements (values, audiences, competitors, claims) are **PROJECT-LEVEL and unverified** until confirmed by a source. Do not turn them into client facts, and never invent research to fill a gap.
- Test findings are observations of a handful of people. State the sample and the pattern; do not report percentages.
- Nothing from one client's sprint carries into another's. Reusable learning is about method only.
- Store outputs under the project, not in `shared/`. Raw workshop artifacts (photos, boards, recordings) are raw sources and are never edited.

## 9. Known gaps

- Sixth Brand Sprint exercise unconfirmed (§3).
- Per-exercise timings for the Brand Sprint and the 2.0 agenda were not retrieved from primary sources. Use them as the facilitator's judgment, not as quotes.
- A cross-check against the book's current edition and GV's original Brand Sprint article is worth doing before this framework is presented externally.

## Related frameworks

| Framework | Relationship |
|---|---|
| `brief-normalization.md` | Workshop output becomes a raw source, then a normalized brief |
| `selling-the-work.md` | Sprint test evidence supports the defense of an idea; it does not replace it |
| `discovery-and-lean-loop.md` | Discovery before, and the Lean loop after, a sprint |
| `creative-object-taxonomy.md` | Classify the prototype (landing page, flow, key visual) before evaluating it |
| `creative-trajectory-evaluation.md` | Compare sprint rounds when a sprint is repeated |
