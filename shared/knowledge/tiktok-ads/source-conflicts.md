# TikTok: source conflicts, ambiguities and coverage gaps

Checked 2026-09-16. These are documentation issues observed on official TikTok Ads Help Center pages, not invented restrictions. Every conflict stays OPEN until an Ads Manager check or TikTok confirmation resolves it.

## Conflicts

| Topic | Source A | Source B | Working guidance |
|---|---|---|---|
| Video duration, In-Feed | [Auction In-Feed](https://ads.tiktok.com/help/article/tiktok-auction-in-feed-ads?lang=en) (June 2026): up to 10 minutes | [Reservation In-Feed](https://ads.tiktok.com/help/article/tiktok-reservation-in-feed-ads-reach-frequency?lang=en) (July 2025) and [TopView](https://ads.tiktok.com/help/article/tiktok-reservation-topview) (June 2026): 5–60 s, recommend 9–15 s | Not a true contradiction: the limits depend on buying type. Always record auction vs reservation before quoting a duration. |
| Bitrate | Auction In-Feed: ≥ 516 kbps | Reservation In-Feed and TopView: ≥ 2,500 kbps | Buying-type dependent. Encoding at ≥ 2,500 kbps satisfies both. |
| File types | Auction In-Feed lists .avi | Reservation In-Feed and TopView omit .avi | Deliver .mp4 or .mov. |
| Spark Ads duration | [About Spark Ads](https://ads.tiktok.com/help/article/spark-ads): 10-minute maximum for a sparked video | Auction In-Feed and TopView: "no restrictions" for Spark Ads Pull | Plan for ≤ 10 minutes. |
| Spark Pull caption length, reservation | Reservation page: "no caption limit" | Same page: "supports max 150 characters or blank" | Keep ≤ 100 characters (TikTok's "See more" guidance); verify in Ads Manager. |
| Spark Pull caption length, TopView | TopView page: "no caption limit" | Same page: "max 100 characters or blank" | Keep ≤ 100 characters. |
| "@" and "#" in Non-Spark captions | Auction In-Feed: captions don't support "@" or hashtags | Reservation/TopView: "@" allowed but not clickable; "#" allowed for commercial, sponsored or organic hashtag challenges | Avoid "@" and "#" in Non-Spark auction captions unless Ads Manager accepts them. |
| Carousel image file size | [Carousel specs](https://ads.tiktok.com/help/article/specifications-for-carousel-ads): "File size ≤100 KB suggested" | [TikTok Ad Network specs](https://ads.tiktok.com/help/article/specifications-for-pangle-ad-assets): carousel images max 100 MB | 100 KB is very small for 720 × 1280 and is worded as a suggestion. Treat it as an unconfirmed target, not a hard cap. Test the upload. |
| Carousel image count | Carousel specs: upload max 35, shown max 20 | TikTok Ad Network: carousel up to 50 images | Placement-dependent. Plan ≤ 20 for TikTok feed display. |
| Global App Bundle image | Page heading says image ad | Resolution field is labelled "Video Resolution" | Treat the minimums as image minimums; confirm. |

## Common spec-sheet contamination

Agency spec sheets often combine the **Global App Bundle / Pangle** copy rules (app name 4–40 Latin letters, brand name 2–20, description 1–100, no emojis, no "{ }" or "#") with **TikTok In-Feed** video specs. On current TikTok In-Feed pages, the app name is pulled automatically from the app store, the account name shows at most 20 characters, and Non-Spark reservation/TopView captions *allow* v11 emojis, counted as 2 characters. Do not apply Global App Bundle copy rules to TikTok feed ads.

## Safe zones: not transcribed

TikTok publishes In-Feed and TopView safe zones only as downloadable .zip templates (Standard LTR, with Anchor, Arabic RTL, RTL with Anchor; TopView open-screen and in-feed stages). These files were **not downloaded** in this pass, so no pixel margins are recorded here. The pages state that the safe area gets smaller as captions get longer and when add-ons or anchors are used. Before finishing any TikTok layout, download the current template from the linked page and check the creative in TikTok's preview tool.

## Coverage not verified

- Availability in any specific ad account, market or objective (NOT_TESTED).
- Auction In-Feed caption character limit and full CTA list. They were published only on the reservation and TopView pages. Dynamic/automatic CTA behaviour in auction campaigns was not verified.
- Commercial Music Library / Creative Center music licensing rules beyond the carousel page's CML statements.
- Collection ads, Search ads, Branded Effects, Branded Mission, Pulse, Interactive Add-ons, Instant Pages / lead forms, TikTok Shop ads, Smart+ creative limits, photo-post Spark Ads.
- Image Ads playbook PDF (not opened).
- Upload acceptance, ad review, rendering and delivery. This was public-document research only.
