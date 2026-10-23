# 目标双T4验收门禁（待实际执行）

日期：2026-10-23。此文件是交接操作顺序，不是已有GPU实验结果。当前沙箱虽已装Torch供CPU测试，但没有可用CUDA/训练权重（实际Faster/HF已安装供CPU接口实验，不代表完整模型）、物理麦克风或DeepSeek通路；不得把本地CPU、Mock、界面截图或surface_preflight_passed填进真实实验结果栏。

## G0：保护基线与凭据

保留原始与step1/2/3/4/5/6/7/8/9/10/11包及SHA256。升级前先确认所有旧版本GPU进程停止，再解包到目标ROOT；资源锁只约束本版本合作进程，不能自动迁移旧服务。使用可丢弃的独立Kaggle会话，双T4、Internet On；依赖和模型revision尚未完整锁定，先审查安装流程，不在含无关凭据的环境执行。Kaggle Secret使用QTTS_ACCESS_TOKEN（32–256位非空格ASCII）与按需的HF_TOKEN/DEEPSEEK_API_KEY；不写进命令行、截图、共享日志或交接文件。

仅解包检查可在Notebook子进程中运行（脚本须先上传到当前目录）：

```python
import os, subprocess, sys
subprocess.run([sys.executable, 'kaggle-fixed-step17.py'], check=True,
    env={**os.environ, 'QTTS_UNPACK_ONLY':'1',
         'QTTS_ROOT':'/kaggle/working/qtts-step17-inspect'})
```

这是解包，不安装/下载/加载权重。不要把QTTS_UNPACK_ONLY留在完整启动环境中，避免把仅解包退出0误当模型成功。

## G1：先收集环境，再做表面探针

在目标Notebook记录实际GPU名称/数量、驱动、Python、Torch/CUDA版本、计算能力、总/空闲显存和磁盘。当前探针只记录总显存，不代替空闲显存测量。

完整启动前明确QTTS_MOCK=0、QTTS_DTYPE=fp16、禁用QTTS_ALLOW_SINGLE_GPU；首次建议QTTS_TUNNEL=none，暂不启公网隧道。必须在启动模型进程之前设置，事后在另一个shell里unset不会改变已经运行的Mock进程。

安装流程审查后，真实启动示例（会安装依赖和下载模型，当前沙箱没有执行）：

```python
import os, subprocess, sys
runtime_env={**os.environ, 'QTTS_MOCK':'0', 'QTTS_DTYPE':'fp16', 'QTTS_TUNNEL':'none'}
for key in ('QTTS_UNPACK_ONLY','QTTS_ALLOW_SINGLE_GPU'):
    runtime_env.pop(key,None)
subprocess.run([sys.executable,'kaggle-fixed-step17.py'],env=runtime_env,check=True)
```

默认ROOT=/kaggle/working/qtts；如果自定义QTTS_ROOT或QTTS_STATE，后续路径必须同步。启动失败时先保留STATE/backend_probe.json与脱敏错误类别，不重复安装/重试掩盖失败。

运行时探针独立复现：

```bash
python /kaggle/working/qtts/tools/backend_probe.py --runtime --expected-gpus 2 --dtype fp16 --timeout 120 --output /kaggle/working/qtts/state/backend_probe.json
```

退出2=阻断/仅检查；退出0=设备与API调用形状通过。后者仍没有加载权重，四个model/inference/training/performance验证标志均为false；**kwargs能接收参数不证明内部语义，SDPA/CUDA Graph/精度稳定性还需实际推理。

## G2：证明不是Mock，再做最小真实推理

启动后在Notebook本机用受认证的GET /api/health、/api/workers检查两个worker的健康详情，记录engine=faster-qwen3-tts、dtype=fp16、GPU编号0与1。`ok:true`、HTTP200、两个端口或模拟正弦PCM都不足以证明真实模型。worker /health不应被公网直接暴露。

使用合法同说话人的短WAV参考，自己命名声音库，提供与锚点逐字匹配的文本；没有文本的样本另测真实ASR，不把ASR失败伪装为成功。创建与启用声音档案只准备缓存，**不是训练**。

既有工具的参数已对照源码，声音档案创建后可运行：

```bash
python /kaggle/working/qtts/tools/selftest.py
python /kaggle/working/qtts/tools/e2e_check.py --url http://127.0.0.1:7860 --mode read --min-gpus 2
```

