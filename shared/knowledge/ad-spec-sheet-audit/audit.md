# Audit: "Digital Ad Spec Sheet - Updated"

Audited **2026-09-16** against public official platform, standards-body and media-owner pages. Raw sheet: [snapshot](sheet-snapshot-2026-09-16.md). No ad account was opened, so every finding is documentation-level; availability is NOT TESTED.

## Verdict

**The sheet is out of date and should not be used as a production reference.** No row is fully current. It names no sources and no check dates, several rows copy another format's or another market's specs, and three cells contradict themselves.

| Status | Rows |
|---|---|
| OUTDATED | Google Responsive Display, YouTube, TikTok In-Feed |
| PARTLY OUTDATED | Google Responsive Search (incomplete), Performance Max, Meta Static, Meta Carousel, Meta Video, Snapchat, LinkedIn Single Image, Nextdoor Display, Nextdoor Video, Connected TV, Programmatic Display, Digital OOH tab |
| INCOMPLETE | Nextdoor Spotlight, Programmatic Video (empty) |

Where the sheet came from, where it could be traced:

- **Digital OOH tab:** a Vistar Media venue spec list from December 2023. Vistar now says plan-specific Deal Desk specs are the source of truth.
- **Nextdoor rows:** Nextdoor's **UK** page, word for word. The US page differs substantially.
- **TikTok copy rules:** TikTok's Global App Bundle (CapCut/Fizzo) pages, not TikTok In-Feed.
- **Programmatic Display:** probably StackAdapt (unconfirmed; the page is now behind a login).
- **Responsive Display copy:** pasted from Responsive Search Ads.

The replacement is the per-platform modules below. Each carries source URLs, requirement vs recommendation labels and open conflicts.

## Row-by-row findings

"Req" means a hard platform requirement; "rec" means a recommendation. Source URLs are in each module.

### Google Ads and YouTube → [google-youtube-ads](../google-youtube-ads/README.md)

| Row | Verdict | Key corrections |
|---|---|---|
| Responsive Search | PARTLY OUTDATED | Headlines 3–15 (not "15x"), descriptions 2–4. Missing: 2 × 15-char display paths, business name 25, logo, CJK characters count double |
| Responsive Display | OUTDATED | Copy is RSA's. Actual: 1–5 headlines (30), 1 long headline (90), 1–5 descriptions (90), business name 25 (req). Images 1–15 per ratio, not 2. **JPG/PNG only, no GIF** (req). Logo 1:1 1200×1200 is the main logo; 4:1 is optional. No text/logo overlays on images |
| YouTube | OUTDATED | Max file **256 GB**, not 128 GB. Skippable has no maximum (under 3 min rec). Non-skippable: official pages disagree (7–15 s, 15–60 s, ≤60 s). Recommends 16:9, 9:16 and 1:1, not 16:9 only. Video action campaigns moved to Demand Gen (May 2026). Missing: bumper, in-feed, Shorts, masthead, thumbnail and companion specs |
| Performance Max | PARTLY OUTDATED | Headlines 3–15 with at least one ≤15; long headlines 1–5; descriptions 2–5 with **no verified 60-char rule**. Missing: square logo required, minimum image sizes, business name, video assets (Google auto-generates video if none supplied). Sheet's Help link is now a general index |
| *(missing)* Demand Gen | — | 40-char headlines, 4:5 and 9:16 images, 2–10 card carousels |

### Meta → existing [meta-paid-ads](../meta-paid-ads/README.md) (researched 2026-09-12)

| Row | Verdict | Key corrections |
|---|---|---|
| Static | PARTLY OUTDATED | Feed recommendation is now **4:5 at 1440×1800**, not 1:1 at 1080. Stories/Reels recommend **1440×2560**. Facebook Feed recommends a 27-char headline; Instagram Feed 40. The 30-char description is not a published value for these placements |
| Carousel | PARTLY OUTDATED | Text recommendations vary by placement (Facebook Feed 80/20/18; Instagram Feed 125 primary). Cards 2–10. Stories/Reels safe zone is **14% top, 35% bottom, 6% sides**, not 14% top and bottom (Facebook Stories carousel says 14/20). Facebook Stories carousel is images only, 3–10 cards |
| Video | PARTLY OUTDATED | Max length is placement-specific, not 10 minutes (Facebook Feed up to 241 min, Instagram Stories 60 min, Facebook Stories 3 min). Instagram Reels accepts MP4/MOV only, no GIF. Facebook Feed recommends 4:5, not 1:1 |

### TikTok → [tiktok-ads](../tiktok-ads/README.md) · Snapchat → [snapchat-ads](../snapchat-ads/README.md)

