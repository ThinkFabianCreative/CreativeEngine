# Source conflicts, ambiguities and coverage gaps

Checked 2026-09-16. Nextdoor's official pages disagree. Every item below stays OPEN. Scope, recency or page type does not resolve it. Confirm in the actual Ads Manager setup and preview.

## en-gb enterprise page vs US Nextdoor Ads Manager page

| Field | en-gb enterprise ([source](https://business.nextdoor.com/en-gb/enterprise/creative-specs)) | US NAM ([source](https://business.nextdoor.com/en-us/nam/nextdoor-ads-manager/creative-specs)) |
|---|---|---|
| Format names | Display, Video, Spotlight, Carousel, Digest, For Sale & Free | Image, Video, Carousel, Lead Gen, For Sale & Free, Right Hand Rail |
| Advertiser name | 25 | 70 |
| Subject line / headline | 70 (subject line) | 70 (headline) |
| Body copy | 800 (90 before truncation) | 1,700 (90 before truncation) |
| Offer text | 50 | Not listed as a field (customizable per carousel card) |
| CTA | 10 | 45 (carousel 30) |
| Image file | <1 MB JPEG, PNG or GIF | Up to 150 MB JPEG or PNG (no GIF) |
| Image dimensions | 1200 x 628 ("1:91:1", a typo) | 1200 x 628 (1.91:1) or 1200 x 1200 (1:1) |
| Video length / size / ratio | 3-120 s; 50 MB; 16:9 | 2-300 s; 500 MB; 16:9 or 1:1 |
| Video thumbnail | 1200 x 628 | Auto-generated |
| Carousel | 1-5 images (+ end card); ideal 464 x 464, min 232 x 232; body 240 (108 iOS); offer 33 | 2-10 images; min 1200 x 1200; body 1,700; CTA 30 |
| Spotlight | 1200 x 1200, <1 MB, "Sponsored by + logo" | Not listed |

The two pages may describe different buying paths: managed enterprise Sponsored Posts vs self-serve NAM. They may also be different generations of one product. This was not established. The US enterprise URL redirects to the NAM page, which suggests the US enterprise spec set was retired or merged. Not confirmed.

## US NAM page vs about.nextdoor.com/sp-guidelines

| Field | NAM page | [about.nextdoor.com/sp-guidelines](https://about.nextdoor.com/sp-guidelines) |
|---|---|---|
| Image ratio | 1.91:1 or 1:1 | "16:9 rectangle" at 1200 x 628 (internally inconsistent: 1200 x 628 is 1.91:1) |
| Body copy | 1,700 | 1,500 |
| CTA | 45 (carousel 30) | 20 |
| Video length / ratio | 2-300 s; 16:9 or 1:1 | 2-120 s; 16:9 |
| Lead Gen creative / fields | Image or video; 16:9 or 1:1; 2-11 fields; up to 3 multiple choice | Image only; 16:9; 2-8 fields |
| For Sale & Free | Name 70; headline 70 | Name 25; headline 45 |
| Right Hand Rail | Name 70; CTA 45 | Name 25; CTA 20 |

## Other ambiguities

- **"30 sec. loop"** appears under en-gb Display with no label. It may mean a GIF loop cap. This is not explained, so do not treat it as a video spec.
- **Spotlight "Sponsored by + logo"**: must be built into the image *if Nextdoor is not providing creative assistance*. Who provides assistance depends on the deal and is not public.
- **Carousel video**: the [12 Nov 2025 press release](https://about.nextdoor.com/press-releases/nextdoor-introduces-ai-driven-ad-performance-optimization-and-new-video-ad-formats) says videos can be used in Carousel ads in US/CA/UK. The NAM specs page still says "Images only".
- **Small-business specs** ([source](https://business.nextdoor.com/en/en-us/small-business/resources/ads-creative-specs)): headline 120 characters; one block 1:1 at 1080 x 1080, another 2:1 at 1080 x 540, both 30 MB. The [Local Deals transition page](https://business.nextdoor.com/en-us/local/localdealstransition) says 70-character headline and 1x1 photo. It is unclear which ad goal each photo block belongs to.
- **Hard vs recommended**: Nextdoor rarely labels its numbers. PUBLISHED_LIMIT values may be enforced limits or guidance.
- **150 MB image allowance** on NAM is unusually large. It is recorded as published, not as a production target.

## Platform claims (not specs)

- "CTR increases by 15% when the creative is personalized with location" (en-gb and US pages).
- "CTRs are 10% higher when less than 1/4 of the image contains text" (en-gb and US pages).
- For Sale & Free product-only images have "almost double the CTR" (US page).
- Press release figures (134% CTR lift, 35% CPA improvement) are Nextdoor's own test claims.

## Coverage not verified

- **Nextdoor Ads Manager help center** (`adsmanager.help.nextdoor.com`) returned "under construction" (HTTP 503) on the research date. **help.nextdoor.com** ad-spec articles render only with JavaScript and could not be read. Either may hold more current specs.
- en-ca pages (enterprise creative-specs URL returned 404).
- Geo-personalized image/Spotlight pilot, weather targeting, AI-generated creative, Local Deals legacy formats, Digest/email availability outside the UK, safe zones, video codecs, captions and accessibility requirements.
- Account availability, upload acceptance, review, delivery and performance. All NOT_TESTED.
