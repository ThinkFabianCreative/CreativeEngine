#!/usr/bin/env python3
"""Checks for CreativeEngine's instapage-production skill.

  ip_check.py plan <build-sheet.json>     lint a build sheet before anything is built
  ip_check.py qa <qa-result.json>         validate a QA result and recompute the publish gate
  ip_check.py skeleton [--stage STAGE]    print a QA result skeleton with every catalog check

Standard library only. Reads local JSON files, writes to stdout, makes no
network calls and never touches credentials. Exit code 0 means no FAIL
(plan) or a valid result (qa); 1 means the file failed; 2 means bad usage.
"""

import argparse
import json
import re
import sys

# ---------------------------------------------------------------------------
# Verified Instapage vocabulary (references/platform.md, verified 2026-09-24)
# ---------------------------------------------------------------------------

PRIMITIVES = {
    "headline", "paragraph", "button", "image", "video", "form",
    "box", "circle", "line", "timer", "accordion", "carousel", "html",
}
TEXT_PRIMITIVES = {"headline", "paragraph", "button"}
SHAPES = {"box", "circle"}                      # not allowed in Fluid Grid Blocks
BLOCK_TYPES = {"fluid_grid", "canvas"}
REUSE = {"page", "my_block", "global_block"}
VISIBILITY = {"both", "desktop", "mobile"}
LINK_TYPES = {"outside_url", "landing_page", "popup", "on_page", "file_download"}
VIDEO_HOSTS = {"youtube", "vimeo", "wistia"}
FONT_ROLES = {"headline", "paragraph", "button"}
MAX_BRAND_COLORS = 14
ASSET_STATUSES = {"EXPLORATION", "PROTOTYPE", "PLACEHOLDER", "PRODUCTION-APPROVED"}
CODE_LOCATIONS = {
    "scripts_privacy", "workspace_scripts", "page_js", "page_css",
    "inline_css", "global_block_settings",
}
AFTER_SUBMIT = {"thank_you", "redirect", "download"}
SUCCESS_EVENTS = {"form_submission", "link_click", "external_page", "OPEN"}
GOALS = {"form_submissions", "link_clicks", "external_page"}
# Claim-ledger statuses other than VERIFIED (brief-normalization.md §5)
CLAIM_NOTES = {
    "SOURCE-STATED": "confirm before publishing; blocks publishing until VERIFIED",
    "PENDING APPROVAL": "keep out of external work; blocks publishing until approved",
    "CONDITIONAL": "use only with its stated condition, visible on the page",
    "OUTCOME CLAIM": "qualitative and hedged only; never quantified or guaranteed",
}

# ---------------------------------------------------------------------------
# QA catalog (references/qa.md §3). Every check is blocking except RS-07.
# ---------------------------------------------------------------------------

QA_CATALOG = {
    **{f"CF-{n:02d}": True for n in range(1, 10)},
    **{f"NA-{n:02d}": True for n in range(1, 11)},
    **{f"FN-{n:02d}": True for n in range(1, 10)},
    **{f"RS-{n:02d}": True for n in range(1, 11)},
    **{f"GV-{n:02d}": True for n in range(1, 9)},
}
QA_CATALOG["RS-07"] = False
QA_STATUSES = {"PASS", "FAIL", "WARNING", "NOT_RUN"}
QA_STAGES = {"PLAN", "DRAFT", "STAGING", "LIVE"}
QA_OWNERS = {"DC", "WS", "BM", "CD", "PR", "US"}


class Findings:
    def __init__(self):
        self.items = []

    def fail(self, rule, where, message):
        self.items.append(("FAIL", rule, where, message))

    def warn(self, rule, where, message):
        self.items.append(("WARNING", rule, where, message))

    def count(self, level):
        return sum(1 for item in self.items if item[0] == level)


def _nonempty(value):
    return isinstance(value, str) and value.strip() != ""


# ---------------------------------------------------------------------------
# plan
# ---------------------------------------------------------------------------

