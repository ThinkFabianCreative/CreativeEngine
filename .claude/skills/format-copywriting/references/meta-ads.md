# Meta paid ads: copy

Covers copy for single image, video, Reels and Stories, carousel, collection, lead ads and click-to-message ads across Facebook, Instagram, Messenger, Threads and WhatsApp placements, where applicable.

## Specifications

Copy-field character recommendations, truncation behavior, hidden-field configurations, caption support and safe zones come from `shared/knowledge/meta-paid-ads/`:

- **Field recommendations per placement:** the "Text: primary / headline / description" rows in `image-specs.md`, `video-specs.md` and `carousel-specs.md`. They differ by placement and some values are not published.
- **Truncation and hidden fields:** `production.md`.
- **Caption-track support by placement:** `production.md`, `video-specs.md`.
- **Automated enhancements, partnership ads, lead forms and click to message:** `additional-experiences.md`, `formats-and-placements.md`.

These are recommendations, not enforced maxima, unless a record says otherwise. Never use QUARANTINED records. The final check is Meta's own placement preview. This reference holds craft only.

## The copy surfaces

| Surface | Where it appears | What it is for |
|---|---|---|
| On-asset type | Inside the image or video (DesignChamp composes it) | The idea's words, when the image needs them. Few words, part of the composition |
| Primary text | Above the asset in Feed placements; shortened with a "more" affordance | Context, voice, the reason to care. The first line must work alone |
| Headline | Below the asset, near the CTA button, in many placements | A short, specific payoff or proposition. Not a repeat of the primary text |
| Description | Below the headline, in some placements and configurations only | Supporting detail. Assume it may not show |
| CTA button | A platform label chosen from Meta's available options | The action. Copy should not duplicate it word for word |
| Card headlines (carousel) | Under each card | The card's own step in the sequence |
| Lead form screens | Intro, questions, privacy, completion | The value exchange and what happens next |
| Greeting and suggested replies (click to message) | Inside the messaging app | Starting the conversation the ad promised |

Which surfaces actually render depends on placement, objective and configuration. Some configurations hide the headline, description and CTA footer (`production.md`). Map the surfaces for each placement before writing.

## Craft by surface

**Primary text.**
- Front-load. The first line carries the reason to care, before the "more" cut.
- After the first line, add what the asset cannot say: context, proof, specificity, voice.
- Short often wins in Feed, but length is a choice for the idea. A story that earns attention may run longer, and its first line still has to stop someone.
- One idea per ad. Line breaks for breath, not a bulleted brochure.
- No URLs unless the record for that placement supports them.

**Headline.**
- The payoff under the picture: a specific proposition, offer, proof or twist that completes the thought without depending on the primary text.
- Short enough to read at a glance; check the placement's recommendation.
- It is not a caption of the image and not a second CTA.

**Description.** Optional reinforcement: a proof point, a condition or a detail. Nothing the ad depends on.

**CTA and destination.**
- Use the approved CTA wording exactly (`formats-and-placements.md`: exact approved CTA wording and eligible Meta CTA button are separate facts).
- The copy can motivate the action. It should not end "Click Learn More" beside a Learn More button.
- Promise only what the destination delivers.

**On-asset type.** Write it with DesignChamp:
- A few words per frame, readable on a phone at arm's length, inside safe zones.
- Legally required lines and offer conditions go where they will actually be seen, not in a field that may be hidden.

## Craft by format

**Single image.** One visual-verbal idea. Image and headline together should make one thought, 1 + 1 = 3. Resist fitting a brochure into the fields.

**Video, Reels and Stories.**
- The copy lives mostly inside the asset: supers, captions, VO.
- Fields may be minimal or hidden in vertical placements.
- Script it with `social-video.md`.
- Write primary text that supports the video's first seconds without spoiling the reveal.

**Carousel.**
- Card one is the hook and works alone. Each card has its own job: a step, a proof, a reveal, a comparison, a product.
- Card headlines progress; they are never the same line repeated. Give a reason to swipe: an unfinished thought or a sequence.
- The primary text frames the whole set, not card one only.
- If the sequence matters, check whether automation can reorder cards (`creative-best-practices.md`).

**Collection and Instant Experience.**
- The cover copy makes a promise that the tiles and experience keep.
- Instant Experience copy is its own designed space: short, scannable, one next action.
- It is not a landing page (`meta-paid-ads/README.md`).

**Lead ads (instant forms).**
- **Intro:** the value exchange in one or two sentences. What they get, and why now if a real reason exists.
- **Questions:** only what qualification needs. Plain labels. Every extra question is friction the copy must justify.
- **Privacy and consent:** use the wording from approved sources exactly; never write legal text.
- **Completion screen:** say what happens next and when, and give a useful next action.
- The form must deliver what the ad promised.

**Click to message.**
- The ad says why to start a conversation.
- The greeting continues that exact promise, in the brand's voice.
- Suggested replies are real questions people would ask.
- The conversation must be able to fulfill the ad.

**Partnership and creator ads.**
- The creator's voice is part of the asset: write talking points or a brief, not the brand's corporate copy in someone else's mouth.
- Disclosure and partnership labeling follow Meta's current setup and policy (verify). Never write copy that hides the paid relationship.

## Automated enhancements and text options

When flexible creative, multiple text options or Advantage+ enhancements are enabled:

- Every text option must work with every asset it may be paired with, and in any combination with the other fields.
- Enhancements may alter or generate text and media. Confirm what is enabled (`production.md`). A client's approval of the copy does not approve a generated variation.
- Variants should differ by hypothesis, not synonym (`SKILL.md`, "Variants and testing").

## Policy watch-outs

Meta's live review and current advertising policies decide. This knowledge base does not replicate them (`production.md`). Flag for verification against current official policy:

- language implying knowledge of the reader's personal attributes (health, finances, identity, beliefs, circumstances)
- before-and-after claims and body or health outcome claims
- special or regulated categories, such as housing, employment, credit, finance, politics and social issues, health, alcohol and education outcomes
- sensational, misleading or engagement-bait phrasing
- unsupported "free", price, discount or deadline claims

## Fidelity check additions

- [ ] Copy surfaces are mapped for every placement shown.
- [ ] The first line of primary text works alone.
- [ ] Headline and primary text do not repeat each other.
- [ ] Nothing essential lives in the description or a field that may be hidden.
- [ ] Carousel card headlines progress and card one works alone.
- [ ] Lead form or messaging copy delivers the ad's promise.
- [ ] Character counts are cited to the placement record and date.
