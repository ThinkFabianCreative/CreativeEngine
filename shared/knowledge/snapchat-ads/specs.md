# Snapchat ad specifications

Checked 2026-09-16. Public Snapchat Business Help Center articles (read in a live browser; the pages load with JavaScript and show no "last updated" date) plus the Snapchat for Business ad formats page. No ad account was inspected. Read [usage rules](README.md) and [source conflicts](source-conflicts.md) before production.

A dash means not published, never zero or unlimited. **Snap's own pages disagree on length, copy limits, resolution and safe zones.** Where they do, both values are shown and the record is marked SOURCE_ISSUE.

| ID | Format | Status |
|---|---|---|
| [SNAP-001](#snap-001) | Single Image or Video ("Snap Ad", full-screen) | SOURCE_ISSUE |
| [SNAP-002](#snap-002) | Story Ads (Discover tile + 1–10 Snaps) | SOURCE_ISSUE |
| [SNAP-003](#snap-003) | Collection Ads | SOURCE_ISSUE |
| [SNAP-004](#snap-004) | Commercials (Standard and Extended Play) | SOURCE_ISSUE |
| [SNAP-005](#snap-005) | Sponsored Snaps (Chat Feed) | SOURCE_ISSUE |
| [SNAP-006](#snap-006) | Safe zones (all major formats) | DOCUMENTED |

## SNAP-006

**Safe zones for Snap ads · DOCUMENTED**

[Source](https://businesshelp.snapchat.com/s/article/safe-zones?language=en_US) · checked 2026-09-16 · account availability NOT_TESTED.

Snap says one safe-zone spec applies to Single Image/Video, Story Ads, Collection Ads (including Dynamic Collection) and Commercials, across Stories, Spotlight and Commercials. The article shows the buffers as percentages on a diagram only. The pixel values below are **calculated** for a 1080 × 1920 canvas and are not published by Snap.

| Buffer (keep clear of logos, text, CTAs, disclaimers) | Published % | Calculated at 1080 × 1920 | Classification |
|---|---|---|---|
| Top | 10% of height | 192 px | Guidance (Snap: "should remain clear") |
| Bottom (full width) | 35% of height | 672 px | Guidance |
| Left and right sides | 6% of width each | ~65 px each | Guidance |
| Lower-right column (action buttons) | 15% of width × bottom 45% of height | 162 px wide × 864 px tall | Guidance |

- Use the Safe Zone toggle in Ads Manager. Dynamic CTA variants do not appear in Ads Preview, so stay inside the safe zone even if the preview looks clear.
- Put disclaimers and legal text well above the bottom buffer.
- Older per-format numbers still on other Snap pages (top 150 / bottom 330 px; bottom 450 px; top and bottom 150 px) are narrower. See [conflicts](source-conflicts.md). Plan to the percentage spec, which is the strictest and the only one describing itself as covering all formats.

## SNAP-001

**Single Image or Video · SOURCE_ISSUE**

[Specs](https://businesshelp.snapchat.com/s/article/top-snap-specs?language=en_US) · [About](https://businesshelp.snapchat.com/s/article/image-video-ads?language=en_US) · [Best practices](https://businesshelp.snapchat.com/s/article/snap-ads-practices?language=en_US) · [Ad formats page](https://forbusiness.snapchat.com/advertising/ad-formats) · checked 2026-09-16 · account availability NOT_TESTED.

Full-screen ad between or after content (User Stories, Publisher, Creator, Our Stories) and in Spotlight. Attachments (About page): Web View, App Install, Deep Link, AR Lens, Call or Text. The CTA article also lists Lead Form CTAs.

| Field | Value | Classification |
|---|---|---|
| Canvas | 1080 × 1920 px, 9:16, scaled proportionally | Design spec (Help Center) |
| Resolution (formats page) | 720 × 1280 | Listed as a requirement on forbusiness page |
| Image minimum | 720 × 1280 px; 9:16 required; other sizes can be cropped in Ads Manager | Requirement |
| Acceptable creatives | Live, motion graphic or stop-motion video; cinemagraph; slideshow; GIF-like; still image | Documented |
| Length (Help Center specs) | 3 seconds to 30 minutes (if ≤ 1 GB); videos under 3 s are looped to reach 3 s | Requirement |
| Length (About page) | Up to 3 minutes | Conflicts with above |
| Length (formats page) | 3–180 s | Conflicts with 30 min |
| Recommended length | 3–5 s (About page; best practices "Ads between 3–5 seconds often drive action"); best practices also says "around 5–6 seconds" | Recommendation |
| Image conversion | Still images become a 5-second video | Behaviour |
| File types | Video .mp4 or .mov, H.264; image .jpg or .png (Ads Manager only) | Requirement |
| Aspect ratios | SAR 9:16; DAR 9:16; PAR 1:1 | Requirement |
| File size | Video ≤ 1 GB; image 5 MB; Dynamic Ads ≤ 6 MB | Requirement |
| Audio | 2 channels (L/R) balanced; target −16 LUFS; PCM or AAC; ≥ 192 kbps; 16 or 24 bit | Requirement (48 kHz is listed on the Commercial page, not this one) |
| Brand name | Up to 32 characters with spaces; must reflect the paying advertiser; cannot equal the headline; links to Public Profile | Requirement (Help Center) |
| Brand name (formats page) | Up to 25 characters with spaces | Conflicts with 32 |
| Headline | Up to 34 characters with spaces | Requirement |
| Other requirements | Brand name and headline must be added; full-screen vertical; approved for 13+ audience; Sponsored Creative Tool ads need persistent branding and an actionable text overlay (e.g. "Unlock Lens"); advertiser licenses fonts, emojis, tools | Requirement |
| Creative guidance | Hero message in opening frame; branding before 0:02 but don't open on a static logo/product frame; offer message around seconds 2–3; native/UGC style; one CTA; don't reuse the same creative from every platform | Recommendation |
| Safe zone | See SNAP-006. Best-practices page still says keep top 150 px and bottom 330 px clear | Guidance; conflict |
| Dynamic CTA | Eligible ads may have CTA format and placement chosen automatically | Behaviour |

## SNAP-002

**Story Ads · SOURCE_ISSUE**

[Source](https://businesshelp.snapchat.com/s/article/story-ad-specs?language=en_US) · checked 2026-09-16 · account availability NOT_TESTED.

A branded tile in Discover, or a series of ads between content, opening to 1–10 images or videos. The tile is required for automatic or Discover Feed placement and optional for between-content-only delivery.

| Field | Value | Classification |
|---|---|---|
| Tile logo | 993 × 284 px PNG, transparent background; fill full height, or full width and ≥ 50% of height | Requirement |
| Tile image | One 360 × 600 px .png, up to 2 MB, 8-bit or lower | Requirement |
| Tile image buffers | 175 px clear at top (logo). With CTA: 175 px top and 269 px bottom; text inside a 300 × 128 px safe area | Requirement (overlap guidance) |
| Tile headline | Up to 55 characters with spaces; emojis allowed and counted | Requirement |
| Tile tip | On a white background, add a gradient toward the bottom so the headline stands out | Recommendation |
| Story Snaps | 1–10 Single Image or Video ads as separate files; each must meet SNAP-001 specs | Requirement |
| Story Snap length | Each up to 180 s (formats page: 3–180 s) | Requirement; conflicts with SNAP-001's 30 min |
| Brand name / headline | Up to 32 / 34 characters with spaces (formats page: brand up to 25) | Requirement; conflict |
| Attachments | WebView, App Install, Deep Link; tile CTA for App Install and Website | Documented |
| Headline behaviour | Built in one create flow, the Ad-level headline applies to all Snaps. With "Use Existing Creative", the Snaps keep their original headlines. Check each Snap | Behaviour |
| Branding | Visible branding on every Snap is not required (exception to SNAP-001 guidelines) | Documented |
| Safe zone | See SNAP-006 | Guidance |

## SNAP-003

**Collection Ads · SOURCE_ISSUE**

[Source](https://businesshelp.snapchat.com/s/article/collection-ad-specs?language=en_US) · checked 2026-09-16 · account availability NOT_TESTED.

A full-screen Single Image or Video with 2, 3 or 4 tappable product thumbnails near the bottom. Built manually or dynamically from a product catalog.

| Field | Value | Classification |
|---|---|---|
| Main media | Single Image or Video per SNAP-001 | Requirement |
| Thumbnails | 2, 3 or 4 square static images, .jpg or .png | Requirement |
| Thumbnail size | ≥ 160 × 160 px; ≤ 2 MB each | Requirement |
| URLs | One URL per thumbnail (URLs may repeat) plus a required main click URL | Requirement |
| CTA | Applied by Snap at upper left of thumbnail area, chosen from Ads Manager list; "AD" slug at upper right | Behaviour |
| Length, recommended | 3–5 s; branding before 0:02 | Recommendation |
| Thumbnail guidance | One product per thumbnail, filling the frame; little or no text | Recommendation |
| Safe zone | This page: keep the bottom ~450 px clear. Safe-zone article (SNAP-006): bottom 35% (672 px at 1920 high) | Conflict; plan to SNAP-006 |
| Copy (formats page) | Brand up to 25; headline up to 34 characters | Requirement as stated; see conflicts |

## SNAP-004

**Commercials · SOURCE_ISSUE**

[Source](https://businesshelp.snapchat.com/s/article/commercial-specs?language=en_US) · checked 2026-09-16 · account availability NOT_TESTED.

Non-skippable video in Snap's curated content (Publisher/Creator Stories).

| Field | Value | Classification |
|---|---|---|
| Canvas | 1080 × 1920 px, 9:16 (formats page: 720 × 1280) | Design spec |
| Creatives | Live, motion graphic or stop-motion **video only**; must include audio | Requirement |
| Standard Commercial | 3–6 s, fully non-skippable | Requirement |
| Extended Play Commercial | 7–180 s; first 6 s non-skippable | Requirement |
| File | .mp4 or .mov, H.264; SAR 9:16, DAR 9:16, PAR 1:1 | Requirement |
| File size | ≤ 1 GB | Requirement |
| Audio | 2 channels balanced; −16 LUFS; PCM or AAC; ≥ 192 kbps; 16 or 24 bit; 48 kHz | Requirement |
| Attachments | Web View and AR Lens only | Requirement |
| Markets | AE, AU, AT, BE, BH, CA, CH, DE, DK, FI, FR, IE, IN, IQ, JO, KW, NL, NO, NZ, OM, QA, SA, SE, UK, US | Availability as documented |
| UI | "AD" slug lower right; 6-second ticker at the top | Behaviour |
| Safe zone | This page: no logos/graphics within 150 px of top and bottom. SNAP-006: 10% top, 35% bottom | Conflict; plan to SNAP-006 |
| Recommendations | Single-minded message; clear branding; purposeful sound; hook fast; reveal/payoff around 0:05 | Recommendation |

## SNAP-005

**Sponsored Snaps (Chat Feed) · SOURCE_ISSUE**

[Help Center](https://businesshelp.snapchat.com/s/article/ads-in-chat?language=en_US) · [Ad formats page](https://forbusiness.snapchat.com/advertising/ad-formats) · checked 2026-09-16 · account availability NOT_TESTED.

A placement, not a separate media spec. Single Image or Video, Story and Static Collection ads can deliver to Chat Feed. Opening one shows the full-screen creative, then a 1:1 chat with the advertiser.

| Field | Value | Classification |
|---|---|---|
| Eligible creatives | Single Image or Video, Story Ads, Static Collection. Not Commercials, Dynamic Collection or Dynamic Product Ads | Requirement |
| Media (formats page) | .mp4, .mov, .jpg, .png; 9:16; 720 × 1280; 180 s max | Requirement |
| Length, recommended | Under 10 s | Recommendation (formats page) |
| Brand name | Pulled from Public Profile; up to 25 characters (formats page) | Conflict with 32 on Help Center specs |
| Headline | Aim for 25–28 characters; 34 max | Recommendation / requirement |
| Branded Chat Background (optional) | PNG or JPEG; recommended 1080 × 1920 | Recommendation |
| Chat Message (optional) | Up to 500 characters | Requirement |
| Auto Response (optional) | Up to 500 characters, or video (recommended 1080 × 1920, H.264, < 180 s) | Requirement |
| Exclusions | Not with Offer Details/Ad Disclaimer enabled; not with Deep Link attachment; Public Profile with photo required | Requirement |
| EU and Norway | Help Center says First Snap launches there early June 2026 and auction in July 2026, but also says ads targeting the EU or Norway "will not deliver to Chat Feed at this time" | Conflict; check in account |
| Placement bundling | For Sales, App Promotion and Traffic, Chat Feed can't run alone or be deselected, and is auto-bundled with Discover Feed | Behaviour |
| Impression | Chat cell 50% on screen for ≥ 1 s, or a tap | Definition |

## CTA options by attachment

[Source](https://businesshelp.snapchat.com/s/article/attachment-ctas?language=en_US) · checked 2026-09-16. Choose from the list. Custom CTA text is not documented. Eligible ads may get a Dynamic CTA format and placement.

| Attachment | CTAs |
|---|---|
| Website | Apply Now, Book Now, Buy Tickets, Get Now, Listen, More, Order Now, Play, Read, Shop Now, Show, Showtimes, Sign Up, View, Watch, Donate |
| App Install | Book Now, Download, Get Now, Install Now, Order Now, Play, Shop Now, Sign Up, Use App |
| Lead Form | Apply Now, Book Now, Claim Sample, Free Trial, Get Coupon, Get Now, More, Request Appointment, Request Quote, Sign Up, Test Drive |
| Deep Link | More, Open App, Play, Shop Now, Sign Up, Try, Use App |
| AR Lens | Book Now, Directions, Download, Get Now, Install Now, Order Now, Play, Play Game, Shop Now, Try, Use App, Vote, Watch |

## Not covered in this pass

AR Lens and Filter production specs (formats page only: static filter 945 × 2048 .png; moving filter 720 × 1560 .gif, 1–3 s), Dynamic Product Ads, App Install/Web View/Lead Form attachment specs beyond CTAs, Spotlight-specific differences, First Snap / First Lens / First Story takeovers, and Snap Star collabs.
