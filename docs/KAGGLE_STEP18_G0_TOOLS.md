# 第十八阶段 G0 第七批：工具、LICENSE 与历史 MEMO

## 1. 结论：53项内嵌资产第一遍完成，G0尚未完成

2026-10-23，活动分支 `arena/1160bd87-kagglee`。本批新增8份全文第一遍、1332行；累计 **53/53、13668行、第一遍剩0项**。这是53项内嵌资产的覆盖口径，不是整个Git仓库全部文件或全源三遍语义审查完成。完整第二遍/第三遍仍 **0/0**，G0与发布验收仍 **PARTIAL/BLOCKED**。

- **197项专项×3轮=591通过**：每轮失败/错误/跳过均0。
- 构成：上批172 + 既有probe 13 + 本批新12。新12为 **9项保护、3项OBSERVED_NOT_FIXED见证**。既有项中也有已知缺陷见证，总通过数不意味着产品无缺陷或已修复。
- 三轮各独立执行4个CLI：backend静态/隔离runtime、benchmark默认无`--run`均返回预期exit2/BLOCKED；resource status返回exit0。**预期阻塞合同通过不等于GPU/模型成功。**
- 新确认工具误报通过 F13–F15，均未修复；另记录MEMO文档漂移 D01，不混成第四个运行缺陷。
- 53源码、94冻结hash、15正式工作台文件保持不变；本批开始封存329份历史文档/脚本/收据hash，旧报告不随最新handoff重签。
- 本批没有产品改动、没有18发布包、没有实际训练/完整模型/GPU/Rust编译/物理声卡/真实DeepSeek/用户WAV或质量/提速验收。

## 2. 全文第一遍范围

所有文件按行分段读完，输出截断处另行补读；只在全文读完后计入台账。

| 文件（相对kaggle/source） | 全文区间 | 重点 |
|---|---:|---|
| `tools/backend_probe.py` | 1–200 | 元数据/精度/API surface、隔离子进程、deadline、进程组终止、报告权限/原子提交、exit语义 |
| `tools/e2e_check.py` | 1–180 | 9字节网关帧、文本/统计/END/ERR、顺序、GPU计数、模拟播放与退出门禁 |
| `tools/resource_control.py` | 1–41 | 只读status、1..3600秒预约、租约、信号恢复、拒绝/取消/失败exit |
| `tools/selftest.py` | 1–177 | 各检查的PASS/SKIP/FAIL、NumPy/Rust标签、worker健康/流、e2e/quality调用、报告写入 |
| `tools/voice_benchmark.py` | 1–168 | 显式运行门禁、双worker健康/pin、严格帧与样本数/RTF、私有WAV/ledger、不覆盖证据 |
| `tools/watermark_check.py` | 1–145 | 消费与telemetry线程、水位/饥饿/排空、帧校验、chatter指标与退出判断 |
| `LICENSE-QWEN-DERIVED.txt` | 1–201 | Apache2授权/专利终止/分发条件/变更与归属通知/NOTICE/商标/免责声明，末尾Alibaba Cloud版权 |
| `MEMO.md` | 1–220 | 当前页头与历史阶段混排、数据/训练/隐私/真实验收边界、与当前17源码策略核对 |

本批覆盖：`docs/validation/step18/g0-tools-coverage.json`；保留此前各批覆盖JSON原样。全源第一遍补齐不能解除第二/第三遍或300建议最终处置/失败映射门禁。

## 3. 模块结论与现成功能保护

### backend_probe

默认只查metadata，不安装/下载模型。runtime在有界子进程内检查CUDA及实际调用形状；surface pass也明确不表示模型加载、推理、训练、性能通过。保留T4 BF16/未经批准FP32阻断、签名bind与额外必需参数检查、导入异常脱敏、子进程deadline、原子0600报告。

既有13项probe测试本轮独立重跑三次，虚拟GPU和兼容smoke仅是显式fixtures。新测试及独立CLI又实际启动隔离runtime子进程：本环境缺Torch/Faster，输出blocked、devices空，model_loaded/inference_verified/training_verified/performance_verified均false，exit2，不冒充CUDA成功。真实超时后的全部后代退出与child退出码/报告一致性仍需更完整故障矩阵；现有timeout测试为受控Popen/killpg fixture，不宣称本批真实杀过挂起模型导入树。

### resource_control

仅本机status/预约，不接任意命令、不强制解锁、不运行GPU任务。状态与诊断记录不是显存空闲证明。新保护验证私有临时namespace下fresh status/非法时长不创建锁文件，竞争拒绝后原holder仍busy、SIGINT/SIGTERM处理器还原。既有32项ownership相关测试还包括真实子进程/OFD/flock/信号及预约生命周期；该历史套件本轮实际重跑，不能将CPU锁实验叫GPU工作。

