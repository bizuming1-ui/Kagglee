# 第十八阶段 G0：全源第二遍第7批——前端终态、取消、排空与遥测

日期：2026-10-23；活动分支：`arena/1160bd87-kagglee`。

**本批限定审计完成，产品代码继续冻结；新增F25/F26确认未修，G0仍PARTIAL/BLOCKED。** 浏览器/CPU/VM专项通过不是全功能、真实DeepSeek/Qwen、训练、双GPU、声学或提速验收，没有18发布包。

## 1. 全文阅读与累计覆盖

| 文件（`kaggle/source/web/`） | 行数 | 第二遍语义重点 |
|---|---:|---|
| app.js | 1715 | Parser/Player/Worklet、流终态与错误、访问/turn epoch、停止/锁定、播放排空、遥测/报告、库/参考/训练输入与诊断 |
| recorder.js | 358 | 权限等待、session所有权、设备/上下文/计时器、字节/数量/时长预算、原生封装、停止/取消与回调 |
| index.html | 144 | 脚本加载顺序、空白自命名/训练声明、视图/对话框、锁定与公开静态界面、限额和未验收说明 |
| **合计** | **2217** | **新增3份完整第二遍语义阅读** |

app按1–280/281–560/561–840/841–1120/1121–1400/1401–1715完整分段复读；recorder按1–185/186–358完整复读。index首次合并读取被工具截断，随后补读1–80及81–144，并再单独补齐31–80；最终全144行均已可见并复读，**不把截断输出算已读**。旧测试与VM局部核对不新增源码全文信用，运行测试也不计作第三遍。

- 第一遍保持53/53内嵌资产、13668行；不是整个Git仓库所有文件。
- 第二遍：31/8289 + 3/2217 = **34/53、10506行，剩19份**。
- 第三遍：**0/53**。
- 当前台账：`docs/validation/step18/g0-pass2-frontend-coverage.json`；旧台账/日志保留历史原样。

## 2. F25：END不是解析终态，后续PCM/文本继续处理，第二份汇总替换第一份

源：`app.js:729–776`。**完整冻结前端脚本在Chromium中复现，确认未修。**

case5只把解析出的汇总赋给d，未关闭协议状态或拒绝后续帧；读取继续到网络EOF。因此一条流依次含有效END、PCM、文本、另一份END时，后续PCM仍进入Player，文本仍进入回答区域，最终采用第二份汇总，且没有协议错误。

实验使用原网页及完整app/recorder脚本，不提取或改写产品函数；Chromium原生Response/ReadableStream承载明确wire fixture：

1. 第一份有效END，空timeline/per_gpu。
2. PCM16样本1的帧；Player端收到float32值1/32768。
3. 文本 `after terminal`；回答区域确实显示。
4. 第二份END带 `replacement_summary=7`；最终timeline确实采用它。
5. 网络关闭；只发送一次client report，errbox为空。

这是终态/顺序合同的缺口，**不是线上网关确实发送过这条坏流或外部攻击已成功的证明**。AudioContext/AudioWorkletNode为明确设备替身，只确认PCM传到播放器消息端，没有实际播放/声卡或真实生成模型。该PCM仍是生成流fixture，不拼参考音；不能从本项推断用户听到额外话语的根因。

旧F03是Go worker帧接受问题，本项是浏览器client帧END之后的状态机行为，不重复编号旧奇数PCM/stats后残header。后续需定义终态、重复END、后续帧、读流取消与有效汇总校验；尚未实施产品修复。

## 3. F26：网络EOF时先发报告，后续播放/欠载状态不再更新到报告

源：`app.js:625–644、784–818`。**原前端与真实浏览器计时器/序列化路径复现，确认未修。**

B的finally在网络读取结束后调用markGenerationDone，并把w清为false；随后立刻读取Player状态，发一次 `/api/report`。250ms循环仍刷新本地UI，但 `!x || !w` 后不再发送telemetry。声音可能还未开始或未排空，此时不能视为完整播放结果。

确定性实验：原应用接收0.2秒PCM fixture及有效END，立即网络EOF；设备替身暂不提供Worklet状态。第一次report为 `first_played_ms=0、underruns=0`。收到这份report后才注入：