| Row | Verdict | Key corrections |
|---|---|---|
| TikTok In-Feed | OUTDATED | Copy rules belong to Global App Bundle ads. In-Feed: account name shows 20 chars max (4–10 rec); caption 100; emojis allowed (count as 2). Auction In-Feed now runs **up to 10 minutes**; 5–60 s applies to reservation In-Feed and TopView, which also require ≥2,500 kbps. Missing: safe-zone templates, Spark Ads, carousel (2–35 images), TopView, CTA list |
| Snapchat | PARTLY OUTDATED | Brand name 32 / headline 34 matches the specs page, but another Snap page says brand name 25; write ≤25 to be safe. Length is not 3–10 s: specs page allows 3 s–30 min (other Snap pages cap at 3 min); Snap recommends 3–6 s, not 15–30. File sizes: **video 1 GB, image 5 MB**; "32 MB" is obsolete. Storage aspect ratio is 9:16, not 1:1. Image minimum 720×1280. Safe zone: 10% top, 35% bottom, 6% sides plus a lower-right strip |

### LinkedIn → [linkedin-ads](../linkedin-ads/README.md) · Nextdoor → [nextdoor-ads](../nextdoor-ads/README.md)

| Row | Verdict | Key corrections |
|---|---|---|
| LinkedIn Single Image | PARTLY OUTDATED | The sheet's numbers are truncation recommendations; hard maxima are headline 200, intro 3,000, description 300 (and description 100 rec, not 70). Only recommended vertical is now **4:5 at 720×900**; 1:1.91 gets side borders. Missing: carousel, video, document, event, Thought Leader and other formats |
| Nextdoor Display | PARTLY OUTDATED | UK values. US Ads Manager: "Image ad", 1.91:1 or 1:1, JPEG/PNG only, up to 150 MB; advertiser name 70, headline 70, body 1,700, CTA 45; no offer-text field; circular logo crop. "CTR +15%" is a Nextdoor marketing claim, not a spec |
| Nextdoor Video | PARTLY OUTDATED | US: 2–300 s (<30 s rec), 16:9 or 1:1, up to 500 MB, auto thumbnail |
| Nextdoor Spotlight | INCOMPLETE | Matches UK page; not listed on US specs page (US pilot only). "Creative assistance" condition undefined |

### Connected TV and programmatic → [ctv-programmatic-ads](../ctv-programmatic-ads/README.md)

| Row | Verdict | Key corrections |
|---|---|---|
| Connected TV | PARTLY OUTDATED | One vendor's spec presented as universal. File caps vary: 1 GB fails Amazon (500 MB), Yahoo (300 MB), Hulu-served (250 MB). "Above 7 Mbps" has no official support; minimums run 6–15 Mbps by seller. Accepted frame rates vary by seller. Missing: **loudness −24 LKFS ±2 (US)** / −23 LUFS (EU), AAC stereo ≥192 kbps, no slates, no letterboxing, VAST without VPAID. IAB published new video/CTV guidelines on 2026-07-22 |
| Programmatic Display | PARTLY OUTDATED | 320×480, 480×320, 768×1024 and 1024×768 are DSP sizes, not IAB standard units. File weight far too high: IAB 50–150 KB (250 KB for 300×600 and 970×250), The Trade Desk ≤150 KB, Amazon 40–200 KB with no GIF. **No official source sets a ppi rule**; screens use pixel dimensions, with 2× export where the DSP supports it. No source documents "3 loops". Missing: HTML5 specs, common sizes (300×50, 320×100, 336×280, 300×1050, 970×90) |
| Programmatic Video | INCOMPLETE (empty) | Baseline: MP4 H.264 + AAC, 1920×1080, exactly 6/15/20/30 s, constant native frame rate, 48 kHz, −24 LKFS, VAST 3.0+ with no VPAID, companions 300×250 / 728×90 / 300×60. Confirm with the actual DSP |

### Digital OOH → [dooh-ads](../dooh-ads/README.md)

**PARTLY OUTDATED and INCOMPLETE.** Transcribed from Vistar's December 2023 list; most numbers copy correctly, but:

- Vistar now publishes five standard sizes (1080×1920, 1280×960, 1920×1080, 840×400, 1400×400), accepts video only via VAST, prefers JPEG and says plan-specific Deal Desk specs govern.
- Dropped conditions: Movie Theaters 3840×1080 is :15 only; Office Buildings 1080×1920 is :15 only; Train Stations sizes 1920×1080, 1080×1920 and 1400×400 are static-only (sheet says video); Taxi TV 640×360 is video-only.
- Not in any source: Schools, Spas, billboard sizes 990×495 and 806×390, Fueling ":30 with approval", Subway durations.
- Unlabeled rows are extra rows for the same venue type, not separate owners.
- Missing: file types and sizes, audio-on venues, approval lead times (3–10 business days), roadside billboard rules (many US states restrict motion and require 6–10 s holds, per a 2019 OAAA summary), legibility guidance. Venue labels predate OpenOOH taxonomy 1.2.1.

## Using this audit

1. Don't update the Google Sheet from this page alone. Take values from the linked module records, which separate requirements from recommendations and keep conflicts open.
2. For programmatic, CTV and DOOH, the media vendor's plan-specific spec sheet outranks everything here.
3. Recheck the official page before production. Several platforms changed specs within the last year.

## Research limits

- Public pages only, read 2026-09-16; some through a summarizing fetch tool. Spot-check Google pages before production.
- Not read: StackAdapt (login), TikTok safe-zone template ZIPs, Vistar's live spec dashboard, Nextdoor's help center (JS/under construction), VIOOH and Hivestack public specs.
- No upload, review or delivery test was performed.
