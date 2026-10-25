# 第十八阶段 G0：全源第二遍第1批——训练执行与资源所有权

## 1. 进度与结论

2026-10-23，活动分支 `arena/1160bd87-kagglee`。承接第一遍53/53、13668行检查点，本批**重新逐行读完8份、1056行**并交叉复核调用/失败/租约链，正式第二遍为 **8/53、1056行，剩45份**；第三遍0。不是重复跑测试就给第二遍阅读计分，也不是全源第二遍已经完成。

- **219项×3轮=657通过**，各轮失败/错误/跳过0。旧197 + 另选现有artifact10 + 新12；新12为11保护、1个 `OBSERVED_NOT_FIXED` 见证。
- 新确认 F16：原 `stop_ranks` 对忽略SIGTERM的额外后代存在清理缺口。实际CPU子进程、pidfd、继承OFD及flock执行；未修复。测试最后定向清理所有fixture后代并验证锁释放。
- 正常生产 `run_rank` 没有DataLoader子进程，本次额外后代明确构造；**未证明正常Qwen训练发生了这条故障**，未运行真正训练rank。
- 没有Torch，不执行任何张量/optimizer/Gloo/NCCL测试。AST只抽出纯Python采样、赋值提交回滚及dataset构造/len，不模拟Torch算子，不将其称为训练成功。
- 53源/94冻结hash/15正式文件不变；开始时382个历史文档/脚本/收据hash封存。旧300建议初审和问题25–27各50条保留。
- 无产品改动、无18包、无完整模型/GPU/Rust/物理声卡/真实训练/用户录音/提速或声学验收。G0仍 **PARTIAL/BLOCKED**。

## 2. 本次重新完整阅读与不计分的局部阅读

| 文件 | 第二遍重新阅读区间 | 复核重点 |
|---|---:|---|
| `py/training_job.py` | 1–227 | 内容pin、预算、两类租约、准入、子进程环境、信号屏蔽/启动登记、停止/结果、原子checkpoint |
| `py/gpu_ownership.py` | 1–151 | 固定namespace、inode/OFD/nonce/模式、继承/duplicate关闭、诊断非权威、最后引用释放 |
| `py/resource_limits.py` | 1–172 | multipart预预算/重放、构建记录与准入所有权、HTTP取消与执行器提交失败门闩 |
| `py/tts_training.py` | 1–200 | JointLoss/DDP.forward、codec/text位置、采样/累积、全rank finite、更新/digest/保存与退出 |
| `py/tts_dataset.py` | 1–125 | 文本格式/裁尾假设、16组codes、序列拒绝非截断、cache复制、mask/label/index与单batch布局 |
| `py/lora_adapter.py` | 1–91 | q/v目标、Base冻结、FP32 A/B存储、严格restore、prepare-before-commit、BaseException回滚 |
| `tools/train_tts.py` | 1–49 | public参数、内部受控rank路径、结构化退出、私有rank日志与公开错误 |
| `tools/resource_control.py` | 1–41 | status/预约预算、GPU工作标记false、取消/拒绝/信号还原 |

共8份1056行。第二遍计分证据为当前报告与 `g0-pass2-training-coverage.json`，各份第一遍信息原样保留。

另交叉查看 `training_codes.py` 的lease_with_fd/adopt_lease、`encode_training.py` 的arm_parent_death、`supervisor.py` 的Proc生命周期，以及现有控制器/所有权/产物测试。这些是**局部调用点/测试阅读**，不把对应依赖文件记成全文第二遍。

## 3. 跨文件语义复核记录

### 3.1 CLI→controller→rank→训练核心

