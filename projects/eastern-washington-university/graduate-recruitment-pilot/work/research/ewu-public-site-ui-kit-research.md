# EWU public-site UI kit research

**Purpose:** Source-backed reference for an Eastern Washington University UI kit in Figma. This documents what EWU publicly exposes about its `ewu.edu` WordPress implementation and separates documented facts from visual inferences.

**Reviewed:** October 27, 2026  
**Scope:** Public `www.ewu.edu` site and EWU’s public Web / MarCom documentation. No authenticated WordPress or server access.

## Executive read

EWU’s public marketing site runs on WordPress. EWU describes its components as a custom implementation of Advanced Custom Fields (ACF) Flexible Content. Public docs expose a component showcase, editor styles, a custom icon set, and internal web-team reporting tools. This is enough to model a useful Figma UI kit, but it does not establish exact source-code structures, plugin versions, or all visual tokens.

## Publicly documented implementation

| Finding | Evidence | Confidence |
|---|---|---|
| `www.ewu.edu` uses WordPress | [EWU Web team](https://www.ewu.edu/marcom/web/) and its [two-site WordPress explanation](https://inside.ewu.edu/mchildress/websites-at-ewu/) | Confirmed by EWU |
| The external and internal EWU sites are separate WordPress environments | [Websites at EWU](https://inside.ewu.edu/mchildress/websites-at-ewu/) | Confirmed by EWU |
| Component authoring is a custom implementation of ACF Flexible Content | [Web Tools & Reports](https://www.ewu.edu/marcom/web/tools/) describes its Component Report this way | Confirmed by EWU |
| EWU has a public component showcase | [Components List](https://www.ewu.edu/marcom/web/components/) | Confirmed |
| The theme has custom `ea` icon classes | [Icons](https://www.ewu.edu/marcom/web/icons/) and [Editing HTML](https://www.ewu.edu/marcom/web/wysiwyg-styles/) | Confirmed |
| Theme CSS supports custom rich-text classes and button variants | [Editing HTML](https://www.ewu.edu/marcom/web/wysiwyg-styles/) | Confirmed |
| The public WP REST index includes an `ewu/api` namespace | [WP REST API index](https://www.ewu.edu/wp-json/) | Confirmed; route purpose not established |
| Public domain infrastructure has an Azure-related DNS clue (`wp-ewu.azurewebsites.net`) | [Public DNS report](https://sitetrends.org/site/ewu.edu/) | Third-party clue; treat as tentative |
| EWU web Eagle Red is `#B7142E` | [Logo Usage Guide](https://cdn.ewu.edu/wp-content/uploads/2021/02/EWU-Logo-Usage-Guide.pdf) | Official guide; says web/video build RGB 183,20,46 |
| EWU recommends Arial as a universal system font closest to its brand font | [Logos, Templates & Standards](https://www.ewu.edu/marcom/logos-standards/) | Official recommendation for PowerPoint templates; not confirmation of the production website font |
| User-supplied webfont files identify as Open Sans 400 regular and 400 italic | Files supplied in this conversation: `memvYaGs…woff2` (roman) and `memQYaGs…woff2` (italic); filenames match Google Fonts Open Sans assets | Family/styles agree with the supplied theme CSS; supplied font subsets/versions are not fully inspected |
| The theme CSS sets the site body font to Open Sans, Helvetica, Arial, sans-serif; base body is 16px / 400 / 1.5 line-height | User-supplied theme-7d3014a760.min.css, body rule and :root font-family variable | Confirmed in the supplied stylesheet |
| Supplied theme CSS includes Font Awesome Free 6.7.2 and styles ea wrappers for inline SVG content | theme-7d3014a760.min.css header, @font-face blocks, and .ea svg rules | Confirmed; the per-name ea-* to SVG mapping is not present in this CSS |
| Stylesheet root includes EWU primary #b7142e, secondary #333, and responsive breakpoints at 576, 768, 992, and 1200px | Supplied theme-7d3014a760.min.css, :root | Confirmed; root also contains framework defaults |

## Component inventory

Names below follow the public Components page. Descriptions are concise paraphrases of its examples and notes.

| Component | Documented role / options |
|---|---|
| Hero image | Hero treatment is shown at the top of the showcase; rich-text guide references headings in the Hero component |
| Accordion | Expand/collapse grouped content; optional notes paragraph |
| Calls to Action | Highlighted links/actions |
| Catalog: Courses | Course details and catalog links |
| What You’ll Learn | Curriculum and requirements content; expandable area and plan of study |
| Columns | Two to six equal-width columns; optional full-width intro copy |
| Contact Cards | Contact details and biographies, photos, optional button |
| Copy with Image | 50/50, 25/75, small image, and YouTube options; crop and background pattern controls |
| Destination Eastern | Feature/resource links, icons, optional details and quote callout |
| Eastern Stories | Story feed with category filters |
| Events Display | Events presentation / calendar link |
| Link Cards | Highlighted link cards and buttons |
| Section Footer | Contact and institutional footer content |
| Stats Bar | Repeated statistics |
| Text | General rich-text content |
| Mirror Component | Custom mirror pattern named by the Web Tools page; individual component showcase details are not in the public Components List |

## Rich-text styles and editor markup

Source: [Editing HTML](https://www.ewu.edu/marcom/web/wysiwyg-styles/).

- H1–H3 receive the theme’s red underline by default.
- `hr-none` removes the heading underline; `hr-center` centers it.
- `steps-list` styles a sequence of steps.
- Buttons use `btn`, with `btn-md` / `btn-sm`, `btn-secondary`, and `red` variants.
- The theme applies a visible H1–H6 and paragraph type hierarchy.
- Standard `<blockquote>` markup is supported.
- Icon example: `<span class="ea ea-alumni"></span>`.
- Outlined heading text classes: `ewu-text-outline` and `ewu-text-outline-white` (recommended for Hero headings).

## Supplied production theme CSS

The user supplied `theme-7d3014a760.min.css` on October 27, 2026. It adds production-level detail beyond the public showcase:

- Base body style: white background, `#333` text, Open Sans / Helvetica / Arial sans-serif, 16px, weight 400, line-height 1.5.
- EWU theme variables include primary `#b7142e` and secondary `#333`; the file also includes framework color defaults and responsive breakpoints at 576, 768, 992, and 1200px. The exact framework/version is unconfirmed from this bundle alone.
- Component selectors confirm implementations for `.hero`, `.accordion`, `.calls-to-action`, `.copy-with-image`, `.contact-card`, `.destination-eastern`, `.eastern-stories`, `.events-display`, `.link-card`, `.section-footer`, `.stats`, and `.steps-list`, among others. These names can now anchor a closer Figma reconstruction.
- The stylesheet contains Font Awesome Free 6.7.2 CSS, but its font-face URLs point to a `fontawesome-6.4.2` folder. Resolve this version/path mismatch against matching deployed assets before relying on the font files.
- EWU's `.ea` rule styles inline SVG children and applies `currentColor`. The stylesheet does not contain class-by-class mappings from the 225 public `ea-*` names to SVG artwork. The three supplied Font Awesome font files therefore do not, by themselves, recover those custom EWU icons.

## Custom icon library

The [Icons page](https://www.ewu.edu/marcom/web/icons/) states a total of 225 names and demonstrates the markup `<span class="ea ea-alumni"></span>`. The supplied theme CSS indicates that `.ea` contains inline SVG. The names below are a reference index; the custom SVG source/mapping is still not included in the supplied CSS. Do not substitute a visually similar Font Awesome glyph and present it as EWU's original artwork.

```text
ea-alumni · ea-apple-books · ea-apple · ea-arrow-next · ea-art-frame · ea-bank-vault · ea-baseball · ea-basketball · ea-beach-chair · ea-binoculars · ea-book-open · ea-books · ea-briefcase · ea-building · ea-bus · ea-cactus-sun · ea-cactus · ea-calculator · ea-calendar · ea-canvas · ea-cash · ea-catalog · ea-certificate · ea-chart1 · ea-chart2 · ea-chat · ea-chevron-down · ea-chevron-left · ea-chevron-right · ea-chevron-up · ea-chevron · ea-clapperboard · ea-clipboard · ea-close · ea-coffee-cup · ea-coins · ea-communication · ea-community · ea-compass · ea-compensation-analyst · ea-computer-report · ea-computer · ea-contact · ea-covid-handwashing · ea-covid-mask · ea-covid-sanitizing · ea-covid-stop-spread · ea-covid-temp-scan · ea-credit · ea-crutches · ea-database · ea-diamond · ea-diaper · ea-digital-writing · ea-dining · ea-director-chair · ea-directory · ea-dna-strain · ea-document · ea-dollars · ea-eagle · ea-eaglenet · ea-ear · ea-electric-plug · ea-electrical-plug · ea-entrepreneur · ea-envelope · ea-facebook · ea-fax · ea-files · ea-film-reel · ea-fishing · ea-football · ea-garden · ea-gavel · ea-gears · ea-geologic-mapping · ea-gift · ea-global-supply · ea-globe · ea-gold · ea-grad-cap · ea-hand-coin · ea-hand-heart · ea-hand-plant · ea-handcuffs · ea-handshake · ea-hard-hat · ea-head-gear · ea-head-puzzle · ea-heart-leaves · ea-heartbeat · ea-hotair-balloon · ea-house-circulation · ea-hr-director · ea-hr · ea-human-services · ea-ice-skates · ea-id-badge · ea-import-export · ea-info · ea-instagram · ea-international-manager · ea-inventory · ea-key-turn · ea-leaves · ea-light-bulb · ea-lightbulb-leaves · ea-linkedin · ea-location-anderson · ea-location-dressler · ea-location-pearce · ea-location-snyamncut · ea-location-streeter · ea-lounge-chair · ea-machine-arm · ea-magnifying-glass · ea-mallet · ea-management · ea-map-marker · ea-medal · ea-medical-chart · ea-megaphone · ea-microphone1 · ea-microphone2 · ea-microscope · ea-minus · ea-molecule · ea-mountains · ea-museum · ea-music-notes · ea-nav-square-active · ea-nav-square-default · ea-network · ea-newspaper · ea-nonprofit · ea-number-1 · ea-number-2 · ea-number-3 · ea-number-4 · ea-number-5 · ea-number-6 · ea-open-sign · ea-open · ea-paint-palette · ea-pantone-guide · ea-paper-airplane · ea-pencil-paper · ea-pencil · ea-pennant · ea-person-locator · ea-phone · ea-piggy-bank · ea-planning · ea-plant · ea-plus · ea-police-car · ea-poster · ea-potted-plant · ea-presentation · ea-programming · ea-puzzle · ea-radio-tower · ea-read · ea-recorder · ea-recycling · ea-research1 · ea-research2 · ea-rocket · ea-roos-field · ea-running-shoes · ea-sales-chart · ea-scales · ea-scarecrow · ea-school · ea-search · ea-season-fall · ea-season-spring · ea-season-summer · ea-season-winter · ea-share · ea-shopping · ea-signs · ea-silverware · ea-snapchat · ea-soccer · ea-social-services · ea-speech-bubble · ea-squirrel · ea-stage-light · ea-stamps · ea-stethoscope · ea-stopwatch · ea-substance-abuse · ea-sunglasses · ea-syringe · ea-systems-dev · ea-taj-mahal · ea-target · ea-tech-writing · ea-test-tubes · ea-thumbs-up · ea-ticket · ea-tiktok · ea-token · ea-tooth · ea-toothbrush · ea-train · ea-trophy · ea-twitter · ea-umbrella · ea-us-capitol · ea-video-camera · ea-visit · ea-volleyball · ea-vote-btn · ea-warning · ea-washington-state · ea-waste-plant · ea-water-faucet · ea-water-tower · ea-website · ea-writing-tools · ea-x-twitter · ea-youtube
```

Count check: 225 names transcribed.

## Student Life page mapping

Source: [Student Life](https://www.ewu.edu/about/student-life/). These mappings are inferred from the public layout because the page does not expose its ACF field data.

| Visible section | Likely component(s) | Confidence |
|---|---|---|
| Hero: “Student Life at EWU” | Hero image | Medium |
| “Experience Eagle Nation” intro | Text / Copy with Image | Low–medium |
| Five student-life metrics | Stats Bar | High |
| Clubs & Organizations | Copy with Image and/or Calls to Action | Medium |
| Recreation & Adventure | Columns / Copy with Image | Medium |
| Sororities & Fraternities | Copy with Image | Medium |
| EWU Traditions | Columns, Copy with Image, or Text | Low–medium |
| Experience Checklist image grid | No exact documented match; likely custom composition or a component not represented in the showcase | Low |
| Events Calendar | Events Display | High |
| “We’ll Be There For You” service cards | Columns, Link Cards, or Copy with Image | Low–medium |
| “Be an #Eagle4Life” close | Calls to Action | High |

## Web tools EWU says it has

The [Web Tools & Reports page](https://www.ewu.edu/marcom/web/tools/) documents tools for staff, including:

- Component Report: component usage across pages (explicitly described as ACF Flexible Content implementation)
- Plugin Activation Status, Gravity Forms Report, Shortcode Report, and Mirror Content Report
- Site map, content search, menu report, media export, and crawler reports

These listings document tool availability, not anonymous access. The report contents may require EWU editor permissions.

## Figma UI kit plan

Create a native Figma file with a clear “observed / inferred / confirm” distinction. Suggested pages:

1. **Read Me** — source links, confidence legend, scope and known gaps.
2. **Foundations** — supplied theme CSS confirms Open Sans body typography and EWU red; neutrals, spacing, type ramp, border, radius and layout values remain inferred until measured.
3. **Components** — components documented above, with variants only where EWU’s public docs specify them (buttons, copy-with-image layouts, heading underline, outlined text).
4. **Icon reference** — icon names and sample glyphs only if assets can be obtained from the public site; otherwise list names and mark artwork pending.
5. **Page patterns** — a structural Student Life page map using inferred component relationships.

Do not claim the Figma kit is EWU’s source library. It is a reconstruction from public documentation and supplied CSS. The exact theme name, frontend JavaScript libraries and versions, complete CSS tokens, exact custom SVG icon mappings, and some component-to-page mappings remain unconfirmed. The supplied CSS confirms Open Sans as the public theme's base body font. EWU’s Web Tools Component Report and authenticated theme documentation could resolve remaining component/data gaps if editor access is available.

## Sources

- [Components List](https://www.ewu.edu/marcom/web/components/)
- [Editing HTML / WYSIWYG styles](https://www.ewu.edu/marcom/web/wysiwyg-styles/)
- [Icons](https://www.ewu.edu/marcom/web/icons/)
- [Web Tools & Reports](https://www.ewu.edu/marcom/web/tools/)
- [EWU Web team](https://www.ewu.edu/marcom/web/)
- [Websites at EWU](https://inside.ewu.edu/mchildress/websites-at-ewu/)
- [Student Life](https://www.ewu.edu/about/student-life/)
- [Public WP REST API index](https://www.ewu.edu/wp-json/)
- [Third-party DNS report](https://sitetrends.org/site/ewu.edu/)
