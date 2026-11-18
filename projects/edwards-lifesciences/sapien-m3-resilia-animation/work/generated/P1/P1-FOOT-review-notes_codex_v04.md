# P1 Footing — shiny metal and mesh fabric v04

2026-10-15 · Latest user requests: “expose the struts” and “improve textures, metals to look shiny, fabric to look meshy”. This v04 is the current product-render set; prior versions are retained.

## Visible changes
Existing inner struts stay exposed. Metal is now polished silver with controlled studio reflections: stent base #A2A7AB,metalness.93,roughness.17,reflection intensity1.05. Dense metal markers use metalness.9,roughness.20. The reflection map is generated locally from Three.js's procedural RoomEnvironment; it is assigned to metal materials only. Beige background and diffuse key/fill light settings stay the same. Covered dock surfaces remain fabric/off-white, not invented bare chrome.

White fabric uses supplied _PascalSquareCloth.01_Alpha and _ZDepth textures for real weave openings and yarn relief. Roughness.92,alpha cutoff.36,bump amplitude.0015 source units. The contoured StageP_FurBase_v4_Expand source shell is visible, preserving its actual folds. Its original texture coordinates collapsed the weave; only UV coordinates were replaced with a cylindrical mapping around the supplied stent axis,with seam handling and60×15repeat. No vertex positions,normals,face connectivity or fold geometry changed.
The overlapping flat StageP_OutsideCloth_V4Expand shell is hidden to prevent it filling the weave openings or producing duplicate-surface speckling. This differs from v03,which kept both outer shells visible. The contoured outer fabric remains fully represented through the textured source shell. Its inward-facing backs are culled; it is not replaced by generated geometry.

The four inner lining/simplified skirt layers hidden in v03 remain hidden:
- StagePSimp_InsideCloth_V4Expand
- StagePSimp_LL_Cloth
- Sap323_ARv2Skirt_Expand_InsideStent
- Sap323_ARv2Skirt_Expand

Existing source stent,all3leaflets,top/bottom rims,white stitches/knots,and green stitching remain. Source white stitching on the metal remains visible; no new lattice or struts were drawn across the central opening. Leaflets stay smooth warm tan with subtle golden-beige material slots,distinct from the white weave.

## Source and alignment
Geometry comes solely from supplied M3.ValveP.Simp_02.01_(.zip,which contains a single authored valve–dock assembly and textures. Hero PNGs in SAPIEN M3 Resilia.zip guide appearance. No image-generation model was used for any product or texture revision.
The authored relative alignment is retained. Entire scene uniformly converts/calibrates from inch units to29mm stent diameter using factor27.9878221094mm/source unit. Estimated functional-coil inner diameter30.9128mm. No independent51% dock enlargement; that belongs to oldv01only. See v02 notes/source audits for measurements and their limitations.

## Exports and verification
11native3840×2160product PNGs: dock0/20/40deg; valve-only12/30deg; assembly12/30deg; valve and assembly detail; S06transparent product and separate transparent shadow. Required14px #8A7F72 bottom-left RENDER review label is burned into each. No logos/claims/copy added.
Camera parameters and projected bounds match v02 for all11views. Native dimensions,required label colour and S06alpha channels verified. Main12deg camera,30deg alternate/detail,and8deg end-card framing retained. Shadow-map coverage fixes from v02 are retained.
The latestZIP includes these11v04product renders plus3unchangedv01anatomical-heart MOOD frames. MOOD is upscaled4K concept imagery; product renders are native4K. The two image types remain separate frames. Each S06pass carries the required label; show it only once when compositing the two passes into a layout.

## Review status
These are material/visibility review drafts. Exposing lining and depicting open fabric weave are user-authorized illustration choices,not confirmation of actual manufactured layer visibility or porosity. Source leaflet pose/geometry still differs from the hero PNG. Shiny materials and texture corrections do not establish RESILIA-specific geometry; Q2/Q18/client approval remain open. The requested supplied-first-gen review label is retained; new-source generation/version is not independently confirmed.

Exact renderer/shader/UV and source-visibility settings are saved in _render-source-v04. Converted supplied source maps and earlier audits are in _render-source-v02. Original supplied ZIPs remain unchanged in Downloads. No product source was uploaded to image generation.
