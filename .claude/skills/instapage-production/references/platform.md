# Instapage platform facts

Documentation reviewed 2026-09-24 against Instapage's Help Center, the Public API reference and the MCP guide, all read that day. Paraphrased; the linked articles are the source (list at the end). "Updated" dates are the articles' own.

No target workspace or runtime was inspected. See `capability-map.md` for per-feature status and the recheck notes below. Documentation is not implementation validation.

Instapage changes often, and several features depend on the plan or are rolling out gradually. Re-check a fact before a spec depends on it, when it is older than 90 days, or when the editor behaves differently. Record every divergence in §15 with its date.

## 1. Page model

- New pages are standard pages: blank, from a template, or uploaded as an `.instapage` file. AMP pages can no longer be created (Instapage notes Google phased AMP out in 2025). [New page]
- Every page renders with the Thor engine. Custom code has to be written for it. [Thor]
- A page is a vertical stack of **blocks**. There are two kinds:
  - **Canvas blocks** (Instablocks): fixed layout, elements placed freely, a separate mobile arrangement.
  - **Fluid Grid Blocks**: a grid of containers that reflows by itself (§3).
  Block templates exist for both kinds. [Block Templates; Fluid Grid]
- The first and/or last block can be made a sticky header or footer in page settings. Stickiness does not show in the editor, only on a published page. [Sticky Bar]
- **Popups** are built in a popup builder (Assets > Popups) and opened on click or by page triggers. A global popup pushes its changes to every page that uses it. Earlier notes claimed a white-only popup background; this was not found in the rechecked popup article. Treat it as OPEN, not a platform mandate. [Popups, updated 2026-03-27; Assets]

## 2. Elements and widgets

| Element | What it does natively | Limits | Source |
|---|---|---|---|
| Headline | Text box; tag selectable h1 to h6; bold, italic, underline, strikethrough, sub/superscript; weight and size per box | No lists | Text boxes (2026-03-27); h tags |
| Paragraph | Text box; ordered and unordered lists, custom list markers (SVG recommended), marker color | — | Text boxes |
| Button | Label and a link: outside URL, a published Instapage page, a popup, an on-page anchor, or a file download. Options: new tab, count as conversion, pass URL parameters, Google Analytics event | Form submit buttons are configured in the form, not here | Links |
| Image | From the workspace image library; mask (crop), set as block or page background, link, alt text | Under 30 MB; WEBP, PNG, JPEG, GIF, SVG; at most 4000 × 4000 px, ideally uploaded at the size used. Alt text changed in the library applies only to future inserts, not to images already placed | Images |
| Video | YouTube, Vimeo or Wistia by URL; accessibility title; muted autoplay; progress bar on or off for YouTube | Other hosts, uploaded files and looping need an HTML embed | Videos |
| Form | A Form Library form, on the page or in a popup (§6) | — | Add a form |
| Box, Circle | Fill, opacity, background image, drop shadow | Not allowed inside Fluid Grid Blocks. Cannot take a click action | Shapes; Fluid Grid |
| Line | Horizontal or vertical | Vertical lines show on desktop only by default | Shapes |
| Timer | Counts down to one fixed date and time; color, language, label position | Not evergreen or per-visitor; stays at zero after the date for everyone; labels are not shown on mobile | Timer |
| Accordion | Collapsible text sections; background, arrow and divider style, vertical spacing, separate text styles for section titles and content | Text only: no images or links inside. Recommended inside Fluid Grid Blocks so the block grows as sections open | Accordion |
| Carousel | Slides that can hold any elements; autoplay, arrows, dots, loop (three slides or more), transition time, background | Use inside Fluid Grid Blocks is not documented | Carousel |
| HTML | Custom HTML widget | Sits on top of the page structure: not part of its responsiveness, native integrations, lead collection, lead notifications or form-submission conversion goals. Some embeds render in preview; the vendor recommends published testing. Record unavailable draft tests as NOT_RUN. Instapage support does not troubleshoot it | Embedding custom HTML |

