# marketing-ideas

| | |
|---|---|
| Source | `coreyhaines31/marketingskills` (GitHub), skill `marketing-ideas` v2.0.1 |
| Owner | BriefMachine |
| Status | Approved by the user 2026-10-03 after review (option A: manual only) |
| Installed | `.claude/skills/marketing-ideas/` |
| Local change | Added `disable-model-invocation: true` to the frontmatter. Runs only when someone types `/marketing-ideas` |
| Scope | Channel and tactic options: a 139-item growth-tactic catalog with a guerrilla-marketing deep dive |

## Review (2026-10-03)

- Markdown and JSON only (`SKILL.md`, `references/`, `evals/evals.json`). No scripts, credentials, external calls or destructive commands.
- Reads `.agents/product-marketing.md` or `.claude/product-marketing.md` if present. Neither exists in CreativeEngine; do not create one. Client context comes from the client workspace and the normalized brief.
- Upstream description triggers on broad phrases ("brainstorm marketing", "what else can I try"), so it would have hijacked EXPLORE. Hence manual only.
- Points to sibling skills (`marketing-plan`, `programmatic-seo`, `competitors`, `emails`, `free-tools`, `referrals`) that are not installed. Ignore those references.

## Use

- **Tactics, not ideas.** Use it to widen channel and tactic options when BriefMachine or CreativeDirector asks "where and how could this show up?" Never as a source of concepts, and never as a substitute for WordSmither's or DesignChamp's exploration.
- **SaaS assumption.** The catalog, stages and budgets are written for SaaS and software. On any other client, treat every item as a prompt to translate, not a recommendation. CLAUDE.md's industry-agnostic rule wins.
- **Output stays labeled.** Suggestions are hypotheses for the brief or a work packet. Its "expected outcome" lines are unsourced. Never present them as evidence or benchmarks.
- `references/guerrilla-marketing.md` is useful alongside guerrilla / stunt / brand-act routing. Its case library is illustration, not proof.
