# Discovery and Lean Loop

> CreativeEngine shared framework. Owner `sprint-facilitator`. Consulted by `brief-machine` (insight synthesis into a brief), `creative-engine-director` (evidence in JUDGE), and `design-champ` and `word-smither` when a prototype needs a testable hypothesis.

## Provenance

Method summarized in our own words from public descriptions of:
- The **LUMA System** of human-centered design (LUMA Institute, now part of Mural; *Innovating for People*): 36 bite-sized methods in three skills, Looking, Understanding, Making, combined into sequences the LUMA material calls "recipes".
- **Lean UX** (Jeff Gothelf and Josh Seiden), which joins UX design, agile and Lean Startup.
- **Lean Startup** (Eric Ries): the build-measure-learn loop and the minimum viable product.
- **Lean Canvas** and *Running Lean* (Ash Maurya, 2010 and after): a one-page business-model hypothesis adapted from Osterwalder's Business Model Canvas, tested box by box in order of risk.

Rules:
- Attribute method names to their sources. LUMA is a proprietary system; describe and adapt its methods, and do not reproduce its handbook, cards or worksheets.
- The full set of 36 LUMA method names is verified from the physical card set (§2).
- Anything not confirmed in a source we read is marked UNVERIFIED.

## Purpose

The Design Sprint (`design-sprint.md`) is one compressed run. This framework covers the work around it:

```
WHAT DO WE ACTUALLY KNOW ABOUT PEOPLE AND THE PROBLEM?
WHAT ARE WE ONLY ASSUMING?
WHICH INSIGHT SUPPORTS WHICH FEATURE, AND HOW STRONGLY?
WHAT IS THE SMALLEST TEST THAT COULD PROVE US WRONG?
```

It converts observation into insight, insight into a feature or page decision, and a decision into an experiment. Its bias is toward evidence and away from opinion, and it is deliberately not a creative method.

## What this framework is not

- **Not a substitute for creative judgment.** An insight does not write the idea, and a feature backlog is not a concept.
- **Not statistics.** A handful of interviews yields patterns and hypotheses, not percentages.
- **Not client knowledge.** Findings from one project stay in that project (§8).
- **Not always needed.** A small change with known needs does not need discovery.

## 1. Three roles for three methods

| Source | Job in CreativeEngine | Use it for |
|---|---|---|
| LUMA (Looking, Understanding, Making) | Gather and make sense of what people do and need, with a shared vocabulary for a team | Pre-sprint discovery, synthesis, participatory prioritization, evaluation |
| Lean UX and Lean Startup | Turn beliefs into hypotheses and cheap experiments | Post-sprint iteration, deciding what to build next, landing-page and flow tests |
| Design Sprint | Compress the big decision into a tested prototype | The moment when a real decision is stuck |

Sequence for a typical web project:

```
LUMA discovery → synthesis → (Brand Sprint) → Design Sprint → Lean loop on live or near-live pages
```

Skip stages that do not pay for themselves.

## 2. LUMA in use: Looking, Understanding, Making

All 36 methods, as grouped on the *Innovating for People* method card set (verified from photos of the physical cards and summary card, `SprintFacilitator/SprintBook_Design_thinking/`).

| Skill | Category | Methods |
|---|---|---|
| **Looking** (observe the human experience) | Ethnographic research | Interviewing, Fly-on-the-Wall Observation, Contextual Inquiry, Walk-a-Mile Immersion |
| | Participatory research | What's on Your Radar?, Buy a Feature, Build Your Own, Journaling |
| | Evaluative research | Think-Aloud Testing, Heuristic Review, Critique, System Usability Scale |
| **Understanding** (make sense of what was seen) | People & systems | Stakeholder Mapping, Persona Profile, Experience Diagramming, Concept Mapping |
| | Patterns & priorities | Affinity Clustering, Bull's-eye Diagramming, Importance/Difficulty Matrix, Visualize the Vote |
| | Problem framing | Problem Tree Analysis, Statement Starters, Abstraction Laddering, Rose, Thorn, Bud |
| **Making** (give ideas a tangible form) | Concept ideation | Thumbnail Sketching, Creative Matrix, Round Robin, Alternative Worlds |
| | Modeling & prototyping | Storyboarding, Schematic Diagramming, Rough & Ready Prototyping, Appearance Modeling |
| | Design rationale | Concept Poster, Video Scenario, Cover Story Mock-up, Quick Reference Guide |

