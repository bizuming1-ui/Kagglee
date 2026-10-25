# 第十八阶段 G0：全源第二遍第3批——provider、参考绑定与推理生命周期

日期：2026-10-23。分支：`arena/1160bd87-kagglee`。

**本批限定审计完成；产品未改、缺陷未修、G0仍PARTIAL/BLOCKED，无18发布包。** 专项通过不是完整功能、真实模型、训练或声学验收。

## 1. 全文阅读和进度

| 文件（`kaggle/source/py/`） | 全文行数 | 第二遍复核重点 |
|---|---:|---|
| `qwen_compat.py` | 97 | HF/旧发行包命名空间、现代/旧RoPE配置、registry身份与幂等、失败分类和smoke边界 |
| `voice_binding.py` | 60 | 跨语言domain与长度前缀、生成参数规范化、参考文件类型/预算/no-follow、绑定的能力边界 |
| `worker.py` | 680 | GPU准入、模型/提示缓存、版本检查与锁、取消/错误/终态、generated-only播放、统计和ASGI生命周期 |
| `clone_stream.py` | 126 | 条件模式、生成码与参考码隔离、有限左上下文/右lookahead、提交位置、finish与生成器清理 |
| `adapter_engine.py` | 108 | Base/adapter绑定、磁盘profile重读、适配器选择提交、真实句缓冲语义、取消与PCM验证 |
| **新增合计** | **1071** | **5份重新全文语义阅读** |

worker按1–170、171–340、341–510、511–680逐段完整复读；其余四份完整输出。上述源输出无截断。测试/调用点的局部查看不计其他产品文件第二遍；分析API全文留在下一批，不以测试经过API路径代替全文覆盖。

- 第一遍：53/53内嵌资产、13668行，保持；不是整个Git仓库所有文件已审。
- 第二遍：上批15/2582 + 本批5/1071 = **20/53、3653行，剩33份**。
- 第三遍：0/53。
- 当前覆盖：`docs/validation/step18/g0-pass2-inference-coverage.json`。既往台账/报告/收据保持历史意义，不重签。

## 2. 语义链与必须保持的合同

### 2.1 provider / RoPE / 实际运行边界

桥先根据发行包元数据选择HF路径，拒旧`qwen-tts`与`qwen-tts-hf`同命名空间并存，以及已加载兼容模块却无HF元数据的状态。对现代default配置，从实际`rope_parameters`取theta/partial factor，复制config后委托已识别的原initializer，不猜默认theta、不修改权重、不全局覆盖其他registry项；未知schema、非法范围、registry漂移必须拒绝。

桥强制比较HF/Transformers组合；Faster版本虽收集进versions，桥本身未逐项对照其PINS。**此处仅记录源码观察，尚需完整启动/安装/preflight政策链反证，不升级为已证生产故障。** 新registry保护使用明确上游函数fixture，不是实际Transformers/Mimi数值运算；旧真正wheel/config实验保留历史证据，当前未重跑。

`RealEngine.load`要求单可见CUDA设备和允许的dtype；T4不能把软件BF16支持当原生能力，FP32只可显式准入。warmup/sanity是运行门禁，不是声纹、逐字正确或质量验收。新测试不执行这些模型步骤，不把`model_loaded`字段或mock health当GPU证明。

### 2.2 绑定、缓存与加载

reference pin由domain、参考原始字节、参考文本、语言与四个规范化生成参数组成；显示名称、quality和未选候选不纳入这个内容pin。它**不是认证、候选贡献评分，也不单独绑定trained adapter权重**。训练后端另有binding/manifest/Base交叉检查，不能拿普通参考pin代替适配器绑定。

文件打开含no-follow/nonblock，先fstat确认普通文件与1..64MiB，再有界读取。空/超预算/FIFO拒绝；本批FIFO在真实短子进程中验证，超时会由subprocess.run定向清理，不依赖“当前没卡住”的猜测。

Worker持同一锁读取磁盘profile、验证session模式/内容pin、提取prompt后二次检查，再提交worker profile/binding；不得在锁外先抓旧快照，不得先发静音或参考PCM掩盖错误。新测试验证初次提取期间参考变化会拒绝且不登记worker绑定，**不宣称engine内部prompt已事务回滚**：F08仍未修。

### 2.3 生成、generated-only与指标

Faster路径把参考码仅用于talker conditioning，GeneratedCodecWindow只接生成码；16组、24kHz、1920样本/帧、25帧左上下文与默认0右lookahead合同不变。窗口保留/提交/finish需要真Torch与实际codec进一步证明；本批全文复核不等于执行了Torch张量或预训练codec。

