# deck_v04 notes

```
CLIENT:        Edwards Lifesciences
PROJECT:       TMTT capabilities pitch (Tuesday meeting, likely 2026-10-06, unconfirmed)
SOURCE SCOPE:  PROJECT-LEVEL. Structure: Brent Shoji outline (sources/2026-10-03_brent-shoji_deck-outline.md, user-confirmed order). Copy/look: creative-team brief + User decisions in ../../README.md
LOOK:          TRAFFIK's own identity, OBSERVED from wearetraffik.com (not approved guidelines)
MODE:          DEVELOP, second design pass (ambition high). Response to "v03 looks boring"
FILE:          deck_v04.html (v03 kept). Same 12-slide order, copy, status labels and rules as v03
```

## Concept sentence

The work does the talking: a paced editorial sequence that alternates quiet white typographic slides with full-bleed black, film and image slides, so Edwards' own films carry the middle of the deck; red has one job (labels and "Delivered"), yellow is saved for the close, where Edwards gets the voice.

## What changed from v03

- Real imagery from three TRAFFIK-owned videos (user-confirmed) replaces every grey slot that had a usable frame. Slides with no verifiable asset (7 Surgical) became typographic instead of showing empty boxes.
- Videos are local H.264 MP4s (verified with ffprobe: High/Main profile), each with a poster frame. Dropbox URLs removed. Videos pause when you leave their slide.
- Pacing: 1 white+image, 2 white, 3 black, 4 full-bleed reel, 5 film + white, 6 white typographic, 7 white typographic, 8 black film, 9 full-bleed still, 10 black, 11 white, 12 yellow.
- Scale contrast: Caslon at 206-224px on cover/TMTT/close, 220px numerals on slide 2, against 11-15px Acumin Wide labels. Equal-box grids removed.
- Rendered and checked at 1920x1080 in headless Chrome, all 12 slides: no overflow, posters and video controls render.

## Per slide: frames chosen

| # | Slide | Treatment | Frames / media | Checks |
|---|---|---|---|---|
| 1 | Cover | White type left, image bleeds right | els_015 (white chess king, Edwards chess campaign; no copy) | Approved TRAFFIK mark; Edwards identifier |
| 2 | Who we are | White, 220px 40/20 numerals, 3-image mosaic | reel_014 Notre Dame Academy, reel_013 Uber Freight, reel_004 character campaign (client unnamed) | Confirm wording |
| 3 | What we do | Black, 3 tall crops | reel_019 Chicago International Boat Show, reel_008 app screen, reel_012 live event | Brent to confirm offer language |
| 4 | Reel | Full-bleed video | assets/video/traffik-showreel.mp4, poster reel_001 | Test audio on meeting machine |
| 5 | Relationship with Edwards | Film left (1180px), opener + status list right | assets/video/els-x-traffik-showreel.mp4, poster els_014 (chess board, red square) | Film opens with "Over a decade" on screen (film copy, not a deck claim); contains Huddle stat frames: play, never lift |
| 6 | TMTT | Typographic: "Mitral. Tricuspid. Where we'd start." | None | PENDING. No TMTT work claimed; yellow placeholder flag kept |
| 7 | Surgical | Typographic index, statuses | None (no surgical work in the three videos) | Add one hero when Dropbox assets arrive; KONECT To verify |
| 8 | THV | Black, wall film hero left, stills + status list right | assets/video/sapien-wallscreen.mp4, poster wall_005 (valve, no copy); els_014 chess; els_029 valve render (cropped, no copy) | Film carries product lines and an ISI end card: play as delivered, do not lift as stills. els_029 captioned generically (source piece unconfirmed) |
| 9 | Events | Full-bleed still, list + statuses | els_007 New Frontiers TCT film title (player chrome cropped out) | ACC, Huddle/KOL To verify |
| 10 | Beyond Edwards | Black, hero + 4-item rail | Hero reel_014 Notre Dame Academy; rail reel_003 Balt (medical device), reel_020 SDSU Global Campus, reel_013 Uber Freight, reel_019 Chicago International Boat Show | Labels = visible client + category only, no results. Healthcare slot unfilled. Client permission per case; yellow placeholder flag kept |
| 11 | How we work (optional) | White, large numerals, red on step 4 rule | None | Brent to confirm |
| 12 | Close | Full yellow, "Let's talk." 220px + 3 questions | None | Verify Q1 terminology |

Avoided on purpose: els_019-021 (Huddle "leading cause" / "72%" stats), els_009/016/017 (product claim lines), els_024/025 (Edwards claim panel), wall_006-026/030 (on-screen product lines), wall_034 (ISI), els_001-004 (tenure-like line "Over a decade").

## Open questions


**Meeting**
- Exact date, attendees, and whether they are TMTT or broader Edwards brand/digital/acquisition leaders (decides slide 10 Q1).

**Assets**
- Dropbox access for Global Pulmonic, S3UR, Tissue Is Trending, SAVR LMS/JAPAC, TAVR community files (Michael).
- Approved TRAFFIK logo file (and whether to use the health lockup); Edwards identifier usage.
- Adobe Fonts kit for the presenting machine.

**Content**
- Which cases for slide 10 (medical device, healthcare, other industry), with client permission and approved outcomes.
- TMTT slide 6: does any delivered mitral or tricuspid work exist (ask Michael)? If not, cut the slide, keep it as a "where we'd start" moment, or show SAPIEN M3 RESILIA labelled Proposed? Showing unsigned scope as sample work is not recommended.
- Global Pulmonic: does it sit under THV, or stand alone?
- KONECT RESILIA, ACC, Huddle, KOL events: confirm delivery, or drop them.
- Videos now local MP4s in assets/video: keep the whole design folder together when moving to the meeting machine. No air dates or results claimed.
- Fonts: Adobe Caslon/Acumin not loaded; Libre Caslon (Google Fonts) is the online fallback, Georgia offline.
- Keep slide 11 (How we work)? The deck is now 12 slides.
- Is "S3UR" acceptable client-facing, or spell out SAPIEN 3 Ultra RESILIA (verify exact name)?
- Brent: agency description, offer language (slide 5), working approach (slide 9).
- Tenure line stays out unless the user decides otherwise.

**Format**
- Final delivery: HTML on the night, PDF, or rebuild in Keynote/PowerPoint/Figma for team editing?
