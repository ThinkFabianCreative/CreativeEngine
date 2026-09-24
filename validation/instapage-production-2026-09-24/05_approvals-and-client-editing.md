# Approvals and client editing · LP1 (SYNTHETIC)

## What needs a human decision, and whose

| Decision | Who | Why it is theirs | Status |
|---|---|---|---|
| Spec approved for production | creative-engine-director | Creative approval of the selected idea's execution | Synthetic approval, validation only |
| CON-01 rotated stamp → unrotated | DesignChamp | A craft choice inside the approved idea; not material | Resolved (synthetic) |
| CON-02 nested bordered stamp → its own container | DesignChamp | Restructures the hero grid; the stamp idea survives | Resolved (synthetic) |
| CON-03 per-device headline size | DesignChamp; creative-engine-director only if the fix changes the hierarchy materially | Depends on a limited-release setting | Open until INSPECT |
| C1 "more than 900 tools" | Client, via BriefMachine; if unverifiable, WordSmither rewrites and creative-engine-director approves | The proof line carries the page's argument, so replacing it is material | Open; blocks publishing |
| IMG-01 production photo | DesignChamp directs, client supplies rights and approval | Only PRODUCTION-APPROVED assets go live | Open; blocks publishing |
| Q1 list, Q2 recipients, Q3 GA4 property | Client, via BriefMachine | Measurement and data routing are the client's | Open |
| Making B05 a Global Block | Client (legal line owner) | Editing it later changes every Fernwick page | Approved (synthetic) |
| Staging publish for functional QA | User | A public URL, even on pagedemo | Not requested |
| Final creative approval of the built page version | creative-engine-director | Exact page version, after QA | Not yet due |
| Publish go-ahead naming page, URL, domain and time | User or client | Publishing is theirs | Not yet due |
| Pressing Publish | An Instapage Manager (default) | Editors cannot push live; the build key is an Editor's | Not yet due |

## What the client can edit afterwards, without us

Handoff note draft (`references/publishing.md` §6):

- **Text:** every headline and paragraph in the editor: double-click and type. The approved words are the starting point, and the client owns later changes.
- **Buttons:** label and link in the button's link setup.
- **Images:** swap the image and edit its alt text on the placed image (library alt edits only affect future inserts).
- **Sections:** duplicate, reorder, hide on mobile, or delete blocks; change mobile stacking in the block's mobile layout.
- **The form:** field labels, order and required state in the Form Library (Assets > Forms); the thank-you message in the form's submission settings.
- **My Blocks:** `Fernwick / Hero / Split · v01` and `Fernwick / Form / Card signup · v01` can be inserted on other Fernwick pages and changed there freely; edits never spread.
- **Global Block:** `GLOBAL · Fernwick / Footer / Legal · v01`. **Editing it changes every Fernwick page that uses it, live pages included.** Only the communications office changes it, and a Manager applies the change after checking the list of affected pages.
- **Settings:** fonts, colors, search and social, cookie bar, conversion goal (Form submissions), integrations. Ask before changing the conversion goal or integrations, because measurement depends on them.
- **Rollback:** Version History in page settings.
- **Exceptions:** none. Nothing on the page needs a developer.
