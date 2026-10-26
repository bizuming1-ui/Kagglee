# G0 全源第三遍第2批：参考分析、库API与档案事务

日期：2026-10-23；分支 `arena/1160bd87-kagglee`。

**第三遍累计12/53份、3860行，剩41份9808行。前两遍各53/53、13668行保持。产品未改，G0仍PARTIAL/BLOCKED。**

## 1. 本批全文复读

| 文件（相对 kaggle/source/） | 行数 | 交叉核对重点 |
|---|---:|---|
| py/analyst.py | 1211 | 解码/清理、ASR时间与候选、缓存/centroid、档案提交、worker重载、校准及文本/候选API |
| py/library_api.py | 163 | 严格JSON、原始库修改、准入/租约与后台线程handoff、结果提交 |
| py/persist.py | 99 | 本地打包/恢复范围、临时档案排除、远端备份入口与失败语义 |
| py/reference_segments.py | 106 | 16/24秒合同、词级切分、窗口重识别、可选words和短尾 |
| py/voice_library.py | 351 | 私有文件、revision、flock、snapshot/begin/finish、失败后旧结果与租约清理 |
| **本批合计** | **1930** | **5份均重新完整阅读，无源输出截断** |

analyst按1–245、246–490、491–735、736–980、981–1211分段读完。其他四份完整读完；辅助旧测试组合输出曾截断且一次检索使用了不存在的测试文件名，已改查实际test_libraries.py与相关范围，不给这些辅助测试全文信用。all_three_complete仅表示对应文件三遍语义阅读记录齐全，不表示问题修复/质量签收。

参考链仍是：最多24候选预排/嵌入评分、最多3份落盘、实际单锚点ICL；centroid是分析空间统计，不是原生Qwen多参考融合。长输入接受、分析覆盖、参考提示、真实训练是不同事项，`all_audio_used_as_model_prompt=False`和`model_trained=False`保持。breath bank被提取不等于播放参考PCM，generated-only要求不变。

## 2. 新增12项合同：10保护＋2未修观察

`kaggle/tests/test_pass3_reference_boundaries.py`实际执行原ASGI路由、HeavyAdmission、CPU线程、文件、flock和tar。模型、ASR、speaker评分及worker回执是显式fixture。

| 合同 | 验证及边界 |
|---|---|
| 候选复制失败 | HTTP500、旧profile/pin不变、不reload；不是成功提交 |
| 候选JSON提交失败 | 旧选中profile/pin保持、不reload；**新anchor副本残留，不能称完整回滚** |
| trained档案三类变更 | text/candidate/calibrate均409，文件不改；只有metadata fixture，非真实adapter验证 |
| snapshot遇BaseException | 自有租约FD关闭、blobs清空，后续修改不busy |
| snapshot顺序/归属 | 明确选择顺序保留，先读合法后遇foreign样本仍释放租约 |
| 只读snapshot | 已准备结果、revision、元数据字节不变，training/inference验证仍false |
| 本地稳定pack/extract | 所有参考字节/pin一致，active一致；排除_cal与原始libraries，非并发/远端证明 |
| 归档末尾非法成员 | 链接/FIFO/设备成员在写前拒绝，不覆盖已有active；不是磁盘IO失败事务保证 |
| DELETE重复revision | 两个同值字段仍400，存储删除函数不调用 |
| 24秒词级分段 | 完整可信词时间切成两个24秒段，原始数据不改、不调用窗口ASR；不是语音对齐模型验证 |
| F33 | Heavy拒绝已晚于磁盘变更，详见下节 |
| F34 | 校准旧评分提交到新转写版本，详见下节 |

## 3. 两项新增未修问题

### F33：接口返回429时，参考已经保存，但未报告reference_saved

用两个真实执行器CPU线程占满原HeavyAdmission(2)，保持占用期间通过实际ASGI分别调用原text/candidate路由。

- text先原子写入新ref_text和对应candidate.text，再尝试HEAVY.run；返回429，但磁盘pin已变。
- candidate先复制cand1到anchor_1、更新profile anchor/index/ref_text，再尝试HEAVY.run；返回429，但磁盘选择与pin已变。
- 两次响应都未包含`reference_saved`，worker reload函数未执行。最后自有线程结束、两个名额可重新获取。

这是**拒绝语义与持久化状态不一致**：不能把429解释为未发生修改或盲目重试。与原有“保存后worker失败返回503/reference_saved=true”的合同不是同一条路径。没有执行真实模型/worker，没有证明用户已经听到旧声或错声。需在修改前完成准入并在合适的档案版本合同内提交，或明确返回已保存但未加载的事实，不能只改状态码掩盖资源所有权。

### F34：文本改版后仍提交旧candidate评分，不产生版本冲突

执行原校准API，用两个候选、四次合成/ASR/声纹fixture评估；四次均使用旧候选转写。通过结束释放钩子控制交错，在评分后、提交前调用实际text ASGI接口。文本编辑在第二个Heavy名额内成功，磁盘pin随新转写改变。原calibrate随后重新读取新版profile，保存旧评分并返回200/chosen0；最终新转写档案带着旧版本calibration。

