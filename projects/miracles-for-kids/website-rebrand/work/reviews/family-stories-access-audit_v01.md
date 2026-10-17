# Family stories and video access audit, v01

```
CLIENT:   Miracles for Kids Charity
PROJECT:  website-rebrand
CHECKED:  2026-10-16, desktop, in-app browser + DOM inspection
SITES:    live miraclesforkids.org · Jordan's Webflow prototype miracles-for-kids-8843ee.webflow.io · MFK YouTube channel
WHY:      Andres, 2026-10-16: "people come to this site to read and learn about families and family stories,
          videos are the most compelling ways to take users on this journey, so family stories should be
          easily accessible."
```

## Live site (miraclesforkids.org)

| Check | Finding |
|---|---|
| Stories in the main nav | **No.** The nav has How We Help, Take Action, Why We Help, Contact Us, Donate, Volunteer Now. Family stories aren't in it. |
| Stories on the homepage | One carousel (Michelle, Kiara, Oziel) at about 4,500px of a 6,400px page, roughly 70% of the way down. "Read More" links to `/families-weve-helped/?fam=0–2`. |
| Stories page `/families-weve-helped/` | 3 family stories (the same 3) + 3 parent testimonials (Miranda M., Denise M., Diego O.). Text only. **No videos.** Links to the YouTube channel. |
| Video on the homepage | 1 YouTube embed, "20 Years of Miracles" (5:25), about 950px down. An anniversary film, not a family story. |
| Findability | Low. Reaching a story takes scrolling the homepage or knowing the URL. |

## Jordan's Webflow prototype

| Check | Finding |
|---|---|
| Stories in the main nav | **Yes.** "Family Stories" is a top-level nav item → `/family-stories`. |
| Stories on the homepage | A carousel of 10 story cards (Alexa, Efren, Alexander, Kimberly, Julio, Emerson, Jaxxon, Dailani, Sebastian, Mariah) at about 3,700px of a 9,800px page, roughly 38% down. Each links to its own page. Program tags on most cards. |
| Stories page `/family-stories` | A featured story slot plus "All Family Stories": **about 20 stories** (Darla, Alice, Marie, Greyson, Benbarry, Leonel, Jeremiah, Abraham, William, Jaxxon, Julio, Alexander, Mariah, Alexia, Isaias, Emerson and more). No filter by program or diagnosis. The featured area rendered blank until scrolled (the same reveal issue as the homepage hero). |
| Individual story page (`/family-stories/dailani`) | About 530 words, a headline, a donation module, then events and newsletter. **No video.** |
| Video | One background loop in the hero area (`heroLoop9_square.mp4`, muted, decorative). The "See the difference we make" section shows a play button over a still, but no video embed or lightbox was found in the page. **It appears not to play.** (Verify by clicking in a real browser.) |
| Story names | Different from the live site's names. Several (Darla, Willow, Remington) are also in round 2. Consent status unknown (Q2). |

## MFK's YouTube channel (youtube.com/user/miraclesforkids)

- **109 videos, about 102 subscribers.** Low reach. The site is the main way people would ever see these.
- **Family story videos exist and are ready to use:** *The Story of William, Battling Leukemia* (1:43, 2 months ago) · *Meet Willow and Her Family* (3:01, 4 months, 248 views, the most-viewed story) · *Kharter's Story* · *Where Are They Now: Terri* · *Jeremiah's Family – Where Are They Now?* (155 views) · *Berenice and Mayte – Where Are They Now?*
- Also: yearly commercials (2023: 361 views, 2024, 2025), *20 Years of Miracles*, gala and tea recaps, Surf & Paddle Camp TV features (FOX LA, KCAL), Birthday Bash, the Basket of Miracles news segments, Miracle Maker honorees.
- **New claims in the channel description:** "88 cents on every dollar raised channeled directly into its programs" and "100% of Fund-a-Family program donations given directly to each family"; "Founded in 2002." Added to the claim ledger as SOURCE-STATED. The 88¢ figure conflicts with Jordan's 84.2¢.

## What this means

1. **Neither site meets the need.** The live site hides stories (not in nav, 70% down, 3 stories, no video). Jordan's prototype fixed findability (nav item, 10 stories on the homepage, a 20-story library) but has **no playable family video anywhere**.
2. **The video content already exists.** MFK has at least six family story videos plus "Where Are They Now?" follow-ups. "Where Are They Now?" is a strong format: it proves the help worked over time.
3. **Design implications for P2 (aesthetic pass, design only):**
   - "Family Stories" as a top-level nav item.
   - A **story-led hero, or a story within the first screen and a half**: a family video as the centerpiece (William or Willow), with a clear play affordance.
   - A **video story rail** on the homepage: thumbnails with name, age, program tags and running time; "Watch their story."
   - A **story library** design: filter chips by program (Lifeline, Safe Haven, Balance, Boost, Pillars) and by format (Video, Read, Where Are They Now?).
   - **Story page template:** video first, then the written story, the family's own quote, the programs that helped, then a "Help a family like [Name]'s" donation card.
   - The donation card stays visible but secondary: the journey is story → feeling → gift.
4. **This shifts the brief:** the primary *behavior* is reading and watching family stories; the primary *ask* stays a monthly gift. The landing page's job becomes **take the visitor into a family's story, then let them help.**

## Not verified

The play button behavior was found by DOM inspection only, not clicked. Mobile not checked. Video embedding permissions and consent for each family (Q2).
