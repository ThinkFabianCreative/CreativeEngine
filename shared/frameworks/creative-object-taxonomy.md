# Creative Object Taxonomy

> CreativeEngine shared framework. Used by all agents; `creative-engine-director` especially.

Creative work must be evaluated according to what it is trying to be.

- A tagline is not a campaign platform.
- A headline is not a brand platform.
- A hero graphic is not an integrated campaign.
- A stunt is not body copy.
- A visual identity is not a key visual.
- An execution is not necessarily an idea.

So the first step in serious creative evaluation is: **classify the creative object.**

The taxonomy answers one question: **what are we actually making or evaluating?**

It does not determine whether the work is good. Other frameworks and agents handle that.

## Related frameworks

| Framework | Evaluates | Status |
|---|---|---|
| `creative-object-taxonomy.md` (this file) | What is being evaluated | Active |
| `creative-trajectory-evaluation.md` | How the idea developed | Active |
| `hey-whipple-copycraft.md` | How ideas and language are generated, developed and sharpened | Active |
| `creative-direction-audit.md` | How far the idea goes, and what limits its ceiling | Active |

The framework registry in the root `CLAUDE.md` is the source of truth for what exists.

---

## Core routing logic

For serious creative work:

```
OBJECT
  ↓
JOB TO BE DONE
  ↓
PARENT / CHILD RELATIONSHIP
  ↓
TYPE-SPECIFIC SUCCESS CRITERIA
  ↓
RELEVANT GENERATION / EVALUATION FRAMEWORKS
```

Classification comes before scoring.

If terminology is ambiguous, classify according to the object's **job**, not merely what somebody called it.

## Three levels of quality

For every object, preserve the distinction between:

| Level | Question |
|---|---|
| **Strategic fitness** | Is this the right thing to make? |
| **Conceptual quality** | Is the underlying idea strong? |
| **Craft quality** | Is this particular expression exceptionally made? |

Do not collapse these.

Example: a beautifully written headline may have high strategic fitness, mediocre conceptual quality and excellent craft quality. CreativeDirector should be able to diagnose: *"Beautifully written solution to a mediocre idea."*

## Primary vs secondary classification

Every object gets a **primary type**. A **secondary type** is optional.

Use secondary classifications only when genuinely useful. Do not classify everything as a hybrid to avoid making a decision.

Also identify:

- **Parent:** what larger creative system does this belong to?
- **Job:** what specifically must this object accomplish?

---

## V1 taxonomy

### 01 · Brand concept / brand platform

**Job:** Define the enduring organizing idea, territory or meaning the brand can credibly own over time. This sits above individual campaigns.

**Primary success criteria:** brand truth, strategic durability, distinctiveness, emotional territory, cultural relevance, simplicity, ownability, longevity, flexibility, generativity.

**Ask:**
- Can this survive multiple campaigns?
- Can it influence communications, behavior, design, voice, experience and potentially product decisions?
- Does it give the brand a recognizable worldview?
- Is it broad enough to endure but specific enough to own?

**Failure modes:**
- campaign idea pretending to be brand platform
- proposition pretending to be worldview
- generic purpose statement
- vague emotional territory
- category cliché
- fashionable positioning with no longevity

### 02 · Campaign platform

**Job:** Create a generative creative rule capable of producing a coherent family of ideas and executions.

**Primary success criteria:** central creative idea, strategic tension, generativity, extensibility, coherence, brand ownership, visual potential, verbal potential, media elasticity, audience relevance.

**Ask:**
- Can this produce many genuinely different executions?
- Does it have recognizable campaign DNA?
- Can different creative teams create new expressions without breaking it?
- Does each execution reveal another dimension rather than repeat the same joke?

**Failure modes:**
- one execution pretending to be platform
- tagline pretending to be platform
- broad theme with no creative rule
- endless repetition of one mechanic

### 03 · ADLOB / advertising idea

> **Provisional terminology.** "ADLOB" is CreativeEngine's internal shorthand for a discrete advertising idea or conceptual advertising thought. It is not assumed to be universal industry terminology.

**Job:** Deliver one strong conceptual advertising thought.

**Primary success criteria:** Post-it simplicity, strategic relevance, conceptual leap, surprise, originality, brand necessity, memorability, visual/verbal potential, elegance.

**Ask:**
- Can I explain the idea simply?
- Where is the leap?
- Does the audience mentally participate?
- Why this brand?

**Failure modes:**
- execution without idea
- strategy presented as concept
- visual gag without brand relationship
- cleverness without meaning

### 04 · Tagline / endline

**Job:** Compress enduring brand or campaign meaning into a memorable verbal signature.

**Primary success criteria:** compression, memorability, rhythm, distinctiveness, ownability, meaning, longevity, tonal fit, flexibility.

