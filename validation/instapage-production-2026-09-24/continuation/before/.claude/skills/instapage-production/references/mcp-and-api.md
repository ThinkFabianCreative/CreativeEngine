# Instapage MCP and API

Facts from Instapage's MCP help article (2026-09-17), the MCP setup guide and tool catalog at `mcp.instapage.com/howto`, and the Public API reference (changelog to 2026-09-17), all read 2026-09-24. The Claude Code configuration notes come from Claude Code's MCP documentation, read the same day.

## 1. What the official MCP is

- A hosted, remote MCP server at `https://mcp.instapage.com`. Instapage says it is built for, and supported on, Claude.
- It forwards a **personal Instapage API key** to the Public API on every request and does not store it.
- **The key has no scopes.** It carries every permission of the Instapage user who created it, in every workspace that user can reach. The permission headers below only limit which tools the MCP shows the model; they do not reduce what the key can do elsewhere.
- 39 tools: 20 read, 19 write. Leads and team details come back masked unless unmasking is requested. Several write tools default to a preview (`dryRun`).
- Limits: 200 requests a minute per key (and IP) plus the plan's daily quota; list pages should not be fetched in parallel; page exports are stored as snapshots that expire after 24 hours; images are uploaded from direct HTTPS URLs (redirects are not followed).

## 2. What it can and cannot do

| Can | Cannot |
|---|---|
| List and search workspaces, pages, folders, domains, assets, collections, experiments, personalizations | Add or change blocks, containers, elements or widgets |
| Export a page as a JSON snapshot and read slices of it | Edit an existing page in place |
| Patch **scalar** values in a copy of a snapshot, and save it as a **new** page | Create or edit forms, integrations, conversion goals, lead notifications, page scripts, SEO settings |
| Create a page from an exported snapshot (standard pages only) | Save or insert My Blocks or Global Blocks |
| Upload an image into an existing, writable asset folder | Create asset folders, collections or domains |
| Publish, unpublish, change a live URL (with confirmation) | Start or stop experiments |
| Aggregate analytics; masked submissions; team roster | Undo a deleted collection page |

**Consequence for this skill:** the MCP cannot compose a page. Structure is authored natively in the Instapage editor (SKILL.md routes B and C) or copied from a page that was (route A). The MCP inspects, copies and patches, uploads, checks, measures and, only in the PUBLISH profile, publishes.

## 3. Setting it up

The user does this. Claude never asks for, reads, stores or prints the key.

**Which Instapage user owns the key.** A dedicated production user in the client's workspace, with the **Editor** role and **Developer Access**. An Editor cannot push anything live, publish, unpublish, start experiments or apply Global Blocks used on live pages, and its API key is held to the same limits (`platform.md` §9). Invite that user only to the workspaces it needs. If the agency works across several clients' Instapage accounts, use one user and one key per client, so a key cannot reach another client's pages.

**Claude Code (recommended): key in the macOS Keychain, headers from a helper.** Claude Code runs a `headersHelper` command at connection time and merges its JSON output into the request headers, so the key never sits in a config file.

1. Store the key (the command prompts for it):

   ```bash
   security add-generic-password -a "$USER" -s "instapage-build-<client>" -w
   ```

2. Create a helper outside the repo, for example `~/.claude/bin/instapage-auth-<client>.sh`, and make it executable (`chmod 700`):

   ```sh
   #!/bin/sh
   key=$(/usr/bin/security find-generic-password -a "$USER" -s "instapage-build-<client>" -w) || exit 1
   printf '{"Authorization":"Bearer %s"}\n' "$key"
   ```

3. Register the BUILD server, private to you and this project (local scope), with the allowlist from §4:

   ```bash
   claude mcp add-json instapage-build --scope local '{"type":"http","url":"https://mcp.instapage.com","headers":{"X-Instapage-MCP-Allowed-Tools":"<BUILD allowlist>"},"headersHelper":"/Users/<you>/.claude/bin/instapage-auth-<client>.sh"}'
   ```

4. Check it with `claude mcp get instapage-build`, then in a session run `session_info` and `workspaces_list`.

Do not put the server in the project's `.mcp.json`: that file is committed. Environment-variable expansion (`${VAR}`) works only in `.mcp.json`, which is why the helper is used instead.

**Claude Desktop chat.** Instapage's generator produces a `claude_desktop_config.json` entry that runs `npx -y mcp-remote@latest` with the key in the entry's `env`. It works, but it leaves the key in a plain config file and runs a package fetched from npm each time. Prefer Claude Code for production work.

