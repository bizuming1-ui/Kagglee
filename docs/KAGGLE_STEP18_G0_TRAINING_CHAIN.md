# 第十八阶段G0第二批：训练数据、声码、原始库与发布链

## 当前结论

本批对12份、1974行源码完成第一遍全文语义阅读。加上第一批6份/930行，当前53资产中第一遍完整覆盖18份/2904行，剩35份尚未获得第一遍全文信用；完整第二/三遍签收仍为0。**这不是全源三遍完成，G0仍未通过。** 53资产外的仓库服务、生成器、测试与工作台也不能遗漏。

实际新增执行：135项CPU/文件/租约/进程内HTTP/安全张量格式专项，每轮失败0、错误0、跳过0，三轮一致；其中125项现有测试、10项新增artifact边界测试。另6项提供包元数据/构造器合同案例，各三轮。未执行完整Torch训练、完整Qwen、GPU、真实用户WAV、实际双T4、浏览器声卡或性能比较。

**新确证项：CPU声码编码器查询了不匹配的发行版名。** `training_codes.py:99`查询`qwen-tts`；项目固定运行栈则为`qwen-tts-hf==0.1.1.post1`，两者共享模块名但不是同一发行版。在HF元数据存在、旧发行版不存在且前置加载步骤成功的条件下，会抛PackageNotFoundError。重型加载步骤由显式fixture代替，版本查询来自真实wheel元数据；因此这是受控的提供包收据合同复现，不宣称完整编码器已经在目标环境运行。

产品源码/冻结包/正式工作台未改，未创建18。25–27题、300条原建议与第一批收据保留。此次新增发现另存`g0-training-chain-findings.json`，只关联原建议，不把300条历史建议重写成已修。

## 第一遍全文范围及语义结果

### 1. training_data.py：1–285

- canonical_wav先审RIFF总长、fmt/data唯一性、完整chunk和PCM16单声道24k，再作预算及常量拒绝；只规范容器，不自动重采样、截断或把强弱变化识别为语音。
- prepare要求权益/单人声明严格为true、逐样本转写、唯一ID和选中的参考；全局存储锁内获取原始库revision/lease，临时目录完整写入/verify后rename；异常BaseException清理。
- 单样本上限min(240秒,配置)，总输入min(900秒,配置)，参考≤16秒。长录音上传能力不等于可直接把一条20分钟音频训练；长数据拆分仍需正确逐段音文与用户数据审阅，不能按比例编造转写。
- manifest/jsonl/音频/分配计划独立hash，确切成员及租约保护；lease不长持全局锁，但阻止合作式删除。它证明内容/结构和来源声明，**不证明转写、权益、身份或训练质量**。
- rank_plan是数学分配说明；tts_training.epoch_indices才是运行时采样。两种算法不同不自动是错，但报告不能把前者当后者的执行轨迹。

### 2. training_codes.py：1–355

- 材料化本地tokenizer目录拒symlink/hardlink/pickle/auto_map和不安全shard映射；CPU/FP32/eager/offline加载，加载后检查24k、1920、16码本及2048词表。hash与结构不是权重质量证明。
- 每条声码帧数ceil(frames/1920)、16个严格整数、0..2047；处理每样本前后查取消，来源租约和全局代码锁内准备，临时目录异常清理，发布前复核输入/hash和取消。
- schema2封存原始manifest/jsonl，核对去掉audio_codes后的行、参考、逐样本hash；不是只有一个外部source_id。fixture始终test_only_codes，不能以“结构正确”升级为真实tokenization。
- lease/adopt用同inode/实际flock/共享描述符保护跨进程读；与训练admit及真实语义审核分开，不能把拿到FD当训练授权。
- **F01**：99行旧发行版版本查询不匹配HF栈；原测试`test_adapter_loader_contract_with_stub_imports_no_real_model`把所有metadata.version替换为stub-only，因此测试通过不能反驳此缺陷。`tts_training.provider_version`已有HF优先的轻量函数体可用于对照，但本步不修改或跨模块导入Torch来“快速修”。

