# wearetraffik.com styles: handoff for Figma

Extracted 2026-11-22 from the homepage. Traffik's own site: client-level candidate, not yet confirmed as the approved brand source.

**Paste into Figma's agent:** "Run Extract Website Styles part 2 with this token list", then the contents of `tokens.json`. Upload everything in `assets/` to the page first.

## Palette
| Variable | Hex | Use |
|---|---|---|
| color/brand/primary | #D91F1F | link hover, arrow links, labels |
| color/brand/black | #000000 | text, backgrounds |
| color/brand/white | #FFFFFF | backgrounds, reversed text |
| color/neutral/50 · 100 · 200 | #FAFAFA · #EEEEEE · #DDDDDD | surfaces, rules |
| color/neutral/700 · 800 | #444444 · #313131 | dark sections |
| semantic (all four) | Not found | |

## Type
| Style | Font | Size / line |
|---|---|---|
| Display | Adobe Caslon Pro 400 | 70 / 84 (inferred) |
| Heading 1–4 | Adobe Caslon Pro 400 | 64/83 · 48/58 (inferred) · 36/43 · 25/30 |
| Body Large · Body · Body Small | Acumin Pro 300 | 20/30 · 16/24 · 12/18 |
| Label · Caption | Acumin Pro Wide 700 | 15/30 +0.9 · 10/11 +0.6 |
| Nav | Acumin Pro Wide 700 | 36/54 |
| Button | Adobe Caslon Pro 400 | 25/44 |

All four families are Adobe Fonts. If Figma can't see them, substitutes: Libre Caslon Text, Inter, Archivo Expanded, Literata.

## Trimmed, inferred, failed
- Case-study colors (teals, golds, blues in cases.css) are client colors, not Traffik's. Left out.
- WordPress preset colors and framework CSS left out. Client logos and award badges not extracted.
- Root font size is 10px, so rem values were converted at 10, not 16.
- No CSS variables, no H5/H6, no semantic colors on the site.
- Nothing failed to download.