1. public `train` 参数由argparse设类型；实验确认/数据审阅与schema2真实编码准入不可由fixture bypass进入正式CLI。既有Admission8项中实际CLI拒绝fixture的合同本轮继续执行。
2. controller先持码读取OFD核验固定manifest，核验Base及speech tokenizer内容pin，再查训练依赖，最后获取offline-reservation。拒绝时不自动停推理、不下载模型、不替换默认引擎。
3. GPU整组租约与码读取租约通过pass_fds分别传给两个受控rank；信号在Popen到登记process之间屏蔽，避免取消丢PID。父进程保存自己的引用，rank接管duplicates后关闭原继承FD，不使用LOCK_UN释放共享OFD。
4. rank在Torch/CUDA导入前设置Linux PDEATHSIG并重核ppid；随后解除继承信号屏蔽、检查rank和请求，再接管offline及码租约。码接管再次验证目录/内容/manifest，并不绕过正式训练admit。
5. 已有六项ControllerLifetime测试在CPU替身下运行真实Popen/lease/PDEATHSIG，覆盖无checkpoint的双exit0不能成功、timeout、单rank失败、第二次spawn失败、offline显式接管、控制器SIGTERM/SIGKILL。其内部注入admit/dependency/模型fingerprint，不是真实模型rank或优化器。
6. controller完成后在父租约仍持有时再verify码、Base及checkpoint manifest存在。这里只是父端完成检查；完整产物语义还依赖受控rank写出合同及后续TrainedArtifacts验证，不把manifest存在当作独立优化器或质量证明。父端语义复核加固仍是待测/待设计项，本轮未用恶意假rank伪造“真实训练成功”证据。

### 3.2 OFD与资源准入

- fresh打开同一inode不等于持有同一个open file description；新保护用实际fresh FD验证adopt拒绝，原holder保持busy。
- inference_guard默认只接管inference；offline FD不能作为启动推理的默认许可。新测试失败后原holder仍持有，最后close后释放。
- child_environment只清理列出的凭据键/旧lease/PYTHONPATH，设置离线与线程限制，保留CUDA可见性；它不是任意名称凭据的全面沙箱。新保护用固定fixture值验证枚举清理和真实私有lease导出，不在证据中保存token/nonce值。
- BodyBudgetMiddleware先spool再解析，含unknown-length独立实际字节限制，重放完才透传receive。HeavyAdmission在HTTP取消后仍等执行真正结束才释放；run_in_executor提交可能先排队后启动失败，submitted门闩阻止拒绝任务迟执行。相关既有安全/库API测试均包含在组合中；不是OS内存/CPU隔离或全部ASGI事件矩阵证明。
- BuildAdmission.start的slot预先获取由调用方负责，start不再次acquire，线程启动失败由调用方释放；不把单个文件的finally读成整个链已完整。原调用点部分查阅不能算analyst/library_api全文第二遍。

### 3.3 dataset / JointLoss / LoRA（源码结论，张量运行仍阻塞）

- dataset深复制rows，缓存tokens/codes并在命中返回clone；reference_mel仍共享，不将cache当作训练/新增参考融合。新AST构造测试只验证深复制/预算/计数，不运行tokenizer或collate。
- 文本token布局包含固定格式与末5 token裁尾假设；codes要求非空16列、0..2047；tokens+codes+8超预算拒绝而非截断。mask、speaker固定位置6、BOS/EOS和label移位重新按源码推导；仍须实际固定Qwen tokenizer/张量验证，不能把AST构造当作mask数值一致。
- JointLoss把参数相关路径放在DDP.forward内部，包含text_projection、speaker条件、16-codebook嵌入与subtalker loss。源码布局复核不证明实际provider API/hidden_states结构在完整模型上可用。
- epoch_indices确定性打乱、前缀padding补齐两rank等步数，不drop最后样本。原函数AST执行检查world2/3/4、count从world到32：全覆盖、等长、padding次数正确；另验证跨epoch变化、同seed复现与too-few拒绝。这是纯Python采样数学，不是DDP执行。
- optimize_epoch按实际尾部group_size缩放、边界才同步/更新，全rank finite失败策略与GradScaler/clip顺序重新审查。没有Torch，**未重新运行反向、混合精度、nonfinite梯度、Gloo/NCCL或参数一致性**。旧CPU证据仍是历史，不据此给本轮数值验收。
- LoRA A/B存储FP32与实际autocast算子执行精度不是同一命题；没有声称所有matmul以FP32计算、T4无溢出或快于原方案。
- prepare先构造/检查全部替换，commit遇BaseException逆序恢复。新AST测试用普通Python对象/setter注入KeyboardInterrupt验证赋值回滚，不伪装nn.Module、CUDA、真实adapter切换或推理声音保持。
- run_rank先逐条检查tokenized长度后建optimizer，内容pin复核、adapter digest跨rank汇聚、全部更新/一致才保存；checkpoint原子发布与产物加载仍需真实Torch/权重。F01旧provider metadata缺口仍未修，是训练链阻塞因素之一，不把依赖缺失单说成只有GPU问题。

## 4. 新确认 F16：停止直接rank不等于清空整个进程组

