# Trello references from Mobbin, mapped to the Task Hub gap

```
CLIENT:   Traffik (internal)
PROJECT:  Task Hub board
SOURCE:   Mobbin, Trello web screens (current 2025 UI), searched 2026-10-20
SUPPORTS: trello-gap-libraries-type_2026-10-20.md §1
```

Links only. Mobbin image URLs expire after 30 days, so cite `mobbin.com/screens/...`.

## What the screens confirm

| Gap item | What Trello does | Reference |
|---|---|---|
| **Card front** | Title first. Below it, one row of small icon badges: watch, date range, attachment count, checklist `0/1`, location. Member avatar sits bottom-right. No status chip. | [board, single card](https://mobbin.com/screens/b019519b-d4c1-4184-a1dc-71422b1f4719), [cards with cover images + badges](https://mobbin.com/screens/d22c4c5a-ae26-4533-8b19-7af80af8927b) |
| **Checklist on the front** | The badge turns green with a tick when complete (`1/1`). | [card back, checklist 100%](https://mobbin.com/screens/d6f92345-a559-4d4b-8c3c-ec0dec5d2c24) |
| **Card back** | A two-pane modal. On the left: the list as a status dropdown at the top-left, a round "complete" toggle before the title, then an action row (Add, Checklist, Members, Attachment), then Members / Labels / Dates, Description, Attachments and Checklists. On the right: "Comments and activity" with its own composer. | [card back, full](https://mobbin.com/screens/04203c15-a39d-4cd7-b39a-4d2c24d4ca72), [with description + activity log](https://mobbin.com/screens/845a4e80-5789-4885-b023-2478fac05dba) |
| **Checklist mechanics** | Progress bar with %, items with their own due date and assignee, "Hide checked items", "Add an item". Created from a small popover that asks only for a title. | [checklist items](https://mobbin.com/screens/0db37349-aa0e-46f1-8f07-0d5bf295ef7c), [add checklist popover](https://mobbin.com/screens/1eb6f630-e6c8-495a-95ab-ad8d483f52a8), [empty checklist](https://mobbin.com/screens/7f261c3a-1f4f-4efb-b263-9c269348249b) |
| **Inline add** | "+ Add a card" at the foot of every list, plus a template icon. "+ Add another list" sits beside the last list. | [board](https://mobbin.com/screens/b019519b-d4c1-4184-a1dc-71422b1f4719), [add list input](https://mobbin.com/screens/d62c52f6-851d-49b2-b58d-83503f645896) |
| **Collapse a list** | The `→←` icon in the list header collapses the list to a narrow vertical strip with its name rotated. | [collapsed To Do](https://mobbin.com/screens/c29a5060-9452-4286-924d-9f4a1746210d) |
| **Personal intake** | "Inbox" is a left panel visible only to you, with a quick add field. Planner is a calendar panel docked next to the board. Both are switched from a floating bottom bar. | [Inbox](https://mobbin.com/screens/bf8f7dbd-11a0-43eb-8c9b-79fa8b151271), [Planner](https://mobbin.com/screens/ce59dfd6-acfb-43b3-826a-2842713b0a56) |

## What to take

1. **Card front (1–2 days):** keep the title, a badge row (due, checklist n/m, comments) and an avatar. Drop the status chip. Labels are a strip of colour above the title.
2. **Card back (3–5 days):** use the two-pane layout. The status dropdown in the top-left replaces Leo's three status buttons, and activity stays on the right. Our side sheet can keep the same order of content.
3. **QC as a checklist:** the default "QC" checklist gets items with a due date and an owner, and its badge turns green when it's done. This replaces the QC column.
4. **Inline add + collapse (about 1 day):** a quick add at the foot of each list that takes a title only and lands in Intake. Allow collapsing Complete and On hold.
5. **Hold for later:** the Inbox and Planner panels. Our Workload and Calendar views already cover this ground.

Trello's chrome (background photos, purple gradients) is not a reference. We take the structure only.
