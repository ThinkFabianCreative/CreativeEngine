---
name: instapage-production
description: Build, check and publish an approved landing page natively in Instapage from DesignChamp's approved Figma specification, using native authoring tools inside Instapage. Modes INSPECT, BUILD, UPDATE, QA, PUBLISH, MEASURE. Use when an approved landing-page direction must become a real Instapage page the client can keep editing, or when the user mentions Instapage. Native Authorability is mandatory - native blocks, elements and forms, with explicitly approved integration exceptions. Never rewrites approved copy, never makes creative decisions, never publishes without explicit approval. Prototypes belong to format-prototyping.
---

# Instapage production

## Authoring restriction — user instruction, 2026-09-25

Build and edit pages only with native authoring tools inside Instapage, operated by a person or authorized browser automation. Figma remains the specification. Do not develop pages through external HTML/CSS recreation, generated page JSON, adapter-driven writes, API imports, or snapshot patch/save workflows, even if their outputs contain native elements. Use editor duplication and native blocks/elements for reuse. Read-only exports and offline checks remain evidence tools only. Historical adapter/import descriptions below are reference material, not authorized development routes. Previously approved CRM integration exceptions remain narrowly scoped integrations added through the editor; they do not authorize custom page/component development. Preserve creative ownership, saved editor changes, client isolation and the prohibition on unapproved publishing.

CreativeEngine decides what is made. Figma makes DesignChamp's visual intent explicit. This skill turns the approved work into a native Instapage page that a client-side marketer can keep editing without us. Instapage is where the page is produced and published. It is not where creative decisions are made.

It is platform-specific and client-agnostic: it defines how to build in Instapage, never what a client looks like. Its consistency should show in quality, maintainability and authorability, never in clients looking alike.

This skill is method. DesignChamp owns the visual system and its translation into Instapage. WordSmither owns every word on the page. BriefMachine owns the ask: CTA wording, destination, measured event. CreativeDirector owns creative approval and decides whether a compromise to the selected idea is acceptable. The user or client decides when a page goes live.

## Where it sits

```
APPROVED CREATIVE DIRECTION (creative-engine-director, JUDGE)
        │
DesignChamp + Figma, using the Instapage Native Kit (references/figma-kit.md)
        │
APPROVED SPEC  +  APPROVED COPY (WordSmither)  +  PACKET ASK (BriefMachine)
        │
INSPECT → build sheet → BUILD (native, draft) → QA ─── constraint? → DesignChamp / WordSmither
        │                                               └── material? → creative-engine-director
PUBLISH (separate approval) → MEASURE
```

| `instapage-production` | `format-prototyping` |
|---|---|
| How do we faithfully implement the approved page with Instapage's own authoring tools? | Does the approved idea work convincingly as a landing page? |
| A native, client-editable Instapage page | A prototype in Figma, Webflow or HTML |
| Starts after JUDGE, from an approved spec | Runs in DEVELOP and JUDGE |

A prototype is never promoted into production. The production page is built again, natively, from the approved spec. Code-first web skills (`design-taste-frontend`, `image-to-code`, `redesign-existing-projects`, the `ui-ux-pro-max` stacks) produce what Native Authorability forbids and are not used here.

## Entry gate

Before BUILD, stop and name what is missing, routed to its owner, unless all of these exist:

| Input | Owner | Minimum |
|---|---|---|
| Creative approval for production | CreativeDirector | Verdict (ADVANCE or BET THE PITCH) and an explicit go to production, dated, in `work/reviews/` |
| Work packet with the ask | BriefMachine | Objective, audience, offer and proposition, claims with ledger status, mandatories, exact CTA wording, destination, measured event and its definition. Open items cite their Q# |
| Approved copy | WordSmither | A versioned copy doc in `work/copy/` with every word the page shows: headings, body, buttons, form labels and consent text, thank-you message, alt text, SEO title and description |
| Approved spec | DesignChamp | A Figma spec built with the Instapage Native Kit, desktop and mobile, version named (`references/figma-kit.md` §5) |
| Assets | DesignChamp and the client | Every image with provenance, rights and status (hard rule 5) |
| Workspace | User | The client's Instapage workspace, recorded in `projects/<client>/client/design-library.md` |

