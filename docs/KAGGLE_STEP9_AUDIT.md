# 第九阶段审查：完整来源封存与码版本读取租约

> 第九阶段冻结证据；当前源码/重打包入口为step10，见KAGGLE_STEP10_AUDIT.md。以下保留当时结果；旧verify_delivery只适用当时源码，不据此称当前训练尚无实现。

2026-10-21。先保存STEP9计划与Q8的50行动建议，再增量实现。**只验证来源文件与合作式读取生命周期，没有执行真实Qwen编码、GPU或训练。**

## 独立交付与保留

- `kaggle/kaggle-fixed-step9.py`：233074字节、37资产，SHA256 `8ec892dcc5ca10daf20c8de84dd2be08d9a3de8807872c2051ddf52bd5882a9b`。`source_manifest_step9.json`与确定性重打包相符。原始与step1–8冻结；默认repack只生成step9。
- 仅修改生产`py/training_codes.py`、`tools/encode_training.py`及MEMO；无新生产语言、模型依赖、HTTP端点或训练按钮。生产JS/HTML/Go与GPU整组FD协议不改。
- 两主视图、命名空库/样本、授权隔离、逐条转写、输入准备/输入租约、旧参考处理/档案恢复、录音/播放/打断、认证/备份及工作台原有编辑/命名/复制/保存均保留回归。
- 正式工作台仍15文件1043155字节，HEAD `39ed7670-ec8a-4565-a1ae-fff0064d5246`，1MiB余5421字节。新包不写正式工作台、不提高上限、不删历史；浏览器用临时项目。最终只读核对全部15个SHA256及HEAD匹配上阶段，见本阶段formal-api-readonly.json及delivery.json。

## 来源封存设计

| 范围 | 本次实现 | 边界 |
|---|---|---|
| 新版本 | schema2新增`source/manifest.json`与`source/train_raw.jsonl`原始完整字节 | 不猜测来源，不从当前库重新补写历史声明 |
| 原始记录 | 保留源库ID/自定义名/修订、原始样本名/ID/hash、规范WAV/hash/帧数、顺序、文本hash/逐条原文、统一参考、使用权/单说话人声明及源检查记录 | 声明只是用户自述，不是法律授权、身份或实际单说话人鉴定 |
| 固定与交叉核对 | 源manifest hash等于创建时固定hash；原始JSONL和同一rank计划hash等于源manifest；所有当前码行的audio/text/ref与原始行一致；全部样本ID/顺序/帧数/audio/text hash一致 | 主清单固定hash是信任锚，非签名；持有写权限者可另造版本，新pin不是官方背书 |
| 安全/预算 | source纳入限定成员、拒绝软硬链接/嵌套目录、0700/0600、单份/总字节预算；准备时原子暂存/核验/发布，失败取消整份回滚 | 沿用已有预算和安全打开；不是同UID恶意并发写隔离或断电耐久保证 |
| 删除源之后 | 新码可独立核对封存记录，无需原库或输入目录仍存在 | 删原库不等于删码副本、备份或安全擦除 |
| 旧版本 | schema1继续列表/核验/读取/删除，明确`legacy-unsealed`，不重写旧manifest/hash | 不能声称缺失来源已恢复；测试静态提取冻结step8代码生成旧码，不执行旧安装器 |
| 列表与核验 | list的`source_provenance_policy`只说明schema政策，`provenance_verified_now=false`；本次完整verify成功且schema2才为true | 列表不是刚刚扫描全部文件；schema1结构verify仍不产生来源封存证据 |

不保留原库原始音频字节的第二份，只保留其hash/来源名；码目录中仍是既有完整规范WAV。原始JSONL包含私人转写，因此封存跟码副本一起保持本机私有，不新增HTTP下载，也不自动Dataset备份。旧profiles备份内容和语义不变。

## 读取协议与真实进程验证