**Header rules** (Instapage): names are case-sensitive; lists are comma-separated; `*` is accepted only as the whole value; unknown or empty values make the server return HTTP 400.

## 4. CreativeEngine's profiles

Instapage offers four client-side levels: read only (`X-Instapage-MCP-Access: read`, 20 tools), all tools (`…-Access: write`), selected write groups (`X-Instapage-MCP-Write-Groups`), and an exact allowlist (`X-Instapage-MCP-Allowed-Tools`), which overrides the others. The `pages` write group mixes building with publishing and deleting, so CreativeEngine uses exact allowlists only.

| Profile | Header value (`X-Instapage-MCP-Allowed-Tools`) | Used for | Key |
|---|---|---|---|
| **READ** | `workspaces_list,workspace_get,session_info,pages_list,pages_search,page_get,page_export_json,page_snapshot_read,groups_list,asset_folders_list,asset_images_list,domains_list,analytics_get,experiments_list,personalizations_list,collections_list,collection_get,collection_pages_list` | INSPECT, QA, MEASURE | Editor |
| **BUILD** | READ plus `page_snapshot_patch,page_snapshot_save,page_import_json,asset_image_upload,group_create,page_update` | BUILD, UPDATE | Editor |
| **PUBLISH** | `workspaces_list,workspace_get,session_info,pages_list,pages_search,page_get,domains_list,page_publish,page_unpublish,page_publication_url_update` | One approved PUBLISH action | Manager |

- **Default: no PUBLISH server at all.** A Manager publishes in the Instapage UI after the gate in `publishing.md`. If the user wants Claude to publish, they configure `instapage-publish` separately with a Manager's key, keep it switched off in `/mcp`, switch it on for the one approved action, and off again after.
- **On request only:** `submissions_list` (masked leads, for MEASURE when the user asks) and `team_members_list` (to confirm roles when setting up least privilege). Add them for that session, then remove them.
- **In no profile:** `page_delete`, `group_update`, `group_delete`, `team_members_invite`, `team_members_edit`, `team_members_remove`, `collection_page_add`, `collection_page_delete`, `collection_page_publish`, `collection_page_unpublish`. Deletion and access changes are the client's or the user's to make in the UI. Collections are outside single-page production; review them before adding.

## 5. Tool catalog and policy

| Tool | R/W | What it does (Instapage) | CreativeEngine |
|---|---|---|---|
| `workspaces_list` | R | Workspaces the key can reach | All profiles. Confirms the client's workspace; if others appear, the key is broader than it should be |
| `workspace_get` | R | One workspace by ID or name | All profiles |
| `session_info` | R | Key holder (masked) and quota | All profiles; first call of a session |
| `pages_list` | R | Pages in a workspace, filterable | READ |
| `pages_search` | R | Find a page by ID, title or URL across workspaces | READ; restrict follow-up to the client's workspace |
| `page_get` | R | Page metadata, not content | READ |
| `page_export_json` | R | Stores the page JSON as a snapshot; returns a summary and snapshot ID | READ; INSPECT and QA |
| `page_snapshot_read` | R | Reads part of a snapshot by path; expires after 24 h | READ |
| `page_snapshot_patch` | W | Scalar edits to a forked copy of a snapshot | BUILD, route A. Only values the build sheet changes; text exactly as approved |
| `page_snapshot_save` | W | Creates a **new** page from an edited snapshot; never overwrites | BUILD, route A. The result is a draft |
| `page_import_json` | W | Creates a new standard page from an export or HTTPS URL | BUILD, only with JSON Instapage exported. Never with JSON written by hand or by a model |
| `asset_image_upload` | W | Uploads from a direct HTTPS URL into a writable folder | BUILD; only assets allowed at the page's stage (SKILL.md hard rule 5) |
| `asset_folders_list`, `asset_images_list` | R | Image folders and images | READ |
| `group_create` | W | New page folder | BUILD (organizing drafts) |
| `page_update` | W | Moves a page between folders | BUILD |
| `groups_list` | R | Page folders | READ |
| `domains_list` | R | Custom domains and SSL state | READ; PUBLISH |
| `analytics_get` | R | Visits, conversions and leads by page over a date range | READ; MEASURE |
| `experiments_list`, `personalizations_list` | R | A/B tests and personalizations (cannot start or stop) | READ; MEASURE |
| `collections_list`, `collection_get`, `collection_pages_list` | R | Collections and their pages | READ |
| `submissions_list` | R | Form submissions, masked by default | On request; never unmasked without the user's consent; never saved to the repo |
| `team_members_list` | R | Members and roles, masked | On request |
| `page_publish` | W | Makes a page live at a URL; confirmation required | PUBLISH only, after the gate |
| `page_unpublish` | W | Takes a page offline, clears schedules | PUBLISH only (rollback) |
| `page_publication_url_update` | W | Changes a live page's URL | PUBLISH only |
| `page_delete` | W | Soft delete; UI restore for three days | No profile |
| `group_update`, `group_delete` | W | Rename or delete a folder | No profile |
| `team_members_invite`, `_edit`, `_remove` | W | Access changes | No profile |
| `collection_page_add`, `_delete`, `_publish`, `_unpublish` | W | Collection pages (delete has no undo) | No profile |