"Brainstorming" is not a LUMA method; Statement Starters ("How might we…", "In what ways might we…", "How to…") is the LUMA framing that the Sprint's How Might We notes echo. Each card carries a quick guide and helpful hints; describe them in our own words, do not reproduce them.

Selection guide for web design work:

| Question | Method family |
|---|---|
| What do visitors actually do and say? | Interviewing, observation, Think-Aloud Testing |
| Which features matter to them? | Buy a Feature, What's on Your Radar |
| How do we make sense of 30 sticky notes? | Affinity Clustering, Rose Thorn Bud |
| Is the problem the one we think it is? | Abstraction Laddering, Problem Tree Analysis, Problem Framing |
| Is the existing site usable? | Heuristic Review, System Usability Scale, Think-Aloud Testing |
| How do we show the stakeholders one idea to react to? | Concept Poster, Storyboarding |

Use the smallest number of methods that answers the question. A recipe is two to four methods, not twelve.

## 3. Insight to feature: the evidence chain

Every feature, page section or content block that the workshop or discovery proposes must trace back to something observed.

```
OBSERVATION (what happened, who, when)
   → PATTERN (seen in more than one place)
      → INSIGHT (what it means; labeled DERIVED)
         → HYPOTHESIS (what we believe will change)
            → FEATURE / DECISION (what we will try)
               → EXPERIMENT (how we will know)
```

Label each link:
- **OBSERVED**: directly seen or heard, with source and sample.
- **DERIVED**: our interpretation. State confidence.
- **ASSUMED**: no evidence yet. It becomes an experiment or stays a flagged risk.

A feature list where every item is ASSUMED is a wish list. Say so.

Prioritization, in order of evidence, not volume:
1. Impact on the sprint or project question.
2. Strength of the evidence (multiple independent observations beat one loud stakeholder).
3. Cost to test (cheapest experiment first).
4. Reversibility.

A participatory prioritization exercise such as Buy a Feature can rank preferences, but a ranking is stated preference, not behavior. Confirm with a test.

## 4. Lean UX in use: assumptions, hypotheses, MVPs

Lean UX starts from the position that everything is an assumption until tested and that a design is a hypothesis.

1. **Problem statement.** The business or user problem, not a solution.
2. **Assumptions.** List what must be true. Rank by risk (how bad if wrong) and uncertainty (how little we know). Test the top-right first.
3. **Hypothesis statement.** "We believe [this]. We will know we are right or wrong when we see [qualitative or quantitative signal]." The signal must be observable and agreed before the test.
4. **MVP.** The smallest thing that can test the hypothesis. It is a test instrument, not a small product.
5. **Experiment and learn.** Run it, record what happened, decide: persevere, pivot or stop.

Working principles worth keeping: outcomes over output, small batches, continuous customer contact, making artifacts visible, and permission to be wrong.

## 5. MVPs for web design projects

| Hypothesis type | Lightweight test |
|---|---|
| Visitors will understand the offer | Five-second or comprehension test on a static or clickable prototype |
| Visitors will take the next step | Landing page or fake-door page with one clear call to action, measured on a real audience |
| A message beats another message | Headline or hero variants on live traffic, when volume allows. Below sample thresholds report direction only |
| A flow works | Task-based Think-Aloud Testing on a prototype, five to six participants |
| People want a feature | Fake door, concierge (do it by hand) or a Buy-a-Feature exercise with real users |

Landing pages built for tests follow client rules and, on Instapage, the `instapage-production` skill. A test page is not a claim that the page is approved creative. Use only claims the client has substantiated.

## 5a. Lean Canvas in use

