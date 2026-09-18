# Brief Normalization

> CreativeEngine shared framework. Owned by `brief-machine`. Used by `creative-engine-director` for brief readiness and routing, and read by any department that receives a work packet.

Real briefs arrive as working documents that mix facts, strategy, audiences, targeting, proof, creative suggestions, funnel instructions, deliverables, constraints and unresolved claims. CreativeEngine does not create from that document directly. It normalizes it first.

## Related frameworks

This framework sits upstream of the creative frameworks. It organizes and interprets the brief; it does not evaluate creative work.

| Framework | Relationship |
|---|---|
| `creative-object-taxonomy.md` | Downstream. The deliverable matrix names formats; the taxonomy classifies what a deliverable is when that affects the criteria. |
| `hey-whipple-copycraft.md`, `creative-trajectory-evaluation.md`, `creative-direction-audit.md` | Downstream. Creative work and ambition judgment start from a normalized brief or a work packet, never from the raw source. |
| `education-enrollment-intake.md` | Optional extension to this framework. Load it only when the assignment concerns education, training or institutional communication, and only for intake fields. It adds questions and field definitions; it changes no rule here. |

The framework registry in the root `CLAUDE.md` is the source of truth for what exists.

---

## 1. Four layers

```
RAW SOURCE         what the client, strategist, agency or media plan actually supplied
NORMALIZED BRIEF   the same information, reorganized and labeled
DERIVED LAYER      conclusions CreativeEngine draws from the source
CREATIVE WORK      ideas generated after normalization
```

These layers are not interchangeable. Each one points back to the layer above it. None replaces it.

```
NORMALIZE FIRST.  INTERPRET SECOND.  CREATE THIRD.
```

BriefMachine owns the first two steps. It does not do the third.

The derived layer holds two kinds of interpretation, always labeled DERIVED and always kept apart from source content:

| Derived work | When |
|---|---|
| **Audience intelligence** (section 12) | When the source contains enough audience or targeting data to show patterns, or when asked |
| **Strategy improvement** | Only when the user or CreativeDirector requests it |

Elsewhere in CreativeEngine, an **optimized brief** means a normalized brief plus any requested strategy improvement.

## 2. What normalization is for

Its first job is epistemic clarity:

```
WHAT DID THE SOURCE ACTUALLY SAY?
WHAT TYPE OF INFORMATION IS IT?
HOW CERTAIN IS IT?
WHAT IS MISSING?
WHAT SHOULD CREATIVE USE?
```

**Normalization may:**

- reorganize, group and deduplicate
- separate a portfolio into offerings and a journey into funnel states
- turn repeated deliverables into a matrix
- label provenance and claim status
- quote the source exactly
- expose gaps, conflicts and strategic weaknesses

**Normalization must not:**

- improve, sharpen or reinterpret the source's strategy. Interpretation belongs only in the derived layer, labeled.
- resolve a conflict by choosing a side
- mark a claim verified without reviewed evidence, or make a claim more specific, larger, more certain or more comparative than the source
- promote a source-suggested idea into strategy
- generate territories, concepts, headlines, taglines, names, visual ideas or example copy, including "illustrative" ones
- evaluate, rank, extend or improve the source's creative suggestions
- drop source content silently. Anything meaningful lands in a section, or in open questions if it fits nowhere.

**Fidelity rule.** Quote exactly wherever the wording is the substance: mandatories, CTAs, claims, legal lines, prohibited language, positioning statements, targeting signals and source-suggested creative. Paraphrase only to organize.

## 3. The raw source stays intact

The raw source is evidence. The normalized brief is an organization layer on top of it.

```
RAW SOURCE  →  NORMALIZED REPRESENTATION
```

not:

```
RAW SOURCE  →  REWRITTEN SOURCE THAT REPLACES IT
```

- Never edit, overwrite, rename or delete raw source material.
- When a new version of the source arrives, keep both. The normalized brief records which version it was built from.
- Write files only when the user or main session asks. Otherwise return the normalized brief inline.

When files are written, use the project's folder in the client workspace (`projects/README.md`):

```
projects/<client>/<project>/
  raw/                  source material as received; never edited
  normalized-brief.md   the master working brief
  packets/              work packets, one file per packet
```

## 4. Provenance

Two questions are kept apart:

1. What kind of information is this, and who said it? (provenance labels, below)
2. For anything that could appear in advertising, how well supported is it? (claim status, section 5)

