# Publishing

Publishing puts client work in front of the public under the client's name. It is always a separate, explicit act, approved per action. A successful build or a passing QA does not publish anything.

## 1. What counts as publishing

Any action that changes what the public can see:

- publishing a page, or publishing it to pagedemo for testing;
- unpublishing a page, or scheduling either;
- changing a live page's URL or publishing method;
- pressing **Update** in the builder on a published page;
- applying changes to a Global Block or global popup used on any live page;
- adding, changing or removing Workspace Scripts, or scripts and integrations on a live page;
- starting, stopping or changing the traffic of an experiment;
- publishing or unpublishing a collection page.

## 2. The gate

Every publish action needs all four, recorded:

| Gate | Who | Evidence |
|---|---|---|
| **G1 Creative approval** | `creative-engine-director`, for the exact page version | Verdict and approval note in `work/reviews/`, naming page ID and version |
| **G2 QA clear** | This skill | The latest QA JSON validates, with no blocking FAIL or NOT RUN (`qa.md`) |
| **G3 Go-ahead** | The user, and the client where the user says the client decides | A message naming the page, the URL and domain, and when. One go-ahead covers one action |
| **G4 Authority** | A Manager or Owner in Instapage, or the PUBLISH profile (`mcp-and-api.md` §4) | Who pressed the button, when |

Claude asks for G3 in chat, in this form, and waits for a clear yes:

```
Ready to publish: <page name> (<page ID>, version <v>) to <URL> on <domain>, <now / scheduled time>.
QA: <path to QA JSON> · no blocking issues. Creative approval: <reviewer, date>.
It will be public at that URL. Search-engine indexing: <off (default) / on per <source>>.
Publish?
```

## 3. Staging for QA

Forms, page scripts, sticky bars and some embeds only run on a published page, so functional QA needs a staging publish, usually to a pagedemo address. It is a lighter case but still a publish action:

- The user's OK is needed (G3), naming the pagedemo URL. G1 is not needed for staging; G2 applies to the checks that can run on a draft.
- Pagedemo pages keep "Hide page from search engines" on and are not used for ad traffic (Instapage limits them to 30 requests a minute per IP).
- Test submissions follow `forms-and-tracking.md` §3.
- Unpublish the staging page, or move it to the production URL, as the next approved step. A forgotten staging page is still a public page.

## 4. Doing it

1. Re-run `ip_check.py qa` on the latest QA JSON; it must pass.
2. Present the G3 message and wait.
3. The executor publishes: a Manager in the UI (default), or Claude with the PUBLISH profile switched on for this action only.
4. Smoke-test the live URL at once: page loads at the right URL and domain; desktop and mobile; primary CTA and links; one agreed test submission if the client wants it; tags fire; the cookie bar behaves; noindex matches the brief.
5. Switch the PUBLISH profile off again, if it was used.
6. Write the publish record.

## 5. Publish record

`projects/<client>/<project>/outputs/delivered/YYYY-MM-DD/<packet>_instapage-publish-record.md`, following the approval-record fields in `projects/README.md`:

```
ASSET:          Instapage page <name> · <page ID> · version <v> (<Version History timestamp>)
URL:            <live URL> · domain <domain> · method <custom domain / WordPress / Drupal / pagedemo>
DELIVERED TO:   public web, for <client>
APPROVED BY:    creative: <creative-engine-director review path, date> · go-ahead: <who, date, message or evidence>
EXECUTED BY:    <Manager name, or Claude with the PUBLISH profile> · <date, time>
QA:             <path to QA JSON and report>
EXCEPTIONS:     <EXC IDs live on this page, or none>
GLOBAL BLOCKS:  <names, and every page they touch>
CONDITIONS:     <schedule, expiry, markets, caveats>
SMOKE TEST:     <result>
```

A delivered record is never edited afterwards. A later change is a new record on its own date.

## 6. Client handoff note

Written with the first publish of a page, in the same folder:

- what can be edited freely in the editor (text, images and alt text, buttons and links, sections, the form in the Form Library);
- which blocks are **My Blocks** (safe to edit on this page) and which are **Global** (an edit changes every listed page);
- any exception on the page, what it does, and who maintains it;
- where Version History is, for rolling back a page;
- who to ask before changing integrations, conversion goals or scripts.

## 7. Rolling back

| Situation | Native way back | Class |
|---|---|---|
| A bad edit on a draft | Version History | Build |
| A bad edit already live | Restore the previous version in Version History, then Update | Publish |
| The wrong page is live | Unpublish, or change the URL back | Publish |
| A Global Block change went wrong | Edit the block back and apply to all pages | Publish |

Deleted collection pages and deleted submissions cannot be recovered through the API, which is why this skill never deletes.
