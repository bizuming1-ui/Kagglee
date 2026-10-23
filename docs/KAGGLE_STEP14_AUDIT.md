# 第十四阶段审查：已实现边界与未完成门禁

## 不能写成“用户全部需求已完成”

| 需求 | 本轮代码/证据 | 尚未完成 |
|---|---|---|
| 连续十多分钟录音 | 约20分钟/8192块/64MiB单文件，服务端1200秒；11分钟虚拟控制与完整合成PCM解码验证 | 物理麦克风、休眠/后台冻结和真实长语音采集 |
| 保质提速 | 冻结step13真实CPU小LoRA A/B，loss/更新/参数逐位一致；重复tokenize从12次到3次 | Qwen/T4吞吐、峰值显存、相同数据训练音质A/B |
| 网页点击真实训练 | 原真实双rank训练CLI保留，快照明确不训练 | 独立CPU控制面、维护态租约交接、网页启动/取消/进度/恢复服务及训练后发布闭环 |
| 自然呼吸 | 默认不后加呼吸，reference模式只有真实片段，无合成噪声回退 | 模型自身气声、呼吸自然度与音色实听 |
| 首声更快 | 区分模型首块与裁边后首个非空PCM；可选首段chunk=2实验 | 未保证首播更快；真实T4端到端首播/欠载A/B |
| 文本完全一致 | 实际会话不再CleanDelta清理正文或补句号；多delta原文连接测试 | 没有逐句ASR核验/拒播闭环，不保证模型无漏字添字；纯标点/纯空白片段仍按旧规则过滤 |

step13用户现场已通过双T4加载/预热/ready门禁；不应再把此前双GPU启动说成完全未知。但上述新增目标仍不能从那次日志推出成功。

## 三轮审查/自问自答

REVIEW1/2/3各100条建议，完整源结构/哈希见review-before.json；重点逐链路审查，不宣称逐行无错或300项全部修复。问题13→50建议→问题14→50建议→问题15→50建议已按顺序记录。共15题750建议。处置表review-disposition.json区分本轮实现、原有回归保留、未闭环/待真实硬件；完整目标清单仍22/300。

## 具体改动

1. recorder默认1199000ms，8192 chunks，64MiB单文件、127MiB本地合计。UploadLimits默认1200秒单段、1800秒合计、128MiB请求、64MiB文件；Go上传上限同步128MiB，浏览器上传检查同步。原始库仍64MiB/库/512MiB总体，其他独立预算仍可先触发；不是无限录音或所有编码格式都能存满20分钟。上传超过限制拒绝，原件不截断。训练快照仍保留短段及序列预算，不能把长参考直接送入SFT。
2. TTSDataset深拷贝输入冻结调用者来源；64MiB有界CPU text/code tensor缓存，超过预算回退旧计算，不裁切不替换样本。返回clone避免缓存被调用者改坏，reference mel只读契约不变。run_rank保留逐样本准入，记录tokenizer_calls/cache_hits/cache_bytes。
3. 训练梯度finite flags在同一设备合并后一次host读取，跨rank collective与loss/accumulation/clipping/AdamW不变。HF/官方训练元数据查询兼容修复，不再在HF成功训练末尾查询不存在的官方发行包而报错。
4. Go实际newSession使用ExactSegCfg；不逐delta清洗markdown/URL/emoji、不合并内部空格、不添加句末标点。DefaultSegCfg/CleanDelta留给显式历史契约测试。不能因此说模型发音与文字已完全相同。
5. Worker默认QTTS_BREATH_MODE=off；reference模式只使用真实bank，空bank返回安静pause，删除合成breath噪声兜底。保留模型原声与淡入淡出，不盲滤气声/辅音。
6. model_first_chunk_ms与first_chunk_ms分别记录；后者从裁边后非空PCM才开始，不把被裁掉的空片段算首声。注意旧EdgeTrimmer在runaway静音时可放行静音并标异常，非空PCM不等于ASR确认的人声/真实首播。前端first_played与欠载保持，acoustic_text_verified=False。QTTS_FIRST_CHUNK_SIZE可选2..8，默认4不变，不通过降低播放器稳定阈值美化延迟。
7. 语言分工仍Python/PyTorch+CUDA、Go、Rust和浏览器JS；没有目标机数据就不引入新语言/自定义C++内核或高风险BF16/FA2/compile开关。

## 实验与证据

- test_step14新增12项：长解码/独立预算、录音≠训练、默认无呼吸、真实呼吸无噪声回退、非空PCM计时、缓存张量/优化器参数等价、字节上限/隔离、梯度finite/HF发行。
- training_cache_check.py加载冻结step13的真实训练与dataset源，不以重写基线代替。三独立CPU进程，每次同数据/seed，三epoch共6次optimizer更新，两路径loss与所有adapter tensor逐位一致；tokenizer调用12→3。只报告减少重复调用，fixture墙钟包含冷启动与执行顺序偏差，不能据此宣称端到端倍速或质量提高。
- 虚拟浏览器11分钟与2640块继续录音/约20分钟自动停止；合成660秒24k PCM解码长度完整。都不是真实麦克风/真人声音实验。
- 保留真实完整Faster/Qwen导入与微型Mimi构造/保存/重载三进程，保护已成功RoPE路径；不是Qwen1.7B训练或T4实验。
- 三轮完整Python285×3=855 PASS，Node30×3=90 PASS，Go race count3 PASS；资源所有权真实进程/输入HTTP/本地码CLI/Mock管线/Go+SSE+双worker adapter替身各三轮、fatal真实supervisor+CPU worker三轮PASS。
- 浏览器117×3=351 PASS（10.4分钟），最终step14整包逐字节复制另3 PASS。独立3001复制页真实Chromium三轮剪贴板/下载精确、授权拒绝全选/375px手机无横向溢出、正式15文件不变PASS。见copy-page.json与final-checks.json。
- 这些通过项仅覆盖实现范围，整体用户需求仍PARTIAL/BLOCKED。

## 初始记录

恢复会话后依赖缓存/venv不在，测试环境按现有测试锁恢复，未写进生产包/未改变Kaggle平台Torch。首个Go测试从仓库根运行找不到go.mod，改在真实go/gateway目录执行后通过；未改源码去适配错误目录。初检记录保留。全量失败若有，必须保留而不是只删测试。

## 下一步必须做而非继续虚报

优先实现网页训练的独立CPU控制面与维护态：网关/状态服务不能随GPU服务退出；停止并确认所有GPU持有者、传递可验证租约、固定实际数据/Base/码版本、真实两rank训练、受控取消/恢复、候选发布/明确切换。需要本地物化Base与审核过的逐段转写，不能猜这些信息或自动拿用户音频权利作假确认。真实首声、质量与声学一致性需相同参考/文本/种子A/B和试听，验收前本阶段整体需求状态为PARTIAL/BLOCKED，不得输出全部成功。

## 长数据覆盖补充门禁

现有训练快照仍最多16条；若高质量切分产生更多片段，还需扩展受限分片/manifest与完整样本覆盖后才能全部入训，不能只选前16条冒充完整十分钟训练。

## 最终交付

step14为285094字节/48资产，SHA256 73a02a95919406c4570ea563f0c0475fdde17535e6ccd16764c32514fce2c369；repack可重现，原始至13冻结，正式15文件/HEAD不变。39完整备忘录、300建议处置、15题750建议均有独立核验；不提升真实质量/性能门禁。
