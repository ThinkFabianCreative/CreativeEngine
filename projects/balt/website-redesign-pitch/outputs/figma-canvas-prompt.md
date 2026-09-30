# Figma Canvas agent prompt: Balt website redesign proposal deck

Copy everything below the line into the Figma Canvas agent.

---

Build a 15-slide presentation in this Figma file. Recreate each slide exactly as specified: sizes, positions, colors, type and copy. Do not add decorative elements, icons, gradients, shadows, rounded corners or stock imagery that are not listed. Do not rewrite any copy.

## Global setup

**Frames.** 15 frames, each 1920 × 1080 px, named "01 Cover" … "10 Next steps", "A Site performance" … "E Methods". Lay them out left to right with 200 px gaps. Clip content on every frame.

**Margins.** 128 px on all sides unless a slide says otherwise. The content area is 1664 × 824 px. Footer lines sit with their baseline block at y = 992 (bottom: 64 px).

**Color styles.** Create these as local color styles:

| Style name | Hex | Use |
|---|---|---|
| Balt/Forest | #0F2B21 | Dark slide backgrounds, photo scrims |
| Balt/Paper | #F2F1EA | Light slide backgrounds; text on dark |
| Balt/Ink | #16241E | Headings and primary text on light |
| Balt/Body | #4A5A52 | Body text on light |
| Balt/Label | #5E6E66 | Slide labels on light |
| Balt/Footnote | #6B7A72 | Footer source lines on light |
| Balt/Mist | #A9C2B5 | Labels and secondary text on dark |
| Balt/Green | #1F6B4C | Accent: big numbers, callouts, phase 1 rule |
| Balt/Lime | #C5DE5A | Used once only: the "No." on slide 06 |
| Balt/Rule | #C9CFC8 | 1 px divider lines on light |
| Balt/Muted | #9AA59F | Inactive phase numbers and rules |

**Fonts.** Sora (Light 300, Regular 400, SemiBold 600) for display; Public Sans (Regular 400, SemiBold 600) for text. Both are Google Fonts.

**Text styles.** Create these as local text styles:

| Style name | Font | Size / line height | Color |
|---|---|---|---|
| Display/Cover | Sora Light | 104 / 105% | Paper |
| Display/Answer | Sora SemiBold | 280 / 100% | Lime |
| Display/Stat | Sora Light | 160 / 100% | Green |
| Heading/H1 | Sora Regular | 72 / 110% | Ink |
| Heading/H2 | Sora Regular | 60 / 110% | Ink |
| Heading/Addendum | Sora Regular | 56 / 110% | Ink |
| Heading/Question | Sora Light | 56 / 115% | Mist |
| Row/Fact | Sora SemiBold | 44 / 110% | Ink |
| Row/Title | Sora SemiBold | 36 / 120% | Ink |
| Block/Title | Public Sans SemiBold | 32 / 120% | Ink |
| Lead/Scenario | Sora Light | 34 / 140% | Paper |
| Lead/Callout | Sora Regular | 36 / 130% | Green |
| Body/L | Public Sans Regular | 28 / 140% | Body |
| Body/M | Public Sans Regular | 26 / 150% | Body |
| Table | Public Sans Regular | 26 / 140% | Ink |
| Table/Small | Public Sans Regular | 24 / 140% | Ink |
| Label | Public Sans Regular | 26 / 140% | Label (on light) or Mist (on dark) |
| Footnote | Public Sans Regular | 24 / 140% | Footnote (on light) or Mist (on dark) |
| List/Large | Sora Light | 48 / 160% | Paper |

Label format on every slide: slide number, a middle dot, then a sentence-case title, e.g. "04 · What they find". No all caps, no letter spacing.

**Dividers.** 1 px lines in Balt/Rule, full width of their column. Rows are separated by a top rule; the last row also gets a bottom rule.

**Tables.** No fills or zebra striping. A 1 px Balt/Rule line under the header row and between rows. Header cells in Public Sans SemiBold, same size as the table. Cell padding 12 px vertical, 16 px horizontal.

**Photos.** Download these from Balt's public site and place them as image fills (Fill mode, centered crop):

| Name | URL |
|---|---|
| IMG-Brain-scans | https://baltgroup.com/wp-content/uploads/homebanner-1.jpg |
| IMG-Loupe | https://baltgroup.com/wp-content/uploads/home-greenSec-hero@2x-scaled.jpg |
| IMG-Physician-monitors | https://baltgroup.com/wp-content/uploads/ourImpact-accordion1@2x-scaled.jpg |
| IMG-Cleanroom-team | https://baltgroup.com/wp-content/uploads/homefam.jpg |
| IMG-Catheter-hands | https://baltgroup.com/wp-content/uploads/cg-careers.jpg |

