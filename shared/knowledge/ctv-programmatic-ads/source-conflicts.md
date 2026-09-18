# Source conflicts, vendor differences and coverage gaps

Checked 2026-09-16. These are observed documentation issues, differences between vendors and research limits. They are not invented restrictions. Record IDs refer to [specs.md](specs.md) and [specifications.json](specifications.json).

## Vendor differences that matter for production

| Topic | Range observed | Records | Handling |
|---|---|---|---|
| CTV minimum video bitrate | 6 Mbps (Roku self-serve), 8 Mbps (Amazon non-Prime supply), 10–15 Mbps (Propensity premium), 15 Mbps (Prime Video, TTD mezzanine), 15–60 Mbps CBR (Disney programmatic, Yahoo), 18–30 Mbps (Quantcast) | CTV-001–003, DSP-008/011/013/014 | Encode the master to the strictest seller on the plan. No single threshold is "good" everywhere |
| CTV max file size | 250 MB (Hulu-served), 300 MB (Yahoo), 500 MB (Amazon), 1 GB (DV360, Roku, Propensity, Quantcast hosted), 1.9 GB (Disney programmatic), 10 GB (TTD mezzanine, Quantcast 3P) | same | A 1 GB file is rejected by Amazon, Yahoo and Hulu-served delivery |
| CTV frame rates | Amazon: no 30. Roku: no 24 or 30. DV360/TTD: 23.98 or 29.97. Disney: 23.98–30. IAB: 23.976–60 | CTV-001/003, DSP-004/008, CTV-002, IAB-003 | 23.976 or 29.97 native, constant, is the widest overlap |
| CTV durations | IAB 6/15/20/30. Amazon by market and supply (US Prime Video 15/30/45/60; 3P apps 6–90). Roku 6–92 s. Propensity max 60 | IAB-003, CTV-001/003, DSP-014 | "Exactly :15 or :30" is the safest, not the only, choice |
| Duration tolerance | IAB: exact, ≤1 s transcoding drift. DV360: shorter creative fits longer slot; ~10% over tolerated by most publishers. TTD: shorter fits bucket | IAB-003, DSP-003, DSP-007 | Deliver exact lengths for CTV; do not rely on tolerance |
| Loudness | IAB -24 LKFS ±2 (US) / -23 LUFS ±1 (EU), ≤ -6 dBTP. DV360 video -24 LKFS ±2. TTD average -24 LKFS. Amazon STV, Disney, Roku ad pages: not published | IAB-003, DSP-003/008 | Master to -24 LKFS ±2 (US) or EBU R128 (EU) and confirm with seller |
| VAST version | IAB current: 4.3 plus CTV Addendum 2024. DV360 CTV and TTD CTV: 2.0 most scalable. Amazon, Disney: inline 2.0/3.0, no wrappers. DV360 OLV: 2.0–4.0. Quantcast: 2.0–4.0 | IAB-005, DSP-003/004/008/013, CTV-001/002 | Ask each seller; do not assume 4.x reaches CTV scale |
| VPAID | IAB: deprecated. CTV sellers reject. DV360 OLV and TTD OLV still accept VPAID 2.0 in some paths | IAB-005, DSP-003/007 | Do not build new VPAID units; use VAST + OMID/SIMID |
| Display static weight | IAB 50–300 kB by size; TTD ≤150 KB; Amazon 40–200 kb; DV360 upload ≤10 MB (publishers may want less); StackAdapt 750 KB optimal / 3.5 MB GIF (UNVERIFIED) | IAB-001, DSP-001/005/009/012 | Heavy files may upload to one DSP and lose scale or be rejected elsewhere |
| Display animation | IAB ≤15 s, no looping beyond 15 s. TTD ≤15 s looping then static. DV360 HTML5 ≤30 s | IAB-002, DSP-002/005 | ≤15 s total including loops is the common safe rule. A loop count alone is not a documented rule in the sources read |
| GIF | DV360, TTD accept. Amazon DSP static display lists JPG / PNG-8 only | DSP-001/005/009 | Supply a JPG/PNG version |
| High-density export | DV360 recommends up to 2x. Amazon requires @2x on several mobile units and 970x250 onsite. IAB weights calculated at 2x. TTD, StackAdapt: not documented in sources read | DSP-001/009, IAB-001 | Exact pixel size is safe everywhere; 2x only where the DSP says it scales |

