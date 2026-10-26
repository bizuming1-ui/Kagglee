# G0 全源第二遍第9批：Go安全／测试与文档收尾

日期：2026-10-23；分支 `arena/1160bd87-kagglee`。

**第二遍53项全文复读已完成；完整第三遍仍0，G0仍PARTIAL/BLOCKED。产品未改，未生成18发布包。**

## 1. 阅读范围与进度

以下均重新全文阅读，工具输出未截断；不把测试执行计作源码阅读。

| 文件（相对 kaggle/source/） | 行数 |
|---|---:|
| LICENSE-QWEN-DERIVED.txt | 201 |
| MEMO.md | 220 |
| go/gateway/fidelity_test.go | 187 |
| go/gateway/go.mod | 3 |
| go/gateway/preflight_test.go | 67 |
| go/gateway/reliability_test.go | 159 |
| go/gateway/security.go | 247 |
| go/gateway/security_test.go | 342 |
| go/gateway/segmenter_test.go | 123 |
| go/gateway/voice_binding_test.go | 113 |
| **本批合计** | **1662** |

第一遍53/53、13668行保持；第二遍由43/53、12006行推进至 **53/53、13668行，剩0**。此范围是冻结包内53资产，不等于整个Git仓库所有文件，更不等于三遍全文或所有功能验收。

## 2. 安全与既有测试的交叉核对

本批检查认证失败/owner预算隔离、令牌桶锁、并发名额与panic/取消清理、已知/未知Content-Length、JSON单值与Unicode、代理凭据剥离/请求取消、CORS、首prefix调度与原文保留测试、档案绑定和preflight只读行为。

`kaggle/tests/pass2_security_boundaries_test.go`新增12主测试，**10保护＋2未修观察**，只在SHA匹配的产品副本旁编译，不把探针放进冻结源码：

1. 失败认证只耗失败桶，不消耗owner通用/语音预算或占名额。
2. 1000个真实goroutine竞争容量7令牌桶，恰好7次通过；启用race。
3. 8项预算环境变量的上下边界、越界、非整数和整数溢出拒绝。
4. 重操作限额独立于语音名额，取消至handler退出后释放。
5. handler panic展开defer后不泄漏语音名额，后续合法请求仍可进入。
6. Unicode JSON字节预算在精确边界通过、少1字节拒绝；已知和未知长度两种路径。
7. CORS预检不等于API认证：跨host拒绝、合法预检不调用业务、未认证POST仍拒绝。
8. 代理删除全部凭据header值，保留有界请求内容和目标路径。
9. 原反向代理取消传到实际本地HTTP上游，错误不包含上游地址，名额释放。
10. 混合BMP/补充平面Unicode字符预算、history/system边界和非法角色；直接非法UTF-8字符串被validator拒绝。
11. F29：wire畸形Unicode在解码后被替换并接受。
12. F30：供应商HTTP错误正文可把假配置密钥带入客户端帧与指标。

### F29：解码先替换畸形Unicode，后续UTF-8检查失效

实际本地HTTP→原Guard→原decodeJSON→原validateSpeak：孤立高代理项、孤立低代理项、原始非法UTF-8字节三类输入，均HTTP200，输入字符串变为 `a�b`。直接将非法UTF-8交给validator会拒绝，但JSON解码已完成替换，后续 `utf8.ValidString` 只能检查替换后的字符串。

这是**严格输入与原文保真边界缺口**，不是认证绕过。见证使用组合校验handler，不执行完整speak、TTS或实际读音；没有声称正常浏览器JSON.stringify会产生这些畸形输入。修复阶段仍需统一非法编码、代理项、重复键等策略及兼容范围，不能直接删除或改写合法正文。

### F30：未脱敏上游HTTP错误进入客户端ERROR／END与metrics

实际授权网关 `/api/speak`→原Session.produce→原StreamLLM→本地HTTP401替身。请求未提供X-DeepSeek-Key，使用配置的**合成假密钥**。替身错误正文回显Authorization和私有详情；原StreamLLM把前800字节拼入错误，客户端ERROR、END和metrics记录均包含假密钥。

这是第三方错误内容未脱敏的传播路径；**不是未授权访问证明，也不是某真实供应商已泄密的证明**。API仍需要有效共享Bearer；供应商、错误正文与配置密钥全部是fixture，没有读取真实凭据、调用真实DeepSeek或生成PCM。后续应采用稳定公开错误码/安全消息，保留受保护诊断，不把截800字节误当脱敏。

