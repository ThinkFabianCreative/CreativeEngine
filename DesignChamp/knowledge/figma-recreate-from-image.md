# Recreate From Image

Goal: rebuild the reference image as a Figma frame that matches it as closely as possible. This is a fidelity task. Prioritize matching the source image over reusing existing library components, unless told otherwise.

## Before starting

Confirm you have:
1. The reference image.
2. The font(s) to use. If not specified, ask before building rather than guessing a font from the image. Verify the font is available in Figma before applying it anywhere.

If the target file or page isn't obvious, ask.

## Step 1: Study the reference before building anything

Look at the image and work out:
- **Structure**: major sections top to bottom (header, hero, cards, footer), and the sub-groups within each that align/move together.
- **Grid and spacing**: frame width, margins, gutters, and the gap pattern between elements. Look for a consistent spacing scale (e.g. 8/16/24/32) rather than eyeballing each gap on its own.
- **Colors**: the distinct colors used for backgrounds, text, borders, accents. Note approximate hex values.
- **Typography**: the distinct size/weight pairs present and which role each serves (heading, subheading, body, caption, button label).
- **Corner radius**: check each container's four corners individually, don't assume a uniform radius. Uneven radii (e.g. only top corners rounded, or one corner sharp) are common and easy to miss if you're not deliberately checking each one.
- **Repeating elements**: cards, list rows, nav items — anything appearing more than once with the same structure and different content. These should be built once and duplicated, not built separately each time.

Do this analysis before placing a single node. It's what prevents messy, inconsistent structure later.

## Step 2: Plan the structure

- One top-level frame for the whole composition.
- One frame per major section, using auto layout, stacked to match the reference.
- Within a section, only add a child container when its contents are actually grouped (a row, a column, a repeating card). Don't wrap a single element in its own frame just to hold it.

**Nesting rule of thumb**: if a frame could be deleted and its children moved up one level without changing the visual result or losing needed auto-layout behavior, delete it. Every container should exist for a reason: it manages layout for genuinely grouped content, or it's a repeating unit. A frame wrapping a frame wrapping a single text node is the failure mode to avoid.

## Step 3: Build section by section

For each section:
1. Create the section frame with auto layout — set direction, gap, padding, and alignment to match the reference.
2. Add children in order. Use auto-layout containers for grouped content, direct children for standalone elements.
3. Set sizing (hug/fill/fixed) appropriately once each element is in its parent.
4. Apply the colors and fonts identified in Step 1. For corner radius, set each corner independently based on what you observed, never apply a single radius value to all four corners by default.
5. **Name every layer contextually as you create it** (rules below). Don't leave default names anywhere.

### Layer naming rules

Name for what a layer *is*, not its shape or a generic index:
- Sections: `Header`, `Hero`, `FeatureCards`, `Footer` — not `Frame 1`.
- Repeating units: `FeatureCard`, `NavItem`, `TestimonialCard` — singular, so duplicates read clearly.
- Text layers: name by role, not by literal content — `Heading`, `Eyebrow`, `BodyCopy`, `CTALabel` — not `Text 1` and not the actual sentence.
- Interactive elements: `PrimaryButton`, `SecondaryButton`, `IconButton-Close`.
- Pure layout wrappers: name by what they arrange — `ButtonGroup`, `IconTextRow`, `CardGrid`.

If unsure what to call something, name it by its function in the layout.

## Step 4: Review against the reference — up to 3 passes

After the full composition is built, compare it against the reference image. Do up to 3 passes. Stop early if a pass finds nothing worth fixing.

Each pass, check for:
- Layout or position drift
- Spacing mismatches against the reference's rhythm
- Color mismatches
- Typography mismatches (size, weight, line-height, letter-spacing, wrong font applied to wrong role)
- Missing or extra elements
- Text that's truncated, overflowing, or wrapping incorrectly
- Corner radius on each container, check all four corners against the reference, not just whether it "looks rounded"

Fix issues with targeted edits to the specific layers involved — don't rebuild sections that are already correct. If a pass finds nothing meaningful, stop rather than making cosmetic micro-adjustments for the sake of using all 3 passes.

After the loop, report what was checked and flag anything that couldn't be matched exactly (e.g. a font substitution, an effect that can't be replicated), rather than silently approximating it.

## CreativeEngine rules for this skill

Added for CreativeEngine work. Where they conflict with the steps above, these win.

- **Fidelity means no anti-slop fixes.** Rebuild what the image shows, including things the antislop review (`figma-antislop-impeccable.md`) would flag: an eyebrow label, a gradient, a glow. Clean-up is a separate step, run afterwards only when asked, on a duplicate.
- **Whose image it is decides what the rebuild is for.** A rebuild of a client's own material (an existing ad, a page from their site) is working material for that client, saved in that client's project. A rebuild of a competitor's or any other third party's work is an internal reference only: never handed to a client as our work, never used as a template for a client's design, and never saved under another client's project.
- **Logos are never redrawn.** Use the supplied logo component, or a placeholder labelled `Logo: <brand>`. The same goes for trademarks, product shots and photographs: use supplied assets or labelled placeholder rectangles with the crop the reference shows.
- **Text is transcribed exactly.** Copy every word as it appears in the image, including spelling, case and punctuation. If a word can't be read, leave a visible red note instead of guessing.
- **Fonts follow the "ask first" rule above.** If the exact font isn't available, report it before substituting; any substitute is named in the report and on the frame.
- **The reference image is a raw source.** Don't crop, edit or overwrite it. Place it beside the frame, locked, on a layer named `Reference`, so the review passes compare against the original.

## Before calling it done

- [ ] Every layer has a contextual name — no default names, no literal text used as a layer name
- [ ] Auto layout used everywhere content is structurally grouped
- [ ] No redundant single-child wrapper frames
- [ ] Repeating elements share one consistent structure
- [ ] Fonts match exactly what was specified
- [ ] Corner radius checked per corner on every container, not assumed uniform
- [ ] Review loop completed and findings reported
- [ ] Logos and photos are supplied assets or labelled placeholders, never redrawn
- [ ] Text transcribed exactly; unreadable words marked with a red note
- [ ] Reference image placed beside the frame, locked and unedited
