# Files, names, the generation log and attribution

Generated files are working files for inspiration and pitch, never commercial assets (Andres, 2026-09-24). Every file can be traced to its prompt, model, cost and the artists it references.

## Where files go

```
projects/<client>/<project>/work/generated/
  generation-log.md          committed · one log per project, newest run last
  <packet-id>/               local only (gitignored) · one folder per packet
    P2-A_key-visual_COMP_nb2-2k_v01.jpg
    P2-A_motion-draft_COMP_sd20mini-480_v01.mp4
    P2_vo-30s_TEMP_eleven-v2_v01.mp3
    P2_bed-60s_TEMP_lyria3pro_v01.wav
```

- **Media stays local.** The root `.gitignore` ignores everything under `projects/**/work/generated/` except Markdown files. Images, video and audio live on the machine that generated them; the committed log is the reference. A lost local file is regenerated from its logged prompt and settings, or re-downloaded from Artlist while the subscription is active.
- Prompt files stay where the project already keeps them (`work/image-prompts/`, `work/motion/`). The log points to them.
- Pitch exports in `outputs/review/` embed or link the comps. Generated media never goes into `outputs/approved/` or `outputs/delivered/`.

## File names

```
<packet>_<descriptor>_<LABEL>_<model-setting>_v<NN>.<ext>
```

| Part | Values |
|---|---|
| LABEL | `MOOD` · `COMP` · `PLACEHOLDER` · `PRE-VIZ` · `TEMP` (audio) |
| model-setting | Short: `nb2-2k`, `nbpro-4k`, `gpt25sun`, `sd5pro`, `artlist-orig-1080`, `sd25-1080`, `sd20mini-480`, `veo31fast-1080`, `kling30pro`, `flux3-1080`, `eleven-v2`, `lyria3pro` |

Never reuse a version number. A regeneration is a new version, even from the same prompt.

## Log format

```
# Generation log · <client> · <project>

| Date | Packet | File (local) | Label | Model · settings | Inputs (refs, kit) | Style references | Prompt (file · ID) | Credits (est. / actual) | Artlist gen ID | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-09-24 | P2 | generated/P2/P2-A_key-visual_COMP_nb2-2k_v01.jpg | COMP | Nano Banana 2 · 2K · 4:5 · 2 outputs | P2-A_comp_v02.jpg (ours) · kit <client>-<campaign> | <Photographer>, <Director> | work/image-prompts/p2_prompts_v01.txt · P2-A | 260 / 260 | abc123 | kept → Figma |
```

Status values: `kept → <where>` · `rejected: <reason>` · `regenerate: <what to change>` · `failed: <error> (credits used? y/n)` · `names blocked → translation only`.

At the end of each run, add one summary line under the table:

```
RUN 2026-09-24 · approved 530 · spent 530 · by [who approved]
```

## Attribution in pitch documents

Every artist named in a prompt is credited wherever the comp appears in a pitch: deck, board or document.

- **Per comp** (caption under the image or on the slide):
  `Generated comp · style reference: <Name>, <Name> · not for commercial use`
- **Per pitch** (credits page or the last slide), gathered from the log's Style references column:
  `Style references: <Name> (photography), <Name> (cinematography), … Generated comps for pitch and inspiration only; production will be shot, licensed or recorded.`

Spell names exactly as the artist is credited, and use the discipline that describes why they're referenced (photography, cinematography, painting, film grade). The log is the source for the credits page, so a name added to a prompt is added to the log in the same run.
