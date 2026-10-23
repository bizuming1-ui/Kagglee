# 第十二阶段：根据Kaggle实际日志修复MimiConfig.rope_theta

2026-10-21。先保存STEP12计划与Q11的50项建议，再写实现。原始至step11冻结；这次直接修用户已遇到的模型加载故障，不另设训练准备阶段。

## 1. 现场事实与诊断

用户日志显示：Python3.12.13、Torch2.10.0+cu128、faster-qwen3-tts0.5.4、Transformers5.20.2；两张Tesla T4、计算能力7.5、每卡总显存15636037632字节。依赖探针形状通过，Go/Rust编译和模型下载完成；随后两worker均报`AttributeError: 'MimiConfig' object has no attribute 'rope_theta'`并被监督器重启。**这些日志证明到达模型加载并失败，不证明模型已常驻或推理成功。** HF未登录警告不是此次核心异常。

读取实际PyPI wheel与元数据后确认：

- faster0.5.4依赖`qwen-tts-hf>=0.1.1.post1,<0.2`及`transformers>=5.15.1,<6`。不能只把Transformers降到4.x，那个组合违反依赖。
- qwen-tts-hf0.1.1.post1共享`qwen_tts`命名空间，其中`_transformers_compat._default_rope_parameters`仍直接读`config.rope_theta`。
- Transformers5.20.2的实际MimiConfig已使用`rope_parameters`，不存在该旧属性。默认配置及旧`rope_theta=12345`输入都被规范化到现代字典。
- CPU中使用**实际TF5.20.2类+实际Qwen-HF wheel函数**复现同一个AttributeError，修复后检查10000/12345/1000000三个theta的精确频率及原配置不变，通过三次独立进程。未构造完整Qwen、未载权重、未用CUDA。

来源与许可证：
- https://pypi.org/pypi/faster-qwen3-tts/0.5.4/json
- https://pypi.org/pypi/qwen-tts-hf/0.1.1.post1/json
- https://pypi.org/pypi/transformers/5.20.2/json
- Qwen函数来源`qwen_tts/_transformers_compat.py`，Apache-2.0。新桥接调用原函数，不把整份第三方实现混写进新模块；包内原Apache许可保留。
- 实际Qwen-HF wheel SHA256 `ed5b7aae64cf795243369fb5226173f459a45689ea86db1c6d3eb14fc0c2c01d`，所用成员SHA256 `033673335ed7bcb19054cdabc6c8400e443493f4b54340f8f449577d122bf982`。三项完整requires_dist/wheel digest记录在step12证据目录。

## 2. 实际修复

| 部分 | 改动 | 边界 |
|---|---|---|
| `qwen_compat.py` | 仅包装已识别Qwen默认RoPE函数；从真实现代配置读theta/partial factor，用临时config副本传给原函数；重复安装幂等、第三方覆盖/非法值/未知scaled schema拒绝 | 不给所有Mimi硬加property、不写死10000、不修改权重/config文件、不假称修复所有5.x版本 |
| Worker/原生/CPU编码/训练 | 导入Qwen后、加载模型前安装桥；保留原Base/LoRA、现有码/授权与质量标志 | 其他未见过的真实模型错误仍可能出现；实际完整加载须再运行 |
| 预检 | 新`qwen_mimi_rope_cpu`：实际MimiConfig、实际Qwen默认函数的CPU数学smoke，明确NO model/GPU；HF/官方provider检查可区分命名空间 | 解决此前只验签名而漏配置错误的缺口，但不能把smoke当完整模型通过 |
| 依赖 | 固定faster0.5.4 / qwen-tts-hf0.1.1.post1 / TF5.20.2三个直接版本；安装时对已装Torch/torchaudio/torchvision加版本约束；缺平台Torch拒绝替换；官方/HF重叠命名空间拒绝 | 不是完整环境锁，不保证Kaggle所有现有包无冲突；不强制升级/卸载CUDA库或照装沙箱Torch |
| fatal控制 | 已知rope_theta AttributeError及明确兼容异常标fatal；supervisor停止该worker重试，并原子写当前启动nonce绑定的失败记录 | transient错误仍保留有界重试；不按旧日志PID或模糊名称盲杀 |
| bootstrap清理 | 看见fatal健康/当前nonce收据立即结束等待；失败/异常/中断时只停止自己创建的supervisor Popen；等待其正常清理直接children和FD | 45秒未确认会明确要求停止完整Kaggle会话，不删除锁或假称所有GPU已空闲 |
| 会话驻留 | 默认QTTS_RESIDENT=1，保留每worker单GPU0/1映射；不在600次请求或旧13.5GB门槛主动回收模型，显存高只告警；显式0保留旧策略 | CUDA empty_cache不释放活模型权重；OOM、真实错误/服务重启/平台回收仍可打断，不保证永久会话 |
| health | requested_model、model_loaded、cuda_visible_devices、fatal_error、residency_policy | Mock明确不报真实model_loaded，requested_model不是权重内容签名；不把GPU映射配置说成现场模型成功 |

