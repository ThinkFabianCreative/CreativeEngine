# MFK homepage, qualitative preference study: discussion guide v01

```
CLIENT:  Miracles for Kids Charity
PROJECT: website-rebrand
METHOD:  Moderated qualitative interviews, think-aloud and comparative probing
STATUS:  Draft for Andres. Findings will be PROJECT-LEVEL and unverified.
DATE:    2026-10-29
COMPANION: user-test-plan_v01.md (logistics, recruiting, families protocol)
```

## Research questions

| # | Question | How we'll hear it |
|---|---|---|
| RQ1 | Which new design is preferred, and **why**? | Think-aloud, final choice and its reasons |
| RQ2 | Which one best fits MFK's goal: helping families with critically-ill children so they can focus on their kids? | Mission match, "who is this for?" |
| RQ3 | Which **font combination** works best? | Blind type boards, then type in context |
| RQ4 | Which **color palette** works best? | Blind color boards, then color in context |
| RQ5 | Which one is **easiest to use**? | Task think-aloud, hesitation and recovery |
| RQ6 | Which one lifts the brand to **clean and elegant, yet human and friendly**? | Word choice, the brand-tension exercise, laddering |

This study is about **why** people react as they do, not about scores. Anything people count, such as card placements, is there to start a conversation and is never reported as a statistic.

## The sites

Participants only ever hear "Site 1, 2, 3, 4."

| Code | Site | URL |
|---|---|---|
| E | Live site | https://miraclesforkids.org/ |
| A | Version A | https://boisterous-pothos-e638ac.netlify.app/ |
| W | Jordan, Webflow | https://miracles-for-kids-8843ee.webflow.io/ |
| J | Jordan, Figma build | https://sensational-lebkuchen-da9227.netlify.app/ |

**Order:** E first, as the reference point. Then A, W and J in one of six rotations (see the plan).

## Participants

Twelve to sixteen 30-minute interviews: donors, workers and volunteers, staff, and families, 3 or 4 from each group. Families follow the care protocol in the plan: a liaison invites them, there is no giving task, and they can stop at any time.

## Materials to prepare

1. **The four live URLs**, open in tabs, on the participant's own device where possible. About half the sessions should be on a phone.
2. **Blind type boards (4).** Each board shows one site's headline and body fonts with the same neutral text, at the same size, in black on white. No colors, logos or photos.
   - Sample text: *"Help is on the way. When a child is in the hospital, the bills don't stop. We help families keep a roof, food and hope."*
3. **Blind color boards (4).** Each board shows one site's palette as proportioned swatches, in the share each color gets on the page, with no text or images.
4. **Brand-tension sheet.** Two lines, with the four site thumbnails to place on each:
   - *Clean and elegant ← → Cluttered and plain*
   - *Human and friendly ← → Corporate and distant*
5. **Screenshots** of the top of each page, printed or on a shared board, for the final comparison.

Make the boards from the deploy builds: E from the live site; A from `v4`; W from Webflow; J from `v5-jordan` (Haboro Soft, Zooja Pro, Cabin).

## Session flow (30 minutes)

| Time | Part | Answers |
|---|---|---|
| 0:00–0:02 | Welcome | |
| 0:02–0:06 | Blind type and color boards | RQ3, RQ4 |
| 0:06–0:10 | Site E, the live site | Baseline |
| 0:10–0:22 | Sites A, W and J in rotation, 4 minutes each | RQ1, RQ2, RQ5 |
| 0:22–0:29 | Side-by-side comparison | RQ1, RQ3, RQ4, RQ6 |
| 0:29–0:30 | Thanks | |

The blind boards come **before** any site, so people judge fonts and colors before the photos and copy can sway them.

---

### 1. Welcome (2 min)

> "We're looking at a few website designs for Miracles for Kids. I didn't make them, and there are no right answers. Please think out loud as you go."

- "In one sentence, how would you describe Miracles for Kids to a friend?" *(Write down their words.)*

### 2. Blind boards (4 min), RQ3 and RQ4

