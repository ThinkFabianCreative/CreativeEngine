```
INSTAPAGE QA · SYNTHETIC Fernwick Tool Library · card-drive · LP1 · PLAN · 2026-09-24
PAGE:       not built (Instapage MCP not connected; no workspace)
COMPARED:   packet 01_work-packet_SYNTHETIC.md · copy 02_approved-copy_SYNTHETIC.md v01 ·
            spec Figma node 18-39 v01 · build sheet LP1_instapage-build-sheet_v01.json
RESULT:     14 PASS · 2 FAIL · 0 WARNING · 30 NOT RUN · publish allowed: NO
VALIDATED:  ip_check.py qa → "RESULT FILE: valid"

BLOCKING
- GV-01 Asset status: IMG-01 is a PLACEHOLDER. Fine in a draft; publishing waits for the
  production photo with provenance, rights and approver → DesignChamp and the client
- GV-02 Claims: PROOF-H uses C1 ("more than 900 tools"), SOURCE-STATED. Publishing waits
  until C1 is VERIFIED, or WordSmither writes a replacement within the ledger and
  creative-engine-director approves it → BriefMachine
- 29 blocking checks NOT RUN (below)

WARNINGS
- none at QA level. The plan lint's three warnings map to GV-01, GV-02 and CON-03

NOT RUN
- CF-03 to CF-09, NA-01, NA-08 to NA-10, FN-01, FN-02, FN-04, FN-07 to FN-09, RS-01 to RS-10,
  GV-03, GV-04: no Instapage page exists, because the Instapage MCP is not connected.
  They run at DRAFT once the page is built
- FN-05 (test submission reaching the integration): needs a published test environment,
  the agreed test identity, and answers to Q1 (list) and Q2 (recipients). Not run, and no
  page will be published just to make it pass

NEEDS A DECISION
- CON-03 per-device headline size → DesignChamp, after INSPECT shows whether the workspace
  has the limited-release setting (not material)
- Q1 email list, Q2 notification recipients, Q3 GA4 property ID → the client, via BriefMachine
```