RealEngine迭代器在消费方close或采样率错误时应调用下游close；新检查使用有限PCM重放迭代器及仅`manual_seed`的显式模块fixture，不安装Torch、不模拟Tensor/算子，不测生成性能。实际目标text与参考text分离、参考PCM不拼接的既有保护继续回归。

Worker只产生规划静音，不插入参考呼吸；trimmer/leveler旧短块/短尾问题保留。`model_first_chunk_ms`是引擎首数组到达，`first_chunk_ms`是DSP后首PCM，不是浏览器或声卡首声。speech_samples、flush、规划暂停与端到端首声不得混算；EMA、rtf_target字段不证明RTF≤0.3。

排队取消验证只覆盖未读取profile、未启动引擎、未释放他人持锁以及唯一stats/None收尾。**锁等待/刚取得锁时的提前返回目前缺少cancelled标志**，不以这项所有权保护签收取消终态语义；列为后续矩阵观察。

### 2.4 训练后端

AdapterEngine每次选择重读受预算/no-follow保护的磁盘profile，比较trained binding，检查Base/adapter/codes pin与speaker维度，准备并提交adapter。不得静默回退到Base/Mock。新测试执行真实文件访问与原`_profile_now`，拒重绑定、删除、symlink和超预算，失败不改变key/prompt；没有执行模型加载、adapter张量提交或真实推理。

该后端明确**整句缓冲**：官方generate返回完整单条波形后才yield，取消只能通过StoppingCriteria/返回后检查配合，不能抢占CUDA kernel或codec。不能把它的一个yield切成假块就宣称原生声学流式、真实首声提速或双GPU一致。

## 3. 新实证 F18：正文开始前断连，没有传递取消到已启动生产线程

**确认未修。** 源位置`worker.py:650–674`：`synth`在返回StreamingResponse前启动生产线程；cancel只在内部async generator的finally中设置。若正文生成器尚未第一次进入，关闭这个未启动的生成器不会执行其finally。

两条真实Starlette响应控制流，各独立三轮：

1. **ASGI 2.4**（纳入每轮336项）：真实原`synth`启动明确CPU生产线程；真实StreamingResponse发送`http.response.start`时，send fixture抛断连OSError。原响应抛ClientDisconnect，正文未开始。再显式aclose body iterator，生产cancel仍未设置，线程仍等待。
2. **ASGI 2.3**（独立companion probe）：真实响应在发送响应头的await期间暂停；receive fixture随即返回`http.disconnect`。真实响应task group退出/取消header发送任务，正文仍未开始；生产cancel仍未设置，线程仍等待。

所有实验finally只设置自己创建的cancel并join自己创建的生产线程，验证其退出；没有留下后台等待线程。使用实际安装的Starlette1.9.0，收据包含版本和responses模块hash。ASGI send/receive时机与生产工作负载明确fixture；**没有实际TCP/浏览器断连、模型生成、显存增长或Kaggle线上故障证据**。不把它认作用户噪声根因，也不保证所有服务器版本都走相同分支。

它补足旧测试“已取到首PCM再aclose”的盲区：旧测试仍通过，但不能覆盖首次迭代前断连。与F07无界队列不同，本项证据是**取消所有权缺失**，不以有限CPU实验声称测出了无限内存或GPU泄漏。

F18登记在`g0-pass2-inference-findings.json`；F01–F17与其他历史边界/专题发现保留，不被绿色观察测试消除。后续方向需比较响应全生命周期清理、生产者启动时机、取消令牌和有界队列的联合所有权；**尚未实现或作新设计定案**，不能只补测试里的断连分支。

## 4. 新12项边界：11保护 + 1原缺陷观察

文件：`kaggle/tests/test_pass2_inference_boundaries.py`。预检12/12通过，无失败/错误/跳过。

| # | 检查 | 证据边界 |
|---:|---|---|
| 1 | generation默认值等价、合法int/float规范化、无关元数据排除及非法边界拒绝 | 原Python pin/编码函数 |
| 2 | 空参考与64MiB+1稀疏文件拒绝 | 真实fstat/文件，不分配大数组 |
| 3 | FIFO无writer仍能及时拒绝 | 真实CPU子进程/系统FIFO，有超时清理 |
| 4 | 排队取消不读profile/调用engine，不释放他人持锁，仅一次stats/None | 真实锁/线程；不验收cancelled标志 |
| 5 | 初次提取中参考改变，拒绝并不登记worker profile/pin | 原Worker + 文件；提取回调fixture，不代表F08修复 |
| 6 | RealEngine采样率错误仍关闭重放迭代器一次 | 原stream + 明确manual_seed/PCM重放fixture |
| 7 | 消费方关闭时下游close一次、seed掩码保持 | 同上；不执行真实codec |
| 8 | 无prompt时不创建生成迭代器 | 同上；无模型 |
| 9 | RoPE桥不改其他registry/原config，原异常和参数传递保持 | 原桥 + 明确initializer fixture |
| 10 | trained磁盘binding变化/删除拒绝，恢复原文件后可读 | 原AdapterEngine._profile_now + 文件 |
| 11 | trained profile symlink/超预算拒绝，key/prompt未变 | 同上；无adapter加载 |
| 12 | ASGI2.4响应头阶段断连后取消未传给生产线程 | **F18观察通过=确认缺陷，非修复** |

