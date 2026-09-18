# Image direction reference

> DesignChamp knowledge. Vocabulary and practice for directing photography and image generation: photographic styles, camera angles and lenses, light, prompt anatomy, and how the main generation models differ. Supports `shared/frameworks/visual-craft.md` §5 and `barry-concept-art-direction.md` §2, §6. Holds no client facts. Written 2026-09-17.

**Order of authority.** The concept (Barry §1) → the image argument (Barry §6) → the client's photography rules → this reference. Generation tests a decided idea; it never finds one (Barry §2). Where a client or brief forbids generated people or imagery, that rule wins everywhere, including internal comps.

**Model facts go stale.** Section 6 describes the generation models as they're generally known at the time of writing. Features, terms and quality change often: check the current tool before relying on a capability, and check the provider's terms for commercial use before any generated image goes near client work.

---

## 1. Photographic styles

Pick the style for what the image must argue, then describe it in words the model or photographer can act on. Photographers and directors are excellent **references for the team** (section 8), but prompts use the **technical translation** of what makes their work look the way it does: light, lens, aperture, grade, film stock. "In the style of [living artist]" imitates a person's signature work, is blocked or ignored by many models, and produces pastiche.

| Style | What it argues | Recognizable by | Watch for |
|---|---|---|---|
| **Documentary / reportage** | This is real; we were there | Available or practical light, imperfect framing, lived-in detail, grain | Staged "documentary" that's too tidy |
| **Documentary still life** | The evidence of a life, without the person | Objects left mid-use, one practical light, a sense of minutes ago | Props arranged like a shop window |
| **Editorial still life** | This object matters; look closely | Deliberate arrangement, controlled light, a strong graphic idea | Product hero in a void (Barry §10) |
| **Environmental portrait** | This person, in their world | Subject in context, eye level, natural light | Stock poses, eye contact and a smile at camera |
| **Street / candid** | Life as it happens | Motion, layers, chance juxtapositions | Needs releases; generated "candid" looks staged |
| **Studio product** | Precision, desirability | Seamless backgrounds, sculpted light, reflections controlled | Sterile, category-generic |
| **Flash / direct flash** | Immediacy, humor, rawness | Hard frontal light, dark falloff, saturated color | Trend surface without an idea |
| **Cinematic** | A story is happening | Wide ratios, motivated light, color contrast, depth | Teal-and-orange grade, "movie still" cliché |
| **Minimal / graphic** | One idea, nothing else | Big negative space, a single subject, flat light | Emptiness with no pointer |

**Style is also a grade.** Contrast, saturation, color temperature, grain and the color of the shadows are part of the style. Specify them, don't hope for them.

## 2. Camera angle and height

Viewpoint decides whose experience the picture is.

| Angle | Camera | What it says | Use for |
|---|---|---|---|
| **Eye level, standing** | About 1.6 m, lens level | Neutral, "I'm in the room" | Wide scenes, environments, people in context |
| **Eye level, seated** | About 1.1–1.2 m | Intimate, at the table with it | Tabletop still lifes, desk scenes |
| **High angle (30–45°)** | Above, tilted down | Overview, the whole arrangement, slight distance | Tables of objects where every item must read |
| **Overhead / flat lay (90°)** | Straight down | Graphic, catalog, organized | Pattern and layout ideas. A social-media cliché when used by default; loses the room |
| **Low angle** | Below the subject, looking up | Power, scale, monument | Making something small feel heroic, sparingly |
| **Worm's eye** | At floor level | Drama, strangeness | Rarely; very noticeable |
| **Over the shoulder** | Behind a person | Their point of view | Scenes with people; not for person-free work |
| **Dutch tilt** | Rotated horizon | Unease | Almost never in advertising; reads as an error |
| **Straight-on (frontal)** | Parallel to a wall or object | Order, formality, deadpan | Symmetrical, deadpan compositions |

**Shot size.** Wide (the whole place), medium (the group of objects and some room), close (one or two objects), detail or macro (a texture, a mark, a single element). A campaign set gets variety by mixing shot sizes across executions, not by changing style.

**Horizon and camera height stay consistent across a set** unless the variation is the idea.

## 3. Lens, focus and depth

| Lens (full-frame equivalent) | Character | Use for |
|---|---|---|
| 24–28 mm | Wide, context, some distortion near edges | Rooms and environments; keep verticals straight |
| 35 mm | Natural, documentary, "a person standing there" | Wide and medium scenes |
| 50 mm | Neutral, close to how the eye crops | Medium and tabletop |
| 85 mm | Compression, isolation, soft background | Close details, portraits |
| 100 mm macro | Texture, detail, intimacy | Detail cards, materials |