- Worklet缓冲状态fill=4800，应用发送play命令、UI变为“播放中”。
- 一条延迟状态含underruns=1，真实UI刷新到欠载1。

核对最终仍只有一份report、内容与最初逐字段相同，期间telemetry数量也不增加。**延迟状态与设备均为fixtures，数值1不是实际物理欠载；play命令不是扬声器出声，不构成延迟/提速成绩。** 实验不主张正常Worklet在已经接收end后必然新增欠载，而是确认迟到状态和实际播放阶段不能进入当前“结束报告”。

第一遍“report before drain”原先仅源观察，本批补成完整网页事件链实证，首次正式登记F26。旧 `firstPlayedMs`在play命令处赋值的问题继续保留；本项额外是报告生命周期与后续更新缺口，不能只改字段名称就认为解决。

跨语言复核：Go在speak/serve返回后注销session，旧网络EOF后继续发telemetry也可能没有活动session。因此后续需区分生成结束、播放排空、取消与最终client-report合并，设计有界的状态/报告归属；不能简单把w永远保持true。Go调用点是上批已读源码的局部复核，不增本批全文信用，也没有修改任何端点。

## 4. 新增12项：10保护 + 2未修观察

文件：`tests/browser/pass2-frontend.spec.js`及专用fixture helper。预检12通过，失败/跳过/flaky/retry为0。HTTP/音频/设备故障明确替身，完整冻结脚本由浏览器实际执行。

| # | 合同 | 执行边界 |
|---:|---|---|
| 1 | 网络EOF后锁定仍abort旧session、hold/reset播放并清空聊天；重新解锁下一请求history为空 | 真DOM/turn/access epoch，fetch和音频替身 |
| 2 | pagehide在未结束body中锁定，迟到END经旧turn检查取消reader，不产生旧report/私密输出 | 原生流、真实事件与取消回调；非实际页面导航/远端Go |
| 3 | HTTP503 JSON错误可见，按钮释放，无PCM/无成功client report | 原B错误路径；HTTP响应fixture |
| 4 | body.read拒绝可见并释放按钮，不把等待状态永久卡住 | 原生流error；不声称旧F05取消/报告政策已修 |
| 5 | 坏END JSON不生成成功timeline，错误可见、无PCM | 原parser/JSON路径；保留既有错误处理 |
| 6 | 逐字节碎片化UTF8中英日韩/emoji与HTML字面文本正确合并，以textContent显示、不执行HTML | 原帧解析与浏览器DOM，无模型 |
| 7 | 录制中另增文件耗尽数量预算，finish再次核对后丢弃当前片段 | 原recorder、受控duration=1700ms/数据Blob，非真实1.7秒录音 |
| 8 | 重复stop回调只提交一次File，块清空、设备释放 | 原recorder、明确MediaRecorder/track替身 |
| 9 | 旧track-ended不能停止新owned recorder | 原owns检查与事件回调，不能当F04旧onerror已修 |
| 10 | 首次addModule失败后第二次可重新初始化并发请求，旧context关闭 | 音频替身；失败Blob仍未revoke，旧F06保留 |
| 11 | END后PCM/文本/替换汇总仍被接受 | **F25观察通过=缺陷存在**，不是修复 |
| 12 | EOF先发report，随后play/欠载UI变化不更新报告 | **F26观察通过=缺陷存在**，非物理音频测量 |

旧F04旧录音error影响新session、F05解析失败未cancel/abort、F06失败Blob URL不回收仍在旧11项中复现，未修。取消与权限、容器封装、空库/训练输入、安全/访问、正式工作台/复制等旧浏览器合同也全部重跑；没有把“准备训练输入”改说成真正训练按钮或训练闭环。

## 5. 三轮浏览器、VM与CPU回归，分别计数

runner：`docs/validation/step18/run_pass2_frontend.py --round N`。每轮独立Playwright进程，`--retries=0`；既有134 + 新12 = **146项/轮**。真实Chromium中的旧原生录制用振荡器/静音输入替换getUserMedia，不是实体麦克风。新12全部是明确网络/音频设备/事件fixtures。

