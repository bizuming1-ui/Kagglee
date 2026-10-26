"""S5 full-script integration/syntax + real Node Player/Worklet execution, not audio quality."""
import hashlib,json,subprocess,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[2];OLD=R/'kaggle/source/web/app.js';NEW=R/'kaggle/step18/web/app.js'
class PlaybackSourceContracts(unittest.TestCase):
    def test_01_frozen_matches_real_prechange_archive(self):
        self.assertEqual(OLD.read_bytes(),(R/'docs/validation/step18/s5-before/kaggle/source/web/app.js').read_bytes())
    def test_02_complete_ui_suffix_unchanged(self):
        marker='  var r = (t) =>';self.assertEqual(NEW.read_text().split(marker,1)[1],OLD.read_text().split(marker,1)[1]);self.assertGreater(len(NEW.read_bytes()),50000)
    def test_03_network_parser_unchanged(self):
        self.assertEqual(NEW.read_text().split('  var V = `',1)[0],OLD.read_text().split('  var V = `',1)[0])
    def test_04_arrival_predictor_unchanged(self):
        a,b='    X = {','    P = class';self.assertEqual(NEW.read_text().split(a,1)[1].split(b,1)[0],OLD.read_text().split(a,1)[1].split(b,1)[0])
    def test_05_formal_source_not_switched(self):
        base=json.loads((R/'docs/validation/step18/baseline.json').read_text())
        self.assertEqual(json.loads((R/'workspace/HEAD.json').read_text())['revision'],base['formal_revision'])
        self.assertNotEqual(OLD.read_bytes(),NEW.read_bytes())
    def test_06_npm_inputs_unchanged(self):
        for n in ('package.json','package-lock.json','playwright.config.js'):
            with self.subTest(n=n):self.assertEqual((R/n).read_bytes(),(R/'docs/validation/step18/s5-before'/n).read_bytes())
    def test_07_candidate_full_script_syntax(self):
        cp=subprocess.run(['node','--check',str(NEW)],capture_output=True,text=True,timeout=10);self.assertEqual(cp.returncode,0,cp.stderr)
    def test_08_actual_player_worklet_contracts(self):
        cp=subprocess.run(['node','kaggle/tests/test_step18_playback.mjs'],cwd=R,capture_output=True,text=True,timeout=20)
        self.assertEqual(cp.returncode,0,cp.stderr);d=json.loads(cp.stdout);self.assertEqual(d['tests'],37);self.assertEqual(d['passed'],37);self.assertEqual(d['failures'],0);self.assertTrue(d['actual_player_and_worklet_vm'])
if __name__=='__main__':unittest.main(verbosity=2)
