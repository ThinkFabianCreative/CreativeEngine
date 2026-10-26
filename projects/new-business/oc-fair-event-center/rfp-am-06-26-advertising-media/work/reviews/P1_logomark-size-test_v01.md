# P1 · Logomark size test · v01

```
ASSET:     work/design/ai-inspiration-inbox/gpt-2026-10-22c/Fairlandia-logomark-{positive,negative,compact-positive,compact-negative}.svg
TEST:      Imported as vectors into the templates file (frame "Logomark size test"); rendered at 600 / 200 / 120 / 64 / 32 px wide, royal on cream and gold on royal
DATE:      2026-10-22
```

| Width | Full (with tagline) | Compact (no tagline) |
|---|---|---|
| 600 px | Excellent | Excellent |
| 200 px | Good; tagline still readable | Good |
| 120 px | Lettering good; **tagline illegible** | Good: "A Country of Its Own" reads |
| 64 px | Fails (tagline is noise) | Borderline: "Country" and "Own" read; "A" and "of Its" start to go; swirls blur into the letters |
| 32 px | Fails | **Fails**: reads as an ornamental blob |

**Findings**
- The vector is clean: smooth curves, one path, recolors perfectly to royal and gold. Gold on royal passes contrast comfortably.
- Compact differs from full only by dropping the tagline; the lettering and swirls are identical. It is not yet a small-size version.
- The weak points at small sizes: the small "of Its", the thin swash "A" on top, the swirl tails under the word that touch the letters, and tight counters in "ry" and "wn".

**Recommendations**
1. **Use a size ladder:** full lockup ≥ 200 px; compact ≥ 100 px; below that a separate small mark.
2. **Small mark (≤ 80 px):** don't shrink the wordmark. Use the passport stamp, or a monogram from the lockup's own letters (for example the swash "C" with "OC", or the "A" + "C"), solid, with no swirls.
3. **For a true compact:** remove the lower swirl tails, enlarge "of Its" by about 30%, thicken the swash "A", open the "ry" and "wn" counters, add a little letter space. Flat single color, no bevel.
4. **Tagline:** never inside the mark below 200 px; set it separately in Playfair SC when needed.
