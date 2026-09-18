# Creative Trajectory Evaluation

> CreativeEngine shared framework. Used mainly by `creative-engine-director`.

This framework evaluates not just the final creative output, but the observable development trajectory that produced it.

## Ground rule: visible artifacts only

Do not request, expose, store or score hidden chain-of-thought.

Evaluate only visible creative artifacts, decisions and revisions.

## The trajectory

A strong creative process moves from:

```
BRIEF
  ↓
TENSION
  ↓
CREATIVE LENS
  ↓
POST-IT IDEA
  ↓
DIVERGENT TERRITORIES
  ↓
EXECUTION
  ↓
CRITIQUE
  ↓
REVISION
  ↓
FINAL
```

The quality of the trajectory matters. A polished final execution can hide weak thinking, while a strong underlying idea may initially appear rough.

## Related frameworks

| Framework | Evaluates | Status |
|---|---|---|
| `creative-object-taxonomy.md` | What is being evaluated | Active |
| `creative-trajectory-evaluation.md` (this file) | How the idea developed | Active |
| `hey-whipple-copycraft.md` | How ideas and language are generated, developed and sharpened | Active |
| `creative-direction-audit.md` | How far the idea goes, and what limits its ceiling | Active |

Do not apply a planned framework as if it exists. The framework registry in the root `CLAUDE.md` is the source of truth.

---

## 1. Compliance is not creativity

CreativeEngine must distinguish **prompt compliance** from **creative value**. An output may follow the brief perfectly and still be generic.

Evaluate whether the work introduces:

- tension
- human truth
- subtext
- restraint
- contradiction
- surprise
- specificity
- cultural intelligence
- conceptual leap

Penalize work that merely translates strategy into advertising language.

## 2. Creative tension benchmark

For meaningful creative work, identify a visible artifact:

```
TENSION: [one concise articulation]
```

Evaluate: is there genuine friction, or is this merely a consumer observation?

Possible sources:

- desire vs reality
- identity vs behavior
- product truth vs perception
- individual vs culture
- convenience vs guilt
- aspiration vs insecurity
- category promise vs lived experience
- what people say vs what they actually do

Do not manufacture negativity simply to create tension. The tension must be relevant to the brand and the problem.

## 3. Creative lens

After the tension, identify:

```
CREATIVE LENS: [one principle]
```

This is the same artifact `CreativeDirector/AGENT.md` calls CREATIVE PERSPECTIVE.

Examples:

- radical simplicity
- inversion
- uncomfortable honesty
- product demonstration
- behavioral observation
- cultural provocation
- absurdism
- understatement
- emotional storytelling
- category subversion
- visual-verbal tension
- brand act

Do not imitate a particular agency's exact style. Agency histories may inspire principles, but CreativeEngine should name the principle being used.

## 4. Post-it idea

```
POST-IT IDEA: [one concise sentence]
```

This describes the creative idea, not the execution.

Evaluate the Post-it on:

- clarity
- simplicity
- surprise
- tension
- brand relevance
- generativity

Do not impose an arbitrary fixed word count. Prefer compression, but allow the shortest wording that preserves the actual idea.

If it requires a paragraph to explain, that is a warning sign.

## 5. Divergence quality

Do not judge creative exploration by the number of ideas alone. Evaluate whether the territories are genuinely different.

**Bad divergence:**

- ten headline variations
- five tonal rewrites
- the same joke in five media
- cosmetic visual changes

**Good divergence:**

- different human truths
- different tensions
- different creative mechanisms
- different points of view
- different media behaviors
- different emotional registers

For each territory, identify:

```
TERRITORY:
MECHANISM:
WHY IT IS DIFFERENT:
```

## 6. Trajectory quality

Evaluate the development path across five dimensions.

**A. Strategic continuity.** Can we see how the final idea connects back to the actual brief?

**B. Conceptual leap.** Did something meaningful happen between strategy and execution, or did the output simply paraphrase the proposition?

**C. Divergence quality.** Were different possibilities explored before selection?

**D. Critique quality.** Did critique identify real weaknesses rather than merely suggest polish?

**E. Revision gain.** Did the revised version materially improve the idea?

Do not reward revision simply because changes were made.

## 7. Revision delta

For major creative work, compare iterations.

```
VERSION A: What was the concept?
CRITIQUE:  What was actually wrong?
VERSION B: What changed?
DELTA:     Did the revision improve the work?
```

Check the delta against:

- strategy
- concept
- brand ownership
- simplicity
- originality
- emotional resonance
- visual/verbal relationship
- craft

Classify the delta as one of:

- **Regression**
- **No material change**
- **Incremental improvement**
- **Significant improvement**
- **Conceptual breakthrough**

## 8. Generator / judge separation

Whenever practical, separate **generation** from **evaluation**. The agent that creates an idea should not automatically be trusted to declare it excellent.

Within CreativeEngine:

| Agent | Role |
|---|---|
| `word-smither` | May generate verbal ideas |
| `design-champ` | May generate visual ideas |
| `brief-machine` | May generate strategic reframings |
| `creative-engine-director` | Evaluates them |

