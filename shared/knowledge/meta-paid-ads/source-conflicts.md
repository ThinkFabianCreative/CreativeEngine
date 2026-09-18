# Source conflicts, quarantine and coverage gaps

Checked 2026-09-12. These are observed documentation issues or explicit research limits, not invented platform restrictions. Follow the links in the corresponding specification records.

## Quarantined entries

| Record | Issue | Required resolution |
|---|---|---|
| META-017 image / Audience Network Rewarded Video | Description and fields repeat Facebook Feed, including panoramas | Confirm actual eligibility and obtain placement-specific specs |
| META-033 video / Facebook Right Column | Feed-style content, mobile ratios and 360-video material | Confirm the rendering and accepted asset type in current Ads Manager |
| META-034 video / Facebook Groups Feed | Feed-style fallback on legacy-labeled route | Confirm current existence and eligible format |
| META-046 carousel / Facebook In-Stream Video | Image cap shown as 4 GB, count shown as 10 without bounds | Verify image cap, card bounds and availability; do not use 4 GB as an image allowance |
| META-050 carousel / Audience Network Rewarded Video | Generic Feed carousel description and long-duration values | Confirm eligibility rather than treating route existence as proof |
| META-051 carousel / Messenger Stories | Generic Feed carousel description and square/long-video values | Confirm eligibility and rendering |
| META-052 carousel / Facebook Groups Feed | Generic Feed carousel fallback on legacy-labeled route | Confirm current existence and eligible format |

Values in quarantined records are observations retained for traceability, not validated production specifications.

## Field-level issues

- **Instagram Feed image-only carousel 4:5:** the Ads Guide presents it broadly; [carousel best practices](https://www.facebook.com/business/help/927639917355563) restricts 4:5 to Advantage+ catalog product images. Keep the conflict OPEN. Do not silently choose the more convenient statement.
- **Facebook Stories carousel:** source recommends 1:1 but lists 1080 × 1920. Both are preserved; neither is converted into an invented exact canvas.
- **Audience Network image:** grouped native/banner/interstitial source lists 9:16 alongside 398 × 208. Those are not the same shape. Verify the exact subplacement rather than creating a universal banner template.
- **Generic square pixel pairs on vertical pages:** Messenger Stories image, some Reels carousels and collection pages show vertical ratios with an “at least 1080 × 1080” size. This may describe minimum dimensions rather than a finished canvas. It does not justify exporting a square vertical ad.
- **Safe zones:** Facebook Stories image and video differ; Messenger differs again. Approximate pixel examples do not consistently match the stated percentages at every resolution. Use percentage-derived planning with the current setup-specific preview; document any conflict.
- **Instagram Reels video minimum:** the guide says 0 seconds. A zero-length file is not a meaningful ad. Verify before encoding; do not blindly encode this as an accepted minimum.
- **Facebook Reels video maximum:** the guide says no maximum duration, while file size remains capped. Treat this as a source statement in its context, not a promise about every creation route or account.
- **Right Column carousel video fields:** video limits appear in the guide, but no account test establishes actual video rendering. Image use and video capability should not be conflated.
- **Threads CTA/crop wording:** a video CTA statement appears inside the image section, and carousel crop wording differs from single-media wording. Verify the actual preview and avoid depending on an unverified button.
- **WhatsApp destination sources differ:** the broad WhatsApp help overview says interactions lead to chat; the more detailed Meta Status pages also document website destinations and conditional app support. Preserve that scope difference; use the actual Status setup, not a blanket chat-only assumption.

## Coverage not yet verified

- Availability in the user's actual ad accounts, market, currency, language and campaign setup.
- Every objective × conversion location × performance goal × CTA combination.
- Full supported-ratio grids, every mobile/desktop rendering, boosted-post versus Ads Manager differences and all regional restrictions.
- Complete Instant Experience component limits, form field limits, catalog schema, reminder ads, flexible creative and every Advantage+ enhancement.
- WhatsApp Channels/promoted Channels upload specifications; placement listings alone do not supply them.
- Current availability or retirement of legacy products, including ambiguous guide-menu entries, AR and sponsored messages.
- Universal video FPS/bitrate requirements beyond the encoding guidance actually retrieved.
- Upload acceptance, ad review, delivery, click behavior, form submission, measurement or performance. This was public-document research.

Do not call this V1 an exhaustive inventory of every available product. It is a comprehensive pass through the visible core guide with explicit adjacent-product coverage and gaps. Add verified records as specific assignments require them.