Merging them causes errors. A fact stated confidently in a brief is not thereby verified.

| Label | Meaning |
|---|---|
| **SOURCE FACT** | Stated as fact in the supplied material. Operational or contextual: offering names, dates, budget, formats, schedules, media targeting parameters. |
| **SOURCE STRATEGY** | Strategic direction supplied by the source: objectives, positioning, audience definitions, message priorities, asserted insights. |
| **SOURCE REQUIREMENT** | A mandatory instruction: deliverable, CTA, format, legal line, constraint, prohibited language. |
| **SOURCE HYPOTHESIS** | A recommendation or suggestion: possible territory, example line, suggested creative direction, "consider" or "could" statements. |
| **DERIVED** | Concluded by CreativeEngine rather than stated by the source. Always show the basis. |
| **OPEN** | Missing, conflicting or ambiguous. See section 10. |

- **Author.** When the source mixes authors, record who said it: `client`, `agency`, `media plan` or the named document, for example `SOURCE STRATEGY · agency`. A client strategy is a direction. An agency strategy is a recommendation.
- **Label where it matters.** Section placement carries the default label: everything under Mandatories is SOURCE REQUIREMENT, everything under Source-suggested creative is SOURCE HYPOTHESIS, everything in the derived layer is DERIVED. Tag inline only in mixed sections (master strategy, offering briefs) and wherever confusing fact, recommendation and inference would change the creative work. Do not decorate every line.
- **When unsure,** choose SOURCE HYPOTHESIS over SOURCE STRATEGY, and put a fact in the claim ledger rather than leaving it as context.
- Any fact that could appear in advertising goes into the claim ledger, whatever its label.
- An insight the source asserts about people ("our audience feels stuck") is SOURCE STRATEGY. Record its evidence basis, or "none given".

### Source-only and derived fields

Some fields are authoritative: downstream agents treat what they contain as what the client or source established.

**Source-only fields:** anything labeled SOURCE FACT, SOURCE STRATEGY or SOURCE REQUIREMENT · Assignment & scope · Objectives · Mandatories & constraints · claim wording, in the ledger and in any proof field · the deliverable matrix's formats, quantities, message jobs and CTAs · the handoff's CREATIVE PROBLEM(S), WHAT MUST BE TRUE, BEST AVAILABLE PROOF and MANDATORIES · the packet's source-grounded core (section 15).

- They contain only material stated in the raw source, inherited from the master level (section 6), or taken from a resource marked REVIEWED (section 11), which is then named.
- Nothing BriefMachine concludes, reframes or decides as a precaution enters a source-only field, even with a DERIVED label beside it.
- A pointer is not inference. "Not supplied by source", "Not clearly supplied" and "CONFLICT, see Q3" are allowed and expected where the source is silent or contradicts itself.

**Derived fields:** the derived layer (schema section 16) · every pattern-record field except SOURCE SIGNALS · PRIMARY TENSION unless the source states one · DO NOT ASSUME · SAFE HANDLING UNTIL RESOLVED · the packet's derived layer: communication hypothesis and creative stimulus.

- Every interpretation, reframing, inference or precaution BriefMachine produces lives in a derived field, with its basis.
- A derived field may quote source material as its basis. It never copies its conclusion back into a source-only field.

```
"No pricing was supplied, so do not imply affordability"
   is SAFE HANDLING UNTIL RESOLVED (derived, cites its question),
   not WHAT MUST BE TRUE (the source never required it).
```

## 5. Proof & claim ledger

One ledger for the whole brief.

| ID | Claim (exact source wording) | Applies to | Status | Source | Needed before use | Creative use |
|---|---|---|---|---|---|---|

| Status | Meaning | Creative use |
|---|---|---|
| **VERIFIED** | Supported by authoritative material that was actually reviewed, or explicitly confirmed as approved by the client. The ledger names that material. | Use as stated, within what the evidence says. |
| **SOURCE-STATED** | Asserted in the supplied material. No supporting evidence reviewed. | May shape strategy and exploration. Confirm before presenting or publishing as fact. |
| **PENDING APPROVAL** | The source says it needs client approval. | Keep out of work shown externally until approved. |
| **CONDITIONAL** | True only under a stated condition (schedule, eligibility, location, start date, offering). | Use only with its condition. |
| **OUTCOME CLAIM** | Promises a result for the audience, such as career advancement, earnings or time saved, without reviewed supporting data. | Qualitative and hedged only. Never quantified, guaranteed or comparative. |

