# G0 全源第三遍第5批：启动、监督、preflight、资源测量与 DSP 接口

日期：2026-10-23；活动分支 `arena/1160bd87-kagglee`。

**第三遍累计38/53份、8920行，剩15份4748行；前两遍各53/53份、13668行保持。产品冻结未改，G0及整体仍PARTIAL/BLOCKED。** 本批是阅读与故障边界核验，不是完整功能、真实训练、声学或提速签收。

## 1. 全文重新阅读11份2253行

| 文件（相对 kaggle/source/） | 行数 | 审查重点 |
|---|---:|---|
| py/bootstrap.py | 451 | 自有进程组、超时/后代管道、冻结依赖、preflight/nonce、旧标记不盲杀、启动回收 |
| py/supervisor.py | 219 | 秘密环境最小化、子进程组与OFD、重试/STOP、fatal回执、退出释放与信号恢复 |
| py/audio_rt.py | 222 | ctypes ABI/符号、加载降级、NumPy状态/有限值、淡入/flush/限幅 |
| rust/audio_rt/Cargo.toml | 17 | cdylib、构建与依赖、接口版本 |
| rust/audio_rt/src/lib.rs | 433 | ABI3及全部导出、指针/长度、DC/RMS/平滑/呼吸/flush；仅源码，未运行Rust |
| tools/backend_probe.py | 200 | 静态/运行时区分、callshape非语义、子进程限时与回执、退出码与成功状态 |
| tools/e2e_check.py | 180 | health/生成/终端统计的成功定义、原F13及错误流边界 |
| tools/resource_control.py | 41 | 合作OFD状态/等待/占用，不将CPU状态冒充GPU运行 |
| tools/selftest.py | 177 | 原F15、fixture/真实服务与自检失败含义，不提升为全功能验收 |
| tools/voice_benchmark.py | 168 | 明确--run、双卡health/实际stats绑定、terminal/计数/RTF、私有O_EXCL产物 |
| tools/watermark_check.py | 145 | 原F14、PCM/统计及真实听感界限 |
| **合计** | **2253** | **11份全文，无产品源输出截断** |

bootstrap连续1–225/226–451，Rust lib连续1–215/216–433，其他全文。辅助旧测试组合输出曾截断，不计辅助测试完整阅读。6667+2253=8920，13668−8920=4748。余15份是LICENSE 201、MEMO 220、Go gateway10份2110行、web3份2217行；调用/继承测试不自动给予这些文件第三遍信用，LICENSE阅读也不等于法律签收。

## 2. 新合同12项：10保护＋2未修观察

测试：`kaggle/tests/test_pass3_startup_boundaries.py`。执行原启动/监督/探针/benchmark/DSP Python代码，真实自有CPU进程、线程、文件和OFD；C ABI 测试库仅用于符号故障注入，不重写DSP，不是Rust实测或多语言性能成果。

| 新保护 | 证据与明确边界 |
|---|---|
| bootstrap活跃直属子进程超时 | 原sh以真实Timer终止自有会话组，直属child为SIGKILL退出且stdout关闭；不修F21“leader已退出、后代仍持管道”路径 |
| bootstrap资源忙/旧PID标记 | 真OFD忙409；释放后旧marker仍409且不更改，去掉本测试marker后才允许通过，killpg未调用 |
| supervisor已退出leader的后代 | 自有leader先exit0，后代忽略TERM并继承真fleet FD；原Proc.kill仍发送组KILL，pidfd确认后代退出、OFD busy恢复false；不是CUDA测量，不修训练F16 |
| supervisor停止优先于重启 | 真线程/Event在重试流程发STOP，原restart退出且start不调用；kill/start为控制替身，不作为重启时延性能测量 |
| supervisor认证准入失败 | 真OFD先取得，认证替身抛UploadRejected；原main返回2，未build子服务，清本次PID、还OFD并恢复SIGTERM/INT处理器；未完整启动服务 |
| preflight超时 | 原isolated_runtime控制器终止/回收真实自有睡眠CPU child，返回blocked与runtime_timeout，模型/推理/训练/性能标志均false |
| callshape不执行模型 | classmethod、实例方法只inspect不调用；额外必填参数阻塞；即便callshape接受也保留behavior untested，非实际provider语义签收 |
| benchmark流及分母 | 分裂header/payload可重组；拒绝终端后数据、重复stats、残帧、超16MiB声明、缺stats、bool/错误sample数、错误pin/engine、cancel/failed/anomaly、NaN/不一致RTF；HTTP、PCM、stats、clock均fixtures，.1/.2不是实测性能 |
| benchmark不覆盖历史报告 | 不带--run时不联网；既存0600报告导致FileExistsError且字节/权限不变，无ledger/WAV创建；只证明拒绝覆盖，不签收友好CLI错误呈现 |
| NumPy有限值边界 | 非连续float64/NaN/±Inf/±1e6输入，经原Leveler得到同长度有界int16，空输入零长、flush192/末端0及再次flush0、close幂等；不声明分块不变/DC状态复位/真实听感 |