1. `TrainingCodesStore.lease(id,pinned_sha256)`替代不适用于码格式的继承输入租约。全局锁内取得目录外`.use-{id}`独占flock，完整验证固定版本；取得码metadata/rows后释放全局锁再yield。
2. 长读取期间同版本删除/第二读取409，列表、完整核验和其他版本操作仍可进行。删除与读取共用外部锁，不在快照里添加运行标记。
3. 正常退出、异常、进程死亡由关闭描述符释放；不按PID/TTL抢占，不发LOCK_UN。真实fork继承FD在父上下文退出后仍维持锁，最后继承进程退出后可删除。
4. 这是合作式约定只读，不是OS只读挂载；返回本地路径给可信调用者，并不能防拥有写权限者恶意修改。只提供单版本独占检查原语，没有真实训练器或自动DDP多rank接管。
5. `hold-read`只保持1..3600秒检查租约，沿用控制器总超时、SIGTERM/INT、Linux PDEATHSIG/ppid握手，不提供任意命令/模型/GPU/HTTP执行。收据不输出完整源manifest或转写，`training_allowed=false`、`gpu_verified=false`、`training_verified=false`。
6. fixture读后仍`test_only_codes`，旧码读后仍`legacy-unsealed`；租约不是训练许可。未来训练器必须维持保护直到所有读者退出，并分别执行真实编码、语义/权利政策、硬件、训练门禁。不能把目录完整性当作真实人声/训练质量。

## 本机使用说明（不是目标GPU执行证明）

先用现有`list --state`取实际码ID/manifest SHA256，用固定pin完整verify，不能填虚构ID或拿输入manifest hash冒充码manifest hash。变量来自当前本机结果。

```bash
ROOT=${QTTS_ROOT:-/kaggle/working/qtts}
python "$ROOT/tools/encode_training.py" list --state "$QTTS_STATE"
python "$ROOT/tools/encode_training.py" verify --state "$QTTS_STATE" --id "$CODES_ID" --manifest-sha256 "$CODES_SHA256"
python "$ROOT/tools/encode_training.py" hold-read --state "$QTTS_STATE" --id "$CODES_ID" --manifest-sha256 "$CODES_SHA256" --seconds 5 --timeout 15
```

正常完成0，拒绝/总超时2（busy code409），SIGTERM/INT取消130，SIGKILL由OS处理。hold时间不含准备/核验，timeout含启动/核验；默认timeout1800秒，选择更长保持需显式提高至不超过3600秒，不能保证3600秒保持恰在3600总预算内完成。没有开始/结束训练、优化器或检查点。

升级前先停旧GPU服务再解包覆盖ROOT；仅静态检查用独立QTTS_ROOT及UNPACK_ONLY。第八阶段整组锁/人工处理旧runtime PID标记规则保留，不能删fleet.lock恢复，不把status空闲当实际显存空闲。

## 验证记录（docs/validation/step9/）

