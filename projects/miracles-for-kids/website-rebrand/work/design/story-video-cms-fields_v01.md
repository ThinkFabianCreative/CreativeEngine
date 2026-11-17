# Story video: Webflow CMS fields, v01

```
CLIENT:       Miracles for Kids Charity
PROJECT:      website-rebrand
COLLECTION:   Family Stories (Webflow)
SOURCE SCOPE: PROJECT-LEVEL
STATUS:       Draft for proposal. Not client-approved.
DATE:         2026-11-01
```

## Why

The proposal puts a video on every story page, existing and upcoming. The Family Stories collection has no video field today. The scrape of the 36 live staging stories (`../research/webflow-family-stories.csv`) found no video on any page. The site already ships a video lightbox (`.videoplayer`, `body:has(.videoplayer.is-open)`) with nothing wired to it, so the player exists and only the fields and content are missing.

## Fields to add

| Field | Webflow type | Required | Notes |
|---|---|---|---|
| Story video | Video link | No (until produced) | YouTube or Vimeo URL. Feeds the lightbox. Unlisted upload, captions on |
| Video poster | Image | Yes when video set | First frame of the cut as a still, 16:9, min 1600px wide. Must work without the video (hook rule) |
| Video length | Plain text | No | e.g. "1:12". Shown on the play button |
| Vertical cut | Video link | No | 9:16 version for social and mobile; same story, re-edited |
| Video status | Option | Yes | Not started / Assets requested / In edit / In review / Live |
| Consent on file | Switch | Yes | Parent or guardian video release signed. Video link must stay empty while off |
| Transcript | Rich text | Yes when video set | Accessibility and SEO. Real words only; never written for a child |
| Captions file | File | No | .vtt or .srt, if the host doesn't hold captions |

Not added on purpose: autoplay toggle (story videos play on tap only) and a separate video title (the story headline is the title).

## Template behavior

- **Video set and consent on:** play button over the hero image, opens the lightbox. Length shown on the button.
- **Video empty:** page renders exactly as today. No empty player, no "coming soon".
- **Story cards on /family-stories:** small play badge on the card image when a video exists. Use a conditional visibility rule on Story video.
- **Upcoming stories:** the editor fills Video status at creation, so the backlog is visible in the CMS list view.

## Rollout for existing stories

From the scrape: 21 stories have hero + at least one gallery photo (enough for a photo-led cut); 15 have the hero only and need new photos, family footage or a shoot. Prioritize by Video status, not by publish order.

## Open

- Video host (YouTube vs Vimeo) and who owns the account
- Video release form wording; MFK's existing photo consent may not cover video
- Whether the Webflow plan in use allows the extra fields (collection field limits)
