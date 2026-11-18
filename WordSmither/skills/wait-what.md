# wait-what

| | |
|---|---|
| Source | `mattpocock/skills` (GitHub), `skills/productivity/wait-what` |
| Owner | WordSmither (plain-language clarity); usable by any role in any session |
| Status | Approved by the user 2026-10-03 after review |
| Installed | `.claude/skills/wait-what/` (unchanged from upstream) |
| Scope | Session utility. The user types `/wait-what` when the last message did not land; Claude re-pitches it with context, in simple English |

## Review (2026-10-03)

- One prompt in `SKILL.md`, plus `agents/openai.yaml` (display metadata for another tool). No scripts, credentials, external calls or destructive commands.
- Upstream already sets `disable-model-invocation: true`: manual only.
- No overlap: `humanizer` removes AI tells from prose; this re-explains where the work has got to.

## Use

- The skill asks for terms from `GLOSSARY.md`. CreativeEngine has none. Use CreativeEngine's own vocabulary from `CLAUDE.md` instead (EXPLORE / DEVELOP / JUDGE, the four verdicts, normalized brief, work packet, source scope, the role names).
- ASD-STE100 is for the re-pitch only. It is not a house style for copy or client material.