默认读取已启用档案；无档案应跳过并返回非成功，不能计为模型通过。也可用实际档案ID传--profile，不填虚构ID。访问口令由私有环境/认证目录读取，不放命令参数。selftest中的可选Rust检查可能单独失败，逐项记录；--quality会调用真实质量模型，待下载/硬件条件具备后再执行。旧工具个别输出将速度倍率rtf_x标成rtf并带×，应按定义解释，不当作标准RTF。

每卡保存并试听真实PCM/WAV：24kHz、有限值、非空、非全零、无异常幅度/系统性爆音；记录实际流式chunk时间、数量与间隔，排除“整段生成完再切块”伪流式。短句/长句、冷热启动、多段调度和取消恢复分别测量。不通过则回到后端兼容适配，不能静默替换小模型或换预置说话人。

## G3：容器与浏览器链路

分别测试真实浏览器麦克风录制的WebM/Ogg/MP4容器与WAV上传，记录浏览器MIME、解码器/ffmpeg版本、实际采样率、声道、时长、大小和服务端拒绝条件。当前沙箱只有原生Chromium软件输入编码与soundfile小WAV路径，未测物理麦克风或真实ffmpeg。

可信HTTPS浏览器中验证权限拒绝/等待取消、切换主视图、诊断、锁定、麦克风设备结束、超限、上传失败后片段保留。测试虚拟键盘、横屏、缩放、中文字体与屏幕阅读器；当前自动化只覆盖列出的Chromium CSS视口，不能扩展为全设备通过。

## G4：DeepSeek与性能指标

先核对真实模型名、服务端上下文/输出上限与收费额度；Key只用Secret或浏览器内存。测试长流、错误帧、断网、取消、恢复以及切换声音；不自动重试可能重复扣费的请求。

- 分开记录首token、首模型chunk、首PCM、浏览器第一段实际播放；首PCM不是可听首声。
- 标准RTF=生成耗时/音频时长；rtf_x=音频时长/耗时，是倒数速度倍率。分卡与系统聚合指标不可混用。
- 冷/热、短/长文本、两卡调度、浏览器缓冲分别报告，记录足够样本的分布与失败比例，不只展示最好的一次。
- 首声<3秒、RTF≤0.5、无系统性断音是待验收目标。ECAPA余弦或内部fidelity指数不等于99.5%身份一致率；先定义测量/盲听协议和保留集。

## G5：真正双卡训练（实验性核心已实现，Qwen/T4执行未验收）

独立训练作业必须验证world_size=2、两rank实际处理样本、可复现样本覆盖、梯度同步、优化器更新、显存、检查点保存及重载真实试听。当前已有训练输入与声学码准备入口/来源封存/读取租约：逐条文本、统一参考、授权/单说话人声明、完整24kHz mono PCM16 WAV、固定哈希与双rank数学分配计划。真实audio_codes仍blocked；已有FP16 LoRA/DDP/optimizer与adapter代码及CPU小网络梯度/参数更新证据，但未执行Qwen/CUDA训练或自动训练/推理模式切换；不能按创建档案、候选校准或准备输入验收训练。输入副本应先按固定manifest SHA256校验，上游工具必须在快照目录解析相对路径；其他音频格式需受限解码另验，不静默裁剪。

不要将官方BF16/FlashAttention2/全参数AdamW示例直接用于T4，或只加accelerate launch --num_processes 2就称完成。先核对T4支持、模型包装属性、优化器内存和检查点语义；LoRA、ZeRO/FSDP等方案均须实际接口与显存验证，不在缺权重时猜测兼容。训练与推理应隔离，避免每GPU推理实例占满显存时并发训练。

## G5a：声学码准备（入口已有，真实模型未验收）

第七阶段仅本机CPU离线CLI，使用固定输入manifest租约与可信本地12Hz tokenizer模型内容树hash；无自动下载或GPU编码入口。先按KAGGLE_STEP7_AUDIT.md验证真实单条全PCM编码、输出ceil(frames/1920)×16与完整样本覆盖，再实际decode试听、测CPU RAM/耗时。fixture码与stub调用不是该门禁证据；当前真实encode缺qwen_tts/权重且无GPU，仍blocked。

