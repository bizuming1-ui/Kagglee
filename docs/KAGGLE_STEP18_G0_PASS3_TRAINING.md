# G0 全源第三遍第3批：训练输入、声学码与产物提交

日期：2026-10-23；分支 `arena/1160bd87-kagglee`。

**第三遍累计20/53份、5365行，剩33份8303行。前两遍各53/53份、13668行保持。产品冻结，G0仍PARTIAL/BLOCKED。** 这是冻结包53源资产，不是整个Git仓库全审/全功能/目标模型验收。

## 1. 本批全文复读：8份1505行

| 文件（相对 kaggle/source/） | 行数 | 复核重点 |
|---|---:|---|
| py/training_data.py | 285 | WAV全部帧、文本/声明、选中来源/revision、预备目录/发布、只读租约 |
| py/training_codes.py | 355 | 模型指纹/结构、schema2封存来源、逐样本完整码、取消末门、继承OFD |
| py/training_job.py | 227 | 严格准入/参数、双rank进程、FD/密钥、checkpoint发布与最终回执 |
| py/tts_training.py | 200 | JointLoss/DDP/累积/溢出、采样覆盖、实际优化入口、rank报告/保存；仅源码语义 |
| py/tts_dataset.py | 125 | 完整文本/16码本序列预算、缓存克隆、collate偏移/标签/掩码；仅源码语义 |
| py/trained_profiles.py | 155 | 完成记录/hash/实际safetensors解析、绑定、固定参考文本、发布前重核 |
| tools/encode_training.py | 128 | 离线CPU子进程、parent-death、私有回执、超时/取消与提交提示 |
| tools/trained_voice.py | 30 | 显式未验adapter声明、describe/publish参数与脱敏错误 |
| **合计** | **1505** | **8份重新完整阅读** |

初次三组拼接输出被截断，不计那次为全文；随后逐组完整补读，training_codes分1–180/181–355，其余完整范围均无截断。tts_training与tts_dataset的张量/优化语义是源码审查，不冒充Torch执行。adapter_engine/lora_adapter/qwen_compat及train_tts等剩余文件不因调用或旧辅助测试阅读获得本批全文信用。

**计数纠正：**进度曾手算为1605行，信用生成器断言失败，未写错误覆盖文件；逐项求和为1505。已保存`pass3-training-credit-correction.json`，校正为3860+1505=5365、13668−5365=8303。没有加文件/测试或修改源代码抵消错误。

## 2. 新增12项：11保护＋1未修观察

`kaggle/tests/test_pass3_training_boundaries.py`实际执行文件、PCM、flock/OFD、原控制器与受控CPU子进程、原产物检查/发布事务及CLI。明确不导入Torch算子，不进行优化器/Gloo/NCCL/模型/实际训练。

| 项目 | 已验证及边界 |
|---|---|
| raw输入准备遇KeyboardInterrupt | audio/JSONL已写后中断，清pending，保留已有snapshot/原库，释放租约后可重试 |
| PCM极值/奇数帧数 | −32768/+32767和36001帧完整保留，带奇数长度JUNK元数据被移除；总帧预算少1明确413，不裁切 |
| acoustic codes最终取消 | 原完整_verify已经通过后置取消，最后rename前409、清pending；原输入保持，可重新prepare |
| 第二样本encoder遇BaseException | 第一份已编码/落盘后KeyboardInterrupt，全部本次pending清理，源租约释放，后续重试成功 |
| Qwen finish指纹 | 只构造无tokenizer对象执行原finish，materialized字节变更409；**未执行构造器/编码，不绕过F01** |
| code OFD最后引用 | 原adopt_lease保留dup，父上下文先关后删除仍409；最后adopt上下文关后才可删。进程内FD试验，不是此项执行双rank |
| cancelled结果拒绝 | 即使有可解析的合成adapter，结果改cancelled仍409、不创建profile |
| request/epoch拒绝 | request样本顺序不一致、rank loss NaN各自409；未穷尽所有rank/类型/报告矛盾 |
| publish第二次检查 | 写完候选JSON后更改speaker tensor，原最终inspect拒绝、清临时档案、保留active；profiles正常.lock保留 |
| 固定参考匹配 | 非首行的真实参考WAV配其自身文本、保存pin，不改active/不声称quality/reload；code lease元数据及adapter均为fixture |
| trained_voice CLI | 错pin返回rejected/409/exit2、不创建档案、不带私有路径或Traceback；无模型加载 |
| F35 | 原控制器空检查点仍报告优化器执行，产物检查器会拒绝，详见下节 |

