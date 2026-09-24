# Reusable blocks: independent or synchronized

A client's reusable components are native saved blocks in the client's own Instapage workspace, not code. There are two kinds, and confusing them is how one edit changes many live pages by accident.

## 1. Three reuse classes

| Class | Instapage feature | After insertion | Editing it changes | Use for |
|---|---|---|---|---|
| **Page-local** | An ordinary block | — | This page only | Anything built for one page |
| **Independent reusable** | Saved block in **My Blocks** | A copy; each instance can diverge | This page only | Patterns that recur but should be adapted per page: hero arrangements, proof sections, testimonial layouts, benefit sections, CTA sections, FAQ sections, form sections, product-detail sections |
| **Synchronized** | **Global Block** (plan-dependent) | The same block everywhere | **Every page that uses it, live pages included** | One source of truth deliberately required: legal or footer content, a compliance module, truly global navigation, a centrally maintained shared section |

The default is page-local or My Blocks. **A block is never made global just because it is reusable.**

## 2. When a Global Block is allowed

All of these must be recorded in the build sheet (`reuse: "global_block"`):

- **Reason:** why one synchronized source of truth is required, in one sentence. "We reuse it" is not a reason.
- **Owner:** who is allowed to change it (a named role at the client or agency).
- **Approver:** who approved making it global (the client, for legal and compliance modules).
- **Pages:** the pages expected to carry it.

Rules that come from the platform (`platform.md` §8):

- A given Global Block loads only once per page. Never place it twice.
- Applying a change to a Global Block that sits on any live page needs Manager permission and changes those live pages. It is a **publish-class action** (`publishing.md`): list the affected pages from the Apply Changes dialog, get the go-ahead, then apply.
- "Disconnect" turns one instance into an ordinary block. Use it when a page genuinely needs to differ, and record it.
- Whether a Global Block link survives an MCP snapshot copy is unverified (`platform.md` §15). Until tested, re-insert Global Blocks in the editor after route A.

## 3. The client's block library

- **Lives in the client's workspace.** Saved blocks, Global Blocks and images are per workspace and cannot cross to another workspace.
- **Recorded in the client's knowledge area**, in `projects/<client>/client/design-library.md`:

```
INSTAPAGE WORKSPACE:  <name> · <workspace ID> · supplied by <who, date> · plan features checked <date>
| Block name | Class (My Block / Global) | Pattern it serves | Built from (spec, version) | Pages using it (Global) | Owner | Date |
```

- **Naming** mirrors the client's Figma library (`figma-kit.md` §6): `<Client> / <Section> / <Variant> · v<NN>` for My Blocks, for example `<Client> / Hero / Lead Form · v01`, and `GLOBAL · <Client> / <Section> / <Variant> · v<NN>` for Global Blocks, so anyone editing can see at a glance which blocks are synchronized.
- **Built from an approved spec.** A saved block enters the library only from approved, QA-passed work. Exploration and prototypes are not saved as blocks. A block that served one project becomes a client standard only through promotion (`projects/README.md`).
- **Isolation.** Never recreate one client's blocks, layouts or patterns in another client's workspace, and never start a client's library from another client's. The global Figma kit carries the neutral vocabulary only (`figma-kit.md` §1).

## 3a. No house library, no template authority

- There is no CreativeEngine-branded block library ("CreativeEngine Hero", "CreativeEngine CTA") to be recolored per client. Each client's blocks express that client's design system; two clients' libraries may share primitives and nothing else.
- Saved blocks, Instapage's page and block templates, and Instapage's AI page generator are implementation resources, never creative authorities. Production never picks the "closest" block or template and fits the design to it. It builds the approved spec, reusing a client block only when the spec calls for that block.

## 4. Forms, popups and images reuse too

- **Form Library** forms can be reused across pages. Whether editing a library form updates pages already using it is not documented: treat each placement as its own until verified in the workspace.
- **Popups** can be regular or global; a global popup behaves like a Global Block (§2).
- The **image library** is shared across the workspace. Alt text edited in the library only affects future inserts, so fix alt text on the placed image.

## 5. Tell the client

The handoff note for every published page lists which blocks are My Blocks (safe to edit per page) and which are Global (an edit changes every listed page), so a client-side editor cannot change many live pages by accident (`publishing.md` §6).
