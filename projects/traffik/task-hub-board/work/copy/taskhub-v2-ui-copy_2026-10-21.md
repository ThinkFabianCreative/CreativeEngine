# Task Hub v2: UI copy

CLIENT: Traffik (internal). PROJECT: Task Hub board. Source: DesignChamp interaction pass §4/§6 and Leo v2 handoff (2026-10-20). Voice: Leo's mockup. Reviewed against the handoff specs 2026-10-21: settings options and the age label corrected to the agreed decisions. Sentence case, no exclamation marks, no emoji. `{braces}` are dynamic. "Changed:" marks a departure from DesignChamp's draft.

## 1. Header band

| Location | String | Notes |
|---|---|---|
| Count label | Overdue | Confirmed |
| Count label | On hold | Confirmed |
| Count label | Needs someone | Confirmed. Means no maker assigned |
| Count label | Needs a date | Confirmed |
| Count aria | {n} overdue. Show them | Same pattern for each: "{n} on hold", "{n} need someone", "{n} need a date" (singular: "needs") |
| All zero | Nothing overdue, on hold or missing a person or date. | Changed: "unassigned" skipped the date count; now covers all four |
| Phone button | {n} issue / {n} issues | Singular at 1. Hidden at 0 |
| Phone button aria | {n} issues on the board. Show them | |
| Filter control | Clear | Visible while a count filter is on |
| Filter aria | Clear filter: {label} | e.g. "Clear filter: Overdue" |
| Filter announcement | Showing {n} {label} tasks. | Announced on click, e.g. "Showing 3 overdue tasks." |

## 2. Scope

| Location | String | Notes |
|---|---|---|
| Scope label | Mine | |
| Scope label | My team | |
| Scope label | Everyone | |
| Mine empty | Nothing assigned to you. Showing your team. | Changed: added the full stop; link follows |
| Mine empty link | Back to Mine | Returns to the empty Mine view |
| No role fallback | Showing your team. Set a default in Settings. | Only if shown. "Settings" links to Personal settings |

## 3. Home

| Location | String | Notes |
|---|---|---|
| Today panel empty heading | Nothing due today | |
| Next up fallback | Next up: {task} for {client}, due {date}. | If nothing is scheduled at all: "Nothing coming up." |

## 4. Personal settings

| Location | String | Notes |
|---|---|---|
| Dialog title | Your settings | Signals personal, not workspace-wide |
| Intro line | These apply only to you. Changes save as you make them. | Matches Leo's footer voice |
| Section | Appearance | Theme, Text size, Density, Motion |
| Section | Workspace | Opens on, Default scope, Show weekends, Preferred team. Matches the nav name |
| Section | Notifications | |
| Theme | System / Light / Dark | |
| Text size | Default / Large | Spec: two options (Large = 112.5%) |
| Density | Comfortable / Compact | |
| Opens on | Role default / Home / Weekly / Day view / Calendar / Status | Spec options; names as they appear in the app (there is no screen called "Board") |
| Default scope | Role default / Mine / My team / Everyone | Spec: Role default comes first |
| Default scope helper | Whose work you see when the Workspace opens. | |
| Role default helper | Set for your role by an admin. | Shown under any setting left on Role default |
| Motion | System / Reduced | Spec options |
| Motion helper | System follows your device setting. | |
| Show weekends | On / Off | Toggle; label carries the meaning |
| Preferred team | Pick a team | Placeholder for the select |
| Preferred team helper | Used for My team when you work across teams. | |
| Notifications | Keep Leo's existing per-type switches and labels | Spec: notifications already exist; they move from the browser to the profile, wording unchanged |
| Saved | Saved | Quiet inline, next to the changed control |
| Save failure | Couldn't save to your profile. This applies on this device until you try again. | Changed: "It'll apply" was ambiguous about "it"; same meaning |

## 5. QC early-send prompt

| Location | String | Notes |
|---|---|---|
| Title | Send before QC is done? | |
| Body | {n} of {total} QC checks are still open: | Followed by the open items as a list |
| Open item | {check name} | One per line, as named in the QC list |
| Reason label | Why send it now? * | Asterisk per Leo's convention |
| Reason placeholder | e.g. Client asked for it today | |
| Blank-reason error | Add a reason to send it early. | Shown beside disabled Send; also aria-describedby on the button |
| Primary | Send anyway | Neutral style per handoff, not destructive red |
| Cancel | Cancel | Card returns to its column |
| Activity log | {person} sent this to client with QC {done}/{total}: "{reason}" | Timestamp from the log row |
| Card tag | QC {done}/{total} · sent early | Confirmed |
| Card tag aria | QC {done} of {total} checks done. Sent to client early. | |
| QC progress on card | QC {done}/{total} | |
| QC progress aria | QC: {done} of {total} checks done | |

## 6. Move toast

| Location | String | Notes |
|---|---|---|
| Toast | Moved to {column} | |
| Action | Undo | |
| After undo | Moved back to {column} | Short, then dismisses |
| Screen reader (move) | {task} moved to {column}. Undo is available. | Polite live region |
| Screen reader (undo) | {task} moved back to {column}. | |

## 7. Role picker

| Location | String | Notes |
|---|---|---|
| Row labels | Account manager / Project manager / Creative lead / Maker / Reviewer | Confirmed |
| Search placeholder | Search people | |
| No match | No one called "{query}". Check the spelling or pick from the list. | Changed: "the team" implied a scope filter; "the list" is what they see |
| Reviewer = maker | The reviewer can't be the person doing the work. | Confirmed, added full stop |
| Change control | Change | aria: "Change {role}", e.g. "Change reviewer" |
| Empty row | Not set | Shown before a person is picked |

## 8. Task pop-up

| Location | String | Notes |
|---|---|---|
| Step label | Current step | |

## 9. Age label

| Location | String | Notes |
|---|---|---|
| Card | {n}d in stage | Kept DesignChamp's "stage": the age counts days in the board column, not the plan step, so "step" would point at the wrong thing |
| Aria / tooltip | In {column} for {n} days | Singular: "1 day". Names the column, like Leo's current tooltip |
