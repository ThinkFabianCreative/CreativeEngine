"""Tests for ip_check.py. Run from the repo root:

    python3 -m unittest discover -s .claude/skills/instapage-production/scripts/tests -v

Fixtures are synthetic and hold no client facts.
"""

import copy
import json
import pathlib
import re
import subprocess
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
SCRIPTS = HERE.parent
SKILL = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

import ip_check  # noqa: E402


def good_sheet():
    """A small, valid synthetic build sheet: hero, form section, global footer."""
    return {
        "format": "instapage-build-sheet/1",
        "meta": {
            "client": "SYNTHETIC", "project": "test-page", "packet": "LP1", "version": "v01",
            "date": "2026-09-24",
            "workspace": {"name": "test", "id": "OPEN"},
            "spec": {"figma": "https://www.figma.com/design/x", "version": "v01"},
            "copy_doc": {"path": "work/copy/LP1_copy_v01.md", "version": "v01"},
        },
        "ask": {
            "cta_wording": "Join now",
            "destination": "native form on this page",
            "success_event": "form_submission",
            "conversion_goals": ["form_submissions"],
        },
        "copy": {
            "H1": "One headline.",
            "SUB": "A supporting line.",
            "CTA": "Join now",
            "F-NAME": "First name",
            "F-EMAIL": "Email",
            "TY": "Thanks. Check your inbox.",
            "ALT-HERO": "A test image.",
            "FOOT": "Legal line.",
            "FAQ-Q": "A question?",
            "FAQ-A": "An answer.",
        },
        "mandatories": ["FOOT"],
        "styles": {"brand_colors": ["#111111", "#FFFFFF"], "fonts": {"headline": "A", "paragraph": "B", "button": "B"}},
        "assets": [
            {"id": "IMG-01", "description": "hero", "status": "PRODUCTION-APPROVED", "generated": False,
             "provenance": "client shoot", "rights": "client-owned", "approved_by": "client, 2026-09-24",
             "alt_copy": "ALT-HERO"},
        ],
        "blocks": [
            {"id": "B01", "name": "Hero", "type": "fluid_grid", "reuse": "my_block",
             "grid": {"columns": 12, "rows": 1},
             "containers": [
                 {"id": "B01.C1", "span": "1-7", "mobile_order": 1, "flow": "vertical"},
                 {"id": "B01.C2", "span": "8-12", "mobile_order": 2, "flow": "vertical"},
             ],
             "elements": [
                 {"id": "E01", "primitive": "headline", "container": "B01.C1", "level": 1, "copy": "H1", "text": "One headline."},
                 {"id": "E02", "primitive": "paragraph", "container": "B01.C1", "copy": "SUB", "text": "A supporting line."},
                 {"id": "E03", "primitive": "button", "container": "B01.C1", "copy": "CTA", "text": "Join now",
                  "link": {"type": "on_page", "target": "B02"}},
                 {"id": "E04", "primitive": "image", "container": "B01.C2", "asset": "IMG-01"},
             ]},
            {"id": "B02", "name": "Form", "type": "fluid_grid", "reuse": "page",
             "containers": [{"id": "B02.C1", "span": "1-12", "mobile_order": 1, "flow": "vertical"}],
             "elements": [
                 {"id": "E05", "primitive": "form", "container": "B02.C1", "form": "F01"},
                 {"id": "E06", "primitive": "accordion", "container": "B02.C1",
                  "items": [{"title_copy": "FAQ-Q", "title": "A question?", "body_copy": "FAQ-A", "body": "An answer."}]},
             ]},
            {"id": "B03", "name": "Footer", "type": "fluid_grid", "reuse": "global_block",
             "global": {"name": "GLOBAL · Footer · v01", "reason": "legal line maintained once for every page",
                        "owner": "client marketing", "approved_by": "client, 2026-09-24"},
             "containers": [{"id": "B03.C1", "span": "1-12", "mobile_order": 1, "flow": "vertical"}],
             "elements": [
                 {"id": "E07", "primitive": "paragraph", "container": "B03.C1", "copy": "FOOT", "text": "Legal line."},
             ]},
        ],
        "forms": [
            {"id": "F01",
             "packet_fields": [
                 {"label": "First name", "type": "first_name", "required": True},
                 {"label": "Email", "type": "email", "required": True},
             ],
             "fields": [
                 {"label_copy": "F-NAME", "label": "First name", "type": "first_name", "required": True},
                 {"label_copy": "F-EMAIL", "label": "Email", "type": "email", "required": True},
             ],
             "submit": {"copy": "CTA", "text": "Join now"},
             "after_submit": {"type": "thank_you", "copy": "TY", "text": "Thanks. Check your inbox."},
             "integration": "OPEN (Q1)"},
        ],
        "code": [
            {"id": "CODE-01", "location": "scripts_privacy", "kind": "infrastructure", "owns_ui": False,
             "purpose": "analytics tag behind the cookie bar", "exception": "EXC-01"},
        ],
        "exceptions": [
            {"id": "EXC-01", "class": "INFRASTRUCTURE", "status": "APPROVED", "approved_by": "client, 2026-09-24",
             "summary": "tag with no native integration"},
        ],
        "constraints": [],
    }


