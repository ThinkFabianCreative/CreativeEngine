# Rich media and HTML5 display

Covers standard animated HTML5 banners and rich media units: expandable, in-banner video, interactive (swipe, drag, hotspot, scratch, slider), mobile interstitial or full-screen, dynamic (data or feed driven) and synced or takeover placements.

## The encounter

Display lives in peripheral vision, beside content the person came for. Most viewers never click and many never look directly. For most people, the brand impression and the end frame are the whole ad. Interaction is a bonus for the few.

## The format's job

Leave an unmistakable branded impression of the idea in a few seconds, and reward the rare person who engages.

## Specifications

Sizes, file weight, animation length, loop count, border, click-through and expansion rules are set by the ad server, network and publisher, and they vary. Get the assignment's spec sheet or official documentation (for example IAB guidance, the ad server's HTML5 requirements, the publisher's spec) and cite it. Otherwise label UNVERIFIED. None of these numbers are held in CreativeEngine knowledge yet.

## Craft

**Design the hardest size first.** Start with the smallest mobile banner or the most extreme ratio, not the generous rectangle. If the idea survives there, it survives everywhere.

**Size families, not one layout.** Wide (leaderboard, billboard), tall (skyscraper, half-page), box (medium rectangle), small mobile. Each family gets its own composition of the same mechanism.

**Frame choreography.** Hook, develop, resolve. Each frame holds long enough to be read by someone who is not really looking. Fewer frames almost always beats more.

**The end frame is the ad.** Brand, the idea in its most compressed form, and the call to action. It must also work alone as the static backup image.

**Legibility in small canvases.** Heavier weights, generous contrast, few words, no text over busy moving backgrounds. Judge at 1x pixel size on a real screen.

**Separate the ad from the page.** Publisher pages are unpredictable. Make the unit read as a contained object; some specs require a border.

**Interaction must be discoverable without instructions.** The first frame shows the affordance: something that looks draggable, a visible hotspot, a hint of what is behind. "Tap to explore" copy is a fallback, not a design.

**Respect user control.** Expansion, sound and full-screen are typically user-initiated, with an obvious close. Verify the exact rules; design them as if they are always required.

**Dynamic units.** Design the template for the longest, shortest and ugliest real data: a long product name, a missing image, a price with many digits.

## What to prototype

- Each size family at actual pixel size, not zoomed.
- The full animation at true timing, with replay and a "jump to end frame" control.
- Collapsed, expanded and closed states for expandables; muted, playing and ended for video.
- The unit placed in a generic, unbranded page mock, so reviewers judge it in peripheral context.
- For dynamic units, three data variants including an extreme one.

## Buildability flags

- Initial file weight: video, custom fonts, 3D and large imagery are the usual budget breakers. Fonts often need to be images or tightly subset.
- Animation length or loops beyond the spec.
- Interactions or APIs (camera, gyroscope, geolocation) that the ad server or browser environment may not allow.
- Data feeds the client does not actually have.

## Fidelity check additions

- [ ] The end frame alone communicates the idea and brand.
- [ ] The smallest size is legible at 1x.
- [ ] Timing and loops are within the cited spec, or flagged.
