# 第十八阶段 G0 第六批：分析/API、参考切分、Python/Rust DSP

## 1. 本批结论与边界

2026-10-23，活动分支 `arena/1160bd87-kagglee`。延续已完成第五批，不改冻结产品，不重开 PR2、不预填问题28、不生成第18阶段发布包。本批是**全文第一遍补审与限定范围执行验证**，不是已实施首声/声质优化，也不是完整三轮全功能/模型验收。

- 本批新增全文第一遍 **6份、2152行**；累计 **45/53、12336行，剩8份**。
- 完整第二遍、第三遍仍均为 **0**。三轮专题各100建议及问题25–27各50建议保留，不冒充全源三遍语义审查。
- **172项×3轮=516项通过**，每轮失败/错误/跳过均0。其中旧测试160项，新12项：9保护、3 `OBSERVED_NOT_FIXED` 原行为见证。旧测试中也含已知缺陷见证，不能将总通过数解释为没有缺陷。
- 另行 **14个分析端AST控制流案例×3轮**、**12个NumPy合成DSP案例×3轮**。与单元测试存在行为重叠，不相加冒充独立完整功能覆盖。
- 新确认 F10–F12 三类边界，**均未修复**。历史校准/候选缺陷、NumPy分块依赖也仍复现。
- 实际执行：原Python函数、NumPy DSP、requests/TCP本地HTTP、库进程内ASGI与本地文件操作。重型ASR/embedding/模型生成使用明确fixtures。
- 未找到 `rustc`/`cargo`；Rust两份文件**只完成源码审查**，未编译、未跑内置Rust测试、未加载实际Rust库。不用NumPy结果替代Rust运行证明，不为完成语言数量安装来源不明编译器。
- 无Torch/Qwen完整权重/CUDA、真实DeepSeek、用户WAV、物理声卡及双T4；没有证明相似度、无沙沙、自然连续朗读、RTF≤0.3或真实提速。

冻结基线继续为53资产、94冻结hash与15正式文件；本批保存295个既有文档/收据/脚本hash，旧证据不改写。NumPy为实际2.2.6，不是需求文件中的2.4.6。Starlette/httpx的弃用警告保留在控制台，未为消除警告擅改产品依赖。

## 2. 全文第一遍范围

全文阅读分段进行；analyst最初只读到1050行，补完1051–1211后才计入覆盖，不把部分阅读提前记全文。其余5份也均完整读完。阅读区间不是运行覆盖率。

| 资产 | 行数与完整区间 | 本次重点 |
|---|---:|---|
| `kaggle/source/py/analyst.py` | 1211，1–1211 | 解码/上传限额、ASR/speaker生命周期、指标、worker帧协议、候选评分/重叠选择、校准、旧API、consistency |
| `kaggle/source/py/audio_rt.py` | 222，1–222 | ctypes符号与参数、NumPy DC/AGC/淡入/尾部、转换、极短breath |
| `kaggle/source/py/library_api.py` | 163，1–163 | 严格JSON、multipart、修订CAS、租约、共享准入、后台任务提交/失败/清理、错误脱敏 |
| `kaggle/source/py/reference_segments.py` | 106，1–106 | 有效时间戳、词级校验、长段窗口重转写、短尾收据、原文不可按比例切割 |
| `kaggle/source/rust/audio_rt/Cargo.toml` | 17，1–17 | cdylib/rlib、无第三方依赖、2021 edition、release LTO/abort，未实际编译 |
| `kaggle/source/rust/audio_rt/src/lib.rs` | 433，1–433 | Leveler跨块状态、DC/AGC/淡入/flush、noise、unsafe C入口、内置测试；只读源码 |

覆盖台账：`docs/validation/step18/g0-analysis-dsp-coverage.json`。旧 `g0-runtime-coverage.json` 等保持为历史检查点。

## 3. 按模块的语义结论

### 3.1 分析、候选、校准与指标

1. build内embedding缓存按规范化float32内容hash；命中返回copy，build之间不共享。新保护验证float64/非连续输入规范化及调用者修改不污染缓存。它是缓存，不是训练。
2. 全参考参与分析/统计与centroid，最终至多三候选按评分和同文件重叠规则选择；实际ICL仍用选中锚点。保留“全部音频参与统计不等于全部同时进入模型prompt”的透明边界。
3. 评分涉及长度、帧能量分位差、ASR logprob、speaker相对centroid、F0离散度及语速。分数不是人声相似度真值；低RMS截图不能定位沙沙声来源。
4. `synth_full`用于离线校准/诊断，不能继承浏览器/Go已做的协议校验来假定安全。其HTTP状态、终结与残留校验不足独立记录F12。
5. 本次14项AST重跑保留：ASR不可用仍CER0.05、旧评分提交期间更改后的转写、重载失败回执被忽略、全合成失败仍chosen0；均是确定性交错/依赖fixture，不是线程压力测试。
6. 旧 `/candidate` 存在bool/小数强转及null/容器未捕获异常；本次9个输入案例重新执行。不能用该结果推断严格库JSON路由也同样接受。
7. `consistency`同文调用seed100/101不同的旧诊断行为再次验证。正式播放同会话seed一致的功能不得被这条诊断观察反向改坏。fixture返回相同speaker值不是真实双卡等效参数或声学一致性证明。
8. 建档两个worker加载失败后任务是否仍done、旧修改/删除接口与校准并发、实际HTTP竞争、缺CER/proxy值是否进入质量门禁，继续列为待证/待设计，不把本轮14个AST例说成覆盖全部。

