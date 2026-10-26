# G0第11批：候选／文本／校准版本冲突的真实TCP组合

## 结论和进度口径

- **G0与整体仍为PARTIAL/BLOCKED；产品未改、声音优化未实施、S1–S8未实施，不跳Q28，不发布18。**
- 全源53/53资产的三遍语义阅读已完成，每遍13668行；原3×100建议和300条处置说明保留。
- 75/300条建议现在至少有关联的部分限定证据，即25%证据映射覆盖；这不是整体完成率、修复率或功能签收率。最终／功能签收仍为0/300。
- 本批补充版本组合证据，不是新的3×100建议或真实模型三轮验收。没有用户原始声音可供听感判断，不能推断沙沙根因、相似度或提速成功。

## 1. 测试边界

`kaggle/tests/test_version_http_boundaries.py`新增12个unittest方法，8项限定保护、4组未修观察。复用冻结的`input_http_fixture.py`，每个场景只运行一个Uvicorn服务器及一个事件循环，通过httpx真实环回TCP调用原analyst.app。

与上批不同，本批恢复原`analyst.load_on_workers`，原pin比较和`calibrate_profile`实际执行；仅worker传输、合成、ASR及说话人评分为可控替身。临时WAV、固定文本及人为分数不是声音模型。重叠通过HEAVY执行器中的worker/ASR Event屏障实现，事件循环仍能处理另一HTTP请求。不是在同步写盘里阻塞事件循环、不是双服务器，也不是随机线程压力。

fixture传输返回的ACK不能证明模型实际重载。没有经过Go鉴权代理、浏览器、真实麦克风／扬声器、DeepSeek、Torch/Qwen、CUDA或双T4。

## 2. 新增12项的实际结果

首次预检12/12通过，原stdout和结构化结果保存在`version-http-precheck-first.{txt,json}`。8项保护只签下表所列范围：

| 保护范围 | 结果及限制 |
|---|---|
| 串行先候选后文本、先文本后候选 | 两个顺序均保持当前选择对应的参考字节／转写／pin；不等于多文件事务合同完成 |
| 两方向HTTP重叠编辑 | 旧reload的pin失配被原检查挡为503，后一个编辑成功；不能笼统说所有候选／文本并发都无保护 |
| trained档案三入口 | candidate/text/calibrate均409，不启动校准或worker重载 |
| worker ACK错误pin | 原reload拒绝，HTTP503并保留reference_saved语义；不是回滚或真实worker测试 |
| 稳定fixture校准 | 固定两候选、4次合成评分，chosen1且临时目录清理；不证明真实评分质量 |
| 全合成错误的临时清理 | 仅签临时清理；原接口可能200/chosen0，不签有效校准 |

4组未修观察：

| ID | 真实交错与见证 | 不能推出的结论 |
|---|---|---|
| S2-TCP-O01 | 同profile两变更占满HEAVY后，第三text和第四candidate均429，但分别已改变磁盘；前两reload最终503 | 不等于每profile锁、可回滚或429有reference_saved合同 |
| S2-TCP-O02 | 原校准已用旧文本完成评分，在ASR释放屏障期间通过真实HTTP选候选、改转写；最终校准200，旧评分仍被保存 | 新转写保留，不是被覆盖；没有真实错声音证明 |
| S2-TCP-O03 | 同名cand1.wav旧SHA被评估，屏障期间换为另一份自有候选bytes，最终200并把新SHA复制进anchor | bytes由自有文件fixture修改，不是HTTP上传或远程任意文件利用 |
| S2-TCP-O04 | 校准提交前真实HTTP DELETE成功，校准500而非4xx；没有复活档案，临时目录清理 | 不证明adapter状态变化路径；500不是功能成功 |

这些补充而不改写旧F33/F34等历史。尤其R1-016现已区分普通编辑已有pin保护和校准组合仍缺冲突响应，不将旧相关证据扩大为所有路径均失败。

## 3. 三轮回归收据

使用全新命名的`run_version_http_cpu.py`，不覆盖第10批runner或日志。

