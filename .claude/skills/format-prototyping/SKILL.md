---
name: format-prototyping
description: Design know-how for hi-fi interactive prototypes of creative executions - landing pages, rich media display units, Meta ad units, digital OOH, email and slideshows - built in Figma, Webflow or HTML. Use when an approved idea must be shown as a believable execution in its real format and context. Prototypes only, never production code.
---

# Format prototyping

A prototype is a promise about an execution. It must look like the real thing, in its real context, behaving the way the real thing can behave, and it must carry the idea. It is never production code.

This skill is method. DesignChamp owns the visual judgment; CreativeDirector owns selection. Taste for Andres lives in `shared/knowledge/ANDRES_CREATIVE_OS.md`; retrieve the sections a job needs rather than restating them here.

## When to use

- An idea has survived EXPLORE and needs to be seen as a real execution (DEVELOP), or prepared for review or client presentation (JUDGE).
- Someone asks for a mockup, prototype, comp or "show it in context" for any format below.

Do not use it to polish an idea that has not been chosen. Concept comes before polish: in EXPLORE, sketch the encounter roughly and stop.

## Fidelity by mode

| Mode | Prototype | Stop when |
|---|---|---|
| EXPLORE | Rough frames or a storyboard of the key moment. Greyscale, real words, no finish | The idea can be judged |
| DEVELOP | Hi-fi key moments and the one interaction that carries the concept | The weakness under test is answered |
| JUDGE | Hi-fi, in context, at real size, every state a reviewer will ask about | A reviewer could mistake it for the shipped work, and nothing in it overpromises |

## Format references

Read only the reference the job needs.

| Format | Reference |
|---|---|
| Landing page | `references/landing-page.md` |
| Rich media and HTML5 display | `references/rich-media-display.md` |
| Meta ad units | `references/meta-ad-units.md` |
| Digital OOH | `references/digital-ooh.md` |
| Email | `references/email.md` |
| Slideshow / presentation | `references/slideshow.md` |
| Choosing and working in Figma, Webflow or HTML | `references/build-environments.md` |

## Specifications come from verified knowledge

The references teach craft. They deliberately do not hold platform numbers.

| Format | Verified source |
|---|---|
| Meta | `shared/knowledge/meta-paid-ads/` (dated, source-linked) |
| Display and programmatic video | `shared/knowledge/ctv-programmatic-ads/` (IAB standards plus DSP and seller specs). The ad server, network or publisher spec for the actual buy still governs |
| Digital OOH | `shared/knowledge/dooh-ads/` (by venue, network and media owner). The media owner's plan spec still governs |
| Google and YouTube, TikTok, LinkedIn, Snapchat, Nextdoor | The matching `shared/knowledge/<platform>-ads/` module |
| Email | Not yet in CreativeEngine knowledge. Use the ESP's documentation or the assignment's spec, cited with source and date, or label the value UNVERIFIED |

Follow `shared/knowledge/channel-preferences.md`: channel, placement, creative format, goal, CTA and destination are separate facts. If the placement or format is not supplied and it would change the prototype, raise it. If the user says to proceed, record it as a PROTOTYPE ASSUMPTION on the handoff.

## Process

1. **Anchor the idea.** State the parent idea in one sentence. The prototype is an EXECUTION (`shared/frameworks/creative-object-taxonomy.md`, 10): it must make that idea stronger, not invent a new one.
2. **Identify the encounter.** Format, placement, device or environment, and the realistic attention budget: a glance, a scroll-past, a dwell, a session.
3. **Read the format reference** and retrieve verified specs.
4. **Find the format's job for this idea.** What must the idea do in this particular encounter that it does not have to do elsewhere?
5. **Storyboard the moments before building.** First glance, engagement, resolution or end state. Design the smallest state first.
6. **Choose the build environment** by what the prototype must prove (`references/build-environments.md`).
7. **Build it in context**, at real size, with real copy from WordSmither or clearly labeled placeholder copy.
8. **Run the fidelity check** below.
9. **Hand off** with the note below.

## Craft that holds across formats

**Design the worst realistic encounter first, then reward the best one.** Most people meet an ad for a moment and never interact. The idea must land in the glance; interaction and length are the reward for the few who stay.

**The idea must survive its smallest state.** Every format has one: the end frame or static backup, the first frame, the feed thumbnail, images-off, sound-off, a random frame of a DOOH loop, the subject line. If the idea dies there, redesign; do not decorate the larger state.

**Adapt the mechanism, do not shrink the layout.** A campaign's visual idea is a mechanism (a crop, a type behavior, a juxtaposition, a transformation) that re-composes for each canvas. Resizing one master across 9:16, 728×90 and a roadside board produces lifeless adaptation.