- Being written in the brief is not verification. Most claims in a raw brief start as SOURCE-STATED.
- Do not invent verification. If no supporting data was supplied, write "none supplied".
- An outcome claim backed by reviewed data is VERIFIED, and its use is limited to what that data says.
- **Claim-drift rule.** Neither normalization nor later creative work may make a claim more specific, larger, more certain or more comparative than its status allows. "Potential for increased earning power" does not become "graduates earn X% more" without VERIFIED data.
- A number attributed to an unreviewed source ("22%, per agency research") stays SOURCE-STATED and is raised as an open question.
- A status changes only when evidence or approval arrives. Record what changed it.

Downstream agents treat anything below VERIFIED as a claim requiring caution.

## 6. Offering hierarchy

Do not flatten a multi-offering brief into one proposition.

An **offering** is anything with its own audience, proposition or proof: a program, product, service, line or sub-brand.

```
PROJECT
├── MASTER LEVEL   shared objective, brand, voice, audience context, funnel model, constraints
└── OFFERINGS
    ├── 01 [offering]   audience · targeting signals · need · positioning · offering truth ·
    │                   proof · differentiation · funnel and CTA overrides · open questions
    └── 02 [offering]   ...
```

- Offerings inherit master-level content. State only what differs, and mark overrides explicitly, for example "overrides master CTA rule, see Q3".
- Do not copy master content into every offering.
- Relationships between offerings (shared audience, overlap, priority) belong in the offering architecture. If priority is not stated, that is OPEN.
- A single-offering brief collapses the hierarchy. There is no master / offering split.

## 7. Audience, targeting and funnel state

Three things are recorded separately:

```
STRATEGIC AUDIENCE   who the source says the offering is for          SOURCE STRATEGY
TARGETING SIGNALS    what the media plan explicitly targets           SOURCE FACT · media plan
FUNNEL STATE         where the person is in the decision journey      SOURCE FACT or SOURCE STRATEGY
```

**Audience and funnel state are different dimensions.**

```
AUDIENCE       who the person is: identity, situation, need, barrier
FUNNEL STATE   what they have already done
```

- Describe funnel states by behavior ("started an application, has not submitted"), never by demographics.
- Describe audiences by identity and situation, never by funnel position.
- A creative problem sits at the intersection of the dimensions the assignment uses, most often **offering × audience × funnel state**. Others, such as occasion, channel, format, market or message job, may define it too. Record the dimensions the source actually uses; do not invent a missing one.
- **Funnel state is optional.** Record it only where the source establishes a journey. Many assignments have none: a launch, a brand message, a publication, an institutional or internal communication may sit outside any funnel. Where the source defines no journey, say so once and omit the architecture below; do not construct a funnel to fill the section, and do not infer a stage from a channel, placement, format, goal or CTA.

**Targeting signals are audience evidence, not just media metadata.** Record them exactly, per offering and per funnel state where the source separates them. They feed audience intelligence (section 12). Where the targeting and the strategic audience definition describe different people, record an AMBIGUITY.

| Stage | Entry condition | Job | Default CTA | Legitimate levers | Source |
|---|---|---|---|---|---|

- **Legitimate levers.** Urgency, scarcity and deadlines are legitimate only when the underlying fact is a SOURCE FACT or VERIFIED. Otherwise they are OPEN.
- Offering-specific funnel or CTA rules are recorded as overrides in that offering's brief and checked against the master rule. A clash is a CONFLICT (section 10), not something to reconcile.

## 8. Deliverable matrix

Repeated execution information becomes one matrix.

| Problem | Offering | Funnel state | Format | Qty | Objective | Message job | CTA | Destination | Notes |
|---|---|---|---|---|---|---|---|---|---|

- Use the dimension columns the assignment needs: drop Funnel state where the source defines none; add occasion, market or channel where they define the problem.
- **Problem** groups the rows that share one creative problem. A new format usually adds an execution, not a problem. A new offering, audience or funnel job usually adds a problem.
- State the count: "N distinct creative problems, M executions."
- The matrix is an execution-routing layer. It does not replace the strategic brief, and a row does not require its own campaign idea.
- A mismatch between counts ("1–2 creative options" against a twenty-item list) is an open question.

### Goal, CTA, destination and measurement

Four different things are routinely collapsed into one. Keep them apart, in the matrix and in every packet that has an ask:

```
PRIMARY GOAL:                    what the source asks the communication to achieve
CTA WORDING:                     the exact words the audience sees
DESTINATION / ACTION LOCATION:   where the action happens
MEASURABLE SUCCESS EVENT:        the event that counts as success
MEASUREMENT DEFINITION / SOURCE: how that event is defined, and by what system
OPEN MEASUREMENT QUESTIONS:      Q# for anything above that the source leaves undefined
```

- **Preserve supplied CTA wording exactly.** Approved wording is a SOURCE REQUIREMENT. Unapproved wording is a SOURCE HYPOTHESIS. No CTA wording is written here.
- A goal is not a CTA, a CTA is not a destination, and none of them is a measured event. "Learn more" is CTA wording; the success event might be a landing-page view or a completed information request.
- **Do not convert a communication goal into a platform optimization setting or a verified conversion event.** A platform objective is recorded only where the source supplies it or it is verified, and it is labeled as the platform's setting, not as the creative goal.
- An intent is not a completion. A form opening is not a submission; a download button click is not a completed download; a booking is not attendance; a registration is not attendance; a form submission may not be a confirmed subscription; a started application is not a completed one; a completed application is not enrollment.
- A video completion needs a stated threshold. An engagement goal needs a named action: comment, share, save, click or another stated behavior.
- Where measurement is unspecified, record it as an open question. Do not invent tracking capability, attribution or a conversion definition.

### Channel, placement and format

Recorded separately, each only as far as the source establishes it:

```
CHANNEL / PLATFORM   where the work runs
PLACEMENT            the specific surface within it
CREATIVE FORMAT      what is actually made, with its specification
PLATFORM OBJECTIVE   the platform's own optimization setting; only where supplied or verified
```

- **A platform name is not a creative format.** "Social", "Meta", "search", "email" or any platform name establishes a channel, not a placement, a format, a ratio or a duration.
- Where the source names a channel but no placement or format, record those as not supplied, and make them an open question when they would change the work.
- Platform specifications, availability and objective names are external facts. Use them only from an official source, cited with its date; otherwise mark them UNVERIFIED. Do not reconstruct a platform's current specification from memory.
- An ambiguous channel name is an AMBIGUITY (section 10), not something to interpret. Record the possible readings and ask.

## 9. Source-suggested creative

Includes territories, platform lines, headlines, taglines, example executions and "strongest territory" recommendations supplied in the brief.

- Record each one with its exact wording, author, what it applies to, and what the source claims for it.
- They are **input to consider, not a creative boundary**.
- Never move them into master strategy, positioning, proposition or the handoff's creative problem.
- When source positioning and a suggested territory share words, keep the positioning (SOURCE STRATEGY) and the territory (SOURCE HYPOTHESIS) as separate entries, and note the overlap.
- When a so-called "messaging territory" is plainly a priority about what to say (which proof to lead with), record the priority as `SOURCE STRATEGY · agency` and keep its wording out of the creative territory list. If this is not plain, treat it as a hypothesis.

**Downstream.** EXPLORE generates its own territories. Source hypotheses may be considered, tested, or developed when specifically requested. They do not count toward exploration's territories. CreativeDirector may withhold them from a first exploration round to avoid anchoring. Only the user can make a source-suggested idea mandatory; it then becomes a SOURCE REQUIREMENT, with that instruction noted.

## 10. Open questions, conflicts and ambiguities

| Type | Meaning |
|---|---|
| **CONFLICT** | Two source statements cannot both hold. |
| **AMBIGUITY** | A statement can reasonably be read more than one way. |
| **GAP** | Information the creative work needs is missing. |

Detect rigorously; triage by consequence. Every issue gets a priority from what happens downstream if it stays open, not from its type. A CONFLICT can be minor; a GAP can stop the work.

| Priority | Meaning | BLOCKS |
|---|---|---|
| **BLOCKER** | The affected creative work cannot proceed safely until it is resolved. | WORK |
| **CLAIM BLOCKER** | Exploration may proceed, but a specific claim, fact or lever cannot be used until resolved or verified. | CLAIM USE |
| **IMPORTANT** | Blocks nothing yet, but could materially change strategy, execution or approval. | APPROVAL or NOTHING YET |
| **MINOR** | Worth recording. Leaving it open changes nothing downstream yet. | NOTHING YET |

- A blocker blocks only the problem IDs it names. One offering's CTA conflict does not block another offering.
- A claim whose only issue is its ledger status needs no separate question; the ledger already restricts it. Raise a CLAIM BLOCKER only when someone must act (supply evidence, grant approval, confirm scope), and cite the ledger ID rather than restating the claim.
- An issue keeps its ID if its priority changes.

