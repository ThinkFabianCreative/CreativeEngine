# Video specifications

Checked 2026-09-12. Public Meta documentation, not account validation. Read [usage and evidence rules](README.md) and [source conflicts](source-conflicts.md) before production.

Recommendations are distinct from technical requirements. A dash means not specified in the inspected entry, never zero or unlimited. Text values are primary/headline/description character recommendations, not automatically hard limits. Guide entries use the observed objective/context shown in each record; inspect the actual objective and conversion location before launch.

| ID | Placement | Recommended ratio | Recommended pixels | Status |
|---|---|---|---|---|
| [META-018](#meta-018) | Facebook Feed | 4:5 | 1440 x 1800 | DOCUMENTED |
| [META-019](#meta-019) | Instagram Feed | 9:16 | 1080 x 1920 | DOCUMENTED |
| [META-020](#meta-020) | Facebook Stories | 9:16 | 1440 x 2560 | DOCUMENTED |
| [META-021](#meta-021) | Instagram Stories | 9:16 | 1440 x 2560 | DOCUMENTED |
| [META-022](#meta-022) | Instagram Reels | 9:16 | 1440 x 2560 | SOURCE_ISSUE |
| [META-023](#meta-023) | Facebook Reels | 9:16 | 1440 x 2560 | SOURCE_ISSUE |
| [META-024](#meta-024) | Facebook In-Stream Video | 16:9 or 1:1 | At least 1080 x 1080 | DOCUMENTED |
| [META-025](#meta-025) | Facebook Marketplace | 1:1 | At least 1080 x 1080 | DOCUMENTED |
| [META-026](#meta-026) | Facebook Search Results | 1:1 | At least 1080 x 1080 | DOCUMENTED |
| [META-027](#meta-027) | Facebook Business Explore | 1:1 desktop/mobile; 4:5 mobile | At least 1080 x 1080 | DOCUMENTED |
| [META-028](#meta-028) | Audience Network Native, Banner and Interstitial | 9:16 | At least 1080 x 1080 | DOCUMENTED |
| [META-029](#meta-029) | Audience Network Rewarded Video | 9:16 | At least 1080 x 1080 | DOCUMENTED |
| [META-030](#meta-030) | Messenger Stories | 9:16 | 1080 x 1920 | DOCUMENTED |
| [META-031](#meta-031) | Instagram Explore home | 9:16 | 1080 x 1920 | DOCUMENTED |
| [META-032](#meta-032) | Ads on Facebook Reels (overlay) | 1:1 | 1440 x 1440 | DOCUMENTED |
| [META-033](#meta-033) | Facebook Right Column | 1:1 desktop/mobile; 4:5 mobile | 1440 x 1440 / 1440 x 1800 | QUARANTINED |
| [META-034](#meta-034) | Facebook Groups Feed | 1:1 desktop/mobile; 4:5 mobile | 1440 x 1440 / 1440 x 1800 | QUARANTINED |
| [META-062](#meta-062) | Threads Feed | 1.91:1–9:16 supported; taller than 4:5 center-cropped to 4:5 | 1440 x 1800 | DOCUMENTED |
| [META-065](#meta-065) | WhatsApp Status | Native surface 9:16; source accepts aspect ratio smaller than 1.91:1 | 720 x 1280 | DOCUMENTED |

## META-018

**Facebook Feed · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/video) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 4:5 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 1800 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 50–150/27/— | Recommendation, unless verified otherwise |
| Maximum file size | 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 120w x 120h | Technical requirement when published |
| Duration | 1 second–241 minutes | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

Do not confuse upload duration with a useful ad length. Mobile footer can be hidden by objective/performance-goal configuration; see production notes.

## META-019

**Instagram Feed · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/video/instagram-feed) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 9:16 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1080 x 1920 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/—/— | Recommendation, unless verified otherwise |
| Maximum file size | 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 250w | Technical requirement when published |
| Duration | 1 second–60 minutes | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

1% tolerance. Hashtags 30 in text recommendations. 9:16 uses Stories/Reels safe-zone guidance.

## META-020

**Facebook Stories · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/video/facebook-story) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 9:16 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 2560 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/— | Recommendation, unless verified otherwise |
| Maximum file size | 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 250w | Technical requirement when published |
| Duration | 1 second–3 minutes | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

1% tolerance. Source says 14% top / 20% bottom, unlike Facebook image Stories; preview current safe-zone overlay.

## META-021

**Instagram Stories · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/video/instagram-story) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 9:16 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 2560 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/—/— | Recommendation, unless verified otherwise |
| Maximum file size | 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 250w | Technical requirement when published |
| Duration | 1 second–60 minutes | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

1% tolerance; safe zone 14% top / 35% bottom / 6% sides. Upload length is not guaranteed uninterrupted display.

## META-022

**Instagram Reels · SOURCE_ISSUE**

[Meta source](https://www.facebook.com/business/ads-guide/update/video/instagram-reels) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV | Source design guidance; exclusions still apply |
| Ratio | 9:16 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 2560 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 44/—/— | Recommendation, unless verified otherwise |
| Maximum file size | 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 250w under 30 seconds; 500w at 30 seconds or longer | Technical requirement when published |
| Duration | Source: 0 seconds–15 minutes | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

MP4/MOV only in this entry; 0-second lower bound is anomalous, not a usable export. Safe zone 14% top / 35% bottom / 6% sides. Additional restrictions in video notes.

## META-023

**Facebook Reels · SOURCE_ISSUE**

[Meta source](https://www.facebook.com/business/ads-guide/update/video/facebook-facebook-reels) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 9:16 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 2560 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 40/55/— | Recommendation, unless verified otherwise |
| Maximum file size | 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | Source: no maximum duration | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

Do not interpret duration wording as a universal account guarantee. Source says no auto-captioning; captions optional/recommended.

## META-024

**Facebook In-Stream Video · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/video/facebook-instream-video) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 16:9 or 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/— | Recommendation, unless verified otherwise |
| Maximum file size | 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | Desktop 5–15 seconds; mobile 5 seconds–10 minutes; varies by objective | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

Source describes truncation after first 15 seconds for longer ads and possible skip after 5 seconds. Confirm current placement and format treatment.

## META-025

**Facebook Marketplace · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/video/facebook-marketplace) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | —/25/— | Recommendation, unless verified otherwise |
| Maximum file size | 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 120w x 120h | Technical requirement when published |
| Duration | 1 second–241 minutes | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

Primary text is not specified in this inspected entry.

## META-026

**Facebook Search Results · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/video/facebook-search) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/30 | Recommendation, unless verified otherwise |
| Maximum file size | 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 120w x 120h | Technical requirement when published |
| Duration | 1 second–241 minutes | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

Long upload allowance is not a creative recommendation.

## META-027

**Facebook Business Explore · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/video/facebook-biz-disco-feed) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 1:1 desktop/mobile; 4:5 mobile | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/27/27 | Recommendation, unless verified otherwise |
| Maximum file size | 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 120w x 120h | Technical requirement when published |
| Duration | 1 second–241 minutes | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

Actual account availability untested.

## META-028

**Audience Network Native, Banner and Interstitial · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/video/audience-network-native) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 9:16 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/30 | Recommendation, unless verified otherwise |
| Maximum file size | 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | 1 second–2 minutes | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

Caption tracks not supported per page. Grouped placements; verify actual rendering.

## META-029

**Audience Network Rewarded Video · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/video/audience-network-rewarded-video) · checked 2026-09-12 · account availability NOT TESTED.

Context: Traffic / Website; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 9:16 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/30 | Recommendation, unless verified otherwise |
| Maximum file size | 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | 3–61 seconds | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

Caption tracks not supported per page; do not replace 61 with a remembered 60-second limit.

## META-030

**Messenger Stories · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/video/messenger-story) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 9:16 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1080 x 1920 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/— | Recommendation, unless verified otherwise |
| Maximum file size | 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 500w | Technical requirement when published |
| Duration | 1–60 seconds | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

1% tolerance. Source recommends 14% top and bottom, with approximate pixel examples; use live preview.

## META-031

**Instagram Explore home · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/video/instagram-explore-home) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 9:16 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1080 x 1920 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/—/— | Recommendation, unless verified otherwise |
| Maximum file size | 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 250w | Technical requirement when published |
| Duration | 1 second–60 minutes | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

1% tolerance.

## META-032

**Ads on Facebook Reels (overlay) · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/video/facebook-facebook-reels-overlay) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV | Source design guidance; exclusions still apply |
| Ratio | 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 1440 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 60/—/— | Recommendation, unless verified otherwise |
| Maximum file size | 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | 4–15 seconds | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

MP4/MOV only in this entry; distinct from fullscreen Reels; confirm current availability.

## META-033

**Facebook Right Column · QUARANTINED**

[Meta source](https://www.facebook.com/business/ads-guide/update/video/facebook-right-hand-column) · checked 2026-09-12 · account availability NOT TESTED.

Context: Traffic / Website; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 1:1 desktop/mobile; 4:5 mobile | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 1440 / 1440 x 1800 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 50–150/27/— | Recommendation, unless verified otherwise |
| Maximum file size | 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 120w x 120h | Technical requirement when published |
| Duration | 1 second–241 minutes | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

QUARANTINE: Feed-style description, mobile wording and 360-video section on Right Column route; not confirmed video eligibility.

## META-034

**Facebook Groups Feed · QUARANTINED**

[Meta source](https://www.facebook.com/business/ads-guide/update/video/facebook-groups-feed) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 1:1 desktop/mobile; 4:5 mobile | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 1440 / 1440 x 1800 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 50–150/27/— | Recommendation, unless verified otherwise |
| Maximum file size | 4 GB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 120w x 120h | Technical requirement when published |
| Duration | 1 second–241 minutes | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

QUARANTINE: Feed-style fallback content on legacy-labeled Groups route; current availability unconfirmed.

## META-062

**Threads Feed · DOCUMENTED**

[Meta source](https://www.facebook.com/business/help/655859553779869) · checked 2026-09-12 · account availability NOT TESTED.

Context: Help-center format guidance; consult conversion-location compatibility table.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | 1.91:1–9:16 supported; taller than 4:5 center-cropped to 4:5 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 1800 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 80–160/40/— | Recommendation, unless verified otherwise |
| Maximum file size | Not published in inspected section | Technical requirement when published; quarantine overrides |
| Minimum dimensions | No min/max resolution per source | Technical requirement when published |
| Duration | Not published | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

Caption tracks not supported. Source image section contains a video CTA non-rendering statement; preview rather than rely on CTA visibility.

## META-065

**WhatsApp Status · DOCUMENTED**

[Meta source](https://www.facebook.com/business/help/723817683917948) · checked 2026-09-12 · account availability NOT TESTED.

Context: Help-center format guidance; consult conversion-location compatibility table.

| Field | Documented value | Classification |
|---|---|---|
| File types | MP4/MOV/GIF | Source design guidance; exclusions still apply |
| Ratio | Native surface 9:16; source accepts aspect ratio smaller than 1.91:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 720 x 1280 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | —/—/— | Recommendation, unless verified otherwise |
| Maximum file size | Not published in inspected section | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 120w x 120h | Technical requirement when published |
| Duration | Not published | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

Rollout/country-dependent; captions not supported; duration and file-size cap unpublished here.
