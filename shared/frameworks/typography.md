# Typography

> CreativeEngine shared framework. Owner `design-champ`. Used by `word-smither` when type decides how a line is read, and by `creative-engine-director` in review.

## Provenance

In-house CreativeEngine framework, synthesizing ordinary professional typographic practice as it applies to advertising and brand work. It is not derived from a single named book, designer, foundry or curriculum.

- Do not attribute its tests, categories or labels to any named source.
- Typeface categories named here are examples of kinds, not recommendations and not licence-cleared choices.

## Purpose

`barry-concept-art-direction.md` §7 decides **what type does**: carries a voice, becomes the image, or stays out of the way. This framework starts there and answers everything after.

```
WHAT IS THE TYPE'S JOB, AND DOES THIS FACE DO IT?
DOES THE HIERARCHY DELIVER THE IDEA, OR JUST RANK THE CONTENT?
DOES IT SURVIVE WHERE IT WILL ACTUALLY BE READ?
DOES THE SETTING AGREE WITH WHAT THE WORDS ARE SAYING?
```

It especially fights:

- a typeface chosen for how it looks in a specimen rather than what it has to do
- hierarchy as a size chart rather than a reading order
- dramatic typographic treatment with no job
- type that reads in a comp and fails in a feed, at distance, or over video
- the category default worn as a house style

## Related frameworks

| Framework | Relationship | Status |
|---|---|---|
| `barry-concept-art-direction.md` | §7 assigns the type's job; §5 sets the reading order that hierarchy serves | Active |
| `creative-object-taxonomy.md` | §15 visual identity / design system, distinct from §14 hero graphic / key visual | Active |
| `pricken-idea-mechanisms.md` | Omission and literal language often become typographic mechanisms | Active |
| `hey-whipple-copycraft.md` | §9 compression: the line and its setting are decided together | Active |
| `narrative-craft.md` | §9 supers are a second script, not a transcript | Active |
| `visual-craft.md` | Grids, color, imagery and the layout system around the type | Planned, not implemented |

Where they overlap, the more specific treatment wins. Whether there is a *visual idea* is Barry's question. Whether the *type delivers it* is this framework's.

---

## 1. Job before face

Never open a font menu before this is answered.

```
JOB:       voice / image / invisible   (barry §7)
SAYS:      what the words say, in tone as well as content
SURVIVES:  the smallest size, worst background and shortest exposure it must live through
EXCLUDES:  what this category already looks like
LOCKED:    what the client's brand system mandates
```

LOCKED comes first in practice. A client's approved identity typeface is a mandatory, not an option (root `CLAUDE.md`, authority per domain). Where the real freedom lies inside a locked system is §10.

## 2. What actually decides a typeface

Four filters, in this order. Aesthetic preference does not appear until the end.

**1. Voice.** Letterforms carry association before anyone reads a word: period, place, craft, formality, warmth, authority, cheapness. Name the association you want in plain words — "a face that sounds like someone who has done this a long time" — then look for faces that do that, rather than starting from a shortlist and working backwards.

**2. Survival.** What must this face endure?

- the smallest real size (a caption, a legal line, a 320px banner)
- the worst background (over photography, over moving video, inside a busy feed)
- the shortest exposure (a thumb passing, a car passing)
- the widest range (one family working from 8pt legal to a 40-foot headline)

Faces fail differently. High-contrast display faces thin out and disappear at small sizes and over texture. Low-contrast grotesques stay legible and say less. Tightly drawn display faces collapse when set in all caps.

**3. Exclusion.** Every category has a default: the geometric sans of technology and finance, the humanist serif of direct-to-consumer, the condensed grotesque of sport, the collegiate slab of universities. Using the default is a decision to look like the category — sometimes correct, never automatic. Check what the neighbors actually do in `DesignChamp/knowledge/brand-design-md/`.

**4. Availability.** Licensing, web-font performance, language and glyph coverage, and whether the client can keep using it are real constraints. A face the client cannot licence is not a proposal. Never state licensing terms as fact from memory; flag it as a question.

## 3. Pairing

Most pairings fail for one of two reasons: **too similar to read as contrast**, or **too different to read as a system**.

Three models that work:

| Model | How | Best for |
|---|---|---|
| **One family, full range** | A single superfamily across weights, widths and optical sizes | Systems, long documents, anything needing discipline. The safest and most underrated |
| **Contrast of era** | Two faces from clearly different periods — a modern grotesque with a transitional serif | Editorial work, and brands with a point of view |
| **Contrast of construction** | Two faces built on opposite logic — geometric against humanist, rational against written | Work where the tension itself carries meaning |

Rules of thumb:

- **Two is a system. Three is usually a mistake**, unless the third has a strictly separate job (data, legal, code).
- **Pair by proportion, not by mood.** Faces with compatible x-heights and widths sit together. Faces chosen because they "feel similar" usually don't.
- **One leads.** If both faces are trying to be the voice, neither is.

## 4. Hierarchy is a reading order

Hierarchy is not a ranking of content importance. It is the order in which the idea is received (`barry-concept-art-direction.md` §5).

- **Levels are earned.** Three is usually enough. A layout with six typographic levels normally has content that was never edited.
- **Contrast, not increments.** Levels that differ slightly read as a mistake. Make the difference unmistakable, in size, weight, case, color or position.
- **One dominant element.** If everything is emphasized, the eye chooses for itself and the reading order is accidental.
- **The reveal comes after the setup.** If the punchline is typographically louder than its premise, it is read first and spoiled.
- **Position is hierarchy.** Isolation and placement often outrank size.

Test: squint until the words are illegible. What is still distinguishable is the hierarchy you actually built.

## 5. Scale and rhythm

- **A scale is a decision.** Modular ratios are a starting point, not an answer. Adjust by eye against the real content at the real size.
- **Relationships matter more than values.** 48/24/16 and 44/22/15 behave almost identically. 48/44/40 works at no absolute size.
- **Advertising runs one step too small.** Comps are viewed at arm's length on a large screen; feeds are viewed on a phone and out of home across a street. Set at the real viewing condition and the type is usually larger than the comp suggested.
- **Line length and leading move together.** Roughly 45–75 characters per line for sustained reading; shorter lines want tighter leading, longer lines want more. Most ad copy is far shorter than either rule anticipates, so decide by eye.
- **Vertical rhythm is optional here.** A strict baseline grid serves documents and systems. A single key visual generally does not need one.

## 6. Micro-typography

Worth fixing, in roughly this order of impact:

- **Tracking at display size.** Large type almost always needs negative tracking; default spacing was drawn for text size.
- **All caps needs positive tracking.** Uppercase letterforms were not designed to sit beside each other.
- **Correct marks.** Typographic quotes and apostrophes, en and em dashes, real ellipses, proper minus signs. A prime standing in for an apostrophe is the most common tell in a generated comp.
- **Widows and orphans in short copy.** In a three-line headline, one word alone on line three is a visible mistake. In running body copy it matters less than people claim.
- **Headline line breaks are written, not wrapped.** Break for sense and rhythm. Never let a headline break where the container happens to end.
- **Numerals.** Lining figures in tables and interfaces; oldstyle in running text where the face offers them.
- **Hyphenation off** for display and short copy; acceptable in justified long copy.

When it does not matter: in EXPLORE. Micro-typography applied to a rough is noise, and polishing a concept that has not survived the rough test is the polish trap (`creative-direction-audit.md` §8.1).

## 7. Type as image

When the letterforms are the idea rather than the delivery of it.

Mechanisms that carry meaning:

- **Scale** — a word large enough that its size changes what it means.
- **Crop** — legibility withheld, the audience completing the word (`pricken-idea-mechanisms.md`, omission).
- **Material** — the word made of, or written in, the thing it names.
- **Arrangement** — the shape the words make is the argument.
- **Distortion or damage** — the condition of the letterform is the content.
- **Substitution** — one glyph replaced by an object, where the substitution itself means something.

The test: **remove the treatment and set the same words plainly. What is lost?** If the answer is "it looks less designed," the treatment has no job. If the answer is a meaning, the type is the idea.

This is the section most at risk of decoration. A dramatic typographic treatment with no job is the typographic form of the polish trap.

## 8. Legibility in real conditions

The constraint advertising has and most design writing skips.