def rules(findings, level=None):
    return {rule for lvl, rule, _, _ in findings.items if level is None or lvl == level}


class PlanLint(unittest.TestCase):

    def assertFails(self, sheet, rule):
        findings = ip_check.lint_plan(sheet)
        self.assertIn(rule, rules(findings, "FAIL"), findings.items)

    def test_good_sheet_passes(self):
        findings = ip_check.lint_plan(good_sheet())
        self.assertEqual(findings.count("FAIL"), 0, findings.items)
        self.assertEqual(findings.count("WARNING"), 0, findings.items)

    def test_unknown_primitive(self):
        s = good_sheet()
        s["blocks"][0]["elements"][1]["primitive"] = "react_component"
        self.assertFails(s, "P02")

    def test_html_without_approved_exception(self):
        s = good_sheet()
        s["blocks"][0]["elements"].append({"id": "E09", "primitive": "html", "container": "B01.C1"})
        self.assertFails(s, "P05")
        s["blocks"][0]["elements"][-1]["exception"] = "EXC-01"   # exists but is INFRASTRUCTURE
        self.assertFails(s, "P05")
        s["exceptions"].append({"id": "EXC-02", "class": "COMPONENT", "status": "PROPOSED", "approved_by": ""})
        s["blocks"][0]["elements"][-1]["exception"] = "EXC-02"   # component, but only proposed
        self.assertFails(s, "P05")

    def test_shape_in_fluid_grid(self):
        s = good_sheet()
        s["blocks"][0]["elements"].append({"id": "E09", "primitive": "box", "container": "B01.C1"})
        self.assertFails(s, "P04")

    def test_shape_in_canvas_allowed(self):
        s = good_sheet()
        s["blocks"].insert(1, {"id": "B09", "name": "Canvas", "type": "canvas", "reuse": "page",
                               "elements": [{"id": "E09", "primitive": "box"}]})
        self.assertNotIn("P04", rules(ip_check.lint_plan(s)))

    def test_accordion_with_link(self):
        s = good_sheet()
        s["blocks"][1]["elements"][1]["items"][0]["link"] = "https://example.org"
        self.assertFails(s, "P07")

    def test_copy_must_match_exactly(self):
        s = good_sheet()
        s["blocks"][0]["elements"][0]["text"] = "One headline"          # full stop dropped
        self.assertFails(s, "P11")

    def test_cta_wording_exact(self):
        s = good_sheet()
        s["ask"]["cta_wording"] = "Join now!"
        self.assertFails(s, "P12")

    def test_mandatory_must_be_placed(self):
        s = good_sheet()
        del s["blocks"][2]
        self.assertFails(s, "P13")

    def test_generated_asset_never(self):
        s = good_sheet()
        s["assets"][0]["generated"] = True
        self.assertFails(s, "P14")

    def test_placeholder_warns(self):
        s = good_sheet()
        s["assets"][0]["status"] = "PLACEHOLDER"
        findings = ip_check.lint_plan(s)
        self.assertIn("P14", rules(findings, "WARNING"))
        self.assertEqual(findings.count("FAIL"), 0, findings.items)

    def test_missing_alt_text(self):
        s = good_sheet()
        s["assets"][0]["alt_copy"] = ""
        self.assertFails(s, "P14")

    def test_form_must_match_packet(self):
        s = good_sheet()
        s["forms"][0]["fields"][1]["required"] = False
        self.assertFails(s, "P15")
        s = good_sheet()
        s["forms"][0]["fields"].reverse()
        self.assertFails(s, "P15")

    def test_global_block_needs_reason(self):
        s = good_sheet()
        s["blocks"][2]["global"]["reason"] = ""
        self.assertFails(s, "P08")

    def test_global_block_twice(self):
        s = good_sheet()
        dup = copy.deepcopy(s["blocks"][2])
        dup["id"] = "B04"
        dup["containers"][0]["id"] = "B04.C1"
        dup["elements"][0]["container"] = "B04.C1"
        s["blocks"].append(dup)
        self.assertFails(s, "P08")

    def test_exactly_one_h1(self):
        s = good_sheet()
        s["blocks"][1]["elements"].append({"id": "E09", "primitive": "headline", "container": "B02.C1",
                                           "level": 1, "copy": "SUB", "text": "A supporting line."})
        self.assertFails(s, "P10")

    def test_brand_color_limit(self):
        s = good_sheet()
        s["styles"]["brand_colors"] = [f"#0000{i:02X}" for i in range(15)]
        self.assertFails(s, "P09")

    def test_extra_font_role(self):
        s = good_sheet()
        s["styles"]["fonts"]["display"] = "C"
        self.assertFails(s, "P09")

    def test_infrastructure_may_not_own_ui(self):
        s = good_sheet()
        s["code"][0]["owns_ui"] = True
        self.assertFails(s, "P06")

    def test_inline_css_needs_component_exception(self):
        s = good_sheet()
        s["code"].append({"id": "CODE-02", "location": "inline_css", "kind": "component", "owns_ui": False,
                          "purpose": "letter spacing", "exception": "EXC-01"})
        self.assertFails(s, "P05")

    def test_goals_follow_measured_event(self):
        s = good_sheet()
        s["ask"]["conversion_goals"] = ["link_clicks"]
        self.assertFails(s, "P16")
        s = good_sheet()
        s["ask"]["conversion_goals"] = ["external_page", "form_submissions"]
        self.assertFails(s, "P16")
        s = good_sheet()
        s["ask"]["conversion_goals"] = ["form_submissions", "link_clicks"]
        self.assertIn("P16", rules(ip_check.lint_plan(s), "WARNING"))

    def test_mobile_order_unique(self):
        s = good_sheet()
        s["blocks"][0]["containers"][1]["mobile_order"] = 1
        self.assertFails(s, "P17")

    def test_on_page_target_exists(self):
        s = good_sheet()
        s["blocks"][0]["elements"][2]["link"]["target"] = "B99"
        self.assertFails(s, "P19")

    def test_material_constraint_blocks_build(self):
        s = good_sheet()
        s["constraints"].append({"id": "CON-01", "constraint": "x", "affects": "B01", "route_to": "creative-engine-director",
                                 "material": True, "status": "OPEN"})
        self.assertFails(s, "P20")

    def test_video_host_and_timer(self):
        s = good_sheet()
        s["blocks"][0]["elements"].append({"id": "E09", "primitive": "video", "container": "B01.C2", "host": "tiktok"})
        self.assertFails(s, "P21")
        s = good_sheet()
        s["blocks"][0]["elements"].append({"id": "E09", "primitive": "timer", "container": "B01.C2", "mode": "evergreen"})
        self.assertFails(s, "P22")


