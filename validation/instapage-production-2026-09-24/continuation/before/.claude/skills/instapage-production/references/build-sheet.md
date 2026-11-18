# The build sheet

The build sheet is the production plan: every node of the approved spec mapped to a native Instapage primitive, with the exact approved words, the assets and their status, the form, the reuse class and any code. It is written before anything is built, linted, and then used as the reference side of QA.

It is a translation, not a design document. Every value in it comes from an approved source: the spec (DesignChamp), the copy doc (WordSmither), the packet (BriefMachine), the asset records, the exception register.

File: `work/production/<packet>_instapage-build-sheet_v<NN>.json`. A new version whenever the spec, the copy or the ask changes; earlier versions are kept.

## 1. Format

```json
{
  "format": "instapage-build-sheet/1",
  "meta": {
    "client": "<as in the packet>", "project": "<project>", "packet": "<packet ID>",
    "version": "v01", "date": "YYYY-MM-DD",
    "workspace": { "name": "<Instapage workspace>", "id": "<ID or OPEN>" },
    "spec": { "figma": "<page or frame link>", "version": "<version name or date>" },
    "copy_doc": { "path": "work/copy/<file>", "version": "<v>" }
  },
  "ask": {
    "cta_wording": "<exact, from the packet>",
    "destination": "<from the packet>",
    "success_event": "form_submission | link_click | external_page | OPEN",
    "conversion_goals": ["form_submissions | link_clicks | external_page"]
  },
  "copy": { "<COPY-ID>": "<exact approved text>" },
  "mandatories": ["<COPY-ID>"],
  "styles": {
    "brand_colors": ["#RRGGBB"],
    "fonts": { "headline": "<face>", "paragraph": "<face>", "button": "<face>" }
  },
  "assets": [
    { "id": "IMG-01", "description": "<what it shows>", "status": "PLACEHOLDER | PRODUCTION-APPROVED | PROTOTYPE | EXPLORATION",
      "generated": false, "provenance": "<source>", "rights": "<as recorded>", "approved_by": "<who, date>",
      "alt_copy": "<COPY-ID>", "decorative": false }
  ],
  "blocks": [
    { "id": "B01", "name": "<section>", "type": "fluid_grid | canvas",
      "reuse": "page | my_block | global_block",
      "global": { "name": "GLOBAL · <pattern> · v01", "reason": "", "owner": "", "approved_by": "" },
      "grid": { "columns": 12, "rows": 1 },
      "containers": [ { "id": "B01.C1", "span": "1-7", "mobile_order": 1, "flow": "vertical", "mobile_hidden": false } ],
      "elements": [
        { "id": "E01", "primitive": "headline", "container": "B01.C1", "level": 1, "copy": "<COPY-ID>", "text": "<exact>" },
        { "id": "E02", "primitive": "button", "container": "B01.C1", "copy": "<COPY-ID>", "text": "<exact>",
          "link": { "type": "on_page | outside_url | landing_page | popup | file_download", "target": "<block ID or URL>" } },
        { "id": "E03", "primitive": "image", "container": "B01.C2", "asset": "IMG-01", "visibility": "both | desktop | mobile" }
      ] }
  ],
  "forms": [
    { "id": "F01",
      "packet_fields": [ { "label": "", "type": "", "required": true } ],
      "fields": [ { "label_copy": "<COPY-ID>", "label": "", "type": "", "required": true } ],
      "submit": { "copy": "<COPY-ID>", "text": "<exact>" },
      "after_submit": { "type": "thank_you | redirect | download", "copy": "<COPY-ID>", "text": "<exact>", "target": "" },
      "integration": "<list, or OPEN with Q#>" }
  ],
  "code": [
    { "id": "CODE-01", "location": "scripts_privacy | workspace_scripts | page_js | page_css | inline_css | global_block_settings",
      "kind": "infrastructure | component", "owns_ui": false, "purpose": "", "exception": "EXC-01" }
  ],
  "exceptions": [ { "id": "EXC-01", "class": "INFRASTRUCTURE | COMPONENT", "status": "PROPOSED | APPROVED | REJECTED", "approved_by": "", "summary": "" } ],
  "constraints": [ { "id": "CON-01", "constraint": "", "affects": "", "route_to": "", "material": false, "status": "OPEN | RESOLVED", "resolution": "" } ]
}
```

Primitives: `headline`, `paragraph`, `button`, `image`, `video` (with `host`), `form` (with `form`), `box`, `circle`, `line`, `timer` (with `mode`), `accordion` (with `items`), `carousel`, `html` (with `exception`). IDs in the sheet match the layer names in the Figma spec (`figma-kit.md` §4).

`styles` records the current client's system (Layer 2): its colors and its three faces, from its own approved sources. The global skill supplies no values; the lint checks only the platform limits (at most 14 colors, three font roles). An element may add `"client_component": "<Client> / <Section> / <Variant>"` to record which client component it came from.

## 2. Lint rules

`python3 .claude/skills/instapage-production/scripts/ip_check.py plan <file>` (add `--json` for machine output). A FAIL stops the build; a WARNING is reported to its owner.

| Rule | Checks | Level |
|---|---|---|
| P01 | Format, client, project, packet, version; spec and copy doc versions named | FAIL |
| P02 | Every element uses a primitive from the verified vocabulary | FAIL |
| P03 | Every block is `fluid_grid` or `canvas` | FAIL |
| P04 | No box or circle inside a Fluid Grid Block | FAIL |
| P05 | HTML elements and code need an exception in the register, APPROVED, with an approver, of the right class | FAIL |
| P06 | Code has a known location; infrastructure code does not own UI; code that owns UI and inline CSS need a component exception | FAIL |
| P07 | Accordion sections hold text only | FAIL |
| P08 | Global Blocks have a name, reason, owner and approver, and are not placed twice | FAIL |
| P09 | At most 14 brand colors, as #RRGGBB; only headline, paragraph and button fonts | FAIL / WARNING |
| P10 | Exactly one h1; levels 1–6; warns when a level is skipped | FAIL / WARNING |
| P11 | Every text, accordion section, form label, submit and thank-you message uses an approved copy ID, word for word | FAIL |
| P12 | The packet's CTA wording is used exactly on a button or the submit | FAIL |
| P13 | Every mandatory is in the approved copy and placed on the page | FAIL |
| P14 | Assets exist; no generated, exploration or prototype assets; placeholders warn (they block publishing); production-approved assets have provenance, rights and an approver; images have approved alt text or are marked decorative | FAIL / WARNING |
| P15 | Form fields match the packet in count, order, label, type and required state; the submit text is approved; the after-submit behavior is defined | FAIL |
| P16 | Conversion goals fit the measured event; external goals are not mixed with on-page ones; an OPEN event warns; link clicks alongside submissions warn | FAIL / WARNING |
| P17 | Fluid Grid Blocks have containers with a unique mobile order; elements sit in a container of their block | FAIL |
| P18 | Visibility is both, desktop or mobile | FAIL |
| P19 | Link types are native; on-page targets exist; outside URLs use https | FAIL / WARNING |
| P20 | A material constraint that is still OPEN stops the build; other open constraints warn | FAIL / WARNING |
| P21 | Native video is YouTube, Vimeo or Wistia | FAIL |
| P22 | Native timers count to a fixed date | FAIL |
| P23 | A carousel in a Fluid Grid Block warns (placement unverified) | WARNING |
| P24 | An exception in the register that the plan does not use warns | WARNING |

What the lint cannot see: whether the spec itself is good, whether the page was actually built as planned, and anything in the editor. That is DesignChamp's and CreativeDirector's judgment, and QA's job.
