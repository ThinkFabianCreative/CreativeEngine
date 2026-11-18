# Review the frame for slop and craft

A frame looks AI-made when nobody decided anything: the gradient is there because gradients are there, the eyebrow label sits above the heading because headings get eyebrows, the cards are equal because cards come in threes. Slop is not one bad element. It is a pile of defaults that hides the idea. Review the frame as one piece, find the defaults, and say for each one what a decision would look like instead. Then consolidate everything into one ranked report.

Slow the frame down. Look at it at thumbnail size first: one thing should be seen first, and it should still come first in grayscale. Then look at it at the size it will actually be seen (a phone held at arm's length, a billboard across a road, a laptop at 100%). Read every word on it, out loud if needed. Click through the layers panel and open the right-hand panel on anything that looks off: raw hex where a variable should be, a detached instance, 13 px where the scale says 12 or 16. What looks fine at fit-to-screen but wrong at 100% is what's subtly wrong.

**Work in the file's own system.** Before proposing any fix, check what the file already has: local and library variables, text styles, color styles, effect styles, components and their variants, grids. Express every fix in that system: "bind fill to `color/surface/raised`", not "#F5F5F5". Never introduce a second set of values just to apply a fix. If the system lacks what the fix needs, say so; adding to the system is a decision for the owner, not for the review.

**The client's approved brand wins.** Anything below that a client's approved rules require (an uppercase tracked label, a heavy display weight, a gradient in the logo, a face on the avoid list) is not slop. Follow the client and record it under Considered but Rejected. Andres's own design decisions stay too: flag a concern, never "fix" it.

**Copy belongs to the copywriter.** This skill may fix interface microcopy (button labels, form labels, empty states, error messages, trailing periods). Headlines, value propositions, taglines and any line that carries the idea are flagged, never rewritten.

Color theory, palette building and new brand direction are out of scope. This skill measures what is on the frame and reports it; it does not repaint the brand.

Sources: slop signs from `unslop` by Damir Sokolovsky (@heydamir, CC BY 4.0, plugin commit `620163e`); craft floor from `impeccable` (`pbakaus/impeccable`, Apache 2.0, skill 4.9.1). Adapted for Figma frames and filtered through CreativeEngine's records `DesignChamp/skills/unslop.md` and `DesignChamp/knowledge/impeccable-playbook.md`, which remain the source of truth. Written 2026-11-18; regenerate when those records change. Holds no client facts.

## How to run a review

### Resolve scope, frame type and mode first

Infer the page, frames or section from the request and the current selection. State the resolved scope in the output.

Then decide the **frame type**, because the rules differ:

| Frame type | Examples | Domains that apply |
| --- | --- | --- |
| `ad` | Social static, carousel card, OOH, print, key visual, banner, deck slide | 1–6 and 8 |
| `interface` | Landing page, web page, app screen, dashboard, component, email | 1–8, including 7 |

A file with both gets both, frame by frame. Never apply interface rules (4 px grid, weights 400–500, sentence-case labels, one primary action) to an ad. Ads are governed by the idea and the client system.

Use `full` when no mode is supplied.

| Mode | Coverage | Finding cap |
| --- | --- | --- |
| `quick` | The selected frame or the hero frame of a set; report only `HIGH` and `MEDIUM` | 5 |
| `full` | Every frame in scope, every domain, including states and breakpoint frames when they exist | 15 |
| `fix` | `full` review, then apply the fixes on a duplicate (see Fixing) | 15 |

If the scope is too large to inspect credibly, narrow it to the most important complete set (one campaign set, one page with its breakpoints) and state the boundary. Never imply uninspected frames were reviewed.

### Recon before judgment

Before judging anything, find out:

- **The idea.** Can you say what the frame is for in one sentence? If the request or the attached files don't say, ask. A frame with no idea gets one finding (no idea to serve) and nothing else; polishing it would hide the real problem.
- **The client system.** Attached brand files, the file's libraries, variables, text styles and components. Which faces, colors and rules are approved.
- **The format.** Canvas sizes, safe zones, breakpoints.
- **The copy source.** Which words were supplied and approved. Anything on the frame that isn't in the supplied copy is a finding.

### Review in this order

Foundational failures must not be hidden by polish:

1. Idea and brand
2. Hard bans
3. Composition and spacing
4. Surface and color
5. Type
6. Image, icons and copy
7. Interface (interface frames only)
8. Figma file craft

Then run the **template look check** last, across everything.

When two domains cover the same issue, give it to the one that owns the underlying rule and mention the side effects in **Why**. Report it once.

### Require evidence

Every finding names the layer path (`Page / Frame / Layer`) and its node ID, and shows the current value: the hex, the size, the weight, the effect, the text. Some findings need the render, not the layer data: contrast over an image, overlaps, what reads first, line breaks. For those, inspect a screenshot of the frame, not just properties. Do not report a visual finding from layer properties alone, or a structural finding (detached instance, raw value) from the picture alone.

### Review without editing by default

A review request is read-only. Annotations are the one exception (see Annotate the frame). Edit frames only in `fix` mode or when the user asks to apply the findings.

## 1. Idea and brand

Craft cannot rescue a missing concept. Check this before anything else.

### 1. One Idea, Made Visible

Say the frame's idea in one plain sentence. The biggest, first-seen element should be the one that carries it. If the largest thing is a logo, a decorative shape or a setup word while the payoff word is small, the hierarchy is fighting the idea.

### 2. Client Rules First

Palette, faces, logo use, mandatories, legal lines and claims rules come from the client's approved files. A frame that breaks them is `HIGH` whatever else is right about it.

### 3. Specific to This Brand

Swap the logo for an unrelated brand's. If the frame still works unchanged, it isn't finished: nothing on it belongs to this brand or this idea.

## 2. Hard bans

No frame and no request earns these back, except where a client's approved system requires one (then it's not a finding).

