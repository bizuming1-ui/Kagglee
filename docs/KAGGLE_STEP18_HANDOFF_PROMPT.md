# 第十八阶段完整交接提示词（进行中）

## 当前优先状态

当前活动分支arena/03d65d8e-kagglee，基于已合并17；原始–17与正式工作台冻结。以下历史首页不是本阶段完工声明。当前累计内嵌60份完整备忘录，包括原57份及本阶段已完成文件。

用户新截图运行17，41.6秒录音成功建档142.3秒，输入RMS约-47.7dBFS/peak0.011，有#0/#1/#2。现在重点是更快实际首声、全部候选的校准/条件作用明确、无沙沙、自然连续朗读；不能把全部候选参与统计说成模型同时融合三参考。不能由截图定噪声根因，不能播放参考PCM增加相似。

当前完成：基线53资产逐字节/76旧冻结哈希/15正式文件核对；第一/第二轮关键路径各100建议；12种case的NumPy DSP基线三轮、20种case的参考条件与状态控制流三轮；Node30与JS/repack检查。没有完成全源三轮语义审查。没有产品代码改动、没有18发布包、没有真实语音模型/GPU实验。

基线发现：NumPy短块淡入依赖分块；同半秒双音target=-6/maxgain0，48样本分块与整块最大差1424 int16；正常AGC1920样本分块差8。三轮一致，见dsp-partition-baseline-round1..3.json。它证明工程分块依赖，不证明用户沙沙根因或真实听感；Rust仅源码对照，未编译执行。

第二轮实际接口核验：Faster0.5.4+qwen-tts-hf0.1.1.post1支持独立批量prompt，不支持把三个列表提示自动融合给单目标；真实resolver拒绝长度不匹配。最初误查旧发行版qwen-tts==0.1.1.post1失败后按pins纠正，只下载解包，未安装旧版/未改变产品依赖。wheel URL/hash与抽取函数来源收据完整保存。

第二轮受控复现：候选bool/小数强转、null/容器未捕获异常；ASR全失败默认CER0.05；校准期间转写更新导致旧评分提交未经该轮评估的新转写；加载失败回执被忽略；全合成失败仍chosen0；双卡诊断同文seed100/101不同（正式播放同会话seed原本相同，必须保留）。三轮每轮20项，外部模型/网络显式fixtures，确定性交错不是HTTP/线程压力测试。未修复，不推断用户噪声根因。

下一步第三轮数值/时序及其余模块100建议；完成后再按问题25起逐题自问自答，每题50实施建议后才能下一题，形成最终方案后才改产品。200条专题建议不代表200个bug或全源三轮完成，不要跳过用户要求先修DSP。

持续中文短进度，不向用户提问，不承诺100%信心/零错误/零噪声。整体PARTIAL/BLOCKED，历史真实RTF0.3/训练闭环/长数据覆盖/声学逐字拒播缺口保留。当前环境只重建NumPy2.2.6到忽略目录.venv，无Torch/完整权重/CUDA证据，旧17收据不是本阶段重新执行。

## 历史首页（仅历史，上述当前状态优先）

# 完整交接提示词：Kaggle双T4 Qwen3-TTS语音克隆聊天

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

## 历史交接首页（step16及更早）

# 完整交接提示词：Kaggle双T4 Qwen3-TTS语音克隆聊天

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

## 历史交接首页（step15及更早）

# 完整交接提示词：Kaggle双T4 Qwen3-TTS语音克隆聊天

## 当前第十五阶段优先：参考隔离/首句/增响/创建复用，真实T4音色与提速仍未验收

用户报告step14播放克隆语音插入参考原音、创建档案256.4秒，要求不播放任何参考片段、DeepSeek首段及时合成、提高输出音量和创建速度，询问单T4双1.7B。截图没有原音频，不能确定具体声学根因；不问用户问题，中文小步进度，不能100%无错或凑多语言。

1. 当前完整包`kaggle/kaggle-fixed-step15.py` **291325B/48资产/SHA256 61c063f0b2053321bfeafc8509bbbc1c91be183da72739186f7e5c4bf1899d43**。原始至14冻结，repack默认15；独立3001固定15完整复制/下载，正式3000的15文件与HEAD不动。
2. 三轮专题代码研究各100建议、全源读取/哈希/AST不等于语义无错。问题16→17→18每题50建议后实施，累计18题900建议；45份完整备忘录内嵌。处置逐条区分修改/保留/文档边界/硬件待测/未实现，不把300建议当300bug或900实现。
3. 实际Faster0.5.4源码ICL会将ref_codes带入codec上下文再裁参考，xvec_only说明防参考phoneme bleed-through。Worker加载、dtype回退预热和生成统一xvec_only=True/ref_text为空/append_silence=False；不提供ICL环境回退。旧breath_files不读取，reference环境也不能启用拼接，lead仅零停顿。模型自身呼吸保留；stats reference_pcm_splicing=false是代码政策，acoustic_text_verified仍false。向量模式可能改变韵律/音色相似度，未做真实试听，不能称质量无损或保证不幻觉。
4. Go仅聊天LiveSegCfg首句完整边界就提交，不等待下一delta；短完整中文句可提交、尾空格处理，ASCII小数点/未闭合引号仍有lookahead。普通朗读ExactSegCfg、后段、顺序/背压/取消/播放器稳定水位不改。不是每个token生成，也不保证<3秒。保留chunk默认4，2..8显式试验。
5. 共享output_target_dbfs默认-18，合法-24..-14，非法/非有限回退-18；Worker新旧档案均最大增益12dB（旧9），保留Rust/NumPy软限幅/DC blocker/平滑/淡入淡出，源录音不改。小信号合成测试较响，不代表全部硬件或语音恰好+3dB。
6. 创建/库处理/UI锁定重置/后端缺省均不追加可选GPU校准，手动入口与勾选仍在；CPU ASR允许复用，QTTS_ASR_KEEP_CPU=0关闭，CUDA仍卸载；ASR RLock覆盖加载/惰性转写迭代/释放，避免诊断与创建并发释放模型。保留全量ASR/beam5/24候选/打分/准确最佳F0。嵌入缓存按样本hash、只本任务最多64条，不跨档案持久化。
7. 创建保存最终quality.build_s/stage_ms/embedding_cache、界面可展开，重新读校准后profile避免覆盖选择。修复“截14秒配全文”，只用完整2.5–16秒对齐回退片段；16秒手动全文不截14秒。超长ASR段无可信切分明确拒绝，不猜对齐。冷下载/CPU大ASR仍可能慢，无用户原录音A/B，不说256秒已降到多少。
8. 单1.7B FP16纯参数约3.4GB、两份6.8GB不含codec/KV/graphs/临时张量；同T4共享计算带宽，装下不等于单请求快。不默认每卡双副本，继续两卡各一模型，峰值/吞吐须真实T4测。
9. 工程验证：Python301×3=903（ASR并发修复后重跑通过）、Node30×3=90、Go race3、6协议脚本各含3轮；真实Faster resolver→prepare→两阶段streaming控制流三轮，每轮chunk2/4/8、40帧76800样本、decoder无参考码，但prompt/talker/codec是明确CPU注入fixture，不是完整Qwen。完整Faster/Qwen import及2651参数tiny Mimi构造保存重载3轮、required HF CPU smoke3轮通过，整体无CUDA仍blocked。完整Chromium120×3=360通过（10.5分钟），最终整包复制另3通过，独立复制页剪贴板/下载/权限拒绝/手机3通过。原初次357通过/3等义提示文案断言失败保留，断言兼容“执行”两种写法后完整重跑通过。最终以step15/final-checks.json为准。
10. 新测试初始低音量同9dB上限无增响，改worker最大12并保留限幅；Go夹具直接读Session.jobs早于enqueue导致race，改真实队列pickLocked后race3通过；ASR惰性迭代需全周期锁的复核修复已补并发回归；日志目录未建导致初次安装重定向失败，已恢复。错误不隐去。
11. **整体PARTIAL/BLOCKED**：真实Qwen/T4参考重播/音色/韵律/首播/创建A/B未验收；历史独立CPU网页训练控制面/维护租约移交/实际start-cancel-progress-restore-publish、长录音审核对齐/超过16样本全覆盖、真实训练保质吞吐、声学逐字拒播仍缺，完整目标22/300不变。不能把部分交付当需求豁免。
12. 用户操作见STEP15_QUICKSTART：备份私有数据→完整Kaggle会话重启→T4×2/Internet/nonMock/faster→复制15→等双worker ready→已有普通档案重启用→不同于参考的目标文本直接朗读试听→再试DeepSeek首句；不要删锁、盲杀PID或卸载Torch。Kaggle配额/会话驻留不保证永久。

下面第十四阶段及更早内容均为历史，冲突时以本段与STEP15_AUDIT/最终收据为准。

## 当前第十四阶段优先：部分功能修复，不能冒称全部需求完成

用户新增十多分钟网站录音、点击真实训练/保质最快、多线程、自然呼吸、首声、准确逐字播放要求；不要问用户重复问题。先三轮审查各100条（REVIEW1/2/3），再顺序问题13/14/15各50建议，已落盘PLAN后实施。15题750建议，完整目标22/300不变，39完整备忘录内嵌；语言分工仍Python/PyTorch+CUDA、Go、Rust、浏览器JS，不为语言数量引入新系统。

1. 最新kaggle/kaggle-fixed-step14.py，285094B/48资产，SHA256 73a02a95919406c4570ea563f0c0475fdde17535e6ccd16764c32514fce2c369。原始至13冻结，repack默认14；3001只读复制页切14，3000正式15文件/HEAD不动。
2. 用户随后提供step13真实Kaggle日志：HF RoPE required pass、两T4加载/预热ready、190s、Rust on、公开隧道完成，SystemExit0只是包装器正常退出。记录step13/user-runtime-startup-ready.json，不能继续说双卡启动未知；但没有真实音频合成/训练/音质证据。
3. 浏览器录音1199000ms、8192 chunks、64MiB单文件/127MiB本地合计；Python/Go请求128MiB，服务端1200秒/1800秒合计。原始库64MiB/库/512MiB总量仍独立限制，高码率WAV可能先到字节上限。11分钟虚拟控制/2640块及660秒合成PCM解码完整验证，不是物理麦克风实验。
4. TTSDataset有界64MiB CPU张量缓存与调用者来源deepcopy/返回clone；不变loss/数据顺序/优化器/步数。grad finite合并host读取、保留collective与clipping。run_rank记录cache/tokenize指标，HF版本报告不再只查官方qwen-tts。
5. frozen13真实训练/数据源与14做CPU tiny LoRA A/B，三进程×三epoch，每次6optimizer步，loss与全部adapter tensor逐位一致，tokenizer12→3。fixture墙钟有冷启动/顺序偏差，不能写真实训练倍速、质量更好或最快。
6. 实际newSession用ExactSegCfg，不再CleanDelta删正文/补句号；保留多delta内容，纯标点/空白片段旧过滤仍在，不保证模型声学无漏添字。没有ASR核验拒播闭环，不要称“播放每字完全核验”。
7. 默认QTTS_BREATH_MODE=off，不后加呼吸；reference只用真实bank，空bank不生成噪声。模型自身呼吸没盲滤，主观自然度仍需试听。first_chunk_ms为裁边后非空PCM，model_first_chunk_ms是模型首块；runaway静音可能仍放行，不是ASR确认人声。first_played/欠载另测。QTTS_FIRST_CHUNK_SIZE=2可实验（2..8），默认4/稳定播放器阈值不变，首声未证明改善。
8. **网页真实训练仍未闭环**：快照/参考处理不执行优化器，未添加假训练按钮。现有真实双rank CLI保留，但网页要独立CPU控制面、维护态停止两GPU/analyst且保留网关、验证租约交接、固定审核数据/Base/码、实际训练/取消/进度/恢复/候选发布。不能在analyst开线程绕过fleet锁，也不能把十分钟当单条SFT或均分文本猜对齐。现有训练快照仍最多16条，长数据分片/manifest及全部样本覆盖亦需扩展；不得只取前16条冒充全量入训。下一核心应做这条闭环，不是再加准备工具。
9. 本阶段全部用户需求状态PARTIAL/BLOCKED：缺真实长音频审校、独立网页控制面、真实Qwen/T4训练/音质/首播/声学逐字验收。三轮回归只覆盖实现范围：Python285×3=855、Node90、Go race3、五协议各3、fatal控制3通过；浏览器117×3=351通过（10.4分钟），最终包复制另3通过，独立剪贴板/下载/手机/拒绝权限三轮通过。结果见step14/final-checks.json；不输出100%或全部成功。HF实际包与微型Mimi CPU回归保护13成功路径，不是完整Qwen/GPU验收。
10. 操作见STEP14_QUICKSTART：先备份私有数据，停止并重启完整Kaggle会话，再T4×2/Internet/nonMock默认faster复制14。不要删锁/按旧PID杀；API口令不公开。健康会话内resident保留，Kaggle配额/超时不可保证永久。原生adapter仍sentence-buffered，真实训练/重载/声音边界保留。

---


## 第十三阶段历史：已获用户双T4 ready日志，新增目标以14为准

用户step12真实Kaggle仍在两个T4上报同一MimiConfig.rope_theta；不要怪用户、不要说上次已修好。下面12及更早记录为历史，当前以本段/STEP13审查/最终收据为准。不问重复问题，中文小步进度，继续同一arena/041344f2-kagglee分支。

1. 最新完整kaggle/kaggle-fixed-step13.py为282346B/47资产，SHA256 dad142d75be94d8efb6567fc1f8755d3f37341a65d5c7fe9454fd36c87770e60。原始至12冻结，尤其12为282031B/SHA2be33a3a6735639ce32ec8750e9a489abd96e4daa780d068557f2b0156f2de08；repack默认13，不能改旧包伪造成功。
2. 真实faster0.5.4 wheel model.py第194行在from_pretrained才导入qwen_tts；顶层只导出包装类。step12只看sys.modules，误把尚未导入当not_applicable。之前手动exec真实wheel函数的数学验证没有覆盖生产入口生命周期，是我们的漏测，当前已真实复现。
3. qwen_compat现在按已安装发行元数据选HF/legacy，先检查HF0.1.1.post1/TF5.20.2和namespace冲突，再正常importlib.import_module导入实际compat及父包，注册完成后安装窄范围bridge；未知组合/导入失败/矛盾元数据拒绝。官方legacy无HF仍不适用。未猜theta、未改权重或config、未改平台Torch/CUDA约束、未全局接管Python导入。
4. backend_probe HF数学smoke必须installed且configuration_smoke_passed=True；HF存在却跳过/不完整时required blocked，不再warning后surface_pass。只有HF发行真不存在的legacy可warning不适用。Worker/native/CPU编码/训练继续共用同一函数并在构造模型前安装。Resident/fatal/nonce/ownedPopen清理原样保留。
5. 实际完整Faster/Qwen包隔离缓存正常导入，不mock第三方导入。冻结step12函数先返回not_applicable，再导入Qwen+构造真实微型Mimi复现相同AttributeError。新函数从同一冷状态installed，真实TF微型MimiModel2651随机参数构造/保存/本地from_pretrained重载，三种theta缓冲精确对照、config不变、实际初始化进入bridge12次、幂等；三独立进程PASS。是完整包导入+微型Mimi，不是完整Qwen1.7B模型加载。
6. 额外真实隔离backend_probe CLI三次：HF smoke required PASS，但无CUDA所以整体blocked，不能把该证据写成GPU预检成功。证据在real-preflight-cpu-round1..3.json；网络被禁止，不下载完整模型。主venv未污染，隔离站点/home/user/.cache/qtts-step13-site与step12-site，轮子在qtts-wheelhouse，不入Git。
7. Python273×3=819PASS，Node30×3、Go race count3，四协议脚本各三次内置三轮共9轮，adapter三轮、fatal真实supervisor CPU worker三轮已PASS。完整浏览器114×3=342PASS（11.4分钟）；最终整包复制另3PASS；独立真实剪贴板/下载/手机/授权拒绝回退三轮PASS；最终门禁见step13/final-checks.json。新增6兼容回归；初始隔离缺依赖、测试断言假设旧接口、旧CPU替身伪造所有发行元数据而触发冲突均保留初始日志，生产门禁没有削弱。
8. 三轮各100条定向建议见review-map；完整目标仍22/300，12题600建议不等于600实现。交接嵌33个完整备忘录。3001只读复制页已切13，原3000工作台15文件1043155B及HEAD39ed7670-ec8a-4565-a1ae-fff0064d5246保留。用户要真实复制按钮，不要只报文件路径。
9. 用户实际现场已确认两个T4、每卡15636037632B/CC7.5、Python3.12.13/Torch2.10+cu128、下载与Go/Rust构建完成；截至step12两worker仍加载失败。新step13完整Qwen/T4加载/graph/显存/声音未验证，不能保证下一次一定成功。SoX二进制在CPU缓存实验缺失警告，不曾验收其音频转换；Faster/flash attention警告不等于本错误。
10. 下一步直接按STEP13_QUICKSTART：先备份需要的私有数据，平台停止并重启完整Kaggle会话（不是只重启内核或网页），T4×2/Internet/nonMock默认faster复制完整13。HF smoke必须pass；两worker真正加载/warmup完成后才验证短句/长句/停止/显存与声音。旧PID不得盲杀或删锁；平台保留旧标记时确认整个会话已重启后可新QTTS_ROOT，旧数据另行管理。不再加开发准备前置。
11. 默认每GPU一份健康模型在会话内resident，不按600次或旧13.5GB阈值主动回收，异常/OOM仍可中断。Kaggle配额/超时/回收不可由应用阻止，不承诺永久双GPU驻留；原生adapter依然sentence-buffered而非声学流，实际训练/NCCL/质量/性能仍未验收。

---


## 第十二阶段历史交付（随后实机再失败，不能沿用其修复完成结论）

2026-10-21。先STEP12计划与Q11（50建议）再实现；中文短进度，不问重复问题。仍在arena/041344f2-kagglee分支，不切换。下面第十一阶段与更早内嵌历史均服从本段。

1. 最新kaggle/kaggle-fixed-step12.py：282031字节/47资产，SHA256 2be33a3a6735639ce32ec8750e9a489abd96e4daa780d068557f2b0156f2de08，repack默认12；原始至11冻结。复制预览3001已切step12，原正式3000工作台15文件1043155B/HEAD39ed7670-ec8a-4565-a1ae-fff0064d5246不改。用户已明确要从浏览器复制，不要只让用户找文件。
2. 用户实际日志：两Tesla T4、CC7.5、每卡15636037632B、Python3.12.13/Torch2.10.0+cu128/faster0.5.4/Transformers5.20.2；下载/Go/Rust完成，但两worker加载报MimiConfig无rope_theta并重启。GPU识别有现场证据，模型加载/声音仍没有成功证据；不能把signature preflight通过当模型通过，也不能继续说用户GPU完全未知。
3. 已审查真实PyPI wheel：faster0.5.4依赖qwen-tts-hf>=0.1.1.post1和TF>=5.15.1，不能单降4.x。HF0.1.1.post1默认RoPE仍读旧字段，现代Mimi用rope_parameters。qwen_compat.py仅包装已识别默认函数，从实际配置读theta/partial factor到临时副本，不猜10000、不改config或权重、不替换未知registry/scaled schema。导入Qwen后、加载模型前接入Worker/原生adapter/CPU编码/训练。
4. 真实TF5.20.2 Mimi类+实际HF wheel函数已在CPU复现相同AttributeError，修复后三种theta10000/12345/1000000频率精确对照、原配置不变，三进程PASS。不是完整Qwen包/权重加载或GPU实验。元数据/完整requires_dist/源成员SHA与失败记录留在step12证据。
5. bootstrap固定faster0.5.4、qwen-tts-hf0.1.1.post1、TF5.20.2，安装对当前Torch/torchaudio/torchvision加版本约束，不盲升级/卸载平台CUDA。官方qwen-tts与HF共享命名空间冲突拒绝；native仍可用官方legacy provider，模型入口能力不因本阶段删掉。预检新增实际Mimi/默认RoPE CPU数学smoke，仍标no model/GPU。
6. 已知RoPE配置错误fatal；supervisor停止该worker重试并写启动nonce绑定的失败收据；bootstrap看fatal健康或本次收据提前失败。失败/异常/中断清理自己创建的Popen，45s未确认则要求完整会话停止，不拿旧日志PID盲杀、不删GPU锁、不假称资源已空闲。真实supervisor+CPU fatal-health三轮验证收据、worker/sup退出和PID标记清理PASS。
7. 默认QTTS_RESIDENT=1，健康模型不再按600请求或旧13.5GB门槛周期重载；高显存告警，empty_cache不释放活权重。QTTS_RESIDENT=0保留旧策略。每worker独立可见GPU0/1；health包含requested_model/model_loaded/cuda_visible_devices/residency_policy/fatal_error，Mock不报真实loaded。错误/OOM/平台回收仍可中断，不作永久驻留保证。
8. 用户要求“永久部署双卡”必须诚实解释：应用只能在会话存活/健康时各卡一份常驻，Kaggle配额/超时/关机会回收GPU；磁盘/私有Dataset缓存不等于GPU继续运行。长期常驻需要持续双GPU服务器，本次没采购外部硬件或绕过平台限制。
9. 完整Python267×3=801PASS，Node30×3/Go race count3、五个旧协议/adapter脚本各三轮PASS；新增14项兼容/驻留/fatal/依赖约束测试。浏览器113×3=339PASS；另最终包复制3PASS，独立真实剪贴板/下载/手机/拒绝授权三轮PASS；首个独立Chromium启动SIGSEGV记录保留，重跑成功，原因未确定。完整收据见step12/final-checks.json。11题550建议，三轮100项范围映射，完整目标22/300不冒充全部修复；完整内嵌30备忘录。
10. 下一步直接按KAGGLE_STEP12_QUICKSTART.md：先备份所需私有数据，停止并重启完整Kaggle会话（非仅内核/网页），复制step12，T4×2/Internet/非Mock。若旧目录PID标记保留，不盲删，可确认完整会话已重启后使用新QTTS_ROOT；旧数据另行管理。先smoke再两worker完成加载/warmup、workers_healthy=2，再真实短句/长句/取消/显存与音质。沙箱无CUDA/完整模型，不能保证此次目标复跑必成功；不再加准备工具前置。

---


日期2026-10-21。中文短进度，先保存计划再写码，不向用户重复提问。当前第十二阶段优先于内嵌历史；失败/blocked原始记录保留，CPU协议/替身不能冒充Qwen/GPU。目录/home/user/Kagglee，分支arena/041344f2-kagglee固定，不切换/改名，不需提交来保存。

## 第十一阶段历史状态：直接adapter推理/聊天接入已实现

1. 最新独立交付kaggle/kaggle-fixed-step11.py，276043字节/46资产，SHA256 cd5346e8ae34f1e2db327a076a7411996982848f9d4e14236f05d94c626d496e。repack默认step11/source_manifest_step11.json，原始至step10冻结；step10仍261429字节43资产SHA256 2bddd6ebad371268f9b3b02315fc29cae588da6c46c7d134476945b50b8a5ac4。源代码变更不能覆盖冻结包。
2. 本轮不是另一个准备工具阶段：先STEP11计划/Q10，再实现trained_profiles.py、adapter_engine.py、trained_voice.py及事务式LoRA切换，接入现有Worker→Go→网页选择/聊天。已有阶段10真实loss/backward/optimizer/DDP/adapter训练代码保留，不要说还没开始开发，也不说真实Qwen已经训练成功。
3. 默认faster声学流式路径保留，原生只有QTTS_TTS_ENGINE=qwen-adapter-buffered显式启用。官方原生完整一段才输出wave，标注sentence-buffered，不切假chunk、不声称<3秒/声学流式。每GPU一个可见设备/一份可信本地Base，FP16/eager。未实测16GBfit/峰值显存/质量，不能自动换小模型或预置说话人。
4. 发布要求真实completed run/request/result、固定manifest/Base/码pin、两个rank更新及每epoch覆盖记录、tensor摘要/shape/finite、实际schema2编码码租约；复制统一参考及对应文本为命名训练候选，不自动active。记录/声明不是官方签名或权利/身份鉴定，不防同UID恶意伪造整个状态。fixture/legacy不升级或发布。
5. 所有新LoRA模块先构造校验再锁内事务切换，支持不同rank及A/B/A；每段复核profile和adapter，保存speaker直接官方x-vector-only prompt。Mock/faster拒绝训练profile，原生拒绝普通profile；缺/坏/错误Base必须报错无PCM回退。缓存不是永远正确，两worker一半加载失败时active保留，下次按请求profile重选。
6. 新profile仍沿旧profiles私有Dataset备份，含一参考WAV/对应文本；run/完整模型/全体样本不自动备份。恢复缺Base/adapter报错；删原码/源库/profile/run/远程备份不同。训练参考只读，编辑/候选/校准409；旧普通profile与删除保留。
7. 原有两主视图、录音波形/上传/命名库/输入/码/认证/DeepSeek文字流/切段/有序播放/停止与源码复制保留；没有第三主视图或假训练按钮。原生取消只在AR步合作检查并丢迟到wave，不抢占CUDA kernel/codec decode。原生无帧/health/supervisor预算180秒，默认60/75/90秒不变；不是性能承诺。修复一致性检测全失败仍可能consistent=true的门禁。
8. Python252×3=756PASS，Node30×3、Go race count3PASS。新24adapter项包括真CPU LoRA输出/切换、隔离/错误拒绝/HTTP/取消；真实本机Go/双worker/本机SSE+CPU tiny LoRA接口替身3轮A/B/A及坏版本503/active保留/无PCM通过，不能写成真实DeepSeek/Qwen/NCCL。旧四协议脚本各调用3次、每次3轮（各9轮）PASS。浏览器112×3=336PASS（11.0分钟），最终包额外逐字复制3次与step11/final-checks.json核验；不是目标模型证据。
9. native runtime probe blocked退出2，沙箱Torch2.8/cu128仅CPU，CUDA不可用、无qwen_tts/真实权重；实际Base config标识base/1b7/16组也未拿真实权重核验。真实双T4训练、新进程重载试听、声学质量/RTF/首声、物理麦克风与DeepSeek外网服务均未验收。
10. 正式工作台仍HEAD39ed7670-ec8a-4565-a1ae-fff0064d5246，15文件1043155字节，1MiB余5421；新包独立交付，不塞入正式满额项目，不提高上限/删历史。用户自命名文件初始为空、自己粘贴；Python复制不是在JS iframe执行。浏览器测试仅隔离临时项目。
11. 已按10题各50建议累计500；300项目标22已验不变，不是代码开发百分比/300新修复。本交接完整内嵌27份备忘录，不以摘要替代原文；历史阶段叙述以本段最新状态覆盖。失败browser-initial/python-initial-failed保留；探针AST修正为分别匹配faster与native真实关键词。

## 直接下一步，不再增加准备阶段

按KAGGLE_TRAINING_QUICKSTART.md和KAGGLE_ADAPTER_QUICKSTART.md在真实双T4/可信模型/自己授权的实际编码数据上尝试首步，收集真实错误/峰值显存；完成后用真实run及pin发布候选，在新进程重载、每卡保存并试听WAV、A/B/A、DeepSeek长回答与停止恢复。仍然没有网页自动训练、完整CustomVoice或可恢复optimizer/scheduler/RNG；不要把新CLI发布当训练。没有可保证的成功日期、99.5%身份相似率、<3秒首声或永久Kaggle会话。当前工具/测试均非下一轮阻塞前置。

## 第十阶段既有实现：实际训练核心已开发

用户追问何时真正开发。本轮停止前置工具循环，保存STEP10/Q9后直接实现lora_adapter、tts_dataset、tts_training、training_job与tools/train_tts.py，附上游完整Apache许可证。没有新语言或生产网页/Go改动，不自动停推理或部署adapter。

- 真实联合loss、text_projection、DDP.forward内全部参数调用、FP16/eager/microbatch1、冻结Base1.7B及speaker encoder、FP32 attention q/v LoRA与AdamW状态、非重入梯度checkpoint、真实backward/梯度同步/正确尾部累积/GradScaler/全rank有限值与更新检查。
- 每rank一个CUDA设备、NCCL、确定性每epoch分片；奇数重复前缀填平不drop_last，保存每rank覆盖。至少参数改变、两rank最终摘要一致且全部样本覆盖才可保存adapter。不是两个独立微调，也不是只启动torchrun。
- 父及两rank受控共享GPU offline-reservation与码读取OFD，子在Torch前PDEATHSIG/ppid握手，Popen记录PID窗口屏蔽取消后子解除屏蔽；启动失败/单rank失败/超时/取消等待直接rank退出，最后FD关闭再释放。DataLoader无额外进程，不能扩展为任意外部子孙任务管理。
- 拒绝fixture/legacy/未实际编码/少于两样本，要求显式数据审阅与实验确认；Base内容pin和其speech_tokenizer必须匹配码来源。严格离线，不自动安装/下载/信任remote code；hash和用户声明不是官方签名或法律/语义鉴定。
- 保存本地adapter.safetensors、speaker.safetensors、Base/码hash与rank数值/版本/显存报告；load_adapter严格绑定/成员/张量核验后挂到单独Base，返回speaker向量。不是完整CustomVoice，没有resume optimizer/scheduler/RNG，未新进程Qwen试听或自动接入网页语音聊天。
- CLI可在真实环境模型/数据就绪后立即尝试，不需等下一开发阶段；KAGGLE_TRAINING_QUICKSTART.md给出实际list取pin、Base指纹、可取消Notebook调用。不要给出没有实测的训练成功日期/显存/音质承诺。

## 第九阶段既有实现（当时来源/读取边界；第十阶段已扩展FD接管）

先保存STEP9计划与Q8的50建议。生产仅增量修改training_codes.py/encode_training.py及MEMO，生产网页/Go/语言与GPU协议不改。没有新HTTP入口或假训练按钮。

- 新码schema2原样封存source/manifest.json和source/train_raw.jsonl；固定创建时源manifest hash，源JSONL/rank计划hash与源清单一致；逐项核对现有码的ID/顺序/帧数/audio/text/ref。保留库名/ID/修订、原始样本名/hash和用户使用权/单说话人声明；声明不是法律或身份鉴定。
- source纳入受限文件集、权限/链接拒绝、全部字节预算和暂存/核验/发布/回滚；不自动云备份，不额外复制原库原件音频。新码删除原库与输入后仍可独立核验封存记录。
- schema1旧码保持列表/核验/读取/删除且旧字节/hash不变，明确legacy-unsealed，不用当前库猜旧授权。list只描述格式政策，provenance_verified_now=false；schema2本次完整verify成功才为true。
- 码专用lease固定码manifest hash并完整验证，持目录外.use-ID独占flock后释放全局锁再yield；读期删除/第二读取同版本409，列表/核验/其他版本可用。正常/异常/进程死亡释放FD；fork继承最后引用活着则仍busy，不LOCK_UN/PID/TTL抢占。
- 这是可信调用者合作式只读，不是OS只读挂载或同UID恶意并发写防护。阶段9当时没有多rank接管；阶段10已接入受控共享FD，仍须保护到所有读者退出，并另做真实编码、语义/权利政策、设备及训练门禁。
- hold-read --seconds 1..3600只保持检查，沿用总timeout1..3600/取消/PDEATHSIG，收据training_allowed/gpu_verified/training_verified均false，不输出私人转写/完整来源、不执行命令/GPU/训练。fixture/legacy状态不升级。timeout含启动/核验，保持时长不含；长保持须留总预算，不能认为3600秒两参数必定刚好完成。

## 第八阶段具体实现（继续保留）

先保存STEP8计划与Q7的50建议。新增py/gpu_ownership.py和tools/resource_control.py，增量接入supervisor/worker/analyst/bootstrap。生产JS/HTML/Go未改，CPU编码仍仅CPU，旧库/授权隔离/输入租约/事务输出与所有快捷流程保留。

- 固定/tmp/qtts-gpu-ownership-{uid}/fleet.lock，同机同UID整组独占，不按STATE/CUDA索引/UUID分区。0700/0600、属主/普通文件/软硬链接/权限检查；应用不unlink/replace锁文件，不按PID或TTL抢占。
- 真supervisor先独占inference，再通过pass_fds仅给worker/analyst；孩子检查inode/nonce/模式/当前锁并采用同一OFD，gateway不继承。close只关引用，不LOCK_UN；父关/父SIGKILL但孩子活着时仍busy，最后引用关闭才释放。
- 独立真实worker/analyst也须独占整组，多个模型进程应统一由supervisor启动。Mock跳过，不宣称GPU所有权；CPU encode不占GPU，剥离GPU内部FD/nonce环境。
- 第二真实supervisor先占锁、失败不写supervisor.pid，成功后只清自己的PID标记。父日志句柄及时关闭，kill等待leader退出并清理仍活的进程组后代；停止信号注册早于启动，STOP期间不再拉起。
- bootstrap不再根据旧PID发信号或宽泛pkill；busy/遗留PID标记在探针/依赖安装前明确阻断，需人工确认停止。ready等待检查本次supervisor仍活着，不把旧服务健康当新启动成功。仍保留原安装/探针/下载/备份流程，真实目标兼容尚待验。
- resource_control.py status / reserve --seconds 1..3600，只观察/空闲预约，无GPU工作/任意命令/HTTP/force-unlock。预约不是显存释放、编码或训练。status观察busy和非权威last_record，永远gpu_verified=false，不公开nonce。
- 预约正常0、拒绝2/code409、SIGINT/SIGTERM取消130；SIGKILL由OS关闭FD回收。父SIGKILL后活孩子持锁是安全行为，不删锁文件强行“恢复”，须核实并停止本应用遗留模型进程。
- supervisor存活检查不等于所有新网关/子进程就绪，尚无本次作业代际ID贯通健康响应；旧端口占用仍需排查。bootstrap前置检查也不替代解包前停旧服务。
- 整组锁是保守准入，更多卡/不重叠子集也不并发。不能限制跨UID/容器或绕过协议的软件，不能防同UID恶意删改；没有实际CUDA测量/OS硬件隔离/显存回收保证。
- 升级前先停干净step1–7进程，旧版本不自动加入协议；新包会写目标ROOT源码，仅检查用独立ROOT/UNPACK_ONLY。旧runtime PID标记须核实旧服务停止后再清，绝不是删资源锁或改正式工作台HEAD。Mock/真实服务不混用同一STATE。

## 前置数据链路与真实边界（继续保留）

训练输入是完整24kHz单声道PCM16 WAV，逐条转写、统一参考、使用权/单说话人声明；固定源库修订/样本ID/哈希。浏览器Opus不可直接作为首版输入，不改后缀或裁剪，旧参考解码流程仍保留。源/选中集合变化清旧声明与文本，关闭/锁定拒绝迟到私有响应。

编码入口仅本机CPU/FP32/eager/两线程/单样本numpy全波形，要求可信本地物化JSON/safetensors全目录指纹，拒绝pickle/软硬链接/auto_map/越界分片。哈希不是官方签名，运行时包version不是源码身份校验。模型前后指纹与输入读取租约、原子输出/预算/回滚仍在。

返回必须一个样本、ceil(frames/1920)×16整数0..2047；规范WAV/text/ref_audio/rank数学计划完整复制。路径以码副本目录为cwd，不能相对原输入猜测。真实返回也只有tokenization_executed，不自动变tokenization_verified/训练/两rank/推理；测试码test_only_codes，不提供CLI Mock参数。

schema2完整封存源记录，schema1仅源ID/hash明确legacy-unsealed。输入与码版本读取租约均已实现，本轮已经接入实验性训练器/两rank受控FD生命周期；不能把检查租约当训练许可。取消/超时可能恰逢rename后收据前，list+固定hash verify再决定重试；临时文件不是安全擦除。

## 第十阶段分层证据（docs/validation/step10/）

- Python227×3＝681 PASS，新增25项训练核心/准入/OS生命周期与step9冻结回归，无Torch跳过；实际CPU联合loss/反向/AdamW参数更新、FP16基座/FP32梯度/冻结不变、尾部累积、nonfinite拒绝、严格adapter保存/重载。
- 实际两进程Gloo小网络参数改变、不同分片、最终摘要相同；每轮单元测试含一次，另trainer_tensor_check.py三轮把摘要/loss/步数保存gloo3.json。不是Qwen、CUDA或T4。保留find_unused警告，真实模型分支未知，不宣称极致速度。
- 控制器生命周期用真实Popen/pass_fds/pidfd/SIGTERM/SIGKILL/共享FD，角色仅CPU持锁替身，测试内部注入绕过fixture准入仅测协议，生产CLI没有此开关。零退出但无checkpoint不成功。
- Node API30×3、Go28顶层/16子测试race三轮、真实HTTP/旧CLI/资源FD/CPU Mock管线各三轮通过；原始至step9冻结、43资产确定性repack/compileall/语法/diff通过。
- 浏览器110唯一（60 QTTS＋50工作台）×3＝330 PASS（10.4分钟），完整step10复制专项另3 PASS（10.2秒）；临时项目保持step9，不改正式工作台，不冒充真实训练/物理麦克风验收。
- Torch2.8/cu128、safetensors0.6.2、packaging25仅沙箱CPU测试依赖，不照装Kaggle；runtime probe依然blocked/退出2，CUDA/qwen/模型与真实推理缺失，无模型加载或Qwen训练。
- 初版夹具manifest返回顺序/缺packaging与扩展夹具kwargs错误保留日志；最终三轮全过。清单22/300是目标验收，不是开发进度，9×50建议也不等于450修复。

## 下一步推荐与不可跳过门禁

下一步直接围绕Kaggle真实首步训练的错误/显存、adapter新进程重载试听与接入现有推理/聊天；不要再排收据/预约工具作为新的前置，不要只添假按钮。需要新专业问题时仍先写具体计划与50建议，不向用户重复提问。已有训练CLI在目标条件就绪后可以现在尝试，不必等另一阶段。
按TARGET_ACCEPTANCE在真实目标设备记录旧进程终止前后nvidia-smi及CUDA空闲/保留显存、合作锁、可信模型真实encode/decode/完整覆盖/内存/时间，验证取消/异常恢复。锁空闲不能代替显存空闲；缺设备/权重/外网就如实blocked，不虚构。

这些训练机制已有代码与CPU证据，仍须在真实Qwen验证文本tokenizer、NCCL world_size=2、两rank数据/梯度/optimizer/loss、显存、adapter与新进程重载试听。不能只加accelerate launch，不能照搬T4不支持的BF16/标准FA2/全参数AdamW；LoRA/FSDP/ZeRO须实际接口/内存证据。DeepSeek、物理录音/真实容器、冷热可听首声/标准RTF/音色保留集分别验收，首PCM不是可听首声，rtf_x是RTF倒数。

## 安全复现与服务

```bash
npm ci
python3 -m venv .venv
.venv/bin/python -m pip install -r kaggle/requirements-training-test.txt  # 沙箱可选张量测试，不替换Kaggle CUDA
.venv/bin/python kaggle/repack.py --check
.venv/bin/python -m unittest discover -s kaggle/tests -v
.venv/bin/go -C kaggle/source/go/gateway test -race -count=3 ./...
npm test
npm run test:e2e -- --repeat-each=3
npm run test:e2e -- tests/browser/studio.spec.js --grep '第十阶段训练器完整Python包' --repeat-each=3
.venv/bin/python kaggle/tests/ownership_process_check.py
.venv/bin/python kaggle/tests/training_gateway_check.py
.venv/bin/python kaggle/tests/codes_cli_check.py
.venv/bin/python kaggle/tests/mock_pipeline.py
.venv/bin/python kaggle/tests/trainer_tensor_check.py --output docs/validation/step10/gloo3.json
```

Go来自CPU requirements的go-bin，这些依赖不是GPU锁文件。所有权进程测试在现有真实holder busy时拒绝启动，不能扰动真实应用。仅解包：QTTS_UNPACK_ONLY=1 QTTS_ROOT=/tmp/qtts-step10-inspect python3 kaggle/kaggle-fixed-step10.py，不安装/下载/启动服务；真实启动仍须审查依赖及模型，QTTS_TUNNEL=none可禁用隧道，真实验收禁止UNPACK_ONLY/Mock替代。

Node工作台3000不同于Kaggle网关，浏览器3100只用临时项目，绝不重置正式workspace。本轮恢复的Node过程仅工作台，不是GPU部署；无应用认证，不能当公网多租户平台。Kaggle单用户Bearer与DeepSeek Key分离，同源可信HTTPS。密钥、私人音频/转写不得进截图/共享日志/Git。

---

## 内嵌备忘录：KAGGLE_PLAN.md

# Kaggle 双 T4 / Qwen3-TTS 语音克隆聊天：实施方案与阻塞说明

## 0. 当前状态，不得略过

**2026-10-21 更新：源码已收到，缺失源码阻塞已解除。** `workspace/HEAD.json` 指向的已保存文件包含原始 `kaggle`，127241字节、SHA256 `26c31621d6265bc25370bc284f2afdcf52f5edaf97e64056c2d8d5eda4a6c461`。通过AST/literal_eval静态解析、Base64/zlib解码及22项内嵌哈希验证，落盘到 `kaggle/source/`，没有运行原安装器。原文件未覆盖。

已完成首批可靠性、第二阶段访问控制/资源预算，第三阶段完成后，现已直接实现第十阶段Base1.7B FP16 LoRA联合loss/双rank DDP/真实优化器与adapter保存核心；真实Qwen/GPU执行仍blocked，最新部分修复包 `kaggle/kaggle-fixed-step17.py`，当前范围及未完成项见KAGGLE_STEP17_AUDIT.md；训练后推理/聊天接入见 [KAGGLE_STEP11_AUDIT.md](KAGGLE_STEP11_AUDIT.md)，已有训练核心证据见 [KAGGLE_STEP10_AUDIT.md](KAGGLE_STEP10_AUDIT.md)，第九阶段历史见 [KAGGLE_STEP9_AUDIT.md](KAGGLE_STEP9_AUDIT.md)，第八阶段历史见 [KAGGLE_STEP8_AUDIT.md](KAGGLE_STEP8_AUDIT.md)，第七阶段历史见 [KAGGLE_STEP7_AUDIT.md](KAGGLE_STEP7_AUDIT.md)，第六阶段历史见 [KAGGLE_STEP6_AUDIT.md](KAGGLE_STEP6_AUDIT.md)，第五阶段历史见 [KAGGLE_STEP5_AUDIT.md](KAGGLE_STEP5_AUDIT.md)，第四阶段历史见 [KAGGLE_STEP4_AUDIT.md](KAGGLE_STEP4_AUDIT.md)；第三阶段见 [KAGGLE_STEP3_AUDIT.md](KAGGLE_STEP3_AUDIT.md)，前阶段见 [KAGGLE_SECURITY_AUDIT.md](KAGGLE_SECURITY_AUDIT.md)。step1与step2历史包冻结保留。证据、具体范围、测试命令及后续风险见 [KAGGLE_SOURCE_AUDIT.md](KAGGLE_SOURCE_AUDIT.md)。这不是完整双T4成品，也不是三轮300项已经验收。

当前虽装Torch作CPU张量测试，仍没有真实GPU、Qwen权重、参考录音或DeepSeek凭据，出站网络也不支持模型托管站或DeepSeek。因此真实模型、双卡训练、音质、首声和RTF验收仍阻塞。本轮没有以Mock测试冒充这些验收。

## 1. 用户目标（保持原意）

- 在 Kaggle 双 T4 上使用 Qwen3-TTS 1.7B，正常推理期间两卡各一个模型实例。
- 简洁网站只设两个主要视图：“录制参考语音”和“语音对话”。主要操作不用滚动页面。
- 先建立自定义名称的语音库，再上传或录制多段参考音频，显示真实采集波形。
- 用户可以选定样本执行真正训练；两卡共同参与同一训练作业，报告全部有效样本的参与情况。
- 训练后克隆聊天，支持情感与音色保持；用户提出99.5%相似度目标，不能转换成无定义的保证。
- 先配置 DeepSeek，再聊天；支持长输出、流式首句优先、切换声音、文字和语音输入。
- 用户提出首声3秒、RTF≤0.5、播放无系统性断音和输入打断目标，需要实测。
- 浏览器工作台应复制最终 Kaggle 代码，不能复制网页HTML冒充Python启动代码。
- 保持此前文件命名、保存、浏览器预览等功能可用；保存真实源码；三轮检查及备忘录需要可追溯。

## 2. 官方资料核查结论

本轮从 GitHub 核对了以下官方文件，Qwen 仓库参考提交为 `022e286b98fbec7e1e916cb940cdf532cd9f488e`：

1. [Qwen README](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/README.md)
2. [单说话人微调说明](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/README.md)
3. [官方训练脚本](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/sft_12hz.py)
4. [FlashAttention 硬件支持说明](https://github.com/Dao-AILab/flash-attention#nvidia-cuda-support)

已核实：

- 克隆参考音频应从 `Qwen/Qwen3-TTS-12Hz-1.7B-Base` 路线验证，不能把预置音色的 CustomVoice 当成任意声音克隆接口。
- 官方提供 `create_voice_clone_prompt` 和 `generate_voice_clone`，前者可复用参考特征，**不等于微调**。
- 官方微调说明是单说话人流程：JSONL 包含 `audio`、`text`、`ref_audio`，先提取声学码，再训练、保存检查点。不同人物不能无区分混入单说话人库。
- 官方示例训练含 BF16、FlashAttention 2、全参数 AdamW；不能原样当作 T4 双卡脚本。
- 标准 FlashAttention 2 CUDA 路线支持 Ampere/Ada/Hopper；文档为 Turing 指向另外的实现。不能默认 `pip install flash-attn` 后 T4 就具备同等内核。建议从 FP16 + 经探测的 SDPA/eager 开始，不静默换小模型。
- 官方训练脚本使用 Accelerate，但还包含包装后模型属性访问和检查点处理等需要多进程专项核对的代码。不能只加 `--num_processes 2` 就声称正确双卡训练。
- 官方公开 Python 示例返回完整波形。模型架构支持流式不等于现有包装器已提供可直接消费的声学流。必须先做兼容性试验，确认 T4 上实际流式后端。

官方总体延迟宣传、其他GPU成绩、整段分句合成成绩，均不作为本项目双 T4 达标证据。

## 3. 推荐架构（已结合原源码修正，训练部分待实现）

```text
HTTPS 浏览器：参考语音视图 / 语音对话视图
    │ 同源鉴权 HTTP + WebSocket
Go 网关/调度（已有）+ Python 分析与训练编排（后者待实现）
    ├── SQLite 元数据与版本清单
    ├── 语音库原始文件、转写、处理结果、训练清单
    ├── DeepSeek 流式客户端 → 文本切段 / turn取消
    ├── 统一有界合成队列 / 有序音频汇聚
    ├── Worker A：物理GPU0，模型独立加载
    └── Worker B：物理GPU1，模型独立加载

训练模式：排空/取消推理 → 释放推理模型 → 两卡同作业训练
    → 校验检查点与样本覆盖 → 原子发布语音版本
    → 两卡分别恢复推理并预热 → 网站显示就绪
```

源码已有Go网关/调度及Rust可选音频库，优先保留其有效实现；Python承担模型、ASR与拟新增训练编排；原生 TypeScript/JavaScript/Web Audio 承担浏览器交互；SQLite 承担元数据。现有 Node 工作台仍负责代码编辑与真实文件保存。只有测量显示CPU密集型瓶颈且已有可靠实现时，才考虑 Rust/C++，不为了语言数量引入额外编译链。

每个推理 worker 用独立 `spawn` 进程；设备映射必须验证物理GPU与逻辑CUDA编号，不能把 `device_map=auto` 模型切分误称为两份独立副本。

### 3.1 模型常驻与“永久”

- 会话运行期间：加载一次、预热一次，不在每轮聊天重新加载。
- Kaggle 会话结束：进程、显存及公网访问入口都会失效，不承诺永久在线、不做绕过平台限制的保活。
- 可交付的是：版本化资产导出、重新挂载、校验及一键恢复流程。`/kaggle/working` 中的文件必须明确导出或保存成平台支持的持久化资产，不能视为自动永久可靠。
- 如果最终要求真正24小时常驻，部署目标需改为可持续GPU服务器；不能偷偷将这项要求标成Kaggle已实现。

### 3.2 训练路线与诚实的降险

先测 Base 克隆基线，参考特征缓存功能明确标为“准备克隆”，不叫训练。

真正微调必须有：选定样本快照、准确转写、声学码、训练参数、两个rank的梯度同步、样本覆盖、检查点与重新加载试听。

DDP 并不会把两张卡的显存合成一个32GB模型空间。标准全参数混合精度 AdamW 的参数、梯度、主权重和动量状态常见估算约16字节/参数：1.7B约27.2GB（十进制），还没算激活。具体取决于实现，**因此不能不测就承诺每张16GB T4可运行官方全参数配置**。

推荐先验证兼容的 LoRA / 参数高效训练方案，确定目标层、可训练参数、FP16缩放、梯度checkpoint和有效batch；未通过真实模型的梯度及恢复测试前不得提供“已支持”结论。若需要 ZeRO/CPU offload，需额外验证Kaggle CPU RAM、吞吐与检查点；不默认引入。

训练期间两卡归训练进程独占，网站明确进入训练维护状态。若用户要求训练和双副本聊天绝不间断，必须重新做资源预算，当前方案不伪装支持这种并发承诺。

“不管多少音频”解释为可持续增加库、分批上传、分页选择及任务化处理，不解释成无限磁盘、无限显存或无上限单次训练。

## 4. 两个主要界面

### 参考语音

固定顶部两个视图切换入口；主体采用分区卡片，列表和日志分页，不依赖页面滚轮才能操作。

- 语音库名称输入、创建和选择。
- 上传音频、开始录音、停止录音、录音时长、权限状态。
- 波形由真实 AnalyserNode 数据驱动；静音时仍显示明确“录音中”，不能只靠随机动画。
- MIME探测、音频解码、采样率/声道正规化、静音和削波检查。
- 参考转写编辑；选中音频、数量、总时长与质量问题。
- “准备克隆”和“训练”分别显示，训练支持取消、真实进度、双卡状态与样本覆盖报告。
- 浏览器麦克风依赖HTTPS、权限与嵌入策略；失败时上传功能仍可用。停止后关闭所有tracks。

### 语音对话

- 服务端保存API配置；前端只显示“已配置/未配置”，密钥不回显、不存localStorage、不写交付代码。
- DeepSeek模型、可用输出预算和超时按真实供应商接口验证，不硬写不确定的长输出上限。
- 文字输入、开始/停止语音输入、发送/打断；ASR后端单独验证，不只依赖不可移植的Web Speech API。
- 声音选择绑定库与检查点版本；选择新声音时推荐取消当前轮并在下一轮使用，避免一条话中途混入不同音色。
- 聊天内容与历史分页显示；状态和错误可见；不使用“没有滚动条”掩盖被裁掉的输入控件。

## 5. 低延迟、连续播放与打断

1. 用户点击开始时解锁同一 AudioContext；自动播放被拒要有明确入口，浏览器权限规则不能靠保证绕过。
2. DeepSeek增量文本经过切句器；首个短段尽快提交，后续按长度/标点/等待时间控制，保留未消费尾部，处理finish_reason。
3. 真正流式TTS能力先用技术试验确认；若只能整句生成，UI与报告必须写清楚，不冒充声学token流式。
4. 两worker只负责并行生产；所有段含 turn_id、segment_id、chunk_id、voice_revision，汇聚后按序输出。
5. 音频统一采样率/声道，使用有界PCM环形缓冲或连续样本时钟调度；不使用多个audio元素收到即play。
6. 用适量预缓冲应对网络抖动，并统计欠载。预缓冲过长会损害首声，必须实测平衡。短淡化只能消除爆音，不能补丢失内容。
7. 打断同时停止浏览器排程节点、清空环形缓冲、取消DeepSeek读取、使旧GPU任务停止或作废；旧turn迟到包一律拒收。
8. 如果当前后端不能中断CUDA生成，单纯关闭WebSocket不算真正取消；需记录释放延迟，不能让旧长生成阻塞新首声。

## 6. 验收定义

| 用户目标 | 实际验收方式 | 当前状态 |
|---|---|---|
| 两卡各一个模型 | 两个物理设备独立PID/显存/探针合成记录 | 未实测，缺GPU/模型 |
| 两卡共同训练 | world_size=2、rank日志、梯度同步、样本覆盖和重载试听 | 未实现/未实测 |
| 训练完整 | 选定/有效/排除/已见样本逐项清单；不是只看loss | 未实测 |
| 99.5%相似度 | 先定义评估模型、保留集、cosine等指标和盲听；不等同概率 | 不作百分比保证 |
| 首声≤3秒 | 从用户提交至实际可听首样本，分冷/热，报告P50/P95与失败率 | 未实测 |
| RTF≤0.5 | 生成耗时/音频时长；纯TTS与端到端分别记录 | 未实测 |
| 连续播放 | 长回答PCM缓冲欠载、丢包、系统断音次数；区分自然停顿 | 未实测 |
| 可打断 | 从用户输入/按钮至静音及旧GPU任务停止的分别测量 | 未实测 |
| 自适应无页面滚动 | 固定常见视口下关键控件可见、列表分页 | 待TTS网站实现 |
| 可复制Kaggle源码 | 复制实际所选文件原文、权限拒绝兜底、不修改磁盘 | 本轮已实现，另有浏览器测试 |

首次真实设备评估只在指标达标时标为通过；不达标时分析瓶颈、报告实际成绩，并明确调整硬件/后端/目标的取舍，不静默缩小模型或跳过音频。

## 7. 小步执行门禁

- G0：已拿到并保留原始kaggle，确认Python封装格式及22项资产，完成首批可复现缺陷修复。原用户实机报错日志仍未提供。
- G1：两个GPU独立加载、FP16兼容与真实克隆最小实验，测显存/延迟。
- G2：克隆准备、音频库、上传录音、转写、恢复；完成样本资产闭环。
- G3：双rank训练最小步、全部样本覆盖、检查点重载；不得先做假训练按钮。
- G4：文本聊天→DeepSeek真实流→单卡声学输出→浏览器连续播放；先贯通再双卡优化。
- G5：双卡顺序汇聚、长输出、声音切换与打断，测TTFA/RTF/欠载。
- G6：三遍完整端到端：正常、异常打断、长文本重启。每遍均有真实录音/模型/供应商与浏览器证据。
- G7：固定依赖、Notebook导出、启动代码复制、无秘密交付与可回滚发布。

首批源码报告及导出见 `KAGGLE_SOURCE_AUDIT.md`；三轮各100项见 `KAGGLE_REVIEW_CHECKLIST.md`；逐项标注已核对、已修复、不适用或阻塞。不能为了满足数量修改正常代码。专业自问自答见 `KAGGLE_DECISIONS.md`，每题后50条建议；答案为明确的推荐暂定方案，不是假装已完全知道缺失源码的细节。

## 8. 收到源码后的交付形式

优先保留其可用逻辑，按模块分离依赖安装、配置、数据、训练、推理、API和前端。最终交付可粘贴的Kaggle代码单元或经验证的Python启动脚本，并附依赖版本、模型revision、运行顺序、持久化导出步骤、真实测试报告。

如果上传的是Notebook，需解析代码单元并处理魔法命令和执行顺序，不能把Notebook JSON或未经处理的拼接字符串说成可直接运行。工作台“复制当前代码”目前是准确复制原文工具，不会自动转译Notebook，也不声明某个文件已经Kaggle验证。

## 9. 本轮实际完成与验证结果

- 已实现顶部“复制当前代码”：复制当前文件完整原文，包括未保存输入；空文件给出提示；剪贴板拒绝时显示只读且全选的原文，保留手动复制入口。没有自动执行Python或伪造Kaggle代码。
- `npm run check`：通过。`npm test`：30/30服务端及文件系统测试通过。
- `npm run test:e2e`：40/40浏览器测试通过，包含之前35项回归与新增5项复制场景。
- `npm run test:e2e -- --grep 复制当前代码 --repeat-each=3`：完整新增复制场景重复3遍，15/15通过。
- 实际视口390、768、900、960、1024、1280、1440px检查无页面横向溢出。
- 机器校验清单为每轮100项、共300项，决策后建议共150项，完整提示词内嵌全部备忘录。
- 以上均为代码工作台及文档验证。**未运行真实Qwen推理、双T4训练、ASR或DeepSeek调用，不能作为这些系统验收通过的证据。**


## 10. 第一阶段源码验证结果（历史保留，2026-10-21）

- Python 18/18；Go 14个顶层测试（含表驱动场景），竞态检测重复3次通过。
- 全部浏览器47/47（原工作台40项＋QTTS6项＋实际启动代码复制1项）；QTTS六项重复3次为18/18。
- CPU双Mock worker配合真实Go网关三轮通过，涵盖有序帧、文本完整、中断恢复和模拟水位，不是GPU实验。
- 重打包原22项完整性＋新23项资产、确定性生成和仅解包逐字节对比均通过；测试日志在 `docs/validation/`。
- 原三标签页仍保留，真实训练/两个主视图/波形UI未实现，公网认证和依赖锁定尚未完成。


## 11. 第二阶段已完成：单用户访问控制与资源预算（历史结果）

- Kaggle网关所有API统一Bearer认证，缺配置不启动；浏览器解锁/锁定、同源凭据、输入/视图清理、请求和录音取消已加入。
- 自动生成口令默认位于/tmp的0700认证目录、0600文件，不进入声音库/Notebook工作目录导出；可优先配置QTTS_ACCESS_TOKEN Secret。
- 请求体、上传文件/时长、历史、语音与昂贵操作并发、令牌桶、后台构建和记录容量均有应用层预算；不是OS级配额/多租户平台。
- Python41/41、Go24个顶层测试开启竞态检测重复3遍、完整浏览器51/51、QTTS专项27/27、受认证Mock管线三轮通过，详见KAGGLE_SECURITY_AUDIT.md与docs/validation/step2/。
- 本阶段当时原始kaggle和step1包均未改；step2共27项资产，清单source_manifest_step2.json。真实GPU依赖/后端探针、两主视图/波形UI与真正训练仍需后续实施。


## 12. 第三阶段：兼容探针与原生录音生命周期

- 计划先落盘KAGGLE_STEP3_PLAN.md，再实施；只新增独立step3包（30资产），历史包哈希不变。
- 元数据/设备/接口形状探针不安装、不下载、不加载模型。安装依赖后、模型下载前运行，阻断时保存报告；API只有受认证GET读取，不提供远程执行。
- 实测getUserMedia→AnalyserNode波形、RMS/峰值与MediaRecorder编码，不连接扬声器。录音可本地移除，不自动上传，失败保留片段。
- 处理未决权限、锁定、迟到事件、设备结束、页面离开与封装超时，加入字节/文件数/块数/时长预算。仍保留三标签页，不把参考缓存叫训练。
- 当前Python56项×3、Go26顶层/16子测试race×3、Node API30项、真实Go+双CPU Mock三轮均通过；完整浏览器66项×3轮=198次通过；详情见KAGGLE_STEP3_AUDIT.md。
- 300项清单仅15项有据勾选；真实GPU/物理麦克风/模型/DeepSeek/质量与性能未验收，不能由软件信号或Mock替代。


## 13. 第四阶段：两主视图与视口布局

- 先保存KAGGLE_STEP4_PLAN.md，再改为录制参考语音/语音对话两主视图；监控为原生辅助诊断窗口，保留所有既有DOM ID与脚本顺序。
- 桌面双栏、手机分区、主操作固定、长文本/档案/选项独立滚动。所列五个标准CSS视口内测试完整控件与祖先裁切；≤640px高允许页面滚动而不是丢失操作。
- 关闭/Escape/焦点恢复/锁定、隐藏面板、键盘导航、顺序轮询与过期报告均覆盖；切换视图/诊断停止采集并保留有效片段，转录页停止播放。
- 自命名1–64Unicode字符，不再回退my-voice；参考文本/校准有常驻“选项”入口。中文布局测试加载仓库现有本地Noto字体，生产不增加外链字体。
- Python59项×3、Go26顶层/16子测试race×3、API30、双Mock管线三轮通过；全量浏览器87项×3轮=261次最终通过，初次失败/中止记录保留，见KAGGLE_STEP4_AUDIT.md。
- 保留原始/step1/2/3，独立step4为30资产；工作台保留所有旧文件，不为重复交接文件放宽1MiB限制。完整交接留仓库，工作台只添能容纳的源码与简报。
- 下一步目标环境验收门禁见KAGGLE_TARGET_ACCEPTANCE.md：非Mock证明、每卡真实推理、容器/DeepSeek/指标与真正双rank训练分别验收，当前均未取得通过证据。

第四阶段最终只勾选18/300项；历史150条建议仍保留。真实双T4/模型/训练/DeepSeek/物理麦克风/音质/首声/RTF未验收。


## 14. 第五阶段：先命名空库、再添加/选择原始参考

- 计划KAGGLE_STEP5_PLAN.md先保存，再增量实现独立STATE/libraries；不把空库/原始音频误当可推理profile。旧一步创建档案与两个主要视图不变。
- UUID/命名分离、SHA256去重与核对、修订CAS、原子清单/写失败回滚、库/文件/总字节预算、0700/0600、链接拒绝。仅本地会话存储，原始样本不自动导出Dataset；处理后档案锚点/转写保留已有备份语义。
- flock租约覆盖参考处理，线程启动/取消/进程死亡不遗留永久busy。原始字节快照固定所选样本；复用既有构建，不是训练。结果提交后才公开终态，失败不删除源样本或上次独立档案。
- 发现并修复线程池提交失败但排队项稍后仍可能执行的边界，真实ThreadPoolExecutor回归；原始/step1/2/3/4冻结，step5独立32资产/196140字节，SHA256 acfa5639324e16aa7dcfe314caef09bee8eb277d59bdd71a5f1f4cffa0a7aaf1。
- Python92×3、Go28顶层/16子测试race×3、Node API30×3、真实Go→analyst原始库HTTP与双CPU Mock各三轮通过；浏览器100唯一×3=300通过/11.2分钟，最终包复制另3次通过；新流程初检12通过。
- 正式工作台保持15文件1043155字节/既有HEAD，剩5421字节不足新包；不提高1MiB、不删除历史，本阶段独立文件交付，复制只在隔离临时工作区验证。
- 仅增R1-073，当前19/300；第4题50建议与历史150建议保留。真实双T4/模型/DeepSeek/物理麦克风/真实训练及质量与性能仍未验收。


## 15. 第六阶段：训练输入，不冒充训练执行

计划KAGGLE_STEP6_PLAN.md与专业问题5的50项建议先落盘，再增量实现TrainingDataStore。逐条转写、统一参考、权利/单说话人声明，固定来源库修订与原始ID/SHA256；只读同库租约不改参考处理状态。独立私有目录、完整24kHz mono PCM16 WAV、规范化容器保留全部PCM帧、JSONL/manifest/数学双rank计划、原子发布/失败回滚、分层预算与固定哈希校验。

界面仅增辅助库窗口的折叠区，仍两主视图。库/所选集合改变必须重新声明；初版程序化建库可能沿用旧勾选的问题复审修正，旧全量105次后中止不计三轮完成。新版106唯一用例×3＝318通过（10.6分钟），详见阶段报告。

step6独立33资产/210003字节，SHA256 781eca6e2e34bdacbe2f5337bd6535512226c2122bbf3876d05634f2fc86d256；step1–5冻结。Python112×3、Go28顶层/16子测试race×3、Node30×3、真实Go/analyst合成WAV输入三轮与两CPU Mock管线三轮通过；浏览器106×3＝318通过（10.6分钟），包含第六阶段完整源码剪贴板三次一致性验证。原始/训练输入不自动Dataset备份，副本要单独删除。

仅新增R1-079与R2-031，累计21/300；专业问题共5×50＝250条建议。没有audio_codes/训练器/optimizer/梯度/检查点/实际两rank、GPU训练与推理互斥或任何真实模型/双T4/DeepSeek/性能/物理录音验收。格式暂不接收浏览器Opus作为训练输入，不篡改后缀冒充WAV。


## 16. 第七阶段：离线声学码入口与真实编码门禁

先保存STEP7计划及Q6的50行动建议，再实现py/training_codes.py与tools/encode_training.py。只允许本机CPU/FP32/eager/两线程/单样本与本地固定hash JSON/safetensors模型，未接GPU或HTTP任务，不抢占两推理实例。真实适配调用Qwen3TTSTokenizer.encode全波形，严格核对一个返回、ceil(frames/1920)×16和0..2047整数，不用zip丢样本。模型目录前后指纹、输入固定manifest租约、完整WAV/text/ref_audio/rank计划副本，原子发布/回滚/预算和独立校验/删除。

取消/超时停止进程组；复审补Linux PDEATHSIG/ppid握手覆盖控制器被强杀。初版浏览器75次后中止保留，不计最终三轮。测试fixture输出强制test_only_codes/tokenization_executed=false；当前Torch/qwen_tts/权重均无，真实编码未运行，tokenization_verified/训练/两rank/推理均false。码副本不自动Dataset备份；未来训练读取租约仍需接入。

step7独立35资产/222808字节，SHA256 3fe57769560c076d6d288a87cae6150b0a9404597eb0ea3997ab26de596f4cd0，原始与step1–6冻结。最终Python146×3、Go race×3、Node30×3、真实Go/analyst HTTP租约与本机CLI/fixture链路三轮、CPU Mock管线三轮通过；浏览器107唯一×3＝321通过（11.5分钟），最终完整包复制另3次通过。正式工作台15文件1043155字节及HEAD不变，不提高1MiB限制或删历史，独立文件交付。

三轮审查清单仍21/300；专业问题6×50＝300建议，不等于300项修复。下一步GPU资源所有权/推理与离线任务互斥和目标设备真实编码/解码/内存/时间门禁，之后才文本tokenizer及真正两rank优化器/检查点。


## 17. 第八阶段：整组GPU资源准入，不是自动训练模式

先保存STEP8计划及Q7的50行动建议，再实现py/gpu_ownership.py、tools/resource_control.py。固定同机同UID整组flock，不随STATE或CUDA别名变化；supervisor先独占，再通过pass_fds只让worker/analyst采用同一OFD，gateway不继承。close不LOCK_UN，父关闭/死亡但活孩子仍持锁，最后引用退出才释放；诊断PID/时间记录非权威，不能TTL抢占。真实模型入口在加载前受控；独立模型进程独占整组，多worker应由supervisor统一启动，Mock/CPU编码不宣称GPU所有权。

补日志FD关闭、kill等待与后代清理、早期信号处理和停止期间禁止重启。bootstrap不再按PID/pkill自动杀旧服务，busy/遗留运行时PID标记阻断；ready检查本次supervisor存活，避免读旧健康误报。没有自动模式切换/排空/显存回收、GPU编码或训练；旧版本升级前必须先人工确认停止，不能删锁文件强行恢复。

step8独立37资产/230559字节，SHA256 777c1d523559c9c734cd5e99841810524284e91269ced23963e8e5ab3f3cc1e1，原始至step7冻结。Python179×3、Go race×3、Node30×3、真实supervisor/FD/CPU替身生命周期三轮、真实HTTP/本机CLI与CPU Mock管线三轮通过；浏览器108唯一×3＝324通过（10.5分钟），完整复制专项见阶段报告。正式工作台仍15文件1043155字节/HEAD不变，不放宽1MiB，不删历史，独立文件交付。

仅新增R2-010的合作式锁设计/协议证据，累计22/300，7×50＝350条建议；并非GPU/显存/两rank验收。下一步码版本完整来源/授权封存与训练读取租约、受控离线任务及目标硬件真实编码/解码/显存门禁，再到实际优化器与检查点。


## 18. 第九阶段：完整来源封存与固定码版本读取租约

先保存STEP9计划与Q8的50行动建议，再增量实现。新schema2把输入manifest及原始JSONL完整字节封存，固定原输入SHA256，逐项交叉核对音频/文本/统一参考/样本顺序及分配计划；原库/修订/原件hash/用户声明均保留。source纳入权限/链接拒绝/预算/原子回滚。来源声明不是法律/身份鉴定。

schema1历史码仍可列表、核验、读取和删除，明确legacy-unsealed，不补写授权、不改变旧hash。list只描述封存政策，不声称当前完整性；完整核验才返回provenance_verified_now。读取租约先固定码manifest并完整核对，然后释放全局锁；目录外.use-ID独占，读期同版本删除或第二读取409，其他版本可操作。异常/进程死亡由FD关闭回收，fork继承引用未关闭前仍busy。

本机hold-read只保持1..3600秒检查，不执行命令/GPU/训练，沿用超时/取消/PDEATHSIG，收据training_allowed=false。协作式约定只读，不是OS只读挂载；未来训练器仍须管理所有读者生命周期并另验真实编码、语义、硬件与训练门禁，未自动实现DDP多rank接管。

独立step9为233074字节/37资产，SHA256 8ec892dcc5ca10daf20c8de84dd2be08d9a3de8807872c2051ddf52bd5882a9b；原始至step8冻结。Python201×3＝603、API30×3、Go race三轮、真实HTTP/CLI/资源FD与CPU Mock各三轮通过；浏览器109唯一×3＝327通过（10.3分钟），最终复制专项另3次通过。当前8×50＝400建议，清单仍22/300，不把建议或测试次数当真实硬件完成。下一步受控离线作业的收据/生命周期门禁与目标T4真实编码/解码测量，再考虑训练器与检查点；缺依赖不伪造任务完成。


## 19. 第十阶段：不再延后核心，实际训练器已开发

回应用户“还有多久才能真正开始开发”：现在直接开发，不再用来源/预约/收据阶段替代训练功能。保存STEP10计划与Q9的50建议后实现lora_adapter/tts_dataset/tts_training/training_job/train_tts，附上游Apache许可证。目标路径FP16/eager/microbatch1/FP32 LoRA和AdamW；所有loss调用在DDP.forward内，文本过projection，真正backward/梯度同步/累积/有限值与参数改变检查、adapter原子保存。父/两rank共享GPU和码FD，取消/超时/父死保护；不自动停推理或部署模型。

新增25项训练核心/准入/张量/真实进程测试及step9冻结回归，全Python227×3＝681 PASS；另CPU小网络真实两进程Gloo三轮，参数真实改变且rank最终摘要相同。不是Qwen、CUDA/NCCL或T4训练证据。Node30×3、Go race三轮、HTTP/CLI/资源FD/CPU Mock各三轮PASS。浏览器110唯一×3＝330 PASS（10.4分钟），完整复制专项另3 PASS。

step10独立261429字节/43资产，SHA256 2bddd6ebad371268f9b3b02315fc29cae588da6c46c7d134476945b50b8a5ac4；原始至step9冻结，正式15文件/HEAD/1MiB不变。当前Torch2.8/cu128仅CPU测试，沙箱无CUDA/权重/Qwen包；不把它当Kaggle依赖锁。

真实开训不需再等一个开发阶段：在双T4及可信模型/授权数据就绪后可以尝试本CLI。耗时、显存和成功日期没有实测，不能保证。下一核心是现场真实首步故障处理、adapter新进程重载试听及接入现有推理/聊天，而非继续工具化前置。训练恢复状态/完整CustomVoice/网页自动训练及质量性能仍未完成。详见KAGGLE_TRAINING_QUICKSTART.md。9题450建议，22/300是目标验收状态，不是代码开发进度百分比。


## 20. 第十一阶段：直接接入训练后的推理与聊天

先落盘STEP11计划与Q10（50建议），选择官方原生adapter后端，诚实标注句级缓冲。默认faster不改，明确选择而不是猜CUDA graph支持LoRA。完成run/pin/双rank更新与tensor摘要、统一参考WAV及转写发布；profile不自动active、质量/重载验收false。每GPU一份可信本地Base，全部LoRA预构造再锁内切换，保存speaker直接构造x-vector-only prompt。损坏/缺依赖/错Base/普通与训练模式混用一律拒绝，不输出Base/Mock冒充训练声音。

现有Worker帧→Go调度/SSE→网页声音选择/聊天已接入；原生是完整一段才返回wave，输出一次而不是切假chunk。取消按AR步合作检查并丢迟到PCM；180秒保护预算不是时延承诺。两主视图、旧参考处理/录音/命名库/原始输入与码/认证/DeepSeek文字流/打断/复制保留。修复一致性检测全失败仍可能判consistent=true的问题。训练候选参考只读，编辑/校准409。

真实本机Go+SSE+双worker+CPU tiny LoRA原生API替身执行3轮A→B→A；损坏版本503、active保留且无PCM回退。真实Qwen/T4训练、新进程重载试听、峰值显存、性能及DeepSeek外部服务未验收。独立step11：276043字节46资产，SHA256 cd5346e8ae34f1e2db327a076a7411996982848f9d4e14236f05d94c626d496e。原始至step10冻结，正式工作台满额15文件/HEAD不改；10题500建议不等于300项完成。直接目标操作见KAGGLE_ADAPTER_QUICKSTART.md，下一步是实际首步与重载/试听，不再加准备工具。


## 21. 第十二阶段：实机Mimi/RoPE故障修复与健康模型会话驻留

用户实际检测到两Tesla T4，Python3.12.13/Torch2.10.0+cu128/faster0.5.4/TF5.20.2；两worker在MimiConfig.rope_theta加载失败。保存STEP12计划与Q11的50建议后审查实际PyPI wheel，发现Qwen-HF旧默认函数与现代Mimi字段不一致；没有采用违反faster依赖的单独降4.x。

新增qwen_compat.py，仅对已识别Qwen默认函数做现代theta真实读取/临时副本桥接，配置/权重不动；接入实际模型各入口和预检CPU数学smoke。实际TF类+Qwen wheel原函数CPU复现同一个错误，三种theta及原配置不变三进程通过，不等于完整Qwen/T4成功。固定三个直接依赖，安装用当前Torch/音视频版本约束保护CUDA栈。

fatal worker停止重试，启动nonce失败收据避免健康端口消失后继续等待；失败/中断清理自己创建的supervisor，不盲杀旧PID。默认QTTS_RESIDENT=1，不再按600次/旧显存阈值周期回收；每worker独立单GPU仍保留，健康模型会话内驻留。Kaggle平台会话/配额/硬件回收不能保证永久。

当前step12独立282031字节47资产SHA256 2be33a3a6735639ce32ec8750e9a489abd96e4daa780d068557f2b0156f2de08；原始至step11冻结。浏览器复制页已换step12，正式15文件/HEAD不改；11题550建议，完整目标22/300保守不升级。下一步按KAGGLE_STEP12_QUICKSTART.md在完整重启会话后复跑两模型加载/warmup、显存和实际短句试听，不加工具前置。

## 22. 第十三阶段：修复step12未覆盖的实际延迟导入

用户再次实机失败，HF未加载警告不应放行。真实Faster wheel证明Qwen直到from_pretrained才导入，旧sys.modules判断错误跳过补丁。本次发行元数据分支、先验证再显式完整导入、HF smoke强制门禁；实际完整Faster/Qwen+微型Mimi构造/保存/重载三进程，冻结step12真实复现旧错误。原始至12冻结，step13为282346B/47资产，SHA256 dad142d75be94d8efb6567fc1f8755d3f37341a65d5c7fe9454fd36c87770e60。

完整三轮收据见step13/final-checks.json；12题600建议，完整目标22/300不变。实际两T4已识别但完整模型仍未加载成功，不能保证下一次实机必成。下一步直接完整会话重启后复制step13复跑，操作见KAGGLE_STEP13_QUICKSTART.md。

## 23. 第十四阶段：长录音/等价计算优化/原文与无额外呼吸

先三轮各100建议，再三题各50自问自答，完整15题750建议；方案见STEP14_PLAN。实际支持20分钟预算、缓存避免重复tokenize并保持CPU小LoRA参数逐位一致、梯度finite合并读取、HF版本报告、实际会话保留正文与默认无后加呼吸。48资产/285094B，SHA256 73a02a95919406c4570ea563f0c0475fdde17535e6ccd16764c32514fce2c369。

网页训练控制面、长音频逐条审核与维护态/真实训练/取消/恢复/部署闭环仍未完成；没有真实Qwen/T4训练、音质、首声、声学校验验收，不把CPU等价或虚拟录音当真人实验。本阶段整体PARTIAL/BLOCKED，完整目标22/300不升级。三轮结果以step14/final-checks.json为准。


## 24. 第十五阶段：参考隔离与可避免等待

三轮100建议、问题16–18各50建议后实施；累计18题900建议。Faster仅向量、禁参考PCM拼接；聊天首句无须等下一delta；输出-18dBFS/最大增益12dB；默认延后GPU校准，CPU ASR复用、构建内嵌入去重与阶段收据。两T4仍各一模型。冻结原始至14与正式工作台。真实Qwen/T4生成/韵律相似度/速度/创建A/B仍待现场，整体PARTIAL/BLOCKED，完整目标22/300不升级。见STEP15_PLAN/AUDIT/QUICKSTART与validation/step15。


## 25. 第十六阶段：相似度取舍修正、参考版本绑定与真实RTF门禁

三轮100建议/问题19–21各50后增量实施。默认恢复匹配转写ICL，但参考码不进codec；Go会话参考内容pin/模式与稳定seed，Worker锁内重读/校验、提示内存快照与同路径缓存失效。codec左25帧有界，实际causal结构tiny实验后默认前瞻0而非原拟2；每任务重置leveler、目标-18、默认最大增益6。提供实际双worker18条WAV/逐GPU标准及wall RTF门禁。真实相似/沙沙/0.3仍blocked，整体PARTIAL；不以CPU或Mock替代，不默认每T4双模型。原始至15与正式工作台冻结，完整目标22/300不变。


## 26. 第十七阶段：长参考对齐修复

截图15的28.7秒报错由长ASR段无短候选复现。17保留words并验证词文后切分，缺失则对实际短窗口重识别，不比例分全文；16默认/24实验锚点，源录音可长达既有预算，非全数据训练。v2指纹加四生成参数，较长朗读聚合不改聊天早触发，低输入RMS风险提示进现有处理决策。三轮100建议及问题22–24每题50后实施，累计24题1200；保留原始–16和工作台。真实音质/相似/无沙沙/双卡一致/自然度/RTF仍blocked，目标22/300不升级。

---

## 内嵌备忘录：KAGGLE_REVIEW_CHECKLIST.md

# Kaggle 双 T4 语音系统：三轮各100项审查清单

**状态：计划检查项，不是已发现的300个缺陷，也不是已经完成的300项修复。**

源码已收到并静态解包验证；首批历史报告见 `KAGGLE_SOURCE_AUDIT.md`；访问控制/容量证据见 `KAGGLE_SECURITY_AUDIT.md`，录音阶段见 `KAGGLE_STEP3_AUDIT.md`，历史两视图阶段见 `KAGGLE_STEP4_AUDIT.md`，历史命名库阶段见 `KAGGLE_STEP5_AUDIT.md`，不可变训练输入历史见 `KAGGLE_STEP6_AUDIT.md`，离线编码历史见 `KAGGLE_STEP7_AUDIT.md`，资源准入历史见 `KAGGLE_STEP8_AUDIT.md`，来源封存历史见 `KAGGLE_STEP9_AUDIT.md`，已有训练核心见 `KAGGLE_STEP10_AUDIT.md`，显式adapter推理/聊天接入见 `KAGGLE_STEP11_AUDIT.md`，当前Mimi/RoPE现场修复与会话驻留见 `KAGGLE_STEP12_AUDIT.md`。前5项源码交接、5项认证/凭据与5项有原生浏览器录音证据及3项两视图/视口条目与1项库名称/ID隔离、2项授权记录/固定清单及1项合作式资源锁设计已完成（共22项）；其余逐项验收尚未汇总完成，保持未勾选，不等于全部未开展。真实GPU验收仍阻塞，CPU/协议模拟不与GPU验收混同。

## 第一轮：源码与环境审查

- [x] R1-001：定位用户实际上传的kaggle源文件，缺失时停止逐行修复结论。
- [x] R1-002：记录源文件SHA256与文件大小，避免审查错误版本。
- [x] R1-003：识别Python脚本和Notebook格式，不把Notebook JSON直接当Python。
- [x] R1-004：保留用户原文件备份，不用默认示例覆盖。
- [x] R1-005：列出全部本地模块、动态生成文件与启动单元。
- [ ] R1-006：标记原有可用功能并建立回归基线。
- [ ] R1-007：梳理安装、下载、预处理、训练、推理、前端六个入口。
- [ ] R1-008：检查Notebook重复执行是否创建重复服务。
- [ ] R1-009：排查硬编码密码与API密钥，仅记录发现位置不输出秘密。
- [ ] R1-010：为每个真实缺陷记录复现步骤、行号和影响范围。
- [ ] R1-011：检查GPU数量是否实际为2，不能只根据平台选项判断。
- [ ] R1-012：记录每块GPU名称、compute capability与可用显存。
- [ ] R1-013：记录驱动、CUDA、PyTorch与Python版本。
- [ ] R1-014：验证两个worker分别绑定不同物理GPU。
- [ ] R1-015：禁止device_map=auto意外将同一模型切分到双卡。
- [ ] R1-016：避免训练主进程初始化CUDA后再不安全地fork。
- [ ] R1-017：使用spawn进程启动方式并防止Notebook递归启动。
- [ ] R1-018：对每个GPU分别执行独立最小推理。
- [ ] R1-019：区分双GPU吞吐与单段音频延迟，不能直接等同。
- [ ] R1-020：在GPU不可用时返回失败状态而不是模拟模型成功。
- [ ] R1-021：确认克隆模型是Qwen3-TTS-12Hz-1.7B-Base。
- [ ] R1-022：确认Tokenizer版本与模型相匹配。
- [ ] R1-023：固定模型权重revision并记录哈希。
- [ ] R1-024：核对官方Python接口签名，不猜测流式参数。
- [ ] R1-025：确认generate_voice_clone返回形式是否为整段波形。
- [ ] R1-026：确认所选后端确实支持增量声学输出。
- [ ] R1-027：区分Base、CustomVoice与VoiceDesign用途。
- [ ] R1-028：不假定Base支持任意自然语言情感指令。
- [ ] R1-029：核实clone prompt能否跨进程直接复用。
- [ ] R1-030：每块GPU独立构建并校验参考特征缓存。
- [ ] R1-031：T4默认研究FP16而不是直接复制BF16示例。
- [ ] R1-032：对SDPA可用内核做真实设备探测。
- [ ] R1-033：保留eager注意力可诊断回退而非静默换模型。
- [ ] R1-034：不默认安装面向Ampere的标准FlashAttention 2。
- [ ] R1-035：不把第三方Turing内核直接视作官方兼容。
- [ ] R1-036：检查推理算子是否出现CPU回退。
- [ ] R1-037：记录FP16非有限输出与溢出。
- [ ] R1-038：检查采样率、声道与波形类型的返回契约。
- [ ] R1-039：用torch.inference_mode限定推理路径。
- [ ] R1-040：为模型预热单独计时，不计入热启动首声成绩。
- [ ] R1-041：核实全部Python依赖的版本约束。
- [ ] R1-042：新建隔离环境，避免破坏Kaggle内置CUDA依赖。
- [ ] R1-043：不无条件升级torch或卸载平台GPU运行库。
- [ ] R1-044：安装前检查磁盘容量与网络权限。
- [ ] R1-045：下载失败保留可诊断错误并支持续传。
- [ ] R1-046：验证下载文件完整性，不能只检查目录存在。
- [ ] R1-047：对冷启动依赖下载显示阶段进度。
- [ ] R1-048：移除每次聊天重复pip安装与模型加载。
- [ ] R1-049：安装日志不包含密钥或私人音频内容。
- [ ] R1-050：生成可重复执行的依赖锁定清单。
- [ ] R1-051：把会话内驻留与跨会话持久化分开描述。
- [ ] R1-052：不承诺Kaggle会话永久运行。
- [ ] R1-053：记录当前平台配额与会话条件，不能写死永久时长。
- [ ] R1-054：为结束会话前导出语音库设计操作入口。
- [ ] R1-055：明确/kaggle/working不是无条件永久存储。
- [ ] R1-056：对恢复的模型与数据执行校验。
- [ ] R1-057：保存模型版本、适配器版本和语音库清单。
- [ ] R1-058：重启后自动发现有效资产但不自动开始收费请求。
- [ ] R1-059：缺少持久化资产时提示重新挂载而非假恢复。
- [ ] R1-060：不使用规避平台会话限制的保活方案。
- [ ] R1-061：核实官方训练脚本实际优化哪些参数。
- [ ] R1-062：估算全参数AdamW权重、梯度、主副本与状态开销。
- [ ] R1-063：不将两块16GB显存简单相加给DDP每卡使用。
- [ ] R1-064：训练前用最小样本测量峰值显存。
- [ ] R1-065：验证LoRA是否兼容目标层与语音架构。
- [ ] R1-066：通过named_modules确定适配层而不是随意猜名字。
- [ ] R1-067：冻结不训练的参数并统计可训练参数数量。
- [ ] R1-068：检查梯度checkpoint与缓存设置是否冲突。
- [ ] R1-069：检查模型训练包装后的属性访问是否支持DDP。
- [ ] R1-070：对分布式保存与恢复做独立可复现实验。
- [ ] R1-071：建立参考音频上传与实际训练的独立状态机。
- [ ] R1-072：不把create_voice_clone_prompt标注成微调训练。
- [x] R1-073：音频库名称使用内部ID，显示名称与磁盘路径分离。
- [ ] R1-074：上传前必须选定或创建语音库。
- [ ] R1-075：音频条目包含来源、时长、采样率和转写。
- [ ] R1-076：检查所有音频解码工具是否存在。
- [ ] R1-077：按实际格式解码，不能只相信文件后缀。
- [ ] R1-078：拒绝空音频、损坏数据与明显静音。
- [x] R1-079：记录训练授权和声音使用同意。
- [ ] R1-080：不得从多个不同说话人混合出单说话人训练集。
- [ ] R1-081：训练数据每条必须有匹配转写。
- [ ] R1-082：自动转写结果允许人工修正。
- [ ] R1-083：检查语言标签和文本正规化规则。
- [ ] R1-084：保留原始音频，预处理输出单独存储。
- [ ] R1-085：对削波、噪声和过短语音提示质量问题。
- [ ] R1-086：限制单次上传大小与总存储额度。
- [ ] R1-087：明确任意数量输入采用分批任务，不承诺无限资源。
- [ ] R1-088：为重复音频提供哈希去重。
- [ ] R1-089：训练和验证按音频来源拆分，避免片段泄漏。
- [ ] R1-090：记录被过滤音频及原因而不是静默跳过。
- [ ] R1-091：扫描HTTP接口的任意路径读写风险。
- [x] R1-092：检查暴露网站的认证与访问令牌。
- [ ] R1-093：DeepSeek密钥仅放服务端配置与安全环境变量。
- [x] R1-094：不把密钥写入前端localStorage或下载包。
- [ ] R1-095：限制出站API地址，防止任意URL导致SSRF。
- [ ] R1-096：检查异常日志是否泄漏请求头。
- [ ] R1-097：为上传、训练和聊天设置请求容量限制。
- [ ] R1-098：核实浏览器录音需要HTTPS和用户权限。
- [ ] R1-099：对跨站写入与WebSocket Origin进行验证。
- [ ] R1-100：完成首轮后输出证据、待办和阻塞，不编造100个已修缺陷。

## 第二轮：训练、双卡与流式链路

- [ ] R2-001：把推理与训练定义为互斥的GPU资源模式。
- [ ] R2-002：训练前停止接收新推理任务并提示服务状态。
- [ ] R2-003：显式取消或排空旧任务后再释放推理显存。
- [ ] R2-004：训练结束后仅在检查点验证通过时恢复推理。
- [ ] R2-005：恢复时将选定模型分别加载到两块GPU。
- [ ] R2-006：防止同时常驻推理副本和全参数训练造成OOM。
- [ ] R2-007：训练失败保留上一可用模型和语音库。
- [ ] R2-008：资源不足时报告原因，不静默降成0.6B。
- [ ] R2-009：检查模型卸载后实际可回收显存。
- [x] R2-010：设计GPU资源所有权锁与超时恢复。
- [ ] R2-011：使用两个真实rank参与同一个训练作业。
- [ ] R2-012：确认每个rank的设备映射和分布式world_size。
- [ ] R2-013：用分布式采样器划分数据而非重复整套样本。
- [ ] R2-014：每轮调用set_epoch更新采样顺序。
- [ ] R2-015：统计原始样本ID的跨rank覆盖情况。
- [ ] R2-016：不因drop_last让选定样本长期不参与训练。
- [ ] R2-017：不能整除world_size时标明填充或重复样本策略。
- [ ] R2-018：记录每rank步数与梯度同步次数。
- [ ] R2-019：显式同步训练异常，避免另一rank永久挂起。
- [ ] R2-020：验证两卡训练不是并行执行两个独立微调。
- [ ] R2-021：FP16训练启用相应GradScaler与溢出检查。
- [ ] R2-022：只对可训练参数创建优化器状态。
- [ ] R2-023：使用梯度累积降低单卡微批显存。
- [ ] R2-024：记录有效全局batch的实际计算方式。
- [ ] R2-025：验证loss有限并实际发生参数更新。
- [ ] R2-026：记录每轮耗时、已见样本数和学习率。
- [ ] R2-027：避免将loss降低等同音色相似度提升。
- [ ] R2-028：支持用户取消后保存可恢复状态。
- [ ] R2-029：验证取消操作对两个rank同时生效。
- [ ] R2-030：防止训练进程结束后留下占显存子进程。
- [x] R2-031：训练清单固定所选音频ID和内容哈希。
- [ ] R2-032：任务启动后音频编辑不改变运行中的数据集。
- [ ] R2-033：音频编码准备阶段显示真实进度。
- [ ] R2-034：保留原始JSONL、分词版本与声学码版本。
- [ ] R2-035：明确保存优化器、调度器和随机数状态需求。
- [ ] R2-036：所有rank按后端要求参与检查点状态收集。
- [ ] R2-037：只有指定写入进程发布最终清单。
- [ ] R2-038：检查点临时目录校验后再原子切换。
- [ ] R2-039：按训练后端正确处理分片或完整state_dict。
- [ ] R2-040：使用新进程加载检查点完成独立试听。
- [ ] R2-041：为单说话人微调保存说话人ID映射。
- [ ] R2-042：保存适配器与基础权重revision的绑定关系。
- [ ] R2-043：不混淆Base克隆接口与训练后CustomVoice接口。
- [ ] R2-044：对多个语音库采用各自版本，不覆盖全局共享状态。
- [ ] R2-045：推理任务携带不可变的voice_revision。
- [ ] R2-046：检查切换语音时缓存键包含模型版本。
- [ ] R2-047：为旧模型引用计数，避免在途推理使用已卸载权重。
- [ ] R2-048：保留模型切换失败回滚路径。
- [ ] R2-049：对同一语音两块GPU生成的音频做一致性抽样。
- [ ] R2-050：训练完整性报告列出选中、有效、已见和排除样本数量。
- [ ] R2-051：DeepSeek以流式模式读取增量文本。
- [ ] R2-052：API模型名称按供应商实际能力配置。
- [ ] R2-053：分别配置输出预算与上下文预算。
- [ ] R2-054：处理finish_reason=length与长文截断。
- [ ] R2-055：避免在第一句之前等待完整长回答。
- [ ] R2-056：为中文句号、问号、感叹号定义切句规则。
- [ ] R2-057：为无标点长文本提供最大等待时间与长度边界。
- [ ] R2-058：保护代码块、小数、URL和缩写不被错误切断。
- [ ] R2-059：记录切句器尚未消费的尾部文本。
- [ ] R2-060：结束流时刷新最后一个不完整句子。
- [ ] R2-061：为每轮聊天生成turn_id。
- [ ] R2-062：为每段文本生成递增segment_id。
- [ ] R2-063：两个GPU按任务队列工作而不是前端并发无序播放。
- [ ] R2-064：首个短段优先调度至空闲且已预热的worker。
- [ ] R2-065：后续段适度增大，以减少句间重启成本。
- [ ] R2-066：限制预合成队列长度，防止长输出撑爆内存。
- [ ] R2-067：对慢段实施顺序等待，不能跳过内容。
- [ ] R2-068：记录各段音频采样率与长度。
- [ ] R2-069：重采样至统一播放格式后再进入浏览器队列。
- [ ] R2-070：不对尚未实现的token级流式接口作虚假声明。
- [ ] R2-071：用WebSocket或流式HTTP传送明确的音频元数据。
- [ ] R2-072：为每个音频包携带turn、segment、chunk和版本信息。
- [ ] R2-073：音频数据采用确定字节序和波形编码。
- [ ] R2-074：处理传输分片、半包和重复包。
- [ ] R2-075：浏览器按样本时钟而不是收到即play调度。
- [ ] R2-076：使用同一AudioContext播放时钟。
- [ ] R2-077：首次用户操作中显式解锁音频上下文。
- [ ] R2-078：为自动播放被拒提供可见的开始播放入口。
- [ ] R2-079：设计有界预缓冲与可观测欠载计数。
- [ ] R2-080：不靠无限预缓冲掩盖首声延迟不达标。
- [ ] R2-081：使用连续PCM调度或AudioWorklet环形队列。
- [ ] R2-082：每块音频采用相同声道与采样率。
- [ ] R2-083：必要时用短交叉淡化消除拼接爆音。
- [ ] R2-084：不得用交叉淡化掩盖句子丢失或重复。
- [ ] R2-085：保存浏览器已排程的所有音频节点。
- [ ] R2-086：打断时停止节点并清空尚未播放队列。
- [ ] R2-087：发送取消信号至DeepSeek读取任务。
- [ ] R2-088：通过生成停止条件取消GPU任务，而不仅关闭界面。
- [ ] R2-089：旧turn迟到音频一律丢弃。
- [ ] R2-090：新输入不等待旧整段合成完成才进入调度。
- [ ] R2-091：麦克风输入与播放回声处理分开设计。
- [ ] R2-092：用户按住或点击语音输入时明确定义打断时点。
- [ ] R2-093：为语音识别提供可选本地后端和文本输入兜底。
- [ ] R2-094：不能将浏览器Web Speech API视为所有浏览器通用。
- [x] R2-095：录音权限失败时保留上传功能。
- [x] R2-096：录音状态以真实MediaRecorder或采样状态驱动。
- [x] R2-097：波形来自AnalyserNode实际信号，而不是假动画。
- [x] R2-098：停止录音后关闭所有麦克风track。
- [ ] R2-099：参考录音不能误发送为聊天输入。
- [ ] R2-100：第二轮输出瓶颈数据和未达标项，不承诺理论性能就是实测结果。

## 第三轮：端到端实验与交付验收

- [ ] R3-001：启动时检查两块GPU的模型加载状态。
- [ ] R3-002：只有两块GPU独立推理成功才显示双卡就绪。
- [ ] R3-003：分别记录冷启动和热启动时间。
- [ ] R3-004：固定性能样本的语言、长度与语音版本。
- [ ] R3-005：对同一请求记录统一时间线和关联ID。
- [ ] R3-006：记录用户提交至DeepSeek首token的延迟。
- [ ] R3-007：记录首个文本段形成的延迟。
- [ ] R3-008：记录GPU排队与模型首声学输出的延迟。
- [ ] R3-009：记录编码、传输和浏览器预缓冲的延迟。
- [ ] R3-010：以实际可听首样本而不是接口返回计算首声。
- [ ] R3-011：首声目标3秒必须注明硬件、网络和预热条件。
- [ ] R3-012：同时报告P50与P95而不是挑选最快一次。
- [ ] R3-013：公布超时比例与最慢样本。
- [ ] R3-014：统计取消请求时不要混入成功首声分位数。
- [ ] R3-015：对未开始播放的失败请求单独报告。
- [ ] R3-016：说明浏览器时间与服务端时间如何关联。
- [ ] R3-017：分别报告端到端RTF和纯TTS RTF。
- [ ] R3-018：用生成耗时除以音频时长计算RTF。
- [ ] R3-019：双卡聚合吞吐与单流RTF分开报告。
- [ ] R3-020：RTF不达0.5时不得自动写成通过。
- [ ] R3-021：测量连续播放中的队列欠载次数。
- [ ] R3-022：区分自然语言停顿与系统缓冲断音。
- [ ] R3-023：记录丢包、重传和乱序恢复计数。
- [ ] R3-024：使用长回答验证后半段不会耗尽缓冲。
- [ ] R3-025：使用无标点回答验证切句器上限。
- [ ] R3-026：使用中英混合文本验证正规化。
- [ ] R3-027：使用多轮上下文验证供应商上下文边界。
- [ ] R3-028：模拟供应商限流并验证有界重试。
- [ ] R3-029：模拟DeepSeek中途断流且不重复播已说文本。
- [ ] R3-030：不在同一turn中无提示地重试产生另一份回答。
- [ ] R3-031：按不同输入长度重复首声测量。
- [ ] R3-032：按两张卡分别测量相同文本RTF。
- [ ] R3-033：记录峰值显存、CPU、内存和网络流量。
- [ ] R3-034：用两卡负载不均场景验证调度。
- [ ] R3-035：用worker崩溃验证队列清理和恢复。
- [ ] R3-036：用GPU OOM验证服务退回可诊断状态。
- [ ] R3-037：用上传大文件验证资源限制。
- [ ] R3-038：用异常音频验证解码失败不影响其他库。
- [ ] R3-039：用零条有效样本验证训练按钮不会假成功。
- [ ] R3-040：用训练取消验证没有残留GPU任务。
- [ ] R3-041：定义训练完成必须包含已见样本和检查点记录。
- [ ] R3-042：验证全部选中有效样本跨rank至少被读取。
- [ ] R3-043：记录不能接受样本的排除清单。
- [ ] R3-044：训练轮次与数据完整性分开验收。
- [ ] R3-045：用恢复训练验证步数与模型版本正确。
- [ ] R3-046：用停止Notebook后重启流程验证资产恢复。
- [ ] R3-047：从干净环境执行安装与启动单元。
- [ ] R3-048：清理仅缓存数据后重新运行可用性测试。
- [ ] R3-049：验证已有资产不会被初始化示例覆盖。
- [ ] R3-050：验证失败的训练检查点不替代最后可用版本。
- [ ] R3-051：定义音色相似度的模型、维度和计算方式。
- [ ] R3-052：不把cosine=0.995直接解释为99.5%人声一致。
- [ ] R3-053：使用未参与训练的参考与文本评估。
- [ ] R3-054：对内容正确性统计CER或WER。
- [ ] R3-055：对情感、节奏、音质分别设置主观评价项。
- [ ] R3-056：进行盲听而不是只由开发者选最好样本。
- [ ] R3-057：记录参考音频环境差异对结果的影响。
- [ ] R3-058：不强制降噪或音高处理导致身份特征丢失。
- [ ] R3-059：记录随机种子与生成采样参数。
- [ ] R3-060：相似度目标未达到时展示实际值与评估限制。
- [x] R3-061：参考语音界面与对话界面保持两个明显入口。
- [x] R3-062：页面适配常见桌面和手机视口。
- [x] R3-063：主要操作无需页面纵向滚动。
- [ ] R3-064：音频列表超量时分页而非无限增长撑开页面。
- [ ] R3-065：训练日志使用分页或切换详情面板。
- [ ] R3-066：窄屏不强行隐藏重要错误或控制按钮。
- [x] R3-067：录音按钮显示开始、停止、时长和权限状态。
- [ ] R3-068：波形在静音时仍保持录音状态标签可见。
- [ ] R3-069：录音、上传、转写和训练采用独立状态。
- [ ] R3-070：对话页面可随时选声音但切换策略明确。
- [ ] R3-071：切换声音时在途段使用旧版本或统一取消，不能混音色。
- [ ] R3-072：语音库删除必须确认并处理正在使用的版本。
- [ ] R3-073：语音库重命名不改变内部ID。
- [ ] R3-074：删除音频不破坏已发布检查点的可追溯清单。
- [x] R3-075：API密钥输入框不回显已保存密钥。
- [ ] R3-076：后端只返回是否已配置及验证结果。
- [ ] R3-077：配置测试不发起意外长文本收费请求。
- [x] R3-078：会话令牌与DeepSeek密钥分离。
- [x] R3-079：公开访问入口默认要求认证。
- [ ] R3-080：导出的代码和日志不得含实际秘密。
- [ ] R3-081：为Kaggle复制按钮明确所复制文件与版本。
- [ ] R3-082：复制完整Python源码而不是网页HTML。
- [ ] R3-083：Notebook需要明确导出为代码单元，不盲拼魔法命令。
- [ ] R3-084：提供复制失败后的手动选择兜底。
- [ ] R3-085：复制成功不宣称运行验证成功。
- [ ] R3-086：提供依赖单元和启动单元的执行顺序。
- [ ] R3-087：验证复制代码的哈希与原交付文件一致。
- [ ] R3-088：下载包包含README、依赖锁定和许可证。
- [ ] R3-089：模型、音频和训练权重不提交到Git。
- [ ] R3-090：保留现有编辑、保存、命名和预览回归测试。
- [ ] R3-091：第一遍端到端覆盖正常录音、训练与聊天。
- [ ] R3-092：第二遍端到端覆盖异常、取消与打断。
- [ ] R3-093：第三遍端到端覆盖重启、长回答和持续播放。
- [ ] R3-094：每遍记录硬件环境、用例数与失败截图。
- [ ] R3-095：单元模拟通过不得代替真实GPU测试。
- [ ] R3-096：公开未实现功能列表，不用占位按钮表示完成。
- [ ] R3-097：所有修复都关联真实源码位置和对应测试。
- [ ] R3-098：为版本发布保留可回滚方案。
- [ ] R3-099：将决策、清单、命令和阻塞汇总到单一提示词。
- [ ] R3-100：缺少源文件、GPU、模型或API时暂停相应验收结论。


第四阶段新增R3-061/062/063的证据限定为所列五个Chromium CSS视口；≤640px高允许页面滚动，实际虚拟键盘/OS缩放未验。内部滚动不等于分页，未勾R3-064。完整日志KAGGLE_STEP4_AUDIT.md。

第八阶段新增R2-010仅覆盖同机同UID合作式整组所有权锁、有界预约和进程/最后描述符退出恢复设计与真实CPU进程验证；不是跨UID/容器隔离、自动训练模式或实际显存回收验收，R2-001/003/006/009/011等仍未勾选。

第九阶段已补强R1-079与R2-031的来源证据及删除互斥，但没有完整训练器/分词版本/DDP数据生命周期，不勾R2-032或R2-034。保持22/300。当前8题400建议不是400项验收。

第十阶段实际训练代码已开发，CPU真实张量/Gloo有梯度/参数更新与跨rank一致证据；不因尚无GPU验收而称“未开始开发”。R2-011/012/025/040等真正Qwen/CUDA目标仍未验收，维持22/300；9题450建议。此分母是目标验收，不是代码开发进度。

第十三阶段：保留300个目标ID和22勾选；新增三轮各100条定向开发建议见validation/step13/review-map.json。明确修复step12延迟导入漏测，不把完整包导入/CPU微型Mimi当真实1.7B/T4加载。12题600建议，三轮结果以step13/final-checks.json为准。

第十四阶段三轮各100建议及逐项处置独立记录，完整清单仍22/300。录音/缓存/原文/额外呼吸代码范围和真正网页训练控制闭环分开，后者未完成；15题750建议，不是750修复。


## 第十五阶段追加状态（不替换完整目标勾选）

REVIEW1/2/3各100定向建议，问题16–18各50建议，处置见step15/review-disposition.json；不是300个bug或900项已实现功能。本轮向量隔离/首句/有界增响/创建复用工程回归与真实T4声学/性能分开，仍缺目标机验收及历史网页训练闭环。完整目标仍22/300，不因CPU/Mock通过自动升级。

---

## 内嵌备忘录：KAGGLE_DECISIONS.md

# 专业决策备忘录（历史决策＋源码到齐后的状态更新）

**2026-10-21：源码现已到齐并保留。** 下列9个问题及每题50条建议保留其历史推理顺序；其中“缺少源码”的输入状态已解除，不再向用户索取同一文件。首批历史修复见 `KAGGLE_SOURCE_AUDIT.md`；认证/资源预算历史证据见 `KAGGLE_SECURITY_AUDIT.md`，兼容探针与原生录音证据见 `KAGGLE_STEP3_AUDIT.md`，两主视图/视口历史证据见 `KAGGLE_STEP4_AUDIT.md`，命名空库/参考样本历史见 `KAGGLE_STEP5_AUDIT.md`，训练输入历史见 `KAGGLE_STEP6_AUDIT.md`，来源封存历史见 `KAGGLE_STEP9_AUDIT.md`，当前训练核心见 `KAGGLE_STEP10_AUDIT.md`。实验性训练核心已开发，真实Qwen/GPU执行仍待验证；历史建议完整保留，当前第9题后累计450条建议。

## 问题1：没有原始kaggle代码时，应选择直接重写，还是先锁定源码和验收边界？

选项A：凭描述编写替代品并宣称修好；选项B：先定位原文件，保留基线，完成有依据的设计与可独立交付部分。推荐并选择B。缺少原文件时不能知道真实报错，也不能承诺保持其成功功能。继续追问的焦点是设备与训练语义。

### 本问题之后的50项具体实施建议

1. [R1-001] 定位用户实际上传的kaggle源文件，缺失时停止逐行修复结论。
2. [R1-002] 记录源文件SHA256与文件大小，避免审查错误版本。
3. [R1-003] 识别Python脚本和Notebook格式，不把Notebook JSON直接当Python。
4. [R1-004] 保留用户原文件备份，不用默认示例覆盖。
5. [R1-005] 列出全部本地模块、动态生成文件与启动单元。
6. [R1-006] 标记原有可用功能并建立回归基线。
7. [R1-007] 梳理安装、下载、预处理、训练、推理、前端六个入口。
8. [R1-008] 检查Notebook重复执行是否创建重复服务。
9. [R1-009] 排查硬编码密码与API密钥，仅记录发现位置不输出秘密。
10. [R1-010] 为每个真实缺陷记录复现步骤、行号和影响范围。
11. [R1-011] 检查GPU数量是否实际为2，不能只根据平台选项判断。
12. [R1-012] 记录每块GPU名称、compute capability与可用显存。
13. [R1-013] 记录驱动、CUDA、PyTorch与Python版本。
14. [R1-014] 验证两个worker分别绑定不同物理GPU。
15. [R1-015] 禁止device_map=auto意外将同一模型切分到双卡。
16. [R1-016] 避免训练主进程初始化CUDA后再不安全地fork。
17. [R1-017] 使用spawn进程启动方式并防止Notebook递归启动。
18. [R1-018] 对每个GPU分别执行独立最小推理。
19. [R1-019] 区分双GPU吞吐与单段音频延迟，不能直接等同。
20. [R1-020] 在GPU不可用时返回失败状态而不是模拟模型成功。
21. [R1-021] 确认克隆模型是Qwen3-TTS-12Hz-1.7B-Base。
22. [R1-022] 确认Tokenizer版本与模型相匹配。
23. [R1-023] 固定模型权重revision并记录哈希。
24. [R1-024] 核对官方Python接口签名，不猜测流式参数。
25. [R1-025] 确认generate_voice_clone返回形式是否为整段波形。
26. [R1-026] 确认所选后端确实支持增量声学输出。
27. [R1-027] 区分Base、CustomVoice与VoiceDesign用途。
28. [R1-028] 不假定Base支持任意自然语言情感指令。
29. [R1-029] 核实clone prompt能否跨进程直接复用。
30. [R1-030] 每块GPU独立构建并校验参考特征缓存。
31. [R1-031] T4默认研究FP16而不是直接复制BF16示例。
32. [R1-032] 对SDPA可用内核做真实设备探测。
33. [R1-033] 保留eager注意力可诊断回退而非静默换模型。
34. [R1-034] 不默认安装面向Ampere的标准FlashAttention 2。
35. [R1-035] 不把第三方Turing内核直接视作官方兼容。
36. [R1-036] 检查推理算子是否出现CPU回退。
37. [R1-037] 记录FP16非有限输出与溢出。
38. [R1-038] 检查采样率、声道与波形类型的返回契约。
39. [R1-039] 用torch.inference_mode限定推理路径。
40. [R1-040] 为模型预热单独计时，不计入热启动首声成绩。
41. [R1-041] 核实全部Python依赖的版本约束。
42. [R1-042] 新建隔离环境，避免破坏Kaggle内置CUDA依赖。
43. [R1-043] 不无条件升级torch或卸载平台GPU运行库。
44. [R1-044] 安装前检查磁盘容量与网络权限。
45. [R1-045] 下载失败保留可诊断错误并支持续传。
46. [R1-046] 验证下载文件完整性，不能只检查目录存在。
47. [R1-047] 对冷启动依赖下载显示阶段进度。
48. [R1-048] 移除每次聊天重复pip安装与模型加载。
49. [R1-049] 安装日志不包含密钥或私人音频内容。
50. [R1-050] 生成可重复执行的依赖锁定清单。

## 问题2：双T4是否应在训练时继续各常驻一个推理副本？

选项A：不做显存预算，同时运行两份推理与双卡全参数训练；选项B：会话内双副本推理，训练期间独占两卡，验证并恢复双副本。推荐并选择B。这是明确的资源模式切换，不假装同时满足互相冲突的显存承诺。LoRA等低内存路径仍需真实模型验证。继续追问的焦点是流式首声与播放。

### 本问题之后的50项具体实施建议

1. [R2-001] 把推理与训练定义为互斥的GPU资源模式。
2. [R2-002] 训练前停止接收新推理任务并提示服务状态。
3. [R2-003] 显式取消或排空旧任务后再释放推理显存。
4. [R2-004] 训练结束后仅在检查点验证通过时恢复推理。
5. [R2-005] 恢复时将选定模型分别加载到两块GPU。
6. [R2-006] 防止同时常驻推理副本和全参数训练造成OOM。
7. [R2-007] 训练失败保留上一可用模型和语音库。
8. [R2-008] 资源不足时报告原因，不静默降成0.6B。
9. [R2-009] 检查模型卸载后实际可回收显存。
10. [R2-010] 设计GPU资源所有权锁与超时恢复。
11. [R2-011] 使用两个真实rank参与同一个训练作业。
12. [R2-012] 确认每个rank的设备映射和分布式world_size。
13. [R2-013] 用分布式采样器划分数据而非重复整套样本。
14. [R2-014] 每轮调用set_epoch更新采样顺序。
15. [R2-015] 统计原始样本ID的跨rank覆盖情况。
16. [R2-016] 不因drop_last让选定样本长期不参与训练。
17. [R2-017] 不能整除world_size时标明填充或重复样本策略。
18. [R2-018] 记录每rank步数与梯度同步次数。
19. [R2-019] 显式同步训练异常，避免另一rank永久挂起。
20. [R2-020] 验证两卡训练不是并行执行两个独立微调。
21. [R2-021] FP16训练启用相应GradScaler与溢出检查。
22. [R2-022] 只对可训练参数创建优化器状态。
23. [R2-023] 使用梯度累积降低单卡微批显存。
24. [R2-024] 记录有效全局batch的实际计算方式。
25. [R2-025] 验证loss有限并实际发生参数更新。
26. [R2-026] 记录每轮耗时、已见样本数和学习率。
27. [R2-027] 避免将loss降低等同音色相似度提升。
28. [R2-028] 支持用户取消后保存可恢复状态。
29. [R2-029] 验证取消操作对两个rank同时生效。
30. [R2-030] 防止训练进程结束后留下占显存子进程。
31. [R2-031] 训练清单固定所选音频ID和内容哈希。
32. [R2-032] 任务启动后音频编辑不改变运行中的数据集。
33. [R2-033] 音频编码准备阶段显示真实进度。
34. [R2-034] 保留原始JSONL、分词版本与声学码版本。
35. [R2-035] 明确保存优化器、调度器和随机数状态需求。
36. [R2-036] 所有rank按后端要求参与检查点状态收集。
37. [R2-037] 只有指定写入进程发布最终清单。
38. [R2-038] 检查点临时目录校验后再原子切换。
39. [R2-039] 按训练后端正确处理分片或完整state_dict。
40. [R2-040] 使用新进程加载检查点完成独立试听。
41. [R2-041] 为单说话人微调保存说话人ID映射。
42. [R2-042] 保存适配器与基础权重revision的绑定关系。
43. [R2-043] 不混淆Base克隆接口与训练后CustomVoice接口。
44. [R2-044] 对多个语音库采用各自版本，不覆盖全局共享状态。
45. [R2-045] 推理任务携带不可变的voice_revision。
46. [R2-046] 检查切换语音时缓存键包含模型版本。
47. [R2-047] 为旧模型引用计数，避免在途推理使用已卸载权重。
48. [R2-048] 保留模型切换失败回滚路径。
49. [R2-049] 对同一语音两块GPU生成的音频做一致性抽样。
50. [R2-050] 训练完整性报告列出选中、有效、已见和排除样本数量。

## 问题3：如何处理3秒首声、连续播放和打断，而不虚构硬件性能？

选项A：整段生成完再播放并把HTTP响应时间当首声；选项B：先验证后端真实流式能力，再做文本增量、序号队列、统一样本时钟与整链路取消，实测后报告。推荐并选择B。若官方包装器或T4不支持所需增量声学输出，必须记录技术试验失败与替代方案，不能把分句整段生成冒称token级流式。此决策形成时缺少源码；现在源码已到齐并完成CPU协议回归，真实模型和GPU环境仍阻塞，不能宣布100%确定。

### 本问题之后的50项具体实施建议

1. [R2-051] DeepSeek以流式模式读取增量文本。
2. [R2-052] API模型名称按供应商实际能力配置。
3. [R2-053] 分别配置输出预算与上下文预算。
4. [R2-054] 处理finish_reason=length与长文截断。
5. [R2-055] 避免在第一句之前等待完整长回答。
6. [R2-056] 为中文句号、问号、感叹号定义切句规则。
7. [R2-057] 为无标点长文本提供最大等待时间与长度边界。
8. [R2-058] 保护代码块、小数、URL和缩写不被错误切断。
9. [R2-059] 记录切句器尚未消费的尾部文本。
10. [R2-060] 结束流时刷新最后一个不完整句子。
11. [R2-061] 为每轮聊天生成turn_id。
12. [R2-062] 为每段文本生成递增segment_id。
13. [R2-063] 两个GPU按任务队列工作而不是前端并发无序播放。
14. [R2-064] 首个短段优先调度至空闲且已预热的worker。
15. [R2-065] 后续段适度增大，以减少句间重启成本。
16. [R2-066] 限制预合成队列长度，防止长输出撑爆内存。
17. [R2-067] 对慢段实施顺序等待，不能跳过内容。
18. [R2-068] 记录各段音频采样率与长度。
19. [R2-069] 重采样至统一播放格式后再进入浏览器队列。
20. [R2-070] 不对尚未实现的token级流式接口作虚假声明。
21. [R2-071] 用WebSocket或流式HTTP传送明确的音频元数据。
22. [R2-072] 为每个音频包携带turn、segment、chunk和版本信息。
23. [R2-073] 音频数据采用确定字节序和波形编码。
24. [R2-074] 处理传输分片、半包和重复包。
25. [R2-075] 浏览器按样本时钟而不是收到即play调度。
26. [R2-076] 使用同一AudioContext播放时钟。
27. [R2-077] 首次用户操作中显式解锁音频上下文。
28. [R2-078] 为自动播放被拒提供可见的开始播放入口。
29. [R2-079] 设计有界预缓冲与可观测欠载计数。
30. [R2-080] 不靠无限预缓冲掩盖首声延迟不达标。
31. [R2-081] 使用连续PCM调度或AudioWorklet环形队列。
32. [R2-082] 每块音频采用相同声道与采样率。
33. [R2-083] 必要时用短交叉淡化消除拼接爆音。
34. [R2-084] 不得用交叉淡化掩盖句子丢失或重复。
35. [R2-085] 保存浏览器已排程的所有音频节点。
36. [R2-086] 打断时停止节点并清空尚未播放队列。
37. [R2-087] 发送取消信号至DeepSeek读取任务。
38. [R2-088] 通过生成停止条件取消GPU任务，而不仅关闭界面。
39. [R2-089] 旧turn迟到音频一律丢弃。
40. [R2-090] 新输入不等待旧整段合成完成才进入调度。
41. [R2-091] 麦克风输入与播放回声处理分开设计。
42. [R2-092] 用户按住或点击语音输入时明确定义打断时点。
43. [R2-093] 为语音识别提供可选本地后端和文本输入兜底。
44. [R2-094] 不能将浏览器Web Speech API视为所有浏览器通用。
45. [R2-095] 录音权限失败时保留上传功能。
46. [R2-096] 录音状态以真实MediaRecorder或采样状态驱动。
47. [R2-097] 波形来自AnalyserNode实际信号，而不是假动画。
48. [R2-098] 停止录音后关闭所有麦克风track。
49. [R2-099] 参考录音不能误发送为聊天输入。
50. [R2-100] 第二轮输出瓶颈数据和未达标项，不承诺理论性能就是实测结果。


## 问题4：空声音库、原始参考与训练产物是否合放profiles并用同一个“训练成功”状态？

选项A：直接创建空profile，保存样本后标为训练完成；选项B：独立命名空库和原始样本存储，显式勾选后调用现有参考处理，真实训练另设硬件门禁。推荐并选择B。阶段计划先保存于KAGGLE_STEP5_PLAN.md，再实现并记录以下50项建议；不再向用户重复提问，也不进入下一个专业问题冒充训练已完成。

### 本问题的50项具体实施与后续建议

1. 将原始库放STATE/libraries，不复用profiles目录。
2. 自定义空库名称，不预填示例或自动命名。
3. 对名称做NFC标准化、去首尾空白与64码点上限。
4. 内部路径只用随机UUID，不拼显示名称。
5. 同名库按大小写折叠拒绝，提示选择原库。
6. 建库不要求音频、不加载模型、不生成假档案。
7. 保留旧的一步创建档案入口与请求格式。
8. 库管理采用辅助dialog，不加第三主导航。
9. 在手机常驻可找到的区域提供管理入口。
10. 允许建库后回到采集页录音，再添加该本地片段。
11. 打开库窗口停止麦克风并保留有效片段。
12. 窗口关闭/Escape恢复入口焦点。
13. 锁定关闭窗口并清空服务端样本名称与文件选择。
14. 为所有异步操作增加访问代际与窗口代际检查。
15. 不假定AbortSignal能撤回已提交的服务端写入。
16. 服务端修订CAS防止旧窗口覆盖新样本清单。
17. 所有库路由继续走单用户认证代理。
18. 只有精确samples上传路径使用较大请求预算。
19. 保持process/删除/建库的JSON请求预算。
20. 拒绝重复JSON字段、非有限常量与未知字段。
21. 限制库数量，避免无限空目录。
22. 限制每库样本数和每文件字节数。
23. 限制每库与全部库的原始音频总字节数。
24. 写入前保留磁盘余量，但不把这称作OS配额。
25. 文件名仅用于显示并去掉目录和控制字符。
26. 以SHA256对同库相同内容去重。
27. 保存样本ID、内容哈希、大小与创建时间。
28. 不从扩展名推断已经成功解码。
29. 不把浏览器墙钟当服务端编码时长。
30. 在真正参考处理阶段再次应用解码时长预算。
31. 原子替换清单，避免并发共享临时文件。
32. 样本写失败或清单提交失败回滚本次新文件。
33. 下一次库修改回收未引用音频/临时文件。
34. 损坏清单报错，不用空清单覆盖真实数据。
35. 创建0700目录和0600文件。
36. 拒绝库路径/清单/参考样本软链接或文件硬链接。
37. 使用Linux flock，而非进程重启后永久busy布尔值。
38. 构建期间禁止同库上传、移除样本和删除库。
39. 固定本次勾选的ID与字节快照，不把后续上传混入运行任务。
40. 复用已有构建准入，避免新旧接口同时占GPU处理。
41. 让HTTP取消与后台线程接管处于同一个准入函数。
42. 只有库结果成功提交后才公开任务终态。
43. 处理失败保留原件及以前成功产生的独立档案。
44. 进程死亡释放租约；遗留running显示interrupted。
45. 原始库不自动加入Dataset，明确会话目录不保证永久。
46. 提醒处理后的锚点/转写仍遵循已有档案备份设置。
47. 删除原始库不连带删除档案，也不承诺安全擦除。
48. 用真实文件系统/FastAPI/Go链路与浏览器夹具分别验证，不混淆证据。
49. 真实训练另验world_size=2、样本覆盖、梯度更新与检查点重载，不能用参考处理替代。
50. 冻结历史交付包；容量不足时独立文件交付，不提高工作台1MiB限制或删除历史。

本阶段实现情况、失败记录和真实硬件阻塞统一见KAGGLE_STEP5_AUDIT.md。前3题150条建议保留，加本题共200条建议；它们不是已修复200项的结论。

## 问题5：没有逐条转写和固定数据版本，是否直接启动双卡训练？

选项A：把参考准备当训练直接启动；选项B：先冻结有逐条转写、统一参考、来源哈希与明确授权的训练输入，再独立验真实分词和双rank训练。推荐并选择B。先保存STEP6计划与本题50项建议，再实施；不进入下一个问题冒充训练已经完成。

### 本问题的50项行动建议

1. 训练输入与profiles/原始库分目录。
2. 必须选定现有命名库。
3. 请求固定库修订号。
4. 每个训练样本显式勾选。
5. 拒绝重复样本ID。
6. 拒绝来自其他库的ID。
7. 取快照期间持有同库租约。
8. 不改写最近参考处理状态。
9. 逐条要求对应转写。
10. 不把公共ref_text复制给全部样本。
11. 校验Unicode与文本长度。
12. 约束累计转写长度。
13. 明确转写是用户提供而非ASR验证。
14. 声音授权需明确声明。
15. 单说话人需明确声明。
16. 声明不冒充身份鉴定。
17. 统一参考必须来自选中集合。
18. 明确要求参考时长上限。
19. 不默默裁剪长参考。
20. 首版严格限定已验证PCM16 WAV格式。
21. 不把Opus改后缀冒充WAV。
22. 核对RIFF长度与chunk边界。
23. 拒绝多data/多fmt歧义容器。
24. 核对24kHz/单声道/16bit。
25. 核对真实PCM帧数。
26. 拒绝过短/超长片段。
27. 核对累计时长。
28. 拒绝空白或恒定信号。
29. 不把非恒定信号认定为有效语音。
30. 规范输出WAV且保留全部PCM帧。
31. 剥离非必要容器元数据。
32. 保存原始内容哈希。
33. 保存规范音频哈希。
34. 保存逐条文本哈希。
35. JSONL严格使用audio/text/ref_audio。
36. 所有相对路径由服务端ID生成。
37. 所有行使用同一个参考路径。
38. 提醒上游工具以快照目录作为工作目录。
39. 双rank分配计划不丢样本。
40. 奇数样本明确记录padding重复。
41. 分配计划不冒充rank执行记录。
42. 训练/分词/梯度/性能标志保持未验。
43. 独立目录原子发布，失败回滚。
44. 控制快照数量和总字节预算。
45. 校验内容，不以文件存在判断完整。
46. 列表不重复传回所有私有转写。
47. 删除原始库不隐式删除训练副本。
48. 单独删除副本且不自动云备份。
49. 保留历史包/工作台文件，不放宽1MiB。
50. 用真实WAV、故障注入、三轮回归与最终完整源码复制记录证据，不把沙箱模拟称为双T4训练。

前4题200建议保留，加本题共250项建议，不等于已完成250项验收。

## 问题6：尚无GPU资源互斥时，是否把声学码任务直接挂到在线双卡服务？

选项A：网页直接调用cuda:0 tokenizer，与现有推理争抢资源；选项B：先实现固定版本租约与离线本地CPU编码事务，真实模型缺失时blocked，GPU入口另设资源门禁。推荐并选择B。CPU不是最终速度方案；此选择先消除错版本、假成功、半成品和误删输入风险，不声称已运行真实模型。

### 本问题的50项行动建议

1. 冻结第六阶段包和哈希。
2. 编码前先保存第七阶段计划。
3. 再读固定上游prepare_data接口。
4. 核对12Hz模型返回二维码形状。
5. 核对1920下采样率和向上取整长度。
6. 核对16列码本而非25Hz一维输出。
7. 核对严格整数与2048范围。
8. 拒绝空结果。
9. 拒绝多返回或少返回，不用zip截断。
10. 单样本编码降低批次峰值。
11. 不把240秒样本偷偷裁短。
12. 输入固定manifest SHA256。
13. 编码前完整校验输入。
14. 长任务持有输入使用租约。
15. 删除输入遇租约明确409。
16. 租约放快照目录外。
17. 进程死亡由OS释放锁。
18. 不长期锁住所有输入列表。
19. 单独保存声学码资产。
20. 所有目录0700。
21. 所有输出文件0600。
22. 复制全部WAV使输出独立。
23. 保留每行audio/text/ref_audio。
24. 保留来源ID顺序和全部成员。
25. 复制并验证原双rank数学计划。
26. 状态区分真实执行和测试fixture。
27. fixture不能标记真实tokenization执行。
28. 编码完成不叫训练成功。
29. 模型只从本地目录加载。
30. 不允许远程模型ID。
31. 固定模型全部文件内容哈希。
32. 拒绝模型目录软硬链接。
33. 只允许JSON/safetensors模型资产。
34. 不加载pickle或远程自定义代码。
35. 加载前后核对模型指纹。
36. 模型必须12Hz/24kHz匹配配置。
37. 当前仅CPU/FP32/eager。
38. 不占用两推理GPU或自动停服务。
39. 限制CPU线程数。
40. 父进程施加总期限。
41. 取消终止完整子进程组。
42. 不向公开输出泄露原始异常和转写。
43. 原子发布并回滚失败。
44. 回收被杀任务的孤立暂存。
45. 设数量、单份、总量和磁盘余量预算。
46. 副本默认不进入Dataset备份。
47. 源输入删除不等于删除声学码副本。
48. 覆盖进程锁、形状错误、故障注入和CLI负向路径。
49. 三轮回归保留全部旧功能和真实源码复制。
50. 真实模型/GPU缺失时如实blocked，下一步资源互斥和真正训练仍独立验收。

前5题250建议保留，加本题共300项建议；建议数量不等于300清单全部完成。

## 问题7：按PID/显卡编号直接切换训练模式，还是先建立可继承的整组资源租约？

选项A：检查supervisor.pid或CUDA索引，超时后自动抢占；选项B：同机同UID整组独占flock、受控FD继承、最后进程退出才释放，手动停服务后再预约。推荐并选择B。PID可能复用、CUDA索引可能别名、父退出不等于孩子释放显存；本阶段只做协议准入，不把预约叫训练。

### 本问题的50项行动建议

1. 冻结第七阶段哈希。
2. 先保存第八阶段计划。
3. GPU租约独立于QTTS_STATE。
4. 不按逻辑CUDA索引拆分锁。
5. 同UID整组独占，优先安全而非并发。
6. 跨UID/容器不宣称全局隔离。
7. 固定私有目录不提供环境分区旁路。
8. 根目录0700。
9. 锁文件0600。
10. 拒绝符号链接。
11. 拒绝硬链接和非普通文件。
12. 核对文件属主。
13. 不删除或原子替换正在使用的锁文件。
14. flock才是占用权威。
15. PID记录只用于诊断。
16. 不依赖TTL强制解锁。
17. supervisor先锁后启动模型进程。
18. 第二supervisor失败不覆盖PID文件。
19. 用pass_fds继承打开文件描述符。
20. 只有worker/analyst继承GPU描述符。
21. gateway不延长GPU租约。
22. 子进程核对实际inode。
23. 子进程核对nonce和协议。
24. 子进程只采用inference类型。
25. 采用前验证文件锁仍可由该OFD持有。
26. close只关闭引用，不LOCK_UN。
27. 父进程关闭后子仍持锁。
28. 父进程SIGKILL不提前解锁。
29. 最后引用关闭才释放。
30. 失效描述符明确拒绝，不静默新建替代。
31. 独立真实worker也需要整组租约。
32. 多worker只由持锁supervisor启动。
33. analyst的延迟模型加载也受保护。
34. Mock路径明确不验证GPU所有权。
35. CPU编码保持不占GPU锁。
36. 不自动杀现有推理服务。
37. reserve只是有界预约，不执行训练。
38. status不因记录PID死亡推断空闲。
39. 预约取消和进程死亡释放原生锁。
40. 不开放任意shell或HTTP控制接口。
41. 修正父进程日志句柄泄漏。
42. 杀进程组后等待leader退出。
43. 清理leader先退出的后代。
44. 启动前安装停止信号处理。
45. 停止期间禁止再次拉起进程。
46. 保留档案恢复、认证与自动重启旧功能。
47. 真实fork/exec/FD/强杀测试而非只Mock布尔。
48. 旧版本进程先停干净，不假装已自动迁移。
49. 三轮验证和最终完整Python复制保留历史。
50. 之后在真实目标硬件验证显存释放/编码/解码，再做GPU模式与真正训练。

前6题300建议保留，加本题共350条建议；不是350项修复，也不是300审查项全部完成。

## 问题8：码副本只保留源hash就删原输入，还是封存完整来源并保护读取期？

选项A：依赖源ID/hash，删源后凭当前库补声明；选项B：新schema原样封存固定输入清单/索引，旧码明确未封存，并用固定版本读取租约阻止误删。推荐并选择B。不发明旧授权，不把文件检查当训练许可；先保存STEP9计划及50行动建议。

### 本问题的50项行动建议

1. 冻结第八阶段包和SHA256。
2. 编码前保存第九阶段计划。
3. 新码使用schema2区分来源封存。
4. 源manifest原样复制而非重新生成。
5. 复制源train_raw.jsonl完整字节。
6. 源manifest hash等于创建时固定hash。
7. 源索引hash取自源manifest。
8. 保留源库ID和自定义名称。
9. 保留源库修订号。
10. 保留原始样本ID与顺序。
11. 保留原始音频hash和来源名。
12. 保留规范WAV hash和帧数。
13. 保留逐条文本hash。
14. 保留统一参考样本ID。
15. 保留使用权声明原记录。
16. 保留单说话人声明原记录。
17. 不把声明等同权利/身份鉴定。
18. 交叉核对当前码行与源索引。
19. 拒绝漏行、多行或成员改变。
20. 拒绝参考路径被替换。
21. 拒绝文本被替换。
22. 拒绝分配计划与源hash不一致。
23. source目录0700。
24. 封存文件0600。
25. 封存拒绝软硬链接。
26. 封存纳入单份/总量预算。
27. 封存失败回滚整个新码副本。
28. 源输入不因封存被修改。
29. 删源后新码仍可独立核对来源。
30. schema1继续可读核验和删除。
31. schema1明确legacy-unsealed。
32. 不自动给旧码补授权。
33. 列表不冒充刚刚全量校验。
34. 只在真校验后返回来源已核验。
35. 读取请求固定码manifest hash。
36. 读取前核对全部文件。
37. 租约放码目录外避免改快照。
38. 长读取不锁住全局列表。
39. 首版同版本读取独占，明确409。
40. 读取期间删除同版本409。
41. 其他版本仍可核验和操作。
42. 进程死亡由OS回收租约。
43. 不用PID/TTL强制解锁。
44. CLI只保持租约，不执行任意命令。
45. CLI不输出私人转写/完整来源。
46. 超时/取消/父杀释放读取引用。
47. 测试fixture保持test_only_codes。
48. 真实训练器未来必须接入读取租约与单独门禁。
49. 不自动云备份，不改变旧profiles备份。
50. 三轮真实文件/进程与全功能回归、完整源码复制留证，不把准备当双T4训练。

前7题350建议保留，加本题共400条建议；建议数量不是已完成修复或300项清单通过数量。

## 问题9：继续封存与收据工具，还是直接实现能反向传播的训练核心？

选项A：继续前置工具并延后核心；选项B：立即交付本地Base1.7B的FP16 LoRA联合loss、真正DDP/优化器/adapter保存入口。推荐并选择B。代码可现在开发，真实T4成功仍需现场设备/权重证据，不伪装CPU为Qwen训练。

### 本问题的50项行动建议

1. 冻结原始至step9及正式工作台。
2. 先保存直接训练核心计划。
3. 不再把检查租约叫训练。
4. 固定官方模型与dataset接口提交。
5. 核对文本投影到talker维度。
6. 保留16码本联合目标。
7. 冻结Base参数。
8. 仅显式q/v线性层注入LoRA。
9. 检查实际命中的层名称。
10. LoRA参数保留FP32。
11. 不用全参数AdamW状态。
12. eager替代标准FA2。
13. T4使用FP16而非BF16。
14. microbatch首版固定1。
15. 限制总序列长度并拒绝截断。
16. 真实文本tokenizer构造助手序列。
17. 规范WAV参考生成mel。
18. 冻结speaker encoder并eval。
19. 参考声纹只计算一次。
20. DDP包装实际loss forward。
21. 禁止经.module绕过训练forward。
22. 要求恰好两个rank。
23. 每rank显式绑定一个CUDA设备。
24. 采用NCCL与集合通信超时。
25. 明确样本不足拒绝与奇数填充。
26. 每epoch确定性变换采样顺序。
27. 记录每rank见过的样本ID。
28. 不把数学分配计划称已训练。
29. GradScaler与有限梯度检查。
30. 正确处理尾部累积步数。
31. 全rank同时拒绝非有限loss。
32. 梯度裁剪前unscale。
33. 实际检验参数发生改变。
34. 原子保存adapter与speaker embedding。
35. 保存基础模型完整hash。
36. 保存数据manifest固定hash。
37. 不把adapter目录当完整CustomVoice。
38. 提供严格adapter加载函数。
39. 不自动发布未试听检查点。
40. fixture与legacy训练拒绝。
41. 要求明确语义与授权实验确认。
42. 用户声明不变成法律鉴定。
43. 父控制器持码与GPU双租约。
44. 两个rank继承相同受控FD。
45. 父死但孩子活着仍保护资源。
46. 取消超时停止并等待全部rank。
47. 离线加载不自动安装下载。
48. 只输出数值日志而非私人转写。
49. CPU真实张量/Gloo与CUDA验收分开。
50. 完成核心测试后保留原功能回归与真实阻塞。

前8题400条保留，累计9题450建议；不等于450项修复或300项清单全部通过。

## 问题10：猜测高速后端能动态挂LoRA，还是显式接官方原生推理并诚实标注缓冲？

选项A：直接往未知CUDA graph/私有对象注入并声称实时；选项B：保留默认高速路径，新增显式原生adapter后端及训练profile，句级缓冲如实标注。推荐并选择B，先完成可测试的训练后推理链路，不伪造声学流式或实机音质。

### 本问题的50项行动建议

1. 冻结step10及正式HEAD。
2. 保存直接推理接入计划。
3. 不猜CUDA graph动态LoRA兼容。
4. 默认faster路径保留。
5. 原生后端必须显式选择。
6. 明确句级缓冲不是声学流式。
7. 拒绝Mock加载训练候选。
8. 读取完成run/result/request互相一致。
9. 固定adapter manifest hash。
10. 拒绝失败取消或缺检查点的run。
11. 要求两NCCL rank更新记录。
12. 核对全部选中样本覆盖。
13. 验证adapter tensor摘要。
14. 验证speaker张量成员形状与finite。
15. 拒绝软硬链接和越界路径。
16. 限定JSON和tensor文件预算。
17. 发布使用用户自定义名称。
18. 不从第一条run猜用户选择。
19. 发布时持码版本租约。
20. 复制实际统一参考和匹配文本。
21. 不自动改active或切换推理。
22. profile绑定run/Base/码hash。
23. 每GPU只驻留一个Base模型。
24. Base必须可信本地且固定hash。
25. 严格离线与trust_remote_code false。
26. 所有目标LoRA形状先验证。
27. 不同LoRA rank可切换。
28. 所有新模块先构造再提交。
29. 失败保留先前adapter不半写。
30. 同一worker锁内切换与生成。
31. 每次使用重新核验profile绑定。
32. 缓存不绕过删除或损坏。
33. 保存speaker向量直接构造prompt。
34. 不凭另一个profile猜speaker向量。
35. x-vector-only不伪装ICL模式。
36. 不自动变成CustomVoice。
37. 完整PCM只输出一次。
38. 拒绝错采样率多声道非有限输出。
39. 取消传到stopping criteria。
40. 取消后丢弃迟到完整音频。
41. 不承诺中断CUDA kernel。
42. health/stats显示缓冲模式。
43. 网页选择器标注训练候选未验收。
44. 拒绝改写固定参考和校准。
45. 原profile删除仍保留。
46. native探针检查官方Qwen不是faster。
47. native不自动下载陌生模型。
48. 备份恢复缺adapter明确失败。
49. CPU真tensor与接口替身分开标注。
50. 完成全功能三轮与完整源码复制留证。

累计10题500建议；建议、代码实现与300项目标验收不是同一统计。

## 问题11：单独降级Transformers，还是在已审查5.x组合上修复真实RoPE配置桥接并前置复现？

A单独降4.x违背faster0.5.4依赖，可能产生另一错误；B固定现场三项组合，对已识别Qwen兼容函数做最小现代字段桥接、真实配置CPU对照和fatal门禁。推荐并选择B；完整Qwen/T4须再运行，不能据此保证成功或永久部署。

1. 保存用户实际版本与设备证据。
2. 不把探针签名通过当模型成功。
3. 冻结原始至step11。
4. 确认faster0.5.4依赖约束。
5. 确认qwen-tts-hf共享模块名。
6. 拒绝单独盲降Transformers4。
7. 读取PyPI实际wheel而非猜测。
8. 定位现代Mimi rope_parameters。
9. 定位旧Qwen默认函数读取字段。
10. 真实CPU复现缺rope_theta。
11. 包装范围限制已识别函数。
12. 不全局给MimiConfig加property。
13. 不硬编码所有模型theta。
14. 不重写权重或config文件。
15. 现代theta必须来自实际配置。
16. 拒绝非有限非正theta。
17. 拒绝未知scaled RoPE桥接。
18. 保持旧rope_theta路径不变。
19. 临时config副本避免改原对象。
20. 正确传递device与seq_len。
21. 保留partial_rotary_factor语义。
22. 验证head_dim实际契约。
23. 兼容桥重复调用幂等。
24. 拒绝未知第三方registry覆盖。
25. 保留Apache归属与来源链接。
26. 探针增加实际配置数学smoke。
27. smoke明确不加载完整模型。
28. 默认worker加载前安装桥。
29. 原生adapter加载前安装桥。
30. CPU tokenizer加载前安装桥。
31. 双rank训练加载前安装桥。
32. 不修改现有码或质量证据。
33. 固定三项直接依赖版本。
34. 不升级卸载平台Torch/CUDA。
35. 共享qwen命名空间冲突拒绝。
36. 不在日志打印HF密钥。
37. 标记确定性配置错误fatal。
38. fatal worker停止重试。
39. bootstrap尽早报告配置失败。
40. 清理只针对自己创建的Popen。
41. 不得拿旧PID盲杀进程。
42. 父及子FD释放后才允许新服务。
43. 保留每worker单GPU映射。
44. 健康显示真实GPU与模型就绪。
45. 确认无空闲自动卸载行为。
46. 明确Kaggle不能永久占GPU。
47. 提供完整会话重启操作。
48. 发布step12及更新复制页面。
49. 三轮回归与原样复制验真。
50. 真实GPU复跑结果仍待收集。

## 问题12：step12相同现场故障再现后，应继续只验证RoPE函数，还是修复实际包延迟导入生命周期？

选择并推荐后者。实际wheel证明Faster直到from_pretrained才导入Qwen；安装元数据判别HF并显式正常导入compat、预检fail-closed，必须用真实完整包加微型Mimi构造回归，不能再把手动exec上游函数当入口验收。无须再问用户。

### 本问题之后的50项具体实施建议

1. 保留用户step12实际失败结论。
2. 定位Faster顶层导出并非Qwen模型导入。
3. 记录真实Faster from_pretrained延迟导入行。
4. 区分发行安装与模块导入状态。
5. 删除HF未导入即不适用的判断。
6. 用发行元数据先选择HF或legacy分支。
7. 先检查官方与HF命名空间冲突。
8. 导入前拒绝未经审查HF版本。
9. 导入前拒绝未经审查Transformers版本。
10. 显式通过importlib导入受审compat模块。
11. 让Python正常执行真实Qwen父包初始化。
12. 不伪造生产sys.modules条目。
13. 不全局替换Python导入钩子。
14. 导入失败转明确兼容错误。
15. 错误消息避免输出凭证。
16. HF导入成功后确认默认注册函数身份。
17. 重复安装验证registry仍指向同一桥接。
18. registry被未知代码覆盖时拒绝。
19. 保留真实配置theta读取。
20. 保留三种theta精确数学对照。
21. 不修改原始Mimi配置。
22. 不修改权重或缓存权重文件。
23. 不独立降级TF4破坏Faster依赖。
24. 保留平台Torch和CUDA约束。
25. 官方legacy无HF时继续不适用。
26. 无HF却出现HF模块时拒绝矛盾环境。
27. HF预检跳过smoke必须阻断。
28. 预检仍明确没有加载完整模型。
29. 添加延迟模块导入单元回归。
30. 添加导入异常回归。
31. 添加版本未通过时不导入回归。
32. 添加冲突时不导入回归。
33. 添加官方legacy不导入HF回归。
34. 添加HF意外not_applicable预检回归。
35. 真实安装Faster完整wheel到隔离缓存。
36. 真实安装完整Qwen包而非只exec函数。
37. 保持主测试venv依赖不污染。
38. 验证Faster顶层导入后Qwen确实未加载。
39. 调用实际生产bridge触发完整Qwen导入。
40. 构造微型真实MimiModel走_init_weights。
41. 禁止真实实验from_pretrained网络下载。
42. 真实实验禁网并记录CPU/no GPU边界。
43. 每个真实导入验证独立新进程。
44. 保留step12及所有旧交付哈希。
45. 保留resident/fatal清理既有行为。
46. 保留训练adapter及两主视图。
47. 三轮全套回归而非只跑新增单测。
48. 更新复制页并验真实剪贴板下载。
49. 更新完整交接与失败反思。
50. 交付step13并明确真实双T4复跑未验。

## 问题13：十多分钟录音应作为长参考直接缓存，还是切成逐条对齐短样本后真正训练？

选A：用参考缓存冒充训练，拒绝。选B：保留完整录音，训练前用可信时间戳分段与逐条转写审核，编码后执行真实双rank LoRA，推荐B。追问：当推理已占双卡时，网页训练如何保持控制面存活？答案是独立CPU控制面和明确维护态；当前没有这条闭环，不能添加假训练按钮或绕过GPU锁。完整网页训练本轮仍是未完成门禁，不向用户虚报。

### 本问题之后的50项具体实施建议

1. 连续录音：将239秒上限与十分钟需求对齐。
2. 连续录音：同时扩大分块数量预算。
3. 连续录音：保留累计字节上限。
4. 连续录音：用虚拟时钟测试十一分钟。
5. 连续录音：停止后才保存有效片段。
6. 连续录音：取消权限晚返回仍关闭设备。
7. 连续录音：禁止空录音提交。
8. 连续录音：保留失败本地片段。
9. 连续录音：显示连续录音最大时长。
10. 连续录音：不把后台计时器当精确音频时钟。
11. 上传预算：同步浏览器与服务端时长。
12. 上传预算：同步客户端与服务端单文件字节。
13. 上传预算：保留整请求总量门禁。
14. 上传预算：保留未知长度流式门禁。
15. 上传预算：原始库独立容量核对。
16. 上传预算：PCM长音频预先计算空间。
17. 上传预算：不把提高秒数等同无限上传。
18. 上传预算：拒绝超过上限而不静默截断。
19. 上传预算：给出明确限额中文提示。
20. 上传预算：加入长WAV完整长度回归。
21. 训练入口：明确参考处理不训练。
22. 训练入口：明确快照不执行优化器。
23. 训练入口：真实训练保留独立确认。
24. 训练入口：不开虚假开始训练按钮。
25. 训练入口：网页训练需独立CPU控制面。
26. 训练入口：训练时停止两GPU推理而非争显存。
27. 训练入口：控制面不能随analyst一起关闭。
28. 训练入口：完成后再恢复原声音服务。
29. 训练入口：取消要等待两个rank退出。
30. 训练入口：未实现端到端入口须明示未完成。
31. 长录音切分：训练不能把十分钟当单条序列。
32. 长录音切分：优先审核ASR时间戳。
33. 长录音切分：不得用均分文本猜对齐。
34. 长录音切分：不得裁去超预算文本。
35. 长录音切分：保留原始音频。
36. 长录音切分：生成独立可审核短WAV。
37. 长录音切分：保留每段来源起止秒。
38. 长录音切分：同一说话人须明确声明。
39. 长录音切分：片段过短需要拒绝或重新切分。
40. 长录音切分：完整语义覆盖要逐项记录。
41. 转写：逐条训练文本对应逐条音频。
42. 转写：ASR提案不能标为人工已核验。
43. 转写：禁止将参考文本套用全部片段。
44. 转写：Unicode转写保持原值。
45. 转写：空转写拒绝。
46. 转写：转写字符总预算保留。
47. 转写：不能凭训练loss证明读音正确。
48. 转写：方言专名需要真实试听。
49. 转写：训练前审核标点断句。
50. 转写：保留来源转写hash。

## 问题14：怎样在不删样本、不减更新步数的情况下提速？

选A：减少epoch或声学码，拒绝无损说法。选B：先消除重复tokenize和host同步，保留loss/样本/顺序/优化器配置，做相同seed参数对照与成本记录，推荐B。继续追问：无限多线程是否更快？不成立，Python调度/内存复制/CPU配额与GPU串行算子有瓶颈；保留双进程DDP，线程有上限。没有真实T4基准，不声称最快或质量更好。

### 本问题之后的50项具体实施建议

1. 张量准备：找出每epoch重复文本tokenize。
2. 张量准备：缓存必须有字节上限。
3. 张量准备：缓存不改变token顺序。
4. 张量准备：缓存返回值避免被调用者污染。
5. 张量准备：超过缓存上限退回原计算。
6. 张量准备：包含声学码形状校验。
7. 张量准备：不缓存未通过预算的样本。
8. 张量准备：保留统一参考mel。
9. 张量准备：比对缓存前后collate张量。
10. 张量准备：用调用次数而非GPU倍速声称改善。
11. 优化器：保持全部联合loss。
12. 优化器：保持0.3子talker系数。
13. 优化器：保持训练样本顺序。
14. 优化器：保持累积步分母。
15. 优化器：保持不足一组累积的缩放。
16. 优化器：保持AdamW权重衰减。
17. 优化器：保持LoRA可训练参数。
18. 优化器：保持FP32适配器。
19. 优化器：不减少epoch作为无损提速。
20. 优化器：记录真实optimizer step数。
21. 双卡：保持两rank NCCL契约。
22. 双卡：不让两rank同时用同一物理卡。
23. 双卡：保持奇数样本补齐策略。
24. 双卡：保持两rank参数摘要一致。
25. 双卡：每epoch报告实际seen_ids。
26. 双卡：不能把CPU Gloo当NCCL。
27. 双卡：OOM后不得标完成。
28. 双卡：不能用两个Python线程替代DDP。
29. 双卡：显存峰值必须实测。
30. 双卡：完成后保存适配器再报告。
31. 同步开销：审查每参数grad finite读取。
32. 同步开销：合并有限性检查到一次CPU读取。
33. 同步开销：跨rank有限性继续一致。
34. 同步开销：非有限梯度两rank一同跳过。
35. 同步开销：保留梯度范数裁剪。
36. 同步开销：不盲开find_unused_parameters=False。
37. 同步开销：loss统计不删训练计算。
38. 同步开销：不盲开torch.compile。
39. 同步开销：不盲开TF32冒充T4原生支持。
40. 同步开销：CUDA优化需独立目标机基准。
41. 线程预算：按CPU配额而非文件数设置线程。
42. 线程预算：两rank线程总数不能压满宿主。
43. 线程预算：ASR线程与训练线程分开预算。
44. 线程预算：限定预处理并发。
45. 线程预算：避免每个worker再套大线程池。
46. 线程预算：保留取消与超时。
47. 线程预算：记录线程配置。
48. 线程预算：默认不引入DataLoader多进程。
49. 线程预算：小数据先消除重复计算。
50. 线程预算：吞吐测试包含预处理成本。

## 问题15：首声更快与逐字音频完全一致能否无条件同时保证？

选A：先播放再宣称已核验，拒绝。选B：应用层先消除文本改写和后加呼吸；真实声学一致性另需逐句ASR核验/试听，严格核验必然增加缓冲等待且ASR非绝对真值，推荐B。继续追问：是否通过降低缓冲来美化首声？不推荐，本轮先修有效语音首块计时与冗余处理；保留稳定缓冲，真实首声/韵律须目标机A/B。不能达到100%声学信心，更不能把未知写成成功。

### 本问题之后的50项具体实施建议

1. 文本链路：定位CleanDelta删除内容。
2. 文本链路：避免每个delta独立清洗URL。
3. 文本链路：朗读路径不补句号。
4. 文本链路：保留中英混合原文。
5. 文本链路：保留数字小数。
6. 文本链路：保留引号。
7. 文本链路：保留专有名词。
8. 文本链路：不添加链接二字。
9. 文本链路：分段连接按规范比较输入。
10. 文本链路：模型声学错字另行核验。
11. 呼吸：默认关闭额外呼吸注入。
12. 呼吸：不以合成噪声冒充真人吸气。
13. 呼吸：保留可选真实参考呼吸。
14. 呼吸：无真实片段时保持安静。
15. 呼吸：不放大短促噪声。
16. 呼吸：保留淡入淡出防爆音。
17. 呼吸：呼吸增益需试听。
18. 呼吸：模型自身呼吸与后加呼吸区分。
19. 呼吸：不盲目滤掉全部气声。
20. 呼吸：去噪不得削掉辅音。
21. 首声：区分模型首块与可听首声。
22. 首声：不把前置静音算有效语音。
23. 首声：修正trimmer前计时。
24. 首声：保留实际首播测量。
25. 首声：分段过短影响韵律须权衡。
26. 首声：小chunk需实机核验。
27. 首声：不要用空PCM刷低首声。
28. 首声：首段优先调度继续保留。
29. 首声：录制到输出完整链路测量。
30. 首声：无真实T4数据不承诺时延。
31. 缓冲：不要无条件降低首播阈值。
32. 缓冲：保留欠载预测。
33. 缓冲：保留迟滞。
34. 缓冲：区分首次启动与恢复。
35. 缓冲：生成慢时继续积累。
36. 缓冲：句级缓冲不能冒称声学流式。
37. 缓冲：记录首PCM和首播放分别。
38. 缓冲：测试短文本尾段可播放。
39. 缓冲：停止后不能漏出迟到PCM。
40. 缓冲：连续朗读不能丢段。
41. 准确朗读：模型可能幻觉不能仅靠输入相等保证。
42. 准确朗读：严格核验需整句缓存。
43. 准确朗读：ASR核验增加首声等待。
44. 准确朗读：ASR也不是绝对真值。
45. 准确朗读：不符应拒绝或请求重试。
46. 准确朗读：重试不改用户文本。
47. 准确朗读：不自动补充解释。
48. 准确朗读：多音字需目标语境测试。
49. 准确朗读：真实试听列为门禁。
50. 准确朗读：不承诺零错字。


## 问题16：怎样让参考录音只能提供音色，不能进入输出波形？

具体选项：A 继续ICL并裁参考波形；B 仅说话人向量且停顿纯静音；C 先生成后整句ASR拒播。

最推荐：B。

回答及追问结论：先取说话人向量，生成与预热均xvec_only=True，ref_text为空；禁止参考呼吸拼接和旧环境开关。A依赖裁切且参考码参与解码，不满足强隔离；C延迟更高且ASR不是真值。B会改变韵律/相似度，必须实机试听，不承诺模型不幻觉。

落实到后续代码的50项建议（本题结清后再进入下一题）：

1. [S15-R1-001] 在`worker.RealEngine`落实：禁止参考码进入解码器；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
2. [S15-R1-002] 在`worker.RealEngine`落实：仅以说话人向量条件生成；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
3. [S15-R1-003] 在`worker.RealEngine`落实：生成调用不传参考正文；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
4. [S15-R1-004] 在`worker.RealEngine`落实：预热采用相同向量模式；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
5. [S15-R1-005] 在`worker.RealEngine`落实：dtype回退后仍用向量模式；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
6. [S15-R1-006] 在`worker.RealEngine`落实：不开放环境变量回退ICL；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
7. [S15-R1-007] 在`worker.RealEngine`落实：明确韵律相似度可能变化；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
8. [S15-R1-008] 在`worker.RealEngine`落实：核对Faster0.5.4实际源码；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
9. [S15-R1-009] 在`worker.RealEngine`落实：生成采样率仍严格24k；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
10. [S15-R1-010] 在`worker.RealEngine`落实：生成器取消时仍close；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
11. [S15-R1-011] 在`worker.lead_audio`落实：废止reference呼吸拼接开关；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
12. [S15-R1-012] 在`worker.lead_audio`落实：前置停顿仅零样本；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
13. [S15-R1-013] 在`worker.lead_audio`落实：旧breath_files不能被读取；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
14. [S15-R1-014] 在`worker.lead_audio`落实：无参考片段也不造噪声；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
15. [S15-R1-015] 在`worker.lead_audio`落实：保留模型自身呼吸；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
16. [S15-R1-016] 在`worker.lead_audio`落实：不把去呼吸等同自然音色；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
17. [S15-R1-017] 在`worker.lead_audio`落实：暂停最长仍1500ms；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
18. [S15-R1-018] 在`worker.lead_audio`落实：负暂停仍归零；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
19. [S15-R1-019] 在`worker.lead_audio`落实：随机种子不能改变静音；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
20. [S15-R1-020] 在`worker.lead_audio`落实：人工试听仍是门禁；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
21. [S15-R1-021] 在`worker.run_job`落实：PCM来源只接受模型和零停顿；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
22. [S15-R1-022] 在`worker.run_job`落实：不因模型失败回放anchor；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
23. [S15-R1-023] 在`worker.run_job`落实：不因空结果播放参考；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
24. [S15-R1-024] 在`worker.run_job`落实：保留nonfinite拒绝；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
25. [S15-R1-025] 在`worker.run_job`落实：保留异常统计；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
26. [S15-R1-026] 在`worker.run_job`落实：保留裁边；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
27. [S15-R1-027] 在`worker.run_job`落实：保留尾部淡出；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
28. [S15-R1-028] 在`worker.run_job`落实：保留取消检查；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
29. [S15-R1-029] 在`worker.run_job`落实：保留每GPU互斥；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
30. [S15-R1-030] 在`worker.run_job`落实：日志报告生成隔离模式；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
31. [S15-R1-031] 在`adapter_engine`落实：核对原生向量模式；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
32. [S15-R1-032] 在`adapter_engine`落实：不能把训练参考当输出；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
33. [S15-R1-033] 在`adapter_engine`落实：固定adapter哈希；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
34. [S15-R1-034] 在`adapter_engine`落实：损坏adapter不能回退Base；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
35. [S15-R1-035] 在`adapter_engine`落实：不改变句级缓冲标记；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
36. [S15-R1-036] 在`adapter_engine`落实：不混驻两种引擎；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
37. [S15-R1-037] 在`adapter_engine`落实：保持取消丢弃迟到wave；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
38. [S15-R1-038] 在`adapter_engine`落实：训练候选不自动激活；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
39. [S15-R1-039] 在`adapter_engine`落实：新进程重载仍需实机；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
40. [S15-R1-040] 在`adapter_engine`落实：无训练证据不称已训练；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
41. [S15-R1-041] 在`朗读内容`落实：不拼接参考文本；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
42. [S15-R1-042] 在`朗读内容`落实：不修改目标文本；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
43. [S15-R1-043] 在`朗读内容`落实：不补额外说明；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
44. [S15-R1-044] 在`朗读内容`落实：不以字符串一致冒充声学一致；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
45. [S15-R1-045] 在`朗读内容`落实：不自动删数字；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
46. [S15-R1-046] 在`朗读内容`落实：不自动删专名；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
47. [S15-R1-047] 在`朗读内容`落实：不裁词谋求首声；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
48. [S15-R1-048] 在`朗读内容`落实：短句仍需语言条件；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
49. [S15-R1-049] 在`朗读内容`落实：模型幻觉单独披露；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
50. [S15-R1-050] 在`朗读内容`落实：严格ASR拒播仍未实现；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。

结论：已足够确定本轮工程取舍，无需向用户追问；真实声学质量和T4性能只能保留待测，不声称100%信心。


## 问题17：能否通过每T4放两个1.7B来降低首声？如何在不破坏朗读内容时早发第一段？

具体选项：A 每卡双副本；B 每卡一模型，首个确定语义边界即提交；C 每token一个TTS任务。

最推荐：B。

回答及追问结论：FP16纯参数约3.4GB/份，双份约6.8GB不是峰值显存；codec、KV、graph及临时张量另占内存。同卡副本共享同一计算资源，单请求不自动变快。保留两卡两模型并行相邻段；首个完整中文句或足够长逗号前缀无需等下一delta，英文点仍保留lookahead。保留播放器抗欠载策略。

落实到后续代码的50项建议（本题结清后再进入下一题）：

1. [S15-R2-001] 在`首段分段`落实：识别当前末尾标点等待lookahead；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
2. [S15-R2-002] 在`首段分段`落实：只为首段新增即时确定边界；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
3. [S15-R2-003] 在`首段分段`落实：句末中文标点可立即提交；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
4. [S15-R2-004] 在`首段分段`落实：逗号达到首段预算可提交；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
5. [S15-R2-005] 在`首段分段`落实：ASCII点仍等lookahead避小数；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
6. [S15-R2-006] 在`首段分段`落实：保留后续正常分段；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
7. [S15-R2-007] 在`首段分段`落实：新段保留原文；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
8. [S15-R2-008] 在`首段分段`落实：不等待LLM全篇完成；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
9. [S15-R2-009] 在`首段分段`落实：不为每token发TTS；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
10. [S15-R2-010] 在`首段分段`落实：短于常规阈值完整句可首发；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
11. [S15-R2-011] 在`单位边界`落实：英文单词不从中间拆开；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
12. [S15-R2-012] 在`单位边界`落实：小数12.50不拆错；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
13. [S15-R2-013] 在`单位边界`落实：英文缩写保留；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
14. [S15-R2-014] 在`单位边界`落实：标点后引号不能丢；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
15. [S15-R2-015] 在`单位边界`落实：跨delta空格仍保存；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
16. [S15-R2-016] 在`单位边界`落实：纯标点不能伪成语音；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
17. [S15-R2-017] 在`单位边界`落实：Unicode原样；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
18. [S15-R2-018] 在`单位边界`落实：组合emoji不作为词；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
19. [S15-R2-019] 在`单位边界`落实：无标点长句保持上限；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
20. [S15-R2-020] 在`单位边界`落实：最后残留仍Flush；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
21. [S15-R2-021] 在`顺序保护`落实：首段任务优先；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
22. [S15-R2-022] 在`顺序保护`落实：第二段可用另一GPU；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
23. [S15-R2-023] 在`顺序保护`落实：已输出失败不重放；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
24. [S15-R2-024] 在`顺序保护`落实：未输出失败才允许重试；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
25. [S15-R2-025] 在`顺序保护`落实：保留段索引；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
26. [S15-R2-026] 在`顺序保护`落实：保留背压高低水位；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
27. [S15-R2-027] 在`顺序保护`落实：保留迟滞；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
28. [S15-R2-028] 在`顺序保护`落实：不无限预生成；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
29. [S15-R2-029] 在`顺序保护`落实：取消移除排队任务；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
30. [S15-R2-030] 在`顺序保护`落实：健康检查不回放参考；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
31. [S15-R2-031] 在`LLM流`落实：保留每delta向前端推送；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
32. [S15-R2-032] 在`LLM流`落实：首句完成即submit；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
33. [S15-R2-033] 在`LLM流`落实：首token计时保留；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
34. [S15-R2-034] 在`LLM流`落实：首段提交计时保留；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
35. [S15-R2-035] 在`LLM流`落实：LLM完成计时保留；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
36. [S15-R2-036] 在`LLM流`落实：非法JSON报错；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
37. [S15-R2-037] 在`LLM流`落实：截断finish_reason报错；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
38. [S15-R2-038] 在`LLM流`落实：取消终止HTTP；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
39. [S15-R2-039] 在`LLM流`落实：不记录API密钥；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
40. [S15-R2-040] 在`LLM流`落实：用本地SSE延迟尾巴测试；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
41. [S15-R2-041] 在`首声指标`落实：区分首token和首段；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
42. [S15-R2-042] 在`首声指标`落实：区分模型首块和PCM；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
43. [S15-R2-043] 在`首声指标`落实：区分首PCM和首播；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
44. [S15-R2-044] 在`首声指标`落实：静音不当作人声；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
45. [S15-R2-045] 在`首声指标`落实：保留欠载次数；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
46. [S15-R2-046] 在`首声指标`落实：不以网络替身称DeepSeek实测；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
47. [S15-R2-047] 在`首声指标`落实：不以MockRTF称QwenRTF；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
48. [S15-R2-048] 在`首声指标`落实：记录首段早于LLM结束；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
49. [S15-R2-049] 在`首声指标`落实：没有CUDA不填GPU延迟；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
50. [S15-R2-050] 在`首声指标`落实：不承诺三秒内；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。

结论：已足够确定本轮工程取舍，无需向用户追问；真实声学质量和T4性能只能保留待测，不声称100%信心。


## 问题18：创建档案怎样提速而不偷偷减数据或伪造训练？

具体选项：A 默认省掉所有质量模型；B 默认延后可选GPU校准，复用CPU ASR及本任务重复嵌入，分阶段计时；C 只处理前十秒。

最推荐：B。

回答及追问结论：保留完整数据ASR、24候选评分和准确最佳锚点F0。可选校准移至用户显式调用；CPU Whisper可复用，CUDA ASR仍卸载；同任务嵌入内容去重。首建仍可能受下载和CPU大模型限制，不预设提速倍数。阶段收据必须最终持久化，长ASR段无可信对齐不能截音频配全文。

落实到后续代码的50项建议（本题结清后再进入下一题）：

1. [S15-R3-001] 在`创建默认`落实：默认关闭可选GPU候选校准；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
2. [S15-R3-002] 在`创建默认`落实：保留手动校准按钮；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
3. [S15-R3-003] 在`创建默认`落实：直接创建与库处理默认一致；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
4. [S15-R3-004] 在`创建默认`落实：后端缺省也关闭校准；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
5. [S15-R3-005] 在`创建默认`落实：锁定重置默认关闭；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
6. [S15-R3-006] 在`创建默认`落实：明确不是训练；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
7. [S15-R3-007] 在`创建默认`落实：不隐藏校准质量代价；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
8. [S15-R3-008] 在`创建默认`落实：保留两卡预热；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
9. [S15-R3-009] 在`创建默认`落实：失败不改active；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
10. [S15-R3-010] 在`创建默认`落实：完成收据不虚报；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
11. [S15-R3-011] 在`ASR成本`落实：已知单段短文本直接使用；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
12. [S15-R3-012] 在`ASR成本`落实：不能把长文本套短片；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
13. [S15-R3-013] 在`ASR成本`落实：保持全量长音频ASR；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
14. [S15-R3-014] 在`ASR成本`落实：不取前十秒冒充完整；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
15. [S15-R3-015] 在`ASR成本`落实：CPU Whisper可驻留复用；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
16. [S15-R3-016] 在`ASR成本`落实：不在GPU常驻ASR；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
17. [S15-R3-017] 在`ASR成本`落实：保留CPU回退；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
18. [S15-R3-018] 在`ASR成本`落实：保留识别beam5；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
19. [S15-R3-019] 在`ASR成本`落实：保留词时间戳；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
20. [S15-R3-020] 在`ASR成本`落实：记录手动转写绕过ASR；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
21. [S15-R3-021] 在`ASR内存`落实：仅CPU默认驻留；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
22. [S15-R3-022] 在`ASR内存`落实：CUDA ASR仍卸载；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
23. [S15-R3-023] 在`ASR内存`落实：显式开关可禁用驻留；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
24. [S15-R3-024] 在`ASR内存`落实：同一重模型入口串行；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
25. [S15-R3-025] 在`ASR内存`落实：不无限缓存音频；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
26. [S15-R3-026] 在`ASR内存`落实：不缓存每个用户转写；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
27. [S15-R3-027] 在`ASR内存`落实：不让驻留伪造模型已加载；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
28. [S15-R3-028] 在`ASR内存`落实：首次下载成本单列；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
29. [S15-R3-029] 在`ASR内存`落实：CPU内存风险披露；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
30. [S15-R3-030] 在`ASR内存`落实：不以第二次速度代表冷启动；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
31. [S15-R3-031] 在`重复计算`落实：档案内部嵌入按内容哈希复用；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
32. [S15-R3-032] 在`重复计算`落实：嵌入缓存仅本次任务；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
33. [S15-R3-033] 在`重复计算`落实：返回向量保持只读语义；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
34. [S15-R3-034] 在`重复计算`落实：不跨档案泄漏用户数据；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
35. [S15-R3-035] 在`重复计算`落实：记录embed实际调用数；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
36. [S15-R3-036] 在`重复计算`落实：记录embed命中数；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
37. [S15-R3-037] 在`重复计算`落实：候选相同波形可复用；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
38. [S15-R3-038] 在`重复计算`落实：不按文件名猜相同；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
39. [S15-R3-039] 在`重复计算`落实：不改变候选排序公式；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
40. [S15-R3-040] 在`重复计算`落实：缓存失败不写半成品；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
41. [S15-R3-041] 在`CPU候选`落实：保留24候选上限；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
42. [S15-R3-042] 在`CPU候选`落实：保留前三非重叠；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
43. [S15-R3-043] 在`CPU候选`落实：保留SNR打分；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
44. [S15-R3-044] 在`CPU候选`落实：保留典型性中心；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
45. [S15-R3-045] 在`CPU候选`落实：保留F0打分；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
46. [S15-R3-046] 在`CPU候选`落实：准确F0仍用于最佳锚点；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
47. [S15-R3-047] 在`CPU候选`落实：不偷偷换MFCC冒充ECAPA；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
48. [S15-R3-048] 在`CPU候选`落实：不降采样输入标准；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
49. [S15-R3-049] 在`CPU候选`落实：不减少可用文件；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
50. [S15-R3-050] 在`CPU候选`落实：不承诺质量无损提速倍数；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。

结论：已足够确定本轮工程取舍，无需向用户追问；真实声学质量和T4性能只能保留待测，不声称100%信心。


## 问题19：音色不像与两种声音，应如何修复且不重新播放参考？

具体选项：A保持15纯向量；B恢复有转写ICL条件、只解码生成码、参考内容固定绑定；C把参考原音混回输出。

推荐选择：B。

详细回答：15向量模式可能弱化相似度；B保留声学/转写条件但参考码绝不进codec，新增内容指纹和路径缓存失效。C明确违反用户先前要求。ICL不能保证无幻觉或绝对相似，用户原音频未提供，实际听感仍待验。

本题回答后、进入下一题前的50项开发建议：

1. [S16-R1-001] 在`参考条件`落实：重新审视15强制向量模式；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
2. [S16-R1-002] 在`参考条件`落实：默认恢复匹配转写的ICL条件；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
3. [S16-R1-003] 在`参考条件`落实：无转写不得静默假设ICL；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
4. [S16-R1-004] 在`参考条件`落实：向量模式保留为显式选项；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
5. [S16-R1-005] 在`参考条件`落实：参考文本只作条件不拼目标正文；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
6. [S16-R1-006] 在`参考条件`落实：解码器不接参考码；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
7. [S16-R1-007] 在`参考条件`落实：保留原始参考录音；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
8. [S16-R1-008] 在`参考条件`落实：不把恢复ICL称相似度已验证；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
9. [S16-R1-009] 在`参考条件`落实：检查参考是否多人；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
10. [S16-R1-010] 在`参考条件`落实：多人参考必须换干净单人样本；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
11. [S16-R1-011] 在`提示缓存`落实：核查Faster路径键缓存；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
12. [S16-R1-012] 在`提示缓存`落实：相同路径换音频必须失效；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
13. [S16-R1-013] 在`提示缓存`落实：比较参考内容哈希；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
14. [S16-R1-014] 在`提示缓存`落实：清除该路径旧缓存项；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
15. [S16-R1-015] 在`提示缓存`落实：不删除模型全局权重；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
16. [S16-R1-016] 在`提示缓存`落实：不信任仅profile_id相同；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
17. [S16-R1-017] 在`提示缓存`落实：预热与生成采用同模式；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
18. [S16-R1-018] 在`提示缓存`落实：dtype重载后重新构建条件；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
19. [S16-R1-019] 在`提示缓存`落实：不把错误预热当就绪；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
20. [S16-R1-020] 在`提示缓存`落实：缓存失效增加回归；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
21. [S16-R1-021] 在`会话绑定`落实：会话开始固定参考内容指纹；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
22. [S16-R1-022] 在`会话绑定`落实：Go与Python指纹算法一致；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
23. [S16-R1-023] 在`会话绑定`落实：包含WAV与匹配文本；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
24. [S16-R1-024] 在`会话绑定`落实：包含语言字段；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
25. [S16-R1-025] 在`会话绑定`落实：长度前缀避免分隔歧义；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
26. [S16-R1-026] 在`会话绑定`落实：每个语段携带同一指纹；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
27. [S16-R1-027] 在`会话绑定`落实：Worker取锁后重新读取档案；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
28. [S16-R1-028] 在`会话绑定`落实：不同版本先拒绝后输出；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
29. [S16-R1-029] 在`会话绑定`落实：不重试成另一个声音；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
30. [S16-R1-030] 在`会话绑定`落实：缺文件不降级原模型；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
31. [S16-R1-031] 在`双卡一致`落实：保留每T4一个模型；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
32. [S16-R1-032] 在`双卡一致`落实：比较两卡使用的参考指纹；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
33. [S16-R1-033] 在`双卡一致`落实：保留同session条件不变；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
34. [S16-R1-034] 在`双卡一致`落实：候选切换只能影响新会话；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
35. [S16-R1-035] 在`双卡一致`落实：旧会话版本不符明确失败；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
36. [S16-R1-036] 在`双卡一致`落实：声音更新与合成共用锁；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
37. [S16-R1-037] 在`双卡一致`落实：锁后重取profile避免旧引用；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
38. [S16-R1-038] 在`双卡一致`落实：不要以profile名称证明相同；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
39. [S16-R1-039] 在`双卡一致`落实：不把RMS一致当同一说话人；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
40. [S16-R1-040] 在`双卡一致`落实：两张卡实际试听仍必需；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
41. [S16-R1-041] 在`生成稳定`落实：相邻段使用稳定seed策略；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
42. [S16-R1-042] 在`生成稳定`落实：不随意每段改变采样条件；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
43. [S16-R1-043] 在`生成稳定`落实：不以降温保证身份；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
44. [S16-R1-044] 在`生成稳定`落实：不默认删除情感；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
45. [S16-R1-045] 在`生成稳定`落实：保留语言参数；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
46. [S16-R1-046] 在`生成稳定`落实：保留max_new_tokens安全预算；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
47. [S16-R1-047] 在`生成稳定`落实：保留取消后的生成器close；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
48. [S16-R1-048] 在`生成稳定`落实：不引入随机参考混合；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
49. [S16-R1-049] 在`生成稳定`落实：不混用候选锚点；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
50. [S16-R1-050] 在`生成稳定`落实：不跨用户共享提示；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。

追问结论：工程取舍已明确，不向用户重复提问；未提供真实音频与T4不能对声学或速度声称100%。


## 问题20：沙沙声和RTF0.3能否靠换语言、加副本或提高增益解决？

具体选项：A强降噪/多副本；B有界生成码上下文、两帧lookahead、限制噪声增益、分阶段测量；C缩短或加速音频冒充RTF下降。

推荐选择：B。

详细回答：删除全历史cat，窗口25帧上下文+chunk+2帧待提交，禁止参考码解码；留160ms未来上下文减少块末不稳定。每任务重置响度状态、默认最大增益从12回到6dB，目标仍-18，显式可调。会增加约160ms音频lookahead，不能称免费低延迟或真实去噪已验。

本题回答后、进入下一题前的50项开发建议：

1. [S16-R2-001] 在`解码路径`落实：使用实际Faster0.5.4准备接口；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
2. [S16-R2-002] 在`解码路径`落实：只解码新生成声学码；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
3. [S16-R2-003] 在`解码路径`落实：禁止参考PCM占位；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
4. [S16-R2-004] 在`解码路径`落实：不得猜比例裁参考音频；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
5. [S16-R2-005] 在`解码路径`落实：codec采样率必须24k；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
6. [S16-R2-006] 在`解码路径`落实：逐帧1920样本契约需检查；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
7. [S16-R2-007] 在`解码路径`落实：不兼容长度明确失败；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
8. [S16-R2-008] 在`解码路径`落实：保留码组16列；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
9. [S16-R2-009] 在`解码路径`落实：不偷改codec权重；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
10. [S16-R2-010] 在`解码路径`落实：API签名变化明确报错；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
11. [S16-R2-011] 在`有界窗口`落实：删除每块全历史cat；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
12. [S16-R2-012] 在`有界窗口`落实：左上下文固定25帧；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
13. [S16-R2-013] 在`有界窗口`落实：待提交尾部保留2帧；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
14. [S16-R2-014] 在`有界窗口`落实：窗口随chunk有上限；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
15. [S16-R2-015] 在`有界窗口`落实：新块仅输出未提交样本；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
16. [S16-R2-016] 在`有界窗口`落实：提交游标单调；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
17. [S16-R2-017] 在`有界窗口`落实：末尾只flush一次；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
18. [S16-R2-018] 在`有界窗口`落实：取消不flush迟到音频；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
19. [S16-R2-019] 在`有界窗口`落实：新旧窗口无重复样本；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
20. [S16-R2-020] 在`有界窗口`落实：窗口长度记录便于核验；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
21. [S16-R2-021] 在`块接缝`落实：未来两帧降低边缘重解码差异；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
22. [S16-R2-022] 在`块接缝`落实：不对每块单独归一化；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
23. [S16-R2-023] 在`块接缝`落实：保留时间连续性；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
24. [S16-R2-024] 在`块接缝`落实：不要对每块强淡入；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
25. [S16-R2-025] 在`块接缝`落实：短于lookahead暂不输出；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
26. [S16-R2-026] 在`块接缝`落实：最后短块不能丢；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
27. [S16-R2-027] 在`块接缝`落实：音频总样本不缩水；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
28. [S16-R2-028] 在`块接缝`落实：不把重叠输出拼两次；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
29. [S16-R2-029] 在`块接缝`落实：真实边界爆音仍要听；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
30. [S16-R2-030] 在`块接缝`落实：增加右边缘不稳定fixture；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
31. [S16-R2-031] 在`沙沙声`落实：不生成额外呼吸噪声；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
32. [S16-R2-032] 在`沙沙声`落实：旧breath环境不能启用拼接；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
33. [S16-R2-033] 在`沙沙声`落实：限制向上增益防底噪变大；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
34. [S16-R2-034] 在`沙沙声`落实：输出目标仍负18dBFS；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
35. [S16-R2-035] 在`沙沙声`落实：保留软限幅；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
36. [S16-R2-036] 在`沙沙声`落实：不默认强低通损坏齿音；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
37. [S16-R2-037] 在`沙沙声`落实：不抹掉所有清辅音；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
38. [S16-R2-038] 在`沙沙声`落实：不假装无声就是降噪成功；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
39. [S16-R2-039] 在`沙沙声`落实：无原音频不确定噪声来源；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
40. [S16-R2-040] 在`沙沙声`落实：分别检查模型原PCM与后处理；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
41. [S16-R2-041] 在`响度状态`落实：每任务重建leveler状态；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
42. [S16-R2-042] 在`响度状态`落实：防双卡历史包络不同；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
43. [S16-R2-043] 在`响度状态`落实：保留每段淡入淡出；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
44. [S16-R2-044] 在`响度状态`落实：无语音不flush上段尾巴；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
45. [S16-R2-045] 在`响度状态`落实：显式配置最大增益；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
46. [S16-R2-046] 在`响度状态`落实：非法增益回退安全值；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
47. [S16-R2-047] 在`响度状态`落实：新旧档案一致输出策略；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
48. [S16-R2-048] 在`响度状态`落实：不能靠过载变响；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
49. [S16-R2-049] 在`响度状态`落实：用低电平与满幅信号测试；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
50. [S16-R2-050] 在`响度状态`落实：Rust与NumPy分别标边界；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。

追问结论：工程取舍已明确，不向用户重复提问；未提供真实音频与T4不能对声学或速度声称100%。


## 问题21：如何验证相似、单一声音、无沙沙与RTF≤0.3而不造硬件结果？

具体选项：A用Mock吞吐宣布达标；B三轮工程/真实库接口实验，提供实际双worker基准入口并保留声学与T4门禁；C只比较文件哈希。

推荐选择：B。

详细回答：工程测试确认绑定、边界、样本完整、取消；真实Faster控制流用明确注入CPU模型fixture，tinyMimi仅保护依赖。目标机基准调用已驻留真实worker、输出逐GPU墙钟RTF与WAV，0.3未达就失败；没有CUDA则blocked。听感与参考单人性仍需真人审核，不称100%信心。

本题回答后、进入下一题前的50项开发建议：

1. [S16-R3-001] 在`代码审查`落实：三轮读全源并记录哈希；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
2. [S16-R3-002] 在`代码审查`落实：Python AST巡检；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
3. [S16-R3-003] 在`代码审查`落实：Go格式和race；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
4. [S16-R3-004] 在`代码审查`落实：浏览器JS语法；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
5. [S16-R3-005] 在`代码审查`落实：Rust未修改仍说明现场边界；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
6. [S16-R3-006] 在`代码审查`落实：逐专题审视引用关系；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
7. [S16-R3-007] 在`代码审查`落实：不把哈希清单当语义证明；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
8. [S16-R3-008] 在`代码审查`落实：每轮100建议逐项处置；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
9. [S16-R3-009] 在`代码审查`落实：未实施项明确保留；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
10. [S16-R3-010] 在`代码审查`落实：别把300建议当300bug；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
11. [S16-R3-011] 在`参考绑定测试`落实：中英转写跨语言指纹一致；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
12. [S16-R3-012] 在`参考绑定测试`落实：WAV变更指纹变化；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
13. [S16-R3-013] 在`参考绑定测试`落实：文本变更指纹变化；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
14. [S16-R3-014] 在`参考绑定测试`落实：语言变更指纹变化；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
15. [S16-R3-015] 在`参考绑定测试`落实：质量统计变化不改变声音指纹；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
16. [S16-R3-016] 在`参考绑定测试`落实：旧Worker缓存不能放行新pin；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
17. [S16-R3-017] 在`参考绑定测试`落实：任务等待期间换档案需重校验；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
18. [S16-R3-018] 在`参考绑定测试`落实：错误绑定不能输出PCM；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
19. [S16-R3-019] 在`参考绑定测试`落实：两卡pin不等必须失败；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
20. [S16-R3-020] 在`参考绑定测试`落实：取消不触发重加载；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
21. [S16-R3-021] 在`解码测试`落实：样本总数等于总帧乘1920；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
22. [S16-R3-022] 在`解码测试`落实：reference marker严格拒绝；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
23. [S16-R3-023] 在`解码测试`落实：短码块可暂存；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
24. [S16-R3-024] 在`解码测试`落实：最大窗口有界；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
25. [S16-R3-025] 在`解码测试`落实：窗口左端超出不可访问；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
26. [S16-R3-026] 在`解码测试`落实：lookahead尾部完整flush；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
27. [S16-R3-027] 在`解码测试`落实：flush幂等；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
28. [S16-R3-028] 在`解码测试`落实：取消丢尾部；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
29. [S16-R3-029] 在`解码测试`落实：非有限输出不得成功；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
30. [S16-R3-030] 在`解码测试`落实：错误采样率拒绝；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
31. [S16-R3-031] 在`RTF实验入口`落实：调用真实worker而非造测量；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
32. [S16-R3-032] 在`RTF实验入口`落实：用户显式启用目标机测试；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
33. [S16-R3-033] 在`RTF实验入口`落实：不启动第三模型；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
34. [S16-R3-034] 在`RTF实验入口`落实：仅读取既有档案；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
35. [S16-R3-035] 在`RTF实验入口`落实：保存生成WAV供试听；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
36. [S16-R3-036] 在`RTF实验入口`落实：报告不含口令；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
37. [S16-R3-037] 在`RTF实验入口`落实：至少三次重复；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
38. [S16-R3-038] 在`RTF实验入口`落实：测前确认双worker真实引擎；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
39. [S16-R3-039] 在`RTF实验入口`落实：未达0.3就failed而非pass；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
40. [S16-R3-040] 在`RTF实验入口`落实：没有CUDA明确blocked；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
41. [S16-R3-041] 在`现有服务`落实：完整Python三轮；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
42. [S16-R3-042] 在`现有服务`落实：Node三轮；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
43. [S16-R3-043] 在`现有服务`落实：Go race count3；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
44. [S16-R3-044] 在`现有服务`落实：完整Chromium三轮；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
45. [S16-R3-045] 在`现有服务`落实：协议生命周期三轮；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
46. [S16-R3-046] 在`现有服务`落实：真实Faster接口三轮；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
47. [S16-R3-047] 在`现有服务`落实：HF导入tinyMimi三轮；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
48. [S16-R3-048] 在`现有服务`落实：保留训练CPU等价门禁；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
49. [S16-R3-049] 在`现有服务`落实：不忽略失败测试；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
50. [S16-R3-050] 在`现有服务`落实：修复后完整重跑；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。

追问结论：工程取舍已明确，不向用户重复提问；未提供真实音频与T4不能对声学或速度声称100%。


## 问题22：超过15秒录音为什么建档失败，如何修复且不伪造对齐？

具体选项：A删16秒限制后配整段全文；B保留音频/转写匹配，使用词级时间戳切分，缺失则短音频窗口真实重识别；C按字数比例分全文。

推荐：B。

详细回答：源码接收长录音，但候选仅取完整2.5–16秒ASR段，忽略已有words。一个28秒段因此无候选。B按完整词切分并验证词文一致；缺词时间不猜，重新ASR实际窗口。保留长音频完整分析，长manual全文不冒充逐字对齐。

进入下一题之前的50项实施建议：

1. [S17-R1-001] `截图与根因`：截图是15而非16不能当新包效果；以代码/测试收据或明确真实硬件门禁核查。
2. [S17-R1-002] `截图与根因`：录音限额与锚点限额分开；以代码/测试收据或明确真实硬件门禁核查。
3. [S17-R1-003] `截图与根因`：重现单个28.7秒ASR段；以代码/测试收据或明确真实硬件门禁核查。
4. [S17-R1-004] `截图与根因`：保留16的逐字匹配约束；以代码/测试收据或明确真实硬件门禁核查。
5. [S17-R1-005] `截图与根因`：不能将长音频硬截配全文；以代码/测试收据或明确真实硬件门禁核查。
6. [S17-R1-006] `截图与根因`：保留ASR词级时间戳；以代码/测试收据或明确真实硬件门禁核查。
7. [S17-R1-007] `截图与根因`：按完整词组而非字符比例切分；以代码/测试收据或明确真实硬件门禁核查。
8. [S17-R1-008] `截图与根因`：词与原段文本必须核对；以代码/测试收据或明确真实硬件门禁核查。
9. [S17-R1-009] `截图与根因`：缺词时间走音频窗口重新ASR；以代码/测试收据或明确真实硬件门禁核查。
10. [S17-R1-010] `截图与根因`：不能凭低RMS断定无人声；以代码/测试收据或明确真实硬件门禁核查。
11. [S17-R1-011] `词级对齐`：验证时间戳有限；以代码/测试收据或明确真实硬件门禁核查。
12. [S17-R1-012] `词级对齐`：验证起止单调；以代码/测试收据或明确真实硬件门禁核查。
13. [S17-R1-013] `词级对齐`：验证不越源音频；以代码/测试收据或明确真实硬件门禁核查。
14. [S17-R1-014] `词级对齐`：拒绝重叠倒序词；以代码/测试收据或明确真实硬件门禁核查。
15. [S17-R1-015] `词级对齐`：Unicode字母数字核对转写；以代码/测试收据或明确真实硬件门禁核查。
16. [S17-R1-016] `词级对齐`：不要丢标点后汉字；以代码/测试收据或明确真实硬件门禁核查。
17. [S17-R1-017] `词级对齐`：长单词超窗口重新ASR；以代码/测试收据或明确真实硬件门禁核查。
18. [S17-R1-018] `词级对齐`：短尾保留在分析收据；以代码/测试收据或明确真实硬件门禁核查。
19. [S17-R1-019] `词级对齐`：跨文件绝不合并文字；以代码/测试收据或明确真实硬件门禁核查。
20. [S17-R1-020] `词级对齐`：对齐失败有明确中文建议；以代码/测试收据或明确真实硬件门禁核查。
21. [S17-R1-021] `长音频重识别`：仅问题长段需要窗口ASR；以代码/测试收据或明确真实硬件门禁核查。
22. [S17-R1-022] `长音频重识别`：每窗口音频和转写独立匹配；以代码/测试收据或明确真实硬件门禁核查。
23. [S17-R1-023] `长音频重识别`：使用原音频实际切片；以代码/测试收据或明确真实硬件门禁核查。
24. [S17-R1-024] `长音频重识别`：偏移恢复绝对时间；以代码/测试收据或明确真实硬件门禁核查。
25. [S17-R1-025] `长音频重识别`：边界优先静音；以代码/测试收据或明确真实硬件门禁核查。
26. [S17-R1-026] `长音频重识别`：窗口必须前进不死循环；以代码/测试收据或明确真实硬件门禁核查。
27. [S17-R1-027] `长音频重识别`：最末窗口不丢；以代码/测试收据或明确真实硬件门禁核查。
28. [S17-R1-028] `长音频重识别`：无语音窗口不伪造文字；以代码/测试收据或明确真实硬件门禁核查。
29. [S17-R1-029] `长音频重识别`：沿用ASR锁及CPU复用；以代码/测试收据或明确真实硬件门禁核查。
30. [S17-R1-030] `长音频重识别`：进度显示窗口计数；以代码/测试收据或明确真实硬件门禁核查。
31. [S17-R1-031] `长参考语义`：长录音可以超过15秒；以代码/测试收据或明确真实硬件门禁核查。
32. [S17-R1-032] `长参考语义`：不能无限把20分钟塞进ICL；以代码/测试收据或明确真实硬件门禁核查。
33. [S17-R1-033] `长参考语义`：提供16与24秒参考窗口；以代码/测试收据或明确真实硬件门禁核查。
34. [S17-R1-034] `长参考语义`：默认16保护旧短样本；以代码/测试收据或明确真实硬件门禁核查。
35. [S17-R1-035] `长参考语义`：24明确标为实验与较慢；以代码/测试收据或明确真实硬件门禁核查。
36. [S17-R1-036] `长参考语义`：手工转写仅单短文件直接采用；以代码/测试收据或明确真实硬件门禁核查。
37. [S17-R1-037] `长参考语义`：长手工全文不能按时长分配；以代码/测试收据或明确真实硬件门禁核查。
38. [S17-R1-038] `长参考语义`：记录源总时长与选中锚点；以代码/测试收据或明确真实硬件门禁核查。
39. [S17-R1-039] `长参考语义`：记录重切分和重识别数量；以代码/测试收据或明确真实硬件门禁核查。
40. [S17-R1-040] `长参考语义`：明确建档不是全数据训练；以代码/测试收据或明确真实硬件门禁核查。
41. [S17-R1-041] `输入与安全`：窗口值只允许16或24；以代码/测试收据或明确真实硬件门禁核查。
42. [S17-R1-042] `输入与安全`：表单和库入口都独立校验；以代码/测试收据或明确真实硬件门禁核查。
43. [S17-R1-043] `输入与安全`：失败保留本地录音；以代码/测试收据或明确真实硬件门禁核查。
44. [S17-R1-044] `输入与安全`：取消不得删除源音频；以代码/测试收据或明确真实硬件门禁核查。
45. [S17-R1-045] `输入与安全`：不自动云传原音；以代码/测试收据或明确真实硬件门禁核查。
46. [S17-R1-046] `输入与安全`：拒绝非有限PCM；以代码/测试收据或明确真实硬件门禁核查。
47. [S17-R1-047] `输入与安全`：保留20分钟录音预算；以代码/测试收据或明确真实硬件门禁核查。
48. [S17-R1-048] `输入与安全`：低电平提示调整设备；以代码/测试收据或明确真实硬件门禁核查。
49. [S17-R1-049] `输入与安全`：提示麦克风距离不替人猜设备；以代码/测试收据或明确真实硬件门禁核查。
50. [S17-R1-050] `输入与安全`：保留原始至16冻结；以代码/测试收据或明确真实硬件门禁核查。

追问结论：方案边界明确，不向用户提问；未知的真实声学结果保留未知，不声称100%。


## 问题23：超长参考是否一定更像，怎样保证短参考与双卡条件一致？

具体选项：A无限参考整段进模型；B可选16/24秒锚点，长录音用于选择代表片段，指纹同时绑定四项采样参数；C混入参考原音增加相似。

推荐：B。

详细回答：更多同说话人干净录音有助选样，但参考上下文不是训练，不能保证长于短。默认ICL与匹配转写保持；新增24秒明确实验和延迟代价。四生成参数及参考内容共同绑定，防两卡不同修订；同条件也不保证硬件波形相同或100%音色。

进入下一题之前的50项实施建议：

1. [S17-R2-001] `短参考与音色`：继续使用ICL匹配文本；以代码/测试收据或明确真实硬件门禁核查。
2. [S17-R2-002] `短参考与音色`：不退回15纯向量默认；以代码/测试收据或明确真实硬件门禁核查。
3. [S17-R2-003] `短参考与音色`：新旧GPU不能混版本；以代码/测试收据或明确真实硬件门禁核查。
4. [S17-R2-004] `短参考与音色`：相同参考绑定采样参数；以代码/测试收据或明确真实硬件门禁核查。
5. [S17-R2-005] `短参考与音色`：Go和Python浮点编码一致；以代码/测试收据或明确真实硬件门禁核查。
6. [S17-R2-006] `短参考与音色`：缺省参数也计入指纹；以代码/测试收据或明确真实硬件门禁核查。
7. [S17-R2-007] `短参考与音色`：不接受NaN温度；以代码/测试收据或明确真实硬件门禁核查。
8. [S17-R2-008] `短参考与音色`：改温度使旧会话失效；以代码/测试收据或明确真实硬件门禁核查。
9. [S17-R2-009] `短参考与音色`：参数相同不是音色绝对相同；以代码/测试收据或明确真实硬件门禁核查。
10. [S17-R2-010] `短参考与音色`：真人试听仍是独立门禁；以代码/测试收据或明确真实硬件门禁核查。
11. [S17-R2-011] `多卡参数`：绑定temperature；以代码/测试收据或明确真实硬件门禁核查。
12. [S17-R2-012] `多卡参数`：绑定top_k；以代码/测试收据或明确真实硬件门禁核查。
13. [S17-R2-013] `多卡参数`：绑定top_p；以代码/测试收据或明确真实硬件门禁核查。
14. [S17-R2-014] `多卡参数`：绑定repetition_penalty；以代码/测试收据或明确真实硬件门禁核查。
15. [S17-R2-015] `多卡参数`：top_k必须整数；以代码/测试收据或明确真实硬件门禁核查。
16. [S17-R2-016] `多卡参数`：统一默认参数数值；以代码/测试收据或明确真实硬件门禁核查。
17. [S17-R2-017] `多卡参数`：每次合成锁内复核；以代码/测试收据或明确真实硬件门禁核查。
18. [S17-R2-018] `多卡参数`：预计算提示快照保留；以代码/测试收据或明确真实硬件门禁核查。
19. [S17-R2-019] `多卡参数`：不混用不同条件模式；以代码/测试收据或明确真实硬件门禁核查。
20. [S17-R2-020] `多卡参数`：不声称两卡波形逐位相同；以代码/测试收据或明确真实硬件门禁核查。
21. [S17-R2-021] `参考质量`：记录原始RMS；以代码/测试收据或明确真实硬件门禁核查。
22. [S17-R2-022] `参考质量`：记录原始峰值；以代码/测试收据或明确真实硬件门禁核查。
23. [S17-R2-023] `参考质量`：记录SNR估计而非真值；以代码/测试收据或明确真实硬件门禁核查。
24. [S17-R2-024] `参考质量`：低电平给风险提示不直接拒绝；以代码/测试收据或明确真实硬件门禁核查。
25. [S17-R2-025] `参考质量`：响度归一化不是降噪；以代码/测试收据或明确真实硬件门禁核查。
26. [S17-R2-026] `参考质量`：MFCC相似不是可靠声纹真值；以代码/测试收据或明确真实硬件门禁核查。
27. [S17-R2-027] `参考质量`：避免强降噪损伤辅音；以代码/测试收据或明确真实硬件门禁核查。
28. [S17-R2-028] `参考质量`：参考多人必须审核；以代码/测试收据或明确真实硬件门禁核查。
29. [S17-R2-029] `参考质量`：24秒未必比10秒好；以代码/测试收据或明确真实硬件门禁核查。
30. [S17-R2-030] `参考质量`：不播放原录音补相似度；以代码/测试收据或明确真实硬件门禁核查。
31. [S17-R2-031] `连续朗读`：只调整朗读聚合不延后聊天首句；以代码/测试收据或明确真实硬件门禁核查。
32. [S17-R2-032] `连续朗读`：减少过多独立合成语段；以代码/测试收据或明确真实硬件门禁核查。
33. [S17-R2-033] `连续朗读`：优先完整句子标点；以代码/测试收据或明确真实硬件门禁核查。
34. [S17-R2-034] `连续朗读`：保留原始全文字符；以代码/测试收据或明确真实硬件门禁核查。
35. [S17-R2-035] `连续朗读`：不合并不同用户任务；以代码/测试收据或明确真实硬件门禁核查。
36. [S17-R2-036] `连续朗读`：保留取消和背压；以代码/测试收据或明确真实硬件门禁核查。
37. [S17-R2-037] `连续朗读`：不跨词叠加PCM；以代码/测试收据或明确真实硬件门禁核查。
38. [S17-R2-038] `连续朗读`：不删除语音以隐藏接缝；以代码/测试收据或明确真实硬件门禁核查。
39. [S17-R2-039] `连续朗读`：保留已有codec有界上下文；以代码/测试收据或明确真实硬件门禁核查。
40. [S17-R2-040] `连续朗读`：自然韵律不能仅靠交叉淡化保证；以代码/测试收据或明确真实硬件门禁核查。
41. [S17-R2-041] `噪声边界`：继续禁参考呼吸拼接；以代码/测试收据或明确真实硬件门禁核查。
42. [S17-R2-042] `噪声边界`：不生成白噪声补停顿；以代码/测试收据或明确真实硬件门禁核查。
43. [S17-R2-043] `噪声边界`：保留软限幅；以代码/测试收据或明确真实硬件门禁核查。
44. [S17-R2-044] `噪声边界`：保留可控增益；以代码/测试收据或明确真实硬件门禁核查。
45. [S17-R2-045] `噪声边界`：不把静音当去噪成功；以代码/测试收据或明确真实硬件门禁核查。
46. [S17-R2-046] `噪声边界`：不默认低通抹齿音；以代码/测试收据或明确真实硬件门禁核查。
47. [S17-R2-047] `噪声边界`：新统计不得泄漏原文本；以代码/测试收据或明确真实硬件门禁核查。
48. [S17-R2-048] `噪声边界`：生成WAV可供独立试听；以代码/测试收据或明确真实硬件门禁核查。
49. [S17-R2-049] `噪声边界`：缺真实音频不宣布零噪声；以代码/测试收据或明确真实硬件门禁核查。
50. [S17-R2-050] `噪声边界`：不得缩短输出冒RTF达标；以代码/测试收据或明确真实硬件门禁核查。

追问结论：方案边界明确，不向用户提问；未知的真实声学结果保留未知，不声称100%。


## 问题24：如何自然连续朗读、排查沙沙声并诚实验收？

具体选项：A强低通加跨词重叠；B适度增大只读文本聚合、保留正文/取消/codec，参考质量提示与真实双卡WAV验收；C静音或删字冒无噪声。

推荐：B。

详细回答：减少独立语段可降低重启韵律次数，但不声称等同整段联合生成。保留聊天第一句早提交，不跨词叠加PCM。记录低输入电平而不从截图猜设备；强降噪会损伤音色，不无证据默认开启。三轮工程/实际库控制实验外，训练权重试听和T4 RTF仍需真实硬件。

进入下一题之前的50项实施建议：

1. [S17-R3-001] `重现门禁`：单个28.7秒词级段建档成功；以代码/测试收据或明确真实硬件门禁核查。
2. [S17-R3-002] `重现门禁`：单个60秒段词级切分；以代码/测试收据或明确真实硬件门禁核查。
3. [S17-R3-003] `重现门禁`：20分钟时间戳规划有界；以代码/测试收据或明确真实硬件门禁核查。
4. [S17-R3-004] `重现门禁`：缺词时间戳实际窗口重识别；以代码/测试收据或明确真实硬件门禁核查。
5. [S17-R3-005] `重现门禁`：文本不匹配必须回识别；以代码/测试收据或明确真实硬件门禁核查。
6. [S17-R3-006] `重现门禁`：长manual全文不错误拼接；以代码/测试收据或明确真实硬件门禁核查。
7. [S17-R3-007] `重现门禁`：短manual16秒保持兼容；以代码/测试收据或明确真实硬件门禁核查。
8. [S17-R3-008] `重现门禁`：24秒锚点不越界；以代码/测试收据或明确真实硬件门禁核查。
9. [S17-R3-009] `重现门禁`：无声和非法时间戳不造成功；以代码/测试收据或明确真实硬件门禁核查。
10. [S17-R3-010] `重现门禁`：每项做三轮回归；以代码/测试收据或明确真实硬件门禁核查。
11. [S17-R3-011] `接口门禁`：浏览器发送参考窗口字段；以代码/测试收据或明确真实硬件门禁核查。
12. [S17-R3-012] `接口门禁`：默认值16可见；以代码/测试收据或明确真实硬件门禁核查。
13. [S17-R3-013] `接口门禁`：24选项真实进入后端；以代码/测试收据或明确真实硬件门禁核查。
14. [S17-R3-014] `接口门禁`：锁定清除私有转写；以代码/测试收据或明确真实硬件门禁核查。
15. [S17-R3-015] `接口门禁`：表单非法值拒绝；以代码/测试收据或明确真实硬件门禁核查。
16. [S17-R3-016] `接口门禁`：库处理同样校验；以代码/测试收据或明确真实硬件门禁核查。
17. [S17-R3-017] `接口门禁`：服务重启新包版本可识别；以代码/测试收据或明确真实硬件门禁核查。
18. [S17-R3-018] `接口门禁`：新包逐字节复制；以代码/测试收据或明确真实硬件门禁核查。
19. [S17-R3-019] `接口门禁`：16包哈希冻结；以代码/测试收据或明确真实硬件门禁核查。
20. [S17-R3-020] `接口门禁`：正式工作台保持不变；以代码/测试收据或明确真实硬件门禁核查。
21. [S17-R3-021] `参数指纹测试`：中英转写跨语言一致；以代码/测试收据或明确真实硬件门禁核查。
22. [S17-R3-022] `参数指纹测试`：默认值与显式默认相同；以代码/测试收据或明确真实硬件门禁核查。
23. [S17-R3-023] `参数指纹测试`：四参数分别变更使pin变化；以代码/测试收据或明确真实硬件门禁核查。
24. [S17-R3-024] `参数指纹测试`：NaN和无穷拒绝；以代码/测试收据或明确真实硬件门禁核查。
25. [S17-R3-025] `参数指纹测试`：非整数top_k拒绝；以代码/测试收据或明确真实硬件门禁核查。
26. [S17-R3-026] `参数指纹测试`：Worker不输出不符pin的PCM；以代码/测试收据或明确真实硬件门禁核查。
27. [S17-R3-027] `参数指纹测试`：Go协议携带固定pin；以代码/测试收据或明确真实硬件门禁核查。
28. [S17-R3-028] `参数指纹测试`：不改adapter来源绑定；以代码/测试收据或明确真实硬件门禁核查。
29. [S17-R3-029] `参数指纹测试`：新旧包混跑明确重启；以代码/测试收据或明确真实硬件门禁核查。
30. [S17-R3-030] `参数指纹测试`：不把指纹当身份认证；以代码/测试收据或明确真实硬件门禁核查。
31. [S17-R3-031] `验证与实验`：Python完整三轮；以代码/测试收据或明确真实硬件门禁核查。
32. [S17-R3-032] `验证与实验`：Node完整三轮；以代码/测试收据或明确真实硬件门禁核查。
33. [S17-R3-033] `验证与实验`：Go race三轮；以代码/测试收据或明确真实硬件门禁核查。
34. [S17-R3-034] `验证与实验`：Chromium完整三轮；以代码/测试收据或明确真实硬件门禁核查。
35. [S17-R3-035] `验证与实验`：六服务协议各三轮；以代码/测试收据或明确真实硬件门禁核查。
36. [S17-R3-036] `验证与实验`：实际Faster控制接口三轮；以代码/测试收据或明确真实硬件门禁核查。
37. [S17-R3-037] `验证与实验`：真实tiny codec三轮；以代码/测试收据或明确真实硬件门禁核查。
38. [S17-R3-038] `验证与实验`：Mimi导入重载三轮；以代码/测试收据或明确真实硬件门禁核查。
39. [S17-R3-039] `验证与实验`：CPU训练等价三轮；以代码/测试收据或明确真实硬件门禁核查。
40. [S17-R3-040] `验证与实验`：所有CPU模型明确不是Qwen音质证据；以代码/测试收据或明确真实硬件门禁核查。
41. [S17-R3-041] `记录与交付`：问题22回答后给50建议；以代码/测试收据或明确真实硬件门禁核查。
42. [S17-R3-042] `记录与交付`：问题23回答后给50建议；以代码/测试收据或明确真实硬件门禁核查。
43. [S17-R3-043] `记录与交付`：问题24回答后给50建议；以代码/测试收据或明确真实硬件门禁核查。
44. [S17-R3-044] `记录与交付`：方案先于产品修改；以代码/测试收据或明确真实硬件门禁核查。
45. [S17-R3-045] `记录与交付`：每次失败日志保留；以代码/测试收据或明确真实硬件门禁核查。
46. [S17-R3-046] `记录与交付`：逐条300建议分类；以代码/测试收据或明确真实硬件门禁核查。
47. [S17-R3-047] `记录与交付`：无硬件保留BLOCKED；以代码/测试收据或明确真实硬件门禁核查。
48. [S17-R3-048] `记录与交付`：真实RTF0.3仍需测量；以代码/测试收据或明确真实硬件门禁核查。
49. [S17-R3-049] `记录与交付`：完整57份备忘录内嵌；以代码/测试收据或明确真实硬件门禁核查。
50. [S17-R3-050] `记录与交付`：不承诺100相似零噪声；以代码/测试收据或明确真实硬件门禁核查。

追问结论：方案边界明确，不向用户提问；未知的真实声学结果保留未知，不声称100%。

---

## 内嵌备忘录：KAGGLE_SECURITY_PLAN.md

# 下一阶段执行门禁：访问控制与资源预算

日期：2026-10-21。继续保留首轮包和原始kaggle，输出独立step2包。

## 本阶段确定范围

1. 所有 `/api` 入口必须验证内存Bearer口令，未配置则拒绝启动，不设免认证旁路；页面静态骨架可公开，声音/指标/收费接口不得匿名访问。
2. Kaggle启动器优先读取 `QTTS_ACCESS_TOKEN` Secret/环境变量，否则在 /tmp 的0700私有认证目录创建0600随机口令文件（默认不进入Notebook输出或声音库导出）；不在URL、日志或浏览器存储中放口令。健康探针与命令行工具同步适配。
3. 浏览器显式解锁/锁定；只在当前内存使用口令，同源请求注入认证，不把口令发送给外部网关地址。
4. 网关限制JSON/上传总字节、文本/历史长度、请求频率、并发会话和昂贵操作；有界请求超时；代理不把口令或DeepSeek Key传给分析服务。
5. 分析服务在multipart解析前限制请求体；文件数量/单文件/总量/空文件限制；只接受有界后台构建，清理终态任务记录，限制解码时长和累计时长。超限必须明确拒绝，不静默截断。
6. 暂不把本版称为完整互联网多租户系统：共享单用户口令、不含账号体系/审计平台，TLS依赖可信代理；OS级磁盘配额/解码器隔离/全局worker队列专项仍需后续。

## 验证门禁

- Go httptest + `-race -count=3`：匿名/错误/正确口令、缺配置、非API静态白名单、请求大小、限流/并发/超时、代理密钥剥离、严格JSON与文本预算。
- Python：口令创建/权限/复用与弱配置拒绝；ASGI未知长度请求体超限；上传数量/尺寸/空文件、忙碌拒绝和失败释放；解码时长边界。
- Chromium：解锁、错误口令、锁定取消、不持久化口令、拒绝向外域发口令；保留首轮播放竞态用例。
- 三轮受认证的真实Go网关+双Mock worker协议回归；完整工作台和实际step2代码复制回归。
- 重打包确定性、所有资产逐字节仅解包对比；保留原始文件和step1。

GPU训练、真实DeepSeek/音质/性能验收不在上述Mock验证结论内。验收不通过则修复再跑，不以跳过或改小模型宣称成功。

---

## 内嵌备忘录：KAGGLE_SOURCE_AUDIT.md

# Kaggle 原始源码：首批修复与验证报告

> 历史首轮报告：当前源码已推进到step10，以下行号和统计对应冻结的 `kaggle-fixed-step1.py`。当前修复与边界以 `KAGGLE_STEP10_AUDIT.md` 为准；重打包器现默认生成step10。

更新日期：2026-10-21。**阶段：已收到源码并完成首批可靠性修复；不是完整GPU产品验收。**

## 1. 原文件与导出

- 原始 `kaggle`：127241字节，SHA256 `26c31621d6265bc25370bc284f2afdcf52f5edaf97e64056c2d8d5eda4a6c461`；保存在工作台正式快照，未覆盖。
- 静态解析FILES字面量，Base64严格校验、zlib解码、原22项内嵌哈希全部匹配；没有执行原启动/安装器。
- 可读源码：`kaggle/source/`。现有架构是Python＋Go＋可选Rust＋已编译JavaScript，不是纯Python单脚本。
- 修复版：`kaggle/kaggle-fixed-step1.py`，134879字节；23项资产（原22项＋Go可靠性测试）。
- 清单：`kaggle/source_manifest.json`，包含每项新旧SHA256和变更标记。
- 重打包器：`kaggle/repack.py`，只解析，不导入/运行原始启动文件；`--check`验证生成文件未过期。
- 导出是**首轮修复包**，不是“已在Kaggle全部运行成功”的最终版；运行会安装依赖、下载模型并可启动隧道，使用前阅读限制。

## 2. 有证据的首批修复

下表是21类修复/交付加固，**不等于300个缺陷或300项验收**。源码位置是当前修复版行号；部分设备依赖只完成源码与协议检查，已在证据栏注明。

| ID | 已确认问题 | 当前源码位置 | 处理 | 证据/边界 |
|---|---|---|---|---|
| A01 | T4可能错误回退BF16；FP32默认扩大显存风险 | `kaggle/source/py/worker.py:173` | 计算能力+支持探测；FP32显式允许 | dtype及模拟BF16支持测试 |
| A02 | 安装器仅在读到日志时检查超时，静默进程可挂住 | `kaggle/source/py/bootstrap.py:49` | 独立定时器终止子进程组 | 静默子进程0.2秒超时/退出码测试 |
| A03 | 并发JSON写入共享.tmp文件，相互覆盖/重命名失败 | `kaggle/source/py/qtts_common.py:104` | 唯一同目录临时文件、fsync、replace、清理 | 80次并发写入测试 |
| A04 | 恢复tar只过滤文件名，允许链接/设备，且新filter参数不兼容当前Python | `kaggle/source/py/qtts_common.py:164` | 先整包验证，再仅提取文件/目录，拒绝已有逃逸链接 | 穿越/软硬链接/已有链接/正常恢复测试 |
| A05 | Go声音ID可用于不受约束的路径拼接 | `kaggle/source/go/gateway/session.go:43` | 安全ID白名单及档案内外ID一致性 | 路径穿越与ID不一致测试 |
| A06 | worker尚未确认就提交active.json，失败也报成功 | `kaggle/source/go/gateway/main.go:244` | POST+串行；两worker确认；唯一临时文件；检查保存错误 | HTTP失败/拒绝/坏JSON/成功/无worker/方法测试 |
| A07 | LLM预算1200 tokens且默认200字限制，长输出被人为限制 | `kaggle/source/go/gateway/main.go:53` | 默认8192，可配置且校验范围；去掉200字限制 | 请求预算转发/配置边界测试；真实供应商限制待验 |
| A08 | 忽略finish_reason、错误JSON与未完成EOF | `kaggle/source/go/gateway/llm.go:61` | 明确报截断/供应商错误，不自动重复请求 | 正常DONE/stop、length、坏JSON、空/断流等7类HTTP流测试 |
| A09 | 旧请求迟到响应/PCM/finally会污染新一轮 | `kaggle/source/web/app.js:521` | 单调轮次所有权；Stop使旧轮次失效；await后检查 | 迟到响应头/迟到body及新流不被end的浏览器用例 |
| A10 | 音频初始化重入可能早发请求/丢PCM，失败形成未处理拒绝 | `kaggle/source/web/app.js:183` | 共享初始化Promise；失败复位并显示错误 | 重叠初始化、初始化失败、初始化期间停止用例 |
| A11 | DeepSeek密钥长期保存localStorage | `kaggle/source/web/app.js:1070` | 清理旧键，不回填/写入新键 | 浏览器旧键迁移与新键只入请求头测试 |
| A12 | 通配CORS允许任意网站读取/调用网关 | `kaggle/source/go/gateway/main.go:335` | 只接受同Origin；移除通配和私网跨域许可 | 同源/跨源/opaque/无Origin测试；仍不是身份认证 |
| A13 | Whisper默认占用第二张GPU，与TTS模型争显存 | `kaggle/source/py/analyst.py:253` | 默认CPU int8，GPU须显式选择 | 源码/编译检查；真实ASR未运行 |
| A14 | 65..95采样点呼吸片段的固定96点淡化会广播失败 | `kaggle/source/py/worker.py:393` | 淡化窗口随片段长度限制 | 65点真实数组单元测试 |
| A15 | NumPy卷积same对64..479点块返回480点导致长度异常 | `kaggle/source/py/audio_rt.py:152` | 改成有状态一阶去直流，保持块长度 | 0..24000采样点多种长度、类型与有限性测试 |
| A16 | 取消在成功拿到锁的瞬间到达，仍会启动旧合成 | `kaggle/source/py/worker.py:419` | 拿锁后再次检查取消，finally仍释放锁并终结协议 | 确定性取消-at-acquisition单测＋HTTP关闭后恢复模拟 |
| A17 | 模型返回非24kHz时仍按固定24kHz PCM发送 | `kaggle/source/py/worker.py:298` | 显式拒绝不兼容采样率，不假装正常播放 | 22050Hz模型返回契约模拟测试 |
| A18 | 自检缺少资源的SKIP被计成PASS | `kaggle/source/tools/selftest.py:39` | 三态记录；缺资源退出码2，失败退出码1 | 无声音档案明确SKIP单元测试 |
| A19 | 空e2e数据的all(empty)可误通过，首声None格式化崩溃 | `kaggle/source/tools/e2e_check.py:143` | 要求非空段和音频；未开始播放显示inf | 空流稳定失败、非格式崩溃单元测试 |
| A20 | 速度倍率rtf_x被UI标成标准RTF，容易倒置目标 | `kaggle/source/py/worker.py:474` | 新增耗时/时长RTF字段；保留原倍速字段和调度算法 | 双Mock管线统计字段校验；UI编译及浏览器回归 |
| A21 | 修复资产无法复现单文件分发，父启动器失败只打印不传播 | `kaggle/repack.py:35` | 独立新文件、全SHA256校验、仅解包模式、传播子进程退出码 | 确定性打包/23资产逐字节解包/原文件不变测试；实机失败传播待验 |


## 3. 本轮真实执行结果

| 检查 | 结果 | 日志 |
|---|---|---|
| Python可靠性＋打包单元测试 | **18/18通过**；包含故意缺资源的SKIP语义断言，不是GPU自检完成 | `docs/validation/qtts-python.txt` |
| Go单元、httptest、SSE、竞态 | **14个顶层测试**（含表驱动场景），`-race -count=3`通过 | `docs/validation/qtts-go-race3.txt` |
| 浏览器全部回归 | **47/47通过**＝原工作台40＋QTTS6＋实际修复包复制1 | `docs/validation/browser-all.txt` |
| QTTS专项浏览器重复3遍 | **18/18通过**；HTTP和Web Audio均为明确Mock | `docs/validation/qtts-browser-repeat3.txt` |
| 真实Go网关＋2个Mock Python worker | **三轮通过**；有序帧、文本完整、两worker参与、中断恢复、模拟零欠载 | `docs/validation/qtts-mock-pipeline.txt` |
| 工作台HTTP/API/存储 | **30/30通过**，临时目录，不修改正式工作区 | `docs/validation/workbench-api.txt` |
| JS语法、Python编译、重打包一致性 | 通过 | `docs/validation/workbench-syntax.txt`、单测日志 |

测试途中确实复现并修复短块处理和旧版Python tar参数不兼容。浏览器首次失败来自测试档案漏填breath_files，补齐真实接口字段后通过，未以修改生产逻辑掩盖无效夹具。
新取消测试最初误以为取消后不会返回统计帧；实际协议finally需要统计＋终结，已改为断言无PCM/无合成而保留终结协议。

**三轮是CPU/协议模拟，不是三轮真实GPU、训练、ASR、DeepSeek和人耳验收。Rust本轮没有重新编译；本地走NumPy路径。**

## 4. 保留的现有行为

- 原始文件及历史快照、工作台自命名空白文件/粘贴/保存/冲突/沙箱/原文复制均保留。
- 原切段器7项测试保留；双worker并行、有序汇聚、水位、失败改派逻辑未重写。
- 原声音库/多参考上传/参考缓存、校准、呼吸库/响度处理和监控保留入口；真实模型相关功能不能因入口存在就宣称实机通过。
- ASR默认改CPU、单卡须显式允许、跨域请求拒绝和密钥不再本地持久化是有意的安全/资源行为变化。

## 5. 尚未闭环的高优先级项目

1. **训练仍未实现**：原源码没有优化器/反向传播/双rank作业/训练检查点。本轮没有把prompt缓存改名为训练。后续需验证官方单说话人路径、T4兼容参数高效训练、world_size=2、样本覆盖、梯度与重载。
2. **没有真实GPU/model/API**：未运行真实Qwen、Whisper、ECAPA或DeepSeek。T4显存、第三方流式后端API、SDPA/精度/图捕获、真实长流token上限待验。
3. **性能/音质目标未达成可确认状态**：首声<3s、RTF≤0.5、99.5%相似度均无实测证据。`rtf_x`不是标准RTF；模型首chunk不等于耳朵听到的首声。
4. **公网认证未实现**：同Origin检查不是登录、不是防DNS rebinding，也不会阻止无Origin脚本/CLI。旧自动隧道逻辑仍在，需访问控制/配额后再公开；可设 `QTTS_TUNNEL=none` 禁用隧道。
5. **依赖/下载未锁定**：GPU依赖安装、第三方模型revision、Go/Rust工具下载及哈希策略待完善。`requirements-test.txt`仅固定本地CPU测试直接依赖，不是GPU安装锁。
6. **UI要求未完成**：原三标签页仍保留；两主视图、真实录音波形、样本选择与训练任务UI待做，不能把现有录音按钮算作完整波形实现。
7. **并发/容量专项仍需做**：上传大小/数量、队列上限、profile重载与任务共享状态、supervisor重启竞态、持续故障和断网恢复；激活的取消上下文/持久化故障等还需更细粒度测试。
8. **不能保证Kaggle永久在线**：会话/显存随平台停止而丢失，Dataset保存只处理资产恢复。

## 6. 可复现命令

仓库根目录，CPU测试环境（不安装torch/模型，不执行bootstrap）：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r kaggle/requirements-test.txt
npm ci
python3 kaggle/repack.py --check
.venv/bin/python -m unittest discover -s kaggle/tests -v
(cd kaggle/source/go/gateway && ../../../../.venv/bin/go test -race -count=3 -v ./...)
.venv/bin/python kaggle/tests/mock_pipeline.py
npm run check
npm test
npm run test:e2e
npm run test:e2e -- tests/browser/qtts.spec.js --repeat-each=3
```

只解包，**不会安装、读Secrets或启动服务**（目录可换成临时目录）：

```bash
QTTS_UNPACK_ONLY=1 QTTS_ROOT=/tmp/qtts-inspect python3 kaggle/kaggle-fixed-step1.py
```

修改任何asset后先 `python3 kaggle/repack.py` 再测试；原始已保存文件始终保留。测试使用临时目录和端口，正式workspace不会被回归用例替换。

## 7. 下一步顺序

先处理公网访问控制、资源限额与可复现依赖/后端兼容探针；再完成两主视图和真实录音波形；训练作为独立真实作业实现，不抢用未释放的双推理副本。具备GPU后执行单卡最小实验、双卡rank/检查点验证、真实DeepSeek和浏览器播放计时。

三轮各100项清单仍是逐项审查计划，当前仅源码交接前5项已勾选；不能用本报告21类修复或测试数量替代完整300项验收。3个历史专业问题每题50条建议保持在KAGGLE_DECISIONS.md，源码已到齐，不再重复索取。

---

## 内嵌备忘录：KAGGLE_SECURITY_AUDIT.md

> 冻结历史阶段证据；当前源码/重打包入口为step10，见KAGGLE_STEP10_AUDIT.md。下列原统计只描述当时交付，训练输入准备与训练执行不得混同。

# 第二阶段：访问控制与资源预算审查报告

日期：2026-10-21。**当前阶段已经实现并本地回归；不代表真实GPU产品验收。**

## 1. 本阶段交付与不可变基线

- 当前启动包：`kaggle/kaggle-fixed-step2.py`，155719字节、27项资产。
- 当前SHA256：`a628d1bf3f320a330d9206b5f1864e4b38a04f0bc04b26028af2e94368f111d0`；资产清单 `kaggle/source_manifest_step2.json`。
- 原始 `kaggle` 的SHA256仍为 `26c31621d6265bc25370bc284f2afdcf52f5edaf97e64056c2d8d5eda4a6c461`，原22项内嵌哈希验证通过。
- `kaggle-fixed-step1.py` 冻结保留，SHA256 `02e9bb45a14f1e168badc8f897cead0ddd7e70c884d7fd26382c9a5b49778007`；首轮清单 `source_manifest.json`不覆盖。
- `repack.py`当前生成step2；确定性比较和仅解包逐字节验证通过。原始安装器未被执行。

## 2. 处理项与对应证据

| ID | 问题 | 当前源码位置 | 处理 | 验证边界 |
|---|---|---|---|---|
| S01 | 匿名可读声音库、指标或调用收费入口 | `kaggle/source/go/gateway/security.go:108` | 所有API统一Bearer校验；缺配置不启动；失败尝试有独立预算 | Go认证/路由/失败预算测试，Mock管线匿名401 |
| S02 | 浏览器缺少解锁/锁定和凭据生命周期 | `kaggle/source/web/app.js:399` | 显式解锁，内存口令，锁定取消请求/播放/录音并清空视图 | 9个QTTS浏览器用例，专项重复3遍 |
| S03 | 跨域网关字段可能向外站发送凭据 | `kaggle/source/web/app.js:437` | 同源强校验；网关地址只读；不使用URL凭据、Cookie或浏览器存储 | 浏览器同源header/只读/刷新锁定测试；服务端Origin检查保留 |
| S04 | 自动生成凭据可能随Notebook输出导出 | `kaggle/source/py/access_control.py:16` | 默认/tmp中状态隔离的0700目录、0600文件；拒绝弱格式/链接；不打印口令 | 并发创建、复用、权限、错误配置、目录外置测试 |
| S05 | 健康探针/工具可能因认证失效，或把凭据转发模型服务 | `kaggle/source/py/access_control.py:65` | 仅本机网关探针附带口令；CLI从环境或私有目录读取 | 探针端口/域名白名单测试，受认证Mock管线 |
| S06 | 分析代理和模型进程不必要持有网关/供应商凭据 | `kaggle/source/go/gateway/main.go:348` | 剥离Authorization/代理授权/Cookie/DeepSeek Key；子进程只继承所需凭据 | 真实httptest代理与child_environment单元测试 |
| S07 | 大JSON/尾随垃圾/未知长度体绕过容量判断 | `kaggle/source/go/gateway/security.go:195` | MaxBytesReader、已知长度预检、单个JSON完整消费 | 已知/未知长度、额外JSON、垃圾与空白超限测试 |
| S08 | 并发长流/昂贵请求和频繁请求无统一准入 | `kaggle/source/go/gateway/security.go:141` | 语音与昂贵请求独立非等待并发槽；令牌桶、有限上下文期限 | 并发拒绝/槽释放/频率/超时/取消测试 |
| S09 | 长文本/历史/一致性评估列表可放大工作量 | `kaggle/source/go/gateway/security.go:225` | 文本与历史字符预算、角色检查；一致性至多6段/段200字/总1000字 | Unicode字符、历史/系统预算、评估文本预算测试 |
| S10 | multipart解析前不受上传容量约束 | `kaggle/source/py/resource_limits.py:64` | 先有界暂存，最多1MiB驻留内存，其余临时磁盘；超限不进入应用解析 | 未知长度与已知长度ASGI测试，边界与坏Content-Length |
| S11 | 无限读取文件、空文件、多文件或积压后台线程 | `kaggle/source/py/analyst.py:882` | 分块读取、数量/单个/总字节限制；后台构建仅1个，忙则429 | 文件过多/空/超限/空名称/忙碌/启动失败及释放测试 |
| S12 | 终态任务记录和声音库数量无界 | `kaggle/source/py/resource_limits.py:111` | 终态淘汰、64条记录、128声音默认限额；低于256MiB空闲拒绝创建 | 记录淘汰、声音数量、磁盘预算测试；不是OS级配额 |
| S13 | 客户端取消时提前释放仍在执行的线程名额 | `kaggle/source/py/resource_limits.py:143` | 分析名额保留到线程实际结束，取消等待者不提前释放 | 确定性取消后仍拒绝新工作，真正结束后恢复的测试 |
| S14 | 先完整解码再截断可能耗尽内存/隐藏丢样本 | `kaggle/source/py/analyst.py:51` | ffmpeg解码期限+输出时长+pipe协议白名单+2线程；soundfile先检查元数据；超时长拒绝 | 模拟ffmpeg契约、真实soundfile WAV正常/超长、累计时长测试；无ffmpeg实测 |
| S15 | 首轮bootstrap安全解包函数未显式导入 | `kaggle/source/py/bootstrap.py:37` | 修复符号导入，保留安全解包实现 | bootstrap导入可调用测试；没有执行未知安装器 |


## 3. 默认资源预算与行为变化

| 项目 | 默认值 | 配置/备注 |
|---|---|---|
| 访问凭据 | 32..256位非空格可打印ASCII；应使用强随机值 | `QTTS_ACCESS_TOKEN`；不提供免认证开关 |
| JSON请求体 | 1MiB | `QTTS_MAX_JSON_BYTES`，网关允许1024..4MiB；分析服务另有1MiB上限，实际采用更严格一侧 |
| 单次上传请求体 | 64MiB，包括multipart开销 | `QTTS_MAX_UPLOAD_BYTES`，最大512MiB |
| 文件数量/单文件大小 | 16段 / 20MiB | `QTTS_MAX_UPLOAD_FILES` / `QTTS_MAX_FILE_BYTES`，最大64段 / 128MiB |
| 解码时长 | 单文件240秒，累计900秒 | `QTTS_MAX_AUDIO_SECONDS` / `QTTS_MAX_TOTAL_AUDIO_SECONDS`；超限失败，不把截断后的数据算成功 |
| 声音库/任务记录 | 128个 / 保留64条 | `QTTS_MAX_PROFILES` / `QTTS_MAX_JOB_RECORDS`；终态淘汰后旧任务ID可能404 |
| 最低空闲磁盘 | 256MiB | 创建前预检；不是全盘硬配额 |
| 并发语音/昂贵HTTP操作 | 2 / 2 | `QTTS_MAX_SPEAK_CONCURRENT` / `QTTS_MAX_HEAVY_CONCURRENT`；拒绝等待队列，429＋Retry-After |
| 实际分析线程/构建 | 2 / 1 | 分析槽跨HTTP取消仍保留到线程结束；构建忙直接429 |
| 语音请求令牌桶 | 初始容量12，每分钟补充12 | `QTTS_SPEAK_PER_MINUTE`；不是严格滚动窗口“每分钟只能12次” |
| 一般API令牌桶 | 初始容量120，每秒补充20 | 进程级、共享单用户预算，不按IP分配无界map |
| 无效口令尝试 | 初始容量10，每秒补充1 | 耗尽返回429；不会把正确口令一起锁死 |
| 单次文本/历史 | 文本20000字符；历史16条/累计32000字符；系统提示4096字符 | `QTTS_MAX_TEXT_CHARS`、`QTTS_MAX_HISTORY_CHARS`；字符不是UTF-8字节 |
| 请求上下文期限 | 1800秒 | `QTTS_REQUEST_TIMEOUT_S`，1..7200秒；HTTP读请求另限120秒 |

静态页面骨架无需口令；所有 `/api` 路径（包括health/metrics/profiles/prep和未知API）都在统一认证边界内。API OPTIONS可响应同源预检但不会返回私密数据。非API静态文件仅允许首页与app.js，不开放目录浏览。

原来“在任意网站填写外部网关地址”的方式被有意移除：请直接打开目标网关自己的HTTPS网址。默认限额和新的显式拒绝取代原来的静默截断/无界排队，是有意且已说明的行为变化。

## 4. 如何使用口令

**推荐**在Kaggle Secrets中配置独立的强随机 `QTTS_ACCESS_TOKEN`，与DeepSeek Key分开。启动器只输出Secret名称是否加载，不输出其值。

没有配置时，由启动器在 `/tmp/qtts-auth-<用户ID>-<状态路径摘要>/` 创建0700目录和0600的 `.access-token`。此目录默认不在 `/kaggle/working` 或声音Dataset中，重启应用可复用，同一Kaggle会话销毁后需要新口令。`QTTS_AUTH_DIR`可覆盖位置，但不要指向Notebook公开输出目录或声音库。

启动日志仅给出文件路径。在**私人且不分享的Notebook**内读取后粘贴到网页“访问口令→解锁”。不要把口令放进URL、工作台代码文件、聊天或公开Notebook输出；查看后清除可能含口令的Notebook输出。浏览器刷新后需重新解锁，锁定会停止播放/录音并清空私密视图。

本地CLI工具自动从环境变量或相同私有目录读取访问口令。可用以下方式在可信Notebook中取得变量（示例本身不打印凭据）：

```python
import os, sys
from pathlib import Path
sys.path.insert(0, "/kaggle/working/qtts/py")
from access_control import auth_directory, load_access_token
state = Path(os.environ.get("QTTS_STATE", "/kaggle/working/qtts/state"))
private_token = load_access_token(auth_directory(state))
# 仅在私人环境查看并复制该变量，用后清除输出；不要公开保存。
```

Bearer必须经可信HTTPS代理传输。直连网关的HTTP仅用于可信本机探针；不要在公网明文HTTP中传口令。TLS不由本应用自动签发。

## 5. 实际验证结果

| 检查 | 结果 | 日志 |
|---|---|---|
| Python全套 | **41/41通过**，含访问控制、上传/线程预算、首轮可靠性与打包验证 | `docs/validation/step2/python.txt` |
| Go全套 | **24个顶层测试**，含表驱动场景，`-race -count=3`通过 | `docs/validation/step2/go-race3.txt` |
| 完整浏览器 | **51/51通过**＝原工作台40＋QTTS9＋两版实际启动包复制2 | `docs/validation/step2/browser-all.txt` |
| QTTS专项重复3遍 | **27/27通过** | `docs/validation/step2/qtts-repeat3.txt` |
| 认证网关＋双Mock worker | **3轮通过**：匿名401、正确口令、有序帧、文字完整、两worker参与、中断恢复、模拟零欠载 | `docs/validation/step2/mock-pipeline.txt` |
| 工作台HTTP/API/存储 | **30/30通过**，测试只用临时工作区 | `docs/validation/step2/workbench-api.txt` |
| 语法/编译/重打包/原始与step1不可变性 | 通过 | `docs/validation/step2/syntax.txt`、Python日志 |

测试中修正了两个夹具问题：对隐藏实验室输入框操作前需要切换标签页；全局模拟Thread.start会误伤TestClient自身线程，因此改为只注入业务准入失败。没有通过放宽生产安全检查掩盖失败。

浏览器API和Web Audio是明确的Mock，不代表真实听感。网关HTTP/SSE和取消链路由实际Go/Python服务模拟验证；soundfile使用真实小WAV验证正常/超长路径。当前没有ffmpeg，相关CLI参数及输出超长契约用模拟验证，不能声称真实ffmpeg兼容测试完成。Rust未重新编译。

## 6. 可复现命令

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r kaggle/requirements-test.txt
npm ci
python3 kaggle/repack.py --check
.venv/bin/python -m unittest discover -s kaggle/tests -v
(cd kaggle/source/go/gateway && ../../../../.venv/bin/go test -race -count=3 -v ./...)
.venv/bin/python kaggle/tests/mock_pipeline.py
npm run check
npm test
npm run test:e2e
npm run test:e2e -- tests/browser/qtts.spec.js --repeat-each=3
```

安全仅解包：

```bash
QTTS_UNPACK_ONLY=1 QTTS_ROOT=/tmp/qtts-step2-inspect python3 kaggle/kaggle-fixed-step2.py
```

这不会读Secrets、安装依赖或启动模型。完整运行会安装GPU依赖并可能打开公网隧道；尚未在本环境执行该安装流程。`QTTS_TUNNEL=none`可禁用隧道。

## 7. 不应扩大解释的边界与下一步

- 仍是单用户共享口令，不是多租户账号/RBAC/MFA体系；口令持有者可以删除声音库和使用配置的DeepSeek额度。没有登录会话撤销中心、逐IP/连接级防护或持久安全审计。
- `/tmp`口令文件的0600不能隔离同UID恶意程序、浏览器扩展或管理员；严禁分享/导出凭据。修改服务端口令后需重启网关，既有在途作业不会自动全球撤销。
- 应用层限额不是OS/cgroup配额，空闲磁盘预检不能阻止其他进程填盘。原生解码器没有进程沙箱，ffmpeg真实路径待验；依赖与模型revision锁定仍待完成。
- HTTP取消不等于Python线程/CUDA一定立即停止；本阶段保证昂贵线程名额不提前释放。worker内部队列、重载/删除竞态、supervisor持续故障、长时间运行需后续专项。
- 真正模型训练仍未实现；没有双rank/梯度同步/训练检查点证据。现有ICL参考缓存与校准仍不称为训练。
- 无真实双T4、Qwen权重、Whisper、ECAPA、DeepSeek或麦克风验收。首声<3秒、RTF≤0.5、99.5%相似度均未获得实测通过证据。
- 下一步先完成GPU依赖/第三方流式后端兼容探针与清晰失败报告，再推进两主视图和真实录音波形；真正训练作为独立作业实施并验证，保留现有已测推理/工作台逻辑。

三轮各100项仍是审查清单，不是300项已完成；本阶段只能勾选有对应证据的访问控制条目。历史3个专业问题及每题50条建议保留，不为凑数改动正常代码。

---

## 内嵌备忘录：KAGGLE_STEP3_PLAN.md

# 第三阶段计划：兼容探针与真实采集波形

日期：2026-10-21。保留原始、step1、step2，另存step3。

1. 探针默认只检查安装元数据与工具，不安装、不下载、不加载模型。显式运行时检查放在有超时的隔离子进程：Torch/CUDA设备、原生精度支持、流式后端公开接口签名；不把接口存在等同于推理、训练或性能达标。
2. 启动器安装依赖后、下载模型前运行运行时探针，失败保存结构化报告并停止后续步骤。网关只提供受认证的只读报告，不开放远程执行探针接口。
3. 从真实getUserMedia流创建AnalyserNode，绘制实测时域波形、RMS/峰值；麦克风不接扬声器。MediaRecorder分块采集，选择浏览器支持的容器格式。
4. 录音权限等待、停止、锁定、初始化失败、设备断开、字节/数量/时间预算和迟到回调必须释放流、节点、计时器与音频上下文；禁止过期录音加入新会话。
5. 提供本地录音片段列表及移除操作，不自动上传。保持已验证的认证、语音播放、文件上传、工作台原文复制和历史包不变。
6. 验证分层：CPU探针契约与失败注入；Go报告路由认证/容量；Chromium合成MediaStream的真实Analyser/MediaRecorder及取消测试。浏览器合成信号不称作物理麦克风验收，元数据探针不称作模型可用证据。

本阶段不宣称真正双卡训练、两个主视图改造、真实Qwen/DeepSeek或首声/RTF/音色验收完成。完整依赖锁定与真实GPU实验仍是后续门禁。

---

## 内嵌备忘录：KAGGLE_STEP3_AUDIT.md

> 冻结历史阶段证据；当前源码/重打包入口为step10，见KAGGLE_STEP10_AUDIT.md。下列原统计只描述当时交付，训练输入准备与训练执行不得混同。

# 第三阶段审查：兼容探针与实测采集波形

日期：2026-10-21。范围是设备/接口前置检查与浏览器录音生命周期，**不是完整双T4训练系统验收**。

## 1. 交付与基线

- 新启动包：`kaggle/kaggle-fixed-step3.py`；新清单：`kaggle/source_manifest_step3.json`，30项资产。`python3 kaggle/repack.py --check`只检查step3，不覆盖历史包。
- 原始127241字节，SHA256 `26c31621d6265bc25370bc284f2afdcf52f5edaf97e64056c2d8d5eda4a6c461`。
- step1冻结SHA256 `02e9bb45a14f1e168badc8f897cead0ddd7e70c884d7fd26382c9a5b49778007`。
- step2冻结SHA256 `a628d1bf3f320a330d9206b5f1864e4b38a04f0bc04b26028af2e94368f111d0`，包装测试分别校验历史包。
- 保留单用户Bearer认证、内存凭据、资源预算、音频播放/打断、档案上传与工作台原文复制。三标签页暂不改造为两主视图，参考准备/缓存不改称训练。

## 2. 本阶段实现与检查证据

| 项 | 具体实现/修复 | 源码与验证 |
|---|---|---|
| 1 | 元数据检查不导入模型，显式运行时检查才导入Torch/流式后端；两者均不下载或加载权重 | `tools/backend_probe.py`；`test_probe.py`静态禁导入与禁止模型加载的假后端契约 |
| 2 | 检查GPU数量、计算能力、总显存与请求dtype；T4上的BF16、未经允许的FP32会阻断 | CPU假设备契约；没有真实T4通过证据。总显存不是可用显存 |
| 3 | 检查worker实际调用的三个API；按Python签名绑定位置/关键字/新增必需参数 | AST测试逐一对比worker的实际关键字；`**kwargs`只代表调用形状可接受，明确转发语义未验证 |
| 4 | 子进程120秒预算、超时杀进程组、丢弃第三方导入stdout/stderr；错误消息脱敏 | 超时/无报告/导入异常注入；只保留结构化报告，不收集无界依赖日志 |
| 5 | 启动前静态初检先保存报告，无GPU也保留失败依据；依赖安装后、模型下载前运行运行时探针 | `py/bootstrap.py`；无GPU/单GPU拒绝及顺序测试；探针失败不开始下载 |
| 6 | 原依赖检测的导入子进程也加入60秒与进程组清理，移除抢在正式探针前抛错的重复导入 | `test_reliability.py`超时与DEVNULL契约，避免正式探针尚未运行就无限等待 |
| 7 | 报告0600临时文件原子替换；只读接口最多读取256KiB，缺失返回not_run，损坏/过大返回通用错误 | `go/gateway/preflight_test.go`含未认证401、非GET405、正常/缺失/损坏/null/过大等场景 |
| 8 | `/api/preflight`沿用Bearer；网页不能远程执行探针；新增`recorder.js`显式静态白名单 | Go路由与静态文件测试；浏览器仅GET读取 |
| 9 | 报告读取异常单独显示，不中断原健康/指标监控 | Chromium报告503与原监控请求回归 |
| 10 | getUserMedia→AnalyserNode读取真实时域样本，计算RMS dBFS/峰值并绘制；不连扬声器 | `web/recorder.js`；原生Chromium振荡器流与静音流测试，无随机信号UI |
| 11 | 原生MediaRecorder协商WebM/Opus、Ogg/Opus、MP4，250ms分块；文件后缀跟随实际MIME | Chromium实际编码并检查WebM EBML头和非空文件；不是伪造Blob内容 |
| 12 | session/epoch隔离迟到权限和录音事件；取消后的迟到流仍必须停止 | 原测试曾暴露“已清理标志跳过迟到流停止”的风险，已把停止track放在幂等清理之前；原生流测试覆盖 |
| 13 | 不堆叠未决权限请求；权限拒绝时仍可选文件 | Chromium权限拒绝、等待中再次取消/开始、锁定后迟到流测试 |
| 14 | 停止/锁定/设备结束/页面离开关闭track、节点、上下文和计时；页面离开同时锁定、清空私有状态 | 原生上下文closed及track ended断言；设备结束由软件事件注入，不冒充拔插硬件 |
| 15 | 若stop事件2秒未返回，丢弃片段并清理，不无限保持stopping | 对原生MediaRecorder的stop回调做故障注入，验证超时路径 |
| 16 | 本地单段20MiB、合计63MiB、合计16文件、2048块、约239秒；<1.5秒/空片段不保存 | 原生录音＋缩小预算注入，分别覆盖字节/时长/分块/文件数，未把超限数据截断成成功片段 |
| 17 | 本地列表可移除；只有明确创建档案才上传；上传失败保留录音，成功只移除已提交文件 | `web/app.js`与原生录音503回归；过期档案轮询不能写回新会话 |
| 18 | 交付完整Python启动源码而非网页HTML，复制结果逐字节相等且保留step2 | `tests/browser/studio.spec.js`第三阶段完整源码剪贴板测试；工作台正常编辑/保存/冲突/预览继续回归 |

## 3. 运行方式

只检查环境，不安装或下载：

```bash
python3 kaggle/source/tools/backend_probe.py
python3 kaggle/source/tools/backend_probe.py --runtime --expected-gpus 2 --dtype fp16 --timeout 120 --output /tmp/qtts-probe.json
```

退出0只表示`surface_preflight_passed`；阻断或仅静态检查退出2。默认检查不会返回“模型已就绪”。报告中`model_loaded`、`inference_verified`、`training_verified`、`performance_verified`恒为false。沙箱实际运行运行时探针得到blocked、退出2：Torch/流式后端未安装，ffmpeg缺失。日志在`docs/validation/step3/runtime-probe*`，没有用Mock替代为通过。

安全仅解包（不运行安装器）：

```bash
QTTS_UNPACK_ONLY=1 QTTS_ROOT=/tmp/qtts-step3-inspect python3 kaggle/kaggle-fixed-step3.py
```

真实完整启动应在Kaggle双T4环境，配置Internet与私有`QTTS_ACCESS_TOKEN` Secret，再运行step3包；安装、依赖供应链与模型下载仍需真实环境审查，**此处没有执行完整安装流程**。`QTTS_TUNNEL=none`禁用自动隧道。生成口令仍默认保存在/tmp私有目录，不进入声音库导出，详见第二阶段安全报告。

浏览器通过可信HTTPS代理访问，解锁后在声音实验室点击录音。曲线为实测输入，不是质量评分；dBFS不是校准声压级。没有物理麦克风或权限被拒绝时仍可上传已有文件。浏览器压缩音频容器需要服务端解码器支持，无ffmpeg时优先上传WAV。片段移除只删除浏览器待提交引用，不会删除已上传声音库。

## 4. 验证日志

实际执行结果均通过：

| 验证层 | 本次结果 | 日志（docs/validation/step3/） |
|---|---|---|
| Python | 56项×3轮=168次 | python-round1/2/3.txt |
| Go竞态 | 26顶层＋16子测试，race重复3遍 | go-race3.txt |
| 完整Chromium | 66项×3轮=198次，包含23项QTTS和43项工作台测试；耗时约6分钟 | browser-repeat3.txt |
| Node工作台API | 30/30 | workbench-api.txt |
| 真实Go＋双CPU Mock | 3/3，文本完整、有序帧、两worker、取消后恢复、模拟水位 | mock-pipeline.txt |
| 实际CPU环境运行时探针 | **blocked，退出2，未加载权重**（环境缺依赖，不是模型通过） | runtime-probe.json / runtime-probe-output.txt |
| 语法/确定性包/原始与历史包 | 通过；仅解包逐字节校验包含于Python测试 | syntax.txt / Python日志 |

最终step3为171251字节、30资产，SHA256 `4b69f9adec43487c731c53e7ae65f91534626e71660f1b50b109bfe0c8cb973b`。工作台复制测试核对整个启动包，不是抽样片段。

复现：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r kaggle/requirements-test.txt
npm ci
.venv/bin/python kaggle/repack.py --check
.venv/bin/python -m unittest discover -s kaggle/tests -v
(cd kaggle/source/go/gateway && ../../../../.venv/bin/go test -race -count=3 -v ./...)
.venv/bin/python kaggle/tests/mock_pipeline.py
npm run check
npm test
npm run test:e2e -- --repeat-each=3
```

Python测试使用CPU依赖，不是GPU生产锁定文件。FastAPI测试有httpx弃用警告，故障注入会打印预期错误堆栈；这些不等于测试失败。浏览器测试使用临时工作区，与正式workspace隔离。

## 5. 不能扩大解释的边界与下一步

1. **真实GPU、Qwen/流式后端、CUDA Graph/SDPA与空闲显存尚未验收。** 方法存在或`**kwargs`可绑定不能保证内部实现兼容，也没有依赖/模型revision锁定结论。
2. 没有物理麦克风、手机/浏览器矩阵、压缩音频经真实ffmpeg解码的端到端测试。原生Chromium的软件输入测试不是上述验收。静音/RMS/削波提示不保证录音质量。
3. 后台页面计时可能被节流，239秒是本地停止预算，不是容器实际时长的权威值。服务端240秒/文件、900秒总时长和64MiB整请求预算仍独立复核；超限失败会保留本地录音。
4. 63MiB客户端预算只约束片段/已选文件字节，不是浏览器总体内存上限；编码器、File/Blob与UI仍占内存。应用限额不等于OS配额、原生解码沙箱或多租户隔离。
5. 原生权限窗口不能被应用撤回，取消后必须等返回再停止迟到流；不会将迟到数据加进已锁定/新会话。
6. **真正world_size=2训练、两个主视图、真实DeepSeek长流/声音质量/首声<3秒/RTF≤0.5/99.5%相似度仍未完成或未验证。** 不把录音、参考缓存、Mock、探针或测试数量当作训练成功。
7. 下一步先在目标硬件执行可复现最小模型推理与容器解码，再实施两主视图及独立双卡训练作业；训练必须核对双rank、样本覆盖、梯度同步、显存和检查点重载。

300项清单只勾选有对应证据的具体项。三次全量自动化模拟不等于三次真实GPU端到端验收；历史三个问题及各50条建议继续保留。

---

## 内嵌备忘录：KAGGLE_STEP4_PLAN.md

# 第四阶段计划：两主视图与视口内操作

日期：2026-10-21。先计划再实施；独立step4，不覆盖原始、step1、step2、step3。

## 范围与取舍

真实双T4/模型/DeepSeek通路在本沙箱不可用，不能制造最小推理或训练通过证据。推进可独立实施的两主视图界面：录制参考语音、语音对话。监控保留为辅助诊断对话框，不再作为第三个主要视图。保留所有已有档案、候选、校准、参考文本、导出、播放和打断功能；不添加假训练按钮。

## 实施顺序

1. 以step3包与全部ID/事件为基线，冻结历史哈希；另存step4包/清单。
2. 两个具备可访问名称/选中状态的主要导航，采用原生按钮。切换隐藏面板使用hidden语义；键盘导航不落入隐藏内容。
3. 主要录音/上传/创建与文字/声音选择/开始/停止操作保留在视口内，长文本、片段、档案、可选项有独立滚动或折叠区域。桌面双栏，手机紧凑分区；不以全页裁切掩盖不可访问控件。
4. 登录/解锁区解锁后折叠为状态条，随时可锁定；凭据仍在内存，锁定恢复表单并清私有数据。公开说明保留；高级诊断放原生dialog，有关闭按钮、Escape和焦点恢复，锁定强制关闭。
5. 切换主视图时停止正在请求/采集的麦克风（保存已停止的本地片段，不丢弃有效录音）；语音播放在切到录音页前停止，避免回声/隐形操作。不能把会话切换当作训练。
6. 保持监测/网关检查/分段/耗时/最近运行/所有档案操作可访问，诊断关闭时不轮询，打开时不重叠轮询。旧会话或关闭对话框后的迟到结果不能恢复私有UI。
7. 验证1440×900、1024×768、768×1024、390×844、375×667及短屏布局；主要操作无页面滚动，过小高度/200%缩放可退化为可滚动布局而不是丢失内容。验证长输出/大量档案/长文件名、键盘焦点、Escape、锁定和已有原生录音/播放回归。
8. CPU/Python、Go race、Node API、Chromium三轮回归与包的仅解包/复制校验，日志另存docs/validation/step4/；完成后更新清单/完整交接提示词及工作台，不提前勾选。

## 验收边界

视口测试仅证明列出的Chromium尺寸与布局行为，不代表所有手机/浏览器/虚拟键盘/屏幕阅读器验收。浏览器音频输入仍为原生软件流，非物理麦克风。真实GPU、world_size=2训练、模型/依赖锁定、DeepSeek长流、首声<3秒、RTF≤0.5及99.5%相似度继续单独列为未完成/未验收。

实施补充：短屏阈值最终为≤640 CSS px；手机新增常驻“选项”入口。测试注入仓库现有本地Noto字体，不打包外链字体；实际OS缩放/虚拟键盘仍待硬件验收。

---

## 内嵌备忘录：KAGGLE_STEP4_AUDIT.md

> 冻结历史阶段证据；当前源码/重打包入口为step10，见KAGGLE_STEP10_AUDIT.md。下列原统计只描述当时交付，训练输入准备与训练执行不得混同。

# 第四阶段审查：两主视图与视口布局

日期：2026-10-21。只验收本阶段界面/生命周期与CPU协议，不验收真实模型或训练。

## 交付

- `kaggle/kaggle-fixed-step4.py`：175985字节，30资产；SHA256 `069421e5f0d4112148211e1289f91ec7a1b184105e5431fde0c3d72e8c744e27`；清单`source_manifest_step4.json`。
- 原始、step1/2/3包均冻结，Python测试分别核对哈希；step3仍为`4b69f9adec43487c731c53e7ae65f91534626e71660f1b50b109bfe0c8cb973b`。repack.py现在只生成step4。
- 计划先保存`docs/KAGGLE_STEP4_PLAN.md`再实施；目标设备门禁另存`docs/KAGGLE_TARGET_ACCEPTANCE.md`，待执行项不伪填为通过。

## 具体实现与证据

| 项 | 改动/保留 | 证据 |
|---|---|---|
| 1 | 主导航只有“录制参考语音”“语音对话”，选中状态aria-pressed，隐藏面板不接受焦点 | `web/index.html`、`app.js:j`；Chromium主导航/方向键/Home/End/隐藏输入测试 |
| 2 | 监测改为原生dialog辅助窗口，保留系统、兼容探针、最近运行、分段、耗时、同源网关 | 旧DOM ID与脚本顺序逐一校验，未删除旧功能；不是第三主视图 |
| 3 | 关闭/Escape/焦点恢复、模态内锁定、清空私有数据后回到登录输入 | 模态与认证回归；锁定强制关闭，未把关闭窗口当作删除档案 |
| 4 | 解锁后访问表单收起为状态条，锁定按钮常驻；凭据仍只在内存 | 现有认证/URL/存储/迟到响应回归继续执行 |
| 5 | 桌面双栏，手机分区；主要操作固定，配置/回答/档案/片段内部滚动 | 1440×900、1024×768、768×1024、390×844、375×667，检查控件完整边界、祖先裁切、中心命中及页面不溢出 |
| 6 | 初查发现中心命中仍可能漏掉控件下缘裁切，已收紧断言并调整375px布局 | 修复文件选择/模式选择部分裁切；声音库滚动区>40px，未用overflow隐藏无法到达的按钮冒充通过 |
| 7 | 高度≤640 CSS px退化为可滚动页面，避免短屏/等效缩放丢失操作 | 375×480测试；不宣称实际OS缩放/手机虚拟键盘通过 |
| 8 | “选项”明确入口始终可见，参考文本与校准设置可折叠、键盘可达 | 375×667显式按钮、summary焦点、Tab到转写、关闭后文件选择恢复 |
| 9 | 切换到采集页停止语音播放/未决初始化；切到对话或打开诊断停止采集 | 原生MediaStream停止/上下文closed、有效WebM片段保留；取消后的迟到权限继续安全释放 |
| 10 | 诊断只打开时顺序轮询，关闭中止，代际隔离迟到结果 | 6秒慢响应无重叠、同一任务关闭/重开、过期报告、关闭后10秒无轮询；使用虚拟时钟故障注入 |
| 11 | 长回答和40个长名称档案不撑开页面，内部滚动仍保留主操作 | 375×667压力场景；原文本保存/候选/启用/校准仍能发出相应请求（HTTP夹具，不是GPU校准） |
| 12 | 自定义名称为空或>64 Unicode字符时不上传，不默填my-voice；失败保留文件 | 空名/超长/自命名503回归；动态参考文本、片段移除补充可访问名称 |
| 13 | 速度倍率不再误标为标准RTF；缺失统计显示未测/未设置 | `app.js:W/et`；不把没有测量的数据补成模型成功 |
| 14 | 中文截图使用仓库现有本地测试字体，确认字形可读后再验布局 | `tests/browser/qtts.spec.js`字体等待；生产包不新增外链字体，依赖浏览器设备的系统中文字体 |
| 15 | 独立step4完整Python源码复制，保留历史包与工作台编辑/保存/冲突/预览 | `studio.spec.js`全包逐字节剪贴板与既有工作台回归；未执行安装器 |
| 16 | 原生录音器已inactive时不重复stop丢弃数据，自动stop也计算采集墙钟时长 | 原生MediaRecorder两种事件顺序、有效片段保留；最低时长用100ms时钟注入独立验证，非物理时间测量 |

## 验证结果

最终全量浏览器87项×3轮=261次通过（QTTS43项＋工作台44项，约7.3分钟），日志browser-repeat3.txt。首次全量为251通过/1失败：设备结束测试错误地假定UI步骤必然少于1.5秒，实际有效片段按设计被保留。已改为明确录制有效片段；静音测试也不再依赖操作必须很快，最低时长另用可复现的100ms时钟注入验证。检查中另补了原生自动stop竞态修复及测试；相关五项×3=15次专项通过。首次日志保留browser-first-attempt.txt，中止调整测试的第二次日志保留browser-interrupted-attempt.txt，不计为通过。最终Python59项×3轮=177次、Go26顶层/16子测试race×3、Node API30项、真实Go＋双CPU Mock管线3轮，均通过。实际CPU运行时探针仍blocked/退出2，没有加载权重；见runtime-probe.json。最终结果与日志在`docs/validation/step4/`。

- `python-round1/2/3.txt`：可靠性/认证/探针/包装/历史哈希/DOM保留。
- `go-race3.txt`、`mock-pipeline.txt`：保持访问控制、有序PCM、两worker、取消恢复与模拟播放器水位。
- `browser-repeat3.txt`：最终完整工作台与QTTS；`recording-races-repeat3.txt`为15次录音专项。不以截图或失败尝试代替通过记录。
- `syntax.txt`、`workbench-api.txt`：语法/确定性包/Node API。
- `chat-1440x900.png`、`reference-1440x900.png`、`chat-375x667.png`、`reference-375x667.png`：已解锁界面的HTTP夹具截图，无真实凭据/模型输出，不是生产或GPU实验。

## 使用与复现

```bash
python3 kaggle/repack.py --check
.venv/bin/python -m unittest discover -s kaggle/tests -v
(cd kaggle/source/go/gateway && ../../../../.venv/bin/go test -race -count=3 -v ./...)
.venv/bin/python kaggle/tests/mock_pipeline.py
npm run check
npm test
npm run test:e2e -- --repeat-each=3
```

测试环境初始化见requirements-test.txt与npm ci；不是GPU生产依赖锁定。安全仅解包：

```bash
QTTS_UNPACK_ONLY=1 QTTS_ROOT=/tmp/qtts-step4-inspect python3 kaggle/kaggle-fixed-step4.py
```

完整运行会安装依赖/下载模型/可能打开隧道，当前沙箱没有执行。真实Kaggle启动、非Mock核对、最小推理、容器/DeepSeek/训练等门禁见`KAGGLE_TARGET_ACCEPTANCE.md`。不把仅解包退出0或探针表面通过当作模型就绪。

## 限制与下一步

- 本次仅测试列出的Chromium CSS视口。中文字体由浏览器设备提供；测试注入的本地Noto字体没有塞入Kaggle包。未做全浏览器、物理麦克风、触屏、屏幕阅读器、真实虚拟键盘/OS缩放验收；高度≤640允许页面滚动，主要操作不滚动不是全尺寸保证。
- 手机语言/Key等次要配置、详细转写、长列表需内部滚动或“选项”；声音库没有分页，不能因此勾选清单的分页项。没有新增先持久化空语音库的独立流程或训练任务UI；对话页仍以文字提问，没有新增语音提问转写。
- 参考创建/校准仍不是训练；没有双rank、梯度、样本覆盖或检查点证据。真正world_size=2训练、真实Qwen/双T4/DeepSeek/ffmpeg容器全链路、首声<3秒、RTF≤0.5、99.5%相似度仍未完成/未验收。
- 下一步应在目标设备按门禁先证明非Mock引擎与每卡真实推理，再适配独立训练作业；不能只包一层accelerate或照搬T4不支持的BF16/标准FA2示例。
- 工作台单项目上限仍为1MiB，不为塞入重复交接文件而提高限制或删除旧文件。完整交接提示词保存在仓库`docs/KAGGLE_HANDOFF_PROMPT.md`；工作台保留历史文件后仅添加能容纳的新源码/简报。

300项清单仍不是已修复300个缺陷，只有具备证据的具体项能勾选；三个历史专业问题及每题50条建议继续保留。

---

## 内嵌备忘录：KAGGLE_STEP5_PLAN.md

# 第五阶段计划：先建库、再管理参考样本

日期2026-10-21；先保存计划再实施。当前真实GPU/模型/DeepSeek/物理麦克风实验条件不具备，不伪造训练或性能通过。

## 范围与取舍

1. 新增与可推理profiles分离的STATE/libraries原始样本库。先用自定义名称创建持久空库，再添加/列出/选择/删除样本，再明确执行“处理所选参考”。空库/原始样本绝不进入声音档案下拉框或被worker当成模型。
2. 原有一步创建声音档案、两主视图、诊断、原生录音/播放/打断全部保留。新流程放独立辅助原生dialog；不是第三主视图。用户可先建库，再回主视图录音，随后添加本地片段到库。
3. 原始样本写入不解码/不加载模型，显示“未解码、未训练”。处理仍调用既有build_profile，生成新的可用档案；是参考处理，不是训练。失败保留源样本，不删除此前成功档案。
4. 原始数据只在本地STATE保存，不自动放入Kaggle Dataset导出，防止扩大私密音频分发。会话结束仍会丢失工作目录；不是永久/跨会话存储保证。

## 实施顺序

- 建独立标准库文件存储模块：UUID路径、0600原子清单/数据、0700目录、拒绝symlink/路径穿越，哈希核对、同库去重、事务提交失败回滚、新进程可读。
- 库数128、样本数16/库、20MiB/文件、64MiB/库、512MiB全局原始字节；沿用整请求64MiB、空闲磁盘256MiB、后台构建单并发与有界记录。库字节预算不是OS总体配额；解码时长仍由原处理器复核。
- fcntl非阻塞库租约跨线程/进程阻止构建期间改样本/删库；操作锁期间快速返回409而不排等待线程。构建失败/线程启动失败/取消/进程退出必须释放或由OS回收租约，遗留processing不得冒充成功。
- 通过已认证/api/prep/libraries反向代理提供仅必要GET/POST/DELETE接口，扩展上传预算只匹配正确samples上传路径；JSON严格字段/类型/容量，错误不暴露私密路径或原始样本。
- 浏览器库管理dialog：命名建库、选择库、文件/本地片段入库、样本勾选/移除、处理所选、明确状态。锁定清空全部私有库视图/选择/文件并关闭；迟到回调不能写回。模态焦点/关闭/Escape保持一致，不让麦克风在覆盖窗口后暗中采集。
- Python文件/事务/并发/故障注入与真实FastAPI上传、Go认证/预算/代理、Chromium流程/隐私/原生录音回归及新包逐字节复制。保存三轮分层日志，不以模拟代替GPU。
- 独立step5包与清单，冻结step1/2/3/4。正式工作台已15文件/1043155字节，剩余不足新包：不提高1MiB、不删/覆盖旧文件。本阶段优先独立文件交付，复制测试在隔离临时工作区验证，不暗改正式HEAD。

## 明确未完成

真正world_size=2训练、训练任务UI/检查点、真实模型/后端/双T4/ffmpeg/DeepSeek/物理录音/质量/首声/RTF验收仍未实现或未验证。三轮各100项只勾有证据的项，原150条专业建议保留。

---

## 内嵌备忘录：KAGGLE_STEP5_AUDIT.md

> 冻结历史阶段证据；当前源码/重打包入口为step10，见KAGGLE_STEP10_AUDIT.md。下列原统计只描述当时交付，训练输入准备与训练执行不得混同。

# 第五阶段：命名空库与参考样本证据

日期2026-10-21。计划先保存于KAGGLE_STEP5_PLAN.md，再增量实施。此文是阶段报告，**不是完整模型/训练产品验收**。最终浏览器全量与最终包复制专项已完成，结果如下。

## 交付与使用

独立启动包：`kaggle/kaggle-fixed-step5.py`；32项内嵌资产。最终196140字节，SHA256 `acfa5639324e16aa7dcfe314caef09bee8eb277d59bdd71a5f1f4cffa0a7aaf1`，见source_manifest_step5.json。原始/step1/2/3/4均冻结不覆盖。

1. 进入“录制参考语音”，点“声音库与样本”。
2. 自行命名，点“仅创建命名空库”；不要求先上传音频，也不生成可用声音档案。
3. 向选定库添加文件，或先关闭窗口在采集页录音，再回库添加本地录音。保存失败保留本地片段/所选文件供核对重试；同库同内容SHA256去重。
4. 手动勾选已保存样本，可填写参考文本并选校准，然后点“处理勾选参考（不是训练）”。原有快速创建声音档案入口与文本/候选/启用/校准操作保留。
5. 处理成功只表示既有参考准备任务完成；不会把空库或未解码样本放进可用声音档案。`training_verified/inference_verified/decoded_duration_verified`在原始库对象中不冒充通过。

## 三轮审查：本阶段具体落实

| 层次 | 落实 | 证据或边界 |
|---|---|---|
| 存储 | STATE/libraries与profiles分离；UUID路径、NFC/大小写折叠库名、0700/0600、新进程可读 | 真实临时文件系统/子进程测试 |
| 限额 | 默认128库、16样本/库、20MiB/文件、64MiB/库、512MiB总原始音频、256MiB磁盘余量 | 注入小预算测试；不是OS配额 |
| 事务 | 内容SHA256/去重、修订CAS、原子清单；上传/清单失败回滚新文件；下一次修改清理未引用音频/临时文件 | 写入/清单失败注入、并发同修订竞争 |
| 安全 | 拒绝UUID穿越/目录和清单链接/样本软硬链接；JSON拒绝重复键/NaN/未知字段 | FastAPI实上传与文件系统测试 |
| 代理 | 库路由继续认证；仅精确POST libraries/{32位hex}/samples扩大上传预算；移除上游私密凭据 | Go真实反向代理/已知长度及chunked预算 |
| 作业 | 新旧流程共享ADMISSION与BUILD_LOCK；Linux flock跨进程同库租约；固定勾选字节快照 | 忙碌409/429、SIGKILL、哈希不符、外来样本ID |
| 终态 | 元数据提交后才发布done；提交失败不宣称成功；失败保留原件及此前独立档案 | 提交屏障与故障注入测试 |
| 取消 | 库租约预约和线程接管在一次准入函数中，HTTP取消不会在两步之间遗留未接管租约 | ASGI取消测试；已提交操作可能继续 |
| 线程池 | 提交可能排队后启动失败；门闩拒绝迟到排队任务执行/二次释放 | 真实ThreadPoolExecutor故障复现及回归 |
| 浏览器 | 库管理是辅助dialog，仍仅两主视图；关闭/Escape/焦点、锁定清私有内容；迟到建库/移除响应隔离 | Chromium夹具；不是真实GPU界面 |
| 录音 | 打开库停止实际MediaRecorder采集并保留有效片段；建库后可添加本地录音 | 软件MediaStream，非物理麦克风 |
| 隐私 | 原始库不自动加入Dataset；删除库不删除生成档案 | 实际_pack的边界测试 |

## 验证日志（docs/validation/step5/）

- Python：`python-round1/2/3.txt`，**92×3=276项通过**。包括原59项、step4冻结检查及32项新库/线程池测试。
- Go：`go-race3.txt`，28顶层＋16子测试，race三轮通过。
- 真实HTTP：`library-http3-final.txt`，Go→真实analyst→磁盘三轮通过。每轮上传1049088字节文件（超过1MiB JSON预算），重启analyst验证恢复，再提交损坏音频，确认**正确报错**且原始SHA256不变；不把这一负向用例当作解码成功。
- 两CPU Mock worker：`mock-pipeline.txt`，三轮有序分段、两worker分配、中断后恢复与模拟无欠载通过；不是T4证据。
- 浏览器新流程初检：`browser-libraries-initial.txt`，12通过；全量100唯一用例×3＝300次通过（55 QTTS＋45工作台），11.2分钟，见`browser-repeat3.txt`。最终196140字节包另作逐字节剪贴板三次核对，`final-copy-repeat3.txt`3通过/11.5秒；全量启动后收尾的后端Unicode与嵌入备忘录也已由最终Python三轮和复制专项覆盖。
- 工作台API：`workbench-api-round1/2/3.txt`，30×3=90通过。新包逐字节真实剪贴板回归在隔离临时工作区，不会改正式HEAD。
- 语法、compileall、重打包：`syntax.txt`通过。运行时探针`runtime-probe.json`仍blocked/退出2，缺Torch/流式后端/ffmpeg，不加载权重。

## 初检失败与修正，不能隐去

1. `python-initial.txt`：91项中2失败。GET只有DELETE的样本资源应为405，不是404；无音频下载能力不变。线程启动故障注入原先命中测试框架/线程池，不是目标build线程。改为按build-线程名精确注入。
2. `python-second.txt`当次91通过，但后续并发负载下`python-failed-executor-submit.txt`重现线程池提交异常留下排队任务，随后线程可能执行该请求。不是简单放宽断言：已修HeavyAdmission提交门闩，新增真实ThreadPoolExecutor回归后全量92连续三轮通过。
3. `python-failed-surrogate-client.txt`：测试客户端默认非ASCII JSON编码先拒绝孤立代理码，尚未到服务器。改用合法ASCII转义JSON传输，服务端明确400；名称/语言/参考文本拒绝无效Unicode，最终92×3重跑通过。
4. Go测试追加最初一次命令工作目录用错，未写入文件；改为仓库根目录执行后通过。没有把该命令失败计作测试通过。
5. 正式API一次只读核对脚本把每个Buffer分块独立转UTF-8，切开中文多字节时误多算21字节；改为Response.json正确解码后15个文件的SHA256逐一与磁盘收据相同、总1043155字节。正式文件从未被该只读检查写入。

## 存储、隐私、部署边界

- 本地磁盘持久化意味着刷新/分析服务重启仍可读，不意味Kaggle会话永久或跨会话恢复。原始库不自动导出；**处理后的档案锚点/转写仍沿用已有Dataset备份设置**，应有参考声音授权。
- 删除不是安全擦除，且不删除独立profiles/既有Dataset备份。语音文件、转写、密钥不进Git。
- 清单提交用文件fsync+replace，不承诺断电原子耐久；中断未引用文件在该库下一次修改回收。损坏清单报错需人工修复，不自动清空“恢复”。元数据量仍受库/样本数限制。
- Linux flock仅保证配合本协议的进程；这不是同UID恶意进程隔离、容器沙箱、多租户账号、硬盘OS配额或多个analyst实例的全局GPU调度方案。
- JOBS仍是有界内存任务表，不是持久审计数据库；库仅保留最近处理状态/来源修订与ID、最近成功档案指针。服务重启释放锁，遗留running显示interrupted，不自动重跑收费/模型任务。
- 原始上传允许未解码数据保存但明确标未验证；真正处理沿用原有容器/时长/总时长检查。没有实际成功处理真实长参考语音、加载Qwen、双T4模型、DeepSeek或训练的实验结果。
- 正式工作台15文件/1043155字节，剩5421字节；本阶段新包不强塞，不提高1MiB、不删历史、不改HEAD。独立文件交付；工作台复制兼容仅在容量充足的隔离工作区验证，不能声称已发布到正式工作台。正式服务已恢复在3000，只读API逐个核对15个SHA256，见formal-api-readonly.json与delivery.json。

## 清单与下一步

仅R1-073（内部ID与显示名称/路径分离）可在本阶段有据增加，清单19/300。R1-074在新库流程满足，但旧快速创建兼容入口仍保留，不以局部结果勾成全局强制；训练数据状态/覆盖/检查点/模型恢复均未验收。专业问题4另存50项建议，前150项保留，共200建议，不等于200项已完成。

下一步仍先按KAGGLE_TARGET_ACCEPTANCE.md做真实非Mock后端/每卡最小推理/容器解码门禁，再适配独立双卡训练作业与资源模式切换；不要只加accelerate launch或训练假按钮。

---

## 内嵌备忘录：KAGGLE_STEP6_PLAN.md

# 第六阶段计划：可校验、不可变的训练输入快照

2026-10-21。先保存计划再编码。接续step5命名库；不是训练执行或双T4验收。

## 核对与选择

训练不能直接复用原始样本的一个公共ref_text：官方固定提交022e286b98fbec7e1e916cb940cdf532cd9f488e的finetuning/README.md要求每行audio/text/ref_audio，建议同一个ref_audio。参考处理/校准不产生optimizer更新，现有supervisor也没有训练/推理互斥资源模式。沙箱无Torch/GPU/模型，不能假装实现并实测双T4训练。

本阶段做独立“训练输入准备”而非训练按钮：用户逐条提供转写、显式选统一参考、声明声音使用授权及单说话人，锁定库修订与所选原始哈希，生成私有本地不可变快照。训练执行、声学码提取和模型检查点仍待下一阶段与真实设备门禁。

## 实施

1. 新STATE/training_data，独立于profiles/libraries。随机UUID/0700目录/0600文件；API只增创建、列举、校验、删除，不提供任意路径或shell命令执行。
2. 训练输入初版严格接受完整24kHz单声道PCM16 RIFF/WAV，结构/帧数/时长/非空/非恒定信号复核；其他格式明确拒绝，不偷偷把浏览器Opus后缀改成WAV，不自动有损转换或截断。既有参考处理保留原解码路径。后续受限解码器另验，不借本阶段冒充ffmpeg通过。
3. 每条转写1–2000码点，累计16000，拒绝空文本/无效Unicode/重复或外来样本；统一参考必须属于勾选集合且≤16秒，训练片段1.5–240秒，累计≤900秒。无自动转写/说话人鉴定/文本匹配验证，用户声明不等于模型验证。
4. 复用Linux同库租约，仅取快照，不改last_build/已生成档案。输出规范WAV（保留全部PCM帧，剥离额外容器元数据）、train_raw.jsonl、manifest.json和rank_plan.json；记录来源库/修订/所选ID/原始和输出哈希/文本哈希/参数/声明。
5. 双rank计划只是可复现数学分配：不drop样本、奇数明确标padding重复；不是已运行rank或梯度同步证据。训练/分词/推理验证标志保持false。
6. 原子目录发布，失败回滚，孤立staging下次操作回收；默认32快照、64MiB/快照、256MiB全部快照、磁盘余量256MiB。与原始库分别限额；只在本地保存，不自动加入Dataset。删除库不删除已生成副本，要明确告知可单独删除。
7. 库管理dialog新增可折叠训练输入区域；逐样本文本、参考选择、两项明确声明；创建/校验/删除结果均真实接口驱动，清楚显示非训练。锁定/关闭清私有转写与输出选择，迟到结果不能恢复。
8. 严格JSON预算与已有HEAVY准入；验完整SHA、JSONL相对路径、逐条文本/引用、rank计划，不信任存在即完整。路径只由服务端UUID生成；同UID恶意进程不是隔离承诺。
9. Python真实WAV/文件/事务/并发/权限/篡改/旧流程回归，Go认证与小JSON预算，新浏览器流程及原有全量三轮，独立step6打包/全包复制；保留step1–5、原工作台15文件和1MiB上限。

## 明确未完成

未进行真实模型/双T4/DeepSeek/物理麦克风/ffmpeg/音质与性能实验；没有训练进程、GPU模式切换、audio_codes、loss/梯度/optimizer/checkpoint。输出state=input_snapshot_ready，绝不叫trained或ready_to_train。三轮300项审查只勾确实有证据的项。

---

## 内嵌备忘录：KAGGLE_STEP6_AUDIT.md

# 第六阶段审查：不可变训练输入，不是训练执行

> 历史第六阶段冻结报告：当前源码入口已推进至step10；最新实现与真实编码阻塞见KAGGLE_STEP10_AUDIT.md，以下统计保留原第六阶段证据。

2026-10-21。先保存KAGGLE_STEP6_PLAN.md与专业问题5的50项行动建议，再实施。这里的“准备完成”仅为训练输入快照；**没有训练器、audio_codes、优化器、GPU模式切换或真正双rank运行**。

## 交付与操作

- 独立`kaggle/kaggle-fixed-step6.py`，210003字节/33资产，SHA256 `781eca6e2e34bdacbe2f5337bd6535512226c2122bbf3876d05634f2fc86d256`。原始与step1–5冻结，清单source_manifest_step6.json。
- “录制参考语音”→“声音库与样本”→先建立并上传到命名库→勾选音频→展开“训练输入快照”。每段单独填对应转写、显式选统一参考，并确认声音使用权/单说话人声明。点“生成训练输入快照（不训练）”。
- 下方可查看所有来源库的输入副本、按固定manifest哈希核对、二步确认删除。没有新增主导航。原始库删除后副本仍在，可继续从这个列表单独删除。
- 首版只接收**完整24kHz单声道PCM16 RIFF/WAV**。参考1.5–16秒、其他片段1.5–240秒、累计≤900秒。WebM/Opus/Ogg/MP4/其他采样率会明确拒绝，不换后缀、不静默转码、不截断；原始库内文件保留。原有参考处理仍走旧解码路径，不因此宣称ffmpeg已通过。
- 转写每条1–2000码点、合计16000；是用户提供的文本，没有ASR匹配/声纹核验。声明是记录用户同意，不是技术证明权利或身份。

## 具体增量与证据

| 项 | 实现 | 证据/限制 |
|---|---|---|
| 来源快照 | LibraryStore.snapshot只读同库租约，固定修订/所选ID/原始字节与SHA256，不修改last_build | 源库修改409、旧档案状态不变、源库删除后副本可验 |
| 格式 | 审查RIFF总长/所有chunk边界，拒绝多fmt/data、错误采样率/声道/位深、短/长/常量信号 | 真实合成PCM16测试；非恒定不等于有效人声 |
| 规范输出 | 每个选中样本保留全部PCM帧，规范WAV剥离额外容器元数据 | 帧数/PCM逐字节相同，原始和规范WAV哈希分别保存 |
| 数据约定 | train_raw.jsonl每行audio/text/ref_audio，统一参考来自选中集合 | 对照Qwen固定提交；没有把一个ref_text复制给全部样本 |
| 可追溯 | manifest记录库/修订/ID、来源名、原始/输出/文本/JSONL/计划哈希、帧数/采样率/峰值/RMS及声明 | 转写只在JSONL，列表/响应不重复返回私人全文 |
| 双rank计划 | 稳定哈希排序与epoch轮换，分两rank、等步数、无drop、奇数显式padding | 只是数学分配；不是DDP/采样器/梯度执行证据 |
| 事务与预算 | 独立UUID暂存→校验→原子目录发布；失败回滚，下次写操作回收孤立staging | 文件/rename故障注入；默认32快照、64MiB/快照、256MiB全局与256MiB磁盘余量 |
| 私密与路径 | 0700/0600、无任意路径/执行接口、软硬链接拒绝、固定哈希核验文件集合/索引/路径/内容 | 同UID恶意进程与断电耐久不是承诺；不是签名系统 |
| 接口 | 已认证/api/prep/training-data创建/列表/verify/DELETE；严格JSON字段/布尔/文本，继续小JSON预算及HEAVY准入 | Go预算/匿名401、FastAPI真实接口及错误脱敏 |
| 界面 | 逐条文本/显式参考/两项声明、结果/校验/单独删除，关闭/锁定清私密与代际隔离 | 浏览器HTTP夹具；不声称对接真实Qwen |
| 声明隔离 | 选中集合、新建/切库、删除库、自动回退源库时，不复用旧声明或转写 | 新增专门浏览器回归；修改后重新确认 |
| 备份边界 | 原始库和训练输入均不自动加入Dataset，既有profiles备份保持 | 真正_pack归档成员测试，独立副本要单独删除 |

## 文件与后续使用约定

数据位于STATE/training_data/{服务端UUID}/：

- audio/{样本UUID}.wav：规范24kHz/单声道/PCM16全部帧。
- train_raw.jsonl：逐条audio/text/ref_audio；路径相对**数据集目录作为工作目录**，不是自动相对JSONL文件。使用上游prepare_data时必须先切到该目录。
- manifest.json：schema1、state=input_snapshot_ready，不是ready_to_train/trained。
- rank_plan.json：kind=assignment_plan_not_execution。真正训练必须由支持等步数/显式padding语义的采样器落实并记录每rank覆盖，不能把这个文件当作实际训练日志。

`audio_format_verified/assignment_plan_verified`只对应格式/数学计划；`transcript_verified/speaker_identity_verified/tokenization_verified/training_verified/two_rank_execution_verified/inference_verified`均false。

列表`integrity_verified_now=false`，表示只读索引未重新验全部文件。明确校验成功才置true；请求携带先前固定manifest SHA256，不把当前任意文件存在当完整。校验失败前清除旧成功展示，失败不删除原件或旧独立副本。

## 分层验证（docs/validation/step6/）

- Python初检111通过；补充真实Dataset备份边界后为112。最终112×3＝336通过，python-round1/2/3.txt。
- Go28顶层/16子测试race三轮通过；工作台Node API30×3通过。
- training-http3-final.txt：真实Go→analyst→文件系统三轮，合成PCM16格式输入/逐条转写/声明拒绝/固定哈希/篡改409/源删除后副本独立/单独删除，且不增加模型JOBS。包含前阶段坏音频正确失败与原始哈希不变的旧链路。
- mock-pipeline.txt：两CPU Mock worker的三轮有序合成/中断恢复；不是真实GPU/人声。
- browser-initial.txt：旧库12＋新输入4＝16通过。training-browser-repeat3.txt：增加声明边界后5×3专项通过。最终全量106唯一用例×3＝318通过（10.6分钟），browser-repeat3.txt；不把中止的旧全量当三轮完成。
- 包原始22哈希＋当前33资产的确定性检查、语法/compileall/diff检查通过。实际runtime-probe.json仍blocked/退出2，缺Torch/流式后端/ffmpeg；没有加载模型。全量内第六阶段完整源码与系统剪贴板逐字节相同三次，且第五阶段包内容保持；均在隔离临时工作区。另跑final-copy-repeat3.txt专项3/3通过。

## 复审发现与中止记录

初版Python/真实HTTP/浏览器初检均通过，但进一步审查发现“新建库/删除库”等程序化切换可能沿用前一组授权勾选。没有放宽断言：新增源库绑定与选择变化失效机制，并覆盖新建/删除/切换/样本集合变化。旧全量已跑105项后中止，保存在browser-interrupted-consent-review.txt，不是全量通过；修正版另跑三轮。

## 仍未完成，不扩大解释

- 仍没有实际Qwen训练器/声学码提取/梯度或optimizer更新/检查点/双rank运行、训练与推理互斥模式。上述输入只是后续训练的可验证前置资产。
- 完整模型/双T4/DeepSeek/物理麦克风/ffmpeg压缩容器/音色/首声<3秒/RTF≤0.5没有验收。不能运行BF16/标准FA2示例或只加accelerate launch就声称T4训练完成。
- 格式首版有意严格；浏览器默认Opus录音通常不能直接生成训练快照，需后续受限解码器与真实容器验收或自行提供合规WAV。既有参考处理功能未移除。
- 准入按原始字节＋128KiB保守预留，可能提前拒绝；不以减少样本/截断音频回避预算。应用限额不是OS配额。损坏清单/未发布staging不假恢复；不是断电耐久或永久会话保证。
- 尚无外部训练进程的数据使用租约；不要在手动上游进程读取时删除副本。后续训练器须绑定固定版本并在运行期间阻止删除，不能从当前文件锁推断此功能已完成。
- 训练副本包含音频/私人转写，不进Git、不自动云导出，删除原始库不等于删除副本或历史Dataset中的既有档案锚点。
- 正式工作台只有5421字节余量，仍不放宽1MiB、不覆盖历史，本阶段独立文件交付。复制回归用隔离临时项目，不能称已发布正式工作台。
- 本阶段只可勾R1-079（记录授权声明）和R2-031（固定训练清单ID/内容哈希），累计21/300。R1-075只有训练输入具备格式/转写，原始库仍未解码；R2-032/采样器/实际rank覆盖等未完成，不勾选。第5题新增50建议，保留共250建议，不等于250项修复。

## 上游核对

https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/README.md

本次通过GitHub API再次读固定提交，核对单说话人audio/text/ref_audio及统一参考建议；没有执行上游训练脚本，也不把它的BF16/FA2示例当作T4可用证明。

---

## 内嵌备忘录：KAGGLE_STEP7_PLAN.md

# 第七阶段计划：有租约、可回滚的离线声学码准备

2026-10-21。本计划在编码前保存。先核对第六阶段冻结包及Qwen固定提交022e286b98fbec7e1e916cb940cdf532cd9f488e的prepare_data.py、tokenizer encode和12Hz配置。

## 推荐方案与真实门禁

不直接从网页启动GPU编码：supervisor尚无训练/推理资源互斥，不能和两个推理worker抢显存。本阶段新增**本机离线CLI、仅CPU、仅本地已物化模型**的真实Qwen tokenizer适配入口；不装依赖、不下载、不执行任意命令、不开放HTTP训练接口、不改变两主视图。CPU路径不是双T4性能方案，而是先验证可追溯编码协议；将来GPU入口必须先实现资源所有权。

当前沙箱无Torch/qwen_tts/本地权重，真实编码预期blocked。测试可注入确定性fixture，但fixture输出必须明确test_only，不能成为真实audio_codes完成证据。不能从编码完成推断训练完成或检查点可用。

## 实施顺序

1. 增TrainingDataStore读取租约：固定manifest哈希、完整核对后持有独立进程锁；编码期间禁止删除该输入，其他数据集操作不持有长时间全局锁；进程退出自动释放。锁文件放输入目录外，不改冻结快照文件集合。
2. 新独立STATE/training_codes，0700/0600、默认32份/64MiB每份/256MiB总量/256MiB剩余，复制完整规范WAV与rank计划，输出train_with_codes.jsonl及manifest，不改变原输入。
3. 对每个样本单条调用真实Qwen3TTSTokenizer.encode(np.ndarray,sr=24000)，不使用上游zip静默忽略缺失结果。要求恰好一个返回、ceil(frames/1920)行、16列、严格整数0..2047；验证完整样本覆盖、原text/ref_audio不变。
4. 全量模型目录内容哈希固定，本地JSON/safetensors、拒绝软硬链接/远程模型ID/pickle/自定义代码；config为12Hz/24kHz/16码本/2048范围，实际加载配置再次核对。固定CPU/FP32/eager/小线程数，不用BF16/FA2/GPU。
5. 原子staging发布、失败/取消清理、下次操作回收进程被杀遗留暂存。源输入删除后已发布码副本独立；副本不自动加入Dataset，单独本机verify/list/delete。
6. CLI父进程施加总超时，SIGINT/SIGTERM终止子进程组并必要时kill；Linux PDEATHSIG/ppid握手覆盖控制器被强杀；不把取消标记为完成。模型日志丢弃，公开输出仅简要状态，不包含私人转写/路径/底层异常。缺依赖/模型/哈希不符明确非零退出。
7. 编码并非训练：没有token级文本tokenizer、optimizer、loss、检查点或实际两rank；真实模型成功执行也只标记tokenization_executed，语义/解码/训练验证仍false。测试fixture另用test_only状态。
8. 新存储/租约/模型清单/返回形状/故障/超时/取消/备份排除/CLI拒绝测试；全部旧测试三轮与完整浏览器三轮，新增step7全源码剪贴板测试，保留原始至step6及正式工作台15文件与1MiB上限。
9. 独立step7包与确定性清单、审查报告、完整交接；真实blocked和所有失败/修正记录保留。没有GPU证据就不勾相应300项清单。

## 非目标

不启动GPU任务、不停止现有服务、不新增网页训练按钮、不宣称真实audio_codes已得到；没有GPU资源模式切换、DDP/梯度更新/模型训练/性能或音色验收。操作系统级RAM沙箱、同UID恶意进程隔离与断电耐久不在本阶段承诺内。

---

## 内嵌备忘录：KAGGLE_STEP7_AUDIT.md

# 第七阶段审查：离线声学码事务与真实编码门禁

> 第七阶段冻结证据；当前源码/打包入口为step10，见KAGGLE_STEP10_AUDIT.md。以下统计保留当时结果，不代表实际GPU/编码/训练已验收。

2026-10-21。先保存KAGGLE_STEP7_PLAN.md与Q6的50条行动建议，再增量编码。**实现了调用真实Qwen tokenizer的本机入口与安全事务，但真实编码仍blocked；没有运行真实权重，没有训练。**

## 交付与已保留内容

- 独立`kaggle/kaggle-fixed-step7.py`：222808字节、35资产，SHA256 `3fe57769560c076d6d288a87cae6150b0a9404597eb0ea3997ab26de596f4cd0`。清单source_manifest_step7.json；repack.py默认生成step7。原始与step1–6冻结。
- 新增`py/training_codes.py`和`tools/encode_training.py`；`py/training_data.py`只增固定版本读取租约与删除互斥，既有准备/校验语义不变。没有新增HTTP路由/网页训练按钮；两主视图、命名库、逐条转写、授权隔离、旧快捷参考处理与全部工作台功能保留。
- 正式工作台仍15文件1043155字节/1MiB余5421字节，HEAD不变；独立交付，不提高容量、不删除历史、不直接改HEAD。复制测试仅在隔离临时项目。

## 实现与边界

| 范围 | 本次实现 | 不扩大解释 |
|---|---|---|
| 输入使用租约 | 先固定manifest SHA256并全量校验，再持有目录外`.use-{id}`文件锁；编码期间HTTP删除409，其他输入列表可读 | 合作式Linux flock，不是同UID恶意进程隔离；不修改快照文件集合 |
| 进程死亡 | SIGINT/SIGTERM/总期限停止worker进程组并必要SIGKILL；Linux PDEATHSIG与ppid握手覆盖控制器被强杀 | 生产编码器是单进程CPU线程；不是任意第三方外部进程的系统级沙箱 |
| 真实适配入口 | 懒加载Qwen3TTSTokenizer，CPU/FP32/eager/两线程、单条numpy float32/24kHz全波形 | 当前无Torch/qwen_tts/权重，真实适配只测了stub调用契约，未执行真实编码 |
| 模型固定 | 本地物化JSON/safetensors全文件内容树SHA256，≤512文件/128目录/4GiB/JSON每份≤1MiB；拒绝软硬链接、pickle、auto_map和越界分片索引 | 需可信来源预先固定hash；不是官方签名或权重真实性证明，不能防同UID恶意竞争写入 |
| 加载约束 | local_files_only/offline/trust_remote_code=false/use_safetensors，CPU与实际dtype/配置/特征采样率复核；加载前后及发布前重算模型hash | HF离线参数不是OS断网沙箱；运行时包版本仅记录，不宣称已校验其源码与上游提交完全一致 |
| 结果契约 | 恰好一个返回，ceil(输入帧/1920)行、16列、严格整数0..2047；全部样本顺序/逐条text/统一ref_audio保留 | 结构检查不证明声学码语义、还原音质或训练可用性 |
| 独立输出 | STATE/training_codes/{UUID}/复制全部WAV、rank_plan，写train_with_codes.jsonl和manifest；源输入可随后删除 | 复制会另占磁盘，删除源输入不删除码副本；没有外部训练读取租约 |
| 事务和预算 | 0700/0600，staging全核对后rename发布、失败回滚、下一写操作清理被杀遗留暂存；32份/64MiB单份/256MiB总量/256MiB余量 | 应用预算非OS配额；保守预留原输入大小+8MiB可能提前拒绝，不裁样本绕过限制；无断电耐久保证 |
| 状态 | 真实适配执行返回才可audio_codes_prepared/tokenization_executed=true；注入测试编码器强制test_only_codes/false | tokenization_verified/training/two_rank/inference始终false；不是文本tokenizer/优化器/检查点 |
| 隐私 | 不自动Dataset备份；公开收据不含私人转写或底层异常；子进程剥离已知HF/DeepSeek/Kaggle/访问凭据 | 原始输入/码JSONL确实含转写；本地可信操作员仍可读，临时操作目录并非安全擦除 |

## 本机使用约定

CLI没有Mock编码参数，不提供远程路径执行或下载/安装模式。请使用目标环境Python；以下是操作说明，**并非本沙箱已经执行的真实编码命令**。

1. 通过原有声音库窗口生成第六阶段输入，取得真实`id`和`manifest_sha256`。输入窗口状态仍是input_snapshot_ready，不因另有离线副本而修改其状态。
2. 准备可信来源的Qwen3-TTS-Tokenizer-12Hz本地完整模型，必须物化JSON/safetensors，不直接使用HF缓存软链接或包含README/其他文件的未整理目录。当前没有自动下载器或GPU依赖锁文件。
3. 对选定目录取树指纹，人工核对可信来源后固定；指纹只是变化检测，不证明这个模型属于官方。

```bash
ROOT=${QTTS_ROOT:-/kaggle/working/qtts}
STATE=${QTTS_STATE:-"$ROOT/state"}
python "$ROOT/tools/encode_training.py" fingerprint --model-dir "${MODEL_DIR:?设置可信本地模型目录}"
# 根据真实结果设置INPUT_ID、INPUT_MANIFEST_SHA256、MODEL_TREE_SHA256，不填虚构UUID或示例hash。
python "$ROOT/tools/encode_training.py" encode --state "$STATE" \
  --id "${INPUT_ID:?设置真实输入ID}" --manifest-sha256 "${INPUT_MANIFEST_SHA256:?设置固定输入hash}" \
  --model-dir "$MODEL_DIR" --model-sha256 "${MODEL_TREE_SHA256:?设置预先固定模型hash}" --timeout 1800
python "$ROOT/tools/encode_training.py" list --state "$STATE"
# 以下两个变量应来自本次真正输出，不能拿输入ID/hash替代。
python "$ROOT/tools/encode_training.py" verify --state "$STATE" \
  --id "${CODES_ID:?设置真实码副本ID}" --manifest-sha256 "${CODES_MANIFEST_SHA256:?设置码清单hash}"
# 确定没有手动训练读取后，才删除这个独立副本。
python "$ROOT/tools/encode_training.py" delete --state "$STATE" \
  --id "$CODES_ID" --manifest-sha256 "$CODES_MANIFEST_SHA256"
```

CLI超时允许1..3600秒，正常0，拒绝/blocked/失败/超时2，常规取消130。公开错误不包含库名/转写/原始异常。超时或取消恰逢rename之后、收据之前时，结果可能已经原子提交：先list及固定hash verify，不盲目重跑。父进程被SIGKILL可能来不及给收据；worker自动死亡释放租约，孤立staging在下次写入清理。

码输出JSONL仍使用audio/text/ref_audio及audio_codes；路径必须按**码副本目录作为cwd**解析，不能按原输入或启动命令cwd猜测。rank_plan仍是数学分配，不是两个rank实际运行。默认配置环境变量QTTS_MAX_CODE_DATASETS/QTTS_MAX_CODE_DATASET_BYTES/QTTS_MAX_ALL_CODE_DATA_BYTES；沿用既有上传音频边界。

输入租约并非训练器使用租约：未来真正训练还需阻止删除码副本，接入显存所有权/推理与训练模式、文本tokenizer/实际两rank/梯度/optimizer/checkpoint及重载试听。当前不自动停在线服务，不允许GPU编码参数。

## 分层验证（docs/validation/step7/）

- Python新增33项码事务/模型门禁/CLI/进程测试，加step6冻结回归，总146项。最终146×3＝438通过，python-round1/2/3.txt。包含真实fork租约、控制器SIGKILL、SIGTERM、超时、SIGTERM忽略的后代SIGKILL及pidfd死亡确认；没有真实模型执行。
- Go28顶层/16子测试race三轮；Node工作台API30×3通过。
- training-http3-final.txt：真实Go→analyst→磁盘三轮，新增本机租约阻止HTTP删除且列表可读，保留原输入篡改/独立副本/单独删除与原始库负向解码回归；不增加模型作业。
- codes-cli3.txt：真实本地CLI list/verify/delete与文件事务三轮，**码全为fixture**；原输入删除后码副本仍可校验。另用明确标注的无效fixture权重目录仅触发缺依赖门禁，三次blocked，未加载任何真实模型。
- mock-pipeline.txt：两CPU Mock worker三轮有序分段/取消恢复，非真实双T4。
- browser-repeat3.txt：60 QTTS＋47工作台＝107唯一×3＝321通过（11.5分钟）。包含第七阶段222808字节完整Python系统剪贴板逐字节一致三次且step6保持；final-copy-repeat3.txt另专项3/3通过。均为隔离临时项目。生产JS/HTML未改，不新增主视图。
- 确定性repack当前35资产/原始22哈希、语法/compileall/diff检查通过。runtime-probe.json仍blocked/退出2，Torch/流式后端/ffmpeg缺失，没有模型/GPU验收。

## 初检、复审和失败记录

1. python-initial.txt保留3个测试辅助错误：两处Fixture.reject不接关键字参数、Mock.poll始终活跃使二次清理消耗完预设wait序列。修正测试调用与真实退出顺序，不放宽业务断言。
2. python-review.txt保留一次异步SIGKILL尚未完成时立即读取/proc的竞态；改用pidfd有限等待确认实际死亡。
3. python-proc-reap-race-failure.txt保留最终第三轮一次/proc在exists与read之间被OS回收的ESRCH。仍必须pidfd死亡确认，然后接受已消失或Z/X；没有把活进程当成功。修正后全146项重新跑三轮。
4. 复审发现控制器被SIGKILL会使原独立会话worker继续执行，补Linux PDEATHSIG/ppid握手及实际强杀回归。初版浏览器已75次通过后中止，browser-interrupted-parent-review.txt保留，绝不计最终三轮；修正后重跑。
5. codes-cli-initial-helper-error.txt保留新增测试脚本误用LibraryStore.delete；核对实际remove接口后修正并重新完成三轮。仅测试助手错误，未改生产删库接口。

## 未通过项与下一步

- 码清单固定源输入ID/hash，但不复制原输入完整manifest；删除原输入后仍能核验码副本，却不能从中恢复完整的原库来源/声明资料。需要溯源时保留原输入清单；真正训练接入前须补完整来源/授权封存策略。
- 当前没有真实audio_codes产物、真实Qwen编码/解码/音质证据；本机入口不是模型验收。CPU速度、RAM峰值与目标依赖组合未实测。
- 仍无真实双T4训练、GPU资源模式、文本tokenizer、梯度/优化器更新、loss、检查点或训练后推理。CPU路径是保守前置，不是最终双卡性能方案。
- DeepSeek、物理麦克风、真实ffmpeg压缩容器、首声<3秒/RTF≤0.5/99.5%音色目标仍未验收，不用协议/fixture代替。
- 清单继续21/300，本阶段不增加GPU/编码真实执行勾选。专业自问自答6×50＝300建议，不等于300项修复。
- 下一步先实现可审计GPU资源所有权/推理与离线任务互斥，再在可用目标设备以可信模型完成单条真实编码/解码、完整覆盖、内存与耗时；之后才接文本tokenizer及真正两rank优化器和检查点。

## 固定上游依据

本轮通过GitHub API再次读取以下固定文件，仅核对源码未执行：

- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/prepare_data.py
- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/qwen_tts/inference/qwen3_tts_tokenizer.py
- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/qwen_tts/core/tokenizer_12hz/configuration_qwen3_tts_tokenizer_v2.py
- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/qwen_tts/core/tokenizer_12hz/modeling_qwen3_tts_tokenizer_v2.py

这里记录的是契约参考提交，不是当前尚未安装的运行时包源码身份校验。

---

## 内嵌备忘录：KAGGLE_STEP8_PLAN.md

# 第八阶段计划：同机GPU资源互斥准入与进程持锁

2026-10-21。编码前保存。先核对第七阶段冻结包、supervisor/worker/analyst启动顺序与离线CPU入口。

## 选择与边界

选择保守的**同机同UID整组GPU独占租约**，不按CUDA_VISIBLE_DEVICES索引分割，避免索引/UUID别名绕过。租约固定在/tmp的私有同UID目录，不随QTTS_STATE/模型目录变化；原生flock为准，不使用PID/超时TTL判断可强制抢占。

真实supervisor先持有inference整组租约，再将同一打开文件描述符通过pass_fds交给GPU worker和analyst；孩子验证目录/inode/nonce/模式后采用。管理进程死亡或关闭自己的引用，不释放仍在孩子手中的资源锁。独立真实worker/analyst无继承描述符时必须独占整个租约，因此多进程推理应由supervisor启动；第二套supervisor/独立GPU进程/离线reservation明确busy。

新增本机resource_control.py status/reserve命令。reserve只是有界离线所有权预约，不执行GPU工作、不代表显存空闲、编码或训练。当前不自动停推理、不增加网页按钮/HTTP训练入口、不启GPU编码；需要显式停止既有推理，等待锁释放，再进入后续真实硬件门禁。CPU encode仍不占GPU锁，Mock路径不宣称占GPU。

## 实施顺序

1. 新py/gpu_ownership.py：0700目录/0600不可替换锁文件，拒绝路径软链接/硬链接/非本UID，不删除锁文件。记录仅用于诊断，非锁权威。
2. acquire/adopt/close/status，严格FD类型/inode/nonce/协议/模式；close只关引用，绝不LOCK_UN释放仍被子进程共享的OFD。无任意命令/路径/强制解锁接口。
3. supervisor在模型子进程前占租约；只worker/analyst继承，gateway无GPU描述符。确保凭据/内部FD环境不意外传其他进程；第二实例失败不覆盖supervisor.pid。
4. worker和analyst在任何模型加载前采用/获取租约；Mock跳过且不假报硬件验证。外部ASGI真实import也受保护。生产目录不提供可任意切换的环境变量，测试用显式隔离路径。
5. 修正Proc日志句柄泄漏、kill必须等待leader死亡并清理后代、停止信号早于启动注册、停止期间不再重启；bootstrap不按旧PID/pkill杀进程，忙或遗留PID标记时需人工确认后重启，ready等待绑定本次supervisor存活；保留自动重启、档案恢复与既有认证/备份行为。
6. resource_control status仅给busy/非权威最后记录，不能凭PID不活就宣布空闲；reserve限时1..3600秒、SIGINT/SIGTERM退出释放，SIGKILL由OS回收。没有实际CUDA资源测量。
7. 真实子进程测试：独占、共享FD、父关/父杀但子仍持锁、最后引用释放、不同STATE仍冲突、伪造FD/nonce/模式拒绝、忙时入口在Torch前停止、日志/停止/重启/信号回归。
8. CPU/HTTP/本机CLI与既有全量三轮、Go竞态三轮、浏览器三轮和最终step8完整Python复制。保留step1–7、正式工作台15文件/1MiB及所有失败/中止记录。
9. 独立step8包/清单、阶段审查与完整交接；真实GPU/模型/训练仍blocked，只按真实证据更新300项清单。

## 明确未完成

不是硬件级GPU隔离或跨UID/跨容器协调，不能约束绕过协议的外部进程；同UID恶意替换文件不属于安全隔离承诺。旧step1–7进程不会自动采用新协议，升级前必须手动停干净。没有自动推理↔训练切换/排空会话、GPU编码、训练器、DDP/梯度/优化器/检查点或实际显存/速度证明。原训练码完整来源清单封存和训练使用租约仍是后续任务。

---

## 内嵌备忘录：KAGGLE_STEP8_AUDIT.md

# 第八阶段审查：合作式GPU资源准入，不是自动训练模式

> 第八阶段冻结证据；当前源码/重打包入口为step10，见KAGGLE_STEP10_AUDIT.md。以下保留当时结果，不代表真实GPU或训练验收。

2026-10-21。先保存STEP8计划与Q7的50条建议，再增量实现。**本阶段验证的是Linux进程/描述符/flock协议，没有实际CUDA、显存释放、模型、GPU编码或训练验收。**

## 交付与保留

- 独立`kaggle/kaggle-fixed-step8.py`：230559字节、37资产，SHA256 `777c1d523559c9c734cd5e99841810524284e91269ced23963e8e5ab3f3cc1e1`。清单source_manifest_step8.json；repack.py默认生成step8。原始与step1–7冻结。
- 新增`py/gpu_ownership.py`及`tools/resource_control.py`；增量接入supervisor/worker/analyst与bootstrap；离线CPU编码只增加内部描述符环境清理，没有改成GPU编码。
- 生产JS/HTML/Go未改，仍两主视图及辅助库窗口。命名空库、逐条输入/授权隔离、参考处理、档案恢复、录音/播放/打断、认证、备份和工作台功能保留。
- 正式工作台15文件1043155字节、1MiB余5421字节、HEAD不变；全部15SHA256与第七阶段收据逐一匹配。新包独立交付，不塞入满额工作台，不提高上限或删除旧文件。

## 具体实现与证据

| 项目 | 实现 | 证据与限制 |
|---|---|---|
| 命名空间 | 固定/tmp/qtts-gpu-ownership-{uid}/fleet.lock整组独占，不随STATE或CUDA_VISIBLE_DEVICES变化 | 同机同UID合作协议；不是按GPU设备号或跨容器/跨UID的系统隔离 |
| 文件安全 | 0700目录/0600普通文件，属主/软硬链接/权限检查，锁文件永不被应用删除或替换 | 同UID恶意改文件及外部/tmp清理不在保证内，操作员不可删除资源锁来“恢复” |
| 权威 | 非阻塞原生flock；记录含模式/PID/nonce/创建时间，status不公开nonce且明确record_is_authoritative=false | PID死亡/记录过期/记录损坏都不表示可抢占，只有flock观测有意义；status是瞬时观测不是预约 |
| 持锁继承 | 真实supervisor先取inference租约，仅worker/analyst通过pass_fds继承同一OFD，校验inode/nonce/模式/锁 | gateway不持锁；不是任意外部进程管理器，正常模型进程必须按本版本启动 |
| 最后引用 | close只关闭本进程FD，不发LOCK_UN；父关闭或被SIGKILL，活孩子仍持锁 | 实际fork/exec/父杀/最后引用关闭测试；未证明CUDA驱动内存此时已经同步回收 |
| 模型入口 | 真实worker/analyst在任何模型加载前采用或取得租约；无继承时独占整组 | 多worker应由supervisor启动；第二套真实服务或离线预约busy；Mock明确不取得GPU租约 |
| 生命周期 | 父日志FD及时关闭；kill等待leader退出并清理幸存后代；停止信号提前注册，停止期间不再重启 | 真实进程与模拟故障测试；现有重启/档案恢复/认证与备份逻辑保留，不是优雅排空会话 |
| PID文件 | 第二真实supervisor占用失败前不写supervisor.pid；成功运行后只清自己的标记 | PID文件不再作为资源所有权依据；旧版本标记须人工核实迁移 |
| 引导安全 | bootstrap不再按旧PID或pkill广泛杀进程，busy/遗留标记时启动前阻断；ready等待核对本次supervisor仍活着 | 有意改变自动停旧服务的行为，避免PID复用/旧健康假阳性；不是自动在线模式切换 |
| 离线预约 | 本机status及reserve --seconds 1..3600，超时/取消/进程死亡释放，busy返回2/code409 | 仅空闲预约，不执行任何GPU任务，不代表显存、编码或训练成功；无shell/HTTP/force-unlock接口 |
| 原CPU入口 | encode_training继续仅CPU，剥离GPU FD/nonce环境，不继承资源描述符 | 真实编码仍缺Torch/qwen_tts/权重blocked；fixture仍test_only_codes |

## 本机操作与升级顺序

以下是目标环境操作说明，不是沙箱已经运行真实GPU的证明。新包会写入QTTS_ROOT源码，**升级前先确认所有旧版本GPU服务已停止**；仅检查必须用独立QTTS_ROOT与QTTS_UNPACK_ONLY=1，不要覆盖运行中版本。

```bash
ROOT=${QTTS_ROOT:-/kaggle/working/qtts}
python "$ROOT/tools/resource_control.py" status
python "$ROOT/tools/resource_control.py" reserve --seconds 5
```

- `status`返回busy/last_record/observation_only/gpu_verified=false。busy=false只表示此刻合作锁未被持有，不能证明硬件空闲，也不保留资源。
- `reserve`成功先输出offline_reserved，期限结束输出released；正常0，busy/拒绝2，SIGINT/SIGTERM取消130，SIGKILL由系统报告。全程training_verified=false，没有命令执行或GPU负载。
- 正在真实supervisor/worker/analyst持锁时预约应拒绝。先通过受控进程的正常停止途径终止本应用，等待所有模型孩子退出，再预约；本CLI不自动杀推理、不按旧PID抢占。
- supervisor被强杀但孩子存活时，busy仍为true是安全行为，不能删除fleet.lock/目录强行绕过；需核实并停止遗留的本应用模型进程。仅一个父PID已死不能推断没有孩子。
- 同UID整组锁有意保守：即便机器有更多GPU或子集不重叠，也只允许一套受管推理/一个离线所有者。与GPU索引/UUID如何重映射无关。
- 真实多worker与analyst应由supervisor统一启动。独立启动worker会单独占整个整组租约；第二个独立模型进程会拒绝，不再将多次手工启动当受管多卡。
- 旧step1–7或其他软件没有自动加入协议，升级前必须停干净并检查实际进程/GPU。若bootstrap报遗留supervisor.pid，仅在确认旧服务停止后清理这个**运行时PID标记**；不是删除资源锁，更不是修改正式工作台HEAD或历史。
- 不在真实STATE混跑Mock与真实服务。CPU测试及浏览器全部使用临时隔离目录；Mock不宣称GPU所有权。

当前没有自动“推理↔训练”切换、请求排空、任务取消后恢复旧模型或GPU编码。`offline-reservation`不是`training`；CPU编码仍然可以与该预约同时运行，因为它不调用GPU入口。

## 验证记录（docs/validation/step8/）

- Python新增32项资源/入口/引导/进程测试＋step7冻结回归，合计179项，最终179×3＝537通过。python-round1/2/3.txt。初检ownership29项通过；扩展bootstrap安全回归后32项通过，全量初检179通过。
- 所有权测试用真实fork/exec/flock/文件描述符/父SIGKILL/子继续存活/最后引用退出，不只Mock布尔状态。另有真实worker/analyst入口在离线锁占用时、Torch导入前拒绝，以及真实第二supervisor不覆盖PID文件。
- ownership-process3.txt：真实supervisor/Proc/pass_fds/正常停止协议三轮，两个worker角色和analyst继承、gateway不继承，在线预约409，停止后可预约。**角色均为CPU stand-in，没有真实模型/GPU工作**。
- Go28顶层/16子测试race三轮、Node API30×3通过。
- training-http3.txt：真实Go→analyst→磁盘三轮，旧库负向解码/原始哈希保留/训练输入独立副本/编码读取租约HTTP删除409仍通过，没有新模型作业。
- codes-cli3.txt：本机CLI/存储三轮，码全为fixture；缺依赖真实入口三次blocked，无真实权重加载。mock-pipeline.txt：两CPU Mock worker有序分段/取消恢复三轮，非真实GPU/音质。
- browser-repeat3.txt：60 QTTS＋48工作台＝108唯一×3＝324通过（10.5分钟）。含第八阶段230559字节完整Python剪贴板逐字节相同三次，且step7内容保留；final-copy-repeat3.txt另专项3/3通过。均为隔离临时项目；生产网页未改，不新增主视图。
- 37资产与原始22哈希确定性repack --check、语法/compileall/diff检查通过。runtime-probe.json仍blocked/退出2，缺Torch/后端/ffmpeg；没有模型或GPU验收。

## 复审、环境恢复和行为变化

- 本轮环境没有持久化.venv/node_modules（它们本来就不进入快照）。首次语法命令因缺解释器退出127，随后按既有CPU requirements/npm lock重新安装，日志requirements-install.txt/npm-ci.txt。没有安装Torch或GPU模型，没有修改GPU依赖宣称可运行。正式工作台在恢复服务前后均逐个哈希核对未变。
- 审查发现旧bootstrap的stop_old会按PID发SIGTERM并运行宽泛pkill，且等待可能读到旧健康服务。没有保留危险自动杀行为：改为启动前明确阻断、用户确认停止，并加本次supervisor存活检查；有对应回归，不把它写成“自动模式切换”。
- 初检及三轮目前无测试失败或隐瞒中止；所有初检/专项/最终日志分别保存。不把依赖blocked当模型通过。

## 清单、未完成项与下一步

- 仅新增勾选R2-010的**设计与合作式协议证据**，累计22/300。不勾R2-001/003/006/009/011等自动模式/显存/实际rank条目。专业自问自答7×50＝350建议，不等于350修复。
- 没有真实GPU/VRAM释放或实际模型，锁不约束不合作软件、其他UID或容器。没有CUDA级设备隔离，不承诺当前资源预约能防所有OOM。
- 尚无本次作业代际ID贯通各健康响应；supervisor存活检查不等于所有新网关/子进程就绪，旧端口占用仍须排查。bootstrap内的前置检查也不能替代运行单文件解包前确认旧服务已经停止。
- 未实现自动在线模式切换、GPU编码、文本tokenizer/真实训练器、梯度/optimizer/loss/检查点/训练后推理。
- 原码副本只保存源输入ID/hash，没有完整来源/授权清单副本；真正训练前仍须补来源封存与码副本训练读取租约。当前输入租约不等于训练作业使用锁。
- DeepSeek、物理麦克风、真实压缩容器、音质、首声<3秒、RTF≤0.5或99.5%目标仍无验收证据。
- 下一步优先封存码版本来源/授权与训练读取租约，再接受控离线任务和目标硬件的真实encode/decode/显存回收测量；只有这些门禁通过，才能接真正两rank优化器与检查点，不能用预约/缓存或进程数代替训练。

---

## 内嵌备忘录：KAGGLE_STEP9_PLAN.md

# 第九阶段计划：来源封存与码版本读取租约

2026-10-21，编码前保存。接续第八阶段资源协议，不执行GPU任务或训练。

## 推荐选择与边界

新码版本使用schema2，原样封存输入manifest及train_raw.jsonl，按输入固定hash和原索引hash交叉验证来源库/修订/样本/音频/逐条文本/统一参考/声明/分配计划。schema1历史码继续可列表、核验、读取和删除，但明确legacy-unsealed，不自动补写或伪造缺失授权。授权仍是用户声明，不是法律/声纹证明。

新增TrainingCodesStore.lease固定版本完整核对和进程读取租约，供将来训练器/当前检查工具使用；租约期间删除该码版本409，其他码版本仍可列表核验。租约不是训练许可，fixture和legacy状态不会因此升级，GPU锁/真实训练门禁独立。

## 实施顺序

1. schema2新输出增加source/manifest.json及source/train_raw.jsonl，保存完整原始输入清单字节，不重写来源或声明。rank计划与全部规范WAV仍原样复制。
2. 封存源manifest SHA256等于创建请求固定hash，源JSONL/计划hash等于源清单；逐项与当前码样本ID/帧数/audio/text/ref/成员顺序交叉核对，拒绝篡改或遗漏。
3. source目录纳入字节预算、安全文件集、0700/0600、链接拒绝、原子发布/回滚与完整验证。仍不自动Dataset备份。
4. 读取兼容schema1，不修改旧清单/hash；列表只显示schema政策，不能在未读文件时宣称当前来源完整。完整校验才返回provenance_verified_now。
5. 目录外.use-{id}进程锁，先固定manifest hash并完整核验，再释放全局锁后yield只读上下文；同版本读取首版独占，最后进程退出释放。删除同版本明确409，不用PID或TTL强制抢占。
6. CLI增加hold-read --seconds 1..3600，只保持检查租约，不执行命令/GPU/训练，不输出私人清单/转写；沿用父总超时、SIGTERM/INT与PDEATHSIG。返回收据不能把读取叫训练。
7. 真实文件/源删除后溯源/旧冻结schema1/损坏交叉链接/缺文件/权限/回滚/预算/多进程/退出/超时/取消/备份排除测试。CPU fixture仍test_only_codes，训练标志不改。
8. 全量Python、Node API、Go竞态、真实HTTP/旧CLI/资源FD/CPU Mock三轮，浏览器全量三轮与step9完整源码复制。保留原始至step8及正式工作台15文件/1MiB。
9. 独立step9包/确定性清单/审查/完整交接；未实际GPU/编码/训练的部分如实blocked，300项清单只勾证据覆盖项。

## 不做

不自动迁移旧码、不从当前库猜旧授权、不开放私有来源HTTP下载/上传或任意命令、不宣称read lease是训练任务。没有自动模式切换/GPU编码/文本tokenizer/DDP/optimizer/梯度/检查点。跨UID恶意进程、原件安全擦除、断电耐久、实际GPU/音质/性能未验收。

---

## 内嵌备忘录：KAGGLE_STEP9_AUDIT.md

# 第九阶段审查：完整来源封存与码版本读取租约

> 第九阶段冻结证据；当前源码/重打包入口为step10，见KAGGLE_STEP10_AUDIT.md。以下保留当时结果；旧verify_delivery只适用当时源码，不据此称当前训练尚无实现。

2026-10-21。先保存STEP9计划与Q8的50行动建议，再增量实现。**只验证来源文件与合作式读取生命周期，没有执行真实Qwen编码、GPU或训练。**

## 独立交付与保留

- `kaggle/kaggle-fixed-step9.py`：233074字节、37资产，SHA256 `8ec892dcc5ca10daf20c8de84dd2be08d9a3de8807872c2051ddf52bd5882a9b`。`source_manifest_step9.json`与确定性重打包相符。原始与step1–8冻结；默认repack只生成step9。
- 仅修改生产`py/training_codes.py`、`tools/encode_training.py`及MEMO；无新生产语言、模型依赖、HTTP端点或训练按钮。生产JS/HTML/Go与GPU整组FD协议不改。
- 两主视图、命名空库/样本、授权隔离、逐条转写、输入准备/输入租约、旧参考处理/档案恢复、录音/播放/打断、认证/备份及工作台原有编辑/命名/复制/保存均保留回归。
- 正式工作台仍15文件1043155字节，HEAD `39ed7670-ec8a-4565-a1ae-fff0064d5246`，1MiB余5421字节。新包不写正式工作台、不提高上限、不删历史；浏览器用临时项目。最终只读核对全部15个SHA256及HEAD匹配上阶段，见本阶段formal-api-readonly.json及delivery.json。

## 来源封存设计

| 范围 | 本次实现 | 边界 |
|---|---|---|
| 新版本 | schema2新增`source/manifest.json`与`source/train_raw.jsonl`原始完整字节 | 不猜测来源，不从当前库重新补写历史声明 |
| 原始记录 | 保留源库ID/自定义名/修订、原始样本名/ID/hash、规范WAV/hash/帧数、顺序、文本hash/逐条原文、统一参考、使用权/单说话人声明及源检查记录 | 声明只是用户自述，不是法律授权、身份或实际单说话人鉴定 |
| 固定与交叉核对 | 源manifest hash等于创建时固定hash；原始JSONL和同一rank计划hash等于源manifest；所有当前码行的audio/text/ref与原始行一致；全部样本ID/顺序/帧数/audio/text hash一致 | 主清单固定hash是信任锚，非签名；持有写权限者可另造版本，新pin不是官方背书 |
| 安全/预算 | source纳入限定成员、拒绝软硬链接/嵌套目录、0700/0600、单份/总字节预算；准备时原子暂存/核验/发布，失败取消整份回滚 | 沿用已有预算和安全打开；不是同UID恶意并发写隔离或断电耐久保证 |
| 删除源之后 | 新码可独立核对封存记录，无需原库或输入目录仍存在 | 删原库不等于删码副本、备份或安全擦除 |
| 旧版本 | schema1继续列表/核验/读取/删除，明确`legacy-unsealed`，不重写旧manifest/hash | 不能声称缺失来源已恢复；测试静态提取冻结step8代码生成旧码，不执行旧安装器 |
| 列表与核验 | list的`source_provenance_policy`只说明schema政策，`provenance_verified_now=false`；本次完整verify成功且schema2才为true | 列表不是刚刚扫描全部文件；schema1结构verify仍不产生来源封存证据 |

不保留原库原始音频字节的第二份，只保留其hash/来源名；码目录中仍是既有完整规范WAV。原始JSONL包含私人转写，因此封存跟码副本一起保持本机私有，不新增HTTP下载，也不自动Dataset备份。旧profiles备份内容和语义不变。

## 读取协议与真实进程验证

1. `TrainingCodesStore.lease(id,pinned_sha256)`替代不适用于码格式的继承输入租约。全局锁内取得目录外`.use-{id}`独占flock，完整验证固定版本；取得码metadata/rows后释放全局锁再yield。
2. 长读取期间同版本删除/第二读取409，列表、完整核验和其他版本操作仍可进行。删除与读取共用外部锁，不在快照里添加运行标记。
3. 正常退出、异常、进程死亡由关闭描述符释放；不按PID/TTL抢占，不发LOCK_UN。真实fork继承FD在父上下文退出后仍维持锁，最后继承进程退出后可删除。
4. 这是合作式约定只读，不是OS只读挂载；返回本地路径给可信调用者，并不能防拥有写权限者恶意修改。只提供单版本独占检查原语，没有真实训练器或自动DDP多rank接管。
5. `hold-read`只保持1..3600秒检查租约，沿用控制器总超时、SIGTERM/INT、Linux PDEATHSIG/ppid握手，不提供任意命令/模型/GPU/HTTP执行。收据不输出完整源manifest或转写，`training_allowed=false`、`gpu_verified=false`、`training_verified=false`。
6. fixture读后仍`test_only_codes`，旧码读后仍`legacy-unsealed`；租约不是训练许可。未来训练器必须维持保护直到所有读者退出，并分别执行真实编码、语义/权利政策、硬件、训练门禁。不能把目录完整性当作真实人声/训练质量。

## 本机使用说明（不是目标GPU执行证明）

先用现有`list --state`取实际码ID/manifest SHA256，用固定pin完整verify，不能填虚构ID或拿输入manifest hash冒充码manifest hash。变量来自当前本机结果。

```bash
ROOT=${QTTS_ROOT:-/kaggle/working/qtts}
python "$ROOT/tools/encode_training.py" list --state "$QTTS_STATE"
python "$ROOT/tools/encode_training.py" verify --state "$QTTS_STATE" --id "$CODES_ID" --manifest-sha256 "$CODES_SHA256"
python "$ROOT/tools/encode_training.py" hold-read --state "$QTTS_STATE" --id "$CODES_ID" --manifest-sha256 "$CODES_SHA256" --seconds 5 --timeout 15
```

正常完成0，拒绝/总超时2（busy code409），SIGTERM/INT取消130，SIGKILL由OS处理。hold时间不含准备/核验，timeout含启动/核验；默认timeout1800秒，选择更长保持需显式提高至不超过3600秒，不能保证3600秒保持恰在3600总预算内完成。没有开始/结束训练、优化器或检查点。

升级前先停旧GPU服务再解包覆盖ROOT；仅静态检查用独立QTTS_ROOT及UNPACK_ONLY。第八阶段整组锁/人工处理旧runtime PID标记规则保留，不能删fleet.lock恢复，不把status空闲当实际显存空闲。

## 验证记录（docs/validation/step9/）

- 新增21项来源/读取测试与step8冻结回归，完整Python201项；最终201×3＝603 PASS，`python-round1/2/3.txt`。新用例涵盖精确字节封存、删源后核验、声明/文本/参考/样本hash/修订篡改、无关完整来源重绑定、成员丢失/多余/软硬链接/嵌套目录、权限/容量/失败/取消回滚、旧schema1字节/hash保持、同版本409与其他版本可用、坏pin/坏文件/异常释放、真实进程死亡/fork最后引用、真实CLI超时/取消/控制器SIGKILL与pidfd退出观测、拒绝无限时间/任意命令。
- 最终收据核对工具初版假定HTTP日志只含3条JSON，实际每轮输入/旧库两类共6条；改为按类型键分别确认3个round，不修改原日志，不算业务失败。`final-checks-initial.txt`保留，最终以final-checks.json为准。
- 初检原有33项PASS，新增测试初版20项中1项夹具错误：重复使用同一库名被正确拒绝；改为明确删除原库再建立新来源，20项PASS，再补fork继承最后引用成为21项。原错误日志保留，不包装为生产缺陷；完整初检201项PASS。
- Node API30×3、Go28顶层/16子测试race三轮PASS，JS语法/compileall/diff/repack检查PASS，npm audit报告0漏洞（不等于完整安全审计）。
- `codes-cli3.txt`本机真实CLI/文件事务三轮：schema2来源原字节、删输入/原库后独立核验、持锁删除409、长读不占全局列表、hold-read收据、删除/列表通过；码与门禁权重均为fixture，真实encode三次blocked_missing_dependencies，没有模型加载。
- `ownership-process3.txt`真实supervisor/Proc/pass_fds正常停止三轮PASS，worker/analyst均CPU角色替身；不是GPU或显存证据。`training-http3.txt`真实Go→analyst→磁盘三轮PASS；旧库损坏解码失败/原始hash不变/输入独立性及输入租约HTTP删除409仍通过。
- `mock-pipeline3.txt`双CPU Mock worker三轮PASS：有序段、取消恢复；不是双T4、真实流式模型或音质证据。
- 浏览器：109唯一（60 QTTS＋49工作台）×3＝327 PASS（10.3分钟），`browser-repeat3.txt`。软件输入录音/五CSS视口/两主视图与旧工作台功能保持，不扩大为物理麦克风/全浏览器或真实GPU训练聊天。
- 最终step9完整源码复制专项另3 PASS（9.2秒），`final-copy-repeat3.txt`；均临时项目，保存step8并逐字节比较233074字节step9原文，不改正式workspace。全量中也已覆盖3次。
- `runtime-probe.json`仍blocked/退出2，缺Torch/真实推理后端/权重；没有GPU、真实encode/decode、训练或性能验收。
- `.venv/bin/python docs/validation/step9/verify_delivery.py`只读核对冻结包/37资产/21完整内嵌备忘录/8题400建议/22of300/最终测试日志与正式15文件、HEAD，写final-checks.json及formal-api-readonly.json；需已有Node工作台3000运行，不重跑模型、不修改工作台。

## 三轮各100项与范围审查

本轮逐项保留原300清单的状态，映射记录见`review-map.json`，不是声称300项修复或验收。已勾选仍22/300，8题×50＝400行动建议。

- 第一轮100项：重点补强R1-079声明的可追溯保存，保留R1-073名称/内部ID隔离；R1-075/081/084仅数据文件层部分证据，真实人声、转写匹配/同说话人判断及训练效果不验收。没有扩大GPU/模型/依赖清单完成率。
- 第二轮100项：补强R2-031固定样本/哈希；R2-032只有码副本读期删除互斥，没有实际训练器对全部读者生命周期保护；R2-034保留原始JSONL/码来源，但文本tokenizer/真实声学码版本链仍缺。因此后两项继续不勾，DDP/参数更新/检查点全部不验收。
- 第三轮100项：回归两视图/录音/编辑保存及真实Python复制；新码来源可在删源后核验，但R3-074尚无已发布训练检查点，不能验收。完整包复制仅临时项目，不声称正式满额工作台已发布，也不把浏览器软件流当物理麦克风/真实聊天。

## 下一步与明确未实现

下一专业问题仍须先保存具体计划和≥50建议。推荐先设计受控离线作业的固定输入/模型/码pin、收据、取消/终止及所有读者生命周期，再接真实任务；检查/预约不能伪装为训练按钮。

真实目标门禁仍是可信Qwen模型的完整encode/decode/覆盖/内存/时间、T4环境与显存回收；随后才文本tokenizer兼容、真正world_size=2、两rank数据/梯度同步/optimizer参数更新/检查点及新进程重载试听。不能照搬T4不支持的BF16/标准FA2/全参数AdamW，不能凭accelerate两进程称训练成功。

DeepSeek、物理麦克风/容器、音质、可听首声/标准RTF与身份保留集均未验；不承诺永久会话、<3秒、RTF≤0.5或99.5%身份一致率。协议不能约束跨UID/容器/绕过协议的软件，不能防同UID恶意删改或证明真实显存可用。

---

## 内嵌备忘录：KAGGLE_STEP10_PLAN.md

# 第十阶段：直接开发最小真正训练器，而非再增加准备阶段

2026-10-21。用户要求继续且追问何时真正开发。本轮立即开发训练核心，先保存计划后写码。不再用纯封存/预约工具充当训练进展。

## 具体交付

1. 对照固定上游022e286b98fbec7e1e916cb940cdf532cd9f488e的dataset/sft/model接口，实现本地数据组装和真实联合loss；修正官方示例未过text_projection的维度风险。
2. T4候选路径为FP16/eager、microbatch1、FP32 LoRA/AdamW状态、冻结Base、talker与sub-talker attention q/v低秩更新；不是全参数AdamW，不假称16GB已测通过。
3. 实现真实torch DDP双rank/GradScaler/梯度累积/有限loss/梯度/参数改变检查、每rank样本覆盖、原子adapter检查点。loss与backward必须在DDP包装forward内，不从.module绕过梯度同步。
4. 父控制器独占GPU整组与码版本读取租约，两个rank受控继承相同FD；父死而活孩子仍持锁，不按PID抢占；取消/超时杀整个进程组并等待，才释放父引用。
5. 训练门禁拒绝fixture/legacy；要求schema2来源核验、实际编码状态、用户明确确认输入语义/授权与实验性训练。模型为可信本地Base1.7B完整指纹，离线/拒绝远程代码，不自动安装/下载/停止推理。
6. 固定模型/码hash写入检查点；保存adapter及统一参考speaker embedding，提供明确的加载函数，不把adapter伪装完整CustomVoice模型，不自动替换推理服务。检查点成功仅表示训练运行，质量/新进程试听单独验收。
7. 可执行CLI与Kaggle操作说明；依赖缺失返回blocked，不运行假训练。CPU小网络实际张量/优化器与双进程Gloo仅验证算法/同步，不替代Qwen/CUDA/NCCL验收。
8. 先针对核心测试、再旧功能回归。旧包1–9冻结、正式15文件/HEAD/1MiB不变；新独立包step10。文档只记录本轮已执行证据，不把测试次数当300项完成率。

## 完成界限与时间回答

核心开发现在开始，本轮目标交付可执行训练代码，而非再等审查。真实开训必须在挂载可信完整Base/tokenizer与授权音频的双T4环境执行；沙箱没有GPU/权重，不能给出可信训练成功日期或保证显存/音质。不得显示训练已通过，也不增加假的训练按钮。

---

## 内嵌备忘录：KAGGLE_STEP10_AUDIT.md

# 第十阶段：直接交付训练核心，真实Qwen/T4执行仍待验证

2026-10-21。回应用户“还有多久才能真正开始开发”：**核心开发本轮已经进行并完成实验性实现，不再等待下一轮基础设施。** 保存STEP10计划与Q9的50建议后，直接实现loss、反向传播、DDP、优化器与adapter保存。不能因为尚无目标硬件验收就说“还没开始开发”，也不能反过来把CPU算法测试说成Qwen训练成功。

## 1. 交付

- `kaggle/kaggle-fixed-step10.py`：261429字节、43资产，SHA256 `2bddd6ebad371268f9b3b02315fc29cae588da6c46c7d134476945b50b8a5ac4`。确定性重打包与source_manifest_step10.json匹配。原始与step1–9冻结。
- 新生产模块`lora_adapter.py`、`tts_dataset.py`、`tts_training.py`、`training_job.py`和入口`tools/train_tts.py`；派生dataset/联合loss保留上游Apache声明并附完整LICENSE-QWEN-DERIVED.txt。
- `training_codes.py`向受控rank导出/采用同一读取OFD，旧lease三元组API不变；`gpu_ownership.py`只新增显式offline模式adopt，推理默认仍拒绝offline租约。没有新语言、HTTP训练端点或假训练按钮。
- 生产网页/Go不改，两主视图及旧库/输入/码/认证/录音/复制保存回归。正式工作台15文件1043155字节及HEAD不变，独立交付，不提高1MiB或删除旧文件。
- 实际Kaggle操作与可取消Notebook代码见`KAGGLE_TRAINING_QUICKSTART.md`。目标环境/模型/数据就绪即可尝试本CLI，不以等待第十一阶段为条件。

## 2. 真正开发的内容与边界

| 功能 | 已实现 | 尚不能声称 |
|---|---|---|
| 真实训练目标 | talker codec0 CE＋0.3×sub-talker loss，16组码；speaker encoder冻结，统一参考embedding | 没有运行真实Qwen权重，不能说语义/音色学到或指标达标 |
| 文本/样本 | 固定上游助手格式/尾部处理与collate布局；完整文本、码、规范WAV参考mel；序列预算超限拒绝 | 未现场验证实际Qwen文本tokenizer和所有语言/长音频，不截断假装全覆盖 |
| 投影修正 | 使用talker.text_projection(get_text_embeddings(...))后再与codec相加 | 官方示例直接相加有维度风险；CPU测试故意使用6维文本/4维talker证明投影必要，但不冒充真实Qwen跑通 |
| T4候选策略 | FP16/eager，microbatch1，冻结Base1.7B；仅实际命中的talker/sub-talker self_attn q/v注入LoRA；A/B及AdamW状态FP32，非重入梯度checkpoint | 没有T4显存证据，不保证16GB、不称LoRA官方兼容已验收，也没有照搬BF16/标准FA2/全参AdamW |
| 双rank | 每rank一个显式CUDA设备、NCCL、120秒集合通信超时；整个参数相关loss在DDP.forward内，非经.module绕过 | CPU Gloo成功不等于NCCL/Qwen/真实双T4成功 |
| 梯度与更新 | 正确累积/尾组缩放、GradScaler、全rank有限loss检查、梯度同步/裁剪；任一rank梯度溢出则全体跳步/降scale；至少一次实际参数变化且两rank最终摘要相同 | 不把进程启动、loss打印、退出0或静态rank计划当训练成功 |
| 覆盖 | 每epoch固定seed打乱后按rank划分，奇数重复前缀补偶数，不drop_last；每rank每epoch保存见过ID，保存时核对全体选中覆盖 | 填充样本有明确重复，不假称无重复；真实数据质量/转写匹配靠操作者审阅，不是算法鉴定 |
| 检查点 | 原子保存adapter.safetensors、speaker.safetensors、Base/码pin/层名/覆盖/rank更新与版本、设备/峰值显存报告；load_adapter检查绑定/成员/hash/shape/finite | 是adapter候选，不是完整CustomVoice；不保存可恢复optimizer/scheduler/RNG状态，不自动部署聊天，也未Qwen新进程重载试听 |

源码对照固定上游`022e286b98fbec7e1e916cb940cdf532cd9f488e`的finetuning/dataset.py、sft_12hz.py和core/models/modeling_qwen3_tts.py。没有直接运行上游训练脚本；修正T4精度/优化器规模、DDP调用边界与文本投影风险。已验证的只是下面分层证据，实际包/API兼容仍需现场模型运行。

## 3. 准入、资源和退出

- 严格拒绝fixture、legacy-unsealed、非真实编码状态、少于两个样本或没有明确数据审阅/实验确认。审阅是用户声明，不把tokenization_verified等原始未验证标志变true，不替代法律/身份/语义鉴定。
- Base1.7B完整本地内容树固定hash，拒绝pickle/链接/远程代码/不完整或越界分片；Base内speech_tokenizer指纹必须等于所用码的encoder指纹。hash不是官方签名，需操作者可信来源。
- 父进程先固定码并持码租约，再持GPU整组offline-reservation OFD；两rank仅受控继承同一对FD并核对锁、inode/nonce、模式与固定码。码验证可在多rank同时进行，不依赖互相冲突的全局写锁。
- rank在Torch/CUDA前安装Linux PDEATHSIG并核对ppid，启动信号屏蔽窗口后解除SIGTERM/INT；父在Popen+记录PID窗口屏蔽取消，防丢刚启动的孩子。父死且孩子还活着时仍持OFD，最后引用才释放，不能删锁/PID/TTL抢占。
- 正常取消/总超时/单rank失败/第二rank启动失败，父停止并等待直接rank后才退租。timeout约束rank启动/加载/训练阶段，不含父进程前置指纹与收尾核验，并另有终止等待；不是全命令硬截止。DataLoader没有额外进程；不提供任意命令/外部进程训练器，不自动停旧推理或恢复模型。不是跨UID/容器/恶意同UID隔离，也不证明驱动显存已回收。
- request、rank日志/结果与adapter只在本地training_runs；目录0700、文件0600，Git忽略且原profiles-only备份不纳入。私有框架日志可能含路径/错误上下文，不能公开分享。正式CLI只输出控制器收据，不输出私人转写。
- 完成只说明两rank实际运行/覆盖/参数改变并保存adapter，quality_verified与inference_reload_verified仍false。没有checkpoint的双进程退出0明确失败；失败不替换旧推理模型。

## 4. 已执行证据（docs/validation/step10/）

### 真正的张量与算法测试，不只是Mock状态

- 新增25项训练核心/准入/进程测试，另加step9冻结回归；完整Python227×3＝681 PASS，`python-round1/2/3.txt`，没有跳过Torch测试。
- 小网络使用不同文本/talker维度和两级attention，实际计算联合loss、真实autograd/AdamW更新、冻结Base保持、FP16基座/FP32训练梯度、尾部累积、非有限loss/梯度拒绝/跳步、严格adapter保存/重载/hash篡改拒绝。
- 两个实际CPU进程使用torch.distributed/Gloo和DDP、不同样本分片；前后参数摘要改变，两个rank最终摘要完全一致，每epoch全样本覆盖。单元测试每轮都执行，另`trainer_tensor_check.py`独立三轮，完整摘要/loss/步数/分片在`gloo3.json`，不是Qwen权重或CUDA/NCCL结果。
- DDP日志提示find_unused_parameters=True在小网络没有unused，属于额外图遍历开销警告。真实Qwen尚未验证所有分支，暂保留诊断安全配置，不把警告隐去或宣称极致性能。

### 真正的OS进程与文件保护测试

- 实际Popen/pass_fds/OFD两CPU持锁者，父/孩子生死、取消/超时/第二启动失败、一个失败终止另一个、控制器SIGTERM/SIGKILL和pidfd退出观测；错inode/未持有FD拒绝，默认推理模式拒绝offline采用。生命周期测试内部注入CPU角色/绕过训练准入，仅测协议，生产CLI没有fixture训练开关，不能用它证明训练执行。
- 真实CLI fixture训练明确409且无training_runs创建；真实数据/模型依赖缺失返回blocked/拒绝，不产生训练成功。

### 原有功能回归

- Node API30×3、Go28顶层/16子测试race三轮PASS。真实Go→analyst→磁盘HTTP、旧编码CLI/fixture、supervisor受控FD/CPU角色、双CPU Mock流管线各三轮PASS，分别记录；没有GPU/真实音频质量或DeepSeek请求。
- 浏览器110唯一（60 QTTS＋50工作台）×3＝330 PASS（10.4分钟），包含step10完整复制/保留step9；最终复制专项另3 PASS（10.2秒）。均临时项目，不修改正式工作台，不推广成物理设备/Qwen训练/全浏览器验收。
- 原始22hash/当前43资产确定性repack、Python compileall、JS语法、diff检查PASS。最终`verify_delivery.py`核对原始至step9冻结、43资产、24完整内嵌备忘录、9题450建议、300项状态、所有最终日志/Gloo数值及正式15文件全部hash/HEAD，生成final-checks.json和formal-api-readonly.json。
- 沙箱新装Torch2.8.0+cu128、safetensors0.6.2、packaging25.0仅为CPU张量测试，不是Kaggle生产锁或GPU实测；runtime-probe仍blocked/退出2：CUDA不可用、qwen_tts/流式后端/真实权重缺失。没有模型下载/加载、Qwen训练或真实音频输出。

### 原始失败留存

首次17项核心测试中两个错误：夹具把manifest返回值顺序取反、safetensors.torch缺未声明的packaging依赖；修夹具/补可选CPU测试依赖后17 PASS。扩展生命周期时一项夹具reject不支持kwargs，改lambda后完整25项进入最终227三轮均通过。`training-core-initial.txt`、`training-core-expanded-initial.txt`保留对应失败，非伪造生产缺陷或隐藏中止。

## 5. 三轮各100项范围复审

300条状态映射保存review-map.json，依然22/300。这里是完整目标验收清单，不是开发完成度百分比。Q9新增50项建议，累计9题450建议。

- 第一轮100条：训练Core、LoRA目标、文本投影、Base/tokenizer绑定与包许可证有实际实现；但R1-011/018/064等真设备与模型试验仍阻塞，不将CPU结果套进T4项。
- 第二轮100条：R2-011/012/015/021/022/025/031/034等有真实算法/同步/采样/低秩优化与保存实现、CPU层证据；没有真实Qwen/NCCL/显存，R2-040没有新进程Qwen重载试听，均不夸大验收。R2-001/003/004没有自动推理↔训练切换。
- 第三轮100条：保持录音/两视图/编辑保存复制；小网络参数/adapter重载不等于真实音色/训练后聊天，也没有物理麦克风/DeepSeek/首声/RTF或99.5%身份结果。

## 6. 时间回答与接下来的直接核心目标

**何时开始核心开发：本轮已经开始并交付实验性训练代码。何时可以尝试开训：双T4、完整可信模型、授权真实数据及依赖就绪后即可执行当前CLI，不必等另一个基础设施阶段。何时训练成功/声音达标：未有现场数据，不能承诺小时数或日期。**

下一步直接围绕真实首步训练的错误/显存与adapter新进程重载、接入现有推理/聊天。不要再把收据/预约工具排成新的前置阻塞，也不要只增加训练按钮而后台仍做缓存。自动模式切换、可恢复训练状态、完整模型导出、GPU编码、UI进度/取消、真实质量与性能仍待实做。

---

## 内嵌备忘录：KAGGLE_TRAINING_QUICKSTART.md

# 现在怎样真正尝试开训：第十阶段 Kaggle 操作顺序

2026-10-21。**训练核心代码已开发，不需要再等下一轮基础设施；但本沙箱没有执行真实Qwen/T4训练。** 本入口是实验性Base1.7B FP16 LoRA双rank训练，不是完整成品。历史step10不接训练后聊天；当前step11已实现显式原生adapter推理/聊天接入，见KAGGLE_ADAPTER_QUICKSTART.md；仍无网页自动训练。

## 0. 先分清三个状态

| 状态 | 当前结论 |
|---|---|
| 实际loss/反向/优化器/DDP代码 | 已实现；真实CPU小网络/Gloo验证参数更新与跨rank一致 |
| Qwen1.7B在双T4上完成一个训练步 | 尚未运行；需要Kaggle双T4、可信完整本地模型和授权数据 |
| 训练后的声音可在现有网页直接选择聊天 | step11已接入显式选择候选，非自动覆盖；真实重载/试听/质量仍待验 |

不承诺首轮成功、16GB显存够用、训练耗时或音色相似率。首轮以1 epoch、microbatch1、短合法样本开始，记录真实结果后再优化。

## 1. 目标环境与升级

1. 在Kaggle启用双T4，实际运行`nvidia-smi`核对两卡与其他进程。平台开关不是设备证明。
2. 先停止本应用旧GPU服务，再解包当前step11到目标ROOT。仅检查用独立ROOT与`QTTS_UNPACK_ONLY=1`；这不等于实际启动。
3. 保留平台已有、与驱动兼容的PyTorch。**不要在Kaggle照装`requirements-training-test.txt`的Torch2.8/cu128沙箱测试轮子，更不要无条件升级/卸载CUDA库。**
4. 检查Qwen/transformers/safetensors等模型依赖并按可信上游要求准备。训练CLI不自动安装或下载；缺依赖会拒绝。沙箱没有验证完整目标依赖锁。
5. 挂载可信、完整且物化的`Qwen3-TTS-12Hz-1.7B-Base`本地目录，包含文本tokenizer、根safetensors及其索引/分片、generation config与`speech_tokenizer`。禁止pickle、远程Python代码、HF缓存软/硬链接；不能只放空config或假权重。可读README/许可证不代表模型权重可信。

参考实现固定来源：
- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/dataset.py
- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/sft_12hz.py
- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/qwen_tts/core/models/modeling_qwen3_tts.py

没有照搬BF16/标准FA2/全参数AdamW；训练器修正文本嵌入到talker隐藏维度的投影，并把完整联合loss放在DDP.forward内。派生代码保留Apache声明，包内附LICENSE-QWEN-DERIVED.txt。

## 2. 真实数据与声学码

- 在已有命名库/输入准备流程提供自己有权使用的同一说话人音频和逐条匹配转写，完整24kHz mono PCM16 WAV；统一参考≤16秒。首轮至少两个不同样本，建议短样本，不接受fixture或旧未封存码。
- 使用原有`encode_training.py`对实际输入固定manifest hash进行真实CPU声学编码；模型目录应取该Base内`speech_tokenizer`的同一物化内容树。CPU编码可能慢，不能据此保证速度。
- `encode_training.py list/verify`读取实际结果。仅schema2且state=`audio_codes_prepared`的真实编码可进入训练；`test_only_codes`或`legacy-unsealed`明确拒绝。
- 结构一致不证明转写/说话人/内容适合训练。训练前由操作者实际检查这些内容与使用权；CLI显式确认不等于机器语义验证或法律鉴定，源码清单原验证标志不会自动升级。

## 3. Notebook内调用：不填写虚构ID，不在命令写密钥

先在私有Notebook中设置以下**真实非密钥路径/ID**环境变量：
- `QTTS_ROOT`：已解包当前step11源码根目录；
- `QTTS_STATE`：当前本地状态目录；
- `QTTS_BASE_LOCAL`：可信完整Base1.7B物化目录；
- `QTTS_TRAIN_CODES_ID`：从当前list结果选定的真实码版本ID。

下面代码读取真实list并取对应固定hash，不猜第一个版本、不自动选择别人的音频。变量没设置会明确失败；不要将私人转写或密钥粘贴到共享报告。

```python
import json, os, subprocess, sys
from pathlib import Path

ROOT = Path(os.environ['QTTS_ROOT'])
STATE = Path(os.environ['QTTS_STATE'])
BASE = Path(os.environ['QTTS_BASE_LOCAL'])
CODES_ID = os.environ['QTTS_TRAIN_CODES_ID']

def cli(tool, *arguments):
    output = subprocess.check_output(
        [sys.executable, str(ROOT / 'tools' / tool), *map(str, arguments)],
        text=True,
    )
    return json.loads(output)

versions = cli('encode_training.py', 'list', '--state', STATE)['result']
matches = [v for v in versions if v['id'] == CODES_ID]
if len(matches) != 1:
    raise RuntimeError('指定的真实码版本不存在；先检查当前list结果')
selected = matches[0]
if selected['schema'] != 2 or selected['state'] != 'audio_codes_prepared':
    raise RuntimeError('拒绝fixture或未封存历史码；先完成真实声学编码')
CODES_SHA = selected['manifest_sha256']
cli('encode_training.py', 'verify', '--state', STATE,
    '--id', CODES_ID, '--manifest-sha256', CODES_SHA)
BASE_SHA = cli('train_tts.py', 'fingerprint', '--model-dir', BASE)['base_model_sha256']
```

再次检查真实推理服务已停止、合作锁空闲，并用`nvidia-smi`检查显存。锁空闲并不证明显存空闲；不要删除fleet.lock或按旧PID强行抢占，不会自动停推理。

**只有亲自完成数据/权利审阅并接受实验风险后，才执行以下训练调用。** 它会真正尝试加载模型和进行优化，不是无副作用的演示：

```python
command = [
    sys.executable, str(ROOT / 'tools/train_tts.py'), 'train',
    '--state', str(STATE), '--id', CODES_ID, '--manifest-sha256', CODES_SHA,
    '--model-dir', str(BASE), '--model-sha256', BASE_SHA,
    '--epochs', '1', '--accumulation', '4', '--max-sequence', '1024',
    '--lora-rank', '8', '--lora-alpha', '16', '--lr', '0.00002',
    '--timeout', '1800', '--confirm-data-reviewed', '--ack-experimental-training',
]
process = subprocess.Popen(command, text=True, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, start_new_session=True)
try:
    stdout, stderr = process.communicate()
except KeyboardInterrupt:
    process.terminate()  # 向本次持有的控制器对象取消，不查旧PID文件
    stdout, stderr = process.communicate(timeout=15)
    print(stdout)
    raise
print(stdout)  # 仅控制器收据，不输出完整私人转写
if process.returncode != 0:
    raise RuntimeError('训练没有完成；检查本机私有training_runs收据/日志，不要标记成功')
receipt = json.loads(stdout)
```

两rank必须各有实际设备、更新参数且最终adapter摘要相同，全部选中样本覆盖，才会保存adapter；奇数样本采用重复打乱序列前缀补偶数，报告保留重复ID，不drop_last。序列超预算整份拒绝，不裁掉文本/音频。timeout包含rank启动/模型加载/训练，不含父进程前置指纹/收尾核验，终止另有等待；未承诺30分钟足够，也不是全命令硬截止。

## 4. 结果、取消与下一步

- 本地`STATE/training_runs/<job_id>/`有request、每rank私有日志/JSON、result；成功有`adapter/adapter.safetensors`、`speaker.safetensors`、manifest。
- 私有日志可能包含框架路径/错误上下文，不要公开粘贴。请求/音频/文本/adapter不进Git，不自动Dataset备份；删原库不等于删输入/码/训练副本。
- 正常完成返回0，失败/拒绝/总超时2，控制器SIGTERM/INT取消130。Notebook仅中断`subprocess.run`不保证自动向孩子发受控取消；长训练应保留明确的Popen对象，向该控制器发terminate并wait，不按陈旧PID发信号。父SIGKILL也有rank PDEATHSIG与共享FD最后引用保护。
- 不支持恢复optimizer/scheduler/RNG训练状态；当前adapter是推理候选，不是完整可恢复训练检查点或CustomVoice模型。中止/失败不覆盖旧推理模型。
- `tts_training.load_adapter(core, checkpoint, base_directory)`严格检查Base绑定/文件hash/层与张量后挂载LoRA，返回保存的统一参考speaker embedding。须单独加载同一Base、按Base克隆prompt协议接入，并用新进程真实合成/试听；当前没有网页自动部署，不能把CPU小网络重载当Qwen验收。

**多久能开始：代码入口现在已有；真实环境与数据就绪即可尝试，不依赖另一个开发阶段。多久训练成功/达到目标音色：目前没有可靠实测，不能给出保证。** 下一开发重点是现场首步故障修复和训练adapter接入现有推理/聊天，而不是继续追加封存工具。

---

## 内嵌备忘录：KAGGLE_STEP11_PLAN.md

# 第十一阶段：训练adapter接入现有声音选择与聊天链路

2026-10-21，先保存计划再写码。原始至step10冻结，继续当前分支，保持正式工作台与两主视图。

## 选定实现

使用显式选择的官方Qwen原生推理后端加载LoRA；不猜faster-qwen3-tts私有模型/CUDA graph能接受动态LoRA。默认faster流式后端完全保留。新模式明确为qwen-adapter-buffered：一条文本段完整生成后才输出一块PCM，不冒充声学流式或<3秒性能。

1. 严格校验完成训练run/result/request/adapter manifest与固定hash、NCCL两rank/参数更新/覆盖、adapter tensor摘要和保存speaker向量。CLI把真实完成的训练候选发布成带固定binding的命名profile，不改active或自动切模型。
2. 发布时持原码租约，复制统一参考WAV和对应文本到profile，保留固定run/Base/码pin。声明和记录不是法律或加密证明；同UID恶意造记录不在保证内。训练目录/模型不自动云备份，profile仍沿既有profile备份语义；恢复缺依赖必须拒绝。
3. Worker显式引擎选择。native模式每GPU只驻留一个可信本地Base1.7B/FP16/eager；默认/Mock不得接收trained profile或静默退回原Base。
4. 预校验/预构造所有LoRA矩阵与speaker prompt后再整体切换，锁内生成，失败不能半挂载/混音色。不同adapter允许不同rank，且必须属于同一固定Base；每次使用核验当前绑定，禁止缓存绕过撤销/损坏。
5. 官方x-vector-only prompt直接使用保存的统一speaker embedding，不重新生成另一个说话人参考；不改成CustomVoice或伪情感模型。实际语音/音色仍须现场试听。
6. 接入现有Worker PCM帧→Go调度/聊天→网页声音选择；health/stats及UI明确训练候选、未质量验收、句级缓冲。没有新增主视图，没有假训练按钮。
7. 取消传入Transformers stopping_criteria，完成后再检查取消并丢迟到整段；不能保证中止正在执行的CUDA kernel或codec decode。保留旧实时后端/播放打断路径。
8. 固定训练profile拒绝文本/候选/校准改写，保留删除。适配启动/探针选择，native不要求faster包；实际依赖/硬件缺失如实blocked。
9. CPU真LoRA张量切换/隔离/失败回滚、恶意/过大/损坏/错误完成记录、准入/Mock拒绝、取消与PCM帧/真实HTTP/浏览器回归。CPU接口替身不冒充Qwen/T4声音实验。
10. 三轮原功能回归、独立step11包、审查与完整交接。下一门禁直接是Kaggle实际训练后重载/试听和真实聊天，不再加收据工具前置。

---

## 内嵌备忘录：KAGGLE_STEP11_AUDIT.md

# 第十一阶段审查：训练adapter已接入原生推理及现有聊天

2026-10-21。先保存STEP11计划及专业问题10的50建议，再写实现；不向用户重复提问。**这是实际接入代码，不是再做一轮训练准备工具。** 当前无真实Qwen/T4权重、CUDA和外部DeepSeek实验，硬件/音质门禁不升级。

## 1. 交付与选择

- `kaggle/kaggle-fixed-step11.py`：276043字节/46资产，SHA256 `cd5346e8ae34f1e2db327a076a7411996982848f9d4e14236f05d94c626d496e`，`source_manifest_step11.json`对应当前source；repack默认step11。
- 原始至step10冻结；step10仍261429字节/43资产、SHA256 `2bddd6ebad371268f9b3b02315fc29cae588da6c46c7d134476945b50b8a5ac4`。不覆盖旧可运行路径、不改正式满额15文件工作台。
- 不猜faster私有对象/CUDA graph支持动态LoRA。保留默认faster路径；显式`QTTS_TTS_ENGINE=qwen-adapter-buffered`启用官方原生推理，**句级缓冲，不是声学流式**，不混驻两种模型或完整Base副本合并。
- 完整目标审查300条仍22项已验，不是开发完成百分比；10题×50=500建议，不是500项已实施修复。

## 2. 具体代码

| 位置 | 已实现 | 不能推导 |
|---|---|---|
| `trained_profiles.py` | 严格完成run/request/result/manifest交叉核验；固定Base/码pin；两NCCL-shaped rank更新及每epoch样本覆盖记录；限定成员/文件大小/hash/tensor digest/FP32/finite；发布持原码租约，复制统一参考WAV和匹配转写 | 本地记录不是官方签名或同UID恶意造记录的防护；声明不是法律/身份证明 |
| `tools/trained_voice.py` | describe取真实pin，publish要求显式run/pin/自命名与未验收确认；不自动active，不输出私人文本或原始模型路径 | 发布不是训练，不证明声音相似或重载完成；不是GUI训练按钮 |
| `lora_adapter.py` | 全量验证/构造replacement后事务提交，可不同rank切换，提交异常回滚；保持原Base模块，不重复叠挂旧LoRA | CPU输出恢复不是Qwen语音可听一致性或CUDA内存适配 |
| `adapter_engine.py` | 本地Base前后指纹、CUDA单可见卡、Base1.7B FP16/eager；每段核对绑定/adapter，不每句重新hash多GB Base；保存speaker直接生成官方x-vector-only prompt | 实际config的base/1b7/16组及版本/停止条件行为仍须真实权重验证；无模型或T4显存证据 |
| `worker.py` | 显式引擎选择，Mock/默认拒绝trained profile，原生拒绝普通profile；锁内切换/生成，原生单wave转既有PCM帧；取消后丢迟到wave，错误无Base回退 | 停止播放/AR stopping不能中断CUDA kernel/codec decode；错误不等于立即清除GPU任务 |
| Go调度/监督 | 原生无帧/health/supervisor预算180秒；默认60/75/90秒不变。继续有序切段、HTTP/SSE、双worker与原activate门禁 | 预算不是延迟承诺，不保证任意长句180秒可完成 |
| 网页/analyst | 选择器/档案/health标注训练候选、句级缓冲、未验收；参考只读，编辑/校准409；旧普通档案操作及删除保留。修复一致性检测全失败仍可能consistent=true | 比较指标不是人工试听、身份或质量验收；没有新增第三主视图 |
| bootstrap/probe | native检查官方Qwen接口，不要求faster包；固定本地Base，不预下载陌生模型；缺依赖blocked，不自动更换引擎 | API形状通过不是模型运行；Kaggle完整安装/启动路径仍待实机执行 |

## 3. 数据与失败边界

- 新profile仍沿旧profiles私有Dataset备份语义，含一段统一参考WAV及对应文本；run/全体训练数据/完整Base不自动备份。操作说明明确告知，不把音频/权重/私密状态进Git。
- 发布时依赖原码固定版本；运行推理需要同一Base和run/adapter。恢复缺adapter/Base必须明确失败，不用参考缓存或Mock输出冒充训练声音。删原码、原库、profile、run和远程备份是不同操作。
- 训练profile绑定固定版本，不自动修改原有active。两worker均确认才改变active，某卡失败保留active；个别worker可能已加载另一adapter，但下一次请求会按其profile在同一锁内重新选择，不能把一次load当后续永远正确。
- 原生一条文本完整生成后才yield一个wave，要求24kHz mono/有限/非空/非全零/长度预算。后处理、停顿与flush产生多个PCM帧不构成声学流式证据。首个真实语音包时间仍由模型wave返回后计算，不能拿预置停顿冒充TTFA。
- 失败切换保留原adapter对象和prompt，但错误请求不得调用原adapter生成；绑定/文件损坏即报错。Base仅加载期固定指纹，后续内存/文件任意同UID恶意修改不属于隔离保证。

## 4. 本轮已执行的验证

- Python完整252×3=756 PASS，38.129/37.891/36.272秒：包括24项新adapter测试和旧训练/存储/访问控制/包/录音契约。真实CPU LoRA数学证明A/B输出不同、A→B→A精确恢复、不同rank、失败预构造不半写、两worker对象隔离。CPU Gloo小网络训练在三轮完整suite内实际运行，不是Qwen/NCCL。
- `adapter_gateway_check.py`：真实本机Go网关/HTTP/SSE、两个独立worker进程、CPU tiny LoRA+注入官方API形状的生成替身，3轮A→B→A，通过真实聊天切段/帧有序与句级缓冲stats；损坏第二版本后activate 503、原active保留，两worker错误请求无PCM。SSE和wave是本机替身，**不是真实DeepSeek、Qwen声音或NCCL**。
- Go race count=3 PASS；Node30×3 PASS。
- 既有ownership_process_check、training_gateway_check、codes_cli_check、mock_pipeline各调用3次，每次内置3轮，均PASS（各9轮CPU/协议，不是9轮GPU验收）。
- 浏览器112×3=336 PASS（11.0分钟）：新训练候选标注/只读/按钮/现有聊天选择/诊断、全量旧录音/存储/安全/视图及包复制均保留。最终包额外逐字复制3/3 PASS（10.0秒），`final-copy-repeat3.txt`与最终`final-checks.json`留证，不用网页截图冒充目标模型证据。
- native runtime probe **blocked/退出2**，model_loaded/inference_verified/training_verified/performance_verified均false。沙箱Torch2.8+cu128仅CPU测试，CUDA不可用，无qwen_tts或真实权重，不是Kaggle依赖锁。

## 5. 失败记录与修复

1. 新浏览器测试首轮1失败/1通过：默认处于语音对话，测试未进入录制参考视图就用可见role找档案按钮。补显式视图切换，2/2通过；`browser-initial.txt`保留，不删失败。
2. 完整Python首轮248测试1失败：旧探针AST测试仅期望faster调用，新增native接口后不再覆盖两引擎。修正为分别核对两份真实调用关键词集合，并补全native sampling参数探针；`python-initial-failed.txt`保留。扩展后252×3全通过。
3. shell曾用错误工作目录调用仓库相对路径和错误gofmt位置；未更改生产代码，改用仓库根/已安装Go实际路径，最终编译/race通过。不是目标Qwen故障或被隐藏的模型成功。

## 6. 三轮各100项建议复审与后续

`review-map.json`逐条保留300条原始建议/目标、当前证据关联与阶段行动，按源码环境、模型音频、系统交互三组100条审查。新增修复以本报告代码表为准，不把300个范围映射当300个新缺陷或已修复条目。完整目标22/300保持，真实权重/GPU/音质/性能未勾选。

下一项直接到真实Kaggle：先小数据真实首个优化步/峰值显存，完成run后在**新进程**按pin加载、每GPU保存和试听WAV、A/B/A、真实DeepSeek长回答/停止恢复，分别记录句级缓冲首声及默认faster声学流式。按KAGGLE_ADAPTER_QUICKSTART.md执行，不增加另一个工具前置阶段，不承诺成功日期、16GBfit、<3秒、RTF或99.5%身份相似率。

---

## 内嵌备忘录：KAGGLE_ADAPTER_QUICKSTART.md

# 第十一阶段：训练adapter → 命名声音 → 现有聊天

2026-10-21。**接入代码已实现，真实Qwen/T4训练、重载及试听未验收。** 原有faster声学流式路径不改；新后端是官方Qwen原生API，**句级缓冲，不是声学流式**。没有新增第三个主视图或假训练按钮。

## 1. 前提与模式边界

- 使用`kaggle-fixed-step11.py`，先停止旧GPU服务再解包到自己的ROOT；可用`QTTS_UNPACK_ONLY=1`仅解包，不代表启动成功。原始到step10均保留。
- 依照`KAGGLE_TRAINING_QUICKSTART.md`，真实完成一个schema2实际编码输入的双rank训练，取得`result.json`中的**实际job_id**。failed/timeout/cancelled/缺检查点、fixture/旧未封存码不能发布。
- 保留训练run下request/result/adapter三件套和原码版本；发布时会持原码租约验证并读取统一参考。不要猜某个目录名或自动选第一个run。
- Base必须是训练使用的同一可信、物化完整本地Base1.7B，hash固定。禁止pickle、remote code与HF缓存链接。目标依赖仍需自行审查，不把沙箱Torch2.8/cu128测试轮子照装到Kaggle。当前代码严格检查base/1b7/16组契约，真实权重config尚未核验；如不一致应对照真实config修正代码，不能改元数据伪造通过。
- 原生启动要求已有官方`qwen-tts`、`safetensors`及兼容依赖，不自动用未知版本替换引擎。与faster的CUDA graph注入兼容性未验证，所以**不向faster动态注入LoRA，也不离线合并并复制完整Base**。
- 每个worker仅一个可见GPU、一份Base；由既有supervisor分配GPU0/1。CPU接口替身测试不是这两卡已运行的证据。原生模式只接受训练候选，普通参考档案仍保留，但要使用原有faster模式；不在同一个worker里混驻两种模型。

## 2. 显式发布，不自动激活

在私有Notebook中设置自己真实的`QTTS_ROOT`、`QTTS_STATE`和`QTTS_TRAIN_RUN_ID`；最后一个来自本次成功训练收据。下面使用实际记录读取hash，不填写虚构ID。

```python
import json, os, subprocess, sys
from pathlib import Path

ROOT = Path(os.environ['QTTS_ROOT'])
STATE = Path(os.environ['QTTS_STATE'])
RUN_ID = os.environ['QTTS_TRAIN_RUN_ID']

def voice_cli(*args):
    output = subprocess.check_output(
        [sys.executable, str(ROOT / 'tools/trained_voice.py'),
         *map(str, args)], text=True)
    return json.loads(output)['result']

record = voice_cli('describe', '--state', STATE, '--run-id', RUN_ID)
```

亲自确认该run及数据来源、权利和实验风险后，设置自己要显示的`QTTS_TRAINED_VOICE_NAME`，再执行：

```python
published = voice_cli(
    'publish', '--state', STATE, '--run-id', RUN_ID,
    '--adapter-sha256', record['adapter_manifest_sha256'],
    '--name', os.environ['QTTS_TRAINED_VOICE_NAME'],
    '--ack-unverified-adapter')
print(published)
```

输出profile_id、pin和`active_changed=false`；音质/现场重载验收标志仍false。**发布不是训练，不会替你启动模型、证明音色相似或自动启用。** 完成记录与声明只是同UID合作流程记录，不是官方加密签名/法律证明，也不能防同UID恶意伪造整个训练目录。

发布会把一段统一参考WAV及匹配转写复制进现有profiles目录；该目录**沿旧私有Dataset备份语义**，启用原有备份后可能上传这些内容。训练run、所有训练样本和完整模型不会因此自动云备份。删除原库不等于删profile或远程备份；删除profile也不自动删除run。备份恢复若缺少对应run/adapter/Base，新后端必须报错，不会换成原Base或另一声音。推理只读取已固定的adapter记录，原码仅是发布时依赖；删除原码后，已发布profile仍需单独管理。

## 3. 原生后端启动

先按既有所有权协议停止自己旧推理任务并确认相关rank已结束；不要删除锁或拿旧PID盲杀。`nvidia-smi`另查真实显存，合作锁不证明设备空闲。

设置`QTTS_BASE_LOCAL`为同一完整本地Base，并在**新启动进程环境**中选择后端：

```python
runtime_env = {
    **os.environ,
    'QTTS_ROOT': str(ROOT),
    'QTTS_STATE': str(STATE),
    'QTTS_MODEL': str(Path(os.environ['QTTS_BASE_LOCAL'])),
    'QTTS_BASE_SHA256': record['base_model_sha256'],
    'QTTS_TTS_ENGINE': 'qwen-adapter-buffered',
    'QTTS_MOCK': '0',
    'QTTS_DTYPE': 'fp16',
    'QTTS_TUNNEL': 'none',
}
runtime_env.pop('QTTS_UNPACK_ONLY', None)
runtime_env.pop('QTTS_ALLOW_SINGLE_GPU', None)
subprocess.run([sys.executable, str(ROOT / 'py/bootstrap.py')],
               env=runtime_env, check=True)
```

这会真正尝试加载模型及运行既有服务，不是无副作用检查；仍需检查目标环境工具链与启动日志。Secret使用既有私有配置，不在共享命令/报告里输出。先本地验证，再决定是否启用公网隧道。bootstrap的实际依赖/编译安装路径尚无Kaggle现场验收，不承诺启动耗时。

新后端在加载前后核对Base树hash，仅启动时读完整Base；每次声音使用核验profile binding、run状态及adapter成员/hash/张量摘要，不每句重新hash多GB的Base。它加载官方eager/FP16，不复用faster图；使用保存的speaker embedding构造x-vector-only prompt，而不是重算一个无关参考或伪装成完整CustomVoice。

## 4. 现有界面选择与对话

1. 打开原有控制台并解锁；只有“录制参考语音 / 语音对话”两主视图。
2. 声音列表显示“训练候选/句级缓冲/未验收”。在档案卡片点“选择此训练版本（双GPU加载，句级缓冲）”。两worker必须确认加载才改变active；某卡失败不把界面标成启用成功。
3. 训练参考文本只读，保存文本/候选校准禁用，后端同样返回409；要变更训练条件请另做明确训练版本。删除入口保留。
4. 先用直接朗读短句测试，再用现有DeepSeek流式文字与语音聊天。网关仍切段、双worker调度、有序转发及播放停止；声音选择使用当前profile_id。
5. 原生API一段文本生成并解码完成才给出一个wave；Worker后处理的PCM尾部/停顿帧不意味着模型声学流式。诊断health、Worker stats标注`sentence-buffered`。首声可能明显慢于faster，不承诺<3秒/RTF/16GB适配。
6. 取消传入Transformers stopping criteria；取消后丢掉迟到完整wave。停止语音播放不等于立即终止正在执行的CUDA kernel/codec decode；下一请求可能仍需等worker释放锁。
7. 原生无帧等待/健康stall/监督重启预算180秒，旧faster分别保持60/75/90秒；这只是保护预算，不保证任意长句180秒完成。超时不能改成“通过”。

切回原有普通参考声音：先正常停止自己原生服务，再以`QTTS_TTS_ENGINE=faster`启动原有模式。原生模式拒绝普通profile，faster/Mock拒绝训练profile；没有自动卸载再偷偷换引擎的路径。

## 5. 必须现场填写的验收

- 双T4实际设备、每worker唯一GPU与各自一份Base、真实峰值显存；先一个小训练步，检查权重变化与跨rank一致。
- **新进程**按固定pin重载同adapter；每GPU输出真实24kHz WAV，确认非空/有限/非全零，盲听参考与输出，不把CPU oracle或profile文件当试听证据。
- 两个已训练版本A→B→A、同文本同seed及不同文本；损坏/缺失绑定必须明确失败，不能输出原Base冒充训练声音。
- 真实普通路径回归、DeepSeek回答中途切换/取消、长回答有序播放、耳听断句和爆音；测首个真实语音包及完整延迟，明确句级缓冲。
- 没有真实Qwen/T4运行、物理音频及外部模型可用性证据时，上述项保持“待验收”。当前下一步就是这组真实运行，不增加工具前置阶段。

---

## 内嵌备忘录：KAGGLE_STEP12_PLAN.md

# 第十二阶段：依据Kaggle现场日志修复Mimi/RoPE兼容与启动重启风暴

2026-10-21。先保存计划与Q11，再写实现；原始至step11冻结。用户已实际识别两张Tesla T4，Python3.12.13/Torch2.10.0+cu128/faster0.5.4/Transformers5.20.2，模型加载报MimiConfig.rope_theta，尚无加载/推理成功证据。

1. 审查PyPI实际wheel：faster0.5.4要求qwen-tts-hf>=0.1.1.post1和Transformers>=5.15.1，不能只降Transformers到4.x造成依赖冲突。qwen-tts-hf兼容函数仍读取config.rope_theta，现代Mimi使用rope_parameters。
2. 在原实际依赖组合上做最小、可拒绝、不猜theta的兼容桥：仅包装已识别Qwen默认RoPE函数；从现代Mimi配置真实rope_parameters读取theta，对临时config副本提供旧字段，不改模型权重/config文件、不把theta统一硬编码为10000、不改非默认scaled RoPE。
3. Worker/CPU编码/原生推理/训练的Qwen加载前接入；前置探针增加真实MimiConfig+Qwen默认RoPE CPU数值smoke，早于权重加载，不再只验签名。固定faster/hf/transformers已审查三版本，保留平台Torch/CUDA，不盲降/升级。
4. 不兼容异常标fatal，supervisor停止该worker而非反复重启；bootstrap看见fatal及启动失败时清理它自己创建的supervisor，保留合作FD直到子退出。不给旧日志PID发盲杀命令。
5. 两worker继续分别只看GPU0/1，健康报告真实设备/驻留状态；模型加载成功后保持常驻，不自动空闲卸载。验证是假设备/CPU替身时不能说双T4模型成功。Kaggle会话/硬件回收不受应用控制，不承诺永久GPU。
6. 新step12包与浏览器复制页面更新，step11冻结；给用户明确“停止并重启完整Kaggle会话后复制新包”，不是仅刷新网页/重跑旧cell。
7. 真实wheel配置复现与修复数值对照、负面配置、旧接口不变、fatal控制器/双卡分配/源码复制及已有回归三轮；完整Qwen/双T4仍需用户目标再次运行验收。

---

## 内嵌备忘录：KAGGLE_STEP12_AUDIT.md

# 第十二阶段：根据Kaggle实际日志修复MimiConfig.rope_theta

2026-10-21。先保存STEP12计划与Q11的50项建议，再写实现。原始至step11冻结；这次直接修用户已遇到的模型加载故障，不另设训练准备阶段。

## 1. 现场事实与诊断

用户日志显示：Python3.12.13、Torch2.10.0+cu128、faster-qwen3-tts0.5.4、Transformers5.20.2；两张Tesla T4、计算能力7.5、每卡总显存15636037632字节。依赖探针形状通过，Go/Rust编译和模型下载完成；随后两worker均报`AttributeError: 'MimiConfig' object has no attribute 'rope_theta'`并被监督器重启。**这些日志证明到达模型加载并失败，不证明模型已常驻或推理成功。** HF未登录警告不是此次核心异常。

读取实际PyPI wheel与元数据后确认：

- faster0.5.4依赖`qwen-tts-hf>=0.1.1.post1,<0.2`及`transformers>=5.15.1,<6`。不能只把Transformers降到4.x，那个组合违反依赖。
- qwen-tts-hf0.1.1.post1共享`qwen_tts`命名空间，其中`_transformers_compat._default_rope_parameters`仍直接读`config.rope_theta`。
- Transformers5.20.2的实际MimiConfig已使用`rope_parameters`，不存在该旧属性。默认配置及旧`rope_theta=12345`输入都被规范化到现代字典。
- CPU中使用**实际TF5.20.2类+实际Qwen-HF wheel函数**复现同一个AttributeError，修复后检查10000/12345/1000000三个theta的精确频率及原配置不变，通过三次独立进程。未构造完整Qwen、未载权重、未用CUDA。

来源与许可证：
- https://pypi.org/pypi/faster-qwen3-tts/0.5.4/json
- https://pypi.org/pypi/qwen-tts-hf/0.1.1.post1/json
- https://pypi.org/pypi/transformers/5.20.2/json
- Qwen函数来源`qwen_tts/_transformers_compat.py`，Apache-2.0。新桥接调用原函数，不把整份第三方实现混写进新模块；包内原Apache许可保留。
- 实际Qwen-HF wheel SHA256 `ed5b7aae64cf795243369fb5226173f459a45689ea86db1c6d3eb14fc0c2c01d`，所用成员SHA256 `033673335ed7bcb19054cdabc6c8400e443493f4b54340f8f449577d122bf982`。三项完整requires_dist/wheel digest记录在step12证据目录。

## 2. 实际修复

| 部分 | 改动 | 边界 |
|---|---|---|
| `qwen_compat.py` | 仅包装已识别Qwen默认RoPE函数；从真实现代配置读theta/partial factor，用临时config副本传给原函数；重复安装幂等、第三方覆盖/非法值/未知scaled schema拒绝 | 不给所有Mimi硬加property、不写死10000、不修改权重/config文件、不假称修复所有5.x版本 |
| Worker/原生/CPU编码/训练 | 导入Qwen后、加载模型前安装桥；保留原Base/LoRA、现有码/授权与质量标志 | 其他未见过的真实模型错误仍可能出现；实际完整加载须再运行 |
| 预检 | 新`qwen_mimi_rope_cpu`：实际MimiConfig、实际Qwen默认函数的CPU数学smoke，明确NO model/GPU；HF/官方provider检查可区分命名空间 | 解决此前只验签名而漏配置错误的缺口，但不能把smoke当完整模型通过 |
| 依赖 | 固定faster0.5.4 / qwen-tts-hf0.1.1.post1 / TF5.20.2三个直接版本；安装时对已装Torch/torchaudio/torchvision加版本约束；缺平台Torch拒绝替换；官方/HF重叠命名空间拒绝 | 不是完整环境锁，不保证Kaggle所有现有包无冲突；不强制升级/卸载CUDA库或照装沙箱Torch |
| fatal控制 | 已知rope_theta AttributeError及明确兼容异常标fatal；supervisor停止该worker重试，并原子写当前启动nonce绑定的失败记录 | transient错误仍保留有界重试；不按旧日志PID或模糊名称盲杀 |
| bootstrap清理 | 看见fatal健康/当前nonce收据立即结束等待；失败/异常/中断时只停止自己创建的supervisor Popen；等待其正常清理直接children和FD | 45秒未确认会明确要求停止完整Kaggle会话，不删除锁或假称所有GPU已空闲 |
| 会话驻留 | 默认QTTS_RESIDENT=1，保留每worker单GPU0/1映射；不在600次请求或旧13.5GB门槛主动回收模型，显存高只告警；显式0保留旧策略 | CUDA empty_cache不释放活模型权重；OOM、真实错误/服务重启/平台回收仍可打断，不保证永久会话 |
| health | requested_model、model_loaded、cuda_visible_devices、fatal_error、residency_policy | Mock明确不报真实model_loaded，requested_model不是权重内容签名；不把GPU映射配置说成现场模型成功 |

## 3. 交付与验证

- step12：`kaggle/kaggle-fixed-step12.py`，282031字节/47资产，SHA256 `2be33a3a6735639ce32ec8750e9a489abd96e4daa780d068557f2b0156f2de08`，独立包与source_manifest_step12.json。原始至step11冻结。
- 浏览器复制预览3001已换step12，代码和下载来自固定hash的完整包，不动原3000工作台及15文件/HEAD。
- 新14项兼容/控制/驻留/安装约束回归已通过；完整Python267×3=801 PASS，含原有训练/实际CPU小网络Gloo、访问控制、存储、包与adapter回归；Node30×3及Go race count3 PASS。
- 既有所有权真实进程/HTTP输入/本机码CLI/Mock管线/Go+SSE+双worker adapter替身各三轮PASS。新增真实supervisor+CPU fatal-health进程三轮，验证当前nonce收据、bootstrap提前失败、所属supervisor及worker退出、PID运行标记移除；不是GPU实验。均非真实Qwen/NCCL/DeepSeek联网；不把已有CPU链路替身算作GPU重载。
- 真实wheel配置数学三进程PASS；完整浏览器113×3=339 PASS，另最终step12包逐字节复制三轮PASS。真实Chromium复制页三轮剪贴板精确一致、下载文件名/内容哈希一致、拒绝授权时全选/手机375px无横向溢出、正式15文件不变，详见copy-page.json与final-checks.json。
- 三轮各100条建议/目标复审见review-map.json。完整目标仍22/300；11题550建议不等于550实现或300修复。当前只新增用户真实双T4识别/加载失败证据，不升级目标推理/质量项。

## 4. 保留的失败与未执行内容

- 首次独立CPU target环境同时存在旧tokenizers/hub dist-info，TF版本检查拒绝；删除该隔离cache中的旧元数据后，真实CPU复现与修复通过，初始错误日志保留。未修改主测试venv或用户Torch。
- 完整Python初轮267中1失败：旧native探针测试强制要求官方qwen-tts发行包，实际HF provider也可提供命名空间。改为显式provider组门禁及对应断言，随后完整三轮通过；初始失败日志保留。
- 新fatal进程脚本初次漏传子进程PYTHONPATH导致找不到supervisor模块；修正测试环境后实际三轮通过，初始日志保留，不是生产模型故障。
- 沙箱CUDA不可用，没有实际两T4或完整模型权重，完整Qwen导入/加载、warmup、声音、峰值显存和性能仍须用户新包复跑。配置层成功不是整个模型已保证可运行。

## 5. 给用户的直接操作与下一门禁

见KAGGLE_STEP12_QUICKSTART.md。先备份所需私有数据，再停止并重新启动**完整Kaggle会话**，不是只重启内核/刷新网页；默认T4×2/Internet On/非Mock，从浏览器step12完整复制。禁止继续同时运行step11或拿日志PID1589盲杀。

重新运行应先看到配置smoke通过，再两worker完成模型加载/warmup及workers_healthy=2，最后真实短句听音/长文本/打断与显存。下一项是实际目标复跑，不再插入工具准备阶段。

**“永久部署在双卡里面”不能在Kaggle保证。** 能实现并已编码的是健康模型在会话存活期间每卡一份常驻；会话结束/配额到期/机器回收后显存消失，磁盘/私有Dataset权重缓存不是GPU继续运行。长期服务需要可持续双GPU服务器与运维预算，本次未采购/部署外部硬件或绕过平台限制。

- 独立复制检查器首次Chromium启动SIGSEGV，尚未进入页面；保留copy-page-initial-browser-error.txt。随后Playwright最终复制三轮及独立检查器真实剪贴板/下载三轮均PASS；未改生产代码，启动异常根因未确定，不隐去失败记录。

---

## 内嵌备忘录：KAGGLE_STEP12_QUICKSTART.md

# step12：修复你现场的Mimi/RoPE加载错误

这是实际修复包，不是让你继续运行出错的step11。浏览器“复制 Kaggle 修复版完整代码（step12）”已换成`kaggle-fixed-step12.py`。

## 你现在怎么做

1. **先备份自己需要的参考音频、转写、已训练adapter及日志**，不要把API Key/Token发到聊天或共享输出。
2. Kaggle中先停止当前运行，再用平台的**停止会话/重新启动完整会话**操作，确认原监督器与GPU进程已结束。**仅停止一个单元格、刷新网页或重启Python内核不一定停止已分离的旧supervisor。** 不要用日志里的1589盲杀，也不要删除GPU锁来抢占。
3. 新会话选GPU T4 ×2、Internet On；进入浏览器复制页，确认标题/文件名是 **step12**，点击“复制全部代码”，替换旧启动单元格的全部内容再运行。不要同时运行step11。若平台保留了旧工作目录并提示旧supervisor.pid，仍不要盲删或按旧PID杀进程；在确认完整会话已重启后可用全新QTTS_ROOT目录启动，旧数据另行备份/管理。
4. 默认就是Qwen/Qwen3-TTS-12Hz-1.7B-Base，每worker一张GPU。默认`QTTS_RESIDENT=1`为健康模型会话内常驻，不需要另写训练命令或启用adapter模式来解决本次加载错误。环境中若留有`QTTS_MOCK=1`应先去掉/设为0；默认高速后端为`QTTS_TTS_ENGINE=faster`。
5. 依赖阶段审查并固定`faster-qwen3-tts==0.5.4`、`qwen-tts-hf==0.1.1.post1`、`transformers==5.20.2`。若需安装，会用当前Torch/torchaudio/torchvision版本作为约束，避免无条件替换平台CUDA栈。若发生命名空间冲突/安装冲突，会拒绝而不是静默卸载Torch。**不要仅执行pip install transformers<5**，这违反faster0.5.4依赖。
6. 预检应出现`qwen_mimi_rope_cpu`通过；这只是实际配置数学检查，**不是模型加载成功**。然后应看到两个worker完成模型加载及warmup、workers_healthy=2，才进入网页短句合成/实际试听。
7. 如果仍报错，需看本次`worker0.out/worker1.out`末尾的完整异常链及新预检结果。确定性兼容错误现在会停止该worker重试，并让启动流程清理其创建的supervisor，不应继续无意义循环加载。清理45秒未确认时必须按平台停止整个会话，不能认为锁已释放。

## 修了什么

实际Qwen-HF默认RoPE函数仍读取旧`config.rope_theta`，Transformers5.20.2 Mimi已使用`config.rope_parameters['rope_theta']`。新桥接只针对已识别的Qwen默认函数，从实际配置读theta、给临时副本提供旧字段，保持原配置/权重不动。10000、12345、1000000三个theta的真实Mimi配置CPU数值已核对；未知类型/缩放/非法参数不猜值。

默认不再每600次请求重载模型，也不因旧13.5GB门槛主动重启；显存高会告警，空闲缓存清理不释放活模型权重。可显式`QTTS_RESIDENT=0`回到旧周期回收策略。模型异常、OOM、服务重启或平台回收仍可能打断驻留，不承诺16GBfit、质量或时延。

## 不能承诺“永久部署在双卡”

应用能控制的是**会话存活且模型健康时，每张GPU保留一份模型**。Kaggle会话到期、配额用尽、关机或GPU回收后，显存必然丢失；磁盘权重/私有Dataset备份不等于模型继续驻留GPU。

真正长期常驻需要你拥有可持续运行的双GPU服务器和相应运维/预算。本次没有替你采购或部署外部服务器，也不绕过Kaggle限制。

## 现场验收还没完成

你提供的日志已经证明两张T4被识别、编译/下载阶段完成并到达模型加载；同时明确证明当时加载失败。修复已在CPU重现并验证该配置异常，但沙箱没有T4或完整Qwen权重，不能代替你新版本的模型重载、显存/实际声音验收。需要重新运行step12后才能进一步确认。

---

## 内嵌备忘录：KAGGLE_STEP13_PLAN.md

# 第十三阶段计划：修复Faster延迟导入导致RoPE补丁未安装

先计划/问题12的50条建议，再实现；不向用户重复提问。

## 现场事实与根因路径
step12在两T4上再次以同一MimiConfig.rope_theta失败。预检明确显示HF5模块未加载却给warning。真实faster0.5.4顶层只导出包装类，直到from_pretrained内部第194行才导入qwen_tts；step12仅查sys.modules，过早not_applicable。此前真实wheel函数CPU实验验证了桥接数学，却没有验证真实包导入生命周期，此缺口必须修正，不能归因用户操作。

## 实施顺序
1. 冻结原始至step12；新step13整包，不覆盖历史证据。
2. 基于安装发行元数据区分HF与官方legacy。HF先检查受审版本/命名空间冲突，再显式importlib.import_module导入实际compat模块，验证注册并安装补丁；不能用“尚未导入”等同“不适用”。未知/导入失败明确阻断。
3. HF runtime预检必须完成真实Mimi CPU数学smoke；legacy不强行依赖HF5。所有模型入口继续复用同一桥接函数。
4. 新增延迟导入、导入失败、冲突、重入幂等、预检fail-closed测试；真实Faster和完整Qwen包不替换导入函数，CPU构造微型MimiModel走真实_init_weights路径，不下载完整模型/不冒充T4。
5. 三轮Python/Node/Go及协议、完整浏览器，实际包导入+微型Mimi三进程；保留初始失败。三轮各100项范围复核，不把目标22/300改成全部实现。
6. 更新真实复制页/完整交付/33备忘录与12题600建议；验证原始至step12和正式工作台只读不变。

## 验收与边界
HF存在但compat未载入不能再跳过。成功要求step13 CPU真实包导入后桥接installed、实际Mimi实例初始化成功，及既有功能回归通过。真实双T4完整1.7B加载、CUDA graph、显存和声音仍需Kaggle实跑；无法保证平台永久驻留。下一步应直接复跑step13，非要求用户再做准备开发。

---

## 内嵌备忘录：KAGGLE_STEP13_AUDIT.md

# 第十三阶段审查：真实导入生命周期修复

## 结论与责任边界

step12在用户Kaggle两T4上仍失败，不能称已修好。原因不是用户没按步骤，而是我们上一版补丁只查sys.modules，没有覆盖Faster实际延迟导入。此前wheel函数数学通过只说明桥接算法有效，无法证明生产入口安装了补丁。此缺口已明确纳入本阶段回归。

## 实际来源与复现

- 受审真实faster0.5.4 wheel顶层导入model/ggml包装类；model.py第194行在from_pretrained内部才from qwen_tts import Qwen3TTSModel。
- 真实HF0.1.1.post1父包导入时注册旧default RoPE。TF5.20.2 _init_weights的ROPE_INIT_FUNCTIONS会覆盖Mimi自带现代默认计算器，导致读取旧rope_theta。
- 来源哈希/导入行见reviewed-import-sources.json。CPU隔离环境正常导入完整Faster，确认Qwen尚未载入；执行冻结step12实际兼容源，返回not_applicable；再正常导入完整Qwen并构造真实微型Mimi，复现与用户一致AttributeError。见real-import-baseline.json，不伪造第三方导入。

## 实施

1. install_qwen_rope_bridge以发行元数据判别HF/legacy，HF先检查版本/命名空间冲突，再显式正常importlib.import_module加载实际compat（及其父包），随后验证并桥接注册函数。未知组合/导入异常/元数据矛盾拒绝；legacy仍无须HF。
2. 保留窄范围bridge和实际theta临时副本，不改配置/权重，不猜默认值，不盲降TF4，不变更平台Torch/CUDA约束。
3. qwen_configuration_check要求installed且数学smoke明确True；HF存在却跳过或不完整时blocked/required=True。只有真正未安装HF的legacy路径可不适用。
4. Worker/native adapter/CPU编码/训练仍在构造前共用同一桥接；驻留、fatal nonce及所属进程清理保持。不增加导入钩子，不绕过验证来消除报错。
5. 新增6项回归：尚未导入时HF显式导入；导入失败；版本/冲突先行拒绝；已载HF缺发行元数据；HF skipped/incomplete smoke阻断；官方legacy保持可选。旧GPU/API/CPU编码替身测试明确模拟其兼容边界，不能伪造全局发行元数据后误称真实包通过。

## 更强的真实CPU验证（不是完整1.7B模型验收）

lazy_rope_import_check.py不替换第三方导入、不下载模型，禁网且HF离线；从真实Faster未载Qwen状态调用生产安装函数，再正常导入完整Qwen，实际TF MimiModel构造2651参数微型随机模型、本地保存后from_pretrained重载。10000/12345/1000000三theta均校验实际rotary缓冲、配置不变、参数finite；实际初始化进入桥接12次。完整Qwen包导入不等于完整Qwen模型构造/加载。这里GPU执行为False、完整Qwen模型加载为False。

额外正常运行真实backend_probe隔离CLI三轮：HF数学smoke均required=True且pass；沙箱无CUDA，整体报告blocked（符合预期），未把该报告当作目标GPU预检通过。见real-preflight-cpu-round1..3.json。

主venv未装这些第三方包；隔离依赖置/home/user/.cache/qtts-step13-site与既有step12-site，不入Git。SoX二进制缺失有警告，本实验未调用其音频功能，不假称通过SoX音频转换。

## 验证状态

最终三轮：Python273×3=819 PASS，Node30×3=90 PASS，Go race count3 PASS；资源所有权真实进程/HTTP训练输入/本地码CLI/Mock管线四脚本各执行3次（每次内置3轮，共各9轮）、adapter真实Go+SSE+双worker CPU小LoRA替身三轮、fatal真实supervisor+CPU worker三轮PASS。

完整浏览器114×3=342 PASS（11.4分钟），另最终step13整包逐字节复制三轮PASS。3001独立复制页真实Chromium三轮剪贴板/下载完整哈希一致、授权拒绝全选、375px手机无横向溢出、正式15文件不变，见copy-page.json。不是用HTTP读取代码冒充剪贴板验收。

最终交付门禁见docs/validation/step13/final-checks.json；三轮各100项不重复定向开发建议与保留目标ID见review-map.json，完整目标仍22/300；12题600建议不等于600修复。

## 初始失败保留

- 新完整包隔离环境首次缺scipy、随后缺cloudpickle等依赖；仅补隔离验证依赖，未修改主venv/生产版本组合。日志real-import-initial.txt/attempt2/依赖日志留存。
- 微型Mimi首次测试断言误以为TF5旋转模块有rope_init_fn字段；实际是默认静态方法+_init_weights registry。修正验证为实际inv_freq/original_inv_freq和函数profile计数，保留real-import-initial-modelassert.txt；不是以不核对频率的方式忽略错误。
- 完整273测试初轮1错误：CPU编码器旧替身把所有发行元数据伪造成stub-only，触发真实namespace冲突。测试明确隔离模拟legacy兼容路径；生产版本/冲突拒绝未削弱。初始日志python-initial.txt保留。

## 下一现场门禁

发布完整step13、只读复制页，旧原始至12冻结。先备份需要的私有数据，再停止并重启完整Kaggle会话，T4×2/Internet/非Mock默认faster，预检必须通过qwen_mimi_rope_cpu，然后看两worker实际完成加载/预热，再短句试听。当前没有真实T4/完整权重，不能保证下一次必成、显存fit、性能、音质或永久Kaggle；有新异常需按实际链路继续修复，不能报成功掩盖。

## 当前交付完整性

step13：282346字节/47资产，SHA256 dad142d75be94d8efb6567fc1f8755d3f37341a65d5c7fe9454fd36c87770e60；source_manifest逐项校验和repack --check可重现。原始至12包冻结，正式3000工作台HEAD/15文件1043155B不变，33备忘录完整内嵌。

---

## 内嵌备忘录：KAGGLE_STEP13_QUICKSTART.md

# step13：修复你现场的Mimi/RoPE加载错误

这是修复step12补丁因延迟导入而跳过的新包，不是让你继续运行已失败的step12。浏览器“复制 Kaggle 修复版完整代码（step13）”已换成`kaggle-fixed-step13.py`。

## 你现在怎么做

1. **先备份自己需要的参考音频、转写、已训练adapter及日志**，不要把API Key/Token发到聊天或共享输出。
2. Kaggle中先停止当前运行，再用平台的**停止会话/重新启动完整会话**操作，确认原监督器与GPU进程已结束。**仅停止一个单元格、刷新网页或重启Python内核不一定停止已分离的旧supervisor。** 不要用旧日志里的PID盲杀，也不要删除GPU锁来抢占。
3. 新会话选GPU T4 ×2、Internet On；进入浏览器复制页，确认标题/文件名是 **step13**，点击“复制全部代码”，替换旧启动单元格的全部内容再运行。不要同时运行step12。若平台保留了旧工作目录并提示旧supervisor.pid，仍不要盲删或按旧PID杀进程；在确认完整会话已重启后可用全新QTTS_ROOT目录启动，旧数据另行备份/管理。
4. 默认就是Qwen/Qwen3-TTS-12Hz-1.7B-Base，每worker一张GPU。默认`QTTS_RESIDENT=1`为健康模型会话内常驻，不需要另写训练命令或启用adapter模式来解决本次加载错误。环境中若留有`QTTS_MOCK=1`应先去掉/设为0；默认高速后端为`QTTS_TTS_ENGINE=faster`。
5. 依赖阶段审查并固定`faster-qwen3-tts==0.5.4`、`qwen-tts-hf==0.1.1.post1`、`transformers==5.20.2`。若需安装，会用当前Torch/torchaudio/torchvision版本作为约束，避免无条件替换平台CUDA栈。若发生命名空间冲突/安装冲突，会拒绝而不是静默卸载Torch。**不要仅执行pip install transformers<5**，这违反faster0.5.4依赖。
6. 预检必须出现`qwen_mimi_rope_cpu`通过；HF发行包已安装时不允许“compatibility module not loaded”警告后继续启动。这只是实际配置数学检查，**不是模型加载成功**。然后应看到两个worker完成模型加载及warmup、workers_healthy=2，才进入网页短句合成/实际试听。
7. 如果仍报错，需看本次`worker0.out/worker1.out`末尾的完整异常链及新预检结果。确定性兼容错误现在会停止该worker重试，并让启动流程清理其创建的supervisor，不应继续无意义循环加载。清理45秒未确认时必须按平台停止整个会话，不能认为锁已释放。

## 修了什么

step12只检查sys.modules，Faster直到from_pretrained才导入Qwen，因此补丁没装上。本次先用发行元数据判断HF存在，版本/namespace检查后显式正常导入完整Qwen兼容模块，再桥接；导入失败/数学检查不完整均阻断。实际完整包+微型Mimi本地保存重载离线CPU三进程验证，不再只测试手动加载的单个函数。


实际Qwen-HF默认RoPE函数仍读取旧`config.rope_theta`，Transformers5.20.2 Mimi已使用`config.rope_parameters['rope_theta']`。新桥接只针对已识别的Qwen默认函数，从实际配置读theta、给临时副本提供旧字段，保持原配置/权重不动。10000、12345、1000000三个theta的真实Mimi配置CPU数值已核对；未知类型/缩放/非法参数不猜值。

默认不再每600次请求重载模型，也不因旧13.5GB门槛主动重启；显存高会告警，空闲缓存清理不释放活模型权重。可显式`QTTS_RESIDENT=0`回到旧周期回收策略。模型异常、OOM、服务重启或平台回收仍可能打断驻留，不承诺16GBfit、质量或时延。

## 不能承诺“永久部署在双卡”

应用能控制的是**会话存活且模型健康时，每张GPU保留一份模型**。Kaggle会话到期、配额用尽、关机或GPU回收后，显存必然丢失；磁盘权重/私有Dataset备份不等于模型继续驻留GPU。

真正长期常驻需要你拥有可持续运行的双GPU服务器和相应运维/预算。本次没有替你采购或部署外部服务器，也不绕过Kaggle限制。

## 现场验收还没完成

你提供的日志已经证明两张T4被识别、编译/下载阶段完成并到达模型加载；同时明确证明当时加载失败。修复已在CPU重现并验证该配置异常，但沙箱没有T4或完整Qwen权重，不能代替你新版本的模型重载、显存/实际声音验收。需要重新运行step13后才能进一步确认。

---

## 内嵌备忘录：KAGGLE_STEP14_REVIEW1.md

# 第十四阶段第1轮审查：100条定向建议

审查覆盖全部源文件的结构/哈希，重点为本轮主题。建议不是已实现清单；实现/保留/待硬件与未完成见STEP14审查处置。

1. [S14-R1-001] 连续录音：将239秒上限与十分钟需求对齐。
2. [S14-R1-002] 连续录音：同时扩大分块数量预算。
3. [S14-R1-003] 连续录音：保留累计字节上限。
4. [S14-R1-004] 连续录音：用虚拟时钟测试十一分钟。
5. [S14-R1-005] 连续录音：停止后才保存有效片段。
6. [S14-R1-006] 连续录音：取消权限晚返回仍关闭设备。
7. [S14-R1-007] 连续录音：禁止空录音提交。
8. [S14-R1-008] 连续录音：保留失败本地片段。
9. [S14-R1-009] 连续录音：显示连续录音最大时长。
10. [S14-R1-010] 连续录音：不把后台计时器当精确音频时钟。
11. [S14-R1-011] 上传预算：同步浏览器与服务端时长。
12. [S14-R1-012] 上传预算：同步客户端与服务端单文件字节。
13. [S14-R1-013] 上传预算：保留整请求总量门禁。
14. [S14-R1-014] 上传预算：保留未知长度流式门禁。
15. [S14-R1-015] 上传预算：原始库独立容量核对。
16. [S14-R1-016] 上传预算：PCM长音频预先计算空间。
17. [S14-R1-017] 上传预算：不把提高秒数等同无限上传。
18. [S14-R1-018] 上传预算：拒绝超过上限而不静默截断。
19. [S14-R1-019] 上传预算：给出明确限额中文提示。
20. [S14-R1-020] 上传预算：加入长WAV完整长度回归。
21. [S14-R1-021] 训练入口：明确参考处理不训练。
22. [S14-R1-022] 训练入口：明确快照不执行优化器。
23. [S14-R1-023] 训练入口：真实训练保留独立确认。
24. [S14-R1-024] 训练入口：不开虚假开始训练按钮。
25. [S14-R1-025] 训练入口：网页训练需独立CPU控制面。
26. [S14-R1-026] 训练入口：训练时停止两GPU推理而非争显存。
27. [S14-R1-027] 训练入口：控制面不能随analyst一起关闭。
28. [S14-R1-028] 训练入口：完成后再恢复原声音服务。
29. [S14-R1-029] 训练入口：取消要等待两个rank退出。
30. [S14-R1-030] 训练入口：未实现端到端入口须明示未完成。
31. [S14-R1-031] 长录音切分：训练不能把十分钟当单条序列。
32. [S14-R1-032] 长录音切分：优先审核ASR时间戳。
33. [S14-R1-033] 长录音切分：不得用均分文本猜对齐。
34. [S14-R1-034] 长录音切分：不得裁去超预算文本。
35. [S14-R1-035] 长录音切分：保留原始音频。
36. [S14-R1-036] 长录音切分：生成独立可审核短WAV。
37. [S14-R1-037] 长录音切分：保留每段来源起止秒。
38. [S14-R1-038] 长录音切分：同一说话人须明确声明。
39. [S14-R1-039] 长录音切分：片段过短需要拒绝或重新切分。
40. [S14-R1-040] 长录音切分：完整语义覆盖要逐项记录。
41. [S14-R1-041] 转写：逐条训练文本对应逐条音频。
42. [S14-R1-042] 转写：ASR提案不能标为人工已核验。
43. [S14-R1-043] 转写：禁止将参考文本套用全部片段。
44. [S14-R1-044] 转写：Unicode转写保持原值。
45. [S14-R1-045] 转写：空转写拒绝。
46. [S14-R1-046] 转写：转写字符总预算保留。
47. [S14-R1-047] 转写：不能凭训练loss证明读音正确。
48. [S14-R1-048] 转写：方言专名需要真实试听。
49. [S14-R1-049] 转写：训练前审核标点断句。
50. [S14-R1-050] 转写：保留来源转写hash。
51. [S14-R1-051] 数据完整性：继续固定manifest hash。
52. [S14-R1-052] 数据完整性：继续拒绝软链接。
53. [S14-R1-053] 数据完整性：继续拒绝硬链接。
54. [S14-R1-054] 数据完整性：样本目录不得路径穿越。
55. [S14-R1-055] 数据完整性：源库删除不等于训练副本删除。
56. [S14-R1-056] 数据完整性：训练时持有读取租约。
57. [S14-R1-057] 数据完整性：保留授权确认。
58. [S14-R1-058] 数据完整性：失败不覆盖旧模型。
59. [S14-R1-059] 数据完整性：保留独立引用参考上限。
60. [S14-R1-060] 数据完整性：不自动上传私人录音到第三方。
61. [S14-R1-061] 格式：浏览器WebM不能改后缀冒充WAV。
62. [S14-R1-062] 格式：真实解码后再重采样。
63. [S14-R1-063] 格式：保持24k单声道PCM16训练契约。
64. [S14-R1-064] 格式：解码时检查完整时长。
65. [S14-R1-065] 格式：解码异常不当成功。
66. [S14-R1-066] 格式：训练长样本切分应在编码前。
67. [S14-R1-067] 格式：统一参考不使用整段十分钟。
68. [S14-R1-068] 格式：不随意降采样谋求提速。
69. [S14-R1-069] 格式：保留nonfinite检测。
70. [S14-R1-070] 格式：输出格式与模型codec契约一致。
71. [S14-R1-071] 并发输入：限制同时解码任务。
72. [S14-R1-072] 并发输入：限制总驻留音频内存。
73. [S14-R1-073] 并发输入：不要每个音频开无限线程。
74. [S14-R1-074] 并发输入：保护ASR共享模型状态。
75. [S14-R1-075] 并发输入：采集线程不承担模型训练。
76. [S14-R1-076] 并发输入：上传回调必须检查当前页面代次。
77. [S14-R1-077] 并发输入：锁定时清空私人转写。
78. [S14-R1-078] 并发输入：晚响应不能恢复已锁定界面。
79. [S14-R1-079] 并发输入：请求取消不等于后台计算结束。
80. [S14-R1-080] 并发输入：并发变更需修订号核对。
81. [S14-R1-081] 浏览器布局：保留两个主要视图。
82. [S14-R1-082] 浏览器布局：训练说明放声音库辅助区。
83. [S14-R1-083] 浏览器布局：长录音状态不能溢出手机宽度。
84. [S14-R1-084] 浏览器布局：保留键盘停止操作。
85. [S14-R1-085] 浏览器布局：录音按钮不能重复启动。
86. [S14-R1-086] 浏览器布局：麦克风波形不能伪造。
87. [S14-R1-087] 浏览器布局：显示准备与实际训练区别。
88. [S14-R1-088] 浏览器布局：为长录音显示时间预算。
89. [S14-R1-089] 浏览器布局：文案不能承诺真人完全一致。
90. [S14-R1-090] 浏览器布局：继续可复制完整Kaggle代码。
91. [S14-R1-091] 验收：保留step13启动成功现场证据。
92. [S14-R1-092] 验收：新包冻结旧版本。
93. [S14-R1-093] 验收：新增十一分钟虚拟录音测试。
94. [S14-R1-094] 验收：物理麦克风仍单独验收。
95. [S14-R1-095] 验收：真实十分钟数据不能用零信号替代质量验收。
96. [S14-R1-096] 验收：保护正式工作台文件。
97. [S14-R1-097] 验收：记录本轮未完成项。
98. [S14-R1-098] 验收：记录训练覆盖而非样本总数猜测。
99. [S14-R1-099] 验收：只有实际执行才标训练通过。
100. [S14-R1-100] 验收：三轮验证证据分开保存。

---

## 内嵌备忘录：KAGGLE_STEP14_REVIEW2.md

# 第十四阶段第2轮审查：100条定向建议

审查覆盖全部源文件的结构/哈希，重点为本轮主题。建议不是已实现清单；实现/保留/待硬件与未完成见STEP14审查处置。

1. [S14-R2-001] 张量准备：找出每epoch重复文本tokenize。
2. [S14-R2-002] 张量准备：缓存必须有字节上限。
3. [S14-R2-003] 张量准备：缓存不改变token顺序。
4. [S14-R2-004] 张量准备：缓存返回值避免被调用者污染。
5. [S14-R2-005] 张量准备：超过缓存上限退回原计算。
6. [S14-R2-006] 张量准备：包含声学码形状校验。
7. [S14-R2-007] 张量准备：不缓存未通过预算的样本。
8. [S14-R2-008] 张量准备：保留统一参考mel。
9. [S14-R2-009] 张量准备：比对缓存前后collate张量。
10. [S14-R2-010] 张量准备：用调用次数而非GPU倍速声称改善。
11. [S14-R2-011] 优化器：保持全部联合loss。
12. [S14-R2-012] 优化器：保持0.3子talker系数。
13. [S14-R2-013] 优化器：保持训练样本顺序。
14. [S14-R2-014] 优化器：保持累积步分母。
15. [S14-R2-015] 优化器：保持不足一组累积的缩放。
16. [S14-R2-016] 优化器：保持AdamW权重衰减。
17. [S14-R2-017] 优化器：保持LoRA可训练参数。
18. [S14-R2-018] 优化器：保持FP32适配器。
19. [S14-R2-019] 优化器：不减少epoch作为无损提速。
20. [S14-R2-020] 优化器：记录真实optimizer step数。
21. [S14-R2-021] 双卡：保持两rank NCCL契约。
22. [S14-R2-022] 双卡：不让两rank同时用同一物理卡。
23. [S14-R2-023] 双卡：保持奇数样本补齐策略。
24. [S14-R2-024] 双卡：保持两rank参数摘要一致。
25. [S14-R2-025] 双卡：每epoch报告实际seen_ids。
26. [S14-R2-026] 双卡：不能把CPU Gloo当NCCL。
27. [S14-R2-027] 双卡：OOM后不得标完成。
28. [S14-R2-028] 双卡：不能用两个Python线程替代DDP。
29. [S14-R2-029] 双卡：显存峰值必须实测。
30. [S14-R2-030] 双卡：完成后保存适配器再报告。
31. [S14-R2-031] 同步开销：审查每参数grad finite读取。
32. [S14-R2-032] 同步开销：合并有限性检查到一次CPU读取。
33. [S14-R2-033] 同步开销：跨rank有限性继续一致。
34. [S14-R2-034] 同步开销：非有限梯度两rank一同跳过。
35. [S14-R2-035] 同步开销：保留梯度范数裁剪。
36. [S14-R2-036] 同步开销：不盲开find_unused_parameters=False。
37. [S14-R2-037] 同步开销：loss统计不删训练计算。
38. [S14-R2-038] 同步开销：不盲开torch.compile。
39. [S14-R2-039] 同步开销：不盲开TF32冒充T4原生支持。
40. [S14-R2-040] 同步开销：CUDA优化需独立目标机基准。
41. [S14-R2-041] 线程预算：按CPU配额而非文件数设置线程。
42. [S14-R2-042] 线程预算：两rank线程总数不能压满宿主。
43. [S14-R2-043] 线程预算：ASR线程与训练线程分开预算。
44. [S14-R2-044] 线程预算：限定预处理并发。
45. [S14-R2-045] 线程预算：避免每个worker再套大线程池。
46. [S14-R2-046] 线程预算：保留取消与超时。
47. [S14-R2-047] 线程预算：记录线程配置。
48. [S14-R2-048] 线程预算：默认不引入DataLoader多进程。
49. [S14-R2-049] 线程预算：小数据先消除重复计算。
50. [S14-R2-050] 线程预算：吞吐测试包含预处理成本。
51. [S14-R2-051] 模型依赖：保留已成功HF导入顺序。
52. [S14-R2-052] 模型依赖：继续执行RoPE强制smoke。
53. [S14-R2-053] 模型依赖：兼容HF发行元数据报告。
54. [S14-R2-054] 模型依赖：不强制卸载平台Torch。
55. [S14-R2-055] 模型依赖：不因训练改变默认推理后端。
56. [S14-R2-056] 模型依赖：T4继续FP16。
57. [S14-R2-057] 模型依赖：不启用仅Ampere支持的BF16。
58. [S14-R2-058] 模型依赖：完整权重来源必须固定。
59. [S14-R2-059] 模型依赖：禁止远程模型代码。
60. [S14-R2-060] 模型依赖：模型物化成本单独记录。
61. [S14-R2-061] 训练发布：不把缓存称adapter。
62. [S14-R2-062] 训练发布：必须真实更新参数。
63. [S14-R2-063] 训练发布：损坏adapter不得回退Base。
64. [S14-R2-064] 训练发布：候选不自动覆盖active。
65. [S14-R2-065] 训练发布：保留保存speaker向量。
66. [S14-R2-066] 训练发布：保留Base绑定。
67. [S14-R2-067] 训练发布：保留训练run来源。
68. [S14-R2-068] 训练发布：新进程重载另行验收。
69. [S14-R2-069] 训练发布：训练后试听不可省略。
70. [S14-R2-070] 训练发布：失败仍保留旧可用档案。
71. [S14-R2-071] 资源所有权：训练前必须排他获取两GPU。
72. [S14-R2-072] 资源所有权：不删除fleet锁抢资源。
73. [S14-R2-073] 资源所有权：不按旧PID杀进程。
74. [S14-R2-074] 资源所有权：保留继承FD证明。
75. [S14-R2-075] 资源所有权：保留nonce校验。
76. [S14-R2-076] 资源所有权：取消只终止所属Popen。
77. [S14-R2-077] 资源所有权：进程退出不等于所有孩子退出。
78. [S14-R2-078] 资源所有权：父进程被杀需释放子进程。
79. [S14-R2-079] 资源所有权：网关与训练控制分离才可网页操作。
80. [S14-R2-080] 资源所有权：不能为一键训练绕过锁。
81. [S14-R2-081] 性能证据：记录端到端训练墙钟。
82. [S14-R2-082] 性能证据：记录加载时间。
83. [S14-R2-083] 性能证据：记录tokenizer调用次数。
84. [S14-R2-084] 性能证据：记录缓存驻留字节。
85. [S14-R2-085] 性能证据：记录优化器更新量。
86. [S14-R2-086] 性能证据：记录CPU线程占用。
87. [S14-R2-087] 性能证据：记录GPU显存峰值。
88. [S14-R2-088] 性能证据：相同数据和seed做A/B。
89. [S14-R2-089] 性能证据：相同loss路径比较参数。
90. [S14-R2-090] 性能证据：无真实基准不写最快。
91. [S14-R2-091] 回归：保留CPU tiny LoRA重载。
92. [S14-R2-092] 回归：保留两进程Gloo测试。
93. [S14-R2-093] 回归：新增缓存等价性测试。
94. [S14-R2-094] 回归：新增缓存淘汰测试。
95. [S14-R2-095] 回归：新增调用者变更隔离测试。
96. [S14-R2-096] 回归：新增HF训练报告发行检查。
97. [S14-R2-097] 回归：新增梯度finite聚合测试。
98. [S14-R2-098] 回归：原CLI拒绝fixture继续有效。
99. [S14-R2-099] 回归：三轮完整Python不是只跑新测试。
100. [S14-R2-100] 回归：逐项登记未实测硬件项。

---

## 内嵌备忘录：KAGGLE_STEP14_REVIEW3.md

# 第十四阶段第3轮审查：100条定向建议

审查覆盖全部源文件的结构/哈希，重点为本轮主题。建议不是已实现清单；实现/保留/待硬件与未完成见STEP14审查处置。

1. [S14-R3-001] 文本链路：定位CleanDelta删除内容。
2. [S14-R3-002] 文本链路：避免每个delta独立清洗URL。
3. [S14-R3-003] 文本链路：朗读路径不补句号。
4. [S14-R3-004] 文本链路：保留中英混合原文。
5. [S14-R3-005] 文本链路：保留数字小数。
6. [S14-R3-006] 文本链路：保留引号。
7. [S14-R3-007] 文本链路：保留专有名词。
8. [S14-R3-008] 文本链路：不添加链接二字。
9. [S14-R3-009] 文本链路：分段连接按规范比较输入。
10. [S14-R3-010] 文本链路：模型声学错字另行核验。
11. [S14-R3-011] 呼吸：默认关闭额外呼吸注入。
12. [S14-R3-012] 呼吸：不以合成噪声冒充真人吸气。
13. [S14-R3-013] 呼吸：保留可选真实参考呼吸。
14. [S14-R3-014] 呼吸：无真实片段时保持安静。
15. [S14-R3-015] 呼吸：不放大短促噪声。
16. [S14-R3-016] 呼吸：保留淡入淡出防爆音。
17. [S14-R3-017] 呼吸：呼吸增益需试听。
18. [S14-R3-018] 呼吸：模型自身呼吸与后加呼吸区分。
19. [S14-R3-019] 呼吸：不盲目滤掉全部气声。
20. [S14-R3-020] 呼吸：去噪不得削掉辅音。
21. [S14-R3-021] 首声：区分模型首块与可听首声。
22. [S14-R3-022] 首声：不把前置静音算有效语音。
23. [S14-R3-023] 首声：修正trimmer前计时。
24. [S14-R3-024] 首声：保留实际首播测量。
25. [S14-R3-025] 首声：分段过短影响韵律须权衡。
26. [S14-R3-026] 首声：小chunk需实机核验。
27. [S14-R3-027] 首声：不要用空PCM刷低首声。
28. [S14-R3-028] 首声：首段优先调度继续保留。
29. [S14-R3-029] 首声：录制到输出完整链路测量。
30. [S14-R3-030] 首声：无真实T4数据不承诺时延。
31. [S14-R3-031] 缓冲：不要无条件降低首播阈值。
32. [S14-R3-032] 缓冲：保留欠载预测。
33. [S14-R3-033] 缓冲：保留迟滞。
34. [S14-R3-034] 缓冲：区分首次启动与恢复。
35. [S14-R3-035] 缓冲：生成慢时继续积累。
36. [S14-R3-036] 缓冲：句级缓冲不能冒称声学流式。
37. [S14-R3-037] 缓冲：记录首PCM和首播放分别。
38. [S14-R3-038] 缓冲：测试短文本尾段可播放。
39. [S14-R3-039] 缓冲：停止后不能漏出迟到PCM。
40. [S14-R3-040] 缓冲：连续朗读不能丢段。
41. [S14-R3-041] 准确朗读：模型可能幻觉不能仅靠输入相等保证。
42. [S14-R3-042] 准确朗读：严格核验需整句缓存。
43. [S14-R3-043] 准确朗读：ASR核验增加首声等待。
44. [S14-R3-044] 准确朗读：ASR也不是绝对真值。
45. [S14-R3-045] 准确朗读：不符应拒绝或请求重试。
46. [S14-R3-046] 准确朗读：重试不改用户文本。
47. [S14-R3-047] 准确朗读：不自动补充解释。
48. [S14-R3-048] 准确朗读：多音字需目标语境测试。
49. [S14-R3-049] 准确朗读：真实试听列为门禁。
50. [S14-R3-050] 准确朗读：不承诺零错字。
51. [S14-R3-051] 调度：保护段索引顺序。
52. [S14-R3-052] 调度：失败只在未输出前重试。
53. [S14-R3-053] 调度：不可重复播放已输出语音。
54. [S14-R3-054] 调度：取消清除队列。
55. [S14-R3-055] 调度：监控两worker健康。
56. [S14-R3-056] 调度：资源锁不因低延迟绕过。
57. [S14-R3-057] 调度：调度公平性回归。
58. [S14-R3-058] 调度：背压不能无限堆积文本。
59. [S14-R3-059] 调度：native超时预算保留。
60. [S14-R3-060] 调度：默认faster启动不退化。
61. [S14-R3-061] 安全：口令只在内存。
62. [S14-R3-062] 安全：不输出密钥到诊断。
63. [S14-R3-063] 安全：预览用相对请求。
64. [S14-R3-064] 安全：只允许可信HTTPS。
65. [S14-R3-065] 安全：训练报告不含转写全文。
66. [S14-R3-066] 安全：不得自动发布私人样本。
67. [S14-R3-067] 安全：上传预算同步Go网关。
68. [S14-R3-068] 安全：锁定终止本地录音。
69. [S14-R3-069] 安全：锁定阻止晚响应。
70. [S14-R3-070] 安全：保留现有访问限制。
71. [S14-R3-071] 包与交付：原始至step13冻结。
72. [S14-R3-072] 包与交付：新step14整包重打。
73. [S14-R3-073] 包与交付：逐资产hash校验。
74. [S14-R3-074] 包与交付：完整剪贴板读回比对。
75. [S14-R3-075] 包与交付：下载内容逐字节比对。
76. [S14-R3-076] 包与交付：手机页面无横向溢出。
77. [S14-R3-077] 包与交付：拒绝剪贴板权限可全选。
78. [S14-R3-078] 包与交付：正式3000工作台不覆盖。
79. [S14-R3-079] 包与交付：复制页固定新hash。
80. [S14-R3-080] 包与交付：文档不把模拟当现场。
81. [S14-R3-081] 语言选择：Python保留模型编排。
82. [S14-R3-082] 语言选择：PyTorch算子执行已编译CUDA。
83. [S14-R3-083] 语言选择：Go保留网关调度。
84. [S14-R3-084] 语言选择：Rust保留DSP。
85. [S14-R3-085] 语言选择：JS保留浏览器采集播放。
86. [S14-R3-086] 语言选择：不为多语言引入额外网络跳转。
87. [S14-R3-087] 语言选择：不无依据重写C++算子。
88. [S14-R3-088] 语言选择：不引入Java服务增加驻留。
89. [S14-R3-089] 语言选择：不引入SQL保存密钥。
90. [S14-R3-090] 语言选择：类型与边界比语言数量重要。
91. [S14-R3-091] 三轮复核：三轮完整Python。
92. [S14-R3-092] 三轮复核：三轮Node文件服务。
93. [S14-R3-093] 三轮复核：Go race count3。
94. [S14-R3-094] 三轮复核：三轮完整浏览器。
95. [S14-R3-095] 三轮复核：三轮协议替身。
96. [S14-R3-096] 三轮复核：真实包Mimi三进程保持。
97. [S14-R3-097] 三轮复核：实际训练质量门禁仍未验。
98. [S14-R3-098] 三轮复核：记录所有初始失败。
99. [S14-R3-099] 三轮复核：汇总300建议处置而非全打勾。
100. [S14-R3-100] 三轮复核：交接提示词完整内嵌新增备忘录。

---

## 内嵌备忘录：KAGGLE_STEP14_PLAN.md

# 第十四阶段方案：长录音、无损训练计算优化、无额外呼吸/文本改写

## 已执行审查与自问自答
三轮审查各100条，见REVIEW1/2/3；全资产结构/哈希与重点链路审查记录见review-before.json，不是全代码无错证明。先问题13，再其50建议，再问题14及50建议，再问题15及50建议，详见DECISIONS。15题750建议，建议不等于已实现。

## 第一性原理与语言职责
录音时长是采集/解码/存储预算问题；训练吞吐是tokenize/数据准备/GPU计算与同步的瓶颈问题；音质取决于数据与模型，不取决于语言种类；准确播放涉及文本源、分段、模型生成、传输顺序与播放器。Python/PyTorch+编译CUDA做模型，Go做调度/传输，Rust/C做已有DSP，浏览器JS做采集播放。没有证据引入C++/Java/C#/SQL/R等重写能提高速度，不为语言数量增加复制和部署风险。

## 完整目标架构（未完成项必须保留）
1. 采集≤20分钟原件并保留，字节/块数/总时长独立门禁；原件不是十分钟单条训练样本。
2. ASR给出时间戳/逐条转写提案，人工审阅、同一说话人及授权确认；切1.5–16秒短样本，保证不猜测对齐、不截去正文，保持来源索引。训练序列超预算拒绝而不裁切。
3. 独立CPU训练控制面保持网页存活；维护态停止双GPU推理及analyst，确认全部孩子退出后才交接排他GPU租约；编码/真实双rank训练/进度/取消/失败收据；结束再恢复推理。当前supervisor退出同时关闭gateway，不能简单在analyst加线程就称网页一键训练完成。
4. 保持loss/优化器/顺序/样本覆盖；有界缓存消除重复tokenize、减少不必要CPU同步；真实T4记录端到端时间与显存后才能确定调参是否提速。
5. 默认不后加呼吸/合成噪声；声音本身的气声不可盲目滤掉。保留可选真实呼吸能力。
6. 默认实际会话不清洗文本、不补句号；输入文本一致不能证明声学无错字。严格逐句ASR核验后播放需要额外延迟，且仍需试听。保留原始低延迟播放并明确尚未自动声学校验。

## 本轮实际执行范围（不是全部目标已经完成）
A. 浏览器与服务端提升为20分钟采集预算、64MiB单文件/128MiB请求、独立块数/本地字节/总量限制，回归十一分钟虚拟时钟和长PCM解码。
B. 实现有界训练输入张量缓存/相同样本序列等价测试；聚合梯度finite检查而不改变联合loss/累积/裁剪；修复HF发行包训练报告版本查询。
C. 会话默认保留原文、不额外补句号；默认禁止后加呼吸（尤其合成噪声），保留显式真实参考呼吸选项；首块计时放在实际可输出语音后。
D. 原始至13冻结，发布14完整可复制包；三轮Python/Node/Go/browser/协议与真实包CPU回归、33+新增备忘录完整交接。

## 本轮不能打勾的目标
网页按钮→长录音自动逐条审校→独立控制面维护态→真实双T4训练→训练后自动部署尚未闭环；不增加只会报成功的假按钮。物理十分钟录音、真实训练质量/速度、首声改善、呼吸主观自然度及逐字声学准确率没有本机证据，不能承诺零错误、真人一样或最快。实际硬件才能解除这些门禁；本轮完成后必须明确报告仍未满足用户全部目标，而非“验收全部成功”。

## 长数据覆盖补充门禁

现有训练快照仍最多16条；若高质量切分产生更多片段，还需扩展受限分片/manifest与完整样本覆盖后才能全部入训，不能只选前16条冒充完整十分钟训练。

---

## 内嵌备忘录：KAGGLE_STEP14_AUDIT.md

# 第十四阶段审查：已实现边界与未完成门禁

## 不能写成“用户全部需求已完成”

| 需求 | 本轮代码/证据 | 尚未完成 |
|---|---|---|
| 连续十多分钟录音 | 约20分钟/8192块/64MiB单文件，服务端1200秒；11分钟虚拟控制与完整合成PCM解码验证 | 物理麦克风、休眠/后台冻结和真实长语音采集 |
| 保质提速 | 冻结step13真实CPU小LoRA A/B，loss/更新/参数逐位一致；重复tokenize从12次到3次 | Qwen/T4吞吐、峰值显存、相同数据训练音质A/B |
| 网页点击真实训练 | 原真实双rank训练CLI保留，快照明确不训练 | 独立CPU控制面、维护态租约交接、网页启动/取消/进度/恢复服务及训练后发布闭环 |
| 自然呼吸 | 默认不后加呼吸，reference模式只有真实片段，无合成噪声回退 | 模型自身气声、呼吸自然度与音色实听 |
| 首声更快 | 区分模型首块与裁边后首个非空PCM；可选首段chunk=2实验 | 未保证首播更快；真实T4端到端首播/欠载A/B |
| 文本完全一致 | 实际会话不再CleanDelta清理正文或补句号；多delta原文连接测试 | 没有逐句ASR核验/拒播闭环，不保证模型无漏字添字；纯标点/纯空白片段仍按旧规则过滤 |

step13用户现场已通过双T4加载/预热/ready门禁；不应再把此前双GPU启动说成完全未知。但上述新增目标仍不能从那次日志推出成功。

## 三轮审查/自问自答

REVIEW1/2/3各100条建议，完整源结构/哈希见review-before.json；重点逐链路审查，不宣称逐行无错或300项全部修复。问题13→50建议→问题14→50建议→问题15→50建议已按顺序记录。共15题750建议。处置表review-disposition.json区分本轮实现、原有回归保留、未闭环/待真实硬件；完整目标清单仍22/300。

## 具体改动

1. recorder默认1199000ms，8192 chunks，64MiB单文件、127MiB本地合计。UploadLimits默认1200秒单段、1800秒合计、128MiB请求、64MiB文件；Go上传上限同步128MiB，浏览器上传检查同步。原始库仍64MiB/库/512MiB总体，其他独立预算仍可先触发；不是无限录音或所有编码格式都能存满20分钟。上传超过限制拒绝，原件不截断。训练快照仍保留短段及序列预算，不能把长参考直接送入SFT。
2. TTSDataset深拷贝输入冻结调用者来源；64MiB有界CPU text/code tensor缓存，超过预算回退旧计算，不裁切不替换样本。返回clone避免缓存被调用者改坏，reference mel只读契约不变。run_rank保留逐样本准入，记录tokenizer_calls/cache_hits/cache_bytes。
3. 训练梯度finite flags在同一设备合并后一次host读取，跨rank collective与loss/accumulation/clipping/AdamW不变。HF/官方训练元数据查询兼容修复，不再在HF成功训练末尾查询不存在的官方发行包而报错。
4. Go实际newSession使用ExactSegCfg；不逐delta清洗markdown/URL/emoji、不合并内部空格、不添加句末标点。DefaultSegCfg/CleanDelta留给显式历史契约测试。不能因此说模型发音与文字已完全相同。
5. Worker默认QTTS_BREATH_MODE=off；reference模式只使用真实bank，空bank返回安静pause，删除合成breath噪声兜底。保留模型原声与淡入淡出，不盲滤气声/辅音。
6. model_first_chunk_ms与first_chunk_ms分别记录；后者从裁边后非空PCM才开始，不把被裁掉的空片段算首声。注意旧EdgeTrimmer在runaway静音时可放行静音并标异常，非空PCM不等于ASR确认的人声/真实首播。前端first_played与欠载保持，acoustic_text_verified=False。QTTS_FIRST_CHUNK_SIZE可选2..8，默认4不变，不通过降低播放器稳定阈值美化延迟。
7. 语言分工仍Python/PyTorch+CUDA、Go、Rust和浏览器JS；没有目标机数据就不引入新语言/自定义C++内核或高风险BF16/FA2/compile开关。

## 实验与证据

- test_step14新增12项：长解码/独立预算、录音≠训练、默认无呼吸、真实呼吸无噪声回退、非空PCM计时、缓存张量/优化器参数等价、字节上限/隔离、梯度finite/HF发行。
- training_cache_check.py加载冻结step13的真实训练与dataset源，不以重写基线代替。三独立CPU进程，每次同数据/seed，三epoch共6次optimizer更新，两路径loss与所有adapter tensor逐位一致；tokenizer调用12→3。只报告减少重复调用，fixture墙钟包含冷启动与执行顺序偏差，不能据此宣称端到端倍速或质量提高。
- 虚拟浏览器11分钟与2640块继续录音/约20分钟自动停止；合成660秒24k PCM解码长度完整。都不是真实麦克风/真人声音实验。
- 保留真实完整Faster/Qwen导入与微型Mimi构造/保存/重载三进程，保护已成功RoPE路径；不是Qwen1.7B训练或T4实验。
- 三轮完整Python285×3=855 PASS，Node30×3=90 PASS，Go race count3 PASS；资源所有权真实进程/输入HTTP/本地码CLI/Mock管线/Go+SSE+双worker adapter替身各三轮、fatal真实supervisor+CPU worker三轮PASS。
- 浏览器117×3=351 PASS（10.4分钟），最终step14整包逐字节复制另3 PASS。独立3001复制页真实Chromium三轮剪贴板/下载精确、授权拒绝全选/375px手机无横向溢出、正式15文件不变PASS。见copy-page.json与final-checks.json。
- 这些通过项仅覆盖实现范围，整体用户需求仍PARTIAL/BLOCKED。

## 初始记录

恢复会话后依赖缓存/venv不在，测试环境按现有测试锁恢复，未写进生产包/未改变Kaggle平台Torch。首个Go测试从仓库根运行找不到go.mod，改在真实go/gateway目录执行后通过；未改源码去适配错误目录。初检记录保留。全量失败若有，必须保留而不是只删测试。

## 下一步必须做而非继续虚报

优先实现网页训练的独立CPU控制面与维护态：网关/状态服务不能随GPU服务退出；停止并确认所有GPU持有者、传递可验证租约、固定实际数据/Base/码版本、真实两rank训练、受控取消/恢复、候选发布/明确切换。需要本地物化Base与审核过的逐段转写，不能猜这些信息或自动拿用户音频权利作假确认。真实首声、质量与声学一致性需相同参考/文本/种子A/B和试听，验收前本阶段整体需求状态为PARTIAL/BLOCKED，不得输出全部成功。

## 长数据覆盖补充门禁

现有训练快照仍最多16条；若高质量切分产生更多片段，还需扩展受限分片/manifest与完整样本覆盖后才能全部入训，不能只选前16条冒充完整十分钟训练。

## 最终交付

step14为285094字节/48资产，SHA256 73a02a95919406c4570ea563f0c0475fdde17535e6ccd16764c32514fce2c369；repack可重现，原始至13冻结，正式15文件/HEAD不变。39完整备忘录、300建议处置、15题750建议均有独立核验；不提升真实质量/性能门禁。

---

## 内嵌备忘录：KAGGLE_STEP14_QUICKSTART.md

# step14 使用与验收边界

这是部分功能修复交付，不是网页一键训练已完成。当前13已有实际双T4 ready日志；14新增功能仍需实机回归。

## 升级
1. 先自行备份需保留的私有原录音/转写/adapter。不要发口令或私人数据给聊天。
2. 在Kaggle停止并重启完整会话（不是只刷新网页/重启内核），避免旧supervisor/GPU进程冲突；不要按旧PID盲杀或删锁。
3. 从3001复制页确认step14，完整替换旧cell，T4×2/Internet/nonMock默认faster运行。仍保留受审HF/TF pins和强制RoPE检查，不需要另改Torch/CUDA。
4. 等两worker加载/预热ready，再解锁网页；仅看到网页不等于模型就绪。

## 长录音
默认约19分59秒自动停止（服务端单段1200秒），最大64MiB/段，16文件、请求128MiB、本地合计127MiB；原始库64MiB/库仍独立生效。块数8192，浏览器后台冻结/休眠仍可能中断，建议前台录制并及时备份。高码率原始WAV可能先达到字节限制，不能保证所有格式录满20分钟。

本地录音在创建档案/添加库前不是服务端持久保存。原始库不自动Dataset备份，清除本地片段/结束会话可能丢失。

## 训练不是“点参考处理”
现有网页的“处理参考”“输入快照”不执行优化器；本轮没有添加假训练按钮。真实训练仍使用train_tts.py双rank CLI，按KAGGLE_TRAINING_QUICKSTART.md准备可信本地Base和逐条对齐短WAV/转写后执行，先停止推理，不并抢双卡。长录音必须先按可信时间戳切短并审核，不可把整段10分钟送入max_sequence1024/2048或均分转写猜对齐。

本轮缓存/finite优化没有减少样本、epoch、联合loss或optimizer步数；CPU小模型逐位等价不代表真实Qwen训练质量/速度已验收。网页训练控制面/取消/恢复/自动部署仍待实现，见STEP14_PLAN/AUDIT。

## 呼吸、正文、首声
- 默认不后加呼吸噪声；模型自身的呼吸仍保留。QTTS_BREATH_MODE=reference可显式使用真实参考片段，无片段不合成噪声。是否更自然需自己试听。
- 实际会话不再清洗正文或补句号，建议直接朗读模式先试多音字/数字/中英混合。并未启用自动ASR核验，模型可能漏字添字，不能保证逐字完全一致。
- 默认首段chunk仍4，保持原稳定策略；可在启动前实验QTTS_FIRST_CHUNK_SIZE=2（有效2..8），但需同参考/同文本测first_played_ms与underruns，变差则恢复4。原生adapter仍句级缓冲，不能冒称声学流式。
- first_chunk_ms为裁边后非空PCM，model_first_chunk_ms是模型首块；真实首播另看first_played_ms。不能把收到前置静音当作已听到人声。

## 必须实测且尚未验收
物理十多分钟录音、真实Qwen/T4训练与音质不降、呼吸自然度、首声实际改善、连续播放准确率和网页一键训练闭环。当前状态PARTIAL/BLOCKED，不是“全部成功”。Kaggle有效会话内健康驻留保留，平台回收/配额不可绕过。

## 长数据覆盖补充门禁

现有训练快照仍最多16条；若高质量切分产生更多片段，还需扩展受限分片/manifest与完整样本覆盖后才能全部入训，不能只选前16条冒充完整十分钟训练。

---

## 内嵌备忘录：KAGGLE_STEP15_REVIEW1.md

# 第十五阶段第1轮专题审查：100条建议

全源文件读取/哈希与Python AST巡检不等于逐行语义正确证明。重点调用链经过人工分析；建议不是100项已修复。处置与实测边界见AUDIT。

1. [S15-R1-001] `worker.RealEngine`：禁止参考码进入解码器。
2. [S15-R1-002] `worker.RealEngine`：仅以说话人向量条件生成。
3. [S15-R1-003] `worker.RealEngine`：生成调用不传参考正文。
4. [S15-R1-004] `worker.RealEngine`：预热采用相同向量模式。
5. [S15-R1-005] `worker.RealEngine`：dtype回退后仍用向量模式。
6. [S15-R1-006] `worker.RealEngine`：不开放环境变量回退ICL。
7. [S15-R1-007] `worker.RealEngine`：明确韵律相似度可能变化。
8. [S15-R1-008] `worker.RealEngine`：核对Faster0.5.4实际源码。
9. [S15-R1-009] `worker.RealEngine`：生成采样率仍严格24k。
10. [S15-R1-010] `worker.RealEngine`：生成器取消时仍close。
11. [S15-R1-011] `worker.lead_audio`：废止reference呼吸拼接开关。
12. [S15-R1-012] `worker.lead_audio`：前置停顿仅零样本。
13. [S15-R1-013] `worker.lead_audio`：旧breath_files不能被读取。
14. [S15-R1-014] `worker.lead_audio`：无参考片段也不造噪声。
15. [S15-R1-015] `worker.lead_audio`：保留模型自身呼吸。
16. [S15-R1-016] `worker.lead_audio`：不把去呼吸等同自然音色。
17. [S15-R1-017] `worker.lead_audio`：暂停最长仍1500ms。
18. [S15-R1-018] `worker.lead_audio`：负暂停仍归零。
19. [S15-R1-019] `worker.lead_audio`：随机种子不能改变静音。
20. [S15-R1-020] `worker.lead_audio`：人工试听仍是门禁。
21. [S15-R1-021] `worker.run_job`：PCM来源只接受模型和零停顿。
22. [S15-R1-022] `worker.run_job`：不因模型失败回放anchor。
23. [S15-R1-023] `worker.run_job`：不因空结果播放参考。
24. [S15-R1-024] `worker.run_job`：保留nonfinite拒绝。
25. [S15-R1-025] `worker.run_job`：保留异常统计。
26. [S15-R1-026] `worker.run_job`：保留裁边。
27. [S15-R1-027] `worker.run_job`：保留尾部淡出。
28. [S15-R1-028] `worker.run_job`：保留取消检查。
29. [S15-R1-029] `worker.run_job`：保留每GPU互斥。
30. [S15-R1-030] `worker.run_job`：日志报告生成隔离模式。
31. [S15-R1-031] `adapter_engine`：核对原生向量模式。
32. [S15-R1-032] `adapter_engine`：不能把训练参考当输出。
33. [S15-R1-033] `adapter_engine`：固定adapter哈希。
34. [S15-R1-034] `adapter_engine`：损坏adapter不能回退Base。
35. [S15-R1-035] `adapter_engine`：不改变句级缓冲标记。
36. [S15-R1-036] `adapter_engine`：不混驻两种引擎。
37. [S15-R1-037] `adapter_engine`：保持取消丢弃迟到wave。
38. [S15-R1-038] `adapter_engine`：训练候选不自动激活。
39. [S15-R1-039] `adapter_engine`：新进程重载仍需实机。
40. [S15-R1-040] `adapter_engine`：无训练证据不称已训练。
41. [S15-R1-041] `朗读内容`：不拼接参考文本。
42. [S15-R1-042] `朗读内容`：不修改目标文本。
43. [S15-R1-043] `朗读内容`：不补额外说明。
44. [S15-R1-044] `朗读内容`：不以字符串一致冒充声学一致。
45. [S15-R1-045] `朗读内容`：不自动删数字。
46. [S15-R1-046] `朗读内容`：不自动删专名。
47. [S15-R1-047] `朗读内容`：不裁词谋求首声。
48. [S15-R1-048] `朗读内容`：短句仍需语言条件。
49. [S15-R1-049] `朗读内容`：模型幻觉单独披露。
50. [S15-R1-050] `朗读内容`：严格ASR拒播仍未实现。
51. [S15-R1-051] `PCM隔离回归`：以非零参考bank诱捕混入。
52. [S15-R1-052] `PCM隔离回归`：旧环境reference模式也应静音。
53. [S15-R1-053] `PCM隔离回归`：断言生成xvec_only为真。
54. [S15-R1-054] `PCM隔离回归`：断言参考正文为空。
55. [S15-R1-055] `PCM隔离回归`：预热断言与生成相同。
56. [S15-R1-056] `PCM隔离回归`：加载不得读取呼吸文件。
57. [S15-R1-057] `PCM隔离回归`：输出频率标记与参考分离。
58. [S15-R1-058] `PCM隔离回归`：完整协议中仅模型PCM。
59. [S15-R1-059] `PCM隔离回归`：失败流不得补参考。
60. [S15-R1-060] `PCM隔离回归`：重复三轮隔离验证。
61. [S15-R1-061] `音量`：新旧档案统一输出目标。
62. [S15-R1-062] `音量`：默认目标从负21到负18dBFS。
63. [S15-R1-063] `音量`：保留可调输出目标。
64. [S15-R1-064] `音量`：合法范围负24到负14。
65. [S15-R1-065] `音量`：非数字回退默认。
66. [S15-R1-066] `音量`：NaN回退默认。
67. [S15-R1-067] `音量`：正无穷回退默认。
68. [S15-R1-068] `音量`：不修改原始录音。
69. [S15-R1-069] `音量`：保持软限幅。
70. [S15-R1-070] `音量`：不承诺所有音量都增加3dB。
71. [S15-R1-071] `DSP质量`：验证低电平正弦增益。
72. [S15-R1-072] `DSP质量`：验证满幅输入不溢出。
73. [S15-R1-073] `DSP质量`：保留DC blocker。
74. [S15-R1-074] `DSP质量`：保留段间淡入。
75. [S15-R1-075] `DSP质量`：保留尾部淡出。
76. [S15-R1-076] `DSP质量`：Rust与NumPy参数相同。
77. [S15-R1-077] `DSP质量`：不新增C++重复实现。
78. [S15-R1-078] `DSP质量`：采样率不降。
79. [S15-R1-079] `DSP质量`：不硬裁削峰。
80. [S15-R1-080] `DSP质量`：测量使用非语音时标明合成。
81. [S15-R1-081] `GPU显存`：1.7B FP16权重估算约3.4GB。
82. [S15-R1-082] `GPU显存`：两模型权重不是全部显存。
83. [S15-R1-083] `GPU显存`：计入codec和speaker。
84. [S15-R1-084] `GPU显存`：计入KV cache。
85. [S15-R1-085] `GPU显存`：计入CUDA graph。
86. [S15-R1-086] `GPU显存`：计入分配器碎片。
87. [S15-R1-087] `GPU显存`：同卡并发争计算带宽。
88. [S15-R1-088] `GPU显存`：不默认每卡两模型。
89. [S15-R1-089] `GPU显存`：以两卡各一模型为基线。
90. [S15-R1-090] `GPU显存`：真双副本收益必须实测。
91. [S15-R1-091] `所有权与安全`：保留单可见GPU契约。
92. [S15-R1-092] `所有权与安全`：不绕过fleet租约。
93. [S15-R1-093] `所有权与安全`：不删除锁。
94. [S15-R1-094] `所有权与安全`：不按旧PID杀。
95. [S15-R1-095] `所有权与安全`：不安装未知CUDA补丁。
96. [S15-R1-096] `所有权与安全`：不输出口令。
97. [S15-R1-097] `所有权与安全`：不保存用户参考到报告。
98. [S15-R1-098] `所有权与安全`：不自动上传录音。
99. [S15-R1-099] `所有权与安全`：不更改已冻结14。
100. [S15-R1-100] `所有权与安全`：保持3000正式工作台。

---

## 内嵌备忘录：KAGGLE_STEP15_REVIEW2.md

# 第十五阶段第2轮专题审查：100条建议

全源文件读取/哈希与Python AST巡检不等于逐行语义正确证明。重点调用链经过人工分析；建议不是100项已修复。处置与实测边界见AUDIT。

1. [S15-R2-001] `首段分段`：识别当前末尾标点等待lookahead。
2. [S15-R2-002] `首段分段`：只为首段新增即时确定边界。
3. [S15-R2-003] `首段分段`：句末中文标点可立即提交。
4. [S15-R2-004] `首段分段`：逗号达到首段预算可提交。
5. [S15-R2-005] `首段分段`：ASCII点仍等lookahead避小数。
6. [S15-R2-006] `首段分段`：保留后续正常分段。
7. [S15-R2-007] `首段分段`：新段保留原文。
8. [S15-R2-008] `首段分段`：不等待LLM全篇完成。
9. [S15-R2-009] `首段分段`：不为每token发TTS。
10. [S15-R2-010] `首段分段`：短于常规阈值完整句可首发。
11. [S15-R2-011] `单位边界`：英文单词不从中间拆开。
12. [S15-R2-012] `单位边界`：小数12.50不拆错。
13. [S15-R2-013] `单位边界`：英文缩写保留。
14. [S15-R2-014] `单位边界`：标点后引号不能丢。
15. [S15-R2-015] `单位边界`：跨delta空格仍保存。
16. [S15-R2-016] `单位边界`：纯标点不能伪成语音。
17. [S15-R2-017] `单位边界`：Unicode原样。
18. [S15-R2-018] `单位边界`：组合emoji不作为词。
19. [S15-R2-019] `单位边界`：无标点长句保持上限。
20. [S15-R2-020] `单位边界`：最后残留仍Flush。
21. [S15-R2-021] `顺序保护`：首段任务优先。
22. [S15-R2-022] `顺序保护`：第二段可用另一GPU。
23. [S15-R2-023] `顺序保护`：已输出失败不重放。
24. [S15-R2-024] `顺序保护`：未输出失败才允许重试。
25. [S15-R2-025] `顺序保护`：保留段索引。
26. [S15-R2-026] `顺序保护`：保留背压高低水位。
27. [S15-R2-027] `顺序保护`：保留迟滞。
28. [S15-R2-028] `顺序保护`：不无限预生成。
29. [S15-R2-029] `顺序保护`：取消移除排队任务。
30. [S15-R2-030] `顺序保护`：健康检查不回放参考。
31. [S15-R2-031] `LLM流`：保留每delta向前端推送。
32. [S15-R2-032] `LLM流`：首句完成即submit。
33. [S15-R2-033] `LLM流`：首token计时保留。
34. [S15-R2-034] `LLM流`：首段提交计时保留。
35. [S15-R2-035] `LLM流`：LLM完成计时保留。
36. [S15-R2-036] `LLM流`：非法JSON报错。
37. [S15-R2-037] `LLM流`：截断finish_reason报错。
38. [S15-R2-038] `LLM流`：取消终止HTTP。
39. [S15-R2-039] `LLM流`：不记录API密钥。
40. [S15-R2-040] `LLM流`：用本地SSE延迟尾巴测试。
41. [S15-R2-041] `首声指标`：区分首token和首段。
42. [S15-R2-042] `首声指标`：区分模型首块和PCM。
43. [S15-R2-043] `首声指标`：区分首PCM和首播。
44. [S15-R2-044] `首声指标`：静音不当作人声。
45. [S15-R2-045] `首声指标`：保留欠载次数。
46. [S15-R2-046] `首声指标`：不以网络替身称DeepSeek实测。
47. [S15-R2-047] `首声指标`：不以MockRTF称QwenRTF。
48. [S15-R2-048] `首声指标`：记录首段早于LLM结束。
49. [S15-R2-049] `首声指标`：没有CUDA不填GPU延迟。
50. [S15-R2-050] `首声指标`：不承诺三秒内。
51. [S15-R2-051] `播放器`：先不盲降全局缓冲。
52. [S15-R2-052] `播放器`：保持starved恢复阈值。
53. [S15-R2-053] `播放器`：保留短尾完成后启动。
54. [S15-R2-054] `播放器`：停止重置ring。
55. [S15-R2-055] `播放器`：迟到PCM不继续播放。
56. [S15-R2-056] `播放器`：初始化失败可重试。
57. [S15-R2-057] `播放器`：保留浏览器重采样。
58. [S15-R2-058] `播放器`：不将gain无限放大。
59. [S15-R2-059] `播放器`：不新增播放参考audio标签。
60. [S15-R2-060] `播放器`：保持手机布局。
61. [S15-R2-061] `首块预算`：保留默认chunk4稳定策略。
62. [S15-R2-062] `首块预算`：允许显式2到8试验。
63. [S15-R2-063] `首块预算`：无效环境回退4。
64. [S15-R2-064] `首块预算`：后段按背压选择。
65. [S15-R2-065] `首块预算`：不把chunk2必然称更快。
66. [S15-R2-066] `首块预算`：重测小chunk欠载。
67. [S15-R2-067] `首块预算`：记录同文同参考条件。
68. [S15-R2-068] `首块预算`：预热成本单列。
69. [S15-R2-069] `首块预算`：不改变max_new_tokens掩盖。
70. [S15-R2-070] `首块预算`：单句质量需真人听。
71. [S15-R2-071] `线程与语言`：Go保留调度路径。
72. [S15-R2-072] `线程与语言`：Python保留模型接口。
73. [S15-R2-073] `线程与语言`：Rust保留DSP。
74. [S15-R2-074] `线程与语言`：JS保留播放。
75. [S15-R2-075] `线程与语言`：不新加Java网络服务。
76. [S15-R2-076] `线程与语言`：不为多语言复制采样器。
77. [S15-R2-077] `线程与语言`：不盲开每卡双进程。
78. [S15-R2-078] `线程与语言`：不启用不支持的BF16。
79. [S15-R2-079] `线程与语言`：不将TF32称T4加速。
80. [S15-R2-080] `线程与语言`：量化质量另实验。
81. [S15-R2-081] `流式测试`：首句单delta即可产生任务。
82. [S15-R2-082] `流式测试`：短中文完整句可首发。
83. [S15-R2-083] `流式测试`：ASCII数字点仍保留。
84. [S15-R2-084] `流式测试`：逗号完整前缀可首发。
85. [S15-R2-085] `流式测试`：相同文本各切片重组。
86. [S15-R2-086] `流式测试`：新特性用应用配置而非旧配置。
87. [S15-R2-087] `流式测试`：晚引号仍完整保留。
88. [S15-R2-088] `流式测试`：SSE未结束worker已收到首段。
89. [S15-R2-089] `流式测试`：最终按索引输出。
90. [S15-R2-090] `流式测试`：Go race三轮。
91. [S15-R2-091] `退化防护`：非首段旧策略不变。
92. [S15-R2-092] `退化防护`：朗读长文不丢段。
93. [S15-R2-093] `退化防护`：URL不清洗。
94. [S15-R2-094] `退化防护`：DeepSeek错误前缀可见。
95. [S15-R2-095] `退化防护`：超时不冒成功。
96. [S15-R2-096] `退化防护`：取消不重复提交。
97. [S15-R2-097] `退化防护`：独立记录早期失败。
98. [S15-R2-098] `退化防护`：浏览器全量回归。
99. [S15-R2-099] `退化防护`：Python全量回归。
100. [S15-R2-100] `退化防护`：无硬件保持部分验收。

---

## 内嵌备忘录：KAGGLE_STEP15_REVIEW3.md

# 第十五阶段第3轮专题审查：100条建议

全源文件读取/哈希与Python AST巡检不等于逐行语义正确证明。重点调用链经过人工分析；建议不是100项已修复。处置与实测边界见AUDIT。

1. [S15-R3-001] `创建默认`：默认关闭可选GPU候选校准。
2. [S15-R3-002] `创建默认`：保留手动校准按钮。
3. [S15-R3-003] `创建默认`：直接创建与库处理默认一致。
4. [S15-R3-004] `创建默认`：后端缺省也关闭校准。
5. [S15-R3-005] `创建默认`：锁定重置默认关闭。
6. [S15-R3-006] `创建默认`：明确不是训练。
7. [S15-R3-007] `创建默认`：不隐藏校准质量代价。
8. [S15-R3-008] `创建默认`：保留两卡预热。
9. [S15-R3-009] `创建默认`：失败不改active。
10. [S15-R3-010] `创建默认`：完成收据不虚报。
11. [S15-R3-011] `ASR成本`：已知单段短文本直接使用。
12. [S15-R3-012] `ASR成本`：不能把长文本套短片。
13. [S15-R3-013] `ASR成本`：保持全量长音频ASR。
14. [S15-R3-014] `ASR成本`：不取前十秒冒充完整。
15. [S15-R3-015] `ASR成本`：CPU Whisper可驻留复用。
16. [S15-R3-016] `ASR成本`：不在GPU常驻ASR。
17. [S15-R3-017] `ASR成本`：保留CPU回退。
18. [S15-R3-018] `ASR成本`：保留识别beam5。
19. [S15-R3-019] `ASR成本`：保留词时间戳。
20. [S15-R3-020] `ASR成本`：记录手动转写绕过ASR。
21. [S15-R3-021] `ASR内存`：仅CPU默认驻留。
22. [S15-R3-022] `ASR内存`：CUDA ASR仍卸载。
23. [S15-R3-023] `ASR内存`：显式开关可禁用驻留。
24. [S15-R3-024] `ASR内存`：同一重模型入口串行。
25. [S15-R3-025] `ASR内存`：不无限缓存音频。
26. [S15-R3-026] `ASR内存`：不缓存每个用户转写。
27. [S15-R3-027] `ASR内存`：不让驻留伪造模型已加载。
28. [S15-R3-028] `ASR内存`：首次下载成本单列。
29. [S15-R3-029] `ASR内存`：CPU内存风险披露。
30. [S15-R3-030] `ASR内存`：不以第二次速度代表冷启动。
31. [S15-R3-031] `重复计算`：档案内部嵌入按内容哈希复用。
32. [S15-R3-032] `重复计算`：嵌入缓存仅本次任务。
33. [S15-R3-033] `重复计算`：返回向量保持只读语义。
34. [S15-R3-034] `重复计算`：不跨档案泄漏用户数据。
35. [S15-R3-035] `重复计算`：记录embed实际调用数。
36. [S15-R3-036] `重复计算`：记录embed命中数。
37. [S15-R3-037] `重复计算`：候选相同波形可复用。
38. [S15-R3-038] `重复计算`：不按文件名猜相同。
39. [S15-R3-039] `重复计算`：不改变候选排序公式。
40. [S15-R3-040] `重复计算`：缓存失败不写半成品。
41. [S15-R3-041] `CPU候选`：保留24候选上限。
42. [S15-R3-042] `CPU候选`：保留前三非重叠。
43. [S15-R3-043] `CPU候选`：保留SNR打分。
44. [S15-R3-044] `CPU候选`：保留典型性中心。
45. [S15-R3-045] `CPU候选`：保留F0打分。
46. [S15-R3-046] `CPU候选`：准确F0仍用于最佳锚点。
47. [S15-R3-047] `CPU候选`：不偷偷换MFCC冒充ECAPA。
48. [S15-R3-048] `CPU候选`：不降采样输入标准。
49. [S15-R3-049] `CPU候选`：不减少可用文件。
50. [S15-R3-050] `CPU候选`：不承诺质量无损提速倍数。
51. [S15-R3-051] `分析阶段计时`：记录speaker加载。
52. [S15-R3-052] `分析阶段计时`：记录解码降噪。
53. [S15-R3-053] `分析阶段计时`：记录ASR。
54. [S15-R3-054] `分析阶段计时`：记录候选评分。
55. [S15-R3-055] `分析阶段计时`：记录呼吸韵律。
56. [S15-R3-056] `分析阶段计时`：记录worker加载。
57. [S15-R3-057] `分析阶段计时`：记录可选校准。
58. [S15-R3-058] `分析阶段计时`：记录总构建时间。
59. [S15-R3-059] `分析阶段计时`：成功后最终写回profile。
60. [S15-R3-060] `分析阶段计时`：旧calibration写回不能覆盖。
61. [S15-R3-061] `候选转写`：长单个ASR段不能截音频保留全文。
62. [S15-R3-062] `候选转写`：长度超界无可信字时间拒绝。
63. [S15-R3-063] `候选转写`：不猜均匀对齐。
64. [S15-R3-064] `候选转写`：提示重录短段或审核切分。
65. [S15-R3-065] `候选转写`：手动16秒整段可不裁。
66. [S15-R3-066] `候选转写`：候选start/end匹配实际波形。
67. [S15-R3-067] `候选转写`：保留多文件来源。
68. [S15-R3-068] `候选转写`：检查负时间。
69. [S15-R3-069] `候选转写`：检查超音频边界。
70. [S15-R3-070] `候选转写`：不静默截断转写。
71. [S15-R3-071] `持久化`：完成前写回quality.build_s。
72. [S15-R3-072] `持久化`：持久化stage_ms。
73. [S15-R3-073] `持久化`：持久化嵌入缓存统计。
74. [S15-R3-074] `持久化`：失败不删除已有档案。
75. [S15-R3-075] `持久化`：新任务失败清理新目录。
76. [S15-R3-076] `持久化`：保持原子JSON。
77. [S15-R3-077] `持久化`：保留worker_load状态。
78. [S15-R3-078] `持久化`：保留校准选择。
79. [S15-R3-079] `持久化`：不把done当两卡加载成功。
80. [S15-R3-080] `持久化`：文件备份范围清楚。
81. [S15-R3-081] `发布交付`：生成新step15不覆盖14。
82. [S15-R3-082] `发布交付`：新增manifest逐文件校验。
83. [S15-R3-083] `发布交付`：复制页固定15哈希。
84. [S15-R3-084] `发布交付`：下载与剪贴板完整一致。
85. [S15-R3-085] `发布交付`：拒绝剪贴板时可全选。
86. [S15-R3-086] `发布交付`：375px无横向溢出。
87. [S15-R3-087] `发布交付`：冻结正式15文件。
88. [S15-R3-088] `发布交付`：交接完整嵌入新增备忘录。
89. [S15-R3-089] `发布交付`：三轮结果分别记录。
90. [S15-R3-090] `发布交付`：未通过项目不得打勾。
91. [S15-R3-091] `现场门禁`：用户截图256.4秒仅作问题证据。
92. [S15-R3-092] `现场门禁`：无原音频不能确定泄漏根因。
93. [S15-R3-093] `现场门禁`：真实Qwen生成必须试听。
94. [S15-R3-094] `现场门禁`：真实T4显存峰值必测。
95. [S15-R3-095] `现场门禁`：同卡双模型不默认试。
96. [S15-R3-096] `现场门禁`：首次和热创建分别测。
97. [S15-R3-097] `现场门禁`：同参考同目标文本比较。
98. [S15-R3-098] `现场门禁`：无额外参考重播需独立检查。
99. [S15-R3-099] `现场门禁`：历史网页训练缺口仍保留。
100. [S15-R3-100] `现场门禁`：不写100%无错误。

---

## 内嵌备忘录：KAGGLE_STEP15_PLAN.md

# 第十五阶段实施方案（产品修改前落盘）

## 优先目标
用户实机截图显示创建档案256.4秒，并报告播放中混入参考录音。截图本身无音频，不能判断确切声学根因。目标是生成路径强隔离、首个完整文字前缀及时调度、更响但不过载、减少可避免的创建等待。

## 三轮研究与顺序自问
已读取全源文件三遍，记录哈希及Python AST；分别分析worker/参考隔离、Go流/浏览器首播、analyst创建/持久化。不是穷尽语义证明。每轮100项建议在REVIEW1–3；问题16→17→18每题回答后50项落实建议已追加DECISIONS。不向用户追问，不承诺100%无错误。

## 分步实施
1. 冻结原始至14、正式工作台15文件。生成独立step15，不改历史包。
2. Faster加载、预热、生成统一x-vector-only，参考正文不参与生成；彻底禁止参考呼吸bank读入/拼接。仅模型输出和零停顿可进入播放。此模式可能改变韵律/音色相似度，不能冒称保质已验。
3. Go仅首段在确定的中文句末/逗号边界及时提交，不等后续delta；英文点仍保留小数lookahead。文本、任务顺序、背压、取消不重写。
4. Worker统一输出目标默认-18dBFS（原-21），覆盖旧档案；QTTS_OUTPUT_DBFS允许-24..-14，非法/非有限回退-18。原始录音不改，保留Rust/NumPy软限幅。
5. 默认关闭可选GPU候选校准，手动入口保留；CPU ASR允许复用（QTTS_ASR_KEEP_CPU=0关闭，CUDA仍卸载）；本次构建嵌入哈希去重；保留全部数据、24候选和评分公式。记录阶段耗时、最终build_s与缓存统计；修正超长ASR单段截音频配全文的危险回退。
6. 增加参考隔离、音量、阶段收据、默认校准与首句SSE尚未结束就开始TTS测试。三轮完整Python/Node/Go race/浏览器，协议与模型接口实验分开记录。
7. 完整重打包、复制下载逐字节验证；汇总审查处置、失败修复记录、快速使用和完整内嵌备忘录交接。

## 双副本结论
1.7B FP16纯参数约3.4GB；双份约6.8GB不含codec、KV、graph、临时张量。两个副本共享同一T4的计算/带宽，不能据此推论单请求更快，OOM风险须实机测。保留每T4一个模型、两T4并行相邻段。未经实测不默认增加副本，不量化/换语言冒充无损提速。

## 验收边界
CPU模型接口/合成信号不是完整Qwen声学实验。本环境无CUDA、真实DeepSeek服务凭据或用户原音频，不能宣布T4速度、音色相似度、零错字、实际256秒降低多少已验收。已有网页训练闭环/长数据全覆盖/严格声学拒播缺口仍未完成。本轮先对可验证工程范围执行三轮，真实硬件项保持BLOCKED并给现场门禁，不能循环空跑到假成功。

---

## 内嵌备忘录：KAGGLE_STEP15_AUDIT.md

# 第十五阶段：参考隔离、首句调度、增响与创建成本审查

日期2026-10-22。**工程实现已完成本轮选定范围，真实Qwen/T4音质与性能仍BLOCKED；不是全部用户需求完成。**

## 用户证据与根因边界
用户提供step14实际网页截图：BZM档案可见、候选6.3/6.4秒、创建日志256.4秒，报告克隆播放中插入原参考录音。截图不包含输出音频、GPU显存与分阶段耗时，所以不能确定这次具体是参考呼吸、ICL串音、模型幻觉或别的声学现象。

查阅实际PyPI Faster0.5.4 wheel的model.py，SHA256 `7d45740b805bb1a4798fbe20ffd580e2a35361e744c4645da106c2b6383d4de2`：ICL模式将ref_codes放入声学解码上下文，再裁去参考部分；上游xvec_only说明明确针对phoneme bleed-through。旧worker三个调用点均xvec_only=False。另有QTTS_BREATH_MODE=reference的显式参考呼吸拼接路径。当前14默认off不能证明该用户开启了reference，不能以存在这条路径就宣布确切根因已证实。

## 本轮实际改动
### 1. 强隔离生成
- worker.RealEngine档案加载、dtype回退预热、正式流式生成统一xvec_only=True、ref_text为空、append_silence=False。参考文件仅用于提取说话人向量，不向Faster ICL提供参考文本/声学码。
- Worker不再读取breath_files，不论旧环境reference设置如何，lead_audio只返回有界零停顿。没有参考音频低延迟占位或失败时回放参考的路径。
- stats使用reference_pcm_splicing=false描述代码策略，acoustic_text_verified仍false。模型自身呼吸不滤除，不能据此保证没有生成幻觉或逐字完全一致。
- 向量模式会改变ICL条件；韵律、口音、音色相似度可能变化，必须真实试听，不称无损切换或已有质量提升。

### 2. 首句调度
- Go新增LiveSegCfg，仅聊天首段使用。完整中文句末、问叹号及达到首段7units的分句不再要求下一delta；短完整句可首发，尾部空格同样处理。
- ASCII点仍等lookahead，避免12.50被拆成12.；未闭合引号/括号保持等待。普通朗读仍ExactSegCfg，后续段和取消、两GPU调度、有序转发、背压、播放器水位不变。
- 没有每token发TTS，LLM尚无确定边界时仍可能积累到FirstMax。纯标点/空白片段仍沿旧过滤，文本分段不是声学ASR核验。
- 实际本地HTTP/SSE实验让LLM尾巴阻塞，观察首段已进入真实scheduler并被HTTP worker fixture接收，再释放LLM尾巴。不是远程DeepSeek或Qwen速度证据。

### 3. 有界增响
- qtts_common.output_target_dbfs共享解析，默认-18dBFS，允许QTTS_OUTPUT_DBFS=-24..-14，非法/非有限回退-18。
- 旧、新档案重新加载时统一使用该输出目标及最大增益12dB（旧9dB），不修改原始录音；保留Rust/NumPy DC blocker、增益平滑、软限幅、淡入淡出。
- 低电平合成正弦验证目标效果及限幅；并非任意语音、静音或硬件音量都会增加恰好3dB，也不是响度LUFS认证。

### 4. 创建成本与正确性
- 网页直建、库处理、后端缺省均关闭可选GPU候选校准；手动按钮和显式勾选保留。不是偷偷删除全部质量模型，不把减少可选校准称质量等价证明。
- CPU Whisper允许跨任务复用同一个模型；QTTS_ASR_KEEP_CPU=0恢复释放；CUDA ASR仍卸载，避免与TTS争VRAM。ASR改RLock保护加载、完整惰性转写及释放；并发回归确认迭代结束前不能释放模型。保留large-v3、beam5、词时间戳与全录音处理，未靠降低识别质量提速。
- 构建局部嵌入缓存按float32样本内容SHA256去重，最多64条、每向量≤16KiB；不持久化录音或向量缓存、不跨声音任务复用。保留24候选、评分公式和最佳锚点准确F0。
- quality.stage_ms记录speaker_load/decode_denoise/asr/candidate_scoring/prosody_analysis/worker_load/optional_calibration；build_s与embedding_cache最终写回profile，页面可以展开查看。重新读取校准后的profile再合并quality，避免覆盖校准选择。
- 修复候选回退截前14秒却配整段文字的问题；仅允许完整2.5–16秒对齐片段，过长不猜切分、明确拒绝。可信手动16秒全文不再被截14秒。这是必要的安全拒绝，不是所有长ASR片段现在都自动可用。
- 首次下载/CPU大模型ASR与ECAPA/F0仍可能很慢；没有拿用户原录音做A/B，不能声称256.4秒已降到某个数值或“大幅提速已实测”。

## 为什么不每张T4放两个1.7B
纯参数1.7e9×2字节约3.4GB/份（十进制），两份约6.8GB；不是整个进程显存。codec、speaker、KV、CUDA graphs、临时张量和碎片另计；同时执行共享同一张T4的计算和带宽。装得下不等于单请求更快，额外副本也可能OOM/恶化首声。当前保持两T4各一模型，用两卡并行相邻段。没有双副本T4实测，不报告可装下或收益。

## 三轮检查与建议处置
REVIEW1/2/3各100项，前置review-before.json记录三次全源文件读取/哈希/Python AST，不是逐行语义正确证明。DECISIONS问题16/17/18顺序展开，每题50建议；累计18题900建议。300条逐项处置见review-disposition.json，区分implemented/preserved/documented-boundary/requires-hardware/not-implemented，不把建议数量当修复数。

## 验证结果（最终计数以final-checks.json为准）
- Python全量301项×3、Node30项×3、Go race count3；新16项隔离/音量/创建成本单测。
- 完整Chromium120项×3=360项在修正等义文案断言后全部通过（10.5分钟），最终完整包剪贴板另3轮通过；独立复制页剪贴板、下载、权限拒绝全选、375px三轮通过。初次357通过/3文案失败日志保留，不隐去。
- 实际Faster0.5.4 resolver→prepare_generation→两阶段streaming控制流三轮，每轮chunk2/4/8，经过生产RealEngine包装；CPU prompt、talker算子与codec为明确注入fixture，40帧/76800样本完整，参考码入decoder为0。不是完整Qwen语音模型。
- 实际完整Faster/Qwen库导入+2651参数tiny Mimi构造/保存/重载三轮通过；强制HF RoPE CPU preflight三轮通过，整体因无CUDA为blocked。
- ownership/input HTTP/codes CLI/mock pipeline/真实本地Go+HTTP+SSE adapter/fatal进程脚本各含三轮，全部三轮通过，结果见收据。
- frozen13与当前实际训练源码CPU tiny LoRA A/B另做三进程×三epoch/6步，loss/全部adapter逐位相同；tokenize12→3。墙钟含冷优化器启动/顺序偏差，不能报告训练倍速或Qwen质量。
- 正式3000项目15文件/revision和原始至14打包件哈希不变。独立3001提供step15完整代码，非Python在线执行器。

## 本轮发现的初始失败，未隐去
1. 验证环境初次启动先重建venv、但日志目录尚未创建，重定向失败exit1；创建目录后安装成功，非产品bug。
2. 初版增响测试发现同一9dB最大增益使很小信号两种目标都饱和于同一上限，无法变响；worker最大增益改为有界12dB，保留软限幅并验证通过。不能只改测试阈值掩盖。
3. 首段HTTP实验最初直接从Session.jobs取任务，早于Scheduler.Submit填写enq，race报错；改为真实scheduler队列锁下pickLocked，避免测试绕过生产同步。最终race三轮通过；此处是新测试夹具错误，没有无依据修改生产锁。
4. 补充首句带尾部空格的边界用例，并同步修复第二处lookahead等待。
5. 初次完整浏览器三轮357通过、3失败，均为旧用例要求“网页训练执行尚未闭环”但新版等义文案为“网页训练尚未闭环”；断言兼容可选“执行”，仍强制展示未闭环，不删除门禁。原日志browser-initial-repeat3.txt保留，完整三轮重跑。
6. CPU驻留复核发现原ASR锁只护加载，惰性转写与释放可能并发；改可重入锁覆盖整个使用周期，并发门禁通过，重新执行三轮全量Python和协议。
7. 交接刷新脚本从39备忘录移植时剩余一个unique数量断言未改，最初assert失败；改为45，完整内嵌及逐篇读回验证，不影响产品包。
8. 首次最终汇总校验器错误地假定协议日志只有3条JSON；输入HTTP含另一组库HTTP收据、adapter含独立损坏拒绝收据。按收据字段/round筛选三轮，并额外强制检查库HTTP与损坏adapter无PCM回退，不删除任何真实失败检查。初始校验器失败日志已保存。

## 保留阻塞
真实Qwen/T4三轮生成、参考重播排查试听、向量模式相似度、真实首播/欠载A/B、首次/热创建同录音A/B、Rust现场DSP和每卡双副本显存/吞吐未验收。没有访问用户GPU和原音频，不可模拟填成功。

历史网页真实训练控制面/维护租约移交/start-cancel-restore-publish、长数据审核对齐/超过16样本完整覆盖、真实训练保质吞吐、严格声学逐字拒播仍未实现/未验收；本轮不是对这些要求的豁免。整体状态PARTIAL/BLOCKED。

---

## 内嵌备忘录：KAGGLE_STEP15_QUICKSTART.md

# step15升级与现场验收

这是参考隔离/首句调度/输出增响/创建成本部分修复，不是全部目标完成，真实Qwen/T4提速和音质尚未验收。

## 升级
1. 下载自己需要保留的私有libraries/profiles及已有training_data/training_codes/training_runs；浏览器待提交录音先保存到库，再备份到自己的设备。不能把Kaggle工作目录当永久备份，不发口令或私人音频给聊天。
2. 停止并重启完整Kaggle会话，不只刷新网页/内核，不按旧PID杀、不删除GPU锁。
3. 选择T4×2、Internet开启；保持平台Torch/CUDA，不自行降级HF/Transformers。
4. 在新启动单元格之前运行下面配置，再将3001复制页的完整kaggle-fixed-step15.py放另一个Code单元格执行。

```python
import os
os.environ['QTTS_MOCK'] = '0'
os.environ['QTTS_TTS_ENGINE'] = 'faster'
os.environ['QTTS_FIRST_CHUNK_SIZE'] = '4'
os.environ['QTTS_OUTPUT_DBFS'] = '-18'
os.environ['QTTS_ASR_KEEP_CPU'] = '1'
os.environ.pop('QTTS_UNPACK_ONLY', None)
```

QTTS_BREATH_MODE=reference在step15已不能启用参考拼接，不必为它删改私有档案。源录音仍保留供音色向量提取、审查和备份，禁止拼接不等于删除源数据。

5. 等required RoPE检查pass、两worker加载/预热ready及QTTS ready后打开网址解锁。SystemExit0正常，不要重复启动。网页应显示“第十五阶段”，旧网页需刷新；若报锁冲突，停止重复启动，不删锁。
6. 可以直接重新启用已有普通参考档案，无需先重新录制。新worker会用向量模式重建缓存，旧档案输出目标也为-18。模型韵律/口音/音色相似度可能变化，不能因网页成功就认为质量已验收。

## 先做直接朗读
选择与参考内容明显不同的短目标句，例如“这次只朗读屏幕上的这句话，现在检查是否有多余内容。”，使用直接朗读模式，听有没有参考里的原话、漏字/添字/重复、断句或爆音。先不用DeepSeek，隔离文字生成变量。随后用中英混合、数字和长段测试。

普通档案参考文本仍用于转写审查/候选评分，当前向量生成不会朗读该文本；保存参考文本不会把它加入目标朗读。目标文字只来自直接朗读输入或DeepSeek正文。

程序禁用的是参考PCM拼接和ICL参考码上下文；没有自动ASR拒播门禁，模型仍可能幻觉，不能承诺零额外内容。

## 首句与增响
- 再切DeepSeek聊天，完整第一句/足够长分句就会提交TTS，不等全篇；不是每个token立即合成。
- 默认chunk4保持稳定播放器水位。先测first_played_ms/underruns，只有同文同档案对照时再试chunk2，变差恢复4。
- 输出默认-18dBFS、最大增益12dB，并保留限幅。音量仍不足可在下一次启动前试QTTS_OUTPUT_DBFS='-16'；合法范围-24..-14，先调耳机到安全音量，避免听力损伤。不会对所有声音精确增大3dB，不保证硬件外放效果。

## 创建档案
默认不勾选较慢的额外GPU校准，手动“候选校准”仍可用。单个≤16秒且有逐字匹配全文的录音可填写已知文本跳过ASR；不要凭空编转写。多段/长录音仍全量转写和评分，不只取前几秒。CPU Whisper模型复用会占用内存，内存紧张可设置QTTS_ASR_KEEP_CPU='0'后完整重启。

创建后在档案“创建阶段耗时”展开看实际分阶段时间。首次模型下载/加载仍可能慢；没有该录音的实测数据，不能给出固定秒数。过长单个ASR段没有可信短段对齐会明确拒绝，不再截14秒却配全文。

## 目标机三轮门禁（目前未执行）
每轮使用同一参考、不同于参考的相同测试文本；区分首次/热创建。记录：
- 两张T4唯一worker、每GPU峰值显存、引擎非Mock。
- 仅生成目标内容且不重播参考的实际试听；保留向量模式与13/14的音色/韵律差异记录。
- 首token/首段/首PCM/first_played_ms/underruns，不能把静音当首声。
- quality.stage_ms和build_s，校准开关一致才比较成本；不能拿关闭校准称同等完整校准快多少。
- 停止、中途取消、切换声音、长回答顺序、物理十多分钟录音和备份。

不默认试每T4双副本。两份权重约6.8GB不含其他显存，同卡共享计算，不保证更快。网页训练执行闭环与声学逐字拒播仍未完成，参考处理/快照不是训练。

---

## 内嵌备忘录：KAGGLE_STEP16_REVIEW1.md

# 第十六阶段第1轮专题审查：100条建议

全源读取/哈希/AST不等于逐行语义无错。重点调用链人工分析，未实测声学或GPU性能不填成功。

1. [S16-R1-001] `参考条件`：重新审视15强制向量模式。
2. [S16-R1-002] `参考条件`：默认恢复匹配转写的ICL条件。
3. [S16-R1-003] `参考条件`：无转写不得静默假设ICL。
4. [S16-R1-004] `参考条件`：向量模式保留为显式选项。
5. [S16-R1-005] `参考条件`：参考文本只作条件不拼目标正文。
6. [S16-R1-006] `参考条件`：解码器不接参考码。
7. [S16-R1-007] `参考条件`：保留原始参考录音。
8. [S16-R1-008] `参考条件`：不把恢复ICL称相似度已验证。
9. [S16-R1-009] `参考条件`：检查参考是否多人。
10. [S16-R1-010] `参考条件`：多人参考必须换干净单人样本。
11. [S16-R1-011] `提示缓存`：核查Faster路径键缓存。
12. [S16-R1-012] `提示缓存`：相同路径换音频必须失效。
13. [S16-R1-013] `提示缓存`：比较参考内容哈希。
14. [S16-R1-014] `提示缓存`：清除该路径旧缓存项。
15. [S16-R1-015] `提示缓存`：不删除模型全局权重。
16. [S16-R1-016] `提示缓存`：不信任仅profile_id相同。
17. [S16-R1-017] `提示缓存`：预热与生成采用同模式。
18. [S16-R1-018] `提示缓存`：dtype重载后重新构建条件。
19. [S16-R1-019] `提示缓存`：不把错误预热当就绪。
20. [S16-R1-020] `提示缓存`：缓存失效增加回归。
21. [S16-R1-021] `会话绑定`：会话开始固定参考内容指纹。
22. [S16-R1-022] `会话绑定`：Go与Python指纹算法一致。
23. [S16-R1-023] `会话绑定`：包含WAV与匹配文本。
24. [S16-R1-024] `会话绑定`：包含语言字段。
25. [S16-R1-025] `会话绑定`：长度前缀避免分隔歧义。
26. [S16-R1-026] `会话绑定`：每个语段携带同一指纹。
27. [S16-R1-027] `会话绑定`：Worker取锁后重新读取档案。
28. [S16-R1-028] `会话绑定`：不同版本先拒绝后输出。
29. [S16-R1-029] `会话绑定`：不重试成另一个声音。
30. [S16-R1-030] `会话绑定`：缺文件不降级原模型。
31. [S16-R1-031] `双卡一致`：保留每T4一个模型。
32. [S16-R1-032] `双卡一致`：比较两卡使用的参考指纹。
33. [S16-R1-033] `双卡一致`：保留同session条件不变。
34. [S16-R1-034] `双卡一致`：候选切换只能影响新会话。
35. [S16-R1-035] `双卡一致`：旧会话版本不符明确失败。
36. [S16-R1-036] `双卡一致`：声音更新与合成共用锁。
37. [S16-R1-037] `双卡一致`：锁后重取profile避免旧引用。
38. [S16-R1-038] `双卡一致`：不要以profile名称证明相同。
39. [S16-R1-039] `双卡一致`：不把RMS一致当同一说话人。
40. [S16-R1-040] `双卡一致`：两张卡实际试听仍必需。
41. [S16-R1-041] `生成稳定`：相邻段使用稳定seed策略。
42. [S16-R1-042] `生成稳定`：不随意每段改变采样条件。
43. [S16-R1-043] `生成稳定`：不以降温保证身份。
44. [S16-R1-044] `生成稳定`：不默认删除情感。
45. [S16-R1-045] `生成稳定`：保留语言参数。
46. [S16-R1-046] `生成稳定`：保留max_new_tokens安全预算。
47. [S16-R1-047] `生成稳定`：保留取消后的生成器close。
48. [S16-R1-048] `生成稳定`：不引入随机参考混合。
49. [S16-R1-049] `生成稳定`：不混用候选锚点。
50. [S16-R1-050] `生成稳定`：不跨用户共享提示。
51. [S16-R1-051] `档案变更`：修正候选更换原路径复用。
52. [S16-R1-052] `档案变更`：文本更改触发提示失效。
53. [S16-R1-053] `档案变更`：手动校准选择不能覆盖回旧。
54. [S16-R1-054] `档案变更`：完成后保存阶段收据。
55. [S16-R1-055] `档案变更`：删除档案不能被旧请求静默复活。
56. [S16-R1-056] `档案变更`：不删除冻结15。
57. [S16-R1-057] `档案变更`：旧档案可重新加载。
58. [S16-R1-058] `档案变更`：参考需审核逐字转写。
59. [S16-R1-059] `档案变更`：ASR提案不是人工真值。
60. [S16-R1-060] `档案变更`：不从短片猜长文。
61. [S16-R1-061] `安全读取`：锚点仅单一安全文件名。
62. [S16-R1-062] `安全读取`：拒绝符号链接。
63. [S16-R1-063] `安全读取`：拒绝目录冒音频。
64. [S16-R1-064] `安全读取`：限制参考读取字节。
65. [S16-R1-065] `安全读取`：路径始终在档案目录。
66. [S16-R1-066] `安全读取`：哈希不输出原音频。
67. [S16-R1-067] `安全读取`：指纹不是授权证明。
68. [S16-R1-068] `安全读取`：不泄漏访问口令。
69. [S16-R1-069] `安全读取`：不自动云传录音。
70. [S16-R1-070] `安全读取`：保持私有备份边界。
71. [S16-R1-071] `原生adapter`：保留训练候选固定binding。
72. [S16-R1-072] `原生adapter`：不向faster注入adapter。
73. [S16-R1-073] `原生adapter`：不修改训练权重。
74. [S16-R1-074] `原生adapter`：缺adapter不回退Base。
75. [S16-R1-075] `原生adapter`：保留句级缓冲标记。
76. [S16-R1-076] `原生adapter`：继续核对Base哈希。
77. [S16-R1-077] `原生adapter`：旧训练功能做回归。
78. [S16-R1-078] `原生adapter`：不要把参考处理叫训练。
79. [S16-R1-079] `原生adapter`：网页真实训练缺口保留。
80. [S16-R1-080] `原生adapter`：真实训练质量仍待验收。
81. [S16-R1-081] `相似度验收`：相似度用真实说话人模型。
82. [S16-R1-082] `相似度验收`：不能伪造99.5百分比。
83. [S16-R1-083] `相似度验收`：文字一致不代表音色一致。
84. [S16-R1-084] `相似度验收`：多段输出分别试听。
85. [S16-R1-085] `相似度验收`：比较两卡相邻段。
86. [S16-R1-086] `相似度验收`：使用与参考不同的目标文字。
87. [S16-R1-087] `相似度验收`：同参考同文同seed对照。
88. [S16-R1-088] `相似度验收`：保留参考与输出独立文件。
89. [S16-R1-089] `相似度验收`：无用户音频不猜根因。
90. [S16-R1-090] `相似度验收`：不承诺100无错。
91. [S16-R1-091] `保护已有功能`：保留原文分段。
92. [S16-R1-092] `保护已有功能`：保留首句及时调度。
93. [S16-R1-093] `保护已有功能`：保留两主视图。
94. [S16-R1-094] `保护已有功能`：保留长录音预算。
95. [S16-R1-095] `保护已有功能`：保留命名空库。
96. [S16-R1-096] `保护已有功能`：保留失败本地片段。
97. [S16-R1-097] `保护已有功能`：保留手动候选校准。
98. [S16-R1-098] `保护已有功能`：保留DeepSeek取消。
99. [S16-R1-099] `保护已有功能`：保留3000正式工作台。
100. [S16-R1-100] `保护已有功能`：保留原始至15整包。

---

## 内嵌备忘录：KAGGLE_STEP16_REVIEW2.md

# 第十六阶段第2轮专题审查：100条建议

全源读取/哈希/AST不等于逐行语义无错。重点调用链人工分析，未实测声学或GPU性能不填成功。

1. [S16-R2-001] `解码路径`：使用实际Faster0.5.4准备接口。
2. [S16-R2-002] `解码路径`：只解码新生成声学码。
3. [S16-R2-003] `解码路径`：禁止参考PCM占位。
4. [S16-R2-004] `解码路径`：不得猜比例裁参考音频。
5. [S16-R2-005] `解码路径`：codec采样率必须24k。
6. [S16-R2-006] `解码路径`：逐帧1920样本契约需检查。
7. [S16-R2-007] `解码路径`：不兼容长度明确失败。
8. [S16-R2-008] `解码路径`：保留码组16列。
9. [S16-R2-009] `解码路径`：不偷改codec权重。
10. [S16-R2-010] `解码路径`：API签名变化明确报错。
11. [S16-R2-011] `有界窗口`：删除每块全历史cat。
12. [S16-R2-012] `有界窗口`：左上下文固定25帧。
13. [S16-R2-013] `有界窗口`：待提交尾部保留2帧。
14. [S16-R2-014] `有界窗口`：窗口随chunk有上限。
15. [S16-R2-015] `有界窗口`：新块仅输出未提交样本。
16. [S16-R2-016] `有界窗口`：提交游标单调。
17. [S16-R2-017] `有界窗口`：末尾只flush一次。
18. [S16-R2-018] `有界窗口`：取消不flush迟到音频。
19. [S16-R2-019] `有界窗口`：新旧窗口无重复样本。
20. [S16-R2-020] `有界窗口`：窗口长度记录便于核验。
21. [S16-R2-021] `块接缝`：未来两帧降低边缘重解码差异。
22. [S16-R2-022] `块接缝`：不对每块单独归一化。
23. [S16-R2-023] `块接缝`：保留时间连续性。
24. [S16-R2-024] `块接缝`：不要对每块强淡入。
25. [S16-R2-025] `块接缝`：短于lookahead暂不输出。
26. [S16-R2-026] `块接缝`：最后短块不能丢。
27. [S16-R2-027] `块接缝`：音频总样本不缩水。
28. [S16-R2-028] `块接缝`：不把重叠输出拼两次。
29. [S16-R2-029] `块接缝`：真实边界爆音仍要听。
30. [S16-R2-030] `块接缝`：增加右边缘不稳定fixture。
31. [S16-R2-031] `沙沙声`：不生成额外呼吸噪声。
32. [S16-R2-032] `沙沙声`：旧breath环境不能启用拼接。
33. [S16-R2-033] `沙沙声`：限制向上增益防底噪变大。
34. [S16-R2-034] `沙沙声`：输出目标仍负18dBFS。
35. [S16-R2-035] `沙沙声`：保留软限幅。
36. [S16-R2-036] `沙沙声`：不默认强低通损坏齿音。
37. [S16-R2-037] `沙沙声`：不抹掉所有清辅音。
38. [S16-R2-038] `沙沙声`：不假装无声就是降噪成功。
39. [S16-R2-039] `沙沙声`：无原音频不确定噪声来源。
40. [S16-R2-040] `沙沙声`：分别检查模型原PCM与后处理。
41. [S16-R2-041] `响度状态`：每任务重建leveler状态。
42. [S16-R2-042] `响度状态`：防双卡历史包络不同。
43. [S16-R2-043] `响度状态`：保留每段淡入淡出。
44. [S16-R2-044] `响度状态`：无语音不flush上段尾巴。
45. [S16-R2-045] `响度状态`：显式配置最大增益。
46. [S16-R2-046] `响度状态`：非法增益回退安全值。
47. [S16-R2-047] `响度状态`：新旧档案一致输出策略。
48. [S16-R2-048] `响度状态`：不能靠过载变响。
49. [S16-R2-049] `响度状态`：用低电平与满幅信号测试。
50. [S16-R2-050] `响度状态`：Rust与NumPy分别标边界。
51. [S16-R2-051] `RTF定义`：标准RTF等于生成墙钟除语音秒数。
52. [S16-R2-052] `RTF定义`：rtf_x是其倒数不是RTF。
53. [S16-R2-053] `RTF定义`：不把双卡速度相加冒单卡RTF。
54. [S16-R2-054] `RTF定义`：排除零停顿分母。
55. [S16-R2-055] `RTF定义`：失败取消样本不能算通过。
56. [S16-R2-056] `RTF定义`：冷预热与热态分开。
57. [S16-R2-057] `RTF定义`：首播与吞吐分开。
58. [S16-R2-058] `RTF定义`：记录每GPU结果。
59. [S16-R2-059] `RTF定义`：目标0.3需每条和汇总检查。
60. [S16-R2-060] `RTF定义`：无T4输出blocked。
61. [S16-R2-061] `计时拆分`：模型prepare单独计时。
62. [S16-R2-062] `计时拆分`：token生成单独计时。
63. [S16-R2-063] `计时拆分`：codec解码单独计时。
64. [S16-R2-064] `计时拆分`：DSP耗时单列。
65. [S16-R2-065] `计时拆分`：总墙钟包括必要同步。
66. [S16-R2-066] `计时拆分`：不拿CPU异步发射当CUDA完成。
67. [S16-R2-067] `计时拆分`：预热不计入热态却单独报告。
68. [S16-R2-068] `计时拆分`：报告first_played与欠载。
69. [S16-R2-069] `计时拆分`：保存原始测量行。
70. [S16-R2-070] `计时拆分`：不删慢样本。
71. [S16-R2-071] `性能选择`：仍用CUDA graph后端。
72. [S16-R2-072] `性能选择`：不盲开torch.compile。
73. [S16-R2-073] `性能选择`：T4继续FP16。
74. [S16-R2-074] `性能选择`：不假称T4原生BF16。
75. [S16-R2-075] `性能选择`：不为语言数量加网络跳转。
76. [S16-R2-076] `性能选择`：不每卡塞两副本。
77. [S16-R2-077] `性能选择`：上下文有界减少复制。
78. [S16-R2-078] `性能选择`：参考prompt按版本复用。
79. [S16-R2-079] `性能选择`：较大后段chunk做可选实测。
80. [S16-R2-080] `性能选择`：质量不降需要真实对照。
81. [S16-R2-081] `实验设计`：同一参考与目标文。
82. [S16-R2-082] `实验设计`：至少三轮独立进程接口实验。
83. [S16-R2-083] `实验设计`：每个chunk2/4/8/12检查。
84. [S16-R2-084] `实验设计`：检查短尾与取消。
85. [S16-R2-085] `实验设计`：参考码标记不能入decoder。
86. [S16-R2-086] `实验设计`：生成总帧对应总样本。
87. [S16-R2-087] `实验设计`：检查窗口峰值上限。
88. [S16-R2-088] `实验设计`：性能fixture不算Qwen性能。
89. [S16-R2-089] `实验设计`：CPU tinyMimi不算完整TTS。
90. [S16-R2-090] `实验设计`：硬件结果不能编造。
91. [S16-R2-091] `降级与边界`：新解码模式不自动回旧混参考路径。
92. [S16-R2-092] `降级与边界`：ICL缺文本给明确提示。
93. [S16-R2-093] `降级与边界`：不要静默改为别的声音。
94. [S16-R2-094] `降级与边界`：不要自动降模型大小。
95. [S16-R2-095] `降级与边界`：不改语速充RTF。
96. [S16-R2-096] `降级与边界`：不删用户正文充速度。
97. [S16-R2-097] `降级与边界`：不缩减训练数据。
98. [S16-R2-098] `降级与边界`：保留故障监督。
99. [S16-R2-099] `降级与边界`：记下每次初始失败。
100. [S16-R2-100] `降级与边界`：整体仍按证据判定。

---

## 内嵌备忘录：KAGGLE_STEP16_REVIEW3.md

# 第十六阶段第3轮专题审查：100条建议

全源读取/哈希/AST不等于逐行语义无错。重点调用链人工分析，未实测声学或GPU性能不填成功。

1. [S16-R3-001] `代码审查`：三轮读全源并记录哈希。
2. [S16-R3-002] `代码审查`：Python AST巡检。
3. [S16-R3-003] `代码审查`：Go格式和race。
4. [S16-R3-004] `代码审查`：浏览器JS语法。
5. [S16-R3-005] `代码审查`：Rust未修改仍说明现场边界。
6. [S16-R3-006] `代码审查`：逐专题审视引用关系。
7. [S16-R3-007] `代码审查`：不把哈希清单当语义证明。
8. [S16-R3-008] `代码审查`：每轮100建议逐项处置。
9. [S16-R3-009] `代码审查`：未实施项明确保留。
10. [S16-R3-010] `代码审查`：别把300建议当300bug。
11. [S16-R3-011] `参考绑定测试`：中英转写跨语言指纹一致。
12. [S16-R3-012] `参考绑定测试`：WAV变更指纹变化。
13. [S16-R3-013] `参考绑定测试`：文本变更指纹变化。
14. [S16-R3-014] `参考绑定测试`：语言变更指纹变化。
15. [S16-R3-015] `参考绑定测试`：质量统计变化不改变声音指纹。
16. [S16-R3-016] `参考绑定测试`：旧Worker缓存不能放行新pin。
17. [S16-R3-017] `参考绑定测试`：任务等待期间换档案需重校验。
18. [S16-R3-018] `参考绑定测试`：错误绑定不能输出PCM。
19. [S16-R3-019] `参考绑定测试`：两卡pin不等必须失败。
20. [S16-R3-020] `参考绑定测试`：取消不触发重加载。
21. [S16-R3-021] `解码测试`：样本总数等于总帧乘1920。
22. [S16-R3-022] `解码测试`：reference marker严格拒绝。
23. [S16-R3-023] `解码测试`：短码块可暂存。
24. [S16-R3-024] `解码测试`：最大窗口有界。
25. [S16-R3-025] `解码测试`：窗口左端超出不可访问。
26. [S16-R3-026] `解码测试`：lookahead尾部完整flush。
27. [S16-R3-027] `解码测试`：flush幂等。
28. [S16-R3-028] `解码测试`：取消丢尾部。
29. [S16-R3-029] `解码测试`：非有限输出不得成功。
30. [S16-R3-030] `解码测试`：错误采样率拒绝。
31. [S16-R3-031] `RTF实验入口`：调用真实worker而非造测量。
32. [S16-R3-032] `RTF实验入口`：用户显式启用目标机测试。
33. [S16-R3-033] `RTF实验入口`：不启动第三模型。
34. [S16-R3-034] `RTF实验入口`：仅读取既有档案。
35. [S16-R3-035] `RTF实验入口`：保存生成WAV供试听。
36. [S16-R3-036] `RTF实验入口`：报告不含口令。
37. [S16-R3-037] `RTF实验入口`：至少三次重复。
38. [S16-R3-038] `RTF实验入口`：测前确认双worker真实引擎。
39. [S16-R3-039] `RTF实验入口`：未达0.3就failed而非pass。
40. [S16-R3-040] `RTF实验入口`：没有CUDA明确blocked。
41. [S16-R3-041] `现有服务`：完整Python三轮。
42. [S16-R3-042] `现有服务`：Node三轮。
43. [S16-R3-043] `现有服务`：Go race count3。
44. [S16-R3-044] `现有服务`：完整Chromium三轮。
45. [S16-R3-045] `现有服务`：协议生命周期三轮。
46. [S16-R3-046] `现有服务`：真实Faster接口三轮。
47. [S16-R3-047] `现有服务`：HF导入tinyMimi三轮。
48. [S16-R3-048] `现有服务`：保留训练CPU等价门禁。
49. [S16-R3-049] `现有服务`：不忽略失败测试。
50. [S16-R3-050] `现有服务`：修复后完整重跑。
51. [S16-R3-051] `浏览器文案`：显示ICL条件不等于回放参考。
52. [S16-R3-052] `浏览器文案`：显示音色尚需试听。
53. [S16-R3-053] `浏览器文案`：显示RTF目标未达证据。
54. [S16-R3-054] `浏览器文案`：保留参考文本编辑。
55. [S16-R3-055] `浏览器文案`：提示转写必须匹配。
56. [S16-R3-056] `浏览器文案`：不新增假训练按钮。
57. [S16-R3-057] `浏览器文案`：不显示100相似度。
58. [S16-R3-058] `浏览器文案`：性能诊断不藏慢行。
59. [S16-R3-059] `浏览器文案`：手机无横向溢出。
60. [S16-R3-060] `浏览器文案`：锁定清空私有文本。
61. [S16-R3-061] `包与版本`：新step16独立文件。
62. [S16-R3-062] `包与版本`：原始至15冻结。
63. [S16-R3-063] `包与版本`：repack逐资产哈希。
64. [S16-R3-064] `包与版本`：内嵌新解码模块。
65. [S16-R3-065] `包与版本`：内嵌新RTF实验入口。
66. [S16-R3-066] `包与版本`：剪贴板全量读回。
67. [S16-R3-067] `包与版本`：下载逐字节核对。
68. [S16-R3-068] `包与版本`：权限拒绝可全选。
69. [S16-R3-069] `包与版本`：复制页固定新hash。
70. [S16-R3-070] `包与版本`：正式工作台不覆盖。
71. [S16-R3-071] `备忘录`：先计划后改产品。
72. [S16-R3-072] `备忘录`：问题19后给50建议。
73. [S16-R3-073] `备忘录`：问题20后给50建议。
74. [S16-R3-074] `备忘录`：问题21后给50建议。
75. [S16-R3-075] `备忘录`：累计问题建议保留。
76. [S16-R3-076] `备忘录`：最终交接完整内嵌。
77. [S16-R3-077] `备忘录`：原失败日志不覆盖。
78. [S16-R3-078] `备忘录`：状态用PARTIAL与BLOCKED。
79. [S16-R3-079] `备忘录`：缺硬件不得改成已达标。
80. [S16-R3-080] `备忘录`：不要求用户提供密钥。
81. [S16-R3-081] `真实声学`：多人参考不是调参可解决。
82. [S16-R3-082] `真实声学`：ICL能改善但非保证。
83. [S16-R3-083] `真实声学`：声纹分数不是听感真值。
84. [S16-R3-084] `真实声学`：模型仍可幻觉添字。
85. [S16-R3-085] `真实声学`：跨语言可能改变口音。
86. [S16-R3-086] `真实声学`：沙沙声需实际音频定位。
87. [S16-R3-087] `真实声学`：不从一张截图断定频谱。
88. [S16-R3-088] `真实声学`：静音延迟不算首声。
89. [S16-R3-089] `真实声学`：质量与速度一起验收。
90. [S16-R3-090] `真实声学`：人声自然度需独立试听。
91. [S16-R3-091] `后续门禁`：优先真实T4不同文本试听。
92. [S16-R3-092] `后续门禁`：逐GPU比较同参考。
93. [S16-R3-093] `后续门禁`：测试候选切换中取消。
94. [S16-R3-094] `后续门禁`：测RTF中位和最慢。
95. [S16-R3-095] `后续门禁`：参考泄漏单独核查。
96. [S16-R3-096] `后续门禁`：新进程重载检查。
97. [S16-R3-097] `后续门禁`：私有音频自行备份。
98. [S16-R3-098] `后续门禁`：历史网页训练闭环未完成。
99. [S16-R3-099] `后续门禁`：长样本全覆盖未完成。
100. [S16-R3-100] `后续门禁`：不把工程通过称全部目标完成。

---

## 内嵌备忘录：KAGGLE_STEP16_PLAN.md

# 第十六阶段计划（产品修改前）

## 目标及证据
用户报告克隆不像/偶尔两种声音/沙沙声，要求RTF≤0.3。当前没有用户输出音频、CUDA/T4或完整模型权重，不能确认声学根因或保证0.3已达标。15向量模式、路径键缓存、缺会话参考pin、流式末端重解码和+12dB增益是本轮需要验证/修复的风险。

已完成三轮专题研究各100建议；全源读取/哈希/Python AST只是巡检，非穷尽语义证明。问题19→20→21各50建议，先记方案再改产品。累计21题1050建议，三轮建议必须逐项处置，不能当300个bug。

## 推荐方案与小步骤
1. 冻结原始–15和正式3000工作台；新建step16，不覆盖历史。
2. 默认ICL匹配参考音频+转写，仅用作talker条件；新生成码专用decoder不接参考码或参考PCM。QTTS_CLONE_MODE=xvector仅显式选择，无转写ICL拒绝，不静默换声音。
3. 参考WAV+匹配文本+语言以长度前缀SHA256指纹绑定；Go会话固定pin，每段携带；worker取锁后复核当前档案和pin，不符在任何PCM前拒绝。替换同路径锚点时清除旧Faster路径缓存；预热与生成条件一致。
4. bounded codec窗口：左25帧、右2帧lookahead，chunk2–16；只提交未输出帧，24k/16码组/每帧1920样本不符拒绝。保留取消，末尾幂等flush。相比15引入约160ms音频前瞻，不承诺首声免费加快。
5. 每任务新leveler避免跨段/双卡历史状态影响；默认最大增益6dB，目标仍-18，QTTS_MAX_GAIN_DB显式0..12。无语音不flush前段尾。没有实际噪声样本，不默认强低通/谱门或声称噪声已清除。
6. 统一同会话生成seed，保留两卡各一模型、真实CUDA graph、FP16、原文分段/取消/长录音/手动校准/训练代码。采样参数先保持，不能把降温说成身份保证。
7. 新增目标机基准入口：仅显式调用已有真实worker，不加载第三模型；逐卡逐条至少三轮保存WAV与RTF(gen_wall/audio)；冷/热、RTF与首播分开。无CUDA必须blocked，0.3未达必须fail，声音质量始终需试听。
8. 三轮完整Python/Node/Go race/Chromium/协议、实际Faster接口fixture及tinyMimi依赖回归；最终完整包复制/下载读回、逐资产哈希、完整备忘录交接。

## 不作的虚假保证
不无依据增加C++/Java/SQL服务，不每卡放两模型，不改语速/删正文/减少数据充RTF，不播放参考片段补相似度，不把Mock或CPU吞吐当T4。真实相似度、单一音色、无沙沙与RTF0.3仍须目标设备三轮测量。历史网页真实训练闭环/长数据完整覆盖/严格声学拒播缺口仍保留；整体PARTIAL/BLOCKED直到有证据。

## 实施中证据驱动修订（保留原方案，未伪装成预先已知）
- 实际HF0.1.1.post1的Qwen12Hz codec是causal attention/causal卷积。真实23813参数tiny decoder随机权重CPU实验，8帧解码与追加到12帧的前缀最大差=0。因此默认前瞻改为0；`QTTS_CODEC_LOOKAHEAD_FRAMES=2`仅显式对照，不凭合成不稳定fixture默认增加160ms。保留通用lookahead回归，不声称真实沙沙根因是右边缘。
- 路径缓存失效之外，保存预计算ICL提示内存快照，合成传入voice_clone_prompt而不重新读取可覆盖的参考文件；dtype重载清空提示快照，后续档案必须重建。避免检查哈希后文件更改的TOCTOU风险。每段还绑定conditioning模式，混合模式先拒绝。
- 候选/文本更新如部分worker失败返回503+reference_saved=true，不宣称已就绪；activation比较两卡pin和模式并再次读当前参考版本。不回滚到另一声音。

---

## 内嵌备忘录：KAGGLE_STEP16_AUDIT.md

# 第十六阶段交付审计

## 状态

**本轮工程修复及最终三轮回归已通过；整体PARTIAL/BLOCKED，绝不声称真实相似度、无沙沙或T4 RTF0.3已经达到。** 最终状态以`validation/step16/final-checks.json`为准。完整目标22/300不因本轮变更自动升级。

最终完整包`kaggle/kaggle-fixed-step16.py`：306580B、52资产，SHA256 `c6ed6c89e6356fc6c7ab554f96a2c3201a8e4690c007ea66626445cc658b4429`。原始–15和正式工作台冻结。

## 实现及原因

1. `clone_stream.py/worker.py`：默认匹配转写ICL，参考文字不拼目标正文；参考声学码只进talker条件，codec仅接新生成码。显式xvector兼容选择，无文本ICL明确拒绝。不会声称ICL必然完全不产生参考音素或文字幻觉。
2. `voice_binding.py/session.go/scheduler.go`：参考WAV、UTF8转写及语言以长度前缀SHA256，Go/Python固定互操作样本；同会话pin/seed固定，每段携带pin与模式。Worker锁内重读档案/复核，版本或模式不符在lead/PCM前拒绝。先前已经播放的段不能撤回，不是整会话事务回滚。
3. 同路径参考变更时清除Faster旧路径键；预计算提示以档案内存快照保存，生成不再读取可覆盖的锚点路径。取prompt前后参考指纹一致才发布；dtype重载清空提示，后续按需重建。无匹配提示不自动回旧参考decoder。
4. 有界25帧左上下文，删除全历史码cat与比例裁参考；16码组/24k/1920样本每帧契约不合即拒绝，样本游标无重复/缺失，尾部幂等、取消不flush。默认前瞻0，实验可选0..2。
5. 最初方案右2帧前瞻被实际因果源码和真实tiny decoder前缀实验推翻：23813随机参数、8帧vs12帧前缀最大差0。故不默认付160ms代价，不把合成不稳定fixture当真实噪声证据。窗口重解码与完整解码在tiny随机参数下相同，不保证训练权重/多层大模型相同。
6. 每任务重置leveler/DC/包络，默认最大增益6dB（0..12显式可调），目标仍-18dBFS、保留软限幅；无生成语音不flush前段尾。降低底噪放大风险，并非真正频谱去噪已验证；很轻的输出可能比15最大12dB稍轻。
7. Analyst文本/候选更新的部分worker失败不再回`ok:true`；返回503并声明reference_saved。Go activation比较pin/模式且重读当前版本；失败保留原active ID，不把不同参考静默混用。
8. 训练adapter档案的sentence-buffered原生模式保持固定，不被gateway的Mock/faster测试标记覆盖；真正不支持训练的Worker仍会拒绝，不绕过adapter来源/权重校验。
9. 新`tools/voice_benchmark.py`明确--run后只调两真实驻留Faster workers，不加载第三模型；至少3轮、逐GPU/文本、无填充speech_samples分母、worker与HTTP wall RTF并列；WAV/JSONL私有保存，慢行保留，0.3未达失败。无硬件不算通过。

## 三轮审查与自问自答

三轮100条专题建议记录于REVIEW1/2/3，逐项处置见validation/step16/review-disposition.json。全源读取/AST/哈希不是穷尽语义无错，也不是300个bug或300项均已实施。问题19→20→21，各50开发建议后才进入下一题，累计21题1050建议；不向用户重复提问，也不声称已理解到100%可保证。

## 最终验证

- Python完整322×3=966项最终通过（37.320/39.911/43.420秒）；原子ready夹具修正后重跑。
- Node30×3=90、Go race count3、六协议脚本各内置3轮通过；完整Chromium121×3=363通过，最终step16完整复制额外3通过，独立复制页剪贴板/下载/拒绝回退/手机3通过；初始360通过/3旧版本文案失败日志保留。
- 实际Faster0.5.4 resolver/prepare与生产generated-only decoder，ICL/xvector、chunk2/4/8/12，CPU注入prompt/talker/kernel/codec：确认参考标记从未入decoder、80帧153600样本、同路径重载提示更新；不是完整模型。
- 实际HF Qwen12Hz tiny随机decoder23813参数：chunk2/4/8/12 ×lookahead0/2，40帧76800样本，固定1920契约/有界窗口/因果前缀；没有训练codec权重或人声音频。
- 保留完整Faster/Qwen导入与2651参数tinyMimi保存重载，CPU tinyLoRA相对冻结13损失/全部adapter张量逐位一致；不把它们称为Qwen训练质量。
- CPU runtime探针真实HF smoke/API签名通过，无CUDA整体仍blocked。真实T4基准本沙箱未运行，target-rtf-not-run.json明确零测量/blocked。

## 初始失败与修正，不隐去

- 初次301项包含旧15纯向量断言、旧stream方法夹具、未重打包、旧probe调用清单失败。保留python-initial/second/third日志，显式向量兼容测试仍在，新增ICL默认隔离测试，没有删除关键检查。
- 新preflight改查实际_prepare_generation/fast_generate_streaming后，旧fake Backend签名需要同步；修正mock声明而非绕过真实API检查。
- 原生adapter HTTP回归首次拒绝：gateway按Mock/faster推断模式而测试实际注入原生adapter。改以发布档案sentence-buffered类型绑定原生模式，加Go回归；A→B→A三轮/损坏adapter拒播重跑通过。初始adapter_gateway_initial.txt保留。
- tiny真实decoder库导入会向stdout打印flash-attn提示，首轮文件不是纯JSON；原文件保留actual-codec-initial-round*.txt，脚本把库输出引到stderr后最终三轮重新生成纯JSON。
- 两次Go命令cwd误用失败（无模块/相对venv路径）；实际竞态检查使用明确绝对Go工具路径与gateway cwd，非把路径错误算通过。

## 未达到/仍需现场验证

没有用户实际噪声音频、训练权重和T4/DeepSeek通路，不能确定报告的两种声音/沙沙全部根因，不能给相似度百分比、真实速度改善倍数或RTF0.3已达结论。ICL转写正确性、多人参考、生成模型幻觉、真实窗口接缝、声纹/自然度与双GPU段间一致性均需真实三轮听测。

没有新增无依据语言重写或每卡第二模型，没有更改语速/删文/加静音充RTF。原文早触发、录音/取消/安全、手动校准、HF/Mimi修复和训练代码保持。历史独立网页真实训练闭环、维护租约切换、长录音完整审核对齐/全样本覆盖、真实训练保质吞吐、严格声学逐字拒播缺口仍未完成。51份完整备忘录已统一内嵌到KAGGLE_HANDOFF_PROMPT.md。
- 最终并行负载下Python第二轮发现既有训练控制器测试夹具ready文件先创建再写PID，父进程读到了空串；这是测试发布竞态而非已证实的生产租约错误。仅改测试夹具临时文件原子rename，并在启动前记录旧run目录，保留python-ready-race-round2.txt后完整重跑三轮；不放宽PID/锁释放断言。
- 首次完整浏览器三轮360通过/3失败，全部为旧step15测试仍断言release-note必须“第十五阶段”；当前确为第十六阶段。只更新版本文案断言并补ICL/真实RTF待测文案检查，原手动校准/默认关闭断言保留；初始日志browser-initial-repeat3.txt保留，完整三轮重跑，不把初始失败算通过。

### 计时解释
`model_stages.prepare_ms/codec_ms/token_decode_ms`与DSP计时是主机观察/后端计数，不是严格CUDA profiler分解；prepare未额外同步，prefill没有独立汇总字段，几项不能简单相加当总GPU耗时。标准gen_ms与HTTP wall包含生成器必要同步、codec CPU取回和实际输出等待；真实RTF门禁使用总墙钟与未填充speech_samples，不用局部计时冒充0.3。

---

## 内嵌备忘录：KAGGLE_STEP16_QUICKSTART.md

# step16 升级与真实双T4验收

## 完整代码

- `kaggle/kaggle-fixed-step16.py`：306580字节，52个完整内嵌资产。
- SHA256：`c6ed6c89e6356fc6c7ab554f96a2c3201a8e4690c007ea66626445cc658b4429`。
- 独立3001复制预览可“复制全部代码”或下载；不改正式3000工作台，不运行Python。
- 原始及step1–15保留，不再把15纯向量模式作为相似度改善的既定答案。

## 升级顺序

1. 先备份需要保留的私有录音、库、档案和adapter；不要删除原录音或手工删除锁文件。
2. 完整停止/重启Kaggle会话，选择T4×2，Internet On。不要让旧15进程与16共用同一GPU/ROOT。
3. 在Code单元格粘贴**完整16代码**运行。默认真实Faster/FP16、每T4一个模型；不要用QTTS_MOCK取得声学结论。保留HF/Mimi正常导入修复，不卸载Kaggle Torch。
4. 可在完整代码之前显式设置：

```python
import os
os.environ['QTTS_CLONE_MODE'] = 'icl'
os.environ['QTTS_MAX_GAIN_DB'] = '6'
os.environ['QTTS_CODEC_LOOKAHEAD_FRAMES'] = '0'
# 紧接着粘贴完整step16，不是只执行这几行。
```

5. 等待双worker ready，再启用已有普通声音档案。**参考音频应只有一个说话人，参考文本必须逐字匹配该锚点**，不是想让它新说的目标文字。选项/档案编辑入口仍在。ICL无转写会明确拒绝，不静默改成另一种声音。
6. 有ASR错字先审核转写。切换候选/修改转写时停止当前会话，再重新启用。若提示reference_saved但worker未全部就绪，保存已发生，需重试启用；不会以旧声音冒充成功。旧会话pin不符会在该段任何PCM前拒绝，已播旧段不能撤回。
7. 首先直接朗读与参考不同的短目标文，再试长文、跨句与两卡交替；最后试DeepSeek第一句及时开始。没有声学逐字拒播器，ICL仍可能产生音素/文字幻觉，不保证无添字或百分百相似。

## 沙沙声的处理边界

- 解码器不接参考码/参考PCM；没有参考呼吸拼接或低延迟占位。
- 只拼未提交生成样本；窗口左25帧有界，默认右前瞻0。真实tiny随机decoder的因果前缀实验通过，故未默认增加160ms前瞻；仅显式实验可设2。
- 每任务重置响度包络，避免上段/双卡历史状态不同；输出目标仍-18dBFS，默认最大向上增益6dB，保留软限幅。需要更响可现场对照9，极限12；底噪也可能被放大，不建议盲开最大值。
- 没有用户实际沙沙样本，不能断定来源是模型、参考噪声、录音环境还是播放链；没有强低通/强谱门掩盖问题，也不声称“已无沙沙”。比较同参考、同文、同seed的独立生成WAV，不把响度变小误判为音质一定变好。

## 真正RTF≤0.3：目标机三轮实验

新工具只调用**已经驻留的两张真实GPU worker**，不启动第三模型。启动完成后可在同Notebook后续Code单元格运行；bootstrap会返回，supervisor在后台。先停止网页合成，确认空闲，填写界面实际档案ID（不是显示名称），输出目录每次用新名称：

```python
import subprocess, sys
subprocess.run([
    sys.executable, '/kaggle/working/qtts/tools/voice_benchmark.py',
    '--run', '--profile', '填写实际档案ID', '--rounds', '3', '--chunk-size', '8',
    '--output', '/kaggle/working/qtts/state/benchmarks/step16-run1/report.json',
], check=False)
```

ROOT或STATE自定义时用实际路径，并让工具继承相同QTTS环境。输出保留在私有state，不能自动上传或共享。

- 两worker必须ready/idle/model_loaded、Faster真实引擎、ICL-generated-only模式、GPU0/1分别独占可见；否则blocked。
- 先单独记录参考提示预热时间，再测3轮×2卡×3段=18条；保存18个生成WAV、逐条原始`measurements.jsonl`与report。后续失败不会删除先前慢行或WAV。
- 标准RTF=`gen_ms/1000/(speech_samples/24000)`，wall RTF包括HTTP/排队/必需等待。分母排除lead/tail/fade填充，失败/取消/anomaly不算成功。`rtf_x`是倒数，不是RTF。
- 任一条worker或wall RTF>0.3均`target-not-met`、退出2；全部满足也只是`measured-speed-only`，**不是音色/无噪声/自然度验收**。
- 不带`--run`时输出blocked、零测量，不会以CPU或Mock替代。这个沙箱当前没有真实T4结果，不能声称0.3已经做到。
- 对比chunk4/8/12请各用新的输出目录、相同参考/文本与seed，保留慢结果；只在试听合格前提下选更快配置。两卡吞吐不能相加冒充单卡RTF，不能改语速/删文/加静音。

## 真正声学验收仍必需

每张卡/每段分别核查：像参考单人、段间一致、自然易懂、无异常沙沙、没有播放参考内容、没有添字漏字；再检查first_played_ms与underruns。声纹余弦分数不能当“99.5%相似”；工程回归与tiny随机权重均不能替代训练权重试听。网页训练闭环、长数据全覆盖、真实双T4训练提速与严格声学拒播等历史缺口仍未完成。

---

## 内嵌备忘录：KAGGLE_STEP17_REVIEW1.md

# 第十七阶段第1轮专题研究：100条建议

本轮前50条针对新问题，后50条复核已成功链路。全源读取/哈希/Python AST不等于逐行语义无错。

1. [S17-R1-001] `截图与根因`：截图是15而非16不能当新包效果。
2. [S17-R1-002] `截图与根因`：录音限额与锚点限额分开。
3. [S17-R1-003] `截图与根因`：重现单个28.7秒ASR段。
4. [S17-R1-004] `截图与根因`：保留16的逐字匹配约束。
5. [S17-R1-005] `截图与根因`：不能将长音频硬截配全文。
6. [S17-R1-006] `截图与根因`：保留ASR词级时间戳。
7. [S17-R1-007] `截图与根因`：按完整词组而非字符比例切分。
8. [S17-R1-008] `截图与根因`：词与原段文本必须核对。
9. [S17-R1-009] `截图与根因`：缺词时间走音频窗口重新ASR。
10. [S17-R1-010] `截图与根因`：不能凭低RMS断定无人声。
11. [S17-R1-011] `词级对齐`：验证时间戳有限。
12. [S17-R1-012] `词级对齐`：验证起止单调。
13. [S17-R1-013] `词级对齐`：验证不越源音频。
14. [S17-R1-014] `词级对齐`：拒绝重叠倒序词。
15. [S17-R1-015] `词级对齐`：Unicode字母数字核对转写。
16. [S17-R1-016] `词级对齐`：不要丢标点后汉字。
17. [S17-R1-017] `词级对齐`：长单词超窗口重新ASR。
18. [S17-R1-018] `词级对齐`：短尾保留在分析收据。
19. [S17-R1-019] `词级对齐`：跨文件绝不合并文字。
20. [S17-R1-020] `词级对齐`：对齐失败有明确中文建议。
21. [S17-R1-021] `长音频重识别`：仅问题长段需要窗口ASR。
22. [S17-R1-022] `长音频重识别`：每窗口音频和转写独立匹配。
23. [S17-R1-023] `长音频重识别`：使用原音频实际切片。
24. [S17-R1-024] `长音频重识别`：偏移恢复绝对时间。
25. [S17-R1-025] `长音频重识别`：边界优先静音。
26. [S17-R1-026] `长音频重识别`：窗口必须前进不死循环。
27. [S17-R1-027] `长音频重识别`：最末窗口不丢。
28. [S17-R1-028] `长音频重识别`：无语音窗口不伪造文字。
29. [S17-R1-029] `长音频重识别`：沿用ASR锁及CPU复用。
30. [S17-R1-030] `长音频重识别`：进度显示窗口计数。
31. [S17-R1-031] `长参考语义`：长录音可以超过15秒。
32. [S17-R1-032] `长参考语义`：不能无限把20分钟塞进ICL。
33. [S17-R1-033] `长参考语义`：提供16与24秒参考窗口。
34. [S17-R1-034] `长参考语义`：默认16保护旧短样本。
35. [S17-R1-035] `长参考语义`：24明确标为实验与较慢。
36. [S17-R1-036] `长参考语义`：手工转写仅单短文件直接采用。
37. [S17-R1-037] `长参考语义`：长手工全文不能按时长分配。
38. [S17-R1-038] `长参考语义`：记录源总时长与选中锚点。
39. [S17-R1-039] `长参考语义`：记录重切分和重识别数量。
40. [S17-R1-040] `长参考语义`：明确建档不是全数据训练。
41. [S17-R1-041] `输入与安全`：窗口值只允许16或24。
42. [S17-R1-042] `输入与安全`：表单和库入口都独立校验。
43. [S17-R1-043] `输入与安全`：失败保留本地录音。
44. [S17-R1-044] `输入与安全`：取消不得删除源音频。
45. [S17-R1-045] `输入与安全`：不自动云传原音。
46. [S17-R1-046] `输入与安全`：拒绝非有限PCM。
47. [S17-R1-047] `输入与安全`：保留20分钟录音预算。
48. [S17-R1-048] `输入与安全`：低电平提示调整设备。
49. [S17-R1-049] `输入与安全`：提示麦克风距离不替人猜设备。
50. [S17-R1-050] `输入与安全`：保留原始至16冻结。
51. [S17-R1-051] `档案变更`：修正候选更换原路径复用。
52. [S17-R1-052] `档案变更`：文本更改触发提示失效。
53. [S17-R1-053] `档案变更`：手动校准选择不能覆盖回旧。
54. [S17-R1-054] `档案变更`：完成后保存阶段收据。
55. [S17-R1-055] `档案变更`：删除档案不能被旧请求静默复活。
56. [S17-R1-056] `档案变更`：不删除冻结15。
57. [S17-R1-057] `档案变更`：旧档案可重新加载。
58. [S17-R1-058] `档案变更`：参考需审核逐字转写。
59. [S17-R1-059] `档案变更`：ASR提案不是人工真值。
60. [S17-R1-060] `档案变更`：不从短片猜长文。
61. [S17-R1-061] `安全读取`：锚点仅单一安全文件名。
62. [S17-R1-062] `安全读取`：拒绝符号链接。
63. [S17-R1-063] `安全读取`：拒绝目录冒音频。
64. [S17-R1-064] `安全读取`：限制参考读取字节。
65. [S17-R1-065] `安全读取`：路径始终在档案目录。
66. [S17-R1-066] `安全读取`：哈希不输出原音频。
67. [S17-R1-067] `安全读取`：指纹不是授权证明。
68. [S17-R1-068] `安全读取`：不泄漏访问口令。
69. [S17-R1-069] `安全读取`：不自动云传录音。
70. [S17-R1-070] `安全读取`：保持私有备份边界。
71. [S17-R1-071] `原生adapter`：保留训练候选固定binding。
72. [S17-R1-072] `原生adapter`：不向faster注入adapter。
73. [S17-R1-073] `原生adapter`：不修改训练权重。
74. [S17-R1-074] `原生adapter`：缺adapter不回退Base。
75. [S17-R1-075] `原生adapter`：保留句级缓冲标记。
76. [S17-R1-076] `原生adapter`：继续核对Base哈希。
77. [S17-R1-077] `原生adapter`：旧训练功能做回归。
78. [S17-R1-078] `原生adapter`：不要把参考处理叫训练。
79. [S17-R1-079] `原生adapter`：网页真实训练缺口保留。
80. [S17-R1-080] `原生adapter`：真实训练质量仍待验收。
81. [S17-R1-081] `相似度验收`：相似度用真实说话人模型。
82. [S17-R1-082] `相似度验收`：不能伪造99.5百分比。
83. [S17-R1-083] `相似度验收`：文字一致不代表音色一致。
84. [S17-R1-084] `相似度验收`：多段输出分别试听。
85. [S17-R1-085] `相似度验收`：比较两卡相邻段。
86. [S17-R1-086] `相似度验收`：使用与参考不同的目标文字。
87. [S17-R1-087] `相似度验收`：同参考同文同seed对照。
88. [S17-R1-088] `相似度验收`：保留参考与输出独立文件。
89. [S17-R1-089] `相似度验收`：无用户音频不猜根因。
90. [S17-R1-090] `相似度验收`：不承诺100无错。
91. [S17-R1-091] `保护已有功能`：保留原文分段。
92. [S17-R1-092] `保护已有功能`：保留首句及时调度。
93. [S17-R1-093] `保护已有功能`：保留两主视图。
94. [S17-R1-094] `保护已有功能`：保留长录音预算。
95. [S17-R1-095] `保护已有功能`：保留命名空库。
96. [S17-R1-096] `保护已有功能`：保留失败本地片段。
97. [S17-R1-097] `保护已有功能`：保留手动候选校准。
98. [S17-R1-098] `保护已有功能`：保留DeepSeek取消。
99. [S17-R1-099] `保护已有功能`：保留3000正式工作台。
100. [S17-R1-100] `保护已有功能`：保留原始至15整包。

---

## 内嵌备忘录：KAGGLE_STEP17_REVIEW2.md

# 第十七阶段第2轮专题研究：100条建议

本轮前50条针对新问题，后50条复核已成功链路。全源读取/哈希/Python AST不等于逐行语义无错。

1. [S17-R2-001] `短参考与音色`：继续使用ICL匹配文本。
2. [S17-R2-002] `短参考与音色`：不退回15纯向量默认。
3. [S17-R2-003] `短参考与音色`：新旧GPU不能混版本。
4. [S17-R2-004] `短参考与音色`：相同参考绑定采样参数。
5. [S17-R2-005] `短参考与音色`：Go和Python浮点编码一致。
6. [S17-R2-006] `短参考与音色`：缺省参数也计入指纹。
7. [S17-R2-007] `短参考与音色`：不接受NaN温度。
8. [S17-R2-008] `短参考与音色`：改温度使旧会话失效。
9. [S17-R2-009] `短参考与音色`：参数相同不是音色绝对相同。
10. [S17-R2-010] `短参考与音色`：真人试听仍是独立门禁。
11. [S17-R2-011] `多卡参数`：绑定temperature。
12. [S17-R2-012] `多卡参数`：绑定top_k。
13. [S17-R2-013] `多卡参数`：绑定top_p。
14. [S17-R2-014] `多卡参数`：绑定repetition_penalty。
15. [S17-R2-015] `多卡参数`：top_k必须整数。
16. [S17-R2-016] `多卡参数`：统一默认参数数值。
17. [S17-R2-017] `多卡参数`：每次合成锁内复核。
18. [S17-R2-018] `多卡参数`：预计算提示快照保留。
19. [S17-R2-019] `多卡参数`：不混用不同条件模式。
20. [S17-R2-020] `多卡参数`：不声称两卡波形逐位相同。
21. [S17-R2-021] `参考质量`：记录原始RMS。
22. [S17-R2-022] `参考质量`：记录原始峰值。
23. [S17-R2-023] `参考质量`：记录SNR估计而非真值。
24. [S17-R2-024] `参考质量`：低电平给风险提示不直接拒绝。
25. [S17-R2-025] `参考质量`：响度归一化不是降噪。
26. [S17-R2-026] `参考质量`：MFCC相似不是可靠声纹真值。
27. [S17-R2-027] `参考质量`：避免强降噪损伤辅音。
28. [S17-R2-028] `参考质量`：参考多人必须审核。
29. [S17-R2-029] `参考质量`：24秒未必比10秒好。
30. [S17-R2-030] `参考质量`：不播放原录音补相似度。
31. [S17-R2-031] `连续朗读`：只调整朗读聚合不延后聊天首句。
32. [S17-R2-032] `连续朗读`：减少过多独立合成语段。
33. [S17-R2-033] `连续朗读`：优先完整句子标点。
34. [S17-R2-034] `连续朗读`：保留原始全文字符。
35. [S17-R2-035] `连续朗读`：不合并不同用户任务。
36. [S17-R2-036] `连续朗读`：保留取消和背压。
37. [S17-R2-037] `连续朗读`：不跨词叠加PCM。
38. [S17-R2-038] `连续朗读`：不删除语音以隐藏接缝。
39. [S17-R2-039] `连续朗读`：保留已有codec有界上下文。
40. [S17-R2-040] `连续朗读`：自然韵律不能仅靠交叉淡化保证。
41. [S17-R2-041] `噪声边界`：继续禁参考呼吸拼接。
42. [S17-R2-042] `噪声边界`：不生成白噪声补停顿。
43. [S17-R2-043] `噪声边界`：保留软限幅。
44. [S17-R2-044] `噪声边界`：保留可控增益。
45. [S17-R2-045] `噪声边界`：不把静音当去噪成功。
46. [S17-R2-046] `噪声边界`：不默认低通抹齿音。
47. [S17-R2-047] `噪声边界`：新统计不得泄漏原文本。
48. [S17-R2-048] `噪声边界`：生成WAV可供独立试听。
49. [S17-R2-049] `噪声边界`：缺真实音频不宣布零噪声。
50. [S17-R2-050] `噪声边界`：不得缩短输出冒RTF达标。
51. [S17-R2-051] `RTF定义`：标准RTF等于生成墙钟除语音秒数。
52. [S17-R2-052] `RTF定义`：rtf_x是其倒数不是RTF。
53. [S17-R2-053] `RTF定义`：不把双卡速度相加冒单卡RTF。
54. [S17-R2-054] `RTF定义`：排除零停顿分母。
55. [S17-R2-055] `RTF定义`：失败取消样本不能算通过。
56. [S17-R2-056] `RTF定义`：冷预热与热态分开。
57. [S17-R2-057] `RTF定义`：首播与吞吐分开。
58. [S17-R2-058] `RTF定义`：记录每GPU结果。
59. [S17-R2-059] `RTF定义`：目标0.3需每条和汇总检查。
60. [S17-R2-060] `RTF定义`：无T4输出blocked。
61. [S17-R2-061] `计时拆分`：模型prepare单独计时。
62. [S17-R2-062] `计时拆分`：token生成单独计时。
63. [S17-R2-063] `计时拆分`：codec解码单独计时。
64. [S17-R2-064] `计时拆分`：DSP耗时单列。
65. [S17-R2-065] `计时拆分`：总墙钟包括必要同步。
66. [S17-R2-066] `计时拆分`：不拿CPU异步发射当CUDA完成。
67. [S17-R2-067] `计时拆分`：预热不计入热态却单独报告。
68. [S17-R2-068] `计时拆分`：报告first_played与欠载。
69. [S17-R2-069] `计时拆分`：保存原始测量行。
70. [S17-R2-070] `计时拆分`：不删慢样本。
71. [S17-R2-071] `性能选择`：仍用CUDA graph后端。
72. [S17-R2-072] `性能选择`：不盲开torch.compile。
73. [S17-R2-073] `性能选择`：T4继续FP16。
74. [S17-R2-074] `性能选择`：不假称T4原生BF16。
75. [S17-R2-075] `性能选择`：不为语言数量加网络跳转。
76. [S17-R2-076] `性能选择`：不每卡塞两副本。
77. [S17-R2-077] `性能选择`：上下文有界减少复制。
78. [S17-R2-078] `性能选择`：参考prompt按版本复用。
79. [S17-R2-079] `性能选择`：较大后段chunk做可选实测。
80. [S17-R2-080] `性能选择`：质量不降需要真实对照。
81. [S17-R2-081] `实验设计`：同一参考与目标文。
82. [S17-R2-082] `实验设计`：至少三轮独立进程接口实验。
83. [S17-R2-083] `实验设计`：每个chunk2/4/8/12检查。
84. [S17-R2-084] `实验设计`：检查短尾与取消。
85. [S17-R2-085] `实验设计`：参考码标记不能入decoder。
86. [S17-R2-086] `实验设计`：生成总帧对应总样本。
87. [S17-R2-087] `实验设计`：检查窗口峰值上限。
88. [S17-R2-088] `实验设计`：性能fixture不算Qwen性能。
89. [S17-R2-089] `实验设计`：CPU tinyMimi不算完整TTS。
90. [S17-R2-090] `实验设计`：硬件结果不能编造。
91. [S17-R2-091] `降级与边界`：新解码模式不自动回旧混参考路径。
92. [S17-R2-092] `降级与边界`：ICL缺文本给明确提示。
93. [S17-R2-093] `降级与边界`：不要静默改为别的声音。
94. [S17-R2-094] `降级与边界`：不要自动降模型大小。
95. [S17-R2-095] `降级与边界`：不改语速充RTF。
96. [S17-R2-096] `降级与边界`：不删用户正文充速度。
97. [S17-R2-097] `降级与边界`：不缩减训练数据。
98. [S17-R2-098] `降级与边界`：保留故障监督。
99. [S17-R2-099] `降级与边界`：记下每次初始失败。
100. [S17-R2-100] `降级与边界`：整体仍按证据判定。

---

## 内嵌备忘录：KAGGLE_STEP17_REVIEW3.md

# 第十七阶段第3轮专题研究：100条建议

本轮前50条针对新问题，后50条复核已成功链路。全源读取/哈希/Python AST不等于逐行语义无错。

1. [S17-R3-001] `重现门禁`：单个28.7秒词级段建档成功。
2. [S17-R3-002] `重现门禁`：单个60秒段词级切分。
3. [S17-R3-003] `重现门禁`：20分钟时间戳规划有界。
4. [S17-R3-004] `重现门禁`：缺词时间戳实际窗口重识别。
5. [S17-R3-005] `重现门禁`：文本不匹配必须回识别。
6. [S17-R3-006] `重现门禁`：长manual全文不错误拼接。
7. [S17-R3-007] `重现门禁`：短manual16秒保持兼容。
8. [S17-R3-008] `重现门禁`：24秒锚点不越界。
9. [S17-R3-009] `重现门禁`：无声和非法时间戳不造成功。
10. [S17-R3-010] `重现门禁`：每项做三轮回归。
11. [S17-R3-011] `接口门禁`：浏览器发送参考窗口字段。
12. [S17-R3-012] `接口门禁`：默认值16可见。
13. [S17-R3-013] `接口门禁`：24选项真实进入后端。
14. [S17-R3-014] `接口门禁`：锁定清除私有转写。
15. [S17-R3-015] `接口门禁`：表单非法值拒绝。
16. [S17-R3-016] `接口门禁`：库处理同样校验。
17. [S17-R3-017] `接口门禁`：服务重启新包版本可识别。
18. [S17-R3-018] `接口门禁`：新包逐字节复制。
19. [S17-R3-019] `接口门禁`：16包哈希冻结。
20. [S17-R3-020] `接口门禁`：正式工作台保持不变。
21. [S17-R3-021] `参数指纹测试`：中英转写跨语言一致。
22. [S17-R3-022] `参数指纹测试`：默认值与显式默认相同。
23. [S17-R3-023] `参数指纹测试`：四参数分别变更使pin变化。
24. [S17-R3-024] `参数指纹测试`：NaN和无穷拒绝。
25. [S17-R3-025] `参数指纹测试`：非整数top_k拒绝。
26. [S17-R3-026] `参数指纹测试`：Worker不输出不符pin的PCM。
27. [S17-R3-027] `参数指纹测试`：Go协议携带固定pin。
28. [S17-R3-028] `参数指纹测试`：不改adapter来源绑定。
29. [S17-R3-029] `参数指纹测试`：新旧包混跑明确重启。
30. [S17-R3-030] `参数指纹测试`：不把指纹当身份认证。
31. [S17-R3-031] `验证与实验`：Python完整三轮。
32. [S17-R3-032] `验证与实验`：Node完整三轮。
33. [S17-R3-033] `验证与实验`：Go race三轮。
34. [S17-R3-034] `验证与实验`：Chromium完整三轮。
35. [S17-R3-035] `验证与实验`：六服务协议各三轮。
36. [S17-R3-036] `验证与实验`：实际Faster控制接口三轮。
37. [S17-R3-037] `验证与实验`：真实tiny codec三轮。
38. [S17-R3-038] `验证与实验`：Mimi导入重载三轮。
39. [S17-R3-039] `验证与实验`：CPU训练等价三轮。
40. [S17-R3-040] `验证与实验`：所有CPU模型明确不是Qwen音质证据。
41. [S17-R3-041] `记录与交付`：问题22回答后给50建议。
42. [S17-R3-042] `记录与交付`：问题23回答后给50建议。
43. [S17-R3-043] `记录与交付`：问题24回答后给50建议。
44. [S17-R3-044] `记录与交付`：方案先于产品修改。
45. [S17-R3-045] `记录与交付`：每次失败日志保留。
46. [S17-R3-046] `记录与交付`：逐条300建议分类。
47. [S17-R3-047] `记录与交付`：无硬件保留BLOCKED。
48. [S17-R3-048] `记录与交付`：真实RTF0.3仍需测量。
49. [S17-R3-049] `记录与交付`：完整57份备忘录内嵌。
50. [S17-R3-050] `记录与交付`：不承诺100相似零噪声。
51. [S17-R3-051] `浏览器文案`：显示ICL条件不等于回放参考。
52. [S17-R3-052] `浏览器文案`：显示音色尚需试听。
53. [S17-R3-053] `浏览器文案`：显示RTF目标未达证据。
54. [S17-R3-054] `浏览器文案`：保留参考文本编辑。
55. [S17-R3-055] `浏览器文案`：提示转写必须匹配。
56. [S17-R3-056] `浏览器文案`：不新增假训练按钮。
57. [S17-R3-057] `浏览器文案`：不显示100相似度。
58. [S17-R3-058] `浏览器文案`：性能诊断不藏慢行。
59. [S17-R3-059] `浏览器文案`：手机无横向溢出。
60. [S17-R3-060] `浏览器文案`：锁定清空私有文本。
61. [S17-R3-061] `包与版本`：新step16独立文件。
62. [S17-R3-062] `包与版本`：原始至15冻结。
63. [S17-R3-063] `包与版本`：repack逐资产哈希。
64. [S17-R3-064] `包与版本`：内嵌新解码模块。
65. [S17-R3-065] `包与版本`：内嵌新RTF实验入口。
66. [S17-R3-066] `包与版本`：剪贴板全量读回。
67. [S17-R3-067] `包与版本`：下载逐字节核对。
68. [S17-R3-068] `包与版本`：权限拒绝可全选。
69. [S17-R3-069] `包与版本`：复制页固定新hash。
70. [S17-R3-070] `包与版本`：正式工作台不覆盖。
71. [S17-R3-071] `备忘录`：先计划后改产品。
72. [S17-R3-072] `备忘录`：问题19后给50建议。
73. [S17-R3-073] `备忘录`：问题20后给50建议。
74. [S17-R3-074] `备忘录`：问题21后给50建议。
75. [S17-R3-075] `备忘录`：累计问题建议保留。
76. [S17-R3-076] `备忘录`：最终交接完整内嵌。
77. [S17-R3-077] `备忘录`：原失败日志不覆盖。
78. [S17-R3-078] `备忘录`：状态用PARTIAL与BLOCKED。
79. [S17-R3-079] `备忘录`：缺硬件不得改成已达标。
80. [S17-R3-080] `备忘录`：不要求用户提供密钥。
81. [S17-R3-081] `真实声学`：多人参考不是调参可解决。
82. [S17-R3-082] `真实声学`：ICL能改善但非保证。
83. [S17-R3-083] `真实声学`：声纹分数不是听感真值。
84. [S17-R3-084] `真实声学`：模型仍可幻觉添字。
85. [S17-R3-085] `真实声学`：跨语言可能改变口音。
86. [S17-R3-086] `真实声学`：沙沙声需实际音频定位。
87. [S17-R3-087] `真实声学`：不从一张截图断定频谱。
88. [S17-R3-088] `真实声学`：静音延迟不算首声。
89. [S17-R3-089] `真实声学`：质量与速度一起验收。
90. [S17-R3-090] `真实声学`：人声自然度需独立试听。
91. [S17-R3-091] `后续门禁`：优先真实T4不同文本试听。
92. [S17-R3-092] `后续门禁`：逐GPU比较同参考。
93. [S17-R3-093] `后续门禁`：测试候选切换中取消。
94. [S17-R3-094] `后续门禁`：测RTF中位和最慢。
95. [S17-R3-095] `后续门禁`：参考泄漏单独核查。
96. [S17-R3-096] `后续门禁`：新进程重载检查。
97. [S17-R3-097] `后续门禁`：私有音频自行备份。
98. [S17-R3-098] `后续门禁`：历史网页训练闭环未完成。
99. [S17-R3-099] `后续门禁`：长样本全覆盖未完成。
100. [S17-R3-100] `后续门禁`：不把工程通过称全部目标完成。

---

## 内嵌备忘录：KAGGLE_STEP17_PLAN.md

# 第十七阶段具体方案（产品修改前）

## 已查明与未知
截图为15，28.7秒录音/RMS约-46.6dBFS/峰0.014，实际报错发生在候选选择，不是录音上传上限。16源码仍忽略ASR已有词级时间戳；单个超过16秒的ASR段无法成为候选。这是可复现的代码缺陷。未收到实际WAV、没有CUDA/训练权重，不能确定沙沙和音色的全部声学根因。

三轮全源读取/AST/哈希及专题审查各100建议已记录；不是穷尽无错证明。问题22→23→24各50建议，累计24题1200建议，记录具体选项/推荐/边界。不询问用户，不承诺100%信心。

## 实施顺序
1. 冻结原始–16和正式工作台，新建17；先复现28.7秒单ASR段失败。
2. 新reference_segments模块：完整保存词级时间，验证词文一致、有限/单调/边界，按完整词切分长段。缺失/不可信的长段对实际音频窗口重新ASR，恢复绝对时间，优先静音边界；不按字数/时长比例分配全文。进度及数量收据；保留ASR全周期锁。
3. 快速建档与库处理均支持16（默认）/24秒（较长参考实验）窗口。长录音仍完整分析并择优，不把20分钟全塞进ICL；单个短文件手工转写直用保持，长manual全文明确自动时间戳转写而非强制对齐。记录源时长、锚点时长、切分/重识别统计。
4. 低输入电平记录RMS/峰值及风险提示，不以小波形认定无声，不强加损音质滤波。保持16 ICL/生成码专用codec/提示快照/禁参考PCM拼接；建档不是训练，更长不保证更像。
5. 参考指纹升级v2，同时绑定四项有效生成参数。Python/Go采用IEEE754小端double规范字节，默认与显式默认一致，拒绝非法/非有限参数。改参数使旧会话失效，避免两卡不同缓存参数；不是声学身份/逐位波形保证。
6. 只朗读模式适度增大自然标点聚合，减少独立合成重启；保留完整正文、取消/背压/顺序和DeepSeek首句早触发。不要跨词叠加PCM或删字掩盖接缝；真实自然度仍须试听。
7. 三轮完整Python/Node/Go race/Chromium/六协议及实际Faster接口、tiny codec/Mimi、CPU训练等价；新增28.7/60/1200秒对齐、缺词重识别、16/24、指纹参数/非法值测试。CPU/Mock不当Qwen声学证明。
8. 更新17完整复制页、全资产校验、下载/剪贴板/手机/权限回退。57份备忘录完整内嵌最终提示词，错误日志与未完成项保留。

## 验收边界
超长采集/对齐修复可工程验证；实际短/长参考相似度、零沙沙、双卡音色完全一致、自然整段韵律和先前RTF≤0.3均需真实双T4与音频。保留硬件BLOCKED，不用合成信号宣布这些目标完成。不无依据新增C++/Java/SQL服务；现有Python/PyTorch/CUDA、Go、Rust、JS分工保持。

## 完成记录（工程范围）

上述8步已落实，原始–16及正式15文件保留。最终Python334×3、Node30×3、Go race3、六协议各三轮、Chromium123×3及完整复制另3通过。冻结16与17相同29秒fixture对照、实际Faster接口/随机tiny codec/完整导入tinyMimi/CPU训练逐位等价各三轮通过。最终全资产逐字节、固定hash复制/下载、57份备忘录、24题各50及冻结文件核对见`validation/step17/final-checks.json`。

工程计划完成不等于所有用户目标完成：没有真实用户录音/完整语音权重/T4证据，仍不签收相似度、零噪声、同卡/跨卡音色、自然完整朗读或RTF≤0.3。历史训练闭环/长数据覆盖/实际吞吐/声学逐字拒播缺口未解决；总体PARTIAL/BLOCKED、目标22/300不变。

---

## 内嵌备忘录：KAGGLE_STEP17_AUDIT.md

# 第十七阶段审计

## 状态与产物

工程修复及最终三轮回归通过；整体**PARTIAL/BLOCKED**。不得称高相似、零噪声、双卡声学完全一致、完整朗读自然度或真实RTF≤0.3已验收。最终收据以validation/step17/final-checks.json为准。

完整包`kaggle/kaggle-fixed-step17.py`，313504B、53资产，SHA256 `6eacaede14f9b5f42ac5c334df5c3f9d1a1c6858fb69b7d3a8ff241ec60427ea`。原始–16与正式工作台冻结。

## 源码确认的缺陷及修复

- 截图是15；现场28.7秒、RMS约-46.6dBFS/peak0.014。上传限额不是15秒；失败处是旧候选仅接受完整2.5–16秒ASR段，忽略words。不能据截图认定无语音或设备故障。
- `reference_segments.py`验证有限/单调/源范围/词文一致，用完整词组切长段；不可信长词时间对实际窗口重ASR，恢复绝对偏移，低能边界优先，短尾留收据，不按字数/时长分全文。短段可保留段级ASR但丢无效可选word元数据，避免后续停顿分析崩溃。ASR依旧不是人工真值。
- `analyst.py/library_api.py/web`都支持16默认/24实验窗口；长manual全文不强配短音频。候选补边不得超窗口，质量记录源总时长、候选时长、切分/重识别计数和非训练声明。默认短manual16秒不回归。
- 原始非有限PCM拒绝；记录归一化前RMS/peak。低于-40dBFS仅给输入距离/增益风险提示，不直接判无声；提示进入现有处理决策显示。没有强滤波损伤辅音或播放参考原音。
- `voice_binding.py/session.go`升级v2：音频/转写/语言加四有效生成参数，规范小端IEEE754 doubles，显式默认与缺省相同，拒绝非法/NaN/Inf/非整数top_k。Worker原有锁内复核/提示快照/模式pin保持；旧会话及混版本须重启。相同条件不保证跨GPU数值或音色完全相同。
- `ReadSegCfg`只朗读增大聚合，FirstMin12/FirstMax24/Min20/Target40/Max80；正文保持、聊天Live首句不变。减少独立重启不是跨段联合建模；可能更慢或降低并行，真实自然度仍待试听。不跨词交叉淡化、不删文。

## 新验证及实验设计

- 最终Python334项×3=1002通过；新增12项覆盖28.7/60/1200秒、缺词重识别实际样本、非法词时间、16/24手工匹配、低输入提示、表单非法值、生成参数pin。
- `long_reference_check.py`从冻结16提取真实build_profile同控制流，对同一29秒合成PCM、28.7秒ASR词段：16复现no aligned，17建档成功并实际读回候选WAV帧数/采样率；缺词实际窗口样本总数完整。ASR/说话人是显式fixture，不是实际Whisper或语音质量。
- 实际Faster resolver/prepare/生成码decoder、真实tiny随机codec、完整Qwen/Mimi导入重载、CPU LoRA对13损失/adapter逐位等价均三轮回归；完整训练权重、GPU、真实人声未执行。
- Node30×3=90、Go race3、六服务协议各三轮、完整Chromium123×3=369、最终整包复制另3、copy页/下载/拒绝回退/手机3均通过。独立3001不改正式3000。

## 初始失败与纠错，保留日志

1. 初次322检查4失败：旧测试to16k替身用24k除2得到12k，新增时长校验正确拒绝伪16k。将测试替身改真实2/3样本比；没有放宽生产时间边界。旧v1固定哈希更新为v2跨语言样本。
2. 旧“长段一律拒绝”断言改为“无可信窗口时间不配全文”；新增旧16失败/17成功对照，不删除拒绝错误对齐的测试。
3. 首次向studio测试写文件的临时编辑脚本误对字符串调用write_text，未写入该文件；后续已正确追加17完整包测试。不是浏览器或产品成功证据。
4. 长参考对照脚本初次stdout混入预期基线失败日志，文件保留long-reference-initial-round*.txt；脚本将库日志导向stderr，三轮重新生成纯JSON。基线错误是预期复现，不是17失败被藏。
5. 低输入提示最初只在API质量字段，最终也合并到已有decision显示，并新增实测合成低电平回归；最终334项重新跑三轮，保留之前333项日志。

## 审查、备忘录与边界

三轮100条见REVIEW1/2/3；全源读取/AST/哈希不等于穷尽语义无错。问题22–24各50建议，累计24题1200建议；处置逐条见review-disposition.json，不将300建议当300bug或全部新功能。最终提示词完整内嵌57份备忘录。

没有用户WAV、Whisper/Qwen训练权重和真实T4，不能保证所有合法录音一定被正确转写，也不能验证声纹/沙沙/自然接缝。长参考可增加重复/噪声和prefill，24实验不能叫质量必提升。参考PCM绝不播放；15向量模式不恢复为默认。先前真实RTF0.3、训练闭环、长数据全覆盖、真实双卡训练吞吐、声学逐字拒播缺口不豁免；完整目标22/300不升级。多语言按实际热路径用，不无证据重写稳定模块。

---

## 内嵌备忘录：KAGGLE_STEP17_QUICKSTART.md

# step17：长录音建档、较长参考与双卡一致性

## 完整代码与升级

`kaggle/kaggle-fixed-step17.py`：313504字节、53个完整内嵌资产。
SHA256：`6eacaede14f9b5f42ac5c334df5c3f9d1a1c6858fb69b7d3a8ff241ec60427ea`。
独立3001预览支持复制全部/下载，不改正式3000工作台。原始–16包均冻结。

**截图标题明确是第十五阶段，不是17。只刷新旧页面不会更新服务端。** 先备份私有录音/档案/adapter，完整停止并重启Kaggle会话，T4×2/Internet On，将完整17粘到Code单元格运行。不要让15/16/17进程混用同一GPU或ROOT；不要删除锁文件或卸载Kaggle Torch。网页应显示“第十七阶段”。指纹已升级v2，旧会话必须停止后重启。

## 超过15秒的现场录音

1. 录音采集/上传上限仍是默认单段1200秒、累计1800秒；不是16秒上限。失败时本地录音保留。
2. 停止采集后打开“选项”。默认模型参考窗口16秒；需要比较较长上下文时选24秒实验选项，再点创建。声音库处理也有16/24秒选择。
3. 17会先使用实际ASR词级时间戳拆长段；词与段文字不一致或缺时间时，对实际音频窗口重新识别，不按字数/时长比例猜转写。长段不再仅因超过16秒就被直接拒绝。
4. 提供手工文本时，单个文件时长≤所选窗口可直接采用，应逐字匹配录音。超过窗口的长全文不会被强行分配给短片段，改用ASR时间戳并留下收据。ASR不是人工真值，仍应审核选中锚点转写。
5. 进度会显示重识别窗口；实际ASR重试可能更慢。若输入无声、重识别仍无有效语音或时间戳不可信，会明确失败而不伪造“成功”。

### 长录音不等于更长模型提示，更不等于训练

长录音用于完整分析、选代表性片段；模型实际用选中的锚点，窗口上限16/24秒，不能把20分钟直接塞进ICL。`quality.reference_context`记录源时长、候选实际时长和`model_trained=false`，`quality.asr[].alignment`记录词切分/重识别窗口。20分钟规划测试不代表已用真实20分钟语音或Whisper权重做质量验收。更长参考可能更慢或增加不必要韵律，不保证比干净10秒更像。

## 短参考不像／沙沙声

- 继续采用16已恢复的匹配转写ICL，codec仅解码新生成码；没有参考PCM/呼吸片段拼接，也没有播放原音充相似度。
- 首先审核实际锚点只有一个人、没有音乐/背景人声、没有削波，转写与该片段逐字对应；录音长不是这几项的替代。
- 截图RMS约-46.6dBFS、峰0.014仅说明输入很轻，不能证明无人声或确定设备原因。17记录原始RMS/峰值，对很轻输入在现有处理决策里提示检查距离和输入增益。归一化也会放大底噪，不是去噪。
- 保留目标-18dBFS、最大增益默认6dB（QTTS_MAX_GAIN_DB可0..12）、软限幅。没有默认强低通/跨词重叠；不把齿音、气声抹掉冒充降噪。
- 没有用户实际WAV和真实权重试听证据，不能声称已经“零噪声”或100%相似；训练模型仍可能幻觉添字。

## 双卡与衔接

参考指纹v2包含音频、转写、语言和有效temperature/top_k/top_p/repetition_penalty；Go/Python使用相同小端IEEE754字节。默认与显式默认一致，参数改变使旧会话失败重启；同会话模式/seed固定、预计算提示快照保留，不能静默混用旧参数。但相同参数和seed不保证不同GPU浮点波形逐位相同，也不保证听感完全一致。

朗读模式适度扩大自然标点聚合（Target40/Max80单位），减少独立合成重启；文字不删改。聊天仍保持第一句及时提交。更大朗读段可能增加等待或降低双卡并行机会，是连续韵律与延迟的取舍，不是已经证明的自然度/提速。保留顺序、背压、取消、有界codec与淡入淡出；不跨词叠加PCM掩接缝。

## 真实验收三轮（仍需目标机）

比较同一个人的干净8–10秒参考、同源16秒/24秒锚点，保持相同目标文、seed、模型与生成参数；每种至少三轮。分别保存GPU0/1同文WAV及完整朗读，审核相似度、单一声音、齿音/沙沙、句间自然度、漏字添字。不要只比较声纹数字或波形幅度。网页音频欠载/first_played与模型RTF分开看。

现有`tools/voice_benchmark.py --run --profile 实际档案ID --rounds 3 --chunk-size 8 --output 新私有目录/report.json`可调用驻留双GPU，保留18条WAV与JSONL，RTF>0.3即不达标；详见STEP16_QUICKSTART。它不代替试听。当前沙箱没有真实T4/Whisper/Qwen语音测量，未运行的结果一律BLOCKED，不用CPU/Mock代替。

网页真实训练闭环、长数据完整审核对齐/训练全覆盖、真实双T4训练提速、严格声学逐字拒播等历史缺口仍未完成。整体仍PARTIAL/BLOCKED。

---

## 内嵌备忘录：KAGGLE_TARGET_ACCEPTANCE.md

# 目标双T4验收门禁（待实际执行）

日期：2026-10-23。此文件是交接操作顺序，不是已有GPU实验结果。当前沙箱虽已装Torch供CPU测试，但没有可用CUDA/训练权重（实际Faster/HF已安装供CPU接口实验，不代表完整模型）、物理麦克风或DeepSeek通路；不得把本地CPU、Mock、界面截图或surface_preflight_passed填进真实实验结果栏。

## G0：保护基线与凭据

保留原始与step1/2/3/4/5/6/7/8/9/10/11包及SHA256。升级前先确认所有旧版本GPU进程停止，再解包到目标ROOT；资源锁只约束本版本合作进程，不能自动迁移旧服务。使用可丢弃的独立Kaggle会话，双T4、Internet On；依赖和模型revision尚未完整锁定，先审查安装流程，不在含无关凭据的环境执行。Kaggle Secret使用QTTS_ACCESS_TOKEN（32–256位非空格ASCII）与按需的HF_TOKEN/DEEPSEEK_API_KEY；不写进命令行、截图、共享日志或交接文件。

仅解包检查可在Notebook子进程中运行（脚本须先上传到当前目录）：

```python
import os, subprocess, sys
subprocess.run([sys.executable, 'kaggle-fixed-step17.py'], check=True,
    env={**os.environ, 'QTTS_UNPACK_ONLY':'1',
         'QTTS_ROOT':'/kaggle/working/qtts-step17-inspect'})
```

这是解包，不安装/下载/加载权重。不要把QTTS_UNPACK_ONLY留在完整启动环境中，避免把仅解包退出0误当模型成功。

## G1：先收集环境，再做表面探针

在目标Notebook记录实际GPU名称/数量、驱动、Python、Torch/CUDA版本、计算能力、总/空闲显存和磁盘。当前探针只记录总显存，不代替空闲显存测量。

完整启动前明确QTTS_MOCK=0、QTTS_DTYPE=fp16、禁用QTTS_ALLOW_SINGLE_GPU；首次建议QTTS_TUNNEL=none，暂不启公网隧道。必须在启动模型进程之前设置，事后在另一个shell里unset不会改变已经运行的Mock进程。

安装流程审查后，真实启动示例（会安装依赖和下载模型，当前沙箱没有执行）：

```python
import os, subprocess, sys
runtime_env={**os.environ, 'QTTS_MOCK':'0', 'QTTS_DTYPE':'fp16', 'QTTS_TUNNEL':'none'}
for key in ('QTTS_UNPACK_ONLY','QTTS_ALLOW_SINGLE_GPU'):
    runtime_env.pop(key,None)
subprocess.run([sys.executable,'kaggle-fixed-step17.py'],env=runtime_env,check=True)
```

默认ROOT=/kaggle/working/qtts；如果自定义QTTS_ROOT或QTTS_STATE，后续路径必须同步。启动失败时先保留STATE/backend_probe.json与脱敏错误类别，不重复安装/重试掩盖失败。

运行时探针独立复现：

```bash
python /kaggle/working/qtts/tools/backend_probe.py --runtime --expected-gpus 2 --dtype fp16 --timeout 120 --output /kaggle/working/qtts/state/backend_probe.json
```

退出2=阻断/仅检查；退出0=设备与API调用形状通过。后者仍没有加载权重，四个model/inference/training/performance验证标志均为false；**kwargs能接收参数不证明内部语义，SDPA/CUDA Graph/精度稳定性还需实际推理。

## G2：证明不是Mock，再做最小真实推理

启动后在Notebook本机用受认证的GET /api/health、/api/workers检查两个worker的健康详情，记录engine=faster-qwen3-tts、dtype=fp16、GPU编号0与1。`ok:true`、HTTP200、两个端口或模拟正弦PCM都不足以证明真实模型。worker /health不应被公网直接暴露。

使用合法同说话人的短WAV参考，自己命名声音库，提供与锚点逐字匹配的文本；没有文本的样本另测真实ASR，不把ASR失败伪装为成功。创建与启用声音档案只准备缓存，**不是训练**。

既有工具的参数已对照源码，声音档案创建后可运行：

```bash
python /kaggle/working/qtts/tools/selftest.py
python /kaggle/working/qtts/tools/e2e_check.py --url http://127.0.0.1:7860 --mode read --min-gpus 2
```

默认读取已启用档案；无档案应跳过并返回非成功，不能计为模型通过。也可用实际档案ID传--profile，不填虚构ID。访问口令由私有环境/认证目录读取，不放命令参数。selftest中的可选Rust检查可能单独失败，逐项记录；--quality会调用真实质量模型，待下载/硬件条件具备后再执行。旧工具个别输出将速度倍率rtf_x标成rtf并带×，应按定义解释，不当作标准RTF。

每卡保存并试听真实PCM/WAV：24kHz、有限值、非空、非全零、无异常幅度/系统性爆音；记录实际流式chunk时间、数量与间隔，排除“整段生成完再切块”伪流式。短句/长句、冷热启动、多段调度和取消恢复分别测量。不通过则回到后端兼容适配，不能静默替换小模型或换预置说话人。

## G3：容器与浏览器链路

分别测试真实浏览器麦克风录制的WebM/Ogg/MP4容器与WAV上传，记录浏览器MIME、解码器/ffmpeg版本、实际采样率、声道、时长、大小和服务端拒绝条件。当前沙箱只有原生Chromium软件输入编码与soundfile小WAV路径，未测物理麦克风或真实ffmpeg。

可信HTTPS浏览器中验证权限拒绝/等待取消、切换主视图、诊断、锁定、麦克风设备结束、超限、上传失败后片段保留。测试虚拟键盘、横屏、缩放、中文字体与屏幕阅读器；当前自动化只覆盖列出的Chromium CSS视口，不能扩展为全设备通过。

## G4：DeepSeek与性能指标

先核对真实模型名、服务端上下文/输出上限与收费额度；Key只用Secret或浏览器内存。测试长流、错误帧、断网、取消、恢复以及切换声音；不自动重试可能重复扣费的请求。

- 分开记录首token、首模型chunk、首PCM、浏览器第一段实际播放；首PCM不是可听首声。
- 标准RTF=生成耗时/音频时长；rtf_x=音频时长/耗时，是倒数速度倍率。分卡与系统聚合指标不可混用。
- 冷/热、短/长文本、两卡调度、浏览器缓冲分别报告，记录足够样本的分布与失败比例，不只展示最好的一次。
- 首声<3秒、RTF≤0.5、无系统性断音是待验收目标。ECAPA余弦或内部fidelity指数不等于99.5%身份一致率；先定义测量/盲听协议和保留集。

## G5：真正双卡训练（实验性核心已实现，Qwen/T4执行未验收）

独立训练作业必须验证world_size=2、两rank实际处理样本、可复现样本覆盖、梯度同步、优化器更新、显存、检查点保存及重载真实试听。当前已有训练输入与声学码准备入口/来源封存/读取租约：逐条文本、统一参考、授权/单说话人声明、完整24kHz mono PCM16 WAV、固定哈希与双rank数学分配计划。真实audio_codes仍blocked；已有FP16 LoRA/DDP/optimizer与adapter代码及CPU小网络梯度/参数更新证据，但未执行Qwen/CUDA训练或自动训练/推理模式切换；不能按创建档案、候选校准或准备输入验收训练。输入副本应先按固定manifest SHA256校验，上游工具必须在快照目录解析相对路径；其他音频格式需受限解码另验，不静默裁剪。

不要将官方BF16/FlashAttention2/全参数AdamW示例直接用于T4，或只加accelerate launch --num_processes 2就称完成。先核对T4支持、模型包装属性、优化器内存和检查点语义；LoRA、ZeRO/FSDP等方案均须实际接口与显存验证，不在缺权重时猜测兼容。训练与推理应隔离，避免每GPU推理实例占满显存时并发训练。

## G5a：声学码准备（入口已有，真实模型未验收）

第七阶段仅本机CPU离线CLI，使用固定输入manifest租约与可信本地12Hz tokenizer模型内容树hash；无自动下载或GPU编码入口。先按KAGGLE_STEP7_AUDIT.md验证真实单条全PCM编码、输出ceil(frames/1920)×16与完整样本覆盖，再实际decode试听、测CPU RAM/耗时。fixture码与stub调用不是该门禁证据；当前真实encode缺qwen_tts/权重且无GPU，仍blocked。

当前已有第八阶段同机同UID整组资源准入协议，但没有自动推理/离线任务模式切换或GPU编码。改为GPU任务前仍需受控作业接入与实际显存测量，不能直接在两模型已占显存时调用cuda:0。输入与码版本租约已实现，码版本已接入实验性双rank训练器并受控共享FD；真实Qwen/T4执行仍未验收，训练器须持有保护直到所有读者退出。语义/解码/训练标志不得因结构检查自动变true。

## G5b：资源准入协议已有，硬件回收尚未验证

按KAGGLE_STEP8_AUDIT.md使用resource_control.py status/reserve；busy=false不代表GPU空闲，预约也不执行模型。真实supervisor/worker/analyst须使用本版本FD协议；父死但孩子持锁时仍busy，不能依PID/TTL强制解锁或删除fleet.lock。多模型进程由supervisor启动，旧版本/外部进程必须另行确认已停。

在目标设备实际记录所有进程停止前后nvidia-smi与CUDA空闲/保留显存，再预约并接入受控GPU任务，验证取消/失败/恢复。此刻有CPU进程/FD与小网络Gloo证据，无实际VRAM回收、自动模式切换或双rank训练证据。bootstrap不再自动按旧PID/pkill停服务；遗留PID标记须人工确认后清理，不能删资源锁。

## G5c：来源封存/读取协议已有，不是训练许可

schema2完整复制输入manifest/JSONL，验证源固定hash、WAV/text/ref/顺序/计划交叉一致；声明只是用户记录。schema1仍legacy-unsealed，禁止凭当前库补写旧授权。list的政策字段不等于完整核验，固定manifest hash verify才返回provenance_verified_now。

hold-read只保持检查租约，第十阶段实验性训练器已接入，但仍须现场验真实编码/语义/权利政策/设备与DDP；首版同版本读取独占，删除/第二读取409，取消/超时/进程退出释放。不能当训练按钮，已有CPU进程/FD接管与小网络参数更新证据，但不能称Qwen/CUDA参数已更新。详见KAGGLE_STEP9_AUDIT.md。

## 待填结果表（当前均未验收）

| 门禁 | 当前真实结果 | 要保存的证据 |
|---|---|---|
| G1 环境/表面探针 | 待目标设备运行；沙箱是blocked | 硬件/版本/报告/空闲显存 |
| G2 双卡真实模型 | 未运行 | 非Mock引擎、每卡真实输出与时间、异常 |
| G3 物理录音/容器 | 未运行 | 浏览器/设备/MIME/ffmpeg/解码与拒绝样本 |
| G4 DeepSeek/性能/音色 | 未运行 | 真实流、分布、取消、听测协议与保留集 |
| G5a 真实声学码/解码 | 未执行；离线CPU入口已有，依赖/权重blocked | 可信模型hash/实际编码/完整覆盖/解码/内存与时间 |
| G5b 资源/显存 | 合作式协议已验证；真实显存/模式切换未验收 | 实际进程/空闲显存/预约与任务取消恢复 |
| G5 双卡训练 | 实验性FP16 LoRA/DDP/adapter代码已实现；真实Qwen/CUDA未运行 | 双rank/样本/梯度/参数更新/检查点重载 |

只有取得对应原始记录后才能改表。秘钥、真实私密语音、完整私人转写和大模型/数据集不进入Git或公开报告。

第十阶段运行入口及具体Notebook取消代码见KAGGLE_TRAINING_QUICKSTART.md；无需等待更多基础设施即可在真实环境尝试。optimizer/adapter执行成功不等于音质通过，不自动替换推理模型，真正Qwen新进程重载/试听与接入聊天仍待执行。


## G11：显式训练adapter后端与聊天（现场待验）

第十一阶段已实现实际接入，不是只写未来工具。按KAGGLE_ADAPTER_QUICKSTART.md从真实completed run取得pin、显式发布命名候选，再使用qwen-adapter-buffered、本地Base及固定hash启动既有supervisor。默认faster保留。两worker加载确认才改变active，错误/缺adapter/Base/错误模式不得回退。

原生API一次生成解码完整段，不接受为G4“声学流式通过”；health/stats/UI必须显示sentence-buffered。只允许称DeepSeek文字/网关段流保留，不能把后处理PCM块或停顿包当模型流式。现场验证保存speaker prompt的真实声音、A/B/A、取消后释放、真实长回答及一份Base/卡的峰值显存。当前CPU数学/本机真实Go+SSE/HTTP是替身系统证据，不是Qwen/T4、新进程试听或外部DeepSeek验收。

固定训练候选拒绝参考文本/候选/校准修改；旧普通档案仍用faster模式，保持删除/认证/两视图。一个参考WAV/转写进入旧profile私有备份范围，run/完整模型不自动备份；恢复缺文件明确失败。源码总目标仍22/300，不因这一开发阶段自动勾满硬件/音质要求。


## G12：现场Mimi/RoPE故障与会话驻留复跑

用户现场已实际识别两T4（各15636037632字节、CC7.5），下载/编译完成；模型加载明确失败，不能保留为“硬件未知”也不能升级成加载成功。step12使用faster0.5.4/qwen-tts-hf0.1.1.post1/TF5.20.2真实现代配置桥接，旧字段异常已在CPU实际wheel函数复现并修复；原配置不变、3个theta验证。CPU数学smoke不是本门禁完成。

目标重新启动完整Kaggle会话后，确认先通过qwen_mimi_rope_cpu，再两个worker各自完成from_pretrained和warmup。检查health的requested_model、model_loaded、单CUDA可见设备与residency_policy，结合实际GPU显存/进程和音频，不能只看这些字段或workers_healthy数字。完成短句/长句/停止与显存记录；配置错误fatal应停止重试并清理本次supervisor，无旧PID盲杀或删锁。

QTTS_RESIDENT=1取消旧600次周期重载和13.5GB主动回收，不自动idle卸载，但错误/OOM/平台回收仍会中断。磁盘权重缓存不等于GPU永久驻留；Kaggle不作永久占用验收。固定三项依赖不是全环境lock，保留平台Torch/CUDA约束后仍需实际安装冲突与模型完整调用验证。

## 第十三阶段现场状态更新（优先于上面历史step12结论）

用户step12仍同错失败，旧CPU函数测试没有覆盖Faster延迟导入。step13显式导入HF后桥接并强制smoke；完整真实包+微型Mimi初始化/重载已在CPU三进程通过，但不是完整Qwen/T4验收。目标22/300不升级，按KAGGLE_STEP13_QUICKSTART.md直接复跑。

## 第十四阶段优先更新

用户step13现场已通过两T4模型加载/预热ready门禁。14仅新增长录音预算/CPU等价缓存/原文分段/默认无后加呼吸。网页一键训练闭环、真实训练提速与质量、首播改善及声学逐字核验未完成/验收，完整目标仍22/300。详见STEP14_AUDIT/QUICKSTART，不能用本轮模拟通过升级真实音质门禁。


## 第十五阶段优先更新

当前step15强隔离参考PCM/ICL上下文，向量模式可能改变音色韵律，不能据CPU证明真实语音完全不串参考。先正常重启会话再运行，按STEP15_QUICKSTART直接朗读与DeepSeek首句分别测试三轮。默认输出-18dBFS、上限12dB增益，校准默认关闭但手动保留，CPU ASR可复用。比较创建耗时时必须区分冷/热、下载和可选校准；比较首声看first_played_ms与underruns。每T4双模型没有实测，不默认开启。旧训练闭环/长数据全覆盖/声学拒播缺口不因本轮交付消失。


## 第十六阶段最新优先门禁（覆盖15纯向量与12dB默认值）

最新包16采用匹配转写ICL条件，codec仅生成码；参考内容及模式pin，默认前瞻0/最大增益6。按STEP16_QUICKSTART先试听不同于参考的目标文本，再做双GPU三轮18条真实基准。tools/voice_benchmark.py不带--run零测量blocked；真实目标0.3任一条不达即失败，达速度也不等于音质合格。旧参考正文继续出声可来自模型幻觉，不能只凭未拼接PCM认为声学逐字已验。历史训练闭环/全覆盖/声学拒播缺口保留，目标22/300仍不升级。


## 第十七阶段最新门禁

先完整重启到17，不用截图15判断17修复。用同源10秒、16秒与24秒对照，长录音按时间戳/真实窗口识别择锚；生成参数也进入v2 pin。核对原文、每卡同文音色/噪声、整段朗读、first_played/underruns与RTF，至少三轮。结构对照16失败17成功不等于实际Whisper识别准确或Qwen质量达标。57份完整备忘录及STEP17_QUICKSTART说明边界，历史训练/覆盖/声学拒播缺口保留。

---

## 内嵌备忘录：KAGGLE_STEP18_PLAN.md

# 第十八阶段：参考条件可追溯、首声、噪声与连续朗读

## 当前状态（2026-10-23）

分支`arena/03d65d8e-kagglee`，活动状态，从已合并17基线继续。已完成基线核对、第一/第二轮关键路径专题审查各100条、DSP分块基线三轮、提示合同/参考状态控制流三轮；第三轮与本阶段自问自答尚未完成。第二轮不等于全部模块的第二遍完整语义审查。**没有修改产品源码、没有生成18发布包、没有宣称声学达标。**

截图事实：已是17；41.6秒录音建档成功，耗时142.3秒；RMS约-47.7dBFS、峰0.011；候选#0/#1/#2约9.1/10.5/11.0秒，SNR估计17.1/16.3/17.8dB。没有附件音频，不能由截图听出噪声或确定声学根因。源码说明单锚点用于ICL，候选参与评分与质心，校准逐个试验再择一，不是三参考同时融合。

用户“参数要结果（#0、#1、#2等所有参考）”按要求采用保守、可检验解释：候选应有完整评估/校准依据，生成条件应明确可追溯；是否支持模型原生多参考融合，必须读实际接口后决策，不能用拼接PCM、混转写或平均不兼容提示冒充。所有参考参与质量分析与全部参考同时作为ICL是不同功能。

## 约束

- 中文小步汇报；每轮100条具体建议，不将建议当已证实bug。
- 完成三轮源码审查后，自问自答按一次一题执行，具体选项、推荐理由、待证边界；每题先列50实施建议再下一题；累计决策从问题25开始，不能先批量伪造回答。
- 总方案先于产品修改；不要求100%信心，不承诺零错误/零噪声。缺真实证据保持BLOCKED。
- 原始–17包、manifest和工作台冻结；参考PCM绝不混入生成播放；首声不能用静音占位或参考原音冒充。
- 已有记录、取消、安全、训练、私有数据及复制功能不豁免。绝不上传私有WAV或把模型权重纳入Git。

## 分阶段执行与验收

1. **基线与审查**：核对53内嵌资产、76历史冻结哈希、15正式文件；保留新阶段快照。每轮分开记录实际读过的路径和未覆盖语义，AST/哈希不是全源语义证明。第一轮见REVIEW1。
2. **第二轮：数据与状态语义**：遍历profile/API/缓存/Go会话/前端条件选择，读实际Faster及Qwen提示接口，确认多候选校准与多参考条件是否可实现；检查切换、取消、双卡一致性和过期会话，记录100建议。
3. **第三轮：数值与时间链路**：逐层追踪源录音清理、codec窗口、Rust/NumPy DSP、协议、重采样、Worklet、调度与文本聚合；覆盖启动/欠载/段间停顿，记录100建议。对其他功能逐模块复核，不能只审4个热点就称所有代码已查完。
4. **逐题决策与最终实施细则**：至少覆盖全部候选的作用和实际条件绑定、首包与实际播放测量、DSP分块一致性、噪声与自然度验收；每题50建议后进入下一题。只有实际接口、复现或测量支撑的改动进入产品实施。
5. **小步实现**：优先修复已复现的确定性状态问题；每个修复先保存失败样例，再修复，局部测试通过后完整回归。多参考/降噪/缓冲策略按实验选择，不直接强滤波、不跨词叠加、不删字。
6. **三轮最终工程验证**：在最终源码上运行完整Python、Node、Go race、六协议与浏览器三轮；当前环境依赖需要重建，旧17收据不能当本阶段执行。涵盖取消/锁定/文件路径/长录音/转写/双卡pin/训练来源及正文完整性。
7. **三轮真实模型实验**：实际双T4上同人同文、固定seed和有效参数，比较每候选及推荐策略；保存实际生成WAV、每层耗时、worker与wall RTF、播放欠载与首样本确认。同文两卡与长文交替分开测，结合盲听和转写审核；真实权重/GPU不可用则明确未运行，不拿合成信号或tiny模型代替。
8. **发布与完整备忘录**：冻结18源码后repack、固定hash复制/下载、手机和剪贴板拒绝回退；逐字节校验及全部历史资产冻结检查。所有完成的备忘录完整内嵌提示词，未完成项明确。此阶段进行中的汇总为`KAGGLE_STEP18_HANDOFF_PROMPT.md`；原17最终提示词暂不覆盖。

## 第一轮实测收据

- 新环境仅安装NumPy2.2.6至被忽略`.venv`，无Torch/完整模型/CUDA运行证据。
- `kaggle/tests/dsp_partition_probe.py`对冻结17 NumPy Leveler输入相同半秒双音信号，比较整块与48/64/96/240/1920及不规则分块，每轮12个案例，三轮。
- 隔离增益（target=-6dBFS/max_gain=0）48分块与整块最大差1424 int16单位；1920分块差0。对应淡入跨短块从零重新起算的源码风险。
- 正常增益（target=-18/max_gain=6）1920分块最大差8单位；48分块差1425。AGC分块实现也非严格分块不变。该实验未编译Rust，不称已实测跨后端数值差。
- 所有案例样本数完整、无非有限输出。该收据证明工程分块依赖，不证明噪声听感、用户根因或模型质量。
- `repack.py --check`、JS语法检查、Node30项基线通过；尚未执行本阶段完整334项Python或Go/浏览器回归。

## 第二轮取证与复现（未修复）

- 实际发行版为`faster-qwen3-tts==0.5.4`及`qwen-tts-hf==0.1.1.post1`，wheel SHA256核验通过；`qwen-tts==0.1.1`仅用于对比发行版依赖，未安装。首次误写`qwen-tts==0.1.1.post1`查询失败后按项目pins纠正，未改变产品依赖。
- 实际接口的列表/字典prompt长度必须与目标批次匹配。三参考提示加单目标被拒绝，三提示三目标是独立批次，不是自动融合；单ICL快照仍可用。
- `reference_state_probe.py`对原函数AST每轮执行6项prompt合同、4项校准场景、9项候选参数和1项双卡seed诊断，三轮结果一致。外部模型、ASR、声纹、tokenizer及网络均显式fixtures；没有HTTP或线程压力测试，也没有完整模型运行。
- 复现`index=true`选1、`1.9`截为1、null/容器类型未捕获异常；校准ASR全部失败默认CER0.05；旧转写评分可选中新转写；全合成失败仍chosen0；校准丢弃加载失败回执；同文双卡诊断seed分别100/101。
- 并发案例是确定性交错：模拟候选1编辑后切回候选0并编辑的合法元数据状态。候选WAV不变，但最终采用的候选1转写未在该轮被评估。它不是实际多线程压力或HTTP事务证明。
- 保留已有成功保护：正式播放同会话seed、Go激活并行加载和二次指纹确认/旧active保留、Worker锁内前后核验、文本/候选reload_response的503与reference_saved、前端accessEpoch锁定防迟到回填。
- 第二轮100条及证据见REVIEW2和`validation/step18/reference-state-baseline-round1..3.json`。初始19项探针收据及源码快照保留initial命名，最终扩展到20项并补充明确的被评分转写。

复现命令：先建立含NumPy2.2.6的隔离环境，执行`.venv/bin/python docs/validation/step18/fetch_reviewed_upstream.py`（只解包经哈希核验的两份源码，不安装、无权重），再执行`.venv/bin/python kaggle/tests/reference_state_probe.py --round 1`，依次2、3。

## 语言与性能原则

PyTorch/CUDA继续承担模型计算，Python组织提示与分析，Go承担调度/协议，Rust承担DSP，JavaScript承担采集/播放。只有实测热路径需要时才增加C/C++等实现；不新增Java/C#/VB/SQL/Fortran服务凑语言。NumPy回退一致性问题应按真实算法合同修复，不用隐藏回退失败冒极致性能。

## 声学验收边界

沙沙声需分别定位原始录音、参考清理、模型生成、codec、后处理及播放欠载；低输入与估计SNR不等于根因。首PCM/发送play命令/Worklet消耗首语音/硬件声学首声不是同一时间。自然度需完整朗读试听与逐字核对。历史真实训练闭环、长数据覆盖及RTF≤0.3缺口继续保留；整体PARTIAL/BLOCKED。

---

## 内嵌备忘录：KAGGLE_STEP18_REVIEW1.md

# 第十八阶段第一轮：参考条件、首声和噪声链路的100条建议

状态：关键路径首轮专题审查；不是全部代码已逐行完成三轮语义审查。产品未修改。建议是后续验证/实现清单，不是100个已证实缺陷。

事实：当前生成使用单个选中锚点；候选参与评分/质心，校准是逐候选试验再择一。播放firstPlayedMs当前是主线程play命令时刻。NumPy/Rust DSP存在需实际验证的分块状态差异。

## 候选真实语义
源码位置：`py/analyst.py:build_profile / calibrate_profile; py/worker.py:FasterEngine.stream`。

1. [S18-R1-001] 将候选参与质心统计与实际ICL锚点分开显示，避免全部片段已融合的误解。
2. [S18-R1-002] 在合成收据记录选中的anchor_candidate，而不是只显示profile ID。
3. [S18-R1-003] 记录实际锚点字节指纹与对应转写指纹；日志不明文写入私有转写。
4. [S18-R1-004] 用不同内容的三个候选验证只选中的音频进入提示提取。
5. [S18-R1-005] 审核“候选校准”文案明确逐个试验后选一个，不称多参考融合。
6. [S18-R1-006] 查验Faster真实接口的多参考能力，未支持时不伪造列表参数。
7. [S18-R1-007] 禁止把三个片段PCM拼成一个提示并配不连续全文。
8. [S18-R1-008] 跨候选声纹中心仅作评分依据，不声称它已替代模型speaker embedding。
9. [S18-R1-009] 为单个合法候选保留最短建档链路，不强迫三候选。
10. [S18-R1-010] 给未来多候选策略保留显式模式与回退边界，不静默改变17默认。

## 候选切换与并发
源码位置：`py/analyst.py:set_candidate; py/worker.py:_load_profile_locked; py/voice_binding.py`。

11. [S18-R1-011] 非法index的布尔、小数、对象与缺省语义分别测试，避免int强转误选或500。
12. [S18-R1-012] 核查切换候选与校准并发时磁盘写入、工作者加载是否形成一致事务。
13. [S18-R1-013] 候选文件复制失败时保留旧profile JSON，不留下半更新锚点。
14. [S18-R1-014] 双卡仅一张加载成功时明确部分失败，不宣称启用完成。
15. [S18-R1-015] 旧会话遇新指纹必须继续拒播，不能热切后拼混音色。
16. [S18-R1-016] 转写编辑与候选选择同时发生时绑定同一版本，防止音文错配。
17. [S18-R1-017] 校准临时profile的anchor_candidate元数据应指向实际试验候选，不能误标0。
18. [S18-R1-018] 候选变更后清理或替换提示快照时保留锁内核验。
19. [S18-R1-019] 为重复点击候选与取消任务增加幂等与状态测试。
20. [S18-R1-020] 训练adapter的固定参考限制保持，不让候选切换绕过来源绑定。

## 首声定义与时钟
源码位置：`py/worker.py:Worker.synth; go/gateway/session.go; web/app.js:tick`。

21. [S18-R1-021] 分别记录请求、首个可用文本、排队、预填充、首PCM、首播放命令。
22. [S18-R1-022] worker t_start在加载提示之后，单独计量冷提示加载而不漏记等待。
23. [S18-R1-023] queue_ms当前覆盖锁等待等前置耗时，拆项后保留旧字段兼容。
24. [S18-R1-024] 浏览器firstPlayedMs当前在发play命令处赋值，标明不是硬件实际出声。
25. [S18-R1-025] 评估AudioWorklet消费首个语音样本的确认消息，区分主线程命令延迟。
26. [S18-R1-026] 跨Python、Go与浏览器仅使用各自单调时间差，不能直接减不同纪元。
27. [S18-R1-027] 显式静音停顿不能计为首个可用人声，保留禁止原音占位。
28. [S18-R1-028] 首包平均之外记录p50/p95与冷暖状态，不用一次幸运值。
29. [S18-R1-029] 将文本长度、参考长度、chunk_size和设备条件写入性能收据。
30. [S18-R1-030] 首声提速必须同时检查缺字与最终音频完整性，不能裁掉开头。

## 浏览器启动缓冲
源码位置：`web/app.js:needToStart / onWorklet / QttsRing`。

31. [S18-R1-031] 对当前0.7秒下限和初始2秒策略建立确定性到达轨迹对照。
32. [S18-R1-032] 分别测试高速稳定、慢速持续、突发包与长网络抖动。
33. [S18-R1-033] 初次启动与欠载恢复分别设计目标，不统一缩到最小。
34. [S18-R1-034] 将预测器无速率样本时的保守回退纳入首次播放测试。
35. [S18-R1-035] 测量AudioWorklet统计消息的刷新间隔对主线程启动判断的影响。
36. [S18-R1-036] 在44.1k及48k上下文验证重采样后的fill计秒正确。
37. [S18-R1-037] 短于启动阈值但已完成的真实语音应及时播放，不等待不可达缓冲。
38. [S18-R1-038] 后台页、暂停恢复、锁定与取消后不得发送迟到play。
39. [S18-R1-039] 记录ring dropped样本；任何丢样不能只显示播放成功。
40. [S18-R1-040] 低延迟策略只能在欠载预算内启用，不能把断续当自然阅读。

## 模型与调度热路径
源码位置：`py/worker.py:FasterEngine; py/clone_stream.py:generated_only_stream; go/gateway/scheduler.go`。

41. [S18-R1-041] 对2/4/8/16帧首块大小做同文本同seed对照，测TTFA及总RTF。
42. [S18-R1-042] 小首块与稳态大块若需不同大小，先确认真实生成器支持，禁止无效传参。
43. [S18-R1-043] 检查decode迭代器首次next含有的预填充时间，不能只测创建生成器。
44. [S18-R1-044] 单独计量token生成、codec解码及CPU拷贝，避免归因全部GPU。
45. [S18-R1-045] 提示快照重用必须与内容指纹一致，不退回仅按路径缓存。
46. [S18-R1-046] 不为首声把ICL换成向量默认，保留相似度条件。
47. [S18-R1-047] 比较首段优先调度与后续并行的队头阻塞，不无证据锁死单卡。
48. [S18-R1-048] 确认Live聊天第一可用前缀触发不被朗读聚合配置覆盖。
49. [S18-R1-049] 保留最大生成token与取消限制，不能为速度删掉输出。
50. [S18-R1-050] 不默认每卡双模型增加显存；只有目标T4实测才接受吞吐结论。

## 输入噪声与参考处理
源码位置：`py/analyst.py:build_profile / denoise / normalize_speech`。

51. [S18-R1-051] 原始RMS约-47.7只作为风险，不推断具体麦克风故障。
52. [S18-R1-052] 分别记录归一化前后语音电平与峰值，注明增益上限14dB。
53. [S18-R1-053] 候选SNR是估计量，不能把17dB阈值当真实噪声声压。
54. [S18-R1-054] 保留raw、strength0.85、strength0.55对照的处理收据。
55. [S18-R1-055] 审查声纹相似0.94与SNR增益2dB门禁是否会误接收失真，不能只看单分数。
56. [S18-R1-056] 验证全零、强直流、很轻语音及背景声输入的处理决策。
57. [S18-R1-057] 对齿音、气声、摩擦音单独测保真，不能以削高频冒无沙沙。
58. [S18-R1-058] 不在用户未授权时保存或上传原始私有WAV作为公共证据。
59. [S18-R1-059] 已存在非平稳降噪不等于生成输出已降噪，明确处理发生阶段。
60. [S18-R1-060] 录音时扬声器回录网页朗读的可能性仅列假设，不能由截图定论。

## 生成输出噪声定位
源码位置：`py/worker.py:Worker.synth; py/clone_stream.py:GeneratedCodecWindow`。

61. [S18-R1-061] 建立模型PCM、后处理PCM、浏览器录回的分层局部诊断，默认关闭私有采集。
62. [S18-R1-062] 将codec窗口起点与边界脉冲位置关联，区分底噪和接缝爆音。
63. [S18-R1-063] 对持续人声与停顿分别计算频谱，但无清洁真值时不称绝对SNR。
64. [S18-R1-064] 继续验证codec只收到生成码，不能回到参考码前缀解码。
65. [S18-R1-065] 真实预训练codec与随机tiny codec的质量证据必须分列。
66. [S18-R1-066] 非有限模型输出当前替换为零，应评估失败拒播而非掩盖异常的策略。
67. [S18-R1-067] 增益提升可能抬噪，记录处理前后噪声地板变化而不自动强门限。
68. [S18-R1-068] 不能用输出全静音或静音段删除作为零噪声验收。
69. [S18-R1-069] 保留模型自然人声呼吸与禁止添加噪声的区别，不自动切除语音气息。
70. [S18-R1-070] 用户全程纯人声目标需真实WAV试听和添字检查，代码指标不替代。

## DSP状态与后端一致
源码位置：`py/audio_rt.py:Leveler; rust/audio_rt/src/lib.rs:Leveler`。

71. [S18-R1-071] 实测同一信号整块与任意分块处理的样本一致性。
72. [S18-R1-072] 重点验证NumPy不足96样本首块时淡入是否在下一块重新从零开始。
73. [S18-R1-073] 核查NumPy按输入块丢弃不足240样本RMS余数与Rust跨块累积差别。
74. [S18-R1-074] 比较Rust逐样本增益平滑与NumPy逐块插值，不能宣称严格等价。
75. [S18-R1-075] 保持输出样本数与输入相等，不能为降噪补偿无记录延迟。
76. [S18-R1-076] 分别测试DC blocker状态、零输入残留与长静音后重新讲话。
77. [S18-R1-077] 测试max_gain_db=0隔离淡入和DC滤波，再开放AGC定位差异。
78. [S18-R1-078] 同卡每段重置与跨卡各自状态不同需测量，不能只凭相同目标响度称一致。
79. [S18-R1-079] flush的192样本衰减不是新生成语音，不能加入RTF语音分母。
80. [S18-R1-080] 若修复NumPy算法须保留Rust接口版本兼容，并添加跨后端容差测试。

## 连续语义与播放接缝
源码位置：`go/gateway/segmenter.go; go/gateway/session.go; web/app.js:QttsRing`。

81. [S18-R1-081] 将独立模型韵律重启、显式停顿、播放欠载三种接缝分类计数。
82. [S18-R1-082] 保留朗读12/24首段、20/40/80稳态配置基线再比较，不盲目扩大。
83. [S18-R1-083] 逐字验证分段重新连接等于原文，保护数字、缩写、引号和标点。
84. [S18-R1-084] 审查PauseBeforeMs与tail_pause_ms是否重复加停顿，先画时序再修改。
85. [S18-R1-085] 禁止跨词PCM重叠掩盖接缝，不牺牲清晰度冒自然度。
86. [S18-R1-086] 段尾8ms衰减及下段淡入需以有声边界实测，不只用零边界波形。
87. [S18-R1-087] 欠载时0.94尾衰减属于播放补偿，不能误标模型本身沙沙。
88. [S18-R1-088] 自然度对照必须同时保存整段朗读，不能只听裁剪后小片段。
89. [S18-R1-089] 不同GPU同文与交替长文分别试听；同seed不等于波形完全相同。
90. [S18-R1-090] 只有真实模型支持的连续条件才能声称跨段联合生成，不换名称包装独立合成。

## 回归、语言和交付门禁
源码位置：`kaggle/repack.py; tests/browser; docs/validation/step17/final-checks.json`。

91. [S18-R1-091] 冻结原始至17包、全部manifest及正式工作台，新增18不得覆盖历史包。
92. [S18-R1-092] 三轮100建议均标已确认问题、待证假设或保留约束，不虚报300个bug。
93. [S18-R1-093] 完成三轮审查后再逐题决策，每题50建议后才进入下一题。
94. [S18-R1-094] 历史334测试不能算18新增验证，依赖缺失需如实记录和重建。
95. [S18-R1-095] 对每个修复保留修复前失败、修复后通过的同输入收据。
96. [S18-R1-096] 三轮Python、Node、Go race、协议和浏览器必须针对最终源码再执行。
97. [S18-R1-097] CPU合成信号实验不代替真实T4语音实验，硬件不足保持BLOCKED。
98. [S18-R1-098] 按实测热路径选择语言；不要新增Java/C#/SQL服务凑多语言。
99. [S18-R1-099] 最终18复制页、下载、剪贴板拒绝回退与手机逐字节校验不可省略。
100. [S18-R1-100] 将全部已完成备忘录内嵌完整提示词；未完成轮次必须明确，不编造结论。


## 第一轮实验补记

S18-R1-081已完成分块对照；S18-R1-082短块淡入问题在三轮冻结17 NumPy路径中复现，隔离增益后48样本分块最大差1424 int16单位。正常AGC1920分块差8。尚未修复，非用户噪声根因证明，非实际模型实验；其他建议不因此自动判为已实施。

---

## 内嵌备忘录：KAGGLE_STEP18_REVIEW2.md

# 第十八阶段第二轮：候选条件、接口合同与并发状态100条建议

状态：第二轮关键路径专题审查完成；第三轮与阶段自问自答未完成。不是全源三轮语义审查完成声明，产品源码未修改。每条建议是待实施/保留合同，不是100个新增已确认bug。

## 取证方法与来源

实际下载并核对faster-qwen3-tts0.5.4与qwen-tts-hf0.1.1.post1的PyPI wheel SHA256；旧qwen-tts0.1.1仅作区别核查，未安装。最初把发行版名写成qwen-tts==0.1.1.post1导致查询失败，纠正为项目真正固定的qwen-tts-hf；不是产品依赖失败。完整URL/hash见`validation/step18/upstream-round2-provenance.json`。

`kaggle/tests/reference_state_probe.py`提取原函数AST执行：真实控制流保留，外部GPU/ASR/tokenizer/说话人/网络为显式fixtures。确定性交错并非线程压力；未跑HTTP、完整模型或GPU，不证明音色或噪声。

## 真实模型接口与批量语义
源码位置：`faster0.5.4:model.py:_resolve_precomputed_voice_clone_prompt; qwen-tts-hf0.1.1.post1:qwen3_tts_model.py`。

1. [S18-R2-001] 保持qwen-tts-hf与旧qwen-tts发行版严格分离，源码同命名空间不等于同版本。
2. [S18-R2-002] 下载源码必须核对PyPI wheel SHA256，收据注明实际提供模型类的发行版。
3. [S18-R2-003] 将三提示单目标被拒绝的实际接口行为加入未来多参考功能合同。
4. [S18-R2-004] 将三提示三目标定义为独立批量任务，界面不能称参考融合。
5. [S18-R2-005] 保留列表prompt每项独立ref_text，不用共享一条文字冒三候选匹配。
6. [S18-R2-006] 字典prompt的批量ref_text共享行为应明确，不直接用于三段不同转写。
7. [S18-R2-007] 引用prompt item中ref_code与speaker embedding的区别，不能用声纹平均替代ICL。
8. [S18-R2-008] 保持单ICL预计算提示的真实接口回归，不能为新模式破坏现有快照。
9. [S18-R2-009] 向量模式继续要求显式选择，不把它作为未实现融合的静默替代。
10. [S18-R2-010] 实际生成器、权重和声学结果未执行时，接口控制流通过不标模型实验通过。

## 候选与生成条件合同
源码位置：`py/analyst.py:build_profile; py/voice_binding.py; py/worker.py:FasterEngine`。

11. [S18-R2-011] 建立全部候选分析清单，逐项列源文件、时间、匹配转写、指纹和有效性。
12. [S18-R2-012] 单锚点模式明确显示被用作ICL的候选及未用作ICL的其他候选。
13. [S18-R2-013] 若后续共享参数来自全部候选评分，记录算法与评分证据而非暗示音频融合。
14. [S18-R2-014] 比较每候选合成时固定同文同seed同采样参数，确保差异确由候选造成。
15. [S18-R2-015] 候选中心与实际Qwen说话人嵌入不同空间时不得直接替换。
16. [S18-R2-016] 实验性的融合嵌入若提出，必须独立模式且真实盲听，不自动作为最佳方案。
17. [S18-R2-017] 不跨候选拼转写或参考码以绕过模型批量长度校验。
18. [S18-R2-018] 候选顺序变化时用内容身份而不只用数组下标定位证据。
19. [S18-R2-019] 候选有效时长按实际WAV而非仅展示start/end计算，避免舍入差。
20. [S18-R2-020] 候选策略、模型模式及参数调整必须使旧会话明确失效。

## 候选入口数据验证
源码位置：`py/analyst.py:set_candidate / set_text; py/library_api.py:body`。

21. [S18-R2-021] index必须严格整数且非bool，拒绝true变1与false变0。
22. [S18-R2-022] 拒绝1.9截断成1，避免非整数JSON静默切换其他参考。
23. [S18-R2-023] 缺失index应明确拒绝还是显式兼容默认0，不让文档与行为矛盾。
24. [S18-R2-024] null、数组、对象及NaN输入转换失败应返回受控4xx而非未捕获异常。
25. [S18-R2-025] 候选入口未知字段与重复字段的策略需与严格library接口一致。
26. [S18-R2-026] 验证candidates为非空合法列表，不能只依赖len和下标访问。
27. [S18-R2-027] 验证候选file为安全单文件名且普通文件，避免损坏profile路径越界。
28. [S18-R2-028] 手工ref_text不接受dict/list被str化，保留严格字符串与Unicode校验。
29. [S18-R2-029] 保留训练档案禁止改候选和转写的409边界，不绕过版本固定。
30. [S18-R2-030] 增加真正HTTP参数与错误码测试；当前AST调用不冒充FastAPI测试。

## 参考版本与并发提交
源码位置：`py/analyst.py:calibrate_profile / set_candidate / set_text; py/qtts_common.py:write_json_atomic`。

31. [S18-R2-031] 校准开始捕获完整候选集合版本，提交时核对未变再采用评分。
32. [S18-R2-032] 禁止用旧候选评分选择重新读取后已更改的同下标候选。
33. [S18-R2-033] 校准期间并发编辑转写不能被结束时静默覆盖，需冲突响应。
34. [S18-R2-034] 候选文件内容更改但文件名不变也要改变校准输入版本。
35. [S18-R2-035] 候选变更、文本变更、校准、删除应协调同一档案锁或乐观版本合同。
36. [S18-R2-036] 进程内线程锁与跨进程文件锁分别评估，不能把一个称全局事务。
37. [S18-R2-037] HEAVY最大2只限制并发数量，不等于每profile串行，不能替代状态锁。
38. [S18-R2-038] 对先写磁盘再等HEAVY被429拒绝的路径核对reference_saved状态。
39. [S18-R2-039] 原子JSON替换只保护单文件，候选复制与JSON提交之间仍需一致性设计。
40. [S18-R2-040] 校准提交前档案已删除或adapter状态已变化时必须停止，不能恢复旧状态。

## 校准缺失指标与失败状态
源码位置：`py/analyst.py:calibrate_profile`。

41. [S18-R2-041] ASR评估全部失败不再用CER0.05冒充实测值，应记录null与失败原因。
42. [S18-R2-042] 部分文本ASR失败时记录覆盖率，不能只对成功样本平均后隐藏缺失。
43. [S18-R2-043] 全部候选合成失败时返回明确未选出有效结果，不能chosen0看似成功。
44. [S18-R2-044] 每候选的有效生成条数和预期条数同时保存，评分先验证完整性。
45. [S18-R2-045] 未测或低可信声纹指标不填高分默认值，应明确阻塞/降级语义。
46. [S18-R2-046] 候选排序排除非有限得分，NaN/Inf不进入max选择。
47. [S18-R2-047] 模型输出空音频、太短、全静音和缺字分别记失败而不只比声纹。
48. [S18-R2-048] 校准报告应保留先前有效结果，失败新校准不覆盖为貌似新最佳。
49. [S18-R2-049] ASR释放与临时目录清理放入覆盖所有异常的finally路径。
50. [S18-R2-050] 错误信息需脱敏且保留阶段，不能把原文和本机私有路径暴露给日志。

## 双卡诊断的可比性
源码位置：`py/analyst.py:consistency; go/gateway/scheduler.go:synthReq`。

51. [S18-R2-051] 同目标文本跨GPU诊断使用相同seed，修复100+17*ti+gi的设备偏移混杂。
52. [S18-R2-052] 将实际seed写入每张卡诊断条目，使测试条件可核验。
53. [S18-R2-053] 会话调度当前各卡同seed的行为应保留，不把诊断偏移引入播放。
54. [S18-R2-054] 两卡同一voice_binding和voice_conditioning都要进诊断收据。
55. [S18-R2-055] 记录实际dtype、模型版本、codec政策与DSP后端，不能仅比profile ID。
56. [S18-R2-056] 相同参数不意味着位级相同；阈值评分和人工听感结论分开。
57. [S18-R2-057] 同文对照与不同文本交替朗读各自设计，不能用同文替代自然衔接。
58. [S18-R2-058] 所有条目失败时speech_db默认0不应参与一致性，明确缺失项。
59. [S18-R2-059] consistent布尔值应附完整性及阈值说明，不能称零噪声或100%同声。
60. [S18-R2-060] 诊断生成在锁定或请求取消后仍进行时保留资源状态，不误报即时停止。

## 双卡加载与启用确认
源码位置：`py/analyst.py:load_on_workers / reload_response; go/gateway/main.go:activate`。

61. [S18-R2-061] 校准结束必须检查load_on_workers回执，不能丢弃失败后正常返回。
62. [S18-R2-062] 保留文本/候选接口已有reference_saved与503部分失败语义。
63. [S18-R2-063] Go激活两卡并行、同绑定同模式核验及旧active保留不得回归。
64. [S18-R2-064] 激活最终再次读磁盘核对指纹的检查必须保留。
65. [S18-R2-065] Python reload最终current为None时应视失败，而不是跳过版本核验。
66. [S18-R2-066] 候选校准只用GPU0的现状须说明；多卡校准需独立计划，不虚报双卡评估。
67. [S18-R2-067] 加载某卡成功某卡失败后，不允许新会话静默只用成功卡冒双卡一致。
68. [S18-R2-068] 冷首次sanity合成耗时应与提示提取耗时分开记录，避免首声归因错误。
69. [S18-R2-069] HTTP断开不等于后台模型加载已停止，未来重试需幂等/状态查询。
70. [S18-R2-070] 不得为降低激活耗时跳过Worker锁内参考前后两次指纹校验。

## 缓存、临时资源与删除
源码位置：`py/worker.py:FasterEngine.load_profile / Worker._load_profile_locked; py/analyst.py:calibrate_profile / delete_profile`。

71. [S18-R2-071] 审查_cal临时profile移除后Worker提示缓存仍驻留的资源生命周期。
72. [S18-R2-072] 重复校准相同临时ID时确保旧提示被替换，不能复用先前参考。
73. [S18-R2-073] 删除档案后清理与它关联的profiles、voice_bindings、levelers和提示快照。
74. [S18-R2-074] 缓存释放必须获取合成同一把锁，不释放正在使用的GPU张量。
75. [S18-R2-075] 缓存容量按可测内存预算管理，而不是只看磁盘profile数量。
76. [S18-R2-076] 临时校准ID与用户可启用ID区分，不能由列表选中临时声音。
77. [S18-R2-077] 备份继续排除_cal档案，不把测试用临时状态持久化为模型。
78. [S18-R2-078] 临时目录清理失败记录状态并可回收，不无声积累数据。
79. [S18-R2-079] 生成器取消仍要close并释放有界codec窗口，不能因缓存修改遗漏。
80. [S18-R2-080] 不要盲目清空CUDA所有缓存导致每段冷启动，资源回收须按作用域。

## 前端状态、认证与用户反馈
源码位置：`web/app.js:apiFetch / m / profile candidate controls; py/access_control.py`。

81. [S18-R2-081] 候选点击期间禁用或序列化同档案变更按钮，避免重复并发写。
82. [S18-R2-082] 响应乱序时按操作版本更新高亮，不让旧响应覆盖新选择。
83. [S18-R2-083] 继续保留accessEpoch和AbortController防锁定后迟到数据回填。
84. [S18-R2-084] 客户端取消只能停止等待时明确提示后台任务可能继续，不伪报服务器取消。
85. [S18-R2-085] 503且reference_saved时显示已保存未全卡就绪，不能笼统当未保存。
86. [S18-R2-086] 校准报告区分逐候选评分、最终提交、双卡加载三个状态。
87. [S18-R2-087] 没有有效候选或指标不全时不显示成功绿标。
88. [S18-R2-088] 参考转写可审阅但日志默认脱敏，token不进URL/localStorage。
89. [S18-R2-089] 新增条件证明信息只放同源授权接口，不能自动上传外部诊断服务。
90. [S18-R2-090] 新增交互保持移动端可操作、录音失败队列保留与锁定清空。

## 保留边界与最终验证
源码位置：`py/voice_library.py; py/trained_profiles.py; py/persist.py; tests/browser`。

91. [S18-R2-091] 原始库已有revision与lease设计可借鉴，但不直接修改其已成功数据格式。
92. [S18-R2-092] 候选处理与真实训练继续分开命名，不把评分或缓存称训练提升。
93. [S18-R2-093] 训练adapter来源hash与固定参考在新条件策略下仍必须核验。
94. [S18-R2-094] 私有原始样本仍排除Dataset自动备份，新增诊断WAV默认不进入归档。
95. [S18-R2-095] 代码、参数和参考版本相同的测试与实际用户WAV声学验收分开报告。
96. [S18-R2-096] 为每个确认缺陷建立独立失败样例，后续修复应让同案例先失败再通过。
97. [S18-R2-097] 受控AST交错不是线程压力测试；实现后补真实并发和HTTP回归。
98. [S18-R2-098] 下载wheel仅源码检查不安装旧qwen-tts，避免命名空间冲突。
99. [S18-R2-099] 本轮100建议与实际实验范围完整入备忘录，不宣称全源三轮完成。
100. [S18-R2-100] 第三轮结束及逐题50建议决策完成后才改产品，继续冻结17包与工作台。

## 三轮受控实验结果

每轮6项上游提示合同、4项校准场景、9项候选输入、1项双卡seed诊断，共20项；三轮结果一致。三提示单目标list/dict均拒绝，三提示三目标是独立批量。ASR全失败产生默认CER0.05、旧评分提交新候选、加载失败未检查、全合成失败仍chosen0、bool/float强转、非法类型异常以及诊断不同seed均复现。它们是控制流/状态问题，不是用户沙沙根因。

保留：Go激活并行加载、指纹/模式确认、最终重读及旧active保留；Python文本/候选reload_response已有503与reference_saved语义；Worker锁内前后核验；前端认证epoch。不能只列缺陷却重写破坏这些成功保护。
