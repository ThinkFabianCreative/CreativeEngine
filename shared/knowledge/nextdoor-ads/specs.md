# Nextdoor ad specifications

Checked 2026-09-16. Nextdoor publishes several official spec pages that disagree. Records are kept per source rather than merged. Read [README](README.md) and [source conflicts](source-conflicts.md) before production.

Classifications: **REQUIREMENT** (stated as a limit or rule), **RECOMMENDATION** (stated as recommended, ideal or to avoid truncation), **PUBLISHED_LIMIT** (a value with no requirement/recommendation label), **PLATFORM_CLAIM** (performance marketing claim, not a spec), **SOURCE_NOTE** (context). A dash means not published in the inspected source.

| ID | Format | Placement | Status |
|---|---|---|---|
| [ND-001](#nd-001) | Display (image) - Sponsored Posts, enterprise | Newsfeed (en-gb page) | SOURCE_ISSUE |
| [ND-002](#nd-002) | Video - Sponsored Posts, enterprise | Newsfeed (en-gb page) | SOURCE_ISSUE |
| [ND-003](#nd-003) | Spotlight - Sponsored Posts, enterprise | Newsfeed (en-gb page) | SOURCE_ISSUE |
| [ND-004](#nd-004) | Carousel - Sponsored Posts, enterprise | Newsfeed (en-gb page) | SOURCE_ISSUE |
| [ND-005](#nd-005) | Digest | Digest email (en-gb page) | DOCUMENTED |
| [ND-006](#nd-006) | For Sale & Free | For Sale & Free (en-gb page) | DOCUMENTED |
| [ND-007](#nd-007) | Image ad - Nextdoor Ads Manager | Newsfeed (US) | DOCUMENTED |
| [ND-008](#nd-008) | Video ad - Nextdoor Ads Manager | Newsfeed (US) | DOCUMENTED |
| [ND-009](#nd-009) | Carousel ad - Nextdoor Ads Manager | Newsfeed (US) | SOURCE_ISSUE |
| [ND-010](#nd-010) | Lead Gen ad - Nextdoor Ads Manager | Newsfeed (US) | DOCUMENTED |
| [ND-011](#nd-011) | For Sale & Free image ad - Nextdoor Ads Manager | For Sale & Free (US) | DOCUMENTED |
| [ND-012](#nd-012) | Right Hand Rail image ad - Nextdoor Ads Manager | Right Hand Rail, desktop only (US) | DOCUMENTED |
| [ND-013](#nd-013) | Nextdoor Ads specs (alternate official page) | Newsfeed, For Sale & Free, Right Hand Rail | SOURCE_ISSUE |
| [ND-014](#nd-014) | Small-business self-serve ads | Newsfeed, For Sale, Right Hand Rail (auto-formatted) | SOURCE_ISSUE |

## ND-001

**Display (image) - Sponsored Posts, enterprise · Newsfeed (en-gb page) · SOURCE_ISSUE**

[Source](https://business.nextdoor.com/en-gb/enterprise/creative-specs) · checked 2026-09-16 · account availability NOT_TESTED

| Field | Value | Classification |
|---|---|---|
| Logo | 100 x 100 px | PUBLISHED_LIMIT |
| Advertiser name | 25 characters | PUBLISHED_LIMIT |
| Subject line | 70 characters | PUBLISHED_LIMIT |
| Body copy | 800 characters | PUBLISHED_LIMIT |
| Body copy before truncation | 90 characters | RECOMMENDATION |
| Offer text | 50 characters | PUBLISHED_LIMIT |
| CTA | 10 characters | PUBLISHED_LIMIT |
| Image | <1 MB JPEG, PNG or GIF | PUBLISHED_LIMIT |
| Dimensions | 1200 x 628 px or '1:91:1' (source typo for 1.91:1) | PUBLISHED_LIMIT |
| Loop | '30 sec. loop' listed with no field label (probably GIF loop length; not explained) | PUBLISHED_LIMIT |

en-gb enterprise page. The US equivalent URL (/en-us/enterprise/creative-specs) redirects to the Nextdoor Ads Manager (NAM) page with different values (ND-007). No en-ca page found (404).

## ND-002

**Video - Sponsored Posts, enterprise · Newsfeed (en-gb page) · SOURCE_ISSUE**

[Source](https://business.nextdoor.com/en-gb/enterprise/creative-specs) · checked 2026-09-16 · account availability NOT_TESTED

| Field | Value | Classification |
|---|---|---|
| Logo | 100 x 100 px | PUBLISHED_LIMIT |
| Advertiser name | 25 characters | PUBLISHED_LIMIT |
| Subject line | 70 characters | PUBLISHED_LIMIT |
| Body copy | 800 characters | PUBLISHED_LIMIT |
| Body copy before truncation | 90 characters | RECOMMENDATION |
| Offer text | 50 characters | PUBLISHED_LIMIT |
| CTA | 10 characters | PUBLISHED_LIMIT |
| File | 50 MB, MOV or MP4 | PUBLISHED_LIMIT |
| Length | 3-120 seconds | PUBLISHED_LIMIT |
| Aspect ratio | 16:9 | PUBLISHED_LIMIT |
| Thumbnail | 1200 x 628 px | PUBLISHED_LIMIT |

Differs from US NAM video (ND-008).

## ND-003

**Spotlight - Sponsored Posts, enterprise · Newsfeed (en-gb page) · SOURCE_ISSUE**

[Source](https://business.nextdoor.com/en-gb/enterprise/creative-specs) · checked 2026-09-16 · account availability NOT_TESTED · also compared: [about.nextdoor.com/…/nextdoor-introduces-ai-driven-ad-performance-optimization-and-new-video-ad-formats](https://about.nextdoor.com/press-releases/nextdoor-introduces-ai-driven-ad-performance-optimization-and-new-video-ad-formats)

| Field | Value | Classification |
|---|---|---|
| Logo | 100 x 100 px; minimum 100 x 100 px | PUBLISHED_LIMIT |
| Image | <1 MB JPEG or PNG; 1200 x 1200 px or 1:1 | PUBLISHED_LIMIT |
| Image copy | <30 characters recommended; keep legible; text is part of the image | RECOMMENDATION |
| Sponsored by + logo | Logo always preceded by 'Sponsored by [+ logo]'; if Nextdoor is not providing creative assistance, this must be included in the image | REQUIREMENT |

Spotlight appears only on the en-gb enterprise page; not listed on the US NAM specs page. The Nov 2025 press release mentions geo-personalized Spotlight creatives (US pilot), so the product exists in some form in the US; current US specs not found.

## ND-004

**Carousel - Sponsored Posts, enterprise · Newsfeed (en-gb page) · SOURCE_ISSUE**

[Source](https://business.nextdoor.com/en-gb/enterprise/creative-specs) · checked 2026-09-16 · account availability NOT_TESTED

| Field | Value | Classification |
|---|---|---|
| Logo | 100 x 100 px | PUBLISHED_LIMIT |
| Advertiser name | 25 characters | PUBLISHED_LIMIT |
| Subject line | 70 characters | PUBLISHED_LIMIT |
| Body copy | 240 characters (90 before truncation); 108 characters iOS | PUBLISHED_LIMIT |
| Offer text | 33 characters | PUBLISHED_LIMIT |
| CTA | 10 characters | PUBLISHED_LIMIT |
| Image | <1 MB JPEG or PNG | PUBLISHED_LIMIT |
| Product image | Ideal 464 x 464 px | RECOMMENDATION |
| Product image minimum | 232 x 232 px at 1:1 | REQUIREMENT |
| Images | Min 1, max 5, excluding end card | PUBLISHED_LIMIT |
| Last card: logo or brand image | Ideal 264 x 264 px; min 132 x 132 px | RECOMMENDATION |

Very different from US NAM carousel (ND-009: 2-10 cards, 1200 x 1200 min).

## ND-005

**Digest · Digest email (en-gb page) · DOCUMENTED**

[Source](https://business.nextdoor.com/en-gb/enterprise/creative-specs) · checked 2026-09-16 · account availability NOT_TESTED

| Field | Value | Classification |
|---|---|---|
| Advertiser name | 25 characters | PUBLISHED_LIMIT |
| Subject line | 50 characters | PUBLISHED_LIMIT |
| Body copy | 90 characters | PUBLISHED_LIMIT |
| CTA | 10 characters | PUBLISHED_LIMIT |
| Image | <1 MB JPEG or PNG; 250 x 250 px | PUBLISHED_LIMIT |

en-gb only.

## ND-006

**For Sale & Free · For Sale & Free (en-gb page) · DOCUMENTED**

[Source](https://business.nextdoor.com/en-gb/enterprise/creative-specs) · checked 2026-09-16 · account availability NOT_TESTED

| Field | Value | Classification |
|---|---|---|
| Logo | 100 x 100 px | PUBLISHED_LIMIT |
| Advertiser name | 25 characters | PUBLISHED_LIMIT |
| Body copy | 40 characters | PUBLISHED_LIMIT |
| Optional offer text (deal or price) | 13 characters | PUBLISHED_LIMIT |
| Image | <1 MB JPG or PNG; 178 x 178 px | PUBLISHED_LIMIT |

## ND-007

**Image ad - Nextdoor Ads Manager · Newsfeed (US) · DOCUMENTED**

[Source](https://business.nextdoor.com/en-us/nam/nextdoor-ads-manager/creative-specs) · checked 2026-09-16 · account availability NOT_TESTED · also compared: [about.nextdoor.com/…/sp-guidelines](https://about.nextdoor.com/sp-guidelines)

| Field | Value | Classification |
|---|---|---|
| Logo | 100 x 100 px, cropped circular | PUBLISHED_LIMIT |
| Advertiser name | 70 characters | PUBLISHED_LIMIT |
| Headline | 70 characters | PUBLISHED_LIMIT |
| Body copy | 1,700 characters | PUBLISHED_LIMIT |
| Body copy before truncation | 90 characters | RECOMMENDATION |
| CTA | 45 characters | PUBLISHED_LIMIT |
| Resolution / ratio | 1200 x 628 px (1.91:1) or 1200 x 1200 px (1:1) | PUBLISHED_LIMIT |
| File | Up to 150 MB; JPEG or PNG | PUBLISHED_LIMIT |
| Emojis / special formatting | Not supported in ad copy | REQUIREMENT |
| Quick Create | Ads created in Quick Create mode appear only in Newsfeed | SOURCE_NOTE |

about.nextdoor.com/sp-guidelines gives different values for the same NAM product (ND-013).

## ND-008

**Video ad - Nextdoor Ads Manager · Newsfeed (US) · DOCUMENTED**

[Source](https://business.nextdoor.com/en-us/nam/nextdoor-ads-manager/creative-specs) · checked 2026-09-16 · account availability NOT_TESTED · also compared: [about.nextdoor.com/…/sp-guidelines](https://about.nextdoor.com/sp-guidelines)

| Field | Value | Classification |
|---|---|---|
| Logo | 100 x 100 px, cropped circular | PUBLISHED_LIMIT |
| Advertiser name | 70 characters | PUBLISHED_LIMIT |
| Headline | 70 characters | PUBLISHED_LIMIT |
| Body copy | 1,700 characters | PUBLISHED_LIMIT |
| Body copy before truncation | 90 characters | RECOMMENDATION |
| CTA | 45 characters | PUBLISHED_LIMIT |
| Length | 2-300 seconds | PUBLISHED_LIMIT |
| Recommended length | Under 30 seconds, with subtitles | RECOMMENDATION |
| Aspect ratio | 16:9 or 1:1 | PUBLISHED_LIMIT |
| File | Up to 500 MB; MOV or MP4 | PUBLISHED_LIMIT |
| Thumbnail | Auto-generated | SOURCE_NOTE |

## ND-009

**Carousel ad - Nextdoor Ads Manager · Newsfeed (US) · SOURCE_ISSUE**

[Source](https://business.nextdoor.com/en-us/nam/nextdoor-ads-manager/creative-specs) · checked 2026-09-16 · account availability NOT_TESTED · also compared: [about.nextdoor.com/…/nextdoor-introduces-ai-driven-ad-performance-optimization-and-new-video-ad-formats](https://about.nextdoor.com/press-releases/nextdoor-introduces-ai-driven-ad-performance-optimization-and-new-video-ad-formats)

| Field | Value | Classification |
|---|---|---|
| Logo | 100 x 100 px, cropped circular | PUBLISHED_LIMIT |
| Advertiser name | 70 characters | PUBLISHED_LIMIT |
| Headline | 70 characters | PUBLISHED_LIMIT |
| Body copy | 1,700 characters | PUBLISHED_LIMIT |
| Body copy before truncation | 90 characters | RECOMMENDATION |
| CTA | 30 characters | PUBLISHED_LIMIT |
| Creative | Images only; min 2, max 10 | PUBLISHED_LIMIT |
| Resolution | 1200 x 1200 px minimum, 1:1 | REQUIREMENT |
| File | Up to 150 MB; JPEG or PNG | PUBLISHED_LIMIT |
| Multi-destination | Offer text, CTA and URLs customizable per card | SOURCE_NOTE |

Specs page says images only; Nextdoor's 12 Nov 2025 press release says videos can now be used in Carousel ads in all markets (US/CA/UK). Video-card specs not published.

## ND-010

**Lead Gen ad - Nextdoor Ads Manager · Newsfeed (US) · DOCUMENTED**

[Source](https://business.nextdoor.com/en-us/nam/nextdoor-ads-manager/creative-specs) · checked 2026-09-16 · account availability NOT_TESTED · also compared: [about.nextdoor.com/…/sp-guidelines](https://about.nextdoor.com/sp-guidelines)

| Field | Value | Classification |
|---|---|---|
| Logo | 100 x 100 px, cropped circular | PUBLISHED_LIMIT |
| Advertiser name | 70 characters | PUBLISHED_LIMIT |
| Headline | 70 characters | PUBLISHED_LIMIT |
| Body copy | 1,700 characters | PUBLISHED_LIMIT |
| Body copy before truncation | 90 characters | RECOMMENDATION |
| CTA | 45 characters | PUBLISHED_LIMIT |
| Creative | Image or video; 16:9 or 1:1 | PUBLISHED_LIMIT |
| File | Image up to 150 MB JPEG/PNG; video up to 500 MB MP4/MOV | PUBLISHED_LIMIT |
| Form fields | Min 2, max 11; prefilled questions, up to 3 custom and up to 3 multiple-choice | PUBLISHED_LIMIT |
| Privacy policy link | Advertiser URL required | REQUIREMENT |

## ND-011

**For Sale & Free image ad - Nextdoor Ads Manager · For Sale & Free (US) · DOCUMENTED**

[Source](https://business.nextdoor.com/en-us/nam/nextdoor-ads-manager/creative-specs) · checked 2026-09-16 · account availability NOT_TESTED

| Field | Value | Classification |
|---|---|---|
| Advertiser name | 70 characters | PUBLISHED_LIMIT |
| Headline | 70 characters max; renders as 2 lines | PUBLISHED_LIMIT |
| Image | 1:1; max 150 MB; JPEG or PNG | PUBLISHED_LIMIT |
| Image content | Product-only images (platform claim: almost double CTR vs products with people) | PLATFORM_CLAIM |

## ND-012

**Right Hand Rail image ad - Nextdoor Ads Manager · Right Hand Rail, desktop only (US) · DOCUMENTED**

[Source](https://business.nextdoor.com/en-us/nam/nextdoor-ads-manager/creative-specs) · checked 2026-09-16 · account availability NOT_TESTED

| Field | Value | Classification |
|---|---|---|
| Advertiser name | 70 characters | PUBLISHED_LIMIT |
| Headline | 70 characters max | PUBLISHED_LIMIT |
| CTA | 45 characters | PUBLISHED_LIMIT |
| Image | 1:1; max 150 MB; JPEG or PNG | PUBLISHED_LIMIT |
| Text in image | Right-hand rail ads should contain no text | RECOMMENDATION |

## ND-013

**Nextdoor Ads specs (alternate official page) · Newsfeed, For Sale & Free, Right Hand Rail · SOURCE_ISSUE**

[Source](https://about.nextdoor.com/sp-guidelines) · checked 2026-09-16 · account availability NOT_TESTED

| Field | Value | Classification |
|---|---|---|
| Image ad | 1200 x 628 px labeled '16:9 rectangle'; up to 150 MB JPEG/PNG; CTA 20; body 1,500 (90 before truncation) | PUBLISHED_LIMIT |
| Video ad | 2-120 s (recommend under 30 s with subtitles); 16:9; up to 500 MB MOV/MP4; CTA 20; body 1,500 | PUBLISHED_LIMIT |
| Carousel ad | 2-10 images; 1200 x 1200 min; 1:1; 150 MB JPG/PNG; body 1,500 | PUBLISHED_LIMIT |
| Lead Gen ad | Image only; 16:9; 150 MB; 2-8 form fields, up to 3 custom; CTA 20; body 1,500 | PUBLISHED_LIMIT |
| For Sale & Free | Advertiser name 25; headline 45 (2 lines); 1:1 image | PUBLISHED_LIMIT |
| Right Hand Rail | Advertiser name 25; headline 70; CTA 20; 1:1 image; desktop only | PUBLISHED_LIMIT |

Older-looking duplicate of the NAM specs on about.nextdoor.com. Every overlapping value except logo and carousel image rules conflicts with ND-007..ND-012. 1200 x 628 is 1.91:1, not 16:9.

## ND-014

**Small-business self-serve ads · Newsfeed, For Sale, Right Hand Rail (auto-formatted) · SOURCE_ISSUE**

[Source](https://business.nextdoor.com/en/en-us/small-business/resources/ads-creative-specs) · checked 2026-09-16 · account availability NOT_TESTED · also compared: [business.nextdoor.com/…/localdealstransition](https://business.nextdoor.com/en-us/local/localdealstransition)

| Field | Value | Classification |
|---|---|---|
| Headline | 120 characters (specs page); Local Deals transition page: 70-character headline for 'Get more messages' and 'Promote a sale or discount' | PUBLISHED_LIMIT |
| Photo (first tab) | 1:1; JPG or PNG; max 30 MB; 1080 x 1080 | PUBLISHED_LIMIT |
| Photo (second tab, labeled Newsfeed) | 2:1; JPG or PNG; max 30 MB; 1080 x 540 | PUBLISHED_LIMIT |
| CTA | Select from pulldown | SOURCE_NOTE |
| Local Deals | Converted into ads managed in the business account 'Ads' tab; budgets converted to daily, neighborhoods to ZIP codes | SOURCE_NOTE |

Tab labels ('Increase website visits', 'Promote a sale or discount') do not map cleanly to the two spec blocks in the retrieved HTML. Headline length conflicts between the two pages.
