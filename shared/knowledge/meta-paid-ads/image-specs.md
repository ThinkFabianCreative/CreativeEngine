# Image specifications

Checked 2026-09-12. Public Meta documentation, not account validation. Read [usage and evidence rules](README.md) and [source conflicts](source-conflicts.md) before production.

Recommendations are distinct from technical requirements. A dash means not specified in the inspected entry, never zero or unlimited. Text values are primary/headline/description character recommendations, not automatically hard limits. Guide entries use the observed objective/context shown in each record; inspect the actual objective and conversion location before launch.

| ID | Placement | Recommended ratio | Recommended pixels | Status |
|---|---|---|---|---|
| [META-001](#meta-001) | Facebook Feed | 4:5 | 1440 x 1800 | DOCUMENTED |
| [META-002](#meta-002) | Instagram Feed | 4:5 | 1440 x 1800 | DOCUMENTED |
| [META-003](#meta-003) | Facebook Stories | 9:16 | 1440 x 2560 | DOCUMENTED |
| [META-004](#meta-004) | Instagram Stories | 9:16 | 1440 x 2560 | DOCUMENTED |
| [META-005](#meta-005) | Instagram Reels | 9:16 | 1440 x 2560 | DOCUMENTED |
| [META-006](#meta-006) | Facebook Reels | 9:16 | 1440 x 2560 | SOURCE_ISSUE |
| [META-007](#meta-007) | Facebook Marketplace | 1:1 | At least 1080 x 1080 | DOCUMENTED |
| [META-008](#meta-008) | Facebook Right Column | 1:1 | At least 1080 x 1080 | DOCUMENTED |
| [META-009](#meta-009) | Instagram Explore home | 4:5 | 1440 x 1800 | DOCUMENTED |
| [META-010](#meta-010) | Facebook Search Results | 1.91:1 to 1:1 | At least 1080 x 1080 | DOCUMENTED |
| [META-011](#meta-011) | Facebook Business Explore | 1.91:1 to 1:1 | At least 1080 x 1080 | DOCUMENTED |
| [META-012](#meta-012) | Messenger Stories | 9:16 | At least 1080 x 1080 (source wording) | SOURCE_ISSUE |
| [META-013](#meta-013) | Ads on Facebook Reels (overlay) | 1:1 | At least 1080 x 1080 | DOCUMENTED |
| [META-014](#meta-014) | Facebook In-Stream Video | 1.91:1 to 1:1 | At least 1080 x 1080 | DOCUMENTED |
| [META-015](#meta-015) | Facebook video feeds ads | 1.91:1 to 4:5 | 1440 x 1440 at 1:1; 1440 x 1800 at 4:5 | DOCUMENTED |
| [META-016](#meta-016) | Audience Network Native, Banner and Interstitial | 9:16 | At least 398 x 208 (source wording) | SOURCE_ISSUE |
| [META-017](#meta-017) | Audience Network Rewarded Video | 4:5 | 1440 x 1800 | QUARANTINED |
| [META-061](#meta-061) | Threads Feed | 1.91:1–9:16 supported; taller than 4:5 center-cropped to 4:5 | 1440 x 1440 | DOCUMENTED |
| [META-064](#meta-064) | WhatsApp Status | Native surface 9:16; source accepts aspect ratio smaller than 1.91:1 | 720 x 1280 | DOCUMENTED |

## META-001

**Facebook Feed · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/image) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 4:5 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 1800 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 50–150/27/— | Recommendation, unless verified otherwise |
| Maximum file size | 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 600w; 750h at 4:5 | Technical requirement when published |
| Duration | — | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

3% ratio tolerance.

## META-002

**Instagram Feed · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/image/instagram-feed) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 4:5 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 1800 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/— | Recommendation, unless verified otherwise |
| Maximum file size | 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 500w | Technical requirement when published |
| Duration | — | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

Supported ratio bounds 400:500 to 191:100; 1% tolerance; hashtags 30 in text recommendations.

## META-003

**Facebook Stories · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/image/facebook-story) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 9:16 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 2560 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/— | Recommendation, unless verified otherwise |
| Maximum file size | 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 500w | Technical requirement when published |
| Duration | Display: 8 seconds or swipe | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

1% tolerance; safe zone 14% top / 35% bottom / 6% sides.

## META-004

**Instagram Stories · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/image/instagram-story) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 9:16 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 2560 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/—/— | Recommendation, unless verified otherwise |
| Maximum file size | 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 500w | Technical requirement when published |
| Duration | Display: 5–16 seconds or swipe | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

1% tolerance; safe zone 14% top / 35% bottom / 6% sides.

## META-005

**Instagram Reels · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/image/instagram-reels) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 9:16 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 2560 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 44/—/— | Recommendation, unless verified otherwise |
| Maximum file size | 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 500w | Technical requirement when published |
| Duration | — | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

1% tolerance; safe zone 14% top / 35% bottom / 6% sides.

## META-006

**Facebook Reels · SOURCE_ISSUE**

[Meta source](https://www.facebook.com/business/ads-guide/update/image/facebook-facebook-reels) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 9:16 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 2560 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 40/55/— | Recommendation, unless verified otherwise |
| Maximum file size | 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 600w x 600h | Technical requirement when published |
| Duration | — | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

3% tolerance. Page contains small-image/no-text advice despite fullscreen dimensions; preview treatment.

## META-007

**Facebook Marketplace · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/image/facebook-marketplace) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/30 | Recommendation, unless verified otherwise |
| Maximum file size | 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | — | Technical requirement when published |
| Duration | — | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

Do not import an unpublished minimum from another placement.

## META-008

**Facebook Right Column · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/image/facebook-right-hand-column) · checked 2026-09-12 · account availability NOT TESTED.

Context: Traffic / Website; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | —/40/— | Recommendation, unless verified otherwise |
| Maximum file size | — | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 254w x 133h | Technical requirement when published |
| Duration | — | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

Meta discourages image text for the small display. File-size cap not listed in this entry.

## META-009

**Instagram Explore home · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/image/instagram-explore-home) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 4:5 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 1800 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/— | Recommendation, unless verified otherwise |
| Maximum file size | 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 500w | Technical requirement when published |
| Duration | — | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

Supported ratio bounds 400:500 to 191:100; 1% tolerance; hashtags 30 in text recommendations.

## META-010

**Facebook Search Results · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/image/facebook-search) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 1.91:1 to 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/30 | Recommendation, unless verified otherwise |
| Maximum file size | 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 600w x 600h | Technical requirement when published |
| Duration | — | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

3% tolerance. Choose dimensions consistent with actual selected ratio.

## META-011

**Facebook Business Explore · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/image/facebook-biz-disco-feed) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 1.91:1 to 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/27/27 | Recommendation, unless verified otherwise |
| Maximum file size | 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 600w x 600h | Technical requirement when published |
| Duration | — | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

3% tolerance; current account placement availability untested.

## META-012

**Messenger Stories · SOURCE_ISSUE**

[Meta source](https://www.facebook.com/business/ads-guide/update/image/messenger-story) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 9:16 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 (source wording) | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/— | Recommendation, unless verified otherwise |
| Maximum file size | 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 500w | Technical requirement when published |
| Duration | — | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

1% tolerance. Ratio and listed resolution do not specify a coherent exact canvas; see conflicts. Source safe-zone percentages 14% top / 20% bottom.

## META-013

**Ads on Facebook Reels (overlay) · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/image/facebook-facebook-reels-overlay) · checked 2026-09-12 · account availability NOT TESTED.

Context: Traffic / Website; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 60/10/— | Recommendation, unless verified otherwise |
| Maximum file size | 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 300w x 300h | Technical requirement when published |
| Duration | — | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

0% tolerance. Distinct from fullscreen Facebook Reels; confirm current delivery.

## META-014

**Facebook In-Stream Video · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/image/facebook-instream-video) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 1.91:1 to 1:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 1080 x 1080 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/30 | Recommendation, unless verified otherwise |
| Maximum file size | 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 600w x 600h | Technical requirement when published |
| Duration | — | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

3% tolerance. Current availability of legacy-labeled placement untested.

## META-015

**Facebook video feeds ads · DOCUMENTED**

[Meta source](https://www.facebook.com/business/ads-guide/update/image/facebook-video-feeds) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 1.91:1 to 4:5 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 1440 at 1:1; 1440 x 1800 at 4:5 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 50–150/27/— | Recommendation, unless verified otherwise |
| Maximum file size | 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 600w; 600h at 1:1 / 750h at 4:5 | Technical requirement when published |
| Duration | — | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

3% tolerance. Legacy-labeled menu entry; current delivery untested.

## META-016

**Audience Network Native, Banner and Interstitial · SOURCE_ISSUE**

[Meta source](https://www.facebook.com/business/ads-guide/update/image/audience-network-native) · checked 2026-09-12 · account availability NOT TESTED.

Context: Awareness / On your ad; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 9:16 | Recommendation unless explicitly described as supported/cropped |
| Resolution | At least 398 x 208 (source wording) | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 125/40/30 | Recommendation, unless verified otherwise |
| Maximum file size | 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 398w x 208h | Technical requirement when published |
| Duration | — | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

Grouped placement with conflicting ratio/resolution; do not convert into one universal banner canvas.

## META-017

**Audience Network Rewarded Video · QUARANTINED**

[Meta source](https://www.facebook.com/business/ads-guide/update/image/audience-network-rewarded-video) · checked 2026-09-12 · account availability NOT TESTED.

Context: Traffic / Website; observed selection, not all variants audited.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 4:5 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 1800 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 50–150/27/— | Recommendation, unless verified otherwise |
| Maximum file size | 30 MB | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 600w; 750h at 4:5 | Technical requirement when published |
| Duration | — | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

QUARANTINE: description and numbers repeat Facebook Feed despite Rewarded Video heading. Not proof that a standalone image is eligible.

## META-061

**Threads Feed · DOCUMENTED**

[Meta source](https://www.facebook.com/business/help/655859553779869) · checked 2026-09-12 · account availability NOT TESTED.

Context: Help-center format guidance; consult conversion-location compatibility table.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | 1.91:1–9:16 supported; taller than 4:5 center-cropped to 4:5 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 1440 x 1440 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | 80–160/40/— | Recommendation, unless verified otherwise |
| Maximum file size | Not published in inspected section | Technical requirement when published; quarantine overrides |
| Minimum dimensions | No min/max resolution per source | Technical requirement when published |
| Duration | — | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

URLs unsupported in primary text; verify CTA rendering. File-size limit not published in inspected section.

## META-064

**WhatsApp Status · DOCUMENTED**

[Meta source](https://www.facebook.com/business/help/723817683917948) · checked 2026-09-12 · account availability NOT TESTED.

Context: Help-center format guidance; consult conversion-location compatibility table.

| Field | Documented value | Classification |
|---|---|---|
| File types | JPG/PNG | Source design guidance; exclusions still apply |
| Ratio | Native surface 9:16; source accepts aspect ratio smaller than 1.91:1 | Recommendation unless explicitly described as supported/cropped |
| Resolution | 720 x 1280 | Design recommendation; not a universal rejection threshold |
| Text: primary / headline / description | —/—/— | Recommendation, unless verified otherwise |
| Maximum file size | Not published in inspected section | Technical requirement when published; quarantine overrides |
| Minimum dimensions | 500w x 320h | Technical requirement when published |
| Duration | — | Source upload/playback rule as labeled; not recommended ad length |
| Cards | — | Technical count where applicable |

Rollout/country-dependent. Do not import Instagram limits; file-size cap unpublished here.
