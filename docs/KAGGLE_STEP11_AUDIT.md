# 第十一阶段审查：训练adapter已接入原生推理及现有聊天

2026-10-21。先保存STEP11计划及专业问题10的50建议，再写实现；不向用户重复提问。**这是实际接入代码，不是再做一轮训练准备工具。** 当前无真实Qwen/T4权重、CUDA和外部DeepSeek实验，硬件/音质门禁不升级。

## 1. 交付与选择

- `kaggle/kaggle-fixed-step11.py`：276043字节/46资产，SHA256 `cd5346e8ae34f1e2db327a076a7411996982848f9d4e14236f05d94c626d496e`，`source_manifest_step11.json`对应当前source；repack默认step11。
- 原始至step10冻结；step10仍261429字节/43资产、SHA256 `2bddd6ebad371268f9b3b02315fc29cae588da6c46c7d134476945b50b8a5ac4`。不覆盖旧可运行路径、不改正式满额15文件工作台。
- 不猜faster私有对象/CUDA graph支持动态LoRA。保留默认faster路径；显式`QTTS_TTS_ENGINE=qwen-adapter-buffered`启用官方原生推理，**句级缓冲，不是声学流式**，不混驻两种模型或完整Base副本合并。
- 完整目标审查300条仍22项已验，不是开发完成百分比；10题×50=500建议，不是500项已实施修复。

## 2. 具体代码

| 位置 | 已实现 | 不能推导 |
|---|---|---|
| `trained_profiles.py` | 严格完成run/request/result/manifest交叉核验；固定Base/码pin；两NCCL-shaped rank更新及每epoch样本覆盖记录；限定成员/文件大小/hash/tensor digest/FP32/finite；发布持原码租约，复制统一参考WAV和匹配转写 | 本地记录不是官方签名或同UID恶意造记录的防护；声明不是法律/身份证明 |
| `tools/trained_voice.py` | describe取真实pin，publish要求显式run/pin/自命名与未验收确认；不自动active，不输出私人文本或原始模型路径 | 发布不是训练，不证明声音相似或重载完成；不是GUI训练按钮 |
| `lora_adapter.py` | 全量验证/构造replacement后事务提交，可不同rank切换，提交异常回滚；保持原Base模块，不重复叠挂旧LoRA | CPU输出恢复不是Qwen语音可听一致性或CUDA内存适配 |
| `adapter_engine.py` | 本地Base前后指纹、CUDA单可见卡、Base1.7B FP16/eager；每段核对绑定/adapter，不每句重新hash多GB Base；保存speaker直接生成官方x-vector-only prompt | 实际config的base/1b7/16组及版本/停止条件行为仍须真实权重验证；无模型或T4显存证据 |
| `worker.py` | 显式引擎选择，Mock/默认拒绝trained profile，原生拒绝普通profile；锁内切换/生成，原生单wave转既有PCM帧；取消后丢迟到wave，错误无Base回退 | 停止播放/AR stopping不能中断CUDA kernel/codec decode；错误不等于立即清除GPU任务 |
| Go调度/监督 | 原生无帧/health/supervisor预算180秒；默认60/75/90秒不变。继续有序切段、HTTP/SSE、双worker与原activate门禁 | 预算不是延迟承诺，不保证任意长句180秒可完成 |
| 网页/analyst | 选择器/档案/health标注训练候选、句级缓冲、未验收；参考只读，编辑/校准409；旧普通档案操作及删除保留。修复一致性检测全失败仍可能consistent=true | 比较指标不是人工试听、身份或质量验收；没有新增第三主视图 |
| bootstrap/probe | native检查官方Qwen接口，不要求faster包；固定本地Base，不预下载陌生模型；缺依赖blocked，不自动更换引擎 | API形状通过不是模型运行；Kaggle完整安装/启动路径仍待实机执行 |

## 3. 数据与失败边界

