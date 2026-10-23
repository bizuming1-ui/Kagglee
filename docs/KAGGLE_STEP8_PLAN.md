# 第八阶段计划：同机GPU资源互斥准入与进程持锁

2026-10-21。编码前保存。先核对第七阶段冻结包、supervisor/worker/analyst启动顺序与离线CPU入口。

## 选择与边界

选择保守的**同机同UID整组GPU独占租约**，不按CUDA_VISIBLE_DEVICES索引分割，避免索引/UUID别名绕过。租约固定在/tmp的私有同UID目录，不随QTTS_STATE/模型目录变化；原生flock为准，不使用PID/超时TTL判断可强制抢占。

真实supervisor先持有inference整组租约，再将同一打开文件描述符通过pass_fds交给GPU worker和analyst；孩子验证目录/inode/nonce/模式后采用。管理进程死亡或关闭自己的引用，不释放仍在孩子手中的资源锁。独立真实worker/analyst无继承描述符时必须独占整个租约，因此多进程推理应由supervisor启动；第二套supervisor/独立GPU进程/离线reservation明确busy。

新增本机resource_control.py status/reserve命令。reserve只是有界离线所有权预约，不执行GPU工作、不代表显存空闲、编码或训练。当前不自动停推理、不增加网页按钮/HTTP训练入口、不启GPU编码；需要显式停止既有推理，等待锁释放，再进入后续真实硬件门禁。CPU encode仍不占GPU锁，Mock路径不宣称占GPU。

## 实施顺序

1. 新py/gpu_ownership.py：0700目录/0600不可替换锁文件，拒绝路径软链接/硬链接/非本UID，不删除锁文件。记录仅用于诊断，非锁权威。
2. acquire/adopt/close/status，严格FD类型/inode/nonce/协议/模式；close只关引用，绝不LOCK_UN释放仍被子进程共享的OFD。无任意命令/路径/强制解锁接口。
3. supervisor在模型子进程前占租约；只worker/analyst继承，gateway无GPU描述符。确保凭据/内部FD环境不意外传其他进程；第二实例失败不覆盖supervisor.pid。
4. worker和analyst在任何模型加载前采用/获取租约；Mock跳过且不假报硬件验证。外部ASGI真实import也受保护。生产目录不提供可任意切换的环境变量，测试用显式隔离路径。
5. 修正Proc日志句柄泄漏、kill必须等待leader死亡并清理后代、停止信号早于启动注册、停止期间不再重启；bootstrap不按旧PID/pkill杀进程，忙或遗留PID标记时需人工确认后重启，ready等待绑定本次supervisor存活；保留自动重启、档案恢复与既有认证/备份行为。
6. resource_control status仅给busy/非权威最后记录，不能凭PID不活就宣布空闲；reserve限时1..3600秒、SIGINT/SIGTERM退出释放，SIGKILL由OS回收。没有实际CUDA资源测量。
7. 真实子进程测试：独占、共享FD、父关/父杀但子仍持锁、最后引用释放、不同STATE仍冲突、伪造FD/nonce/模式拒绝、忙时入口在Torch前停止、日志/停止/重启/信号回归。
8. CPU/HTTP/本机CLI与既有全量三轮、Go竞态三轮、浏览器三轮和最终step8完整Python复制。保留step1–7、正式工作台15文件/1MiB及所有失败/中止记录。
9. 独立step8包/清单、阶段审查与完整交接；真实GPU/模型/训练仍blocked，只按真实证据更新300项清单。

## 明确未完成

不是硬件级GPU隔离或跨UID/跨容器协调，不能约束绕过协议的外部进程；同UID恶意替换文件不属于安全隔离承诺。旧step1–7进程不会自动采用新协议，升级前必须手动停干净。没有自动推理↔训练切换/排空会话、GPU编码、训练器、DDP/梯度/优化器/检查点或实际显存/速度证明。原训练码完整来源清单封存和训练使用租约仍是后续任务。
