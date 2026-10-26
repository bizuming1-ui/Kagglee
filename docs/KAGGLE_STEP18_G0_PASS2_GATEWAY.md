# 第十八阶段 G0：全源第二遍第6批——网关调度、流协议、取消与激活终检

日期：2026-10-23；活动分支：`arena/1160bd87-kagglee`。

**本批限定审计完成，产品代码未改，新增F23/F24确认未修。G0仍PARTIAL/BLOCKED，无18包。** 专项测试通过不等于全功能、真实DeepSeek/Qwen、双GPU、训练、听感或提速签收。

## 1. 全文与累计覆盖

本批全文均位于 `kaggle/source/go/gateway/`：

| 文件 | 行数 | 第二遍语义重点 |
|---|---:|---|
| main.go | 478 | speak生命周期、上下文/注册、激活回执与最终状态、代理脱敏、路由/健康/预检 |
| scheduler.go | 490 | 队列优先级、取消清理、重试与已消费PCM、worker帧、停滞watchdog、健康与RTF估计 |
| session.go | 692 | binding/条件、遥测与水位、逐delta生产/结束flush、顺序转发/END、失败与指标 |
| segmenter.go | 489 | exact/live/read策略、首prefix、词/小数/引号边界、段间暂停和呼吸元数据 |
| llm.go | 137 | 请求参数/认证、逐行SSE、完成/错误判定、上下文取消 |
| **合计** | **2286** | **新增5份完整第二遍语义阅读** |

scheduler先完整1–240、再241–490；session分1–240/241–480/481–692；main分1–155/156–320/321–478；segmenter分1–245/246–489；llm完整1–137。以上产品源输出无截断。旧测试/安全函数等调用点仅局部核对，不记额外全文信用；编译全部Go文件也不等于其余测试文件已完成第二遍。

- 第一遍保持53/53内嵌资产、13668行；不是整个Git仓库所有文件。
- 第二遍：26/6003 + 5/2286 = **31/53、8289行，剩22份**。
- 第三遍：**0/53**，测试经过不补第三遍信用。
- 当前台账：`docs/validation/step18/g0-pass2-gateway-coverage.json`。

## 2. F23：HTTP503的健康响应被计为可用，网关回执报告两节点健康

源：`scheduler.go:434–455`、`main.go:225–238`。**原Go实际编译、本地HTTP复现，确认未修。**

healthLoop只看请求是否返回transport error，未检查HTTP状态码；503响应也继续decode JSON。只要其中ready为true、stalled_s小于阈值，就标记healthy=true。原网关health再按这些标记计数。

实验用真实本地HTTP服务固定返回503及 `{"ready":true,"stalled_s":0}`；为scheduler配置两个fixture worker引用，运行原healthLoop，随后调用原网关health。结果：HTTP200的网关回执中 `workers_healthy=2`、`ok=true`。

原healthLoop没有停止接口，因此实验放在**自有Go测试子进程**，父进程设置15秒保底期限，核对子进程成功退出和观察标记；不把永久goroutine留在外层累计套件中。子进程中的HTTP服务清理后整体退出。这里是两个协议fixture引用同一本地服务，**不是两张GPU或两个真实模型**。没有执行完整bootstrap，也不声称线上worker确实返回过这种状态组合。

结论限定为健康准入未校验HTTP状态，不能用这个回执签收模型可用性。生命周期停止接口、JSON结构/预算与过期健康记录等仍需完整矩阵，本批不一并宣称已解决。

## 3. F24：激活期间条件模式改变，参考binding不变，最终仍提交成功

源：`main.go:281–348`、`session.go:73–82、100–136`。**原激活/文件/哈希与真实本地HTTP复现，确认未修。**

初始loadProfileInfo得到ICL条件和reference binding；收到worker回执时检查初始binding/conditioning。最后重新loadProfileInfo，但只比较binding，未同时复核最终conditioning。binding包含参考字节、ref_text、language、generation参数，不包含model_output_mode；将该元数据改为sentence-buffered会使读取出的conditioning变成trained-speaker-vector，但binding相同。

