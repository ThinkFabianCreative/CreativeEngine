# Digital out-of-home (DOOH) knowledge base

Version 1.0 · researched **16 September 2026** · public sources from platforms, media owners, OpenOOH, OAAA and one European industry body · US focus, one UK reference.

A shared reference for BriefMachine, DesignChamp, WordSmither and CreativeDirector. Load it when an assignment includes digital screens: roadside billboards, urban panels, transit, place-based or point-of-care screens. It is knowledge, not a creative framework, scorecard or client default.

## The key point

**DOOH has no single official spec.** The media owner decides what each screen accepts. Programmatic platforms (SSPs such as Vistar, Place Exchange, Broadsign, Hivestack; DSPs such as The Trade Desk or StackAdapt) group screens into venue types and publish *summaries*. Those summaries are useful for planning. They do not guarantee the specs of any particular network. Screen inventory changes all the time, and a venue-type row can hide several media owners with different canvases, durations and audio rules.

Vistar's own help center (updated 20 May 2026) says the specs its Deal Desk supplies for a specific plan, or a media owner's Deal Summary Export, are the source of truth. Place Exchange says to confirm final specs with its rep. Treat every generic list, including this one, as a starting point.

## Start here

| Need | Read |
|---|---|
| Venue taxonomy, common canvases, file conventions, durations, roadside rules, legibility | [Specifications](specs.md) |
| Structured lookup by source and venue type | [68 records](specifications.json) |
| Where sources disagree, what is ambiguous, what was not verified | [Source conflicts and gaps](source-conflicts.md) |

## How to use it

1. Identify the **buy path** (programmatic SSP/DSP, direct with a media owner, or both), the **venue type**, the **market** and, when known, the **media owner or network**.
2. Plan from the common canvases: 1920×1080 and 1080×1920 cover most place-based and urban screens; 1400×400 and 840×400 cover most US roadside digital billboards. Then check the venue-type record for exceptions such as 1280×960, 1366×768, 3840×1080 and taxi-top sizes.
3. Check the record's status and date. **DOCUMENTED** means the fact was visible in a public source on the research date. **SOURCE_ISSUE** means the source is dated, third-party hosted, a draft, a restatement or ambiguous. **UNVERIFIED** means no primary source was found. Account and network availability is **NOT_TESTED** for every record.
4. Keep requirements and recommendations apart. A "top size" is not a mandate. A slot length is not a video length. A platform summary is not a media-owner requirement.
5. Before production, get the plan-specific spec export from the platform or media owner and design to it. Assume media-owner approval is needed for every creative. Allow approval time: Place Exchange asks for 3 business days (7 for spectaculars, airports and controlled inventory), GSTV and Firefly taxi TV 5, OUTFRONT 10 working days.

Missing values (—) mean the inspected source did not publish them. They never mean zero, unlimited or unsupported.

## Useful findings

- **The legacy agency sheet's Digital OOH tab closely matches a Vistar Media venue-type spec list** (PDF created 8 December 2023). Its venue groups and types, sizes, static/video flags and durations match row by row, including the unlabeled rows, which are extra rows *within the same venue type* in the Vistar list, not separate venues. The sheet adds a few items that no source supports (Schools, Spas, billboard 990×495 and 806×390, :06 durations). It also drops conditions that matter, such as static-only sizes, per-size duration limits and audio flags.
- **Vistar's current public guidance is narrower than that list:** five standard sizes it resizes and letterboxes to (1080×1920, 1280×960, 1920×1080, 840×400, 1400×400), JPEG preferred over PNG, video by VAST only, and no HTML5.
- **Place Exchange (March 2026)** says 1920×1080, 1080×1920, 1400×400 and 840×400 reach about 85% of its inventory. It sets :15 as the standard video length, with airports typically :10. Video should be MP4 with an even-numbered resolution, under 5,000 kbps and at 30 fps.
- **Most roadside digital billboards take static images only.** State laws summarized by OAAA (2019) commonly bar animation and full-motion video and set minimum static display times of 6–10 seconds (4 seconds in some states). Lamar says ads rotate every 6–10 seconds and **prohibits QR codes** on its DOOH. Clear Channel Outdoor describes 8-second slots.
- **Audio is venue-specific, not universally off.** GSTV (fueling stations) is built around audio and publishes an audio spec. Vistar's 2023 list marks audio for airports, doctor's offices, malls, movie theatres, salons, taxi TV and others. Billboards, bus shelters, urban panels and most retail screens are silent. Make every creative work muted unless the network confirms sound.
- **OpenOOH venue taxonomy 1.2.1 (February 2026)** renames and deprecates categories. Taxi & Rideshare Top has moved to Outdoor › Car Top, Train Stations is now Train, and Billboard subtypes are deprecated. Older platform lists, including the 2023 Vistar list, still use the 1.0/1.1 labels.
- **Legibility guidance comes from media owners, not a standard:** text at least 15 px tall on billboards (Vistar 2023), about seven words or fewer (Firefly taxi tops), contrast of at least 4.5:1 and ideally 7:1 (Place Exchange), no pure white fields on LED (Vistar/Lamar), and 8 pt minimum legal copy (GSTV).

## Scope and limits

This version checked public pages and PDFs only. It did not log into any platform, request Deal Desk exports or test uploads, approvals or delivery. Several platform pages (the Vistar inventory dashboard, VIOOH, Hivestack and StackAdapt spec pages) were not accessible or had no specs, and US Clear Channel and OUTFRONT publish no pixel or file specs on the pages read. Roadside regulation is summarized from an industry compendium dated 2019. It is context, not legal advice. See [gaps](source-conflicts.md).

No client, project or campaign facts belong here.
