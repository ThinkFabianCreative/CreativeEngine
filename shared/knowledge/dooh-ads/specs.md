# DOOH specifications

Checked 2026-09-16. Structured records: [specifications.json](specifications.json). Conflicts and gaps: [source-conflicts.md](source-conflicts.md).

Classifications used below:

- **Requirement**: the source says it must be met.
- **Recommendation**: the source advises it or calls it standard or typical.
- **Snapshot**: a dated platform list that the platform itself says is not the source of truth.
- **Context**: industry or legal background, not a creative spec.

Screen inventory changes constantly. A venue-type row is never a guarantee for a specific network or screen.

---

## 1. Venue taxonomy

Programmatic DOOH platforms label screens with the **OpenOOH Venue Taxonomy**, which OAAA supports. Its IDs travel in OpenRTB bid requests. Platforms adopted different versions: the repository's adoption table lists Vistar on 1.0 (parent and child levels only) and Place Exchange and Broadsign on 1.1.

| Group (1.0 / 1.1 label) | Venue types used on platform spec lists | OpenOOH 1.2.1 (2 Feb 2026) changes worth knowing |
|---|---|---|
| Transit | Airports, Buses, Taxi & Rideshare TV, Taxi & Rideshare Top, Subway, Train Stations, Ferry | Singular names (Airport, Bus, Train). **Taxi & Rideshare Top (104) deprecated → Outdoor › Car Top (307).** Added Tram, Highway Rest Area; grandchildren such as Baggage Claim, Gates, Platform |
| Retail | Gas Stations → Fueling Stations, Convenience Stores, Grocery, Liquor Stores, Mall, Dispensaries → Cannabis Dispensaries, Pharmacies, Parking Garages | Adds Furniture, Apparel, Automotive, Laundromat, Vape Shop, Mass Merchandising, Consumer Electronic, Sporting Good, Pet Store, Office Supply, Home Renovation, Retail Other |
| Outdoor | Billboards, Urban Panels, Bus Shelters | Billboard children (Roadside, Highway, Spectacular) deprecated; adds Spectacular (304), Window Panel, Moving Billboard, Car Top, Aerial, EV Charging Station |
| Health & Beauty | Gyms, Salons, Spas | Adds Tattoo |
| Point of Care | Doctor's Offices, Veterinary Offices | Adds Dentist Office, Hospital, Urgent Care, Physiotherapy |
| Education | Schools, Colleges and Universities | Grandchildren: Residence, Common Area, Athletic Facility, Dining |
| Office Buildings | Office Buildings | Adds Warehouse; grandchildren Elevator, Lobby, Gym, Break Room |
| Entertainment (1.0) / Leisure (1.1) / Entertainment (1.2) | Recreational Locations, Movie Theaters, Sports Entertainment, Bars, Casual Dining, QSR, Hotels, Golf Carts, Night Clubs, High-End Dining | High-End Dining deprecated; adds Casinos, Convention Center |
| Government | DMVs, Military Bases, Post Offices | Adds First Responder Facility |
| Financial | Banks | — |
| Residential | Apartment Buildings and Condominiums | Grandchildren Lobby, Elevator, Gym |

