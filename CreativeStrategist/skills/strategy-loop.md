# strategy-loop

| | |
|---|---|
| Source | In-house, built 2026-10-26 |
| Owner | CreativeStrategist |
| Status | Built at the user's request 2026-10-26, alongside the CreativeStrategist role |
| Installed | `.claude/skills/strategy-loop/` |
| Scope | Develop, review and refine strategic assets through a loop: creative-strategist drafts and red-teams; creative-researcher audits evidence; creative-engine-director runs the strategy gate; word-smither and design-champ run the show test; max three rounds, then the user decides |

## Use

- The thinking is in `shared/frameworks/brand-strategy.md` and `creative-effectiveness.md`. The skill must not grow its own version of them.
- Origin: the EWU graduate pilot, where every real fix came from a loop (a cherry-picked swap test, a synthesis presented as a quote, an unshowable line, a false location claim). The red team checklist encodes those failures.
- The show test is not EXPLORE. Agents judge whether the strategy gives them material; they don't produce concepts.
- No scripts, no network calls of its own, no credentials. Agents it calls follow their own tool records (for example, ad-library credits need approval).
