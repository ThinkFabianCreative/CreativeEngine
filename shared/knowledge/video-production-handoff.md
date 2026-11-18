# Video production handoff

Added 2026-10-27. CreativeEngine has no video production role. DesignChamp directs video and WordSmither writes it. A human editor or an outside production partner shoots, edits, mixes and finishes it. This spec is what crosses that line: an approved idea packaged so someone outside the department can produce it without guessing at creative decisions.

**Interim.** A dedicated video engine is planned for later (decided 2026-10-27). Until it exists, this handoff is how video gets made. When the engine is built, review this spec against it rather than keeping both.

Platform-neutral. Specs come from the relevant `shared/knowledge/<platform>/` module; for Meta, also `meta-paid-ads/blueprint-creative-best-practices.md`. No client facts: the filled-in spec lives in the project (`projects/<client>/<project>/work/`).

## When to write it

Only after the idea is approved (end of DEVELOP or after JUDGE). Never as a way to finish a weak idea: if the spec cannot state the idea in one sentence, the work goes back to DEVELOP. AI comps, animatics and pre-viz made with Artlist or other tools can go with the spec as reference. They are for pitch and inspiration only, never footage for the finished ad.

## Ownership

| Section | Owner |
|---|---|
| Idea, look, frames, type on screen, safe zones, formats | DesignChamp |
| Hook line, script, VO, supers, captions | WordSmither |
| Claims, mandatories, legal | WordSmither flags; source from the claim ledger |
| Sign-off before it leaves the department | creative-engine-director |

## The spec

```
CLIENT / PROJECT / CAMPAIGN:
DELIVERABLE:        what this is (e.g. Reel, in-feed video, 6s bumper) and where it runs
IDEA:               one plain sentence
WHAT MUST SURVIVE:  the load-bearing elements; anything an editor must not cut or change
LENGTH:             target duration per placement, and why (the idea sets it, not the upload limit)

HOOK (0–3s):        what the viewer sees and reads in the opening frame; frame one must work as a still
STRUCTURE:          beat by beat with timings: setup, turn, brand entry, CTA (see narrative-craft.md)
STORYBOARD / REFS:  frames, comps or animatic, labelled REFERENCE ONLY where AI-made

ON-SCREEN TEXT:     every super, exact words, timing in and out, position inside the safe zone
SOUND-OFF CHECK:    confirm the full message lands silently through image, motion and text
CAPTIONS:           speech captions, kept separate from designed type
AUDIO:              music direction (own, licensed, royalty-free or trending), VO script and voice direction, SFX
SOUND-ON VALUE:     what audio adds for people listening; never the only carrier of the message

HUMAN PRESENCE:     who is on screen (customer, creator, employee, talent, none) and how they're cast
LOOK:               polished or casual/lo-fi, and why for this brand; grade, filters, effects
EDITING STYLE:      pacing, cuts, transitions, speed; what to avoid
BRAND:              logo, colour, type and identity rules; when the brand appears

FORMATS:            every aspect ratio needed (e.g. 9:16, 4:5, 1:1, 16:9), with what changes in each reframe
SAFE ZONES:         per placement, from the platform module
CUTDOWNS:           each shorter version and what it keeps; a cutdown is a rewrite, not a trim
VARIANTS:           genuinely different angles or hooks to test, and the hypothesis for each

AUTOMATIC CHANGES:  platform enhancements (e.g. Meta Advantage+) to switch off because they would break the idea
CLAIMS / FLAGS:     claim IDs and statuses, mandatories, music licensing, talent releases, UNVERIFIED specs
DELIVERY:           file specs from the platform module, naming, deadline, review rounds
QUESTIONS FOR PRODUCTION: what the editor or partner should come back on, not decide alone
```

Leave a field out only when it doesn't apply, and say so ("Human presence: none, product-only").

## Review when it comes back

DesignChamp and WordSmither check the cut against WHAT MUST SURVIVE, the sound-off check and the safe zones, using the actual placement preview. For Meta, creative-engine-director runs the §9 checklist in `meta-paid-ads/blueprint-creative-best-practices.md`. Production notes that change the idea come back to the department; they are not fixed in the edit.
