# Forms, integrations, conversion goals and tracking

## 1. Native forms by default

Every form is a native Instapage form from the Form Library, unless a requirement cannot be met natively and an exception is approved (`native-authorability.md` §5). An embedded third-party or hand-coded form is never used for visual fidelity: it sits outside the page structure, is not counted by native conversion goals, and does not reach lead notifications or native integrations (`platform.md` §2, §7).

## 2. What the form must preserve

Each item comes from its owner. Production enters it; it does not decide it.

| Item | Source | Rule |
|---|---|---|
| Fields: which, in what order | Work packet (BriefMachine) | Exactly the approved set and order. No extra "nice to have" fields |
| Label and placeholder text | Approved copy (WordSmither) | Exact |
| Required or optional | Packet | Exact. The asterisk setting follows the spec |
| Field types and validation | Packet; spec | Predefined field where one matches (email, phone, country); validation as approved |
| Hidden fields and their values (for example UTM or campaign IDs) | Packet or the client's tracking plan | Named and valued exactly; OPEN if not supplied |
| Consent checkbox wording and links | Mandatories and the approved legal source | Exact wording; links with https |
| Submit button text | Packet CTA wording, as set in the approved copy | Exact. Aria-label written by WordSmither |
| After submitting | Packet destination | A redirect (Instapage page or outside URL) **or** a file download, never both; URL parameters passed on only if required |
| Thank-you message | Approved copy | Exact, or removed if the spec says so |
| Integration (CRM or list) | Packet or the client | The exact destination list; account connected by the client or a Manager |
| Lead notification recipients | The client | Never guessed |
| Conversion goal | Packet measured event (§4) | Configured to match |
| Tracking | Packet measurement requirements | Through the ladder in §5 |

**A mismatch is reported, never resolved.** If the packet asks for a field Instapage cannot provide, or the spec shows a field the packet does not list, write a constraint report to BriefMachine (the ask) or DesignChamp (the spec). Production does not add, drop or reorder fields to make things line up.

Styling limits to design within: the form uses the page's paragraph font, and its field text size cannot be changed except, in limited release, the label size per device (`platform.md` §6, §15). DesignChamp specifies forms within these limits.

## 3. Testing forms without polluting the client's data

- Form submissions cannot be tested in preview. They need a published URL: a staging publish to pagedemo, with the user's OK (`publishing.md` §3).
- A test submission reaches every connected integration, lead notification and automated email. Before testing, agree with the client which test identity to use (for example a dedicated test email address) and whether the CRM should receive it.
- Never use a real person's details. Never unmask submissions to check a test; the masked record and the integration's receipt are enough.
- Deleting submissions through the API is irreversible and is not part of this skill.

## 4. Conversion goals must match the measured event

The packet's MEASURABLE SUCCESS EVENT and MEASUREMENT DEFINITION (`brief-normalization.md` §8) decide the goal. Instapage counts only native links and native forms, and reports one total across all goals configured on a page (`platform.md` §7).

| Measured event in the packet | Conversion goal | Watch for |
|---|---|---|
| Completed form submission | Form submissions only | Link-click goals on the same page would inflate the total with clicks |
| Click to an off-page destination | Link clicks on the specific native links named | Every other tracked link adds to the same total |
| An action completed on another site (purchase, application, booking) | External page visit on the confirmation URL, or the destination's own tracking | On-page goals switch off when external is on; it needs the external tracking set up on that page |
| OPEN in the packet | None configured as "the" success metric | Report it back to BriefMachine; do not choose one |

An intent is not a completion: a CTA click is not a submission, and a submission is not a qualified lead or an enrollment (`brief-normalization.md` §8). MEASURE reports what Instapage counted, under the goal as configured, and says so.

## 5. Tracking and infrastructure ladder

Use the first rung that meets the requirement:

1. **Native integrations** in the page's slideout: Marketing Tags & Pixels (Google Ads, Google Analytics / GA4, Meta Pixel, Google Tag Manager), Form Integrations, Lead Notifications.
2. **Scripts & Privacy** for page-level tracking scripts: applies to every variation of the page, and the native cookie bar blocks it until consent.
3. **Workspace Scripts** for a script many pages need (plan-dependent; Owner or Manager).
4. **Builder JavaScript panel**, last, for a script that must reference an element ID, wrapped in Instapage's documented consent function when consent applies.

Each rung from 2 down is an infrastructure exception with an EXC entry (`native-authorability.md` §6). Tracking code never changes what the visitor sees.

## 6. Consent

- The native cookie bar suits a page that collects data for one processing purpose. With several purposes, add separate consent (for example a consent checkbox in the form, with approved wording).
- A consent-management platform the client requires is an infrastructure exception (Workspace Scripts, usually). Google Consent Mode has no native integration and is an infrastructure exception too.
- Legal adequacy is not production's judgment. It comes from the client's approved legal or compliance source; if none is supplied, it is an OPEN question for the user.

## 7. Search and social settings

Page title, meta description and social share image are copy and imagery: they come from WordSmither and DesignChamp and are entered exactly. "Hide page from search engines" stays on (Instapage's default) unless the packet or the client says the page should be indexed.
