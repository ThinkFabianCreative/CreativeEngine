# Mobile Material 3 Expressive — molecule audit

Date: 2026-10-17. Figma file MFK-Andres, frame 39:136. Audit and repairs apply to Figma only.

## Evidence and measurement

Fresh full-page capture plus normal-size story/filter, program-list and newsletter captures. After captures are 01–03-after.png. The before full view is 00-before-full.png.

Inspected 89 visible text nodes, including their styled runs, resolving bound color variables against ancestor solid fills. Four text nodes failed initially: William, Willow and Jeremiah story titles plus Jeremiah's caption were white on cream (1.08:1). Changed these to on-canvas navy (13.60:1). After repair, no measured text failures; minimum measured ratio 5.55:1. Donate, Sign up and selected All label: 6.85:1. Video and Read labels: 7.16:1.

These are solid-fill text measurements, not a complete accessibility certification. The calculation does not establish contrast over arbitrary images, gradients, raster logo lettering, all opacity combinations or all interactive states. Story labels in this layout are outside images. Focus, keyboard interaction, zoom, screen readers, form validation and real scrolling require implementation testing.

## Molecule review

| # | Molecule | Finding and disposition | Health / remaining work |
|---|---|---|---|
| 1 | Header, logo, menu, Donate | Donate label passes 6.85:1. Kept header and filled CTA flat; they are not overlays in this drawing. | Default visual state sound. Verify menu accessible name, opening state and sticky behavior in code. |
| 2 | Hero photograph, display headline and body | Text sits on navy rather than directly on the photo. Reset excessive inherited negative letter spacing; preserved Outfit/Caveat. | Default contrast passes. Test headline reflow at other phone widths. |
| 3 | Connected story filter group | Selected magenta All has white text; sky Video/Read have navy. Text passes 6.85:1 / 7.16:1. Kept shadow-free. | Selected/unselected are visibly different. Focus, pressed states, selection semantics and actual filtering untested. |
| 4 | Story rail, image, title and metadata | Four white-on-cream failures repaired to navy. Visible next-card edge conveys horizontal continuation. | Default contrast repaired. Add a non-drag browsing alternative and test focus moving to offscreen cards in implementation. |
| 5 | Family quote | Yellow/navy panel remains flat to distinguish content from clickable cards. | Contrast passes. No raised-card affordance added. |
| 6 | Rent/bills statistic and expressive headline | Navy on yellow passes. Removed aggressive negative tracking from the mixed-font headline. | Default sound; claim verification remains project work. |
| 7 | Five program rows | Imported Material list content had insufficient hierarchy: title and description both regular. Added shared Outfit SemiBold 18/24 title style; supporting copy remains 16px. Added shared subtle elevation 1 treatment. | Default hierarchy improved. Whole-row links, focus states and destinations require code testing. |
| 8 | Hospital logo wall and accreditation text | White logo panel on magenta already separates clearly by tone. Kept elevation 0; no decorative shadow. All editable surrounding text passes. | Raster logos inspected visually, not included in text contrast calculation. Bracketed accreditation claims remain unverified. |
| 9 | Inset waitlist and Donate | Navy panel on cream and magenta button already establish hierarchy. Kept the panel flat. | Default contrast passes. Donation interaction remains untested. |
| 10 | Three involvement rows | Applied the same shared low elevation as program rows. No individual ad-hoc shadows. | Consistent clickable-card treatment. Verify whole-row links in code. |
| 11 | Two event listings | Applied the same low elevation to the compact yellow event cards. Text remains navy. | Default contrast passes. Confirm event dates and link behavior. |
| 12 | Closing donation and newsletter form | Corrected cramped headline tracking; natural wrap now separates “today.” Added 1.5px navy inside stroke to the cream input on yellow. Kept filled buttons flat and readable. | Default form boundary improved. Error, success, focus, disabled and loading states still need design/implementation. |
| 13 | Footer disclosures and contact/legal copy | Flat navy footer; text passes. Collapsed navigation headers remain design states only. | Expansion, focus, expanded indicators and keyboard behavior untested. |

## Elevation system applied

- Elevation 0: page sections, header, quote, logo wall, waitlist panel and filled buttons. Separation comes from surface tone and spacing.
- Elevation 1: ten actionable cards (five programs, three involvement rows, two events). Shared Figma effect style: `MFK / M3E / Elevation 1 / actionable cards`.
- Shadow recipe: navy at 10%, offset 0/2, blur 4; second navy shadow at 7%, offset 0/1, blur 2. This is a project adaptation, not a claim of exact official Material elevation-token values.
- No floating dialog/menu state is shown, so no high-elevation shadow was added to ordinary page content.

No unexpected horizontal overflow was found; offscreen story cards are intentional inside the clipped rail. No live website code was changed by this audit.

Reference: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