Every element can be set visible on desktop and mobile, desktop only, or mobile only. Right-clicking an element also offers Duplicate, Order and Edit CSS (§10). [Page builder; Hiding elements]

## 3. Fluid Grid Blocks

- Built on CSS Grid. Insert one from preset layouts, or make a custom grid in the Fluid Block Editor (starts at 3 × 3; add or remove rows and columns). Containers occupy one cell or span several.
- Allowed inside: headlines, paragraphs, forms, images, buttons, HTML, video, horizontal and vertical lines, timers. Shapes are not.
- Each container sets its padding (px, %, rem, em, vh, vw), element flow (horizontal or vertical), justify and align, and the space between elements. It can have a background color or image, a border and rounded corners.
- Block padding is separate from container padding. Instapage recommends at least 20 px on the left and right of the block, and advises against vh for left or right padding.
- Containers are numbered and stack in that order on mobile. The mobile layout is edited on its own: containers can be reordered, resized or hidden there. A swap applies only to the viewport where it is made. Instapage suggests a common-denominator grid (for example 6 columns for 3-up desktop and 2-up mobile).
- A deleted container leaves an empty cell that stays empty on the live page. A hidden container can only be shown again from the block layout editor.
- A Fluid Grid Block can be saved to My Blocks or as a Global Block (§8).

[Fluid Grid Blocks, updated 2026-03-02; Fluid Block Editor]

## 4. Responsive model

- The guide says below 768 px is mobile and above 768 px desktop; exactly 768 is unspecified and requires an observed test. A tablet in portrait gets mobile, in landscape desktop. The mobile version has to be switched on.
- Canvas blocks respond up to 1200 px wide (editor guides at 960 and 1200 px; the inner column is fixed). The mobile canvas is 400 px wide.
- The mobile version uses the same elements as desktop, rearranged and resized. The current mobile guide documents moving an element to a different parent block, also changing its desktop parent. Earlier guidance said this was impossible; confirm rollout in the workspace. Hiding a block hides its elements. "Regenerate" rebuilds the mobile arrangement from desktop. Groups and the mobile aspect-ratio lock keep arrangements together.
- Device-specific settings, in limited release: width, height, padding, font size, line height, text alignment, list styles and custom styles per device; form field label size; image size, background position and top margin.
- Elements can be hidden per device. Blocks can be hidden on mobile but never on desktop.

[Responsiveness; Regenerate; Optimizing for mobile; Hiding elements; Alignment and grouping]

## 5. Type and color

- A page has three font roles: headlines, paragraphs and buttons. Forms use the paragraph family. Size and weight are set per text box; available weights depend on the font.
- 40 preloaded Google fonts, the wider Google library, and custom fonts added in Assets > Fonts, which needs an Owner or Manager and, for fonts not linked through Adobe, a qualifying plan. The client must hold the licence.
- Assets > Styles holds up to 14 brand colors (hex), the default fonts for new pages, and the favicon. Styles are defaults: changing them does not change existing pages, except the favicon, which applies to every page in the workspace. There is no live token system.

[Setting the fonts; Text boxes; Assets, updated 2026-03-27]

## 6. Forms

- Forms live in the Form Library (Assets > Forms), are built in a drag-and-drop form builder, and can be reused across pages.
- Fields: predefined (first and last name, email, phone, website, company, job title, street address, city, state or region, industry, company size, country, gender, marital status) and custom (single-line text, dropdown, checkbox, radio, and a GDPR/terms checkbox whose label can hold links). Any field can be required or not; the asterisk can be hidden separately. Single-line fields can be hidden (hidden fields) and validated, for example as email.
- Multistep forms, with back navigation and optional step dots.
- After submitting: redirect to an Instapage page or an outside URL, **or** download a file. The two cannot be combined. URL parameters can be passed on. A thank-you message shows for a set time, or is removed (a "Processing…" text then shows).
- Style: label position, label and input text colors, field color, border, inner shadow; submit button radius, font, colors and hover, fixed size, shadow, border; button text and its aria-label.
- The form's own font size cannot be changed; only the submit button's font can (see §15 for a limited-release exception).
- No native conditional logic. Forms can also be sent to automated emails and GA events.
- Submissions cannot be tested in preview; the page has to be published.

