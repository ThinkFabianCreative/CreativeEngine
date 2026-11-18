# MFK homepage preference test v02, UserTesting.com format

```
CLIENT:  Miracles for Kids Charity
PROJECT: website-rebrand
METHOD:  Unmoderated UserTesting test (screen and voice recorded) with UserTesting rating scales
STATUS:  Draft for Andres. Findings will be PROJECT-LEVEL and unverified.
DATE:    2026-10-29
REPLACES: survey_v01.md (same goals, rebuilt in UserTesting question types)
```

## How this maps to UserTesting

UserTesting tests are built from **tasks** plus **questions**. The question types used here:

| UserTesting type | Used for |
|---|---|
| **Rating scale** (5-point, labeled ends) | All scaled questions. This is UserTesting's default, so results stay comparable with their benchmarks |
| **Single Ease Question** (rating scale: *Very difficult* to *Very easy*) | Right after each task |
| **Multiple choice** (single answer) | Picks: fonts, colors, preferred site |
| **Written response** | Three words and short "why" answers |
| **Verbal response** (think-aloud, recorded) | The why behind the scores, which the survey can't capture |
| **Task** with a URL | Live site visits, so motion, the donation widget and video are all experienced |

Their **QXscore** template (task success plus attitudinal items for ease of use, trust, appearance and loyalty) fits this well. If your plan includes it, run each site as a QXscore task group and put the custom items below alongside it. Confirm the exact items in your workspace's template library, since plans differ.

## Audience setup

