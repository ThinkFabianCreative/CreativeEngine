# MFK type pairings with the new families — v01

CLIENT Miracles for Kids · PROJECT website-rebrand · MODE DEVELOP (aesthetic pass) · Author design-champ · 2026-10-17
Method: `shared/frameworks/typography.md`. Inputs: brief §10, `tokens/mfk-type-tokens_v01.json`, current prototype (Outfit + Caveat, M3 Expressive 320/900).
Status: exploration. None of these faces is brand-approved. Everything marked **[CHECK]** must be confirmed against the font files or in Figma before it goes in a token.

## Type jobs (what we are choosing for)
- Display/headline: carry warmth and confidence at 48–112px. Friendly, not toy.
- Body: disappear at 16px on mobile, navy on white. Trust lives here.
- Highlight/hand: the human voice, three placements only (hero, truth band, close). One or two words, never sentences.
- M3 Expressive: contrast comes from weight jumps within one family (lite against heavy), so the display face needs a wide range, ideally variable.

## 1. The five families

| Family | Best role | Known | Risks / must check |
|---|---|---|---|
| **Playpen Sans** (Google, OFL) | Highlight/hand; possibly short body-lg | Handwriting-style face built for early-reader legibility, very wide script coverage. Variable wght axis. Loaded in Figma Thin–ExtraBold (so 100–800, no Black) | Childish risk is the big one: as body or headlines it reads "classroom worksheet", which is exactly the condescension the brief rules out. As a highlight it is the most legible hand we have, far easier to read than Caveat at small sizes. No 900, so it can't take the heavy end of an Expressive pair. Free web use; self-host or Google Fonts |
| **Filson Soft** (Mostardesign, commercial) | Display + body, the system workhorse | Rounded geometric sans, wide static family Thin–Black with italics | Probably static, not variable **[CHECK]**, so Expressive uses named steps (Light 300 / Black 900), not 320. Rounded terminals soften long body text; test 16px x-height and paragraph colour against Outfit. Web licence needed, priced by pageviews. Check ¢, curly quotes, tabular figures for stats **[CHECK]** |
| **Anago** (commercial) | Display, maybe body | I have no verified detail on its designer, axes or weight list | Treat everything as unknown: weight range, variable or static, italics, glyphs, licence terms **[CHECK all]**. Judge in Figma once it loads. Only promote it if it beats Filson Soft at 16px body |
| **Bogart** (commercial) | Display only, as an editorial accent face | My understanding is a soft, wedge-serif display family with many weights **[CHECK]** | If it is the soft serif I expect, it brings donor-grade gravitas (feels like a publication, not an app) and keeps warmth. Risk: it pulls toward lifestyle-magazine or brewery-label if the weight is too heavy and too tight. Not for body at 16px. Licence and weight list **[CHECK]** |
| **Bakerie Rough** (commercial, rough display) | Highlight-display only, if at all | Hand-drawn, roughened display face | Least legible of the five. Rough edges break down at small sizes and on low-DPI Android. Likely few weights, not variable **[CHECK]**. Craft-fair / bakery-menu cliché risk. At most one word per page at 64px+, or a sticker/stamp. Never h2 or smaller |

Glyph checklist for every face before tokens: `$ ¢ % + , . – — ' ' " " & #` plus tabular lining figures, Spanish accents (á é í ó ú ñ ¿ ¡) since OC audiences include Spanish speakers, and how the "1" and "7" read in stats.

## 2. Three pairings

Sizes in px, desktop. Line-height in px. Letter-spacing in px. Mobile scales as in the v01 tokens (display about 0.55×, h1 0.6×, body unchanged at 16).

### P1 "Soft Ground" — Filson Soft / Filson Soft / Playpen Sans
One rounded geometric family does display and body, the way Outfit does now, but warmer and softer. Playpen replaces Caveat as the hand: more legible, more childlike in a way that reads as "a kid wrote this" rather than "a greeting card." The firm, softly rounded sans keeps donor trust; the kid's voice appears only in three spots.
Expressive strategy: lite Light (300) against heavy Black (900) inside one headline, for example "Kids are **fighting**." Body Regular (400), labels Bold (700). Playpen highlights at SemiBold/Bold so they hold weight against a Black headline.

| Role | Family | Style | Size | LH | LS |
|---|---|---|---|---|---|
| display | Filson Soft | Black (lite words: Light) | 104 | 96 | -2 |
| h1 | Filson Soft | Black / Light | 64 | 64 | -1.5 |
| h2 | Filson Soft | Bold | 40 | 48 | -1 |
| h3 | Filson Soft | Bold | 24 | 32 | -0.5 |
| stat | Filson Soft | Black, tabular figures **[CHECK]** | 56 | 56 | -1 |
| eyebrow | Filson Soft | Bold, uppercase | 14 | 20 | 1.5 |
| body-lg | Filson Soft | Regular | 20 | 32 | 0 |
| body | Filson Soft | Regular | 16 | 26 | 0.2 |
| caption | Filson Soft | Regular (Book if it exists) **[CHECK]** | 14 | 20 | 0.2 |
| button | Filson Soft | Bold | 16 | 24 | 0.3 |
| highlight-display | Playpen Sans | Bold | 96 | 96 | -1 |
| highlight-h1 | Playpen Sans | SemiBold | 56 | 56 | -0.5 |
| highlight-h2 | Playpen Sans | SemiBold | 36 | 40 | 0 |

