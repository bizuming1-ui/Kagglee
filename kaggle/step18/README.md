# 第18阶段隔离修复候选（未发布）

> 最新前端候选：`web/app.js`（S5完整脚本）；后端候选仍为S4 `worker_s4.py`。这是隔离源码，不是已发布完整18安装包。

> 最新受控worker候选为 `worker_s4.py`；S3 `worker.py` 留作原合同控制。默认正式入口未切换。

本目录是实际可导入／运行的候选分析服务和 worker/DSP 源码，不是测试内的函数替身，也不是完整18安装包。`analyst.py`从冻结17的分析服务复制后作最小修改，来源见`origin.json`；其余模块显式复用`../source/py`，冻结17和正式工作台未改。

## 本次已实现范围

- candidate/text接口严格UTF-8 JSON，精确单字段；拒绝重复／未知键、非对象、NaN/Infinity/溢出数值。
- index为非负整数，拒绝bool、float、字符串及缺省值；ref_text为有效Unicode字符串，去空白后1..20000字符。整个请求另有限额128KiB，因此较大的转义编码也可能413。
- HEAVY准入先于写盘；executor内重新核对档案／trained状态；取消时沿用原HeavyAdmission的实际工作完成后释放语义。
- 候选源仅安全单文件名、Linux no-follow/nonblocking普通文件、有界读取。未验证音频可解码／声学质量。
- 候选锚点按内容SHA命名，已有同内容复用；JSON提交失败不覆盖旧锚点，清理本次未提交文件。
- 候选／文本／删除短提交由有界进程内锁协调，网络加载不持锁。删除也经HEAVY，因此满额时可429。不是跨进程锁或完整档案事务。
- 保留worker pin和503/reference_saved语义；不代表实际双卡模型已加载。

## S2-A新增：校准快照与冲突

校准开始在短锁内捕获完整元数据、全部候选／当前锚点／质心字节；实际评估只读捕获内容，提交前在同一短锁内重新核验。候选／转写实际变化写入修订nonce，改回原值的ABA也冲突；完全相同的重复选择保持幂等。输入改变／删除／转为trained时409且不应用旧评分。同档案第二次校准409；不同档案可并行推进。每次运行使用独立、长度安全的临时ID，临时目录700，仅清理本次所有的目录；ASR释放移入finally。快照最多24候选、聚合文件64MiB，实际峰值内存还包含副本／重新核验，不能称总RSS仅64MiB。

这仍只是进程内乐观提交；外部／跨进程不遵守本锁的文件写入可能在最终检查之后再改变状态，不称完整全局事务。元数据nonce不是身份或模型质量指标。失败／冲突需要显式重试，不自动重复耗时GPU工作。

## S2-B新增：有效指标与加载就绪

逐目标记录seed、目标摘要、样本数／时长、指标、固定错误码和覆盖率。缺失为null；只有全部目标有有限ECAPA及ASR指标才排序，不再补CER0.05或全错chosen0。MFCC代理、坏／无质心及空／非法／全零PCM不冒可靠指标。无完整候选时422、chosen=null、reference_saved=false，不写盘并保留旧报告；一个候选失败不阻止另一个完整候选。仍只是相对排序，quality_verified=false，不加入未经实测的最短音或听感阈值。

临时worker先核验HTTP／严格ok／pin。选择先保存，再检查最终worker并重核保存版本；失败503/reference_saved=true/ready=false，保存后又改／删则saved_version_current=false说明历史曾提交而非当前还存在。成功HTTP200仅表示本次加载确认通过；成功报告仍与磁盘选择报告一致，不提前持久化就绪承诺。公共校准／worker错误使用固定码，可选后台校准记录摘要，但未完整执行真实创建流程。

原reload的其他调用者及跨进程事务、任意IO恢复、旧锚点GC、真实短音／声音质量／双T4／训练／性能仍未验收。最终S2-B证据见docs/KAGGLE_STEP18_S2_VALIDITY.md及progress-s2b.json，候选未发布、未部署。

## 手动启动（仅本地受控开发）

