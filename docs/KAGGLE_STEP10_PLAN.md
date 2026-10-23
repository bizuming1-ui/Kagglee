# 第十阶段：直接开发最小真正训练器，而非再增加准备阶段

2026-10-21。用户要求继续且追问何时真正开发。本轮立即开发训练核心，先保存计划后写码。不再用纯封存/预约工具充当训练进展。

## 具体交付

1. 对照固定上游022e286b98fbec7e1e916cb940cdf532cd9f488e的dataset/sft/model接口，实现本地数据组装和真实联合loss；修正官方示例未过text_projection的维度风险。
2. T4候选路径为FP16/eager、microbatch1、FP32 LoRA/AdamW状态、冻结Base、talker与sub-talker attention q/v低秩更新；不是全参数AdamW，不假称16GB已测通过。
3. 实现真实torch DDP双rank/GradScaler/梯度累积/有限loss/梯度/参数改变检查、每rank样本覆盖、原子adapter检查点。loss与backward必须在DDP包装forward内，不从.module绕过梯度同步。
4. 父控制器独占GPU整组与码版本读取租约，两个rank受控继承相同FD；父死而活孩子仍持锁，不按PID抢占；取消/超时杀整个进程组并等待，才释放父引用。
5. 训练门禁拒绝fixture/legacy；要求schema2来源核验、实际编码状态、用户明确确认输入语义/授权与实验性训练。模型为可信本地Base1.7B完整指纹，离线/拒绝远程代码，不自动安装/下载/停止推理。
6. 固定模型/码hash写入检查点；保存adapter及统一参考speaker embedding，提供明确的加载函数，不把adapter伪装完整CustomVoice模型，不自动替换推理服务。检查点成功仅表示训练运行，质量/新进程试听单独验收。
7. 可执行CLI与Kaggle操作说明；依赖缺失返回blocked，不运行假训练。CPU小网络实际张量/优化器与双进程Gloo仅验证算法/同步，不替代Qwen/CUDA/NCCL验收。
8. 先针对核心测试、再旧功能回归。旧包1–9冻结、正式15文件/HEAD/1MiB不变；新独立包step10。文档只记录本轮已执行证据，不把测试次数当300项完成率。

## 完成界限与时间回答

核心开发现在开始，本轮目标交付可执行训练代码，而非再等审查。真实开训必须在挂载可信完整Base/tokenizer与授权音频的双T4环境执行；沙箱没有GPU/权重，不能给出可信训练成功日期或保证显存/音质。不得显示训练已通过，也不增加假的训练按钮。
