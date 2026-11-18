```
CLIENT:        Edwards Lifesciences
PROJECT:       tmtt-xlt-deck
SOURCE SCOPE:  PROJECT-LEVEL
DATE:          2026-10-07
OWNER:         design-champ
```
# Build and interaction spec: Figma Slides (sBqCMoTCaPupEZj9aRleUq)

Derived from Yash's CLICK cues in the speaker notes (read 2026-10-07, notes unchanged). Slide text is verbatim; builds only reveal it.

## What the Plugin API can and can't do (checked in plugin-api-standalone.d.ts and at runtime)
| Capability | API | Status |
|---|---|---|
| Slide transitions | `SlideNode.setSlideTransition` | **Works.** Applied: all 7 slides DISSOLVE, 0.4 s, EASE_IN_AND_OUT, ON_CLICK |
| Object build-ins (per-element on-click reveals) | none | Not in the API. **Implemented with the magic-move pattern** (build-state slides + Smart Animate), see below |
| Poll element | `InteractiveSlideElementNode` type POLL | Read-only; cannot be created. Insert by hand |
| Video | `VideoPaint` readable; no upload path from MCP | Drag mp4 in by hand |

## IMPLEMENTED 2026-10-08: magic-move build states (CD decision)
Each CLICK is a cloned build-state slide placed after its original, same layer names, Smart Animate between them. The original slide is state 0 (not-yet-revealed elements at opacity 0, y+40) and keeps Yash's full notes verbatim. Later states carry only "(build N of slide 0X)". No slide deleted.
- Transitions: state 0 of every slide = Dissolve 0.4 s, ease in-out, on click (different layers from the previous slide, so Smart Animate would morph unrelated "Rectangle"s). Every later state = SMART_ANIMATE 0.5 s, GENTLE, on click.
- Rows (sections) are named per slide. 7 slides → **22 slides**.

