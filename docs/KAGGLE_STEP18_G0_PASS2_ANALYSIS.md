# 第十八阶段 G0：全源第二遍第4批——分析/API、参考切分与校准所有权

日期：2026-10-23；分支：`arena/1160bd87-kagglee`。

**本批限定审计完成，产品未改、缺陷未修；G0仍PARTIAL/BLOCKED，无18包。** 三轮专项通过不等于全功能、真实训练/模型/双GPU或声学验收。

## 1. 本批全文与累计覆盖

| 文件（`kaggle/source/py/`） | 全文行数 | 第二遍语义重点 |
|---|---:|---|
| `analyst.py` | 1211 | decode/清洗/ASR/候选/质检/建档/校准/重载/一致性/HTTP；版本和失败记录、临时资源与准入所有权 |
| `library_api.py` | 163 | 严格JSON/上传校验、共享admission、库租约与线程handoff、最终结果提交和错误脱敏 |
| `reference_segments.py` | 106 | 可信词级分区、实际PCM窗口重识别、时间戳偏移、低能量边界、短尾与可选词信息 |
| **合计** | **1480** | **新增3份重新全文语义阅读** |

analyst逐段1–200、201–400、401–600、601–800、801–1000、1001–1211完整复读，另两份完整输出，各源输出无截断。测试和resource_limits局部调用点复查不新增源码全文信用；不把经过函数的测试计作第三遍阅读。

- 第一遍：53/53内嵌资产、13668行，保持；不是整个Git仓库所有文件已审。
- 第二遍：上批20/3653 + 本批3/1480 = **23/53、5133行，剩30份**。
- 第三遍：0/53。
- 当前台账：`docs/validation/step18/g0-pass2-analysis-coverage.json`，旧台账/收据作为历史保留。

## 2. 原始参考实际贡献：统计、候选、conditioning不可混为一谈

复读确认的现有路径，不是新增融合算法或最终需求签收：

| 阶段 | 实际使用/记录 | 不能声称 |
|---|---|---|
| 输入/清洗 | 按文件解码、有限时长/总量/有限数值检查，记录原始RMS/peak、估计SNR、清洗决策与低输入警告 | 截图能定噪声根因；归一化等于去噪 |
| ASR/对齐 | 单文件不超anchor limit的手工文本可直配；长手工文本不强行配给短候选，依时间戳/实际窗口ASR | ASR文字是人工真值；长录音全部作为模型prompt |
| 候选评分 | 从可信片段组合窗口，预排后最多24个候选做embedding/评分，再选最多3个非近重复候选落盘 | 每个可能窗口都已评估；每个输入在最终prompt中的贡献都有独立可追溯权重 |
| centroid | 分析说话人空间中候选embedding均值用于典型性/质量评价，存centroid.npy | 这是Qwen条件嵌入融合，或ECAPA/MFCC可直接代替Qwen向量 |
| conditioning | 实际选定一个anchor与匹配ref_text供Worker加载；其余候选可切换/校准 | prompt列表自动融合三参考；统计参与等于模型conditioning参与 |
| 韵律/呼吸 | 全部可用clips/words参与部分韵律统计并保存候选呼吸文件；Worker参考呼吸播放仍禁用 | 可以拼入参考PCM来改善相似度或提前首声 |
| 校准 | 遍历已保存候选，在worker0用固定目标文本/seed合成后评分，最后重载 | 已测全部输入/全部窗口；双卡声学等效；质量/RTF已达标 |

`quality.reference_context`明确`all_audio_used_as_model_prompt=False`、`model_trained=False`，必须保留。默认16秒/24秒实验入口不变。上传配置允许长录音与训练数据入口每文件240秒的上限不是同一合同；本批17秒合成建档和既有20分钟时间戳规划测试**不是>10分钟真实音频转写、实际训练或全数据覆盖验收**。

`estimate_snr`仍是帧能量分位差，不是真值SNR；SpeakerModel可降级MFCC代理，ASR可降级CPU small，必须保留实际方法/能力披露，不把代理分数当声纹认证。`fidelity_index`是内部加权指标而非相似度百分比。ASR失败默认CER0.05、校准旧版本覆盖/失败重载/全合成失败选择、consistency按GPU使用不同seed等既有专题问题仍保留，未修、未重编号为新发现。

## 3. 新实证 F19：同一档案并发校准争用临时目录，并覆盖成功记录

源：`analyst.py:886–936、1085–1096`。**确认未修。**

