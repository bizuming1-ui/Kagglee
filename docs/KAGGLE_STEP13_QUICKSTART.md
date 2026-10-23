# step13：修复你现场的Mimi/RoPE加载错误

这是修复step12补丁因延迟导入而跳过的新包，不是让你继续运行已失败的step12。浏览器“复制 Kaggle 修复版完整代码（step13）”已换成`kaggle-fixed-step13.py`。

## 你现在怎么做

1. **先备份自己需要的参考音频、转写、已训练adapter及日志**，不要把API Key/Token发到聊天或共享输出。
2. Kaggle中先停止当前运行，再用平台的**停止会话/重新启动完整会话**操作，确认原监督器与GPU进程已结束。**仅停止一个单元格、刷新网页或重启Python内核不一定停止已分离的旧supervisor。** 不要用旧日志里的PID盲杀，也不要删除GPU锁来抢占。
3. 新会话选GPU T4 ×2、Internet On；进入浏览器复制页，确认标题/文件名是 **step13**，点击“复制全部代码”，替换旧启动单元格的全部内容再运行。不要同时运行step12。若平台保留了旧工作目录并提示旧supervisor.pid，仍不要盲删或按旧PID杀进程；在确认完整会话已重启后可用全新QTTS_ROOT目录启动，旧数据另行备份/管理。
4. 默认就是Qwen/Qwen3-TTS-12Hz-1.7B-Base，每worker一张GPU。默认`QTTS_RESIDENT=1`为健康模型会话内常驻，不需要另写训练命令或启用adapter模式来解决本次加载错误。环境中若留有`QTTS_MOCK=1`应先去掉/设为0；默认高速后端为`QTTS_TTS_ENGINE=faster`。
5. 依赖阶段审查并固定`faster-qwen3-tts==0.5.4`、`qwen-tts-hf==0.1.1.post1`、`transformers==5.20.2`。若需安装，会用当前Torch/torchaudio/torchvision版本作为约束，避免无条件替换平台CUDA栈。若发生命名空间冲突/安装冲突，会拒绝而不是静默卸载Torch。**不要仅执行pip install transformers<5**，这违反faster0.5.4依赖。
6. 预检必须出现`qwen_mimi_rope_cpu`通过；HF发行包已安装时不允许“compatibility module not loaded”警告后继续启动。这只是实际配置数学检查，**不是模型加载成功**。然后应看到两个worker完成模型加载及warmup、workers_healthy=2，才进入网页短句合成/实际试听。
7. 如果仍报错，需看本次`worker0.out/worker1.out`末尾的完整异常链及新预检结果。确定性兼容错误现在会停止该worker重试，并让启动流程清理其创建的supervisor，不应继续无意义循环加载。清理45秒未确认时必须按平台停止整个会话，不能认为锁已释放。

## 修了什么

step12只检查sys.modules，Faster直到from_pretrained才导入Qwen，因此补丁没装上。本次先用发行元数据判断HF存在，版本/namespace检查后显式正常导入完整Qwen兼容模块，再桥接；导入失败/数学检查不完整均阻断。实际完整包+微型Mimi本地保存重载离线CPU三进程验证，不再只测试手动加载的单个函数。


实际Qwen-HF默认RoPE函数仍读取旧`config.rope_theta`，Transformers5.20.2 Mimi已使用`config.rope_parameters['rope_theta']`。新桥接只针对已识别的Qwen默认函数，从实际配置读theta、给临时副本提供旧字段，保持原配置/权重不动。10000、12345、1000000三个theta的真实Mimi配置CPU数值已核对；未知类型/缩放/非法参数不猜值。

默认不再每600次请求重载模型，也不因旧13.5GB门槛主动重启；显存高会告警，空闲缓存清理不释放活模型权重。可显式`QTTS_RESIDENT=0`回到旧周期回收策略。模型异常、OOM、服务重启或平台回收仍可能打断驻留，不承诺16GBfit、质量或时延。

## 不能承诺“永久部署在双卡”

应用能控制的是**会话存活且模型健康时，每张GPU保留一份模型**。Kaggle会话到期、配额用尽、关机或GPU回收后，显存必然丢失；磁盘权重/私有Dataset备份不等于模型继续驻留GPU。

真正长期常驻需要你拥有可持续运行的双GPU服务器和相应运维/预算。本次没有替你采购或部署外部服务器，也不绕过Kaggle限制。

## 现场验收还没完成

你提供的日志已经证明两张T4被识别、编译/下载阶段完成并到达模型加载；同时明确证明当时加载失败。修复已在CPU重现并验证该配置异常，但沙箱没有T4或完整Qwen权重，不能代替你新版本的模型重载、显存/实际声音验收。需要重新运行step13后才能进一步确认。
