"""Assemble completed stage18 memos without overwriting the frozen stage17 handoff."""
from pathlib import Path
import re, hashlib, json
R=Path(__file__).resolve().parents[3];D=R/'docs';H=Path(__file__).resolve().parent
old=(D/'KAGGLE_HANDOFF_PROMPT.md').read_text()
names=re.findall(r'^## 内嵌备忘录：(\S+)$',old,re.M)
assert len(names)==len(set(names))==57
for name in ['KAGGLE_STEP18_PLAN.md','KAGGLE_STEP18_REVIEW1.md','KAGGLE_STEP18_REVIEW2.md','KAGGLE_STEP18_REVIEW3.md','KAGGLE_STEP18_AUDIT.md','KAGGLE_STEP18_QUICKSTART.md']:
 if (D/name).exists():names.append(name)
assert len(names)==len(set(names))
header=f'''# 第十八阶段完整交接提示词（进行中）

## 当前优先状态

当前活动分支arena/03d65d8e-kagglee，基于已合并17；原始–17与正式工作台冻结。以下历史首页不是本阶段完工声明。当前累计内嵌{len(names)}份完整备忘录，包括原57份及本阶段已完成文件。

用户新截图运行17，41.6秒录音成功建档142.3秒，输入RMS约-47.7dBFS/peak0.011，有#0/#1/#2。现在重点是更快实际首声、全部候选的校准/条件作用明确、无沙沙、自然连续朗读；不能把全部候选参与统计说成模型同时融合三参考。不能由截图定噪声根因，不能播放参考PCM增加相似。

当前完成：基线53资产逐字节/76旧冻结哈希/15正式文件核对；第一/第二轮关键路径各100建议；12种case的NumPy DSP基线三轮、20种case的参考条件与状态控制流三轮；Node30与JS/repack检查。没有完成全源三轮语义审查。没有产品代码改动、没有18发布包、没有真实语音模型/GPU实验。

基线发现：NumPy短块淡入依赖分块；同半秒双音target=-6/maxgain0，48样本分块与整块最大差1424 int16；正常AGC1920样本分块差8。三轮一致，见dsp-partition-baseline-round1..3.json。它证明工程分块依赖，不证明用户沙沙根因或真实听感；Rust仅源码对照，未编译执行。

第二轮实际接口核验：Faster0.5.4+qwen-tts-hf0.1.1.post1支持独立批量prompt，不支持把三个列表提示自动融合给单目标；真实resolver拒绝长度不匹配。最初误查旧发行版qwen-tts==0.1.1.post1失败后按pins纠正，只下载解包，未安装旧版/未改变产品依赖。wheel URL/hash与抽取函数来源收据完整保存。

第二轮受控复现：候选bool/小数强转、null/容器未捕获异常；ASR全失败默认CER0.05；校准期间转写更新导致旧评分提交未经该轮评估的新转写；加载失败回执被忽略；全合成失败仍chosen0；双卡诊断同文seed100/101不同（正式播放同会话seed原本相同，必须保留）。三轮每轮20项，外部模型/网络显式fixtures，确定性交错不是HTTP/线程压力测试。未修复，不推断用户噪声根因。

下一步第三轮数值/时序及其余模块100建议；完成后再按问题25起逐题自问自答，每题50实施建议后才能下一题，形成最终方案后才改产品。200条专题建议不代表200个bug或全源三轮完成，不要跳过用户要求先修DSP。

持续中文短进度，不向用户提问，不承诺100%信心/零错误/零噪声。整体PARTIAL/BLOCKED，历史真实RTF0.3/训练闭环/长数据覆盖/声学逐字拒播缺口保留。当前环境只重建NumPy2.2.6到忽略目录.venv，无Torch/完整权重/CUDA证据，旧17收据不是本阶段重新执行。

## 历史首页（仅历史，上述当前状态优先）

'''
history=old.split('\n## 内嵌备忘录：',1)[0].rstrip()
if history.endswith('---'):history=history[:-3].rstrip()
content=header+history+'\n\n---\n\n'+'\n\n---\n\n'.join('## 内嵌备忘录：'+n+'\n\n'+(D/n).read_text().rstrip() for n in names)+'\n'
for name in names:
 body=re.search(r'^## 内嵌备忘录：'+re.escape(name)+r'\n\n(.*?)(?=\n\n---\n\n## 内嵌备忘录：|\Z)',content,re.M|re.S)
 assert body and body.group(1).strip()==(D/name).read_text().strip(),name
p=D/'KAGGLE_STEP18_HANDOFF_PROMPT.md';p.write_text(content)
receipt={'completed_memos':len(names),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'all_embedded_memos_match_source':True,'stage18_complete':False,'product_modified':False,'real_model_executed':False}
(H/'handoff-progress.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
