# 第十五阶段优先：仅音色向量生成/无参考片段拼接/首句及时调度/有界增响

旧段落为历史。原始至step14冻结，当前step15。用户报告参考串入输出及档案256.4秒；截图没有原音频，具体声学根因未证实。

- Faster加载/预热/生成统一xvec_only=True、ref_text为空、append_silence=False。仅提说话人向量；不能回退ICL。向量模式韵律/相似度可能变化，必须真实试听，不称无损已验。
- Worker不读取旧breath_files；QTTS_BREATH_MODE=reference也不能开启参考拼接；停顿仅零样本。模型自身呼吸保留。reference_pcm_splicing=false是代码策略，acoustic_text_verified仍false，不保证零幻觉。
- Go仅聊天首段LiveSegCfg在完整句/足够长分句立即提交，不等下一delta；ASCII小数点/未闭合引号仍等待。普通朗读ExactSegCfg、后续段、背压/取消/播放器水位不变。两卡各一模型，未经实测不每卡放双副本。
- 新旧档案输出默认-18dBFS，QTTS_OUTPUT_DBFS合法-24..-14，最大增益12dB并保持Rust/NumPy软限幅。原录音不改，不能保证任意声音精确增3dB。
- 创建默认不追加可选GPU候选校准，手动入口保留；CPU ASR可复用，QTTS_ASR_KEEP_CPU=0关闭，CUDA仍卸载。ASR使用RLock覆盖加载、完整惰性转写与释放，防不同分析入口并发释放模型。嵌入缓存只在本构建按样本hash复用，最多64条，不减数据/24候选/评分/准确F0。
- 完成后最终保存quality.build_s、stage_ms及embedding_cache；界面可展开。过长ASR单段不再截14秒配全文；只有完整2.5–16秒对齐段才能回退选用，16秒手动全文保持完整。
- 强制HF RoPE导入顺序/smoke保留；真实Faster控制流CPU注入fixture与tiny Mimi重载不等于完整Qwen音质/T4速度。完整用户要求仍PARTIAL/BLOCKED，网页训练闭环、长数据全覆盖和严格声学拒播仍缺；不要把参考处理叫训练。
- 具体方案、三轮审查各100项、问题16–18各50建议、测试证据和升级步骤见仓库KAGGLE_STEP15_*及validation/step15。完整包身份以source_manifest_step15.json为准，复制页固定hash，正式3000不动。

---

# 第十四阶段：长录音/等价训练准备优化/不后加呼吸与正文

## 当前版本修复

用户step13已在实际双T4通过模型加载/预热与ready门禁；该证据不等于真实合成试听或训练。原始至13冻结，当前14。

本版将浏览器连续采集提升到约20分钟，单文件64MiB、请求128MiB、分块8192均独立受限，服务端完整复核，不截断原件。长录音不能直接当单条训练序列：仍需可信时间戳短段和逐条审核转写。网页训练控制面尚未闭环，不把输入快照/参考缓存冒充训练。

训练保留原样本/顺序/联合loss/优化器/累积步数，有界64MiB输入张量缓存消除重复tokenize，聚合grad finite检查减少逐参数host读取；记录缓存/调用指标。CPU等价不等于T4最快或训练质量更好。HF发行版本查询兼容已成功的qwen-tts-hf。

实际会话不再清洗正文或自动补句号；默认QTTS_BREATH_MODE=off不后加呼吸，reference仅允许真实参考呼吸，无合成噪声回退。模型自身气声仍需试听。可实验QTTS_FIRST_CHUNK_SIZE=2（默认4，范围2..8），保持稳定播放器阈值；不承诺首声必更快。统计区分模型首块与trim后可输出语音，声学文本尚未自动ASR核验，不宣称逐字绝对一致。

---

# QTTS 源码修复备忘录（2026-10-21，第十一阶段增量版；历史分节保留）

## 当前新增：训练adapter → 原生推理 → 原有聊天

新增trained_profiles.py / adapter_engine.py / tools/trained_voice.py。默认faster流式路径保留，只有显式QTTS_TTS_ENGINE=qwen-adapter-buffered才启用官方原生adapter推理。固定本地Base及manifest/code hash；完成记录、tensor摘要/形状/finite、保存speaker向量严格核验；模块先整体构造再锁内切换，每段检查绑定和文件，不静默退回Base/Mock。