[Form Builder and Form Library, updated 2026-08-21; Add a form]

## 7. Integrations, conversion goals and leads

- Per page experience, in the slideout: **Marketing Tags & Pixels** (Google Ads, Google Analytics / GA4, Meta Pixel, Google Tag Manager), **Form Integrations** (CRM and marketing-automation accounts connected at account level), **Lead Notifications** (email recipients per page). Zapier and webhooks cover tools with no direct integration.
- **Conversion goals**, per page: clicks on native links (buttons, images, text), native form submissions, or a visit to an external URL. On-page and external goals are mutually exclusive. Link and form goals can run together, but analytics then show one total with no breakdown by type.
- Only native links and forms count. Elements made with HTML boxes or JavaScript are not part of the page structure and are not counted.

[Connecting integrations; Conversion goals]

## 8. Reuse

- **My Blocks**: a block saved to the workspace library is a copy. Instances can be changed independently. Saved blocks can be organized in folders; Fluid Grid ones are tagged.
- **Global Blocks** (plan-dependent): the same block on every page that uses it. "Apply Changes" lists the affected pages with their draft or live status, then updates them all. Applying a change to a Global Block that sits on a live page needs Manager permission; Editors can only change Global Blocks not used on live pages. A given Global Block can appear only once per page (a second copy does not load on the live page). "Disconnect" turns an instance into a normal block.
- **Form Library**, **Popup Library** and global popups (§1).
- Saved blocks, Global Blocks and image libraries belong to one workspace and are not shared with other workspaces.

[Instablocks; Global Blocks; Fluid Grid; Images]

## 9. Publishing, versions and roles

- Publish from the page slideout or the builder, to: a custom domain (CNAME), WordPress (plugin), Drupal, pagedemo.co, or the main domain through a reverse proxy (Convert plan). Pagedemo is for testing: 30 requests per minute per IP, not for ad traffic.
- "Hide page from search engines" is on by default (noindex, nofollow), in the Search & Social tab.
- Publishing and unpublishing can be scheduled. URL masking and iframe publishing are not supported.
- On a published page, the builder's Update button pushes the changes live within minutes.
- Version History (page settings) keeps a version for every save and every switch to the mobile view. A duplicated page does not carry the history.
- Roles: **Viewer** (read only), **Editor** (edits and saves pages, creates pages, forms and image uploads, cannot push anything live, cannot publish or unpublish, start experiments, edit Styles or Fonts, connect new integrations, or apply Global Blocks used on live pages), **Manager** (everything except billing, audit log, global domains, managing other managers and creating workspaces), **Owner**. **Developer Access** lets a member use their own API key, limited to what their role allows.

[Publishing options; Page builder; Page settings; Team member permissions; Developer Access]

## 10. Where custom code can go (every one is an exception)

| Location | Scope | Notes |
|---|---|---|
| HTML element | One element | §2 |
| Inline Style Editor ("Edit CSS") | One element | Any CSS property; shows the element ID; "Reset to Default" removes it |
| Page HTML/CSS and JavaScript panels (builder settings) | One page variation | Header, body or footer; runs only on the live page; mobile CSS needs a max-width 768 px media query |
| Scripts & Privacy (page slideout) | All variations of one page | Meant for tracking scripts; blocked by the cookie bar when enabled |
| Workspace Scripts (Assets > Scripts) | Many pages | Plan-dependent; Owner or Manager; applied to all pages, opt-in per page, or all except opted-out; loads before page scripts |
| Global Block settings | Every page using the block | Can hold fonts and HTML, CSS or JavaScript |

Instapage support troubleshoots only the code shown in its own guides. [Custom HTML, JavaScript and CSS; Inline Style Editor; Workspace Scripts; Global Blocks]

