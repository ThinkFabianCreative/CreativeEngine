# P1 Footing — Codex review exports, 2026-10-15

Edwards Lifesciences · SAPIEN M3 RESILIA animation · design-champ brief · DEVELOP · internal/pitch only.
Sources: territories-round3_v02.md; territory-review_v04-round3.md; footing-coldread_v01.md; normalized-brief.md v04 §7.3/Q2/Q18; client visual-direction.md; supplied FBX/JPG; R4 scanned brochure p5.

## User revisions in this chat
- Replace the stylized paperweight with a translucent anatomical heart. This supersedes the original no-anatomy MOOD direction for these concept images. Detailed anatomy is not clinically validated.
- Use DOCK_M3_Small.fbx's supplied flared-guard configuration for review drafts, despite differences from the supplied JPG/R4 configuration.
- No product was generated, repainted, inpainted, or modified by an image model. MOOD and RENDER are separate exported frames.

## Delivered
Three MOOD PNGs: S01 uneven ground, S02 footing smoothing, S04 anatomical heart settled.
Eleven native-render PNGs: S03 dock 0/20/40 degree views; S05 assembly 12/30 degree elevations; S06 transparent assembly and separate transparent shadow; supplemental valve-only 12/30 degree views; valve and assembly detail views.
All exported PNGs are 3840 × 2160 with the brief's exact 14 px warm-grey bottom-left label. MOOD source images are 1672 × 941, resized with Lanczos; they are not native 4K. RENDER images are native 3840 × 2160.
S06 contains no copy, lockup, logo or invented footnote. Composite its product and shadow passes over beige; avoid showing the repeated pass label twice in a layout.

## Render method
Three.js 0.180.0 local WebGL renderer, isolated headless Chrome; FBXLoader reads supplied geometry directly. Mesh transforms retained; no vertex deformation or shape reconstruction. Rendering-only material proxies are used because no texture assets were supplied. Fabric/tissue proxies are matte off-white; metal proxies neutral satin; tissue is a placeholder, no RESILIA appearance claim. Some material fidelity and geometry detail remain below final production quality.
90 mm equivalent full-frame 16:9 perspective camera (12.8372 degree vertical field of view), 12 degree elevation; S05 alternate/detail 30 degrees; S06 8 degrees. Main subject x58%/floor contact y60%; S06 x70% and 9% width. Main width approx12%. AI camera metadata is unavailable; pairs are visual framing approximations, not an exact solved camera match.
Adaptive near/far camera planes prevent fine-surface depth artifacts. Soft warm-left key proxy, right fill at20% of key intensity, low ambient; softened VSM shadow (radius32,32 blur samples), matte beige floor. Exact scene and source bounds are in render-settings.json and assembly-render-settings.json. Procedural renderer lighting differs somewhat from the generated mood frames; final art direction matching remains review work.

## Scale and alignment audit — review assembly only
R4 p5 specifies valve width29mm and height22.5mm; dock height23mm. VALVE.fbx stores cm units; DOCK_M3_Small.fbx stores mm units. Numeric coordinates alone must not be combined.
Precise world-space mesh measurements, including authored transforms:
- Valve metal frame before calibration:28.7500mm wide ×22.4500mm high. Full fabric outer diameter30.1503mm and height22.8319mm.
- Applied uniform valve scale1.00869562 after cm-to-mm conversion (total render import factor10.086956208). Frame becomes29.0000mm; outer fabric diameter approximately30.4124mm; full height approximately23.0304mm. No nonuniform scaling.
- Dock supplied dimensions45.9603×13.5867×46.5721mm. Its flared-guard configuration differs from the reference JPG; user authorized using this configuration as a review draft.
- Sampled lower helix world vertices in y88–90mm: fitted axis x≈-0.0019mm,z≈3.0152mm, minimum radial distance10.25345mm. Estimated coil inner diameter20.5069mm BEFORE adjustment. This is a mesh-based clearance estimate, not an engineering specification or validated bore measurement.
- That coil cannot clear the30.4124mm fabric envelope at supplied scale. Applied uniform dock scale1.5116855 (51.17% increase) to give approximately31.0mm minimum sampled coil inner diameter. Overall dock width≈69.48mm, height≈20.54mm, depth≈70.40mm. This large adjustment is provisional and NOT a verified real device assembly scale.
- Aligned valve axis to sampled lower coil centre. Valve translation relative to recentered dock bbox:[-0.2767,0,+4.2033]mm. Both lower bounds placed on floor. No hidden vertex edits, bending, reshaping, material removal, or independent mesh nudges.
- Inflow/outflow and axial seating remain unverified; JPG alone cannot solve the different dock configuration. Combined S05/S06 are review composites of supplied geometry, not approved implantation/fit evidence.

## Open review gates
Q2: supplied FBX is assumed first-generation; RESILIA leaflet appearance unverified. Q18: approved Edwards product/procedure reference needed before client use. No claim that generated anatomy is medically accurate. Current render scale/fit must be reviewed and replaced with an approved assembly pose before production. Final S06 artwork, ENCIRCLE logo, lockup and footnotes still supplied/placed by design-champ.
One AI attempt incorrectly introduced a cutaway/device after a brochure image was in recent context. It was rejected and excluded from this set. Corrected MOOD frames use explicit isolated-heart image paths.

## Prompt set
Built-in image generation only; no Artlist trial credits used. The attached original-shot-brief.txt contains the base LOOK/shot directions. The final MOOD prompts explicitly override the heart form as above:
S04: replace stylized heart with intact translucent ruby anatomical heart sculpture, plausible ventricles/atria, aortic arch with three branches, pulmonary trunk and vena-cava stubs; satin resin; no product inside; same beige set/90mm low side-on12deg/left key; small atx58%,basey60%; smooth floor. Image reference: original stylized S04; final source exec-6ca65c35-57b5-4761-ab4e-937f3968cf63.png.
S01: edit ONLY isolated anatomical S04 source; preserve exact intact exterior heart, size/material/orientation; move tox33%,basey60%; add one shallow irregular floor buckle atx58%,width12%; no cutaway/device,ring/disc/rim/hole. Final source exec-65078a55-0925-4626-b878-c56574d1a801.png.
S02: edit ONLY corrected anatomical S01; replace floor buckle with faint soft straight inward creases,almost flush,no outline; lock heart/camera/light; no cutaway/device/ring/disc. Final source exec-a0eeeafb-988d-4702-9401-9d1447e30988.png.
Image-model consistency is approximate; S04 and S01/S02 retain subtle material/detail differences. Review pair continuity before editing into film.
