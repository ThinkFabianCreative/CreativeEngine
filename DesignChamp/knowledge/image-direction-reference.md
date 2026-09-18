# Image direction reference

> DesignChamp knowledge. Vocabulary and practice for directing photography and image generation: photographic styles, camera angles and lenses, light, prompt anatomy, and how the main generation models differ. Supports `shared/frameworks/visual-craft.md` §5 and `barry-concept-art-direction.md` §2, §6. Holds no client facts. Written 2026-09-17.

**Order of authority.** The concept (Barry §1) → the image argument (Barry §6) → the client's photography rules → this reference. Generation tests a decided idea; it never finds one (Barry §2). Where a client or brief forbids generated people or imagery, that rule wins everywhere, including internal comps.

**Sources.** In-house synthesis of common professional practice. Reviewed external input: Superside, *The AI Image Prompting Guide* (4 pp., 2026-06), reviewed 2026-09-17. Its formula and workflow informed §5 and §10; its advice to name photographers in prompts is adopted (§1, §8).

**Model facts go stale.** Section 6 describes the generation models as they're generally known at the time of writing. Features, terms and quality change often: check the current tool before relying on a capability, and check the provider's terms for commercial use before any generated image goes near client work.

---

## 1. Photographic styles

Pick the style for what the image must argue, then describe it in words the model or photographer can act on. Photographers and directors can be named directly in prompts ("in the style of [name]"), alone or combined with the genre (user direction, 2026-09-18). Pair the name with its **technical translation** from section 8 (light, lens, aperture, grade, film stock): some models block or ignore certain names, and the translation keeps the look when they do. It also lets you keep only the qualities you want from a reference. Style is fair game; recreating one specific published photograph or film frame is not (see section 8).

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
| **POV (first person)** | At the eyes or chest of the viewer-character | "This is you"; immersion, participation | POV video and photography (§9.7); hands may enter frame |

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
5. LIGHT + FEEL source, direction, quality, temperature, and the one feeling it must give
                (visual-craft §1 FEEL): "dramatic shadows, warm late light" tells the model
                how it should feel, not just what it shows
6. GRADE        shadow color, highlight color, saturation, grain, film or digital
7. STYLE        the genre (section 1), reference names (section 8) and their technical
                translation: light, lens, aperture, grade, film stock
