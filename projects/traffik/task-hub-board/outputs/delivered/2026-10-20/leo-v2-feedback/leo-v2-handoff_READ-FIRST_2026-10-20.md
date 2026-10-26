# Leo v2 feedback: read first

```
CLIENT:   Traffik (internal; files name real clients, do not publish)
PROJECT:  Task Hub board
DATE:     2026-10-20
STATUS:   Ready for Leo. All decisions made 2026-10-20
```

## Brief and assumptions

There is no normalized brief for the Task Hub. Requirements come from the Oct 12 v1 spec and the culture-reset workflow.

| | Working answer | Status |
|---|---|---|
| Audience | Makers (designers), Creative Directors, PMs / account. Leadership secondary | From Andres |
| Primary task | At the start of the day, see what needs me next and what's stuck; run standup from the board | From Andres and the v1 spec |
| Outcome | Fewer missed handoffs; problems seen early; brief → review → QC → client actually followed | From the culture-reset workflow |
| Central idea | **A calm board where problems stand out** | **Assumption.** Not written anywhere; the colour and header changes rest on it |
| What each seat needs first | Makers: own work. CDs: review queue and who's stuck. PMs: risk and missing owners or dates | **Hypothesis** until watched (see Outcome checks) |

## Severity

One scale in every document: **Major** (slows or misleads the primary task for a whole seat), **Minor** (friction or noise), **Opportunity** (worth doing, not a fix), **Keep** (protect it). Nothing found **blocks** the primary task. Older drafts said High / Medium / Low: read High as Major, Medium and Low as Minor.

Documents from today's review. Where they overlap, **this page wins**.

| Doc | What it's for |
|---|---|
| `supporting/ux-audit_leo-mockup-v2_2026-10-20.md` | UX findings and scorecard vs the Oct 14 audit |
| `supporting/designchamp-pass_leo-mockup-v2_2026-10-20.md` | DesignChamp, Marketing design lead: colour roles, card anatomy, header band, dialog. **Owns the visual specs** |
| `supporting/designchamp-review_leo-v2_2026-10-20.md` | DesignChamp full review, both specialties: findings M1–M6, m1–m7, O1–O3 with evidence and how to verify each. **The findings list of record** |
| `supporting/designchamp-interaction-pass_leo-v2_2026-10-20.md` | DesignChamp, Interaction design lead: routes per seat, keyboard and focus results, **states for every new feature**, verified vs hypothesis. **Owns the behaviour specs** |
| `supporting/trello-gap-libraries-type_2026-10-20.md` | Trello gap, libraries, type scale, seats, theme, a11y results |
| `TaskHub_Leo-v2_audit-markup_2026-10-20.pdf` + `taskhub-mockup_v2_MARKUP.html` | Visual markup. Pin numbers are the markup's own (#1–32) |

## Resolved conflicts

| Topic | Was | Now |
|---|---|---|
| Parent line on cards | Audit: drop everywhere | Drop on Status board; keep one truncated line on Weekly and Day |
| Summary row position | Audit: above the view switcher | One header band, **below** the switcher, four problem counts, zeros hidden |
| Board columns | Audit dropped Feedback | v1 spec order stands: Intake → Ready → In progress → Internal review → QC → With client → **Feedback** → Done; On hold as a top lane |
| Card title / page title | 14/600 and 24px (type doc) vs 15/500 and 28px (DesignChamp) | DesignChamp's: **15/500 title, 28px page title**, 12px meta, client 12/600 |
| Designer default | Board (type doc) vs Weekly (DesignChamp) | **Mine, Weekly** |
| PM default | "My clients" (type doc) vs Everyone | **Everyone, Status board**. "My clients" scope is later |
| Libraries | Adopt Pragmatic DnD now vs no new libraries | No new dependency now; Leo already has drag. Atlassian tokens as reference only |
| KPI numeral size | DesignChamp said 44px | Measured 30px. Conclusion unchanged: counts out-shout the work |
| "Start standup not a button" | In first audit draft | Wrong, removed |
| "No roles, no QC checklist" | Audit and DesignChamp | Wrong: both exist on Leo's **full task page** (Ownership incl. Reviewer and Creative lead; five-item QC checklist). The fix is to surface them in the quick dialog and on the card |

## Added after the full review