确定性交错：

1. 创建真实私有临时profile和参考哈希输入，保留 `active.json={"id":"previous"}`。参考文件刻意只是哈希fixture，不是可解码音频。
2. 调用原activate。原代码发送真实本地HTTP `/profile/load`。
3. handler在回执前实际改写profile.json，把model_output_mode改为sentence-buffered；返回初始ICL条件与初始binding的成功回执。
4. 原激活终检读取到新的trained-speaker-vector条件，但binding未变，仍提交active.json并返回HTTP200。
5. 验证当前档案条件与回执条件不同、binding相同、活动档案已变成fixture。

worker load回执明确为fixture；**没有创建/验证真实训练产物，没有运行模型、后续合成或播放，不能说已绕过worker训练产物准入或听到错误声音。** 本项是激活成功回执与最终条件版本不一致。与F20的Python重载删除假成功不同；本批另设Go最终删除拒绝保护，原Go删除终检确实会503并保留旧活动档案。

后续需把有效模型/条件/绑定/档案版本纳入一致性终检或事务比较；这只是待实施方向，不在本批修改产品或另开设计问题。

## 4. 新增13项：11保护 + 2未修观察

`kaggle/tests/pass2_gateway_boundaries_test.go`只复制到忽略目录，与逐SHA匹配的原Go包编译，不写入冻结网关。预检13项全部通过，启用race detector。

| # | 合同 | 真实性与限制 |
|---:|---|---|
| 1 | 首次失败丢弃未消费PCM、撤回produced计数、优先另一健康节点，重试回执attempts=2 | 原scheduler、两个本地HTTP协议fixture，无模型 |
| 2 | 已消费PCM后出现worker错误，不重试/重放、不重复计数 | 原run/SegBuf；HTTP流与事件建立确定性交错 |
| 3 | 已取消排队job在健康调度前移除并标记cancelled | 原队列/上下文，无实际合成请求 |
| 4 | 后段先完成仍按段0→1转发PCM，END一次，指标记录一次 | 原serve和实际二进制帧；预填生成PCM fixture、内存ResponseRecorder |
| 5 | PCM Write失败令serve取消上下文，不记录成功END/完整run | 原serve；明确ErrClosedPipe writer fixture，非慢TCP写阻塞实验 |
| 6 | LLM读流取消传播到本地HTTP handler上下文，handler和调用返回 | 真HTTP/SSE头/原StreamLLM，无真实DeepSeek |
| 7 | LLM length截断保留原prefix并上报LLM错误，END仍含错误而非静默成功 | 原produce/serve；真实本地SSE，TTS只注入失败回执 |
| 8 | 100段中英日韩/小数/原始格式文本的read生产不访问LLM、不改写文本 | 原read生产与原分段；文本测试不等于自然连续声学 |
| 9 | 水位高阈值/回滞/恢复及过期遥测的现有放行政策保持 | 原telemetry/allowDispatch；受控时间戳，无真实播放或内存峰值保证 |
| 10 | stats前空EOF、残header、截断PCM负载不能计served | 原scheduler、真实本地HTTP坏流；不同于旧F03的stats后残header |
| 11 | 激活期间档案删除，503且旧active保留、无活动临时文件 | 原activate/真实删除/原子提交；HTTP成功回执fixture |
| 12 | HTTP503仍计入两健康worker | **F23观察通过=确认缺陷**；健康循环在自有子进程 |
| 13 | 条件模式改变但binding不变，激活仍200 | **F24观察通过=确认缺陷**；实际文件变更/HTTP回执fixture |

保留原默认首块4、2–8实验边界、相同session seed/pin、generated-only PCM，不启用参考音拼接或新融合。旧 `TestFirstTTSRequestBeforeLLMTailArrives`本批实际重跑：本地SSE首prefix在LLM尾部放行前到达worker协议端；不是实际DeepSeek/声卡首声成绩。

## 5. 三轮交叉回归：Go与Python分开计数

