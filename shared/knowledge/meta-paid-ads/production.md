# Production requirements and preflight

Research date: 2026-09-12. Numeric placement specifications live in the four format references. This page combines sourced guidance with explicitly labeled CreativeEngine production procedure.

## Canvas and cropping

Use a placement-specific canvas. Do not stretch square artwork into 9:16 or treat a generic minimum pixel pair as an exact recommended export. Retain editable masters and generate the variants actually needed by the assignment. This is CreativeEngine production advice, not an assertion that every placement accepts every ratio.

A useful **derived** canvas set for planning is 1440 × 1800 (4:5), 1440 × 1440 (1:1), 1440 × 2560 (9:16), and 1920 × 1080 (16:9 when required). This is not a blanket Meta requirement; Instagram Feed video and WhatsApp Status have different published recommendations. Never upscale a small source and call it native high resolution.

## Safe zones

[Meta safe-zone guidance](https://www.facebook.com/business/help/980593475366490) says key content should remain clear of interface overlays and cropping. It recommends inspecting the Safe zone guardrail in Ads Manager, notes taller-screen cropping, and says 9:16 Instagram Feed video follows the Stories/Reels guidance. For Reels ads with disclaimers it calls for keeping key creative content clear of the bottom 40%.

| Source context | Published clearance guidance | Handling |
|---|---|---|
| Instagram Stories image/video; Instagram Reels image/video; selected Reels carousel/collection entries | Top 14%, bottom 35%, sides 6% | Use as planning guide; verify the exact placement preview |
| Facebook Stories image | Top 14%, bottom 35%, sides 6% | Do not silently substitute the different video guidance |
| Facebook Stories video and carousel | Top 14%, bottom 20%, with approximate pixel examples | Source differs from the image entry; inspect current overlay |
| Messenger Stories image | Top 14%, bottom 20% | Published pixel examples do not exactly match all resolutions |
| Messenger Stories video | Top and bottom 14% | Do not apply this to Instagram automatically |

For a 1440 × 2560 canvas, **derived arithmetic** for 14/35/6 clearances gives approximately 358 px top, 896 px bottom, 86 px on each side. With a bottom-40% disclaimer treatment, bottom clearance is 1024 px. These are calculated from percentages, not additional official pixel specifications. Clearances protect key content; they do not mean the background must be empty.

Where Meta's pages disagree, preserve the conflict. A current setup-specific overlay is the production check, not a reason to rewrite history as if all sources agreed.

## Video encoding and sound

The Facebook Feed, Stories, Reels and other source-linked video entries recommend H.264, square pixels, a fixed frame rate, progressive scan and stereo AAC at at least 128 kbps. They warn against edit lists/special boxes in containers. Where an inspected entry does not state a codec, do not relabel this shared recommendation as a placement-specific hard limit. A universal numerical frame-rate cap or video bitrate was not established in this pass.

Most inspected entries list MP4/MOV/GIF, but Instagram Reels and the Facebook Reels overlay video entry list MP4/MOV. Collection and carousel media also have exceptions. Check the record before export.

Meta generally recommends captions and audio, but the inspected Audience Network, Threads and WhatsApp Status pages say caption tracks are unsupported. Distinguish a separate caption track from readable text rendered into the visual. Burned-in text must still pass readability and safe-zone checks. Do not assume auto-captioning exists; Facebook Reels' inspected entry explicitly says it does not.

The [Instagram Reels video entry](https://www.facebook.com/business/ads-guide/update/video/instagram-reels) lists exclusions including licensed music, face/camera effects, GIF media, product-tag media and old existing reels. It recommends original audio or Meta Sound Collection. Treat these as setup-sensitive checks; do not infer commercial music rights from the availability of a track in an organic-post editor. No rights or policy approval was performed here.

## Copy and interface behavior

Text recommendations in the tables are not universal enforced maxima. Visibility and truncation depend on placement and configuration. Important meaning must survive a shortened primary text and an absent description.

The [Facebook Feed video guide](https://www.facebook.com/business/ads-guide/update/video) states that certain Awareness/performance-goal configurations hide the mobile footer, including headline, description and CTA. The [image-practices page](https://www.facebook.com/business/help/388369961318508) reports a March 2026 footer change removing displayed URLs for certain Feed ads. Therefore, preview the actual rendering; do not rely on an element merely because it exists in the editor.

## CreativeEngine preflight — recommended procedure

- Confirm format × placement × objective × conversion location, device context and creation path.
- Recheck the relevant source date, restrictions and open conflicts.
- Inspect dimensions, actual ratio, file type, file weight and duration. Confirm carousel card count and image/video compatibility.
- Preview all placements with safe-zone overlays; inspect crops, faces, proof, logo, captions, CTA and disclosures.
- Test sound-on and sound-off comprehension where applicable. Verify audio usage rights separately.
- Inspect the final destination on mobile. Confirm offer continuity, form behavior, downloads, event booking and the actual success event.
- For catalog/collection: check cover, tiles, destination mapping, available products and Instant Experience.
- For automated enhancements: inspect what is actually enabled and how it changes media or text; user/client approval of the asset does not necessarily approve a generated alteration.
- Record a concrete exception or open question rather than inventing a platform rule or predicting results.

This preflight does not replace Meta's live review, current advertising policies or account eligibility checks.