位置：`training_job.py:108–122`。原helper先SIGTERM进程组，等待直接leader，再仅在 `process.poll() is None` 时对组SIGKILL；leader退出后，额外忽略SIGTERM的后代会被跳过。

实际CPU/OFD见证步骤（三轮相同）：
1. 在独立临时root取得offline-reservation，创建本测试拥有的新session leader。
2. leader显式派生一个忽略SIGTERM的额外CPU后代，传同一租约FD；通过ready握手确保handler已安装，用pidfd观察。
3. 调原 `stop_ranks`：直接leader确已回收，但后代pidfd未退出。
4. 关闭测试父进程租约引用，实际status仍busy，证实后代仍持OFD。
5. **测试finally只向自己创建的group定向SIGKILL**，确认后代退出、close全部引用、status变非busy。没有留下fixture进程/租约，也没有按旧PID/名字杀外部进程。

状态 `confirmed_with_explicit_cpu_descendant_fixture_not_fixed`。新见证PASS代表缺口仍复现，不代表产品已增加组清理。当前run_rank无DataLoader子进程，PDEATHSIG用于受控直接rank；本次额外后代并不是实际Qwen/第三方组件产生。因此这是停止helper在明确额外后代场景下的不足，**不能声称真实训练曾泄漏显存、用户进程被锁住、父死正常路径已失效或构成公开攻击**。

正常单个直接CPU子进程的停止/回收保护也通过。未来修复须与supervisor已考虑leader死亡后组后代的策略交叉核对，不能破坏最后引用才释放、仅停止本次进程、取消/故障时不发布成功等保证；当前G0下不改冻结helper。

## 5. 三轮执行与证据

```bash
.venv/bin/python docs/validation/step18/run_pass2_training.py --round 1
# --round 2 / --round 3 同目标、独立进程
```

| 轮次 | unittest | fail/error/skip | 新保护/原行为见证 |
|---|---:|---:|---:|
| 1 | 219 PASS | 0/0/0 | 11/1 |
| 2 | 219 PASS | 0/0/0 | 11/1 |
| 3 | 219 PASS | 0/0/0 | 11/1 |

另选现有10个artifact边界，真实NumPy/safetensors解析、本地文件、手工rank报告；**手工报告不是实际NCCL/训练**。新12项预检日志保留，不计额外完整轮。组合包含旧诊断误PASS等观察，不能将219通过解释为旧缺陷消失。原先单独CLI四项矩阵、14个分析AST、12个DSP分块及Chromium/Go race全协议没有以独立矩阵重跑，不改写旧收据。

主要文件均在 `docs/validation/step18/`：
- `pass2-training-roundN.json` / `pass2-training-regression-roundN.txt` / `pass2-training-roundN-console.txt`：逐ID、源/测试/runner/support/hash、依赖、F16和执行边界。
- `pass2-training-preflight.txt`：新12项预检。
- `pass2-training-preserved.json`：382既有历史文件hash。
- `g0-pass2-training-coverage.json` / `g0-pass2-training-findings.json`：8份第二遍及F16，局部依赖阅读不冒充全文。
- `pass2-training-toolchecks.json`及Node/JS/Python AST/repack日志、`pass2-training-environment.txt`。
- `verify_pass2_training.py` / `pass2-training-progress-verification.txt` / `progress-pass2-training.json` / `pass2-training-run-manifest.json`：独立一致性检查；`progress-checks.json`更新当前检查点。

所有产品Python源码AST解析是语法检查，不是Torch导入/执行。实际NumPy2.2.6、safetensors0.6.2，无Torch/Qwen/CUDA/rustc/cargo；没有扩大实际环境成绩至需求文件版本。

## 6. 后续顺序

全源第一遍53/53保持；第二遍现8/53，尚45份；第三遍仍0。下一批沿码/输入/产物/恢复链逐份重新全文读，再到分析/worker/网关/前端/工具/说明的跨层失败传播，不以局部grep或新增测试自动填满第二遍。

原300建议最终处置/失败见证映射尚未签收。只有真正关键设计选择才按既定顺序另开题并给≥50行动建议，不预填Q28、不向用户索要Continue。G0未完成前不跳S1/发布；首可用DeepSeek prefix、更响受保护输出、更快真实首声/建档、generated-only PCM、自然连续、短参考相似度、双卡同等参数与声音、真实长数据训练、无沙沙及RTF≤0.3仍全部保留，当前未取得新的声学/性能证据。
