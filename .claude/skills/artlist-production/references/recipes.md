# Recipes

Artlist's pitch, mapped onto CreativeEngine's flow. Each recipe says whether it fits, when, how to run it, and what stops it. Models and prices: `models.md`. Prompt craft: `prompting.md`.

**Every recipe produces inspiration or pitch material, never a commercial asset** (Andres, 2026-09-24). Artlist markets these features for production. Here each one shows an idea, and production makes the real thing.

| Artlist's claim | CreativeEngine fit | Recipe |
|---|---|---|
| "Drop in your product, get a full campaign" | **No, not as an idea source.** It skips the brief and the concept (Barry §2, principle 5). Yes for pitching a decided campaign | K |
| "Every ad variant, one run" | **Yes**, as comps of hooks WordSmither wrote as real hypotheses, so the test plan can be pitched | E |
| "Your whole stack works together" | **Yes.** Artlist renders; Figma sets type; Adobe resizes and cuts; Drive and Slack deliver | All |
| "Product UGC at scale" | **Yes, as pitch comps.** Shown as synthetic, never as a testimonial | F |
| "Mockup shots before you commit" | **Yes, the strongest fit** | A |
| "Localize for every market" | **Partial through the MCP.** Voiceover and visuals yes; dubbing existing video is website-only; translation needs a native reviewer | I |
| "Lifestyle shots for retail" | **Yes as comps**, if the product stays accurate | C |

---

## A. Shoot pre-viz and mockup shots

**Fits:** DEVELOP, before a real shoot or before committing to a direction. Label `PRE-VIZ`.

1. For each frame, write a shot-list prompt in the anatomy of `image-direction-reference.md` §5 and §7: scene, shot size, angle and height, lens, light, grade, type zone.
2. Render stills on Artlist Original 1.0 (cinematic look-dev) or Nano Banana 2 (placement control). Draft at 1K first.
3. For camera moves, run image-to-video from the chosen still: Veo 3.1 Lite or Seedance 2.0 Mini draft, 4–5 s, one move.
4. Attach the frames to the shoot brief as comps, never as the target look to copy (§7).

**Stops it:** nothing, as long as it stays labelled and internal.

## B. Key-visual comps and placeholders

**Fits:** DEVELOP comps, JUDGE presentations, pitch-deck imagery (`frontend-slides`, Figma Slides). Label `COMP`, or `PLACEHOLDER` when real photography will replace it.

1. Lock the set: one model, one Style Kit (`<client>-<campaign>`), one grade reference image uploaded with every prompt.
2. Generate each ratio separately (for example 4:5 and 9:16) with the type zone stated in the prompt.
3. Choose by idea and empty type zone, never by the prettiest render. Finish per `image-direction-reference.md` §10. Set type in Figma.

**Stops it:** client rules that forbid generated imagery, even internally.

## C. Product lifestyle and retail context

**Fits:** DEVELOP and pitch, when the client supplies product photography. Label `COMP`.

1. Input: a client product photo, JPEG with no alpha channel, at least 1 MP, cropped to a ratio between 0.4 and 2.5. Where the MCP exposes References, save it as a Prop reference.
2. Model: Nano Banana 2 or Pro for placement, GPT-Image-2.5 Sunburst when the same product goes through many scenes and edits, Seedream 5.0 Pro when the still will be animated with Seedance.
3. Prompt the **setting** and keep the product as the unchanged reference: "Keep the product in @Image1 exactly as it is: shape, color, label, count. Place it…"
4. **Fidelity check** against the real product: pack, label, color, count, size relative to hands and surfaces. Remove anything the model added: price tags, shelf labels, badges, extra branding, "organic" stickers, fake nutrition marks. A single invented price or claim makes the pitch promise something the product isn't. Regenerate, don't retouch.

**Stops it:** no real product photo, an unreleased product the client hasn't cleared for upload, or a product that can't be rendered faithfully.

## D. Animatic and motion test

**Fits:** DEVELOP, to test pacing, reveals and the turn (`narrative-craft.md`) before production. Label `TEMP` on every audio track and `COMP` on picture.

1. Start frames come from approved comps (recipe B). Image-to-video per beat, 4–8 s each. Use first and last frame (Veo 3.1, Flux 3, Gemini Omni) for reveals and transitions.
2. Temp voiceover: text-to-speech of WordSmither's script (`prompting.md` → Voice). Temp music: Lyria 3 at 30 s, or Lyria 3 Pro for a structured bed at an exact BPM so cuts land.
3. Assemble in the edit (Premiere, or Adobe `video_create_quick_cut` for a fast cut). Supers and end card are set in post, never generated.

**Stops it:** nothing; it's internal craft. Keep TEMP labels until audio is replaced or approved.

## E. Hook variants for testing

