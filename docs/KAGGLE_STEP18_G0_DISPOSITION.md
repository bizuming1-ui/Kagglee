# 第十八阶段300条建议处置映射（初审，未签收）

每条保留原ID/建议；测试家族是待执行合同，不等于每条已有独立测试。确证缺陷仅限收据所述范围。三遍全源未完成，G0未通过。

| ID | 初审分类 | 批次 | 建议 | 测试家族 |
|---|---|---|---|---|
| S18-R1-001 | documentation-or-test-contract | S7 | 将候选参与质心统计与实际ICL锚点分开显示，避免全部片段已融合的误解 | 候选条件来源 |
| S18-R1-002 | pending-evidence | S7 | 在合成收据记录选中的anchor_candidate，而不是只显示profile ID | 候选条件来源 |
| S18-R1-003 | pending-evidence | S7 | 记录实际锚点字节指纹与对应转写指纹；日志不明文写入私有转写 | 候选条件来源 |
| S18-R1-004 | pending-evidence | S7 | 用不同内容的三个候选验证只选中的音频进入提示提取 | 候选条件来源 |
| S18-R1-005 | documentation-or-test-contract | S7 | 审核“候选校准”文案明确逐个试验后选一个，不称多参考融合 | 候选条件来源 |
| S18-R1-006 | pending-evidence | S7 | 查验Faster真实接口的多参考能力，未支持时不伪造列表参数 | 候选条件来源 |
| S18-R1-007 | preservation | S7 | 禁止把三个片段PCM拼成一个提示并配不连续全文 | 候选条件来源 |
| S18-R1-008 | preservation | S7 | 跨候选声纹中心仅作评分依据，不声称它已替代模型speaker embedding | 候选条件来源 |
| S18-R1-009 | preservation | S7 | 为单个合法候选保留最短建档链路，不强迫三候选 | 候选条件来源 |
| S18-R1-010 | documentation-or-test-contract | S7 | 给未来多候选策略保留显式模式与回退边界，不静默改变17默认 | 候选条件来源 |
| S18-R1-011 | confirmed-defect-in-stated-scope | S1/S2 | 非法index的布尔、小数、对象与缺省语义分别测试，避免int强转误选或500 | 候选状态事务 |
| S18-R1-012 | pending-evidence | S1/S2 | 核查切换候选与校准并发时磁盘写入、工作者加载是否形成一致事务 | 候选状态事务 |
| S18-R1-013 | pending-evidence | S1/S2 | 候选文件复制失败时保留旧profile JSON，不留下半更新锚点 | 候选状态事务 |
| S18-R1-014 | pending-evidence | S1/S2 | 双卡仅一张加载成功时明确部分失败，不宣称启用完成 | 候选状态事务 |
| S18-R1-015 | preservation | S1/S2 | 旧会话遇新指纹必须继续拒播，不能热切后拼混音色 | 候选状态事务 |
| S18-R1-016 | confirmed-defect-in-stated-scope | S1/S2 | 转写编辑与候选选择同时发生时绑定同一版本，防止音文错配 | 候选状态事务 |
| S18-R1-017 | pending-evidence | S1/S2 | 校准临时profile的anchor_candidate元数据应指向实际试验候选，不能误标0 | 候选状态事务 |
| S18-R1-018 | preservation | S1/S2 | 候选变更后清理或替换提示快照时保留锁内核验 | 候选状态事务 |
| S18-R1-019 | pending-evidence | S1/S2 | 为重复点击候选与取消任务增加幂等与状态测试 | 候选状态事务 |
| S18-R1-020 | preservation | S1/S2 | 训练adapter的固定参考限制保持，不让候选切换绕过来源绑定 | 候选状态事务 |
| S18-R1-021 | documentation-or-test-contract | S6 | 分别记录请求、首个可用文本、排队、预填充、首PCM、首播放命令 | 分阶段首声度量 |
| S18-R1-022 | documentation-or-test-contract | S6 | worker t_start在加载提示之后，单独计量冷提示加载而不漏记等待 | 分阶段首声度量 |
| S18-R1-023 | documentation-or-test-contract | S6 | queue_ms当前覆盖锁等待等前置耗时，拆项后保留旧字段兼容 | 分阶段首声度量 |
| S18-R1-024 | documentation-or-test-contract | S6 | 浏览器firstPlayedMs当前在发play命令处赋值，标明不是硬件实际出声 | 分阶段首声度量 |
| S18-R1-025 | pending-evidence | S6 | 评估AudioWorklet消费首个语音样本的确认消息，区分主线程命令延迟 | 分阶段首声度量 |
| S18-R1-026 | preservation | S6 | 跨Python、Go与浏览器仅使用各自单调时间差，不能直接减不同纪元 | 分阶段首声度量 |
| S18-R1-027 | preservation | S6 | 显式静音停顿不能计为首个可用人声，保留禁止原音占位 | 分阶段首声度量 |
| S18-R1-028 | hardware-or-real-model-blocked | S6 | 首包平均之外记录p50/p95与冷暖状态，不用一次幸运值 | 分阶段首声度量 |
| S18-R1-029 | hardware-or-real-model-blocked | S6 | 将文本长度、参考长度、chunk_size和设备条件写入性能收据 | 分阶段首声度量 |
| S18-R1-030 | documentation-or-test-contract | S6 | 首声提速必须同时检查缺字与最终音频完整性，不能裁掉开头 | 分阶段首声度量 |
| S18-R1-031 | pending-evidence | S5/S6 | 对当前0.7秒下限和初始2秒策略建立确定性到达轨迹对照 | 播放启动 |
| S18-R1-032 | pending-evidence | S5/S6 | 分别测试高速稳定、慢速持续、突发包与长网络抖动 | 播放启动 |
| S18-R1-033 | pending-evidence | S5/S6 | 初次启动与欠载恢复分别设计目标，不统一缩到最小 | 播放启动 |
| S18-R1-034 | pending-evidence | S5/S6 | 将预测器无速率样本时的保守回退纳入首次播放测试 | 播放启动 |
| S18-R1-035 | pending-evidence | S5/S6 | 测量AudioWorklet统计消息的刷新间隔对主线程启动判断的影响 | 播放启动 |
| S18-R1-036 | pending-evidence | S5/S6 | 在44.1k及48k上下文验证重采样后的fill计秒正确 | 播放启动 |
| S18-R1-037 | confirmed-defect-in-stated-scope | S5/S6 | 短于启动阈值但已完成的真实语音应及时播放，不等待不可达缓冲 | 播放启动 |
| S18-R1-038 | pending-evidence | S5/S6 | 后台页、暂停恢复、锁定与取消后不得发送迟到play | 播放启动 |
| S18-R1-039 | pending-evidence | S5/S6 | 记录ring dropped样本；任何丢样不能只显示播放成功 | 播放启动 |
| S18-R1-040 | hardware-or-real-model-blocked | S5/S6 | 低延迟策略只能在欠载预算内启用，不能把断续当自然阅读 | 播放启动 |
| S18-R1-041 | hardware-or-real-model-blocked | S6/S7 | 对2/4/8/16帧首块大小做同文本同seed对照，测TTFA及总RTF | 模型与调度热路径 |
| S18-R1-042 | hardware-or-real-model-blocked | S6/S7 | 小首块与稳态大块若需不同大小，先确认真实生成器支持，禁止无效传参 | 模型与调度热路径 |
| S18-R1-043 | hardware-or-real-model-blocked | S6/S7 | 检查decode迭代器首次next含有的预填充时间，不能只测创建生成器 | 模型与调度热路径 |
| S18-R1-044 | hardware-or-real-model-blocked | S6/S7 | 单独计量token生成、codec解码及CPU拷贝，避免归因全部GPU | 模型与调度热路径 |
| S18-R1-045 | preservation | S6/S7 | 提示快照重用必须与内容指纹一致，不退回仅按路径缓存 | 模型与调度热路径 |
| S18-R1-046 | preservation | S6/S7 | 不为首声把ICL换成向量默认，保留相似度条件 | 模型与调度热路径 |
| S18-R1-047 | hardware-or-real-model-blocked | S6/S7 | 比较首段优先调度与后续并行的队头阻塞，不无证据锁死单卡 | 模型与调度热路径 |
| S18-R1-048 | preservation | S6/S7 | 确认Live聊天第一可用前缀触发不被朗读聚合配置覆盖 | 模型与调度热路径 |
| S18-R1-049 | preservation | S6/S7 | 保留最大生成token与取消限制，不能为速度删掉输出 | 模型与调度热路径 |
| S18-R1-050 | hardware-or-real-model-blocked | S6/S7 | 不默认每卡双模型增加显存；只有目标T4实测才接受吞吐结论 | 模型与调度热路径 |
| S18-R1-051 | documentation-or-test-contract | S7/acoustic | 原始RMS约-47.7只作为风险，不推断具体麦克风故障 | 参考清理 |
| S18-R1-052 | documentation-or-test-contract | S7/acoustic | 分别记录归一化前后语音电平与峰值，注明增益上限14dB | 参考清理 |
| S18-R1-053 | documentation-or-test-contract | S7/acoustic | 候选SNR是估计量，不能把17dB阈值当真实噪声声压 | 参考清理 |
| S18-R1-054 | hardware-or-real-model-blocked | S7/acoustic | 保留raw、strength0.85、strength0.55对照的处理收据 | 参考清理 |
| S18-R1-055 | hardware-or-real-model-blocked | S7/acoustic | 审查声纹相似0.94与SNR增益2dB门禁是否会误接收失真，不能只看单分数 | 参考清理 |
| S18-R1-056 | pending-evidence | S7/acoustic | 验证全零、强直流、很轻语音及背景声输入的处理决策 | 参考清理 |
| S18-R1-057 | hardware-or-real-model-blocked | S7/acoustic | 对齿音、气声、摩擦音单独测保真，不能以削高频冒无沙沙 | 参考清理 |
| S18-R1-058 | preservation | S7/acoustic | 不在用户未授权时保存或上传原始私有WAV作为公共证据 | 参考清理 |
| S18-R1-059 | documentation-or-test-contract | S7/acoustic | 已存在非平稳降噪不等于生成输出已降噪，明确处理发生阶段 | 参考清理 |
| S18-R1-060 | hardware-or-real-model-blocked | S7/acoustic | 录音时扬声器回录网页朗读的可能性仅列假设，不能由截图定论 | 参考清理 |
| S18-R1-061 | hardware-or-real-model-blocked | S3/S7/acoustic | 建立模型PCM、后处理PCM、浏览器录回的分层局部诊断，默认关闭私有采集 | 输出噪声定位 |
| S18-R1-062 | hardware-or-real-model-blocked | S3/S7/acoustic | 将codec窗口起点与边界脉冲位置关联，区分底噪和接缝爆音 | 输出噪声定位 |
| S18-R1-063 | hardware-or-real-model-blocked | S3/S7/acoustic | 对持续人声与停顿分别计算频谱，但无清洁真值时不称绝对SNR | 输出噪声定位 |
| S18-R1-064 | preservation | S3/S7/acoustic | 继续验证codec只收到生成码，不能回到参考码前缀解码 | 输出噪声定位 |
| S18-R1-065 | hardware-or-real-model-blocked | S3/S7/acoustic | 真实预训练codec与随机tiny codec的质量证据必须分列 | 输出噪声定位 |
| S18-R1-066 | pending-evidence | S3/S7/acoustic | 非有限模型输出当前替换为零，应评估失败拒播而非掩盖异常的策略 | 输出噪声定位 |
| S18-R1-067 | hardware-or-real-model-blocked | S3/S7/acoustic | 增益提升可能抬噪，记录处理前后噪声地板变化而不自动强门限 | 输出噪声定位 |
| S18-R1-068 | preservation | S3/S7/acoustic | 不能用输出全静音或静音段删除作为零噪声验收 | 输出噪声定位 |
| S18-R1-069 | preservation | S3/S7/acoustic | 保留模型自然人声呼吸与禁止添加噪声的区别，不自动切除语音气息 | 输出噪声定位 |
| S18-R1-070 | hardware-or-real-model-blocked | S3/S7/acoustic | 用户全程纯人声目标需真实WAV试听和添字检查，代码指标不替代 | 输出噪声定位 |
| S18-R1-071 | confirmed-defect-in-stated-scope | S3 | 实测同一信号整块与任意分块处理的样本一致性 | DSP状态 |
| S18-R1-072 | confirmed-defect-in-stated-scope | S3 | 重点验证NumPy不足96样本首块时淡入是否在下一块重新从零开始 | DSP状态 |
| S18-R1-073 | pending-evidence | S3 | 核查NumPy按输入块丢弃不足240样本RMS余数与Rust跨块累积差别 | DSP状态 |
| S18-R1-074 | pending-evidence | S3 | 比较Rust逐样本增益平滑与NumPy逐块插值，不能宣称严格等价 | DSP状态 |
| S18-R1-075 | preservation | S3 | 保持输出样本数与输入相等，不能为降噪补偿无记录延迟 | DSP状态 |
| S18-R1-076 | pending-evidence | S3 | 分别测试DC blocker状态、零输入残留与长静音后重新讲话 | DSP状态 |
| S18-R1-077 | pending-evidence | S3 | 测试max_gain_db=0隔离淡入和DC滤波，再开放AGC定位差异 | DSP状态 |
| S18-R1-078 | hardware-or-real-model-blocked | S3 | 同卡每段重置与跨卡各自状态不同需测量，不能只凭相同目标响度称一致 | DSP状态 |
| S18-R1-079 | preservation | S3 | flush的192样本衰减不是新生成语音，不能加入RTF语音分母 | DSP状态 |
| S18-R1-080 | documentation-or-test-contract | S3 | 若修复NumPy算法须保留Rust接口版本兼容，并添加跨后端容差测试 | DSP状态 |
| S18-R1-081 | hardware-or-real-model-blocked | S4/S5/acoustic | 将独立模型韵律重启、显式停顿、播放欠载三种接缝分类计数 | 连续朗读 |
| S18-R1-082 | hardware-or-real-model-blocked | S4/S5/acoustic | 保留朗读12/24首段、20/40/80稳态配置基线再比较，不盲目扩大 | 连续朗读 |
| S18-R1-083 | preservation | S4/S5/acoustic | 逐字验证分段重新连接等于原文，保护数字、缩写、引号和标点 | 连续朗读 |
| S18-R1-084 | documentation-or-test-contract | S4/S5/acoustic | 审查PauseBeforeMs与tail_pause_ms是否重复加停顿，先画时序再修改 | 连续朗读 |
| S18-R1-085 | preservation | S4/S5/acoustic | 禁止跨词PCM重叠掩盖接缝，不牺牲清晰度冒自然度 | 连续朗读 |
| S18-R1-086 | hardware-or-real-model-blocked | S4/S5/acoustic | 段尾8ms衰减及下段淡入需以有声边界实测，不只用零边界波形 | 连续朗读 |
| S18-R1-087 | hardware-or-real-model-blocked | S4/S5/acoustic | 欠载时0.94尾衰减属于播放补偿，不能误标模型本身沙沙 | 连续朗读 |
| S18-R1-088 | hardware-or-real-model-blocked | S4/S5/acoustic | 自然度对照必须同时保存整段朗读，不能只听裁剪后小片段 | 连续朗读 |
| S18-R1-089 | hardware-or-real-model-blocked | S4/S5/acoustic | 不同GPU同文与交替长文分别试听；同seed不等于波形完全相同 | 连续朗读 |
| S18-R1-090 | hardware-or-real-model-blocked | S4/S5/acoustic | 只有真实模型支持的连续条件才能声称跨段联合生成，不换名称包装独立合成 | 连续朗读 |
| S18-R1-091 | preservation | G0/S8 | 冻结原始至17包、全部manifest及正式工作台，新增18不得覆盖历史包 | 回归交付 |
| S18-R1-092 | documentation-or-test-contract | G0/S8 | 三轮100建议均标已确认问题、待证假设或保留约束，不虚报300个bug | 回归交付 |
| S18-R1-093 | documentation-or-test-contract | G0/S8 | 完成三轮审查后再逐题决策，每题50建议后才进入下一题 | 回归交付 |
| S18-R1-094 | documentation-or-test-contract | G0/S8 | 历史334测试不能算18新增验证，依赖缺失需如实记录和重建 | 回归交付 |
| S18-R1-095 | documentation-or-test-contract | G0/S8 | 对每个修复保留修复前失败、修复后通过的同输入收据 | 回归交付 |
| S18-R1-096 | documentation-or-test-contract | G0/S8 | 三轮Python、Node、Go race、协议和浏览器必须针对最终源码再执行 | 回归交付 |
| S18-R1-097 | hardware-or-real-model-blocked | G0/S8 | CPU合成信号实验不代替真实T4语音实验，硬件不足保持BLOCKED | 回归交付 |
| S18-R1-098 | preservation | G0/S8 | 按实测热路径选择语言；不要新增Java/C#/SQL服务凑多语言 | 回归交付 |
| S18-R1-099 | documentation-or-test-contract | G0/S8 | 最终18复制页、下载、剪贴板拒绝回退与手机逐字节校验不可省略 | 回归交付 |
| S18-R1-100 | documentation-or-test-contract | G0/S8 | 将全部已完成备忘录内嵌完整提示词；未完成轮次必须明确，不编造结论 | 回归交付 |
| S18-R2-001 | preservation | S7 | 保持qwen-tts-hf与旧qwen-tts发行版严格分离，源码同命名空间不等于同版本 | 实际模型接口 |
| S18-R2-002 | preservation | S7 | 下载源码必须核对PyPI wheel SHA256，收据注明实际提供模型类的发行版 | 实际模型接口 |
| S18-R2-003 | pending-evidence | S7 | 将三提示单目标被拒绝的实际接口行为加入未来多参考功能合同 | 实际模型接口 |
| S18-R2-004 | documentation-or-test-contract | S7 | 将三提示三目标定义为独立批量任务，界面不能称参考融合 | 实际模型接口 |
| S18-R2-005 | preservation | S7 | 保留列表prompt每项独立ref_text，不用共享一条文字冒三候选匹配 | 实际模型接口 |
| S18-R2-006 | documentation-or-test-contract | S7 | 字典prompt的批量ref_text共享行为应明确，不直接用于三段不同转写 | 实际模型接口 |
| S18-R2-007 | preservation | S7 | 引用prompt item中ref_code与speaker embedding的区别，不能用声纹平均替代ICL | 实际模型接口 |
| S18-R2-008 | preservation | S7 | 保持单ICL预计算提示的真实接口回归，不能为新模式破坏现有快照 | 实际模型接口 |
| S18-R2-009 | preservation | S7 | 向量模式继续要求显式选择，不把它作为未实现融合的静默替代 | 实际模型接口 |
| S18-R2-010 | hardware-or-real-model-blocked | S7 | 实际生成器、权重和声学结果未执行时，接口控制流通过不标模型实验通过 | 实际模型接口 |
| S18-R2-011 | documentation-or-test-contract | S7 | 建立全部候选分析清单，逐项列源文件、时间、匹配转写、指纹和有效性 | 候选条件合同 |
| S18-R2-012 | documentation-or-test-contract | S7 | 单锚点模式明确显示被用作ICL的候选及未用作ICL的其他候选 | 候选条件合同 |
| S18-R2-013 | documentation-or-test-contract | S7 | 若后续共享参数来自全部候选评分，记录算法与评分证据而非暗示音频融合 | 候选条件合同 |
| S18-R2-014 | hardware-or-real-model-blocked | S7 | 比较每候选合成时固定同文同seed同采样参数，确保差异确由候选造成 | 候选条件合同 |
| S18-R2-015 | preservation | S7 | 候选中心与实际Qwen说话人嵌入不同空间时不得直接替换 | 候选条件合同 |
| S18-R2-016 | hardware-or-real-model-blocked | S7 | 实验性的融合嵌入若提出，必须独立模式且真实盲听，不自动作为最佳方案 | 候选条件合同 |
| S18-R2-017 | preservation | S7 | 不跨候选拼转写或参考码以绕过模型批量长度校验 | 候选条件合同 |
| S18-R2-018 | documentation-or-test-contract | S7 | 候选顺序变化时用内容身份而不只用数组下标定位证据 | 候选条件合同 |
| S18-R2-019 | documentation-or-test-contract | S7 | 候选有效时长按实际WAV而非仅展示start/end计算，避免舍入差 | 候选条件合同 |
| S18-R2-020 | preservation | S7 | 候选策略、模型模式及参数调整必须使旧会话明确失效 | 候选条件合同 |
| S18-R2-021 | confirmed-defect-in-stated-scope | S1 | index必须严格整数且非bool，拒绝true变1与false变0 | 入口验证 |
| S18-R2-022 | confirmed-defect-in-stated-scope | S1 | 拒绝1.9截断成1，避免非整数JSON静默切换其他参考 | 入口验证 |
| S18-R2-023 | documentation-or-test-contract | S1 | 缺失index应明确拒绝还是显式兼容默认0，不让文档与行为矛盾 | 入口验证 |
| S18-R2-024 | confirmed-defect-in-stated-scope | S1 | null、数组、对象及NaN输入转换失败应返回受控4xx而非未捕获异常 | 入口验证 |
| S18-R2-025 | documentation-or-test-contract | S1 | 候选入口未知字段与重复字段的策略需与严格library接口一致 | 入口验证 |
| S18-R2-026 | pending-evidence | S1 | 验证candidates为非空合法列表，不能只依赖len和下标访问 | 入口验证 |
| S18-R2-027 | pending-evidence | S1 | 验证候选file为安全单文件名且普通文件，避免损坏profile路径越界 | 入口验证 |
| S18-R2-028 | pending-evidence | S1 | 手工ref_text不接受dict/list被str化，保留严格字符串与Unicode校验 | 入口验证 |
| S18-R2-029 | preservation | S1 | 保留训练档案禁止改候选和转写的409边界，不绕过版本固定 | 入口验证 |
| S18-R2-030 | documentation-or-test-contract | S1 | 增加真正HTTP参数与错误码测试；当前AST调用不冒充FastAPI测试 | 入口验证 |
| S18-R2-031 | confirmed-defect-in-stated-scope | S2 | 校准开始捕获完整候选集合版本，提交时核对未变再采用评分 | 校准版本提交 |
| S18-R2-032 | confirmed-defect-in-stated-scope | S2 | 禁止用旧候选评分选择重新读取后已更改的同下标候选 | 校准版本提交 |
| S18-R2-033 | confirmed-defect-in-stated-scope | S2 | 校准期间并发编辑转写不能被结束时静默覆盖，需冲突响应 | 校准版本提交 |
| S18-R2-034 | pending-evidence | S2 | 候选文件内容更改但文件名不变也要改变校准输入版本 | 校准版本提交 |
| S18-R2-035 | pending-evidence | S2 | 候选变更、文本变更、校准、删除应协调同一档案锁或乐观版本合同 | 校准版本提交 |
| S18-R2-036 | documentation-or-test-contract | S2 | 进程内线程锁与跨进程文件锁分别评估，不能把一个称全局事务 | 校准版本提交 |
| S18-R2-037 | documentation-or-test-contract | S2 | HEAVY最大2只限制并发数量，不等于每profile串行，不能替代状态锁 | 校准版本提交 |
| S18-R2-038 | documentation-or-test-contract | S2 | 对先写磁盘再等HEAVY被429拒绝的路径核对reference_saved状态 | 校准版本提交 |
| S18-R2-039 | documentation-or-test-contract | S2 | 原子JSON替换只保护单文件，候选复制与JSON提交之间仍需一致性设计 | 校准版本提交 |
| S18-R2-040 | pending-evidence | S2 | 校准提交前档案已删除或adapter状态已变化时必须停止，不能恢复旧状态 | 校准版本提交 |
| S18-R2-041 | confirmed-defect-in-stated-scope | S2 | ASR评估全部失败不再用CER0.05冒充实测值，应记录null与失败原因 | 校准缺失与失败 |
| S18-R2-042 | documentation-or-test-contract | S2 | 部分文本ASR失败时记录覆盖率，不能只对成功样本平均后隐藏缺失 | 校准缺失与失败 |
| S18-R2-043 | confirmed-defect-in-stated-scope | S2 | 全部候选合成失败时返回明确未选出有效结果，不能chosen0看似成功 | 校准缺失与失败 |
| S18-R2-044 | documentation-or-test-contract | S2 | 每候选的有效生成条数和预期条数同时保存，评分先验证完整性 | 校准缺失与失败 |
| S18-R2-045 | documentation-or-test-contract | S2 | 未测或低可信声纹指标不填高分默认值，应明确阻塞/降级语义 | 校准缺失与失败 |
| S18-R2-046 | pending-evidence | S2 | 候选排序排除非有限得分，NaN/Inf不进入max选择 | 校准缺失与失败 |
| S18-R2-047 | documentation-or-test-contract | S2 | 模型输出空音频、太短、全静音和缺字分别记失败而不只比声纹 | 校准缺失与失败 |
| S18-R2-048 | pending-evidence | S2 | 校准报告应保留先前有效结果，失败新校准不覆盖为貌似新最佳 | 校准缺失与失败 |
| S18-R2-049 | documentation-or-test-contract | S2 | ASR释放与临时目录清理放入覆盖所有异常的finally路径 | 校准缺失与失败 |
| S18-R2-050 | documentation-or-test-contract | S2 | 错误信息需脱敏且保留阶段，不能把原文和本机私有路径暴露给日志 | 校准缺失与失败 |
| S18-R2-051 | confirmed-defect-in-stated-scope | S6/acoustic | 同目标文本跨GPU诊断使用相同seed，修复100+17*ti+gi的设备偏移混杂 | 双卡诊断 |
| S18-R2-052 | documentation-or-test-contract | S6/acoustic | 将实际seed写入每张卡诊断条目，使测试条件可核验 | 双卡诊断 |
| S18-R2-053 | preservation | S6/acoustic | 会话调度当前各卡同seed的行为应保留，不把诊断偏移引入播放 | 双卡诊断 |
| S18-R2-054 | documentation-or-test-contract | S6/acoustic | 两卡同一voice_binding和voice_conditioning都要进诊断收据 | 双卡诊断 |
| S18-R2-055 | hardware-or-real-model-blocked | S6/acoustic | 记录实际dtype、模型版本、codec政策与DSP后端，不能仅比profile ID | 双卡诊断 |
| S18-R2-056 | hardware-or-real-model-blocked | S6/acoustic | 相同参数不意味着位级相同；阈值评分和人工听感结论分开 | 双卡诊断 |
| S18-R2-057 | hardware-or-real-model-blocked | S6/acoustic | 同文对照与不同文本交替朗读各自设计，不能用同文替代自然衔接 | 双卡诊断 |
| S18-R2-058 | documentation-or-test-contract | S6/acoustic | 所有条目失败时speech_db默认0不应参与一致性，明确缺失项 | 双卡诊断 |
| S18-R2-059 | documentation-or-test-contract | S6/acoustic | consistent布尔值应附完整性及阈值说明，不能称零噪声或100%同声 | 双卡诊断 |
| S18-R2-060 | documentation-or-test-contract | S6/acoustic | 诊断生成在锁定或请求取消后仍进行时保留资源状态，不误报即时停止 | 双卡诊断 |
| S18-R2-061 | confirmed-defect-in-stated-scope | S2/S6 | 校准结束必须检查load_on_workers回执，不能丢弃失败后正常返回 | 加载确认 |
| S18-R2-062 | preservation | S2/S6 | 保留文本/候选接口已有reference_saved与503部分失败语义 | 加载确认 |
| S18-R2-063 | preservation | S2/S6 | Go激活两卡并行、同绑定同模式核验及旧active保留不得回归 | 加载确认 |
| S18-R2-064 | preservation | S2/S6 | 激活最终再次读磁盘核对指纹的检查必须保留 | 加载确认 |
| S18-R2-065 | pending-evidence | S2/S6 | Python reload最终current为None时应视失败，而不是跳过版本核验 | 加载确认 |
| S18-R2-066 | hardware-or-real-model-blocked | S2/S6 | 候选校准只用GPU0的现状须说明；多卡校准需独立计划，不虚报双卡评估 | 加载确认 |
| S18-R2-067 | documentation-or-test-contract | S2/S6 | 加载某卡成功某卡失败后，不允许新会话静默只用成功卡冒双卡一致 | 加载确认 |
| S18-R2-068 | hardware-or-real-model-blocked | S2/S6 | 冷首次sanity合成耗时应与提示提取耗时分开记录，避免首声归因错误 | 加载确认 |
| S18-R2-069 | documentation-or-test-contract | S2/S6 | HTTP断开不等于后台模型加载已停止，未来重试需幂等/状态查询 | 加载确认 |
| S18-R2-070 | preservation | S2/S6 | 不得为降低激活耗时跳过Worker锁内参考前后两次指纹校验 | 加载确认 |
| S18-R2-071 | documentation-or-test-contract | S2/resource | 审查_cal临时profile移除后Worker提示缓存仍驻留的资源生命周期 | 缓存生命周期 |
| S18-R2-072 | documentation-or-test-contract | S2/resource | 重复校准相同临时ID时确保旧提示被替换，不能复用先前参考 | 缓存生命周期 |
| S18-R2-073 | documentation-or-test-contract | S2/resource | 删除档案后清理与它关联的profiles、voice_bindings、levelers和提示快照 | 缓存生命周期 |
| S18-R2-074 | preservation | S2/resource | 缓存释放必须获取合成同一把锁，不释放正在使用的GPU张量 | 缓存生命周期 |
| S18-R2-075 | hardware-or-real-model-blocked | S2/resource | 缓存容量按可测内存预算管理，而不是只看磁盘profile数量 | 缓存生命周期 |
| S18-R2-076 | documentation-or-test-contract | S2/resource | 临时校准ID与用户可启用ID区分，不能由列表选中临时声音 | 缓存生命周期 |
| S18-R2-077 | preservation | S2/resource | 备份继续排除_cal档案，不把测试用临时状态持久化为模型 | 缓存生命周期 |
| S18-R2-078 | documentation-or-test-contract | S2/resource | 临时目录清理失败记录状态并可回收，不无声积累数据 | 缓存生命周期 |
| S18-R2-079 | preservation | S2/resource | 生成器取消仍要close并释放有界codec窗口，不能因缓存修改遗漏 | 缓存生命周期 |
| S18-R2-080 | preservation | S2/resource | 不要盲目清空CUDA所有缓存导致每段冷启动，资源回收须按作用域 | 缓存生命周期 |
| S18-R2-081 | documentation-or-test-contract | S1/S2/UI | 候选点击期间禁用或序列化同档案变更按钮，避免重复并发写 | 前端迟到状态 |
| S18-R2-082 | documentation-or-test-contract | S1/S2/UI | 响应乱序时按操作版本更新高亮，不让旧响应覆盖新选择 | 前端迟到状态 |
| S18-R2-083 | preservation | S1/S2/UI | 继续保留accessEpoch和AbortController防锁定后迟到数据回填 | 前端迟到状态 |
| S18-R2-084 | documentation-or-test-contract | S1/S2/UI | 客户端取消只能停止等待时明确提示后台任务可能继续，不伪报服务器取消 | 前端迟到状态 |
| S18-R2-085 | documentation-or-test-contract | S1/S2/UI | 503且reference_saved时显示已保存未全卡就绪，不能笼统当未保存 | 前端迟到状态 |
| S18-R2-086 | documentation-or-test-contract | S1/S2/UI | 校准报告区分逐候选评分、最终提交、双卡加载三个状态 | 前端迟到状态 |
| S18-R2-087 | documentation-or-test-contract | S1/S2/UI | 没有有效候选或指标不全时不显示成功绿标 | 前端迟到状态 |
| S18-R2-088 | preservation | S1/S2/UI | 参考转写可审阅但日志默认脱敏，token不进URL/localStorage | 前端迟到状态 |
| S18-R2-089 | preservation | S1/S2/UI | 新增条件证明信息只放同源授权接口，不能自动上传外部诊断服务 | 前端迟到状态 |
| S18-R2-090 | preservation | S1/S2/UI | 新增交互保持移动端可操作、录音失败队列保留与锁定清空 | 前端迟到状态 |
| S18-R2-091 | preservation | G0/S8 | 原始库已有revision与lease设计可借鉴，但不直接修改其已成功数据格式 | 来源与保留 |
| S18-R2-092 | preservation | G0/S8 | 候选处理与真实训练继续分开命名，不把评分或缓存称训练提升 | 来源与保留 |
| S18-R2-093 | preservation | G0/S8 | 训练adapter来源hash与固定参考在新条件策略下仍必须核验 | 来源与保留 |
| S18-R2-094 | preservation | G0/S8 | 私有原始样本仍排除Dataset自动备份，新增诊断WAV默认不进入归档 | 来源与保留 |
| S18-R2-095 | hardware-or-real-model-blocked | G0/S8 | 代码、参数和参考版本相同的测试与实际用户WAV声学验收分开报告 | 来源与保留 |
| S18-R2-096 | documentation-or-test-contract | G0/S8 | 为每个确认缺陷建立独立失败样例，后续修复应让同案例先失败再通过 | 来源与保留 |
| S18-R2-097 | documentation-or-test-contract | G0/S8 | 受控AST交错不是线程压力测试；实现后补真实并发和HTTP回归 | 来源与保留 |
| S18-R2-098 | preservation | G0/S8 | 下载wheel仅源码检查不安装旧qwen-tts，避免命名空间冲突 | 来源与保留 |
| S18-R2-099 | documentation-or-test-contract | G0/S8 | 本轮100建议与实际实验范围完整入备忘录，不宣称全源三轮完成 | 来源与保留 |
| S18-R2-100 | preservation | G0/S8 | 第三轮结束及逐题50建议决策完成后才改产品，继续冻结17包与工作台 | 来源与保留 |
| S18-R3-001 | preservation | S6/S7 | 保留16码本、24kHz及1920样本每帧合同，不用未知解码器静默替代 | 生成码窗口 |
| S18-R3-002 | preservation | S6/S7 | 左上下文25帧只保留有界生成码，参考码继续禁止进入输出解码 | 生成码窗口 |
| S18-R3-003 | hardware-or-real-model-blocked | S6/S7 | 默认右前瞻0与实验1/2帧分别记录延迟与真实质量，不用随机codec推断最优 | 生成码窗口 |
| S18-R3-004 | documentation-or-test-contract | S6/S7 | 为每次提交记录全局帧偏移与已提交区间，定位接缝是否重复或漏帧 | 生成码窗口 |
| S18-R3-005 | documentation-or-test-contract | S6/S7 | 区分有效生成帧、保留上下文和待提交PCM，不能把重复解码时间当新语音 | 生成码窗口 |
| S18-R3-006 | preservation | S6/S7 | 取消和异常均close生成迭代器并清理pending，禁止取消后尾包泄漏 | 生成码窗口 |
| S18-R3-007 | preservation | S6/S7 | 实际tokenizer返回错误采样率、非有限值或长度不符继续拒绝 | 生成码窗口 |
| S18-R3-008 | hardware-or-real-model-blocked | S6/S7 | 按首2/4/8帧对照时固定后续策略与文本，不能混入候选或seed变化 | 生成码窗口 |
| S18-R3-009 | hardware-or-real-model-blocked | S6/S7 | 真实codec有限上下文与整段解码差值须用预训练权重另测，不凭因果结构宣布无接缝 | 生成码窗口 |
| S18-R3-010 | documentation-or-test-contract | S6/S7 | prepare_ms不含生成器首次next里的全部预填充，拆分前先验证时钟范围 | 生成码窗口 |
| S18-R3-011 | confirmed-defect-in-stated-scope | S3 | 将整块与不规则分块输出一致性列为DSP算法合同而非只检查有限和长度 | DSP ABI |
| S18-R3-012 | confirmed-defect-in-stated-scope | S3 | NumPy淡入使用固定总长度及已处理位置，不让每次短块重新从零起算 | DSP ABI |
| S18-R3-013 | pending-evidence | S3 | NumPy RMS统计保留不足10ms余数，避免按来包边界重新分组 | DSP ABI |
| S18-R3-014 | pending-evidence | S3 | Rust逐样本平滑与NumPy插值应先定义相同算法再设合理量化容差 | DSP ABI |
| S18-R3-015 | documentation-or-test-contract | S3 | flush后Rust清DC状态而NumPy不清的差别须明确，不能称API语义完全一致 | DSP ABI |
| S18-R3-016 | preservation | S3 | 当前Worker每段重建leveler，不能将跨段复用API问题直接认定为生产根因 | DSP ABI |
| S18-R3-017 | hardware-or-real-model-blocked | S3 | 固定目标电平与最大增益仍不保证两段动态响度相同，保留完整语音测量 | DSP ABI |
| S18-R3-018 | pending-evidence | S3 | 纯静音、阶跃和有声转静音须同时检查滤波残留、削波和增益泵动 | DSP ABI |
| S18-R3-019 | documentation-or-test-contract | S3 | Rust ABI加载需区分不兼容符号和库缺失，不能失败后不告知回退路径 | DSP ABI |
| S18-R3-020 | preservation | S3 | 缺Rust编译器时记录未执行，不用C++重写参考实现冒Rust实测 | DSP ABI |
| S18-R3-021 | confirmed-defect-in-stated-scope | S4 | 120样本以下语音块不能因无完整RMS帧就直接丢弃，设计跨块累积 | 裁剪终止 |
| S18-R3-022 | confirmed-defect-in-stated-scope | S4 | 跨输入块保留35ms有界预滚，而非只在检测到声音的当前块向前取 | 裁剪终止 |
| S18-R3-023 | preservation | S4 | 候选静音与未发声辅音不能仅凭能量绝对区分，试听门禁保留 | 裁剪终止 |
| S18-R3-024 | confirmed-defect-in-stated-scope | S4 | 短末块含有非零语音时须有明确finish策略，不能永久留held后销毁 | 裁剪终止 |
| S18-R3-025 | documentation-or-test-contract | S4 | 尾静音裁剪应记录实际删掉时长和阈值，不把删音频冒首声或RTF提速 | 裁剪终止 |
| S18-R3-026 | documentation-or-test-contract | S4 | 900ms超长首静音放行应保留异常说明，不能把放行静音算实际人声 | 裁剪终止 |
| S18-R3-027 | preservation | S4 | 1800ms held上限必须在长无声生成时仍有界，不引入全句缓冲 | 裁剪终止 |
| S18-R3-028 | preservation | S4 | 输入codec固定1920样本倍数与泛用小块测试分开，标注生产可达性 | 裁剪终止 |
| S18-R3-029 | documentation-or-test-contract | S4 | 裁剪器发出的样本索引需可追溯至模型原始PCM，便于核对漏音 | 裁剪终止 |
| S18-R3-030 | hardware-or-real-model-blocked | S4 | 输入很轻时不要单纯升高裁剪阈值，应比较失真与背景噪声的权衡 | 裁剪终止 |
| S18-R3-031 | preservation | S5 | 保持流式相位和上一个输入样本跨PCM帧连续，不能每帧独立插值 | 重采样收尾 |
| S18-R3-032 | documentation-or-test-contract | S5 | 24k直通与44.1k/48k转换各自验证输入时长和输出样本预算 | 重采样收尾 |
| S18-R3-033 | documentation-or-test-contract | S5 | 终止时缺下一个插值端点应定义末样本延拓或明确短尾策略并测试 | 重采样收尾 |
| S18-R3-034 | preservation | S5 | 重采样收尾不能以补充可计入speech的静音改变RTF分母 | 重采样收尾 |
| S18-R3-035 | preservation | S5 | 每段协议标记不应重置同一朗读流的重采样相位，会制造边界跳变 | 重采样收尾 |
| S18-R3-036 | preservation | S5 | 锁定、取消和新流begin应清掉上一任务的相位及延迟端点 | 重采样收尾 |
| S18-R3-037 | preservation | S5 | 分块与整块重采样在数值容差内一致的现有行为应保留 | 重采样收尾 |
| S18-R3-038 | documentation-or-test-contract | S5 | 一输入样本、空块及极短末块需测试，不只测长整秒波形 | 重采样收尾 |
| S18-R3-039 | hardware-or-real-model-blocked | S5 | 扩展至降采样时需考虑抗混叠，不能将线性插值叫任意采样率高保真 | 重采样收尾 |
| S18-R3-040 | hardware-or-real-model-blocked | S5 | 实体浏览器实际采样率与请求24k可能不同，诊断记录两者 | 重采样收尾 |
| S18-R3-041 | confirmed-defect-in-stated-scope | S5 | 生成结束且剩余20ms音频应有播放或明确失败结果，不能永久buffering | 完成短尾状态 |
| S18-R3-042 | confirmed-defect-in-stated-scope | S5 | 精确50ms边界的严格大于判断需单独测试，不能只测51ms | 完成短尾状态 |
| S18-R3-043 | confirmed-defect-in-stated-scope | S5 | 欠载恢复时最后短尾同样应可排空，避免截掉最后一个音节 | 完成短尾状态 |
| S18-R3-044 | preservation | S5 | 已结束数据的排空政策与持续生成时风险缓冲分开，不盲降正常启动阈值 | 完成短尾状态 |
| S18-R3-045 | documentation-or-test-contract | S5 | 有剩余样本但低于阈值时ended判定须有终止路径，不假装已播完 | 完成短尾状态 |
| S18-R3-046 | documentation-or-test-contract | S5 | 一任务只能产生一次最终结束，迟到统计消息不能把ended改回playing | 完成短尾状态 |
| S18-R3-047 | hardware-or-real-model-blocked | S5 | 长网络抖动和低产出速率下测试启动等待与欠载率成对取舍 | 完成短尾状态 |
| S18-R3-048 | hardware-or-real-model-blocked | S5 | 暂停恢复必须在用户授权AudioContext状态下执行，不自动规避浏览器策略 | 完成短尾状态 |
| S18-R3-049 | documentation-or-test-contract | S5 | 单调时钟中的0值不宜兼任未记录标记，检查极早首包的时间哨兵 | 完成短尾状态 |
| S18-R3-050 | preservation | S5 | 运行原播放器VM只能证明逻辑，不可声称浏览器硬件首声变快 | 完成短尾状态 |
| S18-R3-051 | documentation-or-test-contract | S5/S6 | firstPlayedMs目前是主线程play命令时刻，名称与报表需区分实际消费 | Worklet时钟 |
| S18-R3-052 | hardware-or-real-model-blocked | S5/S6 | 增加首样本消费确认前先定义是否跳过显式停顿和极小淡入样本 | Worklet时钟 |
| S18-R3-053 | hardware-or-real-model-blocked | S5/S6 | Worklet currentFrame与主线程performance属于不同时间轴，使用可解释映射 | Worklet时钟 |
| S18-R3-054 | preservation | S5/S6 | 保留ring样本计数与自然结束不额外记欠载的已通过行为 | Worklet时钟 |
| S18-R3-055 | preservation | S5/S6 | 欠载只计一次直至恢复，避免每个渲染量子重复放大统计 | Worklet时钟 |
| S18-R3-056 | documentation-or-test-contract | S5/S6 | 容量溢出dropped必须进入上层状态和失败提示，不能只在底层计数 | Worklet时钟 |
| S18-R3-057 | hardware-or-real-model-blocked | S5/S6 | 固定192样本淡入在24k/48k分别8/4ms，若要求同毫秒则按实际率配置 | Worklet时钟 |
| S18-R3-058 | preservation | S5/S6 | hold与reset后无旧PCM回放，保留现有重置后精确零输出测试 | Worklet时钟 |
| S18-R3-059 | documentation-or-test-contract | S5/S6 | 环形缓冲溢出属于丢样，不得被统计成已自然连续读完 | Worklet时钟 |
| S18-R3-060 | preservation | S5/S6 | 声卡/系统输出延迟仍需实体设备测量，Worklet消费也不是声学听到时间 | Worklet时钟 |
| S18-R3-061 | documentation-or-test-contract | S6 | 规划器PauseBeforeMs由上一边界生成，逐段记录而不是把所有停顿归模型 | 停顿顺序重试 |
| S18-R3-062 | documentation-or-test-contract | S6 | Worker默认只加显式lead pause，核实tail默认0后再判断重复停顿 | 停顿顺序重试 |
| S18-R3-063 | preservation | S6 | 保留首段零规划停顿，不以参考呼吸或原音占位提前出包 | 停顿顺序重试 |
| S18-R3-064 | hardware-or-real-model-blocked | S6 | 模型内部停顿与规划停顿叠加需实际WAV分层对照，不能只删规划停顿 | 停顿顺序重试 |
| S18-R3-065 | preservation | S6 | 有序转发必须保留，不能为了最快包先播后一GPU导致错序 | 停顿顺序重试 |
| S18-R3-066 | preservation | S6 | 已消费部分PCM后禁止跨卡整段重试，保护不重复词句的现有门禁 | 停顿顺序重试 |
| S18-R3-067 | documentation-or-test-contract | S6 | 未消费重试时正确扣除旧produced样本，维持背压与统计一致 | 停顿顺序重试 |
| S18-R3-068 | hardware-or-real-model-blocked | S6 | first_worker_audio可能是显式静音包，报表不可直接称人声首包 | 停顿顺序重试 |
| S18-R3-069 | hardware-or-real-model-blocked | S6 | 第一段4帧与后段6/8/12帧策略保留可追溯，提速不得改变音色条件 | 停顿顺序重试 |
| S18-R3-070 | documentation-or-test-contract | S6 | 正文保留、引号配对、小数和缩写拆分须有实际Go回归，不靠源码注释 | 停顿顺序重试 |
| S18-R3-071 | preservation | G0/resource/acoustic | 在线推理与离线训练GPU租约保持互斥，不为测试盲停驻留模型 | 训练资源安全 |
| S18-R3-072 | hardware-or-real-model-blocked | G0/resource/acoustic | 真实双卡训练、引用缓存与profile建档继续分开报告，避免功能混淆 | 训练资源安全 |
| S18-R3-073 | preservation | G0/resource/acoustic | 子进程继续清除API与认证秘密环境变量，不因性能诊断泄漏 | 训练资源安全 |
| S18-R3-074 | preservation | G0/resource/acoustic | 模型与adapter来源hash及安全权重格式不能为快速加载而跳过 | 训练资源安全 |
| S18-R3-075 | hardware-or-real-model-blocked | G0/resource/acoustic | 训练数据审阅/完整覆盖与声学验收是独立缺口，18音频修复不自动解决 | 训练资源安全 |
| S18-R3-076 | preservation | G0/resource/acoustic | 取消训练只终止本次进程组，不根据旧PID文件杀其他进程 | 训练资源安全 |
| S18-R3-077 | preservation | G0/resource/acoustic | 保留离线代码与模型指纹核验，不自动开启远程代码或下载权重 | 训练资源安全 |
| S18-R3-078 | preservation | G0/resource/acoustic | 新增诊断原始WAV默认私有且关闭，不能进入公开Git和自动备份 | 训练资源安全 |
| S18-R3-079 | preservation | G0/resource/acoustic | 资源状态的CPU成功不标CUDA或GPU优化成功，尤其是当前无Torch环境 | 训练资源安全 |
| S18-R3-080 | documentation-or-test-contract | G0/resource/acoustic | 剩余复杂训练/恢复路径只有入口边界复核，明确语义深审仍需补齐 | 训练资源安全 |
| S18-R3-081 | preservation | G0/S8 | 正式工作台继续只读核对，不因音频审查改写15文件或HEAD | 交付安全 |
| S18-R3-082 | preservation | G0/S8 | 自命名空白文件、用户粘贴、并发版本冲突和磁盘持久化需保留 | 交付安全 |
| S18-R3-083 | documentation-or-test-contract | G0/S8 | 复制预览与正式工作台分别核对，不能用旧17复制成功冒18完整包成功 | 交付安全 |
| S18-R3-084 | documentation-or-test-contract | G0/S8 | 新发布前固定launcher字节数/hash，并校验53以上实际资产完整性 | 交付安全 |
| S18-R3-085 | preservation | G0/S8 | 剪贴板失败回退应选中完整源代码，不能只复制可见窗口 | 交付安全 |
| S18-R3-086 | preservation | G0/S8 | 文件名、路径穿越、脚本/style闭合注入等既有浏览器测试继续执行 | 交付安全 |
| S18-R3-087 | preservation | G0/S8 | 锁定清理、同源token和迟到响应隔离不能被新指标消息绕过 | 交付安全 |
| S18-R3-088 | preservation | G0/S8 | 旧验证脚本固定历史分支属于历史证据，新分支另建验证器而非改旧收据 | 交付安全 |
| S18-R3-089 | preservation | G0/S8 | 新工具依赖留忽略目录，下载源码也不与模型权重混入发布资产 | 交付安全 |
| S18-R3-090 | preservation | G0/S8 | 所有未执行的Go/Rust/真实浏览器/完整模型实验明确标未执行 | 交付安全 |
| S18-R3-091 | preservation | G0/S8 | 完整manifest读取/hash/AST只证明库存与语法，不声明全源逐行语义无错 | 证据与决策 |
| S18-R3-092 | preservation | G0/S8 | 三轮专题各100完成也不等于所有代码已语义审查三遍，覆盖缺口单列 | 证据与决策 |
| S18-R3-093 | documentation-or-test-contract | G0/S8 | 每个实验写方法、注入边界、实际源hash及探针hash，避免不同版本混算 | 证据与决策 |
| S18-R3-094 | documentation-or-test-contract | G0/S8 | 将已复现缺陷、待验证假设与保留保护分别分类，不将300建议全标已修 | 证据与决策 |
| S18-R3-095 | preservation | G0/S8 | 重建环境仅NumPy和Node时旧模型实验收据保留历史，不算新执行 | 证据与决策 |
| S18-R3-096 | preservation | G0/S8 | 第25题起一次一题，具体选项/推荐/理由/50建议全部记录后再下一题 | 证据与决策 |
| S18-R3-097 | documentation-or-test-contract | G0/S8 | 实施方案要将首声、条件来源、状态一致、DSP、裁剪、播放排空分成可回滚小步 | 证据与决策 |
| S18-R3-098 | preservation | G0/S8 | 产品最终源码冻结后完整三轮回归，当前边界探针不能代替全功能通过 | 证据与决策 |
| S18-R3-099 | preservation | G0/S8 | 零噪声/单一音色/自然朗读及RTF0.3仍需真实WAV和双T4，不用绝对承诺替代 | 证据与决策 |
| S18-R3-100 | preservation | G0/S8 | 第三轮备忘录和缺口完整内嵌提示词，发布18之前仍使用17并保持PARTIAL | 证据与决策 |

详见`validation/step18/g0-recommendation-disposition.json`中的原来源、处置理由、已有关联证据和待执行测试合同。无条目标记修复完成或最终签收。
