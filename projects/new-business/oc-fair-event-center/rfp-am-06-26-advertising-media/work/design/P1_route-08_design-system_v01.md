# P1 · Route 08 · A Country of Its Own · Design system v01

```
FIGMA:   https://www.figma.com/design/rCMQj3IDdOSywkypDRwVoh (text styles "Country/…", variables "Country / Color", page "Templates": Components, Type system, Type match board)
DATE:    2026-10-22
STATUS:  Internal, EXPLORE → DEVELOP
```

## The logo family

| Version | Use | Asset |
|---|---|---|
| **Typographic lockup** (primary) | Light grounds; print, outdoor, social | `R08_wordmark-gold-swirl_v01.png` |
| **Typographic lockup, reversed** | Purple and dark grounds (tagline in cream) | `R08_wordmark-gold-swirl_v01_reversed.png` |
| **Zeppelin + layered lockup** (hero) | Film, welcome arch, cover, story/reel | Figma component "Logo / Zeppelin + layered lockup": blank blimp + lockup (no tagline) layered on the envelope + live "THE OC FAIR · FOUNDED MDCCCXC" in the banner (editable text property) |

Production note: the lockup is AI lettering. Redraw as vector before anything goes out, which also fixes the small swirl inconsistencies.

## Type (all Google Fonts)

Read of the lockup: a heavy, soft, bracketed Victorian display serif with ball terminals and swash capitals; the tagline is bracketed roman small caps.

| Role | Google Font | Figma text style | Why |
|---|---|---|---|
| Display / headlines | **Fraunces** Black (use the SOFT and WONK axes on the web) | Country/Display XL 160 · Country/Display 96 | Closest match to the lockup's lowercase: heavy, soft, bracketed, slightly quirky |
| Headline italic | **Fraunces** Black Italic | Country/Headline Italic 64 | The nation's exclamations: "Visa not required." |
| Swash accent (sparingly) | **Berkshire Swash** | Country/Swash Accent 56 | The lockup's curls and swash caps, for short phrases only: "Welcome to the Republic" |
| Official caps | **Playfair Display SC** Bold | Country/Official Caps 32 | Matches the tagline: passports, seals, banners, "Founded MDCCCXC" |
| Body | **Lora** Regular / Italic | Country/Body 24 · Body Italic (nation voice) | Storybook text serif, readable at length |
| Wayfinding | **Archivo** Bold / SemiBold | Country/Wayfinding 40 · Wayfinding Small 22 | The plain, accessible layer under the whimsy: signs, maps, accessible routes |
| Stamps and data | **IBM Plex Mono** Bold / Medium | Country/Stamp & Data 20 · Caption 14 | Passport numbers, stamps, official details |

Rejected from the match board: Caprasimo and Ultra (too blunt, no Victorian softness); Young Serif (too light); Cinzel (too Roman and wide for the tagline); Cinzel Decorative (too costume); Libre Caslon Display (too thin to sit with the lockup).

## Color (Figma variables "Country / Color")

| Token | Hex | Role |
|---|---|---|
| color/royal | #4B1A6E | Primary ground. Royal purple leads |
| color/royal-deep | #2A0C40 | Footers, sign-off bars, night |
| color/gold | #D9A441 | Metallic accent, stamps, ribbons, text on purple |
| color/cream | #FAF2E0 | Paper, light grounds |
| color/orange | #F46B17 | The OC Fair mark and flag; accent only |
| color/leaf, card, sky | #3E8E3A · #C8261E · #6FB3E8 | Region colors only |
| color/ink | #1C1410 | Text on cream |

## Components

Logo slots (3 versions above), Photo slot, Stamp / NORMAL (gold), Ribbon banner (gold, royal text), Sign-off bar, Lower third / Citizen.

## Visual source

Fairytale lore: Victorian-era carnival, The Wizard of Oz, Alice in Wonderland, Dr. Seuss, Disney's Sleeping Beauty (mood: Wonka, Tim Burton, Peter Pan's flying ship). Purple regalia and gold foil are shared fairytale language, not any brand's property. Texture: a little steampunk and retro-futurism, a touch of live-action Howl's Moving Castle and One Piece (a nation that arrives and moves on; the voyage and crew; the nation's machinery). The swirl lettering and the zeppelin are in the system (Andres, 2026-10-22).

## Rules

- Contrast: gold or cream on royal; royal or ink on cream. Check WCAG AA on every text color pair.
- One swash phrase per layout at most; the lockup carries the ornament.
- Every sign bilingual at equal size; wayfinding always has the Archivo layer.
