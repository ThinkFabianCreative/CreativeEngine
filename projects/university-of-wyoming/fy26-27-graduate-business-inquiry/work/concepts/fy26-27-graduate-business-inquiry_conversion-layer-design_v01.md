# Conversion layer · visual system v01

```
CLIENT:     University of Wyoming (College of Business)
PROJECT:    FY26–27 Graduate Business Inquiry Campaign (handle)
MODE:       DEVELOP · internal · 2026-09-15 · design-champ
DIRECTION:  Andres chose "3" on 2026-09-15 to have word-smither and design-champ sketch the missing
            conversion layer (work/reviews/…_gtm-territory-fit_v01.md, "Architecture implied", item 3)
SOURCES:    S7 GTM Deck pp. 6, 10, 19–22 (PROJECT-LEVEL; TRAFFIK recommendation, not client approval) ·
            work/figma-agent-pack/10, 11, 12 · work/image-prompts/d2_program-imagery_v02.md ·
            shared/knowledge/meta-paid-ads (META-003–005 image, META-035–040 carousel)
COPY:       Aligned to work/concepts/…_conversion-layer-copy_v01.md (word-smither, same day, rough,
            not approved). On-asset placement of its lines is a design proposal; mismatches in §8.
SCOPE:      Online MBA build only (GTM priority program). Other programs inherit the grid later.
STATUS:     Rough, not client-facing. Deadlines, start terms, requirements, enrollment steps and advisor
            contact are unknown (Q10): placeholders only, visibly marked. No verdicts.
```

## 1. The system idea

**The campaign's full-stop week line takes on the task, and the gold moves off the trait onto the step: same type, same Brown, same deadpan, but the largest words are now what to do next.**

T2 already owns a typographic grammar: short caps phrases, each closed by a full stop ("TWO PEOPLE SHORT. KID'S RECITAL. MOVING DAY. SAME WEEK."). That grammar is a checklist without drawing a checklist. word-smither's bridge swaps one week item for the task ("…KID'S RECITAL. APPLICATION. SAME WEEK."). The conversion layer builds its frames on that line.

