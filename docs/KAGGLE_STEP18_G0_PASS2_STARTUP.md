# 第十八阶段 G0：全源第二遍第5批——启动、监督与 backend preflight

日期：2026-10-23；活动分支：`arena/1160bd87-kagglee`。

**本批限定审计完成，产品代码仍冻结，新增两项缺陷确认未修；G0仍为PARTIAL/BLOCKED。** 三轮专项通过不是全功能、真实模型/训练、双GPU、声学或性能签收，无18发布包。

## 1. 全文阅读和真实进度

| 文件（`kaggle/source/`） | 行数 | 第二遍语义重点 |
|---|---:|---|
| `py/bootstrap.py` | 451 | 所有权准入、版本安装、runtime probe先后顺序、命令超时/后代、下载与编译、监督启动与失败取消、访问控制/隧道 |
| `py/supervisor.py` | 219 | GPU lease/FD、进程组、日志句柄、重试预算、健康/致命回执、停机、快照与标记所有权 |
| `tools/backend_probe.py` | 200 | 静态与runtime surface区分、CUDA/API检查、隔离子进程/超时、报告预算/结构、原子写入与退出码 |
| **合计** | **870** | **新增3份完整第二遍语义阅读** |

bootstrap按1–155/156–310/311–451，supervisor按1–115/116–219，probe按1–105/106–200输出并全文复读，所有这些源文件输出无截断。之后相关函数、旧测试与provider控制流的局部核对不另增全文信用。

- 第一遍保持：53/53内嵌资产、13668行；并非整个Git仓库全部文件。
- 第二遍：23/5133 + 3/870 = **26/53、6003行，剩27份**。
- 第三遍：**0/53**，不能把测试执行或局部复查计作第三遍。
- 当前台账：`docs/validation/step18/g0-pass2-startup-coverage.json`；前四批台账/日志保持历史原样。

## 2. 版本准入裁决：已验证的控制流与仍未签收的范围

标准 `QTTS_TTS_ENGINE=faster` 启动链：

1. 所有权检查在依赖安装与GPU启动前进行；默认必须看见两张GPU，显式单卡测试不等于双卡验收。
2. 拒绝旧 `qwen-tts` 与HF同命名空间冲突。
3. 对 `PINS` **每一项**检查metadata：Faster `0.5.4`、HF `0.1.1.post1`、Transformers `5.20.2`。已有任一漂移时调用精确pin安装，不是只检查模块能否import。
4. `install_reviewed_faster` 要求平台Torch已存在，以临时constraints约束Torch及已存在的torchaudio/torchvision；传给pip时文件权限0600，退出后删除；安装后Torch版本改变会抛错。
5. 运行隔离runtime preflight之后才进入后台模型下载、Go/Rust构建和监督启动。preflight失败不能当模型已加载。

新增测试对“全部匹配”与“逐一漂移”分别运行原main至probe哨兵：应否调用精确安装均符合预期；下载未启动。安装测试实际创建/读取/清理constraints，核对精确命令与Torch改变后的拒绝。

**限制：** metadata、pip、GPU数量、import和probe调用为明确fixtures；没有执行真实pip resolver、下载或GPU启动。因此只能确认上述控制流，不能说真实部署的所有版本已准入成功。通用/可选依赖安装后的resolver漂移、安装结果的完整再核对、独立入口和native-adapter路径仍待查。`qwen_compat`未单独拒绝Faster漂移，不能脱离标准bootstrap已有全pin预查直接定为标准启动缺陷；反过来也不能把预查测试当所有入口的终态版本证明。

独立probe的成功仅为 `surface_preflight_passed`：metadata/API/CUDA形状检查，不是模型权重、prompt/codec、声学、RTF或双卡等效证明。没有因表面检查通过改变任何冻结版本。

## 3. F21：leader退出而后代持有stdout时，命令超时失效

源：`py/bootstrap.py:62–96`。**实际CPU进程/管道/计时器复现，确认未修。**

`sh`逐行读取合并stdout，在读流结束后才wait；timer回调仅在直接子进程 `poll() is None` 时设置超时并killpg。leader已退出却有同组后代持有stdout时，回调跳过整组清理，读循环不能收到EOF，也不能抵达后面的超时判断。

