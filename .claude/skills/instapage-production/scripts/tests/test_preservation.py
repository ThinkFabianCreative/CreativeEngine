import copy
import sys
from pathlib import Path
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from ip_preserve import merge,digest

class Preservation(unittest.TestCase):
    def setUp(self):
        self.base={'elements':{'E1':{'text':'before','mobile':{'gap':8}},'E2':{'link':'old'}},'unknown':{'keep':True}}
        self.current=copy.deepcopy(self.base)
        self.current['elements']['E1']['text']='human copy'
        self.current['elements']['E1']['mobile']['gap']=19
    def req(self,path,value):
        return {'current_sha256':digest(self.current),'changes':[{'path':path,'value':value}]}
    def test_preserves_human_and_unknown_data(self):
        r=merge(self.base,self.current,self.req(['elements','E2','link'],'new'))
        self.assertEqual(r['elements']['E1'],self.current['elements']['E1'])
        self.assertEqual(r['unknown'],self.base['unknown'])
        self.assertEqual(r['elements']['E2']['link'],'new')
        self.assertEqual(self.current['elements']['E2']['link'],'old')
    def test_conflict_stops(self):
        with self.assertRaisesRegex(ValueError,'conflict'):
            merge(self.base,self.current,self.req(['elements','E1','text'],'automation'))
    def test_noop_keeps_human(self):
        self.assertEqual(merge(self.base,self.current,self.req(['elements','E1','text'],'before')),self.current)
    def test_stale_current_stops(self):
        q=self.req(['elements','E2','link'],'new'); self.current['unknown']['keep']=False
        with self.assertRaisesRegex(ValueError,'changed'): merge(self.base,self.current,q)
    def test_structure_stops(self):
        with self.assertRaisesRegex(ValueError,'structure'): merge(self.base,self.current,self.req(['elements'],{}))
    def test_missing_path_stops(self):
        with self.assertRaisesRegex(ValueError,'missing'): merge(self.base,self.current,self.req(['missing'],'x'))
    def test_reordered_array_stops(self):
        b={'els':[{'id':'one','text':'x'},{'id':'two','text':'x'}]}; c={'els':list(reversed(b['els']))}
        with self.assertRaisesRegex(ValueError,'array changed'):
            merge(b,c,{'current_sha256':digest(c),'changes':[{'path':['els',0,'text'],'value':'wrong target'}]})
    def test_already_applied_is_idempotent(self):
        r=merge(self.base,self.current,self.req(['elements','E1','text'],'human copy'))
        self.assertEqual(r,self.current)
