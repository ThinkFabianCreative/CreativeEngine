---
name: artlist-production
description: Generate inspiration and pitch material through the Artlist MCP (images, video, voiceover, music) once the idea is decided. Covers comps and placeholders, shoot pre-viz, animatics with temporary voiceover and music, hook-variant comps, product-in-context comps, creator-style comps and localized voiceover. Never for commercial use. Use when a decided idea needs to be seen or heard for a pitch or internal review, or when the user mentions Artlist. Every call spends Artlist credits and can't be cancelled, so quote the cost and get approval first. Not for finding ideas.
---

# Artlist production

Artlist's MCP puts about 100 image, video, voice and music models on one credit account, called straight from the conversation. In CreativeEngine it sits after the idea and before the finishing tools. Here it renders a decided concept as a rough, a comp, a pre-viz frame or an animatic. Type, layout, resizing and the edit happen elsewhere.

**Inspiration and pitch only** (Andres, 2026-09-24). Nothing generated here is used commercially: no ad, post or client deliverable runs a generated asset. It shows the idea. Production makes the real thing: a shoot, licensed footage, real talent, recorded voiceover.

This skill is method. DesignChamp owns image and motion judgment. WordSmither owns every word: scripts, voiceover, hooks, lyrics. CreativeDirector owns selection and decides what is worth spending on in JUDGE.

## Where it sits in the flow

```
BRIEF → PACKET → CONCEPT SENTENCE (Barry §1) → ROUGH TEST (Barry §2)
                                                    │
                                   Artlist: render the decided idea
                                   (still · motion · voice · music)
                                                    │
               Figma: type, layout, supers    Adobe: resize, reframe, cut, fix
                                                    │
                          review (work/reviews/) → outputs/review/
```

| Mode | What Artlist is for | Default label | Default fidelity |
|---|---|---|---|
| **EXPLORE** | A rough of an idea that already exists, to see whether it reads. Mood only | `MOOD` | Cheapest model, 1K / 480p, 1–2 outputs |
| **DEVELOP** | Comps, placeholders, pre-viz for a shoot, animatics with temporary voiceover and music, hook variants | `COMP` · `PRE-VIZ` · `TEMP` | Mid-tier model; the set locked to one model, kit and grade |
| **JUDGE / pitch** | Pitch-ready comps and motion tests, at real size in context (with `format-prototyping`) | `COMP` | High-quality render of only the frames CreativeDirector picked |

There is no production row. A generated file never becomes the delivered asset.

## Routing: Artlist or another tool in the stack

| Job | Use | Why |
|---|---|---|
| Video, image-to-video, animatics, native sound, voiceover, music | **Artlist** | The only tool in the stack that does motion, voice and music together |
| Stills that must live inside Adobe files, canvas extension, Generative Fill fixes, clients who require Adobe provenance | **Adobe Firefly / Photoshop tools** | See `image-direction-reference.md` §6 |
| A flow already built in Figma Weave, or frames that live in Figma | **Figma Weave** | Keeps the work in Figma; it has its own cost quote |
| Type, supers, layout, end cards | **Figma**, never the generation | `typography.md`; models garble text |
| Platform sizes, reframing, quick cuts, background removal | **Adobe connector** (`video_resize`, `adobe-create-social-variations`, `image_remove_background`, `video_create_quick_cut`) | Finishing, not generation |

Keep one set on one tool and one model. Mixing tools breaks the grade, and matching it afterwards costs more than choosing once.

## Hard rules

1. **The idea comes first.** Never generate to find a concept (Barry §2). Every run names its packet ID and concept sentence. Artlist sells "drop in your product, get a full campaign." CreativeEngine doesn't work that way: the campaign comes from the brief and the department, and Artlist executes it.
2. **Inspiration and pitch only.** Every output is labelled as a generated comp and stays in internal review or pitch material. It never goes into `outputs/approved/` or `outputs/delivered/`, never runs in media, and never ships to a client as a usable asset. The pitch shows how production will make the real thing.
3. **Client rules outrank everything.** Before the first run on a client, look for the client's rules on generated imagery, people and voices in `normalized-brief.md` and `client/knowledge/`. If none are recorded, AI use in pitches is **OPEN**: generate for internal review, and ask before showing it to the client. Where a client forbids generated people or imagery, that holds for internal comps too.
4. **Quote, then confirm, every time.** Credits are deducted when the request is made. A run can't be cancelled or refunded, and the MCP has no quote step of its own. Unlimited plans don't apply through the MCP. Before each batch, show the model, settings, count and estimated credits (`references/models.md`), plus the files to download, and wait for an explicit yes. One approval covers one batch.
5. **Draft before you render.** Prove one cheap output (one image, or a 480p or 5-second draft) before a batch or a high-quality render. Don't re-submit a job that's still in progress, because that spends twice.
6. **Upload only what the project has rights to.** Allowed: client-supplied product photos, approved client assets and our own generations. Never upload a real person's photo or voice without a release on file. Never clone a voice without the speaker's written permission. No competitor brands. Inputs go to third-party model providers, so check with the user before uploading unreleased or confidential client material.
7. **Isolation holds inside Artlist too.** Style Kits and References are shared across the whole account. Name them `<client>-<campaign>` and never apply one client's kit or reference to another client's work.
8. **Never generate type, logos, prices, labels, badges or claims.** Set them in Figma. If a model invents any of them (for example a price tag or brand label on a product), regenerate. Don't retouch it away. A generated product must match the real one (shape, color, count, pack, label) so the pitch doesn't promise a product that doesn't exist.
9. **Synthetic people are shown as synthetic.** A creator-style comp may show a synthetic person using the product. In the pitch it is labelled a generated comp, never presented as a real customer, review or testimonial. The production plan names real creators or customers with releases.
10. **Label, log, keep locally.** Every file carries its label in its name and in Figma. Every run is logged (`references/run-log.md`). Artlist isn't a storage service and downloads stop when a subscription lapses, so download results into the project's `work/generated/` the same day. Those media files are gitignored and stay on the local machine; the committed log references them.
11. **Artist names stay in prompts, for accuracy.** Name the photographers, directors and artists whose style the reference needs, plus the technical translation (`image-direction-reference.md` §1, §8). Accuracy of the style reference matters. Record every name in the log, and credit each referenced artist in the pitch document (`references/run-log.md` → Attribution). Andres acknowledges Artlist's terms on style references himself (2026-09-24). Music models reject artist and song names, so music prompts describe the sound. If a visual prompt is blocked, rerun with the translation only and note it in the log.

