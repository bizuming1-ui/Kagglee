# G0第五批：Python启动、监督、工作进程与绑定链（未签收）

## 结论与实际覆盖

本批全文语义第一遍新增5份、1536行；累计39/53资产、10184行，尚有14项未完成第一遍。完整第二、第三遍仍为0；专项测试三轮不是全源三遍语义审查。G0未通过、S1未开始，产品/原始–17包/正式工作台不改。

| 文件 | 本批完整范围 | 语义核对重点 |
|---|---|---|
| kaggle/source/py/bootstrap.py | 1–451 | 导入副作用与状态目录；有界子进程与进程组超时；平台Torch保护/发行包身份；工具与模型获取；GPU门禁；恢复；supervisor当前startup_id故障收据；只停止本次创建进程；隧道认证与失败路径 |
| kaggle/source/py/supervisor.py | 1–219 | 子进程角色环境最小化；租约FD/nonce继承；仅自身进程组终止；退避/崩溃循环；健康/致命配置；缓存重载；周期快照；信号、PID与lease清理 |
| kaggle/source/py/worker.py | 1–680 | 模型加载前设备/租约；T4 dtype策略；参考缓存/绑定；生成码适配器调用；锁/取消/静音停顿；逐段DSP/裁剪；统计/错误帧；重启；异步响应队列与HTTP生命周期 |
| kaggle/source/py/clone_stream.py | 1–126 | ICL/xvector输入；生成码窗口/左上下文/可选右看；有限样本率与长度；取消/尾部/生成器关闭；参考码只作conditioning，不传codec。未运行真实Torch窗口或完整生成 |
| kaggle/source/py/voice_binding.py | 1–60 | 文件名/类型/大小/O_NOFOLLOW；UTF-8与长度前缀跨语言hash；gen默认值、数值/布尔/非有限校验。它是内容绑定，不是身份认证/声学分数 |

精确hash及逐文件范围见g0-runtime-coverage.json。当前剩14项：analyst.py、audio_rt.py、library_api.py、reference_segments.py、Rust Cargo.toml/lib.rs、6个工具、LICENSE及MEMO；外围仓库仍有独立审查范围，不由53项台账替代。

## 三轮专项回归与进程协议

每轮独立Python进程执行原G0的84项CPU/安全/租约/可靠性专项，再加10项新运行边界，合计94项；三轮均0失败/错误/跳过，共282通过。新10项为7保护+3原行为观察；捕捉旧缺陷通过不等于已修。

运行器run_runtime_audit.py，逐项结果、源与测试hash、三份观察见runtime-audit-round1..3.json；unittest日志为runtime-regression-round1..3.txt，stdout/stderr另存runtime-round1..3-console.txt。既有测试未修改，历史G0/训练/Go/前端收据不重写。NumPy回退被明确强制，未编译或执行Rust。

新增7个保护：
1. 关闭实际synth异步响应迭代器会设置生产者cancel Event，CPU替身生产线程能退出。
2. 错误voice_binding在任何静音/生成PCM之前失败，不启动engine.stream，并释放锁/busy。
3. 原RealEngine.load_profile只清除同路径prompt缓存，保留其他路径；不启用参考静音增强或参考PCM拼接。
4. 真实文件hash复核既有跨语言字面值17f55c…；采样参数变化改变绑定；bool/小数top_k/非有限值拒绝；符号链接不接受。
5. 即使breath_bank含非零参考数组，原lead_audio仍只输出有界全零计划停顿，不拼接参考音频。
6. 无效clone模式与缺失ICL转写拒绝，不静默回退。
7. 工作帧5字节小端长度头与Unicode统计JSON一致。

另实际执行两个现有协议脚本，各内部3轮，由run_runtime_protocols.py串行调用：

- ownership_process_check.py：真实supervisor、POSIX FD继承/租约、worker/analyst角色继承、gateway不继承、离线争用409、停止后可重新预约、PID清理。**模型角色是CPU stand-in**，没有真实GPU/VRAM或训练。
- fatal_startup_check.py：真实supervisor与本地HTTP致命健康替身，当前startup_id故障收据、bootstrap.wait_ready快速停止、仅本次Popen关闭、子进程退出及PID清理。没有实际触发真实模型MimiConfig加载错误。

脚本hash、实际退出码与每轮JSON输出见runtime-protocol-receipt.json及runtime-protocol-*.txt。不是重跑全部历史6类协议，也不是完整启动Kaggle模型/隧道/下载链。

