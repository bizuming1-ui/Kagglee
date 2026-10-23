from pathlib import Path
import re,json
R=Path(__file__).resolve().parents[3];D=R/'docs';H=Path(__file__).resolve().parent
assert '369 passed (' in (H/'browser-repeat3.txt').read_text()
assert '3 passed (' in (H/'final-copy-repeat3.txt').read_text()
for r in (1,2,3):assert re.search(r'Ran 334 tests in [\d.]+s\n\nOK\s*$',(H/f'python-round{r}.txt').read_text())
p=D/'KAGGLE_STEP17_AUDIT.md';v=p.read_text().replace('工程修复已实现，最终三轮验证进行中；','工程修复及最终三轮回归通过；').replace('最终Python334项×3进行中；','最终Python334项×3=1002通过；').replace('Node、Go race、六服务协议、完整Chromium三轮、最终copy页/下载/拒绝回退/手机进行最终核对。','Node30×3=90、Go race3、六服务协议各三轮、完整Chromium123×3=369、最终整包复制另3、copy页/下载/拒绝回退/手机3均通过。');p.write_text(v)
p=D/'KAGGLE_HANDOFF_PROMPT.md';old=p.read_text();names=re.findall(r'^## 内嵌备忘录：(\S+)$',old,re.M)
for name in ('KAGGLE_STEP17_REVIEW1.md','KAGGLE_STEP17_REVIEW2.md','KAGGLE_STEP17_REVIEW3.md','KAGGLE_STEP17_PLAN.md','KAGGLE_STEP17_AUDIT.md','KAGGLE_STEP17_QUICKSTART.md'):
 if name not in names:names.insert(names.index('KAGGLE_TARGET_ACCEPTANCE.md'),name)
