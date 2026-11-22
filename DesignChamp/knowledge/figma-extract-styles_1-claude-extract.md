# Extract Website Styles, part 1: Claude extracts

Goal: turn a website URL into a clean token handoff that Figma's in-platform agent can build from. Accuracy over completeness: a short, correct palette beats a long, noisy one.

This is the half that needs a shell and the web. Part 2 (`figma-extract-styles_2-figma-build.md`) runs inside Figma and builds the variables, text styles and documentation board from this handoff. Split from Andres's Extract Website Styles example (2026-11-22); method notes in `figma-skill-authoring.md`.

## Before starting

- Needs: the URL, and the client and project this is for (or "internal reference").
- Save to `projects/<client>/<project>/raw/<date>_<domain>_styles/`. The page HTML, CSS and assets are raw sources and are never edited. The handoff goes beside them as `tokens.json` + `handoff.md`.
- Third-party sites are internal reference only. Logos and imagery are filed for study, never reused or redrawn in client work.
- Stop and tell the user if the page is behind a login, is mostly rendered by JavaScript (almost no CSS in the HTML), or blocks fetching.

## Step 1: Fetch

1. `curl -sL <URL>` into the raw folder.
2. Collect `<link rel="stylesheet">` hrefs and inline `<style>` blocks. Resolve relative URLs against the page's base URL. Fetch each stylesheet.
3. Look for theme or token objects in inline JSON or scripts.
4. Log every failed fetch (403, timeout) for the report. Skip it and carry on.

## Step 2: Extract

**Colors.** Hex, rgb(a), hsl(a) and CSS custom properties. Normalize to `#RRGGBB` (keep alpha separately if it matters). Group as brand, neutral (light to dark), accent, semantic. Group by where a color is used (buttons, links, nav, hero, body, borders), not by guessing from its hue.
- CSS custom properties are authoritative when present.
- On Tailwind or Bootstrap sites, keep the site's own overrides and drop framework defaults it doesn't use.
- More than ~30 colors: keep the most used, note the cut.
- Agency, portfolio and multi-brand sites: colors on case-study or client pages (often their own stylesheet) belong to those clients. Leave them out and note it. Same for CMS preset colors (WordPress `.has-*` classes).

**Typography.** font-family per role (headings, body, mono), sizes in px (check the `html` font-size first: `62.5%` means 1rem = 10px; otherwise base 16; convert vw at 1920 and say so), weights, line-height, letter-spacing. Map to Display, H1–H6, Body, Body Small, Caption, Button, Label. Note where a level was inferred rather than found.

**Fonts.** Name each family and where it comes from (Google Fonts, Adobe Fonts, self-hosted). Name a Figma-available substitute for any that may be missing.

**Assets.** Up to ~20: logos first (header images or SVGs with "logo", favicon, apple-touch-icon, og:image), then UI icons, then hero imagery. Save each with its category.

## Step 3: Write the handoff

`tokens.json`:

```json
{
  "source": { "url": "", "domain": "", "fetched": "YYYY-MM-DD", "scope": "internal reference" },
  "colors": {
    "brand":    [{ "name": "color/brand/primary", "hex": "#000000", "usedOn": "buttons, links" }],
    "neutral":  [{ "name": "color/neutral/50", "hex": "#FAFAFA" }],
    "accent":   [],
    "semantic": [{ "name": "color/semantic/success", "hex": null }]
  },
  "type": {
    "families": [{ "family": "", "role": "headings", "source": "Google Fonts", "weights": [400, 700], "substitute": null }],
    "levels":   [{ "style": "Heading 1", "family": "", "weight": 700, "size": 48, "lineHeight": 56, "letterSpacing": 0, "inferred": false }]
  },
  "assets": [{ "file": "logo-primary.svg", "category": "logo", "label": "Primary Logo" }],
  "notes": { "trimmed": [], "failed": [], "inferred": [] }
}
```

`null` means not found. Part 2 shows those as "Not found", never as an invented value.

`handoff.md`: the palette and type scale in plain tables, what was trimmed, inferred or failed, and the line to paste into Figma: "Run Extract Website Styles part 2 with this token list" followed by the JSON.

## Step 4: Hand over

Show the user the palette and type scale before anything goes to Figma. Then either:
- **Figma's agent builds it.** The user pastes `handoff.md` into Figma with part 2, and uploads the assets from the raw folder.
- **Claude builds it.** Load `figma-use`, `create_session` on the target file, `upload_assets` for the assets, then follow part 2 with `use_figma` in small calls (variables, then styles, then the board), returning node IDs and re-fetching by ID between calls.

## Report

URL, color count by group, type levels and families (with substitutes), asset count by category, the raw folder path, and everything that failed, was trimmed or was inferred.