**Scrims.** Photo overlays are rectangles filled with a linear gradient of Balt/Forest (#0F2B21) at the opacities given, from left (0%) to right (100%).

---

## 01 Cover (dark, full-bleed photo)

- Background: Balt/Forest.
- IMG-Brain-scans: x 0, y 0, 1920 × 1080.
- Scrim: 0% at 94% opacity, 45% at 80%, 100% at 15%.
- Label, Mist, x 128, width 1150: "Balt · Website redesign proposal"
- Display/Cover, x 128, width 1150, bottom-aligned so the block ends about y 880: "More people are looking at Balt than ever. Make sure they see the leader."
- Footnote, Mist, x 128, y 992: "Andres Fabian, Creative Director, TRAFFIK · [Date]"
- Stack label and headline with a 40 px gap, anchored to the bottom of the content area.

## 02 Since 2022 (light, photo right)

- Background: Balt/Paper.
- IMG-Loupe: x 1200, y 0, 720 × 1080.
- Left column, x 128, width 960, top 128, vertical gap 48:
  - Label: "02 · Since 2022"
  - Heading/H1: "Balt is making headlines"
  - Four rows, each a two-column grid (260 px + rest, 32 px gap), 24 px vertical padding, top rule; last row adds a bottom rule:
    - Row/Fact "$400M" · Body/L "Investment announced in the US"
    - Row/Fact "Irvine" · Body/L "A second building, now open"
    - Row/Fact "China" · Body/L "New offices opened"
    - Row/Fact "Peripheral" · Body/L "Moving beyond neurovascular"
  - Body/L: "Plus coverage in Les Echos, BFM and the Orange County Business Journal, and a portfolio of 20 devices."
- Footnote, x 128, y 992, width 960: "Source: baltgroup.com newsroom and homepage, 2026."

## 03 After the headline (light, photo left)

- Background: Balt/Paper.
- IMG-Physician-monitors: x 0, y 0, 808 × 1080.
- Right column, x 936, width 856, vertically centered between y 112 and y 968, vertical gap 28:
  - Label: "03 · After the headline"
  - Sora Regular 52 / 110% in Ink: "Everyone who reads about Balt checks the website next"
  - Four rows, 14 px vertical padding, top rules, bottom rule on the last. Public Sans Regular 26 / 135% in Ink, with the first word or words in Public Sans SemiBold:
    - "**Physicians** deciding whether to trust a device in the most delicate procedures there are."
    - "**Talent** choosing between Balt and the biggest names in medtech."
    - "**Partners**: hospitals, distributors and investors sizing up a $400M commitment."
    - "**Press** checking whether the story matches the company."
  - Sora Regular 28 in Green: "For most of them, the website is their first handshake with Balt."

## 04 What they find (light, big stat)

- Background: Balt/Paper. Content area 128 to 1792, gap 48.
- Label: "04 · What they find"
- Heading/H1: "The site still tells the story of 2022"
- Three-column grid, 56 px gaps. Column 1 is one column wide; the rows block spans columns 2–3.
  - Column 1: Display/Stat "15s", then Body/L "for the main content to appear on a phone. Google's "good" is 2.5 s. Mobile performance scores about 48 out of 100."
  - Columns 2–3: four rows, top rule each, 20 px top padding, 24 px gap. Body/L in Ink, bold lead-in in Public Sans SemiBold:
    - "**Products in a flat list.** 20 devices by name, not by condition or procedure."
    - "**Peripheral gets one sentence.** A major growth direction, barely visible."
    - "**Events stuck in 2022.** The featured event is the 2022 ESMINT congress."
    - "**The numbers disagree.** "More than 45 years" in the copy, "48 years" in the stats."
- Footnote, y 992: "Our review of public pages. Lighthouse lab test, single run, Sept 2026; details in Addendum A."

## 05 What physicians get elsewhere (light, table)

- Background: Balt/Paper. Gap 40.
- Label: "05 · What physicians get elsewhere"
- Heading/H2, width 1664: "Competitors are building physician experiences. A copy update won't close that gap."
- Table (Table style), full width, columns 40% / 40% / 20%:

| Physician experience | Who offers it | Balt today |
|---|---|---|
| Video library: talks, interviews, cases | Penumbra, Medtronic | None |
| Case library and clinical evidence hub | Penumbra, Stryker, Terumo Neuro | None |
| Product finder by condition or use | Terumo Neuro | A–Z list |
| Education and training platform | Stryker, Medtronic | None |
| MRI tool, ordering, medical info request | Penumbra, Medtronic, Terumo Neuro | Contact form |

- Callout: 2 px Balt/Green top rule, 24 px padding above text, Lead/Callout: "We found no neurovascular leader that lets physicians explore devices in 3D online. Balt could be first."
- Footnote, y 992: "Public competitor websites, reviewed Sept 2026. Some content sits behind HCP gates. Details in Addendum C."

## 06 The answer (dark, typographic)

- Background: Balt/Forest. Content vertically centered, gap 40.
- Heading/Question, width 1500: "Does Balt's brand and digital experience match where Balt is now, and where it's headed?"
- Display/Answer: "No."
- Public Sans Regular 34 / 140% in Paper, width 1400: "We recommend redesigning baltgroup.com, starting with a two-day Growth Sprint that shapes it."

## 07 Picture it (dark, full-bleed photo)

- Background: Balt/Forest.
- IMG-Cleanroom-team: x 0, y 0, 1920 × 1080.
- Scrim: 0% at 20% opacity, 45% at 85%, 100% at 95%.
- Text column: x 888, width 904, vertically centered, gap 32:
  - Label, Mist: "07 · Picture it"
  - Four Lead/Scenario paragraphs:
    - "A neurointerventionalist in Boston finds the right microcatheter in two taps, between cases, on her phone."
    - "A vascular surgeon discovers Balt's peripheral range and asks for a rep."
    - "An engineer reads about the new Irvine building and applies that night."
    - "A physician in Paris gets the same experience, in French, just as fast."
- No quote marks, bars or icons.

## 08 The redesign (light, four phases)

- Background: Balt/Paper. Gap 56.
- Label: "08 · The redesign"
- Heading/H1: "Four phases, from sprint to relaunch"
- Four equal columns, 40 px gaps. Each has a top rule, 16 px internal gap: a number in Sora Light 64, a Block/Title, then Body/M.
  - Phase 1 has a 6 px Balt/Green top rule and a Green number. Phases 2–4 have 1 px Balt/Muted rules and Muted numbers, with 33 px top padding (28 px on phase 1) so the text baselines align.
  - "1" · "Growth Sprint" · "Priorities, audiences, product structure, scope. The Blueprint."
  - "2" · "Strategy and structure" · "Site map, product architecture, content plan, platform choice."
  - "3" · "Design and build" · "Brand evolution, design system, prototypes, build, English and French."
  - "4" · "Relaunch" · "A campaign introducing the new Balt to physicians and partners."

## 09 Why it's a safe investment (light, rows)

- Background: Balt/Paper. Gap 48.
- Label: "09 · Why it's a safe investment"
- Heading/H1: "A small first step, then one decision at a time"
- Three rows, each a grid of 480 px + rest with a 48 px gap, 28 px vertical padding, top rules, bottom rule on the last. Row/Title on the left, Body/L on the right:
  - "Start small" · "Phase 1 is a fixed-scope sprint: about five weeks, two days of your team's time."
  - "Your team decides" · "Leadership, field, R&D and marketing set the priorities together, so the scope holds."
  - "Approve each phase" · "Every later phase is scoped from the sprint and approved on its own."
- Body/M in Label color: "The sprint uses established methods: GV's Brand Sprint, LUMA Institute and Lean Canvas. See Addenda D and E."

## 10 Next steps (dark, full-bleed photo)

- Background: Balt/Forest.
- IMG-Catheter-hands: x 0, y 0, 1920 × 1080.
- Scrim: 0% at 95% opacity, 50% at 85%, 100% at 30%.
- Content vertically centered, x 128, width 1100, gap 48:
  - Label, Mist: "10 · Next steps"
  - Numbered list, List/Large:
    1. "Approve Phase 1, the Growth Sprint"
    2. "Name the decision-maker and the room"
    3. "Open analytics access, book interviews"
    4. "Set the sprint date: [Date]"
- Footnote, Mist, y 992: "Andres Fabian, Creative Director, TRAFFIK"

---

## Addendum slides (all light: Balt/Paper background, gap 40)

### A Site performance

- Label: "Addendum A · Site performance"
- Heading/Addendum: "Lighthouse results, baltgroup.com"
- Two columns, 3fr and 2fr, 64 px gap.
  - Left, table (Table style), columns 40/20/20/20:

| Measure | Mobile | Desktop | French, mobile |
|---|---|---|---|
| Performance | 48 | 68 | 48 |
| Accessibility | 91 | 94 | 91 |
| Best practices | 79 | 78 | 79 |
| SEO | 92 | 92 | 100 |
| Main content visible | 15.0 s | 3.2 s | 11.5 s |
| First content visible | 7.6 s | 2.3 s | n/a |
| Layout shift | 0.161 | 0.034 | n/a |

  - Right: Block/Title "Biggest mobile savings"; a bulleted list in Body/M: "Render-blocking files: about 5 s", "Text compression: about 2 s", "Unused JavaScript: about 1.7 s", "54 requests not on HTTP/2", "Redirect chains: about 0.9 s"; then Body/M "Google's "good" threshold for main content: 2.5 s."
- Footnote, y 992: "Lighthouse 12 lab test, single run per page, Sept 2026. Not real-user data; scores vary a few points between runs."

### B Platform

- Label: "Addendum B · Platform"
- Heading/Addendum: "What the site runs on today, and what we'll assess"
- Two equal columns, 32 px gap, each with a top rule and 28 px top padding. Block/Title, then a bulleted list in Body/M:
  - "Today": "WordPress with a custom theme", "Hosted on WP Engine, behind Cloudflare", "TranslatePress for English and French", "GeoPlugin for location-based content", "Contact Form 7, cookie consent plugin"
  - "Assessed in Phase 1 and 2": "Speed, hosting and build quality", "How easy it is for Balt to edit and publish", "Multilingual and regional needs (US, France, China)", "Regulated content: IFUs, approvals, audit trail", "HCP-gated content and security review"
- Body/M: "The platform decision is made in Phase 2, from these requirements."

### C Competitor detail

- Label: "Addendum C · Competitor detail"
- Heading/Addendum: "What each competitor offers physicians online"
- Table (Table/Small), columns 22% / 78%:

| Competitor | Notable physician features |
|---|---|
| Penumbra | 30+ video library for US HCPs, filtered by specialty and procedure; cases; clinical evidence; MRI compatibility; regional sites incl. France |
| Stryker | SKILL education program; StrokEnomics economic and clinical data; evidence section; portfolio by stroke type |
| Terumo Neuro | Product finder by disease and by solution; clinical studies hub; medical info requests; order tracking; three regions |
| Medtronic | Medtronic Academy; MedEd video bytes; podcasts; product manuals; MR conditional search; online ordering |
| Balt | A–Z product list; newsroom; events; IFU and safety page; English and French |

- Footnote, y 992: "Public sites reviewed Sept 2026: penumbrainc.com, stryker.com, terumoneuro.com, medtronic.com. Gated content not reviewed."

### D Sprint agenda

- Label: "Addendum D · Sprint agenda"
- Heading/Addendum: "Two days in the room"
- Two equal columns, 32 px gap, top rules, 28 px top padding. Block/Title, then a bulleted list in Body/M:
  - "Day 1 · Understand": "What changed, and the evidence wall", "Brand Sprint: values, audiences, personality, competitive map", "Brand, business and digital reality check", "Overnight: what we heard vs. what the evidence shows"
  - "Day 2 · Decide": "Lean Canvas for priority product lines", "Physician journey maps and friction points", "Opportunities ranked by impact and effort", "Roadmap: Now, Next, Later, Test first"
- Body/M: "In the room: a decision-maker, marketing, field or clinical, R&D, and the site owner. Six or seven people. Facilitated by Andres Fabian."

### E Methods

- Label: "Addendum E · Methods"
- Heading/Addendum: "The methods behind the sprint"
- Three equal columns, 32 px gap, each with a 4 px Balt/Green top rule and 28 px top padding. Block/Title, then Body/M:
  - "GV Brand Sprint" · "Values, audiences, personality sliders and competitive landscape. Shared language for who Balt is now."
  - "LUMA Institute" · "Rose/Thorn/Bud on the evidence, Experience Diagramming for journeys, the Importance/Difficulty Matrix to rank."
  - "Lean Canvas" · "By Ash Maurya. Which segments and products lead, and what makes Balt different for each."
- Body/M: "Every exercise starts with silent individual writing, so the whole room is heard. Evidence and opinion are labeled separately."

---

## Final checks

- All text uses the local text styles, and all colors use the local color styles. No unstyled text.
- No rounded corners, drop shadows, gradients (other than the photo scrims), icons or emoji.
- Lime (#C5DE5A) appears only on slide 06.
- Every frame is exactly 1920 × 1080, and no text crosses y 1016 or the 128 px side margins, except the photo edges.
- Keep [Date] as a visible placeholder.