### 3.2 原始参考库API

完整读取库路由及其依赖的既有32项测试：严格请求体、CAS/lease、选择检查、后台任务、共享准入、失败释放、提交顺序、去重、完整性与私有错误脱敏。重跑实际本地文件与进程内HTTP；后台语音处理为fixture。

保护“成功状态晚于元数据提交”“失败保留原样本及上一成功profile”“请求取消不能丢租约”“executor提交失败不能稍后执行排队修改”“库样本不自动成为可播放模型”。这些是现成功能保护，不是新增了真实训练按钮/训练闭环或验证语音质量。

### 3.3 参考切分

- 合法短段直接用段级文本与时间戳；可选词信息不可信时短段分支清空，不能按字符比例把全文分给不同音频。
- 长段优先使用与词全文一致且时间合法的词分区，否则对**真实对应音频窗口**重转写。新增保护验证32秒由两个16秒窗口产生自己的文本，第二窗口词时间平移16秒。
- 小于1.5秒尾段记录 `short_tail_s`，不与上一段全文拼成伪对齐。17秒fixture实际仅对前16秒重转写，尾1秒不生成候选文本；保护的是“明确报告而非伪造对齐”，不宣称最后1秒已被ASR转写或完整训练覆盖。
- 重转写结果词信息的清洗弱于直接短段分支，详见F11。坏词元数据是明确注入；真实Whisper在用户录音中是否产生相同数据仍未测。

### 3.4 NumPy与Rust DSP

NumPy原函数实际执行；Rust源码显示持有跨调用能量累计与完整淡入位置，flush重置DC状态。NumPy的分块RMS/增益插值、剩余长度重启淡入以及flush保留DC状态需独立同信号同分块对照。当前Worker每段新建leveler这一调用约束必须保留；不能把复用同一个leveler的潜在差异直接当作当前用户播放故障。

本次重跑既有半秒24kHz双音实验12组合：

| 设置 | 分块 | 对整块最大int16差（三轮一致） |
|---|---:|---:|
| target−6 / maxgain0，隔离淡入与DC | 48样本 | 1424 |
| 同上 | 1920样本 | 0 |
| target−18 / maxgain6，正常AGC | 48样本 | 1425 |
| 同上 | 1920样本 | 8 |

这是**工程分块依赖**，不是经过主观试听的接缝损伤、噪声根因或GPU路径对照。没有修正数值，也没有测得质量/性能改善。

新保护还覆盖正常长度breath确定性/长度/有限值、非连续float转连续布局、空输入meter、PCM饱和不回绕、Leveler空/非有限值输入、热信号限幅及尾部归零、close幂等。非有限输入清洗仅验证NumPy路径，不扩展到未执行Rust。

Rust的C入口空指针保护、slice长度/所有权、调用方串行化、版本门槛与符号完备、错误返回值处理仍须真实ABI验证；Python只捕获装载OSError、不检查每个DSP返回码等是**源码待测观察**，不在本轮虚报ABI故障复现。Cargo内置测试未运行，未生成或签收 `.so`。

## 4. 新确认但未修的三个边界

### S18-G0-ANALYSIS-F10：NumPy极短breath形状

`audio_rt.py:86–102`，24kHz卷积核6，`same`输出长度为输入与卷积核长度最大值：
- 请求1样本，实际返回6样本；
- 请求2/3/4/5样本，分别抛ValueError（包络广播不兼容）；
- 请求6样本，返回6；常规64/1920/24000长度保护通过。

直接原函数/真实NumPy执行。只是合成helper边界，**没有播放参考PCM**，未证明当前worker正常分块会触发，更未证明用户沙沙根因。后续修复必须保证长度且不重新启用参考呼吸拼接。

### S18-G0-ANALYSIS-F11：窗口重识别的可选words漏清洗

`reference_segments.py:96–103`，注入合法段时间与字符串text，但可选words为四元组，重识别分支列表推导解包直接ValueError；同样metadata在短段分支被清空。三元组的text=None可被保留进输出。

原helper实际执行，ASR结果显式fixture；未运行真实Whisper，也没有声称实际端到端build崩溃已执行。后续pause/prosody路径依赖word字符串，仅作为需保护的下游风险说明，不能将潜在AttributeError当作本次新跑出的证据。

### S18-G0-ANALYSIS-F12：分析端不完整/失败流被当作正常返回

