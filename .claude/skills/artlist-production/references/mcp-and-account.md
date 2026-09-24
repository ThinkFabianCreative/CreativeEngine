# Artlist MCP and account

Facts from Artlist's help center and Terms of Use, read 2026-09-24. The MCP article was last updated 2026-08-27 and the connector is in **beta**, so check the current article before relying on a limit.

Sources: [Artlist MCP article](https://help.artlist.io/hc/en-us/articles/38948588333469), [AI Toolkit help category](https://help.artlist.io/hc/en-us/categories/33334424159005-AI-Toolkit), [Terms of Use](https://artlist.io/help-center/privacy-terms/terms-of-use/).

## Connecting

Server URL: `https://mcp.artlist.io/mcp` (remote, HTTP). Sign-in is OAuth with the Artlist account. Never ask for or enter credentials.

| Client | Steps |
|---|---|
| Claude desktop / claude.ai | Settings → Connectors → Add custom connector → paste the URL → sign in with Artlist and approve. If you connected from a link, relaunch Claude Desktop |
| Claude Code (CLI) | `claude mcp add --transport http artlist https://mcp.artlist.io/mcp`, then authenticate from `/mcp` in an interactive session |

It isn't in Claude's connector directory (checked 2026-09-24), so add it as a custom connector. If the connection times out on a managed network, IT needs to allow `mcp.artlist.io`. Tools load under the connector's name. Find them with ToolSearch `artlist`.

## What the MCP can and can't do

| Supported through the MCP | Not through the MCP (Toolkit website only, or not at all) |
|---|---|
| Text-to-image, image-to-image (uploaded image or earlier generation as reference) | Video-to-video: Kling O3 Video Edit, Kling 3.0 Motion Control, Seedance reference-video, Gemini Omni edits |
| Text-to-video, image-to-video | Lip-sync on existing footage (Lipsync v2 pro) |
| Text-to-speech, speech-to-speech | Dubbing and translation (HeyGen Translate v2, ElevenLabs Dubbing) |
| Voice cloning from a sample; listing voices, including cloned ones | Catalog search (stock music, footage, SFX) |
| Listing models and their settings | Unlimited generations. **Every MCP call costs credits**, even on Unlimited plans |
| Style Kit: apply a saved kit by name (image and video, model-dependent) | Creating or editing Style Kits (done in the Toolkit) |
| Checking generation status; download links | Cancelling a generation once started |
| Music generation (Lyria 3, Lyria 3 Pro) | SFX-only generation, music stems, song references |

**Unverified until the first connection:** whether the MCP exposes References (Character, Location, Prop), avatar models (image + audio → video), Seedance 2.5 Draft Mode, negative prompts, and outputs-per-request. Record the answers below.

## Limits and behavior

| Item | Value |
|---|---|
| Rate limit | 120 requests per minute per account, all tools combined |
| Parallel generations | Set by plan (for example 8, 10 or 12 at once) |
| Billing | Credits deducted at request, from the same pool as the Toolkit website. No refunds for unwanted results |
| Failures | An error that says "No credits were used" didn't charge. Content-filter blocks, "high demand" and expired uploads say so |
| Prompts | Sent through as written, with no rewriting by the MCP. Artlist may still screen or alter inputs for policy |
| Returns | Images under 500 KB show inline. Larger images, all video and all voiceover come back as download links |
| Output formats | Images JPEG · video MP4 · voiceover MP3 · music WAV 48 kHz 16-bit |
| Video length | Model-dependent: 4–15 s for most models, up to 20 s (Flux 3) and 30 s (Seedance 2.5). Longer pieces are stitched in the edit |
| Storage | Artlist says it isn't a storage service and gives no retention guarantee. After a subscription lapses, image and video outputs can no longer be downloaded. **Download everything into the project the same day** |

## Upload rules (inputs)

| Input | Rule |
|---|---|
| Reference images | Any format (converted). **No transparency**: a PNG with an alpha channel fails, so export as JPEG. At least 0.5 MP (1 MP+ recommended), under 10 MB, aspect ratio between 0.4:1 and 2.5:1 (9:16 = 0.56 passes; 1:4 fails). Clear, front-facing, well-lit subjects keep consistency best |
| Images per request | Model-dependent: Nano Banana Pro / 2 up to 14, GPT-Image-2.5 up to 16, Seedream 5.0 Pro up to 10, Seedance 2.5 up to 30 |
| Style Kit | Up to 2 reference images, a palette and guideline text. One kit per generation. Our own references override the kit's |
| Speech-to-speech source | MP3, WAV or OGG, up to 30 MB, up to 5 min |
| Voice clone sample | MP3, WAV or M4A, 10 s to 5 min, up to 20 MB, one clear speaker. The uploader confirms permission |
| Voiceover text | Up to 5,000 characters per generation |

## Rights and terms that affect agency work

CreativeEngine uses Artlist output for inspiration and pitch only, never commercially (Andres, 2026-09-24). The commercial rights below are context, not a plan.

- **Outputs.** Artlist assigns its rights in the output to the account holder and doesn't restrict commercial use, including ads and client projects, even after the subscription ends. It doesn't guarantee that output is unique, original or non-infringing, and similar output may be generated for other users.
- **Explore and Catalog AI content is different.** AI content downloaded from the Toolkit's Explore page or the Catalog is an *Asset* under the Asset license. It can't go into new projects after the subscription ends.
- **Data.** Inputs and outputs are shared with third-party model providers. Most are contractually barred from training on them, but some models may train on data. The Toolkit marks those with an info icon, and the MCP listing may not show that mark. For confidential client inputs, check the model in the Toolkit first or choose another.
- **Forbidden uses that matter for advertising** (paraphrased; read the Terms for the full list):
  - Content that misleads, including presenting output as authentic or human-made.
  - False advertising or consumer-protection violations.
  - Real people, brands or entities without the necessary rights or consents.
  - Deepfakes or look-alikes of any real person, and deceptive voice clones or avatars.
  - Music or vocals that imitate a real artist's voice, persona or distinctive style (the same clause also names "other Output").
  - Output that gives rise to a trademark claim.
  - Protected health information as input.
  - Using the faces or voices of people in Artlist's stock Assets to build look-alikes.
- **Account responsibility.** The account holder is responsible for violations by employees, contractors and clients using the subscription's outputs. Artlist can ask for proof of rights to any input.

## First-connection checklist

Run this once when the connector first loads, and date the results here. It turns the unverified rows above into facts.

1. List the tools. Record their exact names and what each one does.
2. List the image, video, voice and music models with their settings. Compare them with `models.md` and note what's missing or new.
3. Check the credit balance, plan tier and which asset types the plan includes. Some plans are voiceover-only.
4. List the Style Kits. Confirm they follow `<client>-<campaign>` naming and that no kit mixes clients.
5. Test one cheap text-to-image (for example Z-Image Turbo 1K, about 10 credits) with the user's approval, to learn the request → status → download cycle.
6. Check whether References, avatar models, Draft Mode, negative prompts and outputs-per-request are exposed.

```
FIRST CONNECTION: [date] · by [who]
TOOLS:            [names]
PLAN / CREDITS:   [tier] · [balance] · asset types: [image, video, voice, music]
KITS:             [names]
EXPOSED:          References [y/n] · avatars [y/n] · Draft Mode [y/n] · negative prompt [y/n] · outputs/request [n]
```

## Troubleshooting

| Symptom | Fix |
|---|---|
| No Artlist tools load | Connector not added or not authorized. Re-add it with the exact URL, then relaunch |
| Sign-in loops | Use the same Artlist account as the Toolkit website. Check the SSO session |
| "Inappropriate content" block | No credits used. Rephrase, or replace the reference image. Filters misfire, so check that the prompt names no real person or brand |
| Stuck "in progress" or at 99% | Provider overload. Wait a few minutes, then try another model. Don't re-submit the same job blindly |
| Upload rejected | Transparency, size, or a ratio outside 0.4–2.5. Re-export as JPEG and crop |
| Kit not applied | Kit missing, or the model doesn't support kits. List the kits, then switch model |
| Rate-limit error | Over 120 requests/min. Wait one minute and batch smaller |
