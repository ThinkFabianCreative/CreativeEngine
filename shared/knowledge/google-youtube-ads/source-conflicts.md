# Source conflicts and coverage gaps

Checked 2026-09-16. Observed documentation issues and research limits, not invented rules. Records are in [specs.md](specs.md) and [specifications.json](specifications.json). Each conflict stays OPEN until an account build or a newer official page resolves it.

## Conflicts between official pages

| Record | Issue | Sources | Working rule until resolved |
|---|---|---|---|
| GOOG-001 | RSA minimums: About RSA says at least 3 headlines and 2 descriptions; Search specs table shows 1–15 and 1–4 | [7684791](https://support.google.com/google-ads/answer/7684791), [17092074](https://support.google.com/google-ads/answer/17092074) | Write at least 3 headlines and 2 descriptions |
| GOOG-002 | RDA square image recommended size: 600 × 600 on the RDA specs page; 1200 × 1200 on the create page, best-practices page and image policy | [17090561](https://support.google.com/google-ads/answer/17090561), [7005917](https://support.google.com/google-ads/answer/7005917), [10347108](https://support.google.com/adspolicy/answer/10347108) | Export 1200 × 1200; min 300 × 300 is consistent |
| GOOG-002 | RDA vertical: best-practices page lists 9:16 images (900 × 1600, min 600 × 1067); specs page lists no vertical image and a 2:3 vertical video | [9823397](https://support.google.com/google-ads/answer/9823397), [17090561](https://support.google.com/google-ads/answer/17090561) | Treat vertical image as optional and account-dependent |
| GOOG-003 | PMax image minimum count: "4+" sits in the Recommended column, alongside a Required tick with no number | [17091269](https://support.google.com/google-ads/answer/17091269) | Plan 4+ per required ratio; confirm publish minimum in account |
| GOOG-003 | A "description of 60 characters or fewer" is not stated on any inspected PMax page | [14528373](https://support.google.com/google-ads/answer/14528373) | UNVERIFIED; harmless to include one short description, not a documented rule |
| GOOG-004/006 | Demand Gen logo minimum 144 × 144 (image and specs pages) vs 128 × 128 (video page) | [17140672](https://support.google.com/google-ads/answer/17140672), [17141078](https://support.google.com/google-ads/answer/17141078) | Supply at least 144 × 144 (1200 × 1200 recommended) |
| GOOG-004–006 | Demand Gen logo file cap 150 KB, while PMax and RDA logos share the 5120 KB image cap | [13704860](https://support.google.com/google-ads/answer/13704860), [17091269](https://support.google.com/google-ads/answer/17091269) | Keep reusable logos under 150 KB |
| GOOG-006 | Demand Gen video length: min 5 s, under 10 s ineligible for in-stream, 15 s+ recommended (video page) vs 10–60 s recommended (specs page) | [17141078](https://support.google.com/google-ads/answer/17141078), [17091672](https://support.google.com/google-ads/answer/17091672) | Cut 10 s+; 15–60 s covers both |
| YT-003 | Non-skippable length: "60 seconds or shorter" (Google Ads formats page); "15–60 s depending on subtype" (YouTube Help); 7–15 s and CTV 16–30 s (video reach creation page) | [2375464](https://support.google.com/google-ads/answer/2375464), [YouTube 2375464](https://support.google.com/youtube/answer/2375464), [10510238](https://support.google.com/google-ads/answer/10510238) | Confirm per campaign subtype |
| YT-005 | In-feed text: headline 100 characters (25 may truncate) and 2 × 35 description lines (in-feed page) vs 2 × 40 headline lines (video specs page) vs 40 (Demand Gen) vs 90 long headline (video reach) | [6227733](https://support.google.com/google-ads/answer/6227733), [17091270](https://support.google.com/google-ads/answer/17091270) | Limits depend on campaign type; front-load meaning in the first 25 characters |
| YT-007 | Video specs page still lists "Video action campaigns" text fields (headline 30, long headline 90, description 90, CTA 10), but video action campaigns were upgraded to Demand Gen as of May 2026 | [17091270](https://support.google.com/google-ads/answer/17091270), [10147229](https://support.google.com/google-ads/answer/10147229) | Use Demand Gen limits (GOOG-006) for new action-oriented video work |
| YT-006 | Shorts page says uploads up to 3 minutes; the page also indicates only the first 60 s plays in the Shorts feed; under 60 s recommended | [16041697](https://support.google.com/google-ads/answer/16041697) | Cut under 60 s |

## Ambiguities

- The sheet's specs link [13676244](https://support.google.com/google-ads/answer/13676244) is now a cross-campaign hub. Per-campaign specs pages (170xxxxx IDs) carry the tables.
- Several Google spec tables use Recommended and Required columns. A count in Recommended is not a publish minimum.
- Safe zones for YouTube video are published only as downloadable PNG templates. No numeric pixel or percentage values were found in page text. The image "center 80%" is a recommendation, not a policy requirement.
- "426 × 240 to 3840 × 2160" is YouTube general upload guidance; the ad spec page publishes 1080p recommended and 720p/SD accepted.
- Text fetched through a summarizing reader. Values were cross-checked with a second targeted read where they looked anomalous (PMax table headers, RDA 600 × 600, video reach lengths). Recheck before production.

## Coverage not verified

- Availability in any real account, market, language, vertical or campaign subtype. No account was opened.
- App campaigns, Shopping and Merchant Center product feeds, Demand Gen product ads, uploaded display image and HTML5 ads, Discovery/Gmail rendering details.
- Search assets beyond business name, logo and images: sitelinks, callouts, structured snippets, price, promotion, call and lead form assets.
- Masthead policy page (adspolicy 14540749), CTV-only formats, audio ads, YouTube Select, partnership (creator) ads.
- Video bitrate, frame rate and audio loudness.
- Upload acceptance, ad review, Ad Strength scoring, rendering previews and performance.
