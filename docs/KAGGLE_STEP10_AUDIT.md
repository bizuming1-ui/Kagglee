# 第十阶段：直接交付训练核心，真实Qwen/T4执行仍待验证

2026-10-21。回应用户“还有多久才能真正开始开发”：**核心开发本轮已经进行并完成实验性实现，不再等待下一轮基础设施。** 保存STEP10计划与Q9的50建议后，直接实现loss、反向传播、DDP、优化器与adapter保存。不能因为尚无目标硬件验收就说“还没开始开发”，也不能反过来把CPU算法测试说成Qwen训练成功。

## 1. 交付

- `kaggle/kaggle-fixed-step10.py`：261429字节、43资产，SHA256 `2bddd6ebad371268f9b3b02315fc29cae588da6c46c7d134476945b50b8a5ac4`。确定性重打包与source_manifest_step10.json匹配。原始与step1–9冻结。
- 新生产模块`lora_adapter.py`、`tts_dataset.py`、`tts_training.py`、`training_job.py`和入口`tools/train_tts.py`；派生dataset/联合loss保留上游Apache声明并附完整LICENSE-QWEN-DERIVED.txt。
- `training_codes.py`向受控rank导出/采用同一读取OFD，旧lease三元组API不变；`gpu_ownership.py`只新增显式offline模式adopt，推理默认仍拒绝offline租约。没有新语言、HTTP训练端点或假训练按钮。
- 生产网页/Go不改，两主视图及旧库/输入/码/认证/录音/复制保存回归。正式工作台15文件1043155字节及HEAD不变，独立交付，不提高1MiB或删除旧文件。
- 实际Kaggle操作与可取消Notebook代码见`KAGGLE_TRAINING_QUICKSTART.md`。目标环境/模型/数据就绪即可尝试本CLI，不以等待第十一阶段为条件。

## 2. 真正开发的内容与边界

| 功能 | 已实现 | 尚不能声称 |
|---|---|---|
| 真实训练目标 | talker codec0 CE＋0.3×sub-talker loss，16组码；speaker encoder冻结，统一参考embedding | 没有运行真实Qwen权重，不能说语义/音色学到或指标达标 |
| 文本/样本 | 固定上游助手格式/尾部处理与collate布局；完整文本、码、规范WAV参考mel；序列预算超限拒绝 | 未现场验证实际Qwen文本tokenizer和所有语言/长音频，不截断假装全覆盖 |
| 投影修正 | 使用talker.text_projection(get_text_embeddings(...))后再与codec相加 | 官方示例直接相加有维度风险；CPU测试故意使用6维文本/4维talker证明投影必要，但不冒充真实Qwen跑通 |
| T4候选策略 | FP16/eager，microbatch1，冻结Base1.7B；仅实际命中的talker/sub-talker self_attn q/v注入LoRA；A/B及AdamW状态FP32，非重入梯度checkpoint | 没有T4显存证据，不保证16GB、不称LoRA官方兼容已验收，也没有照搬BF16/标准FA2/全参AdamW |
| 双rank | 每rank一个显式CUDA设备、NCCL、120秒集合通信超时；整个参数相关loss在DDP.forward内，非经.module绕过 | CPU Gloo成功不等于NCCL/Qwen/真实双T4成功 |
| 梯度与更新 | 正确累积/尾组缩放、GradScaler、全rank有限loss检查、梯度同步/裁剪；任一rank梯度溢出则全体跳步/降scale；至少一次实际参数变化且两rank最终摘要相同 | 不把进程启动、loss打印、退出0或静态rank计划当训练成功 |
| 覆盖 | 每epoch固定seed打乱后按rank划分，奇数重复前缀补偶数，不drop_last；每rank每epoch保存见过ID，保存时核对全体选中覆盖 | 填充样本有明确重复，不假称无重复；真实数据质量/转写匹配靠操作者审阅，不是算法鉴定 |
| 检查点 | 原子保存adapter.safetensors、speaker.safetensors、Base/码pin/层名/覆盖/rank更新与版本、设备/峰值显存报告；load_adapter检查绑定/成员/hash/shape/finite | 是adapter候选，不是完整CustomVoice；不保存可恢复optimizer/scheduler/RNG状态，不自动部署聊天，也未Qwen新进程重载试听 |