## 3. 交付与验证

- step12：`kaggle/kaggle-fixed-step12.py`，282031字节/47资产，SHA256 `2be33a3a6735639ce32ec8750e9a489abd96e4daa780d068557f2b0156f2de08`，独立包与source_manifest_step12.json。原始至step11冻结。
- 浏览器复制预览3001已换step12，代码和下载来自固定hash的完整包，不动原3000工作台及15文件/HEAD。
- 新14项兼容/控制/驻留/安装约束回归已通过；完整Python267×3=801 PASS，含原有训练/实际CPU小网络Gloo、访问控制、存储、包与adapter回归；Node30×3及Go race count3 PASS。
- 既有所有权真实进程/HTTP输入/本机码CLI/Mock管线/Go+SSE+双worker adapter替身各三轮PASS。新增真实supervisor+CPU fatal-health进程三轮，验证当前nonce收据、bootstrap提前失败、所属supervisor及worker退出、PID运行标记移除；不是GPU实验。均非真实Qwen/NCCL/DeepSeek联网；不把已有CPU链路替身算作GPU重载。
- 真实wheel配置数学三进程PASS；完整浏览器113×3=339 PASS，另最终step12包逐字节复制三轮PASS。真实Chromium复制页三轮剪贴板精确一致、下载文件名/内容哈希一致、拒绝授权时全选/手机375px无横向溢出、正式15文件不变，详见copy-page.json与final-checks.json。
- 三轮各100条建议/目标复审见review-map.json。完整目标仍22/300；11题550建议不等于550实现或300修复。当前只新增用户真实双T4识别/加载失败证据，不升级目标推理/质量项。

## 4. 保留的失败与未执行内容

- 首次独立CPU target环境同时存在旧tokenizers/hub dist-info，TF版本检查拒绝；删除该隔离cache中的旧元数据后，真实CPU复现与修复通过，初始错误日志保留。未修改主测试venv或用户Torch。
- 完整Python初轮267中1失败：旧native探针测试强制要求官方qwen-tts发行包，实际HF provider也可提供命名空间。改为显式provider组门禁及对应断言，随后完整三轮通过；初始失败日志保留。
- 新fatal进程脚本初次漏传子进程PYTHONPATH导致找不到supervisor模块；修正测试环境后实际三轮通过，初始日志保留，不是生产模型故障。
- 沙箱CUDA不可用，没有实际两T4或完整模型权重，完整Qwen导入/加载、warmup、声音、峰值显存和性能仍须用户新包复跑。配置层成功不是整个模型已保证可运行。

## 5. 给用户的直接操作与下一门禁

见KAGGLE_STEP12_QUICKSTART.md。先备份所需私有数据，再停止并重新启动**完整Kaggle会话**，不是只重启内核/刷新网页；默认T4×2/Internet On/非Mock，从浏览器step12完整复制。禁止继续同时运行step11或拿日志PID1589盲杀。

重新运行应先看到配置smoke通过，再两worker完成模型加载/warmup及workers_healthy=2，最后真实短句听音/长文本/打断与显存。下一项是实际目标复跑，不再插入工具准备阶段。

**“永久部署在双卡里面”不能在Kaggle保证。** 能实现并已编码的是健康模型在会话存活期间每卡一份常驻；会话结束/配额到期/机器回收后显存消失，磁盘/私有Dataset权重缓存不是GPU继续运行。长期服务需要可持续双GPU服务器与运维预算，本次未采购/部署外部硬件或绕过平台限制。

- 独立复制检查器首次Chromium启动SIGSEGV，尚未进入页面；保留copy-page-initial-browser-error.txt。随后Playwright最终复制三轮及独立检查器真实剪贴板/下载三轮均PASS；未改生产代码，启动异常根因未确定，不隐去失败记录。