assert len(names)==len(set(names))==57
history=old.split('\n## 内嵌备忘录：',1)[0].rstrip()
if history.endswith('---'):history=history[:-3].rstrip()
if '## 当前第十七阶段优先' in history:history=history.split('## 历史交接首页（step16及更早）\n\n',1)[1]
header='''# 完整交接提示词：Kaggle双T4 Qwen3-TTS语音克隆聊天

## 当前第十七阶段优先：长录音建档对齐/长短参考实验/生成参数绑定/连续朗读

用户截图是15，28.7秒/RMS约-46.6dBFS/peak0.014，创建报no aligned 2.5–16 s。要求超15秒录音可建档、超长与10秒参考都要更像、无噪声沙沙、双卡音色参数一致、自然完整朗读。先3轮100建议、逐题自问自答每题至少50建议、具体方案后小步实现、3轮检查/模型模拟、完整代码与全部备忘录。中文频繁进度，不向用户提问。不保证100%身份/正确/零噪声，不能凑语言或伪造硬件验收。

1. 最新完整包`kaggle/kaggle-fixed-step17.py` **313504B/53资产/SHA256 6eacaede14f9b5f42ac5c334df5c3f9d1a1c6858fb69b7d3a8ff241ec60427ea**。原始至16冻结，16最终306580B/SHA c6ed6c89e6356fc6c7ab554f96a2c3201a8e4690c007ea66626445cc658b4429。repack默认17；3001固定17完整复制/下载，正式3000的15文件/HEAD保持不改。截图15必须完整重启Kaggle部署17，刷新旧页面无用。
2. 三轮专题建议各100、全源读取/AST/哈希不是穷尽语义证明；问题22→23→24各50建议后实施，累计24题1200建议。57份完整备忘录内嵌。处置93新动作/174保留回归/27文档边界/6真实试听硬件阻塞，不把300建议当300bug或全新功能。
3. 确认根因：长录音限额不是15秒，旧候选只接完整2.5–16秒ASR段而丢弃已有words；单28.7秒段无候选。新reference_segments校验有限/单调/源范围和Unicode词文一致，按完整词切长段；缺时间或不一致就对实际音频窗口重ASR，优先低能边界，恢复绝对时间，不按字数/时长分配全文。短段无效word元数据移除但保留有效段转写；ASR仍非人工真值。
4. 快速建档/库处理/UI都有16默认、24实验参考窗口，手工文本只对单个≤所选窗口录音直用；长manual全文不强对齐，走ASR时间戳并记录策略。候选补边不超窗口，quality.reference_context记源总时长/锚点时长/all_audio_used_as_model_prompt=false/model_trained=false；quality.asr[].alignment记切分/重识别/短尾。长采集完整分析择锚，不等于20分钟全部ICL或训练，更长不保证更像/更快。
5. 原始PCM非有限拒绝，记录归一化前RMS/峰值，<-40dBFS风险提示进入已有decision显示；不是仅从截图判断无语音/设备坏。输入太轻归一化也放大底噪，检查距离与输入增益。保留16 ICL匹配转写、生成码专用codec、提示内存快照、禁参考PCM/呼吸拼接、默认增益6/目标-18与软限幅；不默认强低通或跨词重叠冒零沙沙。
6. 指纹升级qtts-voice-v2：参考WAV/UTF8文本/语言+四有效生成参数temperature/top_k/top_p/repetition_penalty，长度前缀和little-endian4 doubles。显式默认与缺省相同，拒绝NaN/Inf/非法/非整数top_k。同会话pin/模式/seed固定，Worker锁内复核、旧会话/混版本必须停后重启，不静默混旧参数。但相同条件不保证跨GPU逐位波形或声学100%一致。
7. 只朗读ReadSegCfg适度扩大聚合FirstMin12/FirstMax24/Min20/Target40/Max80，减少独立合成韵律重启；保留全文/标点/取消/背压/顺序，不跨词叠加PCM。不改Live聊天首句早触发。可能增加朗读首段等待/减少并行，不声称已经真实更自然或提速。codec仍25帧左上下文、默认右前瞻0。
8. 最终工程验证：Python334×3=1002、Node30×3=90、Go race3、六协议脚本各三轮；Chromium123×3=369、最终17完整复制另3、独立copy页剪贴板/下载/拒绝回退/手机3通过。新12项含28.7/60/1200秒对齐、缺词实际窗口、非法词时、16/24、低输入提示、参数pin。20分钟是时间戳规划，不是实际20分钟人声验收。
9. 冻结16真实build函数控制流vs17对照三轮：同29秒合成PCM、28.7秒ASR词段，16复现no aligned，17建档成功；实际读回24k候选WAV帧数≤16秒；缺词重识别窗口样本总数完整。ASR/说话人明确fixtures，不是真实Whisper。实际Faster0.5.4 resolver/prepare+生成码decoder三轮仍为CPU prompt/talker/kernel/codec fixtures；真实23813参数随机tiny codec三轮、完整Qwen导入/tinyMimi2651保存重载三轮、CPU tinyLoRA相对冻结13损失/全部adapter逐位同且6步骤三轮。都不是完整训练权重或GPU音质证明。
10. 初始失败保留：旧to16k测试替身把24k除2成12k，被新增边界校验拒绝，改测试真实2/3样本比，不放宽生产校验；固定跨语言hash从v1更新v2；旧长段一律拒绝断言改成不可信窗口不配全文；studio临时编辑脚本对字符串write_text失败后正确追加；长参考基线日志stdout污染初次JSON，导向stderr后重做三轮；低输入提示最终进入decision并新增第334项，完整重跑三轮。文件均在validation/step17。
11. **整体仍PARTIAL/BLOCKED**。没有用户实际WAV、Whisper/Qwen训练权重、CUDA/T4/DeepSeek可用通路，不声称短/长参考高相似、零噪声、双卡音色完全相同、自然整段或RTF≤0.3已达。真实基准tools/voice_benchmark.py仍可调用驻留双Faster三轮18条WAV/JSONL，无填充speech分母、worker与wall RTF各判，>0.3失败；本沙箱零真实测量target-rtf-not-run blocked，CPU/Mock不代替。历史网页真实训练闭环/维护租约切换/长数据审核对齐全覆盖/真实训练吞吐/声学逐字拒播缺口保留，完整目标22/300不升级。
12. 操作按STEP17_QUICKSTART：备份→完整重启双T4/Internet/nonMock/faster→完整17→双ready→录长音/选择16或24窗口→审核单人锚点与匹配转写→同源10/16/24秒三轮真机对照→逐GPU同文WAV与长文试听→播放首声/欠载/RTF另测。只问自己，不问用户，不删除锁/盲杀/卸载Torch，不默认每卡第二模型，不无依据重写稳定模块或新增语言服务。

以下step16及更早全部为历史；冲突以本段、STEP17_AUDIT及最终收据为准。

'''
p.write_text(header+'## 历史交接首页（step16及更早）\n\n'+history+'\n\n---\n\n'+'\n\n---\n\n'.join('## 内嵌备忘录：'+n+'\n\n'+(D/n).read_text().rstrip() for n in names)+'\n')
print('57 complete memos',p.stat().st_size,'bytes')
