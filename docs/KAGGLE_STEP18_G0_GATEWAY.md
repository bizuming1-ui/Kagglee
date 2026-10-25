# G0第三批：Go安全、会话、调度及协议链补审（未签收）

## 结论与范围

本批全文语义第一遍新增13份、3527行；累计31/53资产、6431行，尚有22项未完成第一遍。完整第二、第三遍仍为0。三轮测试不是三遍全文语义审查，更不是完整产品功能/声学验收。G0仍未通过，S1未开始，产品与原始–17冻结包、正式15文件工作台均不修改。

实际执行Go 1.23.9，启用CGO与race detector，不下载Go模块。测试副本逐文件核验与53资产基线一致；新增探针放在kaggle/tests，仅临时复制到忽略目录与原包一同编译，不把审计代码写入冻结网关。

## 全文阅读覆盖及语义记录

下表范围均为1至所列末行，含实现、注释和测试。精确源哈希与逐文件状态见g0-gateway-coverage.json；不把目录清单、测试执行或局部交叉查阅计为第二/三遍完成。

| 文件（kaggle/source/go/gateway/） | 末行 | 全文语义核对重点 |
|---|---:|---|
| security.go | 247 | Bearer鉴权、访问令牌、浏览器origin、JSON与上传预算、安全代理和出错路径；既有鉴权功能保留 |
| llm.go | 137 | DeepSeek流式HTTP、SSE增量、前缀文本、取消传播；未连接真实上游 |
| main.go | 478 | 路由与代理、profile激活、预检、私有字段与状态、请求上下文及流式响应；不将HTTP测试称浏览器验证 |
| scheduler.go | 490 | 健康与负载分配、任务租约、最大三次尝试、PCM消费后禁止重试、相同会话seed/绑定、帧校验与完成统计 |
| session.go | 692 | 分段按序转发、背压、取消/生产量、会话指标与快照；已复现快照别名竞争 |
| segmenter.go | 489 | UTF-8与标点边界、单位/时长估计、首段与尾段、原文拼接、聊天增量与朗读；测试不证明自然韵律 |
| fidelity_test.go | 187 | 文本保真、UTF-8与原文拼接既有断言的覆盖边界 |
| preflight_test.go | 67 | 已有预检与profile合同，失败不静默绕过 |
| reliability_test.go | 159 | 截断、有限重试、取消与顺序既有断言；缺失异常帧组合另增探针 |
| security_test.go | 342 | 认证、origin、预算、代理与私密状态既有保护案例 |
| segmenter_test.go | 123 | 中英文、尾段与不同切分策略；不是模型内容质量测试 |
| voice_binding_test.go | 113 | profile/绑定/conditioning固定、训练模式拒绝边界；相同参数不等于双GPU音色相同 |
| go.mod | 3 | module qtts/gateway；Go 1.21声明；本环境执行1.23.9，非目标Kaggle工具链实测 |

## 三轮独立执行与失败分流

每轮分别调用原包与哈希匹配副本，均使用`go test -race -json -count=1`，未依赖缓存测试结果。编译缓存只缓存编译产物。

| 类别 | 第1轮 | 第2轮 | 第3轮 | 能说明什么 |
|---|---:|---:|---:|---|
| 原网关主测试 | 40通过 | 40通过 | 40通过 | 含子测试各56通过、0失败/跳过 |
| 新增边界探针 | 10通过 | 10通过 | 10通过 | 5个保护合同+5个原缺陷观察；观察通过≠修复 |
| 独立竞争见证 | 非零退出且DATA RACE | 同左 | 同左 | **预期失败**，不得并入无失败的回归统计 |

`go vet ./...`退出0。原始、合同和竞争日志分别保存在gateway-{original,contract,race-witness}-round1..3.jsonl，机器收据为gateway-audit-round1..3.json。不是全仓三轮完整功能验收。