确定性实验，而非启动耗时或正常部署证明：

1. 私有临时目录中的真实CPU leader启动一个睡眠后代，后代写出自己的pid/pgid并继承stdout。
2. 自有wrapper用原Popen启动leader，并在返回原sh前等待leader退出；这是明确的Popen观察/调度包装，确保timer装好时leader已经退出，**不是完全未包装的自然竞态压力实验**。
3. wrapper验证后代pgid属于该leader，并持有其pidfd；原sh使用0.1秒期限。
4. 外部0.35秒等待仍超时，wrapper还在原sh读流中，后代pidfd尚未退出。证明该交错下请求的期限没有终止命令。
5. 只通过自有后代pidfd发送KILL；退出可读断言通过，管道EOF后原sh返回0，未报告超时。
6. finally定向终止/回收自有wrapper，后代pidfd退出验证并关闭。无按进程名/任意旧PID杀进程。

这是独立于训练 `stop_ranks` 的F16调用点与行为：本项针对bootstrap命令的超时和管道EOF；没有声称正常run_rank、真实安装/模型下载已发生该问题，更不是显存泄漏证据。后续修复需要把进程组生命周期与leader退出状态解耦，并定义超时/取消/读流的有界清理；本批未实施。

## 4. F22：致命回执写失败会跳过停机，失败计数每轮又清零

源：`py/supervisor.py:147–170`。**原watch控制流复现，确认未修。**

每次HTTP读取成功先把fail_count清零；worker报告fatal_error时，代码先写 `startup-failure.json`，再kill并设gave_up。如果写入抛OSError，直接进入通用except，未执行kill/gave_up，fail_count变为1；下次HTTP成功又归零。同样的致命错误与回执写失败持续存在，也达不到8次健康失败的重启门槛。

测试执行原watch，使用真实STOP事件、8轮受控无睡眠wait；HTTP fatal健康、进程句柄和回执OSError均为fixtures，不制造真实磁盘故障，也不启动工作进程/GPU。started_at置于宽限期之外以排除宽限期影响。结果：

- 8次回执写入尝试/异常；8轮循环。
- kill=0、restart=0、gave_up=False、最终fail_count=1。
- 没有成功落盘的startup-failure.json。

本项不是“GPU实际无法停止”或磁盘故障概率证明，而是**持久化错误能阻断安全停机、并被错误计数策略掩盖**的原控制流证据。后续需比较独立停机与尽力写回执、不同错误计数归属等方案；尚未修改产品。

## 5. 新增12项：10保护 + 2未修观察

测试：`kaggle/tests/test_pass2_startup_boundaries.py`。预检12/12通过，未发生测试失败；日志 `pass2-startup-preflight.log`。

| # | 合同 | 执行范围/限制 |
|---:|---|---|
| 1 | 每项冻结pin漂移触发精确安装；runtime probe先于模型下载 | 原main至哨兵；metadata/安装/设备/导入替身 |
| 2 | 精确pip参数、平台Torch/audio/vision constraints、0600与清理 | 真实临时文件，pip替身 |
| 3 | 安装后Torch改变拒绝，constraints仍清理 | metadata/pip替身；无真实Torch |
| 4 | probe原子替换失败保留原报告并移除临时文件 | 原write_report，真实文件；replace OSError替身 |
| 5 | 子报告超256KiB、坏JSON、checks坏形状均阻塞 | 原isolated_runtime、真实临时报告；子进程替身 |
| 6 | 旧startup nonce失败记录不遮蔽当前活监督与健康回执 | 真实旧JSON；process/HTTP替身 |
| 7 | 已关闭GPU lease不能启动模型角色 | 真实lease/锁；Popen未调用 |
| 8 | Popen OSError关闭日志且不擅自释放监督拥有的lease | 原Proc.start、真实文件/锁；spawn异常替身 |
| 9 | 丢弃过期重试，第7次近期重试give up、不再start | 原restart；kill/start替身 |
| 10 | 流式90秒与句缓冲180秒严格越界才按停滞重启 | 原watch；health/restart与单轮wait替身，非真实等待 |
| 11 | leader退出、后代持stdout导致超时失效 | **F21观察通过=缺陷存在**；真实CPU/pipe/pidfd，确定性交错 |
| 12 | fatal回执I/O失败跳过kill且计数停留1 | **F22观察通过=缺陷存在**；原watch与明确fixtures |

