# Snapchat paid-ad knowledge base

Version 1.0 · researched **16 September 2026** · public official Snapchat Business Help Center and Snapchat for Business pages · English (US).

A shared platform reference for BriefMachine, DesignChamp, WordSmither and CreativeDirector. Load only the format you need. This is knowledge, not a creative framework, scorecard or client default.

## Scope

Six records: Single Image or Video (full-screen Snap Ad), Story Ads, Collection Ads, Commercials, Sponsored Snaps (Chat Feed) and the cross-format safe zone, plus CTA options by attachment. AR Lenses/Filters, Dynamic Product Ads and reservation takeovers (First Snap etc.) are out of scope for this version.

## Start here

| Need | Read |
|---|---|
| Canvas, length, file, audio, copy limits, safe zones, CTAs | [Specifications](specs.md) |
| Structured lookup | [specifications.json](specifications.json) (SNAP-001 to SNAP-006) |
| Where Snap's own pages disagree, and stale sheet values | [Source conflicts](source-conflicts.md) |

## How to use

1. Start with the **safe zone (SNAP-006)**. It applies to every major format and is stricter than older pixel numbers still on some Snap pages.
2. Separate recommendation from requirement. "3–5 seconds" and "aim for 25–28 characters" are recommendations. "Headline up to 34 characters", "video ≤ 1 GB" and "H.264" are requirements.
3. Most Snap records are SOURCE_ISSUE because Snap's pages disagree with each other. Use the working guidance in [source conflicts](source-conflicts.md) and don't pick the most convenient number.
4. **Recheck before production.** Help Center articles show no update date. Record the date you checked.
5. Account availability is **NOT_TESTED** for every record. No ad account was opened.

**DOCUMENTED** = visible on an official page on the research date. **SOURCE_ISSUE** = at least one field conflicts between official pages. **UNVERIFIED** = only non-official evidence (none in this version). A dash means not published, never zero or unlimited.

Platform facts here are reusable. Client offers, claims, audiences and performance are not.

## Useful findings

- **Safe zone:** keep key content out of the top 10%, bottom 35% and 6% on each side, plus a lower-right column 15% wide × 45% tall. At 1080 × 1920 that is roughly 192 px top, 672 px bottom, 65 px sides and 162 × 864 px lower right (calculated).
- **Production safe copy:** brand name ≤ 25 characters (the formats page says 25, the Help Center 32), headline ≤ 34. The brand name must be the paying advertiser and can't equal the headline.
- **Length:** Help Center specs allow 3 s to 30 minutes, but other Snap pages cap at 180 s. Snap recommends 3–5 s. Commercials: 3–6 s Standard, or 7–180 s Extended Play with the first 6 s non-skippable.
- **File:** 1080 × 1920 (720 × 1280 minimum), .mp4/.mov H.264, video ≤ 1 GB, image ≤ 5 MB, SAR/DAR 9:16 with PAR 1:1, audio −16 LUFS stereo ≥ 192 kbps. Stills become 5-second videos.
- **Story Ad tiles** need a 993 × 284 PNG logo, a 360 × 600 PNG image (≤ 2 MB) and a headline of up to 55 characters.
- **Sponsored Snaps** reuse Single Image/Video, Story or Static Collection creative and add optional chat assets (500-character message, auto-response, 1080 × 1920 background).

Nothing was staged or committed. No campaign, account or setting was created.