Show the four **type** boards, then the four **color** boards, each set in random order and labeled 1 to 4.
- "Which feels most like a charity that helps families? Why?"
- "Which feels wrong for it? Why?"

*Don't reveal which board belongs to which site.*

### 3. Each site (E first, then A, W and J in rotation, 4 minutes each)

**a) First 5 seconds.** Show the top of the page, then hide it.
- "What three words come to mind? Who is this for?"

**b) Two quick tasks.** Ask them to think aloud. Every site gets the **giving** task (families: "Where would someone give?"). The second task rotates so all three get covered across sites:

| Site position | Second task |
|---|---|
| 1st site | Families: "Find out about a family Miracles for Kids has helped." |
| 2nd site | Events: "When could you next go to an event?" |
| 3rd site | Video: "Find the video and start it." |
| 4th site | Families again: compare with the first site |

Listen for hesitation, where they look first, and whether giving feels easy, pushy or respectful.

**c) One question.** "What did you like most, and what bugged you?"

### 4. Side-by-side comparison (7 min)

Lay out the four screenshots.

**Brand tension, RQ6.** "Place each site along these two lines": *Clean and elegant ← → Cluttered and plain* and *Human and friendly ← → Corporate and distant*.
- Ask "Why?" about one placement, then "Why does that matter?" once more.
- "Is there one that's both clean **and** warm?"

**Fonts and color in context, RQ3 and RQ4.** "Which site's fonts and colors would you keep?"

**Mission fit, RQ2.** Read the mission aloud. "Which site lives up to it best?"

**Choice, RQ1.** "If Miracles for Kids could launch only one new site, which should it be? Is it better than Site 1 [the live site]? What would you steal from another site?"

### 5. Thanks (1 min)

Give family participants their gift card.

---

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

## Moderator rules

- Never say "new," "old," "redesign," or the designers' names.
- Ask neutral, open questions: "Tell me more," "What makes you say that?", "What did you expect?" Never ask leading ones like "Isn't this cleaner?"
- Let silence work. Count to five before you help.
- If someone asks "Is this the right way?", reply "What would you do if I weren't here?"
- Write down **their exact words**. The words they use are the findings.
- With families: no pressure to talk about their own situation, and stop whenever they want.

## Notes template (one per session)

| Field | Notes |
|---|---|
| ID, group, device, rotation | F02, Family, Android, R3 |
| Brand-in-one-sentence (warm-up) | |
| Type boards: favorite, rejected, why | |
| Color boards: favorite, rejected, why | |
| Per site, first 3 words | E / A / W / J |
| Per site, task observations (hesitation, path, quotes) | |
| Brand-tension placements and laddering results | |
| Mission fit, best and worst | |
| Final pick, compared with live, what to steal | |
| Standout quotes (verbatim) | |

## Synthesis

1. **Debrief within 30 minutes** of each session, with the top 3 observations per site.
2. **Affinity map** all quotes and observations on a board. Tag each one with site, group and research question.
3. **Code the themes by research question.** Example codes:
   - fonts: legibility, personality
   - colors: warmth, trust, dissonance
   - ease of use: findability, friction
   - brand: elegance, humanity, pushiness
4. **Compare across groups.** Note where donors and families diverge. That gap is a finding in itself.
5. **Make a scorecard per site:** for each research question, *strong / mixed / weak*, with the 2–3 quotes that best show it, and how many participants raised it ("6 of 14"). Show counts only as evidence for a theme, never as percentages.
6. **Recommendation:** which design to take forward, which font and color choices to keep or borrow, and the top 5 usability fixes, each traced to what participants said.

## Watch-outs

- **Staff and families know the live site.** Note when they recognize it, and expect some loyalty or fatigue.
- **Content differs between sites.** The copy, photos and features aren't identical. The blind boards keep the font and color judgments clean. For other preferences, probe whether people are reacting to the design or to the content.
- **Font limits.** J renders Haboro Soft at 400 and 700 only. Write down any type comment that might come from that.
- **No real payments.** Check that every site's donate flow stops before real payment. A and J show a prototype message. Check W and the live site's donate page before the first session.