**Primary view.** BLOCKER, CLAIM BLOCKER and IMPORTANT issues are recorded in full, in that order, so the decisions needing human attention come first:

```
Q#  PRIORITY · TYPE
QUESTION:                     [the decision someone must make]
SOURCE SAYS:                  [exact wording of each side, or "not supplied"]
AFFECTS:                      [problem IDs, offerings, funnel states, deliverables, claim IDs]
BLOCKS:                       WORK / CLAIM USE / APPROVAL / NOTHING YET
SAFE HANDLING UNTIL RESOLVED: [optional; DERIVED; what creative must avoid meanwhile]
OWNER:                        [client / agency / media / internal / unknown]
```

- OWNER is who the source says will resolve it ("client to confirm"). If the source does not establish one, write "unknown". Do not guess.

**Grouped minor issues.** MINOR issues follow as one list, one line each. They are compressed, not dropped:

```
MINOR SOURCE GAPS
- Q#  [issue, with source wording where it matters]  (affects ...)
```

- Do not resolve. Safe handling is DERIVED (section 4). It may restrict what creative does, for example "no quantified earnings claims until data arrives". It may not choose one side of a conflict.
- Weak strategy is recorded here, not fixed: a weak proposition, a generic audience, conflicting objectives, unclear priority, excessive deliverables.

Checks worth running, without printing them as a checklist:

- **Scope vs maturity:** "not an awareness campaign" against an offering few people know exists.
- **Counts:** option counts against listed deliverables.
- **Global vs specific:** master rules against offering exceptions (CTAs, tone, formats).
- **Ambition vs evidence:** outcome promises without data.
- **Levers vs facts:** urgency or scarcity without current, source-established support, or a deadline or availability constraint applied outside its documented scope.
- **Strategy vs targeting:** the media plan targets people the strategic audience does not describe, or the reverse.
- **Priority:** which offering, stage or format matters most, when unstated.
- **Mandatories vs each other:** tone against required claims, format against required copy.

## 11. Resource registry

| ID | Resource | Referenced in | Availability | Role | Depends on it |
|---|---|---|---|---|---|

| Availability | Meaning |
|---|---|
| **REVIEWED** | Opened and read during normalization. |
| **AVAILABLE, NOT REVIEWED** | Accessible, but not read. |
| **REFERENCED, NOT AVAILABLE** | Mentioned, but not supplied or not accessible. |

| Role | Meaning |
|---|---|
| **REQUIRED BEFORE CLAIM USE** | One or more claims depend on it. |
| **REQUIRED BEFORE WORK** | Creative work cannot sensibly start without it. |
| **SUPPORTING** | Useful, not required. |

- Never mark a resource REVIEWED unless its content was actually opened. Never describe the contents of a resource that was not read.
- Link the claims and questions that depend on each resource.

## 12. Audience intelligence

A derived step. Media targeting is not only operational metadata: patterns across targeting and audience signals can suggest useful hypotheses about how to communicate. They remain hypotheses.

### Evidence levels

```
TARGETING SIGNAL      what the media plan explicitly targets             SOURCE FACT · media plan
PATTERN               a relationship visible across several signals       DERIVED
CREATIVE HYPOTHESIS   a plausible communication implication of a pattern  DERIVED
HUMAN TRUTH           a behavioral or emotional assertion about people    needs evidence beyond targeting
```

Do not collapse these levels. Targeting data can support a pattern and a hypothesis. On its own, it cannot establish a human truth.

```
MULTIPLE SIGNALS MAY SUPPORT A HYPOTHESIS.
A TARGETING LABEL ALONE DOES NOT DEFINE A PERSON.
```

### When to run it

- As set in section 1.
- When the data is sparse, skip it and say so. Do not inflate a handful of labels into a persona.
- Inspect the actual source signals before concluding anything. No pattern without its listed signals.

### What to look across

Psychographic description, demographics, education, field of study, industry, interests, geography, offering selected, funnel state, and the source's strategic audience definition.

The aim is communication-relevant patterns, not demographic personas. Useful hypotheses may concern professional identity, career stage, ambitions, decision pressures, category familiarity, educational orientation, industry, geographic or life-stage context, value sensitivity, advancement orientation, specialization interests, and likely barriers or motivations.

### Pattern record

