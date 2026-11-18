# 3D + GSAP options study (DEVELOP input)

| | |
|---|---|
| Client | Traffik (the agency itself) |
| Project | Website D2C |
| Source scope | PROJECT-LEVEL. normalized-brief v03 §2, §3a, §3b (case visibility + craft preference notes), director convergence 2026-11-18, discovery deck s10/s29 |
| By | design-champ (Interaction design specialty), 2026-11-18 |
| Mode | DEVELOP input. Options study, not a build. No verdicts |
| Status | For creative-engine-director, then Andres |

## Constraints every option must meet

- **Idea first.** 3D or motion must carry the CCI ("the rule everyone works around becomes the idea") or the "work leads" frame. If removing the effect loses nothing but polish, it is out.
- **Performance (deck s10, s29).** Lighthouse target 90; LCP ≤ 2.5 s; page weight is the current problem (parent site 69 / LCP 4.3 s). Rule for every option: **the LCP element is static HTML text or a poster image, never a canvas.** 3D and GSAP load after first paint (dynamic import on idle or on intersection), with a JS budget of about 60 KB gzip for GSAP + plugins on the homepage and three.js (~150 KB gzip) only where an option needs it.
- **Reduced motion.** `prefers-reduced-motion: reduce` gets the final composed state, no scrubbing, no camera moves; content order and meaning identical.
- **Guardrails (§3a).** No traffic-signal imagery or words (lights, stop/go, barriers, tape, warning signs). No red-pen redlines or APPROVED/REJECTED stamps as a house motif; real markup only where a case has it and A8 allows. Red and yellow carry evidence only.
- **Platform (Q5: most likely Framer or Webflow, not final; Andres 2026-11-18).** Webflow: native GSAP in Interactions (incl. ScrollTrigger, SplitText, Flip), Spline embeds, custom code embeds for three.js. Framer: React code components (three / R3F, gsap), native scroll and appear effects, shared-element page transitions, Spline embeds. Each option below notes how it is done in each, and where the CMS (39 cases as items, filtering, per-item 3D assets) limits it.
- **Note on GSAP licensing:** GSAP and all its plugins (ScrollTrigger, Flip, SplitText, MorphSVG) have been free for commercial use since the Webflow acquisition (2024/25). [verify current terms before build]

## Options

### 1. Rule-to-idea type transform (GSAP SplitText + ScrollTrigger)
- **What it does.** Pick 1 hero. The client's rule sits as plain source text. On first scroll, SplitText breaks it into words; the words that constrain ("can't tell seniors which plan to pick") stay anchored while the line re-sets into the idea ("tell them what to ask"), and the shipped work scales in beside it. Plays once, then settles.
- **Why it serves the idea.** It *is* the CCI happening on screen: the visitor watches the rule become the idea. No other option shows the method this literally.
- **Route.** Pick 1 "The rule, first". Reusable as the opener of each Tier A case page (P1-B headline).
- **Perf.** Text is real HTML and is the LCP; GSAP core + ScrollTrigger + SplitText ≈ 45 KB gzip, deferred. Near-zero LCP risk. Watch CLS: reserve line boxes before splitting.
- **Reduced motion.** Rule and idea shown stacked, static, with the work beside them. Reads the same.
- **Platform.** *Webflow:* native GSAP in Interactions now includes SplitText and ScrollTrigger; build visually, rule/idea lines bound to CMS fields per case. *Framer:* a React code component using gsap + SplitText (Framer's native appear/scroll effects can't split by word and re-set a line); CMS fields passed as props. Both work. CMS: needs two plain-text fields (rule, idea) with length limits.
- **Watch.** Director's fix 2: the work must be the largest thing on screen by first scroll. The transform ends with the work at full scale, the text small.
- **References.** GSAP SplitText showcase demos (gsap.com/showcase); Locomotive's editorial type reveals (locomotive.ca).