def lint_plan(sheet):
    f = Findings()
    if sheet.get("format") != "instapage-build-sheet/1":
        f.fail("P01", "format", 'expected "instapage-build-sheet/1"')
    meta = sheet.get("meta", {})
    for key in ("client", "project", "packet", "version"):
        if not _nonempty(meta.get(key)):
            f.fail("P01", f"meta.{key}", "missing")
    for key in ("spec", "copy_doc"):
        if not isinstance(meta.get(key), dict) or not _nonempty(meta[key].get("version")):
            f.fail("P01", f"meta.{key}", "missing, or no version named")

    copy = sheet.get("copy", {})
    if not isinstance(copy, dict) or not copy:
        f.fail("P11", "copy", "no approved copy entries")
        copy = {}

    exceptions = {e.get("id"): e for e in sheet.get("exceptions", [])}
    used_exceptions = set()

    def approved_exception(ref, where, wanted_class=None):
        if not _nonempty(ref):
            f.fail("P05", where, "needs an approved exception (EXC ID)")
            return
        used_exceptions.add(ref)
        exc = exceptions.get(ref)
        if exc is None:
            f.fail("P05", where, f"{ref} is not in the exception register")
        elif exc.get("status") != "APPROVED":
            f.fail("P05", where, f"{ref} is {exc.get('status', 'unset')}, not APPROVED")
        elif not _nonempty(exc.get("approved_by")):
            f.fail("P05", where, f"{ref} has no approver")
        elif wanted_class and exc.get("class") != wanted_class:
            f.fail("P05", where, f"{ref} must be a {wanted_class} exception")

    def check_text(where, copy_id, text):
        if not _nonempty(copy_id):
            f.fail("P11", where, "no approved copy ID")
            return
        if copy_id not in copy:
            f.fail("P11", where, f"copy ID {copy_id} is not in the approved copy")
            return
        if text != copy[copy_id]:
            f.fail("P11", where, f"text differs from approved copy {copy_id}")

    used_text = []          # (copy_id, text) pairs actually placed

    claims = {c.get("id"): c for c in sheet.get("claims", [])}

    def check_claims(where, refs):
        for ref in refs or []:
            claim = claims.get(ref)
            if claim is None:
                f.fail("P25", where, f"claim {ref} is not in the claim ledger")
                continue
            status = claim.get("status")
            if status == "VERIFIED":
                continue
            if status not in CLAIM_NOTES:
                f.fail("P25", where, f"claim {ref} has unknown status {status!r}")
            else:
                f.warn("P25", where, f"claim {ref} is {status}: {CLAIM_NOTES[status]}")

    # styles
    styles = sheet.get("styles", {})
    colors = styles.get("brand_colors", [])
    if len(colors) > MAX_BRAND_COLORS:
        f.fail("P09", "styles.brand_colors", f"{len(colors)} colors; Styles holds {MAX_BRAND_COLORS}")
    for c in colors:
        if not re.fullmatch(r"#[0-9A-Fa-f]{6}", str(c)):
            f.warn("P09", "styles.brand_colors", f"{c} is not #RRGGBB")
    for role in styles.get("fonts", {}):
        if role not in FONT_ROLES:
            f.fail("P09", f"styles.fonts.{role}", "Instapage pages have headline, paragraph and button fonts only")

    # assets
    assets = {a.get("id"): a for a in sheet.get("assets", [])}
    for aid, a in assets.items():
        where = f"assets.{aid}"
        status = a.get("status")
        if status not in ASSET_STATUSES:
            f.fail("P14", where, f"status {status!r} unknown")
        if a.get("generated"):
            f.fail("P14", where, "generated media never enters an Instapage page")
        elif status in ("EXPLORATION", "PROTOTYPE"):
            f.fail("P14", where, f"{status} assets never enter an Instapage page")
        elif status == "PLACEHOLDER":
            f.warn("P14", where, "placeholder: allowed in drafts, blocks publishing")
        elif status == "PRODUCTION-APPROVED":
            for key in ("provenance", "rights", "approved_by"):
                if not _nonempty(a.get(key)):
                    f.fail("P14", where, f"PRODUCTION-APPROVED needs {key}")

    # blocks
    blocks = sheet.get("blocks", [])
    block_ids = {b.get("id") for b in blocks}
    h1_count = 0
    levels = []
    globals_seen = set()
    for b in blocks:
        bid = b.get("id", "?")
        btype = b.get("type")
        if btype not in BLOCK_TYPES:
            f.fail("P03", bid, f"block type {btype!r} is not fluid_grid or canvas")
        reuse = b.get("reuse", "page")
        if reuse not in REUSE:
            f.fail("P08", bid, f"reuse {reuse!r} unknown")
        if reuse == "global_block":
            g = b.get("global", {})
            for key in ("name", "reason", "owner", "approved_by"):
                if not _nonempty(g.get(key)):
                    f.fail("P08", bid, f"Global Block needs {key}")
            name = g.get("name")
            if name in globals_seen:
                f.fail("P08", bid, f"Global Block {name!r} placed twice; only the first loads")
            globals_seen.add(name)

        containers = {c.get("id"): c for c in b.get("containers", [])}
        if btype == "fluid_grid":
            if not containers:
                f.fail("P17", bid, "Fluid Grid Block without containers")
            orders = [c.get("mobile_order") for c in containers.values()]
            if any(not isinstance(o, int) or o < 1 for o in orders):
                f.fail("P17", bid, "every container needs a mobile_order (1, 2, ...)")
            elif len(set(orders)) != len(orders):
                f.fail("P17", bid, "mobile_order values repeat")

        for e in b.get("elements", []):
            eid = f"{bid}.{e.get('id', '?')}"
            prim = e.get("primitive")
            if prim not in PRIMITIVES:
                f.fail("P02", eid, f"primitive {prim!r} is not in the verified vocabulary")
                continue
            if btype == "fluid_grid":
                if prim in SHAPES:
                    f.fail("P04", eid, "shapes cannot go in a Fluid Grid Block; use container background, border and radius, or a Canvas block")
                if prim == "carousel":
                    f.warn("P23", eid, "carousel inside a Fluid Grid Block is unverified; confirm in the editor")
                if e.get("container") not in containers:
                    f.fail("P17", eid, f"container {e.get('container')!r} not in {bid}")
            vis = e.get("visibility", "both")
            if vis not in VISIBILITY:
                f.fail("P18", eid, f"visibility {vis!r} unknown")

            if prim in TEXT_PRIMITIVES:
                check_text(eid, e.get("copy"), e.get("text"))
                used_text.append((e.get("copy"), e.get("text")))
            check_claims(eid, e.get("claims"))
            if prim == "headline":
                level = e.get("level")
                if level not in (1, 2, 3, 4, 5, 6):
                    f.fail("P10", eid, "headline level must be 1 to 6")
                else:
                    levels.append(level)
                    h1_count += level == 1
            if prim in ("button", "image") and "link" in e:
                link = e["link"]
                ltype = link.get("type")
                if ltype not in LINK_TYPES:
                    f.fail("P19", eid, f"link type {ltype!r} unknown")
                elif ltype == "on_page" and link.get("target") not in block_ids:
                    f.fail("P19", eid, f"on-page target {link.get('target')!r} is not a block")
                elif ltype == "outside_url" and not str(link.get("target", "")).startswith("https://"):
                    f.warn("P19", eid, "outside URL is not https")
            if prim == "image":
                a = assets.get(e.get("asset"))
                if a is None:
                    f.fail("P14", eid, f"asset {e.get('asset')!r} not in the asset list")
                elif not a.get("decorative"):
                    alt = a.get("alt_copy")
                    if not _nonempty(alt) or alt not in copy:
                        f.fail("P14", eid, "image needs approved alt text (alt_copy) or decorative: true")
                    else:
                        used_text.append((alt, copy[alt]))
            if prim == "video" and e.get("host") not in VIDEO_HOSTS:
                f.fail("P21", eid, "native video takes YouTube, Vimeo or Wistia; anything else is an HTML exception")
            if prim == "timer" and e.get("mode", "fixed_date") != "fixed_date":
                f.fail("P22", eid, "native timer counts to one fixed date; per-visitor timers need an approved exception")
            if prim == "accordion":
                for i, item in enumerate(e.get("items", [])):
                    iw = f"{eid}.items[{i}]"
                    if "link" in item or "image" in item:
                        f.fail("P07", iw, "accordion sections hold text only")
                    check_text(iw + ".title", item.get("title_copy"), item.get("title"))
                    check_text(iw + ".body", item.get("body_copy"), item.get("body"))
                    used_text.append((item.get("title_copy"), item.get("title")))
                    used_text.append((item.get("body_copy"), item.get("body")))
            if prim == "html":
                approved_exception(e.get("exception"), eid, "COMPONENT")

    if h1_count != 1:
        f.fail("P10", "headlines", f"{h1_count} h1 headlines; a page needs exactly one")
    previous = 0
    for level in levels:
        if level > previous + 1 and previous != 0:
            f.warn("P10", "headlines", f"heading level jumps from h{previous} to h{level}")
        previous = level

    # forms
    ask = sheet.get("ask", {})
    cta = ask.get("cta_wording")
    form_ids = set()
    for form in sheet.get("forms", []):
        fid = form.get("id", "?")
        form_ids.add(fid)
        packet_fields = form.get("packet_fields", [])
        fields = form.get("fields", [])
        if len(fields) != len(packet_fields):
            f.fail("P15", fid, f"{len(fields)} fields planned, packet asks for {len(packet_fields)}")
        for i, (planned, asked) in enumerate(zip(fields, packet_fields)):
            fw = f"{fid}.fields[{i}]"
            for key in ("label", "type", "required"):
                if planned.get(key) != asked.get(key):
                    f.fail("P15", fw, f"{key} {planned.get(key)!r} differs from the packet's {asked.get(key)!r}")
            check_text(fw + ".label", planned.get("label_copy"), planned.get("label"))
            used_text.append((planned.get("label_copy"), planned.get("label")))
        submit = form.get("submit", {})
        check_text(f"{fid}.submit", submit.get("copy"), submit.get("text"))
        used_text.append((submit.get("copy"), submit.get("text")))
        after = form.get("after_submit", {})
        atype = after.get("type")
        if atype not in AFTER_SUBMIT:
            f.fail("P15", fid, "after_submit must be thank_you, redirect or download")
        elif atype == "redirect" and not _nonempty(after.get("target")):
            f.fail("P15", fid, "redirect needs a target")
        elif atype == "thank_you":
            check_text(f"{fid}.after_submit", after.get("copy"), after.get("text"))
            used_text.append((after.get("copy"), after.get("text")))
    for b in blocks:
        for e in b.get("elements", []):
            if e.get("primitive") == "form" and e.get("form") not in form_ids:
                f.fail("P15", f"{b.get('id')}.{e.get('id')}", f"form {e.get('form')!r} is not defined")

    # CTA and mandatories
    if not _nonempty(cta):
        f.fail("P12", "ask.cta_wording", "missing; it comes from the packet")
    elif not any(text == cta for _, text in used_text):
        f.fail("P12", "ask.cta_wording", "no button or submit uses the approved CTA wording exactly")
    placed_ids = {cid for cid, _ in used_text}
    for m in sheet.get("mandatories", []):
        if m not in copy:
            f.fail("P13", f"mandatories.{m}", "not in the approved copy")
        elif m not in placed_ids:
            f.fail("P13", f"mandatories.{m}", "mandatory not placed on the page")

    # measurement
    event = ask.get("success_event")
    goals = set(ask.get("conversion_goals", []))
    if event not in SUCCESS_EVENTS:
        f.fail("P16", "ask.success_event", f"{event!r} unknown")
    elif event == "OPEN":
        f.warn("P16", "ask.success_event", "measured event is OPEN: BriefMachine to resolve")
    if not goals <= GOALS:
        f.fail("P16", "ask.conversion_goals", f"unknown goals {sorted(goals - GOALS)}")
    if "external_page" in goals and len(goals) > 1:
        f.fail("P16", "ask.conversion_goals", "external page goals cannot run with on-page goals")
    if event == "form_submission":
        if "form_submissions" not in goals:
            f.fail("P16", "ask.conversion_goals", "measured event is a form submission; form_submissions goal missing")
        if "link_clicks" in goals:
            f.warn("P16", "ask.conversion_goals", "link-click goals add clicks to the same total as submissions")
    if event == "link_click" and "link_clicks" not in goals:
        f.fail("P16", "ask.conversion_goals", "measured event is a click; link_clicks goal missing")
    if event == "external_page" and goals != {"external_page"}:
        f.fail("P16", "ask.conversion_goals", "measured event is off-page; use the external_page goal only")

    # code
    for c in sheet.get("code", []):
        cid = c.get("id", "?")
        loc = c.get("location")
        if loc not in CODE_LOCATIONS:
            f.fail("P06", cid, f"location {loc!r} unknown")
        if c.get("owns_ui"):
            if c.get("kind") == "infrastructure":
                f.fail("P06", cid, "infrastructure code may not create or change visible UI")
            approved_exception(c.get("exception"), cid, "COMPONENT")
        elif loc == "inline_css":
            approved_exception(c.get("exception"), cid, "COMPONENT")
        else:
            approved_exception(c.get("exception"), cid)

    # constraints and exceptions
    for con in sheet.get("constraints", []):
        cid = con.get("id", "?")
        if con.get("status") == "OPEN":
            if con.get("material"):
                f.fail("P20", cid, "material constraint OPEN: waiting on creative-engine-director")
            else:
                f.warn("P20", cid, f"constraint OPEN with {con.get('route_to', 'its owner')}")
    for eid in exceptions:
        if eid not in used_exceptions:
            f.warn("P24", eid, "exception in the register is not used by the plan")

    return f


