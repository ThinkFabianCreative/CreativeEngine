# Copilot in PowerPoint: animation prompt

File: `outputs/TMTT Portfolio Orchestration — XLT (TRAFFIK v1).pptx`

> **Status 2026-10-08:** the choreography below is already written into the file: wipes, zooms, cascades and video autoplay. Use these prompts only to tweak it, or to rebuild it after manual edits.

Every animated shape is named in the Selection Pane (Home › Arrange › Selection Pane) as **`S<slide> Click<n> <group> - <text>`**. For example, `S2 Click1 cbar` is slide 2, revealed on the first click. Shapes named `static` never animate.

The file already contains a working click sequence (Fade + small rise, 0.5 s). Use the prompts below to enrich the motion, and paste them **one slide at a time**. Copilot works best on short, specific asks, and its animation support changes often. If it says it can't apply an effect, use the manual steps at the end.

---

## Master prompt (paste first)

> You are refining animations only. **Do not change, rewrite, move, resize, recolour or restyle any text, shape, image or slide layout. Do not apply Designer suggestions, themes or new slides. Do not touch speaker notes.** Work only in the Animation Pane.
>
> Every animated object is named in the Selection Pane as "S[slide] Click[n] [group]". Objects with the same slide and click number must appear on the same click: the first object "On Click", the rest "With Previous", each delayed 0.05 s more than the last. Objects named "static" stay visible and unanimated.
>
> House style for every entrance: **Fade with a short upward float (Float In, distance small), duration 0.5 s, smooth end.** Slide transitions are **Fade, 0.7 s**. Keep the order of the clicks exactly as numbered. Confirm what you changed after each slide.

---

## Slide-by-slide prompts

**Slide 1, Cover**
> On slide 1, animate all objects named "S1 Click1 tag" on click 1: Fade + Float In, 0.6 s. Everything else is static.

**Slide 2, Pizza night (live poll)**
> On slide 2, the question and options A–D are static while the room votes.
> Click 1: "S2 Click1 cbar" uses **Wipe from left, 0.4 s**. Then "S2 Click1 cA2", "S2 Click1 cB2" and "S2 Click1 cC2" Fade With Previous, 0.1 s delay. Then "S2 Click1 panel" **Wipe from right, 0.5 s** With Previous. Then "S2 Click1 rev1" Fade + Float In After Previous.
> Click 2: "S2 Click2 rev2" Fade + Float In, 0.5 s.

**Slide 3, The promise**
> On slide 3, the headline and the image are static.
> Click 1: "S3 Click1 prom" Fade + Float In.
> Click 2: "S3 Click2 rule" **Wipe from left, 0.5 s**. Then the group "S3 Click2 p1" With Previous (0.2 s delay), "p2" (0.35 s) and "p3" (0.5 s), each Fade + Float In, so the three pillars cascade left to right.

**Slide 4, TCT '26 film**
> On slide 4, keep the video set to **play automatically** (Start: Automatically, not on click). After the video starts, "S4 Click1 cap" fades in on click 1, or set it to After Previous with a 1.5 s delay if you prefer no click.

**Slide 5, What we learned**
> On slide 5, the title is static.
> Click 1: all "S5 Click1 ex" objects: the column header first, then 01 and 02, Fade + Float In, cascading 0.08 s.
> Click 2: all "S5 Click2 in" objects, the same treatment for 03 and 04.

**Slide 6, One story, orchestrated**
> On slide 6, the title is static.
> Click 1: "S6 Click1 today": the line Wipe from left 0.6 s, then the labels, ticks and grey dots Fade With Previous.
> Click 2: "S6 Click2 story": the One Story list and Journey Orchestration Fade + Float In, cascading top to bottom.
> Click 3: "S6 Click3 y27": the red 2027 line **Wipe from left, 0.8 s**, then the channel dots and labels **Zoom (small) one after another, 0.08 s apart**, left to right, to show the sequence building.
> Click 4: "S6 Click4 team": Fade + Float In.
> Click 5: "S6 Click5 proof": "2.7x" **Zoom, 0.4 s**, then its caption Fade With Previous.

**Slide 7, Ask first**
> On slide 7, the headline, sub-line, red square and "&" are static.
> Click 1: "S7 Click1 asks": the three asks and the two "&" between them cascade left to right, Fade + Float In, 0.1 s apart.
> Click 2: "S7 Click2 sign": Fade, 0.6 s.

---

## Final check prompt
> List every animation on every slide in order, with object name, effect, start (On Click / With / After Previous), delay and duration. Confirm no text, layout or speaker notes were changed.

## If Copilot can't apply effects (manual steps, about 10 minutes)
1. Open the Selection Pane and the Animation Pane (Animations › Animation Pane).
2. In the Selection Pane, select the objects named for one click, for example everything "S6 Click3".
3. Apply the effect from the Animations tab and set Start, Duration and Delay as above.
4. Use the Animation Pane's arrows to keep the click order matching the numbers.
5. Play with Shift+Cmd+Return from the current slide to check.