在仓库根目录、现有测试依赖环境中，可用独立临时状态启动mock服务：

```sh
QTTS_STATE="$PWD/.cache/step18-dev-state" QTTS_MOCK=1 QTTS_NO_RUST=1 \
  .venv/bin/python kaggle/step18/analyst.py
```

该服务沿用内部127.0.0.1:7010，不是公网预览，不应绕过正式Go鉴权代理暴露。命令不会安装模型或构成完整应用启动；真实模型／权重／资源租约仍要求完整启动环境，未在本批验证。默认17入口、下载／复制页和正式HEAD均未切换。

## 验证

`kaggle/tests/test_step18_profile_inputs.py`对本候选走真实Uvicorn环回TCP，worker/ASR/speaker/synth明确替身。`QTTS_S1_TARGET=frozen17`运行相同HTTP合同作为失败对照；FIFO阻塞路径和新executor/delete合同在旧版对照中明确skip，候选必须全部运行。

本批完整三轮结果见`docs/KAGGLE_STEP18_S1_CANDIDATE.md`及`docs/validation/step18/progress-s1-candidate.json`。旧450项仍验证冻结17，新增项验证本候选；不能把两者合计冒充完整新产品验收。整体G0／模型／双T4／训练／声音质量和性能仍PARTIAL/BLOCKED。

S2-A实际结果见`docs/KAGGLE_STEP18_S2_SNAPSHOT.md`及`docs/validation/step18/progress-s2.json`。旧450控制仍为冻结17；S1的28项已在当前S2候选上重跑，新增22项验证校准状态，不是完整模型实验。

## S3 新增：因果 NumPy DSP 与实际 worker 接入（未发布）

`step18_audio_rt.py` 实现独立候选 `numpy-causal-v1`；`worker.py` 显式使用唯一模块名，避免冻结 audio_rt 的 import 缓存。worker 全部命名函数/类 AST 与冻结17一致，只改模块导入和依赖搜索路径；真实 run_job/trimmer/frame 已用替身引擎接通并测试，不是仅新增闲置 helper。

- DC、固定 10ms RMS 平方和/余数、期望增益与逐样本 30ms/600ms 平滑跨调用保存。
- 淡入按整段绝对样本位置；process 每次立即输出同数量 int16，不等待 RMS 窗口，不改输入。
- `start_segment(fade_samples=None)` 默认原 4ms/至少8样本；可明确 0/1 样本。重启段只重置淡入。
- `flush(0)` 无副作用；正值输出指定合成衰减尾并清 DC/last，保留学习态；负/非整数/布尔长度拒绝。close 幂等，关闭后拒绝其他操作。
- 配置显式约束：整数采样率 8000..384000，target -40..-6dBFS、max gain 0..18dB、min gain -24..0dB，均有限；既有默认值保持。
- float32 输入、float64 标量状态、ties-to-even 量化。-46dB RMS gate 取精确幅度阈值，与旧 NumPy `0.005` 有微小语义变化；因果增益本身也会改变旧整段结果，不能称只修包络、听感不变。
- **本候选仅启用 NumPy。** 不自动使用 QTTS_RT_LIB 或未验收 Rust；冻结 Rust/ABI bridge 不改，无实际编译或数值等效证据，不签收完整 S3。没有新增降噪或参考 PCM 拼接。

受控开发启动候选 worker 示例（不是正式入口切换，不是完整应用启动）：

```sh
QTTS_STATE="$PWD/.cache/step18-worker-dev-state" QTTS_MOCK=1 QTTS_NO_RUST=1 \
  .venv/bin/python kaggle/step18/worker.py --gpu 0 --port 7001
```

默认仍是内部 127.0.0.1，不可直接公开绕过 Go 鉴权。这里的 MOCK 不加载真实模型，不能据此证明声音、双卡、首声或训练。裁剪器已知短块/末尾问题属于下一步 S4，仍未修；本次 DSP 输出守恒不等于整个 worker 端到端不丢样本。完整结果见 `docs/KAGGLE_STEP18_S3_DSP.md` / `progress-s3.json`。