CLI发布命名训练候选，不自动active；候选profile含一段统一参考WAV及对应转写，沿旧profile备份语义；训练run/完整模型不自动备份，恢复缺adapter/Base明确失败。官方x-vector-only prompt使用保存speaker，不重算另一个参考；不是完整CustomVoice。原生模式一段完整生成才输出一块wave，健康/帧/UI标注sentence-buffered，取消合作式并丢迟到PCM，不能中断CUDA kernel。Go和supervisor原生等待预算180秒，旧路径60/75/90秒不变。

Worker支持trained profile前必须显式原生后端，Mock/default拒绝。旧档案、录音、命名库、校准、DeepSeek流/停止/两主视图保留；训练候选固定参考，拒绝改文本/候选/校准。修复一致性检测全失败仍可能consistent=true的门禁。

当前源码独立step11/46资产；原始至step10冻结。CPU LoRA数学/切换和注入的官方API形状/HTTP/网页替身不等于真实Qwen、新进程重载、NCCL或T4语音/显存验证。具体启动顺序见仓库KAGGLE_ADAPTER_QUICKSTART.md；真实权重/GPU仍缺失。

## 0. 目标与现状

目标：Kaggle 双 T4、Qwen3-TTS-12Hz-1.7B-Base、多参考声音库、长文本流式对话、可打断连续播放，并另外实现真正双卡训练。
当前源码已有参考缓存/候选校准/双worker调度，以及**实验性FP16 LoRA双rank训练实现，真实Qwen/T4运行未验收**。缓存/校准仍不是训练。
原始单文件及其22项资产保留，step1/2/3/4/5/6/7/8/9均冻结；当前step10独立导出43项资产，新增实际联合loss/LoRA/DDP/optimizer/adapter入口，保留来源封存/读取租约/GPU合作协议。Torch CPU张量/Gloo不等于Qwen或T4验收。最新证据见仓库docs/KAGGLE_STEP10_AUDIT.md；历史分节仍保留，不代表真实GPU或训练已验收。

## 1. 已确认事实及修复边界

- 原始22项压缩资产的内嵌校验全部通过；原文件不存在已确认的粘贴截断。
- 现有系统使用 Python 模型进程、Go 网关、Rust 可选音频库和已编译的浏览器 JavaScript。
- 实际包内没有 `web-src/*.ts`，不能声称修改了不存在的 TypeScript 源码。
- T4/Turing 不具备原生 BF16。默认 FP16；BF16 回退同时检查计算能力和 torch 支持，FP32 须显式 `QTTS_ALLOW_FP32=1`。
- BF16/FP32、模型接口、CUDA Graph、SDPA 的实际可运行性仍须在真实设备上验证。
- 标准 RTF = 生成耗时/音频时长，越小越快。旧字段 `rtf_x` = 音频时长/生成耗时，是速度倍率，不能混称。
- 不能把第三方 benchmark、模拟波形生成速度或双 worker 理论吞吐算作本系统双 T4 实测成绩。

## 2. 架构与端口