## Procedure

**0. Check the connector.** Run ToolSearch for `artlist`. If no tools load, stop and give the user the connection steps in `references/mcp-and-account.md`. Never ask for credentials. On the first connection, run the first-connection checklist in that file.

**1. Frame the job** in six lines:

```
PACKET / CONCEPT:  P2 · "[concept sentence]"
MODE / LABEL:      DEVELOP · COMP
ASSET JOB:         what this output must prove or do
FORMAT / RATIOS:   placement(s) and ratio(s), from the packet and shared/knowledge
CLIENT AI USE:     rule found (source) / OPEN → internal review; ask before pitching
STYLE REFERENCES:  artists named in the prompts (credited in the pitch)
```

**2. Choose the recipe and model.** Recipes: `references/recipes.md`. Models and credits: `references/models.md`. Confirm the model is still offered by asking the MCP for its model list, because the catalog changes monthly.

**3. Write the prompts and save them before spending.** Stills use the prompt anatomy in `DesignChamp/knowledge/image-direction-reference.md` §5. Video, voice and music use `references/prompting.md`. Scripts, voiceover and hooks come from WordSmither (`format-copywriting`, `narrative-craft.md`). Save to `work/image-prompts/` or `work/motion/` as a versioned file.

**4. Quote and confirm.**

```
ARTLIST RUN · <project> · <packet> · <date>
| # | Asset | Model · settings | Count | Est. credits |
|---|---|---|---|---|
| 1 | P2-A key visual draft | Nano Banana 2 · 1K · 4:5 | 2 | 180 |
| 2 | P2-A motion draft | Seedance 2.0 Mini · 480p · 5 s · 9:16 · audio | 1 | 350 |
TOTAL ≈ 530 credits · downloads: 3 files to work/generated/P2/
Kit: <client>-<campaign> · Uploads: P2-A_comp_v02.jpg (ours)
Approve?
```

**5. Run the draft, review it, then run the batch.** Poll the status. Report failures as they come. An error that says "no credits were used" didn't charge; anything else may have.

**6. Download and log.** Save into `work/generated/<packet>/` (local only; gitignored) with versioned names (`references/run-log.md`), for example `P2-A_key-visual_COMP_nb2-2k_v01.jpg`. Add each file to the project's `work/generated/generation-log.md` (committed), including the artists referenced.

**7. Review before anyone sees it.** Run the checks in `image-direction-reference.md` §6 (every generated image) and §10 (finishing), the product-fidelity and synthetic-people checks above, and for video: hands, faces, and object continuity across the clip, plus whether the sound lands on the action. Regenerate rather than retouch forbidden content.

**8. Hand off to the pitch.** Stills go to Figma: record them in `figma-links.md`, with type set there. Motion goes to the edit, with supers and end card added in post. Resize and reframe with the Adobe connector. Every pitch page or deck that shows a generated comp carries the label line and the artist credits (`references/run-log.md` → Attribution). Pitch exports in `outputs/review/` embed or link the comps; the media files themselves stay in `work/generated/`.

## Report format

```
ARTLIST RUN REPORT · <project> · <date>
Spent: <n> credits of <n> approved · Log: work/generated/generation-log.md
| File | Label | Model | Credits | Style references | Note (what it proves / what failed) |
Pitch credits: Style references: <Name>, <Name>
Next: [regenerate / hand to Figma / hand to edit / needs CD review]
```

## What this skill does not do

- Find ideas, choose between concepts or approve work. That belongs to the department and CreativeDirector.
- Edit existing video through the MCP. Video-to-video, lip-sync on existing footage and dubbing are Toolkit-website jobs (`references/mcp-and-account.md`).
- Make commercial assets. Everything it makes is inspiration or pitch; production makes the real thing.
