# G0 全源第二遍第8批：Python/Rust DSP 与音频工具

日期：2026-10-23；分支 `arena/1160bd87-kagglee`。**专项三轮完成，G0 仍 PARTIAL/BLOCKED；产品未修改，未发布18包。**

## 1. 全文阅读信用

本批重新完整阅读9份1500行，不将测试执行、局部调用点检查计作全文：

| 文件（均位于 kaggle/source/） | 行数 |
|---|---:|
| py/audio_rt.py | 222 |
| rust/audio_rt/Cargo.toml | 17 |
| rust/audio_rt/src/lib.rs | 433 |
| tools/e2e_check.py | 180 |
| tools/encode_training.py | 128 |
| tools/selftest.py | 177 |
| tools/trained_voice.py | 30 |
| tools/voice_benchmark.py | 168 |
| tools/watermark_check.py | 145 |

第一遍保持53/53、13668行；第二遍由34/53、10506行推进至 **43/53、12006行，剩10份1662行**；完整第三遍仍0。Rust全文分段读完；旧测试组合输出曾截断，仅补读相关范围，不给旧测试全文信用。范围是冻结包内53资产，不是整个 Git 仓库。

## 2. 新增合同：10保护＋2未修观察

`kaggle/tests/test_pass2_dsp_boundaries.py`：

1. 非有限输入等价于零替换、不修改调用方数组。
2. 关闭淡入/动态增益后的单纯 DC 过滤跨调用连续；**不是一般分块不变性声明**。
3. 门限下信号不学习语音包络、不改变增益。
4. 禁用 Rust 时不调用动态库加载。
5. ABI2 跳过、ABI3 ctypes 签名设置；符号与库对象为 fixture，未 dlopen Rust。
6. 原 benchmark/measure 的18次请求同文同 seed/同 pin、warmup 独立、私有 WAV/ledger 保留。
7. 后续请求失败仍保留先前慢行、WAV、ledger，最终报告 BLOCKED 且不泄漏异常详情。
8. encoder 控制器移除凭据/租约变量、固定离线 CPU 环境、恢复信号处理器；Popen/回执是显式 fixture。
9. 缺失或超过1MiB回执拒绝，不打印其内容；fixture 子进程角色，不冒称真实编码。
10. trained_voice CLI 非预期错误脱敏、503保留 blocked 状态。
11. F27 NumPy flush DC残留观察。
12. F28 benchmark逐条 GPU 身份观察。

### F27：flush 尾音归零，但 NumPy DC 记忆未归零

实际 NumPy：480样本常量0.2→flush(192)→240样本零输入，尾音最后为0，但后续零输入240样本全部非零，峰值 **6026 int16**；fresh Leveler 同长零输入全零。NumPy仅清 `_last`，Rust源码的非空 flush 还清 `dc_x1/dc_y1`。

**已核对影响范围：** worker `run_job` 每次调用 `_reset_leveler(pid)`，关闭旧对象并创建新对象；这次反证是复用同一 Leveler 的 API/后端一致性缺口，不证明正常跨请求路径复用该残留，更不证明截图里的沙沙声根因。Rust没有编译/执行，不能把源码差异说成已实测双后端等价或不等价。

### F28：benchmark 接受两端点全部测量都声明 GPU0

执行原 `run()`/`measure()`、两实际本地 HTTP 端点、真实 profile/pin/WAV/ledger 文件。health fixture 分别声明 GPU0/1、CUDA_VISIBLE_DEVICES=0/1；18条合成统计却全部声明 GPU0。报告仍为 `measured-speed-only`，`real_gpu_verified=true`、`speed_target_passed=true`，而行内 worker索引仍含0/1。

**证据边界：** health/模型/PCM/计时均为 fixture，报告中的上述 true 是被反证的工具输出，绝不是本批真实GPU验证或RTF成绩。端点身份与逐条实际合成身份缺少一致性校验；不能由此证明部署时真的两端共享GPU，也不能用两个健康回执替代运行期硬件与等效参数证据。两个缺陷均未修复。

## 3. 三轮实际执行

| 范围 | 第1轮 | 第2轮 | 第3轮 |
|---|---:|---:|---:|
| CPU合同，原360＋新12 | 372 PASS | 372 PASS | 372 PASS |
| NumPy DSP分块合成信号案例 | 12 | 12 | 12 |
| 原EdgeTrimmer AST合成信号案例 | 8 | 8 | 8 |
| 独立真实CLI合同 | 4 | 4 | 4 |
| CPU失败/错误/跳过 | 0/0/0 | 0/0/0 | 0/0/0 |

CPU共1116通过；新增36包含30保护和6次未修观察，不能解释为全部功能修复。分块/裁剪器保留既有问题，不重复编号。CLI每轮backend-static、backend-runtime、benchmark-default均按预期exit2/BLOCKED；resource-status exit0但GPU未验证，**预期阻塞不计模型成功**。脚本 `run_pass2_dsp.py` 和 `run_pass2_dsp_cpu.py`；后台执行已正常exit0、无监听端口。

本批没有重跑浏览器146、Player VM22/latency VM16、Go79/独立F02竞争或独立ASGI2.3 companion；这些只保留历史记录，不挪作本批新成绩。CPU合集含原ASGI/进程/文件合同，模型、ASR、声纹及特定调度角色仍为显式fixture。没有Torch tensor/optimizer/Gloo/NCCL、完整模型、GPU、物理麦克风/播放器或声学验收。

## 4. 完整性与未完成项

- 新测试预检12/12通过；三轮测试身份及F27/F28观测一致。
- Node30、JS检查、产品Python AST及新审计脚本语法、repack check通过；不改冻结产品/lockfile。
- 625份历史文件SHA保留；53源资产、94冻结哈希、正式HEAD15文件、300建议原文/处置及Q25–27各50条校验不变。
- 依赖沿用，pip freeze与前端检查点完全相同；没有新增安装。Rust/rustc/cargo、Torch/Qwen不可用；Go可用但本批未跑Go。
- `g0-pass2-dsp-coverage.json`、`g0-pass2-dsp-findings.json`、三轮原始收据、manifest及 `verify_pass2_dsp.py`为当前证据；交接完整内嵌增至79份。
- F01–F26及原DSP分块、短breath、校准/裁剪/播放器短尾问题继续未修，不将合成信号当真实语音。
- 后续仍待：encoder回执内容/退出码一致性、各工具语义终态/样本预算的完整失败矩阵、ABI空指针/长度/返回码与Rust真实工具链验证、两worker版本/参数及测量身份持续一致、真音频听测和端到端首声。

下一批完整复读剩余 Go security 及测试/go.mod、LICENSE/MEMO，共10份1662行；再进行全53份第三遍与300条最终处置/测试映射。真实长录音训练、参考贡献追踪、DeepSeek首prefix、双T4等效参数、自然连续朗读、无沙沙、真实RTF≤0.3等要求均未豁免、尚未签收。**不越过G0先改DSP，不跳S1或另开Q28，不要求用户点击Continue。**
