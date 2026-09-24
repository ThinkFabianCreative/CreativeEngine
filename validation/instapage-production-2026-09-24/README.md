# Validation · instapage-production · 2026-09-24

A synthetic end-to-end run of the `instapage-production` skill, from approved inputs to a lint-clean build plan and a validated QA result. **Everything here is fictional** ("Fernwick Tool Library"). It uses no client's facts, assets, blocks or Figma libraries.

**What is not validated:** anything inside Instapage. The Instapage MCP was not connected in this session, so no page was built, inspected, QA'd or published. The stages that need Instapage are recorded as NOT_RUN, with the next action below.

## The flow, step by step

| # | Step | Artifact | Result |
|---|---|---|---|
| 1 | Approved work-packet inputs (BriefMachine) | `01_work-packet_SYNTHETIC.md` | Ask separated: CTA wording, destination, measured event, measurement; claim ledger C1–C4 |
| 2 | Approved copy (WordSmither) | `02_approved-copy_SYNTHETIC.md` | 26 copy IDs, every visible string |
| 3 | Approved visual direction (DesignChamp) | `03_visual-direction_SYNTHETIC.md` | Concept; Layer 2 client system; Layer 3 composition; range test |
| 4 | Figma-native spec | `04_figma-spec.md` and the kit's Validation page | Desktop 1440 and Mobile 400 from Layer 1 instances, about 40 annotations |
| 5 | Mapping into native Instapage | `04_figma-spec.md` § Mapping; `LP1_instapage-build-sheet_v01.json` | 5 Fluid Grid blocks, 19 elements, 1 Form Library form |
| 6 | Reuse decisions | `04_figma-spec.md` § Reuse | 2 My Blocks, 1 Global Block with reason, owner, approver; nothing global "because reusable" |
| 7 | Native-authorability QA | `LP1_instapage-qa_v01.json` / `.md` | PLAN stage: 14 PASS, 2 FAIL, 30 NOT_RUN, publish allowed NO |
| 8 | What needs human or CreativeDirector approval | `05_approvals-and-client-editing.md` | Material proof-line change and creative approval to CD; craft constraints to DesignChamp; publishing to the user and a Manager |
| 9 | What the client can edit afterwards | `05_approvals-and-client-editing.md` | Text, buttons, images, sections, form, My Blocks; the Global Block with a warning; no developer needed |

## Checks actually run

```
$ python3 .claude/skills/instapage-production/scripts/ip_check.py plan LP1_instapage-build-sheet_v01.json
WARNING P14  assets.IMG-01: placeholder: allowed in drafts, blocks publishing
WARNING P25  B03.E13: claim C1 is SOURCE-STATED: confirm before publishing; blocks publishing until VERIFIED
WARNING P20  CON-03: constraint OPEN with DesignChamp
PLAN: 0 FAIL · 3 WARNING · build may proceed

$ python3 .claude/skills/instapage-production/scripts/ip_check.py qa LP1_instapage-qa_v01.json
QA: 14 PASS · 2 FAIL · 0 WARNING · 30 NOT_RUN · blocking 31 · approvals incomplete · publish allowed: NO
RESULT FILE: valid
```

Negative controls (copies of the sheet in a scratch folder, not kept):

| Change | Lint result |
|---|---|
| Production "tidied" the headline by dropping its full stop | `FAIL P11 B01.E01: text differs from approved copy HERO-H` |
| An FAQ added as an HTML element | `FAIL P05 B02.E30: needs an approved exception (EXC ID)` |
| A box shape dropped into the hero's Fluid Grid block | `FAIL P04 B01.E31: shapes cannot go in a Fluid Grid Block…` |

The skill's unit tests passed at the end of this run (`python3 -m unittest discover -s .claude/skills/instapage-production/scripts/tests`).

## Constraints the run surfaced

Three constraints, all routed to DesignChamp, none material:

- **CON-01:** rotation is not a documented native control.
- **CON-02:** the stamp was drawn as a bordered frame nested inside a container. Containers cannot nest and text has no native border.
- **CON-03:** per-device headline size depends on a limited-release setting.

CON-02 is the kind of error the method exists to catch. It was found in the spec during this run, and the Figma spec was changed to the native option: the stamp became its own bordered container.

## Next action once Instapage is connected

1. The user connects the Instapage MCP with an Editor + Developer Access key, using the BUILD allowlist (`references/mcp-and-api.md` §3–4), and names a **test workspace** that belongs to no client.
2. Run the first-connection checklist (`mcp-and-api.md` §7) there.
3. Build this page as route B or C in the test workspace, re-run QA at DRAFT, record the JSON paths and what a snapshot copy carries, and update `references/platform.md` §15.
4. Do not publish anything. A staging publish, if wanted, is a separate request.
