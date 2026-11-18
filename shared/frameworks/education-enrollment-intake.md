# Education & Enrollment Intake

> CreativeEngine shared framework. Optional extension to `brief-normalization.md`. Owned by `brief-machine`. Loaded only when the assignment concerns education, training or institutional communication. Never loaded by default.

## Activation

Load this extension only when the raw source or the user establishes that the assignment concerns an educational institution, a programme of study, training, a course, or institutional communication on their behalf.

Do not load it because an assignment mentions learning, a young audience, a certificate, a workshop or a campus. Do not load it for a non-education client whose product happens to teach something. When in doubt, ask rather than assume: a wrongly activated extension invites fields the source never established.

Deactivation is silent. Nothing here is required of any assignment, and an education assignment that needs only three of these fields uses three.

## What this file is and is not

It is **global method**: reusable intake questions and field definitions. It holds no facts about any institution, and nothing here describes a real client.

```
GLOBAL METHOD     this file: questions, field definitions, distinctions          no client facts
CLIENT KNOWLEDGE  projects/<client>/client/: what is established about this
                  institution, each entry with its source, date and status
PROJECT KNOWLEDGE projects/<client>/<project>/: this assignment's audiences,
                  goals, intake dates, targeting, constraints
WORK PACKET       projects/<client>/<project>/packets/: only what one creative
                  problem needs
```

- A value established for one institution is never evidence about another, and never a default. `SHARED INTELLIGENCE.  ISOLATED CLIENT TRUTH.`
- Never infer a missing value. An unestablished field is recorded as not supplied, and becomes an open question when it would change the work (`brief-normalization.md` section 10).
- This extension adds no evaluation criteria, no creative method and no verdict. It supplies intake questions and distinctions only.
- It does not restate brief-normalization's rules. Provenance labels, the claim ledger, raw-source immutability and the source-only / derived separation apply unchanged.

## Not only degree enrollment

An education assignment is not by default a degree-enrollment campaign. All of these are education assignments and must fit without distortion:

- a short course, a single module, a workshop, a bootcamp
- an open day, a lecture, a virtual information session
- a guide, a brochure, a report, a newsletter
- a research announcement, a ranking, a donor or alumni communication
- general institutional or reputational communication
- corporate or professional training

Do not add a programme, an intake date, an application step or an enrollment goal because the client is an educational institution.

## Optional parameters

Record only what the source establishes, with its provenance label. Omit the rest. None of these is mandatory, and the list is extensible.

| Field | Notes |
|---|---|
| Institution, school, faculty, programme or offering | Use the offering hierarchy in `brief-normalization.md` section 6 |
| Credential or qualification | Exact wording; a credential claim belongs in the claim ledger |
| Delivery mode and location | For example on campus, online, hybrid, placement-based; as stated |
| Intake or start date | Exact, with its source; never estimated from a season or a term name |
| Geographic market and language | Including whether the market is stated or inferred from targeting |
| Prospective student audience | Identity and situation; source wording |
| Other decision-makers | For example a partner, parent, employer, sponsor, adviser or referrer, where the source establishes their role |
| Eligibility and prerequisites | Exact wording; an eligibility statement is a claim |
| Motivations, barriers, decision factors | Source wording where stated; anything else is DERIVED with its basis |
| Tuition, costs, financial aid | Exact figures and conditions, or not supplied; never approximated |
| Application and enrollment deadlines | Exact, with conditions and scope; see urgency below |
| Educational or career outcomes | Claim ledger entries. Employment rates, salaries, progression and accreditation are claims, not context |
| Journey stage | Only where the assignment establishes one; see below |
| Conversion or communication goal | See goals below |
| Destination, CTA, measurable success event | Separation rule in `brief-normalization.md`, section 8 |

**Urgency.** Urgency must be supported by current, source-established facts. These may include a real deadline, genuinely limited availability or another evidenced constraint. Preserve each fact's conditions, scope and date. Never manufacture scarcity, urgency or consequences. This is an intake and evidence rule: it records what could support urgency and writes no urgency copy.

## Journey stages

Where an assignment establishes a journey, stages may include:

```
AWARENESS · INQUIRY · APPLICATION STARTED · APPLICATION COMPLETED · ADMISSION · ENROLLMENT
```

- These are optional descriptors, not a compulsory sequence, not a funnel every institution runs, and not a set the work must cover.
- Many assignments have no stage at all. A newsletter, a guide or an institutional message may sit outside any journey.
- **Do not infer a stage from the channel, the placement, the format, the CTA or the goal.** A brochure download does not establish inquiry; a paid social placement does not establish awareness.
- Describe a stage by behavior, never by demographics (`brief-normalization.md` section 7).
- A stage the source does not establish is not supplied, and is an open question only when it would change the work.

## Goals

These are selectable or source-specified communication goals. The list is extensible and not exhaustive.

```
Download a brochure                  Book a conversation
Download a free guide                Schedule a campus visit
Learn more                           Register for an event
Get more information / request info  Register for a virtual event
Navigate to a landing page           Subscribe to a newsletter
Complete a lead form                 Complete a video view
Engage with the ad                   Start an application
Complete an application              Enroll
```

- A goal is what the source asks the communication to achieve. It is not a default.
- A communication or conversion goal is not automatically a platform optimization objective, a journey stage or a measured event. Record each separately where relevant. Do not infer one from another.
- None of these is more advanced or more valuable than another. Do not order them into a funnel or escalate a stated goal into a later one.
- Record the goal the source states. Where it states several, each is a separate goal, and usually a separate creative problem.
- Where the source states none, record that, and ask. Do not supply one.

## Goal, CTA, destination and measurement

The separation rule and its packet fields are in `brief-normalization.md`, section 8 ("Goal, CTA, destination and measurement"). It applies to every industry and is not repeated here.

These are education-shaped examples of the same rule. Each pair describes two different events:

| Not the same as | |
|---|---|
| A brochure or guide button click | a completed download |
| A lead form opening | a submission |
| "Learn more" as CTA wording | a landing-page view, or a completed information request |
| A campus-visit booking | attendance |
| An event or virtual-event registration | attendance |
| A newsletter form submission | a confirmed subscription |
| A started application | a completed application |
| A completed application | enrollment |

Where the source does not define the measured event or how it is tracked, record an open measurement question. Do not assert a tracking capability the source has not established.

## Intake questions

Reusable, and free of client facts. Ask only what the assignment needs.

**Offering.** What exactly is being communicated: an institution, a school, a programme, a course, an event, a publication, something else? What credential or qualification, in the client's exact wording? What delivery mode and location? What intake or start date, and from which source?

**People.** Who is the prospective audience, in the source's words? Who else decides, influences or pays? What eligibility or prerequisite does the source state? What motivations, barriers or decision factors does the source state, and which are our inferences?

**Commitment.** What does it cost, and what does the source actually say about aid, funding or conditions? What deadlines, availability limits or other constraints exist, are they current and source-established, and under what conditions?

**Claims.** Which educational or career outcomes are asserted, by whom, with what evidence, and which are approved for use?

**The ask.** What should the audience do? Where does that happen? What event counts as success? How is it measured, and by whom? What is the approved CTA wording?

**Scope.** Which market and language? One creative problem or several? What has this institution run before, and what is its status in client knowledge?

## Boundaries

- This extension normalizes intake. It does not evaluate creative work, generate territories or decide readiness.
- It does not promote anything into client knowledge. Promotion follows `projects/README.md`.
- It carries no institution's facts, preferences, performance or audience patterns into any other assignment.
- A generic education field structure never substitutes for what a particular institution established.
