# Additional formats, experiences and setup layers

Research date: 2026-09-12. These complement the 66 placement records. Missing technical detail remains OPEN; do not fill it from unrelated image/video entries.

## Playable ads

[Official overview](https://www.facebook.com/business/ads/playable-ad-format) describes a lead-in video, interactive app/game demo and app-install CTA. [Official asset specifications](https://www.facebook.com/business/help/412951382532338), read directly:

- A single HTML5 .html/.htm file or a ZIP bundle is accepted.
- Maximum uploaded file/archive size: 5 MB. ZIP: at most 100 files, with index.html at the root and relative asset paths.
- Single-file assets must be embedded. ZIP HTML and JavaScript follow the same constraints: no external network calls or dynamic remote asset loading in either packaging.
- Portrait and responsive layout required. Do not depend on mraid.js or similar frameworks.
- JavaScript redirects are prohibited; Meta recommends its FbPlayableAd.onCTAClick() CTA handler. Follow current integration docs when implementing.
- A video asset is also needed. Its playback and geometry depend on placement; do not treat the playable's responsive canvas as the video specification.

No playable was built, executed, uploaded or account-tested in this pass.

## Slideshow

[Official slideshow overview](https://www.facebook.com/business/ads/slideshow-ad-format) documents image-based motion/sound/text storytelling. Treat it as a production method with a rendered ad result. Use the selected placement's video constraints after checking the current creation tool. A universal image count or slideshow-duration limit was not verified here.

## Instant Experience and collection

[Official Instant Experience help](https://www.facebook.com/business/help/183469315334462) describes a mobile fullscreen experience with media, text, buttons and links, accessible from multiple base formats. Available placements depend on its components. The inspected page says Instant Experience views stopped counting as landing-page views in June 2025. Plan measurement accordingly.

Collection records specify required Instant Experience and, for most inspected entries, a landing URL. Separate cover media from product tiles: Instagram Reels collection explicitly distinguishes 9:16 cover and 1:1 product imagery. Component-level Instant Experience limits were not fully audited. Retrieve those before building a specific experience; do not reuse cover limits for every component.

## Lead ads, messaging and calls

[Meta's current lead-ad overview](https://www.facebook.com/business/ads/ad-objectives/lead-generation) documents native instant forms, website forms, calling, messaging and multiple conversion locations. The acquisition creative still needs a valid placement-format record.

CreativeEngine preparation fields: form/destination owner; value offered; exact questions and required fields; confirmation behavior; privacy/consent requirements from approved sources; follow-up route; lead delivery/CRM integration; and success-event definition. Those are project requirements to establish, not platform capabilities inferred from the word “lead.” Test any CRM/measurement integration separately.

Brochure/guide downloads, campus-visit bookings, event registration and newsletter subscriptions can be project goals. Do not automatically map them to a native form, specific objective or CTA button without checking the selected setup.

## Catalog and partnership layers

Catalog ads can generate delivery from product data; their dimensions depend on the resulting image, video, carousel or collection placement. Check catalog imagery, item eligibility, price/availability, links and actual creative automation. The inspected carousel documentation mentions catalog-dependent ratios and product availability; it does not establish every catalog feature's current support.

Partnership ads add an identity/permission layer. [Meta's Reels page](https://www.facebook.com/business/ads/facebook-instagram-reels-ads) describes using partner content and partner permission. Do not assume that permission or compatibility exists for every surface: the inspected Threads and WhatsApp Status pages list partnership incompatibility. No partner permissions were changed.

## Channels, promoted content and other features

[WhatsApp's official announcement](https://about.fb.com/news/2025/06/helping-you-find-more-channels-businesses-on-whatsapp/) distinguishes promoted Channels from Status advertising. Its [current help overview](https://faq.whatsapp.com/491963319630082) also refers to Status/Channels placements. Exact Channels creative specifications and buying eligibility remain OPEN in this version.

Existing-post promotion, reminder/event ads, flexible creative, site links, catalog variations and Advantage+ enhancements are not represented as separate universal canvas sizes. They need their own compatibility checks when selected. AR/interactive legacy products and sponsored-message inventory were not confirmed as currently available in this research pass; do not advertise them as available or retired without current evidence.
