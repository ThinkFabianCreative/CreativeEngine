# Jordan's homepage, round 2 audit

```
CLIENT:   Miracles for Kids Charity
PROJECT:  Website rebranding and pivot (website-rebrand)
OBJECT:   Jordan's second attempt, Figma "MFK-Refinement" (JHMKRTXVYdvl5p58mvRQwT), page "Homepage 3" (2175:387)
          - 2175:793  "001-Homepage", 1620 wide: bold, playful version (running kid hero, heart Donate). Read as the latest.
          - 2175:388  "Frame 74": the in-between version (script "Miracles" hero, donation card kept, stat icons)
          - 2240:120  palette-overview
MODE:     JUDGE (diagnostic). Compared with round 1 (jordan-homepage-audit_v01.md).
CHECKED:  2026-10-16 from Figma screenshots. Not a live build.
```

## What changed from round 1

Jordan moved from the navy SaaS look to a **warm, playful, saturated** system:
- Royal blue, coral red, butter yellow, blush pink, pale blue
- A rounded humanist sans (Cabin-like) with brush-script accent words ("Miracles," "difference," "programs," "Miracle")
- Doodle shapes (stars, hearts, thumbs-up, apple)
- Hard-edged color blocks

The page is now hero → mission + stats → video → family stories → hospitals → five programs grid → "You can be their miracle" → events → newsletter/socials → Instagram → footer.

Round 1 critiques it **answers**:
- It no longer reads as a fintech template. It feels like a kids' charity.
- Real kids and families carry almost every section.
- The programs are a photo-and-color grid with a plain-language line each ("Rent, utilities, auto payments and groceries"). It's clear and warm.
- The mission line gets its own big block.
- The hospital wall is cleaner and better organized.

Round 1 critiques it **doesn't answer, or makes worse**:
- **The ask got weaker.** The round 1 hero donation module (one-time/monthly, amounts, ratings) is gone from 2175:793. There's a floating heart "Donate," a coral "Take Action" in the nav, and later a Donate button. The best conversion idea from round 1 was dropped. (It survives in 2175:388.)
- **The headline moved toward the cure promise.** "Help families in crisis to find **Miracles**." MFK pays bills and rent; families don't "find miracles." It promises an outcome MFK doesn't deliver and puts the brush script on that word.
- **"Miracle" is still only a slogan.** It appears in the hero, as "You can be their Miracle," and in the footer. None of it uses the bill-paid truth.

## Must fix before anyone sees it again

These are factual and QA problems. Some are probably part of the pushback.

1. **Wrong legal details in the footer.** The address reads "17852 17th St, Suite 105, Tustin, CA 92780" and the EIN reads **75-3149382**. MFK's published details are **17848 Sky Park Circle, Suite C, Irvine, CA 92614** and EIN **91-2160616**. A wrong EIN on a charity site is a serious error.
2. **The stats change in every version.** Families served: production says 2,100+, round 1 said 31,000+, round 2 says **1,500+**. "$70 Million raised to date" is unsourced. "22 Families currently housed" matches round 1. Every number needs a source (990, annual report, MFK confirmation).
3. **Lorem ipsum** in the video section and the hospitals section.
4. **Duplicated copy:** "relief starts with ~~starts with~~ you."
5. **The Instagram handle reads @miracles4kids.** MFK's is instagram.com/miraclesforkids. Check it.
6. **The family names changed again** (Willow, Remington, Darla), but story pages exist for Alexa, Efren, Dailani and others. Use real, consented stories only.

## Design critique

- **The hero image is the best idea on the page.** A kid running away from camera, with no illness signifiers, reads as dignity and freedom. It's the first image that implies a *result* instead of pity. Keep it as the image. The headline on top fights it.
- **The heart-shaped Donate is a gimmick.** It's a sticker sitting on the photo, it competes with the coral Take Action in the nav, and it puts a label inside a shape. It needs one clear, conventional primary button.
- **Too many accents.** Every section has a brush word, a doodle and a new background color (cream, butter, pale blue, pink, peach, royal blue). Every section shouts with equal volume, so nothing does. The script face carries the logo's DNA, which is good, but used everywhere it's decoration, not emphasis. Rule of thumb: one script word per screen at most, and only on the word that carries meaning.
- **The palette is broad and has no roles.** 2240:120 has around 25 swatches: navy, mid blue, slate, plum, rose, gold, yellow, three creams, two 7-step blue ramps, coral, two pinks, a peach. Nothing assigns a job (CTA, background, text, accent). The blues fight the logo's light blue, and the logo itself sits on a blue tab in the nav.
- **The program grid is strong, with two issues.** The checkerboard photos are real and joyful. But the stats are gone (round 1 had "379 families last year"), and the Pillars arrow shape reads as a "next" icon.
- **The "You can be their Miracle" section** repeats round 1 almost unchanged. Same girl, same glass card. It's still a good photo. It's the second hero on the page, so one of the two should go.
- **The 2175:388 middle version is the most balanced.** It has the donation card, a script accent and the stat icons, without the full carnival. If we keep anything structural, it's that hero.

## Round 1 vs round 2

| | Round 1 (Webflow) | Round 2 (Figma 2175:793) |
|---|---|---|
| Feels like MFK | No, generic SaaS | Yes, warm, kid-world, logo DNA |
| Primary ask | Strong (hero donate module) | Weak (heart sticker) |
| Headline | Generic ("vital relief… stability") | Overpromises ("find Miracles") |
| Proof | Strong but inconsistent numbers | Fewer numbers, still inconsistent; wrong EIN |
| Programs | Clear, with numbers | Warm, without numbers |
| Restraint | Too cold | Too loud |
| Finish | Live, animation risk | Lorem, duplicated copy, wrong footer |

**Read:** round 2 found the right temperature and lost the discipline. Neither round has an idea; both are a list of sections in a different style. The redesign needs a concept sentence before more styling (Barry, and principle 6). The best parts to combine are round 2's warmth and real photography, round 1's conversion mechanics and program numbers, production's truth line, and the footer line ("Helping the families who don't have time to ask for help").

## Still open

Who pushed back and on what, the build platform (round 1 was Webflow), sources for the stats, and the rebrand scope (palette and type are being changed with no brand decision behind them).