既有13项probe与监督/所有权保护继续纳入累计回归，不把已有正常killpg、旧标记或停止不重启用例重复报为新发现。F01–F20和原专题问题均保留。

## 6. 三独立轮累计专项回归

runner：`docs/validation/step18/run_pass2_startup.py --round N`；每轮独立Python进程/临时状态。上批348 + 新12 = **360项/轮**，逐ID不重复，原348顺序保持。

| 轮次 | tests | failures | errors | skipped | 结果 |
|---|---:|---:|---:|---:|---|
| 1 | 360 | 0 | 0 | 0 | PASS |
| 2 | 360 | 0 | 0 | 0 | PASS |
| 3 | 360 | 0 | 0 | 0 | PASS |
| **合计** | **1080** | **0** | **0** | **0** | **限定专项，不是全功能验收** |

逐轮JSON/regression/console日志保留测试ID、源/测试/runner/support哈希、依赖、F16–F22观察及真实性字段。F21自有进程/pidfd、旧F16后代/锁、F18线程、F19临时资源/槽位均执行清理断言。日志中预期fatal/spawn等ERROR为故障注入，不能单凭日志级别当作测试失败。

继承真实CPU进程/锁、本地HTTP、ASGI、NumPy/safetensors、WAV/文件/归档合同；没有执行完整bootstrap安装/下载/编译/启动、真实Torch算子/optimizer/Gloo/NCCL、真实Qwen/Faster/Whisper/ECAPA/codec、训练或双T4。本批未重跑独立ASGI2.3 companion、旧CLI四矩阵、全Go/race/协议、Chromium全量、旧14分析AST/12DSP或缺cache的provider六案例，不重签历史成绩。

## 7. 封存、工具与交接

- 沿用现存venv，无新依赖安装；environment与完整pip freeze已保存，freeze与第4批相同，不称所有二进制/运行环境绝对一致。NumPy2.2.6仍不同于生产requirements2.4.6；无Torch/Qwen/rustc/cargo/go。
- Node30、JS检查、33份产品Python加本批测试及4个审计脚本共38份AST、repack检查通过，各有独立日志；最终diff检查不替代运行验证。
- 497份历史文件逐SHA保留；53资产/94冻结哈希/15正式文件、原300建议初审、Q25–27各50项保持。未改原包、工作台、浏览器复制实现、安全/录音/取消或私有数据合同。
- 封存验证器首次把两条新观察的追加顺序误认作编号顺序；unittest按测试名称执行，实际为F22再F21。仅修验证器按唯一ID核对，未改测试或产品、未重写三轮收据，原断言失败日志保存在 `pass2-startup-progress-verification-initial-failed.txt`；重验通过。
- 当前验证器 `verify_pass2_startup.py`；当前覆盖/发现为 `g0-pass2-startup-{coverage,findings}.json`；`progress-pass2-startup.json`经验证后同步 `progress-checks.json`。本批run manifest绑定测试、审计脚本、日志、报告、PLAN/IMPLEMENTATION/交接等文件，不循环哈希进度输出。
- `KAGGLE_STEP18_HANDOFF_PROMPT.md`更新为**76份完整备忘录**；具体字节数/SHA由 `handoff-progress.json`与当前progress收据校验，不把旧75份摘要冒充当前原文。

## 8. 下一步和未签收需求

继续第二遍剩27份，优先网关调度/流协议/取消/超时与前端完成排空跨语言交叉核对；随后补全全53份第三遍和300建议最终处置/失败映射。发现仍按原行为反证，不为凑数量另开问题28，不跳过G0实施S1–S8或发布18包，不要求点击Continue。

相似度、无沙沙、自然连续、双卡同条件声学、真实首声/RTF≤0.3、更响且受保护输出、首个可用DeepSeek prefix立即生成、长录音真实训练/提速、全部候选贡献与generated-only PCM等要求均未撤销、未签收。没有用户WAV/真实模型/双T4/物理声卡实验，不能从截图归因或宣称已解决。