源码对照固定上游`022e286b98fbec7e1e916cb940cdf532cd9f488e`的finetuning/dataset.py、sft_12hz.py和core/models/modeling_qwen3_tts.py。没有直接运行上游训练脚本；修正T4精度/优化器规模、DDP调用边界与文本投影风险。已验证的只是下面分层证据，实际包/API兼容仍需现场模型运行。

## 3. 准入、资源和退出

- 严格拒绝fixture、legacy-unsealed、非真实编码状态、少于两个样本或没有明确数据审阅/实验确认。审阅是用户声明，不把tokenization_verified等原始未验证标志变true，不替代法律/身份/语义鉴定。
- Base1.7B完整本地内容树固定hash，拒绝pickle/链接/远程代码/不完整或越界分片；Base内speech_tokenizer指纹必须等于所用码的encoder指纹。hash不是官方签名，需操作者可信来源。
- 父进程先固定码并持码租约，再持GPU整组offline-reservation OFD；两rank仅受控继承同一对FD并核对锁、inode/nonce、模式与固定码。码验证可在多rank同时进行，不依赖互相冲突的全局写锁。
- rank在Torch/CUDA前安装Linux PDEATHSIG并核对ppid，启动信号屏蔽窗口后解除SIGTERM/INT；父在Popen+记录PID窗口屏蔽取消，防丢刚启动的孩子。父死且孩子还活着时仍持OFD，最后引用才释放，不能删锁/PID/TTL抢占。
- 正常取消/总超时/单rank失败/第二rank启动失败，父停止并等待直接rank后才退租。timeout约束rank启动/加载/训练阶段，不含父进程前置指纹与收尾核验，并另有终止等待；不是全命令硬截止。DataLoader没有额外进程；不提供任意命令/外部进程训练器，不自动停旧推理或恢复模型。不是跨UID/容器/恶意同UID隔离，也不证明驱动显存已回收。
- request、rank日志/结果与adapter只在本地training_runs；目录0700、文件0600，Git忽略且原profiles-only备份不纳入。私有框架日志可能含路径/错误上下文，不能公开分享。正式CLI只输出控制器收据，不输出私人转写。
- 完成只说明两rank实际运行/覆盖/参数改变并保存adapter，quality_verified与inference_reload_verified仍false。没有checkpoint的双进程退出0明确失败；失败不替换旧推理模型。

## 4. 已执行证据（docs/validation/step10/）

### 真正的张量与算法测试，不只是Mock状态

- 新增25项训练核心/准入/进程测试，另加step9冻结回归；完整Python227×3＝681 PASS，`python-round1/2/3.txt`，没有跳过Torch测试。
- 小网络使用不同文本/talker维度和两级attention，实际计算联合loss、真实autograd/AdamW更新、冻结Base保持、FP16基座/FP32训练梯度、尾部累积、非有限loss/梯度拒绝/跳步、严格adapter保存/重载/hash篡改拒绝。
- 两个实际CPU进程使用torch.distributed/Gloo和DDP、不同样本分片；前后参数摘要改变，两个rank最终摘要完全一致，每epoch全样本覆盖。单元测试每轮都执行，另`trainer_tensor_check.py`独立三轮，完整摘要/loss/步数/分片在`gloo3.json`，不是Qwen权重或CUDA/NCCL结果。
- DDP日志提示find_unused_parameters=True在小网络没有unused，属于额外图遍历开销警告。真实Qwen尚未验证所有分支，暂保留诊断安全配置，不把警告隐去或宣称极致性能。

### 真正的OS进程与文件保护测试

