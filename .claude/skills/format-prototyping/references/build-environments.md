# Build environments: Figma, Webflow, HTML

Choose the environment by what the prototype must prove, not by habit.

| Environment | Best at proving | Weak at | Typical formats |
|---|---|---|---|
| **Figma** | Composition, layout systems, flows and click-through, variants across sizes, collaborative review and comments | True motion timing, real scroll behavior, typing and data, sound, performance feel | Meta units, display size families, email, app or screen flows, slides |
| **HTML** | Real motion at true timing, scroll narratives, responsive behavior, device testing, sound, live or dynamic data, loops | Fast layout iteration with non-designers, multi-person comments on the canvas | Rich media, DOOH loops, landing pages, interactive email moments, motion-led decks |
| **Webflow** | Realistic site behavior, CMS-driven pages, client-visible site feel close to the finished site | Speed of exploration, non-web formats; no connector in this environment yet | Landing pages, microsites |

When two apply, prototype the composition in Figma and the behavior in HTML.

## Rules for every environment

- **Prove the key paths only.** The happy path, the signature moment of the idea and the one edge state that matters. Exhaustive screens are production planning, not prototyping.
- **Real sizes and frames.** Device frames, context frames and 1x pixel sizes for ad units.
- **Label it as a prototype.** On the file, the link and the first screen.
- **Accessibility basics.** Contrast, legible sizes, a reduced-motion or static state. Reviewers judge what they see.
- **Version deliberately.** Name versions by what changed, keep the previous one for comparison.

## Figma

- Use components and variants for size families and states, so a change in the master propagates.
- Build the prototype connections around the storyboard moments, not every screen.
- Use Smart Animate and variables for state changes where they read truthfully; hand true timing to HTML.
- Operations: load the Figma plugin skills (`figma-use` first, then `figma-generate-design`, `figma-use-motion` or `figma-use-slides` as needed).

## HTML

- **Single self-contained file** unless assets demand otherwise. No build pipeline, no package installs. Libraries only from an allowed CDN when a shared Artifact is the destination.
- **Fixed canvases for ad units.** Author at 1x pixel size, then scale the stage for presentation, so the real-size view stays one toggle away.
- **One timeline.** Keep all motion timings in one place (a CSS variable set or a single GSAP timeline) so reviewers' timing notes are one edit.
- **Presentation controls layer.** Add unobtrusive controls a reviewer can use: replay, jump to end frame, pause, toggle safe-zone overlay, toggle real size, switch dark mode or images-off, switch data variants. Hide them for a clean capture.
- **Sharing.** Publish as a private Artifact for review. Remember the viewer's theme and phone width.

## Webflow

- Use it when the prototype must feel like the site, or the client will review content in the CMS.
- Keep interactions to what Webflow can do natively unless the flag says otherwise.
- The risk is that a prototype quietly becomes the production site. Keep it labeled, and flag any shortcut that would not survive production.