### 1. No Invented Copy

Use only the supplied words. If a frame seems to need a word, leave a visible red note asking for it.

### 2. No Invented Proof

No made-up customer counts, star ratings, "trusted by" logo rows, testimonials, prices or stats. Placeholder data is labelled as placeholder.

### 3. No Redrawn Logo

Use the supplied logo component or a labelled placeholder. The logo and the same name typed beside it is one brand name too many.

### 4. No Eyebrow Above a Heading

A kicker or eyebrow label ("✨ INTRODUCING", "OUR SERVICES") above a heading is removed. The heading carries its own weight.

### 5. No Gradient Text

In headings, numbers or wordmarks. Emphasis comes from size, weight or color.

### 6. No Emoji or Glyphs as Icons

Icons come from one real set, one stroke, one size.

### 7. No Text Baked into Images

Headlines, buttons, prices and logos sit on the frame as live text and components, never inside a raster.

### 8. No Loaded Symbols as Decoration

Militarist, supremacist or hate-movement emblems and their stylised variants (for example the Rising Sun rays) are never motifs, badges or ornament, even when the subject's world seems to suggest them.

## 3. Composition and spacing

Position and space carry hierarchy before a word is read. A frame that relies on decoration to look organised isn't organised.

### 1. One Focal Point

One element is seen first at thumbnail size and still first in grayscale. If three elements compete, two must step down.

### 2. Group with Space

Tight inside a group, generous between groups: the gap between groups is at least twice the gap within one. A group never sits closer to its neighbour than to its own items. More space above a heading than below it.

### 3. One Spacing Scale

Spacing comes from the file's spacing variables (or 4/8 px steps if none exist). No 7, 13 or 31 px. Sibling cards share one padding; rows in a list share one height and one gap. Every frame in a set uses the same margins.

### 4. Radius by Size, Nested Radius by Math

Not everything is a full pill. On nested surfaces, outer radius = inner radius + padding.

### 5. Find the Composition This Idea Needs

Refuse these scaffolds unless the brief's own words ask for them:

- A row of same-size cards, each icon + bold title + vague line, as the page structure. Nested cards are always wrong.
- The hero-metric template: big number, small label, supporting stats, accent.
- Everything stacked and centered: pill badge, headline, subline, two buttons, image below.
- Section numbers (01 / 02 / 03) when the order carries no information.
- Sparklines, progress rings and soft-shadowed rounded rectangles standing in for content.
- A colored left or right border thicker than 1 px on cards, callouts or list items.
- Bento grids, glass and gradients as trend imitation.