# ---------------------------------------------------------------------------
# qa
# ---------------------------------------------------------------------------

def _find_scores(node, path="$"):
    hits = []
    if isinstance(node, dict):
        for key, value in node.items():
            if "score" in str(key).lower():
                hits.append(f"{path}.{key}")
            hits.extend(_find_scores(value, f"{path}.{key}"))
    elif isinstance(node, list):
        for i, value in enumerate(node):
            hits.extend(_find_scores(value, f"{path}[{i}]"))
    return hits


def _approval_complete(approval):
    return isinstance(approval, dict) and all(_nonempty(approval.get(k)) for k in ("by", "date", "evidence"))


def validate_qa(result):
    errors = []
    if result.get("format") != "instapage-qa/1":
        errors.append('format: expected "instapage-qa/1"')
    meta = result.get("meta", {})
    for key in ("client", "project", "packet", "by"):
        if not _nonempty(meta.get(key)):
            errors.append(f"meta.{key}: missing")
    if meta.get("stage") not in QA_STAGES:
        errors.append(f"meta.stage: {meta.get('stage')!r} not one of {sorted(QA_STAGES)}")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(meta.get("date", ""))):
        errors.append("meta.date: expected YYYY-MM-DD")
    compared = meta.get("compared", {})
    for key in ("packet", "copy", "spec"):
        if not _nonempty(compared.get(key) if isinstance(compared, dict) else None):
            errors.append(f"meta.compared.{key}: missing")

    for hit in _find_scores(result):
        errors.append(f"{hit}: production QA carries no scores")

    seen = {}
    for check in result.get("checks", []):
        cid = check.get("id")
        if cid not in QA_CATALOG:
            errors.append(f"checks: {cid!r} is not in the catalog")
            continue
        if cid in seen:
            errors.append(f"checks: {cid} appears twice")
            continue
        seen[cid] = check
        if check.get("status") not in QA_STATUSES:
            errors.append(f"{cid}: status {check.get('status')!r} not one of {sorted(QA_STATUSES)}")
        if check.get("blocking") is not QA_CATALOG[cid]:
            errors.append(f"{cid}: blocking must be {QA_CATALOG[cid]} (catalog)")
        if check.get("owner") not in QA_OWNERS:
            errors.append(f"{cid}: owner {check.get('owner')!r} not one of {sorted(QA_OWNERS)}")
        if not _nonempty(check.get("evidence")):
            errors.append(f"{cid}: evidence (or the reason it was not run) is missing")
    for cid in QA_CATALOG:
        if cid not in seen:
            errors.append(f"checks: {cid} missing")

    statuses = [c.get("status") for c in seen.values()]
    computed = {
        "pass": statuses.count("PASS"),
        "fail": statuses.count("FAIL"),
        "warning": statuses.count("WARNING"),
        "not_run": statuses.count("NOT_RUN"),
    }
    blocking = sorted(cid for cid, c in seen.items()
                      if QA_CATALOG[cid] and c.get("status") in ("FAIL", "NOT_RUN"))
    listed = sorted(str(item).split(":")[0].strip() for item in result.get("blocking_issues", []))
    if listed != blocking:
        errors.append(f"blocking_issues: lists {listed}, should list {blocking}")

    approvals = result.get("approvals", {})
    approvals_ok = _approval_complete(approvals.get("creative")) and _approval_complete(approvals.get("go_ahead"))
    publish_allowed = not blocking and approvals_ok

    declared = result.get("result", {})
    for key, value in computed.items():
        if declared.get(key) != value:
            errors.append(f"result.{key}: says {declared.get(key)}, checks give {value}")
    if declared.get("publish_allowed") is not publish_allowed:
        errors.append(f"result.publish_allowed: says {declared.get('publish_allowed')}, gate gives {publish_allowed}")

    return errors, computed, blocking, publish_allowed, approvals_ok


