# Native Authorability

> Hard production rule for Instapage work (SKILL.md hard rule 1). Owner: DesignChamp. Enforced by the build-sheet lint, QA and the publish gate (§7).

## 1. The rule

A production landing page built for Instapage stays natively authorable inside Instapage by a competent non-developer. CreativeEngine and the client's own staff work on the same page, in the same editor, with the same tools.

Ordinary marketing content uses native authoring primitives. Infrastructure and approved, narrowly scoped integration exceptions are recorded separately. A client CRM embed may collect leads externally; its fields and behavior are edited in the CRM or provider code, not Instapage. It does not justify rebuilding surrounding content in HTML.

## 2. Acceptance test

> After CreativeEngine produces the page, can a competent client-side marketer open it in Instapage and safely edit ordinary content, imagery and reusable sections without Claude, custom development or knowledge of CreativeEngine's code?

If the answer is no, the page is not finished, unless an approved exception (§6) covers exactly the part that fails.

QA runs it as the **editor test** (NA-08 in `qa.md`). On a duplicate of the draft, using only the editor's own controls:

1. change a headline and a paragraph;
2. change a button's label and link;
3. swap an image and its alt text;
4. duplicate, reorder and delete a section, and rearrange it on mobile;
5. change a field label in the form;
6. confirm desktop and mobile still render correctly;
7. retain the unpublished duplicate, page ID, preview URL and saved export as evidence; do not delete predecessor or test pages as routine validation;
8. apply a subsequent non-conflicting automated change using `preservation.md`, then repeat the render and editing checks. Record a conflicting change as blocked, not overwritten.

Each step either works through native controls, or it is a finding.

## 3. Build with, in this order

1. **Fluid Grid Blocks** and native responsive layout: containers, flow, stacking order, the mobile layout.
2. **Native elements and widgets**: headline, paragraph, button, image, video, line, timer, accordion, carousel; box and circle in Canvas blocks.
3. **Native forms** from the Form Library.
4. **Saved blocks (My Blocks)** for patterns that repeat.
5. **Global Blocks** only where one synchronized source of truth is deliberately required (`reusable-blocks.md`).
6. **Native page and workspace settings**: fonts, styles, sticky bar, popups, search and social, integrations, conversion goals, the cookie bar.

Canvas blocks are native too. Prefer Fluid Grid Blocks for sections that have to reflow; use a Canvas block where the spec needs free positioning or shapes, and specify its mobile arrangement (`responsive.md`).

Client differentiation comes from each client's design system applied to these native structures (`figma-kit.md` §1), never from custom code, embedded sites, proprietary renderers or non-authorable components. Before proposing an exception, DesignChamp pushes the native range: grid spans and custom grids, container backgrounds, borders and radius, the three font roles at any size and weight, images and background images, device-specific settings, visibility per device, Canvas blocks.

## 4. Prohibited for user-facing components

- HTML widgets that recreate something Instapage has natively: text, buttons, images, YouTube, Vimeo or Wistia video, forms, accordions, carousels, timers, sticky bars, popups.
- Page, block or workspace CSS that positions, sizes, lays out, hides or restyles components that can be authored natively. That includes mobile-only CSS media queries.
- JavaScript that creates, moves, hides or changes visible UI or content.
- React, Vue or any framework component, and iframes standing in for native functionality.
- Opaque third-party widgets for ordinary landing-page content: FAQs, testimonials, pricing tables, galleries, reviews.
- Code whose purpose is pixel fidelity with Figma.
- Text set inside an image to get around a native limit. It cannot be edited and it is not accessible. Lettering that *is* the approved image is an image asset: it gets alt text, and DesignChamp and WordSmither decide whether the words also appear as native text.
- Unsupported JSON structure presented as production-ready. Native generators/adapters based on saved exports are eligible only after the validation and preservation gates in `preservation.md`; keep source, fixtures and outputs in the project.
- Anything that makes a routine edit depend on CreativeEngine, Claude or a developer.

Instapage's own documentation gives the practical reasons for several of these: embedded code sits on top of the page structure, is left out of native conversion goals, lead collection, notifications and integrations, and is not supported by Instapage's team (`platform.md` §2, §7, §10).

## 5. Grey zones, ruled

