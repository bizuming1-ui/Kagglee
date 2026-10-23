# 第八阶段审查：合作式GPU资源准入，不是自动训练模式

> 第八阶段冻结证据；当前源码/重打包入口为step10，见KAGGLE_STEP10_AUDIT.md。以下保留当时结果，不代表真实GPU或训练验收。

2026-10-21。先保存STEP8计划与Q7的50条建议，再增量实现。**本阶段验证的是Linux进程/描述符/flock协议，没有实际CUDA、显存释放、模型、GPU编码或训练验收。**

## 交付与保留

- 独立`kaggle/kaggle-fixed-step8.py`：230559字节、37资产，SHA256 `777c1d523559c9c734cd5e99841810524284e91269ced23963e8e5ab3f3cc1e1`。清单source_manifest_step8.json；repack.py默认生成step8。原始与step1–7冻结。
- 新增`py/gpu_ownership.py`及`tools/resource_control.py`；增量接入supervisor/worker/analyst与bootstrap；离线CPU编码只增加内部描述符环境清理，没有改成GPU编码。
- 生产JS/HTML/Go未改，仍两主视图及辅助库窗口。命名空库、逐条输入/授权隔离、参考处理、档案恢复、录音/播放/打断、认证、备份和工作台功能保留。
- 正式工作台15文件1043155字节、1MiB余5421字节、HEAD不变；全部15SHA256与第七阶段收据逐一匹配。新包独立交付，不塞入满额工作台，不提高上限或删除旧文件。

## 具体实现与证据

| 项目 | 实现 | 证据与限制 |
|---|---|---|
| 命名空间 | 固定/tmp/qtts-gpu-ownership-{uid}/fleet.lock整组独占，不随STATE或CUDA_VISIBLE_DEVICES变化 | 同机同UID合作协议；不是按GPU设备号或跨容器/跨UID的系统隔离 |
| 文件安全 | 0700目录/0600普通文件，属主/软硬链接/权限检查，锁文件永不被应用删除或替换 | 同UID恶意改文件及外部/tmp清理不在保证内，操作员不可删除资源锁来“恢复” |
| 权威 | 非阻塞原生flock；记录含模式/PID/nonce/创建时间，status不公开nonce且明确record_is_authoritative=false | PID死亡/记录过期/记录损坏都不表示可抢占，只有flock观测有意义；status是瞬时观测不是预约 |
| 持锁继承 | 真实supervisor先取inference租约，仅worker/analyst通过pass_fds继承同一OFD，校验inode/nonce/模式/锁 | gateway不持锁；不是任意外部进程管理器，正常模型进程必须按本版本启动 |
| 最后引用 | close只关闭本进程FD，不发LOCK_UN；父关闭或被SIGKILL，活孩子仍持锁 | 实际fork/exec/父杀/最后引用关闭测试；未证明CUDA驱动内存此时已经同步回收 |
| 模型入口 | 真实worker/analyst在任何模型加载前采用或取得租约；无继承时独占整组 | 多worker应由supervisor启动；第二套真实服务或离线预约busy；Mock明确不取得GPU租约 |
| 生命周期 | 父日志FD及时关闭；kill等待leader退出并清理幸存后代；停止信号提前注册，停止期间不再重启 | 真实进程与模拟故障测试；现有重启/档案恢复/认证与备份逻辑保留，不是优雅排空会话 |
| PID文件 | 第二真实supervisor占用失败前不写supervisor.pid；成功运行后只清自己的标记 | PID文件不再作为资源所有权依据；旧版本标记须人工核实迁移 |
| 引导安全 | bootstrap不再按旧PID或pkill广泛杀进程，busy/遗留标记时启动前阻断；ready等待核对本次supervisor仍活着 | 有意改变自动停旧服务的行为，避免PID复用/旧健康假阳性；不是自动在线模式切换 |
| 离线预约 | 本机status及reserve --seconds 1..3600，超时/取消/进程死亡释放，busy返回2/code409 | 仅空闲预约，不执行任何GPU任务，不代表显存、编码或训练成功；无shell/HTTP/force-unlock接口 |
| 原CPU入口 | encode_training继续仅CPU，剥离GPU FD/nonce环境，不继承资源描述符 | 真实编码仍缺Torch/qwen_tts/权重blocked；fixture仍test_only_codes |

## 本机操作与升级顺序

以下是目标环境操作说明，不是沙箱已经运行真实GPU的证明。新包会写入QTTS_ROOT源码，**升级前先确认所有旧版本GPU服务已停止**；仅检查必须用独立QTTS_ROOT与QTTS_UNPACK_ONLY=1，不要覆盖运行中版本。

```bash
ROOT=${QTTS_ROOT:-/kaggle/working/qtts}
python "$ROOT/tools/resource_control.py" status
python "$ROOT/tools/resource_control.py" reserve --seconds 5
```

