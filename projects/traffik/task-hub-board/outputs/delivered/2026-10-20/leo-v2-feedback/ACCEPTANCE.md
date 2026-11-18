# v2 acceptance checks

Each batch is done when every check passes, in light and dark themes, on real Hub data. Specs: `leo-v2-handoff_READ-FIRST_2026-10-20.md` and `supporting/designchamp-pass_leo-mockup-v2_2026-10-20.md` (§ numbers below refer to it).

## Batch 1: colour, header, cards, type

### Colour roles (§3.1)
- [ ] Red appears only for problems: overdue dates, blocked / on hold markers, problem counts above zero
- [ ] Primary button is ink `#14151A` with white text (light) and `#F2F2F5` with ink text (dark). At most one per screen
- [ ] Cards have no client-coloured fill or border; the client shows as coloured text on the name only
- [ ] Card surface is one step lighter than the page in dark theme, with a neutral 1px border
- [ ] Board columns are neutral; status shows as a small dot before the column name
- [ ] Today's column uses a neutral lighter fill, not pink or red

### Header band (§3.3)
- [ ] The seven count tiles and the six chips are gone from Weekly, Day, Calendar and Status
- [ ] One band below the view switcher shows four counts: Overdue · On hold · Needs someone · Needs a date
- [ ] Each count is a filter; counts at zero are hidden
- [ ] Header is about 96px tall at 1440px wide (was about 330px)
- [ ] Total, Active, Due this week and With the client appear on Executive only

### Cards (§3.2)
- [ ] Every card has at most four rows: client · title · parent (Weekly and Day only) · due, status, assignee
- [ ] One badge at most (priority: Blocked → Overdue → High)
- [ ] Overdue shows as red due-date text ("Due Oct 12 · 1d late"), not a second chip
- [ ] Status chip is omitted on the Status board (the column says it)
- [ ] Age shows only after 3 days in a stage, as a visible label "7d in stage" (not tooltip-only); amber only when it threatens the date

### Icons
- [ ] One set: Lucide, stroke 1.75, 16px in UI and 20px in nav, `currentColor`
- [ ] Decorative icons are `aria-hidden` beside a text label; icon-only buttons have an `aria-label` and a tooltip
- [ ] No hand-drawn inline icons remain except the Traffik logo

### Type
- [ ] Page title 28px; headings 14/600; card title 15/500; body 14; meta 12/500; client 12/600 sentence case
- [ ] No uppercase letter-spaced text under 12px
- [ ] Dates, counts and hours use tabular figures
- [ ] At 375px, 720px (≈200% zoom) and 1440px, at least one row of cards is visible without scrolling
- [ ] On phones the header band is one "4 issues" button that opens the list; no tile is clipped mid-label
- [ ] With every count at zero, the band shows one quiet line instead of empty space
- [ ] axe (WCAG 2.2 AA) shows 0 violations on Weekly, Status and Home, both themes; text on cards checked by hand at ≥ 4.5:1

## Batch 2: role defaults and personal settings

- [ ] An admin sets a default view and scope per role: makers Mine + Weekly; creative leads My team + Status; PMs Everyone + Status; leadership Executive
- [ ] A new user opens on their role default with no setup
- [ ] Executive is hidden from the nav for roles that don't use it
- [ ] Settings (from the avatar menu) save to the user profile and follow the user to another browser
- [ ] Settings: Theme (System · Light · Dark), Text size (Default · Large), Density (Comfortable · Compact), Opens on, Default scope, Motion (System · Reduced), Show weekends, Preferred team, Notifications
- [ ] Theme and text size apply before first paint (no flash on reload)
- [ ] Large text and Compact density don't break the board at 1280px wide or at 200% zoom
- [ ] "Viewing as" still works for admins
- [ ] Mine with nothing assigned says so and offers the team view; a user with no role falls back to My team
- [ ] If saving to the profile fails, the choice still applies on this device and the user is told

## Batch 3: task pop-up and Quality Control

- [ ] The pop-up shows one status (the project's) and the current step as text; the step Status select and the "Project status" block are gone
- [ ] People are assigned by role: Account manager (one), Creative lead, Maker, Reviewer. Same rows as the full task page
- [ ] The reviewer can't be the maker
- [ ] The 11-person chip wall is replaced by a searchable picker per role
- [ ] Cards and the pop-up show QC progress ("QC 3/5")
- [ ] Moving work to With client with QC under 5/5 asks which items are open and requires a one-line reason; Cancel leaves the card where it was
- [ ] The reason, who gave it and when appear in the task's activity
- [ ] The card shows "QC 3/5 · sent early" until all five are done
- [ ] Executive shows a count of work sent with QC open, per account
- [ ] The pop-up is keyboard-usable: focus moves into it, Escape closes it, focus returns to the card
- [ ] Cancel or Escape on the QC prompt puts the card back in its column (also after a drag) and returns focus to it
- [ ] Send stays disabled until a reason is typed, and says why
- [ ] Picking the maker as reviewer is blocked with a plain message
- [ ] Every new string matches `COPY.md`, including the screen-reader versions
- [ ] Keyboard move with `[` `]` still announces the change
- [ ] Every move (drag or keyboard) shows a toast "Moved to Intake · Undo" for 5 seconds; Undo restores the column and returns focus to the card
- [ ] New prompts (QC reason, role picker, settings) reuse the New Task error pattern: message under the field, focus to the first problem

## Outcome checks (with people, after Batch 2 and Batch 3)

These say whether the changes cut load. Details in the READ-FIRST page.

- [ ] **First useful click:** one maker, one CD, one PM each reach real work in under 10 seconds from load, without changing scope or filters
- [ ] **Five-second glance:** shown Weekly for five seconds, people name the overdue and on-hold items
- [ ] **Status agreement:** three people give the same stage from the task pop-up alone
