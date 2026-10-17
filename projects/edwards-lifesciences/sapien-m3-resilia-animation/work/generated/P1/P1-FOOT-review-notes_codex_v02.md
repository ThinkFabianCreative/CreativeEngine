# P1 Footing — material and supplied-model revision v02

2026-10-15 · Edwards Lifesciences · SAPIEN M3 RESILIA animation · DEVELOP · review/pitch only.

## What changed
The user supplied two hero reference PNGs in SAPIEN M3 Resilia.zip and a newer model/texture package M3.ValveP.Simp_02.01_(.zip during the material-correction task. This v02 uses that newly supplied FBX for all eleven product renders. It contains the valve and dock together; their authored relative positions are preserved. The earlier v01 files and ZIP remain unchanged. Three existing anatomical-heart MOOD v01 images are retained in the revised package; no new AI imagery was made in this revision.

Source geometry: M3.ValveP.Simp_02.01_(f3218Export).fbx, FBX7400,18 meshes,631167 control-point vertices,747286 source polygons. Empty take/layer metadata exists but no playable animation tracks were imported. Supplied textures accompany the FBX.
Appearance reference: SM3R Valve Hero August_7th_0144 for public use.png and SM3R Valve-in-Dock Hero August_7th_0191 for public use.png. These filenames do not themselves close Q18 or establish geometry approval.

## Material correction
- All three SAP323_ARv2Leaflet_Expand meshes have distinct warm-tan tissue materials. Source LeaftLet_forStuidoLightingSide uses #B39B79; top/toon material slots use subdued golden-beige #C6A667. Physical-material sheen is restrained; full native V-Ray subsurface shading is not reproduced by this WebGL renderer.
- White/off-white fabric and lining remain distinct from tissue. Source cloth and skirt maps are bound as bump/normal textures using supplied UVs. The actual supplied SkirtCloth02 colour map is blue-grey, so it is not used as a white-fabric diffuse map; supplied normal/depth maps provide surface relief with a white base colour instead.
- Sapien3_Stent has a separate neutral satin-metal material (#878E92,roughness.43,metalness.60). Existing struts are retained; no new struts were drawn or added across the opening.
- White stitches, source green stitching, neutral covered dock and denser metal marker materials are separate. No red is introduced into product frames.
- TGA/PSD maps were converted locally to PNG. Two16-bit PSDs required macOS format conversion; other maps used standard image decoding. No AI image editing, repainting, geometry generation, vertex displacement or leaflet deformation.

## Geometry/reference differences — unresolved
The newly supplied package includes overlapping detailed and simplified cloth/tissue shells, plus a FurBase surface. All these source surfaces remain in combined renders. Their coverage differs from the supplied hero PNG: more of the inner metal frame and leaflet surfaces are obscured, and the three leaflets do not present the same open central shape at the retained camera angles. The exposed lattice appearance of the hero reference is therefore NOT fully reproduced. Material assignments alone cannot fix that coverage/pose difference.
No fabric was removed, made artificially transparent, repositioned, or cut away to force a reference match. No struts were invented. A validated source visibility/material-opacity setup or an approved model matching the hero would be needed to resolve this. Native V-Ray multilayer/two-sided/fur shader fidelity is also not available in this renderer.

## Scale and alignment audit
FBX UnitScaleFactor2.54cm means source coordinates are inches. Stent mesh width before calibration:26.318589mm; height:20.602777mm.
One uniform scale1.1018827602 is applied to the ENTIRE source scene after inch-to-mm conversion; total factor27.9878221094mm/source unit. Resulting stent diameter29.0000mm; stent height22.7018mm. No different scale or positional offset is applied to the dock, valve or their constituent meshes. Only whole-scene recentring/grounding and specified whole-product turntable rotations are used.
Full assembly dimensions after calibration:48.2438×31.9401×51.0722mm. Top rim outer envelope approx31.2900×31.3365mm.
Functional-coil mesh MesherID3 minimum radial vertex distance from supplied stent axis gives estimated minimum inner diameter30.9128mm; outer radial diameter35.2810mm. This is a mesh-based radial estimate, not an engineering bore or full axial clearance/contact assessment. Authored alignment is retained; real-world seating/implant orientation and fit remain unverified.
The earlier51.17% separate-dock enlargement belongs only to v01 and is NOT used in v02. The new supplied source configuration has the ascending loop and covered turns seen in the reference, instead of the earlier small dock's flared guard.

## Frames and output
Eleven RENDER v02 files: dock S03 at0/20/40degrees; assembly S05 at12/30degree elevation; transparent S06 product and separate shadow; valve-only12/30degree views; valve and assembly detail views.
All are native3840×2160, with the unchanged required14px #8A7F72 bottom-left review label. No lockup, logo or invented copy was added. S06's two pass labels should appear only once when composited into a layout.
Camera90mm equivalent; main elevation12deg,alternate/detail30deg,S06 8deg. Main x58%/floor contacty60%,width12%; S06x70%,width9%. Camera/lighting/composition parameters are retained; distance is recomputed to preserve footprint with the replacement source geometry. Light positions/intensities and beige material colours remain unchanged. Shadow-map coverage was enlarged to eliminate a diagonal shadow-boundary artifact in the empty background, without changing light placement.
Standalone variants hide the opposite supplied product (dock or valve); combined views retain all18meshes. This is source-part selection, not fabric removal. All geometry buffers are unmodified.

## Remaining review gates
Q2/RESILIA geometry and appearance fidelity remain unverified; updated material colours do not establish RESILIA-specific geometry. First-generation review label remains as explicitly requested; the new package does not independently prove generation/version. Q18/client-use approval remains open. The hero references guide appearance but do not close either gate. End-card approved artwork/footnotes remain for design-champ.

## Reproduction
Three.js0.180.0,local headless Chrome. Source code/settings/audits and converted maps are in _render-source-v02. Original source ZIP remains at /Users/andresfabian/Downloads/M3.ValveP.Simp_02.01_(.zip. Extract it to the renderer's resilia-model folder, retain the FBX unchanged as Model.fbx, and serve the renderer locally with its Three.js dependency. No product source was uploaded to an image-generation service.
