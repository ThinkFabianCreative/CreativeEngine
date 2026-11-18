# Codex shot briefs · R3-2 Footing v01

```
CLIENT / PROJECT:  Edwards Lifesciences · SAPIEN M3 RESILIA animation
SOURCES:           work/copy/territories-round3_v02.md (R3-2 Footing, BET THE PITCH conditional; absorbs T03
                   "every mitral is different, the landing zone is the same") · work/reviews/territory-review_v04-round3.md
                   · work/image-prompts/footing-coldread_v01.md (heart form + LOOK) · normalized-brief.md v04 §7.3, Q2, Q18
                   · client/knowledge/visual-direction.md
AUTHOR / MODE:     design-champ, 2026-10-15 · DEVELOP · pitch/internal stills, never commercial
TOOL:              Codex session: image generation + rendering from supplied geometry (render pipeline not yet set up)
```

## Read first (paste this header to Codex with the briefs)

- **Two kinds of image, never mixed in one frame.** MOOD frames are AI-generated and contain no Edwards product, patient, physician, procedure, anatomy or case imagery: no valve, dock, coil, ring, catheter, organ, ECG line. RENDER frames show product only from the supplied geometry (VALVE.fbx, DOCK_M3_Small.fbx, 10062247_valve_assy.zip glTF, "M3 FBX - Copy.jpg" as alignment reference). Never generate, repaint, inpaint or "improve" product geometry with an image model.
- **Labels, burned into the bottom-left corner of every exported file, 14 px, warm grey #8A7F72:**
  MOOD: `EXPLORE · MOOD — AI-generated pitch inspiration` · RENDER: `RENDER · REVIEW DRAFT — supplied first-gen SAPIEN M3 geometry; not approved for client use`.
- **Renders need review before any client use**, against approved Edwards reference (Q18 OPEN). The FBX is assumed to be **first-generation SAPIEN M3**; RESILIA leaflet appearance is unverified (Q2). Valve-dock scale and alignment are unverified: check against "M3 FBX - Copy.jpg" and the R4 dimensions (29 mm valve) before rendering any valve-in-dock frame, and report what you had to adjust.
- **Files:** `work/generated/P1/P1-FOOT-S0n_<MOOD|RENDER>_codex_v01.png`, 3840 × 2160 (16:9), plus a line each in `generation-log.md` (prompt or render settings, source files used, date).

## Shared world (all six frames)