### 3. voice_library.py：1–351

- 原始库与建档/训练分开；私有目录、普通文件/owner/nlink/NOFOLLOW/NONBLOCK、revision、字节预算、独立构建lease保留。重复字节内容去重不等于单说话人或音频语义去重。
- add先写独立样本，再原子JSON提交，失败移除新增文件；remove_sample先更新索引再清孤儿。_sweep只清允许的孤儿/临时文件，不递归删除独立profile。
- snapshot检查选中集合、revision、文件大小/hash，持续持有库lease；begin/finish另外维护reference_prepared/processing_failed；不能把这个状态称训练完成。
- list/get的busy只是合作锁观察，不是GPU占用。目录祖先/恶意同UID改动、跨进程崩溃一致性仍需后续第二/三遍与威胁边界复核，不能称文件系统绝对安全。

### 4. trained_profiles.py：1–155

- inspect核对完成记录、Base/codes/sample/LoRA绑定、两rank每epoch集合与更新记录；再校验真实safetensors字节hash、键/shape/float32/有限值及adapter摘要。
- 这些是**可信本地文件中的记录一致性**，没有硬件签名/执行证明。本批手写rank报告只用于验证拒绝/解析路径；即使describe返回training_execution_recorded，也不能拿它证明本批真的执行NCCL或优化器。
- publish需显式ack、来源代码租约、schema2真实编码状态、样本集合及唯一对应参考转写；临时目录完整写入并再次inspect后rename。它不会自动改变active，质量/推理重载继续false。
- 输出profile包含一份参考锚点和转写，属于现有profile备份范围；CLI确认说明此点。原始库、完整训练数据和adapter不因此进入自动Dataset备份。
- trained binding只允许显式trained后端，禁止Base/Mock静默回退；artifact pin是内容一致性，不是用户认证或声学评分。

### 5. tts_dataset.py：1–125；tts_training.py：1–200

- dataset深拷贝行、严格声码布局/范围、text token布局及max_sequence预算；超长样本报错而非截断。有界cache返回token/code克隆，参考mel共享；完整真实tokenizer与长数据适配仍需模型实验。
- collate保持独立text/codec mask、16码本与EOS标签；JointLoss在DDP.forward内部执行文本投影及talker/subtalker损失，不绕过DDP对参数的追踪。
- epoch_indices使两rank步数一致，奇数数量显式重复前缀而不drop_last；它不意味着绝不重复样本。梯度累积最后不足一组按实际group_size归一；跨rank有限值共识、溢出跳更新及摘要一致性检查。
- run_rank要求恰好两CUDA设备/NCCL，加载本地安全格式模型与固定speaker，所有样本长度先查后更新；训练结束核验参数变化/两rank摘要与模型来源。优化器/权重更新/保存的真实执行本批均未测。
- load_adapter不等于部署；不保存optimizer恢复状态，不能叫可精确断点续训。FP32 LoRA、FP16基础模型、真实吞吐/显存/质量权衡都不能由源码或CPU格式测试签收。

### 6. lora_adapter.py：1–91；adapter_engine.py：1–108

- 只选择talker及其code_predictor attention的q/v线性层，基础参数冻结，FP32 A/B；restore先全量校验再copy。prepare先构造全部替换，commit异常回滚，切换和生成必须由Worker同锁串行。
- trained引擎显式sentence-buffered；它传入保存speaker向量而不是ICL参考码，不能把它称Faster流式或默认单锚点ICL，也不能承诺改善首声。
- 每次_select重新读档案与固定artifact/来源；正确构建prompt后再提交adapter；输出检查24k/一条完整一维有限非零音频，取消会丢弃整句结果但不能抢占正在执行的CUDA kernel。
- Worker调用锁、两卡有效条件和真实输出仍须后续跨模块完整复核。源码相同/seed相同不证明两GPU声学同声。

