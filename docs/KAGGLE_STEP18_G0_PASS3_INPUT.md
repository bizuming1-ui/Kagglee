# G0 全源第三遍第1批：输入、档案内容绑定与认证文件

日期：2026-10-23；分支 `arena/1160bd87-kagglee`。

**第三遍7/53份、1930行；剩46份11738行。第一、第二遍均53/53、13668行。G0仍PARTIAL/BLOCKED，产品与冻结发布包未修改。**

## 1. 本批第三遍全文信用

| 文件（相对 kaggle/source/） | 行数 | 本遍交叉核对 |
|---|---:|---|
| go/gateway/main.go | 478 | speak验证/trim、profile加载、激活重检、错误/代理、路由与认证 |
| go/gateway/security.go | 247 | Unicode解码边界、body预算、令牌桶、名额/取消与期限 |
| go/gateway/session.go | 692 | profile JSON类型、pin序列化、generation默认值/范围、队列/播放遥测、错误与metrics |
| py/qtts_common.py | 211 | 档案路径/读取、原子JSON、归档提取、配置和音量目标 |
| py/voice_binding.py | 60 | 实际跨语言内容hash、类型/范围、NOFOLLOW/NONBLOCK、文件大小变化 |
| py/resource_limits.py | 172 | 上传预算、暂存/replay清理、后台准入与取消所有权 |
| py/access_control.py | 70 | 私有口令文件/锁、文件类型检查时机、转发目标 |
| **合计** | **1930** | **7份全范围重新阅读，无截断** |

浏览器app.js只局部复看660–720请求构造，library_api.py只局部查看严格JSON入口，llm等其他调用点也没有本批第三遍全文信用。没有把第二遍阅读、测试运行或AST扫描当作第三遍全文。7份的all_three_complete仅表示三遍阅读记录齐全，**不表示其缺陷已修或产品验收通过**。

## 2. 新证据与原有建议映射

新增6项Go合同（5保护/1观察）与6项Python合同（5保护/1观察）：

- 实际Go/Python代码比较8个合法pin向量：UTF-8/NUL、缺省与显式gen、gen整体null、metadata排除、top_k负零和0、Unicode不同码点序列、边界参数与长度前缀。
- 12个非法generation类型/范围向量两端均拒绝；不是用另一份hash实现代替产品代码。
- 两本地worker ack fixture期间实际改变generation参数，原activate最终pin重检503，旧active保留。
- 原完整speak对null/空/错误text类型/尾随JSON拒绝，无session/worker调用。
- 两个不同合法profile ID、相同内容的pin相同：pin是内容标识，**不是身份、授权或声学相似度**。
- 上传读取最多预算+1字节即拒绝，不截断冒充完整音频；精确预算保留全部字节。
- body暂存在溢出、断连、下游异常三种路径关闭，不进入不该执行的解析/业务。
- 原子JSON替换失败保留旧私有文件、清临时文件，后续重试可用；不是多文件事务证明。
- 参考文件fstat后长度增长被原binding拒绝；不是同长度恶意改写/同UID隔离保证。
- 两实际认证CPU进程取得同一私有口令，仅输出摘要供临时比较；口令不进日志，临时目录清理。
- F31、F32未修观察，详见下节。

`pass3-input-recommendation-links.json`将8条**原有**建议逐项链接到实际测试身份或未修见证：R1-013/016/020/083、R2-028/039/050/063。每条明确覆盖不足；原300条不改，specific_row_test_signoff/final_disposition_signed_off/product_fix_implemented均false。相邻generation类型保护不能冒充完整ref_text schema签收；单文件replace不能冒充候选/JSON事务；旧训练metadata fixture不能冒充真实训练或原生模型。

## 3. 两项新确认的未修问题

### F31：同一JSON的top_k:null跨语言含义不同

实际磁盘profile包含 `gen:{"top_k":null}`：Go JSON解为map[string]float64时将null变成0，`loadProfileInfo`接受并产生非空pin；同目录/同JSON交给实际Python `reference_binding`，因None不是数值而抛ValueError。合法的gen整体null两端均按缺省处理，不能把两种null混为一谈。

本批Go测试通过受控CPU子进程调用当前Python文件，校验ABI字节和内容pin，不调用模型。参考文件是明确的hash字节fixture、不是可播放WAV。**不证明正常建档会写入该非法字段，也不证明已成功激活或生成错误音色。** 这是配置schema/内容绑定接受域不一致；两端应在计算pin前统一严格类型语义。

### F32：认证文件若为FIFO，无写入方时先阻塞再谈类型校验

