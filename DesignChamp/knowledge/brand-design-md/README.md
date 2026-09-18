# Brand DESIGN.md library

This library holds 74 unofficial, AI-readable analyses of real brands' public websites. Each file follows the DESIGN.md format: tokens in YAML front matter, then prose on colour, typography, layout, elevation, shapes, components, do's and don'ts, and responsive behaviour. This page is the index. The files are in `files/<slug>.md`.

| | |
|---|---|
| Source | `github.com/voltagent/awesome-design-md` (MIT, `LICENSE`), commit `8147538` (2026-07-31) |
| Owner | DesignChamp |
| Status | Added at the user's request 2026-09-14 after review |
| Local changes | Copied `design-md/<slug>/DESIGN.md` to `files/<slug>.md`. The per-brand `README.md` stubs were omitted: they only link to the commercial site `getdesign.md`. File contents are unmodified |
| Holds | No CreativeEngine client facts |

## Review

- **Markdown only.** No scripts, no hidden Unicode, and no text addressed to an agent.
- **Commands are page content.** `ollama` and `opencode.ai` describe on-page `curl … | bash` install snippets. Those are descriptions of the site, never commands to run.
- **No outbound links besides the source.** The only links in the files are to `getdesign.md` (the publisher) and those two install snippets. The upstream README promotes paid products (getdesign.md requests, EveryFeed, LaunchKit), which are not part of CreativeEngine.
- **These are interpretations, not official brand guidelines.** Each file calls itself an "inspired interpretation", and several misspell the brand name in front matter (for example "Stripi"). Values were extracted from public websites around mid-2026 and may be wrong or out of date.

## How DesignChamp uses it

| Mode | Use | Do not |
|---|---|---|
| EXPLORE | Study how a strong brand turns one idea into a system: a single brand colour carrying every CTA, photography-as-gallery, a custom display face as voice. Borrow the *mechanism*, then apply it to our idea | Hand a client another brand's look. "Make it feel like Stripe" is a starting reference, never a territory |
| DEVELOP | Model for documenting our own direction: token naming, component grammar, do's and don'ts, responsive rules | Copy token values or signature components into a client system |
| JUDGE | Category-sameness check. Compare our work with the category's leaders here (fintech, dev tools, automotive, AI labs). If it could sit unnoticed among them, it is not yet distinctive (CLAUDE.md principles 10 and 11) | Treat resemblance to a celebrated brand as quality |
| Competitor context | Inside a project, cite a file as an external, unverified reference about a competitor's public web presence, with source and date | Record it as a verified fact or a client-level finding |

## Guardrails

- **Brands here are not clients.** If a CreativeEngine client appears in this library, its file is *not* a client brand source. Brand identity comes from the client's approved brand sources in `projects/<client>/client/`. Record any conflict as a divergence. Never promote this file into client knowledge.
- **No impersonation.** Do not produce work that could pass as a real brand's own: its identity, trade dress, logo, or a page presented as theirs. Pitch or spec work for that brand is labeled as such. Never publish an artifact imitating a real brand.
- **Fonts are proprietary.** Many systems name proprietary or custom faces (Söhne, SF Pro, Cal Sans, BMW Type Next). Files suggest substitutes; flag licensing before anything leaves prototype.
- **Coverage is skewed.** The library leans towards developer tools, SaaS and AI companies, plus some automotive, consumer and archival sites (`dell-1996`, `nintendo-2001`). It is not a map of good design in general, and gaps are not judgments.
- **Retrieve selectively.** Scan this index, then open only the one to three files the task needs (27–54KB each).

## Index

Size is in KB. The register is the source's own description, trimmed.

