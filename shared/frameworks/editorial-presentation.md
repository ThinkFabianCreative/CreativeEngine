# Editorial Presentation

> CreativeEngine shared framework. Owner `design-champ`. Used by `creative-engine-director` when a deck is the object being judged, and by `word-smither` for chapter lines, slide titles and case-study language.

## Provenance

In-house CreativeEngine framework, adapted from an "Editorial Presentation Art Direction" brief supplied by the user on 2026-10-03. Studios, designers and publications named here are reference points to study, not sources of its tests. Its client-specific extension was moved to that client's workspace; this file holds no client facts.

## Purpose

A deck is a sequence of visual moments, closer to a film, an exhibition or an editorial feature than to a report or a dashboard. This framework covers what is specific to presentations, pitch decks, credentials and case-study decks:

```
DOES EVERY SLIDE HAVE A REASON TO EXIST VISUALLY?
DOES THE SEQUENCE HAVE RHYTHM, OR IS IT ONE LAYOUT REPEATED?
DO CHAPTER BREAKS ADVANCE THE ARGUMENT?
ARE CASE STUDIES STORIES, AND CAPABILITIES OUTCOMES?
WERE REFERENCES CHOSEN FOR A PRINCIPLE, NOT A LOOK?
COULD THIS DECK BELONG TO ANYONE ELSE?
```

Optimize for "feels inevitable for this story", not "looks professional".

## What this framework does not cover

Counted once, under the most specific framework:

| Judgment | Where it lives |
|---|---|
| Is there an idea; what carries it; reading order | `barry-concept-art-direction.md` |
| Composition, grids, color, imagery craft, stock and generated-image rules, generic visual tells (gradients, glass, blobs, card grids, stock clichés), brand-blind test | `visual-craft.md` §2–§9 |
| Type jobs, scale contrast, hierarchy as reading order | `typography.md` |
| One idea per slide, titles that state the point, presented vs read decks, projection legibility, data slides | `format-prototyping` → `references/slideshow.md` |
| Story shape, the turn | `narrative-craft.md` |
| Recommending, what to show, honesty limits (no invented data, quotes, results) | `selling-the-work.md` |
| Building the deck file | `frontend-slides` (HTML), `anthropic-skills:pptx`, `figma-use-slides`; see each skill record |
| Slide shapes by asset format and content limits | `shared/knowledge/deck-layout-archetypes.md` (structure menu only, no look) |
| Motion craft | planned `animation-craft.md`. Until then, §8 below |
| Client look, products, category codes and banned tropes for one client | that client's `projects/<client>/client/knowledge/` |

## 1. The reference hierarchy

Presentation templates and SaaS/UI design are not the primary reference. Look first at disciplines that sequence meaning:

| Territory | Study for | Example sources (to study, not copy) |
|---|---|---|
| **Cinematic** | Sequencing, reveals, cropping, one motif evolving, tension and release | Art of the Title; Saul and Elaine Bass, Pablo Ferro, Kyle Cooper, Karin Fong; Imaginary Forces, Elastic, Prologue |
| **Editorial** | Asymmetric grids, extreme type scale, unexpected crops, captions, folios, dense vs sparse pacing | Magazine and cultural publications; Eye, Creative Review, It's Nice That, BP&O, The Brand Identity, Are.na |
| **Information / annual report** | Authoritative technical information that isn't dry; disciplined data; conceptual covers | annualreport.gallery; IBM, Olivetti, Braun, Herman Miller, Lufthansa; Rand, Vignelli, Aicher, Müller-Brockmann, Chermayeff & Geismar |
| **Brand systems** | One idea across many formats; what makes executions related | Pentagram, Collins, Base, Porto Rocha, Studio Dumbar, Wolff Olins, Koto, Made Thought, DIA, Spin |
| **Spatial** | Type as wall graphic, product as exhibition object, sightlines, physical sequencing | Museum exhibitions, wayfinding, trade-show and experiential design |

**Extract the principle, never the aesthetic.** Not "make it look like Se7en", but "macro-detail imagery, constrained type and abrupt cuts to create precision and intensity".

## 2. Research method and the reference board

1. Do not start by searching "presentation design". Search the subject across disciplines: `<subject> editorial typography`, `<category> annual report`, `<subject> exhibition design`, `<material/product> macro photography`, `scientific/technical diagrams editorial`, `film title typography`.
2. Build a board in the five territories of §1.
3. For each reference, record:

```
REFERENCE:     [title, maker, link]
TERRITORY:     Cinematic / Editorial / Information / Brand / Spatial
PROBLEM IT SOLVES:  [e.g. "very large type organizing a section without cards"]
BORROW:        [the principle]
DO NOT COPY:   [the surface]
```

A reference that only answers "it's beautiful" is cut. Ads specifically: `ad-reference`. Deck style systems: `DesignChamp/knowledge/presentation-style-library.md`. Image vocabulary: `DesignChamp/knowledge/image-direction-reference.md`.

## 3. Rhythm: think in sequences

Judge every slide against the ones before and after it. Patterns to compose with:

- **Dense → sparse.** An evidence slide, then one enormous statement.
- **Wide → close.** The whole environment, then a macro detail.
- **Question → reveal.** Set up tension, then resolve it.
- **Context → proof → implication.** What's happening, what was done, why it matters.
- **Build → break → build.** After several structured slides, a deliberate composition change.

