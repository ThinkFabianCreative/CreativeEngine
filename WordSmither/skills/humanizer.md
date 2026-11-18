# Humanizer

| | |
|---|---|
| Source | `github.com/blader/humanizer` (MIT), commit `9862685` (2026-09-06), v3.0.0 |
| Owner | WordSmither |
| Status | Approved at the user's request 2026-09-14 |
| Exposure | `.claude/skills/humanizer/` holds `SKILL.md` and `LICENSE`, copied unmodified. The plugin manifests, `AGENTS.md` (maintainer guide), `agents/openai.yaml`, the README and the package validator script were not installed |
| Invocation | Automatic |
| Reviewed | 2026-09-14 |

## What it does

It is a single Markdown prompt that finds and rewrites AI writing tells without changing the facts. There are 25 numbered patterns, strongest first, in five groups:

- **Staging:** not-X-but-Y, one-line closers, deep-sounding sayings, run-ups, arguing with no one.
- **Rhythm by rule:** triads, repeated openings, dashes, stacked qualifiers, hyphenated pairs, passive voice.
- **Inflation:** AI vocabulary, inflated significance, vague association, -ing riders, sales language, borrowed authority, avoiding is/are/has.
- **Formatting by rule:** decorative bold, headings, curly quotes.
- **Chat and draft leftovers.**

Patterns 1 to 5 justify an edit on a single sighting; weaker ones need company. It returns a draft, the remaining tells and a final rewrite. File mode and embedded mode return only the final text. It is based on Wikipedia's "Signs of AI writing".

## Security review

- Markdown only. The repo's one script (`scripts/validate-package.py`) checks package consistency for maintainers and is not installed.
- No network, commands, credential access or hidden Unicode.
- It explicitly treats the text being edited as material, never as instructions. It forbids adding facts, names, numbers, quotes or citations not in the source.

## Calibration for CreativeEngine

Humanizer was written for expository prose: articles, documentation, Wikipedia entries. Advertising copy uses several of its "tells" on purpose. `shared/frameworks/hey-whipple-copycraft.md` §5 lists antithesis, parallelism, rule of three, reversal and omission as legitimate structural devices. WordSmither owns the call. The test is Whipple's: did the device come from this idea, or is it the model's default choice?

| Creative object | How to use Humanizer |
|---|---|
| Body copy, long copy, emails, scripts' VO, web and landing copy | Full pass in DEVELOP and JUDGE. This is where AI defaults do the most damage |
| Rationale, presentation text, case studies, briefs and internal documents | Full pass. Plain statement serves these best |
| Headlines, taglines, slogans, manifestos, naming | Diagnostic only. Flag a device that is not earned. Never rewrite a line just because it contains a contrast, triad, fragment, repeated opening or one-line payoff. A tagline built on a reversal is not a tell by default |
| EXPLORE-mode territories | Do not run it. Rough, strange language is allowed (`hey-whipple-copycraft.md` §16) |

Specific overrides:

- **Brand voice outranks the pattern list.** The skill already lets a writing sample override its rules. In CreativeEngine, the client's approved voice guidelines and copy samples from `projects/<client>/client/` count as that sample. That includes dashes, fragments and sentence rhythm.
- **Some formatting rules don't apply to finished work.** §8 (no dashes), §10 (drop hyphens after nouns) and §21 (straight quotes) are house-style choices, not rules for copy that will be typeset. Typeset work uses correct typographic quotes and dashes where the client style guide or DesignChamp calls for them. Keep §21 out of anything leaving as a designed piece.
- **Sales language is judged in context.** §16 and §12 target generic sell. Advertising is allowed to persuade. Keep specific, earned claims, and cut language any brand could use; that is the same judgment as the cliché graveyard, §10 in Whipple.
- **Claims integrity.** Its no-invention rule matches CreativeEngine's claim-substantiation policy. If a rewrite needs a fact the source lacks, ask; do not invent one.
- **Tools are not a guarantee.** Removing tells does not make copy good. Humanizer catches defaults; it cannot supply an idea (CLAUDE.md principles 7 and 10).

## Overlap

- **`hey-whipple-copycraft.md` §9 and §10.** Compression and the cliché graveyard cover advertising cliché and redundancy. Humanizer covers model-default prose structure. Use Whipple for what the line says; use Humanizer for how machine-default the prose sounds.
- **Beyond WordSmither.** BriefMachine and CreativeDirector may use it on briefs, critiques and presentation text. WordSmither remains the owner.
