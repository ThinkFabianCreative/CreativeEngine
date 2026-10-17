# UI/UX guidelines for the landing page, v01

```
CLIENT:  Miracles for Kids Charity · PROJECT: website-rebrand · PACKET: P2
SOURCE:  ui-ux-pro-max skill (local database, run 2026-10-16) + CreativeEngine judgment
QUERY:   generic only ("nonprofit charity children donation storytelling playful"); no client data sent
SCOPE:   aesthetic pass. These rules shape the *designs*; nothing here is built functionality
```

The skill's industry tables are soft signals (DesignChamp record). Where they conflict with the brief, the brief wins. Each item is marked **Adopt**, **Adapt** or **Reject**.

## What the skill recommended

| Area | Skill output | Decision |
|---|---|---|
| Landing pattern | "Storytelling + Trust" → Trust & Authority + Conversion: Hero (mission/credibility) > Proof > Solution > CTA | **Adapt.** Our order puts the story first because people come for family stories: Hero (family video + donation card) > Truth > Stories > Programs > Proof > Urgency > Get involved > Events > Close |
| Style | "Accessible & Ethical": high contrast, 16px+ text, keyboard nav, visible focus, reduced motion | **Adopt** as the floor under every look |
| Color strategy | Navy/grey corporate, trust blue, accent for CTA only | **Reject the corporate palette** (it's the "bank" look the client pushed back on). **Adopt "accent for CTA only"** for the action color: color/action/bg is never used as a large block in the same screen as a CTA |
| Typography | Fredoka + Nunito ("playful, friendly, warm") | **Adopt:** already look B. Confirms the direction. Other matches: Varela Round + Nunito Sans; Baloo 2 + Comic Neue (rejected: Baloo 2 is Gillette's, Comic Neue too childish) |
| Motion | Standard tier: one stagger on load or scroll, 300–450ms; animate 1–2 key elements per view at most | **Adopt.** Directly fixes Jordan's round 1, where every heading animated word by word |
| Anti-patterns | "No impact data", "Hidden financials" | **Adopt.** Proof section stays, sourced; financials link visible |

## Rules every look must pass (design checks)

**Accessibility (critical)**
- Body text at least 4.5:1, large text (24px+, or 19px+ bold) at least 3:1. All MFK Color pairings pass (contrast report in `tokens/mfk-color-tokens_v01.json`); the highlight word is display-size only.
- Base body size 16px or more; line height 1.5–1.75 (all four looks pass: 24/16, 28/18, 26/16).
- Visible focus ring, 3–4px, on every link, button, card and filter chip: `color/focus/ring`. Show one focused state in the designs.
- Meaningful photos get alt text; the design notes record it per image.
- Never rely on color alone (program tags carry text labels, not only color).

**Video (the core of this page)**
- Click to play. No autoplay of story videos. A decorative hero loop is allowed only if it's silent, short, has a visible pause button and has a still fallback.
- Every video shows: poster still (child at eye level), play button with a text label ("Watch William's story · 1:43"), duration, and captions indicated.
- Play buttons are large (at least 64px desktop) with a text label, never an icon alone.

**Carousels and rails (stories)**
- No auto-rotation. Previous/next buttons with labels, plus a position indicator ("3 of 6").
- On mobile, a swipeable rail with visible next card peeking, plus buttons.

**Touch and targets**
- Design all buttons, chips and cards at 44px+ height (WCAG web minimum is 24px; we design above it for a donor audience on phones).
- 8px+ between adjacent targets.

**Layout**
- Design at 1440 and 375 for every look; check 768.
- No horizontal scroll at 375. Text never sits on a photo without a solid or scrim block behind it.

**Motion (designed, not built)**
- Mark in the design notes which 1–2 elements animate per view; everything else is still.
- Reduced-motion state = the final static frame.

**Forms (donation card, newsletter)**
- Visible labels, never placeholder-only. Amount chips are real targets. Error text sits next to the field.

## Pre-delivery checklist (per look)

- [ ] No emoji as icons; SVG icons from one set
- [ ] Every text layer uses an MFK text style; every fill uses an MFK Color role (needed for look switching)
- [ ] Contrast pairs from MFK Color only
- [ ] Focus state shown once
- [ ] Video poster, label, duration, captions shown
- [ ] Story rail has prev/next/position, no autoplay
- [ ] 1440 and 375 frames
- [ ] Max 3 brand colors per screen; max 3 shapes per screen; one highlight word per headline
