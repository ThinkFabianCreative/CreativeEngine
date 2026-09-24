# Figma: the Instapage Native Kit and the three layers

Figma is DesignChamp's specification environment, not the runtime. The approved Figma spec is the production target; `instapage-production` builds it with Instapage's own authoring tools. There is no path from a Figma screenshot to recreated HTML and CSS.

The global kit defines **how to build in Instapage, never what a client looks like.**

## 1. Three layers

| Layer | Lives in | Holds | Never holds |
|---|---|---|---|
| **1 · Instapage native primitives** (global) | The kit file (§2) | Native blocks, containers, elements, widgets, forms, reuse behavior, platform limits, drawn in a deliberately unstyled wireframe register | Any client's faces, colors, button look or spacing; a CreativeEngine landing-page aesthetic; hero or card styling; imagery style; one client's layout as a pattern; performance assumptions |
| **2 · Client design system** (one per client) | That client's own Figma library, for example "<Client> · Instapage components", recorded in `projects/<client>/client/design-library.md` | Built from the client's approved sources: typography, colors (Instapage Styles holds up to 14), spacing principles, button and form styling, imagery and art direction rules, iconography, grid preferences, interaction style, motifs; client components named `<Client> / <Section> / <Variant>`, built from Layer 1 instances | Anything from another client; anything promoted from a project without the promotion process |
| **3 · Project composition** (one per assignment) | The project's Figma file or page, linked in `projects/<client>/<project>/work/design/figma-links.md` | This page's layout, composition, imagery, copy, offer, form, CTA, hierarchy, responsive behavior, experiment, and which sections are reusable or one-off | Standards for the client: a project decision becomes a client standard only through promotion (`projects/README.md`) |

**One native Instapage production grammar, many client design systems, many project expressions.** The production system should be invisible in the final aesthetic. Its consistency shows in quality, maintainability and authorability, not in clients looking alike.

The architecture passes only if all of these can be true at once:

1. Client A has an editorial, minimal, typography-led page.
2. Client B has a dense, product-led, UI-heavy page.
3. Client C has an expressive, image-led, high-energy page.
4. All three are built from native, Instapage-authorable structures.
5. All three can be edited by client-side staff in Instapage.
6. None inherits another client's aesthetic or project decisions.
7. CreativeEngine imposes no recognizable universal look.

The kit's Validation page demonstrates 1–3 and 6–7 with three synthetic clients built from identical primitives and identical words (§2).

Rules that follow:

- **No CreativeEngine-branded component library.** No "CreativeEngine Hero" or "CreativeEngine CTA" recolored per client. That produces visual convergence.
- **Client components belong to their client.** `Client A / Hero / Product` and `Client B / Hero / Editorial` may share the same primitives and nothing else.
- **Never start from another client.** Another client's library, blocks, assets, patterns, stakeholder feedback or results are never a starting point, reference or evidence. A cross-client comparison happens only when the user asks for one, as a separate labelled task, and its findings enter no client's knowledge (root `CLAUDE.md`).
- **A pattern that worked for one client stays with that client.** Global method gains only deliberately generalized, non-confidential production method, through the skills policy.
- **Templates and saved blocks are implementation resources, never creative authorities.** Production asks "what is the most faithful native build of the approved spec?", never "which existing template or block is closest?". Instapage's own templates and block templates are never a design starting point.
- **DesignChamp pushes the native range before asking for an exception.** Client differentiation never comes from custom code, embedded sites, proprietary renderers or non-authorable components (`native-authorability.md`).

## 2. The kit file

**CreativeEngine · Instapage Native Kit**: `https://www.figma.com/design/suQoQdAczG3IZRVMxooqpb`. TRAFFIK team, in the creator's drafts; created 2026-09-24. Publication status UNCONFIRMED on recheck: the published-component query requires a higher plan/seat. Earlier report said pending; do not treat it as current proof (§6).

| Page | Holds |
|---|---|
| Cover, Read me | Purpose, the three layers, how DesignChamp uses the kit by mode, layer names, annotation categories, never-list |
| Foundations | The three layers; why the primitives look unfinished; platform facts a client layer has to fit (14 Styles colors, three font roles, units, workspace scoping); canvases and the 768 px breakpoint; limits |
| Structure | Fluid Grid Block pattern (Figma grid layout), mobile-order demo, container-settings mapping, Canvas block pattern. Frames, not components |
| Elements | `IP / Headline` (Level H1–H6), `IP / Paragraph` (List), `IP / Button`, `IP / Image`, `IP / Video` (Host), `IP / Line` (Orientation), `IP / Box (Canvas only)`, `IP / Circle (Canvas only)` |
| Widgets | `IP / Timer`, `IP / Accordion` (State), `IP / Carousel` |
| Forms | `IP / Form Field` (8 types), `IP / Form Submit`, `IP / Form` |
| Page & reuse | `IP / Tag` (8 kinds, margin annotations), `IP / Popup`, `IP / HTML (exception only)` |
| Molecules & organisms | Neutral starter (added 2026-09-24). Molecules: `IP / Text Group` (eyebrow, title, subtitle, description, each toggleable), `IP / Action` (Primary, Secondary, Tertiary), `IP / Button Group`, `IP / Card` (Color, Image, Image overlay). Organisms, each a Fluid Grid block: `IP / Hero` (Split, Overlay), `IP / Proof · Cards`, `IP / Form Section`, `IP / CTA Band` |

