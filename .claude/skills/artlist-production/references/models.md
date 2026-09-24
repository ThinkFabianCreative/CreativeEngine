# Models and credits

Rate card and capabilities from Artlist's help center, read 2026-09-24 ([image and video credits](https://help.artlist.io/hc/en-us/articles/38815633707421), [voiceover credits](https://help.artlist.io/hc/en-us/articles/37430829289885), [music credits](https://help.artlist.io/hc/en-us/articles/37430797353885), [AI Models section](https://help.artlist.io/hc/en-us/sections/33334550497181-AI-Models)).

**This goes stale.** Artlist adds and retires models monthly. In September 2026 it retired Kling 1.6, Kling 2.1 Master, LTX 2.0 Pro, Sora 2 and Sora 2 Pro. Before quoting a run, confirm the model and its settings through the MCP's model listing, and use the listing's price where it gives one.

**Two prices for one model.** Where the help-center table lists two prices at one resolution, the lower is without native audio and the higher is with it. The table marks audio with an icon, which didn't survive extraction. Confirm in the listing.

**Unlimited doesn't apply through the MCP.** On eligible yearly plans the Toolkit website generates some models (for example Nano Banana 2 at 2K, Seedance 2.0 Mini at 480p) without credits. Large EXPLORE draft volumes on those models are cheaper on the website.

## Stills (credits per image)

| Job | First choice | Alternatives |
|---|---|---|
| **Throwaway rough or mood** | Z-Image Turbo 1K · **10** | Muse · 30 · GPT-Image-2 Low · 40 · Nano Banana 2 Lite · 50 |
| **Comp with references, product in scene, edits** | Nano Banana 2 · 1K **90** · 2K **130** · 4K **200** · up to 14 reference images · the widest ratio set (21:9, 16:9, 3:2, 4:3, 5:4, 1:1, **4:5**, 3:4, 2:3, 9:16, 4:1, 1:4, 8:1, 1:8) | Nano Banana Pro · 1K–2K 160 · 4K 280 · 14 refs · **no 4:5** (1:1, 16:9, 9:16, 21:9, 4:3, 3:2) |
| **Edit-heavy work: one subject kept across many edits** | GPT-Image-2.5 **Sunburst** (precision) or **Flare** (everyday) · Low 90 · Medium 100 · High 170 · XHigh 250 · Max 460 · up to 16 refs · edits stay scoped | GPT-Image-2 · Low 40 · Medium 150 · High 600 |
| **A still that will become a Seedance video** | Seedream 5.0 Pro · 1.5K **75** · 2K **150** · up to 10 refs · outputs are trusted inputs for Seedance 2.x image-to-video | Seedream 5.0 · 100 · Seedream 4.5 · 100 |
| **Cinematic look-dev, pre-viz frames** | Artlist Original 1.0 · 720p **80** · 1080p **160** · 4:3, 16:9, 9:16 · text-to-image only · adjustable "Artlist look" strength · strong on skin and eyes | Flux Pro Ultra · 120 · Imagen 4 · 150 / Ultra 200 |
| **Other photoreal options** | Krea 2 · 75 / 150 · Reve 2.1 · 2K 150 / 4K 400 · Qwen Image 3 · 100 (edit 120) · Luma Uni-1 · 190 (edit 200) · Flux 2.0 Pro · 80 | |
| **Type exploration only** (never final type) | Ideogram V4 · text-to-image only · price in the listing (v3 was 150) | GPT-Image-2 family |

Stills return as JPEG, 1–4 outputs per request (model-dependent). Generate each ratio separately rather than cropping one into another (`image-direction-reference.md` §5).

## Video (credits per second)