Monotony test: lay out every slide as a thumbnail strip. If three or more neighbours share a composition with no reason, break one. If every slide differs, there's no system (`visual-craft.md` §7). Pick 4–6 slide behaviours and vary within them.

## 4. Chapters and the turn

- A chapter divider is an editorial statement that advances the argument, not a label in a pill. Not "OUR CAPABILITIES", but a line with a verb and a stake ("MAKE COMPLEX THINGS CLEAR." "TURN EVIDENCE INTO BELIEF.").
- Read the chapter lines alone, in order. They should form the deck's argument in miniature.
- Credentials and pitch decks usually need one deliberate **turn**: from what we have done to what we could do next (`narrative-craft.md`, the turn). Design it as a hero moment, and design what comes after it to be visually stronger than what came before. The future should look bigger than the archive.

## 5. Case studies are stories

Not a grid of thumbnails. Each case study is a mini-story:

1. **Challenge:** one clear statement.
2. **Idea:** one memorable thought.
3. **Execution:** the real work at meaningful scale.
4. **Proof:** real outcomes or evidence, at its true status (§9).
5. **Relevance:** why it matters to *this* audience.

Select by what the case proves, not by how it looks. Write `THIS PROVES: [capability] for [this audience's need]` before choosing it. Three strong examples beat twelve thumbnails. The archive is proof, not the boundary of what the team can do.

## 6. Capabilities as outcomes, futures as scenarios

- Turn service lists into outcomes in the client's language (not "Strategy · Social · Film", but "Build the brand. Launch the product. Give experts a voice."), then show which capabilities enable each.
- "What's next" is a set of scenarios, not a menu: imperative, specific, visual ("SHOOT THE BRAND FILM." "REIMAGINE THE EVENT."). Each scenario gets its own visual moment, not a bullet.
- Only claim capabilities the team can actually deliver. Ambition is fine; misrepresentation is not (`selling-the-work.md` §8).

## 7. Information design

Charts and diagrams are editorial graphics: one highlighted insight, direct annotation instead of legends, minimal axes, type as part of the chart, the takeaway stated in the title. Use the `dataviz` skill for building. Never fabricate or "illustrate" data that doesn't exist.

## 8. Motion in decks

Motion must explain something: revealing hierarchy, sequencing an idea, showing how something works or moves, linking related states, controlling pace. Remove bouncing, arbitrary zooms, morphs, random fades and decorative loops. Ask: *what does this motion help the audience understand?* If nothing, cut it.

## 9. Imagery in decks: evidence comes first

Supplements `visual-craft.md` §5 for decks:

- **Priority:** the client's real product, people, places and work → real project documentation → archival material, macro crops, diagrams and typography → stock (fixed per `visual-craft.md` §5) → generated.
- **Generated imagery is a minority of the deck** (default ceiling about 10–20% of visuals), and only for what real assets can't show: future-state scenarios, speculative environments, impossible viewpoints, conceptual metaphor.
- **Never false evidence.** No generated people, products, procedures, case-study imagery or results presented as real. Label every generated or placeholder image. Regulated categories may forbid more; the client's knowledge governs.
- Where imagery is thin, use crops, typography, diagrams and documentation before reaching for something irrelevant.

## 10. Specificity test

Before locking a direction: cover the logo. Could this deck belong to a competitor, a consultancy, a tech company or anyone in the same category? If yes, add specificity: the brand's history, real product forms, its own imagery and language, category artifacts, cultural references, distinctive type, subject-specific metaphor. (This is `visual-craft.md` §7's brand-blind test applied to a whole deck.)

## 11. By operating mode

| Mode | Use |
|---|---|
| EXPLORE | §1–§2 to widen territories; rough thumbnail strips of 2–3 deck directions. No craft gates |
| DEVELOP | §3–§9 to build the sequence, chapters, case stories and hero moments |
| JUDGE | Final check (§13), specificity test (§10), evidence status (§9) |

## 12. Framework output

When proposing a deck direction:

```
VISUAL CONCEPT:      [the art-direction idea, one or two sentences]
WHY IT FITS:         [connection to subject and strategy]
REFERENCE BOARD:     [by territory, with BORROW / DO NOT COPY]
DESIGN SYSTEM:       type · grid · photography · color · graphic language · motion
SLIDE BEHAVIOURS:    [the 4–6 behaviours and when each is used]
CHAPTER LINES:       [read alone, in order]
HERO MOMENTS:        [3–5 slides that get disproportionate treatment, and why]
ANTI-TROPES:         [the specific generic treatments this deck will refuse]
ASSET REQUIREMENTS:  [real photography, video, product, data, archive needed; who supplies it]
EVIDENCE STATUS:     [every claim, metric and case: confirmed / proposed / unknown]
```

## 13. Final check, per slide

- **Story:** does it advance the argument? Is the main idea obvious in five seconds?
- **Hierarchy:** is one element clearly dominant?
- **Specificity:** could it belong to another company?
- **Evidence:** is every claim supported and nothing visually fabricated?
- **Restraint:** what can be removed?
- **Rhythm:** does it contrast usefully with its neighbours?
- **Authenticity:** does it feel art-directed or assembled? If it feels like a template, redesign it.

## 14. Framework principle

A deck should feel authored by someone with a point of view, not assembled from components. Use the smallest part of this framework the deck needs.