**Semantic tokens.** The collection `Semantic (client fills)` holds semantic names only: `color/surface/*`, `color/text/*` (including eyebrow and inverse), `color/action/primary|secondary|tertiary`, `color/border/default`, `color/overlay/image`, `space/xs…section`, `radius/card|button`, `opacity/overlay`. The text styles `Semantic/Eyebrow|Title|Subtitle|Body|Action` go with them. In the global file every value is a wireframe placeholder, aliased to `wire/*`. A client library duplicates the starter and sets the values, and optionally adds client-specific names, from that client's approved sources. Molecules and organisms bind to these names, so one structure takes any client's look. Colors that end up in Instapage Styles must fit its 14 slots, and the semantic text roles resolve to the three font roles.

**Native notes.** A card is a container with a background, border and radius, all native container settings. An image-overlay tint is documented for block (Instablock) backgrounds, not for containers; otherwise the tint is part of the approved image. Gradients are not a verified native container setting, so the starter has none. Organisms are starting structures for a client library, not layouts to reuse unchanged: DesignChamp composes each page.
| Spec template | Layer 3 scaffold: spec header, Desktop 1440 and Mobile 400 frames with matching block IDs, margin tags, approved-spec checklist |
| Validation (SYNTHETIC) | Range test (three synthetic clients, same primitives and words) and the synthetic end-to-end spec (`validation/instapage-production-2026-09-24/`). Fixtures, never templates; move to their own file once the kit is a published library |

Audited 2026-09-24: all 17 top-level component families carry official help links; nested variants rely on their family link. A link is not runtime evidence. See `capability-map.md` for per-feature status; Tag is specification metadata, and HTML is an exception boundary, not native content.

**Why the primitives look unfinished.** Layer 1 renders in a wireframe register: grey outlines, radius 0, a placeholder mono face (Roboto Mono), no shadows, no case or hover treatment. Nothing in it can be mistaken for a style or shipped as a default. Variables: `Wireframe (not a style)` (`wire/*`) for the primitives and `Kit docs` for documentation colors. Text styles: `Wireframe/*` role placeholders and `Doc/*` for documentation. Annotation categories: IP · Build, IP · Copy, IP · Asset, IP · Reuse, IP · Exception.

## 3. By mode (progressive constraints)

| Mode | How the kit is used |
|---|---|
| EXPLORE | Not at all. Creative freedom first; nothing is constrained to a component library or killed for being hard to build |
| DEVELOP | For directions getting serious, DesignChamp checks each section maps to a native structure and marks gaps with IP · Exception annotations. Warnings, not verdicts. Push the native range before proposing an exception |
| JUDGE | The spec is realistically buildable natively, or each gap has a proposed exception with native options listed, for `creative-engine-director` to see before approving production |
| PRODUCTION | Mandatory. Every element is a Layer 1 instance or sits inside a client component built from them; the spec is fully annotated (§5) |

These describe how this skill behaves inside the canonical modes; they do not change them.

## 4. Mapping: Figma to Instapage

