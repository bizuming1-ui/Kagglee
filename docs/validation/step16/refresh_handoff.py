"""After final evidence, embed all 51 complete memo bodies; preserve old header as history."""
from pathlib import Path
import re
R=Path(__file__).resolve().parents[3];D=R/'docs';H=Path(__file__).resolve().parent
p=D/'KAGGLE_HANDOFF_PROMPT.md';old=p.read_text()
assert '363 passed (' in (H/'browser-repeat3.txt').read_text()
assert '3 passed (' in (H/'final-copy-repeat3.txt').read_text()
for r in (1,2,3):assert re.search(r'Ran 322 tests in [\d.]+s\n\nOK\s*$',(H/f'python-round{r}.txt').read_text())
a=D/'KAGGLE_STEP16_AUDIT.md';s=a.read_text().replace('**工程修复候选已实现，最终三轮回归进行中；整体PARTIAL/BLOCKED，绝不声称真实相似度、无沙沙或T4 RTF0.3已经达到。**','**本轮工程修复及最终三轮回归已通过；整体PARTIAL/BLOCKED，绝不声称真实相似度、无沙沙或T4 RTF0.3已经达到。**').replace('## 验证（最终执行收据待写入）','## 最终验证').replace('- Python完整322项已通过初次最终策略验证；最终三轮重跑中。','- Python完整322×3=966项最终通过（37.320/39.911/43.420秒）；原子ready夹具修正后重跑。').replace('- Node/Go race/完整Chromium/六协议脚本最终轮进行中。','- Node30×3=90、Go race count3、六协议脚本各内置3轮通过；完整Chromium121×3=363通过，最终step16完整复制额外3通过，独立复制页剪贴板/下载/拒绝回退/手机3通过；初始360通过/3旧版本文案失败日志保留。')
a.write_text(s)
names=re.findall(r'^## 内嵌备忘录：(\S+)$',old,re.M)
for name in ('KAGGLE_STEP16_REVIEW1.md','KAGGLE_STEP16_REVIEW2.md','KAGGLE_STEP16_REVIEW3.md','KAGGLE_STEP16_PLAN.md','KAGGLE_STEP16_AUDIT.md','KAGGLE_STEP16_QUICKSTART.md'):
 if name not in names:names.insert(names.index('KAGGLE_TARGET_ACCEPTANCE.md'),name)