| Feature | Ruling |
|---|---|
| Inline Style Editor ("Edit CSS" on an element) | **Component exception.** Only for one visual property the native controls lack, when DesignChamp shows it carries the idea and CreativeDirector approves. Never for layout, position, visibility or mobile-only behavior. It must pass the **reset test**: after "Reset to Default" the element still reads and works, it just looks plainer |
| Device-specific settings (size, padding, line height per device) | Native. Allowed |
| An element duplicated for desktop-only and mobile-only visibility | Native. Allowed when the spec needs different arrangement per device. The two carry the same approved text unless WordSmither approved per-device copy |
| Canvas block | Native. Allowed |
| Workspace Scripts that make UI (FAQ widgets, sticky headers, banners other than consent) | Prohibited. Use Accordion, Sticky Bar or native elements |
| A consent-management platform's banner | Infrastructure exception, only when the native cookie bar cannot meet the requirement (several processing purposes, a CMP the client requires) |
| A timer that resets per visitor | Component exception (HTML). Otherwise a fixed-date native timer, or no timer |
| Video from another host, or a looping video | Component exception (HTML embed) |
| Client CRM embed (for example Slate) | **INTEGRATION exception.** Record the client requirement, native integration/webhook alternatives, exact editing and maintenance owners, attribution and success tracking, responsive and accessibility tests. Embedded fields are externally editable, not native |
| Form conditional logic | Component exception. First ask BriefMachine and WordSmither whether a multistep or simpler native form meets the ask |
| Prompt to Page, AI Content Generator | Not used on CreativeEngine work (SKILL.md hard rule 4). The structure they make is native; their copy, colors, fonts and images are creative decisions |

A component exception is rare. It needs a recorded constraint, DesignChamp's case that no native option carries the idea, CreativeDirector's approval, and a note to the client on how to maintain it.

## 6. Infrastructure and the exception register

Code for analytics, consent, tag management, conversion pixels, an approved third-party service, or an integration with no native route may be used, in this order:

1. A **native integration**: Marketing Tags & Pixels (Google Ads, Google Analytics / GA4, Meta Pixel, Google Tag Manager), Form Integrations, Lead Notifications.
2. **Native page settings**: the page's Scripts & Privacy section, behind the cookie bar where consent applies.
3. **Workspace Scripts**, when the same script has to run on many pages (plan-dependent; Owner or Manager).
4. The **builder's JavaScript or HTML/CSS panel**, as a last resort, for example a script that must reference an element ID, wrapped for consent where needed.

Infrastructure code never owns editable marketing content. Visible provider UI required for an integration is an INTEGRATION exception; other approved non-native UI is a COMPONENT exception. Neither may silently replace ordinary native content.

Every exception is recorded in the project's `work/production/<packet>_instapage-exceptions.md`:

```
EXC-<nn>
CLASS:              INFRASTRUCTURE | COMPONENT | INTEGRATION
WHAT:               <code or setting, and where it lives: element ID, page panel, Scripts & Privacy, workspace script>
WHY NOT NATIVE:     <the platform limit, citing platform.md>
NATIVE OPTIONS:     <what was considered, and why each fails the approved requirement>
CONSENT:            <cookie bar / wrapper / not applicable>
OWNS UI OR COPY?:   <NO, or YES for COMPONENT / INTEGRATION; name the exact boundary>
DECIDED BY:         <DesignChamp for a component · the brief or client requirement for infrastructure>
APPROVED BY:        <creative-engine-director for a component · user/client for infrastructure or integration; material creative effects also reviewed by creative-engine-director> · <date> · <evidence>
EDITED BY / WHERE:  <named owner and native editor / CRM / provider route>
MAINTAINED BY:      <named owner and support responsibility>
TRACKING METHOD:    <success event, receiving system, attribution method; never assume native form goals>
VALIDATION PLAN:    <draft render, submission, redirect, consent, attribution, duplicate prevention, editor and round-trip tests>
VALIDATION RESULT:  <evidence links or NOT_RUN with reason>
RESET TEST:         <result, for inline CSS>
REMOVE WHEN:        <condition, such as a native feature arriving>
STATUS:             PROPOSED | APPROVED | REJECTED | REMOVED
```

A proposed exception is not approved until the register says so. The build sheet cites the EXC ID on every element or code entry it covers.

## 7. Where the rule is enforced

| Stage | Check | Consequence |
|---|---|---|
| DEVELOP | DesignChamp maps serious directions to the kit (`figma-kit.md` §3) | Warnings only; nothing is killed for being hard to build |
| JUDGE | The spec is buildable natively, or each gap has a proposed exception | CreativeDirector sees the gaps before approving production |
| Build sheet | `ip_check.py plan`: primitives outside the verified vocabulary, HTML or code without an approved exception, code that owns UI, shapes in Fluid Grid Blocks, accordions with links, Global Blocks without a reason, text that does not match the approved copy | A FAIL stops the build |
| QA | NA-01 to NA-09 against the actual page (`qa.md`) | A FAIL or an unrun blocking check stops publishing |
| Publish | The gate refuses while a blocking issue is open | Nothing goes live |
