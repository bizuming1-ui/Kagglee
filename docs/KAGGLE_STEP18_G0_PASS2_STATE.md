# 第十八阶段 G0：全源第二遍第2批——数据、产物、恢复与认证

日期：2026-10-23。分支：`arena/1160bd87-kagglee`。状态：**限定审计/回归完成，G0仍PARTIAL/BLOCKED；产品未改，缺陷未修，18包未发布。**

## 1. 本批范围与真实覆盖

沿已确定的G0计划继续，不重开问题、不新增问题28，不以测试通过代替源码三遍审查。新增第二遍全文语义阅读7份、1526行，读至各文件末尾；按分段输出核对首尾，无截断。登记脚本只依据该阅读事实、基线hash/行数更新台账，不从测试数量推导阅读覆盖。

| 全文文件（`kaggle/source/py/`） | 行数 | 本次交叉复核重点 |
|---|---:|---|
| `voice_library.py` | 351 | 私有普通文件/no-follow、全局/库租约、revision与原始字节hash、snapshot/begin/finish、元数据原子替换及失败清理 |
| `training_data.py` | 285 | 严格24k mono PCM16 RIFF边界、每样本文本与权利声明、不可变输入快照、manifest/audio/jsonl/rank_plan绑定、staging发布、读租约与删除 |
| `training_codes.py` | 355 | 本地模型树fingerprint/安全JSON、CPU encoder提供包身份、schema2来源封存、逐row/code/audio验证、发布前复验、同OFD继承/adopt与失败关闭 |
| `trained_profiles.py` | 155 | request/result/rank报告交叉核对、真实safetensors NumPy结构与hash、fixture/legacy声码拒绝发布、参考文本绑定、发布前二次pin验证、禁止Base/Mock静默回退 |
| `persist.py` | 99 | profiles/active备份范围、上传与恢复分支、scope预检、候选切换与归档一致性、远端操作证据边界 |
| `qtts_common.py` | 211 | JSON/日志、profile定位、tar路径预检与逐文件替换、输出增益配置边界 |
| `access_control.py` | 70 | 默认认证目录不进入Notebook输出、token格式/权限/本地锁、仅本地同端口HTTP gateway转发 |
| **合计** | **1526** | **7份第二遍全文** |

另局部复查 `analyst.set_candidate` 原函数及既有测试fixture；**不计analyst第二遍全文**。测试文件的局部读取也不计产品源码覆盖。

- 第一遍：53/53内嵌资产，13668行，保持不变；不是整个Git仓库全部文件已审。
- 第二遍：上批8/1056 + 本批7/1526 = **15/53、2582行；剩38份**。
- 第三遍：0/53。
- 当前台账：`docs/validation/step18/g0-pass2-state-coverage.json`；历史台账和已发收据不重写。

## 2. 依赖链、边界与保留合同

1. 原始库保留原始字节与revision；训练输入按明确样本id/独立文本/显式权利确认生成新快照，不把库的建档记录当训练成绩。
2. `canonical_wav`要求完整24kHz、单声道PCM16，至少1.5秒；训练路径每文件/累计上限还受`min(240, limits.seconds)`与`min(900, limits.total_seconds)`约束。可忽略合法非fmt/data chunk并重封装，但PCM不得被截短、重采样或悄悄换声。该严格入口**不是已经支持任意>10分钟单条录音训练**，分段、文本对齐与真实长数据训练仍未验收。
3. 输入manifest pin、JSONL、逐WAV与rank_plan建立一致绑定；rank_plan只是数学分配计划，不是双GPU采样或优化器实际执行轨迹。
4. 声码构建持输入租约，封存来源manifest/原始JSONL、独立复制PCM，逐条验证`ceil(frames/1920) × 16`个0..2047普通整数，完成后复验输入与整个staging，再rename发布。取消/IO失败必须清staging且释放输入租约，原库与输入不应被改写。
5. schema2声码可脱离已删除原库/输入继续校验封存来源；这只证明本地来源/结构绑定。`test_fixture`即使完整封存、能取得读租约，也始终`test_only_codes`，tokenization/training/inference标记仍false；**租约不是训练准入许可**。
6. `adopt_lease`要求继承同一个开放文件描述而非仅同inode；校验失败须关自己的dup，不能关调用方FD，也不能遗留额外OFD阻塞删除。本批实际flock/FD故障回路验证这一点。
7. 训练产物检查会读取真实safetensors容器及NumPy数组、交叉检查rank报告/成员/摘要；本批使用合成权重与手工报告。**JSON里写了NCCL/optimizer已执行，不等于实际跑过NCCL/优化器**。发布还要求真实已准备声码、来源一致、显式未验收确认；无fallback合同必须保持。
8. `_pack`只遍历profiles及active，不自动保存raw libraries/training_data/training_codes/training_runs或默认认证目录，也排除`_cal_`临时profile。因此当前Dataset备份**不是完整训练工程/权重恢复方案**；不能许诺跨Kaggle会话完整恢复训练。profiles内参考/转写本身仍属敏感数据；不能把“排除训练目录”说成备份无隐私内容。
9. tar scope/path/type预检拒绝越界与链接；实际落盘是逐文件临时文件+replace，**不是整个状态目录事务**。第一批已记录第二成员IO失败部分提交；本批未修，不能冒称恢复原子性已验收。
10. 默认auth目录以state路径摘要隔离、位于临时目录；重复provision保留同一token、目录0700/文件0600。只向精确本地gateway端口HTTP附加token，不传给不同端口worker、外部host或userinfo伪装host。测试只用临时生成token/固定合成token，不向远端发请求、不输出token值。

