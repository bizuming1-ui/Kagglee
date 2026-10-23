# 第七阶段计划：有租约、可回滚的离线声学码准备

2026-10-21。本计划在编码前保存。先核对第六阶段冻结包及Qwen固定提交022e286b98fbec7e1e916cb940cdf532cd9f488e的prepare_data.py、tokenizer encode和12Hz配置。

## 推荐方案与真实门禁

不直接从网页启动GPU编码：supervisor尚无训练/推理资源互斥，不能和两个推理worker抢显存。本阶段新增**本机离线CLI、仅CPU、仅本地已物化模型**的真实Qwen tokenizer适配入口；不装依赖、不下载、不执行任意命令、不开放HTTP训练接口、不改变两主视图。CPU路径不是双T4性能方案，而是先验证可追溯编码协议；将来GPU入口必须先实现资源所有权。

当前沙箱无Torch/qwen_tts/本地权重，真实编码预期blocked。测试可注入确定性fixture，但fixture输出必须明确test_only，不能成为真实audio_codes完成证据。不能从编码完成推断训练完成或检查点可用。

## 实施顺序

1. 增TrainingDataStore读取租约：固定manifest哈希、完整核对后持有独立进程锁；编码期间禁止删除该输入，其他数据集操作不持有长时间全局锁；进程退出自动释放。锁文件放输入目录外，不改冻结快照文件集合。
2. 新独立STATE/training_codes，0700/0600、默认32份/64MiB每份/256MiB总量/256MiB剩余，复制完整规范WAV与rank计划，输出train_with_codes.jsonl及manifest，不改变原输入。
3. 对每个样本单条调用真实Qwen3TTSTokenizer.encode(np.ndarray,sr=24000)，不使用上游zip静默忽略缺失结果。要求恰好一个返回、ceil(frames/1920)行、16列、严格整数0..2047；验证完整样本覆盖、原text/ref_audio不变。
4. 全量模型目录内容哈希固定，本地JSON/safetensors、拒绝软硬链接/远程模型ID/pickle/自定义代码；config为12Hz/24kHz/16码本/2048范围，实际加载配置再次核对。固定CPU/FP32/eager/小线程数，不用BF16/FA2/GPU。
5. 原子staging发布、失败/取消清理、下次操作回收进程被杀遗留暂存。源输入删除后已发布码副本独立；副本不自动加入Dataset，单独本机verify/list/delete。
6. CLI父进程施加总超时，SIGINT/SIGTERM终止子进程组并必要时kill；Linux PDEATHSIG/ppid握手覆盖控制器被强杀；不把取消标记为完成。模型日志丢弃，公开输出仅简要状态，不包含私人转写/路径/底层异常。缺依赖/模型/哈希不符明确非零退出。
7. 编码并非训练：没有token级文本tokenizer、optimizer、loss、检查点或实际两rank；真实模型成功执行也只标记tokenization_executed，语义/解码/训练验证仍false。测试fixture另用test_only状态。
8. 新存储/租约/模型清单/返回形状/故障/超时/取消/备份排除/CLI拒绝测试；全部旧测试三轮与完整浏览器三轮，新增step7全源码剪贴板测试，保留原始至step6及正式工作台15文件与1MiB上限。
9. 独立step7包与确定性清单、审查报告、完整交接；真实blocked和所有失败/修正记录保留。没有GPU证据就不勾相应300项清单。

## 非目标

不启动GPU任务、不停止现有服务、不新增网页训练按钮、不宣称真实audio_codes已得到；没有GPU资源模式切换、DDP/梯度更新/模型训练/性能或音色验收。操作系统级RAM沙箱、同UID恶意进程隔离与断电耐久不在本阶段承诺内。
