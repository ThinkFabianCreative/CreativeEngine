# MFK website design rules

Status: working design direction for the local homepage prototype, October 18, 2026. Client approval remains pending. User instructions and client evidence take priority over these rules.

## Purpose and character

Make the ordinary family life MFK helps protect visible and easy to support. Warm, photo-led, readable and trustworthy. Evolve the existing identity. Preserve the supplied logo, family-centered voice, program names and destinations.

Taste Skill configuration: DESIGN_VARIANCE4, MOTION_INTENSITY2, VISUAL_DENSITY4. This is a restrained brand evolution. Material 3 Expressive informs selected shapes and component grouping; the static HTML is a custom implementation, not the official Material Web package.

## Color roles

All reading text and icon strokes remain greyscale: primary#242424, secondary#595959 on tested light surfaces, reversed#FFFFFF on tested dark surfaces. Never assume a neutral color passes on every background. Keep source logos and documentary before screenshots unchanged.

| Role | Existing identity | Optional light program surface |
|---|---|---|
| Lifeline / bill pay | #31B744 green | #EAF7EC |
| Safe Haven / housing | #A92061 magenta | #F8E9F0 |
| Balance / wellness | #27BBC9 teal | #E8F7F9 |
| Boost / basic needs | #F99400 orange | #FFF0DB |
| Pillars / stability | #79BDE9 sky | #EBF5FC |

Keep all five existing hues. Program names and service descriptions accompany color. Primary Donate actions use#A92061 with white text. Retain navy#002855 for established structural surfaces. Yellow #FFD23F supports bold emphasis in the bills section and family quote. Use deliberate saturated section blocks alongside calm reading areas. The page should retain Material 3 Expressive surface contrast rather than becoming uniformly pale.

## Typography

Default proposal: Anago as the reading/interface/display family, with Playpen Sans for a brief meaningful accent. Bogart+Anago remains a comparison option, not an extra simultaneous family. Preserve the supplied wordmark without retyping it.

- Hero:40–60px desktop,34–40px phone, about1.12 line-height. Protect the full handwritten line with1.16 line-height. Aim for2–3 natural lines without shrinking readable body text.
- Section heading:32–48px, line-height1.15. Card heading20–28px/1.2–1.25.
- Body 17px/1.55; lead 19px/1.6 desktop and17px/1.5 mobile. Keep long reading measures below roughly60–65characters.
- Interface16px/24px, weight700 on buttons. Metadata14–16px. Eyebrow14px with modest tracking.
- Avoid animated weight changes and excessive negative tracking. These can shift labels or crowd letterforms.
- Adobe web project: https://use.typekit.net/scu3oyi.css. Test the actual loaded font and fallback, not just the declared family name.

## Spacing and layout

Use a4px base:4,8,12,16,24,32,48,64,96. Main content caps around1200px. Side padding20px on phones and at least24px on larger screens. Section padding80px desktop,48px phone; allow64px where dividers need room.

Desktop hero separates neutral text from a4:3 family photograph in a friendly arch. Keep the invitation to donate visible in the initial desktop viewport at 1280 × 720. On phones, image precedes text. Avoid text overlays across faces.

Mobile story cards form a native horizontal rail, navigable through keyboard focus as well as touch scrolling. Put the family quotation outside the story-card sequence. Mobile programs use88px photo thumbnails beside a shared text hierarchy. Preserve the five names and colors. Do not turn every service into a full-screen image card.

## Controls and states

Primary action: magenta fill, white label, minimum 52px height,16px/24px700,12px24px padding, pill radius. Hover#8D1B51, pressed#741642. Use subtle transform feedback; never change font weight on hover. Secondary actions use neutral text and a visible boundary or clear text-link treatment.

Native mobile menu disclosure restores the links hidden by the desktop navigation breakpoint. Keep the logo at 99px wide on phones and 112px on desktop; do not allow flexbox to shrink it to zero. These sizes are prototype choices, not an approved brand minimum-size rule.

Story filters must change visible stories, not only their pressed appearance. Visible focus uses a3px neutral outline with4px offset. Reversed surfaces require a white focus outline. All tap targets should be44px or larger; primary actions52px.

Review tools live in a collapsed Preview settings disclosure in normal flow. Never place a review stamp over the logo or customer content. Do not auto-open a donation dialog or show a second floating Donate button over the page.

