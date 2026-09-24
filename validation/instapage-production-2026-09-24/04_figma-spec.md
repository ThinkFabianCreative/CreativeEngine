# Figma spec and native mapping · LP1 (SYNTHETIC)

Kit file: `https://www.figma.com/design/suQoQdAczG3IZRVMxooqpb`, page **Validation (SYNTHETIC)**.

| Frame | Node | Link |
|---|---|---|
| Range test (three synthetic clients) | `16:2` | `…/suQoQdAczG3IZRVMxooqpb?node-id=16-2` |
| Fernwick · Layer 2 client system | `18:19` | `…?node-id=18-19` |
| SPEC · Desktop 1440 | `18:39` | `…?node-id=18-39` |
| SPEC · Mobile 400 | `19:52` | `…?node-id=19-52` |

Spec version v01, 2026-09-24. Built with Layer 1 instances restyled by the Fernwick layer; about 40 Figma annotations under the IP · Build, Copy, Asset, Reuse and Exception categories.

## Structure (desktop; mobile has the same IDs)

```
Desktop · 1440
├─ B01 · Hero · Fluid Grid  (12 × 3)                      IP · Reuse: My Block · Fernwick / Hero / Split · v01
│   ├─ B01.C1 · m1        cols 1–7, row 1   E01 Headline h1 [HERO-H] · E02 Paragraph [HERO-SUB]
│   ├─ B01.C2 · m4        cols 8–12, rows 1–3   E05 Image [IMG-01 · PLACEHOLDER · alt ALT-HERO]
│   ├─ B01.C3 · m2        cols 1–3, row 2   container border 2px stamp red · E03 Paragraph [STAMP]
│   └─ B01.C4 · m3        cols 1–7, row 3   E04 Button [CTA] → on-page B04
├─ B02 · How it works · Fluid Grid (12 × 2)               IP · Reuse: Page-local
│   ├─ B02.C1 · m1  cols 1–12   E06 Headline h2 [HOW-H]
│   ├─ B02.C2 · m2  cols 1–4    E07 h3 [STEP1-H] · E08 Paragraph [STEP1-P]
│   ├─ B02.C3 · m3  cols 5–8    E09 h3 [STEP2-H] · E10 Paragraph [STEP2-P]
│   └─ B02.C4 · m4  cols 9–12   E11 h3 [STEP3-H] · E12 Paragraph [STEP3-P]
├─ B03 · Proof · Fluid Grid (12 × 1)                      IP · Reuse: Page-local
│   └─ B03.C1 · m1  cols 1–9    E13 h2 [PROOF-H · claim C1 SOURCE-STATED] · E14 Paragraph [PROOF-P]
├─ B04 · Form · Fluid Grid (12 × 1)                       IP · Reuse: My Block · Fernwick / Form / Card signup · v01
│   ├─ B04.C1 · m1  cols 1–5    E15 h2 [FORM-H] · E16 Paragraph [FORM-P]
│   └─ B04.C2 · m2  cols 6–12   E17 Form F01: First name · Email · ZIP code · consent · submit [CTA]
└─ B05 · Footer · Fluid Grid (12 × 1)                     IP · Reuse: Global Block · GLOBAL · Fernwick / Footer / Legal · v01
    └─ B05.C1 · m1  cols 1–12   E18 Paragraph [FOOT] · E19 Paragraph with text link [FOOT-LINK]
```

## Mapping into native Instapage

| Spec | Native Instapage build |
|---|---|
| B01–B05 grid frames | Five Fluid Grid Blocks, custom grids in the Fluid Block Editor (12 columns; B01 with 3 rows, B02 with 2) |
| Containers `B##.C# · m#` | Fluid Grid containers with the spans shown; vertical element flow; mobile stacking set to the `m#` numbers (B01 reordered on mobile: C1, C3, C4, C2) |
| Stamp container border | Container border setting (2 px, stamp red), container padding |
| Headlines | Headline elements, tags h1 (once), h2, h3 |
| Paragraphs | Paragraph elements; the footer link is a text link (outside URL, new tab) |
| Button E04 | Button element, link setup: on-page link to B04 |
| Image E05 | Image element; placeholder in the draft; replaced by the approved photo before publishing; alt text ALT-HERO on the placed image |
| Form E17 | Form Library form F01: predefined First name and Email, a single-line text for ZIP code, a GDPR/terms checkbox for consent, all required; submit text CTA with aria-label F-ARIA; after submit: thank-you message TY, no redirect |
| Page settings | Default fonts: Fraunces (headline), Work Sans (paragraph), Courier Prime (button); Styles palette of 5; cookie bar on; GA4 through Marketing Tags & Pixels (native integration, property ID OPEN); conversion goal "Form submissions" only; search title SEO-TITLE, description SEO-DESC, indexing off (default) |

## Reuse decisions

| Block | Class | Why |
|---|---|---|
| B01 Hero | My Block `Fernwick / Hero / Split · v01` | The split hero recurs on Fernwick pages but each page adapts its words and photo: an independent copy |
| B02 How it works | Page-local | Specific to this page's offer |
| B03 Proof | Page-local | Carries a claim that is specific to this page and still unverified |
| B04 Form | My Block `Fernwick / Form / Card signup · v01` | Reused for card drives; each page may adjust copy |
| B05 Footer | Global Block `GLOBAL · Fernwick / Footer / Legal · v01` | One source of truth for a mandatory legal line; owner: Fernwick communications office; approved by the library (synthetic). Editing it changes every page that uses it, live ones included |

Nothing was made global because it is reusable. Nothing reuses another client's blocks: there is no other client in this fixture.

## Constraints raised during DEVELOP and production planning

| ID | Constraint | Native options | Route | Material? | Status |
|---|---|---|---|---|---|
| CON-01 | The direction rotated the stamp. Rotation is not a documented native control; the only known route is inline CSS, a component exception | Unrotated stamp in a bordered container · stamp as a text-free graphic (rejected: the words would sit in an image) | DesignChamp | No | RESOLVED: unrotated (DesignChamp, synthetic) |
| CON-02 | The stamp was drawn as a bordered frame nested inside the text container. Instapage containers cannot nest, text has no native border, and shapes are not allowed in Fluid Grid blocks | Stamp as its own container with a native border (restructures the hero grid) · hero as a Canvas block with a Box behind the stamp · stamp as red text without a border | DesignChamp | No | RESOLVED: own container (DesignChamp, synthetic); the spec was updated |
| CON-03 | Headline 72 px desktop and 40 px mobile needs per-device font size, a limited-release setting | Confirm the setting in the workspace at INSPECT · one size for both devices · desktop-only and mobile-only headline copies with identical text (native, but two elements to edit) | DesignChamp | No | OPEN until INSPECT |
