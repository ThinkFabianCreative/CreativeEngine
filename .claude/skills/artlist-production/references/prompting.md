# Prompting on Artlist

The MCP sends prompts through as written, so the model reads exactly what we write. Stills use the anatomy in `DesignChamp/knowledge/image-direction-reference.md` §5; this file doesn't repeat it. It adds what video, multi-reference, voice and music need. Sources: Artlist's prompt, video, voiceover and music help articles and model pages (read 2026-09-24).

## Stills: Artlist specifics

- **Exclusions:** put them in the model's negative-prompt setting where the model offers one, and keep a short EXCLUDE line in the prompt as well.
- **References:** say what each reference is for. "Keep the product in @Image1 unchanged; match the grade of @Image2." Our references override a Style Kit's.
- **Length:** text-to-image prompts cap at about 2,000 characters on some models. Short and physical beats long and adjectival.
- **Faces and hands:** state age, pose and light. Prefer waist-up or chest-up framing. Higher resolution reduces distortion.

## Video prompt anatomy

Write one clip as one event.

```
1. START        text-to-video: the opening frame in one sentence
                image-to-video: "@Image1 is the first frame." Describe only what changes
2. ACTION       one action, present tense, active verb, small and physical
                ("she lifts the portafilter and taps it once")
3. CAMERA       one move: locked off · slow push-in · tracking back · handheld drift ·
                orbit left. Name the lens feel if it matters (35mm, shallow focus)
4. TIMING       duration; for multi-shot models, the shots in order with rough seconds
5. SOUND        what we hear, named: room tone, the grinder, rain on glass.
                Dialogue in double quotes: "Okay, this is the good part."
6. LOOK         grade, light, film or digital, from the still's anatomy
7. EXCLUDE      negative prompt: text, logos, extra people, morphing hands
8. SETTINGS     ratio, resolution, duration, audio on/off, quality tier
```

**What works:**
- Small, natural motion. A look over the shoulder, a pour, a hand turning a dial. Choreography, acrobatics and crowds glitch.
- Short clips, stitched. Consistency drifts with length, so plan 4–8 s beats and cut them together.
- Mid-shots for people. Wide full-body shots multiply limb errors.
- Keep the anatomy readable. Arms away from the torso, face uncovered, feet visible or cleanly cropped.
- Name the sound. Quiet, low-motion scenes come back silent unless the prompt asks for a sound (Flux 3 says so explicitly; it holds elsewhere too).
- Speech in other languages: Veo 3.1 speaks any language. Kling 3.0 covers English, Chinese, Japanese, Korean and Spanish. Check the model before scripting.
- Prompt limits: Kling 2,500 characters, Seedance 5,000.

**First and last frame** (Veo 3.1, Flux 3, Gemini Omni, Kling 3.0 Standard image-to-video): use it when the landing frame matters, for reveals, before-and-after, and a product resolving into the end-card position. Make both frames with the same model and grade.

## Multi-reference tagging

Seedance 2.x, Kling O3 and Gemini Omni accept several references tagged in the prompt. Give each reference **one job**:

| Job | Wording |
|---|---|
| First frame | "Set @Image1 as the first frame." |
| Identity | "Keep the appearance of @Image2 throughout." |
| Product | "The product in @Image3 stays exactly as shown." |
| Motion | "Imitate the action of @Video1." |
| Camera | "Follow the camera movement of @Video1." |
| Rhythm | "Cut to the beat of @Audio1." |

Limits: Seedance 2.0 takes up to 9 images, 3 video clips (15 s total) and 3 audio files. Seedance 2.5 takes up to 30 images, 10 clips (30 s total) and 10 audio files. Reference-video inputs may be website-only (`mcp-and-account.md`).

## Voice

Scripts come from WordSmither. Formatting for the voice models:

| Need | Write |
|---|---|
| Natural phrasing | Short sentences. Group phrases in brackets: `[First coffee.] [Last train.]` |
| Direction (Eleven v3) | A tag before the line: `[calm] Take your time.` or `[fast] Ends Friday.` |
| Short pause | A comma or a dash |
| Long pause | `<break time="1s" />` (native accent) · `<#1.0#>` (non-native accent) |
| Questions | Two question marks: `Still reading??` |
| Numbers and dates | As spoken, or broken up: "January 26th, 2026"; long strings `<spell>4454AB</spell>` |
| URLs and symbols | As spoken: "example dot com slash start", "hashtag" |
| Brand names | Phonetic spelling when the model mispronounces them. Keep a pronunciation line in the project |

- Match the language setting to the text. Never quote for emphasis; use punctuation.
- Generate by section for pacing, and assemble in the edit.
- Pick one model per campaign, because voices change between models. Lower stability gives more expression but less consistency across takes.
- Up to 5,000 characters per generation.

## Music

Formula: **genre and era + instrumentation + mood and energy + exact BPM + vocal profile (or "instrumental") + structure + use.**

```
Late-1970s soul instrumental, dry drums, warm Rhodes, muted guitar, bass-led groove.
Confident, unhurried, 92 BPM. Instrumental. Builds from bass and drums to full band
by 0:08; clean stop at 0:14 for a one-second end card. For a 15-second vertical
social ad with voiceover on top: leave room in the mids.
```

- An exact BPM makes cuts easy to sync.
- Describe the sound, never the artist. Artist and song names block the generation.
- Lyria 3 (30 s) often starts and ends abruptly. Use Lyria 3 Pro when the track needs a real start and ending.
- An image reference (the key visual) works as a mood anchor.

## Style Kit

- Created in the Toolkit (not through the MCP). Up to 2 reference images, a palette and guideline text.
- Name it `<client>-<campaign>`. Guidelines hold the look (grade, light, texture, exclusions), never client facts that would leak into another job.
- Apply it by name in the request. One kit per generation. Our own references fill slots before the kit's.
- Video support depends on the model. If the kit doesn't apply, pass the grade reference image directly.