校准临时id为`_cal_{pid}_{candidate_index}`，没有每调用独立标识或同档案互斥；共享HEAVY默认可接受两个操作。测试用两个真实进程内ASGI POST `/profiles/voice/calibrate`、原HEAVY(2)、原calibrate_profile、实际文件复制/JSON/rmtree，以及原Mock Worker.load_profile控制流，安排如下交错：

1. A创建`_cal_voice_0`，真实Mock Worker完成加载，A停在明确的合成替身回调。
2. B也为同一档案创建/写入`_cal_voice_0`，进入重载回调等待A完成。
3. A继续完成合成替身评分，在原finally中删除共享临时目录，提交成功的校准记录并返回。
4. B随后通过原Worker.load_profile读取该临时档案，真实文件已经不存在，返回找不到档案的错误；B得到score=-9的候选错误结果。
5. B把自己的错误校准记录覆盖A的成功记录。两个ASGI请求都返回HTTP200；最终记录是后来的失败结果。

每轮核对A的成功分数、B的缺失档案错误、仅A进入合成替身、最终记录等于B结果、临时目录清空和两个HEAVY槽位均释放。A/B按事件建立确定性交错，非概率压力测试；HTTP是ASGITransport进程内调用，worker transport、合成、ASR、说话人模型明确fixtures，仅一个Mock Worker角色，不是真双卡/真实网络/模型/音色实验。fixture分数不作为成绩。

F19不是“任意陌生用户可攻击”证明；它确认已准入的同档案校准操作缺少隔离与结果版本归属。全失败候选仍返回chosen等现象已有历史专题证据，这次新增裁决的核心是**两个原校准请求共享临时资源并相互清理/覆盖结果**，不是重复报旧问题。

## 4. 新实证 F20：档案在重载期间删除，最终仍报告成功/已保存

源：`analyst.py:388–412`。**确认未修。**

`load_on_workers`先取profile和expected pin，再收各worker回执；最终仅在`current`存在且pin变化时拒绝。如果目录在重载回调期间删除，`load_profile`返回None，最终复核条件被跳过，旧的成功回执原样返回；原reload_response据此生成HTTP200、`ok=True`、`reference_saved=True`。

测试真实创建/删除临时档案、执行原helper与JSONResponse；worker成功回执明确fixture，没有合成。每轮验证目录实际不存在、回执仍全部ok、响应仍200/已保存。

**没有验证删除后可继续播放旧声，也不是激活或认证绕过证明。** 非Mock Worker后续合成仍有缺失profile拒绝门禁；本项是重载最终状态与事实不符，不能拿此成功回执作为已删除档案可用/已保存的签收。

F19/F20分别单列新finding，原F01–F18及原始300建议/历史专题不覆盖。后续方向需比较同档案操作串行化、不可变版本/CAS提交、临时资源单调用所有权，以及重载终检把不存在视为失效；**尚未实施或作新的设计定案**。不能只换临时目录名而忽略最终结果归属、取消、删除与版本事务。

## 5. 新增12项：10保护 + 2原缺陷观察

文件：`kaggle/tests/test_pass2_analysis_boundaries.py`。预检12/12通过，失败/错误/跳过0。

| # | 检查 | 真实性/限制 |
|---:|---|---|
| 1 | 重载拒503、非布尔ok、错误pin、错误回执形状 | 原load helper；worker回执fixture |
| 2 | 重载终检参考文本版本变化，所有回执改为失败 | 原helper、实际JSON/内容pin |
| 3 | training-data嵌套重复JSON字段在准备前拒绝 | 真实FastAPI/TestClient；不执行训练 |
| 4 | 库处理非法Unicode/非bool校准标记/16.0上下文在租约前拒绝 | 真实路由与校验；begin未调用 |
| 5 | CPU ASR惰性迭代错误向上抛出，不默默变成功或重试模型 | 原ASR控制流，明确metadata iterator fixture，无Whisper |
| 6 | 超16384字节embedding结果不进入构建缓存，不虚报hit | 原缓存、NumPy与speaker fixture |
| 7 | 低能量边界切到15.3秒，实际PCM两窗口无重叠/遗漏、语言与时间戳正确 | 合成20秒PCM，ASR回调fixture |
| 8 | 进度回调异常在窗口ASR前传播，源段/PCM保持不变 | 原prepare_segments；不等于有公开建档取消API |
| 9 | 17秒长手工文本不覆盖短候选ASR文本，保留来源策略与非训练标记 | 原build函数/真实WAV/JSON；模型/信号分析明确fixtures |
| 10 | 后台build声称done却给不安全profile id时不得提交库成功；原始样本保留、租约可再编辑 | 真实库/路由/BuildAdmission；build callback fixture |
| 11 | 两个同档案ASGI校准共享临时目录，成功结果被错误结果覆盖 | **F19观察通过=确认缺陷，非修复** |
| 12 | 重载期间真实删除档案，仍得到200/已保存 | **F20观察通过=确认缺陷，非修复** |