A one-page set of hypotheses about a business or offer, built for early stages with more questions than answers. Nine boxes: Problem (top one to three, plus existing alternatives), Customer Segments, Unique Value Proposition, Solution (top features, one per problem), Channels, Revenue Streams, Cost Structure, Key Metrics, Unfair Advantage.

- **Fill in order of certainty, not left to right.** Start with Customer Segments and Problem as a pair (a problem exists only for a person), then Unique Value Proposition, then Solution, then Channels.
- **Every box is a hypothesis.** Mark each OBSERVED, DERIVED or ASSUMED (§3). The riskiest assumption at idea stage is usually the Problem and Customer Segment pair. Test in order of "if this is wrong, does it die?".
- **Interview ladder** (*Running Lean*): a Problem Interview asks whether the segment has the problem badly enough; a Solution Interview shows a mock-up or prototype; an MVP Interview watches use of the real thing. Problem Interview structure (2nd ed., chapter 7, as listed by O'Reilly and practitioners): welcome and set the stage → collect demographics (tests the segment) → tell a story that sets the problem context → have them rank the problems (tests the problem) → explore how they deal with it today (tests the problem) → wrap up: replay their story in 30 seconds and ask to follow up or refer others. Match the interview to what the canvas says is riskiest. A sprint's Day 4 test is roughly the Solution Interview.
- **Web use.** Use it to sharpen a project's problem, audience and value proposition before a sprint, and to turn the Solution and Channels boxes into the page's job and traffic source. Key Metrics becomes the sprint question's signal.
- **Not for every project.** A client with a settled offer and audience does not need a canvas. Use it when the offer, audience or model is unclear, or for a new product, service or campaign page. Revenue, Cost and Unfair Advantage are the client's to supply. Never invent them.

## 6. Where each method plugs into a Design Sprint

| Sprint stage | Add |
|---|---|
| Before Day 1 | Lean Canvas, when the offer or audience is unclear; interviews or observation as pre-work; problem framing; a stakeholder map to choose the Decider and experts |
| Day 1 | Abstraction Laddering or Problem Tree to sharpen the challenge; assumptions become the sprint questions |
| Day 2 | Visualize the Vote or Concept Poster for display |
| Day 4 | Think-Aloud prompts within the five-act interview; hypotheses written beforehand, with signals |
| After | Lean loop on the winning direction; affinity cluster of findings; decide persevere, pivot or stop |

## 7. Facilitation notes

- Make the hypothesis and the signal visible on the wall before the test starts; do not change the criteria afterwards.
- Cluster silently, name clusters together, and keep the participants' own words.
- Separate observation from interpretation on every board (two colors of note).
- Stop discovery when patterns repeat; do not chase completeness.

## 8. Evidence and scope rules

- Findings are PROJECT-LEVEL and carry source, date and sample. Client knowledge only through deliberate review and the user's confirmation.
- No invented participants, quotes, analytics or benchmarks. A simulated rehearsal is labeled SIMULATED and does not enter project knowledge.
- Test data from one client is never evidence for another.
- Personal data from interviews is handled per the project's rules and participants' consent; do not store more than needed.

## 9. Known gaps

- The 36 LUMA method names and categories are now verified from the physical card set (§2). Per-method steps were read only for a few cards; check the card before running an unfamiliar method.
- Lean Canvas and the Problem Interview steps are from the book's table of contents and summaries, not the full text (O'Reilly pages returned 403). Solution and MVP interview scripts are not detailed here. The nine boxes are consistent across sources.
- No source was retrieved for quantitative sample-size guidance; treat small-sample findings as directional.

## Related frameworks

| Framework | Relationship |
|---|---|
| `design-sprint.md` | The compressed run this framework feeds and follows |
| `brief-normalization.md` | Synthesis output enters as a raw source; audience hypotheses stay labeled DERIVED |
| `selling-the-work.md` | Evidence chain supports the defense of an idea |
| `creative-trajectory-evaluation.md` | Compare rounds of experiments and iterations |
