# Prompt for Claude (Leo's builder)

Copy everything below the line into Claude Code from the root of the Task Hub codebase. Put this folder where Claude can read it and replace `<FEEDBACK>` with its path.

---

You're helping me, Leo, apply design feedback to our in-house Task Hub. Andres, the creative director, reviewed my latest mockup with his design team and sent decisions, specs, design tokens, an icon library choice and acceptance checks. Build the changes **inside our existing app, on our real data, following its current architecture**. Don't port code from any reference file, and don't add frameworks. The only new dependency allowed is the Lucide icon set.

## Read first, in this order

1. `<FEEDBACK>/README.md`: overview, what changed since Oct 12, the three batches
2. `<FEEDBACK>/leo-v2-handoff_READ-FIRST_2026-10-20.md`: **decisions, assumptions and build order. It wins over every other document**, including the Oct 12 handoff
3. `<FEEDBACK>/ACCEPTANCE.md`: the checks that define "done", per batch, plus outcome checks with people
4. `<FEEDBACK>/references/tokens-v2.css`: colour roles, surfaces, type scale, spacing, icon sizes for light, dark and system
5. `<FEEDBACK>/references/REFERENCES.md`: icon rules (Lucide) and the patterns to follow
6. `<FEEDBACK>/supporting/designchamp-review_leo-v2_2026-10-20.md`: every finding with evidence and how to verify it
7. `<FEEDBACK>/supporting/designchamp-pass_leo-mockup-v2_2026-10-20.md`: visual specs (colour §3.1, card §3.2, header §3.3, pop-up §3.4)
8. `<FEEDBACK>/supporting/designchamp-interaction-pass_leo-v2_2026-10-20.md`: behaviour specs, **§4 states** (empty, error, recovery, success) for every new feature
9. `<FEEDBACK>/taskhub-mockup_v2_MARKUP.html`: my mockup with numbered notes (open in a browser; press M to toggle)
10. `<FEEDBACK>/COPY.md`: final copy for every new string, with screen-reader versions
11. `<FEEDBACK>/screenshots/`: marked-up views, the phone layout, and the New Task error pattern to reuse

The rest of `supporting/` is background.

## Replaced from the Oct 12 handoff

- **Red is not the primary colour.** Red is for problems only. Primary buttons are ink `#14151A` on light and off-white `#F2F2F5` on dark, one per screen.
- **Quality Control is advisory**, not a gate, with no ACD override. Moving work to With client under 5/5 asks for a one-line reason that's logged.
- **Icons:** Lucide replaces Feather (same family, maintained).

## Before writing any code

1. Find where the app defines colour variables, type sizes, icons, the Workspace header (count tiles and chips), card templates, the board columns, the task pop-up, the full task page (Ownership, QC), Settings and user/role data.
2. Map `tokens-v2.css` onto the existing variables. List anything that has no home.
3. Inventory the current inline SVG icons and map each to a Lucide name.
4. Propose a plan for **Batch 1 only**, listing every file you'll touch.
5. List anything in the specs that conflicts with how the app is built, with a suggested adjustment.

**Wait for my approval before changing anything.**

## Build order

**Batch 1: colour, header, cards, type, icons** (CSS and templates)
- Colour roles from `tokens-v2.css`: red only for problems; neutral primary; client as text colour on the name only; no card tints or coloured borders; neutral columns with a status dot; neutral Today.
- One header band below the view switcher: Overdue · On hold · Needs someone · Needs a date. Each count is a filter; zeros hidden; all-zero shows one quiet line. Totals move to Executive. **On phones, one "4 issues" button** that opens the list.
- One card layout: client · title · parent (Weekly and Day only) · due, status, assignee. One badge. Lateness on the due date. Age only after 3 days, as a visible "7d in stage" label.
- Five-step type scale; no uppercase letter-spaced text under 12px; tabular figures.
- Lucide icons everywhere except the Traffik logo.
- Board order: Intake, Ready, In progress, Internal review, Quality Control, With client, Feedback, Done; On hold as a lane across the top.

**Batch 2: role defaults and personal settings**
- Add a **Mine** scope. Admin sets defaults per role: makers Mine + Weekly, creative leads My team + Status, PMs Everyone + Status, leadership Executive. Hide Executive from roles that don't use it.
- Extend my existing Settings dialog. Save to the **user profile**, not the browser: Theme (System · Light · Dark), Text size, Density, Opens on, Default scope, Motion, Show weekends, Preferred team, Notifications. Apply theme and text size before first paint.
- States: empty Mine, no role, save failure (interaction pass §4).

**Batch 3: task pop-up, QC, feedback**
- Pop-up shows one status (the project's) and "Current step". Ownership rows from the full task page with a searchable picker per role; reviewer can't be the maker.
- "QC 3/5" on cards and in the pop-up. Moving to With client under 5/5 opens the reason prompt; Cancel or Escape puts the card back (also after a drag) and returns focus. Log reason, person and time; card shows "QC 3/5 · sent early".
- Every move shows a toast "Moved to <column> · Undo" for 5 seconds.
- New prompts reuse the New Task form's error pattern (message under the field, focus to the first problem).

## Copy

All interface copy for the new features is final in `<FEEDBACK>/COPY.md`: count labels, empty states, errors, the QC prompt, the move toast, the role picker, Settings, and the screen-reader versions. Use it exactly; `{braces}` are dynamic values. If a string doesn't fit the UI or a case isn't covered, ask me rather than writing new copy. Keep Leo's existing strings where COPY.md says to (Notifications).

## Constraints

- Don't break existing views, data, "Viewing as", or keyboard support (skip link, visible focus, `[` `]` moves with announcements, focus return after dialogs).
- Both themes: 0 axe violations (WCAG 2.2 AA), text ≥ 4.5:1, reduced motion respected, targets at least 24px or properly spaced.
- Check at 375px, 720px and 1440px wide.
- Don't remove information: totals go to Executive, parent lines stay on Weekly and Day, roles and QC already exist on the full page, so reuse them.
- Don't build anything outside the three batches.

## Work in small steps

After each batch: show me what changed, run its `ACCEPTANCE.md` checks in light and dark at the three widths, report pass or fail with evidence, list any string you couldn't place, and wait for my go-ahead before the next batch. Ask rather than guess about anything the specs don't settle.
