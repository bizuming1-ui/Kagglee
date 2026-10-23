"""Static HTML preservation checks complement, never replace, Chromium viewport tests."""
import ast
import base64
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import unittest
import zlib

REPO=Path(__file__).resolve().parents[2]

class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.ids=[];self.scripts=[];self.primary=[];self.nav=False;self.feed(text)
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs:self.ids.append(attrs['id'])
        if tag=='script':self.scripts.append(attrs.get('src'))
        if tag=='nav':self.nav=attrs.get('aria-label')=='主要视图'
        if tag=='button' and self.nav:self.primary.append(attrs.get('id'))
    def handle_endtag(self,tag):
        if tag=='nav':self.nav=False

class LayoutTests(unittest.TestCase):
    def test_step3_dom_ids_and_script_order_are_preserved_without_duplicates(self):
        source=(REPO/'kaggle/kaggle-fixed-step3.py').read_text()
        tree=ast.parse(source)
        node=next(node for node in tree.body if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='FILES' for t in node.targets))
        files=ast.literal_eval(node.value)
        previous=Page(zlib.decompress(base64.b64decode(files['web/index.html'][1])).decode())
        current=Page((REPO/'kaggle/source/web/index.html').read_text())
        self.assertTrue(set(previous.ids)<=set(current.ids),set(previous.ids)-set(current.ids))
        self.assertFalse([name for name,count in Counter(current.ids).items() if count>1])
        self.assertEqual(previous.scripts,current.scripts)

    def test_only_two_primary_buttons_with_separate_native_diagnostics(self):
        text=(REPO/'kaggle/source/web/index.html').read_text()
        current=Page(text)
        self.assertEqual(current.primary,['nav-lab','nav-speak'])
        self.assertIn('<dialog id="diagnostics" aria-labelledby="diagnostics-title">',text)
        self.assertIn('id="reference-options"',text)
        self.assertNotIn('https://fonts.',text)  # no new third-party font/network dependency

if __name__=='__main__':unittest.main()
