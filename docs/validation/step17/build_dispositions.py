from pathlib import Path
import ast,json,hashlib,collections
R=Path(__file__).resolve().parents[3];H=Path(__file__).resolve().parent
reviews=json.loads((H/'review-before.json').read_text())
I=[set([2,3,6,7,8,9,*range(11,20),21,22,23,24,25,26,27,30,31,33,38,39,41,42,46,48]),set([4,5,6,7,8,11,12,13,14,15,16,21,22,24,31,32,34]),set(range(1,29))|set(range(31,47))|{49}]
D=[{1,10,20,32,35,37,40,49},{3,9,20,23,25,26,29,40,45,47,50},{29,30,47,48,50}]
HARD=[set(),{10,28,49},set()]
anchors={1:'py/reference_segments.py;py/analyst.py;py/library_api.py;web/index.html;tests/test_step17.py;tests/long_reference_check.py',2:'py/voice_binding.py;go/gateway/session.go;go/gateway/segmenter.go;go/gateway/main.go;tests/test_step17.py',3:'tests/test_step17.py;tests/browser/qtts.spec.js;tests/browser/studio.spec.js;validation/step17/verify_delivery.py'}
counts=collections.Counter();out=[]
for r,review in enumerate(reviews):
 rows=[]
 for i,(ident,topic,text) in enumerate(review['entries'],1):
  kind='preserved-with-regression'
  if i in I[r]:kind='implemented-action'
  if i in D[r]:kind='documented-boundary'
  if i in HARD[r]:kind='hardware-listening-blocked'
  if i>50 and any(v in text for v in ('真实试听','真实训练质量','真实T4','真实边界爆音','用户音频','仍要听','需要真实对照','真人试听','须真实')):kind='hardware-listening-blocked'
  if i>50 and any(v in text for v in ('不保证','不能保证','不假装','不能伪造','不承诺','不声称','不猜根因','不是训练','仍需','明确blocked','无CUDA输出')):kind='documented-boundary'
  if r==1 and i==49:kind='hardware-listening-blocked'
  counts[kind]+=1
  rows.append({'recommendation':ident,'topic':topic,'suggestion':text,'disposition':kind,'anchors':anchors[r+1],
    'note':'工程修复/测试或保留边界按收据核查；并不证明真实ASR转写正确、克隆相似、无噪声、双卡声学相同或RTF达标。'})
 out.append({'round':r+1,'items':rows})
(H/'review-disposition.json').write_text(json.dumps({'stage':17,'total':300,'counts':dict(counts),'all_user_requirements_completed':False,'rounds':out},ensure_ascii=False,indent=2)+'\n')
inventory=[]
for p in sorted((R/'kaggle/source').rglob('*')):
 if not p.is_file() or any(v in p.parts for v in ('state','target','__pycache__')) or p.name=='gateway':continue
 b=p.read_bytes()
 if p.suffix=='.py':ast.parse(b)
 inventory.append({'path':str(p.relative_to(R/'kaggle/source')),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
(H/'review-final.json').write_text(json.dumps([{'round':r,'read_hash_ast_not_semantic_proof':True,'topic_review':f'KAGGLE_STEP17_REVIEW{r}.md','files':inventory} for r in (1,2,3)],ensure_ascii=False,indent=2)+'\n')
print(dict(counts))
