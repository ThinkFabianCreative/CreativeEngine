# Gorilla base v02: notes (2026-11-25)

File: `traffik-gorilla_base_v02.blend`. Object `Gorilla` (right half + Mirror modifier, clipping and merge on, 0.001 m). Hidden `Gorilla_tripo_half_ref` is the bisected original Tripo half, kept for retopo reference / shrinkwrap.

## What was done
- Imported the Tripo GLB. Orientation was already right after glTF import (X 1.00 wide, Y 0.27 deep, Z 0.73 tall; faces -Y). The W/D/H mismatch was Tripo's axis labelling, not a real swap.
- Applied transforms, centred on X=0 / Y=0, feet at Z=0 (body midline measured at X ≈ -0.003, within tolerance).
- Bisected at X=0, mirrored, Quadriflow at 4,000 target with symmetry → 3,175 faces evaluated (1,590 per half, 97% quads; the rest are tris/ngons from the re-bisect on the centre seam).
- Flat shading, `Matte_Grey` material (0.45 grey, roughness 1, specular 0).

## Compared with the turnarounds
Silhouette, proportions and T-pose match the front/back sheets; side view matches the hunched posture and belly of `side-tpose_v02`. It is far denser and smoother than the sheet's big-faceted look: the faceting style is not there yet.

## Manual cleanup needed
- **Arms**: Quadriflow under-sampled the forearms. Long stretched quads/tris from elbow to wrist (visible in the wire screenshot, back view). Rebuild with clean cylinder loops; elbow and wrist need 3 loops each.
- **Edge loops for rigging**: Quadriflow does not give guaranteed loops at shoulders, elbows, wrists, hips, knees. Flow is grid-like; joint rings must be added or retopologised by hand (or retopo on top of the ref with snapping).
- **Hands**: fingers are fused lumps; no separable digits. Model knuckle-walking fists/fingers simply (4 fingers + thumb as boxes) if the hands animate.
- **Face**: brow, muzzle, mouth and eyes are mush at this density. Needs a mouth loop and eye loops, and the brow ridge/sagittal crest planes from the sheet.
- **Feet**: toes merged; foot base not flat. Flatten the sole and block the big toe.
- **Centre seam**: a few tris/ngons on X=0 from the re-bisect; dissolve or quad-fill.
- **Look**: for the sheet's faceted low-poly look, the final retopo should land well under this count (est. 800–1,500 faces), or decimate (planar) a copy for display while keeping this quad cage for rigging.

# v03 (2026-11-25): hands and face
File: `traffik-gorilla_base_v03.blend` (v02 kept). 3,047 faces total (1,526 per half, 96% quads; remaining tris/ngons are on the X=0 seam and the wrist cut).
- **Hand**: old hand cut at X=0.405 and rebuilt from the 10-vert wrist ring: 3 wrist loops, palm, a knuckle bend with alternating ridge facets, fingers curled down and tucked under, grid-filled tip, 3-segment thumb on the front. All quads. Reads as a loose curled fist, close to the front turnaround.
- **Face**: sculpted on the existing quads by displacement: forward brow ridge, sloping forehead, deep eye sockets, broad nose pad, forward muzzle, mouth crease.
- **Still open**: fingers are one mitten block with ridges, not separate digits. The brow is a sharp visor (soften if it reads too cartoon). Nose is still soft (no nostril planes). The face is still Quadriflow-dense, not the sheet's big facets. The wrist ring has only 10 verts, so it's fine for bending but low for detailed deformation. No ear changes.
Screenshots: `v03-compare_hand_before-v02.png`, `v03-compare_hand_after-v03.png`, `v03-compare_face_before-v02.png`, `v03-compare_face_after-v03_solid.png`, `v03-compare_face_after-v03_wire.png`.