## 新确认行为：均未修复

### S18-G0-RUNTIME-F07：异步响应队列没有容量与生产反压

worker.py:650–673：asyncio.Queue()默认maxsize=0，emit仅call_soon_threadsafe(q.put_nowait,item)，不等待消费者。直接执行原synth，使用有界CPU生产替身排入512个小PCM帧及终止哨兵；未消费时观察maxsize=0、队列513项，随后正常消费并清空。三轮一致。

这是应用层容量/反压缺口，不是测得无限内存增长或外部DoS。fixture不是TCP慢客户端压力；真实模型token上限、Go单worker并发、ASGI/socket缓冲和取消共同影响实际占用，尚未测量。后续策略需在有界排队、跨线程投递、断连取消、终止哨兵和阻塞退出间建立合同，不能直接塞一个会抛QueueFull的put_nowait后声称修复。

### S18-G0-RUNTIME-F08：重载失败后engine prompt缓存与已接受绑定不原子一致

worker.py:257–275、396–409、452–466：RealEngine.load_profile先更新_prompts，再由Worker复核文件绑定。已缓存成功参考A；把文件改成B并重载，显式resolver替身读取B、随后把磁盘恢复A，Worker正确检测重载中变更而抛异常。但engine._prompts已是B，Worker旧profiles/voice_bindings仍是A；下一任务以当前A的正确pin进入，缓存存在判定不触发重建，原run_job调用的生成替身拿到B prompt。

三轮观察：failed_reload_rejected=true，当前文件与接受pin匹配=true，缓存prompt与当前文件匹配=false；初次+失败重载resolver共2次，下一job未重建且未标failed。

实际执行原Worker和RealEngine.load_profile及真实文件hash；重型resolver/prompt/stream和GPU清理明确为fixture。没有执行真实ICL提取、Qwen/codec或听到错误声音。这是确定性失败原子性控制流复现，不冒称线上并发HTTP或音色混淆已声学复现。后续应设计准备/验证/提交与失败回滚或缓存失效合同，并与Q25的候选/绑定版本一致性一起保留测试；当前不改产品。

### S18-G0-RUNTIME-F09：模式规范化与报告/会话检查不一致

clone_stream.py:13–22用strip().lower()接受` XVECTOR `，返回xvector=true、空ref_text；worker.py:65–70对原环境值做精确比较，反而报告icl-generated-only-codec。三轮直接调用原函数一致复现；未运行模型。

这会使被接受的有效条件与报告字段不一致；不等于证明真实双GPU声音不一致。后续需统一规范化/拒绝政策并保证请求pin、加载回执、health和实际生成条件相同；不能通过更换UI标签掩盖实际条件。当前未修。

## 仅源码观察或仍阻塞的验证

- bootstrap的后台模型下载join没有总体期限；Go/cloudflared获取未见固定版本内容hash校验、Rust引导运行远端脚本。此批未访问/执行这些下载或安装路径，不能称验证了供应链/可用性故障。
- 子进程启动OSError后gave_up、非worker健康失效、全部关键进程退出时的总退出政策，仍需专用故障矩阵；现有致命健康用例不涵盖所有启动失败。
- Worker after_job在锁释放后执行、重启与忙状态交错、长生成/慢客户端真实资源峰值，仍需压力/生命周期补验，不将源码疑点写成实证缺陷。
- 原trimmer预滚/短尾、NumPy分块依赖、指标语义等历史问题仍未修；本批不是DSP新实现。
- GeneratedCodecWindow和fast_generate_streaming的真实Torch/完整模型路径未执行；没有靠安装假Torch把它们签为真实codec测试。源码生成码隔离意图/文件pin/fixture调用不等于真实声纹、无额外语音或同条件双卡声学证明。

## 保持、归档与下一步

新F07–F09另列g0-runtime-findings.json，原300建议初审映射/Q25–27各50项/F01–F06和各历史验证器保持hash不变。新台账不把本批测试当成全源第二/第三遍。Node30、JS/新测试语法、5份Python AST及只读repack/冻结一致性检查均通过；正式15文件工作台未动，没有18发布包。

下一步补剩14项的分析/API/参考切分与DSP/工具/说明全文，再完成全源第二/第三遍和建议处置更新，不跳G0先实施S1，不预填Q28。用户录音、完整权重/真实训练、双T4同条件输出、自然连续朗读、首声/RTF≤0.3及无沙沙仍未验收；整体PARTIAL/BLOCKED。
