# Barry Concept Art Direction

> CreativeEngine shared framework. Owner `design-champ`. Used by `creative-engine-director` in review, and by `word-smither` when layout decides how a line is read.

## Attribution

This is an operational CreativeEngine framework. It is inspired by the concept-first approach the user associates with Pete Barry's *The Advertising Concept Book: Think Now, Design Later*.

- It was not built from notes on the book or from the book itself. The stages, tests, labels and examples below are CreativeEngine terminology.
- Do not claim that any test, label or example appears in Barry's book, or that the book structures art direction this way.
- Do not quote the book or invent quotations from it.
- Do not imitate or recreate published ads as ideas for a client.

## Purpose

This framework takes a visual idea from **thought to layout** without letting design come in before the idea exists.

```
TRUTH  →  CONCEPT  →  ROUGH  →  LAYOUT  →  CRAFT
          think now            design later
```

It answers:

```
IS THERE A VISUAL IDEA, OR ONLY A LOOK?
DOES IT SURVIVE AS A ROUGH?
DOES THE LAYOUT DELIVER THE IDEA IN THE RIGHT ORDER?
CAN IT BECOME A CAMPAIGN WITHOUT BECOMING A TEMPLATE?
```

It especially fights:

- style chosen before the idea exists
- polished rendering hiding a weak or missing concept
- AI image generation used to think instead of to execute
- layouts that put every element at equal volume
- a campaign that is one layout with the pictures swapped

## Related frameworks

| Framework | Relationship | Status |
|---|---|---|
| `pricken-idea-mechanisms.md` | Supplies the move (omission, fusion, reversal…) that creates the gap. This framework takes the idea through roughs and layout | Active |
| `hey-whipple-copycraft.md` | Idea and line craft. Its §12 generativity test applies to visual campaigns | Active |
| `creative-trajectory-evaluation.md` | Shared 1 + 1 = 3 gate (§10), Post-it idea (§4), divergence (§5) | Active |
| `creative-object-taxonomy.md` | Hero graphic, key visual and identity criteria. Separates visual identity from key visual | Active |
| `visual-craft.md` | Composition, grids, color, imagery craft, visual codes, systems and generic visual tells | Active |
| `typography.md` | Type job, selection and pairing, hierarchy, micro-typography, type as image, legibility in real placements | Active |

Where they overlap, the more specific treatment wins:

- **Which move creates the gap:** `pricken-idea-mechanisms.md`.
- **Whether the idea is simple enough:** this framework's rough test (§2) is the visual form of the Post-it idea in `creative-trajectory-evaluation.md` §4.
- **Type craft** (selection, pairing, hierarchy, micro-typography, legibility in the real placement): `typography.md`.
- **Remaining craft detail** (composition, grids, color, imagery systems, visual codes, systems, finish): `visual-craft.md`. This framework covers craft only where it decides whether the idea reads.

---

## 1. Think now, design later

Before any layout, typeface, palette or generated image, write:

```
TRUTH:        what must be understood or felt (from the work packet)
CONCEPT:      the visual idea in one plain sentence, without style words
AUDIENCE SEES: what is on the page, screen or wall, described literally
AUDIENCE GETS: what they realize
```

Test the concept sentence:

- **Style words only?** "Bold, minimal, vibrant, premium" describes a look, not an idea.
- **Technique only?** "3D render," "glassmorphism," "collage," "kinetic type" describes production.
- **Could any brand in the category run it?** The concept isn't specific yet.

If CONCEPT can't be written, the problem is conceptual, not visual. Go back to the truth, use the mechanisms, work with WordSmither or return the packet. Do not open a design tool to find the idea.

Exception: in EXPLORE, making things can be a way to think (a type experiment, a crop, a found image). That is legitimate as long as it is labeled exploration and judged by the idea it produces, not by its finish.

## 2. The rough test

A strong visual idea survives as a rough: a thumbnail, a stick-figure sketch, a written description of the frame.

- If the rough is boring, rendering will not save it.
- If the idea only works at full finish, check whether craft is the concept (legitimate, but rare and should be deliberate) or is covering for a missing one.
- Roughs are cheap. Make many, show few.

