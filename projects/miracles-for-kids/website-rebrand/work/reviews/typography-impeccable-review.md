# MFK typography review · 18 October 2026

## Recommendation
Use Filson Soft as the primary family for the upscale Montessori / Swiss geometry direction. Use Regular 400 for paragraphs and Bold 700 for headings and controls. Anago remains a credible alternative if compact reading and a less overtly rounded character take priority.

The brand should feel hopeful through confident color, family photography, generous space, and purposeful geometric shapes. Keep the language adult and respectful: the Montessori reference informs the visual atmosphere, not the charity’s positioning.

## Assessment
| Family | Role fit | Decision |
| --- | --- | --- |
| Filson Soft | Rounded geometric forms, generous counters, clear friendly rhythm; broad letterforms need more room | First choice for the requested direction; avoid overcrowding cards |
| Anago | Narrower and more human in rhythm; current heading/body pairing works, but feels less like geometric building blocks | Strong runner-up |
| Playpen Sans | Human, informal, intentionally irregular | Reserve for a short family quotation or child’s contribution; remove from the main hero sentence in a future implementation |
| Bogart | Strong editorial, retro storybook personality | Good alternate creative direction, less aligned with the requested Swiss structure |

## Gaps in the current page
- Hero switches weight and family inside one sentence, giving handwriting disproportionate emphasis. A consistent sans headline would provide a calmer anchor for saturated surfaces and organic shapes.
- Some styles request 600, but the supplied Adobe kit provides 400 and 700 for these families. The browser selects a supplied face rather than a distinct Medium face. Use the actual supplied weights deliberately.
- Typography should not compete with expressive card silhouettes, program colors, and decorative shapes. Establish a consistent type role hierarchy across sections.

## Proposed roles
- Display: Filson Soft Bold, 52–60px desktop, 36–40px mobile, 1.08–1.15 line height. Review wrapping against the actual hero layout.
- Section heading: Bold, 32–40px desktop, 28–32px mobile, 1.15–1.2 line height.
- Card title: Bold, 22–26px, 1.2–1.3 line height.
- Reading: Regular, 17–18px, 1.5–1.6 line height; aim for 45–70 characters on roomy text columns.
- Buttons: Bold, 16px, at least 48px control height.
- Keep text charcoal or white. Maintain the restored saturated Material 3 Expressive surfaces. White on magenta; charcoal on yellow, sky, teal, orange, and green.
- Avoid adding letter spacing to paragraphs or rounded display type. Labels may use modest tracking.

## Evidence and limits
Read official Impeccable typography, craft, and critique guidance from pbakaus/impeccable revision 0665bd812ae0908fcab17b96fd4f840defb882d9. The skill is not installed locally; its context and detect launchers were unavailable. This is a manual typography review, not a successful automated Impeccable scan.

Reviewed the current Anago landing page and a separate comparison using the actual Adobe kit https://use.typekit.net/scu3oyi.css. Kit includes Anago, Filson Pro, Filson Soft, Playpen Sans, and Bogart; 400 / 700 faces checked in the fetched stylesheet. Filson Pro was considered as a more restrained geometric alternative, but Filson Soft better matches the requested warmth.

Comparison: ../prototype/typography-review.html. Visually checked desktop and 390px mobile rendering; no horizontal overflow observed in the comparison. Screenshot: taste-reference-audit/06-font-comparison.jpg. Not a full accessibility certification or user research result.

The main landing page remains unchanged by this typography study.

## Installed-skill reassessment · supersedes the initial recommendation

Impeccable 4.6.0 context and typography detector now ran successfully. An independent typography assessment challenged using Filson Soft for all reading: broad rounded forms fit the display brief, but can overstate childcare associations and increase mobile stacking. Refined recommendation: Filson Soft 700 for headlines and card titles; Anago 400 for paragraphs and 700 for controls. Playpen is optional for a rare personal quotation. Bogart is outside the primary direction.

Updated the comparison with equal physical headline measures (430px maximum), balanced headings, pretty paragraphs, and a combined-family specimen containing the existing long event title and bill-pay copy. The earlier 12ch measure gave different physical widths for each family; conclusions from its wrapping were insufficiently controlled.

Baseline scan found two redundant section kickers in the main prototype and Arial framing in the review page. Review framing now uses Anago. Main-page kicker findings are documented, not silently removed during a font study. The comparison’s final type detector output is stored alongside this review. No clean scan should be read as proof of full accessibility or font-load performance. Existing Google/Adobe duplicate families and unsupported weight requests remain implementation cleanup for the landing page.

Screenshot: taste-reference-audit/07-impeccable-pairing.jpg. Main landing page unchanged.
