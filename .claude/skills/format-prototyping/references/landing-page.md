# Landing page

## The encounter

A landing page is a continuation, not a beginning. The visitor arrives mid-thought, carrying a promise made by an ad, email, post or link. They decide within the first screen whether this is what they were promised. Check the assignment's traffic source: when it is mobile placements, the phone is the primary canvas, not a responsive afterthought.

## The format's job

Keep the promise, prove it, and make one next step easy.

## Craft

**Message match.** The first screen should visibly continue the thing that sent the visitor: the same key visual mechanism, the same claim in the same words, the same offer. A different headline and a stock hero break the thread and make the ad feel like bait.

**The first screen answers three questions.** What is this? Why does it matter to me? What do I do? Proof belongs near the claim it supports, not in a testimonial band four sections down.

**One primary action.** Secondary actions exist but never compete visually. On mobile, consider keeping the primary action reachable (a sticky bar) once the visitor scrolls past it.

**Structure is an argument, not a template.** Order sections by what the visitor needs next: claim, proof, the objection they are holding, the action. The default anatomy (hero, three feature cards, logo strip, testimonials, pricing, FAQ) is a symptom of no argument.

**Carry the idea down the page.** The campaign mechanism should keep working below the fold: in section transitions, in how proof is shown, in the form. A page where the idea stops after the hero is a brochure with a campaign header.

**Forms are part of the design.** Ask only what the goal needs. Say what happens after submitting. Design the empty, focused, error and success states; success is the last impression.

**Typography and measure.** Headlines sized for the phone first. Body text at a comfortable measure. Test long real headlines, not the short ideal one.

## What to prototype

- Mobile and desktop at common real widths (for example a 390 px phone and a 1440 px desktop).
- The scroll narrative, including the transition from ad to first screen when presenting.
- One signature interaction that enacts the concept, if the concept has one.
- Primary CTA states and the form flow, through success.
- Sticky or persistent elements on mobile.

Skip exhaustive states for secondary pages and navigation that nobody will review.

## Buildability flags

- Scroll-hijacking, heavy WebGL, large background video: feasible but costly, and can hurt load on mobile networks.
- Interactions that Webflow or the client's CMS cannot reproduce without custom code.
- Content that depends on personalization or live data the client may not have.
- Claims, prices, deadlines and offers on the page must come from the client's reviewed evidence.

## Fidelity check additions

- [ ] Ad-to-page message match holds when the ad and first screen are shown side by side.
- [ ] The first screen works on a phone without scrolling.
- [ ] Every section earns its place in the argument.