当前已有第八阶段同机同UID整组资源准入协议，但没有自动推理/离线任务模式切换或GPU编码。改为GPU任务前仍需受控作业接入与实际显存测量，不能直接在两模型已占显存时调用cuda:0。输入与码版本租约已实现，码版本已接入实验性双rank训练器并受控共享FD；真实Qwen/T4执行仍未验收，训练器须持有保护直到所有读者退出。语义/解码/训练标志不得因结构检查自动变true。

## G5b：资源准入协议已有，硬件回收尚未验证

按KAGGLE_STEP8_AUDIT.md使用resource_control.py status/reserve；busy=false不代表GPU空闲，预约也不执行模型。真实supervisor/worker/analyst须使用本版本FD协议；父死但孩子持锁时仍busy，不能依PID/TTL强制解锁或删除fleet.lock。多模型进程由supervisor启动，旧版本/外部进程必须另行确认已停。

在目标设备实际记录所有进程停止前后nvidia-smi与CUDA空闲/保留显存，再预约并接入受控GPU任务，验证取消/失败/恢复。此刻有CPU进程/FD与小网络Gloo证据，无实际VRAM回收、自动模式切换或双rank训练证据。bootstrap不再自动按旧PID/pkill停服务；遗留PID标记须人工确认后清理，不能删资源锁。

## G5c：来源封存/读取协议已有，不是训练许可

schema2完整复制输入manifest/JSONL，验证源固定hash、WAV/text/ref/顺序/计划交叉一致；声明只是用户记录。schema1仍legacy-unsealed，禁止凭当前库补写旧授权。list的政策字段不等于完整核验，固定manifest hash verify才返回provenance_verified_now。

hold-read只保持检查租约，第十阶段实验性训练器已接入，但仍须现场验真实编码/语义/权利政策/设备与DDP；首版同版本读取独占，删除/第二读取409，取消/超时/进程退出释放。不能当训练按钮，已有CPU进程/FD接管与小网络参数更新证据，但不能称Qwen/CUDA参数已更新。详见KAGGLE_STEP9_AUDIT.md。

## 待填结果表（当前均未验收）

| 门禁 | 当前真实结果 | 要保存的证据 |
|---|---|---|
| G1 环境/表面探针 | 待目标设备运行；沙箱是blocked | 硬件/版本/报告/空闲显存 |
| G2 双卡真实模型 | 未运行 | 非Mock引擎、每卡真实输出与时间、异常 |
| G3 物理录音/容器 | 未运行 | 浏览器/设备/MIME/ffmpeg/解码与拒绝样本 |
| G4 DeepSeek/性能/音色 | 未运行 | 真实流、分布、取消、听测协议与保留集 |
| G5a 真实声学码/解码 | 未执行；离线CPU入口已有，依赖/权重blocked | 可信模型hash/实际编码/完整覆盖/解码/内存与时间 |
| G5b 资源/显存 | 合作式协议已验证；真实显存/模式切换未验收 | 实际进程/空闲显存/预约与任务取消恢复 |
| G5 双卡训练 | 实验性FP16 LoRA/DDP/adapter代码已实现；真实Qwen/CUDA未运行 | 双rank/样本/梯度/参数更新/检查点重载 |

只有取得对应原始记录后才能改表。秘钥、真实私密语音、完整私人转写和大模型/数据集不进入Git或公开报告。

第十阶段运行入口及具体Notebook取消代码见KAGGLE_TRAINING_QUICKSTART.md；无需等待更多基础设施即可在真实环境尝试。optimizer/adapter执行成功不等于音质通过，不自动替换推理模型，真正Qwen新进程重载/试听与接入聊天仍待执行。


## G11：显式训练adapter后端与聊天（现场待验）

第十一阶段已实现实际接入，不是只写未来工具。按KAGGLE_ADAPTER_QUICKSTART.md从真实completed run取得pin、显式发布命名候选，再使用qwen-adapter-buffered、本地Base及固定hash启动既有supervisor。默认faster保留。两worker加载确认才改变active，错误/缺adapter/Base/错误模式不得回退。

原生API一次生成解码完整段，不接受为G4“声学流式通过”；health/stats/UI必须显示sentence-buffered。只允许称DeepSeek文字/网关段流保留，不能把后处理PCM块或停顿包当模型流式。现场验证保存speaker prompt的真实声音、A/B/A、取消后释放、真实长回答及一份Base/卡的峰值显存。当前CPU数学/本机真实Go+SSE/HTTP是替身系统证据，不是Qwen/T4、新进程试听或外部DeepSeek验收。

