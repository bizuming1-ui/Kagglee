#!/usr/bin/env python3
"""Refresh complete memo bodies, retaining historical sections and latest header."""
from pathlib import Path
import re
repo=Path(__file__).resolve().parents[3];path=repo/'docs/KAGGLE_HANDOFF_PROMPT.md'
value=path.read_text();names=re.findall(r'^## 内嵌备忘录：(\S+)$',value,re.M)
for name in ('KAGGLE_STEP13_PLAN.md','KAGGLE_STEP13_AUDIT.md','KAGGLE_STEP13_QUICKSTART.md'):
    if name not in names:names.insert(names.index('KAGGLE_TARGET_ACCEPTANCE.md'),name)
assert len(names)==33 and len(set(names))==33
header=value.split('\n## 内嵌备忘录：',1)[0].rstrip()
if header.endswith('---'):header=header[:-3].rstrip()
path.write_text(header+'\n\n---\n\n'+'\n\n---\n\n'.join('## 内嵌备忘录：'+name+'\n\n'+(repo/'docs'/name).read_text().rstrip() for name in names)+'\n')
print('refreshed',len(names),'complete embedded memos;',path.stat().st_size,'bytes')