def filled_qa(status="PASS", approvals=True):
    result = ip_check.skeleton("STAGING")
    result["meta"].update({"client": "SYNTHETIC", "project": "test-page", "packet": "LP1", "date": "2026-09-24", "by": "test"})
    result["meta"]["compared"] = {"packet": "p", "copy": "c v01", "spec": "s v01", "build_sheet": "b"}
    for check in result["checks"]:
        check["status"] = status
        check["evidence"] = "synthetic evidence"
    blocking = [c["id"] for c in result["checks"] if c["blocking"] and c["status"] in ("FAIL", "NOT_RUN")]
    result["blocking_issues"] = [f"{cid}: x" for cid in blocking]
    if approvals:
        result["approvals"] = {
            "creative": {"by": "creative-engine-director", "date": "2026-09-24", "evidence": "review v01"},
            "go_ahead": {"by": "user", "date": "2026-09-24", "evidence": "chat"},
        }
    n = len(result["checks"])
    result["result"] = {"pass": n if status == "PASS" else 0, "fail": n if status == "FAIL" else 0,
                        "warning": n if status == "WARNING" else 0, "not_run": n if status == "NOT_RUN" else 0,
                        "publish_allowed": status in ("PASS", "WARNING") and approvals}
    return result


class QAValidation(unittest.TestCase):

    def test_skeleton_structure(self):
        sk = ip_check.skeleton("PLAN")
        self.assertEqual(len(sk["checks"]), len(ip_check.QA_CATALOG))
        self.assertFalse(sk["result"]["publish_allowed"])

    def test_all_pass_with_approvals_allows_publish(self):
        errors, _, blocking, allowed, _ = ip_check.validate_qa(filled_qa())
        self.assertEqual(errors, [])
        self.assertEqual(blocking, [])
        self.assertTrue(allowed)

    def test_missing_approval_blocks(self):
        qa = filled_qa(approvals=False)
        errors, _, _, allowed, _ = ip_check.validate_qa(qa)
        self.assertEqual(errors, [])
        self.assertFalse(allowed)

    def test_claimed_publish_is_recomputed(self):
        qa = filled_qa()
        qa["checks"][0]["status"] = "FAIL"
        qa["result"]["pass"] -= 1
        qa["result"]["fail"] = 1
        errors, _, blocking, allowed, _ = ip_check.validate_qa(qa)
        self.assertFalse(allowed)
        self.assertIn(qa["checks"][0]["id"], blocking)
        self.assertTrue(any("blocking_issues" in e for e in errors))
        self.assertTrue(any("publish_allowed" in e for e in errors))

    def test_blocking_flag_cannot_be_lowered(self):
        qa = filled_qa()
        qa["checks"][0]["blocking"] = False
        errors, *_ = ip_check.validate_qa(qa)
        self.assertTrue(any("blocking must be True" in e for e in errors))

    def test_no_scores(self):
        qa = filled_qa()
        qa["checks"][0]["creative_score"] = 8
        errors, *_ = ip_check.validate_qa(qa)
        self.assertTrue(any("no scores" in e for e in errors))

    def test_missing_check_and_evidence(self):
        qa = filled_qa()
        qa["checks"].pop()
        qa["checks"][0]["evidence"] = ""
        errors, *_ = ip_check.validate_qa(qa)
        self.assertTrue(any("missing" in e and "checks" in e for e in errors))
        self.assertTrue(any("evidence" in e for e in errors))

    def test_warning_does_not_block(self):
        qa = filled_qa(status="WARNING")
        errors, _, blocking, allowed, _ = ip_check.validate_qa(qa)
        self.assertEqual(errors, [])
        self.assertEqual(blocking, [])
        self.assertTrue(allowed)