| Finding | Severity | Change |
|---|---|---|
| No visible confirmation after a move; a card dragged off screen vanishes, no undo | Minor | Toast "Moved to Intake · Undo" for 5 seconds; Undo restores column and focus |
| Phone (375px): tiles clipped mid-label, chips stack five rows, first card below the fold | Major | Header band collapses to one "4 issues" button on phones |
| Age box explained only by hover tooltip; no tooltip on touch | Minor | Visible label "7d in stage", shown only after 3 days |
| No icon system: ~15 hand-drawn icons, mixed strokes (1.4 / 1.6 / 1.75) and grids | Minor | **Lucide** (Feather's maintained successor, ISC licence): 24 grid, stroke 1.75, 16px in UI, 20px in nav, `currentColor`, decorative icons `aria-hidden` beside a text label; icon-only buttons get an `aria-label` |
| New Task form errors | Keep | Inline message under each field, required marked, focus to first error. Reuse for every new prompt |

## Outcome checks (does it actually cut load?)

Build checks are in `ACCEPTANCE.md`. These check the result with people, after Batch 2 and again after Batch 3:

1. **First useful click.** Watch one maker, one CD and one PM open the Hub on a real morning. Time from load to the first click that starts real work. Target: under 10 seconds, without changing scope or filters.
2. **Five-second glance.** Show the Weekly view for five seconds; ask "what's in trouble?" Target: people name the overdue and on-hold items, not the red client.
3. **Status agreement.** From the task pop-up alone, ask three people "what stage is this in?" Target: all three give the same answer.

## Decisions (Andres, 2026-10-20)

### 1. Primary action colour: neutral, not red

Andres agreed with DesignChamp: red means problems only. This replaces Oct 14 audit B3.10 ("red for + New Task").

| Theme | Primary button (New Task, Next, Save, Send to client) | Text on it |
|---|---|---|
| Light | Ink fill `#14151A` (Leo's `--text-primary`) | White |
| Dark | Off-white fill `#F2F2F5` (Leo's dark `--text-primary`) | `#14151A` |

- Why neutral: every hue is already taken (red problems, amber warning, blue/purple/yellow/green status, many client colours). A hued primary would collide with one of them. Inverse ink is how Linear, Vercel and Notion keep one obvious action without adding a colour. Both pairs are well above 4.5:1.
- One primary button per screen. Everything else is secondary (outline or ghost).
- Traffik red stays in the logo only.

### 2. Personal settings: every user gets a Settings panel

Assume the backend stores per-user settings. Settings live on the profile, follow the user across devices, and apply before first paint (no flash). Open from the avatar menu.

| Setting | Options (default first) | Why it cuts load |
|---|---|---|
| Theme | System · Light · Dark | Comfort; replaces the browser-only toggle |
| Text size | Default · Large (112.5%) | Legibility without browser zoom breaking the board |
| Density | Comfortable · Compact | Compact for PMs scanning many cards, Comfortable for makers |
| Opens on | Role default · Home · Workspace (Weekly / Day / Calendar / Status) | People land where their work is |
| Default scope | Role default · Mine · My team · Everyone | Role default: makers Mine, CDs My team, PMs Everyone, leadership Executive |
| Motion | System · Reduced | Honours reduced-motion and lets people choose it |
| Show weekends | Off · On | Fewer empty columns |
| Preferred team | Role default · any team | Leo's existing setting: defines "My team". Keep it |
| Notifications | Per type, on/off | Leo's existing switches; move from this browser to the profile |

Leo already has a Settings dialog (Preferred team, notifications, "How the Hub treats work"); it saves to the browser only. Extend that dialog rather than building a new one. "Role default" is set by an admin per role, so most people never touch this panel. Leo's "Viewing as" stays for admins and demos.

### 3. QC: advisory, with a logged reason

Andres chose advisory plus a logged reason (2026-10-20). This replaces the v1 spec line "Send / present waits on it".

- The checklist never blocks a status change (Leo's current rule stays).
- Moving work to **With client** with QC under 5/5 opens a short prompt: which items are open, and a required one-line reason. Cancel keeps the card where it was.
- The reason, who gave it and when go into the task's activity log, and the card shows "QC 3/5 · sent early" until the checklist is complete.
- Executive can count "sent with QC open" per account, so the pattern is visible without policing each move.

## Reference files

`references/tokens-v2.css` (colour roles, type scale, spacing, icon sizes for light, dark and system; contrast checked) and `references/REFERENCES.md` (Lucide icon rules and pattern sources).

## Order for Leo

1. Colour roles (DesignChamp §3.1), with the neutral primary in Decision 1
2. Role default scope: Mine (makers), My team (CDs), Everyone (PMs), Executive (leadership)
3. Header band: one row of four counts, once per page (§3.3)
4. Card anatomy + type scale (§3.2; type doc §3)
5. Quick dialog: one status; reuse the full page's Ownership rows instead of the chip wall
6. QC progress ("QC 3/5") on the card and dialog; reason prompt when sent under 5/5 (Decision 3)
6a. Move toast with Undo; phone header pattern; Lucide icons (with Batches 1 and 3)
7. Personal settings panel (Decision 2)
8. Later: inline add card, quick edit, shortcuts

## Not checked

Screen reader; touch drag on a real phone; loading states (static mockup); Resourcing, Clients and Executive drill-downs; 18px checkboxes against WCAG 2.2 target spacing; 22 text-on-tinted-card contrast cases (axe couldn't resolve); Trello compared from knowledge, not re-tested. Keyboard, focus, 200% zoom and reduced motion were checked on the working mockup (interaction pass §3). Role needs are hypotheses until watched with real users (§5).

## Copy

Final copy for every new string is in `COPY.md` (WordSmither, 2026-10-21; source `work/copy/taskhub-v2-ui-copy_2026-10-21.md`). It supersedes the draft wording in the interaction pass §4.
