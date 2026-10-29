# HyperFrames

HeyGen's HTML-to-video renderer: titles, lower thirds, kinetic type, charts, maps, captions and overlays, rendered frame by frame.

| Skill | Source | Installed | Runs code |
|---|---|---|---|
| `hyperframes` | `heygen-com/hyperframes` (Apache-2.0, ~74K stars), commit `8e63faf` | `~/.agents/skills/hyperframes/`, symlinked for Claude Code (global) | Yes: the `hyperframes` CLI via `npx` (downloaded from npm), ffmpeg/ffprobe, headless Chrome |

| | |
|---|---|
| Owner | DesignChamp |
| Status | Approved by the user 2026-10-28 after review |
| Invocation | Automatic for film motion graphics; DesignChamp owns use |
| Local changes | None. Installed copy verified identical to the reviewed copy |

## Review (2026-10-28)

- `hyperframes-animation`, the name listed on skills.sh, no longer exists in the repo; animation lives in `hyperframes` (`references/motion.md`).
- Network: `scripts/bake-basemap.mjs` fetches map tiles (Esri, CARTO) and MapLibre/topojson from jsDelivr. `scripts/locate.mjs` posts an image to Google Gemini only if `GEMINI_API_KEY` is set (it is not).
- Credentials: none read besides that optional key. No destructive commands. No instructions to skip checks or override other rules.
- The CLI sends anonymous usage telemetry; `npx hyperframes telemetry` manages it.
- `npx hyperframes init` installs `hyperframes-cli`, `hyperframes-registry` and `media-use` if missing. Those three are **not reviewed**: run `init` with `--skip-skills` (or `HYPERFRAMES_SKIP_SKILLS=1`) until they are.
- HeyGen paid items (voices, avatars, catalog music) need a HeyGen sign-in.
- Overlap: `remotion-best-practices`. HyperFrames sits beside Remotion for film and documentary motion graphics; it does not replace it.

## Rules on CreativeEngine work

1. **No Whisper.** Never use `npx hyperframes transcribe` or a Whisper path in `media-use` on a project where the user has ruled Whisper out (the Nigeria documentary). Build captions from the project's approved transcripts.
2. **Maps protect people.** Never render a basemap zoomed to a sensitive site (camps, shelters, routes). Country or region scale only, with source credit on screen, after the project's safety review.
3. **No paid HeyGen items** (voice, avatar, music) without the user's approval and cost.
4. **Concept first.** Motion carries a decided idea (`barry-concept-art-direction.md`, `narrative-craft.md`); the planned `animation-craft.md` will govern motion judgment once it exists.
5. Generated or rendered work follows the project's evidence rules: every on-screen fact or statistic carries its source.
