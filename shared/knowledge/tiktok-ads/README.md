# TikTok paid-ad knowledge base

Version 1.0 · researched **16 September 2026** · public official TikTok Ads Help Center pages · English.

A shared platform reference for BriefMachine, DesignChamp, WordSmither and CreativeDirector. Load only the format you need. This is knowledge, not a creative framework, scorecard or client default.

## Scope

Eight records: auction In-Feed video (Non-Spark), Spark Ads, reservation In-Feed (including Reach & Frequency), TopView, carousel (image) ads, TikTok Ad Network (formerly Pangle) assets, and Global App Bundle video and image. Collection, Search, Branded Effect, Interactive Add-on and Shop formats are out of scope for this version.

## Start here

| Need | Read |
|---|---|
| Dimensions, duration, file limits, copy rules, CTAs by format | [Specifications](specs.md) |
| Structured lookup | [specifications.json](specifications.json) (TT-001 to TT-008) |
| Conflicts between TikTok pages, safe-zone gap, unverified coverage | [Source conflicts](source-conflicts.md) |

## How to use

1. Identify the **buying type** first: auction or reservation. TikTok's duration and bitrate limits differ between them (auction In-Feed up to 10 minutes at ≥ 516 kbps; reservation In-Feed and TopView 5–60 s at ≥ 2,500 kbps).
2. Identify **Spark vs Non-Spark**. Spark Ads inherit the organic post's caption, name and media, and most technical limits don't apply.
3. Separate recommendation from requirement. "9:16 (recommended)", "recommend 9–15 s" and "keep captions within 100 characters" are recommendations. "≥ 540 × 960", "≤ 500 MB" and "max 100 characters" are requirements.
4. **Recheck before production.** Pages carry their own "Last updated" dates and change often. Record the date you checked.
5. Account availability is **NOT_TESTED** for every record. No ad account was opened in this research.

**DOCUMENTED** = visible on an official page on the research date. **SOURCE_ISSUE** = at least one field conflicts or is ambiguous. **UNVERIFIED** = only non-official evidence (none in this version). A dash means not published, never zero or unlimited.

Platform facts here are reusable. Client offers, claims, audiences and performance are not.

## Useful findings

- The copy rules often quoted for "TikTok In-Feed" (app name 4–40, brand name 2–20, description 1–100, no emojis, no "#") come from the **Global App Bundle** (CapCut/Fizzo) pages. On TikTok feed ads the app name is pulled from the app store automatically, the account name displays at most 20 characters, and reservation/TopView captions allow v11 emojis, which count as 2 characters.
- Auction In-Feed video now allows **up to 10 minutes**. The familiar "5–60 s, recommend 9–15 s" applies to reservation In-Feed and TopView.
- TopView is 9:16 only, needs pre-approval, must have sound and must keep the first 3 seconds clear of the TikTok logo, skip button and swipe-up link. The same creative can't run elsewhere that day.
- Carousel ads need music (.mp3, ≥ 2 s) and allow one caption and one CTA for all images. Commercial Music Library tracks play silent on TikTok Ad Network.
- TikTok safe zones are published only as downloadable templates that change with caption length and add-ons. They were not transcribed. Download the current template and use the preview tool.

Nothing was staged or committed. No campaign, account or setting was created.