ASGI2.3补充脚本：`docs/validation/step18/probe_pass2_inference_asgi23.py --round N`，不塞进336项、也不冒充另一轮完整回归。

## 5. 三独立轮与真实性

runner：`docs/validation/step18/run_pass2_inference.py --round N`，独立Python进程、独立临时状态，完整专项轮依次执行。组成：上批324 + 新12 = **336项/轮**，逐ID去重、原324顺序保持。

| 轮次 | tests | failures | errors | skipped | 结果 |
|---|---:|---:|---:|---:|---|
| 1 | 336 | 0 | 0 | 0 | PASS |
| 2 | 336 | 0 | 0 | 0 | PASS |
| 3 | 336 | 0 | 0 | 0 | PASS |
| **合计** | **1008** | **0** | **0** | **0** | **限定专项，不是全功能验收** |

另ASGI2.3 companion独立三轮，各1项观察通过；不计入1008。每轮正式收据保留逐ID、53源/测试/runner/support hash、依赖版本、F16/F17/F18观察真值和真实性标记。历史F16额外后代最后定向清理/锁释放、本批F18生产线程退出均实际检查。console里的故障注入异常不是未捕获套件错误，结果以逐ID收据为准。

既有真实本地HTTP/文件/flock/子进程、NumPy与合成safetensors测试本轮重跑；新ASGI断连是进程内事件，不冒充socket断连。没有真实Torch算子、optimizer、GradScaler、DDP/Gloo/NCCL、Qwen/Faster模型/编码、训练、双T4、Rust编译/执行、用户音频、声纹/沙沙/自然连续听感、DeepSeek真实prefix或物理声卡/性能测量。

## 6. 环境、工具与冻结

本轮开始发现`.venv`及其CPU依赖未保留。首次探测命令出现`.venv/bin/python: No such file or directory`，**不是测试失败或产品缺陷**；随后重建隔离venv，固定NumPy2.2.6、safetensors0.6.2、FastAPI0.156.4、Starlette1.9.0、httpx0.28.1、requests2.34.2、soundfile0.14.0、uvicorn0.34.0、python-multipart0.0.20。安装日志与完整pip freeze保留；未承诺全部传递依赖与旧环境完全相同，以当前environment/freeze为准。没有安装Torch/Qwen、Rust或Go；NumPy版本仍不等于生产requirements的2.4.6。

- Node30项、JS check、产品Python与本批test/runner/advance/verifier/probe/refresh共39份AST、repack一致性：检查日志单列。
- 本批开始435份历史证据hash保留，53源/94冻结/15正式文件及正式revision不变，旧handoff保持。没有18包。
- 新校验器`verify_pass2_inference.py`核对当前20/53覆盖、336×3逐ID/观察/hash、ASGI2.3 companion三轮、旧300建议/Q25–27各50、冻结和完整内嵌交接。
- 当前`progress-pass2-inference.json`与`progress-checks.json`保存结果；新manifest覆盖本批输入/日志/收据/报告/校验器/交接，排除自引用进度输出。
- 交接新增此完整报告，累计**74份备忘录全文**，实际字节/SHA在`handoff-progress.json`，逐份内嵌原文核对，不在报告预填自引用hash。
- `git diff --check`作为最终检查；本轮未重跑独立旧CLI四矩阵、完整Go/race/协议、Chromium全量、14分析AST/12DSP或需要缺失upstream cache的真实provider六案例，不挪用历史数字。

## 7. 下一步与未签收门禁

下一批复读分析/API及参考切分，核对provider版本政策与启动/worker/会话间失败、取消、参考贡献和校准版本链；继续剩33份第二遍、全53份第三遍和300条建议最终处置/失败见证映射，再按既定G0→S1–S8实施。新发现不等于已有纠正，当前不绕过G0修产品、不新增问题28、不要求Continue。

保持冻结17、正式工作台空白文件/用户粘贴/完整浏览器复制；不盲目prompt列表融合、改向量策略、强滤波或拼入参考PCM。>15秒/极长录音、<10秒相似度、>10分钟真实训练、双GPU等效参数、generated-only、DeepSeek首可用prefix即生成、更响受保护输出、更低创建与实际首声延迟、安全/取消/隐私/版本冻结等要求均未撤销，仍须真实分层证据。整体**PARTIAL/BLOCKED**。