新增5个保护合同：已消费PCM禁止重试；未消费重试清空与样本计数一致；取消使实际本地HTTP工作请求停止且busy释放；两个本地worker请求保持同seed/voice_binding/conditioning；大于32MiB帧在分配前拒绝。它们不执行模型，也不证明两个真实GPU输出相同。

## 新增确认问题（均未修复）

### S18-G0-GO-F02：指标快照共享run map产生编码竞争

session.go:659–689：snapshot只复制slice，未复制每个run map；mergeClient稍后在锁内写同一map，快照的JSON编码在锁外。顺序探针先取snapshot再merge，证实先前快照内容改变；独立并发见证对原Metrics同时mergeClient与json.Marshal(snapshot)，三轮race detector均报告encoding/json/reflect读取与session.go:664写入竞争。

这是实际执行原方法的合成并发，不是线上压测/外网利用证明。潜在后果包括不一致与map并发读写故障，不能把本见证称线上崩溃复现。未来修复要明确快照所有权、嵌套对象不可变/深拷贝合同与锁范围，再保留无竞争验证；当前不改产品。

### S18-G0-GO-F03：工作进程帧合同校验不足

scheduler.go:351–407，真实本地HTTP fixture每轮复现四项：

1. 3字节PCM16负载被转发，样本计数以n/2取整为1。
2. 没有PCM、仅声明audio_s=0.01的stats仍被标记served。
3. 非法JSON错误帧`{`被忽略，后接合法stats仍成功。
4. 合法stats后仅2字节的下一帧头被忽略，仍成功。

本地工作进程是受信任边界；这不等于外部攻击入口。探针没有修复这些问题，也没有证明当前模型正常输出会触发它们。未来应规定PCM16对齐、统计与实收PCM一致、错误JSON与截断流失败策略，且不能让已消费PCM重试产生重复语音。

## 仅源码观察/待验证，不升级为已确认运行缺陷

- W01：scheduler.go:428的queue_wait_ms在完成时赋值，含生成耗时；Q26已记录该含义。没有用延迟fixture测出真实排队时间，不宣称性能改善。
- W02：healthLoop忽略HTTP状态及JSON解码错误；本批未增加有界健康循环故障fixture，仍待验证，不能宣称已复现错误健康判定。
- 上游SSE行预算、慢客户端写阻塞/超时为后续评估问题，未运行针对性压力实验。

## 真实本地协议链：仅选择3类，各内部3轮

1. mock_pipeline.py：实际Go→两个Python mock worker，鉴权、按序原文拼接、生成fixture帧、两worker被使用、关闭流后恢复；播放欠载为事件模拟，非声卡试听。
2. library_gateway_check.py：实际Go→analyst→文件系统，空库、超JSON预算上传、重启恢复、CAS/删除、原始hash；损坏音频处理**预期失败**，不称解码成功。
3. training_gateway_check.py：同链及合成PCM16训练输入快照、样本转写、hash篡改拒绝、租约禁止删除、源删除后副本仍在；未执行tokenizer/优化器/训练rank。

gateway-protocol-receipt.json记录脚本/hash/日志与每轮实际输出。没有重跑全部历史6类：adapter_gateway_check需要当前缺失Torch；codes_cli_check与ownership_process_check本批未选，不借历史通过冒充重新执行。

## 保持与下一步

新F02/F03另列g0-gateway-findings.json，不改原300条处置映射和训练链F01。Q25–27及各50建议文件保持hash不变，不为此自动新增Q28。历史各批覆盖、收据与验证器保留；新验证器只验证本批证据边界，不把旧验证器硬编码数量改成当前数。

继续G0剩余22项的前端、Python运行/分析、DSP/启动与恢复源码第一遍及外围脚本；之后完成全源第二、第三遍和建议映射更新，才可通过G0并进入S1。真实用户WAV、完整模型、实际训练、双T4同条件声学、物理首声/RTF≤0.3、无沙沙和自然完整朗读仍未验收，整体PARTIAL/BLOCKED。
