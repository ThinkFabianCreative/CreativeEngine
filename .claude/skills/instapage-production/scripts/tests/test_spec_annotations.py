import copy
import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from ip_spec_check import lint

class AnnotationParity(unittest.TestCase):
    def setUp(self):
        nodes=[{'name':'B01 · section','annotations':[]}, {'name':'E01 · Headline','annotations':[{'category':'copy','label':'HERO-H'}],'text':'Same words'}]
        self.data={'policy':'explicit-repeat','desktop':nodes,'mobile':copy.deepcopy(nodes)}
    def test_repeated_plus_mobile_setting(self):
        self.data['mobile'][1]['annotations'].append({'category':'build','label':'Mobile size 40'})
        self.assertEqual(lint(self.data),[])
    def test_missing_copy_fails(self):
        self.data['mobile'][1]['annotations']=[]
        self.assertTrue(lint(self.data))
    def test_duplicate_id_fails(self):
        self.data['mobile'].append(copy.deepcopy(self.data['mobile'][1]))
        self.assertTrue(lint(self.data))
    def test_unnamed_counterpart_fails(self):
        self.data['mobile'][1]['name']='IP / Headline'
        self.assertTrue(lint(self.data))
    def test_copy_drift_fails(self):
        self.data['mobile'][1]['text']='Changed'
        self.assertTrue(lint(self.data))

    def test_annotation_serialization_entities(self):
        self.data['desktop'][1]['annotations'][0]['label']='Claim "tools"'
        self.data['mobile'][1]['annotations'][0]['label']='Claim &quot;tools&quot;'
        self.assertEqual(lint(self.data),[])