class DocsInSync(unittest.TestCase):
    """The checker and the references must describe the same rules."""

    def test_qa_catalog_matches_qa_md(self):
        text = (SKILL / "references" / "qa.md").read_text(encoding="utf-8")
        rows = re.findall(r"^\| ((?:CF|NA|FN|RS|GV)-\d{2}) \| (.+?) \|", text, flags=re.M)
        documented = {cid: "(blocking: no)" not in check for cid, check in rows}
        self.assertEqual(documented, ip_check.QA_CATALOG)

    def test_plan_rules_match_build_sheet_md(self):
        text = (SKILL / "references" / "build-sheet.md").read_text(encoding="utf-8")
        documented = set(re.findall(r"^\| (P\d{2}) \|", text, flags=re.M))
        code = (SCRIPTS / "ip_check.py").read_text(encoding="utf-8")
        used = set(re.findall(r'f\.(?:fail|warn)\("(P\d{2})"', code))
        self.assertEqual(used, documented)


class CommandLine(unittest.TestCase):

    def test_plan_exit_codes(self):
        tmp = HERE / "_tmp_sheet.json"
        try:
            tmp.write_text(json.dumps(good_sheet()), encoding="utf-8")
            ok = subprocess.run([sys.executable, str(SCRIPTS / "ip_check.py"), "plan", str(tmp)], capture_output=True, text=True)
            self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
            bad = good_sheet()
            bad["blocks"][0]["elements"][0]["text"] = "Changed."
            tmp.write_text(json.dumps(bad), encoding="utf-8")
            fail = subprocess.run([sys.executable, str(SCRIPTS / "ip_check.py"), "plan", str(tmp)], capture_output=True, text=True)
            self.assertEqual(fail.returncode, 1)
            self.assertIn("P11", fail.stdout)
        finally:
            tmp.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