8. EXCLUDE      what must not appear
9. RATIO        the aspect ratio, set in the tool's settings where possible
```

- **Physical beats abstract.** "A scuffed white hard hat" works; "a sense of hard work" doesn't.
- **One scene per prompt.** Generate ratios separately rather than cropping one into another.
- **Say where things are.** "In the lower middle, right of center; the top 40% dark and plain" controls composition better than "leave space for text".
- **Exclusions:** most models follow "no X" only partly, and some ignore it. Use the model's own exclusion field or parameter where it has one; otherwise keep exclusions short and specific, and regenerate rather than retouch.
- **Text never goes in the image.** Set it in design software. Models garble text, and even when they don't, the type decision belongs to `typography.md`.
- **Generate several, choose one.** Choose by the idea and the empty type zone, not by the prettiest render.
- **Build in layers for complex images.** Get the scene, composition and light right first with a short prompt; then refine one thing per pass (an object, the grade, the empty type zone) with edits, inpainting or generative fill. Asking for everything at once produces compromises everywhere.
- **Refining the prompt with a language model is fine**, as long as the result still follows this anatomy and the client's rules. Check it before running: rewrites tend to add adjectives, style names and decoration.
- **Wardrobe and material are part of SUBJECT.** Name fabrics, finishes and wear ("scuffed white hard hat", "washed navy cotton") rather than "styled, rich textures".

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

Use the names in prompts, mood boards and briefs. Add the **translation** alongside the name: it steers the model toward the qualities you want and carries the look if a model refuses or ignores the name. Descriptions are of widely known qualities of each body of work; they are not claims about any specific image. **The one line:** don't recreate a specific published photograph or film frame (its particular composition, subject and moment) as a client execution. That's a copyright problem for the client, not a style reference.

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

### 8.2a Fashion photographers

| Reference | Known for | Prompt translation |
|---|---|---|
| **Peter Lindbergh** | Natural, unretouched black-and-white fashion with a cinematic, narrative feel | Black and white, natural light, minimal retouching, real skin texture, candid within a story |
| **Richard Avedon** | Stark subjects against plain white seamless; frank, full-length and close portraits | Plain white seamless background, flat even light, subject isolated and frank, no props |
| **Tyler Mitchell** | Soft natural light, pastel color, joy and tenderness | Soft daylight, pastel palette, relaxed natural poses, warm and hopeful |
| **Helmut Newton** | High-contrast black-and-white glamour with strong, confrontational poise | Hard light, high-contrast black and white, strong poses, urban settings |
| (see also Tim Walker, Juergen Teller in 8.2) | | |

### 8.2b Architectural and interiors photographers

| Reference | Known for | Prompt translation |
|---|---|---|
| **Julius Shulman** | Mid-century modern houses at twilight, deep perspective, interior light glowing against dusk | Blue-hour exterior, warm interiors lit, two-point perspective, straight verticals, long view |
| **Ezra Stoller** | Precise, formal modernist architecture | Corrected verticals, formal symmetry, crisp edges, high clarity, black and white or restrained color |
| **Iwan Baan** | Buildings in use, with people, context and city around them | Architecture with everyday life around it, context over isolation, natural light |
| **Hélène Binet** | Light and shadow on architectural fragments, black and white | Close architectural fragment, raking light, deep shadow, black and white, texture of material |

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

## 9. Genre playbooks

One block per genre: what it argues, how it's lit and shot, the grade, references (team only) and a prompt skeleton. Pick the genre from the image argument (Barry §6), not from the category's habit (visual-craft §6).

### 9.1 Product

| | |
|---|---|
| **Argues** | This object is worth wanting, trusting or understanding |
| **Sub-types** | *Packshot* (clean, catalog, e-commerce) · *hero* (one dramatic image of the product) · *lifestyle* (the product in use, in a real place) · *macro / material* (texture, finish, craft) · *liquid and motion* (pour, splash, frozen action) · *deconstructed* (parts arranged to explain) |
| **Light** | Packshot: large soft sources, controlled reflections, clean gradations. Hero: one shaped key, rim light to separate edges, deep background. Lifestyle: motivated natural or practical light. Macro: raking light for texture. Liquid: hard backlight and short flash duration |
| **Lens / aperture** | 90–120mm for packshots (little distortion); 100mm macro for material; 35–50mm for lifestyle. f/8–16 for packshot sharpness front to back; f/2–4 for hero and lifestyle isolation |
| **Angle** | Packshot: eye level with the product or 15–30° above. Hero: slightly low to give stature. Lifestyle: the user's eye level |
| **Grade** | Accurate product color comes first (brand colors and materials must match reality). Hero may push contrast; lifestyle stays natural |
| **References** | Irving Penn, Carl Kleiner, Dan Winters (still life) |
| **Prompt skeleton** | "[Product described physically, no brand name] on [surface], [shot size], [angle], [lens] at [f-stop]. [Light setup]. [Background]. Accurate true-to-life color and materials. [Space for type]. No logos or readable text." |
| **Clichés** | Product floating on a gradient with light rays (Barry §10); water splash for "fresh"; dramatic smoke for "premium" |
| **Caution** | A generated product image must not misrepresent the real product (shape, size, features, results). Generated packshots are comps; final product photography is real |

### 9.2 Fashion

| | |
|---|---|
| **Argues** | Who you become, or who you belong with, wearing this |
| **Sub-types** | *Campaign* (the brand's world in a few images) · *editorial* (a story across pages) · *lookbook* (clear, consistent, every garment readable) · *street / candid* (clothes in real life) · *beauty* (face and skin, very close) |
| **Light** | Campaign and editorial: anything that serves the story (natural, hard sun, flash, cinematic). Lookbook: soft, even, repeatable. Beauty: soft frontal (butterfly, clamshell), very controlled |
| **Lens / aperture** | 50–85mm full-length and three-quarter; 85–105mm beauty; 35mm for environmental campaign. f/2–4 for editorial mood; f/5.6–8 for lookbooks so fabric reads |
| **Angle** | Full-length: camera at waist height or lower lengthens the figure. Beauty: eye level. Editorial: free, but deliberate |
| **Grade** | Garment color must be accurate in lookbooks and e-commerce. Campaigns and editorials take a signature grade (black and white, film stock, flash) |
| **References** | Peter Lindbergh, Richard Avedon, Tyler Mitchell, Helmut Newton, Tim Walker, Juergen Teller |
| **Prompt skeleton** | "[Garment described by fabric, cut and color] worn by [person described without identifiable features], [pose and action], [location], [shot size], [lens] at [f-stop], [light], [grade or film stock]." |
| **Clichés** | Model staring blankly at camera in an empty studio with no idea; wind machine for "freedom"; luxury shorthand (gold, marble, champagne) |
| **Caution** | Generated people are a risk and are banned where a brief requires real people. Never generate a real, identifiable person. Casting diversity is a real decision, not a prompt setting |

### 9.3 Documentary realism

| | |
|---|---|
| **Argues** | This is true; it happened; we didn't stage it |
| **Sub-types** | *Reportage* (events as they unfold) · *documentary portrait* (a person in their real world) · *documentary still life* (the evidence of a life) · *social documentary* (a condition or community over time) |
| **Light** | Available and practical only; mixed color temperatures left as they are; no visible fill |
| **Lens / aperture** | 28–35mm, close to the subject; 50mm for portraits. f/2.8–5.6 so context stays readable |
| **Angle** | Eye level of the person being photographed; the camera is a participant, not a crane |
| **Grade** | Natural, slightly muted, fine grain; nothing glossy. Film stocks: Portra, Tri-X for black and white |
| **References** | Stephen Shore, William Eggleston, Alec Soth, Todd Hido; DPs Harris Savides, Bradford Young |
| **Prompt skeleton** | "[Place and moment, specific], [what just happened], [objects or person mid-action], [35mm lens at f/4], [practical light source], natural muted color, fine grain, unposed, real." |
| **Clichés** | Staged "documentary" that's too tidy; sad-filter poverty imagery; the lone figure at a window |
| **Caution** | Documentary style implies truth. A generated "documentary" image presented as real is deception. Label every generated image, and never generate a documentary scene of real people, places or events as if it happened |

### 9.4 Editorial

| | |
|---|---|
| **Argues** | Here is an idea about the subject, not just the subject |
| **Sub-types** | *Editorial portrait* (a person, with a point of view) · *conceptual editorial* (a visual metaphor for a story) · *editorial still life* (objects arranged to say something) |
| **Light** | Chosen for the idea: one shaped key for gravity, flash for irreverence, window light for intimacy |
| **Lens / aperture** | 35–85mm; f/2.8–8 depending on how much the setting carries the idea |
| **Angle** | Often deliberate and unexpected: frontal deadpan, high angle, tight crop |
| **Grade** | A consistent point of view across a story; publication or brand signature |
| **References** | Dan Winters, Platon, Nadav Kander, Irving Penn, Carl Kleiner |
| **Prompt skeleton** | "[Subject] [doing or placed in a way that expresses the idea], [set or background], [shot size and angle], [lens] at [f-stop], [light setup], [grade]." |
| **Clichés** | Visual pun that explains itself; headline-caption images (1 + 1 = 1) |
| **Caution** | The concept must survive without the caption: Barry §2 rough test |

### 9.5 Architectural and interiors

| | |
|---|---|
| **Argues** | This space has a character; this is what it feels like to be here |
| **Sub-types** | *Exterior* · *interior* · *detail and material* · *architecture in use* (with people and life) · *twilight* (inside lights against a blue sky) |
| **Light** | Soft overcast or low sun for form; twilight (blue hour) to balance interior and exterior; interiors lit by windows and practicals, balanced rather than flash-flat |
| **Lens / aperture** | 17–24mm for interiors and full exteriors (keep verticals straight: tilt-shift or correction); 35–50mm for details. f/8–11 for front-to-back sharpness |
| **Angle** | Camera level (no tilting up or down) so verticals stay vertical; chest height for interiors; two-point perspective for exteriors, one-point for symmetrical interiors |
| **Grade** | Clean, true whites and materials; restrained saturation; no heavy HDR |
| **References** | Julius Shulman, Ezra Stoller, Iwan Baan, Hélène Binet |
| **Prompt skeleton** | "[Space type], [materials and furniture], [time of day and light], [camera level at chest height, verticals perfectly straight], [lens] at f/8, [one- or two-point perspective], clean natural color, no HDR." |
| **Clichés** | Converging verticals from a tilted camera; overcooked HDR; empty showroom rooms with no sign of life |
| **Caution** | Don't generate a real, identifiable building or place as if photographed, and don't imply a location's features that don't exist. Real locations need property releases when shot |

### 9.6 Cinematic

| | |
|---|---|
| **Argues** | A story is happening; this is one frame of it |
| **Sub-types** | *Film still* (one frozen moment implying before and after) · *tableau* (a staged scene, everything placed) · *night / neon* · *natural-light epic* |
| **Light** | Motivated sources; mixed temperatures; contrast between a lit subject and a dark world; atmosphere (haze, rain) used sparingly |
| **Lens / aperture** | 24–50mm for immersive frames; anamorphic look for widescreen; f/1.4–2.8 for shallow cinema focus, f/8 for deep-focus tableaux |
| **Angle** | Deliberate: one-point perspective, over-the-shoulder, low for stature; camera height as a storytelling choice |
| **Grade** | A single controlled palette per piece; film-emulation grain; avoid teal-and-orange by default |
| **References** | Roger Deakins, Bradford Young, Emmanuel Lubezki, Wong Kar-wai with Christopher Doyle, Stanley Kubrick, Gregory Crewdson |
| **Prompt skeleton** | "Cinematic film still, [widescreen or specific ratio], [scene and moment implying a story], [lens] at [f-stop], [motivated light sources], [palette], [film stock or grain], [atmosphere if any]." |
| **Clichés** | Teal-and-orange; lens flare as decoration; letterbox bars on a non-cinematic image; "epic" with nothing happening |
| **Caution** | Widescreen ratios fight vertical placements: frame for 9:16 separately (visual-craft §7 format test) |

### 9.7 POV: first-person video and photography

| | |
|---|---|
| **Argues** | This is you: your hands, your view, your moment. The viewer is inside the ad, not watching it |
| **Sub-types** | *Eye-level POV* (what I see) · *hands-in-frame POV* (what I'm doing: holding, opening, making, scrolling) · *body-mount POV* (chest or head mount, action) · *over-the-shoulder hybrid* (almost POV) · *object POV* (the camera is a thing: a mug, a dashboard, a locker) |
| **Camera** | Phone held at the eyes, chest or head mount, or an action camera. Height matches the character's eyes exactly; if it's too high or too low the illusion breaks |
| **Lens / aperture** | Ultra-wide to wide (roughly 14–24mm equivalent) for immersion; phone main camera (~24–26mm) for everyday POV. Deep focus, since the eye sees near and far sharp |
| **Movement** | Motivated by the body: a turn of the head, a step, a reach. Stabilized but alive; no drone-smooth glides, no seasickness. Cut on the character's actions |
| **Light** | Available light of the real place; the POV character shouldn't carry lights |
| **Sound** | Diegetic sound is half the immersion: breath, footsteps, the object's own sounds |
| **References** | *Hardcore Henry* (feature film shot entirely in first person on action cameras); *Peep Show* (UK sitcom built on POV shots); *Enter the Void* (Gaspar Noé; floating first-person camera); *Being John Malkovich* (Spike Jonze; the portal POV) |
| **Prompt / shot skeleton** | "First-person point of view at eye level, [my hands doing X] entering from the bottom of the frame, [place], [wide lens, deep focus], [available light], [slight natural handheld movement for video]." |
| **Clichés** | POV of scrolling a phone screen; the "unboxing" hands on a white table; fisheye action-cam for no reason |
| **Caution** | Hands are where generated images fail most (fingers, grip, anatomy). Where a brief bans generated people, generated hands count as people. POV that simulates a real user's experience of a product must not show results or features the product doesn't deliver |

### 9.8 Handheld device (phone) photography

| | |
|---|---|
| **Argues** | Real, immediate, one of us. Closeness and credibility over polish |
| **Sub-types** | *Everyday snapshot* · *UGC-style* (looks like a customer's post) · *selfie / front camera* · *flash-at-night phone* · *brand work shot on a phone, crafted* (phone as a deliberate aesthetic) |
| **Camera character** | Main camera about 24–26mm equivalent wide; secondary ultra-wide (~13mm) and short telephoto (~48–120mm, varies by model). Small sensor: deep depth of field unless a portrait mode fakes blur (look for its edge errors). Computational HDR: bright skies held, shadows lifted, slightly flat contrast. Noise in low light; harsh direct LED flash |
| **Framing** | Held at arm's length or eye level; slightly imperfect, subject not perfectly centered, horizon occasionally a touch off; vertical by default |
| **Light** | Whatever is there: window, overhead, streetlight, the phone's flash |
| **Grade** | The phone's own processing look: punchy but flat, crisp detail, mild oversharpening. Don't add film grain to a "phone" image; it contradicts itself |
| **References** | Apple's *Shot on iPhone* campaign (real users' phone photographs used as brand advertising); creator content native to each platform |
| **Prompt skeleton** | "Candid smartphone photo, shot on a phone's main wide camera, vertical, deep focus, natural HDR look with lifted shadows, [available light or direct phone flash], [slightly imperfect framing], [real, unstyled place], [what's happening]." |
| **Clichés** | Fake-casual "UGC" that's obviously a production: perfect light, styled props, models; the mirror selfie with the product |
| **Caution** | **A generated or staged image made to look like a real customer's post is a fake testimonial.** Never present it as real user content. Real UGC needs the creator's permission and the platform's partnership or branded-content disclosure (verify current policy). Crafted brand work in phone style is fine when it doesn't pretend to be someone else's post |

### 9.9 Vertical video (9:16)

| | |
|---|---|
| **Argues** | Made for this phone, this feed, this second. Native, not resized |
| **Sub-types** | *Talking head / creator-style* (to camera) · *POV* (§9.7) · *demo* (product or process, hands and object) · *vertical cinematic* (composed film for 9:16) · *type-led / motion graphic* (kinetic type over image or color) · *still-to-motion* (a push, pull or pan on a still) |
| **Frame** | Compose for 9:16 from the start; don't crop a 16:9 master. Subject in the middle band, horizontally inside the central ~75% of the width; faces in the upper-middle, never under the interface. Key content, supers and logos inside the platform's safe zone (`shared/knowledge/<platform>/`; Meta: `meta-paid-ads/`). Vertical space is the story: movement up and down (tilt, reveal, fall, rise) reads naturally |
| **First frame** | The hook is the first frame, not the first three seconds: something is already happening. No logo sting, no fade from black (`.claude/skills/format-copywriting/references/social-video.md`) |
| **Camera** | Phone or cinema camera in portrait orientation (rotated rig or vertical sensor crop). Handheld for native feel; locked or gimbal for crafted; talking heads at eye level, lens 24–35mm, not closer than arm's length unless it's a selfie |
| **Light** | Talking head: soft key from a window or large source at 30–45°, not a ring light by default (the ring light's circular eye catchlight is a creator cliché). Match the setting's look |
| **Pacing** | Cuts on action and on the beat; a new visual idea every 1–3 seconds for most social formats; hold longer when stillness is the point (narrative-craft §6 time budgets) |
| **Sound** | Designed to work with sound off first (supers and captions carry it), rewarded with sound on. Captions for all speech, in the safe zone |
| **Loop** | Short verticals replay: an ending that flows into the opening can earn a second view |
| **References** | Platform-native creator formats; brand work built vertical-first rather than cut down |
| **Prompt / shot skeleton** | "Vertical 9:16 video, [shot type], subject in the middle band within the central 75% of the frame, top and bottom 15–20% clear, [camera: handheld or locked], [lens], [light], [first-frame action], [duration]." |
| **Clichés** | Letterboxed 16:9 inside a 9:16 frame; ring-light talking head; captions in the top or bottom UI zone; trending audio with no link to the idea |
| **Caution** | Durations, safe zones, caption support and music rules differ by platform and placement: cite the verified record, never memory. Trending audio needs rights clearance |

## 10. After generation: the finishing workflow

A generated image is a raw file, not a finished one.

| Step | Do | Don't |
|---|---|---|
| **1. Select** | Choose by the idea, focal point and empty type zone (§5) | Choose the prettiest render |
| **2. Upscale** | Upscale to the largest output size needed. Two gentle passes (one to keep texture and detail, one to sharpen) usually beat one aggressive pass | Oversharpen: halos and plastic texture are generated-image tells (visual-craft §9) |
| **3. Clean** | Fix craft artifacts: edges, repeated textures, warped straight lines, melted small objects, extra fingers in the background | **Retouch away content that shouldn't be there.** If the image contains something the brief forbids (people where they're banned, readable text, logos, a misrepresented product), regenerate. Retouching hides the problem; it doesn't remove the risk |
| **4. Color** | Grade to the brand and campaign system (visual-craft §4): shadow color, highlight color, saturation, contrast. Keep skin tones natural when people appear. Film grain can soften an over-clean render when the look calls for film | Apply a default "bump contrast and vibrance". Add grain to a phone-style image (§9.8). Treat grain as a disguise: a generated image is labelled whatever its grain |
| **5. Export** | Save high-res, keep the layered file, and record the model, prompt, settings and date with it (§6) | Flatten the only copy, or lose the prompt |

**Labelling travels with the file.** Placeholder, comp or mood: the label stays on every export and in every file name until the image is replaced by real photography or approved for use.
