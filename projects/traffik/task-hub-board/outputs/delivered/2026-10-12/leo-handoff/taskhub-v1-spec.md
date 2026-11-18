# Task Hub v1: the short list (for Leo)

From: Andres Fabian, Creative Director · Oct 2026
Full spec and the "later" list: `taskhub-board-spec.md` · Prototype: `taskhub-board-prototype.html`

The board and four changes. Nothing else in month 1.

## 0. Side navigation (must-have)

**Side navigation (must-have).** A persistent left sidebar replaces the top-only nav:
- **Order, top to bottom:** brand · For you · Hot Sheet · Resourcing · Department (e.g. Creative) · Clients (each client filters every view; "All clients" first).
- **Collapsible** to a 64 px icon rail with a chevron toggle. The user's choice is remembered. Narrow screens default to the rail; it never disappears.
- **Every item has a tooltip and an accessible name** in rail mode. The current page and the selected client are clearly marked.
- The top bar keeps search, + Create and the user avatar.

## 1. A Board view

A new Hot Sheet view with the existing Team, Person and Client filters, plus Mine / My team / Everyone.

- **Columns** follow the step each task is on: Intake, Ready, In progress, Internal review, Quality Control, With client, Feedback, Done.
- **Cards** show four things: title, client, assignee and one status badge (Blocked, Overdue or High).
- **Clicking a card** opens the existing task detail.
- **"Move to"** in the task detail, as an alternative to dragging.

## 2. One owner per role

- **Account lead:** one person, never a pair. Others go in an "Account team" field.
- **New fields:** creative lead, and a reviewer who can't be anyone assigned to the work.

## 3. Quality Control checklist

Rename "Pre-launch QA" to **Quality Control**. It has five yes/no questions, and each answer records who gave it and when:

1. Meets the brief?
2. On brand?
3. Delivers what was asked?
4. Any mistakes?
5. Presentation ready?

"Send / present" can't start until all five are Yes. A No needs an ACD override with a reason.

## 4. Blockers with a reason

Setting a step to Blocked asks for a reason and an owner (a person or "Client"). The board shows blocked work in a lane at the top.

## 5. Brief link

A field on the task. It's required before the first work step goes active on Full-track work.

## Not in v1 (on purpose)

These come in months 2–3, after the board is in daily use:
- Time-log prompt
- Dates from standard times
- Light/Full track
- Rounds and change orders
- WIP warnings
- List and Calendar views
- Leadership and Completed views
- Behavioral nudges
- Intake form rework
- Hiding unreliable capacity numbers

## Questions

1. Can the board read each task's current step from existing data?
2. How long would items 1–5 take?