F01（旧`qwen-tts`元数据查询与HF提供包不符）和F16（额外后代持OFD退出清理）仍未修。此次完整复读不改变其既有证据边界。特别是未重新运行已缺失upstream cache依赖的独立真实wheel-provider六案例，不用当前fixture替代该历史证据。

## 3. 新实证 F17：备份与候选切换交错，恢复后引用缺失锚点

**确认未修；不是猜测、不是修复后的绿色测试。**

源位置：`persist.py:27–36`、`analyst.py:1067–1082`，以及`qtts_common.extract_tar_safely`的逐文件恢复。`_pack`递归`tarfile.add`没有与profile候选切换共享一致性屏障/不可变版本快照。

确定性步骤（每轮均重建独立临时状态）：

1. 准备合成PCM WAV候选0/1，当前profile指向`anchor_0.wav`，尚无`anchor_1.wav`。
2. 原`_pack`递归归档profile，tarfile已经枚举该目录的现有文件名。
3. 在已打入`anchor_0.wav`、尚未读取后面的`profile.json`时，由serializer hook运行**原`set_candidate`函数体**，切换index=1：真实`shutil.copy`生成新锚点，真实原子JSON替换更新anchor/ref_text。只有admission/worker reload是明确fixture；不执行模型。
4. live profile及其新锚点完整存在，且锚点字节等于候选1。
5. tar按先前枚举的文件名继续打包，读到新的`profile.json`，却不会追加刚创建的`anchor_1.wav`。
6. 用原`extract_state_members`和`extract_tar_safely`实际解包不抛异常；恢复的profile指向`anchor_1.wav`，文件不存在。

这证明本地并发可达的备份一致性缺口；并未调用远端Kaggle snapshot/restore、未跑完整HTTP竞争/线程压力、未证明用户现有Dataset损坏、未运行Worker模型加载，也不把它当用户沙沙/低响度根因。测试不是修改产品来制造失败，只在原函数间控制交错时机。

三轮观察收据均包含F17的live-anchor-present与restored-anchor-missing真值；旧F16亦保留在本轮观察收据中。新增finding只登记F17，不重编号、覆盖历史问题或300条原始建议。

后续修复方向（**尚未实施/未作新设计签收**）：需在G0完成后比较与候选变更共享profile级锁、从不可变版本打包、以及发布前自校验/重试；恢复要验证profile引用/版本，并明确整体事务与失败回滚政策。不能仅补齐这次漏掉的文件名或忽略缺失锚点。

## 4. 新增12项边界：11保护 + 1原缺陷观察

文件：`kaggle/tests/test_pass2_state_boundaries.py`。

| # | 检查 | 结果含义 |
|---:|---|---|
| 1 | 封存第二文件写失败，清staging、释放输入租约、原库/输入不变且可重试 | 保护 |
| 2 | 最终发布rename失败，回滚staging且可再次构建 | 保护 |
| 3 | encoder返回后立即取消，只执行一条fixture编码且不发布 | 保护 |
| 4 | adopt校验期间封存来源损坏，失败关dup而不关parent FD，parent释放后可删除 | 真实FD/flock保护 |
| 5 | 原库和输入删除后，封存来源仍可验证；所有fixture执行/训练标记仍false | 保护，不是训练 |
| 6 | 38400/38401帧按20/21码帧、0/2047边界，拒bool/浮点/字符串/越界及少帧 | 结构保护，不是编码精度 |
| 7 | 合法odd-sized JUNK chunk重封装，全部36000个PCM样本逐字节不变 | 合成WAV保护 |
| 8 | pack只收profiles/active，排除校准临时目录、raw库/数据/训练/认证目录，不运行远端命令 | 备份范围保护 |
| 9 | 目标已有指向恢复根外的symlink，完整预检后拒绝，前面合法成员也不写入 | 安全预检保护，不是IO故障整体回滚 |
| 10 | 默认auth按state隔离、位于state外、稳定token与0700/0600权限 | 本地临时认证保护 |
| 11 | 仅local gateway同端口HTTP附header，异端口/外部host/https/userinfo伪装不附 | 转发保护，无网络请求 |
| 12 | 打包与原候选切换确定性交错后，解包profile引用缺失锚点 | **F17观察通过=确认缺陷，不是已修** |

