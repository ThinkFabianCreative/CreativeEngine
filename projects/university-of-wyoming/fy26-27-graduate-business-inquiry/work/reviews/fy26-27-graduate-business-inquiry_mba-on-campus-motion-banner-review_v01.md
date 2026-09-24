# UW graduate business: On-Campus MBA motion banner review v01

```
PROJECT:   University of Wyoming · FY26–27 Graduate Business Inquiry Campaign (handle)
ASSET:     Figma, "UofW - Meta Ad Campaign", frame "ON-CAMPUS MBA | Motion Banner" (node 643-62),
           1080 × 1080, 15 s loop, built by Andres in Figma Motion. Keyframes read through the
           Figma connector (get_motion_context), 2026-09-23
MODE:      DEVELOP · internal · 2026-09-23 · design-champ, method from review-animations
CALIBRATION: review-animations is an interface-motion skill. Per DesignChamp/skills/emil-kowalski-skills.md
           its UI rules (sub-300 ms, no ease-in, frequency gate) do not govern advertising motion.
           Used here for method and output only; timing judged as a 15 s sound-off Meta video
           (pack 11: T2 video = camera pull-out, no VO; pack 12 video timing).
STATUS:    No verdicts on the idea. Copy and imagery findings from the carousel review
           (…_mba-on-campus-carousel-comps-review_v01.md) still apply and are not repeated here.
```

## Timeline as built (seconds)

| State | Visible | Type on screen (solid hold) | Background move |
|---|---|---|---|
| 00 week | 0 – 5.5 | 4 items build 0.09–1.7 (box pop, slide, tick, strike each); "All in the same week." 3.8–5.0 (1.2 s) | 643:191 zoom-out 1.12→1, 0–2.8, then static |
| 01 STUBBORN | 5.1 – 7.5 | 5.85–6.96 (**1.1 s**) | 643:192 zoom 2.48–**5.54** (done 0.4 s after it appears; static after) |
| 02 COWBOY | 7.1 – 9.9 | 7.74–9.33 (1.6 s) | 643:193 scale 0.16–8.28, translate **1.33**–8.28 (mostly while hidden) |
| 03 tagline | 9.5 – 13.1 | 10.53–12.18 (**1.65 s for 8 words**) | 643:86 zoom 9.48–13.05 ✓ |
| 04 end card | 12.1 – 15 | MBA / label / logo settled ~13.5; hold **1.5 s** | 643:125 zoom 12.08–15 ✓ |
| under all | — | — | 647:62 "Continuous Zoom Background" 1.65→1, 0–9.78, fades 9.45–10.08. Image + 2 linear gradients |

Structure tracks pack 12 closely (week 0–5, STUBBORN ~5–7.5, COWBOY ~7.5–10, tagline 10–12.5, proof 12.5–15). Pull-out-only camera is correct for the brief.

## Findings

