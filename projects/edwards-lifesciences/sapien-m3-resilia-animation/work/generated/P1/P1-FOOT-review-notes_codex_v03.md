# P1 Footing — exposed inner struts v03

2026-10-15. User instruction: “expose the struts”. This revision supersedes v02's instruction to retain all inner lining coverage. It changes rendering visibility, not the source FBX file or frame shape.

Eight valve-containing images have been rerendered at native3840×2160: valve-only12/30deg, valve detail, assemblyS05 at12/30deg, assembly detail, S06 transparent product and separate shadow. Required14px warm-grey review labels remain. Prior exports are preserved.

Existing source Sapien3_Stent geometry is now visible around the inner circumference. Four obstructing lining/simplified skirt meshes are hidden for these review views:
- StagePSimp_InsideCloth_V4Expand
- StagePSimp_LL_Cloth
- Sap323_ARv2Skirt_Expand_InsideStent
- Sap323_ARv2Skirt_Expand

The exterior StageP_OutsideCloth_V4Expand and StageP_FurBase_v4_Expand remain visible; their inward-facing backs are culled with FrontSide materials to avoid covering the inner metal. Outer fabric coverage, top/bottom rim surfaces, source white stitches/knots and green stitching are retained. This is an editorial exposure of the supplied frame, not a claim that these layers are absent from the manufactured device.

No struts were invented. No source vertices, face connectivity, leaflet shapes, normals or relative assembly transforms were changed. No AI repainting or generation. Source stitches remain on the exposed frame; this is not a bare-metal CAD cutaway. Satin metal roughness increased to.68 and metalness reduced to.35 to restrain reflections; warm-tan leaflets/golden material slots and white fabric remain distinct.

Camera settings, image footprint and visible geometry bounding dimensions were checked against v02 and are identical for all8views. Beige set,light placement/intensities,authored valve–dock alignment and whole-scene scale are retained. The single supplied M3.ValveP.Simp_02.01_(.zip assembly is uniformly calibrated to a29mm stent. Estimated functional-coil inner diameter30.9128mm; no independent51% dock enlargement is used. See v02 review notes for source-unit measurements,shader/texture limitations,and source/model provenance.

This visibility change improves the inner-frame read; leaflet pose and detailed fabric/strut appearance still differ from the supplied hero reference. Material/visibility changes do not validate RESILIA-specific geometry. Q2/Q18 remain open; supplied-first-gen review labels retained. Before client use, confirm that this exposed-lining depiction is acceptable against approved reference.

The latest review ZIP includes8v03valve-containing renders,3unchangedv02dock views,and3unchangedv01anatomical-heart mood frames. Mood frames are upscaled4K concept images; product renders are native4K. S06 product/shadow transparency is verified. Exact settings and hidden-layer lists are saved in _render-source-v03; provided texture conversions/source audits remain in _render-source-v02.