The live catalog wins: at session start, compare the tools the server exposes with this table. A tool that has appeared, disappeared or changed behavior is recorded in §7 before it is used.

**Route A, what a copy may not carry.** A snapshot copy is a new page. Instapage documents that uploaded `.instapage` pages lose integrations, scripts and privacy, search and social settings and Global Blocks (`platform.md` §13); until the first-connection test shows otherwise, assume a snapshot copy loses them too. After route A, check and re-apply in the editor: integrations, conversion goals, lead notifications, Scripts & Privacy and the cookie bar, search and social settings, and any Global Block.

## 6. The Public API directly

Base URL `https://api.instapage.com/v1`, bearer key, 200 requests a minute per key and IP, a daily plan quota, HTTP 429 with `Retry-After` when exceeded. Beyond the MCP it offers lead-notification configuration, submission deletion, and workspace and team management.

CreativeEngine uses the MCP. The API is used directly only when an operation the job needs is missing from the MCP and is deterministic, for example setting lead-notification recipients the client supplied, with the user's approval for that call. The key is read from the Keychain at run time and never printed. No API-calling script ships with this skill. Submission deletion and workspace or team changes are never done through the API.

## 7. First-connection checklist

Run once per new key, in a test workspace or on a test page, never on a live client page. Date the result here.

1. `session_info`: the key belongs to the dedicated production user. The user confirms in Instapage (Workspace Settings > Team Members) that its role is Editor with Developer Access.
2. `workspaces_list`: only the intended workspace or workspaces appear. If another client's workspace appears, stop and tell the user.
3. The exposed tools match the BUILD allowlist, with no publishing or deleting tools.
4. Export a test page and read its snapshot. Record the JSON paths for block type, element type, text, heading level, links, image source and alt text, form reference, inline CSS, and page-level HTML, CSS and JavaScript, so QA can check them from a snapshot. Copy them into `platform.md` §15.
5. Route A test: patch one headline on the test page, save as a new page, open it in the editor, and record what carried over: blocks and containers, mobile layout, saved-block origin, Global Block links, the form and its integration, conversion goals, Scripts & Privacy, search and social settings, lead notifications.
6. Upload one image we own from an HTTPS URL; confirm the folder, the file and how alt text is set.
7. Record which write tools accept `dryRun`.

```
FIRST CONNECTION: <date> · by <who> · test workspace <name, ID>
KEY OWNER ROLE:   Editor + Developer Access, confirmed in the UI by <who>
TOOLS EXPOSED:    <n> · matches BUILD allowlist: yes / no
WORKSPACES SEEN:  <n> · only the intended ones: yes / no
JSON PATHS:       element type <path> · text <path> · heading level <path> · link <path> · image <path> · inline CSS <path> · page code <path>
ROUTE A CARRIES:  blocks · mobile layout · Global Block link · form · integration · conversion goals · Scripts & Privacy · search and social · lead notifications  (y/n each)
DRYRUN:           <tools>
```

Status: **not yet connected** (2026-09-24).

## 8. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| No Instapage tools load | Server not configured, or the helper failed | `claude mcp get instapage-build`; run the helper script by hand and check that it prints JSON (the key will appear on screen, so clear the terminal afterwards) |
| HTTP 400 on connect | A header name or value is wrong (case, empty value, unknown tool name) | Check the allowlist spelling against §5 |
| 401 Unauthorized | Key revoked, expired or mistyped | The user generates a new key and replaces the Keychain item |
| 429 Too Many Requests | Rate or daily quota exceeded | Wait for `Retry-After`; stop parallel list calls |
| A write the build needs is refused | The Editor role cannot do it (by design), or the plan lacks the feature | If it is a publish-class action, route it through `publishing.md`. If it is a plan feature, it is a constraint |
| Snapshot not found | Snapshots expire after 24 hours | Export again |
| Image upload fails | The URL redirects, is not HTTPS, or the folder does not accept uploads | Use the direct file URL; pick a writable folder from `asset_folders_list` |
