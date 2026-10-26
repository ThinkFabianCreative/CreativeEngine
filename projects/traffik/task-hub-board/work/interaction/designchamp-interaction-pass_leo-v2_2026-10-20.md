# DesignChamp: Interaction design pass on Leo's mockup v2

```
CLIENT:     Traffik (internal; mockup names real clients)
PROJECT:    Task Hub board
SPECIALTY:  Interaction design leads (dashboard and task flows). Marketing design supports
            (brand expression: colour roles, type), covered in designchamp-pass_leo-mockup-v2_2026-10-20.md
MODE:       JUDGE on the working mockup, DEVELOP for the three decisions
EVIDENCE:   Keyboard, focus, zoom and reduced-motion checks run on the working mockup in headless
            Chrome (1440×900 and 720×900), 2026-10-20. axe-core results in trello-gap-libraries-type
            §6. No users observed; role needs come from Andres and the culture-reset workflow
```

The first DesignChamp pass worked from screenshots and led with Marketing design. Under the updated role, this pass covers what that one couldn't: routes, states, keyboard and focus, and what's verified versus assumed.

## 1. Users and primary tasks

| Seat | Primary task on opening the Hub | Information needed at that decision | Outcome |
|---|---|---|---|
| Designer / maker | "What do I work on next?" | My items due today or in progress, anything blocked, the brief | Starts the right task |
| Creative Director | "What needs my review, and who's stuck?" | Internal review and QC queues for my team; blocked and at-risk people | Clears review, unblocks someone |
| PM / account | "What's at risk, and what's missing an owner or date?" | Overdue, on hold, needs someone, needs a date, across accounts | Assigns, dates or escalates |

*Source: Andres's direction and the culture-reset workflow. Hypothesis until watched with real users.*

## 2. Task routes today (verified on the mockup)

| Route | Steps today | Friction |
|---|---|---|
| Designer finds their next task | Workspace opens on Everyone → toggle My team's work (there's no Mine) → scan 7 tiles + 6 chips → find own cards among the team's | No "Mine" scope; counts come before the work |
| CD clears review | Status → scroll right to Internal review / QC → open card → quick dialog → Open full page to see Reviewer and QC | The roles and QC that decide the review are one level deeper than the dialog |
| PM fixes "Needs a date" | Click chip → filtered list → open card → set date in dialog | Works. Chip and tile duplicate each other first |
| Move a card by keyboard | Tab to card (36 tabs, or Skip to content then ~1) → `]` / `[` | **Works well.** Focus stays on the card, a live region announces "moved to Intake" |

## 3. Keyboard, focus and access (verified)

| Check | Result |
|---|---|
| Skip to content | ✅ Present; lands on the view switcher |
| Visible focus | ✅ 2px ring on cards, buttons, selects |
| Move card by keyboard | ✅ `[` `]`, focus kept, change announced |
| Enter opens task dialog | ✅ Modal; focus starts on the Status select |
| Escape closes dialog | ✅ Focus returns to the card |
| Standup open/close | ✅ Focus goes to the heading; Escape returns focus to "Start standup" |
| Tab past the dialog's last control | ⚪ Leaves the dialog after 26 stops. The dialog is a native modal, so the page behind is inert; focus most likely went to browser chrome. Not a defect; check by hand in a real browser |
| Reduced motion | ✅ 9 reduced-motion rules present |
| Targets under 24px | 🟡 17, mostly 18px checkboxes in filter popovers. Passes WCAG 2.2 2.5.8 only if spacing gives each a 24px zone. Check by hand |
| 720px wide (≈200% zoom) | ✅ Sidebar becomes a bottom tab bar; no sideways scroll. 🔴 **The count tiles and chips fill the entire first screen; no work is visible without scrolling** |

The last row is the strongest evidence for the header band (DesignChamp §3.3): at 200% zoom, the current header pushes all the work below the fold.

## 4. States for the decided changes (to specify before build)

None of these exist yet. Each needs a behaviour and, where marked ✎, copy from WordSmither.

| Feature | Empty | Loading | Error / failure | Recovery | Success |
|---|---|---|---|---|---|
| Header band (four counts) | All zero: show one quiet line "Nothing overdue, on hold or unassigned" ✎ | Keep last counts, no spinner | Counts fail: hide the band, the board still works | — | Click count → filtered view with a visible "Clear" |
| Role default scope | Mine is empty: "Nothing assigned to you. Showing your team" with a link back ✎ | — | No role set: fall back to My team, not Everyone | Settings → Default scope | — |
| Personal settings | — | Apply saved theme before first paint | Save fails: keep the choice for this session and say "Couldn't save to your profile. It'll apply on this device until you try again" ✎ | Retry on next change | Quiet inline "Saved" ✎ |
| QC reason prompt (With client under 5/5) | — | — | Reason blank: disable Send, say why ✎ | **Cancel or Escape returns the card to its column and focus to the card** | Card shows "QC 3/5 · sent early"; reason in activity |
| Role picker in the dialog | No match: "No one called 'xyz'. Check the spelling or pick from the team" ✎ | — | Reviewer = maker: block with "The reviewer can't be the person doing the work" ✎ | Change either person | Avatar + name appear in the row |
| Drag to With client under 5/5 | — | — | — | Same prompt as above; dropping and cancelling must put the card back | — |

## 5. What's verified vs hypothetical

| Verified on the working mockup | Hypothesis, needs real use |
|---|---|
| Keyboard move, focus return, live announcement, skip link, modal dialog, reduced-motion rules, 720px layout, 0 axe violations | That designers want Mine + Weekly first, CDs My team + Status, PMs Everyone + Status |
| Count tiles fill the first screen at 200% zoom | That the four counts are the right four for every seat |
| Roles and QC exist on the full task page | That a logged reason changes behaviour without creating friction PMs route around |

Check after Batch 1–2: watch one designer, one CD and one PM open the Hub on a real morning for five minutes each and time the first useful click. The `ux-design-review` skill is planned, not installed, so this is a manual check.

## 6. For WordSmither

Copy needed for the ✎ items in §4, plus: the four count labels, the "sent early" card tag, the QC prompt title and button ("Send anyway" or similar), and Settings section names. Tone: plain, the way Leo's dialog footer already talks ("Status, dates and people save as you change them").