- 新profile仍沿旧profiles私有Dataset备份语义，含一段统一参考WAV及对应文本；run/全体训练数据/完整Base不自动备份。操作说明明确告知，不把音频/权重/私密状态进Git。
- 发布时依赖原码固定版本；运行推理需要同一Base和run/adapter。恢复缺adapter/Base必须明确失败，不用参考缓存或Mock输出冒充训练声音。删原码、原库、profile、run和远程备份是不同操作。
- 训练profile绑定固定版本，不自动修改原有active。两worker均确认才改变active，某卡失败保留active；个别worker可能已加载另一adapter，但下一次请求会按其profile在同一锁内重新选择，不能把一次load当后续永远正确。
- 原生一条文本完整生成后才yield一个wave，要求24kHz mono/有限/非空/非全零/长度预算。后处理、停顿与flush产生多个PCM帧不构成声学流式证据。首个真实语音包时间仍由模型wave返回后计算，不能拿预置停顿冒充TTFA。
- 失败切换保留原adapter对象和prompt，但错误请求不得调用原adapter生成；绑定/文件损坏即报错。Base仅加载期固定指纹，后续内存/文件任意同UID恶意修改不属于隔离保证。

## 4. 本轮已执行的验证

- Python完整252×3=756 PASS，38.129/37.891/36.272秒：包括24项新adapter测试和旧训练/存储/访问控制/包/录音契约。真实CPU LoRA数学证明A/B输出不同、A→B→A精确恢复、不同rank、失败预构造不半写、两worker对象隔离。CPU Gloo小网络训练在三轮完整suite内实际运行，不是Qwen/NCCL。
- `adapter_gateway_check.py`：真实本机Go网关/HTTP/SSE、两个独立worker进程、CPU tiny LoRA+注入官方API形状的生成替身，3轮A→B→A，通过真实聊天切段/帧有序与句级缓冲stats；损坏第二版本后activate 503、原active保留，两worker错误请求无PCM。SSE和wave是本机替身，**不是真实DeepSeek、Qwen声音或NCCL**。
- Go race count=3 PASS；Node30×3 PASS。
- 既有ownership_process_check、training_gateway_check、codes_cli_check、mock_pipeline各调用3次，每次内置3轮，均PASS（各9轮CPU/协议，不是9轮GPU验收）。
- 浏览器112×3=336 PASS（11.0分钟）：新训练候选标注/只读/按钮/现有聊天选择/诊断、全量旧录音/存储/安全/视图及包复制均保留。最终包额外逐字复制3/3 PASS（10.0秒），`final-copy-repeat3.txt`与最终`final-checks.json`留证，不用网页截图冒充目标模型证据。
- native runtime probe **blocked/退出2**，model_loaded/inference_verified/training_verified/performance_verified均false。沙箱Torch2.8+cu128仅CPU测试，CUDA不可用，无qwen_tts或真实权重，不是Kaggle依赖锁。

## 5. 失败记录与修复

1. 新浏览器测试首轮1失败/1通过：默认处于语音对话，测试未进入录制参考视图就用可见role找档案按钮。补显式视图切换，2/2通过；`browser-initial.txt`保留，不删失败。
2. 完整Python首轮248测试1失败：旧探针AST测试仅期望faster调用，新增native接口后不再覆盖两引擎。修正为分别核对两份真实调用关键词集合，并补全native sampling参数探针；`python-initial-failed.txt`保留。扩展后252×3全通过。
3. shell曾用错误工作目录调用仓库相对路径和错误gofmt位置；未更改生产代码，改用仓库根/已安装Go实际路径，最终编译/race通过。不是目标Qwen故障或被隐藏的模型成功。

## 6. 三轮各100项建议复审与后续

`review-map.json`逐条保留300条原始建议/目标、当前证据关联与阶段行动，按源码环境、模型音频、系统交互三组100条审查。新增修复以本报告代码表为准，不把300个范围映射当300个新缺陷或已修复条目。完整目标22/300保持，真实权重/GPU/音质/性能未勾选。

下一项直接到真实Kaggle：先小数据真实首个优化步/峰值显存，完成run后在**新进程**按pin加载、每GPU保存和试听WAV、A/B/A、真实DeepSeek长回答/停止恢复，分别记录句级缓冲首声及默认faster声学流式。按KAGGLE_ADAPTER_QUICKSTART.md执行，不增加另一个工具前置阶段，不承诺成功日期、16GBfit、<3秒、RTF或99.5%身份相似率。
