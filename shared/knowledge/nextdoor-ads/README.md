# Nextdoor paid-ad knowledge base

Version 1.0 · researched **16 September 2026** · public official Nextdoor sources · English (US and UK pages).

A shared platform reference for BriefMachine, DesignChamp, WordSmither and CreativeDirector. Load only the placement you need. This is knowledge, not a creative framework, scorecard or client default.

## Scope

Nextdoor publishes **four official spec pages that disagree**. Records are kept per source so none is silently merged:

| Source | Records | What it covers |
|---|---|---|
| [en-gb enterprise creative specs](https://business.nextdoor.com/en-gb/enterprise/creative-specs) | ND-001 to ND-006 | Sponsored Posts: Display, Video, Spotlight, Carousel, Digest, For Sale & Free |
| [US Nextdoor Ads Manager (NAM) creative specs](https://business.nextdoor.com/en-us/nam/nextdoor-ads-manager/creative-specs) | ND-007 to ND-012 | Image, Video, Carousel, Lead Gen, For Sale & Free, Right Hand Rail |
| [about.nextdoor.com/sp-guidelines](https://about.nextdoor.com/sp-guidelines) | ND-013 | An alternate NAM specs page with older-looking values |
| [Small-business ad specs](https://business.nextdoor.com/en/en-us/small-business/resources/ads-creative-specs) and [Local Deals transition](https://business.nextdoor.com/en-us/local/localdealstransition) | ND-014 | Self-serve business-account ads, including converted Local Deals |

The US enterprise URL (`/en-us/enterprise/creative-specs`) redirects to the NAM page. No en-ca enterprise specs page was found (404).

## Start here

| Need | Read |
|---|---|
| Copy lengths, dimensions and file rules | [Specifications](specs.md) |
| Structured lookup | [14 records](specifications.json) |
| en-gb vs US vs alternate pages, gaps | [Source conflicts](source-conflicts.md) |

## How to use

1. **Pick the source for the buying path.** Most self-serve and agency buying in the US goes through Nextdoor Ads Manager, so use ND-007 to ND-012 there. The en-gb enterprise page describes a different, fixed Sponsored Posts spec set. Confirm which one the account uses before designing.
2. **Recommendation is not requirement.** Nextdoor rarely labels its numbers. Unlabeled values are recorded as PUBLISHED_LIMIT. Only "before truncation", "recommended" and "ideal" values are RECOMMENDATION. "90 characters before truncation" is a writing target. The 800 / 1,700 body maximum is the upload limit.
3. **Performance statements are platform claims.** "CTR increases by 15% when the creative is personalized with a location" and "CTRs are 10% higher when less than 1/4 of the image contains text" are Nextdoor marketing claims, not specs. Do not quote them to clients as evidence.
4. **Recheck before production.** The Nextdoor Ads Manager help center was unavailable on the research date ("under construction"), and help.nextdoor.com articles render only with JavaScript. Check the live Ads Manager preview.
5. **Account availability is NOT_TESTED** for every record.

**DOCUMENTED** means visible on a public official page on the research date. **SOURCE_ISSUE** means another official page conflicts or the value is ambiguous. **UNVERIFIED** means only third-party evidence exists.

## Useful findings

- **US NAM image ads accept 1200 x 628 (1.91:1) or 1200 x 1200 (1:1)**, up to 150 MB, with advertiser name 70, headline 70, body 1,700 (90 before truncation) and CTA 45. The en-gb enterprise Display spec is much tighter: under 1 MB, name 25, CTA 10.
- **US NAM video: 2-300 s, 16:9 or 1:1, up to 500 MB, thumbnail auto-generated.** en-gb enterprise video: 3-120 s, 16:9, 50 MB, 1200 x 628 thumbnail.
- **Spotlight** (1200 x 1200, "Sponsored by + logo") is documented only on the en-gb enterprise page. A Nov 2025 Nextdoor press release mentions geo-personalized Spotlight creatives in a US pilot. No current US Spotlight specs were found.
- **Carousel** exists in both specs. en-gb: 1-5 product images at 464 x 464 ideal plus end card. US NAM: 2-10 cards, 1200 x 1200 minimum. Nextdoor announced video in carousels in Nov 2025, but no video-card specs are published.
- **Lead Gen, Right Hand Rail and For Sale & Free** are documented NAM placements. **Digest** is on the en-gb page only.
- **Local Deals** have been converted into regular business-account ads (70-character headline, 1:1 photo).
- Emojis and special formatting are not supported in NAM ad copy.

Nothing was staged or committed. No campaign or account setting was created.