### voice_benchmark

默认无`--run`直接blocked，既不合成也不把CPU/Mock当双卡证明。新CLI保护实际保存0600报告，并验证第二次相同路径拒绝覆盖；该拒绝目前会产生FileExistsError/非零而非结构化重试收据，未改产品。

`measure`已有比另三个诊断工具更严格的HTTP状态、16MiB帧界限、64MiB PCM预算、终结后禁止数据、残留/失败/取消/未知引擎/pin/anomaly/样本数/RTF一致性检查。新本地HTTP测试保护15个协议/统计拒绝分支及HTTP503拒绝；只通过header声明超大帧，不分配16MiB或64MiB攻击体，未做大包内存压力。

合法fixture为240 speech samples+192 tail，fake worker元数据及全零PCM，仅验证解析/分母排除padding。该fixture中的engine字符串/统计数字不是真实Faster、可听语音或RTF成绩；本批没有调用benchmark的真实`run=True`，也没有生成用于声学验收的WAV。真实双worker身份、dtype/参数同等、私有pin与听感仍须目标设备验证。

### e2e_check / selftest / watermark_check

三者是运维工具，不应继承浏览器或网关的协议保证来替代自身验证。既有空E2E失败保护保留；新测试同时保护显式ERR、HTTP非200失败、SKIP/FAIL/PASS区分、模拟短尾排空与已知欠载。

`e2e_check.simulate_player`在所有到达后可立即排短尾；不代表实际浏览器Player的已知完成短尾问题已修复。watermark消费线程不是浏览器Worklet，也没有实体音频输出；source注释“exactly like browser”不构成等价证据。selftest的 `t_rust`即使NumPy回退也可执行，其名字不能证明Rust已编译；本批不运行完整selftest.main或quality网络链，不访问真实worker/analysis/gateway。

## 4. 新确认且未修复的三个误报通过边界

### S18-G0-TOOLS-F13：E2E硬门禁仍接受无效证据

原 `run`/二进制parser/`main`，真实requests+有限本地HTTP fixture，4种输入各三轮：

| case | 实际行为 |
|---|---|
| stats缺gpu字段 | `{None}`长度为1，默认min-gpus1竟通过；输出展示过滤None后仍看不到设备 |
| END含failed/cancelled=true | 只要求END存在，不拒绝失败字段，RESULT PASS/exit0 |
| PCM payload为3字节 | `ln//2`静默向下取整，RESULT PASS/exit0 |
| 合法流后残留2字节下个header | EOF残留未校验，RESULT PASS/exit0 |

fixture有segment/PCM/stats/END，不是历史空流例。**没有实际Go网关、模型或GPU**。这说明工具的验收可信性不足，不说明真实双卡已失败、公开网关已被利用或正常音频已受损。

### S18-G0-TOOLS-F14：watermark零音频也PASS

原 `main`、player/telemetry线程实际执行，本地HTTP三类：空503、显式网关ERR帧、残缺header。各自均 audio=0、first play=None、starvations=0，最后RESULT PASS/exit0；高水位分支仅提示文本太短，不使结果失败。

没有验证HTTP状态/有效PCM/END/ERR/残留，因此“未播放无欠载”可变成通过。测试捕获并等待工具两个daemon线程退出，避免线程污染后续轮次；这不等于产品已新增finally/join，也不覆盖网络/JSON异常时线程清理。没有证明真实调度水位或chatter性能正常。

### S18-G0-TOOLS-F15：selftest失败/取消Mock流仍报stream通过

原 `stream_once`与装饰后的 `t_stream` 实际调用本地HTTP，送3帧各12000样本以及 `failed:true,cancelled:true,engine:mock` 的stats。原检查仅依据分块数、到达/总时间、audio>1秒、无anomalies字段，返回True且status passed。

时间为显式确定性fixture，端口列表只有一个本地fixture worker，**不是测得首声/吞吐或双GPU结果**。不推断整个selftest.main会退出0，因为其他检查没有在这条见证中一起执行。stream_once的HTTP/终结校验弱项也列后续统一修复合同，不重复计成其他新bug。

三条状态均 `confirmed_with_explicit_local_http_fixtures_not_fixed`。197 PASS中的见证是“仍可复现”而非“已修复”。机器台账 `g0-tools-findings.json`，原300建议处置文件不改写。

## 5. LICENSE与MEMO结论

### 许可证：保留文本，不作法律认证

读完Apache2各条及附录，特别保留分发附许可证、修改文件显著说明、来源归属/版权保留以及**若上游分发含NOTICE则按条件携带**。专利授权/诉讼终止与商标权限不同，AS IS不等于无需遵守条件。文本末尾有2026 Alibaba Cloud版权；这一存在性不证明所有依赖、模型权重、音频和再分发许可已完整核验。

