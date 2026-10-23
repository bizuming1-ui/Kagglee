# 第九阶段计划：来源封存与码版本读取租约

2026-10-21，编码前保存。接续第八阶段资源协议，不执行GPU任务或训练。

## 推荐选择与边界

新码版本使用schema2，原样封存输入manifest及train_raw.jsonl，按输入固定hash和原索引hash交叉验证来源库/修订/样本/音频/逐条文本/统一参考/声明/分配计划。schema1历史码继续可列表、核验、读取和删除，但明确legacy-unsealed，不自动补写或伪造缺失授权。授权仍是用户声明，不是法律/声纹证明。

新增TrainingCodesStore.lease固定版本完整核对和进程读取租约，供将来训练器/当前检查工具使用；租约期间删除该码版本409，其他码版本仍可列表核验。租约不是训练许可，fixture和legacy状态不会因此升级，GPU锁/真实训练门禁独立。

## 实施顺序

1. schema2新输出增加source/manifest.json及source/train_raw.jsonl，保存完整原始输入清单字节，不重写来源或声明。rank计划与全部规范WAV仍原样复制。
2. 封存源manifest SHA256等于创建请求固定hash，源JSONL/计划hash等于源清单；逐项与当前码样本ID/帧数/audio/text/ref/成员顺序交叉核对，拒绝篡改或遗漏。
3. source目录纳入字节预算、安全文件集、0700/0600、链接拒绝、原子发布/回滚与完整验证。仍不自动Dataset备份。
4. 读取兼容schema1，不修改旧清单/hash；列表只显示schema政策，不能在未读文件时宣称当前来源完整。完整校验才返回provenance_verified_now。
5. 目录外.use-{id}进程锁，先固定manifest hash并完整核验，再释放全局锁后yield只读上下文；同版本读取首版独占，最后进程退出释放。删除同版本明确409，不用PID或TTL强制抢占。
6. CLI增加hold-read --seconds 1..3600，只保持检查租约，不执行命令/GPU/训练，不输出私人清单/转写；沿用父总超时、SIGTERM/INT与PDEATHSIG。返回收据不能把读取叫训练。
7. 真实文件/源删除后溯源/旧冻结schema1/损坏交叉链接/缺文件/权限/回滚/预算/多进程/退出/超时/取消/备份排除测试。CPU fixture仍test_only_codes，训练标志不改。
8. 全量Python、Node API、Go竞态、真实HTTP/旧CLI/资源FD/CPU Mock三轮，浏览器全量三轮与step9完整源码复制。保留原始至step8及正式工作台15文件/1MiB。
9. 独立step9包/确定性清单/审查/完整交接；未实际GPU/编码/训练的部分如实blocked，300项清单只勾证据覆盖项。

## 不做

不自动迁移旧码、不从当前库猜旧授权、不开放私有来源HTTP下载/上传或任意命令、不宣称read lease是训练任务。没有自动模式切换/GPU编码/文本tokenizer/DDP/optimizer/梯度/检查点。跨UID恶意进程、原件安全擦除、断电耐久、实际GPU/音质/性能未验收。