| Row | State order (slide IDs) | Reveal per click |
|---|---|---|
| 01 Cover | 3:2 → 13:2 | 1: tagline "Patient-matched & Advancing with every case" (no CLICK in notes; added because the user asked for a reveal on every slide) |
| 02 Pizza poll | 3:10 → 13:10 → 13:34 | 1: red C highlight + dark panel + "&" + "Your guests are not all the same…"; 2: "That's the value of the full portfolio…". The C highlight was on at load, which gave away the answer before the vote; it now arrives with click 1 |
| 03 Promise | 3:34 → 13:58 → 13:76 | 1: "Our promise…"; 2: rule + Empower / Enable / Elevate |
| 04 Video | 3:52 → 13:94 | 1: caption "TCT '26 - validated with 230+ clinicians (EU, US)" (no CLICK in notes; added for the every-slide rule). Video sits on both states. Set autoplay on 3:52 only, or the clip restarts on the click |
| 05 Learned | 4:5 → 13:98 → 13:118 | 1: EXTERNAL column; 2: INTERNAL column |
| 06 Orchestration | 4:25 → 13:138 → 13:206 → 13:274 → 13:342 → 13:410 | 1: Today + timeline; 2: ONE STORY chain + JOURNEY ORCHESTRATION + Adobe; 3: 2027 sequence + "What we learn…"; 4: team row; 5: 2.7x |
| 07 Close | 4:86 → 13:478 → 13:498 | 1: three asks; 2: "Patient-matched & Advancing with every case". The two separator "&" layers (Yash's content) are visible and build in with the asks on click 1 |

Caveats
- Smart Animate matches by layer name and order. Repeated names ("Rectangle", "Field visit") match by order because clones keep the same order. Check slide 6 in presenter view.
- A text edit after this point has to be made on every state of that slide. Make final text and Vesta edits first, then rebuild the states (or edit all states).
- The video slide has two states. If playback restarts on the click, drop the caption reveal (skip 13:94, or delete it with the user's OK).

## Global motion rules (manual fallback, if the states are dropped)
- One transition for the whole deck: Dissolve 0.4 s. No slide/push/move transitions, no Smart Animate.
- One build style: Fade in, 0.3 s, ease out, On click. No fly-ins, bounces, scale or rotation.
- Red elements never animate color. Logo never animates.
- Every build below is one click. Builds = CLICK cues in Yash's notes, no more.

## Per-slide builds
**1 Cover (3:2).** No builds; all on at load. Transition in: Dissolve.

**2 Poll (3:10).** 2 clicks.
- On load: "LIVE POLL --- VOTE NOW", question, A–D and their sub-lines, and the live poll element.
- Click 1: dark panel + "Your guests are not all the same. Neither are mitral and tricuspid patients."
- Click 2: "That's the value of the full portfolio: the therapy fits the patient, not the other way around."
- The "&" text node on this slide: keep hidden/off unless Yash wants it; it is a second ampersand before the slide 4 reveal (flag, no change made).

**3 Promise (3:34).** 2 clicks.
- On load: "The full portfolio changes what is possible."
- Click 1: "Our promise: …patient-matched care."
- Click 2: rule + Empower / Enable / Elevate columns together (one click; Yash talks through all three).

**4 Video (3:52).** No builds. Video autoplay on slide entry, sound on, no loop, plays once (30 s); poster frame = the clean wide "&" couch frame (~0:04). Caption "TCT '26 - validated with 230+ clinicians (EU, US)" on at load. This is the first appearance of the couch.

**5 Learned (4:5).** 2 clicks.
- On load: title.
- Click 1: EXTERNAL column (What customers told us, 01, 02).
- Click 2: INTERNAL column (What it asks of us, 03, 04).

**6 Orchestration (4:25).** 5 clicks.
- On load: title "One story for every physician. …right time".
- Click 1: "Today each therapy on its own calendar" + its timeline (field visits, scattered dots).
- Click 2: ONE STORY list (Portfolio promise, Three pillars, The & creative, Therapy campaigns) + JOURNEY ORCHESTRATION + "who · what · when · where" + "Adobe: …".
- Click 3: "2027 a sequence built…" + its timeline (Paid media, ABX, Social, Web, Email, field visits) + "What we learn across the portfolio feeds the next conversation".
- Click 4: team row (Portfolio marketing / Audience intelligence, Brand / Content system, Digital / Orchestration).
- Click 5: "2.7x" + "more case volume in accounts with ABX engagement".

**7 Close (4:86).** 2 clicks.
- On load: red square + white "&", "Ask first. Then order what fits.", "For every patient, …right moment."
- Click 1: three asks (Use the playbook / Keep therapy the hero / Build the partner beyond the device) together.
- Click 2: "Patient-matched & Advancing with every case".
- Footer "Edwards Confidential — For Internal Use Only." and logo on at load.
- Two separator "&" text nodes between the asks: KEEP. They are Yash's original content and build in with the asks.

## Video
- Slide 4 rectangle "VIDEO — creativeVideo.mp4" area: 1464×824 at x228 y128 (Design file 1:58 geometry; mirror in Slides).
- Source ~/Movies/creativeVideo.mp4 (30 s, 1280×720). Drag in by hand; set Autoplay on, Loop off, Muted off.
- Backup: if the venue has no audio or Figma video stalls, keep a still of the clean wide couch frame as the poster and play from a local file.
- Copy in the end frame carries PP-US-13208 v1.0; keep the film unedited.

## Live poll: options
| Option | Pros | Cons |
|---|---|---|
| **Figma Slides native Poll (recommended)** | Lives on the slide, results render live in presenter mode, no second screen or app | Audience must open the Figma Slides presentation link on their devices (needs a Figma login or public view link); check Edwards IT allows figma.com; 4 options fit A–D |
| Slido / Mentimeter (external) | Familiar for exec rooms, QR code join, no Figma account | Leaves the deck; extra license; Edwards approved-vendor check needed; results on a separate screen |
| Show of hands (fallback) | Zero risk | No results to read out on the close |

Recommendation: native Poll, options entered exactly "12 pepperoni", "One of everything", "Ask first, then order", "Pineapple for all", placed over the A–D list area or replacing it only if Yash agrees (the on-slide A–D text stays as is). Rehearse with one test voter on the venue network. Keep show of hands as fallback. Confirm with Yash (still open in README).
