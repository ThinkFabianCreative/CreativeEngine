```
CLIENT:        Edwards Lifesciences
PROJECT:       tmtt-xlt-deck
SOURCE SCOPE:  PROJECT-LEVEL
DATE:          2026-10-07
OWNER:         design-champ
FORMAT:        visual-craft.md §12.1 Figma agent brief
```
# Figma canvas-agent prompts

Run each in the user's local Figma (Vesta Std installed). Each prompt is self-contained. Paste one at a time.

---

## Prompt A · Vesta text fixes, Design file (YQnErPzBivWfYbbxlUeAX5)

```
Fix text in the Edwards TMTT XLT deck, Design file, page "Slides — craft". Internal only.
Do not change any words except as listed. Do not add or remove quotes, colons, periods or footers. Keep Vesta Std, current sizes and weights.

SET UP
- Work only in section "FINAL SET" unless a step names another frame.
- Frames are 1920 × 1080. Outer margin 128 px. Type flush left.
- Color: red #C8102E (never tinted, no gradients), dark gray #505759, gray #898D8D, ground #F0EEEA-ish (keep as is).

PART 1 · FINAL SET (the delivery set)
1. Frame "FINAL 02 Pizza night", layers "A.", "B.", "C.", "D.": change each to "A", "B", "C", "D" (remove the period; the speaker's slide has no period).
2. Frame "FINAL 02 Pizza night": confirm the C row reads "Ask first, then order" / "The vegan, the picky kid, pineapple people…" (with the single ellipsis character). Do not change.
3. Frame "FINAL 03 The promise", layer "The full portfolio changes what is possible.": confirm the fill is flat #C8102E (gradient already removed). If any gradient remains, set fill to solid #C8102E.
4. Frame "FINAL 07 Ask first": KEEP the two red "&" separators between the three asks. They are Yash's original content. Do not remove, hide or restyle them beyond brand colour. Keep the white "&" in the red square. Do not add any other "&".
5. Frame "FINAL 01 Cover": confirm "XLT  |  October 2026" appears once only.

PART 2 · Source variants (only if the user wants them kept usable)
6. Frame "01 Cover" (A): "XLT | October 2026" appears twice. Delete the second instance; keep one, top-left above the title.
7. Frames "06 One story, orchestrated-B" and "06 One story, orchestrated - C":
   - "Portfolio promise" appears twice. Delete the duplicate; keep one in the ONE STORY list.
   - Change "THE "&" CREATIVE" to "The & creative" (no added quotes; match Yash's case as on his slide).
   - Restore these exact strings, missing from the variant:
     "Today  each therapy on its own calendar"
     "Adobe: one platform for each physician profile & journey"
     "Portfolio marketing" / "Audience intelligence"
     "Brand" / "Content system"
     "Digital" / "Orchestration"
     "2.7x" / "more case volume in accounts with ABX engagement"
   - Delete the footer "Do Not Reproduce Or Distribute" (not in Yash's slide).
   Note: FINAL 06 (built from frame 11:2) already has all of this; these variants are reference only.

DO NOT
- No gradients, vignettes, tints of #C8102E, rounded corners, drop shadows.
- No 3D, stone, ribbon or red-extruded ampersands. No generated imagery.
- Do not reword, re-case or re-punctuate any other text.
- Do not touch speaker notes.

REPORT
List each layer changed with before/after text, anything you skipped and why.
```

---

## Prompt B · Builds and animations, Slides file (sBqCMoTCaPupEZj9aRleUq)

> STATUS 2026-10-08: the builds are already implemented as magic-move build-state slides (22 slides; see build-spec.md). Use Prompt B only as a fallback if the deck goes back to 7 slides with object builds. Prompt D (poll) still applies.

