# 第六阶段审查：不可变训练输入，不是训练执行

> 历史第六阶段冻结报告：当前源码入口已推进至step10；最新实现与真实编码阻塞见KAGGLE_STEP10_AUDIT.md，以下统计保留原第六阶段证据。

2026-10-21。先保存KAGGLE_STEP6_PLAN.md与专业问题5的50项行动建议，再实施。这里的“准备完成”仅为训练输入快照；**没有训练器、audio_codes、优化器、GPU模式切换或真正双rank运行**。

## 交付与操作

- 独立`kaggle/kaggle-fixed-step6.py`，210003字节/33资产，SHA256 `781eca6e2e34bdacbe2f5337bd6535512226c2122bbf3876d05634f2fc86d256`。原始与step1–5冻结，清单source_manifest_step6.json。
- “录制参考语音”→“声音库与样本”→先建立并上传到命名库→勾选音频→展开“训练输入快照”。每段单独填对应转写、显式选统一参考，并确认声音使用权/单说话人声明。点“生成训练输入快照（不训练）”。
- 下方可查看所有来源库的输入副本、按固定manifest哈希核对、二步确认删除。没有新增主导航。原始库删除后副本仍在，可继续从这个列表单独删除。
- 首版只接收**完整24kHz单声道PCM16 RIFF/WAV**。参考1.5–16秒、其他片段1.5–240秒、累计≤900秒。WebM/Opus/Ogg/MP4/其他采样率会明确拒绝，不换后缀、不静默转码、不截断；原始库内文件保留。原有参考处理仍走旧解码路径，不因此宣称ffmpeg已通过。
- 转写每条1–2000码点、合计16000；是用户提供的文本，没有ASR匹配/声纹核验。声明是记录用户同意，不是技术证明权利或身份。

## 具体增量与证据

| 项 | 实现 | 证据/限制 |
|---|---|---|
| 来源快照 | LibraryStore.snapshot只读同库租约，固定修订/所选ID/原始字节与SHA256，不修改last_build | 源库修改409、旧档案状态不变、源库删除后副本可验 |
| 格式 | 审查RIFF总长/所有chunk边界，拒绝多fmt/data、错误采样率/声道/位深、短/长/常量信号 | 真实合成PCM16测试；非恒定不等于有效人声 |
| 规范输出 | 每个选中样本保留全部PCM帧，规范WAV剥离额外容器元数据 | 帧数/PCM逐字节相同，原始和规范WAV哈希分别保存 |
| 数据约定 | train_raw.jsonl每行audio/text/ref_audio，统一参考来自选中集合 | 对照Qwen固定提交；没有把一个ref_text复制给全部样本 |
| 可追溯 | manifest记录库/修订/ID、来源名、原始/输出/文本/JSONL/计划哈希、帧数/采样率/峰值/RMS及声明 | 转写只在JSONL，列表/响应不重复返回私人全文 |
| 双rank计划 | 稳定哈希排序与epoch轮换，分两rank、等步数、无drop、奇数显式padding | 只是数学分配；不是DDP/采样器/梯度执行证据 |
| 事务与预算 | 独立UUID暂存→校验→原子目录发布；失败回滚，下次写操作回收孤立staging | 文件/rename故障注入；默认32快照、64MiB/快照、256MiB全局与256MiB磁盘余量 |
| 私密与路径 | 0700/0600、无任意路径/执行接口、软硬链接拒绝、固定哈希核验文件集合/索引/路径/内容 | 同UID恶意进程与断电耐久不是承诺；不是签名系统 |
| 接口 | 已认证/api/prep/training-data创建/列表/verify/DELETE；严格JSON字段/布尔/文本，继续小JSON预算及HEAVY准入 | Go预算/匿名401、FastAPI真实接口及错误脱敏 |
| 界面 | 逐条文本/显式参考/两项声明、结果/校验/单独删除，关闭/锁定清私密与代际隔离 | 浏览器HTTP夹具；不声称对接真实Qwen |
| 声明隔离 | 选中集合、新建/切库、删除库、自动回退源库时，不复用旧声明或转写 | 新增专门浏览器回归；修改后重新确认 |
| 备份边界 | 原始库和训练输入均不自动加入Dataset，既有profiles备份保持 | 真正_pack归档成员测试，独立副本要单独删除 |

## 文件与后续使用约定

数据位于STATE/training_data/{服务端UUID}/：

