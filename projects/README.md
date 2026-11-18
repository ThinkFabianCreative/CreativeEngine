# Projects

Client workspaces. Each client has one folder, and everything CreativeEngine knows or makes for that client lives inside it. That folder is the client's isolation boundary.

The scope rules are in the root `CLAUDE.md` ("Clients, projects and knowledge scope"). This file is the filesystem contract. Each client's identity is stated in its own `client/README.md`.

## Layout

```
projects/
  <client>/                    one per client
    client/                    client knowledge, which may outlive any one project
      README.md                identity record: name, folder, identity source, unknowns
      sources/                 client-level raw sources, as received; never edited
      knowledge/               reviewed client knowledge, one topic per file
      assets/                  reusable production assets, with provenance and approval status
      design-library.md        Figma library links and Adobe asset locations, when supplied
    <project>/                 one per assignment
      README.md                project summary and index; links to the brief, never replaces it
      raw/                     project-level raw sources, as received; never edited
      normalized-brief.md      the master working brief
      packets/                 work packets, one file per packet
      work/                    exploration, development, critique and iterations
        strategy/  copy/  concepts/  design/  motion/  interaction/  reviews/     all optional
      outputs/                 exported and final work
        review/                exports shared for review
        approved/              approved exports, with approval records
        delivered/YYYY-MM-DD/  one dated folder per delivery
      results/                 optional: performance evidence and learnings
```

Every subfolder is optional and created only when it holds material. No industry, funnel stage, channel or software gets a compulsory folder; name an extra `work/` subfolder after the job it does when one is needed.

- One client holds many projects. One project holds many sources and many creative problems (one packet per problem). One creative problem holds many iterations and executions, in `work/` and `outputs/`, named by its problem or packet ID.
- Folder names are short lowercase slugs. They are handles, not evidence: identity is stated inside the files.
- `client` is reserved and is never a project name.
- `new-business/` holds pitch and RFP prospects that are not yet clients. Each prospect inside it follows this same layout (`new-business/<prospect>/client/`, `new-business/<prospect>/<pitch>/`) and moves to `projects/<client>/` if won. See `new-business/README.md`.
- Create a folder only when there is something to put in it.
- Nothing in one client's folder references, copies or summarizes another client's.
- Brief normalization, work packets and their schema: `shared/frameworks/brief-normalization.md`.

## Sources

- A source that arrives with an assignment goes in that project's `raw/`. BriefMachine records its scope (CLIENT-LEVEL, PROJECT-LEVEL or UNKNOWN) in the normalized brief.
- A source goes in `client/sources/` only when the user files it there or confirms that it is enduring. A confirmed project source is copied there; the project copy stays.
- Raw sources are never edited, renamed, moved or deleted, at either level. A new version sits beside the old one.
- Supplied files keep their original filenames.
- Brand guidelines, identity files and other material the user files as enduring go in `client/sources/`. Anything reviewed from them becomes a `client/knowledge/` entry.

## Client identity record

`client/README.md` is the first file in every client workspace. It states:

```
CLIENT:           [name exactly as supplied]
FOLDER:           projects/<client>/
IDENTITY SOURCE:  [who supplied the name, where, and when]
IDENTITY STATUS:  AS SUPPLIED / PENDING CONFIRMATION / CONFIRMED BY [who, when]
```

followed by what is unknown, and links to whichever client-level locations exist. It records identity only. Brand, audience, offering, claims, contacts and approvers are `client/knowledge/` entries, added only from reviewed sources.

## Client assets and design library

`client/assets/` holds reusable production files, such as logos, fonts, templates and approved photography, that more than one project uses. Each asset, or a manifest beside a group of assets, records:

```
ASSET:            [filename or link, with version]
PROVENANCE:       [client source path, originating project, or who supplied it, and when]
USAGE / RIGHTS:   [as stated by the source, or UNKNOWN]
APPROVAL:         APPROVED BY [who, date, evidence] / NOT APPROVED / UNKNOWN
```

A file in `assets/` is not approved because it is there.

`client/design-library.md` lists design-system locations only when they are supplied: Figma team libraries and files, Adobe Creative Cloud Libraries and shared asset folders. Each entry records the link or path, what it contains, its owner, who has access if known, and the date it was checked. A link records a location; it does not make the contents reviewed client knowledge.

## Client knowledge entries

`client/knowledge/` holds reviewed conclusions about the client, one topic per file: for example brand, voice, identity, portfolio, claims, legal, audience, stakeholders or creative history. Each entry states:

```
CLIENT:
DOMAIN:
ENTRY:          [what is established; source wording where the wording matters]
SOURCE:         [source path(s): a client-level source, or the originating project]
DATE:           [of the source, where known]
STATUS:         CURRENT / HISTORICAL / SUPERSEDED
CONFIRMED BY:   [who confirmed it, and when; required for anything promoted from a project]
```

- A claim keeps its claim-ledger status. Being client-level does not make it verified.
- A HISTORICAL entry is context for later projects, not current truth.

## Project README

Each project starts from `shared/templates/project-readme.md`. The README identifies the client and project and indexes the work. Its scope, audience, goals, channels and deliverables are a short summary that links to `normalized-brief.md`.

- `normalized-brief.md` is the briefing authority. Where the README and the brief differ, the brief governs and the README is corrected.
- Before a brief exists, the README records only what the user has supplied, labeled as such, and leaves the rest OPEN.
- Education, funnel and channel sections apply only where the assignment establishes them.

## Working files

`work/` holds everything still in development. Use only the subfolders a project needs:

| Subfolder | Holds |
|---|---|
| `strategy/` | Strategic development: research notes, audience analysis, strategy options. Changes to the brief itself go through BriefMachine |
| `research/` | CreativeResearcher output: competitor maps, voice-of-customer files, benchmark lists, reference boards, asset audits. Screen-grabs are internal working references, named `YYYY-MM-DD_<source>_<subject>` with their source URL |
| `copy/` | Scripts, headlines, body copy and verbal development |
| `concepts/` | Concept boards, territories and idea development |
| `design/` | Figma links, Adobe editable files, layouts, identity and visual development |
| `motion/` | Animatics, edits and motion design files |
| `interaction/` | User flows, wireframes, prototypes and developer handoff |
| `reviews/` | Feedback and decisions, tied to exact asset versions |

**Figma.** Figma files live in Figma. Record them in a `figma-links.md` inside the relevant subfolder: file link, the page or frame link, what it shows, the packet ID, and the version name or date it was checked. Link the specific page or frame being reviewed, not only the file.

**Adobe Creative Cloud.** Keep editable files (such as `.psd`, `.ai`, `.indd`, `.aep`, `.prproj`) in the relevant subfolder. Keep their linked dependencies in a `links/` folder beside the file, or record where each dependency lives when it cannot be copied, such as fonts or Creative Cloud Library items. A file whose links are missing is not a complete source.

**Interaction.** Keep flows, prototype links and handoff material (specifications, redlines, annotated frames and developer notes) under `interaction/`. Record which prototype version a handoff describes.

**Reviews.** Each review record in `reviews/` states:

```
ASSET:        [exact filename and version, or Figma link with version or date]
REVIEWER:     [who]
DATE:
FEEDBACK:     [as given; source wording where it matters]
DECISION:     [what was decided, and by whom]
NEXT VERSION: [filename of the version that responds, once it exists]
```

## Naming created files

Files CreativeEngine or the team creates use readable, versioned names, starting with the packet ID when there is one:

```
<packet-id>_<descriptor>_v<NN>.<ext>        P1_instagram-carousel-card-03_v02.png
<project>_<descriptor>_v<NN>.<ext>          <project>_moodboard_v01.pdf
```

- Never reuse a version number, and never overwrite an earlier version that someone reviewed, approved or received.
- Supplied sources keep their original filenames.

## Production copies and caches

- When a raw source must be changed for production (cropped, converted, retouched), work on a copy in `work/` or `client/assets/`, never the original. Record `COPIED FROM: [raw path]` and what was changed.
- Media caches, render previews, proxies, autosaves and other temporary files stay outside `projects/`, in the application's own cache or scratch location. They are not part of the archive.

## Outputs, approval and delivery

| Folder | Holds |
|---|---|
| `outputs/review/` | Exports shared for review. Not approved. |
| `outputs/approved/` | Exports that have an approval record |
| `outputs/delivered/YYYY-MM-DD/` | Exactly what was delivered on that date. Add a short label after the date if two deliveries share one. |

A folder name does not establish approval. Every approved or delivered file is covered by a record in that folder:

```
ASSET:        [exact filename and version]
APPROVED BY:  [who]                  or  DELIVERED TO: [who]
DATE:
EVIDENCE:     [path to the email, comment export or signed file, or where it is held]
CONDITIONS:   [scope, markets, expiry or caveats, if any]
```

- Without a named approver, date and evidence, the file is not approved, wherever it sits.
- Delivered files are never edited or renamed afterwards. A correction is a new version in a new dated delivery.

## Results

`results/` is optional project knowledge: performance data, reports, research findings and learnings. Each item records its source, date, metric definition and the exact assets or versions it describes.

Results stay project knowledge. They reach `client/knowledge/` only through promotion (below), and never reach another client.

## Client creative history

Creative history is client and project knowledge, never global method. Record it in the project where it happened. A client-level `knowledge/creative-history.md` may index it.

| Type | Meaning |
|---|---|
| EXPLORED | Territories investigated |
| USED | What actually ran |
| APPROVED | What the client approved |
| REJECTED | What the client rejected, and why if known |
| LEARNED | What research or performance revealed |

Every item carries its project, date and source.

## Source consensus and divergence

**Consensus.** Independent reviewed sources converging on one derived finding:

```
FINDING:        [DERIVED]
SUPPORTED BY:   [each source · scope · project · date]
SCOPE:          [project or client: the narrowest scope all the sources share]
CONFIDENCE:
USE:            [how it may inform strategy or creative stimulus]
```

- Two documents repeating the same research are one source.
- Consensus raises confidence in a derived finding. It does not make it a source fact or a verified claim.
- Sources from different clients cannot form a consensus.

**Divergence.** Sources that materially disagree within one domain:

```
SOURCE A:       [exact wording · source · scope · date · status]
SOURCE B:
DOMAIN:
AFFECTS:
IMPACT:
SAFE HANDLING:  [DERIVED]
RESOLUTION:     OPEN
```

- Inside a normalized brief, a divergence is recorded as a CONFLICT in the open-question register, with each side's source and scope named.
- It stays OPEN until whoever owns that domain resolves it.

## Promotion

**Project → client.** A project finding becomes a client knowledge entry only after deliberate review and user confirmation. The entry records its originating project, date and confirmer, and states the finding no more broadly than the evidence supports: "Segment X responded to price proof in Campaign Y" does not become "this client's audiences prioritize price". The project record is not changed.

**Client → global.** Client facts never become global method. A reusable reasoning method, stated without client facts, may be added to global method only through the framework or skills policy in `CLAUDE.md`.

**Across clients.** Reserved and not implemented. See "Cross-client learning" in `CLAUDE.md`.