- **Set:** warm beige seamless, floor curving into wall, no horizon (#E3D6C4; floor slightly darker tan #D6C6B0). One red only (#C8102E), and only on the heart in MOOD frames. RENDER frames carry **no red**: product in its own materials on the same beige.
- **Camera (locked for every frame, so pairs cut):** 90 mm equivalent, camera height low, **12° above the floor plane**, side-on, subject axis at frame centre-right (x ≈ 58%, y ≈ 60%). Small subject: heart or footing patch ≈ 12% of frame width; dock/valve in renders occupy the **same footprint** as the footing patch they replace.
- **Light (locked):** one large soft key from camera left, 45° azimuth, 35° elevation (north-window quality, 5200 K slightly warm), low fill from right at 20%, soft long shadow falling right. Grade matte, low contrast, fine grain.
- **Heart (MOOD only, per cold-read decision):** small, solid, heavy cast object in matte red stone-like resin, familiar heart silhouette, thick, slightly asymmetric, softened edges. Sits low like a paperweight. Never: face, eyes, limbs, gloss highlight, bounce, tilt, squash.
- **Footing:** a flat level plane, flush with the floor. Never a rim, disc, ring, groove, concentric mark or spiral. One footing ahead at most; never a row.
- **The match-cut principle:** mood and render rhyme on **camera, scale, light and inward motion**, not on shape. The footing never borrows the coil's circular form (§16.2.5 ring read); the dock simply occupies the place where the footing was forming.

---

### S01 · Uneven ground · MOOD
1. **Idea / role:** "Every mitral anatomy is different." The heart is ready to move; the ground ahead is not. Opens :30 sc1 / :60 sc1.
2. **Type:** AI mood.
3. **Frame:** heart still at left third; one shallow buckled patch of floor at centre-right (the footing position), same material as the floor; empty space right. Locked camera and light.
4. **Prompt:**
   > Product-grade still-life photograph, 16:9. Warm beige seamless paper backdrop (#E3D6C4), floor curving into wall, no horizon. A small, solid, heavy red heart-shaped object (#C8102E) cast in matte stone-like resin, thick, slightly asymmetric, softened edges, no gloss, sits low on the floor in the left third, about one eighth of frame width. At centre-right, one patch of the floor is uneven: a shallow irregular dip with a slight ridge on one side, the beige surface pressed and buckled, same material and colour. The rest of the floor is smooth. Camera 90 mm, 12 degrees above the floor, side-on. One large soft key light from camera left, long soft shadow to the right, low fill. Matte, low-contrast, warm neutral grade, fine grain. Irving Penn still-life restraint. Only one red object. No text, logos, people, hands, medical devices, organs, ECG lines, rings, coils, spirals, discs.
5. **Open:** none (mood only). Cold-read risk: cute (see footing-coldread_v01.md fixes).

### S02 · The ground draws in · MOOD · match-cut A (pairs with S03)
1. **Idea / role:** the footing forms by drawing in from its own edges: the mechanism as a feeling. Last frame before the cut to the dock (:30 sc4, :60 sc5).
2. **Type:** AI mood.
3. **Frame:** identical to S01. The patch mid-way to level: soft straight creases converging inward, mostly flat, no outline. Heart has not moved.
4. **Prompt:**
   > Same scene, same camera, same light as the previous image. The uneven patch at centre-right is in the act of levelling: its edges draw inward from all sides, soft straight creases in the beige surface converging toward the centre like a tablecloth being smoothed, the dip filling, already mostly flat and flush with the floor. No raised edge, no rim, no circular outline, no concentric marks, no spiral. The red heart object has not moved. [repeat set, light, grade and exclusions from S01]
5. **Open:** none. If it reads as a ring or coil, re-run with "you should barely see where the patch begins".

### S03 · The dock captures · RENDER · match-cut B (pairs with S02)
1. **Idea / role:** the real thing behind S02: the dock draws the apparatus inward and makes the landing zone. "The dock draws the anatomy in."
2. **Type:** model render, DOCK_M3_Small.fbx only.
3. **Frame:** dock alone on the beige set, standing on its axis as implanted orientation in the reference, centred on the S02 footing position, outer diameter matched to the patch width (≈ 12% frame). Encircling turn and functional turns read in profile; nitinol PVL guard and radiopaque markers visible, not hero'd.
4. **Render brief:**
   - Camera: 90 mm, 12° elevation, side-on, same position/target as S02 (export a camera match from the S02 frame or use x 58% / y 60% target).
   - Lighting: soft area key camera-left 45°/35°, 5200 K; 20% fill right; ground-contact shadow on beige seamless (#E3D6C4, matte, catches shadow).
   - Materials: fabric covering = woven PET-like, off-white, visible weave at close range, matte (roughness ~0.8); nitinol = satin metal, low specular, not chrome; radiopaque markers = slightly darker dense metal dots. No coloured tints, no red.
   - Output: 3840 × 2160, also a 3-frame turntable (0°, 20°, 40°) to pick the clearest read of the encircling turn. Label: RENDER.
5. **Open:** no anatomy may be shown or generated, so "capturing the leaflets" is implied by the cut only; a capture animation needs an approved Edwards procedure asset (Q18). Dock orientation relative to the valve (inflow/outflow) unverified against approved reference. Mesh is first-gen M3.

### S04 · Settled, moving forward · MOOD · match-cut A (pairs with S05)
1. **Idea / role:** the heart has glided onto the level footing and settled with weight; trail behind flush, nothing pre-formed ahead. "A standardized landing zone."
2. **Type:** AI mood.
3. **Frame:** same camera and light. Heart now **at the S02 footing position** (centre-right), low and settled with contact shadow; smooth floor behind; empty floor ahead.
4. **Prompt:**
   > Same scene, same camera, same light. The red heart object now rests on the levelled spot at centre-right, sitting low and settled with a soft contact shadow, as if it slid there with an even, weighted glide. Behind it on the left the floor is smooth and level, only the faintest trace where the ground had been uneven. Ahead, on the far right, the floor is smooth and empty. Slight horizontal motion softness only at the heart's trailing edge. No footprints, no stepping stones, no row of discs, no path. [repeat set, light, grade and exclusions from S01]
5. **Open:** none.

### S05 · The valve lands in the dock · RENDER · match-cut B (pairs with S04)
1. **Idea / role:** what S04 stands for: the valve seated in the landing zone. "The beat lands with the valve."
2. **Type:** model render, VALVE.fbx + DOCK_M3_Small.fbx (glTF valve as fallback for a quick look only).
3. **Frame:** valve-in-dock at the same position and footprint as the heart in S04. Side-on: cobalt-chromium frame and PET skirt read; leaflets only glimpsed through the frame cells, not hero'd.
4. **Render brief:**
   - Camera/light/set: identical to S03.
   - Assembly: align valve inside dock using "M3 FBX - Copy.jpg" as the target pose; R4 states a 29 mm valve; scale both from file units and report the resulting valve diameter and dock inner diameter. Do not nudge geometry to "look right" without logging it.
   - Materials: frame = cobalt-chromium, satin brushed metal, cool-neutral, soft specular, no mirror finish; skirt = PET fabric, off-white, fine weave, matte; leaflet tissue = pale warm off-white, soft subsurface, matte, no sheen (placeholder, see Open); dock as S03.
   - Output: 3840 × 2160, plus one alternate from 30° elevation for internal use. Label: RENDER.
5. **Open:** **RESILIA leaflet appearance unverified** (FBX assumed first-gen ThermaFix tissue, Q2); this frame must not be read as M3 RESILIA. Valve-dock scale/alignment unverified. Approved reference needed before client use (Q18).

### S06 · Hero / end card · RENDER + layout
1. **Idea / role:** "Same footing. Every step forward." The last footing, flush, carrying the product. End card for :30 sc6 / :60 sc10 and the deck title slide.
2. **Type:** model render (S05 setup) composited by design-champ onto the beige layout. No AI in this frame.
3. **Frame:** wider: camera pulled back to 90 mm at 8° elevation, valve-in-dock at x 70%, ≈ 9% of frame width, long soft shadow right; left 55% clear beige for the line; bottom band reserved for SAPIEN M3 RESILIA lockup, ENCIRCLE logo and footnote zone (approved artwork only, placed later).
4. **Render brief:** as S05, camera changed as above; render with transparent background + shadow pass (separate PNGs) so the beige and type are set in layout. 3840 × 2160. Label: RENDER.
5. **Open:** approved lockup and ENCIRCLE logo files; footnote text (claims ledger, beyond territory stage); same RESILIA and alignment flags as S05. Glass-heart variant would replace this frame with an approved glass-heart asset (Q37), not a render.

---

**Pairs:** S02 → S03 (footing forming → dock), S04 → S05 (heart settled → valve seated). If a pair does not cut cleanly at matched camera, fix the render camera, never the mood frame's heart or footing form.