两个接口均200，临时_cal目录已清理；旧转写未覆盖新转写，但**旧评分被附加到未按该版本评估的新档案**。这是版本/评分溯源缺口，与F19临时目录碰撞不同，不重复编号。合成、ASR、speaker数值与worker ack全部fixture；0.9等评分不是测得的相似度，不能据此证明实际音质/错误音色或双GPU一致。

F33/F34三轮复现，均未修。F01–F32、D01、F17备份交错、F19/F20校准/重载、F24模式绑定等继续保留，不因本批测试通过而关闭。

## 4. 三轮验证与封存范围

| 项目 | 第1轮 | 第2轮 | 第3轮 |
|---|---:|---:|---:|
| CPU/ASGI/进程/文件合同，原378＋新12 | 390 PASS | 390 PASS | 390 PASS |
| 其中新保护/未修观察 | 10/2 | 10/2 | 10/2 |
| 失败/错误/跳过 | 0/0/0 | 0/0/0 | 0/0/0 |

共1170通过；新保护30次、未修观察6次。预检12/12通过。后台三轮正常exit0，无监听端口；各轮测试身份与F33/F34观察一致，自有线程/准入槽/临时目录清理核对。

**本批未重跑Go（含F31及独立F02）、浏览器/Player与latency VM、独立ASGI2.3、CLI四项、NumPy分块/裁剪器探针，不挪用旧成绩。** CPU合集含原ASGI、HTTP、进程、锁、NumPy和档案合同，F32认证FIFO见证等实际重跑；模型和特定调度角色仍为明确fixture，不是全功能或目标模型验收。

Node30、JS检查、38份Python AST（33产品库存＋新测试＋4审计脚本）、repack通过。795份历史SHA、53源资产/94冻结哈希、正式HEAD15文件保持；pip freeze与第三遍第1批完全相同，无新增安装。Go可用但本批未执行其套件；Rust/Torch/Qwen不可用，实际训练/双T4/物理音频/声学/提速未签收。

独立校验首版曾误用收据字段modules（实际targets），AST准备也曾只计source/py24而漏了tools9。首错原始日志和correction说明保留，改正校验接线/实际交接格式后exit0；没有修改产品/测试/runner、没有重跑或改写三轮收据。最终manifest28项，历史795份另行逐项核对。

## 5. 原300建议的部分证据链接与待实施顺序

本批为10条原建议建立`pass3-reference-recommendation-links.json`；与上一批去重共16个原建议ID有暂定链接，**不是16条完成**。原文及原处置不修改，specific_row_test_signoff/final_disposition_signed_off/product_fix_implemented全部false。涉及R1-012/013、R2-029/031/032/035/039/062/077/094。

下一实施阶段应先完成以下合同，当前仅记录、不改产品：

1. 明确每档案的内容版本，包含候选集合/文件hash、转写、gen和conditioning模式。
2. text/candidate在持久化前取得准入；取消或准入失败不得偷偷提交，保持原始引用。
3. 提交与reload分阶段给回执，区分未修改、已保存未就绪、已在所有worker核验。
4. 校准开始捕获全输入版本，提交前CAS核对，变化则冲突/废弃结果而非静默采用旧分数。
5. 将校准结果按内容身份关联候选，不仅存数组下标。
6. 记录每候选预期/实际有效生成数、评估算法/模型版本与缺失指标，不把缺CER默认值当已验证发音。
7. 覆盖校准与转写/候选/删除/训练模式变更的同档案并发矩阵，保持旧成功结果和可重试状态。
8. 区分单文件replace、候选副本和多文件事务；对提交失败的新anchor孤立文件明确回收策略。
9. 保持trained参考不可变和409，不用宽松转换绕过固定版本。
10. 保留只读库快照顺序/hash/租约语义，取消后不提前释放仍在工作线程使用的资源。
11. 稳定本地归档回环只作基础保护；继续解决F17并发快照与恢复预算/失败部分提交，不宣称远端隐私/持久化完整。
12. 在全源第三遍与300最终映射完成前不跳S1，更不能用统计中心、参考缓存或fixture替代真实训练/多参考条件贡献/音质验证。

## 6. 当前检查点与下一步

`g0-pass3-reference-coverage.json`、`g0-pass3-reference-findings.json`、三轮原始收据、manifest、`verify_pass3_reference.py`、`progress-pass3-reference.json`为当前证据。交接完整内嵌82份。

下一批继续第三遍训练输入/声学码/训练产物与持久化绑定，核对输入来源、租约、失败/取消提交和实际训练边界；之后完成余41份及300最终处置映射。长录音真实训练、参考贡献追踪、首prefix立即调度、自然连续朗读、无沙沙、双GPU等效参数和真实RTF≤0.3等要求均未豁免。产品保持冻结，不生成18包，不跳Q28，不要求用户点击Continue。