Source: [openooh/venue-taxonomy](https://github.com/openooh/venue-taxonomy) (spec 1.2.1; JSON updated 2026-09-08). The repository README still labels v1.1 "Current Version". **DOOH-047.**

---

## 2. Common canvases and where they are used

| Canvas (px) | Shape | Seen for | Sources |
|---|---|---|---|
| 1920×1080 | 16:9 landscape | Nearly all place-based venues, airports, taxi TV, urban panels, train stations, GSTV | Vistar 2023, Vistar help, Place Exchange, Broadsign, DMI, GSTV |
| 1080×1920 | 9:16 portrait | Urban panels, bus shelters, malls, office, residential, airports, gyms; TTD calls it the most consistently used size across DOOH SSPs | Vistar, PX, TTD, Broadsign, DMI |
| 1400×400 | 7:2 | US digital bulletins; PX also uses it for taxi tops and transit | Lamar, Vistar, PX, Broadsign, TTD |
| 840×400 | ≈2.1:1 | US digital posters | Lamar, Vistar, PX, TTD |
| 1280×960 | 4:3 | Bars, casual dining, buses, convenience, gas stations, taxi TV | Vistar 2023, Vistar help, Broadsign; PX 2024 only |
| 1366×768 | ≈16:9 | Doctor's and veterinary offices | Vistar 2023, TTD (Broadsign and Hivestack examples) |
| 3840×1080 | 32:9 | Malls, movie theatres | Vistar 2023 |
| 560×160, 1920×674, 384×124, 384×128 | Wide strip | Taxi and rideshare tops | Vistar 2023, Firefly (560×160 and 1920×674), TTD (Hivestack 560×160) |
| 728×90, 300×250, 1024×576, 640×360 | IAB-like or small | Grocery and mall screens, gyms (static), taxi TV (640×360 video only) | Vistar 2023 |
| 3840×2160, 1920×1200, 1600×1200 | UHD, 16:10, 4:3 | European screen standard | DMI 2020 |
| 864×432 | 2:1 | UK roadside digital 48-sheet | Bauer Media Outdoor UK |

Vistar resizes and letterboxes creative into five standard sizes: 1080×1920, 1280×960, 1920×1080, 840×400 and 1400×400. The OpenOOH creative-formats draft (2021) proposes letterboxing rather than cropping when sizes don't match. Neither guarantees how a given media owner will render off-size creative.

---

## 3. Records

### DOOH-001 to DOOH-045 · Vistar Media venue-type spec list (2023 snapshot)

Source: [DOOH – VISTAR Specifications PDF](https://coegipartners.com/wp-content/uploads/2023/12/DOOH-Vistar-Media-Specifications.pdf) · checked 2026-09-16 · status **SOURCE_ISSUE**

| Field | Value | Classification |
|---|---|---|
| Provenance | Vistar-branded list; PDF created 2023-12-08; hosted on a third-party agency domain | Snapshot |
| Static file | JPG | Snapshot |
| Video file | MOV or MP4 | Snapshot |
| Max file size | 10 MB static; 50 MB video | Snapshot |
| Static color space | "RGB and CMYK" (see conflicts) | Snapshot |
| Approval | All creative subject to media-owner approval and category/content restrictions | Requirement |
| Caveat on several venues | Specs vary by screen; refer to the DSP or Vistar for exact specs | Recommendation |

| ID | Group › Venue type (row) | Canvases | Static | Video | Duration | Audio | Conditions |
|---|---|---|---|---|---|---|---|
| 001 | Transit › Airports (1) | 1920×1080 | Y | Y | :10 | N | |
| 002 | Transit › Airports (2) | 1920×1080, 1080×1920 | Y | Y | :15/:30 | Y | |
| 003 | Transit › Airports (3) | 1920×1080 | Y | Y | :15/:30 | Y | |
| 004 | Residential › Apartment Buildings | 1920×1080, 1080×1920 | Y | Y | :15/:30 | N | |
| 005 | Entertainment › Bars | 1080×1920, 1920×1080, 1280×960 | Y | Y | :15/:30 | Varies | |
| 006 | Outdoor › Billboards | 1400×400, 840×400, 1000×400, 1600×400, 1200×400, 600×600 | Y | **N** | — | N | Static only; LED design tips |
| 007 | Outdoor › Bus Shelters | 1080×1920 | Y | N | — | N | Static only |
| 008 | Transit › Buses | 1280×960 | Y | Y | :15/:30 | N | |
| 009 | Entertainment › Casual Dining | 1920×1080, 1280×960 | Y | Y | :15/:30 | Varies | |
| 010 | Education › Colleges and Universities | 1920×1080 | Y | Y | :15/:30 | Varies | |
| 011 | Retail › Convenience Stores (1) | 1920×1080, 1080×1920 | Y | Y | :15/:30 | N | |
| 012 | Retail › Convenience Stores (2) | 1920×1080, 1080×1920, 1280×960 | Y | Y | :15 | N | |
| 013 | Retail › Dispensaries | 1920×1080 | Y | Y | :15/:30 | N | |
| 014 | Government › DMVs | 1920×1080 | Y | Y | :15/:30 | N | |
| 015 | Point of Care › Doctor's Offices (1) | 1920×1080 | Y | Y | :15/:30/:60 | Y | |
| 016 | Point of Care › Doctor's Offices (2) | 1366×768 | Y | Y | :15 | Y | |
| 017 | Retail › Gas Stations | 1280×960, 1920×1080 | Y | Y | :15 | Y | No :30 stated |
| 018 | Retail › Grocery (1) | 1920×1080, 728×90 | Y | Y | :15 | N | |
| 019 | Retail › Grocery (2) | 1080×1920 | Y | Y | :08 | N | |
| 020 | Retail › Grocery (3) | Audio only | N | N | :15/:30 | Y | MP3/AAC required |
| 021 | Health & Beauty › Gyms (1) | 1920×1080 | Y | Y | :15/:30 | Varies | |
| 022 | Health & Beauty › Gyms (2) | 1920×1080, 300×250 | Y | N | — | N | Static only |
| 023 | Health & Beauty › Gyms (3) | 1920×1080 | Y | Y | :15/:30 | N | |
| 024 | Entertainment › Hotels | 1920×1080, 1600×900 | Y | Y | :15/:30/:60 | N | 1600×900 line: ":10s – :115s video spots" |
| 025 | Retail › Liquor Stores | 1920×1080 | Y | Y | :15/:30 | N | |
| 026 | Retail › Malls (1) | 1920×1080, 1080×1920 | Y | Y | :10/:15/:30 | Y | |
| 027 | Retail › Malls (2) | 3840×1080 | Y | Y | :15/:30 | Y | |
| 028 | Retail › Malls (3) | 1080×1920, 728×90, 1024×576 | Y | Y | :15 | N | |
| 029 | Entertainment › Movie Theatres | 1920×1080, 1080×1920, 3840×1080 | Y | Y | :15/:30 | Y | 3840×1080 :15 only |
| 030 | Office Buildings | 1920×1080, 1080×1920 | Y | Y | :15/:30 | N | 1080×1920 :15 only |
| 031 | Retail › Parking Garages | 1920×1080 | Y | Y | :15/:30 | Y | |
| 032 | Retail › Pharmacies | 1920×1080 | Y | Y | :15/:30 | N | |
| 033 | Entertainment › Recreational Locations | 1920×1080 | Y | Y | :15/:30 | Varies | |
| 034 | Health & Beauty › Salons | 1920×1080 | Y | Y | :15 | Y | |
| 035 | Entertainment › Sports Entertainment (1) | 1920×1080 | Y | Y | :15/:30 | N | |
| 036 | Entertainment › Sports Entertainment (2) | 1920×1080 | Y | N | — | N | Static only |
| 037 | Entertainment › Sports Entertainment (3) | 1080×1920, 1920×1080 | Y | Y | :15 | N | |
| 038 | Transit › Subway | 1080×1920, 1920×1080 | Y | Y | — (blank) | N | No duration stated |
| 039 | Transit › Taxi and Rideshare Top | 560×160, 1920×674, 384×124, 384×128 | Y | Y | :08; :01–:480 for 384×128 only | N | |
| 040 | Transit › Taxi and Rideshare TV (1) | 1920×1080, 1280×960, 1920×674, 640×360 | Y | Y | :15/:30 | Y | No static at 640×360 |
| 041 | Transit › Taxi and Rideshare TV (2) | 1920×1080 | Y | Y | :10–:30 | Y | |
| 042 | Transit › Train Stations | 1920×1080, 1080×1920, 1400×400, 3840×3240, 3600×720, 2480×720, 2400×720, 1680×720, 2160×640, 1280×320 | Y | Y | :15 | N | 1920×1080, 1080×1920 and 1400×400 are static only |
| 043 | Outdoor › Urban Panels (1) | 1080×1920, 2160×2160 | Y | N | — | N | Static only; 2160×2160 black and white only |
| 044 | Outdoor › Urban Panels (2) | 1080×1920, 1920×1080 | Y | Y | :15 | N | |
| 045 | Point of Care › Veterinary Offices | 1366×768 | Y | Y | :15 | Y | |

### DOOH-046 · Vistar Media: Creatives best practices

Source: [help.vistarmedia.com](https://help.vistarmedia.com/hc/en-us/articles/360059687631-Creatives-Best-Practices) · updated 2026-05-20 · checked 2026-09-16 · **DOCUMENTED**

| Field | Value | Classification |
|---|---|---|
| Source of truth | Deal Desk specs by venue type and media owner, or a media owner's Deal Summary Export | Requirement (stated as source of truth) |
| Pre-RFP overview | A monthly-updated dashboard; did not load on the research date | — |
| Images | JPEG preferred over PNG; hosted by the DSP; sizes must match the bid request | Recommendation / requirement |
| Video | VAST only, at most one redirect | Requirement |
| HTML5 | Not accepted | Requirement |
| Standard resolutions | 1080×1920, 1280×960, 1920×1080, 840×400 (poster), 1400×400 (bulletin) | Recommendation |
| Resizing | Vistar may resize and letterbox; Deal Desk resizing from layered PSD in 5 business days | Context |
| Approval | Media owner must approve every creative | Requirement |

### DOOH-048 · OpenOOH creative-formats (draft)

Source: [openooh/creative-formats](https://github.com/openooh/creative-formats) · last commit 2021-03-08 · **SOURCE_ISSUE**

| Field | Value | Classification |
|---|---|---|
| Candidate sizes | 1920×1080, 1080×1920, 1024×768, 1400×400 (→1920×540, 720×208, 560×160), 840×400 | Draft |
| Candidate ratios | 16:9, 9:16, 4:3, 7:2 | Draft |
| Candidate durations | 6, 10, 15, 30 s | Draft |
| Containers / codecs | JPG, PNG, MP4, HTML5; H.264; AAC/MP3 | Draft |
| Mismatch handling | Letterbox up to ~10%; no cropping; freeze last frame when a video is shorter than its slot | Draft |

### DOOH-049 · Place Exchange: DOOH creative specs overview

Source: [Spec_Best_Practices_One_Sheet.pdf](https://www.placeexchange.com/assets/marketing/Spec_Best_Practices_One_Sheet.pdf) · PDF created 2026-03-26 · checked 2026-09-16 · **DOCUMENTED**

| Field | Value | Classification |
|---|---|---|
| Display sizes | 1920×1080, 1080×1920 (Entertainment, Health and Beauty, Movie Theaters, Office Buildings, Point of Care, Residential, Retail, Transit, Urban Panels); 1400×400 and 840×400 (Billboards, Taxi Tops, Transit) | Recommendation (about 85% of inventory) |
| Video sizes | 1920×1080, 1080×1920, 1400×400 (Taxi Tops, Transit) at :15 | Recommendation |
| Static | .jpg or .png, 72 ppi, RGB | Standard |
| Video | .mp4, even-numbered pixel resolution, <5,000 kbps, 30 fps | Standard |
| File size | Varies by publisher | — |
| Exceptions | Spectaculars vary by screen; select airport inventory uses non-standard sizes and typically :10 | Context |
| Lead time | 3 business days before launch; 7 for spectaculars, airports and controlled inventory | Requirement |
| Tags | Static display tags without animation or HTML, or VAST (no VPAID); no DV/IAS/MOAT wrappers | Requirement |

### DOOH-050 · Place Exchange: pharma best practices (2024)

Source: [PX_Pharma_Best_Practices.pdf](https://www.placeexchange.com/assets/marketing/PX_Pharma_Best_Practices.pdf) · PDF created 2024-03-26 · **SOURCE_ISSUE** (older sizing than DOOH-049)

| Field | Value | Classification |
|---|---|---|
| Video length | ≤15 s recommended; longer for stationary venues (bars, doctors' offices, gyms) | Recommendation |
| Motion for mobile audiences | Play video at reduced speed | Recommendation |
| Contrast | At least 4.5:1, optimally 7:1 | Recommendation |
| Branding | Brand or logo on screen at all times | Recommendation |
| Audio | "May be supported in some contexts" | Context |
| Top display sizes (2024) | 1920×1080, 1080×1920, 1400×400, 1280×960 | Superseded by DOOH-049 |

### DOOH-051 · The Trade Desk: creative specifications, DOOH section

Source: [Creative_Specifications-en.pdf](https://www.thetradedesk.com/assets/global/documents/Creative_Specifications-en.pdf) · Last-Modified 2025-03-10 · **SOURCE_ISSUE** (restates SSP specs)

| Field | Value | Classification |
|---|---|---|
| Reach size | 1080×1920 ("D6") used consistently across DOOH SSPs | Recommendation |
| Broadsign (billboard/street) | JPG or PNG; 40 KB (750 KB max); billboards 1400×400, 840×400; transit centers and street panels 1080×1920, 1920×1080 | Restated recommendation |
| Broadsign (place-based) | Train stations 1280×720; airports 720×1280; doctors' office 1366×768 | Restated recommendation |
| Ströer | MP4 with no audio track; 5–30 s; 25/29.97/30 fps; H.264; ≤12 Mbps | Restated recommendation |
| Hivestack | JPG, PNG, BMP, MP4, MOV, WEBM, FLV, AVI, MPG; <10 MB; 1920×1080, 560×160, 1080×1920, 1280×720, 1366×768 | Restated recommendation |

### DOOH-052 · Broadsign: DOOH specs guide

Source: [broadsign.com blog](https://broadsign.com/blog/dooh-specs-guide-what-media-buyers-and-planners-need-to-know-before-launching-a-campaign/) · published 2026-06-17 · **DOCUMENTED** (vendor guidance)

| Field | Value | Classification |
|---|---|---|
| Common sizes | 1920×1080, 1080×1920, 1400×400, 1280×960 | Recommendation |
| Static | JPG/PNG, 72 ppi, RGB | Recommendation |
| Video | MP4, even-numbered resolution, <5,000 kbps, 30 fps | Recommendation |
| Durations | 8, 10, 15, 30 s; 15 s as default | Recommendation |
| HTML5 / DCO | Needs publisher pre-approval | Requirement |

### DOOH-053 · Digital Media Institute (Germany): DOOH creative specifications v2.0

Source: [DMI_Standards_DOOH_Creative_Specs.pdf](https://www.dmi-org.com/download/DMI_Standards_DOOH_Creative_Specs.pdf) · dated 2020-09-09 · **SOURCE_ISSUE** (European, 2020)

| Field | Value | Classification |
|---|---|---|
| Video sizes | 1920×1080, 3840×2160, 1920×1200, 1080×1920, 2160×3840; 1600×1200 (4:3) | Industry standard (EU) |
| Encoding | H.264 in MP4; 25 fps progressive; 6–10 Mbit/s VBR (FHD), 24–40 Mbit/s (UHD) | Industry standard (EU) |
| Max video size | ≈1 MB per second (FHD and 4:3), 4 MB per second (UHD); e.g. 15 MB for a 15 s FHD spot | Industry standard (EU) |
| Stills | Uncompressed JPG at the same sizes; 6 MB FHD, 24 MB UHD | Industry standard (EU) |
| Roadside | Stills needed for street and highway videoboards where moving images are prohibited | Context |

### DOOH-054 · Lamar: programmatic media formats

Source: [lamar.com media formats](https://lamar.com/en/products/programmatic/media-formats) · checked 2026-09-16 · **DOCUMENTED**

| Field | Value | Classification |
|---|---|---|
| Billboard sizes | 1400×400 and 840×400 reach over 90% of Lamar screens | Recommendation |
| Rotation | Every 6–10 s depending on location | Context |
| QR codes | Not permitted on Lamar DOOH | Requirement |
| Airports | 1920×1080, 1080×1920 | Documented |
| NYC urban panels | 480×672, static or video; alcohol, political and cannabis ads prohibited | Documented |
| File type, motion | — | — |

### DOOH-055 · Lamar: individual panel spec sheet (example)

Source: [Panel 37202 spec sheet](https://resources.lamar.com/SMCoreServices/public/materials/pdf/reports/specsheet/424/37202/) · "Updated 9/2026" · **DOCUMENTED** (single panel)

| Field | Value | Classification |
|---|---|---|
| Size | 1400×400 at 72 ppi (autoscale bulletin template) | Requirement for this panel |
| Color | RGB; convert PMS; black R0 G0 B0; LED whites may tint | Requirement / context |
| Scope | Each Lamar panel has its own sheet | Context |

### DOOH-056 · GSTV (fueling stations)

Source: [GSTV editorial guidelines](https://www.gstv.com/editorial-guidelines) and linked Creative Best Practices and Video Spec Guide PDF (uploaded July 2025) · **DOCUMENTED**

| Field | Value | Classification |
|---|---|---|
| Resolution | 1920×1080 | Requirement |
| File | MP4, H.264, 29.97 fps, target 20 Mbps, max 100 MB | Requirement |
| Duration | 5 s min, 30 s max; longer by arrangement with a GSTV rep | Requirement |
| Audio | AAC; 48 kHz/24-bit min (96 kHz preferred); true peak –2 max; M&E on left, dialogue/VO on right; avoid 20–250 Hz | Requirement / recommendation |
| Safe area | Title safe within a 4:3 center cut (serves 4:3 and 16:9 screens) | Recommendation |
| Type | Bold type; legal copy at least 8 pt; high contrast; no motion blur | Recommendation |
| QR | ≥250×250 on 1920×1080 (200×200 floor); centre or lower corners; for the whole spot or at least 15 s | Recommendation |
| Lead time | Ready-to-air spots 5 business days before air | Requirement |

### DOOH-057 / DOOH-058 · Firefly (taxi and rideshare tops, taxi TV)

Source: [Firefly NYC taxi advertising design guide](https://www.fireflyon.com/blog/nyc-taxi-advertising-design-guide) · published 2026-07-07 · **DOCUMENTED**

| Field | Value | Classification |
|---|---|---|
| Top: canvas | 560×160; 1920×674 required for NYC | Requirement |
| Top: static | PNG, RGB, 72 ppi, ≤3 MB | Requirement |
| Top: video | MP4, "29.974 fps" (as published), 8 s, ≤5 MB | Requirement |
| Top: copy | Seven words or fewer | Recommendation |
| Top: lead time | 3 business days | Requirement |
| TV: video | ≥1280×720 (16:9); MP4/MOV/WMV; ≥1,200 kbps | Requirement |
| TV: companion | Optional 120×450 vertical banner, ≤100 KB | Documented |
| TV: lead time | 5 business days | Requirement |

### DOOH-059 · OUTFRONT

Sources: [posting standards](https://www.outfront.com/posting-standards), [digital OOH page](https://www.outfront.com/media/digital-ooh) · **SOURCE_ISSUE** (no pixel or file specs published on these pages)

| Field | Value | Classification |
|---|---|---|
| Spot | Purchased increment, e.g. 8 or 15 s, within a rotating loop | Definition |
| Typical length | Billboards 8–10 s; transit 10–15 s | Context |
| Lead time | At least ten working days before start | Requirement |
| Delivery guarantee | 92.5% of contracted display time | Context |

### DOOH-060 · Clear Channel Outdoor (US)

Source: [CCO blog, 2025-02-20](https://clearchanneloutdoor.com/blog/printed-vs-digital-billboards-how-to-choose-the-right-format-for-your-campaign/) · **SOURCE_ISSUE**. Digital billboards rotate ads in slots of "typically 8 seconds". No public US file or pixel spec was found.

### DOOH-061 · Bauer Media Outdoor UK: Billboard Live (roadside digital 48-sheet)

Source: [bauermediaoutdoor.co.uk](https://www.bauermediaoutdoor.co.uk/resources/specifications/billboard-live-specification) (the former clearchannel.co.uk URL redirects here) · **DOCUMENTED** · UK only

| Field | Value | Classification |
|---|---|---|
| Canvas | 864×432 | Requirement |
| File | JPG/PNG, RGB, ≤1 MB (≤20 MB programmatic) | Requirement |
| Slot | 10 s unless agreed | Context |
| Video | Not supported | Requirement |
| Text | Min 8 px, 12 px recommended; nothing that mimics traffic signs or distracts drivers | Requirement / recommendation |

### DOOH-062 / DOOH-063 · Roadside digital billboards: regulation context

Sources: [OAAA compendium of state changeable-message laws (PDF, 2019)](https://oaaa.org/wp-content/uploads/2022/11/Changeable-Message-Digital-Technology-Compendium-2019.2.pdf) (**SOURCE_ISSUE**, dated); [OAAA digital traffic safety brief](https://oaaa.org/policy-advocacy/policy-issue-briefs/digital-traffic-safety/) (**DOCUMENTED**)

| Field | Value | Classification |
|---|---|---|
| Typical operation | Static messages, typically 6 or 8 s | Context (OAAA) |
| Motion | Many state rules prohibit animation, scrolling, flashing or full-motion video. Examples: Arizona (no animation), and state texts barring "full-motion video" | Context (legal, 2019) |
| Minimum dwell | Varies by state, commonly 6–10 s and 4 s in some. Arizona and Tennessee: static at least 8 s, transition 2 s or less | Context (legal, 2019) |
| Federal | FHWA guidance memo of 2007-09-25 is cited as the basis for state regulation | Context |
| Exception noted | Washington listed as prohibiting changeable message technology (2019) | Context |

Local ordinances, permits and on-premise versus off-premise rules also apply. Check the media owner's current rules for each board. This is not legal advice.

### DOOH-064 to DOOH-068 · UNVERIFIED legacy-sheet items

Schools (1920×1080, :15/:30), Spas (1920×1080, :15), billboard 990×495 and 806×390, :06 durations for Subway and Train Stations, and 1080×1920 for Gyms. No primary source read supports these. See [source-conflicts.md](source-conflicts.md).

---

## 4. File conventions across sources

| Item | Convergent practice | Where sources differ |
|---|---|---|
| Static type | JPG (Vistar prefers JPEG); PNG widely accepted | Vistar 2023 list JPG only; Firefly tops PNG; DMI uncompressed JPG; legacy Lamar JPG/BMP/GIF, no animated GIF |
| Video type | MP4 / H.264 | Vistar list also MOV; Hivestack many containers; Vistar programmatic by VAST only |
| Frame rate | 30 fps (PX, Broadsign); 29.97 (GSTV) | 25 fps (DMI, Europe); Ströer 25/29.97/30 |
| Bitrate | <5,000 kbps (PX, Broadsign) | GSTV targets 20 Mbps; DMI 6–10 Mbit/s FHD; Ströer ≤12 Mbps |
| File size | Set by the publisher | Vistar 10 MB / 50 MB; Hivestack <10 MB; Broadsign static 750 KB (via TTD); Bauer 1 MB / 20 MB; GSTV 100 MB; Firefly 3 MB / 5 MB |
| Color | RGB, 72 ppi | Vistar 2023 list says "RGB and CMYK" |
| HTML5 / dynamic | Only where the publisher supports it | Vistar: not accepted; PX: not in standard tags; Broadsign: publisher pre-approval |
| Audio | Silent by default | Audio-on networks exist (GSTV, taxi TV, some point-of-care, malls, cinemas); Ströer requires no audio track |

## 5. Durations: spot, slot and loop

- A **spot or slot** is the time bought in a rotating loop (OUTFRONT: e.g. 8 or 15 s). A **video length** must fit the spot. Common programmatic lengths are :08, :10, :15 and :30. :15 is the most common default (PX, Broadsign).
- Roadside billboards take static images that hold for the slot, usually 6–10 s (Lamar, CCO, OAAA).
- Airports often use :10 (PX exception note; Vistar airports row 1).
- Taxi tops use :08 (Vistar, Firefly).
- Stationary venues with long dwell take longer spots: :60 at doctor's offices and hotels, up to :115 on one hotel network (Vistar 2023), and PX notes bars, doctors' offices and gyms.
- The OpenOOH draft suggests freezing the last frame when a video is shorter than its slot. Confirm per network.

## 6. Creative and legibility guidance (attributed)

| Guidance | Source |
|---|---|
| One idea; bold, high-contrast colours; limited elements | Place Exchange 2024; Lamar |
| Text contrast at least 4.5:1, optimally 7:1 | Place Exchange 2024 |
| Billboard text at least 15 px tall | Vistar 2023 list |
| UK roadside text at least 8 px, 12 px recommended | Bauer UK |
| Seven words or fewer (taxi tops) | Firefly |
| Avoid white backgrounds on LED; strong focal point; bold colours by day, pastels at night | Vistar 2023 list; Lamar |
| Keep the brand on screen throughout | Place Exchange 2024 |
| Slower video pacing for people on the move | Place Exchange 2024 |
| No motion blur; bold, dark type; legal copy at least 8 pt; title-safe 4:3 centre cut | GSTV |
| No QR codes on Lamar DOOH; QR sizing rules on GSTV | Lamar; GSTV |
| Don't mimic traffic signs on roadside screens | Bauer UK |
