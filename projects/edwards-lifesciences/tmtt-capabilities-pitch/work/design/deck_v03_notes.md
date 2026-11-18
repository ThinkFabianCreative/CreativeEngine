# deck_v03 notes

```
CLIENT:        Edwards Lifesciences
PROJECT:       TMTT capabilities pitch (Tuesday meeting, likely 2026-10-06, unconfirmed)
SOURCE SCOPE:  PROJECT-LEVEL. Structure: Brent Shoji outline (sources/2026-10-03_brent-shoji_deck-outline.md, user-confirmed order). Copy/look: creative-team brief + User decisions in ../../README.md
LOOK:          TRAFFIK's own identity, OBSERVED from wearetraffik.com (not approved guidelines)
MODE:          DEVELOP, first editable design pass
FILE:          deck_v03.html (supersedes v02 for Tuesday; v02 kept for reference)
```

## Concept sentence

The work does the talking, organized by Edwards business so each person in the room finds their own work, TRAFFIK listens at the end: a quiet white editorial deck where image slots carry most of the space, red marks the way through, and yellow appears only where Edwards gets a voice (their input points on slide 11, the close on slide 12).

## Build

- 16:9 at 1920×1080, scaled to window. Keys: arrows/space/PageUp/Down, Home/End, N speaker notes, E toggle editing (text is contenteditable; Esc leaves a field), P print. Edits are not saved to disk: edit in the source or print to PDF.
- Type: Adobe Caslon Pro (headlines), Acumin Pro 300 (body), Acumin Pro Wide 700 (labels). Fallbacks: Libre Caslon Text / Big Caslon / Georgia; Helvetica Neue / Arial. Adobe Fonts kit not loaded; the presenting machine needs the fonts or a kit link added.
- Color: black/white base; red #D91F1F for labels, numbers, "Delivered" tags; yellow #F4D803 only for Edwards' role and placeholder flags.
- Logo: typographic wordmark placeholder (circle T + TRAFFIK). Swap for the approved file.

## Per slide: asset selections and checks

Status labels on slides: **Delivered** = CONFIRMED DELIVERED; **Historical** = ARCHIVE EVIDENCE or asset exists without usage dates; **To verify** = UNKNOWN (drop before release if unconfirmed); **Proposed** = PROPOSED SCOPE (not used on any slide currently).

| # | Slide | Asset slots | Checks |
|---|---|---|---|
| 1 | Cover | TRAFFIK mark; Edwards identifier (text placeholder) | Approved marks |
| 2 | Who we are | 3-strip of real TRAFFIK work | 40 / 20 confirmed by Brent; confirm wording |
| 3 | What we do | 3 work crops: brand story / digital experiences / engagement | Brent to confirm offer language |
| 4 | Reel | TRAFFIK agency showreel, Dropbox `<video>` embed (kept exactly as set by coordinator) | Agency reel, not ELS reel; TRAFFIK owns it (user-confirmed); local copy + still fallback; test playback |
| 5 | Our relationship with Edwards | Work wall: Global Pulmonic, S3UR EU (Delivered); Tissue Is Trending, SAVR LMS/JAPAC, TAVR community + portal (Historical); Film column: ELS × TRAFFIK showreel (1:08) embedded, Dropbox .mov | No tenure; no TAVR Talk |
| 6 | Sample work: TMTT | PLACEHOLDER (hero + 2, need / contribution / status) | No delivered mitral/tricuspid work in ledger. SAPIEN M3 RESILIA animation is PROPOSED SCOPE and deliberately not shown |
| 7 | Sample work: Surgical | Tissue Is Trending, SAVR LMS/JAPAC, INSPIRIS patient profiles (Historical); KONECT RESILIA (To verify) | Approved published patient-profile layouts only |
| 8 | Sample work: THV | S3UR EU launch + style guide (Delivered); SAPIEN 3 Ultra RESILIA animation, SAPIEN Platform wall-screen film (1:43) embedded, Dropbox .mov (Historical; could double for slide 9 Events); Global Pulmonic as its own "Pulmonic portfolio" column (Delivered) | Pulmonic kept distinct from aortic; confirm it belongs under THV |
| 9 | Sample work: Events and conferences | TCT experience + New Frontiers TCT film, EuroPCR archive work (Historical); ACC, Huddle/KOL events (To verify) | No traffic/lead/ROI; no physician imagery without approval |
| 10 | Beyond Edwards | PLACEHOLDER, 3 columns: medical device / healthcare / other industries | User selects; client permission; no invented results |
| 11 | How we work (optional) | Diagram | Brent to confirm; cut if time is short |
| 12 | Close | Three open questions, Q1 names mitral and tricuspid care | Verify terminology; adjust to attendees |

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
- Embedded .mov files (ELS showreel, SAPIEN wall-screen film): TRAFFIK owns these videos (user confirmed 2026-10-03); .mov may not play in Chrome, so test in the presenting browser or transcode to MP4; bring local copies of all three videos. No air dates or results claimed.
- Keep slide 11 (How we work)? The deck is now 12 slides.
- Is "S3UR" acceptable client-facing, or spell out SAPIEN 3 Ultra RESILIA (verify exact name)?
- Brent: agency description, offer language (slide 5), working approach (slide 9).
- Tenure line stays out unless the user decides otherwise.

**Format**
- Final delivery: HTML on the night, PDF, or rebuild in Keynote/PowerPoint/Figma for team editing?
