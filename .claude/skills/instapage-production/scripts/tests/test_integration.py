import copy
import unittest
from test_ip_check import good_sheet,filled_qa
import ip_check

class IntegrationExceptions(unittest.TestCase):
    def sheet(self):
        s=good_sheet()
        s['exceptions'] += [{'id':'EXC-CRM','class':'INTEGRATION','status':'APPROVED','approved_by':'Synthetic approver',
            **{k:'Synthetic documented value' for k in ('requirement','native_alternatives','editing_owner','editing_route','maintenance_owner','tracking_method','validation_plan','approval_date','approval_evidence')}}]
        s['forms'][0].update(delivery='external',exception='EXC-CRM')
        el=s['blocks'][1]['elements'][0];el.pop('form');el.update(primitive='html',exception='EXC-CRM',integration_form='F01')
        s['ask'].update(success_event='external_submission',conversion_goals=[],external_tracking={k:'Synthetic value' for k in ('provider','success_event','attribution','deduplication','validation_plan')})
        return s
    def test_approved_external_form_allowed(self):
        self.assertEqual(ip_check.lint_plan(self.sheet()).count('FAIL'),0)
    def test_external_not_native_submission(self):
        s=self.sheet();s['ask'].update(success_event='form_submission',conversion_goals=['form_submissions'])
        self.assertTrue(any(x[1]=='P16' and x[0]=='FAIL' for x in ip_check.lint_plan(s).items))
    def test_owners_and_tracking_required(self):
        for key in ('editing_owner','maintenance_owner','tracking_method','native_alternatives'):
            s=self.sheet();s['exceptions'][-1].pop(key)
            self.assertGreater(ip_check.lint_plan(s).count('FAIL'),0)
    def test_proposed_exception_blocked(self):
        s=self.sheet();s['exceptions'][-1]['status']='PROPOSED'
        self.assertGreater(ip_check.lint_plan(s).count('FAIL'),0)
    def test_external_primitive_not_native(self):
        s=self.sheet();s['blocks'][1]['elements'][0].update(primitive='form',form='F01')
        self.assertGreater(ip_check.lint_plan(s).count('FAIL'),0)
    def test_incomplete_qa_never_authorizes(self):
        q=filled_qa();q['checks'].pop()
        errors,_,_,allowed,_=ip_check.validate_qa(q)
        self.assertTrue(errors);self.assertFalse(allowed)
