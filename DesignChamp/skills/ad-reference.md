# ad-reference

| | |
|---|---|
| Source | CreativeEngine (in-house) |
| Owner | DesignChamp (reference libraries); used equally by WordSmither and CreativeDirector |
| Status | Built at the user's request 2026-09-24 ("build it and wire it in" for Ads of the World). First live run: UW T2 done-before check |
| Installed | `.claude/skills/ad-reference/` (SKILL.md + `references/adsoftheworld.md`) |
| Index | `shared/knowledge/ad-reference/` (README, index, entries) |
| Scope | Find precedents, harvest reference ads, and check whether a concept has been done, using Ads of the World and our own index |

## Review (2026-09-24)

- **Source terms.** Ads of the World is covered by the Clio terms (`clios.com/terms-use`): personal, non-commercial, transitory viewing only; no commercial use or public display; no mirroring. The skill therefore stores links, bibliographic facts and our own analysis only, with the ad's own headline quoted when 15 words or fewer. No image downloads, no copied descriptions or body copy.
- **robots.txt.** Paginated listings (`/*?page=`), `/tags`, `/watchlist`, `/bookmarked`, `/follows`, `/settings` are disallowed; the skill never requests them and narrows by keyword and filter instead.
- **Access.** Public; no login, credentials or paid membership. WebFetch reads search and campaign pages; the built-in browser views ad images (Claude in Chrome only if the user asks).
- **Executables.** None. Markdown only.
- **Isolation.** The index is shared method and holds no client facts. Done-before reports and job-specific reference picks live in the client's project folder.
- **Overlap.** Complements `DesignChamp/knowledge/presentation-style-library.md` and `brand-design-md/` (visual systems, not ads) and `WordSmither/knowledge/writers-room.md` (lenses; reference shelves list famous work by title). No installed skill covers ad archives.

## Use

- **WordSmither and DesignChamp:** Find mode in EXPLORE and DEVELOP for precedents by mechanism; Harvest when good work turns up.
- **CreativeDirector:** Done-before mode before client presentation; informs the originality score and the defense (`selling-the-work.md`).
- References are stimulus and precedent, never evidence about a client.