### 首错记录（不隐藏）

首次新预检12项中11通过、1 error：测试误访问不存在的`UploadRejected.status`，实际字段为`code`；产品已按预期拒绝。仅改两处测试断言字段，保留`pass3-startup-precheck-first.txt`与`pass3-startup-precheck-correction.json`，修正后12项通过。没有以产品改动消除该测试错误。

## 3. F37：子进程非零退出，但原父控制器仍接受成功回执（未修）

原`backend_probe.isolated_runtime`先wait，随后只按报告文件大小与部分JSON形状接受回执，没有先检查returncode。测试替换的**报告生产者**是自有真实CPU child：写相同schema1/status=surface_preflight_passed/checks=[]、全部模型验证标志false的合成报告，然后分别exit0与exit23。原父控制器均原样返回该报告，真实child均已回收。

三轮新CPU见证一致。确认的是**非零child退出状态没有参与回执准入**；不是实际GPU preflight误通过，不是Torch/provider实际先成功后崩溃的证明。报告生产者明确替身，不能据此宣称有真实GPU/模型。未来修复还需组合returncode、必要checks/报告完整性和状态，不能只看宽松JSON。

## 4. F38：缺必需符号的ABI3库令ctypes导入中止，而非回退（未修）

使用已有`/usr/bin/cc`在自有临时目录真实编译极小C共享库，仅导出`unsigned int rt_version(void)`，以编译宏分别返回2/3；在独立真实Python child中导入原`audio_rt`，实际ctypes加载该库：

1. ABI2：版本太旧，原加载器跳过，结果NumPy；
2. ABI3：访问首个必需符号`rt_leveler_new`时抛`AttributeError`，原except只捕获`OSError`，import以非零码中止；
3. 同ABI3但`QTTS_NO_RUST=1`：显式绕过native加载，结果NumPy。

三轮均一致，回执保存C源码SHA及实际编译器版本。库/源/child临时文件不入Git。**这是实际C ABI 故障注入＋ctypes执行，不是Rust编译或Rust DSP执行；没有证明正式Rust库损坏，也没有声学、跨后端等价或性能结论。** 加载策略应先明确“明确失败关闭”还是“可观察、明确标注的NumPy回退”，不能掩盖native缺失；本阶段没有修改产品实现。

## 5. 三轮重新运行的结果与未执行项

| 实际执行 | 第1轮 | 第2轮 | 第3轮 |
|---|---:|---:|---:|
| CPU继承集合＋新合同 | 426 PASS | 426 PASS | 426 PASS |
| failure/error/skip | 0/0/0 | 0/0/0 | 0/0/0 |
| 独立NumPy分块探针 | 12 case | 12 case | 12 case |
| 独立trimmer探针 | 8 case | 8 case | 8 case |
| 实际CLI期望合同 | 4 | 4 | 4 |

CPU **426×3＝1278 PASS**，每轮完整保留前批414项并新增12项；新增保护30次、观察见证6次。比较逐项测试ID与结果，不以总数替代继承核验。原F01–36/D01保留，观察通过不是bug修复。独立分块探针仍观察到48样本切块差1424 int16等已知分块依赖，实验完成不是算法通过容差/去沙沙成功；裁剪探针也是合成信号，不是真实逐字听感签收。