总runner：`docs/validation/step18/run_pass2_gateway.py --round N`。每轮Go `-race -count=1`，测试副本逐文件hash核对；Go模块网络下载禁用。原包40主测含子测56；旧G0专项10；新专项13。Python companion沿用全部360项，**本批无新增Python测试**。

| 轮次 | Go原主测 / 含子测 | 旧专项 | 新专项 | Go通过主测 / 含子测 | Python通过 | F02独立竞争见证 |
|---|---:|---:|---:|---:|---:|---|
| 1 | 40 / 56 | 10 | 13 | 63 / 79 | 360 | 预期非零、DATA RACE |
| 2 | 40 / 56 | 10 | 13 | 63 / 79 | 360 | 预期非零、DATA RACE |
| 3 | 40 / 56 | 10 | 13 | 63 / 79 | 360 | 预期非零、DATA RACE |

通过套件每轮失败/错误/跳过0，没有race warning；Go含子测试合计237通过，Python合计1080通过。主测试/子测试、不同语言不揉成一个“全功能通过”分母。

旧F02 map alias竞争见证是**独立预期失败**：每轮非零并检出 `WARNING: DATA RACE`，不加入通过套件。旧F03奇数PCM、stats-only、坏error JSON与stats后残header仍复现未修。F16–F22在360项中也重新观察、验证自有资源清理。

Go的实际LLM HTTP取消测试不同于F18用户合成响应断连：本批未做浏览器→Go→真实worker的TCP断连或慢TCP客户端实验。F18仍是进程内ASGI2.4观察，独立ASGI2.3 companion未重跑。也未重跑旧三类网关协议脚本/完整历史六矩阵、Chromium全量、独立旧CLI四矩阵、14分析AST/12DSP或缺cache的provider六案例。

## 6. 工具、环境和封存

- 原有Go不可用，审计venv新增 `go-bin==1.23.9`（历史同版），`--no-deps`安装。保存安装日志、pip安装报告（含wheel URL/SHA）、Go可执行哈希、版本、完整freeze；对比上批freeze，**只新增这一发行包**，其余依赖保持，不称freeze完全相同或全部二进制环境等同。未安装Torch/Qwen/Rust或模型。
- Node30、JS、全部33份产品Python加本批5个审计脚本共38份AST、repack、原Go及含新增探针副本的go vet、gofmt检查通过。gofmt未提供venv顶层wrapper，最初该路径不可用，已按实际GOROOT/bin/gofmt格式化并检查；三轮正式收据在格式化之后生成。
- 525份历史文件逐SHA保持，53资产/94冻结哈希/15正式文件及原300建议、Q25–27各50未改；旧checkpoint不重签。冻结代码、原包、正式工作台、浏览器复制实现和隐私/录音/取消功能未改。
- 当前 `g0-pass2-gateway-{coverage,findings}.json`、`verify_pass2_gateway.py`、`progress-pass2-gateway.json`；验证后同步progress-checks。run manifest绑定本批代码、报告、日志、环境、检查和交接，排除自身及可变进度输出。
- 完整交接更新至**77份原文备忘录**；字节数/SHA由handoff-progress和当前progress收据核对。产品未修改、问题未修复，不能把观察通过当成发布可用。

## 7. 下一步与未撤销需求

继续剩22份第二遍，优先前端app/recorder/index的流终止、取消、遥测与完成排空，再DSP/工具及剩余Go安全/测试文件；随后完成全部53份第三遍及300建议最终处置/失败映射。G0未完成前不跳S1–S8或问题28，不发18包，不要求点击Continue。

更快真实首声、首个可用DeepSeek prefix立即生成、更响受保护输出、全部参考候选贡献可追踪、generated-only PCM、无沙沙、自然连续、短参考相似度、双卡同条件声学、RTF≤0.3、>10分钟录音与真实训练/提速等要求均未撤销或签收。无用户真实WAV/完整模型/双T4/物理声卡证据，不能从截图确定噪声根因，也不宣称已完成所有功能/语音质量验证。
