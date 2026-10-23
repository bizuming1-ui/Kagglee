# 第十五阶段：参考隔离、首句调度、增响与创建成本审查

日期2026-10-22。**工程实现已完成本轮选定范围，真实Qwen/T4音质与性能仍BLOCKED；不是全部用户需求完成。**

## 用户证据与根因边界
用户提供step14实际网页截图：BZM档案可见、候选6.3/6.4秒、创建日志256.4秒，报告克隆播放中插入原参考录音。截图不包含输出音频、GPU显存与分阶段耗时，所以不能确定这次具体是参考呼吸、ICL串音、模型幻觉或别的声学现象。

查阅实际PyPI Faster0.5.4 wheel的model.py，SHA256 `7d45740b805bb1a4798fbe20ffd580e2a35361e744c4645da106c2b6383d4de2`：ICL模式将ref_codes放入声学解码上下文，再裁去参考部分；上游xvec_only说明明确针对phoneme bleed-through。旧worker三个调用点均xvec_only=False。另有QTTS_BREATH_MODE=reference的显式参考呼吸拼接路径。当前14默认off不能证明该用户开启了reference，不能以存在这条路径就宣布确切根因已证实。

## 本轮实际改动
### 1. 强隔离生成
- worker.RealEngine档案加载、dtype回退预热、正式流式生成统一xvec_only=True、ref_text为空、append_silence=False。参考文件仅用于提取说话人向量，不向Faster ICL提供参考文本/声学码。
- Worker不再读取breath_files，不论旧环境reference设置如何，lead_audio只返回有界零停顿。没有参考音频低延迟占位或失败时回放参考的路径。
- stats使用reference_pcm_splicing=false描述代码策略，acoustic_text_verified仍false。模型自身呼吸不滤除，不能据此保证没有生成幻觉或逐字完全一致。
- 向量模式会改变ICL条件；韵律、口音、音色相似度可能变化，必须真实试听，不称无损切换或已有质量提升。

### 2. 首句调度
- Go新增LiveSegCfg，仅聊天首段使用。完整中文句末、问叹号及达到首段7units的分句不再要求下一delta；短完整句可首发，尾部空格同样处理。
- ASCII点仍等lookahead，避免12.50被拆成12.；未闭合引号/括号保持等待。普通朗读仍ExactSegCfg，后续段和取消、两GPU调度、有序转发、背压、播放器水位不变。
- 没有每token发TTS，LLM尚无确定边界时仍可能积累到FirstMax。纯标点/空白片段仍沿旧过滤，文本分段不是声学ASR核验。
- 实际本地HTTP/SSE实验让LLM尾巴阻塞，观察首段已进入真实scheduler并被HTTP worker fixture接收，再释放LLM尾巴。不是远程DeepSeek或Qwen速度证据。

### 3. 有界增响
- qtts_common.output_target_dbfs共享解析，默认-18dBFS，允许QTTS_OUTPUT_DBFS=-24..-14，非法/非有限回退-18。
- 旧、新档案重新加载时统一使用该输出目标及最大增益12dB（旧9dB），不修改原始录音；保留Rust/NumPy DC blocker、增益平滑、软限幅、淡入淡出。
- 低电平合成正弦验证目标效果及限幅；并非任意语音、静音或硬件音量都会增加恰好3dB，也不是响度LUFS认证。

### 4. 创建成本与正确性
- 网页直建、库处理、后端缺省均关闭可选GPU候选校准；手动按钮和显式勾选保留。不是偷偷删除全部质量模型，不把减少可选校准称质量等价证明。
- CPU Whisper允许跨任务复用同一个模型；QTTS_ASR_KEEP_CPU=0恢复释放；CUDA ASR仍卸载，避免与TTS争VRAM。ASR改RLock保护加载、完整惰性转写及释放；并发回归确认迭代结束前不能释放模型。保留large-v3、beam5、词时间戳与全录音处理，未靠降低识别质量提速。
- 构建局部嵌入缓存按float32样本内容SHA256去重，最多64条、每向量≤16KiB；不持久化录音或向量缓存、不跨声音任务复用。保留24候选、评分公式和最佳锚点准确F0。
- quality.stage_ms记录speaker_load/decode_denoise/asr/candidate_scoring/prosody_analysis/worker_load/optional_calibration；build_s与embedding_cache最终写回profile，页面可以展开查看。重新读取校准后的profile再合并quality，避免覆盖校准选择。
- 修复候选回退截前14秒却配整段文字的问题；仅允许完整2.5–16秒对齐片段，过长不猜切分、明确拒绝。可信手动16秒全文不再被截14秒。这是必要的安全拒绝，不是所有长ASR片段现在都自动可用。
- 首次下载/CPU大模型ASR与ECAPA/F0仍可能很慢；没有拿用户原录音做A/B，不能声称256.4秒已降到某个数值或“大幅提速已实测”。

