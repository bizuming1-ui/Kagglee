"""Explicit dispositions: recommendations are not 300 implemented fixes."""
from pathlib import Path
import json
from collections import Counter
H=Path(__file__).resolve().parent
rows=json.loads((H/'review-before.json').read_text())
implemented={
1:set([1,2,3,4,5,6,11,12,13,16,17,19,20,21,35,36,37,38,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67]),
2:set([1,2,3,4,6,8,10,14,41,42,43,44,45,81,82,83,84,86,87,88,89]),
3:set([1,2,3,4,5,15,16,20,21,22,23,24,31,32,33,34,35,36,37,38,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,71,72,73,77,81,82,83,84,85,86,87,88,89,90])}
# Code changes / fixtures cannot satisfy these acoustic, target GPU or broader architecture items.
hardware={1:{20,90},2:{66},3:{93,94,96,97,98}}
documented={1:{7,16,40,70,80,81,82,83,84,85,86,87,88},2:{46,47,49,50,65,67,68,80},3:{6,7,29,30,50,80,91,92,95,100}}
deferred={1:{50},2:set(),3:{99}}
anchors={
1:'kaggle/source/py/worker.py; py/qtts_common.py; tests/test_step15.py; reference-isolation-round{1,2,3}.json',
2:'kaggle/source/go/gateway/{segmenter,main,session,scheduler}.go; fidelity_test.go; go-final-race3.txt; tests/browser/qtts.spec.js',
3:'kaggle/source/py/{analyst,library_api}.py; web/{index.html,app.js}; tests/test_step15.py; python-round{1,2,3}.txt; browser-repeat3.txt'}
result=[]
for row in rows:
 r=row['round'];items=[]
 for n,(ident,anchor,text) in enumerate(row['entries'],1):
  if n in deferred[r]:status='not-implemented';reason='严格声学拒播/历史网页训练闭环仍缺；不是本轮已验收功能。'
  elif n in hardware[r]:status='requires-hardware';reason='代码或风险文档已处理其工程部分，真实Qwen/T4、原音频、听感或峰值/吞吐仍未执行，不能打完成。'
  elif n in documented[r]:status='documented-boundary';reason='对应取舍/风险已在PLAN、AUDIT或QUICKSTART明确；说明边界不是运行实测或修复性能的证据。'
  elif n in implemented[r]:status='implemented';reason='本轮相关路径修改或新增回归，详见锚点与AUDIT；CPU测试不等于该条全部声学目标达标。'
  else:status='preserved';reason='保留现有约束/算法/入口，未为凑修改量重写；完整回归只证明已测范围。'
  items.append({'recommendation':ident,'anchor':anchor,'text':text,'status':status,'reason':reason,'evidence':anchors[r]})
 result.append({'round':r,'items':items})
counts=Counter(item['status'] for row in result for item in row['items'])
(H/'review-disposition.json').write_text(json.dumps({'recommendations':300,'all_recommendations_implemented':False,'implemented_means':'code/test action, not a distinct bug fix or GPU acceptance','counts':dict(counts),'rounds':result},ensure_ascii=False,indent=2)+'\n')
print(dict(counts))