**Roughs in an AI workflow.** A generated image is a very finished rough. It adds lighting, styling and detail nobody decided on, and those details start to look like decisions.

- Decide the concept and the layout logic in words or simple sketches before generating imagery.
- Use generation to test whether a decided idea reads, not to browse for one.
- When an image is generated, judge the idea it shows, not the polish it came with.
- Before using an image-generation skill on CreativeEngine work, read its department record in `DesignChamp/skills/` (the index is `DesignChamp/skills/README.md`; a skill from a pack is covered in the pack's record, for example `identity-design` in `ui-ux-pro-max.md`). Its rules win: for `identity-design`, confirm each generation run on client work, naming the provider and what is sent, and treat the output as EXPLORE material. A skill with no record has not been reviewed for this use.

## 3. Who carries the idea

Decide early which element does the conceptual work:

| Led by | The idea lives in | Other elements |
|---|---|---|
| **Visual** | The image or action. May need no words | Copy, if any, adds a second meaning or brand link |
| **Verbal** | The line. Type may be the whole visual | Image, if any, sets context without repeating |
| **Visual-verbal** | The gap between image and line | Each withholds what the other supplies (1 + 1 = 3) |
| **Typographic** | The letterforms, their scale, cropping or arrangement | Type is the image, not a layer on top of one |
| **Behavioral** | What the audience does: scroll, tap, walk past, participate | Visual and copy set up the action |

Then remove anything that doesn't carry, support or sign the idea. A visual-led idea with a headline explaining the picture has two elements doing one job.

Work out the split with WordSmither. Neither discipline owns it by default.

## 4. Single-mindedness

One piece, one idea. A layout asked to communicate a benefit, an offer, a product range, a mission and an event usually communicates none of them.

- Identify the one thing the piece must do. Everything else is subordinate or elsewhere.
- Mandatories (legal lines, logos, required offers) stay. Make them clearly subordinate, never quietly remove them.
- When the brief demands several equal messages, surface the conflict to CreativeDirector or BriefMachine instead of designing a compromise.

Single-minded does not mean empty. Richness that carries the idea is allowed.

## 5. Layout delivers the idea

Layout decides the order in which the idea is received. Design that order on purpose.

```
FIRST:   what stops the eye (usually the image, the type or the anomaly)
SECOND:  what creates the question or turns the reading
THIRD:   what resolves it
LAST:    who it's from (logo, endline, CTA)
```

- **One dominant element.** Use scale, contrast, isolation or position to make one thing unmistakably first.
- **The reveal must come after the setup.** If the eye reaches the punchline before the premise, the idea is spoiled.
- **Brand at the right moment.** Too early and it's "an ad" before it's interesting; too hidden and the idea is remembered without the brand.
- **Space is a decision.** Negative space should direct attention or create tension. Empty space that points nowhere is just empty.
- **Conventions are tools.** Image top, headline, body, logo bottom right is a convention because it reads. Break it when breaking it serves the idea, not as decoration.

Test: **show the layout for two seconds.** What was seen, in what order, and was the idea received? Then check at real viewing size and distance: a phone feed, a bus shelter across the street, a banner at the edge of a page.

## 6. Image decisions are arguments

Every choice in the image either supports the idea or dilutes it.

- **Photograph, illustration, type, found object or nothing?** Choose by what the idea needs (credibility, abstraction, humor, speed), not by trend.
- **Casting, styling, props, location, light:** each is a claim about the audience and the brand. Specific details make the idea believable. Generic details make it stock.
- **Crop and viewpoint:** the crop can be the idea (what's left out), and the viewpoint decides whose experience it is.
- **Real vs rendered:** rendered imagery makes impossible ideas possible, but can make real claims feel fake. Check for anything that could read as a misleading product depiction.

Ask: *if this image were stock photography, would anyone notice?* If not, it isn't yet argued.

## 7. Type as concept

Before choosing a typeface, decide what the type does:

- **Carries a voice:** it sounds like someone.
- **Becomes the image:** scale, crop, arrangement or material is the idea.
- **Stays out of the way:** the image or the line leads, and type delivers it cleanly.

Each is valid. What is not valid is a dramatic typographic treatment with no job. Detailed selection, pairing, hierarchy and craft belong to `typography.md`.

## 8. Campaign: premise, not template

A visual campaign needs a rule that produces different executions, not one execution with the contents swapped.

```
CONSTANT:  what makes every piece recognizably this campaign (premise, device, tone, structure)
VARIABLE:  what changes so each piece is a new idea (situation, subject, audience, medium)
```

Test with three executions:

- Are they three ideas, or three pictures in one layout?
- Could a fourth be written from the premise by someone who hasn't seen the first three?
- Does each one work alone, and do they gain something together?
- Does the premise stretch into media with different behavior (video, social, out of home, experiential), or only resize?

A consistent layout and visual identity are useful. They are not the campaign idea. Use Whipple §12 and the taxonomy's campaign criteria alongside this.

## 9. Medium as part of the idea

Before designing for a format, ask what the medium itself offers:

- **Where** it's seen: location, context, what surrounds it, the moment of the day.
- **How** it's seen: glance, scroll, dwell, repeated exposure, sound on or off.
- **What it can do** that others can't: time and sequence (video, carousel), physical presence (out of home, ambient), response (interactive, social).

The strongest executions often use the medium's context as part of the idea rather than placing a finished image into a slot. Placement specs, safe zones and policies come from verified knowledge in `shared/knowledge/`, never from this framework.

## 10. Visual clichés

Watch for work retrieved from visual memory instead of found for the problem:

- **Stock human emotion:** diverse group laughing at a laptop, handshake, arms raised on a summit, person staring out of a window.
- **Category shorthand:** swooshes and speed lines for performance, leaves for sustainability, blue circuitry for technology, gold on black for luxury.
- **Product hero in a void:** the product floating on a gradient with light rays, with no idea attached.
- **Template layouts:** centered headline, neutral sans, generous margins, logo bottom right, on every job regardless of idea.
- **Trend surface as concept:** a fashionable look (grain, 3D chrome, glassmorphism, Y2K, brutalism) presented as if it were the idea.
- **AI finish:** everything evenly lit, smooth and detailed, with nothing decided.

These are warnings, not bans. A cliché used knowingly and visibly subverted can be the idea. Craft-level generic visual tells are in `visual-craft.md` §9.

## 11. By operating mode

| Mode | Use |
|---|---|
| **EXPLORE** | Many cheap roughs across different carriers (§3) and different mechanisms. Written frame descriptions and thumbnails over finished images. Don't apply cliché warnings or layout polish as filters yet. |
| **DEVELOP** | Take the strongest concepts to layout. Fix reading order, single-mindedness, image arguments and the campaign premise. Use the rough test to catch ideas that only work when rendered. |
| **JUDGE** | Is there a visual idea, or a look? Does the layout deliver it in the right order at real size? Is the campaign a premise or a template? Name clichés precisely. Judge rough-stage concepts as concepts, not as finished art. |

## 12. Presenting visual concepts

- Present the idea at the finish its stage needs. Over-rendered early concepts get judged on execution and anchor the room to details nobody decided.
- One board per concept: the concept sentence, the key visual or rough, and one or two extensions showing it can grow.
- Label roughs and generated comps as such. Never present a generated image as a photographed or produced result.
- Explain as little as the idea allows. If the board needs a paragraph to be understood, check the rough test again.

## 13. Framework output

When useful, surface:

```
CONCEPT:        [one plain sentence, no style words]
CARRIED BY:     [visual / verbal / visual-verbal / typographic / behavioral]
READING ORDER:  [first → second → third → brand]
IMAGE ARGUMENT: [the key image decisions and why]
EXTENSIONS:     [constant / variable, if a campaign]
RISK:           [most likely way it fails at real size or in real context]
```

Don't produce this wrapper when the user wants finished work and it would make the answer worse. Don't expose hidden chain-of-thought.

## 14. Framework principle

The art director's first job is the idea, not the look. Design comes later and does everything it can to make that idea impossible to miss.