- **Use your own participants** (UserTesting's "Invite network" / custom audience link) rather than the general panel. We need MFK's donors, volunteers, staff and families, under NDA.
- Screener: "How are you connected to Miracles for Kids?" *Donor · Volunteer/event worker · Staff · Family we've served · Other (reject)*.
- **Target:** 10–15 per group for the scaled comparison (UserTesting sessions cost more per person than a plain survey). Five per group is enough for the verbal themes.
- **Families:** separate test variant without the giving task; a liaison sends the link.
- **Device split:** run a desktop test and a mobile test (UserTesting sets device at test level). Aim for about half on mobile.

## Test flow (about 15 minutes)

**Order:** the live site (E) first. Then A, W and J in **randomized order**. Use UserTesting's *randomize task order* for the three new-site task groups.

Participants see "Site 1, 2, 3, 4" only. Never "new," "old" or designer names.

### Intro
> "You'll look at four versions of a website for Miracles for Kids, a charity that helps families with critically-ill children. There are no right answers. Please think out loud the whole time: what you notice, like, dislike or find confusing."

### Block 1: Blind fonts and colors (2 min)
Upload the boards as images inside the test.

1. **Multiple choice, image:** "Which of these text styles feels most like a charity that helps families?" *Board 1–4*
2. **Multiple choice:** "Which is easiest to read?" *Board 1–4*
3. **Multiple choice, image:** "Which color palette feels most hopeful and trustworthy?" *Palette 1–4*
4. **Multiple choice:** "Which palette feels least right for this charity?" *Palette 1–4*
5. **Verbal:** "Tell us why you picked those."

### Block 2: One task group per site (about 3 minutes each)

Repeat for E, then A, W and J in random order.

**Task a, first impression.**
"Go to [URL]. Look at the top of the page for 5 seconds without scrolling, then answer."
- **Written response:** "What three words describe this site?"
- **Multiple choice, multiple answers (up to 5):** "Which words describe this site?" Randomize the order. The four target words are mixed in with the others so they don't stand out:
  *Clean · Elegant · Human · Friendly · Joyful · Calm · Warm · Polished · Hopeful · Modern · Playful · Approachable · Trustworthy · Sincere · Busy · Corporate · Cute · Dated · Generic · Cold*

**Task b, find a family story or the video.**
"Find out about a family Miracles for Kids has helped, or watch the video. Talk us through it."
- **Rating scale (SEQ), 1–5:** "How easy or difficult was that?" *Very difficult → Very easy*

**Task c, find an event.**
"Find the next event you could go to."
- **SEQ, 1–5**

**Task d, start a donation** *(not in the family variant)*.
"Show us how you'd start a $50 monthly gift. Click the button you'd press to give. Nothing will be charged, and the button may not go anywhere."
- **SEQ, 1–5**

**Ratings after each site.** Rating scale, 1–5, *Strongly disagree → Strongly agree*:

| Code | Statement |
|---|---|
| R1 | This feels like Miracles for Kids. |
| R2 | I would trust this organization with a donation. |
| R3 | The text is easy to read. |
| R4 | The colors suit the organization. |
| R5 | It invites me to give without pressuring me. *(family variant: "It asks for donations respectfully.")* |
| R6 | This site looks clean and elegant. |
| R7 | This site feels human and friendly. |

### Block 3: Compare (2 min)

- **Multiple choice:** "Which site best shows this mission: *We help families with critically-ill children battle bankruptcy, homelessness, hunger and depression, so they can fight for their kids' lives*?" *Site 1–4*
- **Multiple choice:** "If Miracles for Kids could launch only one of Sites 2, 3 or 4, which should it be?"
- **Rating scale, 1–5:** "Compared with Site 1, your pick is…" *Much worse → Much better*
- **Verbal:** "Why? What would you take from another site to make it even better?"

## Adjective coding frame (moderators and analysis only)

These are the adjectives we expect each version to earn. They're our hypothesis, **never shown to participants**. Use them to code open answers ("three words," verbal comments), and to check whether people see each version the way we expect.

| Version | Expected strengths | Expected risks |
|---|---|---|
| **E, live site** | Sincere, familiar, photographic, gentle | Dated, generic, scattered |
| **A, Version A** | Joyful, energetic, optimistic, playful, bold, expressive | Busy, loud, childish |
| **W, Jordan Webflow** | Clean, calm, modern, refined, airy, polished | Cool, corporate, impersonal |
| **J, Jordan Figma build** | Warm, friendly, hopeful, heartfelt, approachable, whimsical | Decorative, cute, less polished |

**The target profile:** a version that earns *clean, elegant, warm, hopeful, trustworthy* together. No version is expected to earn the full set. The gap shows what the final design should borrow from the others.

**Coding:** tag each word or comment to the matching cell, for example "busy" → A risk. Words that don't fit a cell go under "other" and are reviewed as possible new themes.

## What we'll report

| Question | Measure |
|---|---|
| Is a new site better than the live one? | Each new site's R1–R7 and SEQ means against E, from the same people; plus the "compared with Site 1" rating |
| Which new design is preferred? | Share of picks, overall and by group |
| Fonts | Block 1 picks, then R3 in context |
| Colors | Block 1 picks, then R4 in context |
| Ease of use | SEQ per task per site; task success from the recordings (completed / with difficulty / failed) |
| Clean and elegant, yet human and friendly | R6 and R7 together. The target is high on both |
| Mission and values fit | R1, mission pick |
| Giving without pressure | Donate-task SEQ, R5 |
| Adjective fit | Word picks per site against the coding frame: share of expected strengths, expected risks, and target words |
| The why | Verbal clips per site, tagged by theme; highlight reel for MFK |

**Reading it**
- On a 5-point scale with 10–15 per group, look for differences of about **0.5 or more**. Smaller ones need the verbal clips to back them.
- UserTesting's dashboard compares rating results across task groups. Export to Sheets for the paired, per-person comparison against E.
- Report by group. If donors and families disagree, that matters more than the overall average.

## Watch-outs

- **Donate goes nowhere** in the test builds (confirmed by Andres). The donate task measures whether people can find and set up a gift and how it feels, up to the click. It doesn't test checkout. Tell participants up front so a dead button doesn't read as a bug.
- **Order.** E always comes first, by your choice. Randomizing A, W and J keeps comparisons between them fair; each still carries the "after E" effect.
- **Recognition.** Staff and families know E. Note who mentions it, and compare their scores with donors'.
- **Fonts.** J uses Haboro Soft 400 and 700 only. Tag any comment about weight.
- **Length.** About 15 minutes is the most an unmoderated test holds before quality drops. If needed, give each person E plus two new sites (randomized).

## Build checklist
- [ ] Confirm the UserTesting plan: own-audience invites, task randomization, QXscore availability
- [ ] Make the type and color boards (images)
- [ ] Build a desktop test and a mobile test; family variant without the donate task
- [ ] Pilot with 2 staff, watch the recordings, fix unclear wording
- [ ] Send links through the donor, volunteer, staff and family-liaison channels