### 7. qwen_compat.py：1–97；CLI三文件共207行

- 固定Faster0.5.4/HF0.1.1.post1/Transformers5.20.2；共享模块命名空间不能据此允许旧发行版并装。RoPE桥只认具体registry与default schema，不猜theta；配置smoke不是完整模型实验。
- encode_training.py 1–128：子进程离线CPU/清列举秘密；Linux父死SIGKILL及arming后ppid复查，bounded private报告，超时/取消只停本次进程组。SIGTERM/创建子进程竞态等完整生命周期还需后续第二/三遍覆盖，不能只凭注释签收。
- train_tts.py 1–49：参数预算与内部rank入口分离，公开错误脱敏；fingerprint不加载模型，未完成返回非成功。
- trained_voice.py 1–30：显式发布未验证候选，ack含参考锚点进入profile备份的说明；错误pin/来源不得静默替换。脚本可达不等于已经有UI真实训练按钮或实际训练数据。

## 本批执行方法与边界

### 135项专项×3轮

`run_training_chain_regressions.py`选择test_training_data、test_training_codes、test_code_provenance、test_libraries、test_qwen_compat与新增test_training_artifact_boundaries。每轮135通过、失败0/错误0/跳过0；这是子集，不是本阶段最终全功能三轮。

新增10项使用真实NumPy/safetensors序列化/解析：合成artifact合法解析、错误manifest pin、张量篡改、更新hash后仍拒非有限值、拒float64、每epoch覆盖缺失、无ack不inspect、fixture代码不能发布、禁止未训练后端回退、错误绑定ID/hash。rank报告明确手写fixture；未运行torch/LoRA计算/Gloo/NCCL/声学生成。

### 6项provider合同×3轮

`fetch_chain_metadata.py`从PyPI下载HF0.1.1.post1 wheel，SHA256固定`ed5b7aae64cf795243369fb5226173f459a45689ea86db1c6d3eb14fc0c2c01d`；仅提取METADATA至忽略.cache，不安装HF/旧Qwen，不导入其代码、不取权重。来源URL与METADATA hash见chain-provider-provenance.json。

`training_provider_probe.py`在独立进程限定sys.path，使metadata读取真实HF METADATA，确认旧发行版不存在；原编码器仅重型加载/桥接用fixture，随后真实版本查询按原码抛错。另证明宽泛版本stub会隐藏问题、错误模型pin在loader前拒绝、原训练provider_version函数体能识别HF，以及仅有元数据不满足运行栈门禁。**退出0表示复现到预期旧行为，不是编码器已修复。**

新增依赖只有忽略.venv中的safetensors0.6.2，用于真实NumPy格式测试；NumPy保持2.2.6。未安装Torch、Qwen发行版、模型权重或替换生产依赖。缺失.cache时按fetch工具重新获取经固定hash核验的元数据，不改历史round2收据。

## 后续门禁

1. 当前18/53仅是第一遍全文，另35资产及外围仓库、完整第二/三遍继续推进；不因本批测试数较多就通过G0。
2. 下一批优先Go安全/会话/调度及对应协议链，随后覆盖完整前端与启动恢复；跨链的Worker锁、训练CLI进程竞态也需复查。
3. F01加入后续最小修复/失败测试清单；不能安装旧qwen-tts来消除异常，不能使同模块命名空间冲突，不借修收据启用新模型或更改默认声音模式。
4. 300建议仍是初审映射、未逐条最终签收。全功能三轮、真实长数据训练、同文双卡及自然长文/无沙沙/首声/RTF≤0.3仍独立BLOCKED。
5. 25–27题不变，不机械追加问题28；若后续发现必须选择的新方案，再按一次一题、50建议规则记录。当前产品未改、18未生成，整体PARTIAL/BLOCKED。