### 6. No Accidents at the Edges

No unintended crops, no elements floating a few pixels from an edge, key content inside the safe zone on social formats.

## 4. Surface and color

Depth comes from surface steps and hairlines, not effects. Color is a job, not a mood.

### 1. Flat Surfaces Unless the World Says Otherwise

Purple-to-blue or violet-to-pink gradients on backgrounds, cards or buttons become one flat surface. Blurred blobs, orbs, radial washes and glowing grid lines behind content are removed.

### 2. No Glow

Colored outer glows, glowing pills, drop shadows on emoji and zero-offset colored halos are removed. A shadow, when it exists, has an offset and a soft blur.

### 3. Hairlines, Not Neon

Saturated or neon borders become a hairline at 6–10% opacity.

### 4. One Accent, Used Once or Twice

If everything is highlighted, nothing is. The accent marks the one meaningful thing on the frame.

### 5. Three Text Roles from One Ramp

Five near-identical tints of one hue for text become three roles (primary, secondary, tertiary) from one ramp. On a colored surface, tint secondary text from that hue; never plain grey.

### 6. No Costume Effects

Glass with a white inner highlight and colored shadow becomes a plain raised surface with a hairline. Hard offset block shadows (4/4/0) are removed outside a world that is deliberately neobrutalist.

### 7. Light or Dark from the Use Scene

Not from the category ("tech means dark"). Who sees it, where, in what light.

## 5. Type

Good type is mostly restraint, and the type has a job: to carry, become or deliver the idea.

### 1. The Approved Face, or a Reported Gap

Only client-approved faces. If one is missing, the closest installed font is not a fallback: report the gap. A system face (Arial Black, Impact, the platform sans) as display voice is a finding.

### 2. Faces Picked, Not Defaulted

Inter as display, DM Sans, Space Grotesk, IBM Plex and Playfair are what models reach for when nobody chose. Flag them unless the client system specifies them.

### 3. Few Sizes, Few Weights

Text styles from the file's scale. Hierarchy from size first. Weights of 800–900 used everywhere by default become the weight the type job calls for.

### 4. Tracking and Case

Negative tracking on small text becomes 0 or slightly positive; display tracking no tighter than −4%. On interface frames, uppercase labels with wide tracking become sentence case (unless the client system uses them).

### 5. Emphasis with One Method

At most one or two meaningful words per line, one method only (weight, or color, not both). Italic for emphasis by habit becomes weight or color.

### 6. Numbers in One Format

`$48,210` beside `$124,860.40` becomes one format, with tabular figures where numbers line up.

### 7. Mono Only for Code, Data or Measurement

Monospace as a "technical" costume is removed.

### 8. Readable Where It's Read

Body measure 65–75 characters on reading text. Line breaks follow reading pauses; no orphans. Minimum sizes for the format: 32 px on a 1080-wide social frame, 40 px on a 1440-wide frame, 16 px for interface body text.

## 6. Image, icons and copy

### 1. The Product or One Concrete Metaphor

Glossy 3D blobs, liquid chrome and purple nebulas as the hero become the product itself, or one concrete image of what it does. Stock robots, glowing brains, circuit lines and holograms for anything AI are removed. The ✨ for AI is removed.

### 2. One Visual Where It Helps

Not a visual on every section. An image with a hard edge and a different black from the frame gets its background matched and its edge softened.

### 3. Real Masks

Circles or polygons faking an organic cut-out become a real cut-out asset, or no mask.

### 4. One Icon Set

One set, one stroke, one size, drawn in the text color role. Icon stroke matches the weight of the text beside it. Icons sit in the same column in every row.

### 5. Copy: Flag, Don't Rewrite

Flag for the copywriter: exclamation marks, hype words (supercharge, seamless, unlock, magic, revolutionize, elevate), and any headline that would fit another product with the name swapped. Fix directly only interface microcopy: trailing periods on labels and buttons, greeting titles (`Welcome back, Sam! 👋` becomes the page name), changes without a reference (`+12%!!` becomes `+12% vs last month`), wordy placeholders (`Search anything...` becomes `Search`).

## 7. Interface (interface frames only)

These are product-UI defaults. Never apply them to ads, OOH, print or decks.