- **Shallow depth (f/1.8–2.8):** one thing is sharp and the world falls away. Directs attention; can feel intimate or precious.
- **Deep depth (f/8–11):** everything reads. Documentary, informational, flat.
- **Focus is the focal point.** Put the sharp plane on the thing the idea needs, not the nearest object.

## 4. Light

Light sets the feeling faster than anything else in the frame.

- **Source:** practical (a lamp, a doorway, a screen, a work light in the scene or just out of it), window, overhead, studio. Practical light reads as real.
- **Quality:** hard (crisp shadows, drama, midday, flash) or soft (gradual shadows, calm, overcast, bounced).
- **Direction:** side (texture, form), back (silhouette, rim), front (flat, frank), below (unusual, uneasy), top (institutional).
- **Ratio:** how dark the shadows are against the light. High ratio (8:1 and above) is low-key and dramatic; low ratio is bright and even.
- **Color temperature:** warm (tungsten, evening), neutral (daylight), cool (shade, screens, fluorescent). Mixed temperatures read as real life; one controlled temperature reads as designed.
- **Keep bright areas out of the type zone.** Where type will sit, the photo has to be dark (or light) and plain already (visual-craft §5).

## 5. Prompt anatomy (for any model)

Write the prompt as a shot list, in this order. Short, concrete sentences beat long lists of adjectives.

```
1. SCENE        where, when, what just happened
2. SUBJECT      the key objects (or person), specific and physical
3. SHOT         shot size, angle, camera height, lens, focus
4. COMPOSITION  where the subject sits; which area stays empty and dark for type
5. LIGHT        source, direction, quality, temperature
6. GRADE        shadow color, highlight color, saturation, grain, film or digital
7. STYLE        the photographic genre (section 1) and the technical translation of any
                reference (section 8): light, lens, aperture, grade, film stock
8. EXCLUDE      what must not appear
9. RATIO        the aspect ratio, set in the tool's settings where possible
```

- **Physical beats abstract.** "A scuffed white hard hat" works; "a sense of hard work" doesn't.
- **One scene per prompt.** Generate ratios separately rather than cropping one into another.
- **Say where things are.** "In the lower middle, right of center; the top 40% dark and plain" controls composition better than "leave space for text".
- **Exclusions:** most models follow "no X" only partly, and some ignore it. Use the model's own exclusion field or parameter where it has one; otherwise keep exclusions short and specific, and regenerate rather than retouch.
- **Text never goes in the image.** Set it in design software. Models garble text, and even when they don't, the type decision belongs to `typography.md`.
- **Generate several, choose one.** Choose by the idea and the empty type zone, not by the prettiest render.

## 6. Generation models: how they differ

At the time of writing. Verify current features, and check the governing skill record and the client's rules before any use on client work. On client work, confirm each run and name the provider and what is sent (the `identity-design` record sets this pattern).

| Model | Generally strong at | Generally weak at | Notes |
|---|---|---|---|
| **Adobe Firefly** (web app, and Generative Fill / Expand in Photoshop) | Clean photoreal scenes; working inside Adobe files; extending a canvas (Generative Expand) to add dark space above a subject; reference images for style and structure | Complex object interactions, precise small details; can look "stock" | Adobe states it is trained on licensed and public-domain content and positions it for commercial use; attaches Content Credentials. Aspect ratios are limited (commonly 1:1, 3:4, 4:3, 16:9, 9:16): generate 3:4 and crop to 4:5 |
| **OpenAI image generation** (in ChatGPT and the API) | Following long, detailed prompts; placing objects where asked; rendering text; iterative edits in conversation | A glossy, over-clean finish unless the grade is specified; faces can look generic | Useful for comps that need exact arrangement |
| **Google Imagen / Gemini image** | Photorealism, prompt adherence, conversational edits | Can drift toward a polished commercial look | Check which model version the product is using |
| **Midjourney** | Aesthetic quality, mood, lighting, texture, stylization | Literal prompt adherence and exact placement; pushes toward its own "beautiful" look | Parameters such as aspect ratio, reduced stylization ("raw" style) and "no" exclusions. Check commercial terms for the plan in use |
| **FLUX** (Black Forest Labs; several versions, some open-weight) | Photorealism, natural light and skin, prompt adherence | Depends heavily on which version and host | Available through third-party services; terms vary by host and version |
| **Ideogram** | Typography and text in images | Photographic subtlety | Useful for type exploration only; final type is still set by hand |

**Choosing a model.** Pick by the job:
- a comp where arrangement must be exact → a model that follows prompts closely
- a mood or texture study in EXPLORE → a stylized model, labelled as mood
- anything that must live inside Adobe files, or extend an existing photo → Firefly and Generative Expand
- client work with provenance requirements → the model whose training and commercial terms the client accepts, confirmed first

