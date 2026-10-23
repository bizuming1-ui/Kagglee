# 第十一阶段：训练adapter接入现有声音选择与聊天链路

2026-10-21，先保存计划再写码。原始至step10冻结，继续当前分支，保持正式工作台与两主视图。

## 选定实现

使用显式选择的官方Qwen原生推理后端加载LoRA；不猜faster-qwen3-tts私有模型/CUDA graph能接受动态LoRA。默认faster流式后端完全保留。新模式明确为qwen-adapter-buffered：一条文本段完整生成后才输出一块PCM，不冒充声学流式或<3秒性能。

1. 严格校验完成训练run/result/request/adapter manifest与固定hash、NCCL两rank/参数更新/覆盖、adapter tensor摘要和保存speaker向量。CLI把真实完成的训练候选发布成带固定binding的命名profile，不改active或自动切模型。
2. 发布时持原码租约，复制统一参考WAV和对应文本到profile，保留固定run/Base/码pin。声明和记录不是法律或加密证明；同UID恶意造记录不在保证内。训练目录/模型不自动云备份，profile仍沿既有profile备份语义；恢复缺依赖必须拒绝。
3. Worker显式引擎选择。native模式每GPU只驻留一个可信本地Base1.7B/FP16/eager；默认/Mock不得接收trained profile或静默退回原Base。
4. 预校验/预构造所有LoRA矩阵与speaker prompt后再整体切换，锁内生成，失败不能半挂载/混音色。不同adapter允许不同rank，且必须属于同一固定Base；每次使用核验当前绑定，禁止缓存绕过撤销/损坏。
5. 官方x-vector-only prompt直接使用保存的统一speaker embedding，不重新生成另一个说话人参考；不改成CustomVoice或伪情感模型。实际语音/音色仍须现场试听。
6. 接入现有Worker PCM帧→Go调度/聊天→网页声音选择；health/stats及UI明确训练候选、未质量验收、句级缓冲。没有新增主视图，没有假训练按钮。
7. 取消传入Transformers stopping_criteria，完成后再检查取消并丢迟到整段；不能保证中止正在执行的CUDA kernel或codec decode。保留旧实时后端/播放打断路径。
8. 固定训练profile拒绝文本/候选/校准改写，保留删除。适配启动/探针选择，native不要求faster包；实际依赖/硬件缺失如实blocked。
9. CPU真LoRA张量切换/隔离/失败回滚、恶意/过大/损坏/错误完成记录、准入/Mock拒绝、取消与PCM帧/真实HTTP/浏览器回归。CPU接口替身不冒充Qwen/T4声音实验。
10. 三轮原功能回归、独立step11包、审查与完整交接。下一门禁直接是Kaggle实际训练后重载/试听和真实聊天，不再加收据工具前置。