## 11. Consent

- The native cookie bar is switched on per page in Scripts & Privacy, with a link to the privacy terms. It blocks the Marketing Tags & Pixels integrations and the Scripts & Privacy scripts until the visitor accepts. Builder-panel scripts are blocked only when wrapped in Instapage's documented `__gdprComplianceScripts` function.
- The bar is suitable only when data is collected for one processing purpose. With several purposes, separate consent (for example form checkboxes) is needed.
- Google Consent Mode has no native integration.

[Cookie opt-out notification]

## 12. Experiments and personalization

- A/B experiments (plan-dependent) serve variations of one published page at one URL; they are created in the Optimize area and only for published pages. AI Experiments shift traffic toward the better-converting variation (plan-dependent).
- Personalization serves different experiences to different audiences.
- Through the API and MCP, experiments and personalizations can be listed but not started or stopped.

[A/B testing; AI Experiments; MCP guide]

## 13. Export, transfer and import

- Pages move only as `.instapage` files, and only on paid plans. An uploaded page loses most slideout settings (integrations, scripts and privacy, search and social) and its Global Blocks.
- Moving a page to another workspace by download and upload creates a new page without its analytics, leads, integrations or slideout settings. Instapage support can move live pages.
- The API and MCP can export a page as JSON and create a new page from that JSON. The JSON format is not documented.

[Downloading and uploading; Transfer pages; API reference]

## 14. Instapage's own AI

- **Prompt to Page** (beta, rolling out): generates a whole page from a prompt, including layout, copy, colors, fonts and AI images, built on Fluid Grid Blocks; generated images go to an AI-generated folder in the image library.
- **AI Content Generator**, **AI translation** for collections, and **AI Experiments** (§12).

Not used for creative decisions on CreativeEngine work (SKILL.md hard rule 4). [Prompt to Page; AI Content Generator]

## 15. Divergences and unverified items

| Item | Status |
|---|---|
| Form label font size | DIVERGENCE (2026-09-24): the Form Builder article (2026-08-21) says form font size cannot be changed; the limited-release mobile article lists form field label size as a per-device setting. Check in the client's workspace |
| Carousel inside a Fluid Grid Block | UNVERIFIED: not in the Fluid Grid element list; check in the editor |
| Accordion inside a Fluid Grid Block | Recommended by the Accordion article, though missing from the Fluid Grid element list; treat as allowed, confirm in the editor |
| What `page_snapshot_save` and `page_import_json` carry into the new page (integrations, conversion goals, scripts and privacy, SEO, lead notifications, Global Block links) | UNVERIFIED until the first connection (`mcp-and-api.md` §7). The `.instapage` upload loses them (§13); assume the same until tested |
| MCP host support | The help article says the MCP is supported only on Claude; the setup guide also generates configurations for Cursor, ChatGPT and other hosts |
| Page JSON paths for element type, inline CSS and page code | UNVERIFIED; record them at the first connection so QA can check them from a snapshot |

## Continuation recheck (2026-09-24)

