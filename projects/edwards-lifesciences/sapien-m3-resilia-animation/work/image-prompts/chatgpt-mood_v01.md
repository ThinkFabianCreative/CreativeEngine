# ChatGPT image prompts · pitch MOOD frames v01

```
CLIENT / PROJECT:  Edwards Lifesciences · SAPIEN M3 RESILIA animation
SOURCES:           normalized-brief.md v03 §16.2 (A: "draws the anatomy in, instead of pushing against it"; B alternate)
                   work/copy/t03-same-landing-zone_v01.md (T03) · work/copy/p1-nature-30s_v02.md (nature)
                   work/image-prompts/t03-mood_v01.md + generated/generation-log.md (M1 works; M2 read "one among many")
AUTHOR / MODE:     design-champ, 2026-10-15 · EXPLORE/DEVELOP · MOOD, pitch only, never commercial
TOOL:              ChatGPT (GPT image model)
CLIENT AI RULE:    visual-direction.md: NEVER generate patients, physicians, clinical procedures, Edwards
                   products/devices or case imagery, even in comps. Every prompt below is abstract form or
                   nature still life. No valve, no coil that could read as the dock, no catheter, no organ tissue.
```

## How to use in ChatGPT

1. Open one new chat per territory (T03 in one, Nature in another). Paste the **LOOK** block first as its own message: "For every image in this chat, use this look:" + LOOK. Then paste prompts one at a time. Same chat keeps the set consistent.
2. Each prompt still repeats the LOOK block, so it also works pasted alone.
3. Always say "16:9 landscape". If it returns square, reply: "Same image, 16:9 landscape, extend the beige."
4. Iterate with short edits in the same chat ("keep everything, make the red smaller", "remove the shadow on the right") rather than re-prompting from scratch. Use the select/edit brush for local fixes.
5. If it adds text, a medical object or a heart-shaped organ: reply "Remove X, nothing else changes." If it persists, start that prompt in a fresh chat.
6. Download at full size, rename `P1-<ID>_MOOD_gpt_v01.png`, save to `work/generated/P1/`, and add a row to `generation-log.md`.

## Shared LOOK block (paste into every prompt)

