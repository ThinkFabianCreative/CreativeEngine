# artlist-production

| | |
|---|---|
| Source | CreativeEngine (in-house), for the third-party Artlist MCP connector |
| Owner | DesignChamp (image and motion generation). WordSmither supplies scripts, voiceover text, hooks and lyrics. CreativeDirector decides what is worth rendering at pitch quality in JUDGE |
| Status | Built at the user's request 2026-09-24 ("integrate artlist mcp into the production flow where it makes sense"). **Connector not yet connected**; first-connection checklist pending |
| Installed | `.claude/skills/artlist-production/` (SKILL.md + `references/`: `mcp-and-account.md`, `models.md`, `recipes.md`, `prompting.md`, `run-log.md`) |
| Scope | Rendering decided ideas as stills, video, voiceover and music through the Artlist MCP: comps, pre-viz, animatics, hook variants, product lifestyle, creator-style video, localized voiceover. **Inspiration and pitch only, never commercial use** (Andres, 2026-09-24) |
| Storage | Generated media stays on the local machine: `projects/**/work/generated/` is gitignored except its Markdown logs, which reference the files (Andres, 2026-09-24) |

## Review (2026-09-24)

The skill itself is Markdown only, with no executables. The review covers the connector it drives.

- **Connector.** Remote MCP at `https://mcp.artlist.io/mcp`, OAuth with the Artlist account, beta (help article updated 2026-08-27). Not in Claude's connector directory, so it's added as a custom connector. No credentials pass through Claude.
- **Spend.** Every call spends plan credits at request time. Calls can't be cancelled or refunded, the MCP gives no cost quote, and Unlimited plans don't apply through it. The skill therefore quotes each batch from its rate card and requires explicit approval, and drafts cheap before rendering. This follows the Figma Weave pattern already in the stack.
- **Data sent.** Prompts, reference images, audio samples and product photos go to Artlist and on to third-party model providers. Most providers are contractually barred from training on them; some models may train (flagged in the Toolkit UI, possibly not in the MCP). The skill limits uploads to material the project has rights to and asks before any unreleased or confidential client material is uploaded.
- **Rights.** Artlist assigns output rights to the account holder, with commercial and client use allowed even after the subscription ends. There is no guarantee of uniqueness or non-infringement. AI content from Artlist's Explore page or Catalog is an Asset under a different license. CreativeEngine doesn't use these rights commercially: outputs are inspiration and pitch only, and production makes the real assets.
- **Terms that bind the account** (the agency's Artlist account, whoever runs it). No deceptive "authentic" or human-made presentation; no false advertising; no real people, brands or likenesses without consent; no deceptive voice clones or avatars; no imitation of a real artist's voice, persona or distinctive style (the clause names music and vocals, and also "other Output"); the account holder is liable for use by staff, contractors and clients. The skill's rules on product fidelity, synthetic people and releases implement these.
- **Artist names.** Names stay in prompts for accuracy of the style reference (Andres, 2026-09-18, confirmed 2026-09-24; `image-direction-reference.md` §1). Andres edits and acknowledges Artlist's terms on style references himself. Every referenced artist is recorded in the generation log and credited in the pitch documentation (`references/run-log.md` → Attribution). Practically, Lyria blocks artist and song names, and a blocked visual prompt is rerun with the technical translation only.
- **Isolation.** Style Kits and References are account-wide in Artlist, so they're named `<client>-<campaign>` and never crossed between clients. Generated files and logs live in the client's project folder. The skill's own files hold no client facts.
- **Overlap.** Adobe Firefly and Photoshop tools (Adobe connector), Figma Weave, and the `identity-design` skill's Gemini, Atlas Cloud or MuAPI calls also generate images. The skill routes stills that must live in Adobe files, or need Adobe provenance, to Firefly, and flows already built in Weave to Weave. Artlist is the only tool in the stack for video with native sound, voiceover and music together. `format-prototyping` shows the results in their real format; this skill only produces them.
- **Gaps it doesn't close.** Video-to-video, lip-sync and dubbing remain Toolkit-website jobs. Platform AI-disclosure rules aren't in any `shared/knowledge/` module (checked 2026-09-24); that doesn't block this skill, because generated assets are never published.

## Use

- **DesignChamp:** recipes A–D, G, H for comps, pre-viz, animatic picture and consistent sets. Checks every output against `image-direction-reference.md` §6 and §10 before anyone sees it.
- **WordSmither:** writes the scripts, voiceover text, hooks (recipe E) and lyrics. Voice and music formatting is in `references/prompting.md`. Never writes a synthetic person's lines as a customer testimonial (recipe F).
- **CreativeDirector:** approves pitch-quality renders in JUDGE, checks that every pitch carries the comp labels and artist credits, and reviews the run report's spend against what the work needed.
- **Any role, any session:** this record governs Artlist use on CreativeEngine work (root `CLAUDE.md`).