assert len(names)==len(set(names))==51
history=old.split('\n## 内嵌备忘录：',1)[0].rstrip()
if history.endswith('---'):history=history[:-3].rstrip()
header='''# 完整交接提示词：Kaggle双T4 Qwen3-TTS语音克隆聊天

## 当前第十六阶段优先：相似度取舍修正/单一参考版本/底噪风险/真实RTF0.3门禁

用户报告克隆根本不像、偶尔两种声音、沙沙声，要求真实RTF≤0.3。中文小步进度，不向用户提问；先3轮100建议与逐题自问自答，每题后50建议，再方案、增量实现、3轮完整验证、保存全部备忘录。不能保证100%身份/正确/自然度/速度，不凑多语言。

1. 最新完整包`kaggle/kaggle-fixed-step16.py` **306580B/52资产/SHA256 c6ed6c89e6356fc6c7ab554f96a2c3201a8e4690c007ea66626445cc658b4429**。原始–15冻结；15最终SHA61c063f0b2053321bfeafc8509bbbc1c91be183da72739186f7e5c4bf1899d43。repack默认16，3001固定hash完整复制/下载；正式3000的15文件/HEAD保持。
2. 三轮专题审查各100、问题19→20→21各50，累计21题1050建议；51份完整备忘录内嵌。全源哈希/AST不是穷尽语义无错。处置161新动作/53保留/49文档边界/32硬件试听阻塞/5未实施或否决，不当300个bug或300项全部实施。
3. 15强制纯向量可能牺牲相似度，不能假定正确。16默认有匹配转写的ICL，仅作为talker参考条件；decoder只接新生成码，绝不参考码或参考PCM。无转写拒绝，显式QTTS_CLONE_MODE=xvector仍可选。目标文字与参考转写分开，ICL仍可能音素/文字幻觉，严格声学拒播尚无。
4. 参考WAV+UTF8匹配文本+语言采用长度前缀SHA256，Go/Python互操作；会话每段携带同pin和conditioning模式、同seed。Worker取合成锁后重读档案检查版本/模式，在任何lead或PCM前拒绝不符。activation核对双卡收据并再次读版本；文本/候选部分reload失败返回503/reference_saved，不能宣称全卡ready。已播旧段不能撤回。
5. Faster0.5.4路径键不识别同路径音频替换，reload清该路径旧键；预计算提示保存内存快照，生成传voice_clone_prompt而非重新读取可覆盖锚点。提取前后内容指纹一致才发布；dtype重载清提示，后续需重建。原生训练adapter仍走受检句级缓冲路径，不回退Base；gateway按sentence-buffered发布类型固定native条件模式。
6. codec固定16码组/24k/1920样本每帧，契约不符明确失败；25帧左上下文、有界窗口，不全历史cat，不比例裁参考。仅输出未提交样本；尾flush幂等、取消无迟到PCM。最初拟2帧前瞻，实际Qwen12Hz因果源码/真实23813参数tiny随机decoder的8→12帧前缀误差0后改默认0；QTTS_CODEC_LOOKAHEAD_FRAMES=2仅显式实验，不能假装真实沙沙根因已知。
7. 输出目标仍-18dBFS，默认最大增益6（显式0..12，非法回6），每任务重建leveler/DC/包络，保留Rust/NumPy软限幅/淡入淡出；空生成不flush旧声尾。低噪声放大风险改善不等于声学降噪已验，轻声可能比15上限12稍轻；不默认强低通/谱门伤清辅音。用户未供实际噪声音频，不能精确确认所有声学根因。
8. tools/voice_benchmark.py显式--run，调用已有真实双Faster worker而非第三模型；空闲、ready、ICL生成码模式、物理GPU0/1独占。参考预热单列，3轮×2卡×3文=18条，保留私有WAV与逐条JSONL；标准RTF=gen_wall/未填充语音秒数，另HTTP wall RTF，排除lead/tail/fade、失败/取消/anomaly。任一条>0.3即target-not-met，达标仍仅measured-speed-only、音质待听。当前沙箱零真实测量、target-rtf-not-run.json blocked，不把CPU/Mock/双卡相加/改语速/填静音当0.3。
9. 最终工程证据：Python322×3=966，Node30×3=90，Go race3，六协议脚本各三轮；Chromium121×3=363，最终整包复制额外3，独立copy页剪贴板/下载/拒绝回退/手机3。真实Faster resolver/prepare+生产generated-only decoder三轮，每轮ICL/xvector×chunk2/4/8/12、80帧153600样本，参考标记从不进codec、同路径提示正确更新，但prompt/talker/kernel/codec为明确CPU fixtures。实际tiny随机Qwen12Hz decoder23813参数三轮、每轮8组合/40帧76800样本；不是训练codec或完整TTS。完整Faster/Qwen导入/tinyMimi2651参数保存重载三轮；CPU tinyLoRA相对冻结13损失和全部adapter张量逐位相同、6步骤三轮；真实HF smoke/API检查pass但无CUDA整体blocked。
10. 初始失败全部保留：旧15策略/接口/未重打包断言；native adapter测试实际注入引擎与Mock/faster模式误推断，按发布类型修正后A-B-A与损坏adapter拒播通过；测试ready文件先创建后写PID被并行父进程读空，测试夹具改原子rename且启动前记录旧run，不放宽锁释放；浏览器360通过/3同旧“第十五阶段”文案断言失败，改16并新增ICL/待测声明，定向3后完整363+复制3通过。不能把这些初始失败藏掉。
11. **整体仍PARTIAL/BLOCKED**：无用户实际音频/完整训练权重/真实T4/DeepSeek，不能声称高相似/单一音色/无沙沙/真实RTF≤0.3已验。历史网页训练CPU控制面闭环、维护租约切换、长录音审核对齐/全样本覆盖、真实双T4保质训练吞吐、声学逐字拒播仍缺；完整目标22/300不升级。两T4各一模型不改，不默认每卡两模型，不无依据换语言重写稳定模块。
12. 实机按STEP16_QUICKSTART：备份→完整重启Kaggle→T4×2/Internet/nonMock/faster→完整16→双ready→审核单人锚点及逐字匹配转写→重新启用→不同正文直接朗读/长文跨卡试听→真实基准18条→DeepSeek首句/播放first_played/欠载。bootstrap返回后可用后续Notebook单元格跑CLI。不给密钥、不删锁、不盲杀或卸载Torch；Kaggle配额和会话永久性不能承诺。

以下step15与更早均为历史，冲突时以本段、STEP16_AUDIT及最终final-checks.json为准。

'''
# Keep the previous header too, explicitly historical; avoid repeatedly nesting on refresh.
if '## 当前第十六阶段优先' in history:
 history=history.split('## 历史交接首页（step15及更早）\n\n',1)[1]
p.write_text(header+'## 历史交接首页（step15及更早）\n\n'+history+'\n\n---\n\n'+'\n\n---\n\n'.join('## 内嵌备忘录：'+n+'\n\n'+(D/n).read_text().rstrip() for n in names)+'\n')
print('51 complete memos',p.stat().st_size,'bytes')