## Field-level issues in sources

- **IAB 970x90:** listed in the Fixed Size Ad Specifications table (IAB-001) and marked "Delist" in the complete portfolio's status table (IAB-002). Both kept. DV360 still lists 970x90 as common.
- **IAB portfolio age:** the display documents are dated 2017 (files 2019). IAB Tech Lab's guidelines page (dated 2024-02-07) still presents them as current, and no newer display portfolio was found. The "In Transition" flex replacements never displaced fixed sizes in DSP lists.
- **TTD CTV bitrate (DSP-008):** "typically a minimum of 1200–1500 kbps… 1.6–3.2 Mbps preferred" sits beside a mezzanine requirement of ≥15,000 kbps and a tier table of 4,000–6,500 kbps for 1080p HQ. The low figures probably describe served renditions, not uploads. Kept OPEN.
- **TTD HTML5 (DSP-006):** some table cells (individual file max, auto-started video) are scrambled in the PDF text layer. The PDF is undated.
- **Amazon OLV VPAID (DSP-010):** the same paragraph says tags "may include VPAID 2" and "We do not accept VPAID or Wrapper Tags".
- **Disney (CTV-002):** "Main Profile @ Main Level" is an MPEG-2 profile label listed beside 1080p H.264 and 15–60 Mbps. The page also shows template placeholder text. Durations and loudness were not found on the inspected tabs, and the "Safety Zones" variants were not transcribed.
- **DV360 companions (DSP-003):** "Companion banner size 20K" is ambiguous. It probably means 20 KB, which is far below IAB's 200 kB companion guidance (IAB-006).
- **Quantcast and Yahoo (DSP-011/013):** read through fetch summaries, not raw text. Re-read before relying on exact values.

## Sheet-source identification

- **Display row ("DSP | Programmatic Display Ad"):** the combination *optimal JPG/PNG 750 KB, max GIF 3.5 MB, min 72 ppi, recommended 144 ppi* matches web-search index extracts attributed to StackAdapt's help page `support.stackadapt.com/plan/creative-setup/display-ad-specs`. That page now returns 403 and redirects to a login-restricted page, and the Internet Archive was offline during this pass. **Probable source: StackAdapt (UNVERIFIED).** The size list, the "15 s and/or 3 loops" rule and the export note were not recovered.
- **CTV row:** no exact public match. Propensity's April 2026 CTV page (DSP-014) shares 1920x1080, MP4, up to 1 GB, 48 kHz and the idea that durations other than 15 or 30 s "may experience limited scale". It does not contain "above 7 Mbps good", "15–30 Mbps recommended" or "avoid pull-downs". The sheet's frame-rate list and "native frame rate" wording match publisher-style guidance (IAB-003, Disney). StackAdapt is a plausible source because it is the likely display source and its CTV page is also gated, but this is **not established**.

## Coverage not verified

- Any live DSP or seller account, upload validation, creative audit or delivery. Nothing was uploaded.
- StackAdapt, Simpli.fi, Basis, Vistar, Viant, Xandr/Microsoft Invest spec pages (gated or not read). Xandr/Microsoft Invest CTV guidelines exist on learn.microsoft.com and were not read.
- YouTube on CTV (Google Ads / DV360 YouTube & partners), Samsung Ads, Vizio, LG, Paramount, NBCU/Peacock, Warner Bros. Discovery, Tubi and FAST channel specs.
- Safe title and action-safe percentages. Amazon provides a downloadable template image only. No inspected source published numeric safe areas.
- Closed captions, audio description, legal/regulatory disclaimers (for example UK Clearcast, US political ad rules) and QR code size rules (Disney refers to separate guidelines).
- The IAB CTV Ad Portfolio's per-format dimensions and signaling details beyond the 350 kB static limit.
- DOOH, native, audio and rich-media specifics beyond what appears incidentally in vendor documents.
- Whether any value changed after 2026-09-16.
