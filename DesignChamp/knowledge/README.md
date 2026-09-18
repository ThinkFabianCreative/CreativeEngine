# DesignChamp knowledge

Reference material specific to DesignChamp.

| Item | What it is |
|---|---|
| `figma-agent-pack/` | Plain-text export (00–08; 08 added 2026-09-17 from `shared/frameworks/visual-craft.md`) of CreativeEngine visual taste and Meta ad craft for Figma's built-in agent. Derived from `shared/knowledge/ANDRES_CREATIVE_OS.md`, `shared/frameworks/hey-whipple-copycraft.md` §2 and §10, `shared/frameworks/creative-trajectory-evaluation.md` §9–10 and `.claude/skills/format-prototyping/references/meta-ad-units.md` (2026-09-13). Those files remain the source of truth; regenerate the pack when they change. Holds no client facts: client files live in each project's `work/figma-agent-pack/` |
| `image-direction-reference.md` | Photography and image-generation direction: photographic styles, camera angles and height, lenses and apertures, light setups, prompt anatomy, how the main generation models differ, and a reference library of photographers, directors, painters, film stocks and grades with prompt translations (names brief the team; prompts use the translation). Supports `visual-craft.md` §5. No client facts. Model facts dated 2026-09-17; verify before relying on them |
| `presentation-style-library.md` | Retrieval index for the 12 presets and 34 bold design systems in the `frontend-slides` skill: what each layer holds, how to read it progressively, and how DesignChamp uses it as reference in EXPLORE, DEVELOP and JUDGE. Third-party reference, not taste; the files stay in `.claude/skills/frontend-slides/` |
| `brand-design-md/` | 74 unofficial DESIGN.md analyses of real brands' public websites (tokens, type, components, do's and don'ts), from `voltagent/awesome-design-md` (MIT, 2026-07-31). Index, review and guardrails in `brand-design-md/README.md`. Reference and category-sameness baseline only: never a client brand source, never a template to impersonate |

Material useful across departments belongs in `shared/knowledge/`.