| Slug | KB | Register |
|---|---|---|
| `airbnb` | 30 | A warm, generous consumer marketplace anchored on a clean white canvas and Airbnb Rausch (#ff385c), the single brand voltage that carries… |
| `airtable` | 35 | A sober, editorial workflow-software interface anchored on white canvas and dark-ink type, where brand voltage comes from full-bleed… |
| `apple` | 36 | A photography-first interface that turns marketing into a museum gallery. Edge-to-edge product tiles alternate light and dark canvases,… |
| `binance` | 39 | A confident financial-platform interface anchored on a deep near-black canvas, where Binance's iconic yellow (#FCD535) carries every… |
| `bmw` | 27 | BMW's corporate site — distinct from BMW M's motorsport-bombastic variant, this is a measured and settled corporate-automotive interface.… |
| `bmw-m` | 30 | A motorsport-engineering interface anchored on a near-black canvas with white BMW Type Next Latin display headlines in confident UPPERCASE.… |
| `bugatti` | 28 | An austere luxury-automotive interface that uses near-pure black canvas, white uppercase letterspaced display, and full-bleed automotive… |
| `cal` | 30 | A clean, calendar-software-first interface anchored on white canvas with black primary CTAs and custom Cal Sans display typography. The… |
| `claude` | 33 | A warm-canvas editorial interface for Anthropic's Claude product. The system anchors on a tinted cream canvas with serif display headlines,… |
| `clay` | 25 | A vibrant claymation-meets-data interface for Clay.com (GTM data-orchestration platform). Anchors on white canvas with dark-navy primary… |
| `clickhouse` | 25 | A high-performance database interface anchored on near-pure black canvas with electric yellow as the brand voltage. White typography in… |
| `cohere` | 20 | Cohere's 2026 web system is a controlled enterprise AI interface built from stark white editorial space, deep green-black product bands,… |
| `coinbase` | 25 | An institutional-grade crypto exchange whose marketing surfaces read like a quietly-confident financial-services brand. The base canvas is… |
| `composio` | 20 | A developer-tools brand for AI-agent tool integration whose marketing surfaces lean into a dark, technical aesthetic with a single… |
| `cursor` | 21 | An AI-first code editor whose marketing site reads like a quietly-confident developer-tools brand with a warm-cream editorial canvas… |
| `dell-1996` | 34 | a catalog-era enterprise web design built around a literal black page frame, vivid flat color-block "ribbon cards" tinted in sage, salmon,… |
| `elevenlabs` | 20 | A voice-AI brand whose marketing surfaces read like a quietly editorial print magazine. The base canvas is off-white (`#f5f5f5`) holding… |
| `expo` | 21 | A React Native developer-platform whose marketing site reads like a quietly-confident infrastructure brand. The base canvas is pure white… |
| `ferrari` | 24 | A luxury-automotive brand whose marketing surfaces read as cinematic editorial. The base canvas is **near-black** (`#181818`) holding pure… |
| `figma` | 32 | A confident black-and-white editorial frame interrupted by oversized, hand-cut pastel color blocks. The marketing canvas is rigorously… |
| `framer` | 28 | A confident dark-canvas builder marketing site that treats the page like a working artboard — pure black surfaces, white display type set… |
| `hashicorp` | 27 | An enterprise-infrastructure marketing canvas built around a near-black ground (#000000) and a system of per-product accent colors —… |
| `hp` | 36 | a white-paper enterprise-consumer system anchored by HP Electric Blue (`#024ad8`) as the lone signal CTA, near-black ink (`#1a1a1a`) for… |
| `ibm` | 26 | An enterprise-marketing canvas faithful to Carbon Design System: white surfaces, charcoal type, IBM Blue (#0f62fe) as the single confident… |
| `intercom` | 23 | An editorial customer-service marketing canvas built around a soft cream-white ground, charcoal type set in Saans (Intercom's proprietary… |
| `kraken` | 4 |  |
| `lamborghini` | 20 |  |
| `linear.app` | 24 | A near-black product-focused marketing canvas built around #010102 (the deepest dark surface of any tool in this collection), light gray… |
| `lovable` | 17 |  |
| `mastercard` | 26 |  |
| `meta` | 37 | Meta's design system spans hardware commerce (Quest VR, Ray-Ban Meta AI glasses) and brand surfaces with a confident product-merchandising… |
| `minimax` | 37 | MiniMax presents itself as a premium AI infrastructure brand through a striking duality — bold black-pill CTAs and stark white canvas for… |
| `mintlify` | 43 | Mintlify presents documentation infrastructure with a dual-mode aesthetic — atmospheric sky-gradient marketing heroes (cloud illustration… |
| `miro` | 36 | Miro presents itself as the AI-powered visual workspace through a confident, almost playful brand voice — anchored by its signature canary… |
| `mistral.ai` | 35 | Mistral AI brands itself with a singular signature — atmospheric sunset gradients (mustard, orange, deep red) layered over photography of… |
| `mongodb` | 31 | MongoDB carries a strong dual-mode visual identity — dark deep-teal hero bands with bright MongoDB green ({colors.brand-green}) CTAs paired… |
| `nike` | 36 | / |
| `nintendo-2001` | 38 | An analysis of Nintendo.com's 2001 design language — a brushed-periwinkle "console chrome" interface where every panel is a beveled metal… |
| `notion` | 35 | Notion presents itself as the all-in-one workspace through a confident, illustration-rich brand voice — anchored by a deep navy hero band… |
| `nvidia` | 35 | / |
| `ollama` | 32 | / |
| `opencode.ai` | 32 | / |
| `pinterest` | 36 | / |
| `playstation` | 39 | / |
| `posthog` | 40 | / |
| `raycast` | 40 | / |
| `renault` | 29 | / |
| `replicate` | 31 | / |
| `resend` | 31 | / |
| `revolut` | 31 | / |
| `runwayml` | 14 |  |
| `sanity` | 21 |  |
| `sentry` | 35 | a developer-tools brand built on a deep purple-violet midnight canvas, electric lime accents, and a slightly subversive illustrated… |
| `shopify` | 26 | a cinematic commerce platform that runs two parallel design tracks. The marketing-hero and product-narrative pages live on near-black… |
| `slack` | 24 | a workplace messaging brand built on a deep aubergine primary, with cream-lavender hero gradients, blue inline links, and pill CTAs. The… |
| `spacex` | 19 | a mission-oriented aerospace brand built on pure black canvas, full-bleed photographic and video heroes of rockets and Mars landscapes, and… |
| `spotify` | 12 |  |
| `starbucks` | 37 |  |
| `stripe` | 24 | a financial-infrastructure brand built on a deep navy ink, an electric indigo primary, and a recurring atmospheric gradient mesh that… |
| `supabase` | 21 | an open-source database platform built on a clean white-and-near-black system with a single signature emerald-green CTA, a custom humanist… |
| `superhuman` | 21 | a fast-email productivity brand split between an editorial dark hero (deep indigo navy with violet-sky atmospheric backdrop and a portrait… |
| `tesla` | 22 |  |
| `theverge` | 28 |  |
| `together.ai` | 38 | an AI infrastructure platform whose surface alternates between near-black hero bands (with a three-color orange-magenta-periwinkle gradient… |
| `uber` | 34 | a transportation-and-delivery super-app brand whose web surface is a black-and-white duet, framed by a custom geometric display sans,… |
| `vercel` | 41 | a developer-platform brand whose surface is a stark black-and-ink duet on near-white canvas, broken at hero scale by a multi-color mesh… |
| `vodafone` | 27 | a telecom super-brand whose web surface alternates between editorial photography hero bands with massive uppercase display headlines and… |
| `voltagent` | 25 | a developer-focused AI agent engineering platform whose surface is an unrelenting near-black canvas broken only by a single electric-green… |
| `warp` | 24 | an agentic terminal-and-development-environment brand whose surface is a warm near-charcoal canvas (a tint warmer than pure black), broken… |
| `webflow` | 27 | a visual web development platform whose surface contrasts a deep near-black `#080808` primary against a generous white canvas, broken by a… |
| `wired` | 23 | a flagship technology-magazine brand whose surface is a strict editorial duet of stark black wordmark on white canvas, anchored by a tall… |
| `wise` | 24 | a global money-transfer brand whose surface combines an unusually heavy near-black display sans (weight 900 at 64–126 px) with a vivid… |
| `x.ai` | 21 | Elon Musk's frontier-AI company whose web surface is a strict near-black canvas broken only by white pill outlines, occasional warm sunset… |
| `zapier` | 22 | a workflow-automation platform whose surface combines warm-cream neutrals (`#fffefb` canvas, `#f8f4f0` soft cream) with deep coffee ink… |