- 新增21项来源/读取测试与step8冻结回归，完整Python201项；最终201×3＝603 PASS，`python-round1/2/3.txt`。新用例涵盖精确字节封存、删源后核验、声明/文本/参考/样本hash/修订篡改、无关完整来源重绑定、成员丢失/多余/软硬链接/嵌套目录、权限/容量/失败/取消回滚、旧schema1字节/hash保持、同版本409与其他版本可用、坏pin/坏文件/异常释放、真实进程死亡/fork最后引用、真实CLI超时/取消/控制器SIGKILL与pidfd退出观测、拒绝无限时间/任意命令。
- 最终收据核对工具初版假定HTTP日志只含3条JSON，实际每轮输入/旧库两类共6条；改为按类型键分别确认3个round，不修改原日志，不算业务失败。`final-checks-initial.txt`保留，最终以final-checks.json为准。
- 初检原有33项PASS，新增测试初版20项中1项夹具错误：重复使用同一库名被正确拒绝；改为明确删除原库再建立新来源，20项PASS，再补fork继承最后引用成为21项。原错误日志保留，不包装为生产缺陷；完整初检201项PASS。
- Node API30×3、Go28顶层/16子测试race三轮PASS，JS语法/compileall/diff/repack检查PASS，npm audit报告0漏洞（不等于完整安全审计）。
- `codes-cli3.txt`本机真实CLI/文件事务三轮：schema2来源原字节、删输入/原库后独立核验、持锁删除409、长读不占全局列表、hold-read收据、删除/列表通过；码与门禁权重均为fixture，真实encode三次blocked_missing_dependencies，没有模型加载。
- `ownership-process3.txt`真实supervisor/Proc/pass_fds正常停止三轮PASS，worker/analyst均CPU角色替身；不是GPU或显存证据。`training-http3.txt`真实Go→analyst→磁盘三轮PASS；旧库损坏解码失败/原始hash不变/输入独立性及输入租约HTTP删除409仍通过。
- `mock-pipeline3.txt`双CPU Mock worker三轮PASS：有序段、取消恢复；不是双T4、真实流式模型或音质证据。
- 浏览器：109唯一（60 QTTS＋49工作台）×3＝327 PASS（10.3分钟），`browser-repeat3.txt`。软件输入录音/五CSS视口/两主视图与旧工作台功能保持，不扩大为物理麦克风/全浏览器或真实GPU训练聊天。
- 最终step9完整源码复制专项另3 PASS（9.2秒），`final-copy-repeat3.txt`；均临时项目，保存step8并逐字节比较233074字节step9原文，不改正式workspace。全量中也已覆盖3次。
- `runtime-probe.json`仍blocked/退出2，缺Torch/真实推理后端/权重；没有GPU、真实encode/decode、训练或性能验收。
- `.venv/bin/python docs/validation/step9/verify_delivery.py`只读核对冻结包/37资产/21完整内嵌备忘录/8题400建议/22of300/最终测试日志与正式15文件、HEAD，写final-checks.json及formal-api-readonly.json；需已有Node工作台3000运行，不重跑模型、不修改工作台。

## 三轮各100项与范围审查

本轮逐项保留原300清单的状态，映射记录见`review-map.json`，不是声称300项修复或验收。已勾选仍22/300，8题×50＝400行动建议。

- 第一轮100项：重点补强R1-079声明的可追溯保存，保留R1-073名称/内部ID隔离；R1-075/081/084仅数据文件层部分证据，真实人声、转写匹配/同说话人判断及训练效果不验收。没有扩大GPU/模型/依赖清单完成率。
- 第二轮100项：补强R2-031固定样本/哈希；R2-032只有码副本读期删除互斥，没有实际训练器对全部读者生命周期保护；R2-034保留原始JSONL/码来源，但文本tokenizer/真实声学码版本链仍缺。因此后两项继续不勾，DDP/参数更新/检查点全部不验收。
- 第三轮100项：回归两视图/录音/编辑保存及真实Python复制；新码来源可在删源后核验，但R3-074尚无已发布训练检查点，不能验收。完整包复制仅临时项目，不声称正式满额工作台已发布，也不把浏览器软件流当物理麦克风/真实聊天。

## 下一步与明确未实现

下一专业问题仍须先保存具体计划和≥50建议。推荐先设计受控离线作业的固定输入/模型/码pin、收据、取消/终止及所有读者生命周期，再接真实任务；检查/预约不能伪装为训练按钮。

真实目标门禁仍是可信Qwen模型的完整encode/decode/覆盖/内存/时间、T4环境与显存回收；随后才文本tokenizer兼容、真正world_size=2、两rank数据/梯度同步/optimizer参数更新/检查点及新进程重载试听。不能照搬T4不支持的BF16/标准FA2/全参数AdamW，不能凭accelerate两进程称训练成功。

DeepSeek、物理麦克风/容器、音质、可听首声/标准RTF与身份保留集均未验；不承诺永久会话、<3秒、RTF≤0.5或99.5%身份一致率。协议不能约束跨UID/容器/绕过协议的软件，不能防同UID恶意删改或证明真实显存可用。
