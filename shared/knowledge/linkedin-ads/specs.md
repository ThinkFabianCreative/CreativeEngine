# LinkedIn ad specifications

Checked 2026-09-16. Primary source: LinkedIn Marketing Solutions Help Center (linkedin.com/help/lms). The business.linkedin.com ads guide was compared and its differences recorded. Read [README](README.md) and [source conflicts](source-conflicts.md) before production.

Classifications: **REQUIREMENT** (stated as a limit or rule), **RECOMMENDATION** (stated as recommended, ideal or to avoid truncation), **PUBLISHED_LIMIT** (a value with no requirement/recommendation label), **PLATFORM_CLAIM** (performance marketing claim, not a spec), **SOURCE_NOTE** (context). A dash means not published in the inspected source.

| ID | Format | Placement | Status |
|---|---|---|---|
| [LI-001](#li-001) | Single image ad (Sponsored Content) | LinkedIn feed (desktop + mobile; vertical mobile only); LinkedIn Audience Network where enabled | DOCUMENTED |
| [LI-002](#li-002) | Carousel image ad (Sponsored Content) | LinkedIn feed | SOURCE_ISSUE |
| [LI-003](#li-003) | Video ad (Sponsored Content) | LinkedIn feed; LinkedIn Audience Network; in-stream video (testing) | SOURCE_ISSUE |
| [LI-004](#li-004) | Document ad (Sponsored Content) | LinkedIn feed; LinkedIn Audience Network | DOCUMENTED |
| [LI-005](#li-005) | Event ad (Sponsored Content) | LinkedIn feed | SOURCE_ISSUE |
| [LI-006](#li-006) | Thought Leader Ad | LinkedIn feed (sponsored member post) | SOURCE_ISSUE |
| [LI-007](#li-007) | Article and Newsletter ad | LinkedIn feed | DOCUMENTED |
| [LI-008](#li-008) | Conversation ad (Sponsored Messaging) | LinkedIn Messaging, desktop + mobile | DOCUMENTED |
| [LI-009](#li-009) | Message ad (Sponsored Messaging) | LinkedIn Messaging, desktop + mobile | SOURCE_ISSUE |
| [LI-010](#li-010) | Text ad | Right rail of LinkedIn desktop pages | SOURCE_ISSUE |
| [LI-011](#li-011) | Lead Gen Form | Attached to single image, carousel, video, event, message, document, conversation ads | DOCUMENTED |
| [LI-012](#li-012) | Connected TV (CTV) ad | Connected TV publisher inventory | DOCUMENTED |
| [LI-013](#li-013) | Dynamic ad: Spotlight | Desktop | DOCUMENTED |
| [LI-014](#li-014) | Dynamic ad: Follower | Desktop | DOCUMENTED |

## LI-001

**Single image ad (Sponsored Content) · LinkedIn feed (desktop + mobile; vertical mobile only); LinkedIn Audience Network where enabled · DOCUMENTED**

[Source](https://www.linkedin.com/help/lms/answer/a426534) · checked 2026-09-16 · account availability NOT_TESTED · also compared: [business.linkedin.com/…/single-image-ads-specs](https://business.linkedin.com/advertise/ads/sponsored-content/single-image-ads-specs)

| Field | Value | Classification |
|---|---|---|
| Ad name (optional) | 255 characters | REQUIREMENT |
| Introductory text, to avoid truncation | 150 characters incl. spaces, emojis, punctuation | RECOMMENDATION |
| Introductory text, maximum | 3,000 characters; up to 10 emojis; URLs over 23 characters converted to short link | REQUIREMENT |
| Headline, to avoid truncation | 70 characters | RECOMMENDATION |
| Headline, maximum | 200 characters | REQUIREMENT |
| Description, to avoid truncation | 100 characters | RECOMMENDATION |
| Description, maximum | 300 characters; may vary on LinkedIn Audience Network (LAN) | REQUIREMENT |
| Description display condition | Shown when image is under 200 px wide or ad serves beyond the feed via LAN | SOURCE_NOTE |
| Call to action (optional) | Choose from available CTAs | REQUIREMENT |
| Image alt text (optional) | Supported; only visible to screen-reader users | SOURCE_NOTE |
| Destination URL | http:// or https:// prefix; up to 2,000 characters (or Lead Gen Form) | REQUIREMENT |
| File type | JPG, PNG or GIF; animated GIF 250 frames or fewer | REQUIREMENT |
| File size | 5 MB | REQUIREMENT |
| Image size | 7680 x 4320 px; images under 401 px wide display as a thumbnail | REQUIREMENT |
| Horizontal 1.91:1 (recommended ratio) | Recommended 1200 x 628 px | RECOMMENDATION |
| Horizontal dimension range | Min 640 x 360 px; max 7680 x 4320 px | REQUIREMENT |
| Square 1:1 | Recommended 1200 x 1200 px | RECOMMENDATION |
| Square dimension range | Min 360 x 360 px; max 4320 x 4320 px | REQUIREMENT |
| Vertical 4:5 (recommended ratio) | Recommended 720 x 900 px | RECOMMENDATION |
| Vertical dimension range | Min 360 x 640 px; max 2430 x 4320 px | REQUIREMENT |
| Vertical delivery | Vertical recommended, but paid vertical assets serve on mobile only. 1:1.91 vertical still supported but gets side borders; use 4:5 to avoid borders | RECOMMENDATION |
| Thumbnail rendering | Aspect ratio between 3:2 and 16:9 for optimal thumbnail previews; square/vertical may be cropped when shared organically | RECOMMENDATION |

Business page (single-image-ads-specs) still lists description 70 characters 'LAN only', vertical 1:1.91 at 628 x 1200 and 2:3 at 600 x 900, and no hard maximums for text. Help Center page is the more detailed and more recently maintained source; see source-conflicts.md LI-C1.

## LI-002

**Carousel image ad (Sponsored Content) · LinkedIn feed · SOURCE_ISSUE**

[Source](https://www.linkedin.com/help/lms/answer/a427022) · checked 2026-09-16 · account availability NOT_TESTED · also compared: [business.linkedin.com/…/specs](https://business.linkedin.com/advertise/ads/sponsored-content/carousel-ads/specs)

| Field | Value | Classification |
|---|---|---|
| Ad name (optional) | 255 characters | REQUIREMENT |
| Introductory text, to avoid truncation on some devices | 150 characters | RECOMMENDATION |
| Introductory text, maximum | 255 characters | REQUIREMENT |
| Card headline | 45-character limit (for URL destination and for Lead Gen Form CTA); truncates after two lines | REQUIREMENT |
| Destination URL | http:// or https://; up to 2,000 characters; cards may use different URLs, but Lead Gen Form applies to all cards | REQUIREMENT |
| CTA button | Only available for carousels using Lead Gen Forms (Sponsored Content overview page) | SOURCE_NOTE |
| Cards | Minimum 2, maximum 10 | REQUIREMENT |
| File size per card | 10 MB | REQUIREMENT |
| Max image dimension | 4320 x 4320 px | REQUIREMENT |
| File types | Help: JPG, PNG, GIF (non-animated only). Business page: JPG or PNG | REQUIREMENT |
| Recommended card image | 1080 x 1080 px, 1:1; images scaled to 312 x 312 px | RECOMMENDATION |
| Editing | Cards cannot be edited after the ad is saved | REQUIREMENT |

Help page's '45-character limit' lines sit under 'Character limits' without naming the field; the business page names it card headline 45. Business page also says carousel ads do not support video. GIF support differs between the two official pages.

## LI-003

**Video ad (Sponsored Content) · LinkedIn feed; LinkedIn Audience Network; in-stream video (testing) · SOURCE_ISSUE**

[Source](https://www.linkedin.com/help/lms/answer/a424737) · checked 2026-09-16 · account availability NOT_TESTED · also compared: [business.linkedin.com/…/specs](https://business.linkedin.com/advertise/ads/sponsored-content/video-ads/specs)

| Field | Value | Classification |
|---|---|---|
| Ad name (optional) | 255 characters | REQUIREMENT |
| Introductory text (optional), to avoid truncation | 150 characters | RECOMMENDATION |
| Introductory text, maximum | Help: 3,000 characters, up to 10 emojis. Business page: 600 characters | REQUIREMENT |
| Video headline, to avoid truncation | 70 characters | RECOMMENDATION |
| Video headline, maximum | 200 characters | REQUIREMENT |
| Non-standard text | Ad might be rejected with more than four emojis, symbols or repeated characters | REQUIREMENT |
| Destination URL | http:// or https://; up to 2,000 characters | REQUIREMENT |
| CTA | Choose from available CTAs; in-stream placements may not show a CTA | SOURCE_NOTE |
| Recommended ratio | 4:5 vertical (0.80) | RECOMMENDATION |
| 16:9 (1.78) | Recommended 1920 x 1080 or 1200 x 675 px; range 640 x 360 to 1920 x 1080 | RECOMMENDATION |
| 1:1 | No recommended size given; range 360 x 360 to 1920 x 1920 | RECOMMENDATION |
| 4:5 (0.80) | Recommended 720 x 900 px; range 360 x 450 to 1080 x 1350 | RECOMMENDATION |
| 9:16 (0.56) | Recommended 720 x 1280 px; range 360 x 640 to 1080 x 1920 | RECOMMENDATION |
| Aspect ratio bounds | Max 16:9 (1.777); business page: min 9:16 (0.563), 5% tolerance | REQUIREMENT |
| Length | 3 seconds to 30 minutes; in-stream up to 90 seconds | REQUIREMENT |
| Recommended length | 15-30 seconds to qualify for all feed and Audience Network placements | RECOMMENDATION |
| File size | 75 KB to 500 MB | REQUIREMENT |
| Format / codec | MP4; H.264 or VP8; Apple ProRes not supported | REQUIREMENT |
| Frame rate | Help: less than 30 fps. Business page: recommended 30 fps | REQUIREMENT |
| Audio | AAC or MPEG4; less than 64 kHz | REQUIREMENT |
| Captions | SRT, text only, no custom formatting | REQUIREMENT |
| Thumbnail (optional) | JPG or PNG; max 2 MB; should match video ratio and resolution | REQUIREMENT |
| Upload limits | Max 25 videos per 24 hours; desktop upload only; must be uploaded (no YouTube/Vimeo links) | REQUIREMENT |
| Playback | Videos under 30 s loop until at least 30 s of playback | SOURCE_NOTE |

Introductory-text maximum (3,000 vs 600) and frame rate (<30 vs 30 recommended) differ between Help Center and business page. In-stream video ads are described as testing / gradual release.

## LI-004

**Document ad (Sponsored Content) · LinkedIn feed; LinkedIn Audience Network · DOCUMENTED**

[Source](https://www.linkedin.com/help/lms/answer/a493903) · checked 2026-09-16 · account availability NOT_TESTED · also compared: [business.linkedin.com/…/specs](https://business.linkedin.com/advertise/ads/sponsored-content/document-ads/specs)

| Field | Value | Classification |
|---|---|---|
| Ad name (optional) | 255 characters | REQUIREMENT |
| Introductory text, to avoid shortening | 150 characters | RECOMMENDATION |
| Introductory text, maximum | 3,000 characters | REQUIREMENT |
| Headline, to avoid shortening (pre-filled with file name) | 70 characters | RECOMMENDATION |
| Headline, maximum | 200 characters | REQUIREMENT |
| File size / pages | Max 100 MB and 300 pages; 1 million words | REQUIREMENT |
| File types | PPT, PPTX, DOC, DOCX, PDF; lead generation objective: PDF only | REQUIREMENT |
| Upload amount | Up to five documents | REQUIREMENT |
| PDF preparation | Flatten multi-layer PDFs; fit mixed page sizes to one size | REQUIREMENT |
| Video/animation | Not supported; renders as static images | REQUIREMENT |
| Hyperlinks | Clickable only if the member downloads the document; keep links secure | SOURCE_NOTE |
| Page count | Under 10 pages (business page) | RECOMMENDATION |
| Page layouts | Standard PDF layouts (Letter, Tabloid, Legal, Statement, Executive, Folio, A3, A4, B4, B5); vertical, horizontal or square (business page) | RECOMMENDATION |

Business page lists the same text lengths without hard maximums.

## LI-005

**Event ad (Sponsored Content) · LinkedIn feed · SOURCE_ISSUE**

[Source](https://www.linkedin.com/help/lms/answer/a462024) · checked 2026-09-16 · account availability NOT_TESTED · also compared: [business.linkedin.com/…/specs](https://business.linkedin.com/advertise/ads/sponsored-content/event-ads/specs)

| Field | Value | Classification |
|---|---|---|
| Ad name (optional) | 255 characters | REQUIREMENT |
| Introductory text (optional) | Up to 600 characters; same text used before, during and after the event | REQUIREMENT |
| Ad image | Help: optional; upload or media library; replaces the LinkedIn Event cover image. Business page: 4:1 image pulled from the Event page | SOURCE_NOTE |
| Video preview (optional) | 30-second preview of LinkedIn Live stream or recording | SOURCE_NOTE |
| Event destination URL | LinkedIn Event or off-platform event URL (business page: LinkedIn Event page URLs only, 2,000 characters) | REQUIREMENT |

Help Center now allows off-platform events and a custom ad image; the business page still describes LinkedIn Event pages only and a 4:1 pulled image. Business page's Help Center link points to the carousel spec page. No image dimensions published for the custom ad image.

## LI-006

**Thought Leader Ad · LinkedIn feed (sponsored member post) · SOURCE_ISSUE**

[Source](https://www.linkedin.com/help/lms/answer/a1399568) · checked 2026-09-16 · account availability NOT_TESTED · also compared: [business.linkedin.com/…/specs](https://business.linkedin.com/advertise/ads/sponsored-content/thought-leader-ads/specs)

| Field | Value | Classification |
|---|---|---|
| Headline / introductory text | Cannot be added; edits must come from the post author | REQUIREMENT |
| CTA | Help: no CTA for single image or video; Event Thought Leader Ads include a CTA. Business page: no CTA buttons | REQUIREMENT |
| URLs | None added; URLs in the organic post stay hyperlinked | SOURCE_NOTE |
| Content specs | Member post must meet single image (LI-001) or video (LI-003) specs | REQUIREMENT |
| Eligible posts | Public text, single image, video, article/newsletter posts; LinkedIn Live Event attendee posts. Not: celebrations, documents, polls, multi-image, reposts | REQUIREMENT |
| Format / objective | Single image or text: brand awareness, engagement. Video: + video views. Event, Article/Newsletter: brand awareness, engagement | REQUIREMENT |
| Permissions | Author approval required; full name on profile; post public; cannot duplicate | REQUIREMENT |

CTA statement differs between the Help Center (event exception) and the business page.

## LI-007

**Article and Newsletter ad · LinkedIn feed · DOCUMENTED**

[Source](https://business.linkedin.com/advertise/ads/sponsored-content/articles-and-newsletters-ads/specs) · checked 2026-09-16 · account availability NOT_TESTED

| Field | Value | Classification |
|---|---|---|
| Headline / introductory text | Cannot be added; edits come from the original author | REQUIREMENT |
| CTA | Lead generation objective (Article Ads only): 'Unlock Article'; no CTA for other objectives | REQUIREMENT |
| Content specs | Same as single image ads (LI-001) | REQUIREMENT |
| Destination | No URL; click opens the organic Article or Newsletter | SOURCE_NOTE |

Business marketing page only; linked Help Center article (a5966218) not retrieved in this pass.

## LI-008

**Conversation ad (Sponsored Messaging) · LinkedIn Messaging, desktop + mobile · DOCUMENTED**

[Source](https://www.linkedin.com/help/lms/answer/a426057) · checked 2026-09-16 · account availability NOT_TESTED · also compared: [business.linkedin.com/…/specs](https://business.linkedin.com/advertise/ads/sponsored-messaging/conversation-ads/specs)

| Field | Value | Classification |
|---|---|---|
| Ad name | 255 characters | REQUIREMENT |
| Subject (optional) | Up to 60 characters incl. macros; may truncate; short recommended | REQUIREMENT |
| Intro message | Up to 8,000 characters; up to 10 emojis; rich text counts toward limit | REQUIREMENT |
| Message length | Feedback prompt above 500 characters; fewer characters can drive engagement | RECOMMENDATION |
| Each message | Up to 8,000 characters; 10 emojis per message layer | REQUIREMENT |
| CTA button text | 25 characters | REQUIREMENT |
| CTA buttons | 5 per message, 50 per conversation; 'Not Interested' required and auto-applied on intro | REQUIREMENT |
| Custom footer and terms (optional) | 20,000 characters | REQUIREMENT |
| Destination URL | http:// or https://; up to 2,000 characters | REQUIREMENT |
| Banner creative (optional) | Max 300 x 250 px; desktop only; JPG or PNG; max 2 MB | REQUIREMENT |
| Image (optional) | 250 x 250 px; JPG or PNG; max 5 MB; mobile may render differently | REQUIREMENT |
| EEA / Switzerland | Delivered only to members who opted in to Sponsored Messaging | SOURCE_NOTE |

Business page summarizes message text as 8,000 maximum and CTA 25 maximum, consistent with Help.

## LI-009

**Message ad (Sponsored Messaging) · LinkedIn Messaging, desktop + mobile · SOURCE_ISSUE**

[Source](https://www.linkedin.com/help/lms/answer/a425533) · checked 2026-09-16 · account availability NOT_TESTED · also compared: [business.linkedin.com/…/specs](https://business.linkedin.com/advertise/ads/sponsored-messaging/message-ads/specs)

| Field | Value | Classification |
|---|---|---|
| Ad name | 255 characters | REQUIREMENT |
| Subject | Up to 60 characters incl. macros; may truncate | REQUIREMENT |
| Message text | Help: up to 1,500 characters, 10 emojis. Business page: 8,000 maximum | REQUIREMENT |
| Clickable links | Up to 3; hyperlinked text up to 70 characters | REQUIREMENT |
| CTA | Help: 20 characters, plus required 'Not Interested'. Business page: 25 maximum | REQUIREMENT |
| Custom footer and T&Cs | 20,000 characters | REQUIREMENT |
| Landing page URL | Help: up to 1,024 characters. Business page: 2,000 | REQUIREMENT |
| Banner creative (optional) | Max 300 x 250 px; desktop only; JPG, non-animated GIF or PNG; max 2 MB | REQUIREMENT |

Business message-ads page repeats conversation-ad values (8,000 / 25 / 2,000) and links its resources to single image ads, suggesting a copied template. Third-party reports claim Message Ads were sunset in 2023; the Help Center page is still live. Availability UNVERIFIED.

## LI-010

**Text ad · Right rail of LinkedIn desktop pages · SOURCE_ISSUE**

[Source](https://www.linkedin.com/help/lms/answer/a423705) · checked 2026-09-16 · account availability NOT_TESTED · also compared: [business.linkedin.com/…/specs](https://business.linkedin.com/advertise/ads/text-ads/specs)

| Field | Value | Classification |
|---|---|---|
| Ad name (optional) | 255 characters | REQUIREMENT |
| Headline | 25 characters incl. spaces | REQUIREMENT |
| Description | 75 characters incl. spaces | REQUIREMENT |
| Destination URL | Help: up to 500 characters. Business page: 2,000 | REQUIREMENT |
| Ad image | 100 x 100 px; JPG or PNG; 2 MB or smaller | REQUIREMENT |
| Rendered sizes | 300 x 250, 700 x 17, 160 x 600, 728 x 90, 496 x 80 | SOURCE_NOTE |

Still listed in the Help Center and in the business ads guide as of the research date; no official retirement notice found. URL length differs between sources.

## LI-011

**Lead Gen Form · Attached to single image, carousel, video, event, message, document, conversation ads · DOCUMENTED**

[Source](https://www.linkedin.com/help/lms/answer/a423364) · checked 2026-09-16 · account availability NOT_TESTED · also compared: [business.linkedin.com/…/specs](https://business.linkedin.com/advertise/ads/sponsored-content/lead-gen-ads/specs)

| Field | Value | Classification |
|---|---|---|
| Form headline | 60 characters | REQUIREMENT |
| Details | 160 characters | REQUIREMENT |
| Privacy policy text (optional) | 2,000 characters; privacy policy URL required | REQUIREMENT |
| Disclosure checkboxes (optional) | Up to 5; 500 characters each | REQUIREMENT |
| Confirmation message | 300 characters | REQUIREMENT |
| CTA (business page) | 20 characters | REQUIREMENT |
| Profile fields | Up to 12 (custom questions count); at least one question | REQUIREMENT |
| Custom questions | Up to 3; 100 characters each | REQUIREMENT |
| Form image (optional) | 552 x 200 px | RECOMMENDATION |
| Field count | 3-4 fields (business page) | RECOMMENDATION |

## LI-012

**Connected TV (CTV) ad · Connected TV publisher inventory · DOCUMENTED**

[Source](https://www.linkedin.com/help/lms/answer/a6282198) · checked 2026-09-16 · account availability NOT_TESTED

| Field | Value | Classification |
|---|---|---|
| Dimensions | 1920 x 1080 or 1280 x 720 px; recommended 1920 x 1080 | REQUIREMENT |
| Aspect ratio | 16:9 | REQUIREMENT |
| Duration | 6-60 s; recommended 6, 15, 30, 45 or 60 s; some inventory rejects 45/60 s | REQUIREMENT |
| Format / codec | MP4; H.264 | REQUIREMENT |
| Bit rate | 1.2 Mbps or higher; recommended 15-40 Mbps | REQUIREMENT |
| Audio | 2-channel, -23 LUFS integrated; PCM (preferred) or AAC; 192 kbps min; 48 kHz; must match video duration | REQUIREMENT |
| Max file size | 500 MB | REQUIREMENT |
| Frame rate | Constant 23.98, 24, 25, 29.97 or 30 fps | REQUIREMENT |
| Chroma subsampling | 4:2:0; recommended 4:2:2 | REQUIREMENT |

Meeting specs does not guarantee delivery to all publishers.

## LI-013

**Dynamic ad: Spotlight · Desktop · DOCUMENTED**

[Source](https://www.linkedin.com/help/lms/answer/a425222) · checked 2026-09-16 · account availability NOT_TESTED

| Field | Value | Classification |
|---|---|---|
| Ad description (above images) | 70 characters | REQUIREMENT |
| Ad headline (below images) | 50 characters | REQUIREMENT |
| Ad name (optional) | 255 characters | REQUIREMENT |
| Company name | 25 characters | REQUIREMENT |
| CTA button text | 18 characters | REQUIREMENT |
| Landing page URL | Max 500 characters | REQUIREMENT |
| Company image | Min 100 x 100 px JPG or PNG; larger reduced to 100 x 100 | REQUIREMENT |
| Custom background (optional) | Exactly 300 x 250 px, 2 MB or less; white area 276 x 148 px; removes description and member photo | REQUIREMENT |

Not the same product as Nextdoor Spotlight.

## LI-014

**Dynamic ad: Follower · Desktop · DOCUMENTED**

[Source](https://www.linkedin.com/help/lms/answer/a420350) · checked 2026-09-16 · account availability NOT_TESTED

| Field | Value | Classification |
|---|---|---|
| Ad description | 70 characters (custom text not translated) | REQUIREMENT |
| Ad headline | 50 characters | REQUIREMENT |
| Ad name (optional) | 255 characters | REQUIREMENT |
| Company name | 25 characters | REQUIREMENT |
| CTA | Pre-set (Visit company / jobs / life); non-followers see Follow | REQUIREMENT |
| Ad image | Min 100 x 100 px JPG or PNG | REQUIREMENT |

No third-party tracking.
