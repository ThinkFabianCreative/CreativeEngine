# Jordan's homepage redesign audit, v01

```
CLIENT:   Miracles for Kids Charity
PROJECT:  Website rebranding and pivot (website-rebrand)
OBJECT:   Jordan's homepage, built in Webflow ("Made in Webflow" badge), captured as a flat image in
          Figma file "MFK-Andres" (9tYtPFq2Nek4tzaz5NOVq8), node 1:3 (1440 x 9046), plus a mission
          close-up at node 1:6. Production capture sits beside it at node 1:4.
MODE:     JUDGE (diagnostic). We don't know the client's actual pushback yet.
CAVEAT:   Checked live 2026-10-16 (see the end of problem list). Originally: this is a full-page screenshot of a live build. Some flaws below (blank bands, a duplicated
          donation card, half-faded text, a clipped heading) may be scroll-animation capture artifacts
          rather than design. Check them in the live Webflow link before raising them with anyone.
```

## Page order

1. Nav: About, Programs, Family Stories, Events | Take Action, **Donate** (a single primary button)
2. Hero: "Providing vital relief for families in crisis to find stability." Positioning line, heart-cropped photo of a staff member, and a **Quick Donation** card ("Give today, for a kid like change tomorrow," one-time/monthly toggle, $50/$100/$250/$500, Charity Navigator 4-star, Candid Platinum, Tax ID)
3. Mission statement band (cream): "We help families with critically-ill children battle bankruptcy, homelessness, hunger and depression…"
4. Stats band (navy gradient): **31,000+** families served, **84.2¢** of every dollar to mission, **9** hospitals, **$70M+** raised
5. Video (a mother and son, real people)
6. Family stories carousel: William, Dailani, Alexia, Emilia…, each with program tags
7. "Our five programs": Lifeline, Safe Haven, Balance, Boost, Pillars, each with a one-line description, a last-year number and an arrow
8. "You can be their miracle": real child against a wall. "A monthly gift covers a week of groceries, a co-pay, a therapy session…" with Join us and Donate Now
9. "Trusted by leading children's hospitals": logo wall
10. Upcoming events list (Gala, Wellness Fest, Thanksgiving, Holiday baskets)
11. Newsletter and socials
12. Instagram strip
13. Footer: "Helping the families who don't have time to ask for help," full sitemap (programs, every giving method, 360° Miracle, corporate partner), a giant "Miracles for Kids" wordmark

## What Jordan got right

Much of it fixes what we found in the production audit:

- **One primary ask.** Donate is the only filled button, and the donation module is in the hero with a monthly toggle and suggested amounts. That's the biggest conversion upgrade over production.
- **Proof up front.** Ratings in the donate card, a stats band on the second screen, the hospital wall.
- **The programs are finally the product.** All five get a row with a real number ("379 families," "387 sessions"). This is the best section on the page.
- **Real families replace stock.** William, Dailani, Alexia, the girl against the wall. Specific, unpolished, true.
- **Dollars become tangible.** "A week of groceries, a co-pay, a therapy session" is exactly the right move.
- **The footer line** "Helping the families who don't have time to ask for help" is the best new line on the page, and it's hidden in the footer.
- **The information architecture is cleaner.** About / Programs / Family Stories / Events, plus a full set of giving methods in the footer.

## Problems, ranked

1. **The headline is weaker than the truth it replaced.** "Providing vital relief for families in crisis to find stability" is category language that any social-services nonprofit could use. The sharp line (bankruptcy, homelessness, hunger, depression) is demoted to band 3. Copycraft (Whipple): "vital," "relief," "crisis," "stability" are interchangeable nonprofit words.
2. **The hero image does the wrong job.** A heart-cropped photo of a staff member at a desk shows the organization, not the family. The heart crop is a cliché, and it gets covered by the donation card, so the image never reads. Barry: who carries the idea? Here nobody does.
3. **"Give today, for a kid like change tomorrow"** reads as a broken sentence. It needs a copy fix whatever the direction.
4. **The numbers conflict with MFK's own site (OPEN divergence).** Production says **2,100+ families**; Jordan says **31,000+**. The $70M+ raised and the 84.2¢ figures have no visible source. With a charity's donors, one wrong number costs more trust than a good design earns. The source for each must be confirmed (990, annual report) before anything ships. **This may be part of the pushback.**
5. **It looks like a SaaS template.** Navy gradient blobs, mono-type eyebrow labels ("QUICK DONATION · SECURE," "OUR MISSION ———"), pill buttons, glass cards, a giant footer wordmark: the 2024–25 Webflow startup kit. Polished, but it could be a fintech site. Against principle 10 (predictable AI and template aesthetics) and principle 6 (craft doesn't replace an idea), the page modernizes without having a point of view. **Likely also part of the pushback** if MFK felt it didn't look like them.
6. **The brand drifted without a decision.** The script "Miracles" wordmark survives but nothing else of it does: script accents gone, magenta reduced to icons, a new peach button color. That's fine if this is the rebrand, but nobody seems to have made a brand decision. It's a style swap. (That's where the "Rebranding and Pivot" question comes in: what is the pivot?)
7. **Too much repetition.** Mission + stats + video + stories + programs + miracle CTA + hospitals + events + newsletter + socials + Instagram: about 12 bands, and three of them ask you to donate. The page tells the same thing three times before it tells you anything new.
8. **"Miracle" is still a slogan, not an idea.** "You can be their miracle" is the old "Be our miracle" reworded. The interesting tension (the miracle is a paid electric bill) is still unused.
9. **The hero renders empty on load (live check, 2026-10-16).** On https://miracles-for-kids-8843ee.webflow.io/ the first screen was a blank gradient on two of three loads at 1440 and on mobile at 375. The headline animates in word by word ("Providing / vital / relief…" are separate elements) and the donation card hadn't appeared after 3 seconds. A donor who lands and sees nothing leaves. Test on a real phone before treating this as final; it may be an emulation quirk, but text-reveal-on-load is a risk either way.
10. **Every heading is a word-by-word reveal** ("See / the / difference / we / make," "You / can / be / their / miracle"). It's the same motion everywhere, so it reads as a template effect, not emphasis. Screen readers and reduced-motion users need checking.
11. **Small issues:** low-contrast captions in the stats band, "Give today, for a kid like change tomorrow," a mistyped Lifeline line ("medicals stay; solvent and sheltered"), and about half the story cards with no program tags.

Live check resolved the capture caveats: the blank navy band is the "Our impact: by the numbers" heading mid-animation; "Our five programs" is a reveal, not clipped; the event rows do have dates and venues. There's no horizontal scroll at 375. The live page has 10 family stories (Alexa, Efren, Alexander, Kimberly, Julio, Emerson, Jaxxon, Dailani, Sebastian, Mariah), not the four in the capture. There's also a "5 Programs • 1 Promise" programs menu and program subpages at /programs/<name>.

## What's worth preserving into the redesign

Hero donation module (with copy fixed), the programs-with-numbers rows, real-family storytelling with program tags, the tangible-dollar line, the footer line, the single-Donate navigation, the proof stack.

## Questions for Andres

1. What was the actual pushback, and from whom (MFK marketing, CEO, the board)?
2. Jordan's prototype is Webflow (miracles-for-kids-8843ee.webflow.io); production is WordPress. Memory says our production path is Instapage. Which platform will the redesign be built on?
3. Which stat set is real?
4. Rebrand scope: new identity, or evolving the current one?
