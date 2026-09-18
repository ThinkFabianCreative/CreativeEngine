# Google Ads and YouTube ad specifications

Checked 2026-09-16. Public Google Ads Help, YouTube Help and Advertising Policies pages, not account validation. Read [usage rules](README.md) and [source conflicts](source-conflicts.md) before production.

A dash means not published in the inspected page, never zero or unlimited. **Requirement** means the page labels it required, states a hard maximum/minimum, or it is a policy rule. **Recommendation** means Google labels it recommended, preferred or best practice. Character counts: in Chinese, Japanese and Korean each character counts as 2 where the source says so.

| ID | Campaign type | Format | Status |
|---|---|---|---|
| [GOOG-001](#goog-001) | Search | Responsive search ad | SOURCE_ISSUE |
| [GOOG-002](#goog-002) | Display | Responsive display ad | SOURCE_ISSUE |
| [GOOG-003](#goog-003) | Performance Max | Asset group | SOURCE_ISSUE |
| [GOOG-004](#goog-004) | Demand Gen | Single image ad | SOURCE_ISSUE |
| [GOOG-005](#goog-005) | Demand Gen | Carousel ad | DOCUMENTED |
| [GOOG-006](#goog-006) | Demand Gen | Video ad | SOURCE_ISSUE |
| [YT-001](#yt-001) | All YouTube video ads | Video file, thumbnail, companion banner | DOCUMENTED |
| [YT-002](#yt-002) | Video | Skippable in-stream | DOCUMENTED |
| [YT-003](#yt-003) | Video | Non-skippable in-stream | SOURCE_ISSUE |
| [YT-004](#yt-004) | Video | Bumper | DOCUMENTED |
| [YT-005](#yt-005) | Video | In-feed video ad | SOURCE_ISSUE |
| [YT-006](#yt-006) | Several | YouTube Shorts ad | DOCUMENTED |
| [YT-007](#yt-007) | Video reach | Video ad text fields | DOCUMENTED |
| [YT-008](#yt-008) | Masthead | Masthead | DOCUMENTED |

Google now publishes one "specs and format requirements" page per campaign type, indexed from the [specs hub](https://support.google.com/google-ads/answer/13676244). Use those pages first, then the older "About ... assets" pages for detail.

---

## Search

### GOOG-001

**Responsive search ad · SOURCE_ISSUE**

[About responsive search ads](https://support.google.com/google-ads/answer/7684791) · [Search campaigns specs](https://support.google.com/google-ads/answer/17092074) · checked 2026-09-16 · account availability NOT_TESTED.

| Field | Value | Classification |
|---|---|---|
| Headlines | Min 3, max 15; 30 characters each | Requirement (spec page shows 1–15; see conflicts) |
| Descriptions | Min 2, max 4; 90 characters each | Requirement (spec page shows 1–4) |
| Display path | 2 fields, 15 characters each | Requirement (limit) |
| Final URL | 1; 2,048 characters | Requirement (limit) |
| Double-width languages | Each CJK character counts as 2 | Requirement |
| What serves | Up to 3 headlines and 2 descriptions; headline 3 and description 2 not guaranteed | Platform behavior |
| Pinning | Not recommended for most advertisers; if used, pin 2–3 assets per position | Recommendation |
| Ads per ad group | At least 2 RSAs with Good or Excellent Ad Strength | Recommendation |
| Business name / logo (Search business information) | Name 25 characters; logo 1:1, recommended 1200 × 1200, min 128 × 128 | Requirement (limits) |
| Image assets (Search) | 1:1 rec 1200 × 1200, min 300 × 300; 1.91:1 rec 1200 × 628, min 600 × 314; up to 20 | Requirement (minimums) |

---

## Display

### GOOG-002

**Responsive display ad · SOURCE_ISSUE**

[RDA specs](https://support.google.com/google-ads/answer/17090561) · [Create an RDA](https://support.google.com/google-ads/answer/7005917) · [RDA best practices](https://support.google.com/google-ads/answer/9823397) · [Image asset policy](https://support.google.com/adspolicy/answer/10347108) · checked 2026-09-16 · account availability NOT_TESTED.

| Field | Value | Classification |
|---|---|---|
| Headlines | 1–5; 30 characters | Requirement |
| Long headline | 1; 90 characters | Requirement |
| Descriptions | 1–5; 90 characters | Requirement |
| Business name | 1; 25 characters | Requirement |
| Call to action | Automated, or selected | Requirement (field) |
| Landscape image 1.91:1 | 1–15; rec 1200 × 628; min 600 × 314 | Min size and ratio: requirement; 1200 × 628: recommendation |
| Square image 1:1 | 1–15; rec 1200 × 1200 (spec page says 600 × 600); min 300 × 300 | Min: requirement; recommended size: SOURCE_ISSUE |
| Vertical image 9:16 | Optional, up to 15; rec 900 × 1600; min 600 × 1067 | Best-practices page only |
| Images per ratio | 5–10 | Recommendation |
| Square logo 1:1 | Optional, up to 5; rec 1200 × 1200; min 128 × 128 | Min: requirement |
| Landscape logo 4:1 | Optional, up to 5; rec 1200 × 300; min 512 × 128 | Min: requirement |
| Image file size | 5120 KB max | Requirement |
| Image file types | JPG, PNG | Requirement |
| Text or logo overlays on image assets | Not permitted (PMax exception) | Requirement (policy) |
| Safe area | Important content in center 80% | Recommendation |
| Videos | Optional; up to 5 per orientation (16:9, 1:1, vertical); 30 s preferred | Recommendation |

---

## Performance Max

### GOOG-003

**Asset group · SOURCE_ISSUE**

[PMax specs](https://support.google.com/google-ads/answer/17091269) · [Text assets](https://support.google.com/google-ads/answer/14528373) · [Image assets](https://support.google.com/google-ads/answer/14530211) · [Video assets](https://support.google.com/google-ads/answer/14528532) · checked 2026-09-16 · account availability NOT_TESTED.

| Field | Value | Classification |
|---|---|---|
| Headlines | Min 3, max 15; 30 characters; at least 1 of 15 characters or fewer; 11+ recommended | Count and limits: requirement; 11+: recommendation |
| Long headlines | Min 1, max 5; 90 characters | Requirement |
| Descriptions | Min 2, max 5; 90 characters; 4+ recommended | Requirement; 4+: recommendation |
| Short description (60 characters) | — (not found in official pages) | UNVERIFIED |
| Business name | 1; 25 characters; must match domain or legally verified name | Requirement |
| Call to action | 1; automated or selected | Requirement |
| Display path | Optional, 2 × 15 characters | Requirement (limit) |
| Double-width languages | Each CJK character counts as 2 | Requirement |
| Landscape image 1.91:1 | Required; 4+ recommended, up to 20; rec 1200 × 628; min 600 × 314 | Min size: requirement |
| Square image 1:1 | Required; 4+ recommended, up to 20; rec 1200 × 1200; min 300 × 300 | Min size: requirement |
| Portrait image 4:5 | Optional; 2+ recommended, up to 20; rec 960 × 1200; min 480 × 600 | Min size: requirement |
| Square logo 1:1 | Required; 1 recommended, up to 5; rec 1200 × 1200; min 128 × 128 | Requirement |
| Landscape logo 4:1 | Optional; up to 5; rec 1200 × 300; min 512 × 128 | Min: requirement |
| Image file size / types | 5 MB (5120 KB); JPG, PNG | Requirement |
| Safe area | Center 80% of image | Recommendation |
| Overlays | Allowed in PMax; keep at least one image without overlays per ratio | Recommendation |
| Videos | Optional; 16:9, 1:1, 9:16; min 10 s; up to 15; 1 per orientation recommended | Min length: requirement |
| Vertical video | At least one 9:16 of 10–60 s for Shorts | Recommendation |
| Auto-generated video | Google may generate video when none is supplied | Platform behavior |
| Video file | MPG recommended; ≤ 256 GB; 1080p recommended | See YT-001 |

The minimum image count needed to publish is marked required but not given as a number; the "4+" is in the Recommended column.

---

## Demand Gen

Video action campaigns were upgraded to Demand Gen as of May 2026 ([source](https://support.google.com/google-ads/answer/10147229)). Demand Gen serves on YouTube (in-stream, in-feed, Shorts), Discover, Gmail and the Google Display Network.

### GOOG-004

**Single image ad · SOURCE_ISSUE**

[Demand Gen image assets](https://support.google.com/google-ads/answer/17140672) · [Demand Gen specs](https://support.google.com/google-ads/answer/17091672) · [Demand Gen creative](https://support.google.com/google-ads/answer/13704860) · checked 2026-09-16 · account availability NOT_TESTED.

| Field | Value | Classification |
|---|---|---|
| Headlines | 1–5; 40 characters; at least one of 30 characters or fewer | Limits: requirement; ≤30 rule avoids "Incomplete" Ad Strength |
| Descriptions | 1–5; 90 characters; 3 recommended | Limit: requirement |
| Business name | 1; 25 characters | Requirement |
| Call to action | Automated | Requirement (field) |
| Final URL | 2,048 characters | Requirement |
| Landscape 1.91:1 | Up to 20; rec 1200 × 628; min 600 × 314 | Min: requirement |
| Square 1:1 | Up to 20; rec 1200 × 1200; min 300 × 300 | Min: requirement |
| Portrait 4:5 | Up to 20; rec 960 × 1200; min 480 × 600 | Min: requirement |
| Vertical 9:16 | rec 1080 × 1920; min 600 × 1067; recommended for Shorts | Min: requirement |
| Images per ratio | 3 | Recommendation |
| Square logo 1:1 | Required; up to 5; rec 1200 × 1200; min 144 × 144 (128 × 128 on video page) | SOURCE_ISSUE |
| Image file size / types | 5 MB; JPG, PNG | Requirement |
| Logo file size | 150 KB | Requirement |
| Gmail logo crop | About 21.46% cropped when shown as a circle | Platform behavior |

### GOOG-005

**Carousel ad · DOCUMENTED**

[Demand Gen image assets](https://support.google.com/google-ads/answer/17140672) · checked 2026-09-16 · account availability NOT_TESTED.

| Field | Value | Classification |
|---|---|---|
| Cards | 2–10; one image per card; same aspect ratio across cards | Requirement |
| Ad headline | 1; 40 characters | Requirement |
| Ad description | 1; 40 characters | Requirement |
| Card headline | 40 characters per card | Requirement |
| Business name | 25 characters | Requirement |
| Logo | 1:1; rec 1200 × 1200; min 144 × 144; 150 KB | Requirement |
| Card images | Ratios and sizes as GOOG-004; 5 MB | Requirement |

### GOOG-006

**Video ad · SOURCE_ISSUE**

[Demand Gen video assets](https://support.google.com/google-ads/answer/17141078) · [Demand Gen specs](https://support.google.com/google-ads/answer/17091672) · checked 2026-09-16 · account availability NOT_TESTED.

| Field | Value | Classification |
|---|---|---|
| Headlines | 40 characters; 3+ unique | Limit: requirement; count: recommendation |
| Long headlines | 90 characters; 3+ unique | Limit: requirement |
| Descriptions | 90 characters; 3+ unique | Limit: requirement |
| Business name | 1; 25 characters | Requirement |
| Logo | 1:1; rec 1200 × 1200; min 128 × 128; 150 KB | Requirement |
| Video orientations | 16:9 1920 × 1080; 1:1 1080 × 1080; 4:5 1080 × 1350; 9:16 1080 × 1920 | Recommendation (HD) |
| Videos per orientation | 3 | Recommendation |
| Length | Min 5 s; under 10 s ineligible for in-stream; 15 s+ recommended (spec page: 10–60 s) | Min: requirement; ranges: recommendation |
| File | MPG recommended; ≤ 256 GB | Requirement (size) |

---

## YouTube video ads

### YT-001

**Video file, thumbnail and companion banner · DOCUMENTED**

[About video ad specs](https://support.google.com/google-ads/answer/13547298) · [Video ads specs](https://support.google.com/google-ads/answer/17091270) · [YouTube upload limits](https://support.google.com/youtube/answer/71673) · checked 2026-09-16 · account availability NOT_TESTED.

| Field | Value | Classification |
|---|---|---|
| Recommended file type | .MPG (MPEG-2 or MPEG-4) | Recommendation |
| Also accepted | WMV, AVI, MOV, FLV, MPEG-1, MP4, MPEGPS, 3GPP, WebM, DNxHR, ProRes, CineForm, HEVC (H.265) | Requirement (accepted list) |
| Not accepted | Audio-only files (MP3, WAV, PCM) | Requirement |
| Max file size | 256 GB (YouTube: 256 GB or 12 hours, whichever is less) | Requirement |
| Uploads over 15 minutes | Verified YouTube account | Requirement |
| Hosting | Public or unlisted YouTube video | Requirement |
| Recommended resolution (1080p) | 16:9 1920 × 1080; 9:16 1080 × 1920; 1:1 1080 × 1080 | Recommendation |
| Also accepted 720p | 1280 × 720; 720 × 1280; square 480 × 480 | Accepted |
| Also accepted SD (not recommended) | 640 × 480; 480 × 640; 480 × 480 | Accepted |
| Recommended ratios | 16:9, 9:16, 1:1 | Recommendation |
| Also accepted ratios | 4:3 (SD horizontal); 2:3 and 4:5 vertical | Accepted |
| Safe zones | Downloadable overlay templates; no numeric values in page text | Recommendation |
| Thumbnail | 16:9; rec 1280 × 720; min 1280 × 640; JPG/GIF/PNG; < 2 MB | Min: requirement |
| Companion banner | 300 × 60 (5:1); JPG/GIF/PNG; 150 KB max; desktop only | Requirement |

### YT-002

**Skippable in-stream · DOCUMENTED**

[About video ad formats](https://support.google.com/google-ads/answer/2375464) · checked 2026-09-16 · account availability NOT_TESTED.

| Field | Value | Classification |
|---|---|---|
| Maximum length | No maximum | Requirement (none published) |
| Recommended length | Under 3 minutes; 15 s on video spec page | Recommendation |
| Skip | After 5 seconds | Platform behavior |
| Where | YouTube watch pages, Google video partners | Platform behavior |
| Text fields | See YT-007 (video reach) or GOOG-006 (Demand Gen) | — |

### YT-003

**Non-skippable in-stream · SOURCE_ISSUE**

[About video ad formats](https://support.google.com/google-ads/answer/2375464) · [YouTube Help version](https://support.google.com/youtube/answer/2375464) · [Create a video reach campaign](https://support.google.com/google-ads/answer/10510238) · checked 2026-09-16 · account availability NOT_TESTED.

| Field | Value | Classification |
|---|---|---|
| Maximum length | 60 s or shorter (formats page); 15–60 s depending on subtype (YouTube Help) | Requirement, subtype-dependent |
| Video reach campaign lengths | 7–15 s; 30-second non-skippable on CTV: 16–30 s, horizontal only | Requirement per creation page |
| Skip | Not skippable | Platform behavior |

### YT-004

**Bumper · DOCUMENTED**

[About video ad formats](https://support.google.com/google-ads/answer/2375464) · checked 2026-09-16 · account availability NOT_TESTED.

| Field | Value | Classification |
|---|---|---|
| Length | 5–6 seconds (creation page: up to 6 s) | Requirement |
| Skip | Not skippable | Platform behavior |
| Ratio / resolution | 16:9 1920 × 1080 in efficient reach | Recommendation |

### YT-005

**In-feed video ad · SOURCE_ISSUE**

[In-feed video ads](https://support.google.com/google-ads/answer/6227733) · checked 2026-09-16 · account availability NOT_TESTED.

| Field | Value | Classification |
|---|---|---|
| Headline | 100 characters max; over 25 may be shortened on some devices | Limit: requirement |
| Description | 2 lines, 35 characters per line | Requirement |
| Thumbnail | 1 of 4 auto-selected frames or custom | Requirement (field) |
| Length | No maximum; 15–20 s for awareness, 2–3 min for consideration | Recommendation |
| Where | YouTube search, Watch Next, Home, Subscriptions | Platform behavior |

The video spec page lists in-video headlines as 2 lines of 40 characters. Text limits vary by campaign type (Demand Gen 40; video reach long headline 90).

### YT-006

**YouTube Shorts ad · DOCUMENTED**

[Shorts ads asset specs](https://support.google.com/google-ads/answer/16041697) · checked 2026-09-16 · account availability NOT_TESTED.

| Field | Value | Classification |
|---|---|---|
| Ratio | 9:16; horizontal serves with blurred edges | Requirement for full-screen rendering |
| Resolution | 1080 × 1920 (YT-001) | Recommendation |
| Length | Upload up to 3 minutes; under 60 s recommended; action 10–30 s; video reach 6–60 s; other types 10–60 s | Ranges: recommendation |
| Headline | 40 characters | Recommendation |
| Description | 90 characters | Recommendation |
| Truncation | More than 1 line on mobile, 2 on desktop/TV | Platform behavior |
| CTA timing | 3 s (PMax, App, Demand Gen); 10 s (video views, video reach) | Platform behavior |
| Safe zone | — (not in page text) | — |
| Skip | Swipe | Platform behavior |

### YT-007

**Video reach ad text fields · DOCUMENTED**

[Create a video reach campaign](https://support.google.com/google-ads/answer/10510238) · checked 2026-09-16 · account availability NOT_TESTED.

| Field | Value | Classification |
|---|---|---|
| Call to action | 10 characters | Requirement |
| CTA headline (optional) | 15 characters; accompanies the CTA | Requirement (limit) |
| Long headline | 90 characters; required for multi-format ads | Requirement |
| Description | 90 characters; required for multi-format ads | Requirement |
| Display URL | 255 characters | Requirement |
| Companion banner | Auto-generated from channel (recommended) or uploaded | Recommendation |
| Efficient reach lengths | 16:9: 15 s skippable/in-feed, 6 s bumper; 9:16 and 1:1: 6–60 s | Recommendation |

### YT-008

**Masthead · DOCUMENTED**

[Video ads specs](https://support.google.com/google-ads/answer/17091270) · checked 2026-09-16 · account availability NOT_TESTED.

| Field | Value | Classification |
|---|---|---|
| Video | 16:9, 1920 × 1080; any length; over 10 s recommended | Recommendation |
| Headline | 40 characters | Requirement (limit) |
| Description | 60 characters | Requirement (limit) |
| Call to action | 15 characters | Requirement (limit) |