| Condition | What breaks | What to do |
|---|---|---|
| **Feed at thumb speed** | Anything needing a second look | One thing legible in the first glance |
| **Out of home at distance** | Fine strokes, tight tracking, low contrast, more than a few words | Test at actual viewing distance, not zoomed out on a screen |
| **Supers over moving video** | Contrast changes shot to shot | Test against the worst frame, not a still. Consider a held plate or scrim |
| **Small formats** | Optical sizing; display faces at caption size | Use the family's text cut, or a different face |
| **Text over image** | Contrast varies across the image | Fix it with the image — crop, darken, reposition — not by adding a stroke to the type |
| **Sound-off video** | Everything, when supers are carrying the script | Supers are a second script, not a transcript (`narrative-craft.md` §9) |

**Accessibility contrast minimums are a requirement, not a preference**, and they outrank taste. Platform text-overlay rules, safe zones and caption specifications come from verified knowledge in `shared/knowledge/`, never from this framework and never from memory.

## 9. Typographic tells

Retrieved settings rather than decided ones:

- **The default template** — centered headline in a neutral geometric sans, generous margins, logo bottom right, applied regardless of idea.
- **The generated-comp look** — even weight, even spacing, a generic geometric sans, nothing cropped, nothing decided.
- **Letter-spaced all caps as instant luxury** — thin, wide, gold-adjacent, meaning nothing.
- **The trend face as concept** — a fashionable revival or a distressed display face presented as though it were the idea.
- **The quirky script for "brand personality"** — friendliness applied rather than earned.
- **Gradient or chrome text** — an effect standing in for a thought.
- **Two faces doing the same job** — decoration mistaken for a system.
- **The mismatched voice** — a wry line set in an earnest face, an urgent line set in something serene. See §11.

Warnings, not bans. A default used knowingly and visibly turned can be the idea.

## 10. Working inside a locked brand system

Most advertising is set in type someone else chose. The freedom is real, and it is in:

- **scale** — how big is a decision the guidelines rarely make
- **weight and width** — most identity families contain far more range than the brand actually uses
- **case and arrangement** — line breaks, stacking, alignment
- **crop and containment** — how the type meets the edge
- **pairing at the edges** — where a second face is permitted, and for what job
- **restraint** — using less of the system than the guidelines allow

What is not freedom: substituting the identity face, redrawing letterforms, or treating guidelines as an opening suggestion. A genuine conflict between the brand system and the idea is surfaced to CreativeDirector, not resolved silently (`DesignChamp/AGENT.md`).

Designing the type system itself, rather than working inside one, is a different object — `creative-object-taxonomy.md` §15 — with longevity and system criteria this framework only partly serves.

## 11. Type must agree with the words

The most common invisible failure: typography that contradicts the copy's tone.

- Read the line aloud, then look at the setting. Do they sound like the same person?
- Understatement set loudly stops being understatement.
- A joke set with total sincerity can be the joke, deliberately. Accidentally, it is just wrong.
- When the line changes in a later round, the setting may need to change with it. Copy and type are decided together (`hey-whipple-copycraft.md` §9), which is why WordSmither is a party to this framework.

## 12. By operating mode

| Mode | Use |
|---|---|
| **EXPLORE** | Type experiments as thinking (§7) are legitimate and encouraged. Do not apply micro-typography, pairing discipline or tells as filters. Judge what the experiment produced, not its finish |
| **DEVELOP** | Decide the job, the face and the hierarchy. Test at real size and in real conditions (§8). Fix micro-typography once the concept has survived |
| **JUDGE** | Does the type have a job? Does the hierarchy deliver the idea in the right order? Does it survive where it runs? Does the setting agree with the line? Name tells precisely, and count each weakness once |

## 13. Framework output

When useful:

```
JOB:        [voice / image / invisible]
FACE:       [family and why, in one line — or "locked: client identity"]
PAIRING:    [model used, or "single family"]
HIERARCHY:  [levels, and the reading order they produce]
SET FOR:    [the real viewing condition it was set at]
SURVIVES:   [smallest size / worst background / shortest exposure]
RISK:       [most likely way it fails in the real placement]
```

Do not produce this wrapper when the user wants finished work and it would make the answer worse. Do not expose hidden chain-of-thought.

## 14. Framework principle

Type is not the clothing an idea puts on. It is one of the places an idea can live — and in work that has no idea, it is the first place the emptiness shows.
