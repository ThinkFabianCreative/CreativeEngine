---
name: creative-brief-craft
description: Write, sharpen, or review creative briefs using evidence-grounded human understanding, focused direction, and precise strategic language. Use for requested strategy improvement or brief critique after source normalization; do not use to silently rewrite source strategy during intake or to generate campaign concepts.
---

# Creative Brief Craft

Help BriefMachine produce briefs that are credible enough to trust, focused enough to guide, and interesting enough to inspire. CreativeDirector retains readiness and creative judgment.

This is an original synthesis informed by Jon Steel, Howard Ibach, and Mark Pollard. The lenses below are interpretive adaptations, not quotations, official frameworks, or an imitation of their voices. Apply the useful principles rather than performing a persona.

## Fit within CreativeEngine

Read the root `CLAUDE.md`, `BriefMachine/AGENT.md`, and `shared/frameworks/brief-normalization.md` before applying this skill. Read `projects/README.md` before accessing a client workspace. Resolve these paths from the CreativeEngine project root.

- Normalize raw material first using the existing framework. Preserve raw sources and source-only fields.
- A request to write, optimize, or strengthen strategy authorizes a separate DERIVED strategy-improvement layer. A request to normalize or extract material does not.
- In review mode, diagnose and recommend; do not silently implement strategic changes.
- Use the existing normalized-brief schema and work-packet format. This skill supplements them; it does not create a competing master brief.
- Work only from the current client's eligible sources. Carry source, claim, question, and pattern IDs through the work.
- Do not generate campaign territories, slogans, headlines, scripts, or visual concepts. BriefMachine defines the problem and direction; creative teams develop the expression.

## Three complementary lenses

### 1. Human understanding — informed by Jon Steel

Look for the behavior, circumstance, contradiction, or unmet need that makes the communication problem meaningful to a person. Connect research to a creative opportunity through interpretation, rather than summarizing everything collected.

Distinguish:
- **Observation:** what the evidence actually shows.
- **Interpretation:** what that observation may mean, with its basis and confidence.
- **Strategic implication:** what the communication could address because of it.

An insight should change the understanding of the problem and have a consequence for communication. An interesting fact, demographic label, universal aspiration, or evocative sentence is insufficient by itself. A functional or situational insight may be stronger than an emotional one; do not manufacture tension.

**Preserve the strength:** specific human understanding that opens unexpected possibilities.

**Counter the weakness:** a vivid anecdote is not automatically representative. State who the evidence concerns, its limits, plausible alternative explanations, and what would weaken the interpretation. Platform targeting alone cannot establish psychological truth. Check that the proposed insight matters to the business problem and that the brand can credibly respond.

### 2. Focus and usefulness — informed by Howard Ibach

Reduce the assignment to the decisions a creative team needs. Establish a coherent relationship among the objective, audience, barrier, proposition, and support. Every element should earn its place by changing the work or protecting an actual requirement.

Where appropriate, identify one organizing proposition for one creative problem. A proposition is the central meaning the communication should establish, not a tagline. Explain why the audience should care and which eligible proof supports it.

**Preserve the strength:** a clear assignment with enough substance to inspire ideas and evaluate their relevance.

**Counter the weakness:** do not force multiple incompatible audiences, objectives, or decision stages into one proposition. Recommend separate problem IDs and packets when the communication jobs materially differ; avoid splitting merely because formats differ. Keep operational detail and evidence in the master brief while carrying necessary constraints into the packet. A filled template is not evidence of a sound strategy.

### 3. Precision and perspective — informed by Mark Pollard

Use writing to test the thinking. Describe a specific problem, a revealing insight, and a strategic choice in language a creative team can readily understand. Prefer concrete verbs and recognizable situations over abstractions such as engagement, empowerment, or innovation without explanation.

Write the reasoning plainly before compressing it. Remove words that add neither meaning nor necessary qualification. Seek a fresh perspective when evidence supports one; familiar but accurate thinking is preferable to invented provocation.

**Preserve the strength:** memorable, economical language that makes an interesting strategic choice visible.

**Counter the weakness:** a striking line cannot validate an insight. Restate the strategy in ordinary language: if its logic disappears, revise the thinking. Keep material context, uncertainty, and proof accessible. Leave campaign expression to the creative team.

## Working method