def skeleton(stage):
    return {
        "format": "instapage-qa/1",
        "meta": {
            "client": "", "project": "", "packet": "", "stage": stage,
            "date": "YYYY-MM-DD", "by": "",
            "page": {"workspace_id": "OPEN", "page_id": None, "name": "", "version": None, "url": None},
            "compared": {"packet": "", "copy": "", "spec": "", "build_sheet": ""},
        },
        "checks": [
            {"id": cid, "status": "NOT_RUN", "blocking": QA_CATALOG[cid], "owner": "PR", "evidence": ""}
            for cid in QA_CATALOG
        ],
        "blocking_issues": [f"{cid}: not run" for cid in QA_CATALOG if QA_CATALOG[cid]],
        "approvals": {
            "creative": {"by": None, "date": None, "evidence": None},
            "go_ahead": {"by": None, "date": None, "evidence": None},
        },
        "result": {"pass": 0, "fail": 0, "warning": 0, "not_run": len(QA_CATALOG), "publish_allowed": False},
    }


def _load(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"cannot read {path}: {exc}", file=sys.stderr)
        sys.exit(2)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_plan = sub.add_parser("plan", help="lint a build sheet")
    p_plan.add_argument("file")
    p_plan.add_argument("--json", action="store_true", help="machine-readable findings")
    p_qa = sub.add_parser("qa", help="validate a QA result")
    p_qa.add_argument("file")
    p_sk = sub.add_parser("skeleton", help="print a QA result skeleton")
    p_sk.add_argument("--stage", default="PLAN", choices=sorted(QA_STAGES))
    args = parser.parse_args(argv)

    if args.cmd == "skeleton":
        print(json.dumps(skeleton(args.stage), indent=2))
        return 0

    if args.cmd == "plan":
        findings = lint_plan(_load(args.file))
        fails, warns = findings.count("FAIL"), findings.count("WARNING")
        if args.json:
            print(json.dumps({
                "fail": fails, "warning": warns,
                "findings": [{"level": l, "rule": r, "where": w, "message": m} for l, r, w, m in findings.items],
            }, indent=2))
        else:
            for level, rule, where, message in findings.items:
                print(f"{level:7} {rule:4} {where}: {message}")
            print(f"PLAN: {fails} FAIL · {warns} WARNING · {'build may proceed' if not fails else 'fix or escalate before building'}")
        return 1 if fails else 0

    errors, computed, blocking, publish_allowed, approvals_ok = validate_qa(_load(args.file))
    for error in errors:
        print(f"INVALID {error}")
    print(f"QA: {computed['pass']} PASS · {computed['fail']} FAIL · {computed['warning']} WARNING · "
          f"{computed['not_run']} NOT_RUN · blocking {len(blocking)} · approvals {'complete' if approvals_ok else 'incomplete'} · "
          f"publish allowed: {'YES' if publish_allowed else 'NO'}")
    print("RESULT FILE: " + ("valid" if not errors else f"{len(errors)} problem(s)"))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