| Job | First choice | Alternatives |
|---|---|---|
| **Draft or motion test** | Seedance 2.0 Mini · 480p **70** · 720p 165 · with audio | Gemini Omni 1.1 Flash · 360p 70 · 720p 150 · 1080p 250 · Wan 3.0 · 480p 75 · 720p 150 · Veo 3.1 Lite · 720p 63 / 94 · 1080p 100 / 125 |
| **Hero clip with native sound and many references** | Seedance 2.5 · 480p **300** · 720p 600 · 1080p **1,000** · 4–30 s in one pass · up to 50 refs (30 images, 10 video, 10 audio) · **Draft Mode**: a 480p draft, then the same output rendered at 1080p within 7 days, each billed at its own rate | Seedance 2.0 · 480p 200 · 720p 300 · 1080p 600 · 4K 1,200 · up to 12 refs · dialogue in double quotes lip-syncs |
| **Cinematic prompt adherence, any-language speech** | Veo 3.1 · 720/1080p **250 / 425** · 4K 500 / 750 · 4, 6 or 8 s · first and last frame · Ingredients (character + object + background, 8 s only) · Extend (+7 s) | Veo 3.1 Fast · 125 / 200 · 4K 375 / 500 |
| **Multi-shot scenes, fast or complex motion** | Kling 3.0 Pro · 1080p **100 / 150** · 3–15 s · 1:1, 16:9, 9:16 · several cuts in one generation · voice ID | Kling 3.0 Turbo · 720p 150 · 1080p 180 · Kling O3 · 1080p 350–600 · 4K 500 |
| **One clear event with its sound; first-to-last-frame transitions** | Flux 3 (video) · 720p **220** · 1080p 375 · 5–20 s · 21:9 to 9:21 plus auto · grounding on/off | LTX 2.5 Fast · 720p 170 … 4K 555 · LTX 2.5 Pro · 1080p 315 |
| **Other** | Happy Horse 1.1 · 720p 210 · 1080p 420 · Wan 2.7 · 720p 200 · 1080p 300 · Grok Imagine 1.5 · 480p 200 · 720p 350 · MiniMax H3 · 2K 120 | |

Video returns as MP4. Most models accept only 1:1, 16:9 and 9:16. For 4:5 feed video, compose 9:16 with the subject in the 4:5 safe area and reframe with Adobe `video_resize`.

### Avatars: image + audio → talking video (MCP exposure unverified)

| Model | Credits/s | Notes |
|---|---|---|
| HeyGen Avatar 4 | 175 (720p) | 16:9 only · up to 3 min · gestures follow the voice |
| Omnihuman 1.5 | 200 | Up to 30 s · one speaker · 720/1080p · strong lip-sync, camera movement |
| Fabric 1.0 | 120 (480p) · 220 (720p) | Fast variant 150 / 300 |
| Creatify Aurora | 80 (480p) · 160 (720p) | |

The audio must be a file (a generated voiceover or an upload). Avatar models don't take scripts.

### Toolkit website only (video-to-video)

Lipsync v2 pro · 200/s · HeyGen Translate v2 · 175 (precision) / 100 (speed) · ElevenLabs Dubbing · 1,500 as listed · Kling O3 Video Edit · 600–700/s · Kling 3.0 Motion Control · 700–800/s.

## Voice

| Model | Cost | Use |
|---|---|---|
| Eleven Multilingual v2 | 1 credit per 5 characters | Widest language set, stable delivery |
| Eleven v3 | Check the listing (Eleven v2 is 1 per 5) | Direct the performance with `[bracket]` tags |
| MiniMax 02 HD | 1 credit per 10 characters | Emotion setting |
| Cartesia Sonic 2 (upgraded July 2026) | 1 credit per 10 characters | The only model with an accent setting; emotion setting |
| Voice clone | 500 credits once | Written permission from the speaker first |
| Speech-to-speech | 2 credits per second | Keeps a real read's timing, swaps the voice |

The same voice sounds different on each model. Keep one model per campaign. Output is MP3.

## Music

| Model | Cost | Use |
|---|---|---|
| Lyria 3 | 150 per track | 30 s, often without structure (abrupt start and end). Temp tracks and tests |
| Lyria 3 Pro | 300 per track | 1–3 min, structured. Beds for animatics and pitch films |

Durations: auto, 0:30, 1:00, 1:30, 2:00, 2:30. Vocals or instrumental. Custom lyrics in any language. No stems, no SFX, no audio reference. An image can serve as a mood reference. Output is WAV 48 kHz 16-bit.

## Worked budgets

| Run | Math | Credits |
|---|---|---|
| 5 key-visual comps × 2 options, Nano Banana 2 at 2K | 10 × 130 | 1,300 |
| One 5 s motion draft, Seedance 2.0 Mini at 480p | 5 × 70 | 350 |
| One 15 s hero, Seedance 2.5: 480p draft, then 1080p render | 15 × 300 + 15 × 1,000 | 19,500 |
| 4 hook openings, Veo 3.1 Fast at 1080p with audio, 4 s minimum each | 4 × 4 × 200 | 3,200 |
| 30 s voiceover, about 430 characters, Eleven Multilingual v2 | 430 ÷ 5 | ≈ 86 |
| 60 s music bed, Lyria 3 Pro | 1 track | 300 |

Video dominates spend. Draft at 480p or on Mini/Lite models, and render pitch quality only for frames CreativeDirector has picked.
