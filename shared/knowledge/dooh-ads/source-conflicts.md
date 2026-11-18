# DOOH source conflicts and gaps

Checked 2026-09-16. These are open items. None is resolved by picking the newest or most convenient source.

## Differences between sources

- **Which list is authoritative (Vistar).** The Vistar venue list (DOOH-001–045) is a December 2023 snapshot hosted on a third-party domain. Vistar's help center (updated May 2026) names Deal Desk or Deal Summary Export specs as the source of truth and publishes only five standard sizes. The linked monthly dashboard did not load. Use the 2023 list to understand venue diversity, not to lock specs.
- **Color space.** The Vistar 2023 list gives the static color space as "RGB and CMYK". Place Exchange, Broadsign, Lamar and Bauer UK all require or recommend RGB, and Bauer says CMYK will not display correctly. Deliver RGB.
- **Static image type.** The Vistar 2023 list says JPG only, and Vistar's help center prefers JPEG over PNG. Place Exchange and Broadsign accept JPG or PNG, and Firefly taxi tops ask for PNG.
- **Taxi-top sizes.** Vistar 2023 lists 560×160, 1920×674, 384×124 and 384×128. Firefly lists 560×160 plus 1920×674 for NYC. Place Exchange routes taxi tops to 1400×400 and 840×400. The OpenOOH draft treats 560×160 as a downscale of 1400×400. These may be different networks or scaled renditions, so confirm the network.
- **Taxi-top frame rate.** Firefly publishes "29.974 fps", probably meaning 29.97. Confirm before encoding.
- **1280×960.** Vistar (2023 list and current help center) and Broadsign treat 4:3 1280×960 as standard. Place Exchange's 2026 one-sheet drops it, though its 2024 pharma guide listed it.
- **Frame rate and bitrate.** US platform guidance says 30 fps and under 5,000 kbps (PX, Broadsign). GSTV asks for 29.97 fps at a 20 Mbps target. The European DMI standard says 25 fps at 6–10 Mbit/s. Ströer allows up to 12 Mbps. Encode per network.
- **Audio.** Ströer (via TTD) wants no audio track. GSTV is audio-first with a detailed audio spec. The Vistar 2023 list marks audio Y, N or "Varies" by venue row. Place Exchange says audio "may be supported in some contexts". Never assume sound, and never strip it from a network that expects it without checking.
- **Airport durations.** Place Exchange says airports are typically :10. Vistar 2023 has one airport row at :10 and two at :15/:30. Lamar publishes airport sizes but no durations.
- **Billboard motion.** The Vistar 2023 list marks billboards static only. Lamar's media-formats page does not say. State law summaries commonly prohibit motion on roadside boards, while urban panels, spectaculars and some non-roadside screens accept video. Do not generalize from "Outdoor" to "static", or the reverse.
- **Slot length for roadside boards.** CCO says typically 8 s, Lamar 6–10 s by location, OUTFRONT 8–10 s, OAAA 6 or 8 s, and Bauer UK 10 s. State minimums vary.
- **File-size caps.** They range from 750 KB (Broadsign static, via TTD) to 100 MB (GSTV video). There is no cross-network default.
- **Broadsign place-based examples.** TTD's restatement lists train stations at 1280×720 and airports at 720×1280, which differ from the 1920×1080 and 1080×1920 used elsewhere. The restatement is undated (file last modified March 2025) and its text has extraction typos.

## Taxonomy ambiguities

- OpenOOH 1.2.1 (February 2026) deprecates Transit › Taxi & Rideshare Top (104) in favour of Outdoor › Car Top (307), deprecates Billboard children and High-End Dining, and renames children to singular. The repository README still calls v1.1 current, and its adoption table (not refreshed) lists Vistar on 1.0. Platform UIs and spec lists may use any of these labels.
- Labels mix across versions: Gas Stations / Fueling Stations; Dispensaries / Cannabis Dispensaries; Entertainment (1.0, 1.2) / Leisure (1.1); Train Stations / Train. Map by meaning and enumeration ID, not by string.
- Several Vistar venue types contain two or three rows that are different screen networks under one label. An unlabeled row in a derived sheet is one of these rows, not a new venue.

## Legacy spec sheet audit notes (not client-specific)

The legacy agency Digital OOH tab audited in this pass matches the Vistar 2023 list with these differences:

- **Added without a source:** Education › Schools; Health and Beauty › Spas; billboard sizes 990×495 and 806×390; :06 for Subway and Train Stations; 1080×1920 for Gyms; ":30 sometimes with approval" for Fueling Stations. The last is consistent with GSTV's 5–30 s range but is not in the Vistar list.
- **Conditions dropped:** Train Stations' 1920×1080, 1080×1920 and 1400×400 are static only (the sheet says Y/Y); Office Buildings 1080×1920 takes :15 only; Movie Theatres 3840×1080 takes :15 only; Taxi TV 640×360 takes no static; taxi top 384×128 takes :01–:480; Hotels 1600×900 carries :10–:115 spots.
- **Rows dropped:** a static-only Gyms row (1920×1080, 300×250); a static-only Urban Panels row (1080×1920, plus 2160×2160 black and white only); an audio-only Grocery network (MP3/AAC, :15/:30).
- **Subway duration:** the sheet gives :06/:15, but the source cell is blank.
- **Not carried over:** the document-level file rules (JPG; MOV/MP4; 10 MB / 50 MB), the audio flags and the "specs vary by screen" caveats.

## Coverage not verified

- Plan-level specs from Vistar Deal Desk, Place Exchange reps or media-owner Deal Summary Exports. None were requested.
- Vistar's monthly inventory dashboard, which returned a system error.
- Public creative specs from VIOOH, Hivestack/Perion, StackAdapt and Broadsign Reach as first-party documents. Pages read had none, or specs were only available through TTD's restatement or vendor editorial.
- US pixel and file specs for Clear Channel Outdoor and OUTFRONT, including OUTFRONT transit liveboards. Not published on the pages read.
- JCDecaux, Atmosphere, Curb, Screenverse, Captivate and other place-based network specs.
- Current (post-2019) state and local roadside motion and dwell rules. The OAAA compendium is dated, and local ordinances were not reviewed. FHWA's 2007 memo page returned 404 at the URL tried.
- DPAA or OAAA published creative spec standards for US DOOH. None was found. The only standards document located is the European DMI v2.0 (2020).
- Upload acceptance, letterboxing results, approval outcomes, audio playback and delivery on any network. No accounts were used.
- Spectaculars, 3D/anamorphic, HTML5/dynamic creative and audio-only DOOH, beyond the notes above.
