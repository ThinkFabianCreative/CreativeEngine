# CTV and programmatic specifications

Checked **2026-09-16**. Public pages only, no logins. Each record shows its source, status and whether a value is an **industry standard** (IAB Tech Lab guidance, itself a recommendation), a **vendor requirement** (a DSP or seller says it must be met), a **vendor recommendation** (best practice, preferred or optimal) or an **observation** (research note). "—" means the inspected source does not publish it. Account availability was not tested for any record.

Status: **DOCUMENTED** = read on an official public page on the date shown. **SOURCE_ISSUE** = official page read, but a field needs confirmation. **UNVERIFIED** = official page could not be read. The value comes from secondary evidence only.

Contents: [1 IAB display sizes](#1-iab-standard-display-sizes) · [2 Display file weight and animation](#2-display-file-weight-and-animation) · [3 HTML5](#3-html5-display) · [4 Programmatic video](#4-programmatic-online-video) · [5 CTV](#5-connected-tv-video) · [6 Vendor quick comparison](#6-vendor-quick-comparison)

---

## 1. IAB standard display sizes

### IAB-001 · IAB New Ad Portfolio, Fixed Size Ad Specifications
Source: [IABNewAdPortfolio_LW_FixedSizeSpec.pdf](https://www.iab.com/wp-content/uploads/2019/04/IABNewAdPortfolio_LW_FixedSizeSpec.pdf), © 2017, listed as current on the [IAB Tech Lab guidelines page](https://iabtechlab.com/standards/iab-new-ad-portfolio-guidelines/) (page dated 2024-02-07). Checked 2026-09-16 · DOCUMENTED

| Ad unit | Fixed size (px) | Initial load max (kB) | Subload max (kB) | Classification |
|---|---|---|---|---|
| Billboard | 970x250 | 250 | 500 | Industry standard |
| Smartphone Banner | 300x50 or 320x50 | 50 | 100 | Industry standard |
| Leaderboard | 728x90 | 150 | 300 | Industry standard |
| Super Leaderboard / Pushdown | 970x90 | 200 | 400 | Industry standard |
| Portrait | 300x1050 | 250 | 500 | Industry standard |
| Skyscraper | 160x600 | 150 | 300 | Industry standard |
| Medium Rectangle | 300x250 | 150 | 300 | Industry standard |
| 120x60 | 120x60 | 50 | 100 | Industry standard |
| Mobile Phone Interstitial | 640x1136, 750x1334 or 1080x1920 | 300 | 600 | Industry standard |
| Feature phone banners | 120x20, 168x28, 216x36 | 5 | — | Industry standard (legacy devices) |

| Field | Value | Classification |
|---|---|---|
| Basis | Units "recommended" from an attitudes-and-usage study of which units drive most revenue | Industry standard |
| 300x600 | Not in the fixed-size table. The complete portfolio lists it as "In Transition" to a 1x2 vertical portrait unit, still allowed for now | Industry standard |
| 320x480, 480x320, 768x1024, 1024x768 | Not IAB fixed-size units. They exist as DSP-supported sizes (see DSP-001, DSP-005) | Observation |
| Size grouping | K-weights for sizes are calculated at double density (2x). Example: 728x90 → 728·90·4 pixels | Industry standard |
| Availability | IAB says the guidelines are industry recommendations that publishers may modify. Consult publishers | Industry standard |

**Common in DSP lists (cross-vendor):** 300x250, 728x90, 160x600, 300x600, 320x50 appear in the DV360 common list, TTD "top display/mobile" lists and Amazon DSP static display. 970x250 appears in all three. 300x50, 320x100, 336x280, 300x1050, 970x90 and 468x60 are common in DV360's list and are absent from the audited sheet.

### IAB-002 · IAB New Ad Portfolio, complete guidelines (LEAN and ad-unit status)
Source: [IABNewAdPortfolio_FINAL_0719.pdf](https://www.iab.com/wp-content/uploads/2019/07/IABNewAdPortfolio_FINAL_0719.pdf) (July 2017 portfolio, 2019 file). Checked 2026-09-16 · DOCUMENTED

| Field | Value | Classification |
|---|---|---|
| Animation length | Must not exceed 15 seconds. No looping beyond 15 seconds | Industry standard |
| Animation start | In-page banners delay animation until the page load event. Animation recommended as part of subload | Industry standard |
| Loop count | — (limit is expressed in seconds, not loops) | — |
| Initial-load file requests | Max 10 | Industry standard |
| File weight measurement | Gzipped. Exempt shared libraries capped at 50 kB combined in initial load | Industry standard |
| Slow connection | For 3G (1.5 Mbps) or slower, weights should be 30% less | Industry standard |
| User-initiated load | Unlimited, after a deliberate user action | Industry standard |
| Audio | Muted by default. User may initiate | Industry standard |
| Delisted | Pop-up/floating, auto-expand, UAP, "Rich Media" as separate units, 970x90 (in status table), 180x150, 88x31 | Industry standard |
| Note on 970x90 | Fixed-size table still lists it (IAB-001) while the status table says "Delist" | See source-conflicts |

---

## 2. Display file weight and animation

| Source | Static image max | Animation | Record |
|---|---|---|---|
| IAB New Ad Portfolio | Static image uses the initial-load weight: 50 kB (320x50) to 150 kB (300x250, 160x600, 728x90), 250 kB (300x600, 970x250), 300 kB phone interstitial | ≤15 s, no looping beyond 15 s | IAB-001/002 |
| Google DV360 | Upload ≤10 MB, ≤4000x4000 px. "Publishers may require smaller file sizes" | HTML5: ≤30 s | DSP-001/002 |
| The Trade Desk | 150 KB or smaller (recommendation for scale). Mobile: 40 KB to 1 MB depending on supply vendor | Max 15 s of looping, then static | DSP-005 |
| Amazon DSP (Amazon and offsite static) | 40 kb (300x250, 728x90, 160x600; 50 kb FR/IT/ES/JP), 50 kb 300x600 and 320x50, 200 kb 970x250 and HTML | — | DSP-009 |
| StackAdapt (probable sheet source) | "Optimal" JPG/PNG 750 KB. GIF max 3.5 MB | — (not recovered) | DSP-012 UNVERIFIED |

**Resolution density:** no inspected IAB or DSP source specifies ppi or dpi for display. All of them specify pixel dimensions and file weight. DV360 recommends uploading images **up to twice the creative dimensions** (a 600x500 image for a 300x250 slot) because it scales by device resolution. Amazon DSP **requires @2x** files for several mobile units and 970x250 onsite. The 72/144 ppi values in the sheet have no support in the standards or DSP pages inspected.

### DSP-001 · Google Display & Video 360, image creatives
Sources: [Guidelines for image creatives](https://support.google.com/displayvideo/answer/3017252?hl=en), [Image creatives](https://support.google.com/displayvideo/answer/7129060?hl=en). Checked 2026-09-16 · DOCUMENTED

| Field | Value | Classification |
|---|---|---|
| File types | JPG, GIF, PNG (RGB) | Vendor requirement |
| Dimensions | ≤4000x4000 px | Vendor requirement |
| File size | ≤10 MB. Publishers may require smaller | Vendor requirement |
| High-density | Upload up to 2x the creative dimensions (600x500 for 300x250) | Vendor recommendation |
| Common sizes | 250x250, 300x250, 320x320, 336x280; 120x600, 160x600, 300x600, 300x1050; 468x60, 728x90, 800x250, 970x90, 970x250; mobile 300x50, 300x100, 320x50, 320x100, 320x480, 360x592, 360x640, 375x667 | Vendor observation ("most common") |
| Standards | "Follow IAB guidelines" | Vendor recommendation |

### DSP-005 · The Trade Desk, display creatives
Source: [Creative Specifications PDF](https://www.thetradedesk.com/assets/global/documents/Creative_Specifications-en.pdf) (undated public PDF). Checked 2026-09-16 · DOCUMENTED

| Field | Value | Classification |
|---|---|---|
| File types | GIF, JPEG, PNG | Vendor recommendation ("to scale across most inventory") |
| File size | 150 KB or smaller (first- and third-party) | Vendor recommendation |
| Animation | Max 15 s of looping, then static | Vendor requirement (stated as restriction) |
| Top display | 160x600, 300x250, 728x90, 300x600 | Vendor recommendation ("optimal") |
| Top mobile | 1024x768, 768x1024, 336x280, 300x50, 320x50 | Vendor recommendation ("optimal") |
| Also supported | Long list including 320x480, 480x320, 970x250, 300x1050, 468x60 | Vendor observation |
| Mobile static | Smartphone 300x50, 300x250, 320x50, 336x280, 320x480. Tablet 300x250, 728x90, 160x600, 468x60, 336x280. 40 KB–1 MB (phone) / 150 KB–1 MB (tablet), depending on supply vendor | Vendor requirement (varies by supply) |
| Borders | Partly black or white backgrounds need a visible contrasting border | Vendor requirement |
| Inventory | Availability varies by exchange and region | Vendor observation |

### DSP-009 · Amazon DSP, desktop and mobile web static display
Source: [Amazon DSP desktop and mobile web static display ads](https://advertising.amazon.com/resources/ad-specs/dsp/desktop). Checked 2026-09-16 · DOCUMENTED

| Unit | Creative dimensions | Max weight | Format | Classification |
|---|---|---|---|---|
| 300x250 | 300x250 | 200 kb HTML; 40 kb static (50 kb FR, IT, ES, JP) | JPG / PNG-8 | Vendor requirement |
| 728x90 | 728x90 | same as above | JPG / PNG-8 | Vendor requirement |
| 160x600 | 160x600 | same as above | JPG / PNG-8 | Vendor requirement |
| 300x600 | 300x600 | 200 kb HTML; 50 kb static | JPG / PNG-8 | Vendor requirement |
| 970x250 | 1940x500 @2x (required onsite, preferred offsite); 800x250 DE | 200 kb | JPG / PNG-8 | Vendor requirement |
| Mobile 320x50 | 640x100 @2x required | 50 kb | JPG / PNG-8 | Vendor requirement |
| Mobile 300x250 | 600x500 @2x required | 40 kb | JPG / PNG-8 | Vendor requirement |
| Tablet 728x90 | 1456x180 @2x required | 200 kb | JPG / PNG-8 | Vendor requirement |
| GIF | Not listed | — | — | Observation |
| Serving | Site served, or third party (iframe only) | — | — | Vendor requirement |

### DSP-012 · StackAdapt, display (probable origin of the sheet's DSP row)
Source: `https://support.stackadapt.com/plan/creative-setup/display-ad-specs`, now 403 and redirected to a restricted (login) page. The [StackAdapt Academy ad specifications](https://academy.stackadapt.com/stackadapt-ad-specifications-global) require registration. Checked 2026-09-16 · **UNVERIFIED**

| Field | Value (secondary evidence only) | Classification |
|---|---|---|
| JPG/PNG | 750 KB "optimal" | Vendor recommendation (UNVERIFIED) |
| GIF | 3.5 MB max | Vendor requirement (UNVERIFIED) |
| Resolution | Min 72 ppi, 144 ppi recommended | Vendor recommendation (UNVERIFIED) |
| Sizes, animation, loops | — (not recovered) | — |

Evidence: web-search index extracts attributed to that StackAdapt URL reproduce the three sheet values together. Do not use as production spec until read on the live page or confirmed by the vendor.

---

## 3. HTML5 display

Not in the audited sheet. Record here because programmatic display buys commonly accept HTML5.

### DSP-002 · Google DV360, HTML5 display
Source: [Guidelines for HTML5 display creatives](https://support.google.com/displayvideo/answer/10261241?hl=en). Checked 2026-09-16 · DOCUMENTED

| Field | Value | Classification |
|---|---|---|
| Packaging | ZIP. Up to 100 files. No ZIP size limit, keep small | Vendor requirement |
| Allowed files | .html .htm .css .js; .jpg .jpeg .gif .png .svg; font files | Vendor requirement |
| Clicks | clickTag; not minified; opens new tab/window | Vendor requirement |
| Animation | ≤30 s | Vendor requirement |
| Audio | Autoplay audio prohibited; muted autoplay video allowed | Vendor requirement |
| Download size | ≤5 MB total served. Publishers may require less | Vendor requirement |
| Cookies / HTTP calls | ≤25 cookies; ≤100 HTTP calls | Vendor requirement |
| Standards | Follow IAB guidelines | Vendor recommendation |

### DSP-006 · The Trade Desk, HTML5
Source: [Creative Specifications PDF](https://www.thetradedesk.com/assets/global/documents/Creative_Specifications-en.pdf). Checked 2026-09-16 · SOURCE_ISSUE

| Field | Value | Classification |
|---|---|---|
| Initial load | 300 KB max (200 KB recommended) | Vendor requirement / recommendation |
| Subload | 600 KB | Vendor requirement |
| File counts | Initial 10; subload 100 | Vendor requirement |
| Total file size | 5 MB | Vendor requirement |
| ZIP | <10 MB compressed, <12 MB uncompressed, ≤100 files, primary HTML at root | Vendor requirement |
| Primary HTML | 100 KB in ZIP table; 200 KB for single-file packaging | Vendor requirement (two values) |
| Backup | Static backup image required (hosted HTML5) | Vendor requirement |
| Meta tag | `ad.size` meta tag recommended (IAB) | Vendor recommendation |
| clickTag | Case-sensitive. Platform default `clickTAG` | Vendor requirement |
| Issue | Individual-file and auto-started video values are scrambled in the PDF text layer ("2.2 MB" / "less than 1.1 MB"). Re-read the rendered PDF before relying on them | SOURCE_ISSUE |

---

## 4. Programmatic online video

This fills the sheet's empty "Programmatic Video Ad" row. Values depend on the DSP, exchange and publisher.

### Cross-source summary

| Field | IAB Tech Lab (IAB-003) | DV360 (DSP-003) | The Trade Desk (DSP-007) | Amazon DSP OLV (DSP-010) |
|---|---|---|---|---|
| Container / codec | MP4, H.264 High + AAC-LC (baseline) | .mp4 etc.; H.264 (best practice) | MP4, WebM (VP8), MOV, MPG | MP4 (H.264/MPEG-2/MPEG-4; AAC) |
| Ratio | 16:9 primary; 9:16, 1:1 placements | 16:9, 4:3, 9:16, 3:4 (square sizes in best practice) | 16:9, 4:3; vertical 9:16 | 16:9; 9:16 (Twitch, APD only) |
| Resolution | Renditions 640x360 → 1920x1080 (→ 3840x2160) | 1920x1080 / 1280x720 / 1440x1080 | 1920x1080 recommended; 640x360 min | 1920x1080 min hosted (640x360 3P) |
| Duration | 6, 15, 20, 30 s (also bumpers 3–10 s, 60 s) | Best practice 15 or 30 s. Buckets <15, 15, 20, 30, 60, ≥90. ~10% tolerance | 5–300 s | 6–120 s. Exactly 6, 15, 20, 30 or 60 s recommended |
| Video bitrate | 1080p 4–10 Mbps (lower end OLV) | ≥20 Mbps upload (best practice) | ≥2500 kbps hosted | Min 4 Mbps (2 Mbps 3P); 8 Mbps recommended |
| Frame rate | Native; 23.976–60 supported | 23.98 or 29.97 | — (CTV table 23.98/29.97) | 23.976 rec., 24, 25, 29.97; constant |
| File size | — | ≤1 GB hosted | 200 MB recommended max | 500 MB (site served) |
| Audio | AAC-LC stereo 128–192 kbps, 48 kHz; -24 LKFS ±2 (US) / -23 LUFS ±1 (EU); ≤ -6 dBTP | PCM/AAC, ≥192 kbps, 48 kHz, -24 LKFS ±2 | — | AAC ≥192 kbps (128 3P), 44.1/48 kHz, 2 ch |
| Tags | VAST (4.x current); SIMID for interactivity; VPAID deprecated | VAST 2.0/3.0/4.0; ≤2 wrappers recommended; VPAID 2.0 via Studio/CM360 | 3P: VAST 2.0, 2.0+VPAID 2.0 JS, 3.0; hosted responses 2.0/3.0/4.1 | Inline VAST 2.0/3.0 (may include VPAID 2); no wrappers |
| Companions | 300x250, 468x60, 300x100, 728x90, 300x60; ~200 kB; no audio/video | 300x250, 728x90, 300x60; image or HTML5 | 300x250, 728x90, 320x50, 160x600, 300x600, 300x50, 320x480, 468x60, 970x250 (JPG/GIF/PNG) | — |

### IAB-003 · IAB Tech Lab Digital Video & CTV Ad Format Guidelines v2.0 (linear and ready-to-serve)
Sources: [CTV Ad Portfolio page](https://iabtechlab.com/standards/ctv-ad-portfolio/) (status Final, 2026-07-22), [v2.0 on GitHub](https://github.com/InteractiveAdvertisingBureau/Ad-Format-Guidelines-for-Digital-Video-CTV/blob/main/v2.0.md) (last commit 2026-06-22). Checked 2026-09-16 · DOCUMENTED

| Field | Value | Classification |
|---|---|---|
| Linear durations | 6, 15, 20, 30 s. Duration "should be exact"; transcoding variance ≤1 s. Also bumpers 3–10 s, 60 s sparingly | Industry standard |
| Aspect ratio | 16:9 preferred for linear; use native ratio; avoid stretching | Industry standard |
| Container/codec | Required H.264 (AVC) High Profile in MP4; optional HEVC, VP9, AV1 in addition, not instead | Industry standard |
| Universally safe format | MP4 + H.264 + AAC-LC is the only format assumable everywhere | Industry standard |
| Renditions | 3–4 ready-to-serve renditions plus a mezzanine | Industry standard |
| Target bitrate (H.264) | ≤480p 1.5–3 Mbps; SD 2–4; 720p 2–5; 1080p 4–10; 2160p 15–30. Lower end OLV/web/mobile, upper end CTV; publishers may cap | Industry standard |
| Bitrate formulas | Bits-per-pixel formulas not recommended | Industry standard |
| Frame rate | 23.976, 24, 25, 29.97, 30, 50, 59.94, 60. Keep native frame rate; avoid converting fractional rates unless required | Industry standard |
| Scan | Progressive only | Industry standard |
| Color | SDR Rec.709 4:2:0 default; HDR10/HLG optional | Industry standard |
| Leaders | No slate, countdown or black frames before/after | Industry standard |
| Audio | AAC-LC required; stereo 128–192 kbps; 48 kHz preferred (44.1 acceptable); optional 5.1 DD+ | Industry standard |
| Loudness | US -24 LKFS ±2 (ATSC A/85); EU -23 LUFS ±1 (EBU R128); peak ≤ -6 dBTP | Industry standard |
| Progressive MP4 | "Web-optimized" (moov atom at start) | Industry standard |

### IAB-004 · Same guidelines, mezzanine file
Source: [v2.0](https://github.com/InteractiveAdvertisingBureau/Ad-Format-Guidelines-for-Digital-Video-CTV/blob/main/v2.0.md). Checked 2026-09-16 · DOCUMENTED

| Field | Value | Classification |
|---|---|---|
| Container | .mov preferred, .mp4 | Industry standard |
| Codec | Apple ProRes preferred, DNxHD/DNxHR; H.264 High if unavailable | Industry standard |
| Bit depth | 8-bit min, 10-bit preferred | Industry standard |
| Resolution / ratio / fps | Native; no upscaling | Industry standard |
| Scan / audio | Progressive; PCM, stereo (5.1 optional), 48 kHz | Industry standard |
| Slate | Not permitted | Industry standard |

### IAB-005 · VAST, VPAID and SIMID status
Source: [IAB Tech Lab VAST](https://iabtechlab.com/standards/vast/); [VAST 4.3 PDF](https://iabtechlab.com/wp-content/uploads/2022/09/VAST_4.3.pdf); [VAST CTV Addendum 2024](https://iabtechlab.com/wp-content/uploads/2024/07/VAST-CTV-Addendum-2024-FINAL.pdf). Checked 2026-09-16 · DOCUMENTED

| Field | Value | Classification |
|---|---|---|
| Latest core VAST | 4.3 (released December 2022 per PDF) | Industry standard |
| VAST CTV Addendum 2024 | Brings current features (SIMID, ACIF ad IDs) to VAST 2.x/3.x environments; "ready for implementation" | Industry standard |
| VPAID | Deprecated, replaced by SIMID (interactivity) and OMID (measurement) | Industry standard |
| Practice in CTV | Many DSPs/sellers still recommend or accept VAST 2.0/3.0 and reject VPAID (DSP-004, DSP-008, CTV-001, CTV-002) | Observation |

### IAB-006 · Video companion ads
Source: [v2.0](https://github.com/InteractiveAdvertisingBureau/Ad-Format-Guidelines-for-Digital-Video-CTV/blob/main/v2.0.md). Checked 2026-09-16 · DOCUMENTED

| Field | Value | Classification |
|---|---|---|
| Common sizes | 300x250, 468x60, 300x100, 728x90, 300x60 | Industry standard |
| File size | 200 kB for most. Check display guidelines | Industry standard |
| Content | No video or audio | Industry standard |

### DSP-003 · Google DV360, video creatives
Source: [Guidelines for video creatives](https://support.google.com/displayvideo/answer/3129957?hl=en). Checked 2026-09-16 · DOCUMENTED

| Field | Value | Classification |
|---|---|---|
| File types | .avi .mov .mp4 .m4v .mpeg .mpg .webm .wmv | Vendor requirement |
| Sizes | Landscape 1280x720, 1920x1080, 1440x1080; portrait 720x1280, 1080x1920, 1080x1440; square 720x720, 1080x1080, 1920x1920 | Vendor recommendation |
| Ratio | Landscape 16:9 or 4:3; portrait 9:16 or 3:4 | Vendor requirement |
| Codec / fps / bitrate | H.264; 23.98 or 29.97; at least 20 Mbps | Vendor recommendation |
| Length | 15 or 30 s (best practice). Inventory buckets <15, 15, 20, 30, 60, ≥90. Shorter videos fit longer slots. Most publishers allow ~10% over | Vendor recommendation / observation |
| Rotation | Rotating creatives within 10% of the longest | Vendor requirement |
| File size | ≤1 GB hosted; transcoded serving files ≤10 MB | Vendor requirement |
| Black bars | No black bars, no letterboxing | Vendor recommendation |
| Audio | PCM (preferred) or AAC; ≥192 kbps; 16/24-bit; 48 kHz; -24 LKFS ±2 (CM360 normalizes to -24) | Vendor recommendation |
| File name | ≤50 characters, ASCII only | Vendor requirement |
| VAST | 2.0, 3.0, 4.0; ≤2 wrappers recommended | Vendor requirement / recommendation |
| VPAID | HTML5 VPAID 2.0 via Studio/CM360 only | Vendor requirement |
| Companions | Image or HTML5; include 300x250, 728x90, 300x60; "20K"; 15 s animation; 18–24 fps | Vendor recommendation |

### DSP-007 · The Trade Desk, video creatives
Source: [Creative Specifications PDF](https://www.thetradedesk.com/assets/global/documents/Creative_Specifications-en.pdf). Checked 2026-09-16 · DOCUMENTED

| Field | Value | Classification |
|---|---|---|
| Hosted file types | MP4, WebM (VP8), MOV, MPG, MPEG | Vendor requirement |
| Hosted file size | 200 MB recommended max | Vendor recommendation |
| Hosted formats | 16:9 640x360 min, 1920x1080 rec.; 4:3 480x360 min, 640x480 rec. | Vendor requirement / recommendation |
| Hosted bitrate | ≥2500 kbps; lower supported but limited demand | Vendor recommendation |
| Duration | 5–300 s. Requests use max-duration buckets; a shorter ad can fill a longer slot | Vendor requirement |
| 3P VAST | VAST 2.0, 2.0 + VPAID 2.0 JS, 3.0. Include MP4, WebM, FLV media for scale | Vendor requirement / recommendation |
| Vertical | 1080x1920, 9:16, min height 400 px | Vendor recommendation |
| Companion | JPG, GIF, PNG; 300x250, 728x90, 320x50, 160x600, 300x600, 300x50, 320x480, 468x60, 970x250 | Vendor requirement |
| Resolution tiers | Low ≤360p 500–700 kbps; SD 700–1500; 720p 1500–2500; 1080p 2500–3500 | Vendor recommendation |
| UK | CBA: pre-roll over 31 s combined must be skippable within 6 s; no mid-roll | Vendor-cited regulation |

### DSP-010 · Amazon DSP, online video (OLV)
Source: [Online video (OLV) ad specs](https://advertising.amazon.com/resources/ad-specs/dsp/video/online-video-ads). Checked 2026-09-16 · SOURCE_ISSUE

| Field | Value | Classification |
|---|---|---|
| File size | 500 MB (site served) | Vendor requirement |
| Ratio | 16:9; 9:16 on Twitch and Amazon Publisher Direct only | Vendor requirement |
| Duration | Min 6 s, max 120 s; exactly 6, 15, 20, 30 or 60 s recommended | Vendor requirement / recommendation |
| Min frame | 1920x1080 (640x360 3P); vertical 1080x1920 (360x640 3P) | Vendor requirement |
| Bitrate | Min 4 Mbps (2 Mbps 3P); 8 Mbps recommended | Vendor requirement / recommendation |
| Frame rate | 23.976 (rec.), 24, 25, 29.97; constant | Vendor requirement |
| Audio | AAC; ≥192 kbps (128 3P); 44.1 or 48 kHz; ≥2 channels | Vendor requirement |
| Tags | Inline VAST 2.0/3.0, "may include VPAID 2". Same sentence says "We do not accept VPAID or Wrapper Tags" | SOURCE_ISSUE (contradictory) |

---

## 5. Connected TV video

### CTV cross-source summary

| Field | IAB (IAB-003) | DV360 CTV | TTD CTV | Amazon STV/Prime Video | Disney+/Hulu | Roku self-serve |
|---|---|---|---|---|---|---|
| Resolution | 1920x1080 (CTV); up to 3840x2160 | 1920x1080 pref.; 1280x720 | 1920x1080 mezz./HQ | ≥1920x1080 | 1920x1080 pref.; 1280x720 | — |
| Ratio | 16:9 | — | — | 16:9 | 16:9 required; 1:1, 9:16 rejected | 16:9 required |
| File | MP4 H.264 High | MP4 only | MP4 only | H.264/MPEG-2/MPEG-4; MP4 site served | MOV/MP4/M4V; ProRes 422 HQ or H.264 | MOV/MP4; AVC or ProRes 422 HQ |
| Video bitrate | 15–30 Mbps upper CTV (2160p band) / 4–10 Mbps 1080p | Mezz. 15–30 Mbps; 1080p serve 2.5–3.5 Mbps | Mezz. ≥15 Mbps (15–30) | Min 15 Mbps Prime Video, 8 Mbps others; 50 Mbps rec. Prime Video | CBR 10–40 Mbps; programmatic CBR 15–60 pref. | Min 6 Mbps |
| Frame rate | Native; 23.976–60 | 23.98, 29.97 (25 PAL) | 23.98, 29.97 | 23.976 rec., 24, 25, 29.97 | 23.98, 24, 25, 29.97, 30, native | 23.98, 25, 29.97 |
| Scan / telecine | Progressive | No telecine, interlace, duplicate frames | Constant fps; no telecine/interlace/duplicates | Constant fps | Progressive; constant fps | — |
| Max file size | — | 1 GB hosted | Mezz. 10 GB | 500 MB | 1.9 GB partner/VAST/programmatic; 250 MB Hulu-served | 1 GB |
| Audio | AAC-LC, 48 kHz, 128–192 kbps | 192 kbps, 48 kHz | 48 kHz, ≥192 kbps | AAC ≥192 kbps, 44.1/48 kHz, ≥2 ch | AAC/PCM, 2 ch, ≥128 kbps, 44.1/48 kHz | PCM pref./AAC, ≥96 kbps, 48 kHz, stereo |
| Loudness | -24 LKFS ±2 US; -23 LUFS ±1 EU; ≤ -6 dBTP | — | Average -24 LKFS (best practice) | — | — | — |
| Durations | 6, 15, 20, 30 (+ bumpers, 60) | — | — | Varies by market (US Prime Video 15/30/45/60; 3P apps 6–90) | — | 6–92 s |
| Tags | VAST (+SIMID) | VAST 2.0 rec.; 3.0/4.0 limited scale; no VPAID/MRAID/wrapping on most devices | VAST only; no VPAID; 3.0/4.0 less scalable | Inline VAST 2.0/3.0; no VPAID/wrappers | VAST 2.0/3.0 approved vendors; no wrappers; no VPAID | — |
| Leaders / bars | No slate/countdown/black | — | — | Letter/pillarbox strongly discouraged | No slates/countdowns; no letter/pillarbox (exceptions by approval) | — |
| Safe area | — | — | — | Action-safe image provided (downloadable) | "Safety Zones" variants exist (not transcribed) | — |
| Clickability | Limited on CTV | Non-skippable | No click-through on CTV devices | No click-bait CTA in non-interactive ads | Clickable-looking CTAs not allowed; QR accepted with review | — |

### DSP-004 · Google DV360, Connected TV creatives
Source: [Connected TV creatives](https://support.google.com/displayvideo/answer/14175098?hl=en). Checked 2026-09-16 · DOCUMENTED

| Field | Value | Classification |
|---|---|---|
| Format | MP4 (FLV, WebM unsupported) | Vendor requirement |
| Tags | VAST 2.0 recommended; 3.0/4.0 supported with more limited scale; VPAID, MRAID, wrapping unsupported on most CTV devices | Vendor recommendation / requirement |
| Resolution | 1920x1080 preferred (mezzanine, HQ); 1280x720 | Vendor recommendation |
| Bitrate | Mezzanine 15,000–30,000 kbps; HQ 1,500–2,500 (720p) / 2,500–3,500 (1080p); medium 700–1,500; low 500–700 | Vendor recommendation |
| Frame rate | 23.98 or 29.97; 25 PAL | Vendor recommendation |
| Audio | 192 kbps; 48 kHz | Vendor recommendation |
| File size | 1 GB max upload (DV360-hosted) | Vendor requirement |
| Frames | Avoid telecine, interlacing, duplicate frames | Vendor recommendation |
| Versions | Provide high, medium, low ready-to-serve plus mezzanine | Vendor recommendation |

### DSP-008 · The Trade Desk, CTV creatives
Source: [Creative Specifications PDF](https://www.thetradedesk.com/assets/global/documents/Creative_Specifications-en.pdf). Checked 2026-09-16 · SOURCE_ISSUE

| Field | Value | Classification |
|---|---|---|
| File | MP4 only (hosted auto-converted); WebM unsupported | Vendor requirement |
| Tags | VAST only; VPAID not supported; VAST 3.0/4.0 typically less scalable | Vendor requirement / observation |
| Frame | Constant frame rate; no telecine, interlacing, duplicate frames | Vendor requirement |
| Mezzanine | 1920x1080, ≥15,000 kbps (15,000–30,000), max 10 GB, 23.98/29.97, 48 kHz, ≥192 kbps | Vendor requirement |
| HQ / medium / low | 1920x1080 4,000–6,500 kbps; 1280x720 1,200–3,500; 1280x720 500–1,200 | Vendor recommendation |
| Loudness | Average -24 LKFS | Vendor recommendation (best practice) |
| Clicks | No click-through on CTV devices | Vendor requirement |
| Publisher specs | Bitrates vary drastically by publisher; Hulu-hosted min 15,025 kbps | Vendor observation |
| Issue | "Typically a minimum of 1200–1500 kbps… 1.6–3.2 Mbps preferred" conflicts with the mezzanine ≥15,000 kbps requirement and the tier table | SOURCE_ISSUE |

### DSP-011 · Yahoo DSP, CTV
Source: [Connected TV (CTV) – Yahoo Ad Specs](https://adspecs.yahooinc.com/video-ads/video-ctv). Checked 2026-09-16 · DOCUMENTED (read through a fetch summary; not re-read as raw text)

| Field | Value | Classification |
|---|---|---|
| Resolution | 1920x1080 16:9 preferred; 1280x720; 1440x1080 (4:3) | Vendor requirement |
| Files | MOV, MP4 | Vendor requirement |
| Bitrate | CBR or VBR 15–60 Mbps | Vendor requirement |
| Frame rate | 29.97 or 23.976; constant | Vendor requirement |
| Audio | ≥192 kbps; 16/24-bit; 48 kHz | Vendor requirement |
| File size | 300 MB max | Vendor requirement |
| Color | 4:2:2 | Vendor requirement |
| Tags | VAST 2.0 and 3.0; non-skippable; ≤3 wrappers | Vendor requirement |

### DSP-013 · Quantcast, CTV
Source: [Creative Specifications (CTV)](https://help.quantcast.com/docs/creative-specifications-ctv) (updated 2024-05-20). Checked 2026-09-16 · DOCUMENTED (fetch summary)

| Field | Value | Classification |
|---|---|---|
| Ratio / size | 16:9; 1920x1080 minimum | Vendor requirement |
| Duration | :15 and :30 recommended; under :30 limited inventory | Vendor recommendation |
| Tags | 3P tags or VAST 2.0/3.0/4.0; no VPAID wrappers | Vendor requirement |
| File | .mp4 or .mov; up to 1 GB Quantcast-hosted (10 GB 3P) | Vendor requirement |
| Bitrate | 18,000–30,000 kbps | Vendor requirement |
| Frame rate | Constant 24, 25 (PAL) or 30 (NTSC) | Vendor requirement |
| Audio | 48 kHz | Vendor requirement |

### DSP-014 · Propensity Display Network, CTV
Source: [Using Connected TV (CTV) Ads](https://support.propensity.com/hc/en-us/articles/28306109014043) (updated 2026-04-03; read through the public Help Center API). Checked 2026-09-16 · DOCUMENTED

| Field | Value | Classification |
|---|---|---|
| General | 1920x1080 (1080p recommended); 16:9 recommended; MP4; up to 1 GB | Vendor requirement / recommendation |
| Duration | 15 or 30 s recommended; others "may experience limited scale"; max 60 s | Vendor recommendation / requirement |
| Premium publishers | 10–15 Mbps (15 recommended); H.264; 1920x1080; AAC 48 kHz ≥192 kbps | Vendor requirement |
| Frame rate by publisher | Disney+/Hulu, Paramount, WBD: 23.98, 24, 25, 29.97, 30; NBCU/Peacock: 23.98, 25, 29.97; DHXP: 23.98, 29.97 | Vendor requirement |
| Other | Raw MP4; no letter/pillarboxing; no duplicate/deinterlaced frames; no telecine or 3:2 pulldown | Vendor requirement |

### CTV-001 · Amazon Streaming TV and Prime Video ads
Source: [Streaming TV & Prime Video ad specs](https://advertising.amazon.com/resources/ad-specs/dsp/video/streaming-tv-prime-video-ads). Checked 2026-09-16 · DOCUMENTED

| Field | Value | Classification |
|---|---|---|
| File size | 500 MB max | Vendor requirement |
| Ratio / frame | 16:9; min 1920x1080 | Vendor requirement |
| Video bitrate | Min 15 Mbps Prime Video; 8 Mbps Twitch, Fire TV Channels, 3P apps/exchanges. 50 Mbps recommended for Prime Video | Vendor requirement / recommendation |
| Frame rate | 23.976 (rec.), 24, 25, 29.97; constant | Vendor requirement |
| Codecs | H.264, MPEG-2 or MPEG-4 video; AAC audio; site serving requires MP4 | Vendor requirement |
| Audio | ≥192 kbps; 44.1 or 48 kHz; ≥2 channels | Vendor requirement |
| Durations (US) | Prime Video 15/30/45/60; Twitch 15/30; Fire TV Channels 15/30/45/60/90; 3P STV apps 6–90 (6, 10, 15, 20, 30, 45, 60, 75, 90). 3P exchange: any, at publisher discretion | Vendor requirement |
| Durations (other) | UK/DE/FR/IT/ES/BR/IN Prime Video 10/15/20/30/40/60; JP 15/30; MX/AU 15/20/30/40/60 | Vendor requirement |
| Bars | Pillar/letterbox strongly discouraged; allowed if not mixed in the same ad | Vendor recommendation |
| CTA | Non-interactive ads must not include click-style CTAs | Vendor requirement |
| Tags | Inline VAST 2.0 or 3.0 from certified vendors; no VPAID, no wrappers | Vendor requirement |
| Safe zone | Recommended action-safe template for Prime Video and interactive formats (image download; values not transcribed) | Vendor recommendation |
| Loudness | — | — |

### CTV-002 · Disney+ and Hulu video commercial
Source: [Video Commercial – Disney Advertising MediaKit](https://products.disneyadvertising.com/video-commercial/). Checked 2026-09-16 · SOURCE_ISSUE

| Field | Value | Classification |
|---|---|---|
| Resolution | 1920x1080 preferred; 1280x720 accepted | Vendor requirement |
| Ratio | 16:9 required; 1:1 and 9:16 rejected | Vendor requirement |
| Bars | No letterboxing or pillarboxing (exception by approval) | Vendor requirement |
| Bitrate | CBR 10–40 Mbps (HD); programmatic CBR 15–60 Mbps preferred, VBR 20–60 accepted | Vendor requirement |
| Profile / color | Main Profile @ Main Level; 4:2:2; single video track | Vendor requirement |
| Files / codec | MOV, MP4, M4V; ProRes 422 HQ or H.264 | Vendor requirement |
| Max file weight | Partner, VAST or programmatic 1.9 GB; Hulu-served 250 MB | Vendor requirement |
| Frame rate | 23.98, 24, 25, 29.97 or 30 based on native; constant; progressive | Vendor requirement |
| Audio | Required; 2 channels; ≥128 kbps CBR; 44.1/48 kHz; AAC or PCM; one track matching duration | Vendor requirement |
| Tags | VAST 2.0 and 3.0 from approved vendors; no wrappers; no VPAID; programmatic VAST only, secure | Vendor requirement |
| Leaders | No slates, countdowns | Vendor requirement |
| CTA / QR | No clickable-looking CTA buttons; URLs, hashtags accepted; QR codes accepted subject to review | Vendor requirement |
| Issue | "Main Profile @ Main Level" (an MPEG-2-era label) alongside 1080p H.264 and 15–60 Mbps; page also shows template filler text. Confirm with Disney | SOURCE_ISSUE |
| Durations / loudness | — (not on the inspected page tabs) | — |

### CTV-003 · Roku self-serve (Roku Ads Manager)
Source: [Creative technical requirements](https://help.ads.roku.com/en/articles/7193013-creative-technical-requirements) (dated March 11, 2025). Checked 2026-09-16 · DOCUMENTED

| Field | Value | Classification |
|---|---|---|
| File | .mov or .mp4; ≤1 GB; file name ≤170 characters | Vendor requirement |
| Length | 6–92 s | Vendor requirement |
| Ratio | 16:9 | Vendor requirement |
| Frame rate | 23.98, 25.00, 29.97 | Vendor requirement |
| Codec | AVC or ProRes 422 HQ | Vendor requirement |
| Bitrate | Video ≥6 Mbps; audio ≥96 kbps | Vendor requirement |
| Audio | PCM preferred, AAC accepted; 16/24-bit; stereo; 48 kHz; length matches video | Vendor requirement |
| Action ads | Overlay message ≤40 chars; logo PNG ≤150 kb; text message ≤236 chars | Vendor requirement |
| Scope | Roku self-serve only. Managed Roku buys may differ | Observation |

### IAB-007 · IAB CTV Ad Portfolio (new non-linear CTV formats)
Source: [CTV Ad Portfolio](https://iabtechlab.com/standards/ctv-ad-portfolio/); [v2.0](https://github.com/InteractiveAdvertisingBureau/Ad-Format-Guidelines-for-Digital-Video-CTV/blob/main/v2.0.md). Checked 2026-09-16 · DOCUMENTED

| Field | Value | Classification |
|---|---|---|
| Status | Final 2026-07-22 (comment rounds closed 2026-01-31 and July 2026) | Industry standard |
| Formats | Pause, Screensaver, Menu, In-Scene Insertion, Overlay (2 variants), Squeezeback (5 variants) | Industry standard |
| Static assets | If display/static, file size under 350 kB | Industry standard |
| Video assets | Follow ready-to-serve or mezzanine guidance (IAB-003/004) | Industry standard |
| Interactivity | SIMID recommended; QR codes burned-in or sell-side generated | Industry standard |
| Relevance | Not a replacement for :15/:30 linear commercials; separate product specs apply per seller | Observation |

---

## 6. Vendor quick comparison

| Question | Short answer | Evidence |
|---|---|---|
| Is there one CTV spec? | No. Bitrate minimums range from 6 Mbps (Roku self-serve) to 15 Mbps (Prime Video) to 15–60 Mbps CBR (Disney programmatic). File caps range from 250 MB to 10 GB | CTV-001–003, DSP-004/008/011 |
| Safest CTV master | 1920x1080, 16:9, progressive, constant native frame rate (23.976/29.97 widest), H.264 High MP4 at 15–30 Mbps plus a ProRes mezzanine, AAC/PCM stereo 48 kHz, -24 LKFS ±2, no slate or bars, exact :15/:30 | Convergence of IAB-003/004, DSP-004, CTV-001/002. Still confirm with seller |
| Safest display set | Pixel-exact 300x250, 728x90, 160x600, 300x600, 320x50, 970x250 (plus 2x where DSP scales), ≤150 kB static for broad scale, ≤15 s animation | IAB-001/002, DSP-001/005/009 |
| VAST version | CTV sellers still ask for VAST 2.0/3.0 inline. IAB current is 4.3 plus 2024 CTV addendum. VPAID is deprecated and widely rejected on CTV | IAB-005, DSP-004/008, CTV-001/002 |
