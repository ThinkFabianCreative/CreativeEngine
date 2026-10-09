# ad-library-mcp (MCP server)

- **Source:** `at-dan/ad-library-mcp`, reviewed commit `2da03c1` (2026-04-16), v0.1.0, MIT.
- **Installed:** 2026-10-08, outside the repo at `~/Documents/AI_Traffik_Projects/tools/ad-library-mcp`. Registered at user scope as HTTP MCP `ad-library` → `http://127.0.0.1:3002/mcp`. The server must be running (`npm start` in that folder).
- **Owner:** DesignChamp (reference research). Any role may use it under this record; BriefMachine for competitive context.

## What it does

Searches what competitors are running in paid media now: Meta Ad Library (search, ad detail), Google Ads Transparency Center (search, ad detail), Instagram Reels (search, profile, transcript), cross-platform company lookup. Optional `analyze-creatives` sends ad media URLs to Gemini. README mentions TikTok; no TikTok code exists.

## Review findings

- No shell execution, `eval`, or file reads/writes. No install scripts in the dependency tree (installed with `--ignore-scripts` anyway). Mainstream dependencies.
- Outbound calls only to `api.scrapecreators.com` and, if enabled, Google Gemini.
- No auth and permissive CORS by design. **`HOST` must stay `127.0.0.1`** in `.env`; the upstream default `0.0.0.0` exposes the paid key's credits to the network.
- Requires a paid ScrapeCreators key; Gemini key optional. Keys live only in the tool's `.env`, never in this repo.

## Rules of use

- Complements `ad-reference` (award-level precedents); this is live market evidence. Use it for "what is the category actually running", not for ideas.
- Queries leave the machine. Search competitor brands and public terms only; never put client-confidential brief content in a query or analysis prompt.
- Results are PROJECT-LEVEL evidence for the current client, filed in that project. Never reused for another client (CLAUDE.md isolation).
- Data comes via a scraper: internal reference and pitch work only, links and our own analysis, no copies of competitor ads in deliverables.
- Each call spends credits; batch searches deliberately.
