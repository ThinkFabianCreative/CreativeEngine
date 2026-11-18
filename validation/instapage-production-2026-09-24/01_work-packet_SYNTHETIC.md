# Work Packet: Card sign-up · landing page (SYNTHETIC)

> **Synthetic validation fixture.** Fernwick, the Fernwick Public Library and its Tool Library are fictional. No client, no real facts, no material from any CreativeEngine client. Written in the shape of `shared/frameworks/brief-normalization.md` §15 so the production flow can be tested end to end.

Client:        SYNTHETIC · Fernwick Tool Library (a program of Fernwick Public Library; fictional)
Project:       card-drive (synthetic validation)
From:          synthetic normalized brief, 2026-09-24, APPROVED FOR VALIDATION ONLY
Source scope:  synthetic PROJECT-LEVEL sources only
Problem ID:    LP1
Mode:          JUDGE complete; approved for production (synthetic)

## Source-grounded core

OFFERING:                           Free Tool Library membership (a library card that lends tools)
CHANNEL / PLACEMENT:                Paid social traffic to a landing page (synthetic); placement not relevant to the page
FORMAT(S):                          1 landing page, desktop and mobile, produced in Instapage
OBJECTIVE:                          Grow Tool Library card sign-ups
AUDIENCE:                           "Fernwick residents who own a toolbox but not the tool for the job" (synthetic source wording)
SOURCE PROBLEM / ASSIGNMENT:        "People buy tools they use once, then store them for years." (synthetic)
SOURCE PROPOSITION / POSITIONING:   "Borrow the tool instead of buying it." (synthetic)
RELEVANT PROOF:                     see the claim ledger below
MANDATORIES:                        M1 footer line, exact: "Fernwick Tool Library is a program of Fernwick Public Library." · M2 privacy link, text "Privacy policy", to https://fernwick.example/privacy
PRIMARY GOAL:                       Card requests
CTA WORDING:                        "Get my card" (approved)
DESTINATION / ACTION LOCATION:      Native form on the page; thank-you message, no redirect
MEASURABLE SUCCESS EVENT:           A completed card-request form submission
MEASUREMENT DEFINITION / SOURCE:    Instapage conversion goal "Form submissions" on this page; GA4 through the library's existing property (property ID OPEN, Q3)
OPEN MEASUREMENT QUESTIONS:         Q3
TONE:                               Plain, warm, a little wry. Prohibited: "unlock", "elevate", "empower"

## Form (from the source)

| # | Field | Type | Required |
|---|---|---|---|
| 1 | First name | first name | yes |
| 2 | Email | email | yes |
| 3 | ZIP code | single-line text | yes |
| 4 | "I agree to receive my card confirmation by email." | consent checkbox | yes |

## Proof and claim ledger

| ID | Claim (source wording) | Status | Source | Needed before use | Creative use |
|---|---|---|---|---|---|
| C1 | "More than 900 tools to borrow" | SOURCE-STATED | Catalog count in the synthetic brief; export not reviewed | Reviewed catalog export or library confirmation | May shape work; **confirm before publishing** |
| C2 | "Membership is free for Fernwick residents" | VERIFIED | Synthetic published membership policy, reviewed 2026-09-20 | — | Use as stated |
| C3 | "Tools can be borrowed for up to seven days" | VERIFIED | Synthetic lending policy, reviewed 2026-09-20 | — | Use as stated |
| C4 | "Members are emailed when their card is ready to collect" | VERIFIED | Synthetic process confirmation, 2026-09-20 | — | Use as stated |

## Open issues for this packet

BLOCKERS:              none for building a draft
CLAIM RESTRICTIONS:    C1 cannot go live until VERIFIED
IMPORTANT:             Q1 which email list receives card requests (integration) · Q2 who receives lead notification emails · Q3 GA4 property ID
DO NOT ASSUME:         the CRM, the recipients, or that the catalog count is current
NOT IN THIS PACKET:    ad executions, email follow-ups
