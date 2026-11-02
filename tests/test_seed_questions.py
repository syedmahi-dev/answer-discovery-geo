import importlib.util, unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('seed_questions',Path(__file__).resolve().parents[1]/'scripts'/'seed_questions.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)

class SeedQuestionTests(unittest.TestCase):
    def test_no_frequency_or_fake_observed(self):
        rows=mod.generate({'category':'teacher tool','jobs_to_be_done':['manage attendance']})
        self.assertGreaterEqual(len(rows),25)
        self.assertTrue(all(r['origin_label']=='HYPOTHESIS' and r['observed_frequency']=='unknown' for r in rows))
    def test_no_brand_in_generated_queries(self):
        rows=mod.generate({'offer_name':'Invented Brand X', 'category':'grading tool'})
        self.assertTrue(all('Invented Brand X' not in r['question'] for r in rows))
    def test_excludes_planned_feature(self):
        rows=mod.generate({'capabilities_planned_or_unverified':['magic teleportation'], 'capabilities_verified':['attendance'], 'category':'classroom tool'})
        self.assertTrue(all('magic teleportation' not in r['question'] for r in rows))
    def test_deduplicated(self):
        rows=mod.generate({'jobs_to_be_done':['a', 'a'], 'problems':['b', 'b']})
        qs=[r['question'].lower() for r in rows]
        self.assertEqual(len(qs),len(set(qs)))
if __name__=='__main__': unittest.main()
