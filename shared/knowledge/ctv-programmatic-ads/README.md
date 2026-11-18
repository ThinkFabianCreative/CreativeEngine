# CTV and programmatic ad specifications

Version 1.0 · researched **16 September 2026** · public official IAB Tech Lab, DSP and seller sources · English (US).

A shared reference for BriefMachine, DesignChamp, WordSmither and CreativeDirector on **Connected TV video** and **programmatic (DSP) display and video**. It holds platform knowledge only. It is not a creative framework, a scorecard or a client default.

## The key point

**There is no single CTV spec or DSP spec.** What an ad needs depends on the DSP, the exchange or SSP, the publisher or streaming app, the market and sometimes the deal. IAB Tech Lab publishes industry guidance, and every seller layers its own requirements on top. A file that passes one DSP can be rejected by a CTV publisher reached through it. This module records the standards and a set of named vendor specs as **reference points**, not as universal rules.

## Start here

| Need | Read |
|---|---|
| IAB standard display sizes and file weights | [specs.md §1–2](specs.md#1-iab-standard-display-sizes) |
| HTML5 banners (DV360, The Trade Desk) | [specs.md §3](specs.md#3-html5-display) |
| Programmatic online video: VAST, duration, bitrate, companions | [specs.md §4](specs.md#4-programmatic-online-video) |
| CTV commercials: resolution, codec, bitrate, fps, loudness, durations | [specs.md §5](specs.md#5-connected-tv-video) |
| Quick "safest master" answers | [specs.md §6](specs.md#6-vendor-quick-comparison) |
| Where vendors disagree, source anomalies, unverified coverage | [source-conflicts.md](source-conflicts.md) |
| Structured lookup | [24 records in specifications.json](specifications.json) |

Record prefixes: **IAB-** industry standards (IAB Tech Lab) · **DSP-** buying platforms (Google DV360, The Trade Desk, Amazon DSP, Yahoo DSP, Quantcast, Propensity, StackAdapt) · **CTV-** sellers (Amazon Streaming TV/Prime Video, Disney+/Hulu, Roku self-serve).

## How to use specifications correctly

1. Identify the **buy path**: which DSP, which supply (open exchange, PMP, programmatic guaranteed, direct), which publishers or apps, which markets.
2. Read the record's classification for each value:
   - **Industry standard**: IAB Tech Lab guidance. It is a recommendation that publishers adopt with modifications.
   - **Vendor requirement**: a named DSP or seller says it must be met. It applies to that vendor only.
   - **Vendor recommendation**: preferred, optimal or best-practice values. Missing them may cost scale without causing rejection.
3. Check the record's **status** and date. **DOCUMENTED** = read on an official public page on the research date, not delivery-tested. **SOURCE_ISSUE** = a field needs confirmation. **UNVERIFIED** = the official page could not be read. Do not use it as a production spec. Account availability is **NOT_TESTED** everywhere.
4. **Before production, get the actual media vendor's current spec sheet** (DSP and, for CTV, the publisher list) and reconcile it with this module. Where they differ, the vendor's sheet for that buy governs, and the difference belongs in the project record, not here.
5. A missing value ("—") means the inspected source did not publish it. It never means zero, unlimited or unsupported.

Public platform facts are reusable. Client media plans, publisher lists, deal terms and performance are project knowledge and do not belong in this folder.

## Useful findings

- **IAB's newest video and CTV guidance is final (July 2026).** The [Digital Video & CTV Ad Format Guidelines v2.0](https://github.com/InteractiveAdvertisingBureau/Ad-Format-Guidelines-for-Digital-Video-CTV/blob/main/v2.0.md) set linear durations of 6/15/20/30 s. They require MP4 with H.264 High and AAC-LC, progressive scan, no slates, native frame rate, and loudness of -24 LKFS ±2 (US) or -23 LUFS ±1 (EBU R128) with a true peak of -6 dBTP or lower. The same release adds six new CTV formats, including pause and squeezeback ads. [IAB-003/004/007]
- **VPAID is deprecated.** IAB replaced it with SIMID for interactivity and OMID for measurement. CTV sellers (Amazon, Disney, DV360 CTV, TTD CTV) still ask for plain VAST 2.0/3.0, reject VPAID and often reject wrappers. [IAB-005]
- **CTV bitrate and file caps vary widely.** Minimums run from 6 Mbps (Roku self-serve) to 15 Mbps (Prime Video) to 15–60 Mbps CBR (Disney programmatic). File caps run from 250 MB to 10 GB. A 1 GB file is too large for Amazon (500 MB) and for Hulu-served delivery (250 MB). [source-conflicts](source-conflicts.md)
- **The IAB display portfolio is still the 2017 New Ad Portfolio.** Its fixed sizes are 970x250, 300x50/320x50, 728x90, 970x90, 300x1050, 160x600, 300x250, 120x60 and phone interstitials. Static weights run from 50 to 300 kB, and animation stops at 15 s. 300x600 remains "in transition" but is a top size in every DSP. The tablet and mobile interstitial sizes 320x480, 480x320, 768x1024 and 1024x768 are DSP sizes, not IAB fixed units. [IAB-001/002]
- **Pixels and file weight govern display, not ppi.** No IAB or DSP source inspected sets a ppi value. DV360 recommends uploading up to 2x the slot dimensions, and Amazon DSP requires @2x files for several mobile units. [DSP-001/009]
- **The audited sheet's DSP display row probably comes from StackAdapt.** Its 750 KB / 3.5 MB GIF / 72–144 ppi values match search extracts of StackAdapt's help page, which is now behind a login, so the match is UNVERIFIED. The CTV row's source was not identified. [source-conflicts](source-conflicts.md#sheet-source-identification)

Nothing was uploaded, no account was used, and nothing was staged or committed.