固定训练候选拒绝参考文本/候选/校准修改；旧普通档案仍用faster模式，保持删除/认证/两视图。一个参考WAV/转写进入旧profile私有备份范围，run/完整模型不自动备份；恢复缺文件明确失败。源码总目标仍22/300，不因这一开发阶段自动勾满硬件/音质要求。


## G12：现场Mimi/RoPE故障与会话驻留复跑

用户现场已实际识别两T4（各15636037632字节、CC7.5），下载/编译完成；模型加载明确失败，不能保留为“硬件未知”也不能升级成加载成功。step12使用faster0.5.4/qwen-tts-hf0.1.1.post1/TF5.20.2真实现代配置桥接，旧字段异常已在CPU实际wheel函数复现并修复；原配置不变、3个theta验证。CPU数学smoke不是本门禁完成。

目标重新启动完整Kaggle会话后，确认先通过qwen_mimi_rope_cpu，再两个worker各自完成from_pretrained和warmup。检查health的requested_model、model_loaded、单CUDA可见设备与residency_policy，结合实际GPU显存/进程和音频，不能只看这些字段或workers_healthy数字。完成短句/长句/停止与显存记录；配置错误fatal应停止重试并清理本次supervisor，无旧PID盲杀或删锁。

QTTS_RESIDENT=1取消旧600次周期重载和13.5GB主动回收，不自动idle卸载，但错误/OOM/平台回收仍会中断。磁盘权重缓存不等于GPU永久驻留；Kaggle不作永久占用验收。固定三项依赖不是全环境lock，保留平台Torch/CUDA约束后仍需实际安装冲突与模型完整调用验证。

## 第十三阶段现场状态更新（优先于上面历史step12结论）

用户step12仍同错失败，旧CPU函数测试没有覆盖Faster延迟导入。step13显式导入HF后桥接并强制smoke；完整真实包+微型Mimi初始化/重载已在CPU三进程通过，但不是完整Qwen/T4验收。目标22/300不升级，按KAGGLE_STEP13_QUICKSTART.md直接复跑。

## 第十四阶段优先更新

用户step13现场已通过两T4模型加载/预热ready门禁。14仅新增长录音预算/CPU等价缓存/原文分段/默认无后加呼吸。网页一键训练闭环、真实训练提速与质量、首播改善及声学逐字核验未完成/验收，完整目标仍22/300。详见STEP14_AUDIT/QUICKSTART，不能用本轮模拟通过升级真实音质门禁。


## 第十五阶段优先更新

当前step15强隔离参考PCM/ICL上下文，向量模式可能改变音色韵律，不能据CPU证明真实语音完全不串参考。先正常重启会话再运行，按STEP15_QUICKSTART直接朗读与DeepSeek首句分别测试三轮。默认输出-18dBFS、上限12dB增益，校准默认关闭但手动保留，CPU ASR可复用。比较创建耗时时必须区分冷/热、下载和可选校准；比较首声看first_played_ms与underruns。每T4双模型没有实测，不默认开启。旧训练闭环/长数据全覆盖/声学拒播缺口不因本轮交付消失。


## 第十六阶段最新优先门禁（覆盖15纯向量与12dB默认值）

最新包16采用匹配转写ICL条件，codec仅生成码；参考内容及模式pin，默认前瞻0/最大增益6。按STEP16_QUICKSTART先试听不同于参考的目标文本，再做双GPU三轮18条真实基准。tools/voice_benchmark.py不带--run零测量blocked；真实目标0.3任一条不达即失败，达速度也不等于音质合格。旧参考正文继续出声可来自模型幻觉，不能只凭未拼接PCM认为声学逐字已验。历史训练闭环/全覆盖/声学拒播缺口保留，目标22/300仍不升级。


## 第十七阶段最新门禁

先完整重启到17，不用截图15判断17修复。用同源10秒、16秒与24秒对照，长录音按时间戳/真实窗口识别择锚；生成参数也进入v2 pin。核对原文、每卡同文音色/噪声、整段朗读、first_played/underruns与RTF，至少三轮。结构对照16失败17成功不等于实际Whisper识别准确或Qwen质量达标。57份完整备忘录及STEP17_QUICKSTART说明边界，历史训练/覆盖/声学拒播缺口保留。