两项均三轮复现，**尚未修复**。此前F01–F28及其他专题观察保持，不重复编号或宣称解决。

## 3. 三轮验证结果

| 每轮范围 | 第1轮 | 第2轮 | 第3轮 |
|---|---:|---:|---:|
| 原Go主测试／含子测试 | 40／56 PASS | 40／56 PASS | 40／56 PASS |
| 第一遍Go专项 | 10 PASS | 10 PASS | 10 PASS |
| 上批Go专项 | 13 PASS | 13 PASS | 13 PASS |
| 本批Go专项 | 12 PASS | 12 PASS | 12 PASS |
| **Go合计主测试／含子测试** | **75／91** | **75／91** | **75／91** |
| CPU既有合同 | 372 PASS | 372 PASS | 372 PASS |
| 副本go vet | PASS | PASS | PASS |
| 独立F02竞争见证 | 预期非零＋DATA RACE | 同左 | 同左 |

Go通过集合含子测试共273，CPU共1116；新保护30次、新未修观察6次。通过集合失败/跳过/race warning均0，CPU失败/错误/跳过均0。**独立F02故意失败见证不混入通过数字，F02仍未修。** 各轮使用 `-race -count=1`；第三方服务仅自有loopback HTTP。旧F23无限健康循环仍隔离在自有测试子进程并核对退出；测试服务器/处理goroutine正常清理。后台验证已exit0，无监听端口。

本批继承CPU372并实际重跑，包含原进程/锁/ASGI/NumPy/文件合同及F27/F28 fixture反证。没有新增Python测试；没有重跑独立CLI四项矩阵、NumPy分块/裁剪器探针、独立ASGI2.3、浏览器146和Player/latency VM，不挪用其历史成绩。原Go首prefix→本地worker请求测试重跑，不是实际DeepSeek/模型首声或速度成绩。

## 4. LICENSE与MEMO裁决

- LICENSE已全文读完：许可副本、修改声明、来源归属、条件性的NOTICE保留、商标限制及免责声明等条款已记录。**阅读文件不等于项目依赖、模型、训练数据或再分发法律合规签收**；实际适用范围、依赖许可/NOTICE清单与发布材料仍待核对，不出具法律结论。
- MEMO顶层仍为历史step15、xvector-only及maxgain12等表述；冻结产品当前17 ICL/maxgain6，已有D01文档漂移继续保留，不改冻结MEMO、不重复登记为新缺陷。其部分历史“短breath已修”等说法也不能覆盖后续F10实证。
- 测试通过证明断言成立，不证明断言覆盖全部协议/真实模型/听感；segmenter内部breath标记不等于worker会播放参考片段。generated-only、参考PCM不拼接要求保持。

## 5. 封存与下一步门禁

- 686份历史文件SHA、53源资产、94冻结哈希及正式HEAD15文件保持；原300建议与Q25–27每题50条不变。
- Node30、JS、产品Python与新审计脚本AST、repack、Go探针gofmt以及三轮副本vet通过。
- Go1.23.9沿用，无新安装；pip freeze与DSP批完全相同。Rust/rustc/cargo、Torch/Qwen仍不可用；无完整模型、真实GPU、训练、物理音频或声学/性能签收。
- 封存校验首跑错误地要求F02在 `halt_on_error=1` 下仍发出逐测试fail事件；实际是立即退出并发出包级fail。已保留首错日志，改为同时核对非零退出、DATA RACE、指定见证run与包级fail；不修改产品/测试，不重跑或抹除三轮记录。
- 当前检查点：`g0-pass2-security-coverage.json`、`g0-pass2-security-findings.json`、`progress-pass2-security.json`、`verify_pass2_security.py`；完整交接80份。

**下一步进入第三遍全源交叉审查，不实施S1：**

1. 先按API→Go→Python→文件快照追踪输入、pin、档案修订和错误脱敏；每份必须重新全文阅读，局部跟踪不计信用。
2. 然后核对生成/网络/播放生命周期、取消所有权、GPU租约及训练产物绑定；已知问题建立修复顺序和回归映射，不只重复通过测试。
3. 全53份第三遍和300条最终处置/失败见证映射完成前，G0保持未签收；缺真实硬件/音频的项目继续BLOCKED。
4. 不新增伪训练按钮，不用fixture替代双T4、长录音训练、无沙沙/音色/连续朗读、DeepSeek首prefix和真实RTF≤0.3验收，不要求用户点击Continue。