| Before | After | Why |
|---|---|---|
| Per-state background images (643:191/192/193) each with their own zoom, plus a hidden continuous zoom (647:62) underneath | One camera: 647:62's single pull-out (tight → whole scene) runs 0–9.9 s under States 00–02; delete 643:191/192/193; states carry type only | Pack 11 asks for one camera pull-out. Now the continuous move is invisible except through crossfades, and the per-state moves are mis-timed (below). One move also matches the carousel's tight → wide |
| 643:192 zoom 2.48–5.54 s; 643:193 scale from 0.16 s, translate from 1.33 s | If per-state moves stay: start each at its state's fade-in (5.1 s, 7.08 s), run to its fade-out, same start for scale and translate, `linear` or a very gentle ease | Moves are keyed to 0, so STUBBORN and COWBOY sit on frozen images for ~2 s, and 643:193's scale and translate drift apart (origin wanders) |
| State crossfades with both layers semi-transparent (5.03–5.55, 7.08–7.53, 9.48–10.05) | Incoming state fades in *on top* at full opacity while the outgoing one stays at 1, then cut it; or hard cut on the beat | Two half-transparent frames dip through 647:62 (a third crop with gradients): a muddy flash on every transition |
| State 03 → 04: same photo (20100823_WTM8827) in two layers, 643:86 at scale 1.0 and 643:125 at 1.035, crossfaded over 1.05 s ease-in-out | One photo layer spanning 9.5–15 s with one continuous move; swap only the type and the band | Mismatched scales on a crossfade = ghosted double image for a full second |
| Text entrances `cubic-bezier(0.45, 1.45, 0.8, 1)` (back-out overshoot) on every line | `cubic-bezier(0.16, 1, 0.3, 1)` (strong ease-out, no overshoot), 450–600 ms | Bounce on every headline reads template and playful; UW voice is "confident, direct, credible" (pack 11). Save overshoot for nothing, or one deliberate moment |
| Entry vectors: bullets from ±34 px diagonals, STUBBORN from −90 x, exits −180 x, COWBOY from +180 x, tagline from lower-left, subheading from right | One direction for all type: rise 16–24 px + fade; exits fade only (or fall 12 px) | Six directions in 15 s have no spatial logic; big horizontal whips (180 px) fight the slow pull-out |
| Week build: 16 animations in 1.6 s (box spring 0.82→1.11→1, text slide, tick draw, strike draw ×4) | Checklist kept (decision 2026-09-23). Per item: text appears, then one strike draws; items 400–500 ms apart; no box pop, no tick | Busiest moment of the ad is its first 1.6 s; one gesture per item lets the viewer read each item and see it get done |
| Text exits `cubic-bezier(0.7, 0, 0.84, 0)` *and* the parent state fading at the same time | Let the state transition carry the exit; drop per-text exits, or exit text only on a hard cut | Double exit: text accelerates away while its frame also fades |
| STUBBORN solid hold 1.1 s; tagline 1.65 s for 8 words | STUBBORN ≥ 1.5 s; tagline ≥ 2.5 s (take from the week build's dead time 1.7–3.3 s) | Sound-off feed viewers need about 3–4 words/s plus reaction time; the tagline currently ends before a first-time reader finishes it |
| Tagline exits 12.18–12.93 while MBA enters 12.53 | End the tagline before the end card's type moves | Two text blocks moving in different directions overlap for 0.4 s |
| No logo or label until 10.2 s | Logo + ON-CAMPUS MBA label static from frame 1 (pack 12 video: "logo + label from frame 1") | First exposure: most viewers leave before 10 s |
| First frame (0–0.09 s): photo only | Frame 0 already shows the first week item or set line | Meta may use frame 0 as the thumbnail; muted autoplay needs words at once |
| 647:62 fills: image + 2 linear gradients | Flat scrim or none | Pack 10: no gradients |
| 1080 × 1080 only | Build 4:5 (1440 × 1800) and 9:16 (1080 × 1920) as specified | Pack 11 video formats; 9:16 safe zones change the layout |

## Verdict by tier

1. **Feel-breaking:** crossfade dips through a third image on three transitions; ghosted end-card photo; STUBBORN and COWBOY sitting on frozen images because their camera moves ran while hidden.
2. **Missed simplifications:** one continuous camera instead of four overlapping zooms; the week build cut to one strike per item.
3. **Performance:** none. Only transform, opacity and stroke trim are animated.
4. **Timing:** holds too short on STUBBORN and the tagline; dead air 1.7–3.3 s; double exits; tagline and end card overlap.
5. **Cohesion:** overshoot on every line and six entry directions make it read like a template, not UW.
6. **Accessibility (ad terms):** sound-off readability depends on the hold fixes; branding from frame 1.

**Decision: Block.** The structure and beat timing are right. Fix the transitions and camera (single pull-out, top-layer fades, one end-card photo) and the holds, then review again frame by frame at 0.25× speed.