| 轮次 | 浏览器 | 失败 / 跳过 / flaky / retry | Player VM | 延迟合同VM | Python CPU |
|---|---:|---|---:|---:|---:|
| 1 | 146通过 | 0 / 0 / 0 / 0 | 22通过 | 16通过 | 360通过 |
| 2 | 146通过 | 0 / 0 / 0 / 0 | 22通过 | 16通过 | 360通过 |
| 3 | 146通过 | 0 / 0 / 0 / 0 | 22通过 | 16通过 | 360通过 |

浏览器合计**438通过**；CPU合计**1080通过**，CPU每轮失败/错误/跳过0。本批无新增Python用例。两种VM分别22×3/16×3，原Player/Worklet代码和明确时钟/端口/status替身，不能把它们合并成实体播放成绩。

旧VM中已完成20/50ms短尾卡buffering/starved的观察继续通过，51ms可发play；这意味着旧缺陷仍存在，不是排空修好。重采样结束flush、首块时间/消费/声卡出声区别与Rust/DSP/trimmer分块问题也未修。默认首块4、2–8实验边界、generated-only与参考PCM禁播不变。

浏览器代码复制保护重跑：原始文件使用真实hash及浏览器sentinel保护，1–17完整包复制合同仍保持；不把sentinel声称为原始整文件浏览器复制。正式空白文件/用户粘贴和不强制预填流程保持。

每轮保留原始Playwright JSON/stderr、逐用例状态/单次执行、5份未修观察（F04–06/F25–26）、两种VM JSON、CPU逐ID日志/JSON、源/测试/support哈希。CPU继续F16–F22自有进程/锁/线程/临时资源清理，不重签旧收据。

**本批未重跑Go79项/独立F02竞争见证、独立ASGI2.3 companion、旧独立CLI/协议矩阵、14分析AST/12DSP或缺cache的provider案例。** 这些保留上批/历史成绩，不列作本轮执行。也没有真实DeepSeek、完整模型/codec、双T4、实际训练、远程Kaggle、物理声卡、用户WAV或声学/提速成绩。

## 6. 环境、检查、封存与交接

- node_modules未保留，按冻结package-lock执行 `npm ci --ignore-scripts`恢复；保存日志与依赖树，未改package-lock/产品依赖。预检及三轮使用实际Chromium。审计venv沿用，完整pip freeze与上批相同，没有新增Python发行包；Go1.23.9仍可用但本批未重跑其套件，无Torch/Qwen/Rust运行。
- Node30、JS检查、33份产品Python加本批5个审计脚本共38份AST、repack，以及前端/新探针/VM的JS语法检查通过。最终diff检查和manifest验证不替代模型验收。
- 575份历史文件、53资产/94冻结哈希/15正式文件、原300建议初审及Q25–27各50保持；原包/工作台/安全/录音/复制产品代码未改。
- 当前 `g0-pass2-frontend-{coverage,findings}.json`、`verify_pass2_frontend.py`、`progress-pass2-frontend.json`；验证后同步progress-checks。manifest绑定本批报告/测试/helper/runner/收据/日志/环境/交接，排除自身与可变进度输出。
- 完整交接更新为**78份原文备忘录**，以handoff-progress及当前progress核对具体字节数/SHA。

## 7. 下一步与全部未撤销要求

继续第二遍剩19份：优先Python/Rust DSP、音频边界与工具自检，再补剩余Go安全/测试和LICENSE/MEMO；随后全53份第三遍及300建议最终处置/失败映射。G0未完成前不跳S1–S8/问题28、不发18包、不要求点击Continue。

更快真实首声、首个可用DeepSeek prefix立即生成、更响受保护输出、全部候选贡献可追踪、generated-only、无沙沙、自然连续、短参考相似度、双GPU同条件声学、RTF≤0.3、>10分钟录音和真实长数据训练/提速等均未撤销或签收。截图不能证明噪声根因，fixture不能冒充真模型/实机/试听，整体仍PARTIAL/BLOCKED。