### 首次预检失败及修正

首次收集43项，其中31项是直接导入TestCase类带来的既有重复项；新增断言有1失败：误将正常留下的`.lock`视为发布残留。原事务正确清理了`.trained-profile-*`且没有新profile。改用模块导入避免重复收集，断言明确仅`.lock`保留。产品/旧fixture未改；首次原始日志和`pass3-training-precheck-correction.json`保留。最终预检仅新增12项、12通过；三轮累计不计那31项重复。

## 3. F35：子进程成功＋manifest存在，不足以声称优化器执行

原`run_controller`在两个rank exit0后，核验code pin、Base指纹及`adapter/manifest.json`文件存在，即把最终结果标为`completed`/`optimizer_execution_observed=true`，未在该阶段解析检查点内容或核对完整rank报告。

受控见证：

1. 使用真实本地raw/code fixture快照；仅训练准入、依赖存在与tokenizer一致门禁为显式测试替换，无生产CLI开关。
2. 两个真正自有CPU子进程执行原GpuLease/code OFD adopt与parent-death握手，随后正常exit0，不执行rank_worker/run_rank/优化器。
3. rank0只创建`adapter/manifest.json`，内容为`{}`；没有adapter/speaker tensor。
4. 原控制器仍生成`completed`、rank_exit_codes=[0,0]、optimizer_execution_observed=true；磁盘result与回执一致。
5. 原`TrainedArtifacts.inspect`409拒绝该产物；信号处理恢复，code与GPU租约可再次获取，没有发布非法声音。

**结论仅为控制器回执的证据不足**，不是实际训练成功、真实rank会生成坏检查点、模型错误或发布绕过的证明。正常源码run_rank/save_checkpoint还有完整报告/权重保存与rank同步；本见证有意替换它们，不能用结果否认真实优化代码存在。与F13–15工具自检、F16后代清理及F01包版本元数据不同，不重复编号。F35三轮稳定复现，未修。

后续修正宜抽取**不依赖最终result.json**的检查点/来源/rank验证器，在最终completed回执前使用；不能直接把现有inspect插入控制器造成“inspect先要求completed结果、结果又等inspect”的先决条件环。应区分processes_exited_ok、checkpoint_validated、optimizer_execution_recorded和quality_verified；结构自洽仍非真实硬件/优化器独立证明。

## 4. 三轮执行与独立完整性核验

| 项目 | 第1轮 | 第2轮 | 第3轮 |
|---|---:|---:|---:|
| 累计CPU/ASGI/文件/进程合同，旧390＋新12 | 402 PASS | 402 PASS | 402 PASS |
| 新保护／未修观察 | 11／1 | 11／1 | 11／1 |
| 失败／错误／跳过 | 0／0／0 | 0／0／0 | 0／0／0 |

共1206通过；新保护33次、F35见证3次。三轮测试ID/观察一致，旧390逐项继承；原控制器CPU子进程正常回收，后台进程exit0。旧F16后代与F32认证FIFO等见证随CPU集合重跑，仍未修。

