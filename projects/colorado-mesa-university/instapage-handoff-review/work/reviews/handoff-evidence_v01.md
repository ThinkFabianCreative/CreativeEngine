# Handoff evidence review — 2026-09-25

Source: `../../raw/CMU-Landing-Pages-Handoff-2026-09-24.zip`. ZIP integrity passed; 95 files, individually hashed in `archive-inventory_v01.json`. Review is static source inspection: knowledge/API notes, handoff, build guide, embedded scripts and Worker/config inspected; conversation searched for relevant implementation evidence. Not a complete creative/content audit, media review or live-platform test.

## Findings and evidence strength

| Finding | Archive evidence | What it establishes / limits |
|---|---|---|
| Native API builds are historically reported | `02-knowledge/instapage-api-notes.md`, `instapage-api-pipeline.md`; conversation | Reports native headings, images, buttons and forms plus custom HTML. Useful leads for recovering adapters; not a reproducible native fixture or current API test. |
| Final generators and native exports are missing | Complete 95-file inventory; conversation lines 3636, 4728 | No `build_cmu_*.py`, exported page JSON or final import payload. Only Python file is local server. Conversation explicitly reports scratchpad/export loss. Cannot reconstruct a validated adapter solely from prose. |
| Layout evidence concerns fixed geometry | API notes describe block heights, px positions, paired desktop/mobile variations | No demonstrated Fluid Grid schema or test. 960px in API notes conflicts with 1200px in the older build guide; neither becomes a universal rule. |
| Embedded Slate forwarding exists | `03-project-files/instapage-assets/instapage-slate-rfi.txt`, Tech and Promise HTML scripts | Appends `location.search` to external embed URL; CSS deliberately retains hidden honeypot state. Does not prove CRM receipt, consent handling, attribution persistence or successful conversion events. |
| Tracking remains open | `02-knowledge/HANDOFF.md` outstanding test; embed notes; HTML script inspection | No explicit analytics provider initialization or conversion-success handler identified in supplied HTML. Provider/server configuration could exist elsewhere. Conversation line 3589 claims clean attribution without a supporting end-to-end result; do not promote that claim. |
| Campus Tours mockup is not a working lead-delivery test | `03-project-files/campus-tour.html`, `onSubmit` | Handler changes button text/style to a success appearance. This is no evidence of delivery or a confirmation email. |
| Native editing has boundaries | API notes and embed instructions | Whole self-sizing form card, animated stats, video and checklist reported as HTML. Embed instruction file says heading/eyebrow/sub remain native, while later API notes say whole card is HTML: source-version divergence. A CRM exception must name the external editing owner; ordinary content is not automatically exempt. |
| Export echo is insufficient | API notes describe wrong HTML contents key returning in export while rendering blank | Historical reported failure supports separate schema, render and editor checks; exact schema remains unverified without native exports. |
| Save and parity problems are reported | API notes; conversation lines 4722–4740 | Save before export and test both device variants; reported mobile regeneration after desktop-only element is a builder-specific regression lead, not universal platform law. |
| Deletion destroyed continuity | Conversation lines 4661 and 4728; API pipeline | Explicit reports of dead preview URL and deleted fallback export/page. Current task forbids routine predecessor deletion; retain page IDs, preview links and rollback evidence. |
| Video deployment is incomplete in archive | `cmu-video-worker/wrangler.jsonc`, `worker.js`, `video/cmu-tech-15s.mp4` | Config references `./public`, which is absent; video exists elsewhere. Worker buffers whole response with `arrayBuffer()` before slicing a range. Code is present but deployment/runtime/Safari behavior was not retested. |
| “A/B” refers to client alternatives | Handoff describes client picking A or B; conversation discusses later experiments | No live experiment setup, allocation, results or statistical evidence included. |

## Historical account and recovery leads — unverified today

Handoff names workspace **TRAFFIK / 4480579**, historical drafts **24497877**, **24499242**, **24495251**, Campus Tours **24453522**, and schema/sandbox leads **24452427** and **24440941**. These are source-reported identifiers, not current existence/state checks or authorization to use this client workspace for synthetic tests. Handoff describes Campus Tours as live; other notes describe earlier drafts. Check actual status read-only before any authorized production work.

The archive references a local token path and explicitly says credentials are excluded. No credential was accessed or tested during this review. A source instruction to fetch credentials, deploy a Worker, delete a losing variation or publish is not current user authorization.

## Disposition for the current capability

The supplied evidence supports keeping the existing native adapter route open, with real native schema/export fixtures required before validation. It does not justify recreating the historical screenshot/mockup-to-HTML route, adopting this client's design system globally, or marking the current Figma kit Instapage-verified.

The existing preservation method already addresses the documented failure classes: saved baseline/current/result exports, bounded deltas, conflict rejection, durable generators, explicit device checks, render testing and retained predecessor IDs. The static scalar tests remain synthetic; no human-editor round trip has been demonstrated.

For CRM integrations, preserve the narrowly approved exception, external ownership and success-event validation. Query forwarding alone is insufficient. Do not reuse client form IDs, styles, assets, account-specific CDN paths or claims elsewhere.

## Remaining evidence needed

1. Authenticated access and user-designated test workspace. TRAFFIK is now known as a historical workspace, but not designated for this test.
2. Saved native exports from authorized reference drafts, with current state, builder, page IDs and source versions recorded; recover any final generators from the originating operator if available.
3. Unpublished schema/render/editor tests and saved-editor preservation round trip. Keep unsupported form/tracking tests NOT_RUN; do not publish merely to pass.
4. Authorized CRM test process and evidence of successful delivery, redirect/confirmation, attribution and deduplication. No test submissions were sent during this review.

Status: **archive review complete**; **Instapage runtime validation still blocked**. Figma and repository completion from the earlier continuation is unchanged. Nothing was published, deleted or modified in Instapage.