- 实际Popen/pass_fds/OFD两CPU持锁者，父/孩子生死、取消/超时/第二启动失败、一个失败终止另一个、控制器SIGTERM/SIGKILL和pidfd退出观测；错inode/未持有FD拒绝，默认推理模式拒绝offline采用。生命周期测试内部注入CPU角色/绕过训练准入，仅测协议，生产CLI没有fixture训练开关，不能用它证明训练执行。
- 真实CLI fixture训练明确409且无training_runs创建；真实数据/模型依赖缺失返回blocked/拒绝，不产生训练成功。

### 原有功能回归

- Node API30×3、Go28顶层/16子测试race三轮PASS。真实Go→analyst→磁盘HTTP、旧编码CLI/fixture、supervisor受控FD/CPU角色、双CPU Mock流管线各三轮PASS，分别记录；没有GPU/真实音频质量或DeepSeek请求。
- 浏览器110唯一（60 QTTS＋50工作台）×3＝330 PASS（10.4分钟），包含step10完整复制/保留step9；最终复制专项另3 PASS（10.2秒）。均临时项目，不修改正式工作台，不推广成物理设备/Qwen训练/全浏览器验收。
- 原始22hash/当前43资产确定性repack、Python compileall、JS语法、diff检查PASS。最终`verify_delivery.py`核对原始至step9冻结、43资产、24完整内嵌备忘录、9题450建议、300项状态、所有最终日志/Gloo数值及正式15文件全部hash/HEAD，生成final-checks.json和formal-api-readonly.json。
- 沙箱新装Torch2.8.0+cu128、safetensors0.6.2、packaging25.0仅为CPU张量测试，不是Kaggle生产锁或GPU实测；runtime-probe仍blocked/退出2：CUDA不可用、qwen_tts/流式后端/真实权重缺失。没有模型下载/加载、Qwen训练或真实音频输出。

### 原始失败留存

首次17项核心测试中两个错误：夹具把manifest返回值顺序取反、safetensors.torch缺未声明的packaging依赖；修夹具/补可选CPU测试依赖后17 PASS。扩展生命周期时一项夹具reject不支持kwargs，改lambda后完整25项进入最终227三轮均通过。`training-core-initial.txt`、`training-core-expanded-initial.txt`保留对应失败，非伪造生产缺陷或隐藏中止。

## 5. 三轮各100项范围复审

300条状态映射保存review-map.json，依然22/300。这里是完整目标验收清单，不是开发完成度百分比。Q9新增50项建议，累计9题450建议。

- 第一轮100条：训练Core、LoRA目标、文本投影、Base/tokenizer绑定与包许可证有实际实现；但R1-011/018/064等真设备与模型试验仍阻塞，不将CPU结果套进T4项。
- 第二轮100条：R2-011/012/015/021/022/025/031/034等有真实算法/同步/采样/低秩优化与保存实现、CPU层证据；没有真实Qwen/NCCL/显存，R2-040没有新进程Qwen重载试听，均不夸大验收。R2-001/003/004没有自动推理↔训练切换。
- 第三轮100条：保持录音/两视图/编辑保存复制；小网络参数/adapter重载不等于真实音色/训练后聊天，也没有物理麦克风/DeepSeek/首声/RTF或99.5%身份结果。

## 6. 时间回答与接下来的直接核心目标

**何时开始核心开发：本轮已经开始并交付实验性训练代码。何时可以尝试开训：双T4、完整可信模型、授权真实数据及依赖就绪后即可执行当前CLI，不必等另一个基础设施阶段。何时训练成功/声音达标：未有现场数据，不能承诺小时数或日期。**

下一步直接围绕真实首步训练的错误/显存与adapter新进程重载、接入现有推理/聊天。不要再把收据/预约工具排成新的前置阻塞，也不要只增加训练按钮而后台仍做缓存。自动模式切换、可恢复训练状态、完整模型导出、GPU编码、UI进度/取消、真实质量与性能仍待实做。