# v04 (2026-11-25): hand-built low-poly head
File: `traffik-gorilla_base_v04.blend` (v03 kept). 2,791 faces total.
- Old head deleted; new head hand-authored vertex by vertex on the mirrored half, mapped to `raw/gorilla-turnarounds/2026-11-25_face-reference_geometric-line.png`: crown cap split on the centre line, one wide brow band (pushed out), diamond eye sockets with a 2-ring inset (rim + recessed eye) for an eye loop, long nose bridge, chevron nose pad with nostril planes, two big cheek planes, forward muzzle block, lip slab with a loop around the mouth, narrow chin, simple angled ears.
- 66 faces per half (52 quads, 14 tris where the reference uses crisp triangles).
- **Open**: the head is a separate shell joined into the object, not welded to the neck. Its bottom ring is open and tucked into the body (the old neck has a hole hidden under it). Weld or bridge it before rigging, or skin the shell 100% to the head bone. From the back, the body's neck rises in a notched shape behind the head: tidy it. The eye is a 4-sided inset, not the reference's hexagon. The ears are small boxes, not the reference's C shape.
Screenshots: `v04_face_front_vs-reference.png`, `v04_face_3q.png`.

# v05 (2026-11-25): silverback pass
File: `traffik-gorilla_base_v05.blend` (v04 kept). 2,783 faces total; head is 62 faces per half.
- **Head re-landmarked for a gorilla** (the v04 reference was a chimp): a tall sagittal crest peaking toward the back, a thicker brow shelf jutting out with a flat underside, smaller close-set eyes deep under it, a wide flared nose pad, a shorter wider muzzle, a heavy square jaw. The head is sunk 12 mm down and 6 mm forward. Eye and mouth loops are kept.
- **Body**: a trapezius hump raised behind the neck (up to +35 mm) and slightly wider shoulders/upper chest. Arm and leg lengths are unchanged (left for the rig).
- **Materials**: `Gorilla_Fur_Charcoal` (body), `Gorilla_Skin_Dark` (face mask, hands, feet), `Gorilla_Saddle_Silver` (lower back to hips, stepped faceted border along the polygons), `Gorilla_Crest_Grey` (crown). Flat shading, roughness 1.
- **Open**: the ears are still square boxes in side view (shrink or delete; real silverback ears barely show). The crest-grey only covers 5 faces, so it barely reads. The saddle's top edge is jagged where it follows the Quadriflow grid (tidy into 2–3 deliberate steps). The hump doesn't read strongly in profile because the crest dominates. The head is still a separate shell, not welded to the neck.
Screenshots: `v05_body_saddle.png`, `v05_head_wire.png`, `v05_head_material.png`.

# v06 (2026-11-25): cleanup
File: `traffik-gorilla_base_v06.blend` (v05 kept).
- **Ears**: shrunk to a small low tab sitting nearly flush against the head, angled back; they barely show in profile.
- **Saddle**: reassigned in three deliberate steps (top edge at z 0.50 / 0.47 / 0.44 moving out from the spine; bottom at 0.235 / 0.29), giving a stepped diamond on the back.
- **Crown grey**: now covers the crest and the back of the skull (6 faces per half).
- **Hump**: raised another 20 mm and pushed 18 mm back behind the head base.
- **Still open**: the head isn't welded to the neck. The saddle's side edge is still a little ragged where the Quadriflow grid runs diagonally.
Screenshots: `v06_body_saddle.png`, `v06_head_side.png`.

