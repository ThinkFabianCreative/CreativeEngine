# Carousel specifications

Checked 2026-09-12. Public Meta documentation, not account validation. Read [usage and evidence rules](README.md) and [source conflicts](source-conflicts.md) before production.

Recommendations are distinct from technical requirements. A dash means not specified in the inspected entry, never zero or unlimited. Text values are primary/headline/description character recommendations, not automatically hard limits. Guide entries use the observed objective/context shown in each record; inspect the actual objective and conversion location before launch.

| ID | Placement | Recommended ratio | Recommended pixels | Status |
|---|---|---|---|---|
| [META-035](#meta-035) | Facebook Feed | 1:1 | At least 1080 x 1080 | DOCUMENTED |
| [META-036](#meta-036) | Instagram Feed | 4:5 image-only; video-containing: only 1:1 supported (source wording) | At least 1080 x 1080 | SOURCE_ISSUE |
| [META-037](#meta-037) | Facebook Stories | 1:1 (source wording) | At least 1080 x 1920 (source wording) | SOURCE_ISSUE |
| [META-038](#meta-038) | Instagram Stories | 9:16 | At least 1080 x 1920 | DOCUMENTED |
| [META-039](#meta-039) | Facebook Reels | 9:16 | At least 1080 x 1920 | DOCUMENTED |
| [META-040](#meta-040) | Instagram Reels | 9:16 | At least 1080 x 1080 | SOURCE_ISSUE |
| [META-041](#meta-041) | Facebook Marketplace | 1:1 | At least 1080 x 1080 | DOCUMENTED |
| [META-042](#meta-042) | Facebook Search Results | 1:1 | At least 1080 x 1080 | DOCUMENTED |
| [META-043](#meta-043) | Facebook Business Explore | 1:1 | At least 1080 x 1080 | DOCUMENTED |
| [META-044](#meta-044) | Instagram Explore home | 4:5 | 1080 x 1080 (source wording) | SOURCE_ISSUE |
| [META-045](#meta-045) | Facebook Right Column | 1:1 | At least 1080 x 1080 | SOURCE_ISSUE |
| [META-046](#meta-046) | Facebook In-Stream Video | 1:1 | At least 1080 x 1080 | QUARANTINED |
| [META-047](#meta-047) | Facebook video feeds ads | 1:1 | At least 1080 x 1080 | DOCUMENTED |
| [META-048](#meta-048) | Ads on Facebook Reels (overlay) | 1:1 | At least 1080 x 1080 | SOURCE_ISSUE |
| [META-049](#meta-049) | Audience Network Native, Banner and Interstitial | 1:1 | At least 1080 x 1080 | DOCUMENTED |
| [META-050](#meta-050) | Audience Network Rewarded Video | 1:1 | At least 1080 x 1080 | QUARANTINED |
| [META-051](#meta-051) | Messenger Stories | 1:1 | At least 1080 x 1080 | QUARANTINED |
| [META-052](#meta-052) | Facebook Groups Feed | 1:1 | At least 1080 x 1080 | QUARANTINED |
| [META-063](#meta-063) | Threads Feed | 1.91:1–9:16 supported; source says outside 4:5 center-cropped to 4:5 | 1440 x 1440 | SOURCE_ISSUE |
| [META-066](#meta-066) | WhatsApp Status | 9:16 recommended; source accepts aspect ratio smaller than 1.91:1 | 720 x 1280 | DOCUMENTED |

## META-035

**Facebook Feed · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/carousel) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG; MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 80/20/18 | Recommendation, unless verified otherwise |
| Maximum file size | Image 30 MB; video 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | Video 1 second–240 minutes | Source upload/playback rule as labeled; not recommended ad length |
| Cards | 2–10 | Technical count where applicable |

3% tolerance; landing URL required. Source introduction mistakenly says video format, but carousel-specific fields are present.

## META-036

**Instagram Feed · SOURCE_ISSUE**

[Meta source](https://www.facebook.com/business/ads-guide/update/carousel/instagram-feed) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG; MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 4:5 image-only; video-containing: only 1:1 supported (source wording) | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/—/— | Recommendation, unless verified otherwise |
| Maximum file size | Image 30 MB; video 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | Video 1 second–2 minutes | Source upload/playback rule as labeled; not recommended ad length |
| Cards | 2–10 | Technical count where applicable |

1% tolerance; landing URL required. Conflict: carousel best-practices help restricts 4:5 to catalog images; verify setup before promising 4:5.

## META-037

**Facebook Stories · SOURCE_ISSUE**

[Meta source](https://www.facebook.com/business/ads-guide/update/carousel/facebook-story) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 1:1 (source wording) | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1920 (source wording) | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/— | Recommendation, unless verified otherwise |
| Maximum file size | Image 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 500w | Technical requirement when published |
| Duration | Video not supported | Source upload/playback rule as labeled; not recommended ad length |
| Cards | 3–10 | Technical count where applicable |

Images only; URL required. Ratio/resolution conflict. Source safe zone 14% top / 20% bottom; 1–5 cards may show automatically before expansion.

## META-038

**Instagram Stories · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/carousel/instagram-story) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG; MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 9:16 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1920 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/— | Recommendation, unless verified otherwise |
| Maximum file size | Image 30 MB; video 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | Video 1–15 seconds | Source upload/playback rule as labeled; not recommended ad length |
| Cards | 2–10 | Technical count where applicable |

1% tolerance; URL required; safe zone 14% top / 35% bottom / 6% sides.

## META-039

**Facebook Reels · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/carousel/facebook-facebook-reels) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 9:16 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1920 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 40/—/— | Recommendation, unless verified otherwise |
| Maximum file size | Image 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 500w x 262h | Technical requirement when published |
| Duration | Video not specified | Source upload/playback rule as labeled; not recommended ad length |
| Cards | 2–10 | Technical count where applicable |

1% tolerance; source describes product tiles and requires Catalog or Advantage+ catalog creative source to enable their links; safe zone 14/35/6.

## META-040

**Instagram Reels · SOURCE_ISSUE**

[Meta source](https://www.facebook.com/business/ads-guide/update/carousel/instagram-reels) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 9:16 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | —/—/— | Recommendation, unless verified otherwise |
| Maximum file size | Image 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | Video not specified | Source upload/playback rule as labeled; not recommended ad length |
| Cards | 2–10 | Technical count where applicable |

1% tolerance; image format documented. Catalog variation uses horizontally swipeable product thumbnails; exact recommended canvas unclear.

## META-041

**Facebook Marketplace · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/carousel/facebook-marketplace) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG; MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/20 | Recommendation, unless verified otherwise |
| Maximum file size | Image 30 MB; video 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | Video 1 second–240 minutes | Source upload/playback rule as labeled; not recommended ad length |
| Cards | 2–10 | Technical count where applicable |

3% tolerance; URL required.

## META-042

**Facebook Search Results · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/carousel/facebook-search) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG; MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/20 | Recommendation, unless verified otherwise |
| Maximum file size | Image 30 MB; video 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | Video 1 second–240 minutes | Source upload/playback rule as labeled; not recommended ad length |
| Cards | 2–10 | Technical count where applicable |

3% tolerance; URL required.

## META-043

**Facebook Business Explore · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/carousel/facebook-biz-disco-feed) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG; MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/32/18 | Recommendation, unless verified otherwise |
| Maximum file size | Image 30 MB; video 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | Video 1 second–240 minutes | Source upload/playback rule as labeled; not recommended ad length |
| Cards | 2–10 | Technical count where applicable |

3% tolerance; URL required.

## META-044

**Instagram Explore home · SOURCE_ISSUE**

[Meta source](https://www.facebook.com/business/ads-guide/update/carousel/instagram-explore-home) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 4:5 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1080 x 1080 (source wording) | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/— | Recommendation, unless verified otherwise |
| Maximum file size | Image 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 500w | Technical requirement when published |
| Duration | Video specs absent | Source upload/playback rule as labeled; not recommended ad length |
| Cards | 2–10 | Technical count where applicable |

1% tolerance; URL required. Description mentions video but specs list only images. Ratio/resolution conflict; verify before exporting.

## META-045

**Facebook Right Column · SOURCE_ISSUE**

[Meta source](https://www.facebook.com/business/ads-guide/update/carousel/facebook-right-hand-column) · checked 2026-09-12 · account availability NOT TESTED.

Context: Traffic / Website; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG; MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | —/40/— | Recommendation, unless verified otherwise |
| Maximum file size | Image 30 MB; video 4 GB (source) | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | Video 1 second–240 minutes (source) | Source upload/playback rule as labeled; not recommended ad length |
| Cards | 2–10 | Technical count where applicable |

3% tolerance; URL required. Video specs in this entry do not independently establish current Right Column video delivery.

## META-046

**Facebook In-Stream Video · QUARANTINED**

[Meta source](https://www.facebook.com/business/ads-guide/update/carousel/facebook-instream-video) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/30 | Recommendation, unless verified otherwise |
| Maximum file size | Image 4 GB; video 4 GB (source) | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 600w x 600h | Technical requirement when published |
| Duration | Video up to 15 seconds | Source upload/playback rule as labeled; not recommended ad length |
| Cards | Source says 10 | Technical count where applicable |

QUARANTINE: anomalous image 4 GB cap and ambiguous card count. Reconfirm specs; do not use this image cap for exports.

## META-047

**Facebook video feeds ads · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/carousel/facebook-video-feeds) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG; MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 80/20/18 | Recommendation, unless verified otherwise |
| Maximum file size | Image 30 MB; video 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | Video 1 second–240 minutes | Source upload/playback rule as labeled; not recommended ad length |
| Cards | 2–10 | Technical count where applicable |

3% tolerance; URL required. Legacy-labeled entry; account availability untested.

## META-048

**Ads on Facebook Reels (overlay) · SOURCE_ISSUE**

[Meta source](https://www.facebook.com/business/ads-guide/update/carousel/facebook-facebook-reels-overlay) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 60/10/— | Recommendation, unless verified otherwise |
| Maximum file size | Image 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 600w x 600h | Technical requirement when published |
| Duration | Video not specified | Source upload/playback rule as labeled; not recommended ad length |
| Cards | Source says 10 | Technical count where applicable |

3% tolerance; no minimum card count stated. Do not infer one; distinguish overlay from fullscreen Reels.

## META-049

**Audience Network Native, Banner and Interstitial · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/carousel/audience-network-native) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG; MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/20 | Recommendation, unless verified otherwise |
| Maximum file size | Image 30 MB; video 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | Video 1–240 seconds | Source upload/playback rule as labeled; not recommended ad length |
| Cards | 2–10 | Technical count where applicable |

URL required. Duration is seconds, not the Facebook carousel minutes limit.

## META-050

**Audience Network Rewarded Video · QUARANTINED**

[Meta source](https://www.facebook.com/business/ads-guide/update/carousel/audience-network-rewarded-video) · checked 2026-09-12 · account availability NOT TESTED.

Context: Traffic / Website; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG; MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 80/20/18 | Recommendation, unless verified otherwise |
| Maximum file size | Image 30 MB; video 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | Video 1 second–240 minutes (source) | Source upload/playback rule as labeled; not recommended ad length |
| Cards | 2–10 | Technical count where applicable |

QUARANTINE: Facebook Feed carousel fallback description; current eligibility not established.

## META-051

**Messenger Stories · QUARANTINED**

[Meta source](https://www.facebook.com/business/ads-guide/update/carousel/messenger-story) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG; MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 80/20/18 | Recommendation, unless verified otherwise |
| Maximum file size | Image 30 MB; video 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | Video 1 second–240 minutes (source) | Source upload/playback rule as labeled; not recommended ad length |
| Cards | 2–10 | Technical count where applicable |

QUARANTINE: Facebook Feed carousel fallback description; current eligibility not established.

## META-052

**Facebook Groups Feed · QUARANTINED**

[Meta source](https://www.facebook.com/business/ads-guide/update/carousel/facebook-groups-feed) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG; MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 80/20/18 | Recommendation, unless verified otherwise |
| Maximum file size | Image 30 MB; video 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | Video 1 second–240 minutes (source) | Source upload/playback rule as labeled; not recommended ad length |
| Cards | 2–10 | Technical count where applicable |

QUARANTINE: Facebook Feed carousel fallback description on legacy-labeled route; current eligibility unconfirmed.

## META-063

**Threads Feed · SOURCE_ISSUE**

[Meta source](https://www.facebook.com/business/help/655859553779869) · checked 2026-09-12 · account availability NOT TESTED.

Context: Help-center format guidance; consult conversion-location compatibility table.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 1.91:1–9:16 supported; source says outside 4:5 center-cropped to 4:5 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 1440 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 80–160/40/— | Recommendation, unless verified otherwise |
| Maximum file size | Not published in inspected section | Technical requirement when published; quarantine overrides |
| Minimum dimensions | No min/max resolution per source | Technical requirement when published |
| Duration | Video not supported | Source upload/playback rule as labeled; not recommended ad length |
| Cards | 2–10 | Technical count where applicable |

Images only; landing URL required. Crop wording differs from single-image guidance; confirm preview.

## META-066

**WhatsApp Status · DOCUMENTED**

[Meta source](https://www.facebook.com/business/help/723817683917948) · checked 2026-09-12 · account availability NOT TESTED.

Context: Help-center format guidance; consult conversion-location compatibility table.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 9:16 recommended; source accepts aspect ratio smaller than 1.91:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 720 x 1280 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | —/—/— | Recommendation, unless verified otherwise |
| Maximum file size | Not published in inspected section | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 500w x 320h | Technical requirement when published |
| Duration | Video not supported | Source upload/playback rule as labeled; not recommended ad length |
| Cards | 2–10 | Technical count where applicable |

Images only. Rollout/country-dependent; file-size cap unpublished here.