### 1. Quiet Components

Glowing pills for counts, plans and status become quiet text or a keycap. `PRO`, `New ✨` and `Beta 🚀` badges become none, or one quiet text badge. Rainbow, glowing or pill-shaped chart bars become one or two series, a muted grid and one highlight color. A sparkline on every stat card becomes the number, its label and its change. Equal cards with the same chart become one main chart and compact stats at varied widths.

### 2. One Primary Action

At most one primary and one secondary action per view. No chips or avatar rows stacked under the buttons. A modal only for a task that needs interruption or protected focus.

### 3. Every State Drawn

Default, hover, pressed, focus (visible ring), disabled, loading, error and empty, as component variants, not loose frames. Errors name the problem and the fix. Buttons start with a verb.

### 4. Contrast and Targets

Body and placeholder text at least 4.5:1, large text at least 3:1; measure the rendered pair. Touch targets at least 44 × 44 px; desktop at least 24 × 24 px.

### 5. Real Content at Every Breakpoint

Test the real copy, at its real length, in every breakpoint frame. Fixed-height text containers that clip are findings.

### 6. Right-to-Left Frames

Mirror layout and directional icons; keep media controls and objects as they are. No tracking on Arabic. A family drawn for Arabic with real weights. One digit system per screen. Body line height 1.6–1.8.

### 7. Motion Specs, When Prototyped

One authored moment per screen, not the same entrance on every section. Ease-out from an already-visible default; no bounce on simple UI. No pulse or breathing glow on anything that isn't live. Hover is a color or surface step; press is a small scale-down. Animate position, opacity, blur or masks, not width and height.

## 8. Figma file craft

The frame is also a hand-off. A frame that looks right but is built from raw values breaks the moment someone else touches it.

### 1. Auto Layout on Content Containers

No absolutely positioned text inside a stack. Hug, fill and fixed are chosen on purpose, and the frame survives a width change.

### 2. Variables and Styles, Not Raw Values

Fills, strokes, spacing and radius bind to variables; text uses text styles; shadows use effect styles. A raw hex or a one-off size is a finding even when it matches the right value visually.

### 3. Instances Stay Attached

A detached instance edited into a one-off is a finding. The fix is a variant or a reported gap in the library.

### 4. Layers Named by Role

`Hero / Headline`, `Card / Price`. Never `Frame 482` or `Rectangle 12`.

### 5. Images at Real Resolution

Image fills at the resolution the format needs, cropped on purpose.

## Template look check

Run this last, after everything else is clean. These aren't slop; they're what a cleaned frame falls back to when nobody decided anything.

- Pure grey page, Inter, white text and the brand color on one button, on a brand whose world is warm or bright. The ramp should lean toward the world and the accent should come from it.
- A headline that would fit another product with the name swapped (flag for the copywriter).
- A hero visual that is an empty box or a generic picture instead of the product or the concept's own image.
- **Cross-client test:** does this look like the last cleaned-up frame for a different client? Quiet chrome plus one bright element plus a scene hero becomes the next template if every job gets it.

With every check passed, spend the remaining effort on the idea's own world. When torn between refined and committed, commit.

## Review Output Format

Always use the following sections.

### Scope and Coverage

State the mode, exact scope (page and frames), frame types, the client system found (libraries, variables, styles, approved faces) and any boundary. Then show coverage:

| Domain | Evidence inspected | Result |
| --- | --- | --- |
| Idea and brand | Frames, attached brand files | Findings count or `Clear` |

Include every domain that applies to the frame types in scope, plus the template look check. `Clear` means inspected with nothing to act on; `Not reviewed` must say why; `Not applicable` is only for Interface on ad frames.

### Findings

One table, ordered by severity, then by reach:

| # | Severity | Domain | Location | Before | After | Why |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | HIGH | Hard bans | `Social / Feed 1080 / Headline` (`12:345`) | Gradient fill `#7C3AED → #EC4899` on headline text | Solid fill bound to `color/text/primary` | Gradient text is banned and the client palette has no gradient |

Severity is one shared scale:

- `HIGH`: breaks a client rule, legal or claims line, or a hard ban; invents copy or proof; fails contrast on text that must be read; or hides the idea (the wrong thing is seen first).
- `MEDIUM`: a slop sign or template scaffold that weakens hierarchy, consistency or brand ownership; a raw value or detached instance that will break on hand-off.
- `LOW`: isolated polish with limited effect. Only in `full` and `fix` mode.

Within a severity, rank by reach: a fix to a variable, style or component outranks the same symptom on one layer.

Each row is one root cause: list every location in the same row, not one row per occurrence. Respect the finding cap and never pad to reach it. If there are no findings, omit the table and write "No slop or craft findings."

### Annotate the frame

Every finding also lands on the canvas as a card. Cards go in one top-level group named `Antislop review`, in the empty space left and right of the frame, never on top of the design and never over the frame's own title.

Never move, edit, lock or restyle the frames under review while annotating. Annotations are added; nothing else changes.

The cards are review tooling, not design. They use Inter because Figma always has it loaded; that is not a type recommendation.

#### Card anatomy

Each card is a vertical auto-layout frame: 280 px fixed width, height hugging its contents, 12 px padding, 8 px item spacing, 8 px corner radius, white fill, 1 px black stroke at 8% opacity.

Three children, in order:

1. **Severity pill**: hugging auto-layout frame, 4 px radius, 2 px vertical and 6 px horizontal padding, filled with the severity color below. Label is the severity word in uppercase, 9 px, Inter Semi Bold, 4% letter spacing.
2. **Title**: `#4 Gradient headline`. The finding number, then a three-to-five-word summary. 12 px, Inter Semi Bold, near-black.
3. **Body**: one or two sentences, what is wrong then what to do. 11 px, Inter Regular, 140% line height, mid-grey. 240 characters at most; the full reasoning stays in the table.

| Severity | Pill fill (RGB 0–1) | Pill text |
| --- | --- | --- |
| `HIGH` | `{ r: 0.85, g: 0.19, b: 0.15 }` red | white |
| `MEDIUM` | `{ r: 0.96, g: 0.55, b: 0.13 }` orange | near-black `{ r: 0.1, g: 0.1, b: 0.1 }` |
| `LOW` | `{ r: 0.98, g: 0.84, b: 0.25 }` yellow | near-black |

White on orange or yellow falls below 4.5:1, so those pills use near-black. The pill names the severity in words, so color never carries it alone.

#### Building the card

Auto-layout children only take part in the layout once appended, and fill sizing can only be set after appending. Follow this order:

```js
await figma.loadFontAsync({ family: "Inter", style: "Semi Bold" });
await figma.loadFontAsync({ family: "Inter", style: "Regular" });

const SEVERITY = {
  HIGH:   { fill: { r: 0.85, g: 0.19, b: 0.15 }, text: { r: 1, g: 1, b: 1 } },
  MEDIUM: { fill: { r: 0.96, g: 0.55, b: 0.13 }, text: { r: 0.1, g: 0.1, b: 0.1 } },
  LOW:    { fill: { r: 0.98, g: 0.84, b: 0.25 }, text: { r: 0.1, g: 0.1, b: 0.1 } },
};

function makeText(chars, size, style, color) {
  const t = figma.createText();
  t.fontName = { family: "Inter", style };   // font must already be loaded
  t.fontSize = size;
  t.characters = chars;
  t.fills = [{ type: "SOLID", color }];
  return t;
}

function makeCard(n, severity, summary, body) {
  const card = figma.createFrame();
  card.name = `#${n} card`;
  card.layoutMode = "VERTICAL";             // before any sizing property
  card.resize(280, 100);
  card.layoutSizingHorizontal = "FIXED";
  card.layoutSizingVertical = "HUG";
  card.paddingTop = card.paddingBottom = card.paddingLeft = card.paddingRight = 12;
  card.itemSpacing = 8;
  card.cornerRadius = 8;
  card.fills = [{ type: "SOLID", color: { r: 1, g: 1, b: 1 } }];
  card.strokes = [{ type: "SOLID", color: { r: 0, g: 0, b: 0 }, opacity: 0.08 }];
  card.strokeWeight = 1;

  const pill = figma.createFrame();
  pill.name = "Severity";
  pill.layoutMode = "HORIZONTAL";
  pill.paddingTop = pill.paddingBottom = 2;
  pill.paddingLeft = pill.paddingRight = 6;
  pill.cornerRadius = 4;
  pill.fills = [{ type: "SOLID", color: SEVERITY[severity].fill }];
  const pillLabel = makeText(severity, 9, "Semi Bold", SEVERITY[severity].text);
  pillLabel.letterSpacing = { unit: "PERCENT", value: 4 };
  pill.appendChild(pillLabel);
  pill.layoutSizingHorizontal = "HUG";
  pill.layoutSizingVertical = "HUG";

  const title = makeText(`#${n} ${summary}`, 12, "Semi Bold", { r: 0.1, g: 0.1, b: 0.1 });
  const text = makeText(body, 11, "Regular", { r: 0.4, g: 0.4, b: 0.4 });
  text.lineHeight = { unit: "PERCENT", value: 140 };

  // Append first. A node that is created and positioned but never appended
  // sits on the canvas as a sibling, and the card hugs to nothing.
  card.appendChild(pill);
  card.appendChild(title);
  card.appendChild(text);

  // Only now can the texts fill the card width and wrap downward.
  for (const t of [title, text]) {
    t.layoutSizingHorizontal = "FILL";
    t.textAutoResize = "HEIGHT";
  }
  return card;
}
```

Check each card before placing anything else:

```js
if (card.children.length !== 3 || card.height < 56) {
  throw new Error(`Finding ${n}: card built empty (${card.children.length} children, ${card.height}px tall)`);
}
```

A correct card is at least 56 px tall. Anything near 26 px is padding with nothing inside.

| Symptom | Cause |
| --- | --- |
| Card about 26 px tall, contents floating outside it | Children never appended to the card |
| Every card the same height | Vertical sizing left at `FIXED` |
| Card as wide as its longest line | Horizontal sizing left at `HUG` |
| Body text runs off the card on one line | Text not set to `FILL` width and `HEIGHT` auto-resize |
| Pill spans the whole card width | Pill not set to `HUG` on both axes |
| Text measures zero | Font not loaded before setting `characters` |
| Error setting `FILL` | Set before the node was appended to an auto-layout parent |
| Children ignore the x/y you set | Expected: auto layout owns child positions. Position the card only |

#### Placement

Cards sit in two gutters: one starting 80 px left of the frame, one 80 px right of it. Each card goes to the gutter nearer its target layer; within a gutter, sort by the target's vertical position and stack top to bottom with 16 px between cards. If a stack would run past the frame's bottom edge, move the overflow to the other gutter rather than shrinking or overlapping cards.

Position cards only after all children are appended and sized; until then the height isn't known.

Draw a 1.5 px dashed connector (dash pattern `[4, 4]`) from the card's inner edge to the target layer's nearest edge, stroked in the severity color, as one elbow: horizontal out of the card, vertical, then horizontal into the layer. End it with a 4 px dot on the layer, not an arrowhead. A finding that covers the whole frame gets no connector.

```js
// Absolute canvas coordinates: (x1, y1) on the card edge, (x2, y2) on the target edge.
function connector(x1, y1, x2, y2, color) {
  const left = Math.min(x1, x2), top = Math.min(y1, y2);
  const midX = (x1 + x2) / 2;
  const v = figma.createVector();
  v.vectorPaths = [{
    windingRule: "NONE",
    data: `M ${x1 - left} ${y1 - top} L ${midX - left} ${y1 - top} L ${midX - left} ${y2 - top} L ${x2 - left} ${y2 - top}`,
  }];
  v.x = left; v.y = top;
  v.strokes = [{ type: "SOLID", color }];
  v.strokeWeight = 1.5;
  v.dashPattern = [4, 4];
  v.fills = [];
  const dot = figma.createEllipse();
  dot.resize(4, 4);
  dot.x = x2 - 2; dot.y = y2 - 2;
  dot.fills = [{ type: "SOLID", color }];
  return [v, dot];
}
```

Group each finding's card, connector and dot with `figma.group([...], figma.currentPage)` and name it `#4 MEDIUM Surface and color`. Then group all finding groups into the one `Antislop review` group.

#### Scale