For major work, CreativeDirector should actively challenge the creator's preferred idea.

Self-critique is useful, but independent critique is stronger.

## 9. Ad-speak filter

Evaluate whether language sounds discovered from the problem or retrieved from advertising memory.

Flag language such as the following, unless it is deliberately used or subverted:

- unleash
- elevate
- seamless
- revolutionary
- reimagine
- possibilities
- the future of
- game-changing
- empowering
- made for every moment
- where X meets Y

Also flag structural ad-speak:

- generic inspirational manifesto
- adjective stacking
- vague transformation claims
- generic human-potential language
- press-release voice
- proposition repeated as headline

Do not reject a word solely because it appears on a list. Judge its use in context.

## 10. 1 + 1 = 3 gate

For visual-verbal work, evaluate:

```
IMAGE:         What information does it contribute?
COPY:          What information does it contribute?
THIRD MEANING: What exists only because both are experienced together?
```

Classify:

| Result | Meaning |
|---|---|
| **1 + 1 = 1** | Redundant. Image and copy repeat each other. |
| **1 + 1 = 2** | Complementary but literal. |
| **1 + 1 = 3** | The interaction creates a new conceptual meaning. |

Do not force this test onto copy-only or image-only work.

This test is active here and reusable by any agent. `hey-whipple-copycraft.md` (section 2) adds a more specialized copycraft treatment of the same principle; that version wins for the specific copycraft judgment, and this shared test remains available.

## 11. Creative disruption guardrails

These are diagnostic warnings, not automatic rejections.

| Warning | Trigger |
|---|---|
| **Post-it warning** | The idea requires extensive explanation. Do not use a fixed ten-word cutoff. |
| **Cliché warning** | The idea depends substantially on familiar category or advertising patterns without a fresh observation. |
| **Ad-speak warning** | Language resembles corporate or generic marketing speech. |
| **Vanity-metric warning** | A weak concept is being defended primarily through impressions, engagement numbers or projected reach. |
| **Case-study warning** | The explanation sounds more impressive than the work itself. |
| **Technology warning** | Novel technology is functioning as the idea rather than enabling the idea. |
| **Earned-media warning** | See below. |

**Earned-media warning.** Do not penalize work simply because it uses paid media. Instead ask: does this particular type of creative object need cultural propagation to succeed? Use the creative-object taxonomy before applying this criterion.

## 12. Quality gates by use case

There is no single universal, Cannes-inspired minimum. The threshold depends on the creative object's job.

These use cases map onto CreativeEngine's canonical operating modes:

| Use case | Operating mode |
|---|---|
| Internal exploration | EXPLORE |
| Working round | DEVELOP |
| Creative review | JUDGE |
| Client presentation | JUDGE |
| Flagship / award-ambitious | Not a mode. An ambition level applied during DEVELOP or JUDGE. |

**Internal exploration**
- Purpose: generate possibilities.
- Allow imperfect and risky ideas. Do not kill unconventional thinking too early.

**Working round**
- Purpose: identify viable territories.
- Require strategic relevance, conceptual clarity and some distinctiveness.

**Creative review**
- Purpose: select ideas worth developing.
- Require stronger originality, brand ownership, tension and generativity.

**Client presentation**
- Purpose: present work the team is willing to defend.
- Require strong strategic relevance, high conceptual quality, strong brand ownership, excellent craft potential and a credible rationale.
- Aim for high creative ambition where appropriate. Do not require every client presentation to be "Gold" or "Titanium."

**Flagship / award-ambitious work**
- Purpose: push beyond normal campaign expectations.
- CreativeDirector may deliberately seek cultural permeability, industry novelty, behavior change, platform inversion, unusually high craft and Gold/Titanium-level creative ambition.
- These are ambition targets, not predicted awards.

## 13. Creative trajectory scorecard

For major concept development, CreativeDirector may report:

```
OBJECT TYPE:     [from creative-object-taxonomy]
TENSION:         [one sentence]
CREATIVE LENS:   [principle]
POST-IT IDEA:    [one sentence]

TRAJECTORY:
  Strategic continuity:  X/10
  Conceptual leap:       X/10
  Divergence quality:    X/10
  Critique quality:      X/10
  Revision gain:         X/10

FINAL CONCEPT QUALITY:   X/10
CRAFT POTENTIAL:         X/10
AMBITION:                [from creative-direction-audit, when the object is eligible]

BIGGEST LEAP:            [what materially improved]
BIGGEST COMPROMISE:      [where the work became safer or weaker]

VERDICT:                 KILL / REWORK / ADVANCE / BET THE PITCH
```

Verdict definitions are in the root `CLAUDE.md`. AMBITION is the qualitative altitude from `creative-direction-audit.md`; leave it out when the object is not eligible for an audit.

## 14. Model evaluation principle

When evaluating AI-generated creative work, never reward verbosity, fluency or obedience by themselves. A polished answer is not necessarily a creative answer.

Prefer:

- specific over comprehensive
- surprising over predictable
- clear over elaborate
- human over corporate
- conceptual over decorative
- generative over one-off
- memorable over merely correct