**Ask:**
- Does it become stronger beside the brand name?
- Could a competitor plausibly use it?
- Can people remember it?
- Does repeated use make it richer?

**Failure modes:**
- generic aspiration
- proposition disguised as tagline
- meaningless three-word phrase
- forced cleverness
- trendy language with no shelf life

### 05 · Slogan

**Job:** Create a memorable, repeatable campaign, movement or promotional phrase. Distinguish it from an enduring brand endline when useful.

**Primary success criteria:** memorability, cadence, clarity, repetition value, campaign relevance, distinctiveness, audience participation potential.

A slogan may be deliberately more tactical or campaign-specific than a brand tagline.

### 06 · Headline

**Job:** Make someone stop, think, feel, understand or reinterpret.

**Primary success criteria:** stopping power, idea density, clarity, surprise, rhythm, tension, specificity, brand relevance, visual relationship when applicable.

When the headline works with a visual, apply the 1 + 1 = 3 test where relevant (see `creative-trajectory-evaluation.md`, section 10).

**Ask:**
- Does the line contribute something the image does not?
- Does it reward attention?
- Can another word disappear?

**Failure modes:**
- captioning the image
- strategy restatement
- clickbait
- generic cleverness
- headline-shaped body copy

### 07 · Body copy

**Job:** Reward sustained attention and deepen persuasion, emotion, information or story.

**Primary success criteria:** opening, voice, flow, clarity, rhythm, specificity, progression, persuasion, humanity, ending, editing discipline.

**Ask:**
- Does every paragraph earn the next?
- Does it reveal something beyond the headline?
- Is the voice recognizably this brand?

**Failure modes:**
- corporate filler
- headline repetition
- adjective accumulation
- unnecessary explanation
- generic brand voice

### 08 · Manifesto

**Job:** Articulate a distinctive worldview with emotional momentum.

**Primary success criteria:** point of view, conviction, rhythm, escalation, specificity, emotional truth, originality, quotability, ending.

> **Warning.** AI and advertising frequently abuse manifesto form.

**Ask:**
- Does this brand actually have something worth declaring?

**Failure modes:**
- empty inspiration
- generic empowerment
- dramatic line breaks hiding weak writing
- "we believe" without a distinctive belief
- universal human statements any brand could claim

### 09 · Mission tactic

> **Provisional definition.** A focused action or execution designed to accomplish a specific strategic mission inside a larger campaign or brand system.

**Job:** Solve one defined communication or behavioral objective.

**Primary success criteria:** mission clarity, strategic usefulness, efficiency, contextual intelligence, audience behavior, channel fit, contribution to parent platform.

**Ask:**
- What precise job does this tactic perform?
- Would the larger system be weaker without it?

Do not require every mission tactic to become famous.

### 10 · Execution

**Job:** Express an approved concept in a particular manifestation.

**Primary success criteria:** fidelity to concept, craft, clarity, freshness, channel fit, detail, consistency, audience experience.

**Ask:**
- Does this execution make the parent idea stronger?

**Failure modes:**
- decoration
- concept drift
- overproduction
- unnecessary cleverness
- technically correct but lifeless adaptation

Do not reward an execution for accidentally inventing a different strategy.

### 11 · Integrated brand campaign

**Job:** Create a coherent creative system across multiple audience touchpoints.

**Primary success criteria:** organizing idea, coherence, channel-specific intelligence, meaningful variation, cumulative impact, audience journey, brand consistency, participation where relevant, cultural permeability where relevant, execution quality.

Integrated does **not** mean "the same visual resized into many formats."

**Ask:**
- Does each channel contribute something useful or unique?
- Does the whole become greater than the pieces?

### 12 · Guerrilla

**Job:** Use context, environment, behavior or unconventional placement as part of the creative idea itself.

**Primary success criteria:** contextual intelligence, surprise, simplicity, environmental relevance, brand relevance, feasibility, audience reaction, earned attention potential where appropriate.

**Ask:**
- Would the idea still work exactly the same somewhere else? If yes, the environment may not actually be part of the idea.

**Failure modes:**
- random installation
- inconvenience disguised as creativity
- shock without relevance
- fake guerrilla made primarily for a case-study film

### 13 · Stunt / brand act

**Job:** Make the brand *do* something meaningful, provocative, entertaining or useful.

**Primary success criteria:** conceptual necessity, courage, authenticity, brand ownership, participation where relevant, cultural relevance, real-world consequence, earned attention potential.

**Ask:**
- Why does this brand have permission to do this?
- Would the act matter without the case-study video?
- Does the act itself contain the idea?

**Failure modes:**
- PR bait
- celebrity dependency
- expensive spectacle without meaning
- technology demonstration
- fake social experiment
- manufactured controversy

### 14 · Hero graphic / key visual

**Job:** Compress a brand or campaign idea into one immediately powerful visual expression.