> LOOK: product-grade still-life photograph on a warm beige seamless paper backdrop (approx. #E3D6C4), floor curving into wall with no visible horizon. One single saturated red accent (approx. #C8102E), and only one; everything else beige, cream, bone, warm grey. Soft north-window light from camera left, large diffused source, gentle long shadow falling right, no hard highlights. Shot on a Phase One medium-format camera, 120mm macro lens, f/8, tack-sharp subject, smooth falloff. Grade: matte, low contrast, warm neutral, fine film grain, Kodak Portra 160 feel. Style: Irving Penn still life, Karl Blossfeldt botanical precision, Hiroshi Sugimoto tonal restraint. Calm, precise, expensive, generous empty space. 16:9 landscape. No text, no letters, no numbers, no logos, no labels, no people, no hands, no medical devices, no hospital objects, no anatomical organs.

---

## T03 · One Landing Zone

### T1 · Every mitral is different (0–4 s)
**Must prove:** one irregular, asymmetric form can feel organic and precise at once; "different" is visible in one object.
**Prompt:**
> A single irregular, asymmetric organic form, like a translucent cream-coloured wax or soft resin shell, roughly ring-shaped but uneven: one side thicker, one edge folded, a slight saddle-like warp. Seen from a three-quarter overhead angle, centred-left, filling a third of the frame. No red in this frame except a faint red reflection on the floor beneath it. [LOOK]

**If it goes wrong:** if it looks like a valve or tissue, say "make it a sculpted resin object, like a Noguchi stone, no biological detail".

### T2 · Drawn in, every time (4–12 s) · contact-sheet frame
**Must prove:** variety in, identical result out; extends M1 by adding the *drawing-in* gesture.
**Prompt:**
> A row of six different irregular organic forms evenly spaced across the frame: a lumpy clay ring, a smooth pebble ring, a cracked chalky ring, a large flattened ring, a small tight ring, a ring with one edge drooping. Each one is bound by the same thin red cord that wraps it once and draws its rim inward, pulling every uneven shape into the same perfect circular opening of identical size, at identical height. The variety is obvious; the red circle is identical six times. [LOOK]

**If it goes wrong:** if the red cord reads as a spiral coil or spring (dock), say "one single closed red loop, flat, like a thread tied once, no spiral".

### T3 · The landing zone is the same (12–16 s) · fixes M2
**Must prove:** clearly many → one. Direction, not scatter.
**Prompt:**
> Seven irregular translucent cream rings of different shapes arranged in a precise diagonal sequence from the far left edge towards the centre, each one rounder, sharper and more aligned than the last, like frames of the same object converging. The final ring at the right-centre is a perfect, crisp, solid red circle, and the six translucent rings stack exactly onto it in perfect register, their outlines visible as faint ghost layers behind it. Strong sense of movement from left to right, from irregular to perfect. Right third of the frame empty beige. [LOOK]

**If it goes wrong:** if it scatters again, say "a single line of rings progressing left to right, each one more circular, ending in the red one; like a time-lapse of one object becoming a circle".

### T4 · Rhythm (16–21 s) · abstract membrane, not a valve
**Must prove:** the leaflet "open and close" rhythm can be shown without any valve or tissue.
**Prompt:**
> Three thin, translucent cream silk-like membranes stretched over a fine circular red hoop, photographed in five stages left to right across the frame like a chronophotograph: membranes flat and closed, slowly lifting, fully open like a soft bloom, settling, closed again. Light passes through the membranes, showing a fine fibre texture like paper or silk, not skin. Rhythmic, musical, calm. In the manner of Étienne-Jules Marey's motion studies, shot as a Penn still life. [LOOK]

**If it goes wrong:** if it looks like a heart valve, say "remove the hoop; make the membranes folded paper petals on the beige floor, five stages of opening".

### T5 · Outcomes backdrop (21–25 s) · type space
**Must prove:** the deck/film can hold a stat and logo over the territory's world; left 55% must be empty.
**Prompt:**
> Composition for typography: the left 55% of the frame is completely empty, clean beige seamless. On the right side, one perfect solid red circle rests on the floor, and around it, in a loose orbit, seven small irregular cream forms of different shapes (pebble, clay, seed pod, chalk), quiet and small. Low camera, horizon-less. Very minimal, a lot of air. [LOOK]

**If it goes wrong:** if forms crowd the left, say "move everything into the right third; nothing in the left half".

### T6 · Closing image (25–30 s) · heart moving forward
**Decision:** the brief's heart can be attempted **only** as a sculpture: an anatomical heart cast in solid red glass, smooth, no veins rendered as tissue, no wet surface, plainly an art object. It cannot read as a patient, device or procedure if it is glass on a seamless. If ChatGPT produces anything organic, wet or fleshy after two edits, **drop it and use T6-ALT** (the red circle from T3 rolling forward), which closes the T03 idea better anyway: the constant moves on.
**Prompt (T6):**
> A sculptural anatomical heart made entirely of solid, polished, translucent red glass, like a museum art-glass object by a studio glassblower, smooth and stylised, no veins, no tissue texture, nothing wet. It glides forward across the beige floor from left to right, with a soft horizontal motion blur trailing behind it and a sharp front edge; its glass shadow and red caustic light fall on the beige. Small in frame, lower-right third, lots of empty space ahead of it. [LOOK — the glass heart is the one red accent]

**Prompt (T6-ALT):**
> One perfect solid red glass disc standing on its edge, rolling forward across the beige floor from left to right, with a soft horizontal motion blur trailing behind and a sharp leading edge; red caustic light on the floor. Small in frame, lower-right third, lots of empty space ahead. [LOOK]

**If it goes wrong:** organic → "make it clearly blown glass, an art object, smooth like a Murano sculpture". Still fleshy → switch to T6-ALT.

---

## Nature · Drawn in, moving forward

Nature as product-grade still life: one specimen, centred, Blossfeldt-sharp, on the same beige. Red appears once per frame as a small accent (a red seed, a red stem tip), so the set matches T03.

### N1 · Fern coiling (4–10 s)
**Must prove:** "holds by drawing in" reads as a spiral gesture in one still.
**Prompt:**
> A single young fern fiddlehead, its frond tightly coiled inward into a perfect spiral, standing upright on the beige seamless, photographed as a precise botanical specimen in the manner of Karl Blossfeldt, extreme sharpness on the fine hairs and the curl. Pale green softened towards sage, the very tip of the coil a deep red. Centred-left, plenty of air. [LOOK]

**If it goes wrong:** if the green dominates, say "desaturate the fern to sage and bone; only the tip red".

### N2 · Anemone closing (10–16 s)
**Must prove:** gathering inward, tendrils to centre, without reading as wet or creepy.
**Prompt:**
> A single sea anemone sculpture-like specimen, out of water, its soft cream tendrils gathering inward and closing towards a red centre, captured mid-close. Treated like a Penn flower still life: dry-looking, matte, velvety, elegant, not slimy. Resting on the beige seamless, centred, top-down three-quarter view. [LOOK]

**If it goes wrong:** if slimy or alien, say "make it a dried cream sea anemone, like a museum specimen, matte".

### N3 · Wingbeat (16–22 s)
**Must prove:** rhythm of open/close as natural, graceful motion.
**Prompt:**
> A chronophotograph of a single pale cream moth's wings, isolated with no body visible, shown as five overlapping translucent stages of one wingbeat from closed to fully open and back, across the frame like an Étienne-Jules Marey motion study, printed as a fine still life. One small red mark at the centre where the wings meet. [LOOK]

**If it goes wrong:** if it becomes a butterfly specimen, say "fewer details, translucent ghosted stages, it should feel like motion".

### N4 · Seed pod closed (stretch :60 / backup for anemone)
**Must prove:** the same "hold by gathering" idea with a quieter, cleaner object.
**Prompt:**
> A single dried lotus or poppy seed pod, bracts closed tightly inward around its centre, one red seed visible at the opening. Blossfeldt-precise, sculptural, centred on the beige seamless, side-lit to show the ribs. [LOOK]

**If it goes wrong:** if it looks decorative/floristry, say "single specimen only, no petals, no arrangement".

### N5 · Tree rings · legacy (stretch :60)
**Must prove:** lineage, many years resolving to one centre; also echoes T03's rings.
**Prompt:**
> A thin cross-section of a pale wood log lying flat on the beige seamless, overhead view, fine concentric growth rings sharply detailed, slightly irregular outer rings becoming perfectly circular towards the centre, where a single small red dot marks the heartwood. Penn-style matte still life. [LOOK]

**If it goes wrong:** if the wood is orange/rustic, say "bleached pale ash wood, almost bone-coloured".

---

## Run first

1. **T3** (the M2 fix; the core proof of T03).
2. **T6** then **T6-ALT** if needed (settles whether the brief's heart close is usable at all).
3. **N1** (sets the nature look; if it matches M1, the two territories share one world).

## Labels and credits

- Every frame is labelled **MOOD · generated · pitch only · not a depiction of product, anatomy or procedure** on the slide.
- Never place a frame next to a stat or claim without that label; never let one read as evidence.
- Pitch credit line: *Generated mood frames (ChatGPT image). Style references: Irving Penn, Karl Blossfeldt, Hiroshi Sugimoto, Étienne-Jules Marey.*
- Log each kept frame in `work/generated/generation-log.md` (tool, prompt ID, review note).