### P2 "Storybook Serious" — Bogart / Filson Soft / Playpen Sans
Bogart's soft serif headlines read as a publication with something to say; Filson Soft body keeps it friendly and readable; Playpen is the child's voice. This is the most donor-credible pairing and the most distinctive against the round-sans default of the category (Jordan's rounds, Hyundai Hope on Wheels). Risk: three families is the limit; if Bogart is too heavy it gets "craft brewery."
Expressive strategy: Bogart Light against Bogart Black/ExtraBold in display and h1 only **[CHECK weights]**; h2 and below move to Filson Soft Bold so the serif stays special.

| Role | Family | Style | Size | LH | LS |
|---|---|---|---|---|---|
| display | Bogart | Black or ExtraBold / Light **[CHECK]** | 104 | 100 | -2 |
| h1 | Bogart | Bold / Light **[CHECK]** | 64 | 68 | -1.5 |
| h2 | Filson Soft | Bold | 40 | 48 | -1 |
| h3 | Filson Soft | Bold | 24 | 32 | -0.5 |
| stat | Bogart | Bold, lining figures **[CHECK]** | 56 | 56 | -1 |
| eyebrow | Filson Soft | Bold, uppercase | 14 | 20 | 1.5 |
| body-lg | Filson Soft | Regular | 20 | 32 | 0 |
| body | Filson Soft | Regular | 16 | 26 | 0.2 |
| caption | Filson Soft | Regular | 14 | 20 | 0.2 |
| button | Filson Soft | Bold | 16 | 24 | 0.3 |
| highlight-display | Playpen Sans | Bold | 96 | 96 | -1 |
| highlight-h1 | Playpen Sans | SemiBold | 56 | 56 | -0.5 |
| highlight-h2 | Playpen Sans | SemiBold | 36 | 40 | 0 |

### P3 "Outfit + Playpen" (buildable now) — Outfit / Outfit / Playpen Sans, Bakerie Rough as an optional single stamp
Keep the current Outfit system (variable 100–900, already tested on mobile, 320/900 Expressive contrast intact) and swap only the hand: Caveat → Playpen Sans. That fixes Caveat's weak small-size legibility and gives the hand a kid quality instead of a card quality. Bakerie Rough is allowed once, at most, as a sticker word in the close (for example "Miracles"), never as a token used elsewhere. Lowest risk, least new identity.
Expressive strategy: unchanged. Outfit 320 lite / 900 heavy; body 400; labels 600–700.

| Role | Family | Style | Size | LH | LS |
|---|---|---|---|---|---|
| display | Outfit | 900 / 320 | 104 | 96 | -2 |
| h1 | Outfit | 900 / 320 | 64 | 64 | -1.5 |
| h2 | Outfit | Bold 700 | 40 | 48 | -1 |
| h3 | Outfit | SemiBold 600 | 24 | 32 | -0.5 |
| stat | Outfit | 900, tnum | 56 | 56 | -1 |
| eyebrow | Outfit | Bold 700, uppercase | 14 | 20 | 1.5 |
| body-lg | Outfit | Regular 400 | 20 | 32 | 0 |
| body | Outfit | Regular 400 | 16 | 26 | 0.2 |
| caption | Outfit | Regular 400 | 14 | 20 | 0.2 |
| button | Outfit | SemiBold 600 | 16 | 24 | 0.3 |
| highlight-display | Playpen Sans | Bold (optional stamp: Bakerie Rough, close only **[CHECK style name]**) | 96 | 96 | -1 |
| highlight-h1 | Playpen Sans | SemiBold | 56 | 56 | -0.5 |
| highlight-h2 | Playpen Sans | SemiBold | 36 | 40 | 0 |

Playpen sizes are set slightly smaller than Caveat equivalents because Playpen has a larger x-height and wider set; verify optically in the hero.

## 3. Ranking and recommendation
1. **P2 Storybook Serious** — lead, if Bogart proves to be the soft serif I expect and has a real Light-to-Black range. Most ownable, best donor trust, still warm. Gated on Bogart loading in Figma and a licence quote.
2. **P1 Soft Ground** — the safe new identity; a likely fallback if Bogart disappoints. Gated on Filson Soft loading and its 16px body test.
3. **P3 Outfit + Playpen** — buildable right now with only Playpen loadable. Do it today as the baseline so P1 and P2 are judged against a working page, not against nothing.

Anago: not ranked until it loads. If it outperforms Filson Soft at 16px it can replace Filson in P1 or P2 body.
Next step for Andres: make the other four families visible to Figma (activate them in the OS/font manager and restart Figma or the Figma font helper), then I can test P1 and P2 on the hero, truth band, stat row and a 16px paragraph at 375px wide.

## 4. Avoid
- Playpen Sans or Bakerie Rough as body, h2 or button text. That is the toy/condescension trap.
- Two hand faces on one page (Playpen and Bakerie Rough together only if Bakerie is a single stamp).
- Hand highlights outside hero, truth band and close.
- Faking Expressive weights: no synthetic bold, no in-between values on static families (use named styles only).
- Bogart below 24px or in all caps eyebrows.
- Tight tracking on rounded faces at body size; rounded terminals already blur letter edges.
- Stats in a face without lining/tabular figures, and any stat that uses the unsupported claims (C11).
- Commercial faces in a shipped page without a confirmed web licence; for a pitch prototype, note the licence cost next to the recommendation.
- Four families. Three is the ceiling (P2), and the third must be the hand.