```
AUDIENCE PATTERN:            [the pattern]
SOURCE SIGNALS:              [exact signals, and where each appears]
POSSIBLE MOTIVATION:
POSSIBLE TENSION:
POSSIBLE BARRIER:
COMMUNICATION IMPLICATION:
CREATIVE STIMULUS:           [questions, not answers]
CONFIDENCE:                  HIGH / MEDIUM / LOW, with its basis
DO NOT ASSUME:
WOULD STRENGTHEN OR REVISE:  [evidence that would test it]
```

Only SOURCE SIGNALS is source material. Every other field is DERIVED and is never presented as a source fact.

| Confidence | Basis |
|---|---|
| **LOW** | One signal, or signals that do not clearly agree. |
| **MEDIUM** | Several consistent signals that also agree with the source's strategic audience definition. |
| **HIGH** | Corroborated by evidence beyond targeting: research, CRM, enrollment or performance data, interviews, or client knowledge with a stated basis. |

Targeting metadata alone never reaches HIGH.

### Funnel-sensitive interpretation

The same audience pattern does not produce the same message at every funnel state. The audience may not have changed; the communication job has. For example, an advancement-oriented pattern may imply:

| Funnel state | Communication job for the same pattern |
|---|---|
| Early (inquiry) | Why this particular offering is worth the move |
| Mid (application started) | Reduce hesitation; reconnect the unfinished action to the goal |
| Late (applied, not enrolled) | Shift from "why do this at all?" to "why this provider over the alternatives?" |

### Cross-offering comparison

In a portfolio, compare patterns across offerings, using the actual source data:

| Finding | Meaning |
|---|---|
| **SHARED** | Patterns common to several offerings. Useful at master level. |
| **OVERLAP** | Shared signals that must not be mistaken for differentiation. Often category signals. |
| **DISTINCTIVE** | Patterns that should change the communication by offering. |
| **OUTLIER** | A signal or pattern that may reveal a distinctive opportunity. |

Signals every offering shares (for example postgraduate interest, a broad industry, college education, career advancement) are probably category signals, not distinctive creative territory. Narrower signals (a specific exam, a specialist field, a particular career transition) may point to offering-specific communication.

### Communication opportunity

Audience intelligence may state a communication opportunity, built with this forcing model:

```
OFFERING TRUTH  +  FUNNEL MOMENT  +  AUDIENCE PATTERN  +  RELEVANT PROOF  (+ CONTEXT)
                              =  COMMUNICATION STRATEGY
```

It is a forcing model, not a literal formula. The inputs:

| Input | Question |
|---|---|
| Offering | What is this person considering? |
| Funnel state | What decision have they already made? |
| Audience pattern | What motivations or pressures appear relevant? |
| Proof | What can the brand credibly offer this audience? |
| Context | Where and how will the communication appear? |

- The opportunity says **what to address**: what to spend less effort on, and which needs, barriers and proof to explore. It never says how to say it: no lines, concepts or territories.
- Seek meaningful specificity, not superficial personalization such as swapping in a job title.
- It stays a hypothesis until research, CRM evidence, client knowledge or performance data supports it.

### Creative stimulus

Audience intelligence feeds EXPLORE as provocation, not as an answer. For example:

- What professional transition is this audience trying to make?
- What are they unwilling to sacrifice to make it?
- What does "advancement" specifically mean for this group?
- What proof would make that advancement credible?
- What category assumption might this audience already reject?
- What does this offering understand about their situation that competitors may not?
- What tension exists between where they are and where they want to be?
- What would make this feel written for them rather than for the category's generic customer?

### Stereotype guardrail

- Never infer personality, income, intelligence, family status, politics, emotional state, health or other unsupported traits from age, geography, education, industry, interests or platform targeting categories.
- An advertising-platform category is not a psychological truth.
- Every pattern carries a DO NOT ASSUME line naming what the pattern does not tell us about individuals.

### Evidence over time

Targeting data is one evidence source, not the final word. Future inputs may strengthen or revise patterns: CRM data, search behavior, campaign and media performance, qualitative research, interviews, enrollment data, audience surveys, social listening, client knowledge and previous creative response.

When new evidence arrives, update the pattern's confidence and record what changed it. A pattern corroborated beyond targeting may support a human truth. A contradicted pattern is revised or dropped.

```
MORE EVIDENCE  →  BETTER AUDIENCE PATTERN  →  SHARPER COMMUNICATION STRATEGY  →  MORE SPECIFIC CREATIVE STIMULUS
```

