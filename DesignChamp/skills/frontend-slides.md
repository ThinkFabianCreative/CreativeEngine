# Frontend Slides

| | |
|---|---|
| Source | `github.com/zarazhangrui/frontend-slides` (MIT), commit `9906a34`, 2026-06-23, plugin v2.1.0 |
| Owner | DesignChamp |
| Status | Approved by the user 2026-09-14 (installation requested) |
| Exposure | Installed at `.claude/skills/frontend-slides/` from the repo's `plugins/frontend-slides/skills/frontend-slides/` folder, plus `LICENSE`. The repo root holds an identical duplicate copy, which was not installed |
| Invocation | Automatic |
| Reviewed | 2026-09-14 |

## What it does

It builds single-file HTML presentations on a fixed 1920×1080 stage that scales to fit the screen. It starts with content questions and a density choice (speaker-led or reading-first). It then shows three visual style previews: a safe preset, a bold template and a wildcard. The chosen style is expanded into the full deck. It can also convert PPTX to HTML, deploy to Vercel and export to PDF.

Files: `SKILL.md`, `STYLE_PRESETS.md` (12 presets), `html-template.md`, `viewport-base.css`, `animation-patterns.md`, `bold-template-pack/` (34 templates, each with a `preview.md` and `design.md`, plus `selection-index.json` and `deck-stage.js`) and `scripts/`.

## Security review

- **`scripts/extract-pptx.py`:** local only. Reads a .pptx and writes JSON plus images into an output folder. Needs `pip install python-pptx`.
- **`scripts/export-pdf.sh`:** creates a temp dir and runs `npm install playwright` and `npx playwright install chromium` there (about 150MB download). It serves the deck's parent folder on a random localhost port, screenshots each slide into a PDF, deletes the temp dir and then runs `open` on the PDF. No global installs. The local server reads any path under the deck's folder, only while the export runs.
- **`scripts/deploy.sh`:** **publishes to the public internet.** It may run `npm install -g vercel` (global install) and `vercel login` (interactive auth), then `vercel deploy --yes --prod`. For a single HTML file, it also bundles any local files the HTML references. The resulting URL is public.
- **`deck-stage.js`:** a web component for navigation, scaling and print layout. No fetch, storage, eval or outbound network calls. It posts slide-index messages to its parent window.
- **External URLs:** Google Fonts, Fontshare, jsDelivr and deno.dev CJK font CSS; the author's `beautiful-html-templates` repo (template source links); Vercel, Node.js and Playwright docs.
- **No findings:** no credential access, no reading of `.env` or secrets, no destructive commands beyond cleaning up its own temp dir and preview folder, no prompt-injection text. The whole repo was pattern-scanned. `SKILL.md` and all scripts were read in full; the 34 template `design.md` files were scanned, not read line by line.

## Local dependencies

Installed 2026-09-14 at user level, no admin rights. Tested end to end: PPTX extraction, and PDF export of a 2-slide test deck.

| Dependency | Version | Location | Needed for |
|---|---|---|---|
| Node.js LTS (official build, SHA-256 verified) | v24.21.0 | `~/.local/node`, symlinked into `~/.local/bin` | PDF export, deploy |
| Playwright Chromium | build 1243 | `~/Library/Caches/ms-playwright` | PDF export. The script still runs `npm install playwright` in a temp dir on each run |
| Vercel CLI | 59.16.0 | global npm, symlinked into `~/.local/bin` | Deploy. Not logged in |
| python-pptx | 1.0.2 | user site-packages, system Python 3.9 | PPTX conversion |

## Rules for use in CreativeEngine

- **Deploy is a publish action.** Never run `scripts/deploy.sh` without explicit user confirmation for that deck. Client work must not go to a public Vercel URL by default. Prefer a private Artifact for sharing, and make public deployment the user's decision.
- **Installs need confirmation.** The PDF export downloads Playwright and Chromium, PPTX conversion needs `python-pptx`, and deploy may install the Vercel CLI globally.
- **PDF export needs an absolute output path.** Upstream bug: `export-pdf.sh` changes into its temp dir before writing, so a relative output path such as `deck.pdf` writes the PDF into the temp dir, which is then deleted. The script still reports success. Pass an absolute output path, or omit it; the default is derived from the absolute input path. Found in testing 2026-09-14; the vendored script is unpatched.
- **Where files go.** The skill writes previews to `.frontend-slides/slide-previews/` in the current directory. In client work, write previews and decks inside `projects/<client>/<project>/`, not at the repo root. The skill deletes that preview folder on delivery.
- **Phase 1 questions.** When a normalized brief or work packet already answers purpose, audience, length or density, use it and do not re-ask.

## Fit notes for DesignChamp

- **Art direction comes from `shared/frameworks/editorial-presentation.md`** (added 2026-10-03). Before Phase 2 style discovery on pitch, credentials or case-study decks, produce that framework's direction output (§12): reference board, slide behaviours, chapter lines, hero moments. Of the three previews, at least the wildcard comes from that direction, not a preset. Run its final check (§13) before delivery.

- It serves the slideshow and presentation format in `format-prototyping` (`references/slideshow.md`): pitch decks, credentials, concept presentations and client-facing work in JUDGE. It builds prototypes, not production code, which fits CreativeEngine's build intent.
- **Style library beyond decks.** `DesignChamp/knowledge/presentation-style-library.md` indexes the presets and bold systems as a visual reference library for DesignChamp's work in any format (user request 2026-09-14).
- **Presets and templates are methods, not taste.** Its three-preview discovery is useful. For brand or campaign work, though, the look comes from the brief, the brand and the idea, not from `STYLE_PRESETS.md` or the template pack. Use a template only when it truly fits. Use the wildcard slot for a direction designed from the concept. Principles 5, 6, 10 and 11 apply: do not let a polished template disguise a weak idea.
- **Its own anti-generic-AI stance** (no Inter or purple gradients, distinctive type) matches CreativeEngine principle 10. Its phrase lists are still house style, not CreativeEngine judgment.
- **Overlaps:** `anthropic-skills:pptx` (native PowerPoint), the `design` canvas (hand-editable layouts) and `figma-use-slides` (Figma Slides). Use frontend-slides when the output should be an animated HTML deck.
- **Interface motion vs. story motion.** Its `animation-patterns.md` is reveal and transition motion for decks. Storytelling motion in ad formats belongs to `shared/frameworks/animation-craft.md` (planned).
