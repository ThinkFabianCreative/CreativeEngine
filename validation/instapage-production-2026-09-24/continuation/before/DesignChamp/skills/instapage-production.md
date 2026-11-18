# instapage-production

| | |
|---|---|
| Source | CreativeEngine (in-house), for Instapage's official MCP server and Public API |
| Owner | DesignChamp (turning an approved landing-page spec into a native Instapage page). WordSmither owns every word on the page; BriefMachine supplies the ask; CreativeDirector approves creative compromises and the work before it goes live; the user or client decides when it goes live |
| Status | Built at the user's request 2026-09-24. **Instapage MCP not yet connected** (no Instapage tools in the session); first-connection checklist pending (`references/mcp-and-api.md` §7). Figma Native Kit built the same day |
| Installed | `.claude/skills/instapage-production/`: `SKILL.md`; `references/` (platform, native-authorability, figma-kit, build-sheet, responsive, reusable-blocks, forms-and-tracking, mcp-and-api, publishing, qa); `scripts/ip_check.py` with `scripts/tests/` |
| Figma kit | "CreativeEngine · Instapage Native Kit", `https://www.figma.com/design/suQoQdAczG3IZRVMxooqpb` (TRAFFIK team drafts; Layer 1 only; not yet published as a team library) |
| Scope | Native Instapage production of single marketing landing pages from an approved spec: INSPECT, BUILD, UPDATE, QA, PUBLISH, MEASURE. Not prototyping (`format-prototyping`), not creative development, not a design system |

## Principles set by the user (2026-09-24)

- **Native Authorability.** A production page stays editable in Instapage by a competent non-developer. User-facing structure uses native blocks, elements, widgets and forms; code only for infrastructure, in a fixed preference order, every exception recorded.
- **Client-agnostic platform, client-specific expression.** The skill and kit define how to build in Instapage, never what a client looks like. Three layers: neutral native primitives (global), each client's own design system (client-scoped), each project's composition. No CreativeEngine-branded components or house look; a client pattern never becomes global; templates and blocks are implementation resources, never creative authorities.
- **Publishing is separate and explicit.** Nothing goes live because a build succeeded.

## Review (2026-09-24)

- **Executables.** `scripts/ip_check.py` is standard-library Python: it reads local JSON, prints to stdout, makes no network calls and touches no credentials. 36 unit tests, including two that fail if the references and the checker drift apart. Everything else is Markdown.
- **Connector.** Instapage's hosted MCP (`https://mcp.instapage.com`; help article of 2026-09-17; setup guide and 39-tool catalog at `mcp.instapage.com/howto`). Authentication is a personal API key sent as a bearer header; the key has no scopes and carries its creator's full permissions. Client-side headers limit which tools the model sees. Instapage says the server does not store the key.
- **Least privilege.** Two layers. Server side: the key comes from a dedicated **Editor** with Developer Access, which Instapage prevents from publishing, unpublishing, starting experiments or applying Global Blocks on live pages. Client side: exact tool allowlists (READ, BUILD) with no publishing, deleting or team tools. PUBLISH is a separate Manager-level profile, off by default; the default is a Manager publishing in the Instapage UI.
- **Credentials.** The key lives in the macOS Keychain and reaches Claude Code through a `headersHelper` script outside the repo. It never enters the repo, `.mcp.json`, a prompt or a message. Instapage's Claude Desktop config (via `npx mcp-remote`) is documented but not preferred, because it keeps the key in a plain file.
- **Data.** Page JSON snapshots, images by HTTPS URL, aggregate analytics. Leads and team data are masked by default; unmasking only with the user's consent, never stored in the repo.
- **Destructive operations.** `page_delete`, folder and collection-page deletion, submission deletion and team changes are in no profile. Collection-page and submission deletion have no undo.
- **What the MCP cannot do.** It cannot compose a page: no tools for blocks, elements, forms, integrations, conversion goals, scripts or saved blocks, and no in-place edits (a patched snapshot is saved as a new page). The page JSON format is undocumented. So structure is authored natively in the editor, or copied from a native page, and never synthesized as JSON.
- **Overlap.** `format-prototyping` proves an idea as a prototype, this skill produces it natively; a prototype is never promoted. Code-first web skills (`design-taste-frontend`, `image-to-code`, `redesign-existing-projects`, `ui-ux-pro-max` stacks) produce what Native Authorability forbids and are not used for Instapage production. Instapage's own AI (Prompt to Page, AI Content Generator, AI translation) is not used for creative decisions. The Figma plugin skills do the Figma operations; the kit supplies the mapping.
- **Assets.** Generated media stays inspiration and pitch only (`artlist-production.md`) and never enters an Instapage page. Placeholders are allowed in drafts and block publishing.
- **Isolation.** One key and one workspace per client where the agency spans several client accounts; saved blocks and images are per workspace in Instapage. Client libraries in Figma and Instapage stay with their client; nothing is borrowed across clients.
- **Unverified until first connection.** What a snapshot copy carries into a new page (integrations, conversion goals, scripts, search settings, Global Block links); the JSON paths QA reads; which write tools accept `dryRun`. Recorded as open in `references/platform.md` §15 and `references/mcp-and-api.md` §7.

## Use

- **DesignChamp:** in DEVELOP and JUDGE, checks serious directions against the kit (warnings, never kills); builds the client's Layer 2 library from its approved sources; delivers the approved spec with annotations; owns the build sheet, BUILD, QA of creative fidelity and native authorability, and constraint decisions that are not material.
- **WordSmither:** supplies every word, including form labels, consent, thank-you, alt text and search copy; receives copy-fit constraints; production never rewrites.
- **BriefMachine:** supplies the ask (objective, audience, offer, claims and status, mandatories, CTA wording, destination, measured event and measurement definition) and resolves form-field and measurement mismatches.
- **CreativeDirector:** approves the spec for production, decides material compromises and component exceptions, and gives creative approval before any publish.
- **Any role, any session:** this record governs Instapage work on CreativeEngine (root `CLAUDE.md`).
