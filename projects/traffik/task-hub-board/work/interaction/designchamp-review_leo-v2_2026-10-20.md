# DesignChamp review: Leo's mockup v2

```
CLIENT:      Traffik (internal; mockup names real clients)
PROJECT:     Task Hub board
SPECIALTIES: Interaction design leading; Marketing design supporting
EVIDENCE:    Working mockup in headless Chrome at 1440×900, 720×900 and 375×812: keyboard, focus,
             reduced motion, axe-core (light and dark), New Task form errors, move feedback,
             standup, Home, Weekly, Day, Calendar, Status, Executive. 2026-10-20
BRIEF:       None normalized. Requirements from the Oct 12 v1 spec and the culture-reset workflow.
             Central idea "a calm board where problems stand out" is an assumption
SEVERITY:    Major · Minor · Opportunity · Keep. Nothing found blocks the primary task
```

## Assessment

**Works:** side nav, stage board, a guided standup better than ours; strong keyboard support (skip link, visible focus, `[` `]` moves announced, focus returns after the dialog); New Task errors inline with focus to the first problem; plain, calm helper copy; 0 axe violations in both themes.

**Most threatens the task:** every seat opens on agency-wide numbers before any work. 13 counts above the first card on desktop; at 200% zoom and on a phone, no work is visible without scrolling.

**Most threatens the idea:** colour has no rules. Client tints, status tints and severity red compete, so nothing reads as "the problem."

## Findings

| ID | Sev | Location | Evidence | Impact | Principle | Change | Verify |
|---|---|---|---|---|---|---|---|
| M1 | Major | Scope switch, all Workspace views, Home | As Matt (designer) opens on Everyone, 34 items; options are only My team / Everyone | Makers re-filter every time | Manageable choices; recognition over recall | Add Mine; role defaults (makers Mine, CDs My team, PMs Everyone, leadership Executive); profile override | Sign in per role; time to first useful click |
| M2 | Major | 7 tiles + 6 chips on Weekly, Day, Calendar, Status | ~330px desktop; fills first screen at 720px; at 375px tiles clipped ("IN THE"), chips five rows, first card at 831px of 812; "In the queue" 14 vs 1 | Orientation slowed; work hidden on phone / zoom; conflicting numbers | Progressive disclosure; hierarchy | One band below the switcher, four problem counts as filters, zeros hidden, totals to Executive; phones: one "4 issues" button | A row of cards visible at 375 / 720 / 1440; counts match filters |
| M3 | Major | Weekly card fills, Status column fills, New Task, Today | CSUN dark red beside red Overdue; New Task only filled red at rest; Today pink | Problems don't stand out (visual hypothesis) | Consistent visual relationships; brand expression serving the idea | Red only for problems; neutral primary; client as text colour; neutral columns with status dot; neutral Today | Five-second glance test |
| M4 | Major | Task dialog (steps) | Header chip, Status select and Project status disagree (In the queue vs Quality Control) | Users must work out which status is real; wrong moves | Recognition over recall; feedback | One status (project's), step shown as "Current step"; one card per task | Three users name the same stage from the dialog |
| M5 | Major | Dialog vs Open full page | 11 equal people chips; Ownership roles and QC checklist only on the full page | CDs open two layers per review; PMs assign without roles | Progressive disclosure that keeps decision information | Ownership rows and "QC 3/5" in the dialog; searchable picker per role; QC on card | Time a CD clearing three review cards |
| M6 | Major | Weekly and Status cards | Up to six elements; 11px tracked caps client; late card stacks two chips; 18 type size/weight combinations | Slow scanning; title doesn't lead | Hierarchy; grouping | Four rows, one badge, lateness on the due date; five-step type scale | Time to find a named task; type census ≤ 5 levels |
| m1 | Minor | Board moves | Only a screen-reader message; nothing visible; no undo | Cards dropped off screen vanish; no recovery | Feedback; error recovery | Toast "Moved to Intake · Undo", 5 s | Drag off screen, then Undo |
| m2 | Minor | Status card age box | Yellow 1d–8d on every card; meaning only in a hover tooltip | Noise; unexplained on touch | Clear labels | After 3 days only, grey, "7d in stage"; amber when it threatens the date | Count on a real board; test on touch |
| m3 | Minor | Status columns | "In the queue" before Intake; no Feedback; On hold off screen at 1440 | Reads backwards; stuck work hardest to see | Consistent relationships | v1 order; On hold as a top lane | On hold visible at 1280 without scrolling |
| m4 | Minor | Home | "Nothing on your list" while 7 open, 5 due this week | Misleading empty state | Guiding empty states | Show next three by date | Home as someone with nothing due today |
| m5 | Minor | Standup | 12 steps, opens on Internal review; empty steps counted; Intake ~10 items × 3 buttons | Longer meetings; blockers late | Manageable choices | Start with On hold / blocked; skip empty steps; Intake shows only items without a brief | Time a real standup |
| m6 | Minor | Nav | Executive visible to makers | Noise | Manageable choices | Show by role | View as a maker |
| m7 | Minor | Filter popovers | 17 targets under 24px, mostly 18px checkboxes | Hard on touch; possible WCAG 2.2 2.5.8 issue | Accessible targets | Whole row, label included, is the target | Measure spacing by hand |
| m8 | Minor | All icons | ~15 hand-drawn inline SVGs; strokes 1.4 / 1.6 / 1.75; grids 12 / 16 / 24 | Inconsistent visual weight; costly to extend | Consistent visual relationships | Lucide, stroke 1.75, 16px UI / 20px nav, `currentColor` | Icon census: one set, one stroke |
| O1 | Opp. | Column foot | Small items need the full form | PM effort | Familiar controls (Trello) | "+ Add a card", title only, lands in Intake | PM creates three small tasks, timed |
| O2 | Opp. | Global | 13 clients, dozens of cards | Filtering to find one thing | Recognition over recall | `⌘K` quick find | Time to open a named task |
| O3 | Opp. | Copy | Leo's helper lines tie behaviour and words well | — | Visual / verbal relationship | WordSmither writes the new messages in that voice | Copy review |
| K1 | Keep | New Task form | Inline errors, required marked, focus to first error | — | Error recovery | Reuse for every new prompt | — |

## Untested

No users observed (all role claims are hypotheses); no screen-reader pass; Tab past the dialog's last control leaves the dialog (native modal, likely browser chrome; check by hand); 22 contrast cases unresolved by axe; dark card separation by eye; Resourcing, Clients, Executive drill-downs not reviewed in depth; loading states can't be tested in a static mockup; touch drag not tried on a real phone.