- audio/{样本UUID}.wav：规范24kHz/单声道/PCM16全部帧。
- train_raw.jsonl：逐条audio/text/ref_audio；路径相对**数据集目录作为工作目录**，不是自动相对JSONL文件。使用上游prepare_data时必须先切到该目录。
- manifest.json：schema1、state=input_snapshot_ready，不是ready_to_train/trained。
- rank_plan.json：kind=assignment_plan_not_execution。真正训练必须由支持等步数/显式padding语义的采样器落实并记录每rank覆盖，不能把这个文件当作实际训练日志。

`audio_format_verified/assignment_plan_verified`只对应格式/数学计划；`transcript_verified/speaker_identity_verified/tokenization_verified/training_verified/two_rank_execution_verified/inference_verified`均false。

列表`integrity_verified_now=false`，表示只读索引未重新验全部文件。明确校验成功才置true；请求携带先前固定manifest SHA256，不把当前任意文件存在当完整。校验失败前清除旧成功展示，失败不删除原件或旧独立副本。

## 分层验证（docs/validation/step6/）

- Python初检111通过；补充真实Dataset备份边界后为112。最终112×3＝336通过，python-round1/2/3.txt。
- Go28顶层/16子测试race三轮通过；工作台Node API30×3通过。
- training-http3-final.txt：真实Go→analyst→文件系统三轮，合成PCM16格式输入/逐条转写/声明拒绝/固定哈希/篡改409/源删除后副本独立/单独删除，且不增加模型JOBS。包含前阶段坏音频正确失败与原始哈希不变的旧链路。
- mock-pipeline.txt：两CPU Mock worker的三轮有序合成/中断恢复；不是真实GPU/人声。
- browser-initial.txt：旧库12＋新输入4＝16通过。training-browser-repeat3.txt：增加声明边界后5×3专项通过。最终全量106唯一用例×3＝318通过（10.6分钟），browser-repeat3.txt；不把中止的旧全量当三轮完成。
- 包原始22哈希＋当前33资产的确定性检查、语法/compileall/diff检查通过。实际runtime-probe.json仍blocked/退出2，缺Torch/流式后端/ffmpeg；没有加载模型。全量内第六阶段完整源码与系统剪贴板逐字节相同三次，且第五阶段包内容保持；均在隔离临时工作区。另跑final-copy-repeat3.txt专项3/3通过。

## 复审发现与中止记录

初版Python/真实HTTP/浏览器初检均通过，但进一步审查发现“新建库/删除库”等程序化切换可能沿用前一组授权勾选。没有放宽断言：新增源库绑定与选择变化失效机制，并覆盖新建/删除/切换/样本集合变化。旧全量已跑105项后中止，保存在browser-interrupted-consent-review.txt，不是全量通过；修正版另跑三轮。

## 仍未完成，不扩大解释

- 仍没有实际Qwen训练器/声学码提取/梯度或optimizer更新/检查点/双rank运行、训练与推理互斥模式。上述输入只是后续训练的可验证前置资产。
- 完整模型/双T4/DeepSeek/物理麦克风/ffmpeg压缩容器/音色/首声<3秒/RTF≤0.5没有验收。不能运行BF16/标准FA2示例或只加accelerate launch就声称T4训练完成。
- 格式首版有意严格；浏览器默认Opus录音通常不能直接生成训练快照，需后续受限解码器与真实容器验收或自行提供合规WAV。既有参考处理功能未移除。
- 准入按原始字节＋128KiB保守预留，可能提前拒绝；不以减少样本/截断音频回避预算。应用限额不是OS配额。损坏清单/未发布staging不假恢复；不是断电耐久或永久会话保证。
- 尚无外部训练进程的数据使用租约；不要在手动上游进程读取时删除副本。后续训练器须绑定固定版本并在运行期间阻止删除，不能从当前文件锁推断此功能已完成。
- 训练副本包含音频/私人转写，不进Git、不自动云导出，删除原始库不等于删除副本或历史Dataset中的既有档案锚点。
- 正式工作台只有5421字节余量，仍不放宽1MiB、不覆盖历史，本阶段独立文件交付。复制回归用隔离临时项目，不能称已发布正式工作台。
- 本阶段只可勾R1-079（记录授权声明）和R2-031（固定训练清单ID/内容哈希），累计21/300。R1-075只有训练输入具备格式/转写，原始库仍未解码；R2-032/采样器/实际rank覆盖等未完成，不勾选。第5题新增50建议，保留共250建议，不等于250项修复。

## 上游核对

https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/README.md

本次通过GitHub API再次读固定提交，核对单说话人audio/text/ref_audio及统一参考建议；没有执行上游训练脚本，也不把它的BF16/FA2示例当作T4可用证明。