本批新增独立trained_voice CLI拒绝合同；原CPU合集已有encode CLI/parent-death/真实信号等也执行。**未重跑额外四项专项CLI矩阵、Go/F31/独立F02、浏览器/Player/latency VM、独立ASGI2.3、NumPy分块/trimmer单独矩阵**，不挪用旧成绩。标准Node30/JS/38份Python AST（33产品库存＋新测试＋4审计脚本）/repack通过。

825份历史文件SHA逐项保持，53源资产/94冻结哈希/正式HEAD15文件不变；原300与Q25–27每题50行动保持。pip freeze与上批相同，无安装新依赖。Go存在但本批未跑其套件；无Rust/Torch/Qwen/CUDA/真实双T4/物理音频。NumPy/safetensors/合成WAV为格式/文件证据，不是预训练模型/训练或声学质量证据。

独立封存首次准备也有审计脚本错误：交接生成器的f-string标题中新增空manifest字面量`{}`未转义，AST/manifest准备未完成，首次verifier报缺manifest。已仅将生成器字面量转义为`{{}}`，保留首错与correction说明，重新生成交接/AST/manifest后再校验；原始三轮收据与产品/测试/runner未改、未重跑回归。

## 5. 原建议部分证据与实施前待办

本批链接原7条：R1-020、R2-093、R3-071/072/075/076/080；含本轮真实重跑的旧信号合同。与之前去重22个原ID有暂定证据，**不是22条已完成**。原建议文本和初始处置不改；specific_row_test_signoff/final_disposition_signed_off/product_fix_implemented均false。

1. 训练输入格式完整、声明与内容语义审阅分列，不将declaration当版权/身份自动验证。
2. 长录音接收、样本分段、全部选择覆盖、实际训练迭代和参考prompt使用继续区分；现有每文件240秒/总900秒门禁不等于真实长数据已训练。
3. 保持sealed-source-v1及内容hash，训练前/提交前核验Base、tokenizer与codes来源版本。
4. 保留fixture/legacy拒绝训练和发布；不得为模型测试便利加生产绕过开关。
5. 统一实际provider distribution元数据；F01仍未修，finish-only保护不能掩盖constructor版本入口。
6. 明确final-cancel相对原子rename的线性化点；提交后取消回执必须指引list/verify，不误称从未提交。
7. 取消/失败只清理自有本次pending，保留旧成功版本；继续解决F16已退出leader的额外后代，不根据历史PID乱杀。
8. 校验每rank逐epoch覆盖、padding、步数/溢出与实际代码报告一致；union覆盖不足以穷尽所有矛盾报告。
9. 在真实Torch环境验证DDP forward、变长序列、累积尾组/共同溢出、FP16/FP32 adapter与两rank digest，不靠AST/tiny替代目标模型。
10. 区分受控CPU lease互斥和真实在线推理/离线双GPU资源隔离；不得为测试盲停驻留模型。
11. 发布前重核tensor/hash/固定参考；成功发布仍只是显式未验候选，保持trained无Base/Mock回退。
12. 将控制器进程退出、检查点完整性、优化记录、reload、音质与加速分别出证；F35先修回执合同，不能新增一项true就声称真实训练已验证。

## 6. 当前检查点与下一步

当前证据：`g0-pass3-training-coverage.json`、`g0-pass3-training-findings.json`、三轮原始log/receipt、manifest、`verify_pass3_training.py`和`progress-pass3-training.json`。完整交接83份，顶层PLAN/IMPLEMENTATION已同步。

下一批继续第三遍adapter/推理入口、provider兼容及训练/推理绑定，复核加载失败、取消、缓存版本与原样生成输出；继续剩33份/8303行及300最终处置。无产品修改、不发18包、不跳S1/Q28、不要求Continue。

长录音真实训练、全部参考贡献追踪、<10秒相似度、首可用DeepSeek prefix立即生成、更响受保护输出、更低建档延迟、自然连续朗读/去沙沙/无接缝、generated-only PCM、双GPU等效参数与真实RTF≤0.3等均未豁免，均不由本批替身签收。