library_api的begin+线程handoff同executor准入、后台结果有效profile检查、store.finish异常脱敏/租约清理仍需保持。HeavyAdmission用shield使HTTP等待取消不等于底层计算已取消；本批未把等待结束当ASR/合成停止，也未改其资源政策。既有F11窗口可选words清洗不一致、F12失败/残缺流被接受，三轮原测试仍复现未修。

## 6. 三独立轮专项回归

runner：`docs/validation/step18/run_pass2_analysis.py --round N`，N=1–3。组成：上批336 + 新12 = **348项/轮**；独立Python进程与临时状态，逐轮执行，按测试ID核对无重复且原336顺序保持。

| 轮次 | tests | failures | errors | skipped | 结果 |
|---|---:|---:|---:|---:|---|
| 1 | 348 | 0 | 0 | 0 | PASS |
| 2 | 348 | 0 | 0 | 0 | PASS |
| 3 | 348 | 0 | 0 | 0 | PASS |
| **合计** | **1044** | **0** | **0** | **0** | **专项通过，不是全功能验收** |

每轮`pass2-analysis-roundN.json`及regression/console日志保存逐ID、53源/测试/runner/support hash、依赖版本、F16–F20观察和真实性字段。沿用测试中的F16额外后代退出/锁释放、F18自有生产线程退出，以及本批F19准入槽/临时资源清理均有断言；不是保存PID后向无关进程发信号。

继承实际本地HTTP、CPU子进程/锁、NumPy/safetensors、WAV/文件/归档测试；F19新HTTP请求为进程内ASGI而非TCP。没有Torch真实算子、optimizer/GradScaler/DDP/Gloo/NCCL、真实Qwen/Whisper/ECAPA/Faster/codec、训练或双T4、Rust编译/执行、用户WAV、声纹/沙沙/自然连续听感、DeepSeek真实prefix、物理声卡或提速成绩。

本轮未重跑独立ASGI2.3 companion（348中保留的是F18 ASGI2.4）；也未重跑独立旧CLI四矩阵、完整Go/race/协议、Chromium全量、14分析AST/12DSP及缺缓存的真实provider六案例。不挪用历史数字充本轮成绩。

## 7. 工具、冻结、环境与完整交接

- 本轮venv存在，未重新安装依赖；保存当前environment与pip freeze，核对freeze等于上批快照。不把版本列表一致泛化为全部运行环境/二进制绝对相同。NumPy仍2.2.6，与生产requirements2.4.6不同；无Torch/Qwen/Rust/Go运行证据。
- Node30项、JS检查、全部产品Python加本批test/runner/advance/verifier/refresh共38份AST、repack一致性均检查并单列日志；最终`git diff --check`。
- 本批开始470份历史证据hash保留；53源/94冻结hash/15正式文件、正式revision和历史handoff不变。无产品改动/18包。
- 当前校验器`verify_pass2_analysis.py`核对23/53覆盖、348×3逐ID/hash/旧观察/两新finding、300原建议/Q25–27各50、冻结与完整内嵌交接，不重签旧检查点。
- 当前结果`progress-pass2-analysis.json`、`progress-checks.json`；本批manifest封存输入/报告/日志/收据/校验器/交接，排除自引用进度输出。
- 新报告加入交接，累计**75份备忘录全文**；实际字节/SHA在`handoff-progress.json`，逐份原文核对，不预填循环hash。

## 8. 下一步与未签收要求

继续剩30份第二遍，下一批优先完整启动/监督和backend preflight，核对provider版本、健康、启动失败/取消与进程所有权；随后其余前端、Go、DSP/工具/说明。再补齐全53份第三遍、300条建议最终处置/失败见证映射，按G0→S1–S8顺序实施，不以本批绿色越过G0。

冻结17、正式工作台空白文件/用户粘贴/完整浏览器复制保持；不默认融合prompt列表、改向量策略、强滤波或拼入参考PCM。>15秒/极长录音、<10秒相似度、>10分钟真实训练、双GPU等效参数、generated-only、首个可用DeepSeek prefix即生成、更响受保护输出、更低创建/实际首声延迟、安全/取消/隐私/版本冻结等要求均未撤销，仍待真实分层验证。不新增问题28，不要求Continue。整体**PARTIAL/BLOCKED**。