本地source未发现NOTICE文件，不能据此推断上游原发行版必定没有NOTICE或已违规。旧upstream解包cache缺失，未在本批重下载所有依赖或重新认证其许可证。后续发布仍需来源/修改标记/NOTICE与依赖及权重许可清单；用户语音授权另行核对，许可证不自动授予他人声音权。当前不修改冻结许可证，不出具法律合规签收。

### 文档漂移 D01（不是第四个运行缺陷）

`MEMO.md`页头称当前step15，写vector-only、不回退ICL、maxgain12；当前冻结17源码为默认ICL、generated-only codec、默认maxgain6。旧历史段落还混有14/11/10“当前”字样、已过时录音预算/训练入口边界，以及第83行短呼吸不再广播异常的笼统说法（F10已在极短2..5样本复现）。

新旧阶段曾经的推荐不等于最新策略；不能据MEMO重启参考PCM拼接、改回纯向量、认定网页训练已完成或把历史TorchCPU证据当本机现有依赖。bootstrap诊断会摘出旧“当前版本修复”段，原始console也可见历史14文字，应以manifest/最新阶段报告为准。这里只做本地源码对照，不额外执行安装器，也不篡改历史MEMO；未来新发布包应在新版本说明中消歧，保留旧包hash。

## 6. 执行、证据和环境

运行命令：

```bash
.venv/bin/python docs/validation/step18/run_tools_audit.py --round 1
# --round 2、--round 3，独立进程、同一197项目标
```

| 轮次 | unittest | fail/error/skip | 独立CLI | 其中预期BLOCKED |
|---|---:|---:|---:|---:|
| 1 | 197 PASS | 0/0/0 | 4合同符合 | 3 |
| 2 | 197 PASS | 0/0/0 | 4合同符合 | 3 |
| 3 | 197 PASS | 0/0/0 | 4合同符合 | 3 |

新12预检也全部通过，原始日志 `tools-preflight.txt` 保留，不另计第四轮。没有为凑数把unittest中的内部工具SKIP输出计成模型执行；选中的unittest层级skip实际0。没有重跑上批另行14AST/12DSP或历史Chromium/Go race全协议，旧收据继续有效为历史证据，不称本轮全量重跑。

主要证据位于 `docs/validation/step18/`：
- `tools-audit-roundN.json`、`tools-regression-roundN.txt`、`tools-roundN-console.txt`：197逐ID/观察、53源hash、测试/runner/support hash、原日志与依赖。
- `tools-cli-roundN.json`及 `tools-{backend-static,backend-runtime,benchmark-default,resource-status}-roundN.{json,txt}`：实际CLI命令、预期/实际exit与原始报告/log hash；exit2按阻塞保存。
- `tools-preserved.json`：329既有历史文件hash；旧验证器/收据保持检查点版本，不随新handoff改写。
- `g0-tools-coverage.json` / `g0-tools-findings.json`：53项第一遍覆盖、F13–15与D01。
- `tools-toolchecks.json`、对应Node/JS/Python AST/repack日志，`tools-environment.txt`。
- `verify_tools.py` / `tools-progress-verification.txt` / `progress-tools.json` / `tools-run-manifest.json`：独立检查源码/冻结/正式文件、历史、300建议/QA、三轮一致性、逐log/测试hash、handoff原文；`progress-checks.json`更新指向本批。

实际Python3.11、NumPy2.2.6，不冒充requirements NumPy2.4.6。没有Torch/Qwen/CUDA/rustc/cargo；HTTP为有限本地fixtures，音频为零PCM/合成信号，设备/API smoke含显式虚拟对象。没有实际训练数据/声纹外传，无GitHub凭据或访问口令写进报告，所用token仅固定本地fixture字符串。

## 7. 下一步与未解除门禁

第一遍已无剩余项。下一步转入**全源第二遍**，以53资产完整台账逐份做调用链、失败传播、并发/版本提交和度量语义交叉复核；第三遍再独立反证/回归映射。现有专项重复执行不能自动给某文件第二遍完整阅读计分，也不能把3×100专题建议当作这两遍已完成。

保留300建议原ID与初审，后续补到最终处置/失败见证；F01–F15及D01均按真实边界处理，不将15编号直接解释成15个互不重叠根因。只有需要重大设计选择才按顺序开启新题并给≥50行动建议，本批不预填问题28，不向用户索要Continue。

在G0完成前不跳到S1/Q28/18包。真实首可用DeepSeek prefix触发、更低创建延迟、更响受保护输出、generated-only PCM、自然连续朗读、<10秒参考相似度、>10分钟录音与真实长数据训练、双GPU同等参数/声音、无沙沙与真实RTF≤0.3全部仍未豁免；当前只是工程审查第一遍里程碑，非产品/模型/声学发布签收。