实际原 `ensure_access_token`：自有0700认证目录下，既有`.access-token`是0600 FIFO且无writer，子进程在调用前发送握手，之后不能返回，测试外部强制终止并reap；同脚本的普通文件control正常返回。`_read_file`用NOFOLLOW但没有NONBLOCK，open在fstat确认普通文件之前阻塞。

**边界：** 没有真实口令、用户目录、真实bootstrap、远端请求或GPU工作。攻击者是否能写私有目录不是此测试结论，不能称远程认证绕过。0.25秒是测试收容边界，不是产品性能成绩；自有子进程已清理。后续应在安全打开且不被特殊文件阻塞的前提下检查类型/属主/大小，保留有效私有token及并发锁语义。

F01–F30、D01及旧DSP/播放/训练/校准观察继续未修。本批不靠新编号掩盖既有问题。

## 4. 三轮实际回归

| 每轮范围 | 第1轮 | 第2轮 | 第3轮 |
|---|---:|---:|---:|
| 原Go主测/含子测 | 40/56 PASS | 40/56 PASS | 40/56 PASS |
| 既有Go专项10+13+12 | 35 PASS | 35 PASS | 35 PASS |
| 新Go专项 | 6 PASS | 6 PASS | 6 PASS |
| **Go主测/含子测合计** | **81/97** | **81/97** | **81/97** |
| CPU旧372+新6 | 378 PASS | 378 PASS | 378 PASS |
| 副本go vet | PASS | PASS | PASS |
| 独立F02竞争见证 | 预期非零/DATA RACE | 同左 | 同左 |

Go含子测共291通过，CPU共1134通过。新保护共30次、未修观察共6次。通过集合失败/错误/跳过/race warning均0；F02独立故意失败不混入通过数，仍未修。所有Go回归启用-race/-count=1，产品源码未插入新探针。F29/F30随原S2套件实际重跑，仍未修；F23无限health循环继续隔离于自有子进程，正常退出已核对。

Go/Python预检各6通过。后台三轮正常exit0，无监听端口；CPU进程/FIFO/认证并发进程已清理。没有重跑浏览器146、Player/latency VM、独立ASGI2.3、独立CLI矩阵、分块/裁剪器探针，不挪用历史成绩。原CPU套件包含实际ASGI/进程/锁/NumPy/文件测试及明确模型角色fixture，不是全功能或模型验收。

## 5. 后续实施建议与门禁（尚未修改产品）

1. 为generation建立跨语言schema，区分缺省字段、gen整体null与成员null，禁止无声强制转换。
2. 将本批8合法/12非法向量固化成修复后的公共合同，并增加成员null、额外键和大数策略。
3. 严格检查原始JSON UTF-8和代理项，保留合法码点序列，不用替换字符假装原文保真。
4. 统一重复键、未知字段、浮点/布尔/字符串接受策略，不能仅修改Go而让worker域更宽。
5. 保留生成参数进入pin的属性；不要通过忽略gen来“修复”两端不一致。
6. 激活最终核对同时包含内容pin与conditioning模式，覆盖尚未修复的F24。
7. 准确区分单文件replace与候选/转写/profile多文件事务，保留旧成功档案与失败证据。
8. 认证读取不得在确认文件类型前无限等FIFO；新增特殊文件/目录/链接/权限矩阵。
9. 保留认证目录0700、文件0600、锁与两进程一致性，不把拒绝异常文件改成静默重建口令。
10. 上游错误使用安全公开码和阶段，私有诊断不直接回显HTTP正文/密钥，覆盖未修F30。
11. 首prefix、文本保真与播放终态分别测试；当前browser/API trim并不受producer原文拼接测试完整保护。
12. 将这些证据作为300建议的部分映射，待第三遍全覆盖后才做最终处置，不把本批8行当全300签收。

## 6. 封存与下一步

739份历史证据SHA、53源资产/94冻结哈希、正式HEAD15文件及原300/Q25–27各50保持。Node30/JS/产品与新审计Python AST/repack/Go探针gofmt通过，三轮副本vet通过；pip freeze与第二遍收尾相同，无新依赖。Go沿用1.23.9；无Rust/Torch/Qwen/实际模型/双GPU/训练/物理音频/音质/提速签收。完整交接81份。

当前 `g0-pass3-input-coverage.json`、`g0-pass3-input-findings.json`、`progress-pass3-input.json`、`verify_pass3_input.py`；各轮原始日志、manifest与建议映射保留。

下一批继续第三遍参考分析/API/档案修改与备份事务的完整复读，优先检查候选/转写/pin/模式切换及取消所有权，再依次完成剩46份、300最终映射和真实目标环境门禁。不跳S1/Q28，不实施未获G0签收的DSP修复，不要求用户点击Continue。
