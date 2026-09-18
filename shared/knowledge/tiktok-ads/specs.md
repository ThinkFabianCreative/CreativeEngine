# TikTok ad specifications

Checked 2026-09-16. Public TikTok Ads Help Center pages, read as server-rendered HTML. No ad account was inspected. Read [usage rules](README.md) and [source conflicts](source-conflicts.md) before production.

A dash means not published in the inspected page, never zero or unlimited. "Requirement" means the page states it as a limit (≥, ≤, max, supported, cannot). "Recommendation" means the page says recommend, suggest or best practice. The "Last updated" date is the one printed on each TikTok page.

| ID | Format | Buying type | Source last updated | Status |
|---|---|---|---|---|
| [TT-001](#tt-001) | In-Feed video, Non-Spark | Auction | June 2026 | DOCUMENTED |
| [TT-002](#tt-002) | Spark Ads (organic post boosted) | Auction and Reach & Frequency | June 2026 | DOCUMENTED |
| [TT-003](#tt-003) | In-Feed video, reservation (incl. Reach & Frequency) | Reservation | July 2025 | SOURCE_ISSUE |
| [TT-004](#tt-004) | TopView | Reservation | June 2026 | SOURCE_ISSUE |
| [TT-005](#tt-005) | Carousel (image) ads | Auction | September 2026 | SOURCE_ISSUE |
| [TT-006](#tt-006) | TikTok Ad Network (formerly Pangle) assets | Auction | September 2026 | DOCUMENTED |
| [TT-007](#tt-007) | Global App Bundle video (CapCut, Fizzo) | Auction | July 2025 | DOCUMENTED |
| [TT-008](#tt-008) | Global App Bundle image (CapCut, Fizzo) | Auction | September 2026 | DOCUMENTED |

## Shared: profile photo and account name

Applies to TT-001, TT-003 and TT-004 (same text on each page). For Spark Ads the organic account's profile and name are used.

| Field | Value | Classification |
|---|---|---|
| Profile photo | 98 × 98 px, 1:1; .jpg/.jpeg/.png; < 50 KB; optional for Non-Spark (default used if blank) | Requirement |
| Profile photo safe zone | Key element inside centre 66 × 66 px | Requirement (crop guidance) |
| Account name (nickname) | One line; max 20 characters (10 for Chinese, Japanese, Korean) | Requirement (display limit) |
| Account name, recommended | 4–10 characters (2–5 CJK) | Recommendation (reservation and TopView pages) |
| Account name characters | Emojis and "{ }" not supported; punctuation counts; leading/trailing spaces don't count; full-width CJK characters take 2 spaces | Requirement (reservation and TopView pages) |
| App name | Pulled automatically from App Store / Google Play; cannot be typed manually | Requirement |

## TT-001

**TikTok Auction In-Feed video, Non-Spark · DOCUMENTED**

[Source](https://ads.tiktok.com/help/article/tiktok-auction-in-feed-ads?lang=en) · checked 2026-09-16 · last updated June 2026 · account availability NOT_TESTED.

| Field | Value | Classification |
|---|---|---|
| Aspect ratio | 9:16 vertical (recommended); 16:9 horizontal; 1:1 square | 9:16 is a recommendation; all three are supported |
| Minimum resolution | ≥ 540 × 960 (9:16); ≥ 960 × 540 (16:9); ≥ 640 × 640 (1:1) | Requirement |
| File types | .mp4, .mov, .mpeg, .3gp, .avi | Requirement |
| Duration | Up to 10 minutes | Requirement |
| File size | ≤ 500 MB | Requirement |
| Bitrate | ≥ 516 kbps | Requirement |
| Ad caption | White, fixed font; no clickable links, "@" or hashtags | Requirement (display behaviour) |
| Ad caption length | Not stated on this page. Reservation/TopView pages: max 100, keep within 100 (50 CJK) to avoid "See more" | — (see TT-003, TT-004) |
| Safe zone | Varies with ratio, caption length and add-ons (e.g. anchors). Published only as downloadable zip templates: Standard LTR, Standard with Anchor, Arabic RTL, Arabic RTL with Anchor | Requirement to keep key elements inside; pixel values not transcribed (zip not opened) |
| Download card | App ads only; generated automatically | Automatic |
| Creative basics | 9:16, at least 720p, sound on, keep content in UI safe zone; hook within first 6 s; proposition in first 3 s; 5–10 words per second for on-screen text | Recommendation ([creative best practices](https://ads.tiktok.com/help/article/creative-best-practices?lang=en)) |

## TT-002

**Spark Ads · DOCUMENTED**

[Source](https://ads.tiktok.com/help/article/spark-ads) · checked 2026-09-16 · last updated June 2026 · also [auction in-feed page](https://ads.tiktok.com/help/article/tiktok-auction-in-feed-ads?lang=en) · account availability NOT_TESTED.

| Field | Value | Classification |
|---|---|---|
| What it is | Boosts an organic TikTok post (own account, or a creator's with authorization code); engagement accrues to the organic post | Definition |
| Ratio, resolution, file type, bitrate, file size | No restrictions (whatever posted organically) | Source statement |
| Duration | Max 10 minutes for a sparked video (auction in-feed page says "no restrictions") | Requirement; see conflicts |
| Caption | Taken from the organic post; may be blank; @ tags, emoji and hashtags allowed; max 4 lines shown | Requirement |
| Display name and text | Reflect the organic post; not editable in Ads Manager (Spark Ads push allows text edits) | Requirement |
| Objectives | Auction: Reach, Traffic, Video Views, Community interaction, App promotion, Conversions, Lead generation, Sales. R&F: Reach, Traffic, Video Views | Availability as documented |
| Account cap | 10,000 Spark Ads per Ads Manager account | Requirement |
| Deletion | Post must be un-authorized as a Spark Ad before deleting from organic account | Requirement |

## TT-003

**Reservation In-Feed (incl. Reach & Frequency) · SOURCE_ISSUE**

[Source](https://ads.tiktok.com/help/article/tiktok-reservation-in-feed-ads-reach-frequency?lang=en) · checked 2026-09-16 · last updated July 2025 · account availability NOT_TESTED.

Applies to Non-Spark Ads and Spark Ads Push. Spark Ads Pull: no restrictions beyond a successful organic upload.

| Field | Value | Classification |
|---|---|---|
| Aspect ratio | 9:16 (recommended), 16:9, 1:1 | 9:16 recommendation |
| Minimum resolution | ≥ 540 × 960; ≥ 960 × 540; ≥ 640 × 640 | Requirement |
| File types | .mp4, .mov, .mpeg, .3gp (no .avi) | Requirement |
| Duration | 5–60 s | Requirement |
| Duration, recommended | 9–15 s | Recommendation |
| File size | ≤ 500 MB | Requirement |
| Bitrate | ≥ 2,500 kbps | Requirement |
| Ad caption (Non-Spark / Push) | Max 4 lines before "See more"; keep within 100 characters (50 CJK) | Recommendation (length); 4-line display is behaviour |
| Ad caption characters | Emojis allowed (Unicode v11 only) and count as 2; "{ }" not allowed; "@" allowed but not clickable on Non-Spark; "#" only for commercial, sponsored or organic hashtag challenges, never non-commercial hashtags with commercial intent; no links | Requirement |
| Ad caption (Spark Pull) | From organic caption; max 150 characters or blank (same page also says "no caption limit") | SOURCE_ISSUE |
| CTA | Selected from a fixed list (no custom text or colour; colour auto-matched); default Learn more; auto-translated | Requirement |
| CTA list | App download: Download, Learn more, Listen now, Play game. Landing page (25): Apply now, Book now, Contact us, Download, Experience now, Get quote, Get showtimes, Get ticket now, Install now, Interested, Join this hashtag, Learn more, Listen now, Order now, Play game, Pre-order now, Read more, Shoot with this effect, Shop now, Sign up, Subscribe, View now, View video with this effect, Visit store, Watch now. "Join this hashtag" only for commercial or sponsored Hashtag Challenges | Requirement (list) |
| Audio | All video creatives must have sound; Non-Spark music shown as "Promoted Music" | Requirement |
| Creative notes | No watermarks (incl. TikTok's); must not mimic TikTok UI; avoid white/transparent backgrounds (white UI text); localized language | Requirement / recommendation as stated |
| Safe zone | Same zip templates as TT-001 (LTR, RTL, with/without anchor) | Pixel values not transcribed |
| Asset changes | Cannot change once live; review within 2 days | Requirement |

## TT-004

**TopView · SOURCE_ISSUE**

[Specs](https://ads.tiktok.com/help/article/tiktok-reservation-topview) (June 2026) · [About TopView](https://ads.tiktok.com/help/article/about-topview) (August 2026) · checked 2026-09-16 · account availability NOT_TESTED.

Qualified customers only, via sales rep (some can book in Ads Manager). Opens with a 3-second full-screen takeover, then becomes an in-feed video. Sound on. Supports Spark and Non-Spark.

| Field | Value | Classification |
|---|---|---|
| Aspect ratio | Vertical 9:16 only | Requirement ("Always use vertical videos") |
| Minimum resolution | ≥ 540 × 960 | Requirement |
| File types | .mp4, .mov, .mpeg, .3gp | Requirement |
| Duration | 5–60 s | Requirement |
| Duration, recommended | 9–15 s | Recommendation |
| File size | ≤ 500 MB | Requirement |
| Bitrate | ≥ 2,500 kbps | Requirement |
| Ad caption (Non-Spark / Push) | Max 100 characters; 4 lines before "See more"; same character rules as TT-003 | Requirement |
| Ad caption (Spark Pull) | Page says both "no caption limit" and "max 100 characters" | SOURCE_ISSUE |
| Safe zones | Two stages: open-screen (first 3 s) and in-feed; in-feed is stricter; LTR and RTL; zip templates. Nothing may overlap TikTok logo, skip button or swipe-up link in first 3 s | Requirement; pixels not transcribed |
| First 3 seconds | No plain white; must be vertical (horizontal trailers allowed only after 3 s); no harsh sounds | Requirement |
| Audio | Must not be silent; not pure verbal broadcast; a promotional sentence may not repeat more than twice in a row | Requirement |
| Content | Real people or narrative animation; still pictures not allowed as main narrative (not in first 3 s nor over half the duration); no fake UI (play buttons, calls, messages); no QR codes, barcodes, phone numbers or addresses except required disclaimers | Requirement |
| CTA | Same 25 standard CTAs as TT-003; "Shoot with this effect" not supported for Non-Spark; "Join this hashtag" only for commercial or sponsored Hashtag Challenges; auto-translated, English fallback | Requirement |
| URL | Web view (https) or TikTok in-app URLs; no app-store links; no external deeplinks | Requirement |
| Exclusivity | Same creative cannot run in other placements the same day, nor the day before/after a 100% SOV TopView; pre-approval required; max 20 ads per ad group | Requirement |

## TT-005

**Carousel ads · SOURCE_ISSUE**

[Specs](https://ads.tiktok.com/help/article/specifications-for-carousel-ads) · [About](https://ads.tiktok.com/help/article/carousel-ads?lang=en) · checked 2026-09-16 · last updated September 2026 · account availability NOT_TESTED.

Image carousel in the TikTok feed. Objectives: Traffic, Web Conversions, App Promotion, Lead Generation, Product Sales (Catalog), Brand Auction Reach. Standard Carousel supports Spark and Non-Spark; VSA (catalog) Carousel Non-Spark only.

| Field | Value | Classification |
|---|---|---|
| Image count | Upload min 2, max 35; min 2 shown, max 20 shown | Requirement |
| File types | .jpg/.jpeg or .png | Requirement |
| File size | "≤100 KB suggested" | Recommendation as worded; see conflicts |
| Resolution | Horizontal 1200 × 628; square 640 × 640; vertical 720 × 1280 | Listed without "minimum" or "recommended"; treat as target sizes |
| Music | Required, loops; ≥ 2 s; .mp3, up to 10 MB. Standard: Commercial Music Library or upload. VSA: upload only. CML music is silent on TikTok Ad Network | Requirement |
| Copy | One ad caption and one CTA for all images | Requirement |
| Links | Standard: one URL for all images. VSA: each product image can link to its own product URL (catalog) | Requirement |
| Placement note | Automatic placement filters out TikTok Ad Network and Global App Bundle | Documented behaviour |

## TT-006

**TikTok Ad Network (formerly Pangle) · DOCUMENTED**

[Source](https://ads.tiktok.com/help/article/specifications-for-pangle-ad-assets) · checked 2026-09-16 · last updated September 2026 · account availability NOT_TESTED.

Third-party publisher apps. TikTok recommends supplying all resolutions.

| Asset | Resolutions | Ad formats | File types | Max size |
|---|---|---|---|---|
| Video (up to 10 min) | 1280 × 720; 720 × 1280; 720 × 720 | Interstitial, Rewarded, App Open, Native, Banner | .mp4, .mov, .mpeg, .avi | 500 MB |
| Carousel (up to 50 images) | 1200 × 628; 640 × 640; 720 × 1280 | Interstitial, Rewarded | .jpg, .jpeg, .png | 100 MB |
| Playable | 1280 × 720; 720 × 1280 | Interstitial, Rewarded | .zip | 5 MB |
| Image | 1200 × 628; 640 × 640; 720 × 1280 | Interstitial, App Open, Native, Banner | .jpg, .jpeg, .png | 100 MB |
| Image (Ad Network exclusive) | 600 × 500; 640 × 200; 640 × 100 | Banner | .jpg, .jpeg, .png | 100 MB |

Classification: file size, types and duration are requirements; supplying all resolutions is a recommendation. Video thumbnail defaults to first frame if none is selected.

## TT-007

**Global App Bundle video · DOCUMENTED**

[Source](https://ads.tiktok.com/help/article/global-app-bundle-video-ad-specifications?lang=en) · checked 2026-09-16 · last updated July 2025 · account availability NOT_TESTED.

Placements: App Open (CapCut, Fizzo); In-Feed / 2-Column Feed (CapCut); Banner (CapCut); Interstitial (CapCut, Fizzo); Native (Fizzo).

| Field | Value | Classification |
|---|---|---|
| Resolution | 9:16 ≥ 720 × 1280 (recommended ratio); 16:9 ≥ 1280 × 720; 1:1 ≥ 640 × 640 | Minimums are requirements; 9:16 recommended |
| File types | .mp4, .mov, .mpeg, .avi | Requirement |
| Duration | 5–60 s; recommend 21–30 s | Requirement / recommendation |
| Bitrate | ≥ 516 kbps | Recommendation (worded "recommended") |
| File size | ≤ 500 MB | Requirement |
| Profile image | 1:1; .jpg/.jpeg/.png; < 50 KB | Requirement |
| App name | 4–40 Latin letters; 2–20 Asian characters | Requirement |
| Brand name | 2–20 Latin letters; 1–10 Asian characters | Requirement |
| Ad description | 1–100 Latin; 1–50 Asian; no emojis or special characters | Requirement |

## TT-008

**Global App Bundle image · DOCUMENTED**

[Source](https://ads.tiktok.com/help/article/global-app-bundle-image-ad-specifications?lang=en) · checked 2026-09-16 · last updated September 2026 · account availability NOT_TESTED.

Same placements as TT-007.

| Field | Value | Classification |
|---|---|---|
| Resolution (labelled "Video Resolution" on page) | 9:16 ≥ 720 × 1280 (recommended); 16:9 ≥ 1280 × 720; 1:1 ≥ 640 × 640 | Requirement (minimums) |
| File types | JPG, JPEG, PNG | Requirement |
| File size | Within 100 MB | Requirement |
| App name | 4–40 Latin; 2–20 Asian; no emojis; punctuation and spaces count | Requirement |
| Brand name | 2–20 Latin; 1–10 Asian; no emojis; punctuation and spaces count | Requirement |
| Ad description | 1–100 Latin; 1–50 Asian; no emojis, "{ }" or "#"; punctuation and spaces count | Requirement |
| Truncation | Longer text may be cut off depending on device | Behaviour |

## Not covered in this pass

TikTok Collection ads, Search ads, Branded Effects, Branded Mission, Pulse / premium contextual placements, Interactive Add-ons (display card, gesture, etc.), Lead generation instant forms, TikTok Shop / Video Shopping ads, and single-image "photo" posts outside carousel. See [source conflicts](source-conflicts.md).