- `status`返回busy/last_record/observation_only/gpu_verified=false。busy=false只表示此刻合作锁未被持有，不能证明硬件空闲，也不保留资源。
- `reserve`成功先输出offline_reserved，期限结束输出released；正常0，busy/拒绝2，SIGINT/SIGTERM取消130，SIGKILL由系统报告。全程training_verified=false，没有命令执行或GPU负载。
- 正在真实supervisor/worker/analyst持锁时预约应拒绝。先通过受控进程的正常停止途径终止本应用，等待所有模型孩子退出，再预约；本CLI不自动杀推理、不按旧PID抢占。
- supervisor被强杀但孩子存活时，busy仍为true是安全行为，不能删除fleet.lock/目录强行绕过；需核实并停止遗留的本应用模型进程。仅一个父PID已死不能推断没有孩子。
- 同UID整组锁有意保守：即便机器有更多GPU或子集不重叠，也只允许一套受管推理/一个离线所有者。与GPU索引/UUID如何重映射无关。
- 真实多worker与analyst应由supervisor统一启动。独立启动worker会单独占整个整组租约；第二个独立模型进程会拒绝，不再将多次手工启动当受管多卡。
- 旧step1–7或其他软件没有自动加入协议，升级前必须停干净并检查实际进程/GPU。若bootstrap报遗留supervisor.pid，仅在确认旧服务停止后清理这个**运行时PID标记**；不是删除资源锁，更不是修改正式工作台HEAD或历史。
- 不在真实STATE混跑Mock与真实服务。CPU测试及浏览器全部使用临时隔离目录；Mock不宣称GPU所有权。

当前没有自动“推理↔训练”切换、请求排空、任务取消后恢复旧模型或GPU编码。`offline-reservation`不是`training`；CPU编码仍然可以与该预约同时运行，因为它不调用GPU入口。

## 验证记录（docs/validation/step8/）

- Python新增32项资源/入口/引导/进程测试＋step7冻结回归，合计179项，最终179×3＝537通过。python-round1/2/3.txt。初检ownership29项通过；扩展bootstrap安全回归后32项通过，全量初检179通过。
- 所有权测试用真实fork/exec/flock/文件描述符/父SIGKILL/子继续存活/最后引用退出，不只Mock布尔状态。另有真实worker/analyst入口在离线锁占用时、Torch导入前拒绝，以及真实第二supervisor不覆盖PID文件。
- ownership-process3.txt：真实supervisor/Proc/pass_fds/正常停止协议三轮，两个worker角色和analyst继承、gateway不继承，在线预约409，停止后可预约。**角色均为CPU stand-in，没有真实模型/GPU工作**。
- Go28顶层/16子测试race三轮、Node API30×3通过。
- training-http3.txt：真实Go→analyst→磁盘三轮，旧库负向解码/原始哈希保留/训练输入独立副本/编码读取租约HTTP删除409仍通过，没有新模型作业。
- codes-cli3.txt：本机CLI/存储三轮，码全为fixture；缺依赖真实入口三次blocked，无真实权重加载。mock-pipeline.txt：两CPU Mock worker有序分段/取消恢复三轮，非真实GPU/音质。
- browser-repeat3.txt：60 QTTS＋48工作台＝108唯一×3＝324通过（10.5分钟）。含第八阶段230559字节完整Python剪贴板逐字节相同三次，且step7内容保留；final-copy-repeat3.txt另专项3/3通过。均为隔离临时项目；生产网页未改，不新增主视图。
- 37资产与原始22哈希确定性repack --check、语法/compileall/diff检查通过。runtime-probe.json仍blocked/退出2，缺Torch/后端/ffmpeg；没有模型或GPU验收。

## 复审、环境恢复和行为变化

- 本轮环境没有持久化.venv/node_modules（它们本来就不进入快照）。首次语法命令因缺解释器退出127，随后按既有CPU requirements/npm lock重新安装，日志requirements-install.txt/npm-ci.txt。没有安装Torch或GPU模型，没有修改GPU依赖宣称可运行。正式工作台在恢复服务前后均逐个哈希核对未变。
- 审查发现旧bootstrap的stop_old会按PID发SIGTERM并运行宽泛pkill，且等待可能读到旧健康服务。没有保留危险自动杀行为：改为启动前明确阻断、用户确认停止，并加本次supervisor存活检查；有对应回归，不把它写成“自动模式切换”。
- 初检及三轮目前无测试失败或隐瞒中止；所有初检/专项/最终日志分别保存。不把依赖blocked当模型通过。

## 清单、未完成项与下一步

- 仅新增勾选R2-010的**设计与合作式协议证据**，累计22/300。不勾R2-001/003/006/009/011等自动模式/显存/实际rank条目。专业自问自答7×50＝350建议，不等于350修复。
- 没有真实GPU/VRAM释放或实际模型，锁不约束不合作软件、其他UID或容器。没有CUDA级设备隔离，不承诺当前资源预约能防所有OOM。
- 尚无本次作业代际ID贯通各健康响应；supervisor存活检查不等于所有新网关/子进程就绪，旧端口占用仍须排查。bootstrap内的前置检查也不能替代运行单文件解包前确认旧服务已经停止。
- 未实现自动在线模式切换、GPU编码、文本tokenizer/真实训练器、梯度/optimizer/loss/检查点/训练后推理。
- 原码副本只保存源输入ID/hash，没有完整来源/授权清单副本；真正训练前仍须补来源封存与码副本训练读取租约。当前输入租约不等于训练作业使用锁。
- DeepSeek、物理麦克风、真实压缩容器、音质、首声<3秒、RTF≤0.5或99.5%目标仍无验收证据。
- 下一步优先封存码版本来源/授权与训练读取租约，再接受控离线任务和目标硬件的真实encode/decode/显存回收测量；只有这些门禁通过，才能接真正两rank优化器与检查点，不能用预约/缓存或进程数代替训练。