The values above assume a frame 1000–1600 px wide. Outside that range, multiply every annotation dimension and type size by `frameWidth / 1400`, so cards stay readable at the zoom where the whole frame fits on screen. A 1080-wide social frame sits inside the range; a 375-wide mobile frame or a 4000-wide billboard does not.

#### Re-running

Delete the existing `Antislop review` group before drawing a new one (`figma.currentPage.findOne(n => n.name === "Antislop review")?.remove()`). Annotations replace; they never stack. If the file is view-only, or the user asked for the report only, output the table alone and say the frame was not annotated.

### Fixing

Only in `fix` mode or when the user asks to apply the findings.

- **Work on a duplicate.** Duplicate each frame in scope, place it to the right of the original and name it `<original name> / antislop`. Leave the original untouched unless the user says to edit it in place. A client's file or Andres's own frames are never overwritten silently.
- **Fix in the file's system.** Bind to existing variables and styles; switch to existing variants. Don't hard-code values, and don't add variables, styles or components without asking.
- **Fix in review order.** Idea and brand, hard bans, composition, surface, type, image and icons, interface, file craft. A later fix never undoes an earlier one.
- **Never touch idea-carrying copy.** Leave a red note on the frame instead.
- **Re-review the duplicate** and report which findings are now resolved, at their actual scope.

### Considered but Rejected

Record candidates you looked at and deliberately left. A candidate is rejected when the client's approved system requires it, the request asked for it, it's Andres's own decision, the evidence is too thin, or the change would add complexity with no gain.

Include 1–3 in `quick` mode and 2–5 in `full` and `fix`:

| Location | Candidate | Rejected because |
| --- | --- | --- |
| `Social / Feed 1080 / Label` | Uppercase tracked label | The client's type rules specify uppercase labels at +8% tracking |

These are real candidates from this review, not filler. If there are fewer, list the ones that exist and say so.

### Verification

List what you actually checked and how: thumbnail and grayscale view, view at real size, contrast measured on which pairs, layers and instances inspected, breakpoint frames compared, the annotation group built and every card at least 56 px tall. Separate checks that passed from checks marked **Not verified** (for example, a font that isn't installed so the true render couldn't be seen). Never turn a verification gap into a finding.

### Craft status

End with exactly one. This is a craft status, not a creative verdict; KILL, REWORK, ADVANCE and BET THE PITCH belong to the Creative Director.

- `Has blockers`: one or more `HIGH` findings remain.
- `Needs changes`: only `MEDIUM` or `LOW` findings remain.
- `Clean`: nothing left to act on, and the coverage claimed was verified.

Don't call the work bold, premium, striking or iconic. Describe what was found and done.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Polishing a frame with no idea | Report the missing idea as the only finding |
| "Fixing" a client's approved uppercase labels or gradient logo | Client system wins; record under Considered but Rejected |
| Applying interface rules to an ad | Check the frame type first; Interface rules are for interface frames |
| Rewriting a headline because it has hype in it | Flag it for the copywriter |
| Filling a missing word with your own | Leave a red note asking for it |
| Gradient or glow added "for depth" | Flat surface; depth from surface steps and hairlines |
| Eyebrow label above the heading | Delete it |
| Three equal icon-title-text cards as the layout | Find the composition this idea needs |
| Sparkle ✨ for anything AI | Remove it, or show what the AI makes |
| Closest installed font standing in for the brand face | Report the missing font |
| Raw hex that happens to match the brand color | Bind to the variable |
| Detached instance edited into a one-off | Use or request a variant |
| `Frame 482`, `Rectangle 12` | Name layers by role |
| One finding row per occurrence | One row per root cause, all locations listed |
| Contrast judged from layer colors over an image | Measure on the rendered pair |
| Cards drawn on top of the design | Gutters 80 px left and right of the frame |
| Annotation cards stacking up on every run | Delete the old `Antislop review` group first |
| Fixes applied to the original frame | Duplicate first, fix the duplicate |
| Every client's frames converging on the same clean look | Run the cross-client template check |
| `Clean` with findings still open | Use `Needs changes` or `Has blockers` |

---

*Slop signs adapted from unslop by Damir Sokolovsky ([@heydamir](https://x.com/heydamir)), CC BY 4.0. Craft floor adapted from impeccable (pbakaus/impeccable), Apache 2.0.*
