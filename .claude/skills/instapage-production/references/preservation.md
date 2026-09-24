# Native adapters, preservation and evidence

Status 2026-09-24: offline scalar preservation implemented and tested with synthetic JSON. Native schema, importability, authorability and an actual editor round trip remain NOT_RUN. This is not a page renderer or a documented Instapage schema.

## Routes and limits

The approved annotated Figma specification is the target. Build structure using Instapage authoring tools. A native implementation generator/adapter may transform saved native exports where that specific builder/schema mapping is evidenced and validated. Preserve useful existing adapters, fixtures and exports; never promote a screenshot-to-HTML renderer.

Official [API reference](https://devdocs.instapage.com/#update-page), rechecked 2026-09-24: PATCH Update Page documents group assignment. JSON import creates a new page; it is not an in-place content patch. In-place content changes therefore use the native editor unless a subsequently documented and tested route exists. A successor draft has a new ID: preserve both IDs and preview URLs; do not delete the predecessor or claim its identity was retained.

## Three-way change strategy

1. Save the editor, export baseline B, record workspace/page IDs, builder mode, saved revision, spec/copy versions and native IDs mapped to stable B/E/F IDs. Keep unknown schema fields.
2. After human editing, SAVE and export current C. Compare all differences B→C, including mobile layout, forms, scripts and page settings. Do not infer success from API echo.
3. Express authorized desired changes D as an explicit scalar allowlist. Merge onto C: keep all unrelated editor edits; apply D only where C equals B or already equals D; stop on conflict. A no-op D preserves C. Never replace the whole page or arrays to avoid conflict resolution.
4. `scripts/ip_preserve.py` applies this conservative offline merge and requires the canonical SHA-256 of C. It rejects missing paths, object/array replacement, duplicate paths and any changed array on a numeric path (including reorder). A builder-specific adapter must resolve stable native IDs and verify structure before any more permissive merge. No such adapter is validated yet.
5. Immediately before applying, save/export again and compare with C. If changed, abort and replan. This check is not an atomic server lock: coordinate a single editor during application. Use native editor in-place edits for ID continuity, or import a separate unpublished successor when explicitly using the copy route.
6. Save/export the result R; compare expected scalar edits and every preserved human edit, then repeat schema, desktop/mobile and ordinary editor checks. Export comparison alone cannot certify responsiveness or editability.

## Required draft round trip (NA-10)

On an isolated unpublished draft: save/export B → human edits headline, image/alt and mobile spacing → SAVE/export C → automation changes a different approved scalar → save/export R → prove human edits and unknown fields survived. Repeat with a conflicting headline edit and prove it is refused. Reopen in editor; edit text, image, link, section and form label; check previews at 375, 390, 400, 767, 768, 769, 1200 and 1440 or additional spec widths. Keep the test page. Shared live Global Blocks must not be touched.

Schema validation needs real exported fixtures from the actual workspace/builder, not guessed JSON. Verify desktop/mobile element parity, native element types, form references and stable ID mapping. Save schema fixture/version and adapter hash beside results. Test integrations, redirect/thank-you, consent, attribution and duplicate conversion separately. Unsupported unpublished tests are NOT_RUN; do not publish solely to make them pass.

## Durable project record

Keep under `projects/<client>/<project>/work/production/<packet>_<release>_vNN/`:

- manifest with client/workspace, predecessor/successor page IDs and preview URLs, draft state, source/spec/copy versions, builder/features, timestamps and operator;
- generator/adapter source and version/hash, real schema fixture and assumptions;
- baseline/current/candidate/result JSON (approved handling, no secrets or submitted lead data), requested scalar changes, asset and native/spec ID mappings;
- schema and diff results, screenshots by width, form/tracking results, ordinary editor and preservation results;
- release record and rollback record identifying saved revision/export, affected IDs, exact inverse changes and remaining limitations.

Rollback of an unpublished in-place edit uses the recorded prior saved revision or bounded inverse editor changes after checking for newer human edits. Restoring an export through import creates a successor, not restoration of the old ID. A live rollback is a separate authorized release operation. Do not keep final generators or exports only in temporary folders.