## 为什么不每张T4放两个1.7B
纯参数1.7e9×2字节约3.4GB/份（十进制），两份约6.8GB；不是整个进程显存。codec、speaker、KV、CUDA graphs、临时张量和碎片另计；同时执行共享同一张T4的计算和带宽。装得下不等于单请求更快，额外副本也可能OOM/恶化首声。当前保持两T4各一模型，用两卡并行相邻段。没有双副本T4实测，不报告可装下或收益。

## 三轮检查与建议处置
REVIEW1/2/3各100项，前置review-before.json记录三次全源文件读取/哈希/Python AST，不是逐行语义正确证明。DECISIONS问题16/17/18顺序展开，每题50建议；累计18题900建议。300条逐项处置见review-disposition.json，区分implemented/preserved/documented-boundary/requires-hardware/not-implemented，不把建议数量当修复数。

## 验证结果（最终计数以final-checks.json为准）
- Python全量301项×3、Node30项×3、Go race count3；新16项隔离/音量/创建成本单测。
- 完整Chromium120项×3=360项在修正等义文案断言后全部通过（10.5分钟），最终完整包剪贴板另3轮通过；独立复制页剪贴板、下载、权限拒绝全选、375px三轮通过。初次357通过/3文案失败日志保留，不隐去。
- 实际Faster0.5.4 resolver→prepare_generation→两阶段streaming控制流三轮，每轮chunk2/4/8，经过生产RealEngine包装；CPU prompt、talker算子与codec为明确注入fixture，40帧/76800样本完整，参考码入decoder为0。不是完整Qwen语音模型。
- 实际完整Faster/Qwen库导入+2651参数tiny Mimi构造/保存/重载三轮通过；强制HF RoPE CPU preflight三轮通过，整体因无CUDA为blocked。
- ownership/input HTTP/codes CLI/mock pipeline/真实本地Go+HTTP+SSE adapter/fatal进程脚本各含三轮，全部三轮通过，结果见收据。
- frozen13与当前实际训练源码CPU tiny LoRA A/B另做三进程×三epoch/6步，loss/全部adapter逐位相同；tokenize12→3。墙钟含冷优化器启动/顺序偏差，不能报告训练倍速或Qwen质量。
- 正式3000项目15文件/revision和原始至14打包件哈希不变。独立3001提供step15完整代码，非Python在线执行器。

## 本轮发现的初始失败，未隐去
1. 验证环境初次启动先重建venv、但日志目录尚未创建，重定向失败exit1；创建目录后安装成功，非产品bug。
2. 初版增响测试发现同一9dB最大增益使很小信号两种目标都饱和于同一上限，无法变响；worker最大增益改为有界12dB，保留软限幅并验证通过。不能只改测试阈值掩盖。
3. 首段HTTP实验最初直接从Session.jobs取任务，早于Scheduler.Submit填写enq，race报错；改为真实scheduler队列锁下pickLocked，避免测试绕过生产同步。最终race三轮通过；此处是新测试夹具错误，没有无依据修改生产锁。
4. 补充首句带尾部空格的边界用例，并同步修复第二处lookahead等待。
5. 初次完整浏览器三轮357通过、3失败，均为旧用例要求“网页训练执行尚未闭环”但新版等义文案为“网页训练尚未闭环”；断言兼容可选“执行”，仍强制展示未闭环，不删除门禁。原日志browser-initial-repeat3.txt保留，完整三轮重跑。
6. CPU驻留复核发现原ASR锁只护加载，惰性转写与释放可能并发；改可重入锁覆盖整个使用周期，并发门禁通过，重新执行三轮全量Python和协议。
7. 交接刷新脚本从39备忘录移植时剩余一个unique数量断言未改，最初assert失败；改为45，完整内嵌及逐篇读回验证，不影响产品包。
8. 首次最终汇总校验器错误地假定协议日志只有3条JSON；输入HTTP含另一组库HTTP收据、adapter含独立损坏拒绝收据。按收据字段/round筛选三轮，并额外强制检查库HTTP与损坏adapter无PCM回退，不删除任何真实失败检查。初始校验器失败日志已保存。

## 保留阻塞
真实Qwen/T4三轮生成、参考重播排查试听、向量模式相似度、真实首播/欠载A/B、首次/热创建同录音A/B、Rust现场DSP和每卡双副本显存/吞吐未验收。没有访问用户GPU和原音频，不可模拟填成功。

历史网页真实训练控制面/维护租约移交/start-cancel-restore-publish、长数据审核对齐/超过16样本完整覆盖、真实训练保质吞吐、严格声学逐字拒播仍未实现/未验收；本轮不是对这些要求的豁免。整体状态PARTIAL/BLOCKED。