# v07 (2026-11-25): gem-cut faceting from the faceted-head reference
File: `traffik-gorilla_base_v07.blend` (v06 kept). Reference (shape only, not colour): `raw/gorilla-turnarounds/2026-11-25_head-reference_gold-faceted.webp`.
- Bell silhouette: jaw/cheeks widened up to 22% toward the base; crown domed slightly forward.
- Faceting: the 14 largest planes poked into shallow pyramids (+3.5 mm) and the rest triangulated, giving 128 faces per half (112 tris). Eye rings and lip slab left as quads for animation.
- Materials unchanged (charcoal / skin / silver saddle / crown grey).
- **Open**: the nostril inset landed on the upper-lip plane; the nose has no real nostril holes yet (the reference's strongest feature). The eyes are still 4-sided, not hexagons. The brow has no centre V-notch. The head isn't welded to the neck.
Screenshots: `v07_head_front_vs-reference.png`, `v07_head_views.png`.

# v08 (2026-11-25): head traced from the faceted reference
File: `traffik-gorilla_base_v08.blend` (v07 kept). Whole model 3,185 faces.
- New head built from a 2D trace of the reference's front view (right half): outline, brow band and V-notch, eye socket + hexagonal eye, nose bridge, nostril polygon, nose flare, lip line, chin, cheek pads, crown planes. Triangulated with constrained Delaunay so facet edges follow those lines, then given depth from a front/back profile (superellipse across the width) plus feature offsets (brow forward, eye and nostril recessed, lip line in). The back of the skull is a coarser triangle grid. 278 faces per half (all tris), a closed shell, scaled 0.86 to sit on the body; old head and the neck strip around it removed.
- Bell/dome silhouette now matches the reference (widest at the jaw, rounded crown, no sagittal peak).
- **Open**: eyes and nostrils read weaker than the reference (recesses are 10–16 mm; need deeper holes and a raised hexagonal eyeball). Facets are more even than the reference's mix of big deliberate planes and small ones around the features (merge crown/cheek triangles into larger planes). Small notch at the crown top. Eye/mouth loops are triangles now, not quad loops (consider for rigging). The head is still not welded to the neck.
Screenshots: `v08_head_front_vs-reference.png`, `v08_head_views.png`, `v08_body.png`.

# v09 (2026-11-25): eyes, nostrils, bigger planes
File: `traffik-gorilla_base_v09.blend` (v08 kept).
- Eyes: hexagonal rim pushed back 10 mm, outer socket 4 mm, eyeball centre raised 3 mm, so each eye reads as a raised eye inside a dark socket.
- Nostrils: centre pushed back 16 mm, rim 5 mm.
- Bigger planes: crown, cheeks/jaw sides and back of the skull merged where faces are within 10° (dissolve-limit), leaving 13 large n-gon planes. Head is now 202 faces per half (mostly tris, some n-gons). The brow, eyes, nose and mouth keep the small facets.
- Crown-top notch levelled.
- **Open**: n-gons are near-planar but get triangulated on glTF export (invisible under flat shading). Two small tips remain at the crown top. Crown front triangles were too angled to merge; merging them would need hand edits. The head is still not welded to the neck.
Screenshot: `v09_head_vs-reference.png`.

# v10 (2026-11-25): head rebuilt from Andres's facet drawing
File: `traffik-gorilla_base_v10.blend` (v09 kept). Reference: `raw/gorilla-turnarounds/2026-11-25_head-facets_andres-drawing.webp` (screen-left half is the drawn version; it was mirrored onto the model's right half).
- The drawing was vectorized (skeleton, junctions, corner points) and its edges used as constraints for the front of the head, so the crown, eye sockets and eye shape, nostrils, lip and pout follow the drawn lines. Depth comes from the v09 surface (ray cast from the front; silhouette points at mid-depth). Back of the skull is a coarse triangle fill. Closed shell, no holes; materials carried over from v09 by nearest face.
- Head is 557 faces per half (all tris). Whole model 3,645 faces.
- **Open**: the drawing is front-only, so side planes are long thin triangles in profile. Face count is higher than v09. The head is still not welded to the neck.
Screenshots: `v10_head_views.png`, `v10_head_front_wire.png`.

# v11 (2026-11-25): big planes around the drawn features
File: `traffik-gorilla_base_v11.blend` (v10 kept).
- Collapsed 92 tiny trace edges (<3.5 mm) left by the auto-vectorizing.
- Outside the feature zone (eyes, brow, nose, mouth), merged faces within 13° into large planes: crown, cheeks, jaw sides and the back of the skull. The drawn feature facets stay dense. Head went from 557 to 275 faces per half. Closed shell.
- Smoothed the sawtooth fringe at the crown top.
- **Open**: the side profile still has long horizontal planes (the drawing was front-only). The head is still not welded to the neck.
Screenshot: `v11_head_views.png`.

# v12 (2026-11-25): head welded, side planes merged
File: `traffik-gorilla_base_v12.blend` (v11 kept). New mesh datablock `Gorilla_v12`; Mirror modifier unchanged.
- Head welded to the body: the body's open neck was closed, then joined to the head shell with an exact boolean union, then cut back to the right half at X=0. The whole model is now one closed, manifold mesh (0 open edges, 0 non-manifold edges after mirror).
- Side profile: faces within 20° merged on the head sides (outside the eye/nose/mouth zone), replacing the long horizontal bands with larger planes.
- Whole model 3,066 faces.
- **Open**: the boolean seam around the neck is triangles and n-gons, not clean quad loops (fine for display; tidy before final weight painting). A few merged side planes have notched edges.
Screenshots: `v12_head_wire.png`, `v12_body.png`.

# v13 (2026-11-25): neck seam and side notches cleaned
File: `traffik-gorilla_base_v13.blend` (v12 kept).
- Neck seam: collapsed short boolean edges (<5 mm), dissolved stray 2-edge verts, and joined triangles into quads. The neck band is now 81 quads, 32 tris and 2 small n-gons (it was all tris and n-gons).
- Side notches: the notched n-gons on the head sides were re-triangulated, 5 sliver triangles were collapsed, and the planes were re-merged at 8°. The slit on the side of the head is gone.
- Whole model 3,074 faces, closed and manifold.
- **Open**: the neck still has some triangles. That's fine for display and skinning; full quad loops would need hand retopo of that ring.
Screenshot: `v13_head_wire.png`.

# v14 (2026-11-26): rebuilt on the downloaded high-poly sculpt
File: `traffik-gorilla_base_v14.blend` (v13 kept). Source: `~/Downloads/Gorilla_Highpoly_Basemesh.zip` (Sketchfab GLB, 2.2M tris, no rig/UVs; licence not checked yet).
- Sculpt imported as hidden `Gorilla_sculpt_ref` (scaled to 0.72 m, centred, symmetrised at X=0, decimated to 170k for reference).
- Proportions pushed toward a gorilla: legs shortened 18% below the crotch, belly pushed forward, torso widened slightly.
- Body: voxel remesh then symmetric decimate (Quadriflow refused this mesh even though it tested manifold), triangles paired into quads where flat: about 55% tris.
- Head: the v11 drawn-facet head, scaled 0.8, replacing the sculpt's roaring head; mouth closed. Welded by exact boolean union, cut to the right half for the Mirror modifier.
- Materials: charcoal body, dark skin on face/hands/feet, silver saddle on the lower back, grey crest.
- Whole model 3,738 faces, closed and manifold.
- **Open**: body topology is decimated (no planned joint loops for Rigify); arms are in the sculpt's A-pose, not T-pose; the head is smaller and a little forward, check against the turnarounds.
Screenshot: `v14_body.png`.

# v15 (2026-11-26): joint loops for Rigify
File: `traffik-gorilla_base_v15.blend` (v14 kept).
- Three edge rings (about 12 mm apart) cut at each joint, perpendicular to the limb: shoulder, elbow and wrist along the A-pose arm axis; hip, knee and ankle horizontal on the leg. Each ring is complete (22–31 cut edges).
- Joint centres used: shoulder (0.19, 0.13, 0.50), elbow (0.29, 0.14, 0.43), wrist (0.395, 0.15, 0.35), hip z 0.21, knee z 0.12, ankle z 0.055 (leg at x 0.05, y about 0.15). Use these when placing the Rigify metarig.
- Whole model 4,664 faces (was 3,738). Closed and manifold.
- **Open**: the rings are cut into a decimated mesh, so they're clean loops but the faces between them are still mixed tris/quads. No loops yet in the spine, neck, fingers or jaw.

# v16 (2026-11-26): broader back
File: `traffik-gorilla_base_v16.blend` (v15 kept).
- Upper back and shoulders widened (up to about +25% around z 0.43, more on the back side), then the waist and hips (about +20% around z 0.31), so the back reads as a barrel, not a V. The arms and legs move outward with the torso; the head is untouched. Joint loops are kept; shoulder/elbow/wrist centres are now about 3–4 cm further out in X than the v15 numbers.
- Whole model 4,664 faces, overall width 1.00 m.
Screenshot: `v16_back.png`.

# v17 (2026-11-26): bigger head
File: `traffik-gorilla_base_v17.blend` (v16 kept).
- Head scaled 1.22 about the base of the skull (0, -0.01, 0.525), blended into the neck over about 4 cm so the seam stays smooth. Top of head now z 0.727.
- Removed three loose edges at the back of the skull on the centre line (the dark tick seen in v14–v16), and smoothed 12 boolean-seam spikes at the back of the head.
- Whole model 4,664 faces, closed and manifold.
Screenshot: `v17_body.png`.

# v18 (2026-11-26): protruding muzzle
File: `traffik-gorilla_base_v18.blend` (v17 kept).
- Front-facing face verts pushed forward with soft falloffs: snout up to about 30 mm (centred z 0.585), nose pad about 19 mm (z 0.607), lips about 22 mm (z 0.553), cheeks 9 mm forward and 5 mm out. A 6 mm mouth-line crease (z 0.568) separates upper lip and pout. Nostril recesses deepened by 6 mm relative to the pad.
- No topology change; 4,664 faces, closed and manifold.
Screenshot: `v18_face.png` (plain grey).

# v19 (2026-11-26): gorilla face proportions
File: `traffik-gorilla_base_v19.blend` (v18 kept).
- Snout pulled back 10 mm (about a third of the v18 push): mass kept, less chimp reach.
- Nose pad widened up to 1.6x around z 0.608 with the nostrils carried outward; nose bridge raised 4 mm between the eyes.
- Brow made an overhanging shelf: about 9 mm forward and 3 mm down around z 0.657, shading the eyes.
- Mouth line widened up to 22% and the jaw corners pushed 6 mm outward.
- Points moved only; 4,664 faces, closed and manifold.
Screenshot: `v19_face.png` (plain grey).

# Face file (2026-11-26): `traffik-gorilla_face_v02.blend`
(`traffik-gorilla_face_v01.blend` is an earlier attempt with a non-manifold reference; ignore it.)
- `Gorilla_face_HP_ref`: the sculpt's head (growl), voxel-remeshed at 1.5 mm, made symmetric, cut out with an exact boolean so it is closed (43.6k faces).
- `Gorilla_face_LP`: symmetric decimate of that head to 2,474 triangles, mirrored exactly at X=0, all triangles. Keeps brow shelf, deep-set eyes, wide nostrils, lips, teeth and growl. Note: this saved version still has pinched vertices at the teeth; the cleaned copy lives only inside v20.
- A vertex-group-weighted decimate was tried first and rejected (it concentrated faces at a few spots and left long slivers).
Screenshot: `face_v02_lowpoly.png`.

# v20 (2026-11-26): sculpt face on the body
File: `traffik-gorilla_base_v20.blend` (v19 kept).
- The face-file head (scaled 1.45 wide / 1.28 deep and tall; chin at z 0.555, face front at y -0.16) replaces the drawn-facet head. Neck trimmed with a tilted plane so the throat runs down into the chest.
- Cleaned before welding: pinched vertices at the teeth removed and refilled, then cut and mirrored so the head is exactly symmetric (2,394 tris, closed).
- Body: old head removed (ellipsoid cut kept below z 0.553 at the back, cleared under the jaw), opening closed, then joined with an exact boolean union, cut to the right half for the Mirror modifier.
- Whole model 6,518 faces, closed and manifold. The head is all triangles.
- **Open**: the head is 2.4k of the 6.5k faces (heavier than planned). The growl is fixed in the mesh, so the jaw won't open and close in the rig. A small ledge remains under the jaw at the front. Face materials were assigned by position (skin on the face mask, grey on the crown) and need a visual check.
Screenshots: `v20_head.png`, `v20_body.png`.