`analyst.py:361–385`，使用真正requests + ThreadingHTTPServer本地TCP，原 `synth_full` 实际解析：
1. HTTP503携带PCM/空stats：正常返回2样本；
2. PCM后残留2字节header：正常返回2样本、空stats；
3. PCM后未完整到达的stats payload：正常返回2样本、空stats；
4. stats为 `failed:true`：正常返回音频与failed字段，未抛错；
5. HTTP200空体：正常返回0样本、空stats。

同时保护完整分片UTF-8 stats/PCM，以及显式ERR帧正确抛RuntimeError。这证明分析端协议验证缺口，**不是实际worker模型故障已发生，也不是公开网关利用验证**。没有运行HTTP慢客户端/无上限payload压力或资源泄漏测量。

三条状态均 `confirmed...not_fixed`，新见证通过只意味着原失败行为稳定复现。机器台账：`g0-analysis-dsp-findings.json`。原300建议初审不改写，新观察单列。

## 5. 三轮执行与证据链

每轮运行：

```bash
.venv/bin/python docs/validation/step18/run_analysis_audit.py --round 1
# --round 2 / --round 3 相同目标、独立进程执行
```

172项构成：原G0 84 + runtime 10 + RecordingTests 6 + step15 16 + step17 12 + libraries 32 + 新analysis 12。明确不选需要Torch的 `test_step14.CacheTests`；没有把跳过训练测试算成通过。本轮选中项实际skip为0。

每轮另执行：
- `reference_state_probe.py` 中4校准+9候选输入+1consistency，直接调用旧probe函数，共14。**本地旧upstream解包cache不存在**，因此未跑历史6个prompt接口案例，没有偷偷重建/重签旧wheel收据。旧20案例历史收据保持不变。
- 原 `dsp_partition_probe.py --round N`，12个真实NumPy合成分块组合，保存原始stdout与JSON。

| 轮次 | unittest | 分析AST案例 | 合成DSP案例 | 失败/错误/跳过 |
|---|---:|---:|---:|---:|
| 1 | 172 PASS | 14完成 | 12完成 | 0/0/0 |
| 2 | 172 PASS | 14完成 | 12完成 | 0/0/0 |
| 3 | 172 PASS | 14完成 | 12完成 | 0/0/0 |

主要文件均位于 `docs/validation/step18/`：
- `analysis-audit-roundN.json`：逐测试ID、结果、新观察、53源码hash、测试/runner/support hash、依赖、原log hash、真实性标记。
- `analysis-regression-roundN.txt` / `analysis-roundN-console.txt`：原始测试及console；模拟失败异常与无GPU门禁输出属于预期测试输入，不能据console中ERROR字样误判成功收据，也不能将自检工具的内部SKIP展示当成执行了模型测试。
- `analysis-contracts-roundN.json`：4+9+1 AST函数控制流细项、原probe/source hash。
- `analysis-dsp-roundN.json` / `.txt`：原12组合数值、probe/source/hash与原stdout。
- `analysis-preserved.json`：本批开始时295个既有历史文档/收据/脚本hash，旧签收不因新handoff自动变更。
- `analysis-toolchecks.json` 与对应日志：Node30、JS检查、Python AST、repack一致性检查。
- `analysis-environment.txt`：本机依赖、Rust/模型环境边界。
- `verify_analysis.py` / `analysis-progress-verification.txt` / `progress-analysis.json`：本批独立一致性验证；`progress-checks.json`指向当前检查点，旧验证器和旧收据原样留存。

独立验证器必须确认53源码/94冻结/正式资产、历史295份、原300建议及问题25–27、45/53/12336、三轮目标一致、观察稳定、所有log/test/probe hash、handoff逐memo原文一致。不能以“写出JSON”替代实际断言。

## 6. 后续精确顺序

本批不另开关键设计题；问题25–27各50建议、推荐C保持。仍按G0→S1–S8门禁执行，不跳至DSP产品修复。第一遍剩8份：6个工具 `backend_probe/e2e_check/resource_control/selftest/voice_benchmark/watermark_check` 与 `LICENSE-QWEN-DERIVED.txt`、`MEMO.md`。先读完并补各自执行边界，再补全源第二/第三遍、300建议最终处置与失败见证映射。

Rust真实编译/内置测试/ctypes同信号对照、实际HTTP并发更新、完整模型/双卡/用户录音/长数据真实训练仍是显式缺口；如环境缺失继续标BLOCKED，不把source read变成runtime PASS。必要设计问题继续逐题≥50建议，不提前问用户，不要求点击Continue。

所有性能和声学不变要求仍在：真实首可用DeepSeek prefix立即生成、生成PCM-only、更响且受保护、更低创建延迟、>10分钟录音与真实训练的区分、<10秒参考相似度、双GPU同等参数/声音、自然连续朗读、无沙沙及真实RTF≤0.3。当前没有真实新优化或声学验收，整体 **PARTIAL/BLOCKED**。