## S4 新增：有界裁剪与显式结束（未发布）

`step18_trimmer.py` 使用从流开始对齐的120样本检测网格（24kHz下5ms），跨调用保存不足一格残帧、35ms前史和有界尾队列。正常finish按实际残帧长度检测，释放当前缓存全部非零尾，只能裁掉明确计数的精确零尾；取消/异常finish清空缓存，不追加192样本衰减尾或额外尾暂停。中间停顿与超出尾预算的数据按顺序输出，不靠删句内音频提速。最多保存keep前史、max_held尾及不足120残帧，队列分块复制不持有大输入数组。

实际入口 `worker_s4.py` 由S3 worker派生，只更换EdgeTrimmer导入及Worker.run_job；正常收尾真正调用finish，余数走同一DSP/计数/帧编码。取消后最后发帧前重查，诊断区分trim返回与取消后未发送样本；不宣称跨线程检查与声卡播放原子化。`stats.trim` 记录输入、返回、领先裁掉、精确零尾裁掉、取消丢弃与缓存及守恒结果；不是声学质量指标。

**保留限制**：低于阈值的领先历史仍可被裁掉（仅保留35ms前史），不保证全部弱辅音/低电平声音都保留；精确零政策也不是自然度证明。独立S3 worker/DSP及旧562合同不改，新40合同验证S4真实实现。旧probe仍检查冻结缺陷，不能当当前候选验收。

受控开发命令（内部端口、无模型，不绕过Go鉴权公开）：

```sh
QTTS_STATE="$PWD/.cache/step18-s4-dev-state" QTTS_MOCK=1 QTTS_NO_RUST=1 \
  .venv/bin/python kaggle/step18/worker_s4.py --gpu 0 --port 7001
```

此命令不是完整应用安装或18发布；参考状态分析服务与S3 NumPy DSP保持现有候选，Rust未启用。最终证据见 `docs/KAGGLE_STEP18_S4_TRIMMER.md` 和 `progress-s4.json`。下一步S5播放器结束短尾排空，真实首声/听感/训练/双T4仍未验收。

## S5 新增：完成短尾排空／重采样结束／流epoch

完整 `web/app.js` 从冻结17复制，仅替换Player P与嵌入Worklet V；网络解析器、到达预测器和整个UI后缀逐字节保留，UI实际实例化新Player。正式工作台/下载/默认前端均未切换，不是闲置helper也不是18整包发布。

- 完成后任何正pending（含1源样本、20/50ms和欠载恢复）可启动；未完成的风险缓冲阈值保留。
- pending按已post目标样本数−Worklet消费−明确溢出丢弃计算，陈旧fill0不会提前ended；终止需当前流endACK且pending=0。
- 内部epoch覆盖reset/pcm/play/hold/end/status，stop后迟到状态不复活，旧流状态不污染新begin；不改网络协议。
- 重采样使用全局整数输出坐标，线性插值分块等同整段。正常结束末样本保持，目标长度ceil(Nin*contextRate/24000)；取消不flush。一点保持是插值终端政策，不是参考语音拼接或增加worker speech/RTF分母。
- 奇数字节PCM拒绝，不静默吞尾；markDone幂等，已收到end后不再接收源PCM。保持旧firstPlayedMs是play命令时间，不改名冒实际声学首声。
- status新增queued/pending/dropped/epoch/endAck诊断；溢出仍显式计数，不能称普遍无损。测试只覆盖24k、44.1k、48k，不将线性插值称任意采样率抗混叠高保真。

`kaggle/tests/test_step18_playback.mjs`执行实际Player和Worklet VM；`tests/browser/step18-playback.spec.js`执行真实Chromium AudioContext/Worklet，含完整候选UI的合成HTTP链。浏览器是headless/muted，不是实体扬声器或实际模型。完整结果见 `docs/KAGGLE_STEP18_S5_PLAYBACK.md` 与 `progress-s5.json`。后续实际部署仍需完整鉴权Go/双T4/声学/包验收，不能把测试路由公开作为正式应用。
