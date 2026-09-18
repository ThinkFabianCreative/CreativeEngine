# Digital OOH

Covers roadside digital billboards, street furniture and transit screens, place-based screens (stations, malls, elevators, gyms, venues), spectaculars and anamorphic or 3D screens, including contextual and dynamic DOOH.

## The encounter

Public space, a moving or waiting viewer, and a shared rotation with other advertisers. Encounters range from a driver's glance at speed and distance, to a pedestrian passing, to someone waiting with minutes to spare. The encounter type, not the screen, decides how much the work can say.

| Encounter | Typical condition | Design consequence |
|---|---|---|
| Roadside | Moving, distant, seconds, attention on the road | One thought, very few words, huge type, no fine detail |
| Street and transit passing | Walking, close to mid distance, brief | One thought, one image, readable in stride |
| Place-based dwell | Waiting, close, longer | Can reward a second look: sequence, detail, wit |
| Spectacular or anamorphic | Crowds, fixed viewpoints, event-like | The spectacle must carry the brand idea from where people actually stand |

## The format's job

Be understood at a glance by someone not trying to look, and be remembered as this brand.

## Specifications

Reference specifications by venue, network and media owner, with roadside and legibility guidance, are in `shared/knowledge/dooh-ads/`. They are network-dependent: the media owner's spec for the actual plan governs.

Screen resolution and ratio, spot length, loop, whether motion or transitions are allowed, file types, brightness and approval rules are set by the media owner and often by local regulation, especially for roadside. They vary widely. Use the media owner's spec sheet and cite it; otherwise label UNVERIFIED.

## Craft

**The glance test.** One idea, one image, a handful of words, unmistakable brand. If you need to read it twice, it has failed.

**Every frame must communicate.** The viewer arrives at a random moment in the spot and leaves at another. Motion should be slow and legible, never a build-up to a payoff someone will miss. Where motion is not allowed, design the static version first.

**Scale detail to the screen, not the file.** Large LED screens have low effective resolution. Thin strokes, small type, fine texture and subtle gradients break down or shimmer. Bold shapes and strong contrast survive.

**Contrast for light conditions.** Screens are seen in daylight and at night. Test the design in both, and avoid pale-on-pale palettes that wash out.

**Use the place.** The best DOOH knows where it is: the street, the station, the weather, the time. Context is a creative resource, not only a targeting setting.

**Contextual and dynamic DOOH.** When content changes with time, weather, location or live data, the idea must use the context, not merely insert it. Design a variant set and a simple trigger table, including the fallback when data is missing.

**Anamorphic and 3D.** The illusion only works from specific viewpoints and depends on the screen's corner geometry. Design from the real sightline and show the view from where it breaks.

**No sound.** Assume silence unless the spec says otherwise.

## What to prototype

- The creative at the screen's true ratio, as a loop at real timing with a static fallback.
- A distance simulation: the design rendered very small or blurred beside the full-size version.
- An environment mockup in realistic perspective and scale, with competing surroundings, in day and night light.
- For dynamic work, the variant set and trigger table.
- For anamorphic work, a view from the intended sightline and from an off-axis position.

## Buildability flags

- Motion or transitions where the placement may restrict them.
- Spot length or loop assumptions not confirmed by the media owner.
- Live data feeds, triggers or real-time content the client or vendor cannot provide.
- Screen geometry assumptions for anamorphic content.

## Fidelity check additions

- [ ] Passes the glance test at simulated distance.
- [ ] Any random frame communicates.
- [ ] Holds up in day and night light.
