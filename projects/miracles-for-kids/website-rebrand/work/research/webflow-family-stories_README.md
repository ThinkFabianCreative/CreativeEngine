# Webflow Family Stories scrape

```
CLIENT:       Miracles for Kids Charity
PROJECT:      website-rebrand
SOURCE:       https://miracles-for-kids-8843ee.webflow.io/family-stories (staging), scraped 2026-11-01
SOURCE SCOPE: PROJECT-LEVEL
FILES:        webflow-family-stories.csv, webflow-family-stories.json (JSON adds body_html)
```

36 stories, public pages only. Hidden CMS fields are not visible without the Webflow API.

## Image locations

All images are on Webflow's CDN: `https://cdn.prod.website-files.com/6a32d801c4385d8a325f9838/<asset-id>_<filename>`. The `6a32d801…` folder is the CMS asset site; the `6a32407e…` folder holds site design assets (logo, icons).

| Column | Where it appears | Where it's read from |
|---|---|---|
| `thumbnail_url` | Story card on /family-stories | `img.fs-card-image` inside each `.fs-card2` list item |
| `thumbnail_srcset` | Same card, responsive sizes | The card image's `srcset`: Webflow-generated `-p-500`, `-p-800`, `-p-1080` versions plus the original |
| `main_image_url` | Hero on the story page | First `img.storyheroimage` in `section.stories-section-hero` |
| `gallery_images` | Gallery under the story body | `img.image-12` in the story page's collection list |

**Thumbnail and main image are the same file on all 36 stories.** The collection most likely has one main image field, which the card and the hero share; Webflow only resizes it for the card. A separate thumbnail field, if one exists, is empty or unused. Cards are cropped by CSS, so a photo that works as a hero may crop badly on the card.

The first 8 hex characters of an asset ID are its upload timestamp; `date_guess` uses this.

## Other columns

- `program_tags`: Lifeline, Safe Haven, Balance, Boost, Pillars, from the card's tag list
- `topics`: keyword guesses from the story text, not CMS data
- `*_guess`: labeled stand-ins for blank fields; originals untouched
- `has_video`: false on all 36. `video_status` / `video_source_assets`: see `../design/story-video-cms-fields_v01.md` and `../design/story-video-template_v01.md`