- [Mobile guide](https://help.instapage.com/hc/en-us/articles/40608499118743-Optimizing-Your-Page-for-Mobile): shared structural reparenting and device settings are documented; workspace availability still OPEN. Regenerate resets mobile tweaks, so it is not a routine preservation strategy.
- [Custom HTML](https://help.instapage.com/hc/en-us/articles/205221768-Embedding-custom-HTML-or-widgets-into-an-Instapage-landing-page): some preview rendering is possible; native form goals/lead handling do not cover embeds.
- [External tracking](https://help.instapage.com/hc/en-us/articles/205235648-External-Conversion-Tracking): externally embedded forms are explicitly unsupported; do not equate query forwarding with attribution or completion.
- [Third-party tracking](https://help.instapage.com/hc/en-us/articles/15018624912791-Analytics-tracking-with-third-party-providers): placement and consent behavior require checking, particularly script tags in Scripts & Privacy.
- [API Update Page](https://devdocs.instapage.com/#update-page): group assignment, not a design-content replacement API. Export/import supports a new standard page, with schema and carryover tests still required.

## Sources

Instapage Help Center (`help.instapage.com/hc/en-us/articles/…`), read 2026-09-24:

- New page: `205224788-Creating-a-new-page`
- Thor: `4416755260567-Migrating-your-pages-to-the-Thor-Render-engine`
- Block Templates: `23858320466327-Unlock-the-Power-of-Block-Templates`
- Instablocks: `115015974327-What-are-Instablocks-and-how-to-use-them`
- Global Blocks: `360001095648-What-are-Global-Blocks-and-how-to-use-them`
- Fluid Grid: `26977605805463-Fluid-Grid-Blocks`
- Fluid Block Editor: `42107703617303-Fluid-Block-Editor`
- Responsiveness: `4403844787607-Responsiveness-the-mobile-breakpoint-and-the-size-of-the-mobile-canvas`
- Regenerate: `360026363734-When-to-use-the-Regenerate-button-on-mobile`
- Optimizing for mobile: `40608499118743-Optimizing-Your-Page-for-Mobile`
- Hiding elements: `360019248331-Hiding-page-elements-on-desktop-mobile`
- Alignment and grouping: `225568168-Alignment-grouping-and-improved-mobile-responsiveness`
- Page builder: `206027757-Working-with-the-page-builder`
- Page settings: `205224718-Page-settings-the-right-side-menu`
- Text boxes: `206024197-Text-boxes-headlines-and-paragraphs`
- h tags: `30390283805079-Best-practices-for-h-tags`
- Setting the fonts: `206024297-Setting-the-fonts-for-your-page`
- Assets: `16336153331095-Assets`
- Images: `216108928-Images`
- Videos: `206024877-Adding-videos-to-your-page`
- Links: `206024937-Adding-a-link-to-a-page-element`
- Shapes: `360043106393-Shape-elements-rectangles-boxes-circles-lines`
- Timer: `215452798-Adding-a-countdown-timer-to-your-page`
- Accordion: `33397277077271-Accordion`
- Carousel: `18577482154775-Adding-a-Carousel-to-your-page`
- Sticky Bar: `23659391659031-Sticky-Bar`
- Popups: `31423599531543-Popups`
- Add a form: `206828587-How-to-add-a-form-to-your-page`
- Form Builder and Form Library: `24174660478999-The-Form-Builder-and-Form-Library`
- Connecting integrations: `360019927631-Connecting-integrations-to-an-experience`
- Conversion goals: `205232198-Setting-up-conversion-goals`
- Embedding custom HTML: `205221768-Embedding-custom-HTML-or-widgets-into-an-Instapage-landing-page`
- Custom HTML, JavaScript and CSS: `205178068-Using-Custom-HTML-Javascript-and-CSS-on-Your-Page`
- Inline Style Editor: `223730947-Inline-Style-Editor-CSS-Editor-Module`
- Workspace Scripts: `4415768719895-Workspace-Scripts`
- Cookie opt-out notification: `360012794231-Cookie-opt-out-notification`
- Publishing options: `205860007-Publishing-options`
- Team member permissions: `213113877-Team-members-permissions-list`
- Developer Access: `33320794801559-Developer-Access-for-Team-Members`
- A/B testing: `360039136334-How-do-I-run-an-experiment-A-B-testing`
- AI Experiments: `14497156277271-AI-Experiments`
- Downloading and uploading: `206024827-Downloading-and-uploading-your-landing-pages`
- Transfer pages: `30191364274839-Transfer-pages`
- Prompt to Page: `41852387160855-Prompt-to-Page-Generate-a-Landing-Page-with-AI`
- AI Content Generator: `8976748254871-AI-Content-Generator`
- MCP server: `43500205661079-Instapage-Model-Context-Protocol-MCP-Server`

Also: MCP setup guide and tool catalog, `https://mcp.instapage.com/howto`; Public API reference, `https://devdocs.instapage.com/` (changelog to 2026-09-17).