- CPU **450×3＝1350 PASS**；每轮failure/error/skip均0。
- 逐轮保留旧438个test ID和结果，追加本批12项。旧21组观察保持，追加4组，共25组／轮。
- 每轮85真实TCP请求＝旧61＋新24；三轮合计255，其中新增版本组合72。不要把上批183再次加作本批请求。
- 每轮状态计数：200×32、500×17、400×16、422×6、404×1、409×6、503×5、429×2。错误响应可能是未修观察，测试通过不是该行为满足产品合同。
- 新24请求／轮为200×13、500×1、503×5、409×3、429×2。
- companion每轮NumPy partition12、trimmer8、CLI4；三项CLI期望blocked，resource `gpu_verified=false`。C ABI故障fixture不是Rust编译／执行。
- 运行期间后台等待连接曾中断，未重启CPU；随后读取原日志及当时仍在运行的第三轮，三轮收据完整生成。一次tail通配检查命令误用已单独记录，非测试失败。见`version-http-execution-notes.json`。

附加审计、Node、JS、repack和AST检查及独立封存结果在本报告末尾记录；必须以实际收据核验，不挪用历史通过数。

## 4. 原建议精确映射

`version-http-recommendation-links.json`关联12条原建议：R1-012/016及R2-031/032/033/034/035/037/038/040/049/062。每条保留原文，列出新测试全ID、三轮收据SHA和HTTP case数组下标，并单独说明证据边界。

此前并集70，本批新增进入并集的5条是R2-034/037/038/040/049，现为75。其余7条是对已有部分链接的加强，不算新增建议、修复或最终签收。R2-033仅见旧转写评分沿用，新转写没有被覆盖；R2-040仅见删除，不签adapter变化；R2-049没有覆盖所有异常路径。原300条处置及最终false字段不改。

## 5. 冻结、历史与环境

- 53源资产、94冻结哈希、正式HEAD及15文件保持；原始–17包不改，无18生成包。仅允许`repack --check`。
- `version-http-preserved.json`共1317期待历史路径，1314已有文件SHA匹配、0变更、3旧.log缺失。D02仍在，`full_historical_integrity_passed=false`；不补造、不拿新日志替代旧日志。
- 沿用现有`.venv`，本批无依赖安装，当前pip freeze与第10批逐字节相同。NumPy2.2.6仍非requirements2.4.6，不签目标部署依赖。
- 无Go/Rust/npm安装，无Torch/Qwen或完整模型，未重跑Go/race/vet、实浏览器／clipboard、实体音频、模型训练或声学性能。历史浏览器／复制证据仍保存，不冒充本批重新验证。
- 独立清单保存本批日志、代码及报告SHA；完整交接目标为91份。清单、独立核验及交接结果见末尾。

## 6. 下一步与禁止提前宣布的结果

继续按原300建议补齐仍缺的精确合同与门禁处置。后续产品修复重点应是：校准输入内容快照及提交冲突检查、每profile状态协调、HEAVY准入早于写盘、删除与失败的明确响应；已有普通编辑pin保护必须保留。仍需完成G0门禁后才能实施声音优化，不能把更多模拟测试包装成优化落地。

更快真实首声、全部候选分析／conditioning可追踪、generated-only PCM、自然连续朗读、无沙沙、长录音真训练、受保护的更响输出、双T4等效参数及RTF≤0.3都未豁免。必须在真实模型／设备／音频上验证，不能承诺一定成功或给出可信整体百分比。


## 7. 封存检查记录

附加检查已实际执行三轮：每轮24项审计、Node30项、JS语法、repack检查全部通过，40份Python AST解析通过。封存前独立复核已核对CPU逐ID／结果继承、三轮TCP内容／观察、全部引用日志及SHA、建议下标与环境，首次通过，原stdout为`version-http-seal-preflight-first.txt`。

本批独立清单`version-http-run-manifest.json`覆盖89文件；完整交接为91份，每份内嵌全文与原文件核对。最终封存判据为`verify_version_http.py`连续两次独立执行通过且输出逐字节一致；实际输出保存于`version-http-verification-first.txt`和`version-http-verification-second.txt`，正式结果以`progress-version-http.json`为准，并同步`progress-checks.json`。这些核验只签审计证据与冻结边界，不签整体G0、功能、模型或声学完成。