| Carries over from T2 | Changes in the conversion layer |
|---|---|
| T2 static order: week line on top, small gold rule, one dominant line, lockup bottom left | **Hierarchy flips.** In T2 the provocation is the largest type. Here the stage line (the task, in word-smither's voice) is largest. The T2 question/answer headline is not repeated on these assets |
| The full-stop week line | It carries the task as one of its items (word-smither's bridge). It is set **all White**. "SAME WEEK." loses its gold |
| Gold on one meaningful word | Gold marks **the task or the next milestone** (max 3 words): STARTED, PAPERWORK, DAY ONE, a step's verb. Never the date, the week line or the label |
| Montserrat Bold caps, flush left, no exclamation marks | Adds Montserrat Medium for fact values only (deadline, term) |
| UW Brown dominant, flat fills, White type | Default is **type-only on flat Brown.** Photography drops to one optional variant, where the T2 photo stands in for the week line |
| The small gold rule | In the carousel it becomes one continuous rule crossing the card seams |
| Logo component + legible program label | Lockup on **every** carousel card (conversion cards get seen out of order) |
| | A **fact strip** holds deadline and term, set as information, never as alarm |
| | **Words fall as the funnel narrows:** early stages carry a requirements line; admitted carries none |
| | **No line names the viewer's status** (word-smither rule 1). The asset is true for anyone who sees it |

## 2. Stage map (Online MBA)

On-asset lines come from copy v01. Placing them on the asset is design's proposal. When a line moves onto the image, the Meta headline field needs a different line (§8).

| Funnel stage (GTM p10, p22) | Template | Week line W (small, White) | Stage line A (largest) · gold | CTA (Ads Manager, not drawn) |
|---|---|---|---|---|
| 1 Inquired, no application | **(a)** or **(a-P)** | TWO PEOPLE SHORT. KID'S RECITAL. APPLICATION. SAME WEEK. | YOU'VE STARTED HARDER THINGS. · STARTED | Apply Now |
| 2 Application started, not submitted | **(b)** | TWO PEOPLE SHORT. KID'S RECITAL. HIT SUBMIT. SAME WEEK. (card 1) | Steps 1–3 are client facts · each step's verb | Apply Now |
| 3 Submitted, not complete | **(a)**, or **(b-DOCS)** when there are three distinct documents | TWO PEOPLE SHORT. [REQUIREMENT]. SAME WEEK. | STUBBORN WORKS ON PAPERWORK TOO. · PAPERWORK | Apply Now fallback; copy action "Complete the application." (button unverified) |
| 4 Admitted, not enrolled | **(d)** | TWO PEOPLE SHORT. KID'S RECITAL. DAY ONE. SAME WEEK. | EVERYTHING BETWEEN YES AND DAY ONE. · DAY ONE. | [CTA: client to approve]; working "See enrollment steps" |
| 5 Event attendees, recent UW grads | **T2 prospecting asset** (copy v01) · (a) only if a step-led version is wanted | as d2-program-set_v02 | — | Apply Now |
| Deadline flights (stages 1–3) | **(c)** | as the stage, ≤2 lines | as the stage, ≤2 lines | as the stage |

## 3. System tokens

```
GROUND      #492F24 UW Brown, flat, full bleed. Every frame.
TYPE        #FFFFFF White. Contrast on Brown ≈ 12.2:1.
GOLD        #FFC425. Only: (1) the rule, (2) one task/milestone phrase per frame, max 3 words.
            Gold on Brown ≈ 7.7:1. Never Gold on White. Black unused.
FONT        Montserrat (Gotham stand-in; label frames "Montserrat stand-in").
            Bold for message lines and labels. Medium for fact values.
            No Blackhawk Italic in this layer.
CASE        All caps. Tracking: display 0 to −1%; labels +6%.
LEADING     Display 100%; 48/64 px lines 110%.
MARGIN      W/15: 72 px on 1080 wide, 96 px on 1440 wide. 9:16 uses 72 (clears the 65 px side zone).
BASELINE    8 px grid.
LINE BREAKS Week line breaks only at full stops. No orphaned short word on a stage line.
```

**Type scale**

| Role | 1080×1080 | 1440×1800 | 1080×1920 | Copy-fit (per line, incl. spaces) |
|---|---|---|---|---|
| Stage line A, standard | 104 Bold | 136 Bold | 104 Bold | ≤ 12 characters, ≤ 3 lines |
| Stage line A, step-down (when a line needs 13–14) | 88 Bold | 120 Bold | 88 Bold | ≤ 14 characters, ≤ 3 lines |
| Stage line A, admitted large (only if ≤ 2 lines) | 128 Bold | 170 Bold | 128 Bold | ≤ 10 characters, ≤ 2 lines |
| Week line W, list L, support S, step detail | 48 Bold | 64 Bold | 48 Bold | ≤ 27 characters, ≤ 3 lines (W), ≤ 2 (others) |
| Fact value (deadline, term) | 48 Medium | 64 Medium | 48 Medium | ≤ 28 characters, 1 line |
| Fact label, program label | 32 Bold +6% | 40 Bold +6% | 32 Bold +6% | ≤ 36 characters, 1 line |
| Gold rule | 96 × 6 | 128 × 8 | 96 × 6 | |
| Logo component height | 80 | 104 | 80 | |

Size steps: 104/48 = 2.2, 88/48 = 1.8, 48/32 = 1.5. Character counts assume Montserrat Bold caps at about 0.7 em. Confirm in Figma with the real lines.

**Copy v01 lines fitted**
- YOU'VE STARTED / HARDER THINGS. → 88 px, 2 lines (14/14, the tightest; verify)
- STUBBORN / WORKS ON / PAPERWORK TOO. → 88 px, 3 lines (avoids orphan "TOO.")
- EVERYTHING / BETWEEN YES / AND DAY ONE. → 104 px, 3 lines
- Week lines break as TWO PEOPLE SHORT. / KID'S RECITAL. / APPLICATION. SAME WEEK. (3 lines)

**The 9:16 rule.** The Stories/Reels safe area (y 270–1248, x 65–1015) is almost exactly the 1:1 live area. Every 9:16 frame is the 1:1 layout at the same type sizes, shifted down 198 px. Top 0–270 and bottom 1248–1920 stay flat Brown with nothing in them (the (a-P) photo excepted, with no key content above 300).

**Lockup.** "UW Lockup Placeholder" component, White version, left edge on the margin. Program label "ONLINE MBA" to its right (40 px gap on 1080 wide, 56 px on 1440), centered on the logo's height. One brand mark: no typed university name. Zone: 1:1 y 928–1008 · 4:5 y 1600–1704 · 9:16 y 1126–1206.

## 4. Templates

Wireframes are 1:1. `[ ]` = copy slot. `[[ ]]` = client-fact placeholder with dashed box (§6). Heights listed are maxima.

### (a) Single stage static

Job: the task at its real size. Understood from the stage line alone.

```
┌──────────────────────────────┐
│ TWO PEOPLE SHORT.            │  W 48 · ≤3 lines · y 72–232
│ KID'S RECITAL.               │  all White
│ APPLICATION. SAME WEEK.      │
│ ▬                            │  gold rule · y 296
│ YOU'VE STARTED               │  A 88/104 · y 336–648
│ HARDER THINGS.               │  gold on STARTED
│                              │
│ [[REQUIREMENTS]]             │  L 48 · ≤2 lines · y 704–808 · optional at stage 1
│                              │
│ [LOGO]  ONLINE MBA           │  y 928–1008
└──────────────────────────────┘
```

| Element | 1080×1080 | 1440×1800 | 1080×1920 |
|---|---|---|---|
| Week line W (≤3 lines) | y 72–232 | y 144–360 | y 270–430 |
| Gold rule | y 296 | y 640 | y 494 |
| Stage line A (≤3 lines) | y 336–648 | y 704–1112 | y 534–846 |
| List L (≤2 lines) | y 704–808 | y 1184–1328 | y 902–1006 |
| Lockup | y 928–1008 | y 1600–1704 | y 1126–1206 |

Stage 3 uses the same frame: W "TWO PEOPLE SHORT. [[REQUIREMENT]]. SAME WEEK.", A "STUBBORN / WORKS ON / PAPERWORK TOO." (88), gold PAPERWORK, L = the outstanding documents as a full-stop list (client facts).

**(a-P) photo variant, stage 1 only.** The one place T2 photography returns, because this viewer most likely saw the hook. The photo *is* the week, so the week line is dropped. Top band: the Online MBA T2 detail frame (hands, hanger, tulle), same Brown-hour grade.

| Element | 1080×1080 | 1440×1800 | 1080×1920 |
|---|---|---|---|
| Photo band, full bleed | y 0–400 | y 0–704 | y 0–560 (costume inside y 300–540, x 65–1015) |
| Gold rule | y 448 | y 768 | y 608 |
| Stage line A (≤2 lines at 104/136, or ≤3 at 88/120) | y 488–752 | y 832–1180 | y 648–912 |
| List L (1 line, optional) | y 808–856 | y 1248–1320 | y 968–1016 |
| Lockup | y 928–1008 | y 1600–1704 | y 1126–1206 |

The photo meets flat Brown at a hard edge. No fade, no overlay (pack 10).

### (b) Three-card steps carousel

Job: the application as three finite moves. Card 1 works alone.

```
  CARD 1                     CARD 2                     CARD 3
┌──────────────────────┐┌──────────────────────┐┌──────────────────────┐
│ TWO PEOPLE SHORT.    ││                      ││                      │
│ KID'S RECITAL.       ││                      ││                      │
│ HIT SUBMIT. SAME WEEK││                      ││                      │
│ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬  │  one rule across both seams,
│ 1. [[VERB            ││ 2. [[VERB            ││ 3. [[VERB            │  ends at card 3 right margin
│    STEP ONE]].       ││    STEP TWO]].       ││    STEP THREE]].     │
│ [[DETAIL]]           ││ [[DETAIL]]           ││ [[DETAIL]]           │
│                      ││                      ││                      │
│ [LOGO] ONLINE MBA    ││ [LOGO] ONLINE MBA    ││ [LOGO] ONLINE MBA    │
└──────────────────────┘└──────────────────────┘└──────────────────────┘
```

| Element | 1080×1080 (master) | 1440×1800 (conditional) | 1080×1920 (Stories) |
|---|---|---|---|
| Week line W, card 1 only (≤3 lines) | y 72–232 | y 144–360 | y 270–430 |
| Gold rule | y 280. C1: x 72 → 1080. C2: x 0 → 1080. C3: x 0 → 1008 | y 560, same logic (x 96 / 1344) | y 478, same logic |
| Step: "1." + step (≤3 lines; line 1 = "1. " + ≤9 characters at 104, ≤11 at 88) | y 328–640 | y 624–1032 | y 526–838 |
| Detail (≤2 lines) | y 696–800 | y 1104–1248 | y 894–998 |
| Lockup, every card | y 928–1008 | y 1600–1704 | y 1126–1206 |

- **Numerals are White type, inline, in the full-stop grammar ("1.").** They give the order of a public process, not the viewer's place in it. No "OF 3".
- **Gold per card:** the rule plus the step's verb.
- **The rule is structure, not progress.** Same weight on every card. No segments, fills, percentages or color change along it.
- **Cards 2 and 3 leave the week-line band empty,** so steps and rule align across the swipe.
- **Steps are client facts** (Q10). The application's real steps have not been supplied.
- **(b-DOCS)** for stage 3: the three cards carry three outstanding document types, all `[[ ]]`.
- **In a deadline flight,** card 3's detail is replaced by the (c) fact strip. On 1:1 the strip rule sits at y 680, the label at 712–744, the value at 760–808 and the box at 696–824.
- **4:5 carousel is conditional:** META-036 lists 4:5 image-only for Instagram Feed but flags a conflicting help page. 1:1 is the master. Facebook Stories carousel ratio is also a source conflict (META-037).

### (c) Deadline window static

Job: make the date useful, not frightening. The stage line stays largest; the date is a timetable entry.

```
┌──────────────────────────────┐
│ [WEEK LINE, ≤2 LINES]        │  W 48 · y 72–176
│ ▬                            │  gold rule · y 232
│ [STAGE LINE                  │  A 88/104 · ≤2 lines · y 272–480
│  ≤2 LINES.]                  │
│ [[REQ. REQ.]]                │  L 48 · 1 line · y 536–588
│ ──────────────────────────── │  White 2 px rule · y 648
│ ┆[[TERM]] APPLICATION DEADLINE┆  label 32 · y 688–720
│ ┆[[DEADLINE: CLIENT SUPPLY]] ┆│  value 48 Medium · y 736–784
│                              │
│ [LOGO]  ONLINE MBA           │  y 928–1008
└──────────────────────────────┘
```

| Element | 1080×1080 | 1440×1800 | 1080×1920 |
|---|---|---|---|
| Week line W (≤2 lines) | y 72–176 | y 144–288 | y 270–374 |
| Gold rule | y 232 | y 480 | y 430 |
| Stage line A (≤2 lines) | y 272–480 | y 536–808 | y 470–678 |
| List L (1 line) | y 536–588 | y 880–952 | y 734–786 |
| Fact strip rule, White, full live width | y 648, 2 px | y 1056, 3 px | y 846, 2 px |
| Label "[[START TERM]] APPLICATION DEADLINE" | y 688–720 | y 1104–1144 | y 886–918 |
| Value "[[DEADLINE: CLIENT TO SUPPLY]]" | y 736–784 | y 1168–1232 | y 934–982 |
| Dashed placeholder box | y 672–800 | y 1088–1256 | y 870–998 |
| Lockup | y 928–1008 | y 1600–1704 | y 1126–1206 |

**Why it cannot read as fabricated urgency**
1. The date is never gold, never the largest element, never the first thing read.
2. The date is always paired with the term it serves. A deadline for something is information; a bare date is pressure.
3. **Absolute dates only.** No "TODAY", "TOMORROW", "THIS WEEK" or "DAYS LEFT": the ad cannot know when it is seen. This matches copy v01, which also rejects the GTM example "Finish your application today." (p10).
4. No countdown numerals, clocks, calendars, red, exclamation marks or scarcity words ("LAST CHANCE", "ONLY", "SPOTS").
5. **The date is typed per version, never a dynamic token.** Each version carries an Ads Manager end date before the deadline passes. A stale date is a false claim.
6. **If Q10 stays open, (c) does not run.** The strip is deleted, not softened (same rule as copy v01), and those stages use (a) or (b).

### (d) Admitted, not enrolled static

Job: one clear path after the hard part. No list; the only template where the 128/170 size is allowed.

```
┌──────────────────────────────┐
│ TWO PEOPLE SHORT.            │  W 48 · ≤3 lines · y 72–232
│ KID'S RECITAL.               │
│ DAY ONE. SAME WEEK.          │
│ ▬                            │  gold rule · y 360
│ EVERYTHING                   │  A 104 · ≤3 lines · y 400–712
│ BETWEEN YES                  │  (128, ≤2 lines, if the line fits)
│ AND DAY ONE.                 │  gold on DAY ONE.
│ [[ADVISOR / SUPPORT LINE]]   │  S 48 · ≤2 lines · y 768–872
│ [LOGO]  ONLINE MBA           │  y 928–1008
└──────────────────────────────┘
```

| Element | 1080×1080 | 1440×1800 | 1080×1920 |
|---|---|---|---|
| Week line W (≤3 lines) | y 72–232 | y 144–360 | y 270–430 |
| Gold rule | y 360 | y 640 | y 558 |
| Stage line A (104/136 ≤3 lines, or 128/170 ≤2) | y 400–712 | y 704–1112 | y 598–910 |
| Support S (≤2 lines) | y 768–872 | y 1184–1328 | y 966–1070 |
| Lockup | y 928–1008 | y 1600–1704 | y 1126–1206 |

- **No list line.** One thing remains.
- **Never names admission.** "YES" is shared between the university and the viewer (copy v01); nothing says "you're in". A mismatched or lapsed list then shows nothing false.
- **Support line** is GTM p6 "advisor support", a client fact. Enrollment steps and start term live in post text (copy v01). If the client wants a date on the asset, use the (c) strip in place of S.

## 5. Imagery rules for this layer

1. **Type-only on flat UW Brown is the default** for (a), (b), (c), (d). The viewer has met the campaign; attention now belongs to the task. Type-only also versions quickly per deadline and term.
2. **T2 photography returns only in (a-P)** (stage 1), as the same program's detail frame and grade from `d2_program-imagery_v02.md`. It replaces the week line, never sits beside it. No new placeholder generations for this layer. The final image comes from the released shoot.
3. **No campus, Laramie or state imagery on Online MBA** (pack 11). On-campus programs' (d) could later take a UW Photo Database people-in-action band like their end cards, under the same pack 11 exception. Not built here.
4. **No AI-generated people and no stock**, placeholder or final. The (a-P) placeholder carries "PLACEHOLDER IMAGE - not for external use" (32 px White, top left at margin; 9:16 at y 300).
5. **Do not borrow T3 student imagery.** Proof stays in its own layer with its own releases.
6. **No fake interface or implied tracking.** None of the following:
   - drawn buttons or CTA shapes
   - arrows or swipe cues
   - icons
   - checkboxes, checkmarks, ticks or strike-throughs on "done" items
   - progress bars, step dots, pagination, filled or empty states, percentages
   - "you are here" markers or one step highlighted within a full list
   - countdown timers, calendar or clock graphics
   - form fields, cursors, notification badges
   - email, phone or portal screenshots, and device mockups
7. **Numerals only in the carousel,** as process order. Single statics show no step position.

## 6. Placeholder marking

- **Copy lines** from copy v01: set as written, layer prefix `COPY v01—`. They are rough and unapproved.
- **Client-fact slots** (deadlines, start terms, requirements, steps, documents, advisor contact):
  - bracketed text such as `[DEADLINE: CLIENT TO SUPPLY]`
  - a 2 px White dashed outline 12 px outside the text
  - layer prefix `CLIENT FACT (Q10)—`
  - frame name suffix `_UNCONFIRMED`
- Nothing with a client-fact slot leaves internal comps until the fact is supplied and checked against the claim ledger.

## 7. Figma build block (Online MBA, templates a–d)

```
=====================================================================
UW · CONVERSION LAYER · ONLINE MBA · BUILD v01 (internal comps, not approved)
Attach with: 10_uw_brand_rules.txt, 11_uw_campaign.txt, 00–07 global pack.
OVERRIDES FOR THIS PAGE ONLY (pending a pack update, see flags):
  - Deadline, term, requirement, step and contact SLOTS are allowed as marked
    placeholders. Never type a real-looking date, term, requirement or contact.
  - Lockup on every carousel card; no separate end card.
  - "SAME WEEK." is White on these frames, not Gold.
Do not change the words in quotes. Words in [BRACKETS] are placeholders.
=====================================================================

PAGE: "Conversion layer v01 · Online MBA"
Rows: A (stage 1), A-P (stage 1 photo), A-3 (stage 3), B (stage 2, 3 cards edge
to edge), B-DOCS (stage 3 alt), C (deadline), D (stage 4).
Columns per row: 1080x1080 · 1440x1800 · 1080x1920.
Frame names: UW_CONV_OMBA_<ROW>_<1x1|4x5|9x16>[_C1|_C2|_C3]_UNCONFIRMED

GLOBAL
  Fill every frame #492F24 solid. Image fill only in A-P photo band.
  Montserrat. Bold for message text and labels; Medium for fact values only.
  All caps. Flush left. No centered text. No exclamation marks added.
  Text White #FFFFFF. Gold #FFC425 ONLY on the gold rule and the ONE phrase named
    per row. Never on dates, week lines, labels or logo.
  Margins 72 (1080 wide) / 96 (1440 wide). Text box width 936 / 1248.
  Leading: display 100%; 48/64 px lines 110%. Labels tracking +6%.
  Week lines break only after full stops.
  No gradients, shadows, glass, icons, drawn buttons, arrows, checkboxes,
    checkmarks, progress bars, dots, device or UI mockups.
  Layer prefixes: "COPY v01—" for quoted copy; "CLIENT FACT (Q10)—" for
    [CLIENT TO SUPPLY] slots, each with a 2 px White dashed stroke rectangle
    12 px outside its text bounds.
  Sticky note left of each row: "Copy v01 rough, not approved. Client facts: Q10."

LOCKUP (all frames)
  Instance "UW Lockup Placeholder", White variant. Height 80 (1x1, 9x16) / 104 (4x5).
  x = margin. Bottom edge 1008 (1x1) / 1704 (4x5) / 1206 (9x16).
  "ONLINE MBA" Bold 32 (1x1, 9x16) / 40 (4x5), +6%, White,
    x = logo right + 40 / + 56, vertically centered on the logo.
  Never type "UNIVERSITY OF WYOMING".

GOLD RULE
  Rectangle #FFC425, 96x6 (1x1, 9x16) / 128x8 (4x5), x = margin unless stated.

---------------------------------------------------------------------
ROW A · STAGE 1 · INQUIRED, NO APPLICATION
---------------------------------------------------------------------
                          1x1          4x5           9x16
W  Bold 48/64             y72  h160    y144 h216     y270 h160
   "TWO PEOPLE SHORT. / KID'S RECITAL. / APPLICATION. SAME WEEK."  (3 lines, White)
GOLD RULE                 y296         y640          y494
A  Bold 88/120            y336 h176    y704 h240     y534 h176
   "YOU'VE STARTED / HARDER THINGS."  Gold: "STARTED" only.
   If a line overflows, report it; do not shrink below 88/120.
L  Bold 48/64 (optional)  y704 h104    y1184 h144    y902 h104
   CLIENT FACT: "[REQUIREMENTS: CLIENT TO SUPPLY]"

---------------------------------------------------------------------
ROW A-P · STAGE 1 · PHOTO VARIANT
---------------------------------------------------------------------
PHOTO BAND full bleed: 1x1 y0 h400 · 4x5 y0 h704 · 9x16 y0 h560
  Online MBA "Costume on the locker" DETAIL frame (hands, hanger, tulle),
  d2_program-imagery_v02. Costume center-right; 9x16 inside y300–540, x65–1015.
  Hard edge onto Brown. No fade, no overlay.
  "PLACEHOLDER IMAGE - not for external use" Bold 32 White at x margin,
    y margin (9x16 y300).
No week line in this row.
                          1x1          4x5           9x16
GOLD RULE                 y448         y768          y608
A  Bold 88/120            y488 h176    y832 h240     y648 h176
   "YOU'VE STARTED / HARDER THINGS."  Gold: "STARTED".
L  Bold 48/64 1 line      y808 h48     y1248 h72     y968 h48
   CLIENT FACT: "[REQUIREMENTS: CLIENT TO SUPPLY]"

---------------------------------------------------------------------
ROW A-3 · STAGE 3 · SUBMITTED, NOT COMPLETE
---------------------------------------------------------------------
Same positions as ROW A.
W  "TWO PEOPLE SHORT. / [REQUIREMENT: CLIENT TO SUPPLY]. / SAME WEEK."
   (middle line is a CLIENT FACT box)
A  Bold 88/120 "STUBBORN / WORKS ON / PAPERWORK TOO."  h264 (1x1, 9x16) / h360 (4x5)
   Gold: "PAPERWORK" only.
L  CLIENT FACT: "[DOCUMENT 1]. [DOCUMENT 2]. [DOCUMENT 3]: CLIENT TO SUPPLY"
   max 2 lines

---------------------------------------------------------------------
ROW B · STAGE 2 · APPLICATION STARTED, NOT SUBMITTED · 3 CARDS
---------------------------------------------------------------------
Three frames per format, edge to edge: _C1 _C2 _C3.
                          1x1          4x5           9x16
W  (C1 ONLY) Bold 48/64   y72  h160    y144 h216     y270 h160
   "TWO PEOPLE SHORT. / KID'S RECITAL. / HIT SUBMIT. SAME WEEK."
   C2, C3: leave this band empty.
GOLD RULE (continuous)    y280         y560          y478
   C1: x = margin → right frame edge. C2: x 0 → right edge.
   C3: x 0 → frame width − margin. Same thickness everywhere. No segments.
STEP  Bold 104/136        y328 h312    y624 h408     y526 h312
   C1 "1. [STEP 1: CLIENT TO SUPPLY]."  C2 "2. [STEP 2 …]."  C3 "3. [STEP 3 …]."
   Numeral and period White. Gold on the step's first word (its verb) only.
   Step text is a CLIENT FACT box. Max 3 lines.
DETAIL Bold 48/64         y696 h104    y1104 h144    y894 h104
   CLIENT FACT: "[STEP DETAIL: CLIENT TO SUPPLY]"  max 2 lines
LOCKUP on every card.
Label the 4x5 column: "CONDITIONAL: 4:5 carousel support unverified (META-036)".

ROW B-DOCS · STAGE 3 ALT: duplicate ROW B.
   C1 W: "TWO PEOPLE SHORT. / [REQUIREMENT: CLIENT TO SUPPLY]. / SAME WEEK."
   Steps: "1. [DOCUMENT 1: CLIENT TO SUPPLY]." etc. Gold on the verb only.

---------------------------------------------------------------------
ROW C · DEADLINE WINDOW (runs only in dated flights; Q10)
---------------------------------------------------------------------
Build with ROW A-3 copy shortened to fit; if it does not fit, use placeholders
"[WEEK LINE, 2 LINES MAX]" and "[STAGE LINE, 2 LINES MAX]" and report.
                          1x1          4x5           9x16
W  Bold 48/64 ≤2 lines    y72  h104    y144 h144     y270 h104
GOLD RULE                 y232         y480          y430
A  Bold 88/120 ≤2 lines   y272 h208    y536 h272     y470 h208   Gold: one word as row A-3
L  Bold 48/64 1 line      y536 h48     y880 h72      y734 h48    CLIENT FACT
FACT RULE White full text width
                          y648 h2      y1056 h3      y846 h2
LABEL Bold 32/40 +6%      y688         y1104         y886
   CLIENT FACT: "[START TERM: CLIENT TO SUPPLY] APPLICATION DEADLINE"
VALUE Medium 48/64        y736         y1168         y934
   CLIENT FACT: "[DEADLINE: CLIENT TO SUPPLY]"  White. NEVER Gold. One line.
DASHED BOX around label + value: 1x1 y672 h128 · 4x5 y1088 h168 · 9x16 y870 h128
DO NOT: TODAY/TOMORROW/DAYS LEFT, countdowns, LAST CHANCE, ONLY, clocks,
  calendars, gold dates, date as the largest element.

---------------------------------------------------------------------
ROW D · STAGE 4 · ADMITTED, NOT ENROLLED
---------------------------------------------------------------------
                          1x1          4x5           9x16
W  Bold 48/64             y72  h160    y144 h216     y270 h160
   "TWO PEOPLE SHORT. / KID'S RECITAL. / DAY ONE. SAME WEEK."
GOLD RULE                 y360         y640          y558
A  Bold 104/136           y400 h312    y704 h408     y598 h312
   "EVERYTHING / BETWEEN YES / AND DAY ONE."  Gold: "DAY ONE." only.
S  Bold 48/64 ≤2 lines    y768 h104    y1184 h144    y966 h104
   CLIENT FACT: "[ADVISOR / SUPPORT LINE: CLIENT TO SUPPLY]"
No list. No photo. Nothing that says "admitted" or "you're in".

---------------------------------------------------------------------
SELF-CHECK BEFORE HANDING BACK
---------------------------------------------------------------------
- View each frame at phone width (375). Stage line readable alone? Label readable?
- One gold phrase per frame plus the rule. Gold never on a date or week line.
- 9x16: nothing above y270 or below y1248 except flat Brown (A-P photo excepted,
  with no key content above y300).
- No text below 32 px (1080 wide) or 40 px (1440 wide).
- Every CLIENT FACT has its dashed box and layer prefix.
- Carousel rule aligns across C1 → C2 → C3.
- Report every line that overflowed its slot, with its length, so copy can be cut.
=====================================================================
```

## 8. Flags

**Alignment with copy v01 (word-smither)**
1. **On-asset hierarchy.** Copy v01's bridge keeps "TOO STUBBORN TO STOP? / YOU SOUND LIKE A COWBOY." constant on the asset and swaps only the week line. This system drops the T2 headline from conversion assets and makes the stage line the largest type.
   - Reason: the viewer has seen the provocation, and "what do I do next" must read at a glance.
   - OPEN for creative-engine-director.
2. **Headline field would repeat the asset.** Copy v01's recommended headlines are Meta headline-field lines, and this system puts them on the image. Copy v01's own rule is that asset and footer must not repeat, so the headline field needs another line per stage.
   - Example: stage 1 option C, already used as the primary-text opener.
   - Stage 2 is also close to repeating itself: the asset week line ends "HIT SUBMIT. SAME WEEK." and headline A is "Same week. One more thing: submit."
   - For word-smither.
3. **Gold moves.** Copy v01's bridge inherits gold "SAME WEEK." This system sets the week line White and puts gold on STARTED, PAPERWORK and DAY ONE. The emphasis choice is a proposal. word-smither may prefer other words.
4. **Copy-fit.** Stage 1 and stage 3 lines need the 88 px step-down, and "YOU'VE STARTED / HARDER THINGS." is at the limit (14/14). For the deadline template, copy needs two-line versions of the week line and the stage line.
5. **Agreed, no change needed:**
   - no status language, and articles instead of possessives
   - no relative time; the GTM "today" example is rejected by both files
   - a deadline is deleted, not softened, when none is supplied
   - stage 4 CTA is not Apply Now
   - stage 5 reuses the T2 asset
6. **Parent casting** ("KID'S RECITAL") now appears in three conversion week lines as well as prospecting. The CD concern from 2026-09-13 applies with more weight.

**Brand pack and facts**

7. **Pack files 10 and 11 forbid what this layer needs.** Both ban "deadlines, dates or urgency" on any frame, and 11 defines a separate end card. The build block carries a page-only override. The pack needs a conversion-layer file or exception before any client-facing build. Not edited here.
8. **Q10 is open, so (b), (c), (d) and the L lines cannot go external.** None of these has been supplied:
   - deadlines
   - start terms
   - requirements, steps and document lists
   - advisor contact
   Requirement lines on the image are program facts, and pack 11 puts program facts in post text. Keep them to the minimum the task needs and check each against the claim ledger. Example: "GRE/GMAT not required" is stated only for the online M.S. Accounting (C35), never for the Online MBA.
9. **Hook divergence noticed, not resolved.** Pack 12 has "SOUNDS LIKE A COWBOY." with gold on two words. This task's context and copy v01 say "YOU SOUND LIKE A COWBOY." with gold on one word.

**Platform**

10. **Matched audiences.** Lists lag and deliver beyond the intended stage. Assets are written and designed to be true for any viewer.
    - Neither file found a Meta personal-attributes or custom-audience record in `shared/knowledge/meta-paid-ads/`. Verify before launch.
    - Audience minimums, refresh cadence and CRM upload consent are media and legal questions.
11. **CTA buttons are not drawn.** Button availability for "Complete the application" and "See enrollment steps" is unverified (copy v01). Destinations are unknown (Q11).
12. **Carousel formats.** 4:5 image carousel is SOURCE_ISSUE (META-036), and the Facebook Stories carousel ratio conflicts (META-037). 1:1 is the master. Check the Ads Manager placement preview.

**Craft**

13. **Sameness.** Several Brown type-only frames rotating monthly can blur together. Variety comes from:
    - stage hierarchy: list, then steps, then a single path
    - the (a-P) photo
    Frequency caps belong to media.
14. **Other programs are not built.** The grid transfers by swapping the label, the week line and the (a-P) photo. On-campus (d) needs the pack 11 campus exception. GTM p17 and copy v01 keep M.S. Finance off Meta conversion until its claims are confirmed.
15. **Estimates.** Characters per line assume about 0.7 em. Contrast is computed from the hex values (White ≈ 12.2:1, Gold ≈ 7.7:1 on Brown). Verify both in Figma.

**Predicted taste fit for Andres** (separate from brief compliance and quality; not his approval).
- **Likely fit:** the campaign's own list grammar doing the checklist's job instead of a UI device; the hierarchy flip as the visible shift from provocation to clarity; restraint.
- **Watch:** type-only Brown frames may feel under-designed next to T2's photography. (d) is probably the strongest single frame. (c) is the weakest: an honest fact strip is never exciting.
