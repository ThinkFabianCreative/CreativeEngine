# ChatGPT image prompts · R3-2 Footing cold-read test v01

```
CLIENT / PROJECT:  Edwards Lifesciences · SAPIEN M3 RESILIA animation
SOURCES:           work/copy/territories-round3_v02.md (R3-2 Footing) · work/reviews/territory-review_v04-round3.md §2, §5
                   (conditional BET: cute / stepping stones / ring-coil) · work/image-prompts/chatgpt-mood_v01.md (LOOK conventions)
AUTHOR / MODE:     design-champ, 2026-10-15 · DEVELOP · cold-read test frames, pitch/internal only, never commercial
TOOL:              ChatGPT (GPT image model) · one chat, three prompts in order
CLIENT AI RULE:    visual-direction.md: never generate patients, physicians, procedures, Edwards devices or anatomy.
                   No valve, dock, coil, catheter, organ tissue, ECG line.
```

## Heart-form decision

**Simplified-sculptural, not anatomical.** A small, solid, heavy cast object in matte red: the familiar heart silhouette, but thick, slightly asymmetric, softened edges, matte stone-like surface, sitting with visible weight. Anatomical is out (it breaks the no-generated-anatomy gate and the glass heart is a separate labelled variant). The simplified form is the one most exposed to the cute/mascot read, so it is the honest thing to test: if this form passes, every softer route passes; if it fails, we know before the pitch. Never: face, eyes, limbs, feet, shine highlights like a sticker, bounce, tilt, squash, emoji symmetry.

## Shared LOOK block (paste first as its own message, and keep at the end of each prompt)

> LOOK: product-grade still-life photograph on a warm beige seamless paper backdrop (approx. #E3D6C4), floor curving into wall, no visible horizon. One single saturated red accent (approx. #C8102E), and only one: the heart object. Everything else beige, tan, warm grey. Soft north-window light from camera left, large diffused source, gentle long shadow falling right. Camera low and side-on, almost at floor level, 90mm lens, f/8, sharp subject. Grade: matte, low contrast, warm neutral, fine grain. Style: Irving Penn still life, Hiroshi Sugimoto restraint. Calm, precise, procedural. 16:9 landscape. No text, no letters, no numbers, no logos, no people, no hands, no medical devices, no anatomical organs, no ECG or pulse lines, no rings, no coils, no spirals.

> HEART (identical in all three frames): a small, solid, heavy red heart-shaped object cast in matte red stone-like resin, thick and slightly asymmetric, softened edges, no gloss, no face, no eyes, no limbs, no shine highlight. It sits low and heavy, like a paperweight. Small in frame, about one tenth of frame width.

---

### F1 · Uneven ground ahead
**Must prove:** the heart reads as a weighted object, not a character, and the ground ahead is visibly not ready.
**Prompt:**
> The red heart object [HEART] rests still on the left third of the frame, on the beige floor. Directly ahead of it, to the right, a single patch of the floor is uneven: a shallow irregular dip with a slight ridge on one side, as if the beige paper surface were pressed and buckled, same material and colour as the floor. Only one patch. The rest of the floor is smooth. Lots of empty space on the right. [LOOK]

**If it goes wrong:** if the heart looks cute or toy-like, reply "make the heart heavier and rougher, like carved stone, sitting lower; no gloss". If the patch reads as a hole or crater, "make it a gentle buckle in the floor surface, shallow".

### F2 · The ground draws in to a level footing
**Must prove:** the patch is pulled in from its own edges and becomes flat. A level plane, not a disc, rim, ring or groove.
**Prompt:**
> Same scene, same camera. The uneven patch ahead of the red heart [HEART] is in the act of levelling: its edges are drawing inward from all sides, the folds of the beige surface smoothing towards the centre, the dip filling and becoming perfectly flat and level, flush with the floor. Show it mid-way: faint soft tension lines on the surface converging inward, already mostly flat. No raised edge, no rim, no circular outline, no concentric marks, no spiral. The heart has not moved yet. [LOOK]

**If it goes wrong:** ring or disc read → "no outline at all; the patch is the floor itself becoming flat, you should barely see where it begins". Spiral or coil read → "remove all curved lines; straight soft creases pulling inward, like smoothing a tablecloth".

### F3 · Settled, moving forward
**Must prove:** the heart has travelled and settled on the footing with weight; the trail behind is levelled flush; one forward direction, no path of discs ahead.
**Prompt:**
> Same scene, same camera. The red heart [HEART] now rests on the levelled spot, in the centre-right of the frame, sitting low and settled with a soft contact shadow, as if it slid there with an even, weighted glide. Behind it, on the left, the floor is perfectly smooth and level, with only the faintest trace where the ground had been uneven. Ahead, on the far right, the beige floor is smooth and empty; nothing has formed yet. Slight horizontal motion softness only at the heart's trailing edge, none in the air. No footprints, no stepping stones, no row of discs, no path markings. [LOOK]

**If it goes wrong:** row of discs or a path → "remove everything ahead; one heart, one levelled patch under it, empty floor ahead". Bouncy or airborne → "the heart touches the floor fully, heavy, no lift".

---

## Cold-read protocol

**Who:** two to three people outside the project and outside TRAFFIK creative; at least one clinician (cardiology, nursing or allied health) if reachable. Nobody who has seen the script, title slide or brief.

**How:** show F1, F2, F3 in order, side by side or one after another, no title, no copy, no sound, no context beyond "three frames from a short film". Then ask exactly, once:

> "What is happening here?"

Then, only after they answer: "What do you think it's for?" No other prompts. Do not say heart, ground, step, valve or medical. Record their first words verbatim before any discussion.

**Pass reads (any of these, unprompted):** something steady moving forward; the ground preparing, levelling or getting ready before it moves; making a safe or stable place to land; careful, deliberate, controlled.

**Fail reads (any one, unprompted):** cute, sweet, a character, mascot, Valentine, toy; stepping stones, a path, coins, tokens, buttons; a ring, a target, a hole, a coil or spring; a game, a level, a board game piece; bouncing, hopping, walking.

**Verdict rule (from review v04):** majority pass and no clinician fail = Footing holds BET THE PITCH. Any "cute/mascot" read from the clinician, or from two of three viewers = Footing drops to ADVANCE and The Gather leads. A ring/coil or stepping-stone fail is an art-direction fix: rework the frame and re-run before deciding.

**Log:** add a row per viewer to `work/reviews/footing-coldread-log.md` (create on first use): date · viewer role (no names) · clinician Y/N · verbatim first answer · answer to "what is it for" · PASS / FAIL (which fail code: CUTE, STONES, RING, COIL, GAME) · images used (filenames). Save images as `P1-FOOT-F1..F3_COLDREAD_gpt_v01.png` in `work/generated/P1/` and add them to `generation-log.md`. Report the tally to creative-engine-director.
