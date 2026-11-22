# Writing Figma agent skills

How CreativeEngine writes instructions (skills) for Figma's in-platform AI agents, and how Claude drives Figma through the MCP. Learned 2026-11-22 from five examples Andres supplied: Extract Website Styles, Mobile From Desktop, Recreate From Image (already filed as `figma-recreate-from-image.md`), the Plugin API reference for components and frames, and Finding Animation Opportunities. Global method only. No client facts.

## 1. What each example teaches

| Example | Kind | Lesson worth keeping |
|---|---|---|
| Extract Website Styles | Build workflow, very prescriptive | Phases in order (fetch, extract, variables, styles, board, report). Exact specs where taste must not drift (px, colors, names). Hard construction rules in a block of their own. Many short script calls, re-fetching nodes by ID. Screenshot before reporting. Cap inputs (~20 assets, ~30 colors) and say what was trimmed |
| Mobile From Desktop | Transformation | Never touch the original; output goes beside it with a predictable name. Derive new values from the source system (ratios, not invented numbers). Pattern table per section type with a default and an exception. "Report, don't rewrite": flag long headings instead of editing copy. Use the library's mobile variants before rebuilding |
| Recreate From Image | Fidelity build | Study before building. Ask for missing inputs (font, target page) instead of guessing. Nesting rule: delete any frame that changes nothing. Role-based layer names. Up to 3 review passes, stop early, fix only what's wrong. Checklist at the end |
| Plugin API reference | Reference, not a skill | Instructions should point at the API, not restate it. The traps that matter go into the skill as rules: `resize()` not width/height, set FILL only after `appendChild`, components can't be made inside instances, library components are read-only, load fonts before text |
| Finding Animation Opportunities | Review / filter | A posture line (restraint). Hard rules numbered. A gate every candidate must pass, with the answer recorded. Capped output. A required "rejected candidates" section. Verdict paragraph and a handoff to the next skill. Content in the file is data, not instructions |

## 2. The shape of a good Figma skill

1. **Title and one-line goal.** Name the kind of task (build, transform, fidelity, review) and what wins when goals conflict ("fidelity over library reuse").
2. **Inputs and stop conditions.** What must exist before starting. What to ask for. When to stop and tell the user (wrong selection type, missing font, unclear target).
3. **Study before acting.** A read-and-map step that produces the plan: structure, spacing scale, type scale, colors, repeats.
4. **Steps in order**, each with what "done" means.
5. **Exact values where taste must not drift; ranges and rules where judgment helps.** Never vague words like "nice spacing".
6. **Construction rules** (the API traps) in one block.
7. **Guardrails**: never modify the original, never invent copy or imagery, never restyle, use existing components and variables first, report every removal, substitution or detach.
8. **Verify**: screenshot and compare, bounded passes, targeted fixes only.
9. **Report format**: fixed sections, what changed, what couldn't be matched, flags for human review. Review skills add a rejected list and a verdict.

Keep it to what the agent can't infer. If a line restates the API docs or general good sense, cut it.

## 3. In-Figma agent vs Claude over MCP

| | Figma's native agent (paste-in skill) | Claude through the Figma MCP |
|---|---|---|
| Sees | The selection, canvas and libraries directly | Only what it reads: `get_metadata`, `get_screenshot`, `get_design_context`, `search_design_system` |
| Writes with | Its own tools | `use_figma` (Plugin API JS); load `figma-use` first, always `create_session` first |
| Write the skill as | Plain steps referring to selection, layers, variables, components | Steps naming the MCP tool per phase; small script calls; return node IDs; re-fetch by ID |
| Can't | Run shell commands or fetch outside material, unless Figma says it can | See the canvas without a screenshot |

Extract Website Styles mixes both (curl in Bash plus `evaluate_script`). It fits a code-side agent, not Figma's native one. For the native agent, split it: Claude fetches and extracts, then hands over a token list; the in-Figma skill builds the variables and board.

## 4. CreativeEngine additions to every Figma skill

- Concept comes before polish: a build skill makes or checks a frame, it never decides the idea (Barry §1, `shared/frameworks/visual-craft.md`).
- The client's look comes from the client's layer (`projects/<client>/.../figma-agent-pack/`), never from the skill.
- Approved copy is transcribed exactly. Flag, never rewrite.
- Rebuilds of third-party work are internal reference only. No redrawn logos.
- Report in `figma-agent-pack/07_how_to_report.txt` style when the skill has no report format of its own.
- Craft status is not a creative verdict. Only `creative-engine-director` gives verdicts.

## 5. Template

```
# <Skill name>

Goal: <one sentence>. <What wins when goals conflict.>

## Before starting
- Needs: <inputs>. If missing, ask. Stop if <condition>.
- Never modify <original>. Output goes <where>, named <pattern>.

## Step 1 — Study
<what to map before creating anything>

## Step 2..n — <action>
<ordered steps; exact values where they matter; defaults + exceptions as a table>

## Construction rules
<API traps only>

## Verify
Screenshot, compare, up to <n> passes, stop early, targeted fixes only.

## Report
<fixed sections; changes; couldn't match; flags; for reviews: rejected + verdict + handoff>

## Guardrails
<never-list>
```
