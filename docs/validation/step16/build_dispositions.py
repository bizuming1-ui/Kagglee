from pathlib import Path
import ast,hashlib,json,collections
R=Path(__file__).resolve().parents[3];H=Path(__file__).resolve().parent
reviews=json.loads((H/'review-before.json').read_text())
# Codes are explicit per recommendation: I new action, P preserved/regressed,
# D documented boundary, H hardware/listening still blocked, N deliberately not done.
def nums(text):
 out=set()
 for part in text.split(','):
  if not part:continue
  a,*b=part.split('-');out.update(range(int(a),int(b[0])+1) if b else [int(a)])
 return out
sets=[{
 'I':nums('2-7,11-12,14-20,21-29,32-37,41,51-52,55,57,61-66'),
 'H':nums('9-10,40,81-85,87,89'),
 'D':nums('1,8,30,38-39,43,58-59,67,78,80,86,88,90'),
}, {
 'I':nums('1-2,4-8,10-20,23,25-28,30,33,41-42,44-47,49,54-56,58-59,61-64,67,69,77-78,81-87,91-92'),
 'H':nums('29,39,60,80,89-90'),
 'N':nums('21,40,68'),
 'D':nums('36-38,51-53,57,65-66,70,74-76,79,88,93-96'),
}, {
 'I':nums('1-6,8,11-20,21-28,31-39,41-49,51-56,58,61-68,71-75,77-79'),
 'H':nums('40,81-87,89-96'),
 'N':nums('98-99'),
 'D':nums('7,9-10,29-30,50,57,59-60,69-70,76,80,88,97,100'),
}]
labels={'I':'implemented-action','P':'preserved-with-regression','D':'documented-boundary','H':'hardware-listening-blocked','N':'not-implemented-or-rejected'}
anchors={1:'py/clone_stream.py;py/voice_binding.py;py/worker.py;py/analyst.py;go/gateway/session.go;go/gateway/scheduler.go;go/gateway/main.go',2:'py/clone_stream.py;py/worker.py;tools/voice_benchmark.py;tests/test_step16.py;tests/actual_codec_check.py',3:'tests/test_step16.py;tests/reference_isolation_check.py;tests/actual_codec_check.py;tests/browser;KAGGLE_STEP16_QUICKSTART.md'}
rounds=[];counts=collections.Counter()
for review,selection in zip(reviews,sets):
 used=set()
 for cat,values in selection.items():assert not used&values;used|=values
 rows=[]
 for i,(ident,topic,suggestion) in enumerate(review['entries'],1):
  cat=next((c for c,v in selection.items() if i in v),'P');counts[labels[cat]]+=1
  note={'I':'按方案完成相应动作/测试入口；工程或CPU控制证据不构成声学/T4验收。','P':'保持现有实现及既有回归，不声称本轮新造功能。','D':'明确约束/定义/操作说明，不把文档边界称代码已验收。','H':'需要用户单人参考、完整训练权重、真实T4或真人试听；当前未验证。','N':'未实施或有证据否决默认策略；不隐藏缺口。'}[cat]
  if review['round']==2 and i in (13,21):note+=' 因实际causal源码及tiny前缀实验，默认前瞻0，2仅显式实验；不是默认160ms修复。'
  if review['round']==2 and i==40:note+=' 当前生成WAV是DSP后；原始模型PCM与用户噪声对照仍未做。'
  if review['round']==2 and i==68:note+=' 现有网页first_played/underruns保留，但新CLI未接真实浏览器音频首播。'
  rows.append({'recommendation':ident,'topic':topic,'suggestion':suggestion,'disposition':labels[cat],'implementation_or_review_anchors':anchors[review['round']],'explanation':note})
 rounds.append({'round':review['round'],'items':rows})
(H/'review-disposition.json').write_text(json.dumps({'stage':16,'total':300,'counts':dict(counts),'all_user_requirements_completed':False,'rounds':rounds},ensure_ascii=False,indent=2)+'\n')
inventories=[]
for r in (1,2,3):
 files=[]
 for p in sorted((R/'kaggle/source').rglob('*')):
  if not p.is_file() or any(v in p.parts for v in ('state','target','__pycache__')) or p.name=='gateway':continue
  b=p.read_bytes()
  if p.suffix=='.py':ast.parse(b)
  files.append({'path':str(p.relative_to(R/'kaggle/source')),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
 inventories.append({'round':r,'topic_review':f'KAGGLE_STEP16_REVIEW{r}.md','read_hash_ast_only_not_semantic_proof':True,'files':files})
(H/'review-final.json').write_text(json.dumps(inventories,ensure_ascii=False,indent=2)+'\n')
print(dict(counts))