**Every generated image, whatever the model:**
- check hands, text, reflections, shadows, physics and repeated faces
- make sure it implies no real product, place, person or result that doesn't exist
- label it (placeholder, comp or mood) wherever it appears
- keep the prompt, model, date and settings with the file, so it can be traced and replaced

## 7. Directing a real shoot

The same vocabulary briefs a photographer. For each frame, give: the concept sentence, the scene, shot size, angle and height, lens and focus, light (source, direction, quality, temperature), grade, what must be in frame, what must never be, the type zone for every ratio, and the releases needed (people, property, locations). A generated comp is a good brief attachment, labelled as a comp, never as the target look to copy.

## 8. Reference library: photographers, directors, light, lenses, grades

Use the names to align the team, build mood boards and brief a photographer or director ("this, not that"). Put the **translation** in the prompt. Descriptions are of widely known qualities of each body of work, for reference; they are not claims about any specific image. Don't reproduce a specific published photograph or film frame as a client execution (Barry, attribution rules).

### 8.1 Photographers (documentary and fine art)

| Reference | Known for | Prompt translation |
|---|---|---|
| **Stephen Shore** | Deadpan, frontal color views of ordinary American places; large-format, deep focus | Straight-on frontal view, level horizon, deep focus (f/11–16), even daylight, muted natural color, ordinary subject treated with full attention |
| **William Eggleston** | Everyday objects and places in intense, saturated color; odd, democratic framing | Everyday object as the subject, rich saturated but natural color, slightly unexpected framing, flash or late-day light |
| **Saul Leiter** | Painterly color through glass, rain and reflections; layers; spots of red | Shot through glass or reflection, long lens compression (90–150mm), wide aperture, soft layers, one small saturated accent |
| **Todd Hido** | Suburban houses and interiors at night; practical light, fog, long exposures | Night, lit only by practical lamps and windows, long exposure softness, quiet, low-key |
| **Gregory Crewdson** | Staged cinematic tableaux at twilight, many practical lights, deep focus | Blue-hour exterior light mixed with warm interior practicals, deep focus, frozen cinematic moment |
| **Irving Penn** | Precise still lifes and portraits in soft north light; restraint | Soft north-window light, neutral background, sculptural still life, controlled shadow, nothing extra |
| **Wolfgang Tillmans** | Casual intimate still lifes and interiors, window light | Offhand arrangement, natural window light, soft color, intimacy over polish |
| **Rinko Kawauchi** | Luminous everyday details, soft overexposure, pastel light | Airy, slightly overexposed, soft pastel color, tiny everyday detail, square framing |
| **Alec Soth** | Quiet large-format American portraits and interiors, overcast light | Soft overcast light, large-format stillness, muted palette, patient framing |
| **Martin Parr** | Ring flash, saturated consumer culture, humor | Direct ring flash, high saturation, close and frank, comic detail |

### 8.2 Commercial and editorial photographers