每轮真实CLI：backend静态、backend --runtime、benchmark默认均期望exit2/blocked，resource status期望exit0但gpu_verified=false；合计12次CLI，其中9次预期阻塞。benchmark未加--run、无模型加载或WAV生成。不能把“预期阻塞符合合同”写成GPU/性能成功。CPU集合本来包含的本地HTTP/ASGI/CLI/租约/信号等继续实际重跑，但模型/health/decoder/ASR等明确替身的部分不会升级证据。

另单次新执行Node30、JS语法（工作台及产品web）、Python AST38、repack --check；没有本批Go/race/vet、真实浏览器/VM、独立ASGI2.3 companion。旧历史成绩不挪作本批成绩。沿用现有.venv，无新Python或系统依赖安装；freeze与前批相同（NumPy2.2.6，不冒称requirements2.4.6）。无Torch/Qwen/CUDA/rustc/cargo。C测试库由已有系统cc编译；**Rust未编译、未执行**。

## 6. 完整性、原300建议与交接

- 887份历史文件SHA在本批前保存，历史收据/测试/报告不得改写；53源、94冻结、15正式工作台文件及原17包保持。
- `advance_pass3_startup.py`逐文件核对SHA/行数，新增11/2253；coverage第一/二遍保持，第三遍38/53，未把剩15份涂绿。
- 本批7条原建议仅部分证据链接：R1-075/079/080、R3-019/020/076/079；与前批去重累计33个ID，原300逐字与Q25–27各50项保持。没有新增重大方案选择题，没有跳Q28；所有最终处置/逐条签收仍false。
- 独立`verify_pass3_startup.py`复核历史SHA、冻结、逐项CPU继承、F37/38、探针/CLI原始日志及SHA、manifest、建议映射、环境与完整交接。
- 完整交接85份备忘录逐份嵌入匹配；本报告、PLAN/IMPLEMENTATION及交接优先状态同步。manifest不自哈希，也不嵌入可变交接/进度，避免循环；这些由独立核验器另验。

主要收据：`docs/validation/step18/pass3-startup-cpu-round1..3.json`、`pass3-startup-companions-round1..3.json`、`g0-pass3-startup-{coverage,findings}.json`、`pass3-startup-recommendation-links.json`、`pass3-startup-run-manifest.json`、`progress-pass3-startup.json`；终态以独立核验成功日志为准。

## 7. 后续精确动作（待实施，不冒充修复）

1. 下一批完整复读Go gateway10份2110行；保存历史SHA，新增严格输入/取消/终端协议与私密错误边界合同。
2. 另批完整复读web3份2217行，实浏览器重验录音/复制/排空/取消，不能用Node代替浏览器。
3. 阅读剩LICENSE/MEMO 421行并分开记录技术与法律边界；完成53资产第三遍后仍不自动签收300处置。
4. 对F37规划child exit0必要条件，再验证合法形状但缺checks/错误mode/自相矛盾flags的拒绝政策。
5. 对F38规划明确native加载诊断，测试缺rt_version/各必需符号/损坏ELF/错误ABI；不能静默称Rust已启动。
6. 保留C库仅为符号故障fixture；真正Rust编译、ABI导出、数值与生命周期检查必须在具备Rust环境独立执行。
7. 继续修前完成F21/F22/F16退出与fatal回执设计，不因本批监督器保护成功覆盖另一路缺陷。
8. benchmark将health GPU和每次stats GPU/engine/binding关联校验，F28仍未修；fixture RTF不得签收0.3目标。
9. 对F13–15分别闭合终端统计/错误JSON/早EOF/奇数PCM等失败语义，不把工具自检绿标当全功能证明。
10. NumPy/Rust先统一状态/分块/flush语义再测容差，保留generated-only，禁止拼参考PCM提相似。
11. 后续按G0→S1顺序实施，不碰冻结17与正式工作台，不提前生成18发布包。
12. 真模型、双T4、长录音/真实训练、真实参考与生成WAV、声学/自然连贯/相似度/首声与RTF缺口继续列BLOCKED，具备条件后再真实三轮验收。

**结论：阅读与故障边界证据推进，F37/F38正式登记但未修。不是全功能通过、不是真实声音改善；G0与整体仍PARTIAL/BLOCKED。直接继续下一批，无需用户点击Continue。**