| 层 | 语言 | 文件 | 当前职责 |
|---|---|---|---|
| 浏览器 | JavaScript/Web Audio | web/app.js、index.html | 音频环形缓冲、流式帧、实验室、监控 |
| 网关 | Go | go/gateway/*.go | LLM、切段、双 worker 调度、有序转发、指标 |
| 音频后处理 | Rust，可回退 NumPy | rust/audio_rt、py/audio_rt.py | 去直流、响度、限幅、呼吸 |
| 模型 | Python/PyTorch | py/worker.py | 每 GPU 独立模型，克隆特征缓存，合成 |
| 参考分析 | Python | py/analyst.py | 转写、候选、校准、音色代理评估 |
| 运维 | Python | bootstrap.py、supervisor.py、persist.py | 启动、守护、持久化 |

默认网关7860、workers7001/7002、Analyst7010。模型端口不应直接暴露公网。
Worker帧 `[type:u8][len:u32LE][payload]`，客户端帧 `[type:u8][seg:u32LE][len:u32LE][payload]`。
PCM必须是24kHz、单声道、16bit。收到其他模型采样率时显式报错，不冒充24kHz播放。

## 3. 本轮行为变化

1. 两卡是默认前置要求；单卡仅通过 `QTTS_ALLOW_SINGLE_GPU=1` 显式开启受限测试。
2. DeepSeek默认预算8192 tokens，可用 `DEEPSEEK_MAX_TOKENS` 调整（1..65536），实际服务端模型上限仍需验证。
3. 去除默认200字限制；遇长度截断、错误JSON、供应商错误、未完成EOF均报错，不自动重复收费请求。
4. 声音ID限制安全字符；激活仅POST，两 worker 均确认后才原子提交 active.json，失败保留原激活状态。
5. 旧浏览器请求的迟到响应和 finally 不得干扰新轮次；音频初始化合并、初始化失败可见。
6. DeepSeek Key只留在当前输入框/内存，清理旧版localStorage键；不在浏览器持久保存。
7. Whisper默认CPU int8，避免抢占第二个TTS模型显存；`QTTS_ASR_DEVICE=cuda` 显式选择GPU，速度需重新测量。
8. 静默子进程也受超时控制；原子JSON使用唯一临时文件；恢复归档拒绝路径穿越、链接及非普通文件。
9. 无Rust环境下短音频块的NumPy处理长度保持正确；短呼吸片段不再出现广播长度错误。
10. 自检缺少资源标记SKIP，退出码2表示未完整验证，不把跳过计作通过。

## 3.1 第二阶段访问控制与资源预算

- 所有网关API需 `Authorization: Bearer ...`；直接启动Go网关无口令则退出，不设免认证旁路。
- Kaggle Secret `QTTS_ACCESS_TOKEN` 优先；否则在默认 `/tmp/qtts-auth-用户ID-状态路径摘要/` 0700私有目录中创建0600随机口令。启动日志仅打印路径，不打印口令。不要将此文件分享或放入Notebook输出。
- 网页显式解锁，口令只在内存中；锁定取消请求、停止播放/录音并清空私密视图。只发同源请求，不再支持在别的网站填外部网关地址。
- 默认JSON上限1MiB、上传请求64MiB、16文件/20MiB每文件、240秒每文件、900秒累计；超限拒绝，不静默截断。
- 单次文本20000字符、历史16条/累计32000字符；2个并发语音会话、2个昂贵请求；语音令牌桶12次容量/每分钟补充12次、通用120次容量/每秒补充20次；默认请求期限1800秒。
- 分析服务解析multipart前先有界暂存；后台构建至多1个、记录64条、声音库128个，空闲磁盘低于256MiB拒绝创建。
- 分析线程另设2个执行名额，HTTP取消不提前释放仍在运行的线程名额；解码禁用网络/文件协议、限制时长与线程数。当前环境没有ffmpeg，真实解码器路径仍需实机验证。
- 网关代理剥离访问口令/DeepSeek Key/Cookie；模型进程不继承网关或Kaggle凭据。
- 这是单用户共享口令，不是多租户账号体系。TLS由可信代理提供；OS级全局磁盘/内存配额、解码器沙箱与worker内部队列专项尚待完成。

## 4. 调度设计保留

按韵律分段，双worker并行，有序汇聚；动态高低水位和短首段、预测缓冲、响度处理、呼吸策略、失败改派均保留。
本轮没有重新设计调度，也没有用模拟结果证明所有并发与故障场景完备。

## 5. 训练、相似度和首声定义

- 官方提供单说话人微调流程；官方示例的BF16/FA2/全参数AdamW不能原样当作双T4实现。
- DDP不把两块16GB简单变成每进程32GB。参数高效训练、FP16缩放、显存预算及检查点须逐项适配和验证。
- 不能断言所有T4微调都不可能，也不能未经实测宣称已经可行。
- 99.5%音色一致性没有已约定的测量定义；ECAPA余弦、内部fidelity指数不等于身份相同的百分比。
- 首声从提交到实际可听样本；首PCM、首token、模型首chunk须分别报告。
- <3秒、RTF≤0.5、长回答无系统性欠载是验收目标，**尚未达到可确认状态**。

## 6. 当前验证证据

CPU自动化覆盖：Python可靠性、Go单元/HTTP/SSE/竞态、Chromium请求隔离/密钥与初始化、双Mock worker+真实Go网关的三轮协议模拟。
模拟可验证有序帧、文本不丢失、取消后恢复和测试播放器水位，不能验证真人听感、真实模型或GPU效率。
Rust工具链在当前修复环境未安装，本轮未重新编译Rust；测试了NumPy备用路径。

## 7. 尚未验证与未完成

- 真实双T4、Qwen权重和第三方流式后端的兼容性、显存、输出质量及热/冷启动性能。
- 真正world_size=2训练、所有选定样本覆盖、保存后重载试听。
- DeepSeek真实长流及服务端token上限，依赖固定与下载完整性。
- 第四阶段已改为录制参考语音/语音对话两个主要视图，诊断为辅助窗口；训练任务UI仍未实现。实测波形与本地片段只有Chromium软件输入验证，未做物理麦克风验收。
- 已加入单用户Bearer访问控制、频率/并发/上传预算；仍缺账号体系、持久审计、IP/连接级防护与OS级资源隔离。仅通过可信HTTPS代理访问。
- supervisor的重启竞态、队列上限、持续故障和断网恢复尚需后续专项验证。

## 8. 安全运行说明

Kaggle会话结束将失去进程和显存，不承诺永久在线。Dataset导出/恢复只是资产持久化，不是永久会话。
启动程序会安装依赖、下载模型并可开启公网隧道，不能为本地验证直接执行整套安装器。
仅解包检查可设置 `QTTS_UNPACK_ONLY=1` 和独立 `QTTS_ROOT`，不会安装、加载模型或读Secrets。
真实使用前完成GPU依赖兼容并妥善设置访问口令和HTTPS；可设置 `QTTS_TUNNEL=none` 禁用自动隧道。


## 9. 第三阶段：只读探针与实测采集波形

- tools/backend_probe.py默认只查安装元数据；--runtime在120秒子进程内检查CUDA设备、请求精度与worker实际调用形状，丢弃依赖导入输出，不安装、不下载、不加载权重。引导程序先保存静态初检与GPU数量报告（无GPU也留报告），再于安装依赖后、下载模型前执行运行时探针，失败停止。
- surface_preflight_passed仅表示设备/调用表面检查通过。**kwargs转发语义、SDPA/CUDA Graph、显存、模型输出仍未验证；model_loaded/inference_verified/training_verified/performance_verified均为false。
- 报告0600原子写入STATE/backend_probe.json；网关GET /api/preflight需同一Bearer，只读且限制256KiB，不能远程发起探针。缺报告返回not_run，不返回模型已就绪。
- 浏览器录音由getUserMedia→AnalyserNode获取实际时域样本和RMS/峰值，不连接扬声器、不生成假波形。MediaRecorder每250ms交付数据，协商WebM/Opus、Ogg/Opus或MP4。
- 本地单段20MiB、合计63MiB（给64MiB请求预留封装空间）、合计16文件（含已选上传文件）、2048数据块上限、单段约239秒；页面后台计时可能延迟，服务端240秒/900秒等独立限额仍生效。过短/空数据不保存；超字节预算丢弃整段，不截断冒充完整录音。
- 权限等待取消后无法撤回浏览器原生权限窗口；迟到流立即停止，同一实例不堆叠未决权限请求。停止、锁定、设备结束、错误、页面离开清理资源；封装事件2秒未返回则丢弃并释放。
- 本地片段可移除，不自动上传；创建档案失败保留录音。创建档案/参考缓存仍不是模型训练。无ffmpeg时浏览器压缩容器可能无法解码，请优先上传WAV。


## 10. 第四阶段：两主视图与视口布局

- 主导航仅“录制参考语音”和“语音对话”；系统监控、兼容探针、分段、耗时、最近运行和同源网关移入原生dialog辅助窗口，支持关闭/Escape/焦点恢复，锁定强制关闭。
- 解锁后访问表单收起为状态条；停止/锁定随时可访问。主操作固定，长回答/档案/可选配置独立滚动；短CSS视口允许页面滚动，不裁切控件。只对列出的Chromium视口验证，不宣称全部手机、虚拟键盘或屏幕阅读器通过。
- 切换到采集页停止语音播放；切到对话/打开诊断停止麦克风请求或采集，保留有效片段。诊断仅打开时顺序轮询，关闭取消请求，代际隔离迟到报告。
- 声音库名称不再默认为my-voice，须自行填写1至64Unicode字符，空名/超长不上传且保留本地数据。动态参考文本/录音移除有可访问名称；速度倍率不标为标准RTF。
- 处理原生MediaRecorder先变为inactive、后到track-ended的顺序：保留所有权接收最终数据，不因重复stop抛错丢弃有效片段；原生自动stop也计算采集墙钟时长，容器时长仍由服务端检查。
- 未新增训练按钮或假成功。真正双卡训练、真实模型/DeepSeek/解码器/物理麦克风/首声/RTF/相似度验收仍待目标环境；后续门禁见仓库docs/KAGGLE_TARGET_ACCEPTANCE.md。

## 11. 第五阶段：命名空库、原始样本与参考处理

- 从采集页“声音库与样本”打开辅助窗口，先自命名空库，再添加文件/已有本地录音、勾选样本并处理。原快速创建声音档案流程保留，两个主要视图不变。打开库窗口停止采集/播放；锁定清私有内容，迟到请求不写回旧窗口。
- STATE/libraries与STATE/profiles分开：空库/原始样本不出现在可用档案中。原始样本尚未解码；默认128库、16段/库、20MiB/段、64MiB/库、512MiB总原始音频，并保留256MiB磁盘余量。对应环境变量见代码；这些是应用层预算，不是OS配额或解码隔离。
- UUID文件路径与显示名称分离，NFC/大小写折叠检查重复库名；SHA256同库去重、修订CAS、原子清单提交、上传失败回滚。目录0700/新文件0600，拒绝链接；Linux flock租约保护参考处理期间的修改/删除，进程终止后锁由OS释放，遗留running显示中断而非成功。
- 只处理明确勾选的不可变原始字节快照，继续使用既有decode/降噪/ASR/锚点处理与单并发准入。处理不是训练；完成状态在库结果提交后才公开。失败保留原始数据与上次成功生成的独立档案，未提供假训练按钮。处理成功仍不证明worker推理健康。
- 原始库仅本地工作目录保存，不自动加入Dataset包；会话结束可能丢失。处理生成的档案锚点/转写仍沿用既有Dataset备份设置。删除原始库不删除独立档案，不承诺存储介质安全擦除；参考声音应已获授权。
- 文件fsync+原子replace不等于断电恢复保证；进程在上传中断时，未引用音频/临时文件由该库下一次修改回收，损坏清单会报错需人工修复，不伪造恢复。关闭网页窗口不保证撤销已提交的服务端操作，重开刷新核对。
- 独立step5启动包；step1/2/3/4冻结。正式工作台已接近1MiB预算，本阶段通过独立文件交付，不提高限额或覆盖历史。CPU/协议/软件音频流测试不代替真实双T4、模型训练、DeepSeek、物理录音或性能验收。

- 线程池提交失败的额外边界：提交可能先排队后启动线程失败；增加提交门闩，拒绝任务即使被未来线程取出也不会执行或二次释放准入。测试用真实ThreadPoolExecutor复现这一顺序。


## 12. 第六阶段：逐条转写与不可变训练输入（不是训练执行）

- 库窗口展开“训练输入快照”，先勾选原始样本，每条单独填转写并显式选统一参考，确认声音使用权和单说话人声明。训练器、tokenizer/audio_codes、GPU资源切换和双rank执行尚未实现，不用输入准备代替优化器更新。
- 首版只接受完整24kHz单声道PCM16 RIFF/WAV，核对RIFF/chunk边界、唯一fmt/data、真实帧数、1.5–240秒/段、累计≤900秒、参考≤16秒与非恒定信号。其他格式明确拒绝，不偷偷转码或截断；规范WAV保留全部PCM帧，去掉额外容器元数据。非恒定不等于真实语音或正确说话人。
- 逐条转写1–2000Unicode码点、合计≤16000，拒绝无效Unicode；转写/声纹仅用户声明未做模型验证。同库租约取源数据快照，不改last_build或已处理档案。
- STATE/training_data用独立UUID目录，0700/0600、原子发布/失败回滚、孤立staging下次写操作回收；默认32快照、64MiB/快照、256MiB全局及256MiB磁盘余量。QTTS_MAX_TRAINING_DATASETS/QTTS_MAX_TRAINING_DATASET_BYTES/QTTS_MAX_ALL_TRAINING_DATA_BYTES控制；是应用预算，不是OS配额。
- 输出audio/*.wav、train_raw.jsonl、manifest.json、rank_plan.json，保存来源库/修订/所选ID、原始/音频/文本/JSONL/计划哈希与明确声明；JSONL只含audio/text/ref_audio，相对路径需以快照目录为工作目录。
- 双rank分配计划按固定哈希排序/轮换，不丢样本、奇数显式padding重复、两边步数相等。只是数学计划，不证明实际采样器、梯度同步或两个rank已运行。training/tokenization/two_rank_execution/inference验证标志均false。
- API只提供创建、列表、固定manifest SHA256校验与删除。列表不传回逐条转写，且integrity_verified_now=false；内容校验后才置true。校验检查文件集合/链接/音频与文本哈希/相对路径/统一参考/rank计划；不以存在即完整。不是对同UID恶意进程的签名防护。
- 界面关闭/锁定清转写、声明与结果；代际隔离迟到回复。请求失败不删除原件，已提交准备可能继续，重开刷新核对。校验开始即清旧成功状态，不把过期成功当本次通过。
- 训练输入副本不自动进入Dataset，删除原始库不删除此独立副本；可单独确认删除，亦不承诺安全擦除。仍只保证本地工作目录，不是跨Kaggle会话永久存储。

- 声音库、勾选样本集合或删样本导致所选集合改变时，授权/单说话人声明重新确认；新建库、自动回退选择或删除库不继承旧库的转写、统一参考和声明。


## 13. 第七阶段：离线声学码门禁，不是训练执行

- tools/encode_training.py仅本机CLI：fingerprint/encode/list/verify/delete。真实适配仅CPU/FP32/eager、单样本、两CPU线程、本地已物化JSON/safetensors模型；需要先固定模型目录内容SHA256，不自动下载/安装，不提供GPU或HTTP入口。
- 输入读取租约固定manifest完整核对，编码期间HTTP删除409，其他输入列表仍可用，进程死亡释放。独立STATE/training_codes复制所有规范WAV、原text/ref_audio和rank计划；不改原输入。副本不自动Dataset备份，单独删除。
- 核对上游022e286b98fbec7e1e916cb940cdf532cd9f488e的12Hz契约：恰好一个返回、ceil(frames/1920)行、16列、整数0..2047，不用zip丢掉异常返回。模型hash加载前后及发布前复核，原子发布/回滚/孤立暂存清理与分层预算。
- 父进程总超时1..3600秒，SIGINT/SIGTERM停止子进程组，必要SIGKILL；Linux worker用PDEATHSIG及ppid握手处理控制器被SIGKILL，避免孤立编码器继续持有输入；公开结果不含私人全文/底层异常。取消或超时若恰逢原子发布后响应前，结果可能已提交，应list并按固定哈希verify，不盲目重跑。
- 正常CLI没有Mock编码分支。测试可注入fixture，但输出必须test_only_codes且tokenization_executed=false。真实Qwen返回才可audio_codes_prepared/tokenization_executed=true；tokenization_verified/training/two_rank/inference均false，需要真实解码/语义及训练另验。
- 没有Torch/qwen_tts/本地权重时真实入口blocked，不能把fixture当成真实audio_codes证据。没有文本tokenizer、GPU模式互斥、优化器/梯度/检查点/两rank或性能验收。不抢占两推理GPU，不自动关闭现有服务。CPU/RAM系统沙箱与同UID恶意写入隔离不承诺。


## 14. 第八阶段：资源互斥准入，不是自动训练模式

- py/gpu_ownership.py使用固定/tmp/qtts-gpu-ownership-{uid}/fleet.lock整组独占flock，不受QTTS_STATE/CUDA索引/UUID别名影响。0700/0600、链接/属主校验；记录是诊断不是锁权威，不按PID/TTL抢占，不删除或替换锁文件。
- 真实supervisor先取得inference租约，再以pass_fds只交给workers/analyst，孩子验证inode/nonce/模式并采用同一OFD。关闭仅关本进程引用，不LOCK_UN；父死但孩子存活时仍busy，最后引用关闭才释放。第二真实supervisor失败不覆盖supervisor.pid。独立真实worker/analyst需整组独占，多个模型进程应由supervisor启动。
- tools/resource_control.py仅本机status和reserve --seconds 1..3600。预约没有执行GPU工作，不证明显存空闲/模型/训练；无任意命令/HTTP控制/force-unlock。手动停服务后再预约，Mock和CPU encode不占GPU租约。旧版本/外部进程不自动遵循协议，升级前务必停干净。
- supervisor提前安装停止信号处理、停止期间不重启、父日志句柄及时关闭；kill等待leader死亡并清理仍存活的进程组后代。bootstrap不再根据旧PID或pkill广泛杀进程，busy/遗留PID标记明确阻断，本次ready等待检查新supervisor仍活着，避免读到旧服务就宣称新启动成功。
- SIGKILL留下的活孩子仍持锁，不能删锁文件强行恢复；须核实并停止本应用遗留模型进程。跨UID/容器/非合作进程、同UID恶意改文件和真实显存回收不属于协议保证。
- 没有自动排空会话/推理↔训练切换、GPU编码/训练器/DDP/梯度/optimizer/检查点或真实性能证明。真实目标设备仍须单独验证。码副本完整来源封存及训练读取租约仍待后续。


## 15. 第九阶段：来源封存与读取租约，不是训练执行

- 新码schema2原样封存source/manifest.json、source/train_raw.jsonl，源hash固定为创建请求hash，交叉核对源库/修订/所选ID与顺序/原始及规范音频hash/逐条文本/统一参考/声明/计划。source文件纳入安全目录/预算/原子发布/回滚，不自动云备份。
- schema1历史码仍可列表/核验/读取/删除，明确legacy-unsealed，不猜旧授权、不自动升级或改旧hash。列表source_provenance_policy是格式政策，不声称已经检查所有封存文件；只有本次完整核验才返回provenance_verified_now=true。
- TrainingCodesStore.lease固定主清单hash并全核验后持有目录外.use-{id}独占读取锁，长读取不占全局锁；同版本删除/第二读取409，其他版本仍可操作。进程/最后继承FD关闭释放，不能靠PID/TTL抢占。合作式只读约定，不是OS只读挂载或同UID恶意改写隔离。
- encode_training.py新增hold-read --seconds 1..3600，保持检查租约，不执行GPU/命令/训练；沿用总超时、取消与PDEATHSIG。收据只给schema/状态/计数，training_allowed=false；fixture仍test_only_codes，旧码仍legacy-unsealed。
- 尚无真正训练器/作业执行与DDP多rank读取接管。未来训练器须持有这些租约直到所有读者退出，并另验真实编码/语义/资源/授权政策；读取租约不授予训练许可。GPU模式/编码/优化器/梯度/检查点和真实音质性能仍未验收。


## 16. 第十阶段：真正训练核心已开发，T4/Qwen运行尚未验收

- tools/train_tts.py提供fingerprint与train，不是预约或模拟训练；新增联合loss/DDP/LoRA/GradScaler/梯度累积/参数更新/adapter保存代码。FP16/eager、冻结Base1.7B、FP32 q/v LoRA与AdamW状态，microbatch1，序列超限拒绝而不截断。文本过text_projection，全部参数相关调用在DDP.forward内。
- 只接受schema2实际编码状态与明确数据审阅/实验确认，拒绝fixture/legacy；Base与speech tokenizer内容固定hash，严格离线/非pickle/不信任remote code。用户审阅不是机器语义/法律鉴定，原码的未验证标志不变。
- 两个真实CUDA rank各绑定一个可见设备，NCCL、确定性样本划分、奇数重复前缀填平不drop_last、尾部累积正确缩放；非有限loss全rank失败，非有限梯度全rank跳步降scale，至少有参数变化且两rank最终adapter digest一致才可保存。
- 父持GPU offline-reservation整组OFD与码读取OFD，两个受控rank继承/核验相同FD与pin；默认推理adopt仍拒绝offline模式。父死孩子仍持锁，rank在torch/CUDA前设PDEATHSIG并核对ppid；取消/超时/启动失败等待直接rank退出。DataLoader无额外进程；不自动停推理/恢复或强制解锁。
- 保存adapter.safetensors、speaker.safetensors、固定Base/码hash与每rank覆盖/版本/峰值显存/更新报告，原子发布到本地training_runs；load_adapter可加载到单独可信Base并返回参考speaker embedding。不是完整CustomVoice模型，不保存可恢复optimizer/scheduler状态，不自动接入现有语音聊天/替换推理，也未新进程Qwen重载试听。
- CPU小网络真实张量/联合loss/反向/优化器/FP16冻结参数/Gloo两进程验证与Qwen/CUDA/T4严格分开。沙箱安装Torch仅用于这些测试，无GPU/权重，不能声称真实Qwen训练通过、16GB已可用或音质达标。training_runs及原数据/码均私有，不自动Dataset备份。
- 核心开发现在进行，不再等待额外基础设施阶段。目标真实开训仍需双T4、可信完整本地Base/tokenizer、授权语音及正确依赖；后续直接目标是Qwen现场开训与训练adapter接入推理验证，不再以收据工具替代核心功能。