预检首次1项error来自**测试提取器保留了HTTP注册装饰器**导致`app`未定义；11项已过。修正测试提取为只去装饰器、原函数体不变后12/12通过。保留`pass2-state-preflight-attempt1.txt`失败原日志及最终`pass2-state-preflight.txt`；未修改产品以绕过预检，不隐去失败。

## 5. 三独立轮专项回归

runner：`docs/validation/step18/run_pass2_state.py --round N`，N=1、2、3；独立Python进程，依次执行，临时状态隔离。

组成：上批219项 + 本批另选既有`test_training_data`19、`test_training_codes`33、`test_code_provenance`21、`test_qwen_compat`20（共93）+ 新12 = **324项/轮**。按逐测试ID去重、保留顺序与hash。

| 轮次 | tests | failures | errors | skipped | 结果 |
|---|---:|---:|---:|---:|---|
| 1 | 324 | 0 | 0 | 0 | PASS |
| 2 | 324 | 0 | 0 | 0 | PASS |
| 3 | 324 | 0 | 0 | 0 | PASS |
| **合计** | **972** | **0** | **0** | **0** | **专项通过，非产品验收** |

覆盖包含原始库、合成PCM/JSONL、来源封存、CPU真实子进程/取消/租约、显式HTTP/模型替身、实际本地HTTP、真实NumPy/safetensors解析，以及本批实际tar/文件操作。套件中已有故障注入会打印预期异常；正式结果以逐ID收据为准，不把console出现的fixture traceback当未捕获套件错误。

保存每轮`pass2-state-roundN.json`、`pass2-state-regression-roundN.txt`、`pass2-state-console-roundN.txt`，含53源、测试/runner/support hash、依赖版本、逐ID结果、观察和真实性标记。

**不包含**实际Torch算子/optimizer/GradScaler/Gloo/NCCL、真实Qwen声码、权重训练、GPU/双T4、用户WAV/相似度/去沙沙/自然连续朗读/物理声卡、DeepSeek真实prefix首声或提速测量。NumPy2.2.6不等于生产requirements2.4.6；Rust缺工具链，未编译或执行。此次未重跑独立旧CLI四矩阵、Go race/完整Go协议、Chromium全量、14分析AST/12 DSP独立矩阵或缺缓存的provider六案例，不挪用历史数字充本轮成绩。

## 6. 工具、冻结、证据与交接

- 本批`npm test`：Node30/30；`npm run check`：PASS。
- Python AST：全部产品Python及本批test/runner/advance/verifier/refresh共38份：PASS。
- `kaggle/repack.py --check`：PASS，确定性包内容一致。
- 新校验器：`docs/validation/step18/verify_pass2_state.py`，检查当前覆盖、324×3逐ID/观察/hash、原300建议与Q25–27各50、冻结与完整交接内嵌；不重签旧检查点。
- 原53源、94冻结hash、正式15文件和正式revision保持，历史handoff保持；本批开始408份历史证据hash保留；上批382清单及其后产物仍在。
- 新run manifest冻结本批输入/报告/收据/日志/校验器/交接hash；进度输出为`progress-pass2-state.json`和当前`progress-checks.json`，自引用输出不纳入自身manifest。
- 新完整报告加入交接，累计**73份备忘录全文**。`handoff-progress.json`记录实际字节数与SHA256；嵌入原文逐份核对，不在本报告预填循环依赖hash。
- `git diff --check`须通过；不提交或推送也能保存当前分支工作。

## 7. 下一步与未签收门禁

继续剩38份第二遍，优先模型provider/voice binding/worker/分析API间的版本、失败、取消与参考贡献链；补齐全53份第三遍、300条建议的最终处置/失败见证映射，再按既定S1–S8顺序实施。当前已确认F01–F17及旧边界/专题问题按各自证据保留，不能因专项绿色而消除阻塞。

不改冻结17/正式工作台/空白文件与浏览器复制行为，不发布18包，不默认融合prompt列表、添加参考PCM、切向量策略或强滤波；不提前打开Q28，不要求用户点击Continue。>15秒/极长录音、<10秒相似度、>10分钟真实训练、双GPU等效参数、generated-only播放、DeepSeek首可用prefix即生成、更响受保护输出、更低创建/首声延迟、安全/取消/隐私/冻结版本等要求均未撤销，仍需分层实证。整体保持**PARTIAL/BLOCKED**。