| Reference | Known for | Prompt translation |
|---|---|---|
| **Annie Leibovitz** | Painterly, theatrical portrait lighting; rich color | Large soft key light from one side, painterly falloff, rich deep color, staged grandeur |
| **Dan Winters** | Sculpted, dark, low-key portraits and still lifes | Low-key, single hard-edged key light, deep shadows, textured surfaces, precise |
| **Platon** | Close, confrontational portraits, often black and white | Close portrait, slightly wide lens, low camera, hard light, high contrast |
| **Nadav Kander** | Muted, quiet, precise portraits and landscapes | Desaturated muted palette, soft light, stillness, restrained composition |
| **Carl Kleiner** | Graphic, playful still life (known for IKEA's *Homemade Is Best*) | Clean colored background, graphic arrangement, even soft light, playful precision |
| **Tim Walker** | Fantastical, handmade, theatrical fashion sets | Handmade surreal set, theatrical scale, soft painterly light |
| **Juergen Teller** | Raw direct flash, anti-glamour | Direct on-camera flash, unretouched, frank, bright against dark falloff |

### 8.3 Directors and cinematographers (color, light, frame)

| Reference | Known for | Prompt translation |
|---|---|---|
| **Roger Deakins** (DP) | Motivated, naturalistic light from practical sources; restraint | Every light has a visible or implied source, soft practicals, restrained contrast, clean composition |
| **Bradford Young** (DP) | Underexposed, rich low-light images that hold dark skin tones | Underexposed about one stop, rich shadow detail, warm low light, soft contrast |
| **Harris Savides** (DP) | Soft, underexposed naturalism | Soft available light, slightly underexposed, muted color, quiet |
| **Emmanuel Lubezki** (DP) | Natural light, magic hour, wide lenses close to the subject | Natural late-day light, wide lens close to subject, fluid feeling, no artificial fill |
| **Wes Anderson** (director) | Symmetry, frontal staging, pastel palettes, deadpan | Centered symmetrical frontal composition, flat even light, pastel palette, deadpan |
| **David Fincher** (director) | Desaturated green-yellow, controlled low-key, precision | Desaturated, cool-yellow cast, low-key, locked-off precise framing |
| **Wong Kar-wai** with **Christopher Doyle** (DP) | Saturated neon, motion blur, longing | Saturated reds and greens from practical neon, step-printed motion blur, humid night |
| **Stanley Kubrick** (director) | One-point perspective; candlelit scenes in *Barry Lyndon* shot with an f/0.7 lens | One-point perspective, symmetrical depth; or candle-level practical light with extremely shallow focus |
| **Jonathan Glazer** (director, including commercials) | Bold, stark images; Guinness "Surfer" in black and white | Stark graphic image, high-contrast black and white, one bold visual event |
| **Spike Jonze** (director, including commercials) | Handheld naturalism with playful surreal turns | Handheld, natural light, real locations, one surreal moment treated as ordinary |
| **Sofia Coppola** (director) | Soft natural light, pastel, quiet interiors | Soft window light, pastel palette, quiet, still interiors |

### 8.4 Painters used as light references

| Reference | What lighting people borrow | Prompt translation |
|---|---|---|
| **Johannes Vermeer** | Soft side window light falling across an interior | Soft daylight from a window at the left, gentle falloff across the room |
| **Edward Hopper** | Raking light, solitary interiors, long shadows | Hard raking light across a sparse interior, long shadows, stillness |
| **Caravaggio** | Chiaroscuro: one hard source out of darkness | Single hard light from above-side, deep black shadows, subject emerging from dark |

### 8.5 Film stocks and grades (safe, effective prompt vocabulary)

| Stock or grade | Look |
|---|---|
| **Kodak Portra 400** | Warm, natural skin, soft contrast, fine grain |
| **Kodak Portra 800 / pushed Portra** | Warmer, grainier, low-light |
| **Kodak Gold 200** | Warm, nostalgic, yellow-orange |
| **Kodachrome** | Saturated reds and yellows, deep blues, high contrast |
| **Kodak Ektachrome** | Clean, cool, saturated slide film |
| **Fujifilm Pro 400H** | Cool pastel, green-cyan highlights |
| **CineStill 800T** | Tungsten balance, red halation around lights, night |
| **Kodak Tri-X 400** | Classic gritty black and white |
| **Ilford HP5** | Softer black and white, broad tonal range |
| **Bleach bypass** | Desaturated, high contrast, silvery |
| **Day for night** | Blue, underexposed daylight standing in for night |
| **Teal and orange** | Cinematic cliché; avoid unless it's the idea (visual-craft §9) |

### 8.6 Lighting setups

| Setup | Description | Use |
|---|---|---|
| **Practical only** | Lit by lamps, screens or doorways in or just out of frame | Documentary, night interiors, still life with a lived-in feel |
| **North window** | Soft, cool-neutral daylight from one side | Still life, portraits, calm |
| **Rembrandt** | Key at 45° and above; a triangle of light on the shadow cheek | Classic, dramatic portraits |
| **Butterfly (Paramount)** | Key high and in front; shadow under the nose | Glamour, beauty |
| **Split** | Key at 90°; half the face in shadow | Tension, mystery |
| **Rim / backlight** | Light from behind outlining the subject | Separation, silhouette, atmosphere |
| **Hard sun / direct flash** | Crisp shadows, high contrast | Frankness, energy, humor |
| **Bounce / overcast** | Very soft, shadowless | Clean, gentle, informational |
| **Mixed temperature** | Warm tungsten against cool daylight or blue hour | Realism, cinematic depth |

### 8.7 Lenses and apertures

| Choice | Effect |
|---|---|
| 24mm | Wide, environmental, stretches edges |
| 35mm | Documentary, natural, "in the room" |
| 50mm | Neutral, human view |
| 85mm | Compression, isolation, flattering portraits |
| 100mm macro | Detail and texture |
| 135mm+ | Strong compression, voyeuristic distance |
| Anamorphic | Wide cinematic ratio, oval bokeh, horizontal flares |
| Vintage glass (for example Cooke-style) | Softer, warmer rendering, gentle falloff |
| Tilt-shift | Selective focus plane, corrected verticals, or miniature effect |
| **f/1.2–1.8** | Extremely shallow; one plane sharp, dreamlike |
| **f/2–2.8** | Shallow; subject isolated, context readable |
| **f/4–5.6** | Subject and near context sharp |
| **f/8–11** | Most of the scene sharp; documentary, architectural |
| **f/16–22** | Everything sharp; large-format deadpan, landscape |

In prompts, name the lens and aperture as camera facts ("50mm lens at f/2"). Models treat them as a look, not a physics simulation, so check the result, not the number.