### 2. The case as a document stack in 3D (three.js or CSS 3D)
- **What it does.** Each hero case is a short stack of real artifacts in shallow 3D: the rule (actual form, disclosure, plan-choice sheet), then the brief line, then the shipped work on top. Scroll lifts the stack apart along Z; the work lands flat and full-bleed. Depth = how far the idea travelled from the rule.
- **Why it serves the idea.** Episode anchor (§3a #3): real rule, real material. Depth gives "rule → idea → shipped" a physical order without arrows or signal language.
- **Route.** Pick 1, and Tier A case pages. Could carry Pick 2's lower PIH proof.
- **Perf.** CSS 3D version (transform-style: preserve-3d on 3–4 image planes) costs only the images; preferred. three.js version only if lighting/paper material matters (~150 KB + textures). Poster image is the LCP; scene hydrates on intersection. AVIF textures, ≤ 300 KB per case.
- **Reduced motion.** Planes laid out side by side, flat, left to right.
- **Platform.** *Webflow:* CSS 3D via Interactions' 3D transforms on 3–4 CMS image fields per case, scroll-driven by native GSAP; three.js version via custom code embed reading CMS image URLs, or a Spline embed (but Spline scenes are per-file, not CMS-bound). *Framer:* code component with R3F/three or CSS 3D, images as CMS props; Spline embed same limit. Both work for CSS 3D. CMS: a fixed set of image slots per case (rule artifact, line, work); Webflow multi-image fields cap at 25 images and offer no per-image metadata, so use named single-image fields. Per-case Spline scenes don't scale to 39 items; avoid.
- **Watch.** A8: needs permission to show the real rule material. Paper must not drift into stamp/redline imagery; only real markup, only where allowed.
- **References.** Apple product "exploded view" scroll pages; Stripe Sessions site's layered cards; Active Theory's work (activetheory.net) for restrained WebGL paper.

### 3. Six-case homepage rail with GSAP Flip into the case page
- **What it does.** The 6 hero cases sit as a horizontal (desktop) / vertical (mobile) rail of large stills. Clicking one uses Flip (with a View Transitions API fallback) to grow the still into the case page hero without a cut.
- **Why it serves the idea.** "Work leads" all the way through: the visitor never leaves the work to reach the work. Continuity also makes 6 cases feel like a curated set, not a teaser for a list.
- **Route.** Both picks; strongest in Pick 2 (work-first, full-bleed hero).
- **Perf.** Flip ≈ 6 KB. Stills are the LCP: one priority-loaded, five lazy. Native View Transitions handle the cross-page case with zero JS where supported.
- **Reduced motion.** Instant navigation, standard page load.
- **Platform.** *Framer:* strongest; native shared-element page transitions (magic motion) between a CMS collection list and CMS detail page, no code. *Webflow:* page loads are full reloads; needs custom code with the cross-document View Transitions API (Chromium/Safari 18+) or a Barba.js-style setup, which fights Webflow's interactions re-init. Works best on Framer; Webflow version is a fallback-quality crossfade unless custom code is accepted. Flag: **near Framer-only** at full quality.
- **References.** Flip demos on gsap.com/docs (Flip plugin); Obys agency (obys.agency) case transitions; Chrome's View Transitions docs.

### 4. Work page (39 cases): Flip-animated filtering
- **What it does.** Filtering by division · service · industry (deck s26 tags) re-flows the grid with Flip: matching cases glide to their new slots, others fade out. Each card states its rule (Pick 1) or habit broken (Pick 2) in one line.
- **Why it serves the idea.** Usefulness, not spectacle: the validator sees the set respond to their category, and the rule line becomes the filterable thread. Motion keeps orientation in a 39-card grid.
- **Route.** Work page, both picks.
- **Perf.** Flip only; images lazy, 39 cards rendered server-side (crawlable, fine for SEO and the Orange County local search job). URL reflects filter state.
- **Reduced motion.** Instant re-flow.
- **Platform.** *Webflow:* CMS collection list + Finsweet Attributes (List Filter) + GSAP Flip in custom code, or native GSAP Interactions on filter change; reliable, widely used. *Framer:* native CMS filters on collection lists exist but are limited (filter at build, not visitor-driven); visitor filtering needs a code component holding all 39 items and animating with gsap Flip or Framer Motion `layout`. Both work; Webflow is simpler. CMS: tags as multi-reference fields (division, service, industry); Webflow collection lists show 100 items per list (fine for 39, +12/year) and nested multi-ref filtering needs Finsweet.
- **References.** Pentagram's project index (pentagram.com/work); GSAP Flip filter demo (CodePen, GSAP official).

### 5. Work page as a 3D index field (three.js, optional view)
- **What it does.** An alternate "field" view: 39 case thumbnails as planes in a shallow 3D grid; filters pull the matching cases forward in Z and dim the rest. Hover tilts a plane and reveals the rule line. Grid view stays the default.
- **Why it serves the idea.** Shows the whole body of work at once (39 cases across 4 former sites now in one place), and depth = relevance to the visitor's category. This is the most "3D-forward" option and the clearest home for Andres's 3D preference without putting WebGL on the homepage critical path.
- **Route.** Work page, either pick.
- **Perf.** three.js + instanced planes + a texture atlas (~1–1.5 MB total, loaded only when the field view is opened). Never the default view, never on mobile by default.
- **Reduced motion.** Field view disabled; grid only.
- **Platform.** *Framer:* code component with R3F; CMS data must be fed in (code components can't query the CMS directly, so either pass via a collection list wrapper or a JSON export), workable. *Webflow:* custom code embed reading the rendered collection list from the DOM and building the scene; works but fragile and outside the Designer. A Spline scene can't take 39 dynamic CMS textures. Both possible, neither native; plan it as custom dev either way. CMS: per-item thumbnail at a fixed aspect for the texture atlas.
- **References.** Bruno Simon / Lusion portfolio indexes (lusion.co); Resn and Immersive Garden archive pages.

### 6. The proof row that counts in from source (ScrollTrigger)
- **What it does.** Under the hero, each result figure animates from its source line (client, metric, source + year) into the large number; the source stays attached as a caption.
- **Why it serves the idea.** "Can we trust you?" (five-question test). The motion makes the source the origin of the number, which matches Results cannot publish without source + year (P1 fix 4). Small, but it carries the candor.
- **Route.** Both picks; case pages.
- **Perf.** Negligible. Numbers are real HTML, final values in markup.
- **Reduced motion.** Final number + source shown.
- **Platform.** *Webflow:* native GSAP Interactions (number counter + scroll trigger), figures from CMS number + text fields. *Framer:* native appear effects can't count numbers; small code component (or community counter component). Both work. CMS: each result = number field + source text + year, required together; Webflow and Framer can't enforce 'number requires source' natively, so it's an editorial rule or a validation script.
- **Watch.** All figures `[unverified]`; nothing ships without source. No tally/award-counter feel.
- **References.** NYT/Pudding data reveals (pudding.cool); Stripe annual letter number treatments.

### 7. Ambient depth in the dark ground (shader, Pick 2 only)
- **What it does.** A very slow WebGL noise/grain field behind the Pick 2 full-bleed case, taking its color from the case still (sampled), so the dark Swiss ground feels like a lit room around the work.
- **Why it serves the idea.** Weakest link to the CCI; it serves "work leads" only by staging. Included because it is the cheapest true-3D/shader touch, and to be honest that it is mostly atmosphere. Candidate to cut.
- **Route.** Pick 2.
- **Perf.** One fragment shader via OGL (~10 KB) instead of three.js; starts after LCP; paused off-screen and on low-power devices.
- **Reduced motion.** Static gradient.
- **Platform.** *Webflow:* custom code embed (OGL) or a Spline embed with a looping scene; per-case color sampled at runtime from the CMS image. *Framer:* code component, or Framer's own shader/gradient effects, or Spline embed. Both work.
- **References.** Linear and Vercel ambient backgrounds; OGL examples (github.com/oframe/ogl).

## Summary table

| # | Option | Route | Carries idea? | Perf risk | Webflow / Framer |
|---|---|---|---|---|---|
| 1 | Rule-to-idea type transform | Pick 1, case pages | Strongly (CCI) | Low | Both |
| 2 | Case as document stack (3D) | Pick 1, case pages | Strongly (episode anchor) | Low (CSS) / Med (three.js) | Both (CSS 3D) |
| 3 | 6-case rail + Flip to case | Both, strongest Pick 2 | Work leads | Low | Framer best; Webflow needs custom code |
| 4 | Work page Flip filtering | Work page | Usefulness | Low | Both; Webflow simpler |
| 5 | Work page 3D field view | Work page | Body of work, relevance | Med (opt-in) | Both, custom dev either way |
| 6 | Proof counts in from source | Both | Candor / trust | Negligible | Both |
| 7 | Ambient shader ground | Pick 2 | Weak, staging | Low | Both |

**One-platform flag:** only Option 3 is meaningfully better on one platform (Framer). Every other option works on both.

**CMS limits across options:** 3D assets per case don't scale as Spline scenes (one file each, not CMS-bound), so per-item 3D must be built from CMS images in code (Options 2, 5). Visitor-driven filtering is plugin-based on Webflow (Finsweet) and code-based on Framer (Option 4). Neither CMS enforces 'result requires source + year' (P1 fix 4).

## Top 2 recommendations

1. **Option 1, rule-to-idea type transform** (with Option 6 riding along). It is the CCI made visible, costs almost nothing in performance because the LCP stays HTML text, and it scales from the homepage to every Tier A case page. If Pick 1 survives, this is its signature.
2. **Option 2, the case as a document stack, CSS 3D first.** It gives Andres real 3D that means something (depth from rule to shipped work), works for either pick's PIH proof, and keeps the image as LCP. Upgrade to three.js only if the CSS version proves the idea and needs material quality.

Option 5 is the place for a bigger WebGL moment if Andres wants one, kept off the homepage and opt-in.

## First prototype

**Option 1 on PIH, one HTML file:** rule text → idea line → shipped work scaling in, GSAP SplitText + ScrollTrigger, with the reduced-motion state and a Lighthouse run on throttled mobile. Built as a Framer code component and a Webflow Interactions version side by side, which also tests the platform question. A few hours of build. It answers the three questions that matter at once: does watching the rule become the idea read in 3 seconds, does the work win the scale contest (director fix 2), and does it hold LCP ≤ 2.5 s. Blocked only on Andres Q1 (exact PIH rule wording); a clearly labeled placeholder rule can stand in for the test.

## Open
- Q5 final pick between Framer and Webflow: mainly decides Option 3 quality and how much of Options 4–5 is code.
- A8 per client decides whether Option 2 can show real rule material.
- GSAP licence terms and plugin availability: verify at build.
- References are listed for study, not checked live today.

## Prototype built – 2026-11-18

- File: `work/develop/prototypes/option1_rule-to-idea_pih.html` (single HTML, GSAP 3.12.5 core + ScrollTrigger from cdnjs, manual word split, no SplitText).
- Sequence: placeholder rule on cream panel → "Rule:" line arrives → on scroll (pinned) the rule fades and shrinks, "Idea:" line lands in red, the work placeholder scales past the rule → "Ideas that survive review." → proof row (77% counts up, yellow, UNV) → next step.
- Static page is complete without JS; reduced motion skips all motion except instant figures. LCP is HTML text.
- Checked in browser at 1440×900 and 375×812, no console errors. Mobile fix: line moves above the work so rule + line read in the first screen.
- PIH rule shown at category level ("Medicare marketing limits what a plan can tell a senior."), per Andres 2026-11-18: verbatim wording belongs to new PIH work, not the website; Q1 closed for the site. Shipped work now the real PIH print ad (content inventory, /work/pih/ block 26). Still placeholder: Netwatch rule and figure, benchmark source for 77%. Fonts are stand-ins.
- Not done: Lighthouse throttled-mobile run; Framer code component and Webflow Interactions versions (Q5).
