# Snapchat: source conflicts, ambiguities and coverage gaps

Checked 2026-09-16. These are disagreements between official Snap pages, not invented restrictions. Help Center articles show no "last updated" date, so recency can't settle them. Every conflict stays OPEN until an Ads Manager check or Snap confirmation resolves it.

Sources: Help Center [Single Image or Video specs](https://businesshelp.snapchat.com/s/article/top-snap-specs?language=en_US) (HC-SPECS), [About Single Image or Video](https://businesshelp.snapchat.com/s/article/image-video-ads?language=en_US) (HC-ABOUT), [Best practices](https://businesshelp.snapchat.com/s/article/snap-ads-practices?language=en_US) (HC-BP), [Safe zones](https://businesshelp.snapchat.com/s/article/safe-zones?language=en_US) (HC-SAFE), [Story](https://businesshelp.snapchat.com/s/article/story-ad-specs?language=en_US), [Collection](https://businesshelp.snapchat.com/s/article/collection-ad-specs?language=en_US), [Commercial](https://businesshelp.snapchat.com/s/article/commercial-specs?language=en_US), [Sponsored Snaps](https://businesshelp.snapchat.com/s/article/ads-in-chat?language=en_US), and the Snapchat for Business [ad formats page](https://forbusiness.snapchat.com/advertising/ad-formats) (FB-FORMATS).

## Conflicts

| Topic | Values found | Working guidance |
|---|---|---|
| Single Image/Video maximum length | HC-SPECS: 3 s to 30 minutes (≤ 1 GB). HC-ABOUT: up to 3 minutes. FB-FORMATS: 3–180 s. Story page: each Snap up to 180 s. HC-BP: "vertical video up to 30 minutes" | Plan for ≤ 180 s unless Ads Manager accepts longer. It is the cap that appears on most pages and fits Story Ads too. |
| Recommended length | HC-ABOUT and HC-BP: 3–5 s. HC-BP also: "around 5–6 seconds". Sponsored Snaps (FB-FORMATS): under 10 s. Collection: 3–5 s | Short. No official page recommends 15–30 s. |
| Brand name limit | HC-SPECS and Story page: 32 characters with spaces. HC-BP: up to 32. FB-FORMATS: up to 25 for every format | Write to ≤ 25 characters so it fits both; 32 appears to be the Help Center field limit. |
| Headline | 34 max everywhere; FB-FORMATS Sponsored Snaps: aim for 25–28 | Write to ≤ 34; aim for 25–28 where it shows in Chat. |
| Resolution | HC-SPECS and Commercial: 1080 × 1920 canvas; image minimum 720 × 1280. FB-FORMATS: 720 × 1280 for all formats | Produce at 1080 × 1920. 720 × 1280 is the minimum. |
| Safe zones | HC-SAFE (diagram): top 10%, bottom 35%, sides 6%, lower-right 15% × 45%. HC-BP: top 150 px, bottom 330 px. Collection: bottom ~450 px. Commercial: 150 px top and bottom | HC-SAFE says it is "one safe zone spec across Stories, Spotlight, and Commercials" and is the strictest. Plan to it. The pixel-based pages look like older guidance that was never updated. |
| Audio sample rate | Commercial page lists 48 kHz; HC-SPECS omits the sample rate | Deliver 48 kHz; it is the documented value where one is stated. |
| Sponsored Snaps in EU/Norway | Same article: launching First Snap early June 2026 and auction July 2026, yet also "ads targeting ... the European Union or Norway will not deliver to Chat Feed at this time" | Treat EU/Norway availability as unconfirmed; check Ads Manager. |

## Stale values often seen on agency sheets

- **"File size: 32 MB or less"** and **"storage aspect ratio 1:1"** do not appear on any current Snap page checked. Current HC-SPECS: video ≤ 1 GB, image 5 MB, Dynamic Ads ≤ 6 MB; SAR 9:16, DAR 9:16, **PAR** 1:1. An older sheet appears to have turned "pixel aspect ratio 1:1" into "storage aspect ratio 1:1".
- **"Length 3 to 10 seconds"** matches no current page. HC-SPECS now says 3 s to 30 min, with clips under 3 s looped.
- **"Recommended 15–30 seconds"** isn't supported by any current official page. Snap recommends 3–5 s (or 5–6 s).

## Safe-zone derivation note

HC-SAFE gives the safe zone only as percentages on a diagram image. The pixel values in [specs.md](specs.md) (192 / 672 / ~65 / 162 × 864 px at 1080 × 1920) are calculated, and reading the percentages off the diagram is an interpretation. Verify with the Safe Zone toggle in Ads Manager.

## Coverage not verified

- Availability in any ad account, market or objective (NOT_TESTED).
- AR Lens and Filter full production specs; Dynamic Product Ads; Web View, App Install, Deep Link and Lead Form attachment specs beyond CTAs.
- Spotlight-specific rendering differences; First Snap / First Story / First Lens reservation products.
- Custom CTA text (not documented) and which Dynamic CTA variants apply.
- Upload acceptance, review, rendering and delivery. This was public-document research only.