```
Apply on-click builds in the Edwards TMTT XLT Figma Slides deck. Internal only.
Do not change any words, layout, colors or speaker notes. Slide transitions are already set (Dissolve 0.4 s, on click) on all 7 slides; leave them.

SET UP
- Build style for every element below: Fade in, 0.3 s, Ease out, On click.
- Elements listed under "Click N" appear together on that click. Elements not listed are visible on load.
- No fly-in, scale, rotate, bounce or color animation. Never animate the Edwards logo or the red square.

PART 1 · Slide 6 (lead; review it before continuing)
Slide "6":
  On load: "One story for every physician. In 2027 we orchestrate the right message to each of them at the right time"
  Click 1: "Today  each therapy on its own calendar" + its rule, the three "Field visit" ticks and labels on that rule, and the gray dots
  Click 2: "ONE STORY", "Portfolio promise", "Three pillars", "The & creative", "Therapy campaigns", "JOURNEY ORCHESTRATION", "who · what · when · where", "Adobe: one platform for each physician profile & journey"
  Click 3: "2027  a sequence built for each physician between visits" + its red rule, ticks, "Field visit" labels, dots and "Paid media", "ABX", "Social", "Web", "Email", plus "What we learn across the portfolio feeds the next conversation"
  Click 4: "Portfolio marketing", "Audience intelligence", "Brand", "Content system", "Digital", "Orchestration"
  Click 5: "2.7x", "more case volume in accounts with ABX engagement"

PART 2 · Other slides
Slide "2" (poll):
  On load: "LIVE POLL  ---  VOTE NOW", question, A–D with sub-lines, poll element
  Click 1: dark panel + "Your guests are not all the same. Neither are mitral and tricuspid patients."
  Click 2: "That’s the value of the full portfolio: the therapy fits the patient, not the other way around."
  Set the "&" text layer on this slide to hidden (flag to the user; do not delete).
Slide "3":
  Click 1: "Our promise: a portfolio and partner across the end-to-end mitral and tricuspid pathway to deliver patient-matched care."
  Click 2: rule + Empower, Enable, Elevate columns (all three together)
Slide "4": no builds. Select the video: Autoplay on, Loop off, Mute off.
Slide "5":
  Click 1: "EXTERNAL", "What customers told us", rule, 01 and 02 blocks
  Click 2: "INTERNAL", "What it asks of us", rule, 03 and 04 blocks
Slide "7":
  Do NOT hide the two small "&" layers between the three asks: they are Yash's content. They may build in with the asks on the same click.
  Click 1: "Use the playbook", "Keep therapy the hero", "Build the partner beyond the device" with their rules and sub-lines
  Click 2: "Patient-matched & Advancing with every case"
Slide "1": no builds.

PART 3 · Poll (if Yash confirms native poll)
On slide "2" insert a Figma Slides Poll with options exactly: "12 pepperoni", "One of everything", "Ask first, then order", "Pineapple for all". Square corners, colors #C8102E / #505759 only. Place it so it doesn't cover the A–D text.

DO NOT
- No new text, no edits to text, no changes to speaker notes.
- No gradients, tints of #C8102E, rounded corners, shadows.
- No extra ampersands; no generated imagery.

REPORT
Per slide: builds applied in order, anything skipped and why.
```

---

## Prompt C · Swap the Slides file to Vesta Std (sBqCMoTCaPupEZj9aRleUq)

```
Change the typeface in the Edwards TMTT XLT Figma Slides deck from Merriweather Sans to Vesta Std. Internal only.
Do not change any words, colors, positions, builds, transitions or speaker notes.

SET UP
- Mapping: Merriweather Sans Regular → Vesta Std Regular; Light → Vesta Std Regular; Bold / Black → Vesta Std Bold; Italic → Vesta Std Italic.
- Keep each text box's size, position and alignment (flush left). Keep current font sizes first.

PART 1 · Slide "6" (densest; review first)
- Swap every text layer. If any line now wraps differently or overflows its box, reduce that layer's size in 2 px steps (minimum 22 px for labels, 28 px for body) rather than moving it. Report each change.

PART 2 · Slides "1", "2", "3", "4", "5", "7"
- Same swap and overflow rule.
- Hierarchy by size OR weight, not both: titles Vesta Bold red #C8102E; body Regular dark gray #505759 or black.

DO NOT
- No other typefaces. No tracking or case changes. No new text.
- No gradients, tints of #C8102E, rounded corners, shadows. Logo stays bottom right on clean ground.

REPORT
Layers whose size changed (before/after px), any text that still overflows.
```

---

## Prompt D · Insert the live poll by hand (Slides file sBqCMoTCaPupEZj9aRleUq)

The Plugin API cannot create a Poll. Do this in Figma Slides:

```
Insert a live poll on the Edwards TMTT XLT deck, slide row "02 Pizza poll". Internal only.
Do not change any words on the slide or speaker notes.

1. Open the deck. In the grid, select slide 3:10 (row "02 Pizza poll", FIRST state; the one holding Yash's notes).
2. Toolbar: Insert (+) > Interactive > Poll.
3. Question: Pizza night: 12 guests, one order. What do you do?
4. Options, exactly, in this order:
   12 pepperoni
   One of everything
   Ask first, then order
   Pineapple for all
5. Place the poll in the right half, inside x 1200–1792, y 128–1016 (the area that is empty until click 1). Do not cover the A–D list (x 128–1088).
6. Style: square corners; colors #C8102E and #505759 only; no shadow.
7. Results: show live results to the presenter. Close voting on the next click.
8. Copy the poll element (Cmd+C) and paste in place (Cmd+Shift+V) on slides 13:10 and 13:34, so the morph between states holds it.
   If Figma will not share results across copies, keep the poll on 3:10 only and accept that it leaves the screen on click 1.
9. Present mode test: join from a phone on the venue network, vote once, confirm the results show, then reset the votes.

DO NOT
- Do not delete or move the A–D text, the dark panel or any other layer.
- No extra text, emoji or reaction elements.

REPORT
Poll placement (x, y, w, h), whether it carried across states, test result.
```