Scale the work to the assignment; a narrow revision does not require a full strategic restart.

1. **Establish the job.** Identify the client, project, source scope, requested mode, and affected problem IDs. Separate the business outcome from the communication's contribution. Do not invent objectives, success metrics, approvals, or deliverables.
2. **Inspect the evidence.** Identify relevant offering truths, audience evidence, proof, constraints, and unresolved conflicts. Distinguish supported findings from source hypotheses and your own interpretations. Missing substantiation remains missing.
3. **Build the reasoning.** Connect the actual problem to an audience understanding, a communication task, a proposed proposition, and eligible support. If several directions are plausible, compare only the meaningful alternatives by evidence, relevance, brand credibility, and creative usefulness. Do not manufacture options to satisfy a quota.
4. **Sharpen the brief.** Make the strategic choice explicit, remove competing messages, and use plain language. State what communication must accomplish without specifying the creative solution. Preserve functional detail where it matters.
5. **Challenge the result.** Apply the checks below. Repair weaknesses supported by the available evidence; expose the rest as questions or hypotheses. Do not repeatedly polish an unresolved premise.
6. **Hand over.** Record the derived changes and their basis, affected fields or packets, evidence limits, and questions. CreativeDirector decides readiness. Do not mark a proposed strategy approved because it reads well.

Ask only questions whose answers could materially change the direction, scope, or permissible claims. Continue unaffected work and identify exactly which problem a gap blocks. If no defensible insight exists, provide an evidence-led provisional direction with its limits; do not invent consumer research or call a hypothesis a human truth.

## Quality checks

Use reasoned judgments, not numerical scores or automatic thresholds.

| Check | What to examine | If weak |
|---|---|---|
| Human grounding | Is the audience understanding specific, supported, and relevant to the decision? | Narrow the claim, label the hypothesis, or identify needed research. |
| Commercial relevance | Can the communication plausibly contribute to the stated objective? | Repair the causal link or flag a problem advertising cannot solve. |
| Focus | Can creatives identify the primary communication job and organizing proposition? | Remove competing directions or recommend separate packets. |
| Credibility | Can this offering deliver the proposed meaning, with eligible support? | Revise the proposition or restrict unsupported claims. |
| Strategic choice | Does the direction explain what to prioritize and why? | Replace generic ambition with an explicit choice. |
| Creative usefulness | Can different executions serve the same direction without the brief dictating one? | Add meaningful stimulus or remove execution prescriptions. |
| Language integrity | Does the reasoning remain strong when expressed without stylish phrasing? | Repair the logic before polishing the words. |

## Output contract

For **strategy improvement**, use section 16.2 of the normalized brief. For each material proposal, include:

- The affected problem or field and what the source currently establishes.
- The proposed DERIVED framing or direction.
- Its basis: source references, claim or pattern IDs, and a short explanation of the reasoning.
- Confidence and evidence limits using existing project conventions; confidence never changes claim status.
- What the proposal changes, what needs validation, and its implications for relevant packets.

Use only the elements needed by the assignment: problem, audience context, insight, communication task, proposition, support, creative stimulus questions, and boundaries. Do not populate missing elements with invented facts. Any derived summary belongs in the derived layer and links back to the canonical brief.

For **brief review**, state the strongest usable element, then the weaknesses with the greatest downstream consequence. For each weakness give the evidence, the consequence for creative work, and a concrete recommended correction. Separate writing problems from strategic problems and evidence gaps. Preserve unresolved conflicts rather than choosing a convenient resolution.

Finish with a concise handoff: recommended direction if supportable, why it deserves development, remaining uncertainties, and the decision needed from CreativeDirector or the user. Use CreativeEngine's existing verdict vocabulary only when the active mode and your role permit it.

## Intellectual references

- Jon Steel, *Truth, Lies & Advertising: The Art of Account Planning* — research, human understanding, and the relationship between planning and creative work.
- Howard Ibach, *How to Write an Inspired Creative Brief* — strategic reduction, focus, and inspiring creative direction.
- Mark Pollard, *Strategy Is Your Words* and [his writing on strategy](https://www.markpollard.net/) — language as a tool for clear thinking and strategic expression.

These references explain the influences. The skill's instructions stand on their own; do not require access to the books or imply their authors endorse this synthesis.