**Primary success criteria:** visual concept, stopping power, immediate comprehension, composition, typography, image-making, distinctiveness, brand ownership, scalability, memorability.

**Ask:**
- Can someone understand or feel the idea quickly?
- Does it survive without explanatory copy?
- Could it anchor a larger visual system?

**Failure modes:**
- moodboard aesthetic
- decorative key art
- generic AI imagery
- visual complexity without hierarchy
- logo dependency

### 15 · Visual identity / design system

**Job:** Create a coherent visual language capable of producing recognizable brand expression over time.

**Primary success criteria:** distinctiveness, system logic, typography, color, composition, image language, flexibility, consistency, scalability, recognizability, longevity, cultural appropriateness.

**Ask:**
- Is this actually a system, or merely a look?
- Can different designers create new work from its rules?
- Can it flex without losing identity?

### 16 · Social / channel-native idea

**Job:** Create an idea whose behavior makes sense specifically within a platform, community, medium or format.

**Primary success criteria:** native behavior, cultural fluency, participation, timing, shareability when relevant, voice, format intelligence, brand relevance.

**Ask:**
- Why does this belong *here*?

**Failure mode:**
- campaign advertising merely resized or rewritten for social

### 17 · Experiential / activation

**Job:** Create an experience people participate in rather than merely observe.

**Primary success criteria:** participant role, experience design, behavioral insight, emotional payoff, simplicity of participation, brand relevance, memorability, amplification potential where relevant.

**Ask:**
- What does the participant actually *do*?
- What do they receive emotionally, socially or practically?

---

## Parent / child hierarchy

These are conceptual maps, not mandatory production structures.

**Visual and media expression:**

```
BRAND PLATFORM
    ↓
CAMPAIGN PLATFORM
    ↓
ADVERTISING IDEA
    ↓
EXECUTION
    ├── HERO GRAPHIC
    ├── FILM
    ├── OOH
    ├── SOCIAL
    └── ACTIVATION
```

**Verbal expression:**

```
BRAND PLATFORM
    ↓
CAMPAIGN PLATFORM
    ↓
VERBAL SYSTEM
    ├── TAGLINE
    ├── SLOGAN
    ├── HEADLINES
    ├── BODY COPY
    └── MANIFESTO
```

## Parent / child consistency test

For child work, ask:

- Does it strengthen the parent?
- Does it reveal a new dimension?
- Does it merely repeat the parent?
- Does it contradict the parent?
- Is the child substantially more interesting than the supposed platform?

If every execution requires a different conceptual explanation, the parent platform may not actually be generative.

## Misclassification test

Actively detect:

- tagline pretending to be platform
- tactic pretending to be strategy
- stunt pretending to be cultural idea
- visual style pretending to be art-direction concept
- manifesto pretending to be brand purpose
- headline pretending to be campaign
- collection of media placements pretending to be integration
- moodboard pretending to be design system
- product feature pretending to be insight
- case study pretending to be idea

When detected, **name the misclassification**. Then identify what the object actually is.

## Type-specific weighting

Do not use one universal scorecard. Different objects emphasize different criteria. Examples:

| Object | High relevance | Low / conditional relevance |
|---|---|---|
| Tagline | memorability, compression, ownability, longevity | cultural permeability, channel innovation |
| Hero graphic | visual concept, composition, stopping power, recognizability | body-copy persuasion |
| Campaign platform | strategic tension, generativity, brand ownership, extensibility, creative potential | — |
| Body copy | voice, progression, clarity, rhythm, persuasion | — |
| Stunt / brand act | act necessity, cultural relevance, authenticity, participation, real-world consequence | — |

## Ambition eligibility

`creative-direction-audit.md` should not automatically apply to every object. That framework's section 1 defers to this list.

**Likely eligible:**
- campaign platform
- major advertising idea
- integrated campaign
- brand act
- guerrilla
- experiential
- significant channel-native idea
- major brand concept, when relevant

**Usually unnecessary:**
- individual headline
- body copy
- minor execution
- adaptation
- production task

A brilliant headline is allowed to simply be a brilliant headline.

## Classification output

For serious evaluation, the taxonomy may return:

```
OBJECT TYPE:            [primary]
SECONDARY TYPE:         [only when useful]
PARENT:                 [larger system, or NONE]
JOB TO BE DONE:         [one sentence]
SUCCESS LOOKS LIKE:     [one sentence]
PRIMARY CRITERIA:       [small relevant set]
APPLICABLE FRAMEWORKS:  [only ACTIVE frameworks]
```

Do not manufacture framework names. Consult the framework registry in the root `CLAUDE.md`.

## Boundaries

This taxonomy classifies. It does not automatically:

- score the work
- determine Cannes-style ambition
- generate copy
- generate visual design
- replace CreativeDirector judgment

It routes the work toward the correct evaluation and generation methods.