Newsletter is a design-only component. Do not imply subscription success, collect data or add a backend without explicit project scope.

## Shapes, images and depth

Keep the existing small shape family and section waves. Protect faces in crops. Use a24px card radius,16px utility/input radius and pill buttons. Additional photo shapes require a reason. No heart photo containers.

Flat sections are the baseline. Use a restrained shadow only when a surface needs to read as floating or actionable. Avoid large decorative shadows on ordinary text blocks.

Borrowed/Gillette family images remain labeled placeholders and require replacement. Bracketed metrics require client validation. Keep these disclosures during internal review.

## Icons

React Feather 2.0.10, native24 × 24 grid, strokeWidth 2, round caps/joins, currentColor. Decorative icons are aria-hidden and visible text labels remain. CreditCard/Lifeline,Home/Safe Haven,Sun/Balance,ShoppingBag/Boost,TrendingUp/Pillars. Keep this family instead of adding a second icon package.

## Reference provenance

Method: installed .claude/skills/design-taste-frontend/SKILL.md, subject to DesignChamp/skills/taste-skill.md and this project's brief.

Independent website analyses from VoltAgent/awesome-design-md at revision 3b605329240ce735b510037cca322f1831fdd7f8:

- [Airbnb](https://github.com/VoltAgent/awesome-design-md/blob/3b605329240ce735b510037cca322f1831fdd7f8/design-md/airbnb/DESIGN.md): spacing relationships, restrained elevation, readable controls and mobile navigation. Do not borrow its brand font or primary hue.
- [Figma](https://github.com/VoltAgent/awesome-design-md/blob/3b605329240ce735b510037cca322f1831fdd7f8/design-md/figma/DESIGN.md): neutral reading across playful surfaces, role-based radii and clear action hierarchy. Do not borrow its palette or product aesthetic.
- [Mastercard](https://github.com/VoltAgent/awesome-design-md/blob/3b605329240ce735b510037cca322f1831fdd7f8/design-md/mastercard/DESIGN.md): consistent spacing/radius families and distinction between expression and reading. Reject its extreme whitespace, orbit decoration and proprietary fonts for this page.

These are third-party observations, not official brand specifications or accessibility authorities. MFK values and user choices override them. For accessibility use WCAG source guidance and actual measurements.

## Expressive surface correction

User feedback on October 18 supersedes the muted-surface refinement: saturated program cards are the default. Lifeline green, Balance teal, Boost orange and Pillars sky use charcoal text. Safe Haven magenta uses white text. White statistic chips keep charcoal labels. The trust section returns to magenta with white reading text and a white logo panel; the closing section uses sky with charcoal. Selected story filters use magenta/white against sky/charcoal options. Preserve the restored mobile logo, compact rows, working filters and restrained type. This is an evolution in application, not replacement of the existing program hues.

## Expressive shape trial · October 18

Current Adobe prototype uses Filson Soft Bold for display, section and card headings with Anago reading and controls. The historical `pair=anago` URL selects this pairing; its preview label names both fonts. Existing Bogart and original comparisons remain. Dials: DESIGN_VARIANCE6, MOTION_INTENSITY2, VISUAL_DENSITY4.

Sky hero and closing block, yellow impact section and family quote, and magenta trust block create a connected color story. Program hues remain unchanged. Shape roles: arch for family photography, soft geometric blocks for program grouping, occasional burst for impact, broad wave for section transitions. Rounded utility inputs16px, program blocks32px desktop/24px mobile, actions pill; asymmetric outer corners are intentional display treatments. No clipping of text into decorative shapes. Mobile retains compact thumbnail-and-copy program rows.

This is custom HTML/CSS inspired by Material 3 Expressive geometry, not an official Material Web implementation. Preserve source photography, routes, labels and provisional metric disclosures.

## Warmth, elevation and proximity correction
User feedback supersedes the flat-card trial: actionable cards use two-layer base shadows (3px6px and12px24px) and a stronger hover state. Saturated program shells contain warm paper reading surfaces with neutral333text on desktop and mobile. Preserve the colors; do not reduce them to thin accent strips. Story video actions group play, title and duration with12px proximity, while the whole tile remains a link. Program photographs keep4:3containers at both sizes; the impact cookie is square-native1:1geometry. Playpen400 returns only in the hero phrase and family quotation.
