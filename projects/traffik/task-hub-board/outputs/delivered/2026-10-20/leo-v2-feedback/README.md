# Task Hub v2: feedback for Leo

From Andres Fabian, Creative Director · October 20, 2026

Leo, this is our feedback on your updated mockup (Status, Calendar, Standup). Short version: it's a big step. You've closed most of the Oct 14 list, and the standup is now better than ours. What's left is mostly about how much each screen asks people to take in, and what each person sees by default.

## Start here

| Order | File | Why |
|---|---|---|
| 1 | `leo-v2-handoff_READ-FIRST_2026-10-20.md` | **The decisions and the build order.** Where documents disagree, this one wins |
| 2 | `taskhub-mockup_v2_MARKUP.html` | Your mockup with our notes pinned on it. Open in Chrome, click a pin to read it, press **M** to hide or show the markup |
| 3 | `TaskHub_Leo-v2_audit-markup_2026-10-20.pdf` | The same notes as a 9-page PDF, if that's quicker |
| 4 | `ACCEPTANCE.md` | How we'll check each batch is done |
| 5 | `CLAUDE-PROMPT.md` | Ready-to-paste prompt for your Claude builder: reads everything in order, plans Batch 1, waits for your OK |
| 6 | `COPY.md` | Final wording for every new label, empty state, error and prompt |
| 7 | `references/` | `tokens-v2.css` (colours, type, spacing, icons for light, dark and system) and `REFERENCES.md` (Lucide icons, patterns) |
| — | `supporting/` | The full design review (findings with evidence and how to check each), the visual and behaviour specs, the first audit, Trello / type notes |
| — | `screenshots/` | Marked-up views, the phone layout, and your New Task error pattern (keep it) |

## What changes from the Oct 12 handoff

Four things we told you before are replaced:

1. **Red is no longer the primary button colour.** Red means problems only. The primary button is ink on light, off-white on dark.
2. **Quality Control stays advisory, the way you built it.** Sending work to With client before QC is 5/5 asks for a one-line reason, which is logged. No hard block, no ACD override.
3. **Icons:** Lucide, the maintained version of Feather, one stroke and size throughout.
4. **Board order keeps Feedback:** Intake → Ready → In progress → Internal review → Quality Control → With client → Feedback → Done, with On hold as a lane across the top.

## Three batches

| Batch | What | Rough size |
|---|---|---|
| 1 | Colour roles + neutral primary, one header band (with a phone pattern), card layout, type scale, Lucide icons | ~3–4 days, CSS and templates |
| 2 | Default view by role, personal settings on the profile | ~3–4 days |
| 3 | Task pop-up with one status and the role rows; QC progress on cards; logged reason; move toast with Undo | ~3–5 days |

We'll review each batch against `ACCEPTANCE.md` before the next one starts.

## Where we got it wrong

Our first pass said there were no roles and no QC checklist. Both are on your full task page; we missed them. The ask is to bring them into the quick pop-up and onto the card, not to build them.

## What we need back from you

1. Your estimate for each batch, and anything here that fights how the Hub is built.
2. Can per-user settings be stored on the profile (not the browser)?
3. A time for a 30-minute walkthrough.

## Data note

The mockup and the screenshots show real client names. Keep this folder internal.