Missing packet fields go back to BriefMachine as open questions, never inferred. Missing words go to WordSmither. A spec not built from the kit goes back to DesignChamp.

## Hard rules

1. **Native Authorability.** Ordinary content uses Instapage native blocks, elements, widgets and forms so a competent non-developer can edit it in the editor. An approved CRM embed (including Slate) is a scoped integration exception, with external editing and maintenance ownership; it is never represented as natively editable. No custom HTML, CSS or JavaScript to build, lay out or style user-facing components, and no code whose only purpose is pixel fidelity with Figma. Code is allowed only for infrastructure (analytics, consent, tags, pixels, approved third-party services, integrations with no native route), in the order set in `references/native-authorability.md`, and every exception is recorded there. A page that fails that file's acceptance test is not finished.
2. **Client-agnostic platform, client-specific expression.** Three layers (`references/figma-kit.md` §1): global Instapage-native primitives (this skill and the kit, aesthetically neutral), each client's own design system (that client's Figma library and Instapage blocks, from its approved sources), and each project's composition (the approved spec). The global layer never defines typography, colors, button appearance, spacing preferences, imagery style, art direction or a CreativeEngine landing-page look, and never holds a CreativeEngine-branded component library. A project decision becomes a client standard only through promotion; a client standard never becomes global method. Templates and saved blocks are implementation resources, not creative authorities: production asks "what is the most faithful native build of the approved spec?", never "which existing template or block is closest?".
3. **Approved copy is immutable.** Enter it exactly: words, punctuation, capitals, typographic marks, and line breaks where the spec sets them. Never shorten, improve or rewrite it to fit. Mandatories and CTA wording are exact. If it does not fit, file a constraint report: the verbal problem goes to WordSmither, layout options go to DesignChamp, and CreativeDirector resolves material conflicts.
4. **Production makes no creative decisions.** It does not redesign, simplify, substitute or "improve". When the approved design cannot be built natively, record the exact constraint, name what it affects, list native options without choosing one, return it to DesignChamp, and escalate to `creative-engine-director` if any option would materially change the selected idea, the visual or verbal concept, or its quality. DesignChamp pushes the expressive range of native Instapage before asking for an exception. Instapage's generators (Prompt to Page, AI Content Generator, AI translation) are not used for copy, layout, color, type or imagery on CreativeEngine work.
5. **Only production-approved assets go live.**

   | Asset status | May appear in Instapage | Blocks publishing |
   |---|---|---|
   | EXPLORATION | Never | — |
   | PROTOTYPE / COMP, including all generated media | Never | — |
   | PLACEHOLDER: a flat, labelled box we made | Drafts only | Yes |
   | PRODUCTION-APPROVED: provenance, rights, approver, date, evidence recorded | Drafts and live pages | No |

   Generated media (Artlist, Firefly, image models, Instapage's own AI images) is inspiration and pitch only and never enters an Instapage page (`DesignChamp/skills/artlist-production.md`). Stock and client photography needs recorded rights for this use. A file is not approved because it is in `client/assets/` (`projects/README.md`).
6. **Publishing is a separate, explicit act.** BUILD and UPDATE end in a draft. Nothing goes live because a build succeeded. Publishing needs CreativeDirector's creative approval, a QA result with no blocking issue, and the user's go-ahead naming the page, URL and time (`references/publishing.md`). Changing a live URL, pressing Update on a live page, applying a Global Block or global popup used on live pages, editing workspace scripts, and starting or stopping experiments all count as publishing.
7. **Least privilege, no secrets.** Build with a key from an Instapage Editor who has Developer Access, behind a tool allowlist with no publishing or destructive tools (`references/mcp-and-api.md`). The API key never appears in the repo, a prompt, a file or a message. Leads and team data stay masked; unmask only with the user's consent for a stated purpose, and never store them in the repo.
8. **One client, one workspace, one library.** Confirm the workspace ID against the client's `design-library.md` before any write. Never read, copy, reuse or start from another client's pages, blocks, forms, assets, Figma library, patterns, stakeholder feedback or performance results; a cross-client comparison happens only when the user asks for one, as a separate task. A client's block library lives in that client's workspace, and nothing learned from one client's pages becomes global knowledge.
9. **Verified platform facts only.** Capabilities come from `references/platform.md` (verified 2026-09-24) or the live MCP catalog, never memory. If the editor behaves differently, trust the editor, record the divergence in `platform.md` §15 with its date, and treat the older fact as stale.

## Modes

Operational modes of one skill. EXPLORE, DEVELOP and JUDGE remain CreativeEngine's operating modes. This skill starts after JUDGE; only its translatability check reaches back into DEVELOP (`references/figma-kit.md` §3).

| Mode | Does | Instapage access | Output | Needs |
|---|---|---|---|---|
| **INSPECT** | Confirms the workspace; reads pages, blocks, forms, domains, structure and plan features | READ profile | Inspection note | — |
| **BUILD** | Turns the approved spec into a build sheet, lints it, builds the page natively as a draft | BUILD profile and the editor | Build sheet, draft page, build report | Entry gate |
| **UPDATE** | Changes a page to a newly approved spec or copy version: in place in the editor (keeps URL, analytics, integrations, experiments), or as a new page from a patched copy | BUILD profile and the editor | Updated build sheet, draft, report | Entry gate; a live page also needs PUBLISH |
| **QA** | Compares packet, copy, spec and the actual page | READ profile, browser, a staging URL | QA JSON and report | A staging publish needs the user's OK |
| **PUBLISH** | Makes a page, or a change to a live page, live | A Manager in the Instapage UI, or the PUBLISH profile | Publish record | Creative approval, clear QA and the user's go-ahead, every time |
| **MEASURE** | Reads aggregate performance against the packet's measured event | READ profile | Results note | Unmasking leads needs consent |

## Procedure

**0. Check the connection.** Discover available Instapage tools. If none load, continue independent specification, documentation and local validation work; request an authenticated editor or connector and the designated workspace for platform tests. Do not request an API key in chat. Connection guidance: `references/mcp-and-api.md` §3. Never ask for the key. Run `session_info` and `workspaces_list`, and confirm the client's workspace. On the first connection, run the checklist in `references/mcp-and-api.md` §7.

**1. INSPECT.** Read what exists: saved and global blocks, forms, domains, published pages, and any page being updated (`page_export_json`, then `page_snapshot_read`). Check the plan features the spec relies on (Global Blocks, workspace scripts, custom fonts, experiments). Anything the spec needs that the workspace lacks is a constraint.

**2. Write the build sheet.** Map every node of the approved spec to a native primitive, block, container, copy ID, asset ID, link and reuse class (`references/build-sheet.md`, `references/figma-kit.md` §4, `references/reusable-blocks.md`, `references/forms-and-tracking.md`). Save it as `work/production/<packet>_instapage-build-sheet_v<NN>.json` and lint it:

```
python3 .claude/skills/instapage-production/scripts/ip_check.py plan <build-sheet.json>
```

Fix a FAIL in the sheet, or turn it into a constraint report. Never clear a FAIL by editing approved copy or the spec.

**3. BUILD natively, as a draft.** Choose the route by what exists:

| Route | When | How |
|---|---|---|
| **A. Duplicate in the editor** | An approved native source exists in this client workspace | Duplicate using Instapage’s editor controls, retain the predecessor, then edit with native authoring tools and verify inherited settings |
| **B. Editor build** | New structure | A production designer builds it in the Instapage editor from the build sheet: Fluid Grid Blocks, native elements, Form Library forms, My Blocks |
| **C. Editor build with Claude in the browser** | New structure, and editor operation is within the authorized task | The user signs in themselves. Claude works in the built-in browser, saves drafts only, never enters credentials, and never presses Publish or Update on a live page |

Use Instapage’s native asset controls and authoring tools for the draft. Retain historical generators/exports as evidence only; do not execute them to build or update pages. Write the build report.

**4. QA.** Run every check in `references/qa.md` the unpublished page allows. Some embeds can render in preview; native form submissions and other runtime behaviors may need a published environment. Record unavailable tests as NOT_RUN with the limitation and remaining test. Do not publish solely to obtain a pass. Any separately requested staging publication follows `references/publishing.md`. Write `work/production/<packet>_instapage-qa_v<NN>.json` and its `.md` report, then validate:

```
python3 .claude/skills/instapage-production/scripts/ip_check.py qa <qa-result.json>
```

**5. Constraint reports** go to their owners when they appear, not at the end.

**6. PUBLISH** only through `references/publishing.md`: the three approvals, the executor, the publish record, the live smoke test.

**7. MEASURE** with `analytics_get` and `experiments_list`, read against the packet's measured event and the conversion goals actually configured (`references/forms-and-tracking.md` §4). Results go in the project's `results/` with the metric definition, date range, page ID and version. They reach client knowledge only through promotion (`projects/README.md`) and never reach another client.

## Constraint report

```
CONSTRAINT:     <the platform limit, citing references/platform.md or the observed editor behavior>
AFFECTS:        <block / element / copy ID / asset ID>
SPEC SAYS:      <what the approved spec or copy requires>
NATIVE OPTIONS: <each native way to build it; no choice made>
EXCEPTION?:     <an infrastructure exception, or a component exception proposed for CreativeDirector; or none>
ROUTE TO:       DesignChamp | WordSmither | BriefMachine | creative-engine-director
MATERIAL?:      <would any option change the selected idea, the visual or verbal concept, or its quality? YES → creative-engine-director>
STATUS:         OPEN | RESOLVED · <who, date, decision>
```

Keep reports in the build sheet's `constraints` list. Production waits for the decision; it does not pick an option to keep moving.

## Build report

```
INSTAPAGE BUILD · <client> · <project> · <packet> · <date>
PAGE:          <workspace> · <page name> · <page ID> · DRAFT
FROM:          spec <Figma link, version> · copy <path, version> · build sheet <path>
ROUTE:         A copy / B editor / C editor with Claude
BUILT:         <blocks, forms, saved or global blocks used>
CONSTRAINTS:   <IDs and status>
EXCEPTIONS:    <EXC IDs and status, or none>
PLACEHOLDERS:  <asset IDs still placeholders, or none>
NEXT:          QA · or waiting on <owner>
```

## Where files go

```
projects/<client>/client/design-library.md                  workspace record and block inventory
projects/<client>/<project>/work/production/                build sheets, exceptions, QA results and reports
projects/<client>/<project>/outputs/delivered/YYYY-MM-DD/   publish records
projects/<client>/<project>/results/                        measurement notes
```

## References

| Topic | File |
|---|---|
| Platform documentation, limits and divergences | `references/platform.md` |
| Per-feature capability and validation status | `references/capability-map.md` |
| Native adapters, editor-edit preservation and release evidence | `references/preservation.md` |
| Native Authorability: the rule, exceptions, acceptance test | `references/native-authorability.md` |
| Figma Native Kit and the Figma-to-Instapage mapping | `references/figma-kit.md` |
| Build sheet format and lint rules | `references/build-sheet.md` |
| Responsive behavior and the mobile specification | `references/responsive.md` |
| Reusable blocks: My Blocks and Global Blocks | `references/reusable-blocks.md` |
| Forms, integrations, conversion goals, tracking | `references/forms-and-tracking.md` |
| MCP and API: setup, profiles, tools, first connection | `references/mcp-and-api.md` |
| Publishing boundary, approvals and records | `references/publishing.md` |
| QA checks and the machine-readable result | `references/qa.md` |

## What this skill does not do

- Create or choose the concept, copy, layout, type, color or imagery.
- Prototype. That is `format-prototyping`.
- Recreate ordinary native content in custom code. Approved integration exceptions are covered by `references/native-authorability.md`.
- Publish, unpublish, delete pages or change team access on its own authority.
- Promote project results into client knowledge, or client patterns into global knowledge.