| Figma | Instapage primitive | Where it is built | Limits to design within |
|---|---|---|---|
| Frame with grid layout, named `B## · <section> · Fluid Grid` | Fluid Grid Block | Insert Block > Fluid Grid Block (preset or custom grid) | No box or circle inside; block padding at least 20 px left and right advised |
| Auto-layout frame spanning grid cells, named `B##.C# · m#` | Container | Container settings | Direction = element flow; alignment = justify/align; gap = space between; padding = container padding; fill = background color or image; stroke = border; radius = rounded corners; `m#` = mobile stacking order |
| Frame without auto layout, named `B## · <section> · Canvas` | Canvas block (Instablock) | Insert Block | Free positions; mobile arranged separately at 400 px; elements cannot leave their block on mobile |
| `IP / Headline` (Level) | Headline, tag h1–h6 | Left sidebar | One h1 per page; no lists |
| `IP / Paragraph` (List) | Paragraph, with lists | Left sidebar | — |
| `IP / Button` | Button with link setup | Left sidebar | Label = approved CTA wording, exact; link in IP · Build |
| `IP / Image` | Image | Image library | Formats and size limits; alt text on the placed image; asset status in IP · Asset |
| `IP / Video` (Host) | Video | Left sidebar | YouTube, Vimeo or Wistia only; no upload, no loop |
| `IP / Line` (Orientation) | Line | Left sidebar | Vertical lines desktop-only by default |
| `IP / Box`, `IP / Circle` | Box, Circle shapes | Left sidebar | Canvas blocks only; no click action |
| `IP / Timer` | Countdown timer | Left sidebar | One fixed date; no labels on mobile |
| `IP / Accordion` (State) | Accordion | Left sidebar | Text only inside sections |
| `IP / Carousel` | Carousel | Left sidebar | Placement in Fluid Grid unverified |
| `IP / Form`, `IP / Form Field`, `IP / Form Submit` | Form Library form | Assets > Forms, then insert | Paragraph family at a fixed field size; redirect or download after submit, not both |
| `IP / Popup` | Popup | Assets > Popups | White background |
| `IP / Tag` Global Block (margin) | Global Block | Block menu > Save as Global Block | Reason, owner, approver; once per page; Manager to apply on live pages |
| `IP / Tag` My Block (margin) | Saved block (My Blocks) | Block menu > Save to My Blocks | Per workspace |
| `IP / Tag` Sticky (margin) | Sticky Bar | Page settings | First or last block |
| `IP / Tag` Desktop only / Mobile only (margin) | Visible on | Element menu | Blocks hide on mobile only |
| `IP / HTML (exception only)` | HTML element | Left sidebar | Only with an APPROVED exception |

A client component (Layer 2) maps to whatever Layer 1 instances it contains. The build sheet records the primitives, not the client component name, plus the client component name as its reuse source.

**From spec to build sheet.** Layer names carry the IDs (`B01`, `B01.C1 · m1`, `E01 · Headline h1`, `E05 · Image · IMG-01`); annotations carry the data that is not visible: IP · Copy (copy ID), IP · Asset (asset ID and status), IP · Build (links, visibility, sticky, form settings, conversion goal), IP · Reuse (class, name, reason), IP · Exception (EXC ID or constraint). The build sheet (`build-sheet.md`) is written from those, and the lint checks it against the approved copy and the packet.

## 5. What an approved spec contains

1. A header: client, project, packet, spec version, status and approval, client library and version, copy doc version, the three font roles, colors, search and social copy IDs.
2. Desktop and mobile frames with the same block IDs in the same order. 1440/400 are replaceable preview conventions, not production dimensions.
3. Every block named and typed (Fluid Grid or Canvas), with a reuse tag in the margin.
4. Figma grid/auto layout expresses intended Fluid Grid relationships; every container names its mobile order. FLEX/HUG and grid behavior do not prove importability, runtime responsiveness or native authorability.
5. Every element a Layer 1 instance, or inside a client component built from them.
6. IP · Copy on every text element, IP · Asset on every image, IP · Build for links, visibility, sticky blocks and the form. Repeat shared annotations on both devices; no implicit desktop inheritance. Use stable B/E IDs and form field keys, verify parity, and preserve explicitly marked device-specific notes. The same rule applies inside client components.
7. The form: fields in packet order with required state, after-submit behavior, integration and conversion goal.
8. Every gap from native marked IP · Exception, with native options listed.
9. Nothing from another client, no generated imagery, no copy that is not approved.

The kit's Spec template page is this checklist as a scaffold.

## 6. Setting up a client library (Layer 2)

1. The user publishes the kit as a TRAFFIK team library (Assets > Publish), so other files can use its primitives. If publication is unavailable, copy only neutral Layer 1 primitives into the isolated client file with provenance. Never duplicate Validation (SYNTHETIC) or synthetic client styles into a client library.
2. Create the client's own library file and record it in `projects/<client>/client/design-library.md` with its link, owner, access and date.
3. Preserve client variable/style bindings: wireframe values are replaceable conventions, not reasons to detach bindings. Figma bindings are not live Instapage Styles synchronization. Define the client's variables and text styles **only from the client's approved sources** (`client/knowledge/`, `client/sources/`): the three faces, the colors (at most 14 if they will be the Instapage Styles palette), spacing principles.
4. Build client components from Layer 1 instances and name them `<Client> / <Section> / <Variant>` (for example `<Client> / Hero / Lead Form`). Their structure stays native: the same limits as §4.
5. When a client component becomes an Instapage saved block, give the block the same name (`reusable-blocks.md` §3).
6. Never copy, reference or start from another client's library.

## 7. Figma operations

- Plugin API work: load `figma-use` before any `use_figma` call, and `figma-generate-library` when building components.
- Figma's built-in agent: brief it in the format of `shared/frameworks/visual-craft.md` §12.1 and attach `DesignChamp/knowledge/figma-agent-pack/09_instapage_native_kit.txt` with the client's pack files.
- Reading a spec for the build sheet: `get_metadata` for structure and names, and a read-only `use_figma` script for annotations.
