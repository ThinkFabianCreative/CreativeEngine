# Marble run: visual style options (teaching note)

CLIENT: Traffik (own agency) · PROJECT: website-d2c · SOURCE SCOPE: PROJECT-LEVEL · Author: art-teacher · 2026-11-22
Status: teaching note for design-champ and Andres. Not a verdict, not a build spec.

Fixed givens: black ground #000, paper #F1EBDD, one red #d91f1f (our marble only), evidence yellow #f4d803 (figures only), Acumin Pro Condensed caps, flat 2D, scroll-driven, Webflow later.

The one lesson under all five: **the red marble only reads as the hero if nothing else on the page is red and the path is legible at a glance.** The style's job is to make "right fork / wrong loop" readable without labels. Pick the style that makes the decision points clearest, not the one that looks most like a toy.

---

## 1. Network Map
**Lineage:** Harry Beck's London Underground diagram (1933); Massimo Vignelli's NYC Subway diagram (1972).
- **Track:** paper-colored lines of one weight, 45°/90° angles only; forks are junctions, dead ends are terminus bars.
- **Marbles:** flat dots the width of the line. Red rides the line; greys sit on spurs and loop lines.
- **Obstacles:** closed-station marks or line breaks that close up as red approaches.
- **Type:** Acumin caps as station names ("STRATEGY", "CREATIVE", "MEDIA"); yellow figures at stops as results.
- **Says:** we know the route; navigation, clarity, a system.
- **Risk:** too calm for "disruption"; reads as an infographic. Station names can turn into a services list.
- **Search:** "Beck tube map 1933 original"; "Vignelli 1972 subway diagram"; "Jug Cerovic INAT metro maps".

## 2. Swiss Kinetic
**Lineage:** Josef Müller-Brockmann's concert posters (Tonhalle, *der Film*); Anton Stankowski's constructive graphics.
- **Track:** thick black/paper bars on a strict grid, diagonals at one fixed angle; the track *is* the layout grid.
- **Marbles:** perfect circles, large, scale shifts between sections.
- **Obstacles:** grid bars that slide out of the way, like modules rearranging.
- **Type:** huge condensed caps set into the grid; the belief line becomes part of the track the marble rolls along.
- **Says:** rigor, control, design authority.
- **Risk:** the obvious "designer" choice; can feel cold, and is Andres's own preference, so test it is right for the audience, not just for us.
- **Search:** "Müller-Brockmann Tonhalle poster"; "Stankowski Grafik"; "Experimental Jetset Whitney".

## 3. Title Sequence Cut-paper
**Lineage:** Saul Bass titles (*Anatomy of a Murder*, *Vertigo*, *North by Northwest*); Bass's ragged-edge cut paper.
- **Track:** cut-paper strips with slightly rough edges, paper on black; angles that feel hand-placed.
- **Marbles:** cut circles, a touch irregular; greys are just paper-tone circles muted.
- **Obstacles:** paper shapes that get pulled off frame, hard cuts not eases.
- **Type:** credits-style caps that enter and exit with the motion; the line lands as a title card at the end.
- **Says:** drama, intent, authorship; a story with a payoff.
- **Risk:** Bass pastiche is widely imitated and easy to cheapen; rough edges done by filter look fake. Most expensive to make well.
- **Search:** "Saul Bass Anatomy of a Murder titles"; "Saul Bass North by Northwest title sequence"; "Kyle Cooper Catch Me If You Can titles" (Bass homage, Kuntzel + Deygas).

## 4. Chain Reaction Blueprint
**Lineage:** Fischli/Weiss *Der Lauf der Dinge* (1987); Rube Goldberg drawings; patent and engineering drawings.
- **Track:** thin paper line drawings with dimension marks, labels and hatching; ramps, levers, seesaws.
- **Marbles:** outlined circles; red is the only filled one.
- **Obstacles:** mechanisms (gates, levers) the red marble *triggers*, so obstacles clear because of a cause shown on screen.
- **Type:** small caps annotations as callouts ("FIG. 3: INSIGHT"); yellow numbers as measured outputs.
- **Says:** we engineer results; cause and effect, nothing is luck.
- **Risk:** detail fights legibility on mobile; the "clever contraption" can tip into whimsy instead of disruption. Busy greys can read as mockery.
- **Search:** "Fischli Weiss Der Lauf der Dinge"; "Honda Cog ad 2003" (borrowed the idea, watch for the plagiarism lesson); "Rube Goldberg self-operating napkin".

## 5. Arcade Vector
**Lineage:** 1970s–80s vector arcade (Atari *Asteroids*, *Tempest*), pinball playfield art, Wim Crouwel's *New Alphabet* grid thinking.
- **Track:** glowing single-weight lines on black, sharp bumpers and flippers at forks.
- **Marbles:** bright points with a short trail; greys have dim trails that circle loops.
- **Obstacles:** bumpers that switch off, gates that drop; score-style yellow figures pop on.
- **Type:** caps set like a scoreboard; "TRAFFIC DRIVERS." as high-score screen.
- **Says:** energy, competition, winning; disruptive and a bit cheeky.
- **Risk:** highest generic-AI risk (neon glow on black is everywhere); gloating, since a game frames competitors as losers; glow can sneak red into other elements.
- **Search:** "Atari Tempest 1981 vector"; "pinball playfield art Bally"; "Wim Crouwel New Alphabet 1967".

---

## Cross-cutting risks to teach
- **Gloating:** greys should simply stall (loop, stop), never crash, mock or get labeled. Anonymous stays anonymous.
- **Legibility:** every fork needs one beat of stillness so the reader sees the choice before red takes it.
- **One red:** no red in type, hover states or warnings anywhere on the page.
- **Yellow discipline:** yellow only on figures; resist using it to highlight the route.

## Which I'd teach toward
**Network Map (1), with Swiss Kinetic (2) as its typographic partner.** The idea is "taking the right route", and transit diagrams are the design form whose whole history is making routes and choices readable instantly. It holds the one-red rule naturally (a line colour is an identity), survives phone width, and builds in Webflow as flat SVG. Its weakness, calm, is fixable by pacing: hold still at forks, then let red move fast. Fischli/Weiss (4) is the richer idea if Andres wants causality (we remove obstacles) to be the point; teach it as the alternative, not the default. Arcade (5) is the one to avoid unless DesignChamp can prove it isn't generic.
