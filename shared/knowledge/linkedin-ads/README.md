# LinkedIn paid-ad knowledge base

Version 1.0 · researched **16 September 2026** · public official LinkedIn sources · English (US).

A shared platform reference for BriefMachine, DesignChamp, WordSmither and CreativeDirector. Load only the format you need. This is knowledge, not a creative framework, scorecard or client default.

## Scope

14 formats: Sponsored Content (single image, carousel, video, document, event, Thought Leader, Article and Newsletter), Sponsored Messaging (conversation, message), Text ads, Lead Gen Forms, Connected TV, and Dynamic Spotlight and Follower ads. Dynamic Jobs, single job ads and in-stream video beyond the note in LI-003 were not researched.

## Start here

| Need | Read |
|---|---|
| Copy lengths, dimensions, file rules per format | [Specifications](specs.md) |
| Structured lookup | [14 records](specifications.json) |
| Help Center vs business-page differences and gaps | [Source conflicts](source-conflicts.md) |

## How to use

1. **Primary source is the LinkedIn Marketing Solutions Help Center** (`linkedin.com/help/lms/answer/...`). The business.linkedin.com ads guide is a marketing summary. Several of its pages are older or copied from other formats. Where the two disagree, both values are recorded and the conflict stays open.
2. **Recommendation is not requirement.** LinkedIn gives two numbers for most text fields: a length that avoids truncation (RECOMMENDATION) and a hard maximum (REQUIREMENT). For example, single image headline: 70 recommended, 200 maximum. Write to the recommendation; the maximum only tells you what the upload will accept.
3. **Recommended pixels are not minimums.** Each ratio has a recommended size and a separate min/max range.
4. **Recheck before production.** Open the linked Help Center page and the actual Campaign Manager ad set. Objective, placement (feed vs Audience Network) and account rollout change what is available.
5. **Account availability is NOT_TESTED** for every record. No Campaign Manager account was opened.

**DOCUMENTED** means visible in public official documentation on the research date. **SOURCE_ISSUE** means at least one field differs between official pages or is ambiguous. **UNVERIFIED** means only third-party evidence exists (used only in conflict notes here).

Platform facts are reusable. Client goals, offers, claims and performance are not stored here.

## Useful findings

- The single image **vertical recommendation is now 4:5 (720 x 900)**. 1:1.91 vertical is still accepted but gets side borders. Vertical paid images serve on mobile only.
- Single image **Description is 100 recommended / 300 maximum** in the Help Center, not "70, LAN only". It shows on LinkedIn when the image is under 200 px wide, and on the Audience Network.
- **Video recommends 4:5**, accepts 9:16 to 16:9, 3 s to 30 min, 75 KB to 500 MB. LinkedIn recommends 15-30 s so the ad qualifies for every placement.
- **Carousel intro text maxes at 255**, much lower than the 3,000 for single image, video and document ads. Card headline limit is 45.
- **Thought Leader and Article/Newsletter ads take no headline or intro text.** The post is the creative, and the author controls edits.
- **Message ads** still have a live Help Center page, but LinkedIn's business page repeats the conversation-ad values. Availability of new message ads was not confirmed.
- **Text ads** are still documented (headline 25, description 75, 100 x 100 image).

Nothing was staged or committed. No campaign or account setting was created.