without confusing inference with fact.

## 13. Canonical schema

Markdown is the authoritative working format. Section numbers in this section and the next two refer to the schema below, not to this framework. Omit schema sections that are empty, except the claim ledger, mandatories, source-suggested creative, open questions, resource registry and handoff: they are always present, with "None supplied" when empty. Absence is information.

```markdown
# Normalized Brief: [Project]

| | |
|---|---|
| Client | [as the source or user establishes it; or "not stated"] |
| Project | [as the source or user establishes it; or "not stated"] |
| Sources | [each source: path or "pasted in conversation, <date>"; scope CLIENT-LEVEL / PROJECT-LEVEL / UNKNOWN] |
| Normalized by | brief-machine, <date> |
| Status | DRAFT / CONFIRMED BY USER |
| Derived layer | NONE / audience intelligence / strategy improvement (section 16) |
| Resources not reviewed | [IDs from section 15] |

## 1. Project identity
Client, master brand, project, markets, timing, budget if supplied.

## 2. Assignment & scope
What the source asks CreativeEngine to do, in its own words. In scope / out of scope.

## 3. Objectives
### 3.1 Business / marketing objective
### 3.2 Creative / communication objective
If the source gives none, say so. Do not write one.

## 4. Offering architecture
The offerings, how they relate, any stated priority.

## 5. Audience architecture
Master audience context. Per offering: strategic audience (source wording) and
targeting signals (exact). Detail lives in section 8; interpretation in section 16.

## 6. Funnel architecture
Stage · entry condition · job · default CTA · legitimate levers · source.
Omit where the source establishes no journey; one line says so.

## 7. Master strategy
Source strategy that applies to every offering, labeled.

## 8. Offering briefs
### 8.1 [Offering]
- Strategic audience (source wording)
- Targeting signals (exact)
- Prospect need / barrier
- Positioning (source wording)
- Offering truth
- Proof (ledger IDs)
- Differentiation
- Funnel and CTA overrides
- Open questions (IDs)

## 9. Proof & claim ledger

## 10. Brand, tone & voice
Tone, prohibited language (exact), visual resources and rules.

## 11. Mandatories & constraints

## 12. Deliverable matrix
Ends with: N distinct creative problems, M executions.

## 13. Source-suggested creative
Input to consider, not a creative boundary.

## 14. Open questions, conflicts & ambiguities
Primary view (BLOCKER, CLAIM BLOCKER, IMPORTANT), then MINOR SOURCE GAPS.

## 15. Resource registry

## 16. Derived layer
Everything here is DERIVED. Nothing here is source fact.
### 16.1 Audience intelligence
Pattern records, cross-offering comparison, communication opportunities.
Or: "Not run: targeting data too sparse" / "Not run: no audience data".
### 16.2 Strategy improvement
Empty unless requested. Each item: its basis, and what source content it adds to or changes.

## 17. CreativeEngine handoff
```

## 14. CreativeEngine handoff

The last section of every normalized brief. It tells downstream agents what they may safely use.

```
SOURCE-GROUNDED   (source-only fields; framework section 4)
CREATIVE PROBLEM(S):      [one line per problem ID: what the source establishes, quoted;
                           or "Not clearly supplied"]
WHAT MUST BE TRUE:        [source requirements the work cannot violate]
BEST AVAILABLE PROOF:     [VERIFIED first; everything else with its status]
MANDATORIES:              [the few that shape the work; full list in section 11]

SOURCE-SUGGESTED IDEAS:   [SOURCE HYPOTHESIS; see section 13; input, not boundary]

DERIVED   (BriefMachine interpretation; never source truth)
PRIMARY TENSION:          [DERIVED with its basis, or OPEN. A tension the source itself
                           states is quoted and labeled SOURCE STRATEGY]
AUDIENCE HYPOTHESES:      [pattern IDs with confidence, or "not run"]
SAFE HANDLING UNTIL RESOLVED: [working guardrails, each citing its Q# or claim ID]
DO NOT ASSUME:            [claims, facts, audience traits and resolutions creative must
                           not take for granted]

QUESTIONS   (section 14 holds the full register)
BLOCKERS:                 [IDs, and the problem IDs each blocks]
CLAIM BLOCKERS:           [IDs, and the claim IDs each restricts]
IMPORTANT:                [IDs]
MINOR:                    [count only]
```

