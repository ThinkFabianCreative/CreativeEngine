# MFK homepage next-step preference: Lyssna study v01

```
CLIENT:  Miracles for Kids Charity
PROJECT: website-rebrand
TOOL:    Lyssna, free plan (quick study), account Leo Meskis, space "All TRAFFIK"
STUDY:   "MFK homepage next-step preference (DRAFT)"
EDIT:    https://app.lyssna.com/tests/yguezty51hz0/edit
STATUS:  Draft built 2026-10-29. Not shared or recruited.
```

## What it's for

Find out which of three new homepage designs MFK's people see as **the best next step for Miracles for Kids**. The live site is left out on purpose, so nobody judges by what they already know. "Better than today" is measured through the mission and the "good evolution" rating instead.

## The designs

| Shown as | Build | Screenshot | Live URL (optional) |
|---|---|---|---|
| Design A | Version A (Material 3 Expressive) | `lyssna/design-a.jpg` | https://boisterous-pothos-e638ac.netlify.app/ |
| Design B | Jordan, Webflow build | `lyssna/design-b.jpg` | https://miracles-for-kids-8843ee.webflow.io/ |
| Design C | Jordan, Figma build | `lyssna/design-c.jpg` | https://sensational-lebkuchen-da9227.netlify.app/ |

The screenshots are full-page desktop captures taken 2026-10-29. Lyssna shuffles the order for each participant. Participants never see which team made which design.

## Study content (as built)

**Welcome screen:** Lyssna default ("Hello there! You've been invited to participate in a short test."). A custom welcome needs the Growth plan.

**Section 1: preference test**

Instructions:
> Miracles for Kids helps families with critically-ill children keep a roof, food and hope while they fight for their kids' lives. It's refreshing its website. Take a look at each of these three early homepage designs (click to view full size). There are no right answers. These designs are confidential under your NDA, so please don't share them.
>
> Want to click around first? Optional live versions (open in a new tab): Design A, Design B, Design C [URLs]
>
> Which design would be the best next step for Miracles for Kids?

Main choice: pick one of Design A, B or C. Randomized order.

**Follow-up questions (all required):**

| # | Type | Question |
|---|---|---|
| 1.1.1 | Long text | Why did you choose that design? What makes it the right next step for Miracles for Kids? |
| 1.1.2 | Matrix | How much do you agree with each statement about **Design A**? (1 = strongly disagree, 5 = strongly agree) |
| 1.1.3 | Matrix | Same, for **Design B** |
| 1.1.4 | Matrix | Same, for **Design C** |
| 1.1.5 | Single select (A/B/C) | Which design feels the most **joyful, energetic, optimistic and bold**? |
| 1.1.6 | Single select (A/B/C) | Which design feels the most **caring, trustworthy, hopeful and family-centered**? |
| 1.1.7 | Single select (A/B/C) | Which design looks easiest for finding family stories, upcoming events and how to donate? |

Matrix rows, the same for each design:
1. This is a good evolution for Miracles for Kids
2. The fonts suit the organization
3. The colors suit the organization
4. It looks clean and elegant
5. It feels human and friendly
6. I would trust this organization with a donation

Matrix columns: 1 Strongly disagree · 2 · 3 · 4 · 5 Strongly agree

**Thank you screen:** Lyssna default.

## Where the questions come from

| Question | Research goal |
|---|---|
| Main pick + 1.1.1 | Which design is preferred, and why |
| Matrix row 1 | Is it a good evolution for MFK, without comparing it to the live site |
| Matrix rows 2–3 | Fonts and colors |
| Matrix rows 4–5 | Brand target: clean and elegant, yet human and friendly |
| Matrix row 6 | Trust and giving |
| 1.1.5 | Energy profile: expected to point to Design A (see the adjective coding frame) |
| 1.1.6 | MFK mission and values fit. The adjectives come from MFK's own language; MFK has no formal values statement (`client/knowledge/organization-profile.md`) |
| 1.1.7 | Ease of use: families, events, donating |

**Adjective coding frame:** see `survey_v02-usertesting.md` and `qual-test-guide_v01.md`. Expected strengths: A is joyful, energetic, optimistic and bold. B is clean, calm, modern and refined. C is warm, friendly, hopeful and approachable.

## Free plan limits

- **15 self-recruited responses** (unconfirmed whether that's per study or per account)
- One section only (quick study). No section randomization, no conditional logic, no live website testing, no recordings, no CSV export, no custom welcome screen
- **Links in instructions don't work.** Line breaks are stripped and URLs aren't clickable. Recommended: take the URLs out of the instructions and put them in the invite email

## Recruiting (when approved)

1. Continue to recruit → **Share link** (self-recruited, free). Don't use the Lyssna panel, which uses paid credits.
2. Send to 15 hand-picked people under NDA, for example 4 donors, 4 staff, 4 volunteers and 3 families. Have a family liaison invite the families.
3. Invite email: purpose, the NDA reminder, the study link, and the three optional live URLs.

## Reading the results

- **Preference:** count of main picks for A, B and C, plus the themes in the "why" answers
- **Good evolution, fonts, colors, brand, trust:** median of each matrix row per design
- **Energy vs values:** do 1.1.5 and 1.1.6 point to the same design? If not, that's the key finding
- **Ease:** 1.1.7 picks
- **Brand target:** the design that scores highest on *both* "clean and elegant" and "human and friendly"

With 15 people, report counts and quotes, not percentages or statistical claims. Pair with a few 30-minute interviews (`qual-test-guide_v01.md`) for depth.

## Related files

- `user-test-plan_v01.md`: full moderated plan
- `qual-test-guide_v01.md`: 30-minute qualitative guide
- `survey_v02-usertesting.md`: UserTesting version
- `boards/`: blind type and palette boards, plus `KEY.md`
- `screenshots/`: all four sites, desktop and mobile
- `lyssna/`: the three images uploaded to Lyssna