**One focal point, a short reading order.** Decide what is seen first, second and third. Constrained formats rarely afford a fourth.

**Judge type at its real viewing size.** Actual device pixels, arm's length, projection distance, road distance. A comp zoomed to fill a monitor lies. Type decisions (the type's job, hierarchy as reading order, legibility in the real placement, correct marks in production copy) follow `shared/frameworks/typography.md`. For video and sequential formats, story structure follows `shared/frameworks/narrative-craft.md`.

**Brand is part of the idea, not a tax on it.** Make the brand recognizable early through the mechanism, color, type or product, not only through a logo in the last frame.

**Motion must earn its place.** It reveals a relationship, explains a transition, sets hierarchy or enacts the concept. Every frame a viewer could land on must still communicate.

**Prototype only what the format can really do.** An interaction the real unit cannot support is a false promise. Build it only when asked, and flag it.

**Real content.** Real copy, realistic data, real product and plausible imagery. Lorem ipsum and "Jane Doe" hide problems the client will find later.

**Show it where it lives.** In a feed, on a publisher page, in an inbox, on a street, in a room. Context frames must be generic or official previews: never imply a mockup is a live placement, and never imitate a real publisher's page as if the ad ran there.

## Fidelity check

Run before a prototype leaves DesignChamp.

- [ ] The parent idea is legible in the smallest state.
- [ ] Shown at real size in a realistic context frame.
- [ ] Every value that came from a spec is cited, or labeled UNVERIFIED or PROTOTYPE ASSUMPTION.
- [ ] Key content respects the placement's safe zones and interface overlays.
- [ ] Copy is real or visibly marked as placeholder.
- [ ] Interactions and motion are within what the real format supports, or flagged.
- [ ] Brand mandatories and accessibility basics hold: contrast, legible sizes, a reduced-motion or static state that keeps the meaning.
- [ ] States a reviewer will ask about exist: end frame, hover or tap, expanded, error or success, dark mode, images-off, as the format needs.
- [ ] It is labeled as a prototype.

## Handoff note

```
PROTOTYPE: <execution name> · <format> · <placement>
PARENT IDEA: <one sentence>
ENVIRONMENT: Figma | Webflow | HTML · <link or path>
SHOWS: <moments, states, interactions included>
SPEC SOURCES: <source + date, or UNVERIFIED>
PROTOTYPE ASSUMPTIONS: <values chosen without a supplied spec>
BUILDABILITY FLAGS: <anything richer, heavier or less supported than the real format allows>
OPEN QUESTIONS: <what would change the work>
```

## Related tools

- Figma operations: the Figma plugin skills (`figma-use`, `figma-generate-design`, `figma-use-slides`, `figma-use-motion`). They provide the ability; this skill provides the design decisions.
- HTML prototypes can be published as private Artifacts for sharing.
- UX, accessibility, chart and stack checks inside web and app prototypes: `ui-ux-pro-max` (local search). Its generated design-system recipes are keyword matches, not direction (see `DesignChamp/skills/ui-ux-pro-max.md`).
- Presentations: `frontend-slides` for animated HTML decks (never deploy publicly without confirmation; see `DesignChamp/skills/frontend-slides.md`), `slides` (governed by `DesignChamp/skills/ui-ux-pro-max.md`), the `pptx` skill, or a Claude design artifact.
- Interface motion and interaction feel inside prototypes: `animate`, `apple-design`, `review-animations`, `animation-vocabulary`. Divergent variants in EXPLORE: `prototype`. Their interface-motion rules do not govern storytelling motion in ad formats (see `DesignChamp/skills/emil-kowalski-skills.md`).
- Web aesthetic direction: `design-taste-frontend` (Taste-Skill pack, `DesignChamp/skills/taste-skill.md`). Use its design guidance; its production stack rules (Next.js, package installs, performance targets) do not apply to prototypes. Its house look is a method, not a direction.
- Reference imagery and brand boards: `imagegen-frontend-web`, `imagegen-frontend-mobile`, `brandkit` (same record). Generation tests a decided idea; it doesn't find one (`shared/frameworks/barry-concept-art-direction.md` §2). No generated people where a brief requires real ones, and label every generated image as a placeholder.
- Display banners: `banner-design` (governed by `DesignChamp/skills/ui-ux-pro-max.md`). Its style presets are options, not the idea.

## Boundaries

- Not production code, not a specification library, not an evaluation framework.
- No performance claims. Craft guidance here is practice, not proof of outcomes.
- Holds no client facts. Client brand rules and mandatories come from `projects/<client>/client/`.
