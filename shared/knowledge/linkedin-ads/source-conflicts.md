# Source conflicts, ambiguities and coverage gaps

Checked 2026-09-16. These are documentation differences between official LinkedIn pages, or limits of this research. All stay OPEN until confirmed in Campaign Manager or by LinkedIn. Neither source is silently preferred. Production should follow the Help Center value and verify it in the ad preview.

## Conflicts between official sources

| ID | Record | Help Center (linkedin.com/help/lms) | Business page (business.linkedin.com/advertise/ads) |
|---|---|---|---|
| LI-C1 | LI-001 single image, description | 100 recommended / 300 max; shown under 200 px wide or on LAN | 70 characters, "only required if using LinkedIn Audience Network" |
| LI-C2 | LI-001 single image, vertical | Recommended ratio 4:5, 720 x 900; 1:1.91 supported with borders | Recommended 1:1.91 628 x 1200, 2:3 600 x 900 and 4:5 720 x 900 (same border note) |
| LI-C3 | LI-001 single image, text maximums | Intro 3,000, headline 200 | Only 150 / 70, no maximum given |
| LI-C4 | LI-002 carousel, file types | JPG, PNG, non-animated GIF | JPG or PNG |
| LI-C5 | LI-003 video, intro maximum | 3,000 | 600 |
| LI-C6 | LI-003 video, frame rate | Less than 30 fps | Recommended 30 fps |
| LI-C7 | LI-005 event, image | Optional custom ad image, off-platform events allowed | 4:1 image pulled from the LinkedIn Event page; LinkedIn Event URLs only |
| LI-C8 | LI-006 Thought Leader, CTA | No CTA for image/video; Event Thought Leader Ads include one | No CTA buttons |
| LI-C9 | LI-009 message ads | Message 1,500; CTA 20; URL 1,024 | Message 8,000; CTA 25; URL 2,000 (identical to conversation-ads page) |
| LI-C10 | LI-010 text ads, URL | 500 characters | 2,000 characters |

The business single-image page links to a legacy Help Center ID (`answer/111093`), which now redirects to `a426534`. The event business page links to the carousel Help Center page. These suggest the business pages are maintained less closely.

## Ambiguities

- **Carousel "45-character limit"** (Help Center) is listed twice, for URL destination and Lead Gen CTA, without naming the field. The business page names it card headline.
- **Single image "Image size 7680 x 4320"** is listed as a general size, while the square and vertical maximums are smaller (4320 x 4320; 2430 x 4320). Use the per-ratio ranges.
- **Video square 1:1** has a range but no recommended size.
- **Message ads availability.** Third-party sources (not evidence) report LinkedIn sunset Message Ads in 2023. The official Help Center spec page is still live. Status: UNVERIFIED either way.
- **In-stream video ads** are described as testing / gradual release.

## Coverage not verified

- Campaign Manager availability by account, market, objective and rollout (all NOT_TESTED).
- Help Center "last updated" dates were not in the retrieved HTML. WebFetch reported "1 month ago" for the single image page.
- Dynamic Jobs ads, single job ads, Article/Newsletter Help Center article (a5966218), Conversation Starter / focused-inbox changes, carousel video cards, BrandLink / Wire / Live event ads, Accelerate and flexible-ad automated variants, and LinkedIn Audience Network rendering.
- Upload acceptance, ad review, delivery and performance. This was public-document research only.