**Fits:** DEVELOP, when a test plan exists and WordSmither has written 3–5 opening hooks as distinct hypotheses (`format-copywriting` → `references/social-video.md`). Examples: unboxing, expert review, morning routine, before-and-after, problem first.

1. **One body, many openings.** The MCP can't edit video-to-video, so "same footage, different hooks" means generating the shared body once and generating a separate 2–4 s opening shot per hook.
2. Lock continuity: the same character reference or start frame, wardrobe, location and grade across every opening. Use multi-reference models (Seedance 2.x with `@Image` tags, Veo 3.1 Ingredients).
3. Each variant changes **one variable**, the hook, and is named by its hypothesis: `P3_hook-routine_COMP_v01.mp4`.
4. Cut each opening onto the body in the edit. Export per placement.

**Stops it:** hooks that aren't real hypotheses. Five random openings teach nothing, so return them to WordSmither.

## F. Creator-style (UGC-look) product video

**Fits:** DEVELOP and pitch, to show what the creator program or UGC-style series would look like. Label `COMP`.

1. Look: handheld phone, selfie or POV hands, available light (`image-direction-reference.md` §9.7–9.9). Native-audio models (Seedance 2.x, Veo 3.1, Kling 3.0) put the line in the character's mouth. Wrap dialogue in double quotes.
2. A synthetic person is a **character demonstrating the product**, captioned as a generated comp in the pitch. Its script is the brief for the real creator, not a testimonial: no claims of ownership, time of use, results or feelings ("I've used it for three months", "my skin cleared up"). Those come from real customers or creators with releases.
3. Talking-head avatars (HeyGen Avatar 4, Omnihuman) need an audio file and may not be exposed through the MCP. Check during the first-connection checklist.
4. The production plan beside the comp names who will actually make it (creator roster, casting, shoot).

**Stops it:** client rules against synthetic people in pitches, or a script that reads as a real customer's testimony.

## G. Consistent synthetic talent across a set

**Fits:** a campaign or carousel that needs the same person in many frames.

1. Create an **original** character. Never a real person's likeness, and never a real person altered into someone else (changing someone's nationality or ethnicity, aging a real face). Watch for costume-and-postcard shorthand (visual-craft cliché).
2. Hold the character with a reference image or Character Sheet (Toolkit References; MCP exposure unverified) or a start frame, plus a Style Kit. Name it `<client>-<campaign>-<character>`.
3. Vary shot size and angle across the set, not the style (`image-direction-reference.md` §2).

**Stops it:** any input photo of a real person without a model release on file.

## H. Coverage: several angles of one scene

**Fits:** storyboards, carousel card sets, and cutdown coverage.

1. Lock the scene from one approved frame. Upload it as the reference in every prompt.
2. Prompt one angle per generation: wide, medium, close, detail, reverse, overhead. Keep camera height and light direction consistent unless the change is the idea.
3. For video, one camera move per clip. Multi-shot models (Kling 3.0) can cut inside one generation when the beats are short.

## I. Localization

**Fits:** when a market version is part of the brief. The translated script comes from a native-speaker source. WordSmither writes in English only (V1), so a translation is marked UNVERIFIED until a native speaker reviews it.

| Localize | How | Through the MCP? |
|---|---|---|
| Voiceover | Text-to-speech in the target language (Eleven Multilingual v2 for coverage, Cartesia for accents). Keep one voice across markets where it exists | Yes |
| Visual context | Regenerate settings, wardrobe and props for the market from the same prompt skeleton (Pricken context shift) | Yes |
| On-image text | Set in Figma per market, never generated | n/a |
| Dubbing existing video | HeyGen Translate v2 (175+ languages, with lip-sync) or ElevenLabs Dubbing (voice kept, no lip-sync) | **No, Toolkit website** |

**Stops it:** no reviewed translation; cultural claims nobody in the market has checked.

## J. Music beds and temp tracks

1. Prompt: genre and era + instruments + mood + exact BPM + vocal profile or "instrumental" + structure + use ("15 s social, hit on 0:12 for the end card").
2. Lyria 3 for 30 s tests; Lyria 3 Pro for structured 1–3 min beds. Upload the key visual as a mood reference when words fall short.
3. No artist or song names (blocked). No stems or SFX, so sound design comes from the video models' native audio or the edit.

## K. "Full campaign from a product": the CreativeEngine version

Artlist's one-shot campaign becomes this sequence, each step owned:

1. BriefMachine → packet. CreativeDirector → mode and route.
2. DesignChamp + WordSmither → concept sentence, lines, scripts, hooks.
3. Artlist → recipes A–J for the decided concept, drafted cheap, then rendered.
4. Figma and Adobe → type, layout, sizes, cuts.
5. CreativeDirector → JUDGE. Only then pitch-quality renders, credited per `run-log.md` → Attribution.
6. After the pitch, production makes the real assets: shoot, licensed footage, real talent, recorded voiceover.