- The handoff hands over the problem. It contains no creative solution.
- It is not a readiness decision. CreativeDirector's brief readiness gate makes that call.

## 15. Creative work packet

A work packet is the focused brief for one creative task. Departments receive the smallest relevant packet, not the master brief, unless the task genuinely needs the whole assignment.

```markdown
# Work Packet: [the dimensions that define this problem, e.g. Offering · Funnel state · Format]

Client:        [from the normalized brief]
Project:       [from the normalized brief]
From:          [path or title of the normalized brief, date, status]
Source scope:  [the source scopes this packet draws on: project-level, and any client-level sources the brief cites]
Problem ID:    [from the deliverable matrix]
Mode:          [set by CreativeDirector]
[If a BLOCKER touches this packet, say so here, first.]

## Source-grounded core   (source-only fields; framework section 4)
OFFERING:
FUNNEL STATE:                       [stage and entry condition, where the assignment has one]
OTHER DIMENSIONS:                   [any others that define this problem: occasion, market,
                                     channel, message job; omit if none]
CHANNEL / PLACEMENT:                [as established; "not supplied" where it is not]
FORMAT(S):                          [with quantities; a platform name is not a format]
OBJECTIVE:
AUDIENCE:                           [strategic audience, source wording]
SOURCE PROBLEM / ASSIGNMENT:        [what the normalized source establishes for this
                                     problem, quoted; or "Not clearly supplied."]
SOURCE PROPOSITION / POSITIONING:   [source wording and label; or "Not clearly supplied."]
RELEVANT PROOF:                     [claim · status · creative use]
MANDATORIES:
PRIMARY GOAL:                       [what the source asks this communication to achieve]
CTA WORDING:                        [source wording, exact; an unresolved CTA cites its Q#]
DESTINATION / ACTION LOCATION:
MEASURABLE SUCCESS EVENT:           [source wording, or OPEN with its Q#]
MEASUREMENT DEFINITION / SOURCE:    [or OPEN with its Q#]
OPEN MEASUREMENT QUESTIONS:         [Q#s]
TONE:                               [short; prohibited language]

## Source-suggested territories   (SOURCE HYPOTHESIS)
[Input to consider, not a boundary. They do not count toward exploration's territories.
Or "withheld for first round".]

## Open issues for this packet
BLOCKERS:                           [only those that block this problem]
CLAIM RESTRICTIONS:                 [only claims and levers this problem could use]
IMPORTANT:                          [only those likely to change this problem]
SAFE HANDLING UNTIL RESOLVED:       [DERIVED; each guardrail cites its Q# or claim ID]
DO NOT ASSUME:
NOT IN THIS PACKET:                 [what was left out, and where to find it]

## Derived layer   (optional; everything below except media signals is DERIVED)
### Derived communication hypothesis
### Relevant media signals
### Observed patterns
### Potential motivations / barriers
### Creative stimulus               [questions and provocations, not answers]
### Confidence / evidence limits
### Do not assume
```

- A packet is a projection of the master brief, not a new brief. It adds no source content the brief does not contain.
- **Source problem.** Quote or closely track what the source establishes. Do not rewrite it into a stronger, sharper or more interesting problem. A better framing is a derived communication hypothesis, and lives only in the derived layer.
- **Derived communication hypothesis.** What the work might need to address, built with the forcing model in framework section 12, with its basis (pattern and claim IDs) and confidence. It says what to address, never how to say it.
- The only new material a packet may carry is derived-layer content narrowed to its offering and funnel state. Include the derived layer only when audience intelligence ran or strategy improvement was requested, and it adds meaningful insight. Otherwise one line says so.
- **Question filtering.** Carry only the blockers for this problem, the claim restrictions relevant to it, and the important issues likely to change it. MINOR issues and issues belonging to other offerings, funnel states or formats stay in the master register. Do not copy the whole register into a packet.
- **The ask block.** PRIMARY GOAL through OPEN MEASUREMENT QUESTIONS apply where the packet has an ask. Omit the block where it has none; a brand message or an institutional communication may have no action to measure. Never fill a field by inference: an undefined success event or measurement definition is OPEN, citing its Q#.
- Carry statuses and labels exactly as in the master brief.
- Normally one problem ID per packet.
- BriefMachine prepares packets. CreativeDirector decides which packet a task needs.

## 16. Framework principle

The brief is evidence. BriefMachine's first duty is to report it faithfully: what it says, how certain it is, and what it leaves open.

Creative ambition starts from there, not from the brief's first answers.
