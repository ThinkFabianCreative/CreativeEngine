# Google Ads and YouTube ad knowledge base

Version 1.0 · researched **16 September 2026** · public official Google sources (Google Ads Help, YouTube Help, Advertising Policies Help) · English (US).

A shared platform reference for BriefMachine, DesignChamp, WordSmither and CreativeDirector. Load only the record for the format in hand. This is knowledge, not a creative framework, scorecard or client default. It holds no client facts.

## Scope

Google Ads responsive search ads, responsive display ads, Performance Max asset groups and Demand Gen (single image, carousel, video). YouTube skippable and non-skippable in-stream, bumper, in-feed, Shorts, masthead, video file specs, and the text fields used in video reach and Demand Gen video ads. 14 records.

## Start here

| Need | Read |
|---|---|
| Copy limits, asset counts, image and video sizes per format | [Specifications](specs.md) |
| Structured lookup by record ID | [specifications.json](specifications.json) |
| Where Google's own pages disagree, and what was not checked | [Source conflicts and gaps](source-conflicts.md) |
| Google's current per-campaign specs index | [Google Ads specs hub](https://support.google.com/google-ads/answer/13676244) |

## How to use

1. Identify the **campaign type** first. The same field name has different limits in different campaign types: a YouTube video headline is 40 characters in Demand Gen, 100 in in-feed video ads, and the video reach CTA headline is 15.
2. Separate **requirements** from **recommendations**. Minimum pixels, character maximums, file caps and policy rules are requirements. "Recommended" sizes, counts and lengths are not rejection thresholds. A count in a Google "Recommended" column is not a publish minimum.
3. Check the record's **status**. DOCUMENTED means visible in official public docs on the research date. SOURCE_ISSUE means official pages conflict or are ambiguous on at least one field; read the conflict first. UNVERIFIED means no official source was found.
4. **Recheck before production.** Google revises these pages and is migrating campaign types (video action campaigns became Demand Gen in May 2026). Confirm in the campaign builder.
5. **Account availability is NOT_TESTED** for every record. No account was opened and nothing was uploaded.

A dash means not published in the inspected page. It never means zero, unlimited or unsupported.

## Useful findings

- **Responsive display ads are not responsive search ads.** RDA text is 5 headlines (30), 1 long headline (90), 5 descriptions (90) and a business name (25), with up to 15 images and 5 logos. Image assets are JPG or PNG, 5120 KB max.
- **Performance Max:** 3–15 headlines of 30 characters with at least one of 15 or fewer, 1–5 long headlines, 2–5 descriptions, business name 25, up to 20 images per ratio (4+ recommended for landscape and square), square logo required, video optional (10 s minimum, auto-generated if absent).
- **Demand Gen** has the widest image set (1.91:1, 1:1, 4:5, 9:16), 40-character headlines, a 150 KB logo cap and carousels of 2–10 cards with 40-character card headlines.
- **YouTube video files:** 256 GB cap (YouTube: or 12 hours), MPG recommended, 1080p recommended at 16:9, 9:16 or 1:1. Skippable in-stream has no maximum length (under 3 minutes recommended). Bumpers are 5–6 s. Non-skippable limits depend on campaign subtype.
- **Image policy:** text or logo overlays are not permitted on image assets except in Performance Max. Keeping key content in the center 80% is a recommendation.
- Safe zones for video are only published as downloadable templates; plan from the templates and the in-account preview.
