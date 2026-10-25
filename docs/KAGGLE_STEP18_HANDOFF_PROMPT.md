# 第十八阶段完整交接提示词（进行中）

## 当前优先状态

当前活动分支arena/1160bd87-kagglee，继承已合并的arena/03d65d8e-kagglee两轮审查；历史baseline保留原分支名，不改写历史。原始–17与正式工作台冻结。以下历史首页不是本阶段完工声明。当前累计内嵌111份完整备忘录，包括原57份及本阶段已完成文件。

**当前优先检查点（S5完成短尾/重采样/流epoch实际修复）：** 报告KAGGLE_STEP18_S5_PLAYBACK.md。Q32按四选项选C＋50行动、三遍各100建议先归档，未开33。新增完整kaggle/step18/web/app.js，从冻结17复制只改Player P和嵌入Worklet V；网络解析器/到达预测器/整个UI后缀逐字节保持，页面实际实例化新Player。完成任何正pending可play（初始20/50ms、1样本、starved恢复），未完成缓冲阈值保留。post目标总数−played−dropped计pending，当前epoch endACK且pending0才ended，旧fill0不提前结束；溢出单列不冒无损。全局整数坐标线性插值，末样本保持到ceil(Nin*rate/24000)，取消不flush；epoch拒旧状态/PCM和stop后复活，不改网络协议。firstPlayedMs仍play命令，不冒声卡/消费时间。极短1样本可能被淡入归零，仅计数消费不等于可听人声。

37VM旧红28失败/9保留，候选37、8源码和15真实Chromium预检全PASS。最终610CPU×3=1830PASS（旧602逐ID/结果保留）、37专项VM×3、173Chromium×3=519PASS（原158＋新15，0失败/flaky/skip/retry）；新15含9原生消费、3空/取消/换流、3完整UI合成HTTP到真实Worklet。真实浏览器headless/muted，不是实体扬声器/麦克风，HTTP/PCM/参考状态明确fixtures，无Go/模型/声学新执行。CPU源合同内也跑37VM，不能加总当独立功能数。最终24审计/Node30/AST58/JS/repack与两次seal见progress-s5。浏览器数分钟一轮原进程顺序等待，不因wait超时重启重复。继承237TCP/轮711，新S5无后端TCP。Python复用无安装；node_modules消失后本次确实npm ci --ignore-scripts按旧lock安装，package/lock/既有配置SHA不改。2049保护/2046匹配/3旧日志缺，完整交接111份，17/正式/S3S4不动，18未发未部署，整体PARTIAL/BLOCKED。8原建议限定链接不是原300最终签收。线性插值仅测24k/44.1k/48k，不冒任意降采样抗混叠；设备挂起/后台/队列溢出等仍有边界。下一步S6时序/诊断，保留字段含义，真实双T4/长录音训练/声学/首声/模型RTF和S3native门禁未豁免。直接继续无需Continue，不保证一定成功。

**上批历史检查点（S4有界裁剪与worker结束/取消实际修复）：** 报告KAGGLE_STEP18_S4_TRIMMER.md。Q31四选项选C＋50行动、三遍各100建议先归档，未开32。新增step18_trimmer.py与实际worker_s4.py入口；S3 worker.py/DSP不改以保留39旧合同。新worker只换裁剪器导入和Worker.run_job，其余函数方法AST相同。固定120样本网格残帧（24k下不足5ms）、跨块35ms前史、有界1800ms尾队列；中段静音超限顺序输出而非删除。正常finish处理实际长度残帧、保留缓存全部非零尾、仅裁计数精确零；取消/异常清缓存、不排衰减尾。finish返回后emit前重查取消，stats.trim区分输入/返回/丢弃/缓存与守恒，另记cancelled_after_trim_samples，不冒声卡播放原子取消。领先低电平历史仍可裁（仅保留前史），不能保证全部弱语音保留；非零尾也可含噪声。

候选裁剪30/worker10首次预检PASS；旧版红初41fail+1error为inf keep_ms旧OverflowError，严格ValueError合同保留但转成明确断言失败，最终42fail/0error/skip；初日志/测试/runner源码留档，不是42bug。完整602×3=1806PASS、0fail/error/skip，旧562逐ID和结果完整继承（S3 worker合同仍针对保留的S3入口）；旧237TCP/轮711，新S4无TCP，engine/pin明确替身。21矩阵×3对独立batch参考逐样本相等；601秒合成流×3各14424000样本，实达且守住43200尾上限，不保留PCM历史，不是真录音/训练。CPU约1.097–1.129秒/601秒合成音频，正确性开销比旧裁剪更高，不冒提速/模型RTF/首声改善。最终24审计/Node30/AST57/JS/repack三轮与独立两次封存以progress-s4为准。首次seal对旧S1删除/提交交错误要求与历史状态完全相同，实际原测试已允许200或503；只正规化这个精确test/path/method的既有两状态，其余严格核验，原CPU/测试不改。初verifier/日志/manifest已归档，最终附加检查另名s4-seal-final-checks。1905历史保护/1902匹配/3旧.log缺，不补造；本步复用venv无安装，freeze与S3一致；无Go/Rust/Torch/Qwen/模型/训练/声学新执行。5原建议仅限定链接、原300最终签收仍0。完整交接106份，17/正式工作台不动、18未发未部署，整体PARTIAL/BLOCKED、完整S3 native/声学仍未签。下一步S5播放器完成短尾排空，不把S4工程通过当真实自然无沙沙/同声/双T4/长录音真训练成功。直接继续无需Continue，不保证一定成功。

**上批历史检查点（S3因果 NumPy DSP 与隔离worker实际接入）：** 报告KAGGLE_STEP18_S3_DSP.md。Q30按四选项选C＋50行动及三遍100建议先归档，未开31。新增step18_audio_rt.py，唯一模块名连接隔离worker.py；全部worker命名定义AST与冻结17保持。固定RMS平方和/余数、逐样本30ms/600ms因果增益、淡入绝对位置，process立即同样本数返回，不等未来RMS；定义flush/关闭/非法参数。float64状态/ties-to-even，-46dB精确门限；与旧NumPy整段输出会不同。候选仅启用numpy-causal-v1，不装载未验收Rust，冻结Rust/ABI源码不动。旧版30合同44失败记录/0error/skip，候选30PASS；新worker9合同真实run_job/trimmer/DSP/frame，engine/pin明确替身。完整562×3=1686PASS、0failure/error/skip，旧523逐ID/结果完整保留；继承237TCP/轮，新S3无TCP。14分块矩阵×3输出最大差0int16且最终gain/env相等；601秒合成流×3各14424000样本、只有固定标量状态，不是实际长录音或训练。CPU小块较快而整段/1920较慢，长合成DSP约0.00976–0.01068 CPU时间/音频时长，不能冒模型RTF/首声/听感提升。不新增强降噪/参考PCM。首次worker预检4error为fixture缺dtype_name，只补替身、首错留档；旧极值float32溢出警告由最终红日志保存。最初附加检查成功收据保留、最终另名s3-final-checks三轮24审计/Node30/AST53/JS/repack。独立两次封存以progress-s3和stdout为准。历史保护1768/1765匹配/3旧.log缺，不补造；本次venv重建且freeze与S2-B相同，当前无Go/rustc/cargo/Torch/Qwen，后面的“沿用环境/Go存在”只属历史。完整交接101份，18未发布未部署，完整S3/native/声学及整体PARTIAL/BLOCKED。8原建议限定链接不等于原300最终签收。下一步S4 EdgeTrimmer短块/预滚/held尾/finish/取消，DSP守恒不代表原trimmer已无丢样本。直接继续无需Continue，不保证一定成功。

**上批历史检查点（S2-B有效指标与加载就绪实际实现）：** 报告KAGGLE_STEP18_S2_VALIDITY.md。Q29四选项选C及50行动先完成，未开30，原Q25–28／3×100保持。新增step18_calibration_metrics.py，分析服务相对S2-A仅改build_profile/calibrate_profile/calibrate，其余命名定义AST保持。逐目标缺失null／完整覆盖／有限ECAPA及ASR门禁，保留原排序公式但不再CER0.05／全失败chosen0。无完整候选422、不写盘、保旧报告；失败候选不影响其他完整者。临时HTTP／严格ok／pin核验；选择先提交再检查最终worker和保存版本，失败503/savedtrue/readyfalse，后改／删则saved_version_current=false，不虚构回滚。成功选择报告仍与磁盘一致，quality_verified=false；后台可选校准摘要源代码接入但完整创建未实测。公共错误采用固定码，不回显私有异常。短时长／声音阈值不猜测。

最终23合同对归档S2-A为36失败记录/0error/skip，候选预检PASS。首红34失败+1KeyError因新字段不存在，assertIn后红35，原日志保留。初三轮523PASS后复核发现int16最小值abs溢出，保存受控fixture，改min/max并补子用例，最终另名s2b-final三轮，不覆盖或混算初轮。初源码两份按记录SHA确定性逆变换重建且明确标识，不冒事前快照；真实S2-A改前快照为s2b-before/index。最终三轮／24审计／Node30／AST47／JS／repack及独立两次核验以progress-s2b.json为准，旧450冻结、旧50当前候选、新23当前候选。1609历史保护/1606匹配/3旧.log仍缺；冻结53/94/15及正式17不动，无安装、Go／实浏览器／模型／训练／T4／声学或提速新验收。12条原建议增加当前实现限定证据，有限并集75→81（27%仅证据覆盖、非整体进度），原300最终／功能签收0。完整交接96份，18未发布未部署，G0／整体PARTIAL/BLOCKED。下一步S3分块一致性与后端对照，S2跨进程／创建并发写者／极短音／真实模型门禁仍保留。直接继续无需Continue，不承诺一定成功。


**上批历史检查点（S2-A校准快照实际实现）：** 报告KAGGLE_STEP18_S2_SNAPSHOT.md。隔离18候选新增step18_calibration_state.py并修改calibrate_profile/commit_text/commit_candidate，S1其余命名定义AST保持；完整S1源码、README、origin及旧交接等改前已逐字节归档s2-before与index。短锁捕获完整元数据／候选／锚点／质心文件字节，试验只使用捕获内容；短锁内重核输入后提交，变化／删除／trained转变返回409且不应用旧评分。真实HTTP候选／文本ABA由修订nonce识别，相同重复选择幂等。每档案仅一校准、独立且长度安全的临时ID／700目录、仅清理自有目录、ASR释放finally。最多24候选／聚合文件64MiB，峰值副本内存另计；不声称跨进程／不合作写盘全局事务。S1同一新22合同对照21失败记录/0error/0skip，当前候选22预检首次全PASS；不是21独立bug。三轮完整回归和附加核验实际状态以progress-s2.json为准，分清旧450冻结控制、当前S2上重跑的28项S1及22项新校准合同。校准缺失CER0.05、全失败chosen0、非有限／覆盖率评分、最终worker回执仍未修，不能签完整S2、声音或真双T4。原300／三遍53源各13668行／Q25–28及50行动保留，未开29；新限定链接是已有集合加强，不用映射比例冒充整体完成率。1509保护历史路径中1506匹配、3旧.log D02仍缺，显式归档可变候选而不是伪称活源码未改；53源/94冻结/15正式及17包不动。环境无安装，freeze沿用，无Go/实浏览器/模型/训练/双T4/实体音频/声学性能新验收。完整交接94份，默认服务／复制页仍17、18未发布、G0与整体PARTIAL/BLOCKED。下一步S2-B有效评分／全失败拒选／加载回执，随后才推进DSP等；直接继续无需Continue，不保证一定成功。


**上批历史检查点（S1隔离候选实际实现）：** 用户要求真正推进，问题28按顺序自答A/B/C/D选C并列50行动，完整文件KAGGLE_STEP18_Q28_S1_CANDIDATE.md；未开29，原25–27及各50原文SHA不变。明确流程调整：允许隔离候选修复，但G0整体、发布、默认入口和声学未放行，不伪造G0通过。新增kaggle/step18/analyst.py及step18_profile_inputs.py和来源/README，实代码不是仅测试替身；只改set_text/set_candidate/delete_profile并新增4个提交辅助函数，其余命名函数AST与冻结17一致，包括原校准和reload。严格两个入口JSON/类型/Unicode/重复未知键/128KiB预算；HEAVY准入早于磁盘写入、executor重核档案/固定训练参考；内容地址锚点避免先覆旧字节再JSON失败，候选/文本/删除有限进程内锁且网络等待不持锁。删除也经HEAVY，满额可429；不覆盖校准或跨进程事务，不自动GC旧锚点。相同最终28合同对冻结17为43失败记录/2明确skip/0error（非43独立bug；旧FIFO危险阻塞不跑，新executor删除合同不适用旧版），候选28首次最终预检全PASS/0skip。首次26对照卡在unittest巨大WAV差异格式化，faulthandler保留，仅改文件快照为SHA+长度；初始日志和后续26/28收据均不覆盖。完整CPU478=旧450冻结对照+新28候选合同，3轮全部通过/失败错误跳过0；不能称478都是新运行时全功能验收。每轮159真实TCP，三轮477，新候选74/轮共222；包含期望错误／注入500，非都满足功能的成功响应。15原建议新候选实现／保护证据加强已有75并集，不虚增建议覆盖或把25%说成整体进度，最终原300功能／最终签收仍0。一次元数据预计76实际75的断言已记录，不是测试失败。附加审计24/Node30/JS/repack/AST43和独立核验结果以本批报告及progress-s1-candidate.json为准。1402历史期待/1399匹配/3旧日志D02缺失，53源/94冻结/15正式及17包不动。无安装，freeze与前批字节相同；无Go/race/实浏览器/Torch/Qwen/训练/双T4/实体音频/声学或提速新验收。完整交接93份，默认服务/工作台/复制仍17、18未发布。校准过期评分/假CER/全失败chosen0/临时profile冲突等未修，下一步S2隔离候选快照与提交冲突，不先动DSP或启用融合；继续直接操作无需Continue，不能承诺一定成功。


**上批历史检查点（G0第11批）：** 报告KAGGLE_STEP18_G0_VERSION_HTTP.md。原analyst.app的单Uvicorn事件循环真实HTTP＋HEAVY执行器Event屏障，原load_on_workers/calibrate_profile实际运行，worker传输/ASR/说话人/synth明确替身。不是多server或线程压力、实际模型／Go鉴权链。新增12=8限定保护/4未修观察，首次预检12PASS；CPU450（旧438逐ID/结果完整保留）×3＝1350PASS，失败/错误/跳过0。每轮旧61＋新24＝85真实TCP请求，三轮255，其中新版本组合72；状态200×32/500×17/400×16/422×6/404×1/409×6/503×5/429×2，错误码可为未修见证而不是产品功能成功。普通候选/文本两方向重叠的旧reload被pin挡503，不能将所有并发笼统判成无保护；校准评估后真实HTTP改候选和转写仍200保存旧评分，新文本保留而非被覆盖。另见满HEAVY时新text/candidate429之前已写盘、同名文件旧bytes评估而新bytes被选、真实DELETE后校准500非4xx且未复活档案。文件bytes变化仅自有文件fixture，非HTTP上传或远程利用。全合成失败的清理保护不等于chosen0有效校准。附加审计24/Node30/JS/repack/AST40及独立核验的实际结果见本批checks与progress-version-http.json，不挪用历史成绩。12原建议精确关联新测试与三轮HTTP下标/SHA，证据并集70→75；75/300=25%只是部分证据覆盖，不是整体完成率，最终/功能签收仍0。1317历史期待/1314已有SHA匹配/3旧.log缺失D02/0变更，不伪造缺失。沿用现有venv、无安装、freeze与上批逐字节相同；无Go/Rust/npm/Torch/Qwen/模型/双T4/真训练/声学/提速新验收。53源/94冻结/15正式不改，91份完整交接。后台等待流曾断开，不重启或覆盖CPU，后续原三轮收据完整通过；元数据tail通配检查误用单独留档，非测试失败。产品未改、声音优化未实施、G0与整体PARTIAL/BLOCKED、不跳S1/Q28/18发布。下一步按证据补齐剩余建议具体合同及门禁处置，不再把普通编辑pin已有保护当缺陷；校准快照／提交冲突与HEAVY先写后拒为后续修复重点，真模型与双T4验证仍必需。直接继续无需Continue，不承诺一定成功。


**上批历史检查点（G0第10批）：** 原analyst.app经Uvicorn临时环回TCP端口＋httpx真实socket测试，不是TestClient或AST；worker ACK／profile均明确fixture、无Go鉴权链或模型。CPU438（继承426+新12，7保护/5观察组）×3＝1314 PASS、failure/error/skip0，426逐ID/结果及原16观察与前批完全一致；每轮61真实请求、合计183，状态200×19/500×16/400×16/422×6/404×1/409×3。I01 bool/float/string index强转接受；I02 null/容器/非有限index及顶层NaN/±Infinity500；I03缺省0/重复键最后生效/未知忽略；I04非字符串转写str化且surrogate500；I05损坏candidates及预装父路径/链接file行为，所有文件仅自有临时树，不能称远程任意私密文件读或模型接受。均未修，500是观察见证非功能成功。7保护含合法候选字节/pin/Unicode、越界/缺档、有限非对象422、trained三入口409、library严格JSON400和HEAVY槽恢复。另NumPy12/8＋CLI4各3轮（三项期望blocked，resource gpu_verified=false）；附加24审计/Node30/JS/repack/AST39各3轮通过。新12预检首次通过，探索JSON保存；检查脚本id→test KeyError仅元数据检查，已留档。当前.venv重建、Python固定依赖全匹配旧freeze去掉go-bin，NumPy仍2.2.6非requirements2.4.6；安装日志保存，无Go/Rust/npm/Torch/Qwen/模型安装，C ABI fixture非Rust。12原建议R1-011/020、R2-021..030新增具体test ID与三轮case下标/SHA，有限证据并集70、230未入这些集合不等于无证据，原300及3×100处置和Q25–27各50不改、最终/功能签收0。53资产三遍13668行/94冻结/15正式保持；1228历史期待中1225匹配、3旧.log缺失D02仍在，不以新安装日志冒旧内容。无浏览器/Go/race/vet/真实模型/训练/双T4/实体音频/声学性能验收、无产品改动/18包。交接90份，当前input-http-recommendation-links.json、verify_input_http.py与progress-input-http.json，报告KAGGLE_STEP18_G0_INPUT_HTTP.md。G0与整体PARTIAL/BLOCKED，不跳S1/Q28；下一步版本冲突与候选/文本/校准组合见证及剩余建议精确映射。确保的是核验/失败可见，不承诺整体验收一定成功；继续直接操作无需Continue。


**上批历史检查点（G0第9批）：** 300/300原建议逐条处置说明已归档于g0-disposition-review.json及KAGGLE_STEP18_G0_DISPOSITION_REVIEW.md附录，3个disposition-reviewN.tsv各100条。分类23限定修复/96保留/89文档合同/55真条件阻塞/37先调查不变，review_disposition_recorded只是说明归档，原final_disposition/test/fix与新functional_acceptance全false，最终及功能签收0/300。23原限定缺陷建议手工绑定历史三轮69个JSON Pointer引用，记录源码/收据/probe SHA及完整观察片段，不是新实验、23新bug或完整合同验收。R1-016仅相关校准文本交错，NaN未在旧payload中；早期DSP缺历史probe_sha不能补为已证。旧45部分链接加23绑定交集3，合并65有至少一组限定引用、235未入这两组，不等于无其他历史证据。53资产三遍各13668行保持、94冻结/15正式不动。D02按预期SHA搜索当前仓库非.git且<=2MB文件、查3路径git log --all，无同SHA/可用提交；1183历史期待项中1180匹配、3旧.log仍缺、全历史完整性false，不补造或拿新日志当旧内容。系统Python标准库新执行24审计(继承收尾12+新增12)×3、Node30×3、JS/repack/AST39×3通过；历史失败观察仅重读未重跑，未跑CPU426/浏览器/Go/race/vet/Rust/模型/训练/双T4/物理音频/声学性能，未装依赖。独立verify_disposition.py、progress-disposition.json与89份完整交接同步。产品未改/18未发/G0与整体PARTIAL/BLOCKED，不跳S1/Q28；下一步S1合同精确测试映射及HTTP缺省/非法NaN等失败边界、D02可信恢复；保留长录音真训练/首声/无沙沙/自然朗读等未豁免要求。继续直接操作无需Continue。


**上批历史检查点（第三遍第8批）：** LICENSE201/MEMO220重新完整复读，新增2份421行；53内嵌资产三遍各53/53、13668行，源码阅读子项完成，不是整个Git仓库或零缺陷证明。原300项逐项复核并生成g0-pass3-closure-recommendation-gaps.json，23限定缺陷建议/96保留/89文档合同/55真条件阻塞/37待证保持；三遍专用7链接文件53条记录去重45项，另255无该组专用链接（不等于无历史证据），最终签收0、未闭环300。D01仍为MEMO顶部step15/xvector/12dB与冻结17默认ICL/6dB漂移，不改历史；新增D02为审计可用性缺口：1139期待历史路径中1136可读SHA匹配、变更0，pass2-gateway-go-install.log/pass2-gateway-preflight.log/pass2-startup-preflight.log三份当前缺失且匹配*.log忽略规则，预期SHA仍保留，不补造内容、full_historical_integrity_passed=false。冻结53源/94文件/15正式及HEAD保持。本批旧.venv/node_modules/Go/Rust不存在，初始环境查询/严格历史检查错误已留档；用系统Python标准库，不安装依赖。本批12收尾审计合同（含原conditioning/gain两AST原函数）×3、Node30×3、JS/repack/AST38各三轮通过；其中缺失日志检查通过只是准确暴露缺口。旧158×3浏览器原始JSON只重读SHA/结果，不是本批运行；本批未跑CPU426/Chromium/Go/race/vet/模型/训练/双T4/物理音频或声学性能。法律/NOTICE/模型与语音授权未签收。交接88份，当前g0-pass3-closure-coverage.json、verify_pass3_closure.py、progress-pass3-closure.json与KAGGLE_STEP18_G0_PASS3_CLOSURE.md。产品未改/18未发，F01–42和先前观察未修；下一步原300逐条最终审查处置及精确测试映射、D02找回可信旧日志或另存新执行收据。G0与整体PARTIAL/BLOCKED，不跳S1/Q28，直接继续无需Continue。源码三遍完成不自动签收G0。


**上批历史检查点（第三遍第7批）：** web完整3份2217行复读，第三遍累计51/53、13247行，剩LICENSE201/MEMO220共2份421行；前两遍各53/13668保持。浏览器158（继承146+新12，10保护/2观察）×3＝474 PASS，失败/flaky/skip/retry0；完整继承CPU426×3＝1278 PASS、failure/error/skip0、无新增Python合同；另VM22/16、NumPy分块12/trimmer8/实际CLI4各三轮，三项CLI每轮expected blocked，不是GPU成功。本批新F41：原stop后abort、hold/reset，注入迟到fixture st使原player发play/UI playing，不证明实际原生Worklet竞态/物理漏音；F42：同accessEpoch、两候选mutation0→1、合成profiles响应1→0，使高亮从1回0，不证明实际backend回滚/错声音。两项均未修，旧F01–40/D01保持，每轮另有F04/05/06/25/26浏览器观察。原生clipboard实核三份冻结web完整文本且无额外save，17包/原生振荡器录音/权限回退等旧146项全继承；临时E2E workbench不是正式HEAD，物理麦克风/扬声器/真Go链路/DeepSeek/模型/训练/双T4/声学/RTF未验证。首预检11/1为旧recorder-only壳缺charset中文乱码，仅新审计壳声明UTF-8后12通过，原断言/旧fixture/产品不动、首错留档。1051历史SHA、53源/94冻结/15正式保持；原300本批7部分链接、累计45unique，原文/Q25–27各50及最终处置false不变。Node30/JS/AST38/repack新执行，freeze/lock不变、无新Python/系统依赖或npm重装；C ABI故障fixture非Rust。本批未重跑Go/race/vet/独立ASGI2.3，不挪用历史通过数。交接87份，当前g0-pass3-frontend-coverage.json、verify_pass3_frontend.py、progress-pass3-frontend.json，完整报告KAGGLE_STEP18_G0_PASS3_FRONTEND.md。产品未改/18未发，G0与整体PARTIAL/BLOCKED，不跳S1/Q28；下一步剩2份第三遍及原300最终映射，无需Continue。以下第7批及更早的“最新”仅指当时；以上第8批状态优先。


用户新截图运行17，41.6秒录音成功建档142.3秒，输入RMS约-47.7dBFS/peak0.011，有#0/#1/#2。现在重点是更快实际首声、全部候选的校准/条件作用明确、无沙沙、自然连续朗读；不能把全部候选参与统计说成模型同时融合三参考。不能由截图定噪声根因，不能播放参考PCM增加相似。

当前完成：基线53资产逐字节/94冻结哈希/15正式文件核对；三轮专题各100建议，外围部分入口复核；12种case的NumPy DSP历史基线三轮、20种case的参考状态历史控制流三轮；本分支新增22种播放器/Worklet/协议案例及8种裁剪器案例各三轮，Node30及JS/repack检查。按顺序完成问题25–27及各50建议；本批三题完成。16项首声/短尾VM合同与8项噪声度量合成案例各三轮，不是真实声学或性能测量。**没有完成所有源码逐行语义审查三遍；后续深审仍可触发新的关键决策。** 没有产品代码改动、没有18发布包、没有完整语音模型/GPU实验。

基线发现：NumPy短块淡入依赖分块；同半秒双音target=-6/maxgain0，48样本分块与整块最大差1424 int16；正常AGC1920样本分块差8。三轮一致，见dsp-partition-baseline-round1..3.json。它证明工程分块依赖，不证明用户沙沙根因或真实听感；Rust仅源码对照，未编译执行。

第二轮实际接口核验：Faster0.5.4+qwen-tts-hf0.1.1.post1支持独立批量prompt，不支持把三个列表提示自动融合给单目标；真实resolver拒绝长度不匹配。最初误查旧发行版qwen-tts==0.1.1.post1失败后按pins纠正，只下载解包，未安装旧版/未改变产品依赖。wheel URL/hash与抽取函数来源收据完整保存。

第二轮受控复现：候选bool/小数强转、null/容器未捕获异常；ASR全失败默认CER0.05；校准期间转写更新导致旧评分提交未经该轮评估的新转写；加载失败回执被忽略；全合成失败仍chosen0；双卡诊断同文seed100/101不同（正式播放同会话seed原本相同，必须保留）。三轮每轮20项，外部模型/网络显式fixtures，确定性交错不是HTTP/线程压力测试。未修复，不推断用户噪声根因。

第三轮新复现：生成结束时剩20/50ms音频可永久buffering（24k/44.1k/48k）；35ms预滚跨块少840样本；不足120样本有声输入可被忽略、60样本末尾非零信号留held无finish。小块只是泛用合同测试，不证明当前Faster1920样本倍数路径发生。重采样端点不足需定义尾样本政策，不声称已有可听损伤。首播放指标在发play命令处赋值；不是Worklet/声卡实际出声。上述实验是原播放器VM和裁剪器AST，非实体浏览器/模型/声学实测。Rust仅源码，当前Worker每段重建leveler不能漏记。

第25题选C：全部合格候选用同文同seed同参数评估，明确实际ICL锚点；同句融合若研究，只能独立试验同Qwen模型嵌入，不跨空间用ECAPA、不把列表批量或单锚点回退称融合。尚未选融合公式/权重/默认开关，未验收保持BLOCKED。具体四选项及50实施建议完整内嵌。第25题主体与50条hash核对未变后才进入26。

第26题也选C：先度量/回归合同→参考状态可靠性→DSP/裁剪有界状态→完成短尾排空→真实同条件首块/缓冲实验。正常未完成小缓冲仍等待；完成20/50ms尾部在初始和starved恢复均可能滞留。新增原Player VM16案例三轮，注入时钟300/750ms只说明首PCM与play命令不同，不是测得性能，更不是提速450ms。首段默认4帧保留，首块2–8实验须T4证据。Go queue_wait_ms在结束计入生成、Worker queue_ms含参考准备，后续分阶段/分尝试新指标须保留旧字段含义。Worklet消费/非静音/正确人声/声卡出声分开；未测值null，不称实体出声已验证。26题四选项及50建议完整内嵌，主体hash保留不变。

第27题选C，四选项及50建议完整内嵌：分层诊断与联合门禁。原estimate_snr是20ms帧RMS分位差，不是真值SNR；合成等能量干净/噪声块都可返回0；均匀增益不改善组件SNR；理想FFT滤波反例可同时损失有用6kHz分量。8案例三轮仅合成度量/归一化，不是实际降噪、真实辅音、用户WAV或GPU实验。不默认启用强滤波，不从截图判根因。新增IMPLEMENTATION细则：先G0补全源三遍语义覆盖与300建议处置/失败测试映射，再S1–S8最小步实施。不预填问题28，不跳过门禁；当前产品未改、18未发布。

G0第一批：全文第一遍6份/930行，完整第二/三遍0；53资产台账与300条逐ID初审映射完成，但未签收。23条关联限定范围缺陷建议（有重复）、96保留、89文档/测试合同、55真实条件阻塞、37待证。84项现有CPU/进程/进程内HTTP专项三轮通过；10项边界三轮，复现损坏talker_config的AttributeError与恢复第二成员I/O失败后的部分提交。捕捉缺陷退出0不等于已修复。具体完整内嵌G0_AUDIT/G0_DISPOSITION；第一批收据保留不改。第二批全文12份/1974行，第一遍累计18/53、2904行，剩35项；完整第二/三遍仍0。135项训练链/文件/租约/进程内HTTP/安全张量专项×3通过；6项provider合同×3，以真实HF wheel METADATA和重型加载fixture复现原CPU编码器查询缺失旧qwen-tts版本的异常，未运行真实编码/训练。完整内嵌G0_TRAINING_CHAIN，第二批历史覆盖为g0-training-chain-coverage.json。新增F01单列，300原建议不改写。第三批Go网关全文13份/3527行，第一遍累计31/53、6431行，剩22项，完整第二/三遍仍0；第三批历史覆盖为g0-gateway-coverage.json。原Go40主测试（含子测试56）×3和新增10探针×3通过，独立竞争见证三轮预期非零并报告DATA RACE，不混入通过套件。确认快照map竞争F02及四类帧校验不足F03，均未修复。mock播放、库HTTP、合成训练输入HTTP三类各内部3轮通过，非真实模型/训练/声学，未重跑全部历史6类。完整内嵌G0_GATEWAY。第四批前端全文3份/2217行，第一遍累计34/53、8648行，剩19项，完整第二/三遍仍0；第四批历史覆盖为g0-frontend-coverage.json。Chromium每轮134（原123+新11）三轮通过，无失败/跳过/retry/flaky；新8保护+3原行为观察。F04旧录音error误停新会话、F05协议解析失败未显式取消reader/请求、F06音频初始化失败未revoke URL，各三轮fixture复现，均未修。原Player边界22/延迟16 VM各三轮；第1–17完整包逐字节复制保护通过，原始文件为真实hash核对及浏览器sentinel保留，不冒称完整原始文件复制。原生录音测试输入为振荡器/静音，不是物理麦克风；新故障例为明确设备/HTTP fixture，非真实Go/模型/声学。完整内嵌G0_FRONTEND。第五批Python启动/监督/worker/clone_stream/voice_binding全文5份/1536行，第一遍累计39/53、10184行，剩14项，完整第二/三遍仍0；第五批历史覆盖记录为g0-runtime-coverage.json。94项CPU专项（原84+新10）×3通过，新7保护+3观察；真实supervisor/FD租约/进程组与fatal健康两类各内部3轮，模型角色为CPU替身。F07无界响应队列、F08失败重载prompt与接受pin不一致、F09规范化/报告不一致各三轮fixture复现未修；原Worker/RealEngine.load_profile和真实文件hash执行，重型resolver/生成/GPU清理为fixture，不是实际错误音色或慢客户端资源峰值实验。完整内嵌G0_RUNTIME，39/53是第五批历史检查点。第六批分析/API/参考切分/Python与Rust DSP全文6份2152行，第一遍累计45/53、12336行，剩8份；完整第二/三遍仍0，第六批历史覆盖记录为g0-analysis-dsp-coverage.json。172项专项（旧160+新12，新9保护/3观察）×3通过，各轮失败/错误/跳过0；14个分析AST与12个NumPy分块案例各三轮。F10极短NumPy breath形状、F11窗口重识别漏清洗可选words、F12分析端接受HTTP失败/残缺流各三轮确认未修；F12实际requests/本地TCP，F11显式ASR metadata fixture，无真实模型。历史6个prompt接口案例因本地upstream cache不存在未重跑，不重签旧20项收据。Rust两份只完整阅读源码，未找到rustc/cargo，未编译/运行/加载Rust，不冒用NumPy结果。旧分块差1424/8及校准候选问题仍复现；Node30/JS/Python AST/repack通过，历史295份hash保留。完整内嵌G0_ANALYSIS_DSP。第七批6工具/LICENSE/MEMO全文8份1332行，内嵌53资产第一遍累计53/53、13668行、剩0；这不是全仓库或三遍完成，完整第二/三遍仍0，G0未完成。第一遍收尾历史覆盖为g0-tools-coverage.json。197项专项（上批172+既有probe13+新12，新9保护/3观察）×3通过，各轮失败/错误/跳过0；每轮4个独立真实CLI合同，backend静态/runtime与默认benchmark均按预期exit2/BLOCKED，resource status exit0，阻塞不当模型成功。F13 E2E缺gpu/失败END/奇数PCM/残留误PASS，F14 watermark空HTTP503/ERR/残缺帧零音频误PASS，F15 selftest failed/cancelled Mock流误PASS，本地HTTPfixture三轮确认未修；F15时间明确fixture，不是测得首声或RTF。D01 MEMO旧step15/xvector/maxgain12与当前17 ICL/maxgain6漂移仅记录，不改冻结MEMO。LICENSE全文阅读不是法律/NOTICE/依赖模型授权签收。Node30/JS/全产品Python AST/repack通过；329历史文件hash保留，71份memo原文内嵌。Rust/完整模型/GPU/训练/声学/提速仍未验，无产品改动/18包。完整内嵌G0_TOOLS。全源第二遍第1批已重新全文阅读training_job/gpu_ownership/resource_limits/tts_training/tts_dataset/lora_adapter/train_tts/resource_control共8份1056行，第二遍8/53、剩45，第一遍53/53/13668保持，第三遍0；当前覆盖以g0-pass2-training-coverage.json为准。局部查看training_codes/encode_training/supervisor调用点不计全文。219项专项（旧197+既有artifact10+新12，新11保护/1观察）×3通过，各轮失败/错误/跳过0。新F16 stop_ranks在直接leader退出后漏清理忽略SIGTERM的额外后代，实际CPU进程/pidfd/OFD/flock复现未修；fixture最后定向清理、锁释放已验证。额外后代明确构造，当前run_rank无DataLoader子进程，不证明正常Qwen训练故障。AST只跑采样/赋值回滚/dataset构造，不模拟Torch算子，无tensor/optimizer/Gloo/NCCL/完整模型/GPU/声学/性能验收。Node30/JS/全产品Python AST/repack通过，382历史文件hash保留。完整内嵌G0_PASS2_TRAINING；继续剩45项第二遍、完整第三遍及300建议最终处置/失败见证映射，G0未完成、不改产品/不发18包。

最新检查点为全源第二遍第2批：voice_library/training_data/training_codes/trained_profiles/persist/qtts_common/access_control重新全文7份1526行，第二遍累计15/53、2582行、剩38；第一遍53/53/13668保持，第三遍0。上文8/53及剩45为第1批历史，不是当前进度；当前覆盖以g0-pass2-state-coverage.json为准。analyst候选函数仅局部，不计全文。324项专项（旧219+另选既有93+新12，新11保护/1观察）×3通过，失败/错误/跳过0；新预检先因AST提取器保留HTTP装饰器报NameError，去装饰器保留原函数体后12通过，失败原日志保留。F17原pack目录枚举后候选切换，可归档新版profile.json而漏新锚点；实际本地原pack/extract和原候选AST函数体确定性交错复现未修，live锚点存在、解包无异常但恢复锚点缺失。worker reload/admission明确fixture，非HTTP/线程压力、远端Kaggle或模型加载。F01/F16及旧多成员恢复IO部分提交仍未修；Dataset只备份profiles/active，非训练工程全恢复，也仍含私有参考/文本，不宣称远端隐私策略验收。Node30/JS/AST38/repack通过，408历史文件hash、53源/94冻结/15正式保持。当前verify_pass2_state.py及progress-pass2-state.json、73份memo原文内嵌；完整报告G0_PASS2_STATE。无Torch/optimizer/DDP/NCCL/完整模型/GPU/实际训练/声学/提速验收，无产品修改/18包。G0仍PARTIAL/BLOCKED，继续其余38份第二遍与全53第三遍及300建议最终映射，不跳S1/Q28、不要求Continue。


最新优先检查点为全源第二遍第3批：qwen_compat/voice_binding/worker/clone_stream/adapter_engine全文5份1071行，第二遍累计20/53、3653行、剩33；第一遍53/53/13668保持，第三遍0。上文8/53与15/53均为历史批次，当前以g0-pass2-inference-coverage.json、verify_pass2_inference.py与progress-pass2-inference.json为准。分析API全文留下一批，不计测试经过为全文。336项专项（旧324+新12，新11保护/1观察）×3通过，各轮失败/错误/跳过0；另ASGI2.3 companion各1项观察×3通过，不计入1008。F18：原synth先起生产线程，仅body iterator finally设置cancel；正文首次迭代前在ASGI2.4响应头send抛断连、ASGI2.3响应头等待中receive返回disconnect两条真实Starlette响应路径均未通知生产cancel，线程继续等待。真实原endpoint/响应/CPU线程执行，断连时序与生产工作负载明确fixtures，finally定向取消/join自有线程；未修，非TCP/浏览器/模型/GPU/线上故障证明。旧F01–F17保留。新测试还覆盖有界参考/FIFO、真实锁排队取消所有权、pin加载拒绝、重放迭代器关闭、RoPE控制流、trained磁盘绑定/删除/链接/预算；minimal torch.manual_seed为明确fixture，不是实际Torch算子/codec。环境.venv未保留已重建关键固定CPU依赖，安装日志/完整freeze保存，不声称全部传递依赖与旧环境相同；无Torch/Qwen/Rust/Go安装。Node30/JS/AST39/repack通过，435历史证据hash、53源/94冻结/15正式不变。完整报告G0_PASS2_INFERENCE新增至74份memo原文。没有产品修改/18包/真实训练/双GPU/声学/提速签收；G0仍PARTIAL/BLOCKED，继续剩33份第二遍、全53第三遍及300建议最终映射，不跳S1/Q28、不要求Continue。


最新优先检查点为全源第二遍第4批：analyst/library_api/reference_segments全文3份1480行，第二遍累计23/53、5133行、剩30；第一遍53/53/13668保持，第三遍0。上文8/15/20份第二遍均为历史，当前以g0-pass2-analysis-coverage.json、verify_pass2_analysis.py和progress-pass2-analysis.json为准。348项专项（旧336+新12，新10保护/2原行为观察）×3通过，各轮失败/错误/跳过0。F19两个真实进程内ASGI校准请求通过原HeavyAdmission(2)，原calibrate共用_cal_pid_k目录；A清理后B原Mock Worker.load_profile找不到临时档案，B错误记录覆盖A成功记录，两个响应均200；确定性交错，合成/ASR/声纹与worker transport明确fixtures，非TCP/模型/双GPU。F20原load_on_workers重载期间实际删除档案，最终current None跳过失效检查，原reload_response仍200/ok/reference_saved；worker回执fixture，无删除后播放或激活绕过证据。两项三轮确认未修，临时资源/准入槽清理验证。真实路由严格嵌套JSON/Unicode/标记、库结果合法profile提交、低能量15.3秒PCM窗口连续覆盖、17秒长手工文本不强配短候选等保护通过；不是Whisper/真实音频/训练/质量验收。参考预排最多24、落盘最多3、实际单锚点conditioning，分析空间centroid不是Qwen融合，贡献完整追溯未签收。旧F01–F18/ASR默认CER/旧校准版本/不同GPU seed等问题保留。Node30/JS/AST38/repack通过，470历史证据hash、53源/94冻结/15正式不变。完整报告G0_PASS2_ANALYSIS，交接75份全文；venv沿用并保存freeze，与上批一致，不称全部环境二进制绝对一致。无产品改动/18包/真实模型/训练/双GPU/声学/提速签收。G0仍PARTIAL/BLOCKED，下一批启动/监督/backend preflight完整复读与provider版本/失败取消所有权，继续剩30份第二遍、全53第三遍和300最终映射，不跳S1/Q28、不要求Continue。


最新优先检查点：报告 `docs/KAGGLE_STEP18_G0_PASS2_STARTUP.md`。bootstrap451/supervisor219/backend_probe200全文3份870行，第二遍累计26/53、6003行、剩27；第一遍53/53/13668保持，第三遍0。360项（旧348+新12，新10保护/2观察）×3通过，各轮失败/错误/跳过0。F21原sh在leader退出而后代持stdout时timer跳过killpg，超过请求期限并在外部清理后返回0；真实CPU/pipe/timer/pidfd、观察包装确定性交错，后代退出已验证，非完整bootstrap/性能证明。F22原watch的fatal回执写失败跳过kill/gave_up，HTTP每轮清零使8轮后fail_count仍1；health/IO/process/wait明确fixtures，非真实GPU或磁盘故障。两项未修，F01–F20保留。标准faster启动全部PINS逐项预查/精确安装/constraints0600与清理/Torch变更拒绝、probe先于下载的控制流测试通过；未执行真实pip resolver或GPU，后安装漂移/独立入口/native-adapter仍待证，surface preflight不是质量签收。Node30/JS/AST38/repack通过；497历史hash、53源/94冻结/15正式、300初审与Q25–27各50保持。当前g0-pass2-startup-coverage.json、verify_pass2_startup.py及progress-pass2-startup.json；交接76份原文。无产品修改/18包/真实训练/模型/双GPU/声学/提速验收。继续剩27份第二遍，优先网关调度/流协议/取消/超时及前端排空交叉核对，再全53第三遍/最终映射；G0仍PARTIAL/BLOCKED，不跳S1/Q28、不要求Continue。

最新优先检查点：报告 `docs/KAGGLE_STEP18_G0_PASS2_GATEWAY.md`。main/scheduler/session/segmenter/llm全文5份2286行，第二遍累计31/53、8289行、剩22；第一遍53/53/13668保持，第三遍0。每轮Go原40主测/含子测56、旧专项10、新13（11保护/2观察）通过，合计63主测/79含子测×3；Python旧360×3通过，无新增Python测试。通过套件无失败/跳过/race warning；独立F02竞争见证每轮预期非零/DATA RACE，未混入通过数。F23原healthLoop接受HTTP503 ready=true，原网关报告两worker健康；真实本地HTTP，永久循环隔离于自有Go子进程并核对退出。F24原activate期间实际改profile.model_output_mode，最终conditioning改变而binding相同，仍200/提交active；worker回执为HTTP fixture，无真实训练产物/模型/后续合成。两项未修，F01–F22和专题问题保留。实际Go1.23.9新增于忽略venv，安装报告/wheel SHA与可执行hash保存；freeze仅多go-bin==1.23.9，其余依赖保持，不称全部freeze相同。Node30/JS/AST38/repack/原Go及新探针副本vet/gofmt通过；525历史hash、53源/94冻结/15正式、300初审及Q25–27各50不变。当前g0-pass2-gateway-coverage.json、verify_pass2_gateway.py及progress-pass2-gateway.json；交接77份原文。无产品修改/18包/真实DeepSeek/Qwen/训练/双GPU/声学/提速签收。继续剩22份第二遍，优先前端流终止/取消/遥测/完成排空，再DSP/工具/剩余Go安全和测试；全53第三遍及最终映射仍待完成。G0仍PARTIAL/BLOCKED，不跳S1/Q28，不要求Continue。

最新优先检查点：报告 `docs/KAGGLE_STEP18_G0_PASS2_FRONTEND.md`。app1715/recorder358/index144全文3份2217行；HTML首次合并输出截断，已补读全范围，第二遍累计34/53、10506行、剩19；第一遍53/53/13668保持，第三遍0。新增浏览器12（10保护/2观察）预检通过，既有134+新12=146×3全部通过，失败/跳过/flaky/retry0；Player VM22/延迟VM16各三轮、CPU旧360×3通过，无新增Python测试。本批未重跑Go79/独立F02竞争见证或独立ASGI2.3/旧CLI矩阵，不挪用历史数字。F25原完整前端脚本END后仍收PCM/文本且第二END替换首汇总；F26网络EOF先发report并停telemetry，随后play/欠载UI变化不更新报告；真实Chromium原生流/DOM/timer，网络/设备/Worklet状态明确fixtures，非物理播放、真实欠载或声学/提速。两项未修，F01–F24及<=50ms已完成短尾/旧DSP等保留。Node模块按冻结lockfile npm ci恢复，未改lock；venv freeze与上批相同，无新Python依赖。Node30/JS/AST38/repack/前端探针语法检查通过；575历史hash、53源/94冻结/15正式、300初审及Q25–27各50保持。完整交接78份原文；当前g0-pass2-frontend-coverage.json、verify_pass2_frontend.py与progress-pass2-frontend.json。产品未改/18未发/真实DeepSeek/Qwen/训练/双T4/声学/提速未签收。下一批Python/Rust DSP和工具自检，再余Go安全/测试与LICENSE/MEMO；继续剩19份第二遍、全53第三遍/最终映射。G0仍PARTIAL/BLOCKED，不跳S1/Q28、不要求Continue。

最新优先检查点：报告 `docs/KAGGLE_STEP18_G0_PASS2_DSP.md`。Python/Rust DSP及6工具全文9份1500行，第二遍累计43/53、12006行、剩10份1662行；第一遍53/53/13668保持，第三遍0。CPU372（旧360+新12，新10保护/2观察）×3全部通过，失败/错误/跳过0；NumPy分块12、原EdgeTrimmer AST8各三轮，旧问题未修；4个独立CLI合同×3，backend静态/runtime及默认benchmark按预期exit2/BLOCKED，resource status exit0，阻塞不是模型成功。F27 NumPy flush未清DC状态，常量480→flush192→零240得到240非零/峰6026，fresh为0；Rust源码清DC但未编译执行，正常worker每job重建Leveler，因此不是当前沙沙声根因证明。F28原benchmark/measure两实际HTTP端点health分别GPU0/1、18测量均GPU0，仍real_gpu_verified/speed_target_passed true；health/stats/PCM/clock明确fixtures，报告true是被反证输出，不是硬件/RTF成绩。两项未修。Node30/JS/产品Python AST/新审计语法/repack通过；625历史SHA、53源/94冻结/15正式、300初审及Q25–27各50保持。freeze与前端相同，无新依赖；Rust/Torch/Qwen/实际训练/双GPU/声学/提速未验。本批不重跑浏览器/Player VM/Go/独立F02/ASGI2.3，不挪用历史成绩。完整交接79份；当前g0-pass2-dsp-coverage.json、verify_pass2_dsp.py与progress-pass2-dsp.json。产品未改/18未发；下一批剩余Go安全/测试/go.mod和LICENSE/MEMO共10份，再全53第三遍及300最终映射，G0仍PARTIAL/BLOCKED，不跳S1/Q28，不要求Continue。

最新优先检查点：报告 `docs/KAGGLE_STEP18_G0_PASS2_SECURITY.md`。剩余Go安全/测试/go.mod及LICENSE/MEMO全文10份1662行，第二遍累计53/53、13668行、剩0；第一遍53/53/13668保持，第三遍0。这是冻结包53资产，不是全Git仓库或三遍/全功能完成。每轮Go原40主测/含子测56、旧10、上批13、新12（10保护/2观察），合计75主测/91含子测×3通过；CPU旧372×3通过，无新Python测试；失败/错误/跳过0，通过集合无race warning。独立F02每轮预期非零/DATA RACE，不混入通过数，未修。三轮副本vet通过。F29原guard/decodeJSON/validateSpeak接受孤立高低代理项或非法UTF8，解码成a�b后返回200；实际本地HTTP组合校验handler，非完整合成或认证绕过。F30原授权speak/LLM错误链将HTTP401替身正文回显的配置假密钥带入ERROR/END/metrics；密钥/供应商均synthetic，非真实泄密事件或未授权读取。两项未修。LICENSE全文阅读不等于依赖/模型/数据/NOTICE法律签收；MEMO step15/xvector/maxgain12漂移仍为D01，冻结不改。Node30/JS/产品与新审计Python AST/repack/Go探针gofmt通过；686历史SHA、53源/94冻结/15正式、300初审及Q25–27各50保持。Go沿用、freeze与DSP相同，无新依赖；无Rust/Torch/Qwen/完整模型/真实GPU/训练/声学/提速签收。本批未重跑独立CLI/NumPy与trimmer探针/ASGI2.3/浏览器与Player VM，不挪用旧成绩。完整交接80份；当前g0-pass2-security-coverage.json、verify_pass2_security.py与progress-pass2-security.json。产品未改/18未发；下一步第三遍全源跨层输入/pin/错误、生命周期/取消/播放/训练绑定审查及300最终映射，G0仍PARTIAL/BLOCKED，不跳S1/Q28，不要求Continue。

最新优先检查点：报告 `docs/KAGGLE_STEP18_G0_PASS3_INPUT.md`。main478/security247/session692/qtts_common211/voice_binding60/resource_limits172/access_control70重新全文7份1930行，第三遍7/53、剩46份11738行；第一、第二遍各53/53/13668保持。browser和library_api只局部调用点不计第三遍。新增Go6（5保护/1观察）及Python6（5保护/1观察），预检各6通过；每轮Go81主测/97含子测×3、CPU378（旧372+新6）×3通过，失败/错误/跳过0，通过集合无race warning；独立F02三轮预期非零/DATA RACE不计通过，三轮副本vet通过。实际Go/Python8合法pin与12非法generation向量、两worker ack期间generation变更拒绝、空/错text拒绝、内容pin非身份、上传预算+1、spool清理、原子JSON失败、参考增长拒绝、两认证进程一致性均有明确边界。F31同磁盘top_k:null被Go转0并得pin而Python拒绝；F32认证token FIFO无writer时open先于fstat阻塞，普通文件control通过，外部定向终止并reap自有子进程；两项未修，无真实凭据/模型/错误音色或远程利用证明。原8条建议仅部分证据映射，300与Q25–27各50不改/不签收。739历史SHA、53源/94冻结/15正式保持；Node30/JS/AST/repack/gofmt/vet通过，freeze与第二遍收尾相同，无新依赖。旧S2 F29/F30随套件重跑仍未修；本批未跑浏览器/VM/独立CLI/ASGI2.3/分块裁剪探针，不挪用历史成绩。完整交接81份；当前g0-pass3-input-coverage.json、verify_pass3_input.py及progress-pass3-input.json。产品未改/18未发；无Rust/Torch/Qwen/实际训练/双T4/声学/提速签收。下一批第三遍参考分析/API/档案修改与备份事务，继续剩46份及300最终映射；G0仍PARTIAL/BLOCKED，不跳S1/Q28，不要求Continue。

最新优先检查点：报告 `docs/KAGGLE_STEP18_G0_PASS3_REFERENCE.md`。analyst1211/library_api163/persist99/reference_segments106/voice_library351第三遍完整5份1930行，累计12/53、3860行、剩41份9808行；前两遍各53/53/13668保持。新12（10保护/2观察）预检通过，CPU390（旧378+新12）×3全部通过，失败/错误/跳过0。F33真实两CPU线程占满原HEAVY，原text/candidate ASGI先写盘改pin再429，不reload且不报reference_saved；F34原校准评估旧转写，在结束提交前实际text ASGI改pin仍200，随后calibrate保存旧评分到新档案仍200；临时目录/线程/槽清理核对。模型/ASR/speaker/worker ack为fixtures，无真实音质/错误音色证明，两项未修。复制失败旧pin保护、JSON失败仍遗留孤立anchor明确不称全回滚；trained三入口409、原库snapshot异常/顺序/只读与租约、稳定pack/extract字节pin、归档末尾非法成员先拒绝、DELETE重复revision、24秒可信词切分保护通过。原300本批10条部分链接、与前批去重16个ID，均未最终签收；原文/Q25–27各50保持。795历史SHA、53源/94冻结/15正式保持，Node30/JS/AST/repack通过，freeze与前批相同无新依赖。本批未跑Go/F31/独立F02/浏览器VM/独立ASGI2.3/CLI/分块裁剪探针，不挪用历史成绩。交接82份；当前g0-pass3-reference-coverage.json、verify_pass3_reference.py及progress-pass3-reference.json。产品未改/18未发；无Rust/Torch/Qwen/实际训练/双T4/声学/提速签收。下一批第三遍训练输入/码/训练产物绑定与取消/提交，继续余41份及300最终映射；G0仍PARTIAL/BLOCKED，不跳S1/Q28，不要求Continue。

最新优先检查点：报告 `docs/KAGGLE_STEP18_G0_PASS3_TRAINING.md`。training_data285/training_codes355/training_job227/tts_training200/tts_dataset125/trained_profiles155/encode_training128/trained_voice30全文8份1505行，第三遍累计20/53、5365行、剩33份8303行；前两遍各53/53/13668保持。首组源码输出截断后完整补读。首次测试43项因导入TestCase重复31项，1失败为误判正常.lock；改模块导入与断言，保留首错/说明，预检新12通过。初行数误算1605被信用断言拦住未写错误coverage，逐项纠正1505/5365/8303并留记录。CPU402（旧390+新12，新11保护/1观察）×3全部通过，失败/错误/跳过0。F35原控制器在两个真实CPU替身rank0退出且adapter仅含manifest.json={}时仍completed/optimizer_execution_observed=true，原TrainedArtifacts.inspect409拒绝，信号/租约恢复；训练准入/依赖/tokenizer门禁与rank实现明确替身，原GPU/code OFD adopt实际执行，无Torch/优化器/训练/非法声音发布或正常rank产生坏检查点证明。F35未修，F01–34/D01保留。新保护包括输入BaseException回滚、PCM极值36001帧、codes最终取消、encoder第二样本中断、finish-only pin、adopt最后OFD、cancelled产物拒绝、来源/NaN拒绝、发布末次重核/固定参考文本/active不变及新trained_voice CLI错pin脱敏拒绝；发布codes lease元数据/adapter为fixtures，不能签收真实训练。原300本批7部分链接，与前两批去重22ID，均未最终签收；Q25–27各50保持。825历史SHA、53源/94冻结/15正式保持；Node30/JS/AST38/repack通过，freeze与上批相同无新增依赖。本批未跑Go/F31/独立F02/浏览器VM/独立ASGI2.3/额外四CLI/分块裁剪矩阵，不挪用历史成绩。交接83份；当前g0-pass3-training-coverage.json、verify_pass3_training.py及progress-pass3-training.json。产品未改/18未发，无Rust/Torch/Qwen/实际训练/双T4/声学/提速签收。下一批第三遍adapter/推理/provider兼容与缓存/失败取消，继续余33份及300最终映射，G0仍PARTIAL/BLOCKED，不跳S1/Q28、不要求Continue。

最新优先检查点：报告 `docs/KAGGLE_STEP18_G0_PASS3_INFERENCE.md`。adapter_engine108/lora_adapter91/qwen_compat97/clone_stream126/gpu_ownership151/worker680/train_tts49重新全文7份1302行，无源输出截断，worker连续四段；第三遍累计27/53、6667行、剩26份7001行；前两遍各53/53/13668保持。新增12（11保护/1观察）预检一次通过；CPU414（旧402+新12）×3全部通过，失败/错误/跳过0。F36原generated_only_stream在consumer关闭已启动生成器时，上游close替身抛异常，后续window.finish被跳过；生成器frame本身关闭，测试捕获的真实window仍closed false/pending1920/合成code标记，最后显式清理完成。准备/predictor/decoder/Torch上下文均控制替身、无tensor模拟，没有证明生产上游会抛错或正常GC后持续GPU内存泄漏/沙沙根因，F36未修。adapter来源不符先拒绝、cached仍核验实际safetensors字节、取消前不选择与取消后丢弃返回PCM、native rate/shape/NaN/长度拒绝与单句输出、回放指标合计、worker部分生成失败解锁/后续成功、同pin缺prompt重载、RoPE重试cause/注册表、真实短pwrite释放OFD均保护通过；LoRA prepare/commit和native模型未执行。F01–35/D01保留，旧ASGI/CLI/信号/CPU持有者见证随集合重跑，不代表真实模型。原300本批7部分链接，累计去重27ID，均未最终签收；Q25–27各50保持。858历史SHA、53源/94冻结/15正式保持；Node30/JS/AST38/repack通过，freeze与上批相同无新依赖。未跑Go/F31/独立F02/浏览器VM/独立ASGI2.3/额外四CLI/分块裁剪矩阵，不挪用历史成绩。完整交接84份；当前g0-pass3-inference-coverage.json、verify_pass3_inference.py及progress-pass3-inference.json。产品未改/18未发，无Rust/Torch/Qwen/实际训练/双T4/声学/提速签收。下一批第三遍启动监督/preflight/资源测量工具与DSP接口，继续余26份及300最终映射，G0仍PARTIAL/BLOCKED，不跳S1/Q28、不要求Continue。

最新优先检查点（第三遍第5批）：`docs/KAGGLE_STEP18_G0_PASS3_STARTUP.md`。11份2253行全文复读；累计38/53、8920行，剩15份4748行。CPU426（旧414+新12，10保护/2观察）×3全部通过，失败/错误/跳过0；另NumPy分块12、trimmer8、实际CLI4各三轮，CLI中3项每轮期望blocked而非模型成功。首预检12项中1 error为测试误访问UploadRejected.status，纠正为code后12通过，首错/修正留档。F37原preflight父控制器接受真实CPU替身child exit23写出的合法形状成功回执；生产者明确替身，不证明实际GPU误通过。F38已有系统cc编译仅rt_version的C共享库，真实ctypes在ABI3缺rt_leveler_new抛AttributeError中止import，ABI2及显式NO_RUST为NumPy；不是Rust编译/运行或正式Rust库损坏证明。两项未修，产品不改。887历史SHA、53源/94冻结/15正式保持；原300本批7部分链接、累计33unique，Q25–27各50不变，最终处置仍false。Node30/JS/AST38/repack新执行；无新Python/系统依赖，freeze不变。未跑Go/race/vet/浏览器VM/独立ASGI2.3，未跑Torch/Qwen/实际训练/双T4/声学或提速。交接85份；最新coverage/verifier/progress为pass3-startup。继续余Go10/web3/LICENSE/MEMO及300最终映射，G0与整体PARTIAL/BLOCKED，不跳S1/Q28/18发布，不要求Continue。

最新优先检查点（第三遍第6批）：`docs/KAGGLE_STEP18_G0_PASS3_GATEWAY.md`。剩余Go10资产2110行全文复读，累计48/53、11030行，剩5份2638行（web3份2217/LICENSE201/MEMO220）；前两遍各53/13668保持。新增Go12（10保护/2观察）race预检通过，首编译错因测试误用submitted，已改为真实字段allSubmitted、首错留档；另一次审计元数据括号SyntaxError解析前阻止全部写入，拆开后纠正留档。Go原40+G0十+P2十三+security十二+input六+新十二＝93顶层/109含子测试×3正常通过，意外fail/skip/race0；独立F02 race×3预期非零、仍未修，vet×3通过。CPU完整继承426×3＝1278 PASS，failure/error/skip0，无本批新增Python合同；另NumPy分块12/trimmer8/实际CLI4各三轮，3项CLI每轮期望blocked非GPU成功。F39原Live PreserveText把你好。!?重连成你好。及丢独立空白/标点尾段，非语词漏读或沙沙根因证明；F40原run在活ctx下接受替身cancelled=true stats＋偶数PCM，served1/failed0，非真实生产取消或GPU漏音证明。两项未修；F01–38/D01保持。chat system/history/预算、SSE CRLF/末行无换行/流内错误脱敏、正常read Unicode保字/seed、retry上限、urgency/FIFO、EMA与chunk2/6/pin转发保护通过，非200正文F30仍在。953历史SHA、53源/94冻结/15正式保持；原300本批7部分链接、累计38unique，Q25–27各50/最终处置不变。Node30/JS/AST38/gofmt/repack新执行，无新Python/系统依赖、freeze不变；CPU继承C ABI故障注入不冒称Rust，无Rust/Torch/Qwen/CUDA/真训练/双T4/声学/提速。本批未跑真实浏览器/VM/独立ASGI2.3，不挪用历史成绩。交接86份，最新pass3-gateway coverage/verifier/progress。产品未改/18未发，下一批web完整阅读与实浏览器、另许可/MEMO及300最终映射；G0与整体PARTIAL/BLOCKED，不跳S1/Q28，不要求Continue。

300条专题建议不代表300个bug或全源三遍语义完成。剩余复杂训练/恢复等路径深审、HTTP/真实并发与真机声学仍需补齐，不得跳过门禁先修DSP，不得把任何未知签收。

持续中文短进度，不向用户提问，不承诺100%信心/零错误/零噪声。整体PARTIAL/BLOCKED，历史真实RTF0.3/训练闭环/长数据覆盖/声学逐字拒播缺口保留。当前忽略.venv沿用NumPy2.2.6及固定CPU/HTTP依赖、safetensors0.6.2格式测试；网关第二遍批曾新增go-bin==1.23.9，本批沿用但未重跑Go/race/vet，最近Go成绩仅为历史第三遍第1批；freeze与前批相同。当前无rustc/cargo/Torch/Qwen/完整权重/CUDA；前述无Go仅属先前批次环境。旧17收据不是本阶段重新执行。

## 历史首页（仅历史，上述当前状态优先）

# 完整交接提示词：Kaggle双T4 Qwen3-TTS语音克隆聊天

## 当前第十七阶段优先：长录音建档对齐/长短参考实验/生成参数绑定/连续朗读

用户截图是15，28.7秒/RMS约-46.6dBFS/peak0.014，创建报no aligned 2.5–16 s。要求超15秒录音可建档、超长与10秒参考都要更像、无噪声沙沙、双卡音色参数一致、自然完整朗读。先3轮100建议、逐题自问自答每题至少50建议、具体方案后小步实现、3轮检查/模型模拟、完整代码与全部备忘录。中文频繁进度，不向用户提问。不保证100%身份/正确/零噪声，不能凑语言或伪造硬件验收。

1. 最新完整包`kaggle/kaggle-fixed-step17.py` **313504B/53资产/SHA256 6eacaede14f9b5f42ac5c334df5c3f9d1a1c6858fb69b7d3a8ff241ec60427ea**。原始至16冻结，16最终306580B/SHA c6ed6c89e6356fc6c7ab554f96a2c3201a8e4690c007ea66626445cc658b4429。repack默认17；3001固定17完整复制/下载，正式3000的15文件/HEAD保持不改。截图15必须完整重启Kaggle部署17，刷新旧页面无用。
2. 三轮专题建议各100、全源读取/AST/哈希不是穷尽语义证明；问题22→23→24各50建议后实施，累计24题1200建议。57份完整备忘录内嵌。处置93新动作/174保留回归/27文档边界/6真实试听硬件阻塞，不把300建议当300bug或全新功能。
3. 确认根因：长录音限额不是15秒，旧候选只接完整2.5–16秒ASR段而丢弃已有words；单28.7秒段无候选。新reference_segments校验有限/单调/源范围和Unicode词文一致，按完整词切长段；缺时间或不一致就对实际音频窗口重ASR，优先低能边界，恢复绝对时间，不按字数/时长分配全文。短段无效word元数据移除但保留有效段转写；ASR仍非人工真值。
4. 快速建档/库处理/UI都有16默认、24实验参考窗口，手工文本只对单个≤所选窗口录音直用；长manual全文不强对齐，走ASR时间戳并记录策略。候选补边不超窗口，quality.reference_context记源总时长/锚点时长/all_audio_used_as_model_prompt=false/model_trained=false；quality.asr[].alignment记切分/重识别/短尾。长采集完整分析择锚，不等于20分钟全部ICL或训练，更长不保证更像/更快。
5. 原始PCM非有限拒绝，记录归一化前RMS/峰值，<-40dBFS风险提示进入已有decision显示；不是仅从截图判断无语音/设备坏。输入太轻归一化也放大底噪，检查距离与输入增益。保留16 ICL匹配转写、生成码专用codec、提示内存快照、禁参考PCM/呼吸拼接、默认增益6/目标-18与软限幅；不默认强低通或跨词重叠冒零沙沙。
6. 指纹升级qtts-voice-v2：参考WAV/UTF8文本/语言+四有效生成参数temperature/top_k/top_p/repetition_penalty，长度前缀和little-endian4 doubles。显式默认与缺省相同，拒绝NaN/Inf/非法/非整数top_k。同会话pin/模式/seed固定，Worker锁内复核、旧会话/混版本必须停后重启，不静默混旧参数。但相同条件不保证跨GPU逐位波形或声学100%一致。
7. 只朗读ReadSegCfg适度扩大聚合FirstMin12/FirstMax24/Min20/Target40/Max80，减少独立合成韵律重启；保留全文/标点/取消/背压/顺序，不跨词叠加PCM。不改Live聊天首句早触发。可能增加朗读首段等待/减少并行，不声称已经真实更自然或提速。codec仍25帧左上下文、默认右前瞻0。
8. 最终工程验证：Python334×3=1002、Node30×3=90、Go race3、六协议脚本各三轮；Chromium123×3=369、最终17完整复制另3、独立copy页剪贴板/下载/拒绝回退/手机3通过。新12项含28.7/60/1200秒对齐、缺词实际窗口、非法词时、16/24、低输入提示、参数pin。20分钟是时间戳规划，不是实际20分钟人声验收。
9. 冻结16真实build函数控制流vs17对照三轮：同29秒合成PCM、28.7秒ASR词段，16复现no aligned，17建档成功；实际读回24k候选WAV帧数≤16秒；缺词重识别窗口样本总数完整。ASR/说话人明确fixtures，不是真实Whisper。实际Faster0.5.4 resolver/prepare+生成码decoder三轮仍为CPU prompt/talker/kernel/codec fixtures；真实23813参数随机tiny codec三轮、完整Qwen导入/tinyMimi2651保存重载三轮、CPU tinyLoRA相对冻结13损失/全部adapter逐位同且6步骤三轮。都不是完整训练权重或GPU音质证明。
10. 初始失败保留：旧to16k测试替身把24k除2成12k，被新增边界校验拒绝，改测试真实2/3样本比，不放宽生产校验；固定跨语言hash从v1更新v2；旧长段一律拒绝断言改成不可信窗口不配全文；studio临时编辑脚本对字符串write_text失败后正确追加；长参考基线日志stdout污染初次JSON，导向stderr后重做三轮；低输入提示最终进入decision并新增第334项，完整重跑三轮。文件均在validation/step17。
11. **整体仍PARTIAL/BLOCKED**。没有用户实际WAV、Whisper/Qwen训练权重、CUDA/T4/DeepSeek可用通路，不声称短/长参考高相似、零噪声、双卡音色完全相同、自然整段或RTF≤0.3已达。真实基准tools/voice_benchmark.py仍可调用驻留双Faster三轮18条WAV/JSONL，无填充speech分母、worker与wall RTF各判，>0.3失败；本沙箱零真实测量target-rtf-not-run blocked，CPU/Mock不代替。历史网页真实训练闭环/维护租约切换/长数据审核对齐全覆盖/真实训练吞吐/声学逐字拒播缺口保留，完整目标22/300不升级。
12. 操作按STEP17_QUICKSTART：备份→完整重启双T4/Internet/nonMock/faster→完整17→双ready→录长音/选择16或24窗口→审核单人锚点与匹配转写→同源10/16/24秒三轮真机对照→逐GPU同文WAV与长文试听→播放首声/欠载/RTF另测。只问自己，不问用户，不删除锁/盲杀/卸载Torch，不默认每卡第二模型，不无依据重写稳定模块或新增语言服务。

以下step16及更早全部为历史；冲突以本段、STEP17_AUDIT及最终收据为准。

## 历史交接首页（step16及更早）

# 完整交接提示词：Kaggle双T4 Qwen3-TTS语音克隆聊天

## 当前第十六阶段优先：相似度取舍修正/单一参考版本/底噪风险/真实RTF0.3门禁

用户报告克隆根本不像、偶尔两种声音、沙沙声，要求真实RTF≤0.3。中文小步进度，不向用户提问；先3轮100建议与逐题自问自答，每题后50建议，再方案、增量实现、3轮完整验证、保存全部备忘录。不能保证100%身份/正确/自然度/速度，不凑多语言。

1. 最新完整包`kaggle/kaggle-fixed-step16.py` **306580B/52资产/SHA256 c6ed6c89e6356fc6c7ab554f96a2c3201a8e4690c007ea66626445cc658b4429**。原始–15冻结；15最终SHA61c063f0b2053321bfeafc8509bbbc1c91be183da72739186f7e5c4bf1899d43。repack默认16，3001固定hash完整复制/下载；正式3000的15文件/HEAD保持。
2. 三轮专题审查各100、问题19→20→21各50，累计21题1050建议；51份完整备忘录内嵌。全源哈希/AST不是穷尽语义无错。处置161新动作/53保留/49文档边界/32硬件试听阻塞/5未实施或否决，不当300个bug或300项全部实施。
3. 15强制纯向量可能牺牲相似度，不能假定正确。16默认有匹配转写的ICL，仅作为talker参考条件；decoder只接新生成码，绝不参考码或参考PCM。无转写拒绝，显式QTTS_CLONE_MODE=xvector仍可选。目标文字与参考转写分开，ICL仍可能音素/文字幻觉，严格声学拒播尚无。
4. 参考WAV+UTF8匹配文本+语言采用长度前缀SHA256，Go/Python互操作；会话每段携带同pin和conditioning模式、同seed。Worker取合成锁后重读档案检查版本/模式，在任何lead或PCM前拒绝不符。activation核对双卡收据并再次读版本；文本/候选部分reload失败返回503/reference_saved，不能宣称全卡ready。已播旧段不能撤回。
5. Faster0.5.4路径键不识别同路径音频替换，reload清该路径旧键；预计算提示保存内存快照，生成传voice_clone_prompt而非重新读取可覆盖锚点。提取前后内容指纹一致才发布；dtype重载清提示，后续需重建。原生训练adapter仍走受检句级缓冲路径，不回退Base；gateway按sentence-buffered发布类型固定native条件模式。
6. codec固定16码组/24k/1920样本每帧，契约不符明确失败；25帧左上下文、有界窗口，不全历史cat，不比例裁参考。仅输出未提交样本；尾flush幂等、取消无迟到PCM。最初拟2帧前瞻，实际Qwen12Hz因果源码/真实23813参数tiny随机decoder的8→12帧前缀误差0后改默认0；QTTS_CODEC_LOOKAHEAD_FRAMES=2仅显式实验，不能假装真实沙沙根因已知。
7. 输出目标仍-18dBFS，默认最大增益6（显式0..12，非法回6），每任务重建leveler/DC/包络，保留Rust/NumPy软限幅/淡入淡出；空生成不flush旧声尾。低噪声放大风险改善不等于声学降噪已验，轻声可能比15上限12稍轻；不默认强低通/谱门伤清辅音。用户未供实际噪声音频，不能精确确认所有声学根因。
8. tools/voice_benchmark.py显式--run，调用已有真实双Faster worker而非第三模型；空闲、ready、ICL生成码模式、物理GPU0/1独占。参考预热单列，3轮×2卡×3文=18条，保留私有WAV与逐条JSONL；标准RTF=gen_wall/未填充语音秒数，另HTTP wall RTF，排除lead/tail/fade、失败/取消/anomaly。任一条>0.3即target-not-met，达标仍仅measured-speed-only、音质待听。当前沙箱零真实测量、target-rtf-not-run.json blocked，不把CPU/Mock/双卡相加/改语速/填静音当0.3。
9. 最终工程证据：Python322×3=966，Node30×3=90，Go race3，六协议脚本各三轮；Chromium121×3=363，最终整包复制额外3，独立copy页剪贴板/下载/拒绝回退/手机3。真实Faster resolver/prepare+生产generated-only decoder三轮，每轮ICL/xvector×chunk2/4/8/12、80帧153600样本，参考标记从不进codec、同路径提示正确更新，但prompt/talker/kernel/codec为明确CPU fixtures。实际tiny随机Qwen12Hz decoder23813参数三轮、每轮8组合/40帧76800样本；不是训练codec或完整TTS。完整Faster/Qwen导入/tinyMimi2651参数保存重载三轮；CPU tinyLoRA相对冻结13损失和全部adapter张量逐位相同、6步骤三轮；真实HF smoke/API检查pass但无CUDA整体blocked。
10. 初始失败全部保留：旧15策略/接口/未重打包断言；native adapter测试实际注入引擎与Mock/faster模式误推断，按发布类型修正后A-B-A与损坏adapter拒播通过；测试ready文件先创建后写PID被并行父进程读空，测试夹具改原子rename且启动前记录旧run，不放宽锁释放；浏览器360通过/3同旧“第十五阶段”文案断言失败，改16并新增ICL/待测声明，定向3后完整363+复制3通过。不能把这些初始失败藏掉。
11. **整体仍PARTIAL/BLOCKED**：无用户实际音频/完整训练权重/真实T4/DeepSeek，不能声称高相似/单一音色/无沙沙/真实RTF≤0.3已验。历史网页训练CPU控制面闭环、维护租约切换、长录音审核对齐/全样本覆盖、真实双T4保质训练吞吐、声学逐字拒播仍缺；完整目标22/300不升级。两T4各一模型不改，不默认每卡两模型，不无依据换语言重写稳定模块。
12. 实机按STEP16_QUICKSTART：备份→完整重启Kaggle→T4×2/Internet/nonMock/faster→完整16→双ready→审核单人锚点及逐字匹配转写→重新启用→不同正文直接朗读/长文跨卡试听→真实基准18条→DeepSeek首句/播放first_played/欠载。bootstrap返回后可用后续Notebook单元格跑CLI。不给密钥、不删锁、不盲杀或卸载Torch；Kaggle配额和会话永久性不能承诺。

以下step15与更早均为历史，冲突时以本段、STEP16_AUDIT及最终final-checks.json为准。

## 历史交接首页（step15及更早）

# 完整交接提示词：Kaggle双T4 Qwen3-TTS语音克隆聊天

## 当前第十五阶段优先：参考隔离/首句/增响/创建复用，真实T4音色与提速仍未验收

用户报告step14播放克隆语音插入参考原音、创建档案256.4秒，要求不播放任何参考片段、DeepSeek首段及时合成、提高输出音量和创建速度，询问单T4双1.7B。截图没有原音频，不能确定具体声学根因；不问用户问题，中文小步进度，不能100%无错或凑多语言。

1. 当前完整包`kaggle/kaggle-fixed-step15.py` **291325B/48资产/SHA256 61c063f0b2053321bfeafc8509bbbc1c91be183da72739186f7e5c4bf1899d43**。原始至14冻结，repack默认15；独立3001固定15完整复制/下载，正式3000的15文件与HEAD不动。
2. 三轮专题代码研究各100建议、全源读取/哈希/AST不等于语义无错。问题16→17→18每题50建议后实施，累计18题900建议；45份完整备忘录内嵌。处置逐条区分修改/保留/文档边界/硬件待测/未实现，不把300建议当300bug或900实现。
3. 实际Faster0.5.4源码ICL会将ref_codes带入codec上下文再裁参考，xvec_only说明防参考phoneme bleed-through。Worker加载、dtype回退预热和生成统一xvec_only=True/ref_text为空/append_silence=False；不提供ICL环境回退。旧breath_files不读取，reference环境也不能启用拼接，lead仅零停顿。模型自身呼吸保留；stats reference_pcm_splicing=false是代码政策，acoustic_text_verified仍false。向量模式可能改变韵律/音色相似度，未做真实试听，不能称质量无损或保证不幻觉。
4. Go仅聊天LiveSegCfg首句完整边界就提交，不等待下一delta；短完整中文句可提交、尾空格处理，ASCII小数点/未闭合引号仍有lookahead。普通朗读ExactSegCfg、后段、顺序/背压/取消/播放器稳定水位不改。不是每个token生成，也不保证<3秒。保留chunk默认4，2..8显式试验。
5. 共享output_target_dbfs默认-18，合法-24..-14，非法/非有限回退-18；Worker新旧档案均最大增益12dB（旧9），保留Rust/NumPy软限幅/DC blocker/平滑/淡入淡出，源录音不改。小信号合成测试较响，不代表全部硬件或语音恰好+3dB。
6. 创建/库处理/UI锁定重置/后端缺省均不追加可选GPU校准，手动入口与勾选仍在；CPU ASR允许复用，QTTS_ASR_KEEP_CPU=0关闭，CUDA仍卸载；ASR RLock覆盖加载/惰性转写迭代/释放，避免诊断与创建并发释放模型。保留全量ASR/beam5/24候选/打分/准确最佳F0。嵌入缓存按样本hash、只本任务最多64条，不跨档案持久化。
7. 创建保存最终quality.build_s/stage_ms/embedding_cache、界面可展开，重新读校准后profile避免覆盖选择。修复“截14秒配全文”，只用完整2.5–16秒对齐回退片段；16秒手动全文不截14秒。超长ASR段无可信切分明确拒绝，不猜对齐。冷下载/CPU大ASR仍可能慢，无用户原录音A/B，不说256秒已降到多少。
8. 单1.7B FP16纯参数约3.4GB、两份6.8GB不含codec/KV/graphs/临时张量；同T4共享计算带宽，装下不等于单请求快。不默认每卡双副本，继续两卡各一模型，峰值/吞吐须真实T4测。
9. 工程验证：Python301×3=903（ASR并发修复后重跑通过）、Node30×3=90、Go race3、6协议脚本各含3轮；真实Faster resolver→prepare→两阶段streaming控制流三轮，每轮chunk2/4/8、40帧76800样本、decoder无参考码，但prompt/talker/codec是明确CPU注入fixture，不是完整Qwen。完整Faster/Qwen import及2651参数tiny Mimi构造保存重载3轮、required HF CPU smoke3轮通过，整体无CUDA仍blocked。完整Chromium120×3=360通过（10.5分钟），最终整包复制另3通过，独立复制页剪贴板/下载/权限拒绝/手机3通过。原初次357通过/3等义提示文案断言失败保留，断言兼容“执行”两种写法后完整重跑通过。最终以step15/final-checks.json为准。
10. 新测试初始低音量同9dB上限无增响，改worker最大12并保留限幅；Go夹具直接读Session.jobs早于enqueue导致race，改真实队列pickLocked后race3通过；ASR惰性迭代需全周期锁的复核修复已补并发回归；日志目录未建导致初次安装重定向失败，已恢复。错误不隐去。
11. **整体PARTIAL/BLOCKED**：真实Qwen/T4参考重播/音色/韵律/首播/创建A/B未验收；历史独立CPU网页训练控制面/维护租约移交/实际start-cancel-progress-restore-publish、长录音审核对齐/超过16样本全覆盖、真实训练保质吞吐、声学逐字拒播仍缺，完整目标22/300不变。不能把部分交付当需求豁免。
12. 用户操作见STEP15_QUICKSTART：备份私有数据→完整Kaggle会话重启→T4×2/Internet/nonMock/faster→复制15→等双worker ready→已有普通档案重启用→不同于参考的目标文本直接朗读试听→再试DeepSeek首句；不要删锁、盲杀PID或卸载Torch。Kaggle配额/会话驻留不保证永久。

下面第十四阶段及更早内容均为历史，冲突时以本段与STEP15_AUDIT/最终收据为准。

## 当前第十四阶段优先：部分功能修复，不能冒称全部需求完成

用户新增十多分钟网站录音、点击真实训练/保质最快、多线程、自然呼吸、首声、准确逐字播放要求；不要问用户重复问题。先三轮审查各100条（REVIEW1/2/3），再顺序问题13/14/15各50建议，已落盘PLAN后实施。15题750建议，完整目标22/300不变，39完整备忘录内嵌；语言分工仍Python/PyTorch+CUDA、Go、Rust、浏览器JS，不为语言数量引入新系统。

1. 最新kaggle/kaggle-fixed-step14.py，285094B/48资产，SHA256 73a02a95919406c4570ea563f0c0475fdde17535e6ccd16764c32514fce2c369。原始至13冻结，repack默认14；3001只读复制页切14，3000正式15文件/HEAD不动。
2. 用户随后提供step13真实Kaggle日志：HF RoPE required pass、两T4加载/预热ready、190s、Rust on、公开隧道完成，SystemExit0只是包装器正常退出。记录step13/user-runtime-startup-ready.json，不能继续说双卡启动未知；但没有真实音频合成/训练/音质证据。
3. 浏览器录音1199000ms、8192 chunks、64MiB单文件/127MiB本地合计；Python/Go请求128MiB，服务端1200秒/1800秒合计。原始库64MiB/库/512MiB总量仍独立限制，高码率WAV可能先到字节上限。11分钟虚拟控制/2640块及660秒合成PCM解码完整验证，不是物理麦克风实验。
4. TTSDataset有界64MiB CPU张量缓存与调用者来源deepcopy/返回clone；不变loss/数据顺序/优化器/步数。grad finite合并host读取、保留collective与clipping。run_rank记录cache/tokenize指标，HF版本报告不再只查官方qwen-tts。
5. frozen13真实训练/数据源与14做CPU tiny LoRA A/B，三进程×三epoch，每次6optimizer步，loss与全部adapter tensor逐位一致，tokenizer12→3。fixture墙钟有冷启动/顺序偏差，不能写真实训练倍速、质量更好或最快。
6. 实际newSession用ExactSegCfg，不再CleanDelta删正文/补句号；保留多delta内容，纯标点/空白片段旧过滤仍在，不保证模型声学无漏添字。没有ASR核验拒播闭环，不要称“播放每字完全核验”。
7. 默认QTTS_BREATH_MODE=off，不后加呼吸；reference只用真实bank，空bank不生成噪声。模型自身呼吸没盲滤，主观自然度仍需试听。first_chunk_ms为裁边后非空PCM，model_first_chunk_ms是模型首块；runaway静音可能仍放行，不是ASR确认人声。first_played/欠载另测。QTTS_FIRST_CHUNK_SIZE=2可实验（2..8），默认4/稳定播放器阈值不变，首声未证明改善。
8. **网页真实训练仍未闭环**：快照/参考处理不执行优化器，未添加假训练按钮。现有真实双rank CLI保留，但网页要独立CPU控制面、维护态停止两GPU/analyst且保留网关、验证租约交接、固定审核数据/Base/码、实际训练/取消/进度/恢复/候选发布。不能在analyst开线程绕过fleet锁，也不能把十分钟当单条SFT或均分文本猜对齐。现有训练快照仍最多16条，长数据分片/manifest及全部样本覆盖亦需扩展；不得只取前16条冒充全量入训。下一核心应做这条闭环，不是再加准备工具。
9. 本阶段全部用户需求状态PARTIAL/BLOCKED：缺真实长音频审校、独立网页控制面、真实Qwen/T4训练/音质/首播/声学逐字验收。三轮回归只覆盖实现范围：Python285×3=855、Node90、Go race3、五协议各3、fatal控制3通过；浏览器117×3=351通过（10.4分钟），最终包复制另3通过，独立剪贴板/下载/手机/拒绝权限三轮通过。结果见step14/final-checks.json；不输出100%或全部成功。HF实际包与微型Mimi CPU回归保护13成功路径，不是完整Qwen/GPU验收。
10. 操作见STEP14_QUICKSTART：先备份私有数据，停止并重启完整Kaggle会话，再T4×2/Internet/nonMock默认faster复制14。不要删锁/按旧PID杀；API口令不公开。健康会话内resident保留，Kaggle配额/超时不可保证永久。原生adapter仍sentence-buffered，真实训练/重载/声音边界保留。

---


## 第十三阶段历史：已获用户双T4 ready日志，新增目标以14为准

用户step12真实Kaggle仍在两个T4上报同一MimiConfig.rope_theta；不要怪用户、不要说上次已修好。下面12及更早记录为历史，当前以本段/STEP13审查/最终收据为准。不问重复问题，中文小步进度，继续同一arena/041344f2-kagglee分支。

1. 最新完整kaggle/kaggle-fixed-step13.py为282346B/47资产，SHA256 dad142d75be94d8efb6567fc1f8755d3f37341a65d5c7fe9454fd36c87770e60。原始至12冻结，尤其12为282031B/SHA2be33a3a6735639ce32ec8750e9a489abd96e4daa780d068557f2b0156f2de08；repack默认13，不能改旧包伪造成功。
2. 真实faster0.5.4 wheel model.py第194行在from_pretrained才导入qwen_tts；顶层只导出包装类。step12只看sys.modules，误把尚未导入当not_applicable。之前手动exec真实wheel函数的数学验证没有覆盖生产入口生命周期，是我们的漏测，当前已真实复现。
3. qwen_compat现在按已安装发行元数据选HF/legacy，先检查HF0.1.1.post1/TF5.20.2和namespace冲突，再正常importlib.import_module导入实际compat及父包，注册完成后安装窄范围bridge；未知组合/导入失败/矛盾元数据拒绝。官方legacy无HF仍不适用。未猜theta、未改权重或config、未改平台Torch/CUDA约束、未全局接管Python导入。
4. backend_probe HF数学smoke必须installed且configuration_smoke_passed=True；HF存在却跳过/不完整时required blocked，不再warning后surface_pass。只有HF发行真不存在的legacy可warning不适用。Worker/native/CPU编码/训练继续共用同一函数并在构造模型前安装。Resident/fatal/nonce/ownedPopen清理原样保留。
5. 实际完整Faster/Qwen包隔离缓存正常导入，不mock第三方导入。冻结step12函数先返回not_applicable，再导入Qwen+构造真实微型Mimi复现相同AttributeError。新函数从同一冷状态installed，真实TF微型MimiModel2651随机参数构造/保存/本地from_pretrained重载，三种theta缓冲精确对照、config不变、实际初始化进入bridge12次、幂等；三独立进程PASS。是完整包导入+微型Mimi，不是完整Qwen1.7B模型加载。
6. 额外真实隔离backend_probe CLI三次：HF smoke required PASS，但无CUDA所以整体blocked，不能把该证据写成GPU预检成功。证据在real-preflight-cpu-round1..3.json；网络被禁止，不下载完整模型。主venv未污染，隔离站点/home/user/.cache/qtts-step13-site与step12-site，轮子在qtts-wheelhouse，不入Git。
7. Python273×3=819PASS，Node30×3、Go race count3，四协议脚本各三次内置三轮共9轮，adapter三轮、fatal真实supervisor CPU worker三轮已PASS。完整浏览器114×3=342PASS（11.4分钟）；最终整包复制另3PASS；独立真实剪贴板/下载/手机/授权拒绝回退三轮PASS；最终门禁见step13/final-checks.json。新增6兼容回归；初始隔离缺依赖、测试断言假设旧接口、旧CPU替身伪造所有发行元数据而触发冲突均保留初始日志，生产门禁没有削弱。
8. 三轮各100条定向建议见review-map；完整目标仍22/300，12题600建议不等于600实现。交接嵌33个完整备忘录。3001只读复制页已切13，原3000工作台15文件1043155B及HEAD39ed7670-ec8a-4565-a1ae-fff0064d5246保留。用户要真实复制按钮，不要只报文件路径。
9. 用户实际现场已确认两个T4、每卡15636037632B/CC7.5、Python3.12.13/Torch2.10+cu128、下载与Go/Rust构建完成；截至step12两worker仍加载失败。新step13完整Qwen/T4加载/graph/显存/声音未验证，不能保证下一次一定成功。SoX二进制在CPU缓存实验缺失警告，不曾验收其音频转换；Faster/flash attention警告不等于本错误。
10. 下一步直接按STEP13_QUICKSTART：先备份需要的私有数据，平台停止并重启完整Kaggle会话（不是只重启内核或网页），T4×2/Internet/nonMock默认faster复制完整13。HF smoke必须pass；两worker真正加载/warmup完成后才验证短句/长句/停止/显存与声音。旧PID不得盲杀或删锁；平台保留旧标记时确认整个会话已重启后可新QTTS_ROOT，旧数据另行管理。不再加开发准备前置。
11. 默认每GPU一份健康模型在会话内resident，不按600次或旧13.5GB阈值主动回收，异常/OOM仍可中断。Kaggle配额/超时/回收不可由应用阻止，不承诺永久双GPU驻留；原生adapter依然sentence-buffered而非声学流，实际训练/NCCL/质量/性能仍未验收。

---


## 第十二阶段历史交付（随后实机再失败，不能沿用其修复完成结论）

2026-10-21。先STEP12计划与Q11（50建议）再实现；中文短进度，不问重复问题。仍在arena/041344f2-kagglee分支，不切换。下面第十一阶段与更早内嵌历史均服从本段。

1. 最新kaggle/kaggle-fixed-step12.py：282031字节/47资产，SHA256 2be33a3a6735639ce32ec8750e9a489abd96e4daa780d068557f2b0156f2de08，repack默认12；原始至11冻结。复制预览3001已切step12，原正式3000工作台15文件1043155B/HEAD39ed7670-ec8a-4565-a1ae-fff0064d5246不改。用户已明确要从浏览器复制，不要只让用户找文件。
2. 用户实际日志：两Tesla T4、CC7.5、每卡15636037632B、Python3.12.13/Torch2.10.0+cu128/faster0.5.4/Transformers5.20.2；下载/Go/Rust完成，但两worker加载报MimiConfig无rope_theta并重启。GPU识别有现场证据，模型加载/声音仍没有成功证据；不能把signature preflight通过当模型通过，也不能继续说用户GPU完全未知。
3. 已审查真实PyPI wheel：faster0.5.4依赖qwen-tts-hf>=0.1.1.post1和TF>=5.15.1，不能单降4.x。HF0.1.1.post1默认RoPE仍读旧字段，现代Mimi用rope_parameters。qwen_compat.py仅包装已识别默认函数，从实际配置读theta/partial factor到临时副本，不猜10000、不改config或权重、不替换未知registry/scaled schema。导入Qwen后、加载模型前接入Worker/原生adapter/CPU编码/训练。
4. 真实TF5.20.2 Mimi类+实际HF wheel函数已在CPU复现相同AttributeError，修复后三种theta10000/12345/1000000频率精确对照、原配置不变，三进程PASS。不是完整Qwen包/权重加载或GPU实验。元数据/完整requires_dist/源成员SHA与失败记录留在step12证据。
5. bootstrap固定faster0.5.4、qwen-tts-hf0.1.1.post1、TF5.20.2，安装对当前Torch/torchaudio/torchvision加版本约束，不盲升级/卸载平台CUDA。官方qwen-tts与HF共享命名空间冲突拒绝；native仍可用官方legacy provider，模型入口能力不因本阶段删掉。预检新增实际Mimi/默认RoPE CPU数学smoke，仍标no model/GPU。
6. 已知RoPE配置错误fatal；supervisor停止该worker重试并写启动nonce绑定的失败收据；bootstrap看fatal健康或本次收据提前失败。失败/异常/中断清理自己创建的Popen，45s未确认则要求完整会话停止，不拿旧日志PID盲杀、不删GPU锁、不假称资源已空闲。真实supervisor+CPU fatal-health三轮验证收据、worker/sup退出和PID标记清理PASS。
7. 默认QTTS_RESIDENT=1，健康模型不再按600请求或旧13.5GB门槛周期重载；高显存告警，empty_cache不释放活权重。QTTS_RESIDENT=0保留旧策略。每worker独立可见GPU0/1；health包含requested_model/model_loaded/cuda_visible_devices/residency_policy/fatal_error，Mock不报真实loaded。错误/OOM/平台回收仍可中断，不作永久驻留保证。
8. 用户要求“永久部署双卡”必须诚实解释：应用只能在会话存活/健康时各卡一份常驻，Kaggle配额/超时/关机会回收GPU；磁盘/私有Dataset缓存不等于GPU继续运行。长期常驻需要持续双GPU服务器，本次没采购外部硬件或绕过平台限制。
9. 完整Python267×3=801PASS，Node30×3/Go race count3、五个旧协议/adapter脚本各三轮PASS；新增14项兼容/驻留/fatal/依赖约束测试。浏览器113×3=339PASS；另最终包复制3PASS，独立真实剪贴板/下载/手机/拒绝授权三轮PASS；首个独立Chromium启动SIGSEGV记录保留，重跑成功，原因未确定。完整收据见step12/final-checks.json。11题550建议，三轮100项范围映射，完整目标22/300不冒充全部修复；完整内嵌30备忘录。
10. 下一步直接按KAGGLE_STEP12_QUICKSTART.md：先备份所需私有数据，停止并重启完整Kaggle会话（非仅内核/网页），复制step12，T4×2/Internet/非Mock。若旧目录PID标记保留，不盲删，可确认完整会话已重启后使用新QTTS_ROOT；旧数据另行管理。先smoke再两worker完成加载/warmup、workers_healthy=2，再真实短句/长句/取消/显存与音质。沙箱无CUDA/完整模型，不能保证此次目标复跑必成功；不再加准备工具前置。

---


日期2026-10-21。中文短进度，先保存计划再写码，不向用户重复提问。当前第十二阶段优先于内嵌历史；失败/blocked原始记录保留，CPU协议/替身不能冒充Qwen/GPU。目录/home/user/Kagglee，分支arena/041344f2-kagglee固定，不切换/改名，不需提交来保存。

## 第十一阶段历史状态：直接adapter推理/聊天接入已实现

1. 最新独立交付kaggle/kaggle-fixed-step11.py，276043字节/46资产，SHA256 cd5346e8ae34f1e2db327a076a7411996982848f9d4e14236f05d94c626d496e。repack默认step11/source_manifest_step11.json，原始至step10冻结；step10仍261429字节43资产SHA256 2bddd6ebad371268f9b3b02315fc29cae588da6c46c7d134476945b50b8a5ac4。源代码变更不能覆盖冻结包。
2. 本轮不是另一个准备工具阶段：先STEP11计划/Q10，再实现trained_profiles.py、adapter_engine.py、trained_voice.py及事务式LoRA切换，接入现有Worker→Go→网页选择/聊天。已有阶段10真实loss/backward/optimizer/DDP/adapter训练代码保留，不要说还没开始开发，也不说真实Qwen已经训练成功。
3. 默认faster声学流式路径保留，原生只有QTTS_TTS_ENGINE=qwen-adapter-buffered显式启用。官方原生完整一段才输出wave，标注sentence-buffered，不切假chunk、不声称<3秒/声学流式。每GPU一个可见设备/一份可信本地Base，FP16/eager。未实测16GBfit/峰值显存/质量，不能自动换小模型或预置说话人。
4. 发布要求真实completed run/request/result、固定manifest/Base/码pin、两个rank更新及每epoch覆盖记录、tensor摘要/shape/finite、实际schema2编码码租约；复制统一参考及对应文本为命名训练候选，不自动active。记录/声明不是官方签名或权利/身份鉴定，不防同UID恶意伪造整个状态。fixture/legacy不升级或发布。
5. 所有新LoRA模块先构造校验再锁内事务切换，支持不同rank及A/B/A；每段复核profile和adapter，保存speaker直接官方x-vector-only prompt。Mock/faster拒绝训练profile，原生拒绝普通profile；缺/坏/错误Base必须报错无PCM回退。缓存不是永远正确，两worker一半加载失败时active保留，下次按请求profile重选。
6. 新profile仍沿旧profiles私有Dataset备份，含一参考WAV/对应文本；run/完整模型/全体样本不自动备份。恢复缺Base/adapter报错；删原码/源库/profile/run/远程备份不同。训练参考只读，编辑/候选/校准409；旧普通profile与删除保留。
7. 原有两主视图、录音波形/上传/命名库/输入/码/认证/DeepSeek文字流/切段/有序播放/停止与源码复制保留；没有第三主视图或假训练按钮。原生取消只在AR步合作检查并丢迟到wave，不抢占CUDA kernel/codec decode。原生无帧/health/supervisor预算180秒，默认60/75/90秒不变；不是性能承诺。修复一致性检测全失败仍可能consistent=true的门禁。
8. Python252×3=756PASS，Node30×3、Go race count3PASS。新24adapter项包括真CPU LoRA输出/切换、隔离/错误拒绝/HTTP/取消；真实本机Go/双worker/本机SSE+CPU tiny LoRA接口替身3轮A/B/A及坏版本503/active保留/无PCM通过，不能写成真实DeepSeek/Qwen/NCCL。旧四协议脚本各调用3次、每次3轮（各9轮）PASS。浏览器112×3=336PASS（11.0分钟），最终包额外逐字复制3次与step11/final-checks.json核验；不是目标模型证据。
9. native runtime probe blocked退出2，沙箱Torch2.8/cu128仅CPU，CUDA不可用、无qwen_tts/真实权重；实际Base config标识base/1b7/16组也未拿真实权重核验。真实双T4训练、新进程重载试听、声学质量/RTF/首声、物理麦克风与DeepSeek外网服务均未验收。
10. 正式工作台仍HEAD39ed7670-ec8a-4565-a1ae-fff0064d5246，15文件1043155字节，1MiB余5421；新包独立交付，不塞入正式满额项目，不提高上限/删历史。用户自命名文件初始为空、自己粘贴；Python复制不是在JS iframe执行。浏览器测试仅隔离临时项目。
11. 已按10题各50建议累计500；300项目标22已验不变，不是代码开发百分比/300新修复。本交接完整内嵌27份备忘录，不以摘要替代原文；历史阶段叙述以本段最新状态覆盖。失败browser-initial/python-initial-failed保留；探针AST修正为分别匹配faster与native真实关键词。

## 直接下一步，不再增加准备阶段

按KAGGLE_TRAINING_QUICKSTART.md和KAGGLE_ADAPTER_QUICKSTART.md在真实双T4/可信模型/自己授权的实际编码数据上尝试首步，收集真实错误/峰值显存；完成后用真实run及pin发布候选，在新进程重载、每卡保存并试听WAV、A/B/A、DeepSeek长回答与停止恢复。仍然没有网页自动训练、完整CustomVoice或可恢复optimizer/scheduler/RNG；不要把新CLI发布当训练。没有可保证的成功日期、99.5%身份相似率、<3秒首声或永久Kaggle会话。当前工具/测试均非下一轮阻塞前置。

## 第十阶段既有实现：实际训练核心已开发

用户追问何时真正开发。本轮停止前置工具循环，保存STEP10/Q9后直接实现lora_adapter、tts_dataset、tts_training、training_job与tools/train_tts.py，附上游完整Apache许可证。没有新语言或生产网页/Go改动，不自动停推理或部署adapter。

- 真实联合loss、text_projection、DDP.forward内全部参数调用、FP16/eager/microbatch1、冻结Base1.7B及speaker encoder、FP32 attention q/v LoRA与AdamW状态、非重入梯度checkpoint、真实backward/梯度同步/正确尾部累积/GradScaler/全rank有限值与更新检查。
- 每rank一个CUDA设备、NCCL、确定性每epoch分片；奇数重复前缀填平不drop_last，保存每rank覆盖。至少参数改变、两rank最终摘要一致且全部样本覆盖才可保存adapter。不是两个独立微调，也不是只启动torchrun。
- 父及两rank受控共享GPU offline-reservation与码读取OFD，子在Torch前PDEATHSIG/ppid握手，Popen记录PID窗口屏蔽取消后子解除屏蔽；启动失败/单rank失败/超时/取消等待直接rank退出，最后FD关闭再释放。DataLoader无额外进程，不能扩展为任意外部子孙任务管理。
- 拒绝fixture/legacy/未实际编码/少于两样本，要求显式数据审阅与实验确认；Base内容pin和其speech_tokenizer必须匹配码来源。严格离线，不自动安装/下载/信任remote code；hash和用户声明不是官方签名或法律/语义鉴定。
- 保存本地adapter.safetensors、speaker.safetensors、Base/码hash与rank数值/版本/显存报告；load_adapter严格绑定/成员/张量核验后挂到单独Base，返回speaker向量。不是完整CustomVoice，没有resume optimizer/scheduler/RNG，未新进程Qwen试听或自动接入网页语音聊天。
- CLI可在真实环境模型/数据就绪后立即尝试，不需等下一开发阶段；KAGGLE_TRAINING_QUICKSTART.md给出实际list取pin、Base指纹、可取消Notebook调用。不要给出没有实测的训练成功日期/显存/音质承诺。

## 第九阶段既有实现（当时来源/读取边界；第十阶段已扩展FD接管）

先保存STEP9计划与Q8的50建议。生产仅增量修改training_codes.py/encode_training.py及MEMO，生产网页/Go/语言与GPU协议不改。没有新HTTP入口或假训练按钮。

- 新码schema2原样封存source/manifest.json和source/train_raw.jsonl；固定创建时源manifest hash，源JSONL/rank计划hash与源清单一致；逐项核对现有码的ID/顺序/帧数/audio/text/ref。保留库名/ID/修订、原始样本名/hash和用户使用权/单说话人声明；声明不是法律或身份鉴定。
- source纳入受限文件集、权限/链接拒绝、全部字节预算和暂存/核验/发布/回滚；不自动云备份，不额外复制原库原件音频。新码删除原库与输入后仍可独立核验封存记录。
- schema1旧码保持列表/核验/读取/删除且旧字节/hash不变，明确legacy-unsealed，不用当前库猜旧授权。list只描述格式政策，provenance_verified_now=false；schema2本次完整verify成功才为true。
- 码专用lease固定码manifest hash并完整验证，持目录外.use-ID独占flock后释放全局锁再yield；读期删除/第二读取同版本409，列表/核验/其他版本可用。正常/异常/进程死亡释放FD；fork继承最后引用活着则仍busy，不LOCK_UN/PID/TTL抢占。
- 这是可信调用者合作式只读，不是OS只读挂载或同UID恶意并发写防护。阶段9当时没有多rank接管；阶段10已接入受控共享FD，仍须保护到所有读者退出，并另做真实编码、语义/权利政策、设备及训练门禁。
- hold-read --seconds 1..3600只保持检查，沿用总timeout1..3600/取消/PDEATHSIG，收据training_allowed/gpu_verified/training_verified均false，不输出私人转写/完整来源、不执行命令/GPU/训练。fixture/legacy状态不升级。timeout含启动/核验，保持时长不含；长保持须留总预算，不能认为3600秒两参数必定刚好完成。

## 第八阶段具体实现（继续保留）

先保存STEP8计划与Q7的50建议。新增py/gpu_ownership.py和tools/resource_control.py，增量接入supervisor/worker/analyst/bootstrap。生产JS/HTML/Go未改，CPU编码仍仅CPU，旧库/授权隔离/输入租约/事务输出与所有快捷流程保留。

- 固定/tmp/qtts-gpu-ownership-{uid}/fleet.lock，同机同UID整组独占，不按STATE/CUDA索引/UUID分区。0700/0600、属主/普通文件/软硬链接/权限检查；应用不unlink/replace锁文件，不按PID或TTL抢占。
- 真supervisor先独占inference，再通过pass_fds仅给worker/analyst；孩子检查inode/nonce/模式/当前锁并采用同一OFD，gateway不继承。close只关引用，不LOCK_UN；父关/父SIGKILL但孩子活着时仍busy，最后引用关闭才释放。
- 独立真实worker/analyst也须独占整组，多个模型进程应统一由supervisor启动。Mock跳过，不宣称GPU所有权；CPU encode不占GPU，剥离GPU内部FD/nonce环境。
- 第二真实supervisor先占锁、失败不写supervisor.pid，成功后只清自己的PID标记。父日志句柄及时关闭，kill等待leader退出并清理仍活的进程组后代；停止信号注册早于启动，STOP期间不再拉起。
- bootstrap不再根据旧PID发信号或宽泛pkill；busy/遗留PID标记在探针/依赖安装前明确阻断，需人工确认停止。ready等待检查本次supervisor仍活着，不把旧服务健康当新启动成功。仍保留原安装/探针/下载/备份流程，真实目标兼容尚待验。
- resource_control.py status / reserve --seconds 1..3600，只观察/空闲预约，无GPU工作/任意命令/HTTP/force-unlock。预约不是显存释放、编码或训练。status观察busy和非权威last_record，永远gpu_verified=false，不公开nonce。
- 预约正常0、拒绝2/code409、SIGINT/SIGTERM取消130；SIGKILL由OS关闭FD回收。父SIGKILL后活孩子持锁是安全行为，不删锁文件强行“恢复”，须核实并停止本应用遗留模型进程。
- supervisor存活检查不等于所有新网关/子进程就绪，尚无本次作业代际ID贯通健康响应；旧端口占用仍需排查。bootstrap前置检查也不替代解包前停旧服务。
- 整组锁是保守准入，更多卡/不重叠子集也不并发。不能限制跨UID/容器或绕过协议的软件，不能防同UID恶意删改；没有实际CUDA测量/OS硬件隔离/显存回收保证。
- 升级前先停干净step1–7进程，旧版本不自动加入协议；新包会写目标ROOT源码，仅检查用独立ROOT/UNPACK_ONLY。旧runtime PID标记须核实旧服务停止后再清，绝不是删资源锁或改正式工作台HEAD。Mock/真实服务不混用同一STATE。

## 前置数据链路与真实边界（继续保留）

训练输入是完整24kHz单声道PCM16 WAV，逐条转写、统一参考、使用权/单说话人声明；固定源库修订/样本ID/哈希。浏览器Opus不可直接作为首版输入，不改后缀或裁剪，旧参考解码流程仍保留。源/选中集合变化清旧声明与文本，关闭/锁定拒绝迟到私有响应。

编码入口仅本机CPU/FP32/eager/两线程/单样本numpy全波形，要求可信本地物化JSON/safetensors全目录指纹，拒绝pickle/软硬链接/auto_map/越界分片。哈希不是官方签名，运行时包version不是源码身份校验。模型前后指纹与输入读取租约、原子输出/预算/回滚仍在。

返回必须一个样本、ceil(frames/1920)×16整数0..2047；规范WAV/text/ref_audio/rank数学计划完整复制。路径以码副本目录为cwd，不能相对原输入猜测。真实返回也只有tokenization_executed，不自动变tokenization_verified/训练/两rank/推理；测试码test_only_codes，不提供CLI Mock参数。

schema2完整封存源记录，schema1仅源ID/hash明确legacy-unsealed。输入与码版本读取租约均已实现，本轮已经接入实验性训练器/两rank受控FD生命周期；不能把检查租约当训练许可。取消/超时可能恰逢rename后收据前，list+固定hash verify再决定重试；临时文件不是安全擦除。

## 第十阶段分层证据（docs/validation/step10/）

- Python227×3＝681 PASS，新增25项训练核心/准入/OS生命周期与step9冻结回归，无Torch跳过；实际CPU联合loss/反向/AdamW参数更新、FP16基座/FP32梯度/冻结不变、尾部累积、nonfinite拒绝、严格adapter保存/重载。
- 实际两进程Gloo小网络参数改变、不同分片、最终摘要相同；每轮单元测试含一次，另trainer_tensor_check.py三轮把摘要/loss/步数保存gloo3.json。不是Qwen、CUDA或T4。保留find_unused警告，真实模型分支未知，不宣称极致速度。
- 控制器生命周期用真实Popen/pass_fds/pidfd/SIGTERM/SIGKILL/共享FD，角色仅CPU持锁替身，测试内部注入绕过fixture准入仅测协议，生产CLI没有此开关。零退出但无checkpoint不成功。
- Node API30×3、Go28顶层/16子测试race三轮、真实HTTP/旧CLI/资源FD/CPU Mock管线各三轮通过；原始至step9冻结、43资产确定性repack/compileall/语法/diff通过。
- 浏览器110唯一（60 QTTS＋50工作台）×3＝330 PASS（10.4分钟），完整step10复制专项另3 PASS（10.2秒）；临时项目保持step9，不改正式工作台，不冒充真实训练/物理麦克风验收。
- Torch2.8/cu128、safetensors0.6.2、packaging25仅沙箱CPU测试依赖，不照装Kaggle；runtime probe依然blocked/退出2，CUDA/qwen/模型与真实推理缺失，无模型加载或Qwen训练。
- 初版夹具manifest返回顺序/缺packaging与扩展夹具kwargs错误保留日志；最终三轮全过。清单22/300是目标验收，不是开发进度，9×50建议也不等于450修复。

## 下一步推荐与不可跳过门禁

下一步直接围绕Kaggle真实首步训练的错误/显存、adapter新进程重载试听与接入现有推理/聊天；不要再排收据/预约工具作为新的前置，不要只添假按钮。需要新专业问题时仍先写具体计划与50建议，不向用户重复提问。已有训练CLI在目标条件就绪后可以现在尝试，不必等另一阶段。
按TARGET_ACCEPTANCE在真实目标设备记录旧进程终止前后nvidia-smi及CUDA空闲/保留显存、合作锁、可信模型真实encode/decode/完整覆盖/内存/时间，验证取消/异常恢复。锁空闲不能代替显存空闲；缺设备/权重/外网就如实blocked，不虚构。

这些训练机制已有代码与CPU证据，仍须在真实Qwen验证文本tokenizer、NCCL world_size=2、两rank数据/梯度/optimizer/loss、显存、adapter与新进程重载试听。不能只加accelerate launch，不能照搬T4不支持的BF16/标准FA2/全参数AdamW；LoRA/FSDP/ZeRO须实际接口/内存证据。DeepSeek、物理录音/真实容器、冷热可听首声/标准RTF/音色保留集分别验收，首PCM不是可听首声，rtf_x是RTF倒数。

## 安全复现与服务

```bash
npm ci
python3 -m venv .venv
.venv/bin/python -m pip install -r kaggle/requirements-training-test.txt  # 沙箱可选张量测试，不替换Kaggle CUDA
.venv/bin/python kaggle/repack.py --check
.venv/bin/python -m unittest discover -s kaggle/tests -v
.venv/bin/go -C kaggle/source/go/gateway test -race -count=3 ./...
npm test
npm run test:e2e -- --repeat-each=3
npm run test:e2e -- tests/browser/studio.spec.js --grep '第十阶段训练器完整Python包' --repeat-each=3
.venv/bin/python kaggle/tests/ownership_process_check.py
.venv/bin/python kaggle/tests/training_gateway_check.py
.venv/bin/python kaggle/tests/codes_cli_check.py
.venv/bin/python kaggle/tests/mock_pipeline.py
.venv/bin/python kaggle/tests/trainer_tensor_check.py --output docs/validation/step10/gloo3.json
```

Go来自CPU requirements的go-bin，这些依赖不是GPU锁文件。所有权进程测试在现有真实holder busy时拒绝启动，不能扰动真实应用。仅解包：QTTS_UNPACK_ONLY=1 QTTS_ROOT=/tmp/qtts-step10-inspect python3 kaggle/kaggle-fixed-step10.py，不安装/下载/启动服务；真实启动仍须审查依赖及模型，QTTS_TUNNEL=none可禁用隧道，真实验收禁止UNPACK_ONLY/Mock替代。

Node工作台3000不同于Kaggle网关，浏览器3100只用临时项目，绝不重置正式workspace。本轮恢复的Node过程仅工作台，不是GPU部署；无应用认证，不能当公网多租户平台。Kaggle单用户Bearer与DeepSeek Key分离，同源可信HTTPS。密钥、私人音频/转写不得进截图/共享日志/Git。

---

## 内嵌备忘录：KAGGLE_PLAN.md

# Kaggle 双 T4 / Qwen3-TTS 语音克隆聊天：实施方案与阻塞说明

## 0. 当前状态，不得略过

**2026-10-21 更新：源码已收到，缺失源码阻塞已解除。** `workspace/HEAD.json` 指向的已保存文件包含原始 `kaggle`，127241字节、SHA256 `26c31621d6265bc25370bc284f2afdcf52f5edaf97e64056c2d8d5eda4a6c461`。通过AST/literal_eval静态解析、Base64/zlib解码及22项内嵌哈希验证，落盘到 `kaggle/source/`，没有运行原安装器。原文件未覆盖。

已完成首批可靠性、第二阶段访问控制/资源预算，第三阶段完成后，现已直接实现第十阶段Base1.7B FP16 LoRA联合loss/双rank DDP/真实优化器与adapter保存核心；真实Qwen/GPU执行仍blocked，最新部分修复包 `kaggle/kaggle-fixed-step17.py`，当前范围及未完成项见KAGGLE_STEP17_AUDIT.md；训练后推理/聊天接入见 [KAGGLE_STEP11_AUDIT.md](KAGGLE_STEP11_AUDIT.md)，已有训练核心证据见 [KAGGLE_STEP10_AUDIT.md](KAGGLE_STEP10_AUDIT.md)，第九阶段历史见 [KAGGLE_STEP9_AUDIT.md](KAGGLE_STEP9_AUDIT.md)，第八阶段历史见 [KAGGLE_STEP8_AUDIT.md](KAGGLE_STEP8_AUDIT.md)，第七阶段历史见 [KAGGLE_STEP7_AUDIT.md](KAGGLE_STEP7_AUDIT.md)，第六阶段历史见 [KAGGLE_STEP6_AUDIT.md](KAGGLE_STEP6_AUDIT.md)，第五阶段历史见 [KAGGLE_STEP5_AUDIT.md](KAGGLE_STEP5_AUDIT.md)，第四阶段历史见 [KAGGLE_STEP4_AUDIT.md](KAGGLE_STEP4_AUDIT.md)；第三阶段见 [KAGGLE_STEP3_AUDIT.md](KAGGLE_STEP3_AUDIT.md)，前阶段见 [KAGGLE_SECURITY_AUDIT.md](KAGGLE_SECURITY_AUDIT.md)。step1与step2历史包冻结保留。证据、具体范围、测试命令及后续风险见 [KAGGLE_SOURCE_AUDIT.md](KAGGLE_SOURCE_AUDIT.md)。这不是完整双T4成品，也不是三轮300项已经验收。

当前虽装Torch作CPU张量测试，仍没有真实GPU、Qwen权重、参考录音或DeepSeek凭据，出站网络也不支持模型托管站或DeepSeek。因此真实模型、双卡训练、音质、首声和RTF验收仍阻塞。本轮没有以Mock测试冒充这些验收。

## 1. 用户目标（保持原意）

- 在 Kaggle 双 T4 上使用 Qwen3-TTS 1.7B，正常推理期间两卡各一个模型实例。
- 简洁网站只设两个主要视图：“录制参考语音”和“语音对话”。主要操作不用滚动页面。
- 先建立自定义名称的语音库，再上传或录制多段参考音频，显示真实采集波形。
- 用户可以选定样本执行真正训练；两卡共同参与同一训练作业，报告全部有效样本的参与情况。
- 训练后克隆聊天，支持情感与音色保持；用户提出99.5%相似度目标，不能转换成无定义的保证。
- 先配置 DeepSeek，再聊天；支持长输出、流式首句优先、切换声音、文字和语音输入。
- 用户提出首声3秒、RTF≤0.5、播放无系统性断音和输入打断目标，需要实测。
- 浏览器工作台应复制最终 Kaggle 代码，不能复制网页HTML冒充Python启动代码。
- 保持此前文件命名、保存、浏览器预览等功能可用；保存真实源码；三轮检查及备忘录需要可追溯。

## 2. 官方资料核查结论

本轮从 GitHub 核对了以下官方文件，Qwen 仓库参考提交为 `022e286b98fbec7e1e916cb940cdf532cd9f488e`：

1. [Qwen README](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/README.md)
2. [单说话人微调说明](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/README.md)
3. [官方训练脚本](https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/sft_12hz.py)
4. [FlashAttention 硬件支持说明](https://github.com/Dao-AILab/flash-attention#nvidia-cuda-support)

已核实：

- 克隆参考音频应从 `Qwen/Qwen3-TTS-12Hz-1.7B-Base` 路线验证，不能把预置音色的 CustomVoice 当成任意声音克隆接口。
- 官方提供 `create_voice_clone_prompt` 和 `generate_voice_clone`，前者可复用参考特征，**不等于微调**。
- 官方微调说明是单说话人流程：JSONL 包含 `audio`、`text`、`ref_audio`，先提取声学码，再训练、保存检查点。不同人物不能无区分混入单说话人库。
- 官方示例训练含 BF16、FlashAttention 2、全参数 AdamW；不能原样当作 T4 双卡脚本。
- 标准 FlashAttention 2 CUDA 路线支持 Ampere/Ada/Hopper；文档为 Turing 指向另外的实现。不能默认 `pip install flash-attn` 后 T4 就具备同等内核。建议从 FP16 + 经探测的 SDPA/eager 开始，不静默换小模型。
- 官方训练脚本使用 Accelerate，但还包含包装后模型属性访问和检查点处理等需要多进程专项核对的代码。不能只加 `--num_processes 2` 就声称正确双卡训练。
- 官方公开 Python 示例返回完整波形。模型架构支持流式不等于现有包装器已提供可直接消费的声学流。必须先做兼容性试验，确认 T4 上实际流式后端。

官方总体延迟宣传、其他GPU成绩、整段分句合成成绩，均不作为本项目双 T4 达标证据。

## 3. 推荐架构（已结合原源码修正，训练部分待实现）

```text
HTTPS 浏览器：参考语音视图 / 语音对话视图
    │ 同源鉴权 HTTP + WebSocket
Go 网关/调度（已有）+ Python 分析与训练编排（后者待实现）
    ├── SQLite 元数据与版本清单
    ├── 语音库原始文件、转写、处理结果、训练清单
    ├── DeepSeek 流式客户端 → 文本切段 / turn取消
    ├── 统一有界合成队列 / 有序音频汇聚
    ├── Worker A：物理GPU0，模型独立加载
    └── Worker B：物理GPU1，模型独立加载

训练模式：排空/取消推理 → 释放推理模型 → 两卡同作业训练
    → 校验检查点与样本覆盖 → 原子发布语音版本
    → 两卡分别恢复推理并预热 → 网站显示就绪
```

源码已有Go网关/调度及Rust可选音频库，优先保留其有效实现；Python承担模型、ASR与拟新增训练编排；原生 TypeScript/JavaScript/Web Audio 承担浏览器交互；SQLite 承担元数据。现有 Node 工作台仍负责代码编辑与真实文件保存。只有测量显示CPU密集型瓶颈且已有可靠实现时，才考虑 Rust/C++，不为了语言数量引入额外编译链。

每个推理 worker 用独立 `spawn` 进程；设备映射必须验证物理GPU与逻辑CUDA编号，不能把 `device_map=auto` 模型切分误称为两份独立副本。

### 3.1 模型常驻与“永久”

- 会话运行期间：加载一次、预热一次，不在每轮聊天重新加载。
- Kaggle 会话结束：进程、显存及公网访问入口都会失效，不承诺永久在线、不做绕过平台限制的保活。
- 可交付的是：版本化资产导出、重新挂载、校验及一键恢复流程。`/kaggle/working` 中的文件必须明确导出或保存成平台支持的持久化资产，不能视为自动永久可靠。
- 如果最终要求真正24小时常驻，部署目标需改为可持续GPU服务器；不能偷偷将这项要求标成Kaggle已实现。

### 3.2 训练路线与诚实的降险

先测 Base 克隆基线，参考特征缓存功能明确标为“准备克隆”，不叫训练。

真正微调必须有：选定样本快照、准确转写、声学码、训练参数、两个rank的梯度同步、样本覆盖、检查点与重新加载试听。

DDP 并不会把两张卡的显存合成一个32GB模型空间。标准全参数混合精度 AdamW 的参数、梯度、主权重和动量状态常见估算约16字节/参数：1.7B约27.2GB（十进制），还没算激活。具体取决于实现，**因此不能不测就承诺每张16GB T4可运行官方全参数配置**。

推荐先验证兼容的 LoRA / 参数高效训练方案，确定目标层、可训练参数、FP16缩放、梯度checkpoint和有效batch；未通过真实模型的梯度及恢复测试前不得提供“已支持”结论。若需要 ZeRO/CPU offload，需额外验证Kaggle CPU RAM、吞吐与检查点；不默认引入。

训练期间两卡归训练进程独占，网站明确进入训练维护状态。若用户要求训练和双副本聊天绝不间断，必须重新做资源预算，当前方案不伪装支持这种并发承诺。

“不管多少音频”解释为可持续增加库、分批上传、分页选择及任务化处理，不解释成无限磁盘、无限显存或无上限单次训练。

## 4. 两个主要界面

### 参考语音

固定顶部两个视图切换入口；主体采用分区卡片，列表和日志分页，不依赖页面滚轮才能操作。

- 语音库名称输入、创建和选择。
- 上传音频、开始录音、停止录音、录音时长、权限状态。
- 波形由真实 AnalyserNode 数据驱动；静音时仍显示明确“录音中”，不能只靠随机动画。
- MIME探测、音频解码、采样率/声道正规化、静音和削波检查。
- 参考转写编辑；选中音频、数量、总时长与质量问题。
- “准备克隆”和“训练”分别显示，训练支持取消、真实进度、双卡状态与样本覆盖报告。
- 浏览器麦克风依赖HTTPS、权限与嵌入策略；失败时上传功能仍可用。停止后关闭所有tracks。

### 语音对话

- 服务端保存API配置；前端只显示“已配置/未配置”，密钥不回显、不存localStorage、不写交付代码。
- DeepSeek模型、可用输出预算和超时按真实供应商接口验证，不硬写不确定的长输出上限。
- 文字输入、开始/停止语音输入、发送/打断；ASR后端单独验证，不只依赖不可移植的Web Speech API。
- 声音选择绑定库与检查点版本；选择新声音时推荐取消当前轮并在下一轮使用，避免一条话中途混入不同音色。
- 聊天内容与历史分页显示；状态和错误可见；不使用“没有滚动条”掩盖被裁掉的输入控件。

## 5. 低延迟、连续播放与打断

1. 用户点击开始时解锁同一 AudioContext；自动播放被拒要有明确入口，浏览器权限规则不能靠保证绕过。
2. DeepSeek增量文本经过切句器；首个短段尽快提交，后续按长度/标点/等待时间控制，保留未消费尾部，处理finish_reason。
3. 真正流式TTS能力先用技术试验确认；若只能整句生成，UI与报告必须写清楚，不冒充声学token流式。
4. 两worker只负责并行生产；所有段含 turn_id、segment_id、chunk_id、voice_revision，汇聚后按序输出。
5. 音频统一采样率/声道，使用有界PCM环形缓冲或连续样本时钟调度；不使用多个audio元素收到即play。
6. 用适量预缓冲应对网络抖动，并统计欠载。预缓冲过长会损害首声，必须实测平衡。短淡化只能消除爆音，不能补丢失内容。
7. 打断同时停止浏览器排程节点、清空环形缓冲、取消DeepSeek读取、使旧GPU任务停止或作废；旧turn迟到包一律拒收。
8. 如果当前后端不能中断CUDA生成，单纯关闭WebSocket不算真正取消；需记录释放延迟，不能让旧长生成阻塞新首声。

## 6. 验收定义

| 用户目标 | 实际验收方式 | 当前状态 |
|---|---|---|
| 两卡各一个模型 | 两个物理设备独立PID/显存/探针合成记录 | 未实测，缺GPU/模型 |
| 两卡共同训练 | world_size=2、rank日志、梯度同步、样本覆盖和重载试听 | 未实现/未实测 |
| 训练完整 | 选定/有效/排除/已见样本逐项清单；不是只看loss | 未实测 |
| 99.5%相似度 | 先定义评估模型、保留集、cosine等指标和盲听；不等同概率 | 不作百分比保证 |
| 首声≤3秒 | 从用户提交至实际可听首样本，分冷/热，报告P50/P95与失败率 | 未实测 |
| RTF≤0.5 | 生成耗时/音频时长；纯TTS与端到端分别记录 | 未实测 |
| 连续播放 | 长回答PCM缓冲欠载、丢包、系统断音次数；区分自然停顿 | 未实测 |
| 可打断 | 从用户输入/按钮至静音及旧GPU任务停止的分别测量 | 未实测 |
| 自适应无页面滚动 | 固定常见视口下关键控件可见、列表分页 | 待TTS网站实现 |
| 可复制Kaggle源码 | 复制实际所选文件原文、权限拒绝兜底、不修改磁盘 | 本轮已实现，另有浏览器测试 |

首次真实设备评估只在指标达标时标为通过；不达标时分析瓶颈、报告实际成绩，并明确调整硬件/后端/目标的取舍，不静默缩小模型或跳过音频。

## 7. 小步执行门禁

- G0：已拿到并保留原始kaggle，确认Python封装格式及22项资产，完成首批可复现缺陷修复。原用户实机报错日志仍未提供。
- G1：两个GPU独立加载、FP16兼容与真实克隆最小实验，测显存/延迟。
- G2：克隆准备、音频库、上传录音、转写、恢复；完成样本资产闭环。
- G3：双rank训练最小步、全部样本覆盖、检查点重载；不得先做假训练按钮。
- G4：文本聊天→DeepSeek真实流→单卡声学输出→浏览器连续播放；先贯通再双卡优化。
- G5：双卡顺序汇聚、长输出、声音切换与打断，测TTFA/RTF/欠载。
- G6：三遍完整端到端：正常、异常打断、长文本重启。每遍均有真实录音/模型/供应商与浏览器证据。
- G7：固定依赖、Notebook导出、启动代码复制、无秘密交付与可回滚发布。

首批源码报告及导出见 `KAGGLE_SOURCE_AUDIT.md`；三轮各100项见 `KAGGLE_REVIEW_CHECKLIST.md`；逐项标注已核对、已修复、不适用或阻塞。不能为了满足数量修改正常代码。专业自问自答见 `KAGGLE_DECISIONS.md`，每题后50条建议；答案为明确的推荐暂定方案，不是假装已完全知道缺失源码的细节。

## 8. 收到源码后的交付形式

优先保留其可用逻辑，按模块分离依赖安装、配置、数据、训练、推理、API和前端。最终交付可粘贴的Kaggle代码单元或经验证的Python启动脚本，并附依赖版本、模型revision、运行顺序、持久化导出步骤、真实测试报告。

如果上传的是Notebook，需解析代码单元并处理魔法命令和执行顺序，不能把Notebook JSON或未经处理的拼接字符串说成可直接运行。工作台“复制当前代码”目前是准确复制原文工具，不会自动转译Notebook，也不声明某个文件已经Kaggle验证。

## 9. 本轮实际完成与验证结果

- 已实现顶部“复制当前代码”：复制当前文件完整原文，包括未保存输入；空文件给出提示；剪贴板拒绝时显示只读且全选的原文，保留手动复制入口。没有自动执行Python或伪造Kaggle代码。
- `npm run check`：通过。`npm test`：30/30服务端及文件系统测试通过。
- `npm run test:e2e`：40/40浏览器测试通过，包含之前35项回归与新增5项复制场景。
- `npm run test:e2e -- --grep 复制当前代码 --repeat-each=3`：完整新增复制场景重复3遍，15/15通过。
- 实际视口390、768、900、960、1024、1280、1440px检查无页面横向溢出。
- 机器校验清单为每轮100项、共300项，决策后建议共150项，完整提示词内嵌全部备忘录。
- 以上均为代码工作台及文档验证。**未运行真实Qwen推理、双T4训练、ASR或DeepSeek调用，不能作为这些系统验收通过的证据。**


## 10. 第一阶段源码验证结果（历史保留，2026-10-21）

- Python 18/18；Go 14个顶层测试（含表驱动场景），竞态检测重复3次通过。
- 全部浏览器47/47（原工作台40项＋QTTS6项＋实际启动代码复制1项）；QTTS六项重复3次为18/18。
- CPU双Mock worker配合真实Go网关三轮通过，涵盖有序帧、文本完整、中断恢复和模拟水位，不是GPU实验。
- 重打包原22项完整性＋新23项资产、确定性生成和仅解包逐字节对比均通过；测试日志在 `docs/validation/`。
- 原三标签页仍保留，真实训练/两个主视图/波形UI未实现，公网认证和依赖锁定尚未完成。


## 11. 第二阶段已完成：单用户访问控制与资源预算（历史结果）

- Kaggle网关所有API统一Bearer认证，缺配置不启动；浏览器解锁/锁定、同源凭据、输入/视图清理、请求和录音取消已加入。
- 自动生成口令默认位于/tmp的0700认证目录、0600文件，不进入声音库/Notebook工作目录导出；可优先配置QTTS_ACCESS_TOKEN Secret。
- 请求体、上传文件/时长、历史、语音与昂贵操作并发、令牌桶、后台构建和记录容量均有应用层预算；不是OS级配额/多租户平台。
- Python41/41、Go24个顶层测试开启竞态检测重复3遍、完整浏览器51/51、QTTS专项27/27、受认证Mock管线三轮通过，详见KAGGLE_SECURITY_AUDIT.md与docs/validation/step2/。
- 本阶段当时原始kaggle和step1包均未改；step2共27项资产，清单source_manifest_step2.json。真实GPU依赖/后端探针、两主视图/波形UI与真正训练仍需后续实施。


## 12. 第三阶段：兼容探针与原生录音生命周期

- 计划先落盘KAGGLE_STEP3_PLAN.md，再实施；只新增独立step3包（30资产），历史包哈希不变。
- 元数据/设备/接口形状探针不安装、不下载、不加载模型。安装依赖后、模型下载前运行，阻断时保存报告；API只有受认证GET读取，不提供远程执行。
- 实测getUserMedia→AnalyserNode波形、RMS/峰值与MediaRecorder编码，不连接扬声器。录音可本地移除，不自动上传，失败保留片段。
- 处理未决权限、锁定、迟到事件、设备结束、页面离开与封装超时，加入字节/文件数/块数/时长预算。仍保留三标签页，不把参考缓存叫训练。
- 当前Python56项×3、Go26顶层/16子测试race×3、Node API30项、真实Go+双CPU Mock三轮均通过；完整浏览器66项×3轮=198次通过；详情见KAGGLE_STEP3_AUDIT.md。
- 300项清单仅15项有据勾选；真实GPU/物理麦克风/模型/DeepSeek/质量与性能未验收，不能由软件信号或Mock替代。


## 13. 第四阶段：两主视图与视口布局

- 先保存KAGGLE_STEP4_PLAN.md，再改为录制参考语音/语音对话两主视图；监控为原生辅助诊断窗口，保留所有既有DOM ID与脚本顺序。
- 桌面双栏、手机分区、主操作固定、长文本/档案/选项独立滚动。所列五个标准CSS视口内测试完整控件与祖先裁切；≤640px高允许页面滚动而不是丢失操作。
- 关闭/Escape/焦点恢复/锁定、隐藏面板、键盘导航、顺序轮询与过期报告均覆盖；切换视图/诊断停止采集并保留有效片段，转录页停止播放。
- 自命名1–64Unicode字符，不再回退my-voice；参考文本/校准有常驻“选项”入口。中文布局测试加载仓库现有本地Noto字体，生产不增加外链字体。
- Python59项×3、Go26顶层/16子测试race×3、API30、双Mock管线三轮通过；全量浏览器87项×3轮=261次最终通过，初次失败/中止记录保留，见KAGGLE_STEP4_AUDIT.md。
- 保留原始/step1/2/3，独立step4为30资产；工作台保留所有旧文件，不为重复交接文件放宽1MiB限制。完整交接留仓库，工作台只添能容纳的源码与简报。
- 下一步目标环境验收门禁见KAGGLE_TARGET_ACCEPTANCE.md：非Mock证明、每卡真实推理、容器/DeepSeek/指标与真正双rank训练分别验收，当前均未取得通过证据。

第四阶段最终只勾选18/300项；历史150条建议仍保留。真实双T4/模型/训练/DeepSeek/物理麦克风/音质/首声/RTF未验收。


## 14. 第五阶段：先命名空库、再添加/选择原始参考

- 计划KAGGLE_STEP5_PLAN.md先保存，再增量实现独立STATE/libraries；不把空库/原始音频误当可推理profile。旧一步创建档案与两个主要视图不变。
- UUID/命名分离、SHA256去重与核对、修订CAS、原子清单/写失败回滚、库/文件/总字节预算、0700/0600、链接拒绝。仅本地会话存储，原始样本不自动导出Dataset；处理后档案锚点/转写保留已有备份语义。
- flock租约覆盖参考处理，线程启动/取消/进程死亡不遗留永久busy。原始字节快照固定所选样本；复用既有构建，不是训练。结果提交后才公开终态，失败不删除源样本或上次独立档案。
- 发现并修复线程池提交失败但排队项稍后仍可能执行的边界，真实ThreadPoolExecutor回归；原始/step1/2/3/4冻结，step5独立32资产/196140字节，SHA256 acfa5639324e16aa7dcfe314caef09bee8eb277d59bdd71a5f1f4cffa0a7aaf1。
- Python92×3、Go28顶层/16子测试race×3、Node API30×3、真实Go→analyst原始库HTTP与双CPU Mock各三轮通过；浏览器100唯一×3=300通过/11.2分钟，最终包复制另3次通过；新流程初检12通过。
- 正式工作台保持15文件1043155字节/既有HEAD，剩5421字节不足新包；不提高1MiB、不删除历史，本阶段独立文件交付，复制只在隔离临时工作区验证。
- 仅增R1-073，当前19/300；第4题50建议与历史150建议保留。真实双T4/模型/DeepSeek/物理麦克风/真实训练及质量与性能仍未验收。


## 15. 第六阶段：训练输入，不冒充训练执行

计划KAGGLE_STEP6_PLAN.md与专业问题5的50项建议先落盘，再增量实现TrainingDataStore。逐条转写、统一参考、权利/单说话人声明，固定来源库修订与原始ID/SHA256；只读同库租约不改参考处理状态。独立私有目录、完整24kHz mono PCM16 WAV、规范化容器保留全部PCM帧、JSONL/manifest/数学双rank计划、原子发布/失败回滚、分层预算与固定哈希校验。

界面仅增辅助库窗口的折叠区，仍两主视图。库/所选集合改变必须重新声明；初版程序化建库可能沿用旧勾选的问题复审修正，旧全量105次后中止不计三轮完成。新版106唯一用例×3＝318通过（10.6分钟），详见阶段报告。

step6独立33资产/210003字节，SHA256 781eca6e2e34bdacbe2f5337bd6535512226c2122bbf3876d05634f2fc86d256；step1–5冻结。Python112×3、Go28顶层/16子测试race×3、Node30×3、真实Go/analyst合成WAV输入三轮与两CPU Mock管线三轮通过；浏览器106×3＝318通过（10.6分钟），包含第六阶段完整源码剪贴板三次一致性验证。原始/训练输入不自动Dataset备份，副本要单独删除。

仅新增R1-079与R2-031，累计21/300；专业问题共5×50＝250条建议。没有audio_codes/训练器/optimizer/梯度/检查点/实际两rank、GPU训练与推理互斥或任何真实模型/双T4/DeepSeek/性能/物理录音验收。格式暂不接收浏览器Opus作为训练输入，不篡改后缀冒充WAV。


## 16. 第七阶段：离线声学码入口与真实编码门禁

先保存STEP7计划及Q6的50行动建议，再实现py/training_codes.py与tools/encode_training.py。只允许本机CPU/FP32/eager/两线程/单样本与本地固定hash JSON/safetensors模型，未接GPU或HTTP任务，不抢占两推理实例。真实适配调用Qwen3TTSTokenizer.encode全波形，严格核对一个返回、ceil(frames/1920)×16和0..2047整数，不用zip丢样本。模型目录前后指纹、输入固定manifest租约、完整WAV/text/ref_audio/rank计划副本，原子发布/回滚/预算和独立校验/删除。

取消/超时停止进程组；复审补Linux PDEATHSIG/ppid握手覆盖控制器被强杀。初版浏览器75次后中止保留，不计最终三轮。测试fixture输出强制test_only_codes/tokenization_executed=false；当前Torch/qwen_tts/权重均无，真实编码未运行，tokenization_verified/训练/两rank/推理均false。码副本不自动Dataset备份；未来训练读取租约仍需接入。

step7独立35资产/222808字节，SHA256 3fe57769560c076d6d288a87cae6150b0a9404597eb0ea3997ab26de596f4cd0，原始与step1–6冻结。最终Python146×3、Go race×3、Node30×3、真实Go/analyst HTTP租约与本机CLI/fixture链路三轮、CPU Mock管线三轮通过；浏览器107唯一×3＝321通过（11.5分钟），最终完整包复制另3次通过。正式工作台15文件1043155字节及HEAD不变，不提高1MiB限制或删历史，独立文件交付。

三轮审查清单仍21/300；专业问题6×50＝300建议，不等于300项修复。下一步GPU资源所有权/推理与离线任务互斥和目标设备真实编码/解码/内存/时间门禁，之后才文本tokenizer及真正两rank优化器/检查点。


## 17. 第八阶段：整组GPU资源准入，不是自动训练模式

先保存STEP8计划及Q7的50行动建议，再实现py/gpu_ownership.py、tools/resource_control.py。固定同机同UID整组flock，不随STATE或CUDA别名变化；supervisor先独占，再通过pass_fds只让worker/analyst采用同一OFD，gateway不继承。close不LOCK_UN，父关闭/死亡但活孩子仍持锁，最后引用退出才释放；诊断PID/时间记录非权威，不能TTL抢占。真实模型入口在加载前受控；独立模型进程独占整组，多worker应由supervisor统一启动，Mock/CPU编码不宣称GPU所有权。

补日志FD关闭、kill等待与后代清理、早期信号处理和停止期间禁止重启。bootstrap不再按PID/pkill自动杀旧服务，busy/遗留运行时PID标记阻断；ready检查本次supervisor存活，避免读旧健康误报。没有自动模式切换/排空/显存回收、GPU编码或训练；旧版本升级前必须先人工确认停止，不能删锁文件强行恢复。

step8独立37资产/230559字节，SHA256 777c1d523559c9c734cd5e99841810524284e91269ced23963e8e5ab3f3cc1e1，原始至step7冻结。Python179×3、Go race×3、Node30×3、真实supervisor/FD/CPU替身生命周期三轮、真实HTTP/本机CLI与CPU Mock管线三轮通过；浏览器108唯一×3＝324通过（10.5分钟），完整复制专项见阶段报告。正式工作台仍15文件1043155字节/HEAD不变，不放宽1MiB，不删历史，独立文件交付。

仅新增R2-010的合作式锁设计/协议证据，累计22/300，7×50＝350条建议；并非GPU/显存/两rank验收。下一步码版本完整来源/授权封存与训练读取租约、受控离线任务及目标硬件真实编码/解码/显存门禁，再到实际优化器与检查点。


## 18. 第九阶段：完整来源封存与固定码版本读取租约

先保存STEP9计划与Q8的50行动建议，再增量实现。新schema2把输入manifest及原始JSONL完整字节封存，固定原输入SHA256，逐项交叉核对音频/文本/统一参考/样本顺序及分配计划；原库/修订/原件hash/用户声明均保留。source纳入权限/链接拒绝/预算/原子回滚。来源声明不是法律/身份鉴定。

schema1历史码仍可列表、核验、读取和删除，明确legacy-unsealed，不补写授权、不改变旧hash。list只描述封存政策，不声称当前完整性；完整核验才返回provenance_verified_now。读取租约先固定码manifest并完整核对，然后释放全局锁；目录外.use-ID独占，读期同版本删除或第二读取409，其他版本可操作。异常/进程死亡由FD关闭回收，fork继承引用未关闭前仍busy。

本机hold-read只保持1..3600秒检查，不执行命令/GPU/训练，沿用超时/取消/PDEATHSIG，收据training_allowed=false。协作式约定只读，不是OS只读挂载；未来训练器仍须管理所有读者生命周期并另验真实编码、语义、硬件与训练门禁，未自动实现DDP多rank接管。

独立step9为233074字节/37资产，SHA256 8ec892dcc5ca10daf20c8de84dd2be08d9a3de8807872c2051ddf52bd5882a9b；原始至step8冻结。Python201×3＝603、API30×3、Go race三轮、真实HTTP/CLI/资源FD与CPU Mock各三轮通过；浏览器109唯一×3＝327通过（10.3分钟），最终复制专项另3次通过。当前8×50＝400建议，清单仍22/300，不把建议或测试次数当真实硬件完成。下一步受控离线作业的收据/生命周期门禁与目标T4真实编码/解码测量，再考虑训练器与检查点；缺依赖不伪造任务完成。


## 19. 第十阶段：不再延后核心，实际训练器已开发

回应用户“还有多久才能真正开始开发”：现在直接开发，不再用来源/预约/收据阶段替代训练功能。保存STEP10计划与Q9的50建议后实现lora_adapter/tts_dataset/tts_training/training_job/train_tts，附上游Apache许可证。目标路径FP16/eager/microbatch1/FP32 LoRA和AdamW；所有loss调用在DDP.forward内，文本过projection，真正backward/梯度同步/累积/有限值与参数改变检查、adapter原子保存。父/两rank共享GPU和码FD，取消/超时/父死保护；不自动停推理或部署模型。

新增25项训练核心/准入/张量/真实进程测试及step9冻结回归，全Python227×3＝681 PASS；另CPU小网络真实两进程Gloo三轮，参数真实改变且rank最终摘要相同。不是Qwen、CUDA/NCCL或T4训练证据。Node30×3、Go race三轮、HTTP/CLI/资源FD/CPU Mock各三轮PASS。浏览器110唯一×3＝330 PASS（10.4分钟），完整复制专项另3 PASS。

step10独立261429字节/43资产，SHA256 2bddd6ebad371268f9b3b02315fc29cae588da6c46c7d134476945b50b8a5ac4；原始至step9冻结，正式15文件/HEAD/1MiB不变。当前Torch2.8/cu128仅CPU测试，沙箱无CUDA/权重/Qwen包；不把它当Kaggle依赖锁。

真实开训不需再等一个开发阶段：在双T4及可信模型/授权数据就绪后可以尝试本CLI。耗时、显存和成功日期没有实测，不能保证。下一核心是现场真实首步故障处理、adapter新进程重载试听及接入现有推理/聊天，而非继续工具化前置。训练恢复状态/完整CustomVoice/网页自动训练及质量性能仍未完成。详见KAGGLE_TRAINING_QUICKSTART.md。9题450建议，22/300是目标验收状态，不是代码开发进度百分比。


## 20. 第十一阶段：直接接入训练后的推理与聊天

先落盘STEP11计划与Q10（50建议），选择官方原生adapter后端，诚实标注句级缓冲。默认faster不改，明确选择而不是猜CUDA graph支持LoRA。完成run/pin/双rank更新与tensor摘要、统一参考WAV及转写发布；profile不自动active、质量/重载验收false。每GPU一份可信本地Base，全部LoRA预构造再锁内切换，保存speaker直接构造x-vector-only prompt。损坏/缺依赖/错Base/普通与训练模式混用一律拒绝，不输出Base/Mock冒充训练声音。

现有Worker帧→Go调度/SSE→网页声音选择/聊天已接入；原生是完整一段才返回wave，输出一次而不是切假chunk。取消按AR步合作检查并丢迟到PCM；180秒保护预算不是时延承诺。两主视图、旧参考处理/录音/命名库/原始输入与码/认证/DeepSeek文字流/打断/复制保留。修复一致性检测全失败仍可能判consistent=true的问题。训练候选参考只读，编辑/校准409。

真实本机Go+SSE+双worker+CPU tiny LoRA原生API替身执行3轮A→B→A；损坏版本503、active保留且无PCM回退。真实Qwen/T4训练、新进程重载试听、峰值显存、性能及DeepSeek外部服务未验收。独立step11：276043字节46资产，SHA256 cd5346e8ae34f1e2db327a076a7411996982848f9d4e14236f05d94c626d496e。原始至step10冻结，正式工作台满额15文件/HEAD不改；10题500建议不等于300项完成。直接目标操作见KAGGLE_ADAPTER_QUICKSTART.md，下一步是实际首步与重载/试听，不再加准备工具。


## 21. 第十二阶段：实机Mimi/RoPE故障修复与健康模型会话驻留

用户实际检测到两Tesla T4，Python3.12.13/Torch2.10.0+cu128/faster0.5.4/TF5.20.2；两worker在MimiConfig.rope_theta加载失败。保存STEP12计划与Q11的50建议后审查实际PyPI wheel，发现Qwen-HF旧默认函数与现代Mimi字段不一致；没有采用违反faster依赖的单独降4.x。

新增qwen_compat.py，仅对已识别Qwen默认函数做现代theta真实读取/临时副本桥接，配置/权重不动；接入实际模型各入口和预检CPU数学smoke。实际TF类+Qwen wheel原函数CPU复现同一个错误，三种theta及原配置不变三进程通过，不等于完整Qwen/T4成功。固定三个直接依赖，安装用当前Torch/音视频版本约束保护CUDA栈。

fatal worker停止重试，启动nonce失败收据避免健康端口消失后继续等待；失败/中断清理自己创建的supervisor，不盲杀旧PID。默认QTTS_RESIDENT=1，不再按600次/旧显存阈值周期回收；每worker独立单GPU仍保留，健康模型会话内驻留。Kaggle平台会话/配额/硬件回收不能保证永久。

当前step12独立282031字节47资产SHA256 2be33a3a6735639ce32ec8750e9a489abd96e4daa780d068557f2b0156f2de08；原始至step11冻结。浏览器复制页已换step12，正式15文件/HEAD不改；11题550建议，完整目标22/300保守不升级。下一步按KAGGLE_STEP12_QUICKSTART.md在完整重启会话后复跑两模型加载/warmup、显存和实际短句试听，不加工具前置。

## 22. 第十三阶段：修复step12未覆盖的实际延迟导入

用户再次实机失败，HF未加载警告不应放行。真实Faster wheel证明Qwen直到from_pretrained才导入，旧sys.modules判断错误跳过补丁。本次发行元数据分支、先验证再显式完整导入、HF smoke强制门禁；实际完整Faster/Qwen+微型Mimi构造/保存/重载三进程，冻结step12真实复现旧错误。原始至12冻结，step13为282346B/47资产，SHA256 dad142d75be94d8efb6567fc1f8755d3f37341a65d5c7fe9454fd36c87770e60。

完整三轮收据见step13/final-checks.json；12题600建议，完整目标22/300不变。实际两T4已识别但完整模型仍未加载成功，不能保证下一次实机必成。下一步直接完整会话重启后复制step13复跑，操作见KAGGLE_STEP13_QUICKSTART.md。

## 23. 第十四阶段：长录音/等价计算优化/原文与无额外呼吸

先三轮各100建议，再三题各50自问自答，完整15题750建议；方案见STEP14_PLAN。实际支持20分钟预算、缓存避免重复tokenize并保持CPU小LoRA参数逐位一致、梯度finite合并读取、HF版本报告、实际会话保留正文与默认无后加呼吸。48资产/285094B，SHA256 73a02a95919406c4570ea563f0c0475fdde17535e6ccd16764c32514fce2c369。

网页训练控制面、长音频逐条审核与维护态/真实训练/取消/恢复/部署闭环仍未完成；没有真实Qwen/T4训练、音质、首声、声学校验验收，不把CPU等价或虚拟录音当真人实验。本阶段整体PARTIAL/BLOCKED，完整目标22/300不升级。三轮结果以step14/final-checks.json为准。


## 24. 第十五阶段：参考隔离与可避免等待

三轮100建议、问题16–18各50建议后实施；累计18题900建议。Faster仅向量、禁参考PCM拼接；聊天首句无须等下一delta；输出-18dBFS/最大增益12dB；默认延后GPU校准，CPU ASR复用、构建内嵌入去重与阶段收据。两T4仍各一模型。冻结原始至14与正式工作台。真实Qwen/T4生成/韵律相似度/速度/创建A/B仍待现场，整体PARTIAL/BLOCKED，完整目标22/300不升级。见STEP15_PLAN/AUDIT/QUICKSTART与validation/step15。


## 25. 第十六阶段：相似度取舍修正、参考版本绑定与真实RTF门禁

三轮100建议/问题19–21各50后增量实施。默认恢复匹配转写ICL，但参考码不进codec；Go会话参考内容pin/模式与稳定seed，Worker锁内重读/校验、提示内存快照与同路径缓存失效。codec左25帧有界，实际causal结构tiny实验后默认前瞻0而非原拟2；每任务重置leveler、目标-18、默认最大增益6。提供实际双worker18条WAV/逐GPU标准及wall RTF门禁。真实相似/沙沙/0.3仍blocked，整体PARTIAL；不以CPU或Mock替代，不默认每T4双模型。原始至15与正式工作台冻结，完整目标22/300不变。


## 26. 第十七阶段：长参考对齐修复

截图15的28.7秒报错由长ASR段无短候选复现。17保留words并验证词文后切分，缺失则对实际短窗口重识别，不比例分全文；16默认/24实验锚点，源录音可长达既有预算，非全数据训练。v2指纹加四生成参数，较长朗读聚合不改聊天早触发，低输入RMS风险提示进现有处理决策。三轮100建议及问题22–24每题50后实施，累计24题1200；保留原始–16和工作台。真实音质/相似/无沙沙/双卡一致/自然度/RTF仍blocked，目标22/300不升级。

---

## 内嵌备忘录：KAGGLE_REVIEW_CHECKLIST.md

# Kaggle 双 T4 语音系统：三轮各100项审查清单

**状态：计划检查项，不是已发现的300个缺陷，也不是已经完成的300项修复。**

源码已收到并静态解包验证；首批历史报告见 `KAGGLE_SOURCE_AUDIT.md`；访问控制/容量证据见 `KAGGLE_SECURITY_AUDIT.md`，录音阶段见 `KAGGLE_STEP3_AUDIT.md`，历史两视图阶段见 `KAGGLE_STEP4_AUDIT.md`，历史命名库阶段见 `KAGGLE_STEP5_AUDIT.md`，不可变训练输入历史见 `KAGGLE_STEP6_AUDIT.md`，离线编码历史见 `KAGGLE_STEP7_AUDIT.md`，资源准入历史见 `KAGGLE_STEP8_AUDIT.md`，来源封存历史见 `KAGGLE_STEP9_AUDIT.md`，已有训练核心见 `KAGGLE_STEP10_AUDIT.md`，显式adapter推理/聊天接入见 `KAGGLE_STEP11_AUDIT.md`，当前Mimi/RoPE现场修复与会话驻留见 `KAGGLE_STEP12_AUDIT.md`。前5项源码交接、5项认证/凭据与5项有原生浏览器录音证据及3项两视图/视口条目与1项库名称/ID隔离、2项授权记录/固定清单及1项合作式资源锁设计已完成（共22项）；其余逐项验收尚未汇总完成，保持未勾选，不等于全部未开展。真实GPU验收仍阻塞，CPU/协议模拟不与GPU验收混同。

## 第一轮：源码与环境审查

- [x] R1-001：定位用户实际上传的kaggle源文件，缺失时停止逐行修复结论。
- [x] R1-002：记录源文件SHA256与文件大小，避免审查错误版本。
- [x] R1-003：识别Python脚本和Notebook格式，不把Notebook JSON直接当Python。
- [x] R1-004：保留用户原文件备份，不用默认示例覆盖。
- [x] R1-005：列出全部本地模块、动态生成文件与启动单元。
- [ ] R1-006：标记原有可用功能并建立回归基线。
- [ ] R1-007：梳理安装、下载、预处理、训练、推理、前端六个入口。
- [ ] R1-008：检查Notebook重复执行是否创建重复服务。
- [ ] R1-009：排查硬编码密码与API密钥，仅记录发现位置不输出秘密。
- [ ] R1-010：为每个真实缺陷记录复现步骤、行号和影响范围。
- [ ] R1-011：检查GPU数量是否实际为2，不能只根据平台选项判断。
- [ ] R1-012：记录每块GPU名称、compute capability与可用显存。
- [ ] R1-013：记录驱动、CUDA、PyTorch与Python版本。
- [ ] R1-014：验证两个worker分别绑定不同物理GPU。
- [ ] R1-015：禁止device_map=auto意外将同一模型切分到双卡。
- [ ] R1-016：避免训练主进程初始化CUDA后再不安全地fork。
- [ ] R1-017：使用spawn进程启动方式并防止Notebook递归启动。
- [ ] R1-018：对每个GPU分别执行独立最小推理。
- [ ] R1-019：区分双GPU吞吐与单段音频延迟，不能直接等同。
- [ ] R1-020：在GPU不可用时返回失败状态而不是模拟模型成功。
- [ ] R1-021：确认克隆模型是Qwen3-TTS-12Hz-1.7B-Base。
- [ ] R1-022：确认Tokenizer版本与模型相匹配。
- [ ] R1-023：固定模型权重revision并记录哈希。
- [ ] R1-024：核对官方Python接口签名，不猜测流式参数。
- [ ] R1-025：确认generate_voice_clone返回形式是否为整段波形。
- [ ] R1-026：确认所选后端确实支持增量声学输出。
- [ ] R1-027：区分Base、CustomVoice与VoiceDesign用途。
- [ ] R1-028：不假定Base支持任意自然语言情感指令。
- [ ] R1-029：核实clone prompt能否跨进程直接复用。
- [ ] R1-030：每块GPU独立构建并校验参考特征缓存。
- [ ] R1-031：T4默认研究FP16而不是直接复制BF16示例。
- [ ] R1-032：对SDPA可用内核做真实设备探测。
- [ ] R1-033：保留eager注意力可诊断回退而非静默换模型。
- [ ] R1-034：不默认安装面向Ampere的标准FlashAttention 2。
- [ ] R1-035：不把第三方Turing内核直接视作官方兼容。
- [ ] R1-036：检查推理算子是否出现CPU回退。
- [ ] R1-037：记录FP16非有限输出与溢出。
- [ ] R1-038：检查采样率、声道与波形类型的返回契约。
- [ ] R1-039：用torch.inference_mode限定推理路径。
- [ ] R1-040：为模型预热单独计时，不计入热启动首声成绩。
- [ ] R1-041：核实全部Python依赖的版本约束。
- [ ] R1-042：新建隔离环境，避免破坏Kaggle内置CUDA依赖。
- [ ] R1-043：不无条件升级torch或卸载平台GPU运行库。
- [ ] R1-044：安装前检查磁盘容量与网络权限。
- [ ] R1-045：下载失败保留可诊断错误并支持续传。
- [ ] R1-046：验证下载文件完整性，不能只检查目录存在。
- [ ] R1-047：对冷启动依赖下载显示阶段进度。
- [ ] R1-048：移除每次聊天重复pip安装与模型加载。
- [ ] R1-049：安装日志不包含密钥或私人音频内容。
- [ ] R1-050：生成可重复执行的依赖锁定清单。
- [ ] R1-051：把会话内驻留与跨会话持久化分开描述。
- [ ] R1-052：不承诺Kaggle会话永久运行。
- [ ] R1-053：记录当前平台配额与会话条件，不能写死永久时长。
- [ ] R1-054：为结束会话前导出语音库设计操作入口。
- [ ] R1-055：明确/kaggle/working不是无条件永久存储。
- [ ] R1-056：对恢复的模型与数据执行校验。
- [ ] R1-057：保存模型版本、适配器版本和语音库清单。
- [ ] R1-058：重启后自动发现有效资产但不自动开始收费请求。
- [ ] R1-059：缺少持久化资产时提示重新挂载而非假恢复。
- [ ] R1-060：不使用规避平台会话限制的保活方案。
- [ ] R1-061：核实官方训练脚本实际优化哪些参数。
- [ ] R1-062：估算全参数AdamW权重、梯度、主副本与状态开销。
- [ ] R1-063：不将两块16GB显存简单相加给DDP每卡使用。
- [ ] R1-064：训练前用最小样本测量峰值显存。
- [ ] R1-065：验证LoRA是否兼容目标层与语音架构。
- [ ] R1-066：通过named_modules确定适配层而不是随意猜名字。
- [ ] R1-067：冻结不训练的参数并统计可训练参数数量。
- [ ] R1-068：检查梯度checkpoint与缓存设置是否冲突。
- [ ] R1-069：检查模型训练包装后的属性访问是否支持DDP。
- [ ] R1-070：对分布式保存与恢复做独立可复现实验。
- [ ] R1-071：建立参考音频上传与实际训练的独立状态机。
- [ ] R1-072：不把create_voice_clone_prompt标注成微调训练。
- [x] R1-073：音频库名称使用内部ID，显示名称与磁盘路径分离。
- [ ] R1-074：上传前必须选定或创建语音库。
- [ ] R1-075：音频条目包含来源、时长、采样率和转写。
- [ ] R1-076：检查所有音频解码工具是否存在。
- [ ] R1-077：按实际格式解码，不能只相信文件后缀。
- [ ] R1-078：拒绝空音频、损坏数据与明显静音。
- [x] R1-079：记录训练授权和声音使用同意。
- [ ] R1-080：不得从多个不同说话人混合出单说话人训练集。
- [ ] R1-081：训练数据每条必须有匹配转写。
- [ ] R1-082：自动转写结果允许人工修正。
- [ ] R1-083：检查语言标签和文本正规化规则。
- [ ] R1-084：保留原始音频，预处理输出单独存储。
- [ ] R1-085：对削波、噪声和过短语音提示质量问题。
- [ ] R1-086：限制单次上传大小与总存储额度。
- [ ] R1-087：明确任意数量输入采用分批任务，不承诺无限资源。
- [ ] R1-088：为重复音频提供哈希去重。
- [ ] R1-089：训练和验证按音频来源拆分，避免片段泄漏。
- [ ] R1-090：记录被过滤音频及原因而不是静默跳过。
- [ ] R1-091：扫描HTTP接口的任意路径读写风险。
- [x] R1-092：检查暴露网站的认证与访问令牌。
- [ ] R1-093：DeepSeek密钥仅放服务端配置与安全环境变量。
- [x] R1-094：不把密钥写入前端localStorage或下载包。
- [ ] R1-095：限制出站API地址，防止任意URL导致SSRF。
- [ ] R1-096：检查异常日志是否泄漏请求头。
- [ ] R1-097：为上传、训练和聊天设置请求容量限制。
- [ ] R1-098：核实浏览器录音需要HTTPS和用户权限。
- [ ] R1-099：对跨站写入与WebSocket Origin进行验证。
- [ ] R1-100：完成首轮后输出证据、待办和阻塞，不编造100个已修缺陷。

## 第二轮：训练、双卡与流式链路

- [ ] R2-001：把推理与训练定义为互斥的GPU资源模式。
- [ ] R2-002：训练前停止接收新推理任务并提示服务状态。
- [ ] R2-003：显式取消或排空旧任务后再释放推理显存。
- [ ] R2-004：训练结束后仅在检查点验证通过时恢复推理。
- [ ] R2-005：恢复时将选定模型分别加载到两块GPU。
- [ ] R2-006：防止同时常驻推理副本和全参数训练造成OOM。
- [ ] R2-007：训练失败保留上一可用模型和语音库。
- [ ] R2-008：资源不足时报告原因，不静默降成0.6B。
- [ ] R2-009：检查模型卸载后实际可回收显存。
- [x] R2-010：设计GPU资源所有权锁与超时恢复。
- [ ] R2-011：使用两个真实rank参与同一个训练作业。
- [ ] R2-012：确认每个rank的设备映射和分布式world_size。
- [ ] R2-013：用分布式采样器划分数据而非重复整套样本。
- [ ] R2-014：每轮调用set_epoch更新采样顺序。
- [ ] R2-015：统计原始样本ID的跨rank覆盖情况。
- [ ] R2-016：不因drop_last让选定样本长期不参与训练。
- [ ] R2-017：不能整除world_size时标明填充或重复样本策略。
- [ ] R2-018：记录每rank步数与梯度同步次数。
- [ ] R2-019：显式同步训练异常，避免另一rank永久挂起。
- [ ] R2-020：验证两卡训练不是并行执行两个独立微调。
- [ ] R2-021：FP16训练启用相应GradScaler与溢出检查。
- [ ] R2-022：只对可训练参数创建优化器状态。
- [ ] R2-023：使用梯度累积降低单卡微批显存。
- [ ] R2-024：记录有效全局batch的实际计算方式。
- [ ] R2-025：验证loss有限并实际发生参数更新。
- [ ] R2-026：记录每轮耗时、已见样本数和学习率。
- [ ] R2-027：避免将loss降低等同音色相似度提升。
- [ ] R2-028：支持用户取消后保存可恢复状态。
- [ ] R2-029：验证取消操作对两个rank同时生效。
- [ ] R2-030：防止训练进程结束后留下占显存子进程。
- [x] R2-031：训练清单固定所选音频ID和内容哈希。
- [ ] R2-032：任务启动后音频编辑不改变运行中的数据集。
- [ ] R2-033：音频编码准备阶段显示真实进度。
- [ ] R2-034：保留原始JSONL、分词版本与声学码版本。
- [ ] R2-035：明确保存优化器、调度器和随机数状态需求。
- [ ] R2-036：所有rank按后端要求参与检查点状态收集。
- [ ] R2-037：只有指定写入进程发布最终清单。
- [ ] R2-038：检查点临时目录校验后再原子切换。
- [ ] R2-039：按训练后端正确处理分片或完整state_dict。
- [ ] R2-040：使用新进程加载检查点完成独立试听。
- [ ] R2-041：为单说话人微调保存说话人ID映射。
- [ ] R2-042：保存适配器与基础权重revision的绑定关系。
- [ ] R2-043：不混淆Base克隆接口与训练后CustomVoice接口。
- [ ] R2-044：对多个语音库采用各自版本，不覆盖全局共享状态。
- [ ] R2-045：推理任务携带不可变的voice_revision。
- [ ] R2-046：检查切换语音时缓存键包含模型版本。
- [ ] R2-047：为旧模型引用计数，避免在途推理使用已卸载权重。
- [ ] R2-048：保留模型切换失败回滚路径。
- [ ] R2-049：对同一语音两块GPU生成的音频做一致性抽样。
- [ ] R2-050：训练完整性报告列出选中、有效、已见和排除样本数量。
- [ ] R2-051：DeepSeek以流式模式读取增量文本。
- [ ] R2-052：API模型名称按供应商实际能力配置。
- [ ] R2-053：分别配置输出预算与上下文预算。
- [ ] R2-054：处理finish_reason=length与长文截断。
- [ ] R2-055：避免在第一句之前等待完整长回答。
- [ ] R2-056：为中文句号、问号、感叹号定义切句规则。
- [ ] R2-057：为无标点长文本提供最大等待时间与长度边界。
- [ ] R2-058：保护代码块、小数、URL和缩写不被错误切断。
- [ ] R2-059：记录切句器尚未消费的尾部文本。
- [ ] R2-060：结束流时刷新最后一个不完整句子。
- [ ] R2-061：为每轮聊天生成turn_id。
- [ ] R2-062：为每段文本生成递增segment_id。
- [ ] R2-063：两个GPU按任务队列工作而不是前端并发无序播放。
- [ ] R2-064：首个短段优先调度至空闲且已预热的worker。
- [ ] R2-065：后续段适度增大，以减少句间重启成本。
- [ ] R2-066：限制预合成队列长度，防止长输出撑爆内存。
- [ ] R2-067：对慢段实施顺序等待，不能跳过内容。
- [ ] R2-068：记录各段音频采样率与长度。
- [ ] R2-069：重采样至统一播放格式后再进入浏览器队列。
- [ ] R2-070：不对尚未实现的token级流式接口作虚假声明。
- [ ] R2-071：用WebSocket或流式HTTP传送明确的音频元数据。
- [ ] R2-072：为每个音频包携带turn、segment、chunk和版本信息。
- [ ] R2-073：音频数据采用确定字节序和波形编码。
- [ ] R2-074：处理传输分片、半包和重复包。
- [ ] R2-075：浏览器按样本时钟而不是收到即play调度。
- [ ] R2-076：使用同一AudioContext播放时钟。
- [ ] R2-077：首次用户操作中显式解锁音频上下文。
- [ ] R2-078：为自动播放被拒提供可见的开始播放入口。
- [ ] R2-079：设计有界预缓冲与可观测欠载计数。
- [ ] R2-080：不靠无限预缓冲掩盖首声延迟不达标。
- [ ] R2-081：使用连续PCM调度或AudioWorklet环形队列。
- [ ] R2-082：每块音频采用相同声道与采样率。
- [ ] R2-083：必要时用短交叉淡化消除拼接爆音。
- [ ] R2-084：不得用交叉淡化掩盖句子丢失或重复。
- [ ] R2-085：保存浏览器已排程的所有音频节点。
- [ ] R2-086：打断时停止节点并清空尚未播放队列。
- [ ] R2-087：发送取消信号至DeepSeek读取任务。
- [ ] R2-088：通过生成停止条件取消GPU任务，而不仅关闭界面。
- [ ] R2-089：旧turn迟到音频一律丢弃。
- [ ] R2-090：新输入不等待旧整段合成完成才进入调度。
- [ ] R2-091：麦克风输入与播放回声处理分开设计。
- [ ] R2-092：用户按住或点击语音输入时明确定义打断时点。
- [ ] R2-093：为语音识别提供可选本地后端和文本输入兜底。
- [ ] R2-094：不能将浏览器Web Speech API视为所有浏览器通用。
- [x] R2-095：录音权限失败时保留上传功能。
- [x] R2-096：录音状态以真实MediaRecorder或采样状态驱动。
- [x] R2-097：波形来自AnalyserNode实际信号，而不是假动画。
- [x] R2-098：停止录音后关闭所有麦克风track。
- [ ] R2-099：参考录音不能误发送为聊天输入。
- [ ] R2-100：第二轮输出瓶颈数据和未达标项，不承诺理论性能就是实测结果。

## 第三轮：端到端实验与交付验收

- [ ] R3-001：启动时检查两块GPU的模型加载状态。
- [ ] R3-002：只有两块GPU独立推理成功才显示双卡就绪。
- [ ] R3-003：分别记录冷启动和热启动时间。
- [ ] R3-004：固定性能样本的语言、长度与语音版本。
- [ ] R3-005：对同一请求记录统一时间线和关联ID。
- [ ] R3-006：记录用户提交至DeepSeek首token的延迟。
- [ ] R3-007：记录首个文本段形成的延迟。
- [ ] R3-008：记录GPU排队与模型首声学输出的延迟。
- [ ] R3-009：记录编码、传输和浏览器预缓冲的延迟。
- [ ] R3-010：以实际可听首样本而不是接口返回计算首声。
- [ ] R3-011：首声目标3秒必须注明硬件、网络和预热条件。
- [ ] R3-012：同时报告P50与P95而不是挑选最快一次。
- [ ] R3-013：公布超时比例与最慢样本。
- [ ] R3-014：统计取消请求时不要混入成功首声分位数。
- [ ] R3-015：对未开始播放的失败请求单独报告。
- [ ] R3-016：说明浏览器时间与服务端时间如何关联。
- [ ] R3-017：分别报告端到端RTF和纯TTS RTF。
- [ ] R3-018：用生成耗时除以音频时长计算RTF。
- [ ] R3-019：双卡聚合吞吐与单流RTF分开报告。
- [ ] R3-020：RTF不达0.5时不得自动写成通过。
- [ ] R3-021：测量连续播放中的队列欠载次数。
- [ ] R3-022：区分自然语言停顿与系统缓冲断音。
- [ ] R3-023：记录丢包、重传和乱序恢复计数。
- [ ] R3-024：使用长回答验证后半段不会耗尽缓冲。
- [ ] R3-025：使用无标点回答验证切句器上限。
- [ ] R3-026：使用中英混合文本验证正规化。
- [ ] R3-027：使用多轮上下文验证供应商上下文边界。
- [ ] R3-028：模拟供应商限流并验证有界重试。
- [ ] R3-029：模拟DeepSeek中途断流且不重复播已说文本。
- [ ] R3-030：不在同一turn中无提示地重试产生另一份回答。
- [ ] R3-031：按不同输入长度重复首声测量。
- [ ] R3-032：按两张卡分别测量相同文本RTF。
- [ ] R3-033：记录峰值显存、CPU、内存和网络流量。
- [ ] R3-034：用两卡负载不均场景验证调度。
- [ ] R3-035：用worker崩溃验证队列清理和恢复。
- [ ] R3-036：用GPU OOM验证服务退回可诊断状态。
- [ ] R3-037：用上传大文件验证资源限制。
- [ ] R3-038：用异常音频验证解码失败不影响其他库。
- [ ] R3-039：用零条有效样本验证训练按钮不会假成功。
- [ ] R3-040：用训练取消验证没有残留GPU任务。
- [ ] R3-041：定义训练完成必须包含已见样本和检查点记录。
- [ ] R3-042：验证全部选中有效样本跨rank至少被读取。
- [ ] R3-043：记录不能接受样本的排除清单。
- [ ] R3-044：训练轮次与数据完整性分开验收。
- [ ] R3-045：用恢复训练验证步数与模型版本正确。
- [ ] R3-046：用停止Notebook后重启流程验证资产恢复。
- [ ] R3-047：从干净环境执行安装与启动单元。
- [ ] R3-048：清理仅缓存数据后重新运行可用性测试。
- [ ] R3-049：验证已有资产不会被初始化示例覆盖。
- [ ] R3-050：验证失败的训练检查点不替代最后可用版本。
- [ ] R3-051：定义音色相似度的模型、维度和计算方式。
- [ ] R3-052：不把cosine=0.995直接解释为99.5%人声一致。
- [ ] R3-053：使用未参与训练的参考与文本评估。
- [ ] R3-054：对内容正确性统计CER或WER。
- [ ] R3-055：对情感、节奏、音质分别设置主观评价项。
- [ ] R3-056：进行盲听而不是只由开发者选最好样本。
- [ ] R3-057：记录参考音频环境差异对结果的影响。
- [ ] R3-058：不强制降噪或音高处理导致身份特征丢失。
- [ ] R3-059：记录随机种子与生成采样参数。
- [ ] R3-060：相似度目标未达到时展示实际值与评估限制。
- [x] R3-061：参考语音界面与对话界面保持两个明显入口。
- [x] R3-062：页面适配常见桌面和手机视口。
- [x] R3-063：主要操作无需页面纵向滚动。
- [ ] R3-064：音频列表超量时分页而非无限增长撑开页面。
- [ ] R3-065：训练日志使用分页或切换详情面板。
- [ ] R3-066：窄屏不强行隐藏重要错误或控制按钮。
- [x] R3-067：录音按钮显示开始、停止、时长和权限状态。
- [ ] R3-068：波形在静音时仍保持录音状态标签可见。
- [ ] R3-069：录音、上传、转写和训练采用独立状态。
- [ ] R3-070：对话页面可随时选声音但切换策略明确。
- [ ] R3-071：切换声音时在途段使用旧版本或统一取消，不能混音色。
- [ ] R3-072：语音库删除必须确认并处理正在使用的版本。
- [ ] R3-073：语音库重命名不改变内部ID。
- [ ] R3-074：删除音频不破坏已发布检查点的可追溯清单。
- [x] R3-075：API密钥输入框不回显已保存密钥。
- [ ] R3-076：后端只返回是否已配置及验证结果。
- [ ] R3-077：配置测试不发起意外长文本收费请求。
- [x] R3-078：会话令牌与DeepSeek密钥分离。
- [x] R3-079：公开访问入口默认要求认证。
- [ ] R3-080：导出的代码和日志不得含实际秘密。
- [ ] R3-081：为Kaggle复制按钮明确所复制文件与版本。
- [ ] R3-082：复制完整Python源码而不是网页HTML。
- [ ] R3-083：Notebook需要明确导出为代码单元，不盲拼魔法命令。
- [ ] R3-084：提供复制失败后的手动选择兜底。
- [ ] R3-085：复制成功不宣称运行验证成功。
- [ ] R3-086：提供依赖单元和启动单元的执行顺序。
- [ ] R3-087：验证复制代码的哈希与原交付文件一致。
- [ ] R3-088：下载包包含README、依赖锁定和许可证。
- [ ] R3-089：模型、音频和训练权重不提交到Git。
- [ ] R3-090：保留现有编辑、保存、命名和预览回归测试。
- [ ] R3-091：第一遍端到端覆盖正常录音、训练与聊天。
- [ ] R3-092：第二遍端到端覆盖异常、取消与打断。
- [ ] R3-093：第三遍端到端覆盖重启、长回答和持续播放。
- [ ] R3-094：每遍记录硬件环境、用例数与失败截图。
- [ ] R3-095：单元模拟通过不得代替真实GPU测试。
- [ ] R3-096：公开未实现功能列表，不用占位按钮表示完成。
- [ ] R3-097：所有修复都关联真实源码位置和对应测试。
- [ ] R3-098：为版本发布保留可回滚方案。
- [ ] R3-099：将决策、清单、命令和阻塞汇总到单一提示词。
- [ ] R3-100：缺少源文件、GPU、模型或API时暂停相应验收结论。


第四阶段新增R3-061/062/063的证据限定为所列五个Chromium CSS视口；≤640px高允许页面滚动，实际虚拟键盘/OS缩放未验。内部滚动不等于分页，未勾R3-064。完整日志KAGGLE_STEP4_AUDIT.md。

第八阶段新增R2-010仅覆盖同机同UID合作式整组所有权锁、有界预约和进程/最后描述符退出恢复设计与真实CPU进程验证；不是跨UID/容器隔离、自动训练模式或实际显存回收验收，R2-001/003/006/009/011等仍未勾选。

第九阶段已补强R1-079与R2-031的来源证据及删除互斥，但没有完整训练器/分词版本/DDP数据生命周期，不勾R2-032或R2-034。保持22/300。当前8题400建议不是400项验收。

第十阶段实际训练代码已开发，CPU真实张量/Gloo有梯度/参数更新与跨rank一致证据；不因尚无GPU验收而称“未开始开发”。R2-011/012/025/040等真正Qwen/CUDA目标仍未验收，维持22/300；9题450建议。此分母是目标验收，不是代码开发进度。

第十三阶段：保留300个目标ID和22勾选；新增三轮各100条定向开发建议见validation/step13/review-map.json。明确修复step12延迟导入漏测，不把完整包导入/CPU微型Mimi当真实1.7B/T4加载。12题600建议，三轮结果以step13/final-checks.json为准。

第十四阶段三轮各100建议及逐项处置独立记录，完整清单仍22/300。录音/缓存/原文/额外呼吸代码范围和真正网页训练控制闭环分开，后者未完成；15题750建议，不是750修复。


## 第十五阶段追加状态（不替换完整目标勾选）

REVIEW1/2/3各100定向建议，问题16–18各50建议，处置见step15/review-disposition.json；不是300个bug或900项已实现功能。本轮向量隔离/首句/有界增响/创建复用工程回归与真实T4声学/性能分开，仍缺目标机验收及历史网页训练闭环。完整目标仍22/300，不因CPU/Mock通过自动升级。

---

## 内嵌备忘录：KAGGLE_DECISIONS.md

# 专业决策备忘录（历史决策＋源码到齐后的状态更新）

**2026-10-21：源码现已到齐并保留。** 下列9个问题及每题50条建议保留其历史推理顺序；其中“缺少源码”的输入状态已解除，不再向用户索取同一文件。首批历史修复见 `KAGGLE_SOURCE_AUDIT.md`；认证/资源预算历史证据见 `KAGGLE_SECURITY_AUDIT.md`，兼容探针与原生录音证据见 `KAGGLE_STEP3_AUDIT.md`，两主视图/视口历史证据见 `KAGGLE_STEP4_AUDIT.md`，命名空库/参考样本历史见 `KAGGLE_STEP5_AUDIT.md`，训练输入历史见 `KAGGLE_STEP6_AUDIT.md`，来源封存历史见 `KAGGLE_STEP9_AUDIT.md`，当前训练核心见 `KAGGLE_STEP10_AUDIT.md`。实验性训练核心已开发，真实Qwen/GPU执行仍待验证；历史建议完整保留，当前第9题后累计450条建议。

## 问题1：没有原始kaggle代码时，应选择直接重写，还是先锁定源码和验收边界？

选项A：凭描述编写替代品并宣称修好；选项B：先定位原文件，保留基线，完成有依据的设计与可独立交付部分。推荐并选择B。缺少原文件时不能知道真实报错，也不能承诺保持其成功功能。继续追问的焦点是设备与训练语义。

### 本问题之后的50项具体实施建议

1. [R1-001] 定位用户实际上传的kaggle源文件，缺失时停止逐行修复结论。
2. [R1-002] 记录源文件SHA256与文件大小，避免审查错误版本。
3. [R1-003] 识别Python脚本和Notebook格式，不把Notebook JSON直接当Python。
4. [R1-004] 保留用户原文件备份，不用默认示例覆盖。
5. [R1-005] 列出全部本地模块、动态生成文件与启动单元。
6. [R1-006] 标记原有可用功能并建立回归基线。
7. [R1-007] 梳理安装、下载、预处理、训练、推理、前端六个入口。
8. [R1-008] 检查Notebook重复执行是否创建重复服务。
9. [R1-009] 排查硬编码密码与API密钥，仅记录发现位置不输出秘密。
10. [R1-010] 为每个真实缺陷记录复现步骤、行号和影响范围。
11. [R1-011] 检查GPU数量是否实际为2，不能只根据平台选项判断。
12. [R1-012] 记录每块GPU名称、compute capability与可用显存。
13. [R1-013] 记录驱动、CUDA、PyTorch与Python版本。
14. [R1-014] 验证两个worker分别绑定不同物理GPU。
15. [R1-015] 禁止device_map=auto意外将同一模型切分到双卡。
16. [R1-016] 避免训练主进程初始化CUDA后再不安全地fork。
17. [R1-017] 使用spawn进程启动方式并防止Notebook递归启动。
18. [R1-018] 对每个GPU分别执行独立最小推理。
19. [R1-019] 区分双GPU吞吐与单段音频延迟，不能直接等同。
20. [R1-020] 在GPU不可用时返回失败状态而不是模拟模型成功。
21. [R1-021] 确认克隆模型是Qwen3-TTS-12Hz-1.7B-Base。
22. [R1-022] 确认Tokenizer版本与模型相匹配。
23. [R1-023] 固定模型权重revision并记录哈希。
24. [R1-024] 核对官方Python接口签名，不猜测流式参数。
25. [R1-025] 确认generate_voice_clone返回形式是否为整段波形。
26. [R1-026] 确认所选后端确实支持增量声学输出。
27. [R1-027] 区分Base、CustomVoice与VoiceDesign用途。
28. [R1-028] 不假定Base支持任意自然语言情感指令。
29. [R1-029] 核实clone prompt能否跨进程直接复用。
30. [R1-030] 每块GPU独立构建并校验参考特征缓存。
31. [R1-031] T4默认研究FP16而不是直接复制BF16示例。
32. [R1-032] 对SDPA可用内核做真实设备探测。
33. [R1-033] 保留eager注意力可诊断回退而非静默换模型。
34. [R1-034] 不默认安装面向Ampere的标准FlashAttention 2。
35. [R1-035] 不把第三方Turing内核直接视作官方兼容。
36. [R1-036] 检查推理算子是否出现CPU回退。
37. [R1-037] 记录FP16非有限输出与溢出。
38. [R1-038] 检查采样率、声道与波形类型的返回契约。
39. [R1-039] 用torch.inference_mode限定推理路径。
40. [R1-040] 为模型预热单独计时，不计入热启动首声成绩。
41. [R1-041] 核实全部Python依赖的版本约束。
42. [R1-042] 新建隔离环境，避免破坏Kaggle内置CUDA依赖。
43. [R1-043] 不无条件升级torch或卸载平台GPU运行库。
44. [R1-044] 安装前检查磁盘容量与网络权限。
45. [R1-045] 下载失败保留可诊断错误并支持续传。
46. [R1-046] 验证下载文件完整性，不能只检查目录存在。
47. [R1-047] 对冷启动依赖下载显示阶段进度。
48. [R1-048] 移除每次聊天重复pip安装与模型加载。
49. [R1-049] 安装日志不包含密钥或私人音频内容。
50. [R1-050] 生成可重复执行的依赖锁定清单。

## 问题2：双T4是否应在训练时继续各常驻一个推理副本？

选项A：不做显存预算，同时运行两份推理与双卡全参数训练；选项B：会话内双副本推理，训练期间独占两卡，验证并恢复双副本。推荐并选择B。这是明确的资源模式切换，不假装同时满足互相冲突的显存承诺。LoRA等低内存路径仍需真实模型验证。继续追问的焦点是流式首声与播放。

### 本问题之后的50项具体实施建议

1. [R2-001] 把推理与训练定义为互斥的GPU资源模式。
2. [R2-002] 训练前停止接收新推理任务并提示服务状态。
3. [R2-003] 显式取消或排空旧任务后再释放推理显存。
4. [R2-004] 训练结束后仅在检查点验证通过时恢复推理。
5. [R2-005] 恢复时将选定模型分别加载到两块GPU。
6. [R2-006] 防止同时常驻推理副本和全参数训练造成OOM。
7. [R2-007] 训练失败保留上一可用模型和语音库。
8. [R2-008] 资源不足时报告原因，不静默降成0.6B。
9. [R2-009] 检查模型卸载后实际可回收显存。
10. [R2-010] 设计GPU资源所有权锁与超时恢复。
11. [R2-011] 使用两个真实rank参与同一个训练作业。
12. [R2-012] 确认每个rank的设备映射和分布式world_size。
13. [R2-013] 用分布式采样器划分数据而非重复整套样本。
14. [R2-014] 每轮调用set_epoch更新采样顺序。
15. [R2-015] 统计原始样本ID的跨rank覆盖情况。
16. [R2-016] 不因drop_last让选定样本长期不参与训练。
17. [R2-017] 不能整除world_size时标明填充或重复样本策略。
18. [R2-018] 记录每rank步数与梯度同步次数。
19. [R2-019] 显式同步训练异常，避免另一rank永久挂起。
20. [R2-020] 验证两卡训练不是并行执行两个独立微调。
21. [R2-021] FP16训练启用相应GradScaler与溢出检查。
22. [R2-022] 只对可训练参数创建优化器状态。
23. [R2-023] 使用梯度累积降低单卡微批显存。
24. [R2-024] 记录有效全局batch的实际计算方式。
25. [R2-025] 验证loss有限并实际发生参数更新。
26. [R2-026] 记录每轮耗时、已见样本数和学习率。
27. [R2-027] 避免将loss降低等同音色相似度提升。
28. [R2-028] 支持用户取消后保存可恢复状态。
29. [R2-029] 验证取消操作对两个rank同时生效。
30. [R2-030] 防止训练进程结束后留下占显存子进程。
31. [R2-031] 训练清单固定所选音频ID和内容哈希。
32. [R2-032] 任务启动后音频编辑不改变运行中的数据集。
33. [R2-033] 音频编码准备阶段显示真实进度。
34. [R2-034] 保留原始JSONL、分词版本与声学码版本。
35. [R2-035] 明确保存优化器、调度器和随机数状态需求。
36. [R2-036] 所有rank按后端要求参与检查点状态收集。
37. [R2-037] 只有指定写入进程发布最终清单。
38. [R2-038] 检查点临时目录校验后再原子切换。
39. [R2-039] 按训练后端正确处理分片或完整state_dict。
40. [R2-040] 使用新进程加载检查点完成独立试听。
41. [R2-041] 为单说话人微调保存说话人ID映射。
42. [R2-042] 保存适配器与基础权重revision的绑定关系。
43. [R2-043] 不混淆Base克隆接口与训练后CustomVoice接口。
44. [R2-044] 对多个语音库采用各自版本，不覆盖全局共享状态。
45. [R2-045] 推理任务携带不可变的voice_revision。
46. [R2-046] 检查切换语音时缓存键包含模型版本。
47. [R2-047] 为旧模型引用计数，避免在途推理使用已卸载权重。
48. [R2-048] 保留模型切换失败回滚路径。
49. [R2-049] 对同一语音两块GPU生成的音频做一致性抽样。
50. [R2-050] 训练完整性报告列出选中、有效、已见和排除样本数量。

## 问题3：如何处理3秒首声、连续播放和打断，而不虚构硬件性能？

选项A：整段生成完再播放并把HTTP响应时间当首声；选项B：先验证后端真实流式能力，再做文本增量、序号队列、统一样本时钟与整链路取消，实测后报告。推荐并选择B。若官方包装器或T4不支持所需增量声学输出，必须记录技术试验失败与替代方案，不能把分句整段生成冒称token级流式。此决策形成时缺少源码；现在源码已到齐并完成CPU协议回归，真实模型和GPU环境仍阻塞，不能宣布100%确定。

### 本问题之后的50项具体实施建议

1. [R2-051] DeepSeek以流式模式读取增量文本。
2. [R2-052] API模型名称按供应商实际能力配置。
3. [R2-053] 分别配置输出预算与上下文预算。
4. [R2-054] 处理finish_reason=length与长文截断。
5. [R2-055] 避免在第一句之前等待完整长回答。
6. [R2-056] 为中文句号、问号、感叹号定义切句规则。
7. [R2-057] 为无标点长文本提供最大等待时间与长度边界。
8. [R2-058] 保护代码块、小数、URL和缩写不被错误切断。
9. [R2-059] 记录切句器尚未消费的尾部文本。
10. [R2-060] 结束流时刷新最后一个不完整句子。
11. [R2-061] 为每轮聊天生成turn_id。
12. [R2-062] 为每段文本生成递增segment_id。
13. [R2-063] 两个GPU按任务队列工作而不是前端并发无序播放。
14. [R2-064] 首个短段优先调度至空闲且已预热的worker。
15. [R2-065] 后续段适度增大，以减少句间重启成本。
16. [R2-066] 限制预合成队列长度，防止长输出撑爆内存。
17. [R2-067] 对慢段实施顺序等待，不能跳过内容。
18. [R2-068] 记录各段音频采样率与长度。
19. [R2-069] 重采样至统一播放格式后再进入浏览器队列。
20. [R2-070] 不对尚未实现的token级流式接口作虚假声明。
21. [R2-071] 用WebSocket或流式HTTP传送明确的音频元数据。
22. [R2-072] 为每个音频包携带turn、segment、chunk和版本信息。
23. [R2-073] 音频数据采用确定字节序和波形编码。
24. [R2-074] 处理传输分片、半包和重复包。
25. [R2-075] 浏览器按样本时钟而不是收到即play调度。
26. [R2-076] 使用同一AudioContext播放时钟。
27. [R2-077] 首次用户操作中显式解锁音频上下文。
28. [R2-078] 为自动播放被拒提供可见的开始播放入口。
29. [R2-079] 设计有界预缓冲与可观测欠载计数。
30. [R2-080] 不靠无限预缓冲掩盖首声延迟不达标。
31. [R2-081] 使用连续PCM调度或AudioWorklet环形队列。
32. [R2-082] 每块音频采用相同声道与采样率。
33. [R2-083] 必要时用短交叉淡化消除拼接爆音。
34. [R2-084] 不得用交叉淡化掩盖句子丢失或重复。
35. [R2-085] 保存浏览器已排程的所有音频节点。
36. [R2-086] 打断时停止节点并清空尚未播放队列。
37. [R2-087] 发送取消信号至DeepSeek读取任务。
38. [R2-088] 通过生成停止条件取消GPU任务，而不仅关闭界面。
39. [R2-089] 旧turn迟到音频一律丢弃。
40. [R2-090] 新输入不等待旧整段合成完成才进入调度。
41. [R2-091] 麦克风输入与播放回声处理分开设计。
42. [R2-092] 用户按住或点击语音输入时明确定义打断时点。
43. [R2-093] 为语音识别提供可选本地后端和文本输入兜底。
44. [R2-094] 不能将浏览器Web Speech API视为所有浏览器通用。
45. [R2-095] 录音权限失败时保留上传功能。
46. [R2-096] 录音状态以真实MediaRecorder或采样状态驱动。
47. [R2-097] 波形来自AnalyserNode实际信号，而不是假动画。
48. [R2-098] 停止录音后关闭所有麦克风track。
49. [R2-099] 参考录音不能误发送为聊天输入。
50. [R2-100] 第二轮输出瓶颈数据和未达标项，不承诺理论性能就是实测结果。


## 问题4：空声音库、原始参考与训练产物是否合放profiles并用同一个“训练成功”状态？

选项A：直接创建空profile，保存样本后标为训练完成；选项B：独立命名空库和原始样本存储，显式勾选后调用现有参考处理，真实训练另设硬件门禁。推荐并选择B。阶段计划先保存于KAGGLE_STEP5_PLAN.md，再实现并记录以下50项建议；不再向用户重复提问，也不进入下一个专业问题冒充训练已完成。

### 本问题的50项具体实施与后续建议

1. 将原始库放STATE/libraries，不复用profiles目录。
2. 自定义空库名称，不预填示例或自动命名。
3. 对名称做NFC标准化、去首尾空白与64码点上限。
4. 内部路径只用随机UUID，不拼显示名称。
5. 同名库按大小写折叠拒绝，提示选择原库。
6. 建库不要求音频、不加载模型、不生成假档案。
7. 保留旧的一步创建档案入口与请求格式。
8. 库管理采用辅助dialog，不加第三主导航。
9. 在手机常驻可找到的区域提供管理入口。
10. 允许建库后回到采集页录音，再添加该本地片段。
11. 打开库窗口停止麦克风并保留有效片段。
12. 窗口关闭/Escape恢复入口焦点。
13. 锁定关闭窗口并清空服务端样本名称与文件选择。
14. 为所有异步操作增加访问代际与窗口代际检查。
15. 不假定AbortSignal能撤回已提交的服务端写入。
16. 服务端修订CAS防止旧窗口覆盖新样本清单。
17. 所有库路由继续走单用户认证代理。
18. 只有精确samples上传路径使用较大请求预算。
19. 保持process/删除/建库的JSON请求预算。
20. 拒绝重复JSON字段、非有限常量与未知字段。
21. 限制库数量，避免无限空目录。
22. 限制每库样本数和每文件字节数。
23. 限制每库与全部库的原始音频总字节数。
24. 写入前保留磁盘余量，但不把这称作OS配额。
25. 文件名仅用于显示并去掉目录和控制字符。
26. 以SHA256对同库相同内容去重。
27. 保存样本ID、内容哈希、大小与创建时间。
28. 不从扩展名推断已经成功解码。
29. 不把浏览器墙钟当服务端编码时长。
30. 在真正参考处理阶段再次应用解码时长预算。
31. 原子替换清单，避免并发共享临时文件。
32. 样本写失败或清单提交失败回滚本次新文件。
33. 下一次库修改回收未引用音频/临时文件。
34. 损坏清单报错，不用空清单覆盖真实数据。
35. 创建0700目录和0600文件。
36. 拒绝库路径/清单/参考样本软链接或文件硬链接。
37. 使用Linux flock，而非进程重启后永久busy布尔值。
38. 构建期间禁止同库上传、移除样本和删除库。
39. 固定本次勾选的ID与字节快照，不把后续上传混入运行任务。
40. 复用已有构建准入，避免新旧接口同时占GPU处理。
41. 让HTTP取消与后台线程接管处于同一个准入函数。
42. 只有库结果成功提交后才公开任务终态。
43. 处理失败保留原件及以前成功产生的独立档案。
44. 进程死亡释放租约；遗留running显示interrupted。
45. 原始库不自动加入Dataset，明确会话目录不保证永久。
46. 提醒处理后的锚点/转写仍遵循已有档案备份设置。
47. 删除原始库不连带删除档案，也不承诺安全擦除。
48. 用真实文件系统/FastAPI/Go链路与浏览器夹具分别验证，不混淆证据。
49. 真实训练另验world_size=2、样本覆盖、梯度更新与检查点重载，不能用参考处理替代。
50. 冻结历史交付包；容量不足时独立文件交付，不提高工作台1MiB限制或删除历史。

本阶段实现情况、失败记录和真实硬件阻塞统一见KAGGLE_STEP5_AUDIT.md。前3题150条建议保留，加本题共200条建议；它们不是已修复200项的结论。

## 问题5：没有逐条转写和固定数据版本，是否直接启动双卡训练？

选项A：把参考准备当训练直接启动；选项B：先冻结有逐条转写、统一参考、来源哈希与明确授权的训练输入，再独立验真实分词和双rank训练。推荐并选择B。先保存STEP6计划与本题50项建议，再实施；不进入下一个问题冒充训练已经完成。

### 本问题的50项行动建议

1. 训练输入与profiles/原始库分目录。
2. 必须选定现有命名库。
3. 请求固定库修订号。
4. 每个训练样本显式勾选。
5. 拒绝重复样本ID。
6. 拒绝来自其他库的ID。
7. 取快照期间持有同库租约。
8. 不改写最近参考处理状态。
9. 逐条要求对应转写。
10. 不把公共ref_text复制给全部样本。
11. 校验Unicode与文本长度。
12. 约束累计转写长度。
13. 明确转写是用户提供而非ASR验证。
14. 声音授权需明确声明。
15. 单说话人需明确声明。
16. 声明不冒充身份鉴定。
17. 统一参考必须来自选中集合。
18. 明确要求参考时长上限。
19. 不默默裁剪长参考。
20. 首版严格限定已验证PCM16 WAV格式。
21. 不把Opus改后缀冒充WAV。
22. 核对RIFF长度与chunk边界。
23. 拒绝多data/多fmt歧义容器。
24. 核对24kHz/单声道/16bit。
25. 核对真实PCM帧数。
26. 拒绝过短/超长片段。
27. 核对累计时长。
28. 拒绝空白或恒定信号。
29. 不把非恒定信号认定为有效语音。
30. 规范输出WAV且保留全部PCM帧。
31. 剥离非必要容器元数据。
32. 保存原始内容哈希。
33. 保存规范音频哈希。
34. 保存逐条文本哈希。
35. JSONL严格使用audio/text/ref_audio。
36. 所有相对路径由服务端ID生成。
37. 所有行使用同一个参考路径。
38. 提醒上游工具以快照目录作为工作目录。
39. 双rank分配计划不丢样本。
40. 奇数样本明确记录padding重复。
41. 分配计划不冒充rank执行记录。
42. 训练/分词/梯度/性能标志保持未验。
43. 独立目录原子发布，失败回滚。
44. 控制快照数量和总字节预算。
45. 校验内容，不以文件存在判断完整。
46. 列表不重复传回所有私有转写。
47. 删除原始库不隐式删除训练副本。
48. 单独删除副本且不自动云备份。
49. 保留历史包/工作台文件，不放宽1MiB。
50. 用真实WAV、故障注入、三轮回归与最终完整源码复制记录证据，不把沙箱模拟称为双T4训练。

前4题200建议保留，加本题共250项建议，不等于已完成250项验收。

## 问题6：尚无GPU资源互斥时，是否把声学码任务直接挂到在线双卡服务？

选项A：网页直接调用cuda:0 tokenizer，与现有推理争抢资源；选项B：先实现固定版本租约与离线本地CPU编码事务，真实模型缺失时blocked，GPU入口另设资源门禁。推荐并选择B。CPU不是最终速度方案；此选择先消除错版本、假成功、半成品和误删输入风险，不声称已运行真实模型。

### 本问题的50项行动建议

1. 冻结第六阶段包和哈希。
2. 编码前先保存第七阶段计划。
3. 再读固定上游prepare_data接口。
4. 核对12Hz模型返回二维码形状。
5. 核对1920下采样率和向上取整长度。
6. 核对16列码本而非25Hz一维输出。
7. 核对严格整数与2048范围。
8. 拒绝空结果。
9. 拒绝多返回或少返回，不用zip截断。
10. 单样本编码降低批次峰值。
11. 不把240秒样本偷偷裁短。
12. 输入固定manifest SHA256。
13. 编码前完整校验输入。
14. 长任务持有输入使用租约。
15. 删除输入遇租约明确409。
16. 租约放快照目录外。
17. 进程死亡由OS释放锁。
18. 不长期锁住所有输入列表。
19. 单独保存声学码资产。
20. 所有目录0700。
21. 所有输出文件0600。
22. 复制全部WAV使输出独立。
23. 保留每行audio/text/ref_audio。
24. 保留来源ID顺序和全部成员。
25. 复制并验证原双rank数学计划。
26. 状态区分真实执行和测试fixture。
27. fixture不能标记真实tokenization执行。
28. 编码完成不叫训练成功。
29. 模型只从本地目录加载。
30. 不允许远程模型ID。
31. 固定模型全部文件内容哈希。
32. 拒绝模型目录软硬链接。
33. 只允许JSON/safetensors模型资产。
34. 不加载pickle或远程自定义代码。
35. 加载前后核对模型指纹。
36. 模型必须12Hz/24kHz匹配配置。
37. 当前仅CPU/FP32/eager。
38. 不占用两推理GPU或自动停服务。
39. 限制CPU线程数。
40. 父进程施加总期限。
41. 取消终止完整子进程组。
42. 不向公开输出泄露原始异常和转写。
43. 原子发布并回滚失败。
44. 回收被杀任务的孤立暂存。
45. 设数量、单份、总量和磁盘余量预算。
46. 副本默认不进入Dataset备份。
47. 源输入删除不等于删除声学码副本。
48. 覆盖进程锁、形状错误、故障注入和CLI负向路径。
49. 三轮回归保留全部旧功能和真实源码复制。
50. 真实模型/GPU缺失时如实blocked，下一步资源互斥和真正训练仍独立验收。

前5题250建议保留，加本题共300项建议；建议数量不等于300清单全部完成。

## 问题7：按PID/显卡编号直接切换训练模式，还是先建立可继承的整组资源租约？

选项A：检查supervisor.pid或CUDA索引，超时后自动抢占；选项B：同机同UID整组独占flock、受控FD继承、最后进程退出才释放，手动停服务后再预约。推荐并选择B。PID可能复用、CUDA索引可能别名、父退出不等于孩子释放显存；本阶段只做协议准入，不把预约叫训练。

### 本问题的50项行动建议

1. 冻结第七阶段哈希。
2. 先保存第八阶段计划。
3. GPU租约独立于QTTS_STATE。
4. 不按逻辑CUDA索引拆分锁。
5. 同UID整组独占，优先安全而非并发。
6. 跨UID/容器不宣称全局隔离。
7. 固定私有目录不提供环境分区旁路。
8. 根目录0700。
9. 锁文件0600。
10. 拒绝符号链接。
11. 拒绝硬链接和非普通文件。
12. 核对文件属主。
13. 不删除或原子替换正在使用的锁文件。
14. flock才是占用权威。
15. PID记录只用于诊断。
16. 不依赖TTL强制解锁。
17. supervisor先锁后启动模型进程。
18. 第二supervisor失败不覆盖PID文件。
19. 用pass_fds继承打开文件描述符。
20. 只有worker/analyst继承GPU描述符。
21. gateway不延长GPU租约。
22. 子进程核对实际inode。
23. 子进程核对nonce和协议。
24. 子进程只采用inference类型。
25. 采用前验证文件锁仍可由该OFD持有。
26. close只关闭引用，不LOCK_UN。
27. 父进程关闭后子仍持锁。
28. 父进程SIGKILL不提前解锁。
29. 最后引用关闭才释放。
30. 失效描述符明确拒绝，不静默新建替代。
31. 独立真实worker也需要整组租约。
32. 多worker只由持锁supervisor启动。
33. analyst的延迟模型加载也受保护。
34. Mock路径明确不验证GPU所有权。
35. CPU编码保持不占GPU锁。
36. 不自动杀现有推理服务。
37. reserve只是有界预约，不执行训练。
38. status不因记录PID死亡推断空闲。
39. 预约取消和进程死亡释放原生锁。
40. 不开放任意shell或HTTP控制接口。
41. 修正父进程日志句柄泄漏。
42. 杀进程组后等待leader退出。
43. 清理leader先退出的后代。
44. 启动前安装停止信号处理。
45. 停止期间禁止再次拉起进程。
46. 保留档案恢复、认证与自动重启旧功能。
47. 真实fork/exec/FD/强杀测试而非只Mock布尔。
48. 旧版本进程先停干净，不假装已自动迁移。
49. 三轮验证和最终完整Python复制保留历史。
50. 之后在真实目标硬件验证显存释放/编码/解码，再做GPU模式与真正训练。

前6题300建议保留，加本题共350条建议；不是350项修复，也不是300审查项全部完成。

## 问题8：码副本只保留源hash就删原输入，还是封存完整来源并保护读取期？

选项A：依赖源ID/hash，删源后凭当前库补声明；选项B：新schema原样封存固定输入清单/索引，旧码明确未封存，并用固定版本读取租约阻止误删。推荐并选择B。不发明旧授权，不把文件检查当训练许可；先保存STEP9计划及50行动建议。

### 本问题的50项行动建议

1. 冻结第八阶段包和SHA256。
2. 编码前保存第九阶段计划。
3. 新码使用schema2区分来源封存。
4. 源manifest原样复制而非重新生成。
5. 复制源train_raw.jsonl完整字节。
6. 源manifest hash等于创建时固定hash。
7. 源索引hash取自源manifest。
8. 保留源库ID和自定义名称。
9. 保留源库修订号。
10. 保留原始样本ID与顺序。
11. 保留原始音频hash和来源名。
12. 保留规范WAV hash和帧数。
13. 保留逐条文本hash。
14. 保留统一参考样本ID。
15. 保留使用权声明原记录。
16. 保留单说话人声明原记录。
17. 不把声明等同权利/身份鉴定。
18. 交叉核对当前码行与源索引。
19. 拒绝漏行、多行或成员改变。
20. 拒绝参考路径被替换。
21. 拒绝文本被替换。
22. 拒绝分配计划与源hash不一致。
23. source目录0700。
24. 封存文件0600。
25. 封存拒绝软硬链接。
26. 封存纳入单份/总量预算。
27. 封存失败回滚整个新码副本。
28. 源输入不因封存被修改。
29. 删源后新码仍可独立核对来源。
30. schema1继续可读核验和删除。
31. schema1明确legacy-unsealed。
32. 不自动给旧码补授权。
33. 列表不冒充刚刚全量校验。
34. 只在真校验后返回来源已核验。
35. 读取请求固定码manifest hash。
36. 读取前核对全部文件。
37. 租约放码目录外避免改快照。
38. 长读取不锁住全局列表。
39. 首版同版本读取独占，明确409。
40. 读取期间删除同版本409。
41. 其他版本仍可核验和操作。
42. 进程死亡由OS回收租约。
43. 不用PID/TTL强制解锁。
44. CLI只保持租约，不执行任意命令。
45. CLI不输出私人转写/完整来源。
46. 超时/取消/父杀释放读取引用。
47. 测试fixture保持test_only_codes。
48. 真实训练器未来必须接入读取租约与单独门禁。
49. 不自动云备份，不改变旧profiles备份。
50. 三轮真实文件/进程与全功能回归、完整源码复制留证，不把准备当双T4训练。

前7题350建议保留，加本题共400条建议；建议数量不是已完成修复或300项清单通过数量。

## 问题9：继续封存与收据工具，还是直接实现能反向传播的训练核心？

选项A：继续前置工具并延后核心；选项B：立即交付本地Base1.7B的FP16 LoRA联合loss、真正DDP/优化器/adapter保存入口。推荐并选择B。代码可现在开发，真实T4成功仍需现场设备/权重证据，不伪装CPU为Qwen训练。

### 本问题的50项行动建议

1. 冻结原始至step9及正式工作台。
2. 先保存直接训练核心计划。
3. 不再把检查租约叫训练。
4. 固定官方模型与dataset接口提交。
5. 核对文本投影到talker维度。
6. 保留16码本联合目标。
7. 冻结Base参数。
8. 仅显式q/v线性层注入LoRA。
9. 检查实际命中的层名称。
10. LoRA参数保留FP32。
11. 不用全参数AdamW状态。
12. eager替代标准FA2。
13. T4使用FP16而非BF16。
14. microbatch首版固定1。
15. 限制总序列长度并拒绝截断。
16. 真实文本tokenizer构造助手序列。
17. 规范WAV参考生成mel。
18. 冻结speaker encoder并eval。
19. 参考声纹只计算一次。
20. DDP包装实际loss forward。
21. 禁止经.module绕过训练forward。
22. 要求恰好两个rank。
23. 每rank显式绑定一个CUDA设备。
24. 采用NCCL与集合通信超时。
25. 明确样本不足拒绝与奇数填充。
26. 每epoch确定性变换采样顺序。
27. 记录每rank见过的样本ID。
28. 不把数学分配计划称已训练。
29. GradScaler与有限梯度检查。
30. 正确处理尾部累积步数。
31. 全rank同时拒绝非有限loss。
32. 梯度裁剪前unscale。
33. 实际检验参数发生改变。
34. 原子保存adapter与speaker embedding。
35. 保存基础模型完整hash。
36. 保存数据manifest固定hash。
37. 不把adapter目录当完整CustomVoice。
38. 提供严格adapter加载函数。
39. 不自动发布未试听检查点。
40. fixture与legacy训练拒绝。
41. 要求明确语义与授权实验确认。
42. 用户声明不变成法律鉴定。
43. 父控制器持码与GPU双租约。
44. 两个rank继承相同受控FD。
45. 父死但孩子活着仍保护资源。
46. 取消超时停止并等待全部rank。
47. 离线加载不自动安装下载。
48. 只输出数值日志而非私人转写。
49. CPU真实张量/Gloo与CUDA验收分开。
50. 完成核心测试后保留原功能回归与真实阻塞。

前8题400条保留，累计9题450建议；不等于450项修复或300项清单全部通过。

## 问题10：猜测高速后端能动态挂LoRA，还是显式接官方原生推理并诚实标注缓冲？

选项A：直接往未知CUDA graph/私有对象注入并声称实时；选项B：保留默认高速路径，新增显式原生adapter后端及训练profile，句级缓冲如实标注。推荐并选择B，先完成可测试的训练后推理链路，不伪造声学流式或实机音质。

### 本问题的50项行动建议

1. 冻结step10及正式HEAD。
2. 保存直接推理接入计划。
3. 不猜CUDA graph动态LoRA兼容。
4. 默认faster路径保留。
5. 原生后端必须显式选择。
6. 明确句级缓冲不是声学流式。
7. 拒绝Mock加载训练候选。
8. 读取完成run/result/request互相一致。
9. 固定adapter manifest hash。
10. 拒绝失败取消或缺检查点的run。
11. 要求两NCCL rank更新记录。
12. 核对全部选中样本覆盖。
13. 验证adapter tensor摘要。
14. 验证speaker张量成员形状与finite。
15. 拒绝软硬链接和越界路径。
16. 限定JSON和tensor文件预算。
17. 发布使用用户自定义名称。
18. 不从第一条run猜用户选择。
19. 发布时持码版本租约。
20. 复制实际统一参考和匹配文本。
21. 不自动改active或切换推理。
22. profile绑定run/Base/码hash。
23. 每GPU只驻留一个Base模型。
24. Base必须可信本地且固定hash。
25. 严格离线与trust_remote_code false。
26. 所有目标LoRA形状先验证。
27. 不同LoRA rank可切换。
28. 所有新模块先构造再提交。
29. 失败保留先前adapter不半写。
30. 同一worker锁内切换与生成。
31. 每次使用重新核验profile绑定。
32. 缓存不绕过删除或损坏。
33. 保存speaker向量直接构造prompt。
34. 不凭另一个profile猜speaker向量。
35. x-vector-only不伪装ICL模式。
36. 不自动变成CustomVoice。
37. 完整PCM只输出一次。
38. 拒绝错采样率多声道非有限输出。
39. 取消传到stopping criteria。
40. 取消后丢弃迟到完整音频。
41. 不承诺中断CUDA kernel。
42. health/stats显示缓冲模式。
43. 网页选择器标注训练候选未验收。
44. 拒绝改写固定参考和校准。
45. 原profile删除仍保留。
46. native探针检查官方Qwen不是faster。
47. native不自动下载陌生模型。
48. 备份恢复缺adapter明确失败。
49. CPU真tensor与接口替身分开标注。
50. 完成全功能三轮与完整源码复制留证。

累计10题500建议；建议、代码实现与300项目标验收不是同一统计。

## 问题11：单独降级Transformers，还是在已审查5.x组合上修复真实RoPE配置桥接并前置复现？

A单独降4.x违背faster0.5.4依赖，可能产生另一错误；B固定现场三项组合，对已识别Qwen兼容函数做最小现代字段桥接、真实配置CPU对照和fatal门禁。推荐并选择B；完整Qwen/T4须再运行，不能据此保证成功或永久部署。

1. 保存用户实际版本与设备证据。
2. 不把探针签名通过当模型成功。
3. 冻结原始至step11。
4. 确认faster0.5.4依赖约束。
5. 确认qwen-tts-hf共享模块名。
6. 拒绝单独盲降Transformers4。
7. 读取PyPI实际wheel而非猜测。
8. 定位现代Mimi rope_parameters。
9. 定位旧Qwen默认函数读取字段。
10. 真实CPU复现缺rope_theta。
11. 包装范围限制已识别函数。
12. 不全局给MimiConfig加property。
13. 不硬编码所有模型theta。
14. 不重写权重或config文件。
15. 现代theta必须来自实际配置。
16. 拒绝非有限非正theta。
17. 拒绝未知scaled RoPE桥接。
18. 保持旧rope_theta路径不变。
19. 临时config副本避免改原对象。
20. 正确传递device与seq_len。
21. 保留partial_rotary_factor语义。
22. 验证head_dim实际契约。
23. 兼容桥重复调用幂等。
24. 拒绝未知第三方registry覆盖。
25. 保留Apache归属与来源链接。
26. 探针增加实际配置数学smoke。
27. smoke明确不加载完整模型。
28. 默认worker加载前安装桥。
29. 原生adapter加载前安装桥。
30. CPU tokenizer加载前安装桥。
31. 双rank训练加载前安装桥。
32. 不修改现有码或质量证据。
33. 固定三项直接依赖版本。
34. 不升级卸载平台Torch/CUDA。
35. 共享qwen命名空间冲突拒绝。
36. 不在日志打印HF密钥。
37. 标记确定性配置错误fatal。
38. fatal worker停止重试。
39. bootstrap尽早报告配置失败。
40. 清理只针对自己创建的Popen。
41. 不得拿旧PID盲杀进程。
42. 父及子FD释放后才允许新服务。
43. 保留每worker单GPU映射。
44. 健康显示真实GPU与模型就绪。
45. 确认无空闲自动卸载行为。
46. 明确Kaggle不能永久占GPU。
47. 提供完整会话重启操作。
48. 发布step12及更新复制页面。
49. 三轮回归与原样复制验真。
50. 真实GPU复跑结果仍待收集。

## 问题12：step12相同现场故障再现后，应继续只验证RoPE函数，还是修复实际包延迟导入生命周期？

选择并推荐后者。实际wheel证明Faster直到from_pretrained才导入Qwen；安装元数据判别HF并显式正常导入compat、预检fail-closed，必须用真实完整包加微型Mimi构造回归，不能再把手动exec上游函数当入口验收。无须再问用户。

### 本问题之后的50项具体实施建议

1. 保留用户step12实际失败结论。
2. 定位Faster顶层导出并非Qwen模型导入。
3. 记录真实Faster from_pretrained延迟导入行。
4. 区分发行安装与模块导入状态。
5. 删除HF未导入即不适用的判断。
6. 用发行元数据先选择HF或legacy分支。
7. 先检查官方与HF命名空间冲突。
8. 导入前拒绝未经审查HF版本。
9. 导入前拒绝未经审查Transformers版本。
10. 显式通过importlib导入受审compat模块。
11. 让Python正常执行真实Qwen父包初始化。
12. 不伪造生产sys.modules条目。
13. 不全局替换Python导入钩子。
14. 导入失败转明确兼容错误。
15. 错误消息避免输出凭证。
16. HF导入成功后确认默认注册函数身份。
17. 重复安装验证registry仍指向同一桥接。
18. registry被未知代码覆盖时拒绝。
19. 保留真实配置theta读取。
20. 保留三种theta精确数学对照。
21. 不修改原始Mimi配置。
22. 不修改权重或缓存权重文件。
23. 不独立降级TF4破坏Faster依赖。
24. 保留平台Torch和CUDA约束。
25. 官方legacy无HF时继续不适用。
26. 无HF却出现HF模块时拒绝矛盾环境。
27. HF预检跳过smoke必须阻断。
28. 预检仍明确没有加载完整模型。
29. 添加延迟模块导入单元回归。
30. 添加导入异常回归。
31. 添加版本未通过时不导入回归。
32. 添加冲突时不导入回归。
33. 添加官方legacy不导入HF回归。
34. 添加HF意外not_applicable预检回归。
35. 真实安装Faster完整wheel到隔离缓存。
36. 真实安装完整Qwen包而非只exec函数。
37. 保持主测试venv依赖不污染。
38. 验证Faster顶层导入后Qwen确实未加载。
39. 调用实际生产bridge触发完整Qwen导入。
40. 构造微型真实MimiModel走_init_weights。
41. 禁止真实实验from_pretrained网络下载。
42. 真实实验禁网并记录CPU/no GPU边界。
43. 每个真实导入验证独立新进程。
44. 保留step12及所有旧交付哈希。
45. 保留resident/fatal清理既有行为。
46. 保留训练adapter及两主视图。
47. 三轮全套回归而非只跑新增单测。
48. 更新复制页并验真实剪贴板下载。
49. 更新完整交接与失败反思。
50. 交付step13并明确真实双T4复跑未验。

## 问题13：十多分钟录音应作为长参考直接缓存，还是切成逐条对齐短样本后真正训练？

选A：用参考缓存冒充训练，拒绝。选B：保留完整录音，训练前用可信时间戳分段与逐条转写审核，编码后执行真实双rank LoRA，推荐B。追问：当推理已占双卡时，网页训练如何保持控制面存活？答案是独立CPU控制面和明确维护态；当前没有这条闭环，不能添加假训练按钮或绕过GPU锁。完整网页训练本轮仍是未完成门禁，不向用户虚报。

### 本问题之后的50项具体实施建议

1. 连续录音：将239秒上限与十分钟需求对齐。
2. 连续录音：同时扩大分块数量预算。
3. 连续录音：保留累计字节上限。
4. 连续录音：用虚拟时钟测试十一分钟。
5. 连续录音：停止后才保存有效片段。
6. 连续录音：取消权限晚返回仍关闭设备。
7. 连续录音：禁止空录音提交。
8. 连续录音：保留失败本地片段。
9. 连续录音：显示连续录音最大时长。
10. 连续录音：不把后台计时器当精确音频时钟。
11. 上传预算：同步浏览器与服务端时长。
12. 上传预算：同步客户端与服务端单文件字节。
13. 上传预算：保留整请求总量门禁。
14. 上传预算：保留未知长度流式门禁。
15. 上传预算：原始库独立容量核对。
16. 上传预算：PCM长音频预先计算空间。
17. 上传预算：不把提高秒数等同无限上传。
18. 上传预算：拒绝超过上限而不静默截断。
19. 上传预算：给出明确限额中文提示。
20. 上传预算：加入长WAV完整长度回归。
21. 训练入口：明确参考处理不训练。
22. 训练入口：明确快照不执行优化器。
23. 训练入口：真实训练保留独立确认。
24. 训练入口：不开虚假开始训练按钮。
25. 训练入口：网页训练需独立CPU控制面。
26. 训练入口：训练时停止两GPU推理而非争显存。
27. 训练入口：控制面不能随analyst一起关闭。
28. 训练入口：完成后再恢复原声音服务。
29. 训练入口：取消要等待两个rank退出。
30. 训练入口：未实现端到端入口须明示未完成。
31. 长录音切分：训练不能把十分钟当单条序列。
32. 长录音切分：优先审核ASR时间戳。
33. 长录音切分：不得用均分文本猜对齐。
34. 长录音切分：不得裁去超预算文本。
35. 长录音切分：保留原始音频。
36. 长录音切分：生成独立可审核短WAV。
37. 长录音切分：保留每段来源起止秒。
38. 长录音切分：同一说话人须明确声明。
39. 长录音切分：片段过短需要拒绝或重新切分。
40. 长录音切分：完整语义覆盖要逐项记录。
41. 转写：逐条训练文本对应逐条音频。
42. 转写：ASR提案不能标为人工已核验。
43. 转写：禁止将参考文本套用全部片段。
44. 转写：Unicode转写保持原值。
45. 转写：空转写拒绝。
46. 转写：转写字符总预算保留。
47. 转写：不能凭训练loss证明读音正确。
48. 转写：方言专名需要真实试听。
49. 转写：训练前审核标点断句。
50. 转写：保留来源转写hash。

## 问题14：怎样在不删样本、不减更新步数的情况下提速？

选A：减少epoch或声学码，拒绝无损说法。选B：先消除重复tokenize和host同步，保留loss/样本/顺序/优化器配置，做相同seed参数对照与成本记录，推荐B。继续追问：无限多线程是否更快？不成立，Python调度/内存复制/CPU配额与GPU串行算子有瓶颈；保留双进程DDP，线程有上限。没有真实T4基准，不声称最快或质量更好。

### 本问题之后的50项具体实施建议

1. 张量准备：找出每epoch重复文本tokenize。
2. 张量准备：缓存必须有字节上限。
3. 张量准备：缓存不改变token顺序。
4. 张量准备：缓存返回值避免被调用者污染。
5. 张量准备：超过缓存上限退回原计算。
6. 张量准备：包含声学码形状校验。
7. 张量准备：不缓存未通过预算的样本。
8. 张量准备：保留统一参考mel。
9. 张量准备：比对缓存前后collate张量。
10. 张量准备：用调用次数而非GPU倍速声称改善。
11. 优化器：保持全部联合loss。
12. 优化器：保持0.3子talker系数。
13. 优化器：保持训练样本顺序。
14. 优化器：保持累积步分母。
15. 优化器：保持不足一组累积的缩放。
16. 优化器：保持AdamW权重衰减。
17. 优化器：保持LoRA可训练参数。
18. 优化器：保持FP32适配器。
19. 优化器：不减少epoch作为无损提速。
20. 优化器：记录真实optimizer step数。
21. 双卡：保持两rank NCCL契约。
22. 双卡：不让两rank同时用同一物理卡。
23. 双卡：保持奇数样本补齐策略。
24. 双卡：保持两rank参数摘要一致。
25. 双卡：每epoch报告实际seen_ids。
26. 双卡：不能把CPU Gloo当NCCL。
27. 双卡：OOM后不得标完成。
28. 双卡：不能用两个Python线程替代DDP。
29. 双卡：显存峰值必须实测。
30. 双卡：完成后保存适配器再报告。
31. 同步开销：审查每参数grad finite读取。
32. 同步开销：合并有限性检查到一次CPU读取。
33. 同步开销：跨rank有限性继续一致。
34. 同步开销：非有限梯度两rank一同跳过。
35. 同步开销：保留梯度范数裁剪。
36. 同步开销：不盲开find_unused_parameters=False。
37. 同步开销：loss统计不删训练计算。
38. 同步开销：不盲开torch.compile。
39. 同步开销：不盲开TF32冒充T4原生支持。
40. 同步开销：CUDA优化需独立目标机基准。
41. 线程预算：按CPU配额而非文件数设置线程。
42. 线程预算：两rank线程总数不能压满宿主。
43. 线程预算：ASR线程与训练线程分开预算。
44. 线程预算：限定预处理并发。
45. 线程预算：避免每个worker再套大线程池。
46. 线程预算：保留取消与超时。
47. 线程预算：记录线程配置。
48. 线程预算：默认不引入DataLoader多进程。
49. 线程预算：小数据先消除重复计算。
50. 线程预算：吞吐测试包含预处理成本。

## 问题15：首声更快与逐字音频完全一致能否无条件同时保证？

选A：先播放再宣称已核验，拒绝。选B：应用层先消除文本改写和后加呼吸；真实声学一致性另需逐句ASR核验/试听，严格核验必然增加缓冲等待且ASR非绝对真值，推荐B。继续追问：是否通过降低缓冲来美化首声？不推荐，本轮先修有效语音首块计时与冗余处理；保留稳定缓冲，真实首声/韵律须目标机A/B。不能达到100%声学信心，更不能把未知写成成功。

### 本问题之后的50项具体实施建议

1. 文本链路：定位CleanDelta删除内容。
2. 文本链路：避免每个delta独立清洗URL。
3. 文本链路：朗读路径不补句号。
4. 文本链路：保留中英混合原文。
5. 文本链路：保留数字小数。
6. 文本链路：保留引号。
7. 文本链路：保留专有名词。
8. 文本链路：不添加链接二字。
9. 文本链路：分段连接按规范比较输入。
10. 文本链路：模型声学错字另行核验。
11. 呼吸：默认关闭额外呼吸注入。
12. 呼吸：不以合成噪声冒充真人吸气。
13. 呼吸：保留可选真实参考呼吸。
14. 呼吸：无真实片段时保持安静。
15. 呼吸：不放大短促噪声。
16. 呼吸：保留淡入淡出防爆音。
17. 呼吸：呼吸增益需试听。
18. 呼吸：模型自身呼吸与后加呼吸区分。
19. 呼吸：不盲目滤掉全部气声。
20. 呼吸：去噪不得削掉辅音。
21. 首声：区分模型首块与可听首声。
22. 首声：不把前置静音算有效语音。
23. 首声：修正trimmer前计时。
24. 首声：保留实际首播测量。
25. 首声：分段过短影响韵律须权衡。
26. 首声：小chunk需实机核验。
27. 首声：不要用空PCM刷低首声。
28. 首声：首段优先调度继续保留。
29. 首声：录制到输出完整链路测量。
30. 首声：无真实T4数据不承诺时延。
31. 缓冲：不要无条件降低首播阈值。
32. 缓冲：保留欠载预测。
33. 缓冲：保留迟滞。
34. 缓冲：区分首次启动与恢复。
35. 缓冲：生成慢时继续积累。
36. 缓冲：句级缓冲不能冒称声学流式。
37. 缓冲：记录首PCM和首播放分别。
38. 缓冲：测试短文本尾段可播放。
39. 缓冲：停止后不能漏出迟到PCM。
40. 缓冲：连续朗读不能丢段。
41. 准确朗读：模型可能幻觉不能仅靠输入相等保证。
42. 准确朗读：严格核验需整句缓存。
43. 准确朗读：ASR核验增加首声等待。
44. 准确朗读：ASR也不是绝对真值。
45. 准确朗读：不符应拒绝或请求重试。
46. 准确朗读：重试不改用户文本。
47. 准确朗读：不自动补充解释。
48. 准确朗读：多音字需目标语境测试。
49. 准确朗读：真实试听列为门禁。
50. 准确朗读：不承诺零错字。


## 问题16：怎样让参考录音只能提供音色，不能进入输出波形？

具体选项：A 继续ICL并裁参考波形；B 仅说话人向量且停顿纯静音；C 先生成后整句ASR拒播。

最推荐：B。

回答及追问结论：先取说话人向量，生成与预热均xvec_only=True，ref_text为空；禁止参考呼吸拼接和旧环境开关。A依赖裁切且参考码参与解码，不满足强隔离；C延迟更高且ASR不是真值。B会改变韵律/相似度，必须实机试听，不承诺模型不幻觉。

落实到后续代码的50项建议（本题结清后再进入下一题）：

1. [S15-R1-001] 在`worker.RealEngine`落实：禁止参考码进入解码器；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
2. [S15-R1-002] 在`worker.RealEngine`落实：仅以说话人向量条件生成；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
3. [S15-R1-003] 在`worker.RealEngine`落实：生成调用不传参考正文；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
4. [S15-R1-004] 在`worker.RealEngine`落实：预热采用相同向量模式；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
5. [S15-R1-005] 在`worker.RealEngine`落实：dtype回退后仍用向量模式；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
6. [S15-R1-006] 在`worker.RealEngine`落实：不开放环境变量回退ICL；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
7. [S15-R1-007] 在`worker.RealEngine`落实：明确韵律相似度可能变化；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
8. [S15-R1-008] 在`worker.RealEngine`落实：核对Faster0.5.4实际源码；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
9. [S15-R1-009] 在`worker.RealEngine`落实：生成采样率仍严格24k；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
10. [S15-R1-010] 在`worker.RealEngine`落实：生成器取消时仍close；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
11. [S15-R1-011] 在`worker.lead_audio`落实：废止reference呼吸拼接开关；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
12. [S15-R1-012] 在`worker.lead_audio`落实：前置停顿仅零样本；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
13. [S15-R1-013] 在`worker.lead_audio`落实：旧breath_files不能被读取；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
14. [S15-R1-014] 在`worker.lead_audio`落实：无参考片段也不造噪声；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
15. [S15-R1-015] 在`worker.lead_audio`落实：保留模型自身呼吸；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
16. [S15-R1-016] 在`worker.lead_audio`落实：不把去呼吸等同自然音色；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
17. [S15-R1-017] 在`worker.lead_audio`落实：暂停最长仍1500ms；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
18. [S15-R1-018] 在`worker.lead_audio`落实：负暂停仍归零；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
19. [S15-R1-019] 在`worker.lead_audio`落实：随机种子不能改变静音；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
20. [S15-R1-020] 在`worker.lead_audio`落实：人工试听仍是门禁；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
21. [S15-R1-021] 在`worker.run_job`落实：PCM来源只接受模型和零停顿；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
22. [S15-R1-022] 在`worker.run_job`落实：不因模型失败回放anchor；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
23. [S15-R1-023] 在`worker.run_job`落实：不因空结果播放参考；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
24. [S15-R1-024] 在`worker.run_job`落实：保留nonfinite拒绝；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
25. [S15-R1-025] 在`worker.run_job`落实：保留异常统计；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
26. [S15-R1-026] 在`worker.run_job`落实：保留裁边；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
27. [S15-R1-027] 在`worker.run_job`落实：保留尾部淡出；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
28. [S15-R1-028] 在`worker.run_job`落实：保留取消检查；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
29. [S15-R1-029] 在`worker.run_job`落实：保留每GPU互斥；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
30. [S15-R1-030] 在`worker.run_job`落实：日志报告生成隔离模式；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
31. [S15-R1-031] 在`adapter_engine`落实：核对原生向量模式；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
32. [S15-R1-032] 在`adapter_engine`落实：不能把训练参考当输出；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
33. [S15-R1-033] 在`adapter_engine`落实：固定adapter哈希；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
34. [S15-R1-034] 在`adapter_engine`落实：损坏adapter不能回退Base；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
35. [S15-R1-035] 在`adapter_engine`落实：不改变句级缓冲标记；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
36. [S15-R1-036] 在`adapter_engine`落实：不混驻两种引擎；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
37. [S15-R1-037] 在`adapter_engine`落实：保持取消丢弃迟到wave；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
38. [S15-R1-038] 在`adapter_engine`落实：训练候选不自动激活；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
39. [S15-R1-039] 在`adapter_engine`落实：新进程重载仍需实机；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
40. [S15-R1-040] 在`adapter_engine`落实：无训练证据不称已训练；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
41. [S15-R1-041] 在`朗读内容`落实：不拼接参考文本；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
42. [S15-R1-042] 在`朗读内容`落实：不修改目标文本；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
43. [S15-R1-043] 在`朗读内容`落实：不补额外说明；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
44. [S15-R1-044] 在`朗读内容`落实：不以字符串一致冒充声学一致；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
45. [S15-R1-045] 在`朗读内容`落实：不自动删数字；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
46. [S15-R1-046] 在`朗读内容`落实：不自动删专名；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
47. [S15-R1-047] 在`朗读内容`落实：不裁词谋求首声；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
48. [S15-R1-048] 在`朗读内容`落实：短句仍需语言条件；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
49. [S15-R1-049] 在`朗读内容`落实：模型幻觉单独披露；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
50. [S15-R1-050] 在`朗读内容`落实：严格ASR拒播仍未实现；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。

结论：已足够确定本轮工程取舍，无需向用户追问；真实声学质量和T4性能只能保留待测，不声称100%信心。


## 问题17：能否通过每T4放两个1.7B来降低首声？如何在不破坏朗读内容时早发第一段？

具体选项：A 每卡双副本；B 每卡一模型，首个确定语义边界即提交；C 每token一个TTS任务。

最推荐：B。

回答及追问结论：FP16纯参数约3.4GB/份，双份约6.8GB不是峰值显存；codec、KV、graph及临时张量另占内存。同卡副本共享同一计算资源，单请求不自动变快。保留两卡两模型并行相邻段；首个完整中文句或足够长逗号前缀无需等下一delta，英文点仍保留lookahead。保留播放器抗欠载策略。

落实到后续代码的50项建议（本题结清后再进入下一题）：

1. [S15-R2-001] 在`首段分段`落实：识别当前末尾标点等待lookahead；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
2. [S15-R2-002] 在`首段分段`落实：只为首段新增即时确定边界；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
3. [S15-R2-003] 在`首段分段`落实：句末中文标点可立即提交；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
4. [S15-R2-004] 在`首段分段`落实：逗号达到首段预算可提交；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
5. [S15-R2-005] 在`首段分段`落实：ASCII点仍等lookahead避小数；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
6. [S15-R2-006] 在`首段分段`落实：保留后续正常分段；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
7. [S15-R2-007] 在`首段分段`落实：新段保留原文；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
8. [S15-R2-008] 在`首段分段`落实：不等待LLM全篇完成；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
9. [S15-R2-009] 在`首段分段`落实：不为每token发TTS；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
10. [S15-R2-010] 在`首段分段`落实：短于常规阈值完整句可首发；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
11. [S15-R2-011] 在`单位边界`落实：英文单词不从中间拆开；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
12. [S15-R2-012] 在`单位边界`落实：小数12.50不拆错；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
13. [S15-R2-013] 在`单位边界`落实：英文缩写保留；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
14. [S15-R2-014] 在`单位边界`落实：标点后引号不能丢；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
15. [S15-R2-015] 在`单位边界`落实：跨delta空格仍保存；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
16. [S15-R2-016] 在`单位边界`落实：纯标点不能伪成语音；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
17. [S15-R2-017] 在`单位边界`落实：Unicode原样；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
18. [S15-R2-018] 在`单位边界`落实：组合emoji不作为词；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
19. [S15-R2-019] 在`单位边界`落实：无标点长句保持上限；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
20. [S15-R2-020] 在`单位边界`落实：最后残留仍Flush；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
21. [S15-R2-021] 在`顺序保护`落实：首段任务优先；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
22. [S15-R2-022] 在`顺序保护`落实：第二段可用另一GPU；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
23. [S15-R2-023] 在`顺序保护`落实：已输出失败不重放；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
24. [S15-R2-024] 在`顺序保护`落实：未输出失败才允许重试；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
25. [S15-R2-025] 在`顺序保护`落实：保留段索引；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
26. [S15-R2-026] 在`顺序保护`落实：保留背压高低水位；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
27. [S15-R2-027] 在`顺序保护`落实：保留迟滞；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
28. [S15-R2-028] 在`顺序保护`落实：不无限预生成；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
29. [S15-R2-029] 在`顺序保护`落实：取消移除排队任务；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
30. [S15-R2-030] 在`顺序保护`落实：健康检查不回放参考；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
31. [S15-R2-031] 在`LLM流`落实：保留每delta向前端推送；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
32. [S15-R2-032] 在`LLM流`落实：首句完成即submit；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
33. [S15-R2-033] 在`LLM流`落实：首token计时保留；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
34. [S15-R2-034] 在`LLM流`落实：首段提交计时保留；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
35. [S15-R2-035] 在`LLM流`落实：LLM完成计时保留；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
36. [S15-R2-036] 在`LLM流`落实：非法JSON报错；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
37. [S15-R2-037] 在`LLM流`落实：截断finish_reason报错；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
38. [S15-R2-038] 在`LLM流`落实：取消终止HTTP；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
39. [S15-R2-039] 在`LLM流`落实：不记录API密钥；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
40. [S15-R2-040] 在`LLM流`落实：用本地SSE延迟尾巴测试；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
41. [S15-R2-041] 在`首声指标`落实：区分首token和首段；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
42. [S15-R2-042] 在`首声指标`落实：区分模型首块和PCM；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
43. [S15-R2-043] 在`首声指标`落实：区分首PCM和首播；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
44. [S15-R2-044] 在`首声指标`落实：静音不当作人声；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
45. [S15-R2-045] 在`首声指标`落实：保留欠载次数；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
46. [S15-R2-046] 在`首声指标`落实：不以网络替身称DeepSeek实测；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
47. [S15-R2-047] 在`首声指标`落实：不以MockRTF称QwenRTF；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
48. [S15-R2-048] 在`首声指标`落实：记录首段早于LLM结束；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
49. [S15-R2-049] 在`首声指标`落实：没有CUDA不填GPU延迟；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
50. [S15-R2-050] 在`首声指标`落实：不承诺三秒内；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。

结论：已足够确定本轮工程取舍，无需向用户追问；真实声学质量和T4性能只能保留待测，不声称100%信心。


## 问题18：创建档案怎样提速而不偷偷减数据或伪造训练？

具体选项：A 默认省掉所有质量模型；B 默认延后可选GPU校准，复用CPU ASR及本任务重复嵌入，分阶段计时；C 只处理前十秒。

最推荐：B。

回答及追问结论：保留完整数据ASR、24候选评分和准确最佳锚点F0。可选校准移至用户显式调用；CPU Whisper可复用，CUDA ASR仍卸载；同任务嵌入内容去重。首建仍可能受下载和CPU大模型限制，不预设提速倍数。阶段收据必须最终持久化，长ASR段无可信对齐不能截音频配全文。

落实到后续代码的50项建议（本题结清后再进入下一题）：

1. [S15-R3-001] 在`创建默认`落实：默认关闭可选GPU候选校准；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
2. [S15-R3-002] 在`创建默认`落实：保留手动校准按钮；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
3. [S15-R3-003] 在`创建默认`落实：直接创建与库处理默认一致；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
4. [S15-R3-004] 在`创建默认`落实：后端缺省也关闭校准；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
5. [S15-R3-005] 在`创建默认`落实：锁定重置默认关闭；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
6. [S15-R3-006] 在`创建默认`落实：明确不是训练；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
7. [S15-R3-007] 在`创建默认`落实：不隐藏校准质量代价；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
8. [S15-R3-008] 在`创建默认`落实：保留两卡预热；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
9. [S15-R3-009] 在`创建默认`落实：失败不改active；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
10. [S15-R3-010] 在`创建默认`落实：完成收据不虚报；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
11. [S15-R3-011] 在`ASR成本`落实：已知单段短文本直接使用；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
12. [S15-R3-012] 在`ASR成本`落实：不能把长文本套短片；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
13. [S15-R3-013] 在`ASR成本`落实：保持全量长音频ASR；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
14. [S15-R3-014] 在`ASR成本`落实：不取前十秒冒充完整；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
15. [S15-R3-015] 在`ASR成本`落实：CPU Whisper可驻留复用；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
16. [S15-R3-016] 在`ASR成本`落实：不在GPU常驻ASR；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
17. [S15-R3-017] 在`ASR成本`落实：保留CPU回退；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
18. [S15-R3-018] 在`ASR成本`落实：保留识别beam5；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
19. [S15-R3-019] 在`ASR成本`落实：保留词时间戳；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
20. [S15-R3-020] 在`ASR成本`落实：记录手动转写绕过ASR；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
21. [S15-R3-021] 在`ASR内存`落实：仅CPU默认驻留；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
22. [S15-R3-022] 在`ASR内存`落实：CUDA ASR仍卸载；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
23. [S15-R3-023] 在`ASR内存`落实：显式开关可禁用驻留；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
24. [S15-R3-024] 在`ASR内存`落实：同一重模型入口串行；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
25. [S15-R3-025] 在`ASR内存`落实：不无限缓存音频；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
26. [S15-R3-026] 在`ASR内存`落实：不缓存每个用户转写；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
27. [S15-R3-027] 在`ASR内存`落实：不让驻留伪造模型已加载；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
28. [S15-R3-028] 在`ASR内存`落实：首次下载成本单列；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
29. [S15-R3-029] 在`ASR内存`落实：CPU内存风险披露；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
30. [S15-R3-030] 在`ASR内存`落实：不以第二次速度代表冷启动；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
31. [S15-R3-031] 在`重复计算`落实：档案内部嵌入按内容哈希复用；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
32. [S15-R3-032] 在`重复计算`落实：嵌入缓存仅本次任务；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
33. [S15-R3-033] 在`重复计算`落实：返回向量保持只读语义；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
34. [S15-R3-034] 在`重复计算`落实：不跨档案泄漏用户数据；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
35. [S15-R3-035] 在`重复计算`落实：记录embed实际调用数；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
36. [S15-R3-036] 在`重复计算`落实：记录embed命中数；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
37. [S15-R3-037] 在`重复计算`落实：候选相同波形可复用；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
38. [S15-R3-038] 在`重复计算`落实：不按文件名猜相同；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
39. [S15-R3-039] 在`重复计算`落实：不改变候选排序公式；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
40. [S15-R3-040] 在`重复计算`落实：缓存失败不写半成品；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
41. [S15-R3-041] 在`CPU候选`落实：保留24候选上限；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
42. [S15-R3-042] 在`CPU候选`落实：保留前三非重叠；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
43. [S15-R3-043] 在`CPU候选`落实：保留SNR打分；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
44. [S15-R3-044] 在`CPU候选`落实：保留典型性中心；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
45. [S15-R3-045] 在`CPU候选`落实：保留F0打分；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
46. [S15-R3-046] 在`CPU候选`落实：准确F0仍用于最佳锚点；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
47. [S15-R3-047] 在`CPU候选`落实：不偷偷换MFCC冒充ECAPA；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
48. [S15-R3-048] 在`CPU候选`落实：不降采样输入标准；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
49. [S15-R3-049] 在`CPU候选`落实：不减少可用文件；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。
50. [S15-R3-050] 在`CPU候选`落实：不承诺质量无损提速倍数；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。

结论：已足够确定本轮工程取舍，无需向用户追问；真实声学质量和T4性能只能保留待测，不声称100%信心。


## 问题19：音色不像与两种声音，应如何修复且不重新播放参考？

具体选项：A保持15纯向量；B恢复有转写ICL条件、只解码生成码、参考内容固定绑定；C把参考原音混回输出。

推荐选择：B。

详细回答：15向量模式可能弱化相似度；B保留声学/转写条件但参考码绝不进codec，新增内容指纹和路径缓存失效。C明确违反用户先前要求。ICL不能保证无幻觉或绝对相似，用户原音频未提供，实际听感仍待验。

本题回答后、进入下一题前的50项开发建议：

1. [S16-R1-001] 在`参考条件`落实：重新审视15强制向量模式；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
2. [S16-R1-002] 在`参考条件`落实：默认恢复匹配转写的ICL条件；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
3. [S16-R1-003] 在`参考条件`落实：无转写不得静默假设ICL；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
4. [S16-R1-004] 在`参考条件`落实：向量模式保留为显式选项；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
5. [S16-R1-005] 在`参考条件`落实：参考文本只作条件不拼目标正文；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
6. [S16-R1-006] 在`参考条件`落实：解码器不接参考码；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
7. [S16-R1-007] 在`参考条件`落实：保留原始参考录音；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
8. [S16-R1-008] 在`参考条件`落实：不把恢复ICL称相似度已验证；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
9. [S16-R1-009] 在`参考条件`落实：检查参考是否多人；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
10. [S16-R1-010] 在`参考条件`落实：多人参考必须换干净单人样本；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
11. [S16-R1-011] 在`提示缓存`落实：核查Faster路径键缓存；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
12. [S16-R1-012] 在`提示缓存`落实：相同路径换音频必须失效；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
13. [S16-R1-013] 在`提示缓存`落实：比较参考内容哈希；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
14. [S16-R1-014] 在`提示缓存`落实：清除该路径旧缓存项；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
15. [S16-R1-015] 在`提示缓存`落实：不删除模型全局权重；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
16. [S16-R1-016] 在`提示缓存`落实：不信任仅profile_id相同；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
17. [S16-R1-017] 在`提示缓存`落实：预热与生成采用同模式；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
18. [S16-R1-018] 在`提示缓存`落实：dtype重载后重新构建条件；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
19. [S16-R1-019] 在`提示缓存`落实：不把错误预热当就绪；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
20. [S16-R1-020] 在`提示缓存`落实：缓存失效增加回归；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
21. [S16-R1-021] 在`会话绑定`落实：会话开始固定参考内容指纹；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
22. [S16-R1-022] 在`会话绑定`落实：Go与Python指纹算法一致；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
23. [S16-R1-023] 在`会话绑定`落实：包含WAV与匹配文本；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
24. [S16-R1-024] 在`会话绑定`落实：包含语言字段；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
25. [S16-R1-025] 在`会话绑定`落实：长度前缀避免分隔歧义；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
26. [S16-R1-026] 在`会话绑定`落实：每个语段携带同一指纹；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
27. [S16-R1-027] 在`会话绑定`落实：Worker取锁后重新读取档案；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
28. [S16-R1-028] 在`会话绑定`落实：不同版本先拒绝后输出；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
29. [S16-R1-029] 在`会话绑定`落实：不重试成另一个声音；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
30. [S16-R1-030] 在`会话绑定`落实：缺文件不降级原模型；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
31. [S16-R1-031] 在`双卡一致`落实：保留每T4一个模型；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
32. [S16-R1-032] 在`双卡一致`落实：比较两卡使用的参考指纹；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
33. [S16-R1-033] 在`双卡一致`落实：保留同session条件不变；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
34. [S16-R1-034] 在`双卡一致`落实：候选切换只能影响新会话；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
35. [S16-R1-035] 在`双卡一致`落实：旧会话版本不符明确失败；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
36. [S16-R1-036] 在`双卡一致`落实：声音更新与合成共用锁；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
37. [S16-R1-037] 在`双卡一致`落实：锁后重取profile避免旧引用；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
38. [S16-R1-038] 在`双卡一致`落实：不要以profile名称证明相同；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
39. [S16-R1-039] 在`双卡一致`落实：不把RMS一致当同一说话人；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
40. [S16-R1-040] 在`双卡一致`落实：两张卡实际试听仍必需；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
41. [S16-R1-041] 在`生成稳定`落实：相邻段使用稳定seed策略；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
42. [S16-R1-042] 在`生成稳定`落实：不随意每段改变采样条件；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
43. [S16-R1-043] 在`生成稳定`落实：不以降温保证身份；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
44. [S16-R1-044] 在`生成稳定`落实：不默认删除情感；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
45. [S16-R1-045] 在`生成稳定`落实：保留语言参数；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
46. [S16-R1-046] 在`生成稳定`落实：保留max_new_tokens安全预算；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
47. [S16-R1-047] 在`生成稳定`落实：保留取消后的生成器close；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
48. [S16-R1-048] 在`生成稳定`落实：不引入随机参考混合；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
49. [S16-R1-049] 在`生成稳定`落实：不混用候选锚点；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
50. [S16-R1-050] 在`生成稳定`落实：不跨用户共享提示；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。

追问结论：工程取舍已明确，不向用户重复提问；未提供真实音频与T4不能对声学或速度声称100%。


## 问题20：沙沙声和RTF0.3能否靠换语言、加副本或提高增益解决？

具体选项：A强降噪/多副本；B有界生成码上下文、两帧lookahead、限制噪声增益、分阶段测量；C缩短或加速音频冒充RTF下降。

推荐选择：B。

详细回答：删除全历史cat，窗口25帧上下文+chunk+2帧待提交，禁止参考码解码；留160ms未来上下文减少块末不稳定。每任务重置响度状态、默认最大增益从12回到6dB，目标仍-18，显式可调。会增加约160ms音频lookahead，不能称免费低延迟或真实去噪已验。

本题回答后、进入下一题前的50项开发建议：

1. [S16-R2-001] 在`解码路径`落实：使用实际Faster0.5.4准备接口；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
2. [S16-R2-002] 在`解码路径`落实：只解码新生成声学码；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
3. [S16-R2-003] 在`解码路径`落实：禁止参考PCM占位；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
4. [S16-R2-004] 在`解码路径`落实：不得猜比例裁参考音频；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
5. [S16-R2-005] 在`解码路径`落实：codec采样率必须24k；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
6. [S16-R2-006] 在`解码路径`落实：逐帧1920样本契约需检查；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
7. [S16-R2-007] 在`解码路径`落实：不兼容长度明确失败；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
8. [S16-R2-008] 在`解码路径`落实：保留码组16列；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
9. [S16-R2-009] 在`解码路径`落实：不偷改codec权重；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
10. [S16-R2-010] 在`解码路径`落实：API签名变化明确报错；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
11. [S16-R2-011] 在`有界窗口`落实：删除每块全历史cat；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
12. [S16-R2-012] 在`有界窗口`落实：左上下文固定25帧；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
13. [S16-R2-013] 在`有界窗口`落实：待提交尾部保留2帧；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
14. [S16-R2-014] 在`有界窗口`落实：窗口随chunk有上限；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
15. [S16-R2-015] 在`有界窗口`落实：新块仅输出未提交样本；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
16. [S16-R2-016] 在`有界窗口`落实：提交游标单调；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
17. [S16-R2-017] 在`有界窗口`落实：末尾只flush一次；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
18. [S16-R2-018] 在`有界窗口`落实：取消不flush迟到音频；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
19. [S16-R2-019] 在`有界窗口`落实：新旧窗口无重复样本；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
20. [S16-R2-020] 在`有界窗口`落实：窗口长度记录便于核验；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
21. [S16-R2-021] 在`块接缝`落实：未来两帧降低边缘重解码差异；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
22. [S16-R2-022] 在`块接缝`落实：不对每块单独归一化；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
23. [S16-R2-023] 在`块接缝`落实：保留时间连续性；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
24. [S16-R2-024] 在`块接缝`落实：不要对每块强淡入；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
25. [S16-R2-025] 在`块接缝`落实：短于lookahead暂不输出；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
26. [S16-R2-026] 在`块接缝`落实：最后短块不能丢；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
27. [S16-R2-027] 在`块接缝`落实：音频总样本不缩水；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
28. [S16-R2-028] 在`块接缝`落实：不把重叠输出拼两次；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
29. [S16-R2-029] 在`块接缝`落实：真实边界爆音仍要听；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
30. [S16-R2-030] 在`块接缝`落实：增加右边缘不稳定fixture；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
31. [S16-R2-031] 在`沙沙声`落实：不生成额外呼吸噪声；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
32. [S16-R2-032] 在`沙沙声`落实：旧breath环境不能启用拼接；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
33. [S16-R2-033] 在`沙沙声`落实：限制向上增益防底噪变大；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
34. [S16-R2-034] 在`沙沙声`落实：输出目标仍负18dBFS；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
35. [S16-R2-035] 在`沙沙声`落实：保留软限幅；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
36. [S16-R2-036] 在`沙沙声`落实：不默认强低通损坏齿音；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
37. [S16-R2-037] 在`沙沙声`落实：不抹掉所有清辅音；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
38. [S16-R2-038] 在`沙沙声`落实：不假装无声就是降噪成功；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
39. [S16-R2-039] 在`沙沙声`落实：无原音频不确定噪声来源；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
40. [S16-R2-040] 在`沙沙声`落实：分别检查模型原PCM与后处理；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
41. [S16-R2-041] 在`响度状态`落实：每任务重建leveler状态；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
42. [S16-R2-042] 在`响度状态`落实：防双卡历史包络不同；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
43. [S16-R2-043] 在`响度状态`落实：保留每段淡入淡出；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
44. [S16-R2-044] 在`响度状态`落实：无语音不flush上段尾巴；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
45. [S16-R2-045] 在`响度状态`落实：显式配置最大增益；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
46. [S16-R2-046] 在`响度状态`落实：非法增益回退安全值；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
47. [S16-R2-047] 在`响度状态`落实：新旧档案一致输出策略；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
48. [S16-R2-048] 在`响度状态`落实：不能靠过载变响；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
49. [S16-R2-049] 在`响度状态`落实：用低电平与满幅信号测试；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
50. [S16-R2-050] 在`响度状态`落实：Rust与NumPy分别标边界；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。

追问结论：工程取舍已明确，不向用户重复提问；未提供真实音频与T4不能对声学或速度声称100%。


## 问题21：如何验证相似、单一声音、无沙沙与RTF≤0.3而不造硬件结果？

具体选项：A用Mock吞吐宣布达标；B三轮工程/真实库接口实验，提供实际双worker基准入口并保留声学与T4门禁；C只比较文件哈希。

推荐选择：B。

详细回答：工程测试确认绑定、边界、样本完整、取消；真实Faster控制流用明确注入CPU模型fixture，tinyMimi仅保护依赖。目标机基准调用已驻留真实worker、输出逐GPU墙钟RTF与WAV，0.3未达就失败；没有CUDA则blocked。听感与参考单人性仍需真人审核，不称100%信心。

本题回答后、进入下一题前的50项开发建议：

1. [S16-R3-001] 在`代码审查`落实：三轮读全源并记录哈希；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
2. [S16-R3-002] 在`代码审查`落实：Python AST巡检；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
3. [S16-R3-003] 在`代码审查`落实：Go格式和race；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
4. [S16-R3-004] 在`代码审查`落实：浏览器JS语法；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
5. [S16-R3-005] 在`代码审查`落实：Rust未修改仍说明现场边界；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
6. [S16-R3-006] 在`代码审查`落实：逐专题审视引用关系；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
7. [S16-R3-007] 在`代码审查`落实：不把哈希清单当语义证明；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
8. [S16-R3-008] 在`代码审查`落实：每轮100建议逐项处置；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
9. [S16-R3-009] 在`代码审查`落实：未实施项明确保留；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
10. [S16-R3-010] 在`代码审查`落实：别把300建议当300bug；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
11. [S16-R3-011] 在`参考绑定测试`落实：中英转写跨语言指纹一致；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
12. [S16-R3-012] 在`参考绑定测试`落实：WAV变更指纹变化；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
13. [S16-R3-013] 在`参考绑定测试`落实：文本变更指纹变化；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
14. [S16-R3-014] 在`参考绑定测试`落实：语言变更指纹变化；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
15. [S16-R3-015] 在`参考绑定测试`落实：质量统计变化不改变声音指纹；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
16. [S16-R3-016] 在`参考绑定测试`落实：旧Worker缓存不能放行新pin；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
17. [S16-R3-017] 在`参考绑定测试`落实：任务等待期间换档案需重校验；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
18. [S16-R3-018] 在`参考绑定测试`落实：错误绑定不能输出PCM；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
19. [S16-R3-019] 在`参考绑定测试`落实：两卡pin不等必须失败；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
20. [S16-R3-020] 在`参考绑定测试`落实：取消不触发重加载；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
21. [S16-R3-021] 在`解码测试`落实：样本总数等于总帧乘1920；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
22. [S16-R3-022] 在`解码测试`落实：reference marker严格拒绝；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
23. [S16-R3-023] 在`解码测试`落实：短码块可暂存；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
24. [S16-R3-024] 在`解码测试`落实：最大窗口有界；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
25. [S16-R3-025] 在`解码测试`落实：窗口左端超出不可访问；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
26. [S16-R3-026] 在`解码测试`落实：lookahead尾部完整flush；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
27. [S16-R3-027] 在`解码测试`落实：flush幂等；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
28. [S16-R3-028] 在`解码测试`落实：取消丢尾部；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
29. [S16-R3-029] 在`解码测试`落实：非有限输出不得成功；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
30. [S16-R3-030] 在`解码测试`落实：错误采样率拒绝；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
31. [S16-R3-031] 在`RTF实验入口`落实：调用真实worker而非造测量；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
32. [S16-R3-032] 在`RTF实验入口`落实：用户显式启用目标机测试；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
33. [S16-R3-033] 在`RTF实验入口`落实：不启动第三模型；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
34. [S16-R3-034] 在`RTF实验入口`落实：仅读取既有档案；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
35. [S16-R3-035] 在`RTF实验入口`落实：保存生成WAV供试听；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
36. [S16-R3-036] 在`RTF实验入口`落实：报告不含口令；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
37. [S16-R3-037] 在`RTF实验入口`落实：至少三次重复；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
38. [S16-R3-038] 在`RTF实验入口`落实：测前确认双worker真实引擎；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
39. [S16-R3-039] 在`RTF实验入口`落实：未达0.3就failed而非pass；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
40. [S16-R3-040] 在`RTF实验入口`落实：没有CUDA明确blocked；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
41. [S16-R3-041] 在`现有服务`落实：完整Python三轮；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
42. [S16-R3-042] 在`现有服务`落实：Node三轮；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
43. [S16-R3-043] 在`现有服务`落实：Go race count3；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
44. [S16-R3-044] 在`现有服务`落实：完整Chromium三轮；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
45. [S16-R3-045] 在`现有服务`落实：协议生命周期三轮；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
46. [S16-R3-046] 在`现有服务`落实：真实Faster接口三轮；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
47. [S16-R3-047] 在`现有服务`落实：HF导入tinyMimi三轮；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
48. [S16-R3-048] 在`现有服务`落实：保留训练CPU等价门禁；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
49. [S16-R3-049] 在`现有服务`落实：不忽略失败测试；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。
50. [S16-R3-050] 在`现有服务`落实：修复后完整重跑；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。

追问结论：工程取舍已明确，不向用户重复提问；未提供真实音频与T4不能对声学或速度声称100%。


## 问题22：超过15秒录音为什么建档失败，如何修复且不伪造对齐？

具体选项：A删16秒限制后配整段全文；B保留音频/转写匹配，使用词级时间戳切分，缺失则短音频窗口真实重识别；C按字数比例分全文。

推荐：B。

详细回答：源码接收长录音，但候选仅取完整2.5–16秒ASR段，忽略已有words。一个28秒段因此无候选。B按完整词切分并验证词文一致；缺词时间不猜，重新ASR实际窗口。保留长音频完整分析，长manual全文不冒充逐字对齐。

进入下一题之前的50项实施建议：

1. [S17-R1-001] `截图与根因`：截图是15而非16不能当新包效果；以代码/测试收据或明确真实硬件门禁核查。
2. [S17-R1-002] `截图与根因`：录音限额与锚点限额分开；以代码/测试收据或明确真实硬件门禁核查。
3. [S17-R1-003] `截图与根因`：重现单个28.7秒ASR段；以代码/测试收据或明确真实硬件门禁核查。
4. [S17-R1-004] `截图与根因`：保留16的逐字匹配约束；以代码/测试收据或明确真实硬件门禁核查。
5. [S17-R1-005] `截图与根因`：不能将长音频硬截配全文；以代码/测试收据或明确真实硬件门禁核查。
6. [S17-R1-006] `截图与根因`：保留ASR词级时间戳；以代码/测试收据或明确真实硬件门禁核查。
7. [S17-R1-007] `截图与根因`：按完整词组而非字符比例切分；以代码/测试收据或明确真实硬件门禁核查。
8. [S17-R1-008] `截图与根因`：词与原段文本必须核对；以代码/测试收据或明确真实硬件门禁核查。
9. [S17-R1-009] `截图与根因`：缺词时间走音频窗口重新ASR；以代码/测试收据或明确真实硬件门禁核查。
10. [S17-R1-010] `截图与根因`：不能凭低RMS断定无人声；以代码/测试收据或明确真实硬件门禁核查。
11. [S17-R1-011] `词级对齐`：验证时间戳有限；以代码/测试收据或明确真实硬件门禁核查。
12. [S17-R1-012] `词级对齐`：验证起止单调；以代码/测试收据或明确真实硬件门禁核查。
13. [S17-R1-013] `词级对齐`：验证不越源音频；以代码/测试收据或明确真实硬件门禁核查。
14. [S17-R1-014] `词级对齐`：拒绝重叠倒序词；以代码/测试收据或明确真实硬件门禁核查。
15. [S17-R1-015] `词级对齐`：Unicode字母数字核对转写；以代码/测试收据或明确真实硬件门禁核查。
16. [S17-R1-016] `词级对齐`：不要丢标点后汉字；以代码/测试收据或明确真实硬件门禁核查。
17. [S17-R1-017] `词级对齐`：长单词超窗口重新ASR；以代码/测试收据或明确真实硬件门禁核查。
18. [S17-R1-018] `词级对齐`：短尾保留在分析收据；以代码/测试收据或明确真实硬件门禁核查。
19. [S17-R1-019] `词级对齐`：跨文件绝不合并文字；以代码/测试收据或明确真实硬件门禁核查。
20. [S17-R1-020] `词级对齐`：对齐失败有明确中文建议；以代码/测试收据或明确真实硬件门禁核查。
21. [S17-R1-021] `长音频重识别`：仅问题长段需要窗口ASR；以代码/测试收据或明确真实硬件门禁核查。
22. [S17-R1-022] `长音频重识别`：每窗口音频和转写独立匹配；以代码/测试收据或明确真实硬件门禁核查。
23. [S17-R1-023] `长音频重识别`：使用原音频实际切片；以代码/测试收据或明确真实硬件门禁核查。
24. [S17-R1-024] `长音频重识别`：偏移恢复绝对时间；以代码/测试收据或明确真实硬件门禁核查。
25. [S17-R1-025] `长音频重识别`：边界优先静音；以代码/测试收据或明确真实硬件门禁核查。
26. [S17-R1-026] `长音频重识别`：窗口必须前进不死循环；以代码/测试收据或明确真实硬件门禁核查。
27. [S17-R1-027] `长音频重识别`：最末窗口不丢；以代码/测试收据或明确真实硬件门禁核查。
28. [S17-R1-028] `长音频重识别`：无语音窗口不伪造文字；以代码/测试收据或明确真实硬件门禁核查。
29. [S17-R1-029] `长音频重识别`：沿用ASR锁及CPU复用；以代码/测试收据或明确真实硬件门禁核查。
30. [S17-R1-030] `长音频重识别`：进度显示窗口计数；以代码/测试收据或明确真实硬件门禁核查。
31. [S17-R1-031] `长参考语义`：长录音可以超过15秒；以代码/测试收据或明确真实硬件门禁核查。
32. [S17-R1-032] `长参考语义`：不能无限把20分钟塞进ICL；以代码/测试收据或明确真实硬件门禁核查。
33. [S17-R1-033] `长参考语义`：提供16与24秒参考窗口；以代码/测试收据或明确真实硬件门禁核查。
34. [S17-R1-034] `长参考语义`：默认16保护旧短样本；以代码/测试收据或明确真实硬件门禁核查。
35. [S17-R1-035] `长参考语义`：24明确标为实验与较慢；以代码/测试收据或明确真实硬件门禁核查。
36. [S17-R1-036] `长参考语义`：手工转写仅单短文件直接采用；以代码/测试收据或明确真实硬件门禁核查。
37. [S17-R1-037] `长参考语义`：长手工全文不能按时长分配；以代码/测试收据或明确真实硬件门禁核查。
38. [S17-R1-038] `长参考语义`：记录源总时长与选中锚点；以代码/测试收据或明确真实硬件门禁核查。
39. [S17-R1-039] `长参考语义`：记录重切分和重识别数量；以代码/测试收据或明确真实硬件门禁核查。
40. [S17-R1-040] `长参考语义`：明确建档不是全数据训练；以代码/测试收据或明确真实硬件门禁核查。
41. [S17-R1-041] `输入与安全`：窗口值只允许16或24；以代码/测试收据或明确真实硬件门禁核查。
42. [S17-R1-042] `输入与安全`：表单和库入口都独立校验；以代码/测试收据或明确真实硬件门禁核查。
43. [S17-R1-043] `输入与安全`：失败保留本地录音；以代码/测试收据或明确真实硬件门禁核查。
44. [S17-R1-044] `输入与安全`：取消不得删除源音频；以代码/测试收据或明确真实硬件门禁核查。
45. [S17-R1-045] `输入与安全`：不自动云传原音；以代码/测试收据或明确真实硬件门禁核查。
46. [S17-R1-046] `输入与安全`：拒绝非有限PCM；以代码/测试收据或明确真实硬件门禁核查。
47. [S17-R1-047] `输入与安全`：保留20分钟录音预算；以代码/测试收据或明确真实硬件门禁核查。
48. [S17-R1-048] `输入与安全`：低电平提示调整设备；以代码/测试收据或明确真实硬件门禁核查。
49. [S17-R1-049] `输入与安全`：提示麦克风距离不替人猜设备；以代码/测试收据或明确真实硬件门禁核查。
50. [S17-R1-050] `输入与安全`：保留原始至16冻结；以代码/测试收据或明确真实硬件门禁核查。

追问结论：方案边界明确，不向用户提问；未知的真实声学结果保留未知，不声称100%。


## 问题23：超长参考是否一定更像，怎样保证短参考与双卡条件一致？

具体选项：A无限参考整段进模型；B可选16/24秒锚点，长录音用于选择代表片段，指纹同时绑定四项采样参数；C混入参考原音增加相似。

推荐：B。

详细回答：更多同说话人干净录音有助选样，但参考上下文不是训练，不能保证长于短。默认ICL与匹配转写保持；新增24秒明确实验和延迟代价。四生成参数及参考内容共同绑定，防两卡不同修订；同条件也不保证硬件波形相同或100%音色。

进入下一题之前的50项实施建议：

1. [S17-R2-001] `短参考与音色`：继续使用ICL匹配文本；以代码/测试收据或明确真实硬件门禁核查。
2. [S17-R2-002] `短参考与音色`：不退回15纯向量默认；以代码/测试收据或明确真实硬件门禁核查。
3. [S17-R2-003] `短参考与音色`：新旧GPU不能混版本；以代码/测试收据或明确真实硬件门禁核查。
4. [S17-R2-004] `短参考与音色`：相同参考绑定采样参数；以代码/测试收据或明确真实硬件门禁核查。
5. [S17-R2-005] `短参考与音色`：Go和Python浮点编码一致；以代码/测试收据或明确真实硬件门禁核查。
6. [S17-R2-006] `短参考与音色`：缺省参数也计入指纹；以代码/测试收据或明确真实硬件门禁核查。
7. [S17-R2-007] `短参考与音色`：不接受NaN温度；以代码/测试收据或明确真实硬件门禁核查。
8. [S17-R2-008] `短参考与音色`：改温度使旧会话失效；以代码/测试收据或明确真实硬件门禁核查。
9. [S17-R2-009] `短参考与音色`：参数相同不是音色绝对相同；以代码/测试收据或明确真实硬件门禁核查。
10. [S17-R2-010] `短参考与音色`：真人试听仍是独立门禁；以代码/测试收据或明确真实硬件门禁核查。
11. [S17-R2-011] `多卡参数`：绑定temperature；以代码/测试收据或明确真实硬件门禁核查。
12. [S17-R2-012] `多卡参数`：绑定top_k；以代码/测试收据或明确真实硬件门禁核查。
13. [S17-R2-013] `多卡参数`：绑定top_p；以代码/测试收据或明确真实硬件门禁核查。
14. [S17-R2-014] `多卡参数`：绑定repetition_penalty；以代码/测试收据或明确真实硬件门禁核查。
15. [S17-R2-015] `多卡参数`：top_k必须整数；以代码/测试收据或明确真实硬件门禁核查。
16. [S17-R2-016] `多卡参数`：统一默认参数数值；以代码/测试收据或明确真实硬件门禁核查。
17. [S17-R2-017] `多卡参数`：每次合成锁内复核；以代码/测试收据或明确真实硬件门禁核查。
18. [S17-R2-018] `多卡参数`：预计算提示快照保留；以代码/测试收据或明确真实硬件门禁核查。
19. [S17-R2-019] `多卡参数`：不混用不同条件模式；以代码/测试收据或明确真实硬件门禁核查。
20. [S17-R2-020] `多卡参数`：不声称两卡波形逐位相同；以代码/测试收据或明确真实硬件门禁核查。
21. [S17-R2-021] `参考质量`：记录原始RMS；以代码/测试收据或明确真实硬件门禁核查。
22. [S17-R2-022] `参考质量`：记录原始峰值；以代码/测试收据或明确真实硬件门禁核查。
23. [S17-R2-023] `参考质量`：记录SNR估计而非真值；以代码/测试收据或明确真实硬件门禁核查。
24. [S17-R2-024] `参考质量`：低电平给风险提示不直接拒绝；以代码/测试收据或明确真实硬件门禁核查。
25. [S17-R2-025] `参考质量`：响度归一化不是降噪；以代码/测试收据或明确真实硬件门禁核查。
26. [S17-R2-026] `参考质量`：MFCC相似不是可靠声纹真值；以代码/测试收据或明确真实硬件门禁核查。
27. [S17-R2-027] `参考质量`：避免强降噪损伤辅音；以代码/测试收据或明确真实硬件门禁核查。
28. [S17-R2-028] `参考质量`：参考多人必须审核；以代码/测试收据或明确真实硬件门禁核查。
29. [S17-R2-029] `参考质量`：24秒未必比10秒好；以代码/测试收据或明确真实硬件门禁核查。
30. [S17-R2-030] `参考质量`：不播放原录音补相似度；以代码/测试收据或明确真实硬件门禁核查。
31. [S17-R2-031] `连续朗读`：只调整朗读聚合不延后聊天首句；以代码/测试收据或明确真实硬件门禁核查。
32. [S17-R2-032] `连续朗读`：减少过多独立合成语段；以代码/测试收据或明确真实硬件门禁核查。
33. [S17-R2-033] `连续朗读`：优先完整句子标点；以代码/测试收据或明确真实硬件门禁核查。
34. [S17-R2-034] `连续朗读`：保留原始全文字符；以代码/测试收据或明确真实硬件门禁核查。
35. [S17-R2-035] `连续朗读`：不合并不同用户任务；以代码/测试收据或明确真实硬件门禁核查。
36. [S17-R2-036] `连续朗读`：保留取消和背压；以代码/测试收据或明确真实硬件门禁核查。
37. [S17-R2-037] `连续朗读`：不跨词叠加PCM；以代码/测试收据或明确真实硬件门禁核查。
38. [S17-R2-038] `连续朗读`：不删除语音以隐藏接缝；以代码/测试收据或明确真实硬件门禁核查。
39. [S17-R2-039] `连续朗读`：保留已有codec有界上下文；以代码/测试收据或明确真实硬件门禁核查。
40. [S17-R2-040] `连续朗读`：自然韵律不能仅靠交叉淡化保证；以代码/测试收据或明确真实硬件门禁核查。
41. [S17-R2-041] `噪声边界`：继续禁参考呼吸拼接；以代码/测试收据或明确真实硬件门禁核查。
42. [S17-R2-042] `噪声边界`：不生成白噪声补停顿；以代码/测试收据或明确真实硬件门禁核查。
43. [S17-R2-043] `噪声边界`：保留软限幅；以代码/测试收据或明确真实硬件门禁核查。
44. [S17-R2-044] `噪声边界`：保留可控增益；以代码/测试收据或明确真实硬件门禁核查。
45. [S17-R2-045] `噪声边界`：不把静音当去噪成功；以代码/测试收据或明确真实硬件门禁核查。
46. [S17-R2-046] `噪声边界`：不默认低通抹齿音；以代码/测试收据或明确真实硬件门禁核查。
47. [S17-R2-047] `噪声边界`：新统计不得泄漏原文本；以代码/测试收据或明确真实硬件门禁核查。
48. [S17-R2-048] `噪声边界`：生成WAV可供独立试听；以代码/测试收据或明确真实硬件门禁核查。
49. [S17-R2-049] `噪声边界`：缺真实音频不宣布零噪声；以代码/测试收据或明确真实硬件门禁核查。
50. [S17-R2-050] `噪声边界`：不得缩短输出冒RTF达标；以代码/测试收据或明确真实硬件门禁核查。

追问结论：方案边界明确，不向用户提问；未知的真实声学结果保留未知，不声称100%。


## 问题24：如何自然连续朗读、排查沙沙声并诚实验收？

具体选项：A强低通加跨词重叠；B适度增大只读文本聚合、保留正文/取消/codec，参考质量提示与真实双卡WAV验收；C静音或删字冒无噪声。

推荐：B。

详细回答：减少独立语段可降低重启韵律次数，但不声称等同整段联合生成。保留聊天第一句早提交，不跨词叠加PCM。记录低输入电平而不从截图猜设备；强降噪会损伤音色，不无证据默认开启。三轮工程/实际库控制实验外，训练权重试听和T4 RTF仍需真实硬件。

进入下一题之前的50项实施建议：

1. [S17-R3-001] `重现门禁`：单个28.7秒词级段建档成功；以代码/测试收据或明确真实硬件门禁核查。
2. [S17-R3-002] `重现门禁`：单个60秒段词级切分；以代码/测试收据或明确真实硬件门禁核查。
3. [S17-R3-003] `重现门禁`：20分钟时间戳规划有界；以代码/测试收据或明确真实硬件门禁核查。
4. [S17-R3-004] `重现门禁`：缺词时间戳实际窗口重识别；以代码/测试收据或明确真实硬件门禁核查。
5. [S17-R3-005] `重现门禁`：文本不匹配必须回识别；以代码/测试收据或明确真实硬件门禁核查。
6. [S17-R3-006] `重现门禁`：长manual全文不错误拼接；以代码/测试收据或明确真实硬件门禁核查。
7. [S17-R3-007] `重现门禁`：短manual16秒保持兼容；以代码/测试收据或明确真实硬件门禁核查。
8. [S17-R3-008] `重现门禁`：24秒锚点不越界；以代码/测试收据或明确真实硬件门禁核查。
9. [S17-R3-009] `重现门禁`：无声和非法时间戳不造成功；以代码/测试收据或明确真实硬件门禁核查。
10. [S17-R3-010] `重现门禁`：每项做三轮回归；以代码/测试收据或明确真实硬件门禁核查。
11. [S17-R3-011] `接口门禁`：浏览器发送参考窗口字段；以代码/测试收据或明确真实硬件门禁核查。
12. [S17-R3-012] `接口门禁`：默认值16可见；以代码/测试收据或明确真实硬件门禁核查。
13. [S17-R3-013] `接口门禁`：24选项真实进入后端；以代码/测试收据或明确真实硬件门禁核查。
14. [S17-R3-014] `接口门禁`：锁定清除私有转写；以代码/测试收据或明确真实硬件门禁核查。
15. [S17-R3-015] `接口门禁`：表单非法值拒绝；以代码/测试收据或明确真实硬件门禁核查。
16. [S17-R3-016] `接口门禁`：库处理同样校验；以代码/测试收据或明确真实硬件门禁核查。
17. [S17-R3-017] `接口门禁`：服务重启新包版本可识别；以代码/测试收据或明确真实硬件门禁核查。
18. [S17-R3-018] `接口门禁`：新包逐字节复制；以代码/测试收据或明确真实硬件门禁核查。
19. [S17-R3-019] `接口门禁`：16包哈希冻结；以代码/测试收据或明确真实硬件门禁核查。
20. [S17-R3-020] `接口门禁`：正式工作台保持不变；以代码/测试收据或明确真实硬件门禁核查。
21. [S17-R3-021] `参数指纹测试`：中英转写跨语言一致；以代码/测试收据或明确真实硬件门禁核查。
22. [S17-R3-022] `参数指纹测试`：默认值与显式默认相同；以代码/测试收据或明确真实硬件门禁核查。
23. [S17-R3-023] `参数指纹测试`：四参数分别变更使pin变化；以代码/测试收据或明确真实硬件门禁核查。
24. [S17-R3-024] `参数指纹测试`：NaN和无穷拒绝；以代码/测试收据或明确真实硬件门禁核查。
25. [S17-R3-025] `参数指纹测试`：非整数top_k拒绝；以代码/测试收据或明确真实硬件门禁核查。
26. [S17-R3-026] `参数指纹测试`：Worker不输出不符pin的PCM；以代码/测试收据或明确真实硬件门禁核查。
27. [S17-R3-027] `参数指纹测试`：Go协议携带固定pin；以代码/测试收据或明确真实硬件门禁核查。
28. [S17-R3-028] `参数指纹测试`：不改adapter来源绑定；以代码/测试收据或明确真实硬件门禁核查。
29. [S17-R3-029] `参数指纹测试`：新旧包混跑明确重启；以代码/测试收据或明确真实硬件门禁核查。
30. [S17-R3-030] `参数指纹测试`：不把指纹当身份认证；以代码/测试收据或明确真实硬件门禁核查。
31. [S17-R3-031] `验证与实验`：Python完整三轮；以代码/测试收据或明确真实硬件门禁核查。
32. [S17-R3-032] `验证与实验`：Node完整三轮；以代码/测试收据或明确真实硬件门禁核查。
33. [S17-R3-033] `验证与实验`：Go race三轮；以代码/测试收据或明确真实硬件门禁核查。
34. [S17-R3-034] `验证与实验`：Chromium完整三轮；以代码/测试收据或明确真实硬件门禁核查。
35. [S17-R3-035] `验证与实验`：六服务协议各三轮；以代码/测试收据或明确真实硬件门禁核查。
36. [S17-R3-036] `验证与实验`：实际Faster控制接口三轮；以代码/测试收据或明确真实硬件门禁核查。
37. [S17-R3-037] `验证与实验`：真实tiny codec三轮；以代码/测试收据或明确真实硬件门禁核查。
38. [S17-R3-038] `验证与实验`：Mimi导入重载三轮；以代码/测试收据或明确真实硬件门禁核查。
39. [S17-R3-039] `验证与实验`：CPU训练等价三轮；以代码/测试收据或明确真实硬件门禁核查。
40. [S17-R3-040] `验证与实验`：所有CPU模型明确不是Qwen音质证据；以代码/测试收据或明确真实硬件门禁核查。
41. [S17-R3-041] `记录与交付`：问题22回答后给50建议；以代码/测试收据或明确真实硬件门禁核查。
42. [S17-R3-042] `记录与交付`：问题23回答后给50建议；以代码/测试收据或明确真实硬件门禁核查。
43. [S17-R3-043] `记录与交付`：问题24回答后给50建议；以代码/测试收据或明确真实硬件门禁核查。
44. [S17-R3-044] `记录与交付`：方案先于产品修改；以代码/测试收据或明确真实硬件门禁核查。
45. [S17-R3-045] `记录与交付`：每次失败日志保留；以代码/测试收据或明确真实硬件门禁核查。
46. [S17-R3-046] `记录与交付`：逐条300建议分类；以代码/测试收据或明确真实硬件门禁核查。
47. [S17-R3-047] `记录与交付`：无硬件保留BLOCKED；以代码/测试收据或明确真实硬件门禁核查。
48. [S17-R3-048] `记录与交付`：真实RTF0.3仍需测量；以代码/测试收据或明确真实硬件门禁核查。
49. [S17-R3-049] `记录与交付`：完整57份备忘录内嵌；以代码/测试收据或明确真实硬件门禁核查。
50. [S17-R3-050] `记录与交付`：不承诺100相似零噪声；以代码/测试收据或明确真实硬件门禁核查。

追问结论：方案边界明确，不向用户提问；未知的真实声学结果保留未知，不声称100%。

---

## 内嵌备忘录：KAGGLE_SECURITY_PLAN.md

# 下一阶段执行门禁：访问控制与资源预算

日期：2026-10-21。继续保留首轮包和原始kaggle，输出独立step2包。

## 本阶段确定范围

1. 所有 `/api` 入口必须验证内存Bearer口令，未配置则拒绝启动，不设免认证旁路；页面静态骨架可公开，声音/指标/收费接口不得匿名访问。
2. Kaggle启动器优先读取 `QTTS_ACCESS_TOKEN` Secret/环境变量，否则在 /tmp 的0700私有认证目录创建0600随机口令文件（默认不进入Notebook输出或声音库导出）；不在URL、日志或浏览器存储中放口令。健康探针与命令行工具同步适配。
3. 浏览器显式解锁/锁定；只在当前内存使用口令，同源请求注入认证，不把口令发送给外部网关地址。
4. 网关限制JSON/上传总字节、文本/历史长度、请求频率、并发会话和昂贵操作；有界请求超时；代理不把口令或DeepSeek Key传给分析服务。
5. 分析服务在multipart解析前限制请求体；文件数量/单文件/总量/空文件限制；只接受有界后台构建，清理终态任务记录，限制解码时长和累计时长。超限必须明确拒绝，不静默截断。
6. 暂不把本版称为完整互联网多租户系统：共享单用户口令、不含账号体系/审计平台，TLS依赖可信代理；OS级磁盘配额/解码器隔离/全局worker队列专项仍需后续。

## 验证门禁

- Go httptest + `-race -count=3`：匿名/错误/正确口令、缺配置、非API静态白名单、请求大小、限流/并发/超时、代理密钥剥离、严格JSON与文本预算。
- Python：口令创建/权限/复用与弱配置拒绝；ASGI未知长度请求体超限；上传数量/尺寸/空文件、忙碌拒绝和失败释放；解码时长边界。
- Chromium：解锁、错误口令、锁定取消、不持久化口令、拒绝向外域发口令；保留首轮播放竞态用例。
- 三轮受认证的真实Go网关+双Mock worker协议回归；完整工作台和实际step2代码复制回归。
- 重打包确定性、所有资产逐字节仅解包对比；保留原始文件和step1。

GPU训练、真实DeepSeek/音质/性能验收不在上述Mock验证结论内。验收不通过则修复再跑，不以跳过或改小模型宣称成功。

---

## 内嵌备忘录：KAGGLE_SOURCE_AUDIT.md

# Kaggle 原始源码：首批修复与验证报告

> 历史首轮报告：当前源码已推进到step10，以下行号和统计对应冻结的 `kaggle-fixed-step1.py`。当前修复与边界以 `KAGGLE_STEP10_AUDIT.md` 为准；重打包器现默认生成step10。

更新日期：2026-10-21。**阶段：已收到源码并完成首批可靠性修复；不是完整GPU产品验收。**

## 1. 原文件与导出

- 原始 `kaggle`：127241字节，SHA256 `26c31621d6265bc25370bc284f2afdcf52f5edaf97e64056c2d8d5eda4a6c461`；保存在工作台正式快照，未覆盖。
- 静态解析FILES字面量，Base64严格校验、zlib解码、原22项内嵌哈希全部匹配；没有执行原启动/安装器。
- 可读源码：`kaggle/source/`。现有架构是Python＋Go＋可选Rust＋已编译JavaScript，不是纯Python单脚本。
- 修复版：`kaggle/kaggle-fixed-step1.py`，134879字节；23项资产（原22项＋Go可靠性测试）。
- 清单：`kaggle/source_manifest.json`，包含每项新旧SHA256和变更标记。
- 重打包器：`kaggle/repack.py`，只解析，不导入/运行原始启动文件；`--check`验证生成文件未过期。
- 导出是**首轮修复包**，不是“已在Kaggle全部运行成功”的最终版；运行会安装依赖、下载模型并可启动隧道，使用前阅读限制。

## 2. 有证据的首批修复

下表是21类修复/交付加固，**不等于300个缺陷或300项验收**。源码位置是当前修复版行号；部分设备依赖只完成源码与协议检查，已在证据栏注明。

| ID | 已确认问题 | 当前源码位置 | 处理 | 证据/边界 |
|---|---|---|---|---|
| A01 | T4可能错误回退BF16；FP32默认扩大显存风险 | `kaggle/source/py/worker.py:173` | 计算能力+支持探测；FP32显式允许 | dtype及模拟BF16支持测试 |
| A02 | 安装器仅在读到日志时检查超时，静默进程可挂住 | `kaggle/source/py/bootstrap.py:49` | 独立定时器终止子进程组 | 静默子进程0.2秒超时/退出码测试 |
| A03 | 并发JSON写入共享.tmp文件，相互覆盖/重命名失败 | `kaggle/source/py/qtts_common.py:104` | 唯一同目录临时文件、fsync、replace、清理 | 80次并发写入测试 |
| A04 | 恢复tar只过滤文件名，允许链接/设备，且新filter参数不兼容当前Python | `kaggle/source/py/qtts_common.py:164` | 先整包验证，再仅提取文件/目录，拒绝已有逃逸链接 | 穿越/软硬链接/已有链接/正常恢复测试 |
| A05 | Go声音ID可用于不受约束的路径拼接 | `kaggle/source/go/gateway/session.go:43` | 安全ID白名单及档案内外ID一致性 | 路径穿越与ID不一致测试 |
| A06 | worker尚未确认就提交active.json，失败也报成功 | `kaggle/source/go/gateway/main.go:244` | POST+串行；两worker确认；唯一临时文件；检查保存错误 | HTTP失败/拒绝/坏JSON/成功/无worker/方法测试 |
| A07 | LLM预算1200 tokens且默认200字限制，长输出被人为限制 | `kaggle/source/go/gateway/main.go:53` | 默认8192，可配置且校验范围；去掉200字限制 | 请求预算转发/配置边界测试；真实供应商限制待验 |
| A08 | 忽略finish_reason、错误JSON与未完成EOF | `kaggle/source/go/gateway/llm.go:61` | 明确报截断/供应商错误，不自动重复请求 | 正常DONE/stop、length、坏JSON、空/断流等7类HTTP流测试 |
| A09 | 旧请求迟到响应/PCM/finally会污染新一轮 | `kaggle/source/web/app.js:521` | 单调轮次所有权；Stop使旧轮次失效；await后检查 | 迟到响应头/迟到body及新流不被end的浏览器用例 |
| A10 | 音频初始化重入可能早发请求/丢PCM，失败形成未处理拒绝 | `kaggle/source/web/app.js:183` | 共享初始化Promise；失败复位并显示错误 | 重叠初始化、初始化失败、初始化期间停止用例 |
| A11 | DeepSeek密钥长期保存localStorage | `kaggle/source/web/app.js:1070` | 清理旧键，不回填/写入新键 | 浏览器旧键迁移与新键只入请求头测试 |
| A12 | 通配CORS允许任意网站读取/调用网关 | `kaggle/source/go/gateway/main.go:335` | 只接受同Origin；移除通配和私网跨域许可 | 同源/跨源/opaque/无Origin测试；仍不是身份认证 |
| A13 | Whisper默认占用第二张GPU，与TTS模型争显存 | `kaggle/source/py/analyst.py:253` | 默认CPU int8，GPU须显式选择 | 源码/编译检查；真实ASR未运行 |
| A14 | 65..95采样点呼吸片段的固定96点淡化会广播失败 | `kaggle/source/py/worker.py:393` | 淡化窗口随片段长度限制 | 65点真实数组单元测试 |
| A15 | NumPy卷积same对64..479点块返回480点导致长度异常 | `kaggle/source/py/audio_rt.py:152` | 改成有状态一阶去直流，保持块长度 | 0..24000采样点多种长度、类型与有限性测试 |
| A16 | 取消在成功拿到锁的瞬间到达，仍会启动旧合成 | `kaggle/source/py/worker.py:419` | 拿锁后再次检查取消，finally仍释放锁并终结协议 | 确定性取消-at-acquisition单测＋HTTP关闭后恢复模拟 |
| A17 | 模型返回非24kHz时仍按固定24kHz PCM发送 | `kaggle/source/py/worker.py:298` | 显式拒绝不兼容采样率，不假装正常播放 | 22050Hz模型返回契约模拟测试 |
| A18 | 自检缺少资源的SKIP被计成PASS | `kaggle/source/tools/selftest.py:39` | 三态记录；缺资源退出码2，失败退出码1 | 无声音档案明确SKIP单元测试 |
| A19 | 空e2e数据的all(empty)可误通过，首声None格式化崩溃 | `kaggle/source/tools/e2e_check.py:143` | 要求非空段和音频；未开始播放显示inf | 空流稳定失败、非格式崩溃单元测试 |
| A20 | 速度倍率rtf_x被UI标成标准RTF，容易倒置目标 | `kaggle/source/py/worker.py:474` | 新增耗时/时长RTF字段；保留原倍速字段和调度算法 | 双Mock管线统计字段校验；UI编译及浏览器回归 |
| A21 | 修复资产无法复现单文件分发，父启动器失败只打印不传播 | `kaggle/repack.py:35` | 独立新文件、全SHA256校验、仅解包模式、传播子进程退出码 | 确定性打包/23资产逐字节解包/原文件不变测试；实机失败传播待验 |


## 3. 本轮真实执行结果

| 检查 | 结果 | 日志 |
|---|---|---|
| Python可靠性＋打包单元测试 | **18/18通过**；包含故意缺资源的SKIP语义断言，不是GPU自检完成 | `docs/validation/qtts-python.txt` |
| Go单元、httptest、SSE、竞态 | **14个顶层测试**（含表驱动场景），`-race -count=3`通过 | `docs/validation/qtts-go-race3.txt` |
| 浏览器全部回归 | **47/47通过**＝原工作台40＋QTTS6＋实际修复包复制1 | `docs/validation/browser-all.txt` |
| QTTS专项浏览器重复3遍 | **18/18通过**；HTTP和Web Audio均为明确Mock | `docs/validation/qtts-browser-repeat3.txt` |
| 真实Go网关＋2个Mock Python worker | **三轮通过**；有序帧、文本完整、两worker参与、中断恢复、模拟零欠载 | `docs/validation/qtts-mock-pipeline.txt` |
| 工作台HTTP/API/存储 | **30/30通过**，临时目录，不修改正式工作区 | `docs/validation/workbench-api.txt` |
| JS语法、Python编译、重打包一致性 | 通过 | `docs/validation/workbench-syntax.txt`、单测日志 |

测试途中确实复现并修复短块处理和旧版Python tar参数不兼容。浏览器首次失败来自测试档案漏填breath_files，补齐真实接口字段后通过，未以修改生产逻辑掩盖无效夹具。
新取消测试最初误以为取消后不会返回统计帧；实际协议finally需要统计＋终结，已改为断言无PCM/无合成而保留终结协议。

**三轮是CPU/协议模拟，不是三轮真实GPU、训练、ASR、DeepSeek和人耳验收。Rust本轮没有重新编译；本地走NumPy路径。**

## 4. 保留的现有行为

- 原始文件及历史快照、工作台自命名空白文件/粘贴/保存/冲突/沙箱/原文复制均保留。
- 原切段器7项测试保留；双worker并行、有序汇聚、水位、失败改派逻辑未重写。
- 原声音库/多参考上传/参考缓存、校准、呼吸库/响度处理和监控保留入口；真实模型相关功能不能因入口存在就宣称实机通过。
- ASR默认改CPU、单卡须显式允许、跨域请求拒绝和密钥不再本地持久化是有意的安全/资源行为变化。

## 5. 尚未闭环的高优先级项目

1. **训练仍未实现**：原源码没有优化器/反向传播/双rank作业/训练检查点。本轮没有把prompt缓存改名为训练。后续需验证官方单说话人路径、T4兼容参数高效训练、world_size=2、样本覆盖、梯度与重载。
2. **没有真实GPU/model/API**：未运行真实Qwen、Whisper、ECAPA或DeepSeek。T4显存、第三方流式后端API、SDPA/精度/图捕获、真实长流token上限待验。
3. **性能/音质目标未达成可确认状态**：首声<3s、RTF≤0.5、99.5%相似度均无实测证据。`rtf_x`不是标准RTF；模型首chunk不等于耳朵听到的首声。
4. **公网认证未实现**：同Origin检查不是登录、不是防DNS rebinding，也不会阻止无Origin脚本/CLI。旧自动隧道逻辑仍在，需访问控制/配额后再公开；可设 `QTTS_TUNNEL=none` 禁用隧道。
5. **依赖/下载未锁定**：GPU依赖安装、第三方模型revision、Go/Rust工具下载及哈希策略待完善。`requirements-test.txt`仅固定本地CPU测试直接依赖，不是GPU安装锁。
6. **UI要求未完成**：原三标签页仍保留；两主视图、真实录音波形、样本选择与训练任务UI待做，不能把现有录音按钮算作完整波形实现。
7. **并发/容量专项仍需做**：上传大小/数量、队列上限、profile重载与任务共享状态、supervisor重启竞态、持续故障和断网恢复；激活的取消上下文/持久化故障等还需更细粒度测试。
8. **不能保证Kaggle永久在线**：会话/显存随平台停止而丢失，Dataset保存只处理资产恢复。

## 6. 可复现命令

仓库根目录，CPU测试环境（不安装torch/模型，不执行bootstrap）：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r kaggle/requirements-test.txt
npm ci
python3 kaggle/repack.py --check
.venv/bin/python -m unittest discover -s kaggle/tests -v
(cd kaggle/source/go/gateway && ../../../../.venv/bin/go test -race -count=3 -v ./...)
.venv/bin/python kaggle/tests/mock_pipeline.py
npm run check
npm test
npm run test:e2e
npm run test:e2e -- tests/browser/qtts.spec.js --repeat-each=3
```

只解包，**不会安装、读Secrets或启动服务**（目录可换成临时目录）：

```bash
QTTS_UNPACK_ONLY=1 QTTS_ROOT=/tmp/qtts-inspect python3 kaggle/kaggle-fixed-step1.py
```

修改任何asset后先 `python3 kaggle/repack.py` 再测试；原始已保存文件始终保留。测试使用临时目录和端口，正式workspace不会被回归用例替换。

## 7. 下一步顺序

先处理公网访问控制、资源限额与可复现依赖/后端兼容探针；再完成两主视图和真实录音波形；训练作为独立真实作业实现，不抢用未释放的双推理副本。具备GPU后执行单卡最小实验、双卡rank/检查点验证、真实DeepSeek和浏览器播放计时。

三轮各100项清单仍是逐项审查计划，当前仅源码交接前5项已勾选；不能用本报告21类修复或测试数量替代完整300项验收。3个历史专业问题每题50条建议保持在KAGGLE_DECISIONS.md，源码已到齐，不再重复索取。

---

## 内嵌备忘录：KAGGLE_SECURITY_AUDIT.md

> 冻结历史阶段证据；当前源码/重打包入口为step10，见KAGGLE_STEP10_AUDIT.md。下列原统计只描述当时交付，训练输入准备与训练执行不得混同。

# 第二阶段：访问控制与资源预算审查报告

日期：2026-10-21。**当前阶段已经实现并本地回归；不代表真实GPU产品验收。**

## 1. 本阶段交付与不可变基线

- 当前启动包：`kaggle/kaggle-fixed-step2.py`，155719字节、27项资产。
- 当前SHA256：`a628d1bf3f320a330d9206b5f1864e4b38a04f0bc04b26028af2e94368f111d0`；资产清单 `kaggle/source_manifest_step2.json`。
- 原始 `kaggle` 的SHA256仍为 `26c31621d6265bc25370bc284f2afdcf52f5edaf97e64056c2d8d5eda4a6c461`，原22项内嵌哈希验证通过。
- `kaggle-fixed-step1.py` 冻结保留，SHA256 `02e9bb45a14f1e168badc8f897cead0ddd7e70c884d7fd26382c9a5b49778007`；首轮清单 `source_manifest.json`不覆盖。
- `repack.py`当前生成step2；确定性比较和仅解包逐字节验证通过。原始安装器未被执行。

## 2. 处理项与对应证据

| ID | 问题 | 当前源码位置 | 处理 | 验证边界 |
|---|---|---|---|---|
| S01 | 匿名可读声音库、指标或调用收费入口 | `kaggle/source/go/gateway/security.go:108` | 所有API统一Bearer校验；缺配置不启动；失败尝试有独立预算 | Go认证/路由/失败预算测试，Mock管线匿名401 |
| S02 | 浏览器缺少解锁/锁定和凭据生命周期 | `kaggle/source/web/app.js:399` | 显式解锁，内存口令，锁定取消请求/播放/录音并清空视图 | 9个QTTS浏览器用例，专项重复3遍 |
| S03 | 跨域网关字段可能向外站发送凭据 | `kaggle/source/web/app.js:437` | 同源强校验；网关地址只读；不使用URL凭据、Cookie或浏览器存储 | 浏览器同源header/只读/刷新锁定测试；服务端Origin检查保留 |
| S04 | 自动生成凭据可能随Notebook输出导出 | `kaggle/source/py/access_control.py:16` | 默认/tmp中状态隔离的0700目录、0600文件；拒绝弱格式/链接；不打印口令 | 并发创建、复用、权限、错误配置、目录外置测试 |
| S05 | 健康探针/工具可能因认证失效，或把凭据转发模型服务 | `kaggle/source/py/access_control.py:65` | 仅本机网关探针附带口令；CLI从环境或私有目录读取 | 探针端口/域名白名单测试，受认证Mock管线 |
| S06 | 分析代理和模型进程不必要持有网关/供应商凭据 | `kaggle/source/go/gateway/main.go:348` | 剥离Authorization/代理授权/Cookie/DeepSeek Key；子进程只继承所需凭据 | 真实httptest代理与child_environment单元测试 |
| S07 | 大JSON/尾随垃圾/未知长度体绕过容量判断 | `kaggle/source/go/gateway/security.go:195` | MaxBytesReader、已知长度预检、单个JSON完整消费 | 已知/未知长度、额外JSON、垃圾与空白超限测试 |
| S08 | 并发长流/昂贵请求和频繁请求无统一准入 | `kaggle/source/go/gateway/security.go:141` | 语音与昂贵请求独立非等待并发槽；令牌桶、有限上下文期限 | 并发拒绝/槽释放/频率/超时/取消测试 |
| S09 | 长文本/历史/一致性评估列表可放大工作量 | `kaggle/source/go/gateway/security.go:225` | 文本与历史字符预算、角色检查；一致性至多6段/段200字/总1000字 | Unicode字符、历史/系统预算、评估文本预算测试 |
| S10 | multipart解析前不受上传容量约束 | `kaggle/source/py/resource_limits.py:64` | 先有界暂存，最多1MiB驻留内存，其余临时磁盘；超限不进入应用解析 | 未知长度与已知长度ASGI测试，边界与坏Content-Length |
| S11 | 无限读取文件、空文件、多文件或积压后台线程 | `kaggle/source/py/analyst.py:882` | 分块读取、数量/单个/总字节限制；后台构建仅1个，忙则429 | 文件过多/空/超限/空名称/忙碌/启动失败及释放测试 |
| S12 | 终态任务记录和声音库数量无界 | `kaggle/source/py/resource_limits.py:111` | 终态淘汰、64条记录、128声音默认限额；低于256MiB空闲拒绝创建 | 记录淘汰、声音数量、磁盘预算测试；不是OS级配额 |
| S13 | 客户端取消时提前释放仍在执行的线程名额 | `kaggle/source/py/resource_limits.py:143` | 分析名额保留到线程实际结束，取消等待者不提前释放 | 确定性取消后仍拒绝新工作，真正结束后恢复的测试 |
| S14 | 先完整解码再截断可能耗尽内存/隐藏丢样本 | `kaggle/source/py/analyst.py:51` | ffmpeg解码期限+输出时长+pipe协议白名单+2线程；soundfile先检查元数据；超时长拒绝 | 模拟ffmpeg契约、真实soundfile WAV正常/超长、累计时长测试；无ffmpeg实测 |
| S15 | 首轮bootstrap安全解包函数未显式导入 | `kaggle/source/py/bootstrap.py:37` | 修复符号导入，保留安全解包实现 | bootstrap导入可调用测试；没有执行未知安装器 |


## 3. 默认资源预算与行为变化

| 项目 | 默认值 | 配置/备注 |
|---|---|---|
| 访问凭据 | 32..256位非空格可打印ASCII；应使用强随机值 | `QTTS_ACCESS_TOKEN`；不提供免认证开关 |
| JSON请求体 | 1MiB | `QTTS_MAX_JSON_BYTES`，网关允许1024..4MiB；分析服务另有1MiB上限，实际采用更严格一侧 |
| 单次上传请求体 | 64MiB，包括multipart开销 | `QTTS_MAX_UPLOAD_BYTES`，最大512MiB |
| 文件数量/单文件大小 | 16段 / 20MiB | `QTTS_MAX_UPLOAD_FILES` / `QTTS_MAX_FILE_BYTES`，最大64段 / 128MiB |
| 解码时长 | 单文件240秒，累计900秒 | `QTTS_MAX_AUDIO_SECONDS` / `QTTS_MAX_TOTAL_AUDIO_SECONDS`；超限失败，不把截断后的数据算成功 |
| 声音库/任务记录 | 128个 / 保留64条 | `QTTS_MAX_PROFILES` / `QTTS_MAX_JOB_RECORDS`；终态淘汰后旧任务ID可能404 |
| 最低空闲磁盘 | 256MiB | 创建前预检；不是全盘硬配额 |
| 并发语音/昂贵HTTP操作 | 2 / 2 | `QTTS_MAX_SPEAK_CONCURRENT` / `QTTS_MAX_HEAVY_CONCURRENT`；拒绝等待队列，429＋Retry-After |
| 实际分析线程/构建 | 2 / 1 | 分析槽跨HTTP取消仍保留到线程结束；构建忙直接429 |
| 语音请求令牌桶 | 初始容量12，每分钟补充12 | `QTTS_SPEAK_PER_MINUTE`；不是严格滚动窗口“每分钟只能12次” |
| 一般API令牌桶 | 初始容量120，每秒补充20 | 进程级、共享单用户预算，不按IP分配无界map |
| 无效口令尝试 | 初始容量10，每秒补充1 | 耗尽返回429；不会把正确口令一起锁死 |
| 单次文本/历史 | 文本20000字符；历史16条/累计32000字符；系统提示4096字符 | `QTTS_MAX_TEXT_CHARS`、`QTTS_MAX_HISTORY_CHARS`；字符不是UTF-8字节 |
| 请求上下文期限 | 1800秒 | `QTTS_REQUEST_TIMEOUT_S`，1..7200秒；HTTP读请求另限120秒 |

静态页面骨架无需口令；所有 `/api` 路径（包括health/metrics/profiles/prep和未知API）都在统一认证边界内。API OPTIONS可响应同源预检但不会返回私密数据。非API静态文件仅允许首页与app.js，不开放目录浏览。

原来“在任意网站填写外部网关地址”的方式被有意移除：请直接打开目标网关自己的HTTPS网址。默认限额和新的显式拒绝取代原来的静默截断/无界排队，是有意且已说明的行为变化。

## 4. 如何使用口令

**推荐**在Kaggle Secrets中配置独立的强随机 `QTTS_ACCESS_TOKEN`，与DeepSeek Key分开。启动器只输出Secret名称是否加载，不输出其值。

没有配置时，由启动器在 `/tmp/qtts-auth-<用户ID>-<状态路径摘要>/` 创建0700目录和0600的 `.access-token`。此目录默认不在 `/kaggle/working` 或声音Dataset中，重启应用可复用，同一Kaggle会话销毁后需要新口令。`QTTS_AUTH_DIR`可覆盖位置，但不要指向Notebook公开输出目录或声音库。

启动日志仅给出文件路径。在**私人且不分享的Notebook**内读取后粘贴到网页“访问口令→解锁”。不要把口令放进URL、工作台代码文件、聊天或公开Notebook输出；查看后清除可能含口令的Notebook输出。浏览器刷新后需重新解锁，锁定会停止播放/录音并清空私密视图。

本地CLI工具自动从环境变量或相同私有目录读取访问口令。可用以下方式在可信Notebook中取得变量（示例本身不打印凭据）：

```python
import os, sys
from pathlib import Path
sys.path.insert(0, "/kaggle/working/qtts/py")
from access_control import auth_directory, load_access_token
state = Path(os.environ.get("QTTS_STATE", "/kaggle/working/qtts/state"))
private_token = load_access_token(auth_directory(state))
# 仅在私人环境查看并复制该变量，用后清除输出；不要公开保存。
```

Bearer必须经可信HTTPS代理传输。直连网关的HTTP仅用于可信本机探针；不要在公网明文HTTP中传口令。TLS不由本应用自动签发。

## 5. 实际验证结果

| 检查 | 结果 | 日志 |
|---|---|---|
| Python全套 | **41/41通过**，含访问控制、上传/线程预算、首轮可靠性与打包验证 | `docs/validation/step2/python.txt` |
| Go全套 | **24个顶层测试**，含表驱动场景，`-race -count=3`通过 | `docs/validation/step2/go-race3.txt` |
| 完整浏览器 | **51/51通过**＝原工作台40＋QTTS9＋两版实际启动包复制2 | `docs/validation/step2/browser-all.txt` |
| QTTS专项重复3遍 | **27/27通过** | `docs/validation/step2/qtts-repeat3.txt` |
| 认证网关＋双Mock worker | **3轮通过**：匿名401、正确口令、有序帧、文字完整、两worker参与、中断恢复、模拟零欠载 | `docs/validation/step2/mock-pipeline.txt` |
| 工作台HTTP/API/存储 | **30/30通过**，测试只用临时工作区 | `docs/validation/step2/workbench-api.txt` |
| 语法/编译/重打包/原始与step1不可变性 | 通过 | `docs/validation/step2/syntax.txt`、Python日志 |

测试中修正了两个夹具问题：对隐藏实验室输入框操作前需要切换标签页；全局模拟Thread.start会误伤TestClient自身线程，因此改为只注入业务准入失败。没有通过放宽生产安全检查掩盖失败。

浏览器API和Web Audio是明确的Mock，不代表真实听感。网关HTTP/SSE和取消链路由实际Go/Python服务模拟验证；soundfile使用真实小WAV验证正常/超长路径。当前没有ffmpeg，相关CLI参数及输出超长契约用模拟验证，不能声称真实ffmpeg兼容测试完成。Rust未重新编译。

## 6. 可复现命令

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r kaggle/requirements-test.txt
npm ci
python3 kaggle/repack.py --check
.venv/bin/python -m unittest discover -s kaggle/tests -v
(cd kaggle/source/go/gateway && ../../../../.venv/bin/go test -race -count=3 -v ./...)
.venv/bin/python kaggle/tests/mock_pipeline.py
npm run check
npm test
npm run test:e2e
npm run test:e2e -- tests/browser/qtts.spec.js --repeat-each=3
```

安全仅解包：

```bash
QTTS_UNPACK_ONLY=1 QTTS_ROOT=/tmp/qtts-step2-inspect python3 kaggle/kaggle-fixed-step2.py
```

这不会读Secrets、安装依赖或启动模型。完整运行会安装GPU依赖并可能打开公网隧道；尚未在本环境执行该安装流程。`QTTS_TUNNEL=none`可禁用隧道。

## 7. 不应扩大解释的边界与下一步

- 仍是单用户共享口令，不是多租户账号/RBAC/MFA体系；口令持有者可以删除声音库和使用配置的DeepSeek额度。没有登录会话撤销中心、逐IP/连接级防护或持久安全审计。
- `/tmp`口令文件的0600不能隔离同UID恶意程序、浏览器扩展或管理员；严禁分享/导出凭据。修改服务端口令后需重启网关，既有在途作业不会自动全球撤销。
- 应用层限额不是OS/cgroup配额，空闲磁盘预检不能阻止其他进程填盘。原生解码器没有进程沙箱，ffmpeg真实路径待验；依赖与模型revision锁定仍待完成。
- HTTP取消不等于Python线程/CUDA一定立即停止；本阶段保证昂贵线程名额不提前释放。worker内部队列、重载/删除竞态、supervisor持续故障、长时间运行需后续专项。
- 真正模型训练仍未实现；没有双rank/梯度同步/训练检查点证据。现有ICL参考缓存与校准仍不称为训练。
- 无真实双T4、Qwen权重、Whisper、ECAPA、DeepSeek或麦克风验收。首声<3秒、RTF≤0.5、99.5%相似度均未获得实测通过证据。
- 下一步先完成GPU依赖/第三方流式后端兼容探针与清晰失败报告，再推进两主视图和真实录音波形；真正训练作为独立作业实施并验证，保留现有已测推理/工作台逻辑。

三轮各100项仍是审查清单，不是300项已完成；本阶段只能勾选有对应证据的访问控制条目。历史3个专业问题及每题50条建议保留，不为凑数改动正常代码。

---

## 内嵌备忘录：KAGGLE_STEP3_PLAN.md

# 第三阶段计划：兼容探针与真实采集波形

日期：2026-10-21。保留原始、step1、step2，另存step3。

1. 探针默认只检查安装元数据与工具，不安装、不下载、不加载模型。显式运行时检查放在有超时的隔离子进程：Torch/CUDA设备、原生精度支持、流式后端公开接口签名；不把接口存在等同于推理、训练或性能达标。
2. 启动器安装依赖后、下载模型前运行运行时探针，失败保存结构化报告并停止后续步骤。网关只提供受认证的只读报告，不开放远程执行探针接口。
3. 从真实getUserMedia流创建AnalyserNode，绘制实测时域波形、RMS/峰值；麦克风不接扬声器。MediaRecorder分块采集，选择浏览器支持的容器格式。
4. 录音权限等待、停止、锁定、初始化失败、设备断开、字节/数量/时间预算和迟到回调必须释放流、节点、计时器与音频上下文；禁止过期录音加入新会话。
5. 提供本地录音片段列表及移除操作，不自动上传。保持已验证的认证、语音播放、文件上传、工作台原文复制和历史包不变。
6. 验证分层：CPU探针契约与失败注入；Go报告路由认证/容量；Chromium合成MediaStream的真实Analyser/MediaRecorder及取消测试。浏览器合成信号不称作物理麦克风验收，元数据探针不称作模型可用证据。

本阶段不宣称真正双卡训练、两个主视图改造、真实Qwen/DeepSeek或首声/RTF/音色验收完成。完整依赖锁定与真实GPU实验仍是后续门禁。

---

## 内嵌备忘录：KAGGLE_STEP3_AUDIT.md

> 冻结历史阶段证据；当前源码/重打包入口为step10，见KAGGLE_STEP10_AUDIT.md。下列原统计只描述当时交付，训练输入准备与训练执行不得混同。

# 第三阶段审查：兼容探针与实测采集波形

日期：2026-10-21。范围是设备/接口前置检查与浏览器录音生命周期，**不是完整双T4训练系统验收**。

## 1. 交付与基线

- 新启动包：`kaggle/kaggle-fixed-step3.py`；新清单：`kaggle/source_manifest_step3.json`，30项资产。`python3 kaggle/repack.py --check`只检查step3，不覆盖历史包。
- 原始127241字节，SHA256 `26c31621d6265bc25370bc284f2afdcf52f5edaf97e64056c2d8d5eda4a6c461`。
- step1冻结SHA256 `02e9bb45a14f1e168badc8f897cead0ddd7e70c884d7fd26382c9a5b49778007`。
- step2冻结SHA256 `a628d1bf3f320a330d9206b5f1864e4b38a04f0bc04b26028af2e94368f111d0`，包装测试分别校验历史包。
- 保留单用户Bearer认证、内存凭据、资源预算、音频播放/打断、档案上传与工作台原文复制。三标签页暂不改造为两主视图，参考准备/缓存不改称训练。

## 2. 本阶段实现与检查证据

| 项 | 具体实现/修复 | 源码与验证 |
|---|---|---|
| 1 | 元数据检查不导入模型，显式运行时检查才导入Torch/流式后端；两者均不下载或加载权重 | `tools/backend_probe.py`；`test_probe.py`静态禁导入与禁止模型加载的假后端契约 |
| 2 | 检查GPU数量、计算能力、总显存与请求dtype；T4上的BF16、未经允许的FP32会阻断 | CPU假设备契约；没有真实T4通过证据。总显存不是可用显存 |
| 3 | 检查worker实际调用的三个API；按Python签名绑定位置/关键字/新增必需参数 | AST测试逐一对比worker的实际关键字；`**kwargs`只代表调用形状可接受，明确转发语义未验证 |
| 4 | 子进程120秒预算、超时杀进程组、丢弃第三方导入stdout/stderr；错误消息脱敏 | 超时/无报告/导入异常注入；只保留结构化报告，不收集无界依赖日志 |
| 5 | 启动前静态初检先保存报告，无GPU也保留失败依据；依赖安装后、模型下载前运行运行时探针 | `py/bootstrap.py`；无GPU/单GPU拒绝及顺序测试；探针失败不开始下载 |
| 6 | 原依赖检测的导入子进程也加入60秒与进程组清理，移除抢在正式探针前抛错的重复导入 | `test_reliability.py`超时与DEVNULL契约，避免正式探针尚未运行就无限等待 |
| 7 | 报告0600临时文件原子替换；只读接口最多读取256KiB，缺失返回not_run，损坏/过大返回通用错误 | `go/gateway/preflight_test.go`含未认证401、非GET405、正常/缺失/损坏/null/过大等场景 |
| 8 | `/api/preflight`沿用Bearer；网页不能远程执行探针；新增`recorder.js`显式静态白名单 | Go路由与静态文件测试；浏览器仅GET读取 |
| 9 | 报告读取异常单独显示，不中断原健康/指标监控 | Chromium报告503与原监控请求回归 |
| 10 | getUserMedia→AnalyserNode读取真实时域样本，计算RMS dBFS/峰值并绘制；不连扬声器 | `web/recorder.js`；原生Chromium振荡器流与静音流测试，无随机信号UI |
| 11 | 原生MediaRecorder协商WebM/Opus、Ogg/Opus、MP4，250ms分块；文件后缀跟随实际MIME | Chromium实际编码并检查WebM EBML头和非空文件；不是伪造Blob内容 |
| 12 | session/epoch隔离迟到权限和录音事件；取消后的迟到流仍必须停止 | 原测试曾暴露“已清理标志跳过迟到流停止”的风险，已把停止track放在幂等清理之前；原生流测试覆盖 |
| 13 | 不堆叠未决权限请求；权限拒绝时仍可选文件 | Chromium权限拒绝、等待中再次取消/开始、锁定后迟到流测试 |
| 14 | 停止/锁定/设备结束/页面离开关闭track、节点、上下文和计时；页面离开同时锁定、清空私有状态 | 原生上下文closed及track ended断言；设备结束由软件事件注入，不冒充拔插硬件 |
| 15 | 若stop事件2秒未返回，丢弃片段并清理，不无限保持stopping | 对原生MediaRecorder的stop回调做故障注入，验证超时路径 |
| 16 | 本地单段20MiB、合计63MiB、合计16文件、2048块、约239秒；<1.5秒/空片段不保存 | 原生录音＋缩小预算注入，分别覆盖字节/时长/分块/文件数，未把超限数据截断成成功片段 |
| 17 | 本地列表可移除；只有明确创建档案才上传；上传失败保留录音，成功只移除已提交文件 | `web/app.js`与原生录音503回归；过期档案轮询不能写回新会话 |
| 18 | 交付完整Python启动源码而非网页HTML，复制结果逐字节相等且保留step2 | `tests/browser/studio.spec.js`第三阶段完整源码剪贴板测试；工作台正常编辑/保存/冲突/预览继续回归 |

## 3. 运行方式

只检查环境，不安装或下载：

```bash
python3 kaggle/source/tools/backend_probe.py
python3 kaggle/source/tools/backend_probe.py --runtime --expected-gpus 2 --dtype fp16 --timeout 120 --output /tmp/qtts-probe.json
```

退出0只表示`surface_preflight_passed`；阻断或仅静态检查退出2。默认检查不会返回“模型已就绪”。报告中`model_loaded`、`inference_verified`、`training_verified`、`performance_verified`恒为false。沙箱实际运行运行时探针得到blocked、退出2：Torch/流式后端未安装，ffmpeg缺失。日志在`docs/validation/step3/runtime-probe*`，没有用Mock替代为通过。

安全仅解包（不运行安装器）：

```bash
QTTS_UNPACK_ONLY=1 QTTS_ROOT=/tmp/qtts-step3-inspect python3 kaggle/kaggle-fixed-step3.py
```

真实完整启动应在Kaggle双T4环境，配置Internet与私有`QTTS_ACCESS_TOKEN` Secret，再运行step3包；安装、依赖供应链与模型下载仍需真实环境审查，**此处没有执行完整安装流程**。`QTTS_TUNNEL=none`禁用自动隧道。生成口令仍默认保存在/tmp私有目录，不进入声音库导出，详见第二阶段安全报告。

浏览器通过可信HTTPS代理访问，解锁后在声音实验室点击录音。曲线为实测输入，不是质量评分；dBFS不是校准声压级。没有物理麦克风或权限被拒绝时仍可上传已有文件。浏览器压缩音频容器需要服务端解码器支持，无ffmpeg时优先上传WAV。片段移除只删除浏览器待提交引用，不会删除已上传声音库。

## 4. 验证日志

实际执行结果均通过：

| 验证层 | 本次结果 | 日志（docs/validation/step3/） |
|---|---|---|
| Python | 56项×3轮=168次 | python-round1/2/3.txt |
| Go竞态 | 26顶层＋16子测试，race重复3遍 | go-race3.txt |
| 完整Chromium | 66项×3轮=198次，包含23项QTTS和43项工作台测试；耗时约6分钟 | browser-repeat3.txt |
| Node工作台API | 30/30 | workbench-api.txt |
| 真实Go＋双CPU Mock | 3/3，文本完整、有序帧、两worker、取消后恢复、模拟水位 | mock-pipeline.txt |
| 实际CPU环境运行时探针 | **blocked，退出2，未加载权重**（环境缺依赖，不是模型通过） | runtime-probe.json / runtime-probe-output.txt |
| 语法/确定性包/原始与历史包 | 通过；仅解包逐字节校验包含于Python测试 | syntax.txt / Python日志 |

最终step3为171251字节、30资产，SHA256 `4b69f9adec43487c731c53e7ae65f91534626e71660f1b50b109bfe0c8cb973b`。工作台复制测试核对整个启动包，不是抽样片段。

复现：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r kaggle/requirements-test.txt
npm ci
.venv/bin/python kaggle/repack.py --check
.venv/bin/python -m unittest discover -s kaggle/tests -v
(cd kaggle/source/go/gateway && ../../../../.venv/bin/go test -race -count=3 -v ./...)
.venv/bin/python kaggle/tests/mock_pipeline.py
npm run check
npm test
npm run test:e2e -- --repeat-each=3
```

Python测试使用CPU依赖，不是GPU生产锁定文件。FastAPI测试有httpx弃用警告，故障注入会打印预期错误堆栈；这些不等于测试失败。浏览器测试使用临时工作区，与正式workspace隔离。

## 5. 不能扩大解释的边界与下一步

1. **真实GPU、Qwen/流式后端、CUDA Graph/SDPA与空闲显存尚未验收。** 方法存在或`**kwargs`可绑定不能保证内部实现兼容，也没有依赖/模型revision锁定结论。
2. 没有物理麦克风、手机/浏览器矩阵、压缩音频经真实ffmpeg解码的端到端测试。原生Chromium的软件输入测试不是上述验收。静音/RMS/削波提示不保证录音质量。
3. 后台页面计时可能被节流，239秒是本地停止预算，不是容器实际时长的权威值。服务端240秒/文件、900秒总时长和64MiB整请求预算仍独立复核；超限失败会保留本地录音。
4. 63MiB客户端预算只约束片段/已选文件字节，不是浏览器总体内存上限；编码器、File/Blob与UI仍占内存。应用限额不等于OS配额、原生解码沙箱或多租户隔离。
5. 原生权限窗口不能被应用撤回，取消后必须等返回再停止迟到流；不会将迟到数据加进已锁定/新会话。
6. **真正world_size=2训练、两个主视图、真实DeepSeek长流/声音质量/首声<3秒/RTF≤0.5/99.5%相似度仍未完成或未验证。** 不把录音、参考缓存、Mock、探针或测试数量当作训练成功。
7. 下一步先在目标硬件执行可复现最小模型推理与容器解码，再实施两主视图及独立双卡训练作业；训练必须核对双rank、样本覆盖、梯度同步、显存和检查点重载。

300项清单只勾选有对应证据的具体项。三次全量自动化模拟不等于三次真实GPU端到端验收；历史三个问题及各50条建议继续保留。

---

## 内嵌备忘录：KAGGLE_STEP4_PLAN.md

# 第四阶段计划：两主视图与视口内操作

日期：2026-10-21。先计划再实施；独立step4，不覆盖原始、step1、step2、step3。

## 范围与取舍

真实双T4/模型/DeepSeek通路在本沙箱不可用，不能制造最小推理或训练通过证据。推进可独立实施的两主视图界面：录制参考语音、语音对话。监控保留为辅助诊断对话框，不再作为第三个主要视图。保留所有已有档案、候选、校准、参考文本、导出、播放和打断功能；不添加假训练按钮。

## 实施顺序

1. 以step3包与全部ID/事件为基线，冻结历史哈希；另存step4包/清单。
2. 两个具备可访问名称/选中状态的主要导航，采用原生按钮。切换隐藏面板使用hidden语义；键盘导航不落入隐藏内容。
3. 主要录音/上传/创建与文字/声音选择/开始/停止操作保留在视口内，长文本、片段、档案、可选项有独立滚动或折叠区域。桌面双栏，手机紧凑分区；不以全页裁切掩盖不可访问控件。
4. 登录/解锁区解锁后折叠为状态条，随时可锁定；凭据仍在内存，锁定恢复表单并清私有数据。公开说明保留；高级诊断放原生dialog，有关闭按钮、Escape和焦点恢复，锁定强制关闭。
5. 切换主视图时停止正在请求/采集的麦克风（保存已停止的本地片段，不丢弃有效录音）；语音播放在切到录音页前停止，避免回声/隐形操作。不能把会话切换当作训练。
6. 保持监测/网关检查/分段/耗时/最近运行/所有档案操作可访问，诊断关闭时不轮询，打开时不重叠轮询。旧会话或关闭对话框后的迟到结果不能恢复私有UI。
7. 验证1440×900、1024×768、768×1024、390×844、375×667及短屏布局；主要操作无页面滚动，过小高度/200%缩放可退化为可滚动布局而不是丢失内容。验证长输出/大量档案/长文件名、键盘焦点、Escape、锁定和已有原生录音/播放回归。
8. CPU/Python、Go race、Node API、Chromium三轮回归与包的仅解包/复制校验，日志另存docs/validation/step4/；完成后更新清单/完整交接提示词及工作台，不提前勾选。

## 验收边界

视口测试仅证明列出的Chromium尺寸与布局行为，不代表所有手机/浏览器/虚拟键盘/屏幕阅读器验收。浏览器音频输入仍为原生软件流，非物理麦克风。真实GPU、world_size=2训练、模型/依赖锁定、DeepSeek长流、首声<3秒、RTF≤0.5及99.5%相似度继续单独列为未完成/未验收。

实施补充：短屏阈值最终为≤640 CSS px；手机新增常驻“选项”入口。测试注入仓库现有本地Noto字体，不打包外链字体；实际OS缩放/虚拟键盘仍待硬件验收。

---

## 内嵌备忘录：KAGGLE_STEP4_AUDIT.md

> 冻结历史阶段证据；当前源码/重打包入口为step10，见KAGGLE_STEP10_AUDIT.md。下列原统计只描述当时交付，训练输入准备与训练执行不得混同。

# 第四阶段审查：两主视图与视口布局

日期：2026-10-21。只验收本阶段界面/生命周期与CPU协议，不验收真实模型或训练。

## 交付

- `kaggle/kaggle-fixed-step4.py`：175985字节，30资产；SHA256 `069421e5f0d4112148211e1289f91ec7a1b184105e5431fde0c3d72e8c744e27`；清单`source_manifest_step4.json`。
- 原始、step1/2/3包均冻结，Python测试分别核对哈希；step3仍为`4b69f9adec43487c731c53e7ae65f91534626e71660f1b50b109bfe0c8cb973b`。repack.py现在只生成step4。
- 计划先保存`docs/KAGGLE_STEP4_PLAN.md`再实施；目标设备门禁另存`docs/KAGGLE_TARGET_ACCEPTANCE.md`，待执行项不伪填为通过。

## 具体实现与证据

| 项 | 改动/保留 | 证据 |
|---|---|---|
| 1 | 主导航只有“录制参考语音”“语音对话”，选中状态aria-pressed，隐藏面板不接受焦点 | `web/index.html`、`app.js:j`；Chromium主导航/方向键/Home/End/隐藏输入测试 |
| 2 | 监测改为原生dialog辅助窗口，保留系统、兼容探针、最近运行、分段、耗时、同源网关 | 旧DOM ID与脚本顺序逐一校验，未删除旧功能；不是第三主视图 |
| 3 | 关闭/Escape/焦点恢复、模态内锁定、清空私有数据后回到登录输入 | 模态与认证回归；锁定强制关闭，未把关闭窗口当作删除档案 |
| 4 | 解锁后访问表单收起为状态条，锁定按钮常驻；凭据仍只在内存 | 现有认证/URL/存储/迟到响应回归继续执行 |
| 5 | 桌面双栏，手机分区；主要操作固定，配置/回答/档案/片段内部滚动 | 1440×900、1024×768、768×1024、390×844、375×667，检查控件完整边界、祖先裁切、中心命中及页面不溢出 |
| 6 | 初查发现中心命中仍可能漏掉控件下缘裁切，已收紧断言并调整375px布局 | 修复文件选择/模式选择部分裁切；声音库滚动区>40px，未用overflow隐藏无法到达的按钮冒充通过 |
| 7 | 高度≤640 CSS px退化为可滚动页面，避免短屏/等效缩放丢失操作 | 375×480测试；不宣称实际OS缩放/手机虚拟键盘通过 |
| 8 | “选项”明确入口始终可见，参考文本与校准设置可折叠、键盘可达 | 375×667显式按钮、summary焦点、Tab到转写、关闭后文件选择恢复 |
| 9 | 切换到采集页停止语音播放/未决初始化；切到对话或打开诊断停止采集 | 原生MediaStream停止/上下文closed、有效WebM片段保留；取消后的迟到权限继续安全释放 |
| 10 | 诊断只打开时顺序轮询，关闭中止，代际隔离迟到结果 | 6秒慢响应无重叠、同一任务关闭/重开、过期报告、关闭后10秒无轮询；使用虚拟时钟故障注入 |
| 11 | 长回答和40个长名称档案不撑开页面，内部滚动仍保留主操作 | 375×667压力场景；原文本保存/候选/启用/校准仍能发出相应请求（HTTP夹具，不是GPU校准） |
| 12 | 自定义名称为空或>64 Unicode字符时不上传，不默填my-voice；失败保留文件 | 空名/超长/自命名503回归；动态参考文本、片段移除补充可访问名称 |
| 13 | 速度倍率不再误标为标准RTF；缺失统计显示未测/未设置 | `app.js:W/et`；不把没有测量的数据补成模型成功 |
| 14 | 中文截图使用仓库现有本地测试字体，确认字形可读后再验布局 | `tests/browser/qtts.spec.js`字体等待；生产包不新增外链字体，依赖浏览器设备的系统中文字体 |
| 15 | 独立step4完整Python源码复制，保留历史包与工作台编辑/保存/冲突/预览 | `studio.spec.js`全包逐字节剪贴板与既有工作台回归；未执行安装器 |
| 16 | 原生录音器已inactive时不重复stop丢弃数据，自动stop也计算采集墙钟时长 | 原生MediaRecorder两种事件顺序、有效片段保留；最低时长用100ms时钟注入独立验证，非物理时间测量 |

## 验证结果

最终全量浏览器87项×3轮=261次通过（QTTS43项＋工作台44项，约7.3分钟），日志browser-repeat3.txt。首次全量为251通过/1失败：设备结束测试错误地假定UI步骤必然少于1.5秒，实际有效片段按设计被保留。已改为明确录制有效片段；静音测试也不再依赖操作必须很快，最低时长另用可复现的100ms时钟注入验证。检查中另补了原生自动stop竞态修复及测试；相关五项×3=15次专项通过。首次日志保留browser-first-attempt.txt，中止调整测试的第二次日志保留browser-interrupted-attempt.txt，不计为通过。最终Python59项×3轮=177次、Go26顶层/16子测试race×3、Node API30项、真实Go＋双CPU Mock管线3轮，均通过。实际CPU运行时探针仍blocked/退出2，没有加载权重；见runtime-probe.json。最终结果与日志在`docs/validation/step4/`。

- `python-round1/2/3.txt`：可靠性/认证/探针/包装/历史哈希/DOM保留。
- `go-race3.txt`、`mock-pipeline.txt`：保持访问控制、有序PCM、两worker、取消恢复与模拟播放器水位。
- `browser-repeat3.txt`：最终完整工作台与QTTS；`recording-races-repeat3.txt`为15次录音专项。不以截图或失败尝试代替通过记录。
- `syntax.txt`、`workbench-api.txt`：语法/确定性包/Node API。
- `chat-1440x900.png`、`reference-1440x900.png`、`chat-375x667.png`、`reference-375x667.png`：已解锁界面的HTTP夹具截图，无真实凭据/模型输出，不是生产或GPU实验。

## 使用与复现

```bash
python3 kaggle/repack.py --check
.venv/bin/python -m unittest discover -s kaggle/tests -v
(cd kaggle/source/go/gateway && ../../../../.venv/bin/go test -race -count=3 -v ./...)
.venv/bin/python kaggle/tests/mock_pipeline.py
npm run check
npm test
npm run test:e2e -- --repeat-each=3
```

测试环境初始化见requirements-test.txt与npm ci；不是GPU生产依赖锁定。安全仅解包：

```bash
QTTS_UNPACK_ONLY=1 QTTS_ROOT=/tmp/qtts-step4-inspect python3 kaggle/kaggle-fixed-step4.py
```

完整运行会安装依赖/下载模型/可能打开隧道，当前沙箱没有执行。真实Kaggle启动、非Mock核对、最小推理、容器/DeepSeek/训练等门禁见`KAGGLE_TARGET_ACCEPTANCE.md`。不把仅解包退出0或探针表面通过当作模型就绪。

## 限制与下一步

- 本次仅测试列出的Chromium CSS视口。中文字体由浏览器设备提供；测试注入的本地Noto字体没有塞入Kaggle包。未做全浏览器、物理麦克风、触屏、屏幕阅读器、真实虚拟键盘/OS缩放验收；高度≤640允许页面滚动，主要操作不滚动不是全尺寸保证。
- 手机语言/Key等次要配置、详细转写、长列表需内部滚动或“选项”；声音库没有分页，不能因此勾选清单的分页项。没有新增先持久化空语音库的独立流程或训练任务UI；对话页仍以文字提问，没有新增语音提问转写。
- 参考创建/校准仍不是训练；没有双rank、梯度、样本覆盖或检查点证据。真正world_size=2训练、真实Qwen/双T4/DeepSeek/ffmpeg容器全链路、首声<3秒、RTF≤0.5、99.5%相似度仍未完成/未验收。
- 下一步应在目标设备按门禁先证明非Mock引擎与每卡真实推理，再适配独立训练作业；不能只包一层accelerate或照搬T4不支持的BF16/标准FA2示例。
- 工作台单项目上限仍为1MiB，不为塞入重复交接文件而提高限制或删除旧文件。完整交接提示词保存在仓库`docs/KAGGLE_HANDOFF_PROMPT.md`；工作台保留历史文件后仅添加能容纳的新源码/简报。

300项清单仍不是已修复300个缺陷，只有具备证据的具体项能勾选；三个历史专业问题及每题50条建议继续保留。

---

## 内嵌备忘录：KAGGLE_STEP5_PLAN.md

# 第五阶段计划：先建库、再管理参考样本

日期2026-10-21；先保存计划再实施。当前真实GPU/模型/DeepSeek/物理麦克风实验条件不具备，不伪造训练或性能通过。

## 范围与取舍

1. 新增与可推理profiles分离的STATE/libraries原始样本库。先用自定义名称创建持久空库，再添加/列出/选择/删除样本，再明确执行“处理所选参考”。空库/原始样本绝不进入声音档案下拉框或被worker当成模型。
2. 原有一步创建声音档案、两主视图、诊断、原生录音/播放/打断全部保留。新流程放独立辅助原生dialog；不是第三主视图。用户可先建库，再回主视图录音，随后添加本地片段到库。
3. 原始样本写入不解码/不加载模型，显示“未解码、未训练”。处理仍调用既有build_profile，生成新的可用档案；是参考处理，不是训练。失败保留源样本，不删除此前成功档案。
4. 原始数据只在本地STATE保存，不自动放入Kaggle Dataset导出，防止扩大私密音频分发。会话结束仍会丢失工作目录；不是永久/跨会话存储保证。

## 实施顺序

- 建独立标准库文件存储模块：UUID路径、0600原子清单/数据、0700目录、拒绝symlink/路径穿越，哈希核对、同库去重、事务提交失败回滚、新进程可读。
- 库数128、样本数16/库、20MiB/文件、64MiB/库、512MiB全局原始字节；沿用整请求64MiB、空闲磁盘256MiB、后台构建单并发与有界记录。库字节预算不是OS总体配额；解码时长仍由原处理器复核。
- fcntl非阻塞库租约跨线程/进程阻止构建期间改样本/删库；操作锁期间快速返回409而不排等待线程。构建失败/线程启动失败/取消/进程退出必须释放或由OS回收租约，遗留processing不得冒充成功。
- 通过已认证/api/prep/libraries反向代理提供仅必要GET/POST/DELETE接口，扩展上传预算只匹配正确samples上传路径；JSON严格字段/类型/容量，错误不暴露私密路径或原始样本。
- 浏览器库管理dialog：命名建库、选择库、文件/本地片段入库、样本勾选/移除、处理所选、明确状态。锁定清空全部私有库视图/选择/文件并关闭；迟到回调不能写回。模态焦点/关闭/Escape保持一致，不让麦克风在覆盖窗口后暗中采集。
- Python文件/事务/并发/故障注入与真实FastAPI上传、Go认证/预算/代理、Chromium流程/隐私/原生录音回归及新包逐字节复制。保存三轮分层日志，不以模拟代替GPU。
- 独立step5包与清单，冻结step1/2/3/4。正式工作台已15文件/1043155字节，剩余不足新包：不提高1MiB、不删/覆盖旧文件。本阶段优先独立文件交付，复制测试在隔离临时工作区验证，不暗改正式HEAD。

## 明确未完成

真正world_size=2训练、训练任务UI/检查点、真实模型/后端/双T4/ffmpeg/DeepSeek/物理录音/质量/首声/RTF验收仍未实现或未验证。三轮各100项只勾有证据的项，原150条专业建议保留。

---

## 内嵌备忘录：KAGGLE_STEP5_AUDIT.md

> 冻结历史阶段证据；当前源码/重打包入口为step10，见KAGGLE_STEP10_AUDIT.md。下列原统计只描述当时交付，训练输入准备与训练执行不得混同。

# 第五阶段：命名空库与参考样本证据

日期2026-10-21。计划先保存于KAGGLE_STEP5_PLAN.md，再增量实施。此文是阶段报告，**不是完整模型/训练产品验收**。最终浏览器全量与最终包复制专项已完成，结果如下。

## 交付与使用

独立启动包：`kaggle/kaggle-fixed-step5.py`；32项内嵌资产。最终196140字节，SHA256 `acfa5639324e16aa7dcfe314caef09bee8eb277d59bdd71a5f1f4cffa0a7aaf1`，见source_manifest_step5.json。原始/step1/2/3/4均冻结不覆盖。

1. 进入“录制参考语音”，点“声音库与样本”。
2. 自行命名，点“仅创建命名空库”；不要求先上传音频，也不生成可用声音档案。
3. 向选定库添加文件，或先关闭窗口在采集页录音，再回库添加本地录音。保存失败保留本地片段/所选文件供核对重试；同库同内容SHA256去重。
4. 手动勾选已保存样本，可填写参考文本并选校准，然后点“处理勾选参考（不是训练）”。原有快速创建声音档案入口与文本/候选/启用/校准操作保留。
5. 处理成功只表示既有参考准备任务完成；不会把空库或未解码样本放进可用声音档案。`training_verified/inference_verified/decoded_duration_verified`在原始库对象中不冒充通过。

## 三轮审查：本阶段具体落实

| 层次 | 落实 | 证据或边界 |
|---|---|---|
| 存储 | STATE/libraries与profiles分离；UUID路径、NFC/大小写折叠库名、0700/0600、新进程可读 | 真实临时文件系统/子进程测试 |
| 限额 | 默认128库、16样本/库、20MiB/文件、64MiB/库、512MiB总原始音频、256MiB磁盘余量 | 注入小预算测试；不是OS配额 |
| 事务 | 内容SHA256/去重、修订CAS、原子清单；上传/清单失败回滚新文件；下一次修改清理未引用音频/临时文件 | 写入/清单失败注入、并发同修订竞争 |
| 安全 | 拒绝UUID穿越/目录和清单链接/样本软硬链接；JSON拒绝重复键/NaN/未知字段 | FastAPI实上传与文件系统测试 |
| 代理 | 库路由继续认证；仅精确POST libraries/{32位hex}/samples扩大上传预算；移除上游私密凭据 | Go真实反向代理/已知长度及chunked预算 |
| 作业 | 新旧流程共享ADMISSION与BUILD_LOCK；Linux flock跨进程同库租约；固定勾选字节快照 | 忙碌409/429、SIGKILL、哈希不符、外来样本ID |
| 终态 | 元数据提交后才发布done；提交失败不宣称成功；失败保留原件及此前独立档案 | 提交屏障与故障注入测试 |
| 取消 | 库租约预约和线程接管在一次准入函数中，HTTP取消不会在两步之间遗留未接管租约 | ASGI取消测试；已提交操作可能继续 |
| 线程池 | 提交可能排队后启动失败；门闩拒绝迟到排队任务执行/二次释放 | 真实ThreadPoolExecutor故障复现及回归 |
| 浏览器 | 库管理是辅助dialog，仍仅两主视图；关闭/Escape/焦点、锁定清私有内容；迟到建库/移除响应隔离 | Chromium夹具；不是真实GPU界面 |
| 录音 | 打开库停止实际MediaRecorder采集并保留有效片段；建库后可添加本地录音 | 软件MediaStream，非物理麦克风 |
| 隐私 | 原始库不自动加入Dataset；删除库不删除生成档案 | 实际_pack的边界测试 |

## 验证日志（docs/validation/step5/）

- Python：`python-round1/2/3.txt`，**92×3=276项通过**。包括原59项、step4冻结检查及32项新库/线程池测试。
- Go：`go-race3.txt`，28顶层＋16子测试，race三轮通过。
- 真实HTTP：`library-http3-final.txt`，Go→真实analyst→磁盘三轮通过。每轮上传1049088字节文件（超过1MiB JSON预算），重启analyst验证恢复，再提交损坏音频，确认**正确报错**且原始SHA256不变；不把这一负向用例当作解码成功。
- 两CPU Mock worker：`mock-pipeline.txt`，三轮有序分段、两worker分配、中断后恢复与模拟无欠载通过；不是T4证据。
- 浏览器新流程初检：`browser-libraries-initial.txt`，12通过；全量100唯一用例×3＝300次通过（55 QTTS＋45工作台），11.2分钟，见`browser-repeat3.txt`。最终196140字节包另作逐字节剪贴板三次核对，`final-copy-repeat3.txt`3通过/11.5秒；全量启动后收尾的后端Unicode与嵌入备忘录也已由最终Python三轮和复制专项覆盖。
- 工作台API：`workbench-api-round1/2/3.txt`，30×3=90通过。新包逐字节真实剪贴板回归在隔离临时工作区，不会改正式HEAD。
- 语法、compileall、重打包：`syntax.txt`通过。运行时探针`runtime-probe.json`仍blocked/退出2，缺Torch/流式后端/ffmpeg，不加载权重。

## 初检失败与修正，不能隐去

1. `python-initial.txt`：91项中2失败。GET只有DELETE的样本资源应为405，不是404；无音频下载能力不变。线程启动故障注入原先命中测试框架/线程池，不是目标build线程。改为按build-线程名精确注入。
2. `python-second.txt`当次91通过，但后续并发负载下`python-failed-executor-submit.txt`重现线程池提交异常留下排队任务，随后线程可能执行该请求。不是简单放宽断言：已修HeavyAdmission提交门闩，新增真实ThreadPoolExecutor回归后全量92连续三轮通过。
3. `python-failed-surrogate-client.txt`：测试客户端默认非ASCII JSON编码先拒绝孤立代理码，尚未到服务器。改用合法ASCII转义JSON传输，服务端明确400；名称/语言/参考文本拒绝无效Unicode，最终92×3重跑通过。
4. Go测试追加最初一次命令工作目录用错，未写入文件；改为仓库根目录执行后通过。没有把该命令失败计作测试通过。
5. 正式API一次只读核对脚本把每个Buffer分块独立转UTF-8，切开中文多字节时误多算21字节；改为Response.json正确解码后15个文件的SHA256逐一与磁盘收据相同、总1043155字节。正式文件从未被该只读检查写入。

## 存储、隐私、部署边界

- 本地磁盘持久化意味着刷新/分析服务重启仍可读，不意味Kaggle会话永久或跨会话恢复。原始库不自动导出；**处理后的档案锚点/转写仍沿用已有Dataset备份设置**，应有参考声音授权。
- 删除不是安全擦除，且不删除独立profiles/既有Dataset备份。语音文件、转写、密钥不进Git。
- 清单提交用文件fsync+replace，不承诺断电原子耐久；中断未引用文件在该库下一次修改回收。损坏清单报错需人工修复，不自动清空“恢复”。元数据量仍受库/样本数限制。
- Linux flock仅保证配合本协议的进程；这不是同UID恶意进程隔离、容器沙箱、多租户账号、硬盘OS配额或多个analyst实例的全局GPU调度方案。
- JOBS仍是有界内存任务表，不是持久审计数据库；库仅保留最近处理状态/来源修订与ID、最近成功档案指针。服务重启释放锁，遗留running显示interrupted，不自动重跑收费/模型任务。
- 原始上传允许未解码数据保存但明确标未验证；真正处理沿用原有容器/时长/总时长检查。没有实际成功处理真实长参考语音、加载Qwen、双T4模型、DeepSeek或训练的实验结果。
- 正式工作台15文件/1043155字节，剩5421字节；本阶段新包不强塞，不提高1MiB、不删历史、不改HEAD。独立文件交付；工作台复制兼容仅在容量充足的隔离工作区验证，不能声称已发布到正式工作台。正式服务已恢复在3000，只读API逐个核对15个SHA256，见formal-api-readonly.json与delivery.json。

## 清单与下一步

仅R1-073（内部ID与显示名称/路径分离）可在本阶段有据增加，清单19/300。R1-074在新库流程满足，但旧快速创建兼容入口仍保留，不以局部结果勾成全局强制；训练数据状态/覆盖/检查点/模型恢复均未验收。专业问题4另存50项建议，前150项保留，共200建议，不等于200项已完成。

下一步仍先按KAGGLE_TARGET_ACCEPTANCE.md做真实非Mock后端/每卡最小推理/容器解码门禁，再适配独立双卡训练作业与资源模式切换；不要只加accelerate launch或训练假按钮。

---

## 内嵌备忘录：KAGGLE_STEP6_PLAN.md

# 第六阶段计划：可校验、不可变的训练输入快照

2026-10-21。先保存计划再编码。接续step5命名库；不是训练执行或双T4验收。

## 核对与选择

训练不能直接复用原始样本的一个公共ref_text：官方固定提交022e286b98fbec7e1e916cb940cdf532cd9f488e的finetuning/README.md要求每行audio/text/ref_audio，建议同一个ref_audio。参考处理/校准不产生optimizer更新，现有supervisor也没有训练/推理互斥资源模式。沙箱无Torch/GPU/模型，不能假装实现并实测双T4训练。

本阶段做独立“训练输入准备”而非训练按钮：用户逐条提供转写、显式选统一参考、声明声音使用授权及单说话人，锁定库修订与所选原始哈希，生成私有本地不可变快照。训练执行、声学码提取和模型检查点仍待下一阶段与真实设备门禁。

## 实施

1. 新STATE/training_data，独立于profiles/libraries。随机UUID/0700目录/0600文件；API只增创建、列举、校验、删除，不提供任意路径或shell命令执行。
2. 训练输入初版严格接受完整24kHz单声道PCM16 RIFF/WAV，结构/帧数/时长/非空/非恒定信号复核；其他格式明确拒绝，不偷偷把浏览器Opus后缀改成WAV，不自动有损转换或截断。既有参考处理保留原解码路径。后续受限解码器另验，不借本阶段冒充ffmpeg通过。
3. 每条转写1–2000码点，累计16000，拒绝空文本/无效Unicode/重复或外来样本；统一参考必须属于勾选集合且≤16秒，训练片段1.5–240秒，累计≤900秒。无自动转写/说话人鉴定/文本匹配验证，用户声明不等于模型验证。
4. 复用Linux同库租约，仅取快照，不改last_build/已生成档案。输出规范WAV（保留全部PCM帧，剥离额外容器元数据）、train_raw.jsonl、manifest.json和rank_plan.json；记录来源库/修订/所选ID/原始和输出哈希/文本哈希/参数/声明。
5. 双rank计划只是可复现数学分配：不drop样本、奇数明确标padding重复；不是已运行rank或梯度同步证据。训练/分词/推理验证标志保持false。
6. 原子目录发布，失败回滚，孤立staging下次操作回收；默认32快照、64MiB/快照、256MiB全部快照、磁盘余量256MiB。与原始库分别限额；只在本地保存，不自动加入Dataset。删除库不删除已生成副本，要明确告知可单独删除。
7. 库管理dialog新增可折叠训练输入区域；逐样本文本、参考选择、两项明确声明；创建/校验/删除结果均真实接口驱动，清楚显示非训练。锁定/关闭清私有转写与输出选择，迟到结果不能恢复。
8. 严格JSON预算与已有HEAVY准入；验完整SHA、JSONL相对路径、逐条文本/引用、rank计划，不信任存在即完整。路径只由服务端UUID生成；同UID恶意进程不是隔离承诺。
9. Python真实WAV/文件/事务/并发/权限/篡改/旧流程回归，Go认证与小JSON预算，新浏览器流程及原有全量三轮，独立step6打包/全包复制；保留step1–5、原工作台15文件和1MiB上限。

## 明确未完成

未进行真实模型/双T4/DeepSeek/物理麦克风/ffmpeg/音质与性能实验；没有训练进程、GPU模式切换、audio_codes、loss/梯度/optimizer/checkpoint。输出state=input_snapshot_ready，绝不叫trained或ready_to_train。三轮300项审查只勾确实有证据的项。

---

## 内嵌备忘录：KAGGLE_STEP6_AUDIT.md

# 第六阶段审查：不可变训练输入，不是训练执行

> 历史第六阶段冻结报告：当前源码入口已推进至step10；最新实现与真实编码阻塞见KAGGLE_STEP10_AUDIT.md，以下统计保留原第六阶段证据。

2026-10-21。先保存KAGGLE_STEP6_PLAN.md与专业问题5的50项行动建议，再实施。这里的“准备完成”仅为训练输入快照；**没有训练器、audio_codes、优化器、GPU模式切换或真正双rank运行**。

## 交付与操作

- 独立`kaggle/kaggle-fixed-step6.py`，210003字节/33资产，SHA256 `781eca6e2e34bdacbe2f5337bd6535512226c2122bbf3876d05634f2fc86d256`。原始与step1–5冻结，清单source_manifest_step6.json。
- “录制参考语音”→“声音库与样本”→先建立并上传到命名库→勾选音频→展开“训练输入快照”。每段单独填对应转写、显式选统一参考，并确认声音使用权/单说话人声明。点“生成训练输入快照（不训练）”。
- 下方可查看所有来源库的输入副本、按固定manifest哈希核对、二步确认删除。没有新增主导航。原始库删除后副本仍在，可继续从这个列表单独删除。
- 首版只接收**完整24kHz单声道PCM16 RIFF/WAV**。参考1.5–16秒、其他片段1.5–240秒、累计≤900秒。WebM/Opus/Ogg/MP4/其他采样率会明确拒绝，不换后缀、不静默转码、不截断；原始库内文件保留。原有参考处理仍走旧解码路径，不因此宣称ffmpeg已通过。
- 转写每条1–2000码点、合计16000；是用户提供的文本，没有ASR匹配/声纹核验。声明是记录用户同意，不是技术证明权利或身份。

## 具体增量与证据

| 项 | 实现 | 证据/限制 |
|---|---|---|
| 来源快照 | LibraryStore.snapshot只读同库租约，固定修订/所选ID/原始字节与SHA256，不修改last_build | 源库修改409、旧档案状态不变、源库删除后副本可验 |
| 格式 | 审查RIFF总长/所有chunk边界，拒绝多fmt/data、错误采样率/声道/位深、短/长/常量信号 | 真实合成PCM16测试；非恒定不等于有效人声 |
| 规范输出 | 每个选中样本保留全部PCM帧，规范WAV剥离额外容器元数据 | 帧数/PCM逐字节相同，原始和规范WAV哈希分别保存 |
| 数据约定 | train_raw.jsonl每行audio/text/ref_audio，统一参考来自选中集合 | 对照Qwen固定提交；没有把一个ref_text复制给全部样本 |
| 可追溯 | manifest记录库/修订/ID、来源名、原始/输出/文本/JSONL/计划哈希、帧数/采样率/峰值/RMS及声明 | 转写只在JSONL，列表/响应不重复返回私人全文 |
| 双rank计划 | 稳定哈希排序与epoch轮换，分两rank、等步数、无drop、奇数显式padding | 只是数学分配；不是DDP/采样器/梯度执行证据 |
| 事务与预算 | 独立UUID暂存→校验→原子目录发布；失败回滚，下次写操作回收孤立staging | 文件/rename故障注入；默认32快照、64MiB/快照、256MiB全局与256MiB磁盘余量 |
| 私密与路径 | 0700/0600、无任意路径/执行接口、软硬链接拒绝、固定哈希核验文件集合/索引/路径/内容 | 同UID恶意进程与断电耐久不是承诺；不是签名系统 |
| 接口 | 已认证/api/prep/training-data创建/列表/verify/DELETE；严格JSON字段/布尔/文本，继续小JSON预算及HEAVY准入 | Go预算/匿名401、FastAPI真实接口及错误脱敏 |
| 界面 | 逐条文本/显式参考/两项声明、结果/校验/单独删除，关闭/锁定清私密与代际隔离 | 浏览器HTTP夹具；不声称对接真实Qwen |
| 声明隔离 | 选中集合、新建/切库、删除库、自动回退源库时，不复用旧声明或转写 | 新增专门浏览器回归；修改后重新确认 |
| 备份边界 | 原始库和训练输入均不自动加入Dataset，既有profiles备份保持 | 真正_pack归档成员测试，独立副本要单独删除 |

## 文件与后续使用约定

数据位于STATE/training_data/{服务端UUID}/：

- audio/{样本UUID}.wav：规范24kHz/单声道/PCM16全部帧。
- train_raw.jsonl：逐条audio/text/ref_audio；路径相对**数据集目录作为工作目录**，不是自动相对JSONL文件。使用上游prepare_data时必须先切到该目录。
- manifest.json：schema1、state=input_snapshot_ready，不是ready_to_train/trained。
- rank_plan.json：kind=assignment_plan_not_execution。真正训练必须由支持等步数/显式padding语义的采样器落实并记录每rank覆盖，不能把这个文件当作实际训练日志。

`audio_format_verified/assignment_plan_verified`只对应格式/数学计划；`transcript_verified/speaker_identity_verified/tokenization_verified/training_verified/two_rank_execution_verified/inference_verified`均false。

列表`integrity_verified_now=false`，表示只读索引未重新验全部文件。明确校验成功才置true；请求携带先前固定manifest SHA256，不把当前任意文件存在当完整。校验失败前清除旧成功展示，失败不删除原件或旧独立副本。

## 分层验证（docs/validation/step6/）

- Python初检111通过；补充真实Dataset备份边界后为112。最终112×3＝336通过，python-round1/2/3.txt。
- Go28顶层/16子测试race三轮通过；工作台Node API30×3通过。
- training-http3-final.txt：真实Go→analyst→文件系统三轮，合成PCM16格式输入/逐条转写/声明拒绝/固定哈希/篡改409/源删除后副本独立/单独删除，且不增加模型JOBS。包含前阶段坏音频正确失败与原始哈希不变的旧链路。
- mock-pipeline.txt：两CPU Mock worker的三轮有序合成/中断恢复；不是真实GPU/人声。
- browser-initial.txt：旧库12＋新输入4＝16通过。training-browser-repeat3.txt：增加声明边界后5×3专项通过。最终全量106唯一用例×3＝318通过（10.6分钟），browser-repeat3.txt；不把中止的旧全量当三轮完成。
- 包原始22哈希＋当前33资产的确定性检查、语法/compileall/diff检查通过。实际runtime-probe.json仍blocked/退出2，缺Torch/流式后端/ffmpeg；没有加载模型。全量内第六阶段完整源码与系统剪贴板逐字节相同三次，且第五阶段包内容保持；均在隔离临时工作区。另跑final-copy-repeat3.txt专项3/3通过。

## 复审发现与中止记录

初版Python/真实HTTP/浏览器初检均通过，但进一步审查发现“新建库/删除库”等程序化切换可能沿用前一组授权勾选。没有放宽断言：新增源库绑定与选择变化失效机制，并覆盖新建/删除/切换/样本集合变化。旧全量已跑105项后中止，保存在browser-interrupted-consent-review.txt，不是全量通过；修正版另跑三轮。

## 仍未完成，不扩大解释

- 仍没有实际Qwen训练器/声学码提取/梯度或optimizer更新/检查点/双rank运行、训练与推理互斥模式。上述输入只是后续训练的可验证前置资产。
- 完整模型/双T4/DeepSeek/物理麦克风/ffmpeg压缩容器/音色/首声<3秒/RTF≤0.5没有验收。不能运行BF16/标准FA2示例或只加accelerate launch就声称T4训练完成。
- 格式首版有意严格；浏览器默认Opus录音通常不能直接生成训练快照，需后续受限解码器与真实容器验收或自行提供合规WAV。既有参考处理功能未移除。
- 准入按原始字节＋128KiB保守预留，可能提前拒绝；不以减少样本/截断音频回避预算。应用限额不是OS配额。损坏清单/未发布staging不假恢复；不是断电耐久或永久会话保证。
- 尚无外部训练进程的数据使用租约；不要在手动上游进程读取时删除副本。后续训练器须绑定固定版本并在运行期间阻止删除，不能从当前文件锁推断此功能已完成。
- 训练副本包含音频/私人转写，不进Git、不自动云导出，删除原始库不等于删除副本或历史Dataset中的既有档案锚点。
- 正式工作台只有5421字节余量，仍不放宽1MiB、不覆盖历史，本阶段独立文件交付。复制回归用隔离临时项目，不能称已发布正式工作台。
- 本阶段只可勾R1-079（记录授权声明）和R2-031（固定训练清单ID/内容哈希），累计21/300。R1-075只有训练输入具备格式/转写，原始库仍未解码；R2-032/采样器/实际rank覆盖等未完成，不勾选。第5题新增50建议，保留共250建议，不等于250项修复。

## 上游核对

https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/README.md

本次通过GitHub API再次读固定提交，核对单说话人audio/text/ref_audio及统一参考建议；没有执行上游训练脚本，也不把它的BF16/FA2示例当作T4可用证明。

---

## 内嵌备忘录：KAGGLE_STEP7_PLAN.md

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

---

## 内嵌备忘录：KAGGLE_STEP7_AUDIT.md

# 第七阶段审查：离线声学码事务与真实编码门禁

> 第七阶段冻结证据；当前源码/打包入口为step10，见KAGGLE_STEP10_AUDIT.md。以下统计保留当时结果，不代表实际GPU/编码/训练已验收。

2026-10-21。先保存KAGGLE_STEP7_PLAN.md与Q6的50条行动建议，再增量编码。**实现了调用真实Qwen tokenizer的本机入口与安全事务，但真实编码仍blocked；没有运行真实权重，没有训练。**

## 交付与已保留内容

- 独立`kaggle/kaggle-fixed-step7.py`：222808字节、35资产，SHA256 `3fe57769560c076d6d288a87cae6150b0a9404597eb0ea3997ab26de596f4cd0`。清单source_manifest_step7.json；repack.py默认生成step7。原始与step1–6冻结。
- 新增`py/training_codes.py`和`tools/encode_training.py`；`py/training_data.py`只增固定版本读取租约与删除互斥，既有准备/校验语义不变。没有新增HTTP路由/网页训练按钮；两主视图、命名库、逐条转写、授权隔离、旧快捷参考处理与全部工作台功能保留。
- 正式工作台仍15文件1043155字节/1MiB余5421字节，HEAD不变；独立交付，不提高容量、不删除历史、不直接改HEAD。复制测试仅在隔离临时项目。

## 实现与边界

| 范围 | 本次实现 | 不扩大解释 |
|---|---|---|
| 输入使用租约 | 先固定manifest SHA256并全量校验，再持有目录外`.use-{id}`文件锁；编码期间HTTP删除409，其他输入列表可读 | 合作式Linux flock，不是同UID恶意进程隔离；不修改快照文件集合 |
| 进程死亡 | SIGINT/SIGTERM/总期限停止worker进程组并必要SIGKILL；Linux PDEATHSIG与ppid握手覆盖控制器被强杀 | 生产编码器是单进程CPU线程；不是任意第三方外部进程的系统级沙箱 |
| 真实适配入口 | 懒加载Qwen3TTSTokenizer，CPU/FP32/eager/两线程、单条numpy float32/24kHz全波形 | 当前无Torch/qwen_tts/权重，真实适配只测了stub调用契约，未执行真实编码 |
| 模型固定 | 本地物化JSON/safetensors全文件内容树SHA256，≤512文件/128目录/4GiB/JSON每份≤1MiB；拒绝软硬链接、pickle、auto_map和越界分片索引 | 需可信来源预先固定hash；不是官方签名或权重真实性证明，不能防同UID恶意竞争写入 |
| 加载约束 | local_files_only/offline/trust_remote_code=false/use_safetensors，CPU与实际dtype/配置/特征采样率复核；加载前后及发布前重算模型hash | HF离线参数不是OS断网沙箱；运行时包版本仅记录，不宣称已校验其源码与上游提交完全一致 |
| 结果契约 | 恰好一个返回，ceil(输入帧/1920)行、16列、严格整数0..2047；全部样本顺序/逐条text/统一ref_audio保留 | 结构检查不证明声学码语义、还原音质或训练可用性 |
| 独立输出 | STATE/training_codes/{UUID}/复制全部WAV、rank_plan，写train_with_codes.jsonl和manifest；源输入可随后删除 | 复制会另占磁盘，删除源输入不删除码副本；没有外部训练读取租约 |
| 事务和预算 | 0700/0600，staging全核对后rename发布、失败回滚、下一写操作清理被杀遗留暂存；32份/64MiB单份/256MiB总量/256MiB余量 | 应用预算非OS配额；保守预留原输入大小+8MiB可能提前拒绝，不裁样本绕过限制；无断电耐久保证 |
| 状态 | 真实适配执行返回才可audio_codes_prepared/tokenization_executed=true；注入测试编码器强制test_only_codes/false | tokenization_verified/training/two_rank/inference始终false；不是文本tokenizer/优化器/检查点 |
| 隐私 | 不自动Dataset备份；公开收据不含私人转写或底层异常；子进程剥离已知HF/DeepSeek/Kaggle/访问凭据 | 原始输入/码JSONL确实含转写；本地可信操作员仍可读，临时操作目录并非安全擦除 |

## 本机使用约定

CLI没有Mock编码参数，不提供远程路径执行或下载/安装模式。请使用目标环境Python；以下是操作说明，**并非本沙箱已经执行的真实编码命令**。

1. 通过原有声音库窗口生成第六阶段输入，取得真实`id`和`manifest_sha256`。输入窗口状态仍是input_snapshot_ready，不因另有离线副本而修改其状态。
2. 准备可信来源的Qwen3-TTS-Tokenizer-12Hz本地完整模型，必须物化JSON/safetensors，不直接使用HF缓存软链接或包含README/其他文件的未整理目录。当前没有自动下载器或GPU依赖锁文件。
3. 对选定目录取树指纹，人工核对可信来源后固定；指纹只是变化检测，不证明这个模型属于官方。

```bash
ROOT=${QTTS_ROOT:-/kaggle/working/qtts}
STATE=${QTTS_STATE:-"$ROOT/state"}
python "$ROOT/tools/encode_training.py" fingerprint --model-dir "${MODEL_DIR:?设置可信本地模型目录}"
# 根据真实结果设置INPUT_ID、INPUT_MANIFEST_SHA256、MODEL_TREE_SHA256，不填虚构UUID或示例hash。
python "$ROOT/tools/encode_training.py" encode --state "$STATE" \
  --id "${INPUT_ID:?设置真实输入ID}" --manifest-sha256 "${INPUT_MANIFEST_SHA256:?设置固定输入hash}" \
  --model-dir "$MODEL_DIR" --model-sha256 "${MODEL_TREE_SHA256:?设置预先固定模型hash}" --timeout 1800
python "$ROOT/tools/encode_training.py" list --state "$STATE"
# 以下两个变量应来自本次真正输出，不能拿输入ID/hash替代。
python "$ROOT/tools/encode_training.py" verify --state "$STATE" \
  --id "${CODES_ID:?设置真实码副本ID}" --manifest-sha256 "${CODES_MANIFEST_SHA256:?设置码清单hash}"
# 确定没有手动训练读取后，才删除这个独立副本。
python "$ROOT/tools/encode_training.py" delete --state "$STATE" \
  --id "$CODES_ID" --manifest-sha256 "$CODES_MANIFEST_SHA256"
```

CLI超时允许1..3600秒，正常0，拒绝/blocked/失败/超时2，常规取消130。公开错误不包含库名/转写/原始异常。超时或取消恰逢rename之后、收据之前时，结果可能已经原子提交：先list及固定hash verify，不盲目重跑。父进程被SIGKILL可能来不及给收据；worker自动死亡释放租约，孤立staging在下次写入清理。

码输出JSONL仍使用audio/text/ref_audio及audio_codes；路径必须按**码副本目录作为cwd**解析，不能按原输入或启动命令cwd猜测。rank_plan仍是数学分配，不是两个rank实际运行。默认配置环境变量QTTS_MAX_CODE_DATASETS/QTTS_MAX_CODE_DATASET_BYTES/QTTS_MAX_ALL_CODE_DATA_BYTES；沿用既有上传音频边界。

输入租约并非训练器使用租约：未来真正训练还需阻止删除码副本，接入显存所有权/推理与训练模式、文本tokenizer/实际两rank/梯度/optimizer/checkpoint及重载试听。当前不自动停在线服务，不允许GPU编码参数。

## 分层验证（docs/validation/step7/）

- Python新增33项码事务/模型门禁/CLI/进程测试，加step6冻结回归，总146项。最终146×3＝438通过，python-round1/2/3.txt。包含真实fork租约、控制器SIGKILL、SIGTERM、超时、SIGTERM忽略的后代SIGKILL及pidfd死亡确认；没有真实模型执行。
- Go28顶层/16子测试race三轮；Node工作台API30×3通过。
- training-http3-final.txt：真实Go→analyst→磁盘三轮，新增本机租约阻止HTTP删除且列表可读，保留原输入篡改/独立副本/单独删除与原始库负向解码回归；不增加模型作业。
- codes-cli3.txt：真实本地CLI list/verify/delete与文件事务三轮，**码全为fixture**；原输入删除后码副本仍可校验。另用明确标注的无效fixture权重目录仅触发缺依赖门禁，三次blocked，未加载任何真实模型。
- mock-pipeline.txt：两CPU Mock worker三轮有序分段/取消恢复，非真实双T4。
- browser-repeat3.txt：60 QTTS＋47工作台＝107唯一×3＝321通过（11.5分钟）。包含第七阶段222808字节完整Python系统剪贴板逐字节一致三次且step6保持；final-copy-repeat3.txt另专项3/3通过。均为隔离临时项目。生产JS/HTML未改，不新增主视图。
- 确定性repack当前35资产/原始22哈希、语法/compileall/diff检查通过。runtime-probe.json仍blocked/退出2，Torch/流式后端/ffmpeg缺失，没有模型/GPU验收。

## 初检、复审和失败记录

1. python-initial.txt保留3个测试辅助错误：两处Fixture.reject不接关键字参数、Mock.poll始终活跃使二次清理消耗完预设wait序列。修正测试调用与真实退出顺序，不放宽业务断言。
2. python-review.txt保留一次异步SIGKILL尚未完成时立即读取/proc的竞态；改用pidfd有限等待确认实际死亡。
3. python-proc-reap-race-failure.txt保留最终第三轮一次/proc在exists与read之间被OS回收的ESRCH。仍必须pidfd死亡确认，然后接受已消失或Z/X；没有把活进程当成功。修正后全146项重新跑三轮。
4. 复审发现控制器被SIGKILL会使原独立会话worker继续执行，补Linux PDEATHSIG/ppid握手及实际强杀回归。初版浏览器已75次通过后中止，browser-interrupted-parent-review.txt保留，绝不计最终三轮；修正后重跑。
5. codes-cli-initial-helper-error.txt保留新增测试脚本误用LibraryStore.delete；核对实际remove接口后修正并重新完成三轮。仅测试助手错误，未改生产删库接口。

## 未通过项与下一步

- 码清单固定源输入ID/hash，但不复制原输入完整manifest；删除原输入后仍能核验码副本，却不能从中恢复完整的原库来源/声明资料。需要溯源时保留原输入清单；真正训练接入前须补完整来源/授权封存策略。
- 当前没有真实audio_codes产物、真实Qwen编码/解码/音质证据；本机入口不是模型验收。CPU速度、RAM峰值与目标依赖组合未实测。
- 仍无真实双T4训练、GPU资源模式、文本tokenizer、梯度/优化器更新、loss、检查点或训练后推理。CPU路径是保守前置，不是最终双卡性能方案。
- DeepSeek、物理麦克风、真实ffmpeg压缩容器、首声<3秒/RTF≤0.5/99.5%音色目标仍未验收，不用协议/fixture代替。
- 清单继续21/300，本阶段不增加GPU/编码真实执行勾选。专业自问自答6×50＝300建议，不等于300项修复。
- 下一步先实现可审计GPU资源所有权/推理与离线任务互斥，再在可用目标设备以可信模型完成单条真实编码/解码、完整覆盖、内存与耗时；之后才接文本tokenizer及真正两rank优化器和检查点。

## 固定上游依据

本轮通过GitHub API再次读取以下固定文件，仅核对源码未执行：

- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/prepare_data.py
- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/qwen_tts/inference/qwen3_tts_tokenizer.py
- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/qwen_tts/core/tokenizer_12hz/configuration_qwen3_tts_tokenizer_v2.py
- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/qwen_tts/core/tokenizer_12hz/modeling_qwen3_tts_tokenizer_v2.py

这里记录的是契约参考提交，不是当前尚未安装的运行时包源码身份校验。

---

## 内嵌备忘录：KAGGLE_STEP8_PLAN.md

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

---

## 内嵌备忘录：KAGGLE_STEP8_AUDIT.md

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

---

## 内嵌备忘录：KAGGLE_STEP9_PLAN.md

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

---

## 内嵌备忘录：KAGGLE_STEP9_AUDIT.md

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

---

## 内嵌备忘录：KAGGLE_STEP10_PLAN.md

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

---

## 内嵌备忘录：KAGGLE_STEP10_AUDIT.md

# 第十阶段：直接交付训练核心，真实Qwen/T4执行仍待验证

2026-10-21。回应用户“还有多久才能真正开始开发”：**核心开发本轮已经进行并完成实验性实现，不再等待下一轮基础设施。** 保存STEP10计划与Q9的50建议后，直接实现loss、反向传播、DDP、优化器与adapter保存。不能因为尚无目标硬件验收就说“还没开始开发”，也不能反过来把CPU算法测试说成Qwen训练成功。

## 1. 交付

- `kaggle/kaggle-fixed-step10.py`：261429字节、43资产，SHA256 `2bddd6ebad371268f9b3b02315fc29cae588da6c46c7d134476945b50b8a5ac4`。确定性重打包与source_manifest_step10.json匹配。原始与step1–9冻结。
- 新生产模块`lora_adapter.py`、`tts_dataset.py`、`tts_training.py`、`training_job.py`和入口`tools/train_tts.py`；派生dataset/联合loss保留上游Apache声明并附完整LICENSE-QWEN-DERIVED.txt。
- `training_codes.py`向受控rank导出/采用同一读取OFD，旧lease三元组API不变；`gpu_ownership.py`只新增显式offline模式adopt，推理默认仍拒绝offline租约。没有新语言、HTTP训练端点或假训练按钮。
- 生产网页/Go不改，两主视图及旧库/输入/码/认证/录音/复制保存回归。正式工作台15文件1043155字节及HEAD不变，独立交付，不提高1MiB或删除旧文件。
- 实际Kaggle操作与可取消Notebook代码见`KAGGLE_TRAINING_QUICKSTART.md`。目标环境/模型/数据就绪即可尝试本CLI，不以等待第十一阶段为条件。

## 2. 真正开发的内容与边界

| 功能 | 已实现 | 尚不能声称 |
|---|---|---|
| 真实训练目标 | talker codec0 CE＋0.3×sub-talker loss，16组码；speaker encoder冻结，统一参考embedding | 没有运行真实Qwen权重，不能说语义/音色学到或指标达标 |
| 文本/样本 | 固定上游助手格式/尾部处理与collate布局；完整文本、码、规范WAV参考mel；序列预算超限拒绝 | 未现场验证实际Qwen文本tokenizer和所有语言/长音频，不截断假装全覆盖 |
| 投影修正 | 使用talker.text_projection(get_text_embeddings(...))后再与codec相加 | 官方示例直接相加有维度风险；CPU测试故意使用6维文本/4维talker证明投影必要，但不冒充真实Qwen跑通 |
| T4候选策略 | FP16/eager，microbatch1，冻结Base1.7B；仅实际命中的talker/sub-talker self_attn q/v注入LoRA；A/B及AdamW状态FP32，非重入梯度checkpoint | 没有T4显存证据，不保证16GB、不称LoRA官方兼容已验收，也没有照搬BF16/标准FA2/全参AdamW |
| 双rank | 每rank一个显式CUDA设备、NCCL、120秒集合通信超时；整个参数相关loss在DDP.forward内，非经.module绕过 | CPU Gloo成功不等于NCCL/Qwen/真实双T4成功 |
| 梯度与更新 | 正确累积/尾组缩放、GradScaler、全rank有限loss检查、梯度同步/裁剪；任一rank梯度溢出则全体跳步/降scale；至少一次实际参数变化且两rank最终摘要相同 | 不把进程启动、loss打印、退出0或静态rank计划当训练成功 |
| 覆盖 | 每epoch固定seed打乱后按rank划分，奇数重复前缀补偶数，不drop_last；每rank每epoch保存见过ID，保存时核对全体选中覆盖 | 填充样本有明确重复，不假称无重复；真实数据质量/转写匹配靠操作者审阅，不是算法鉴定 |
| 检查点 | 原子保存adapter.safetensors、speaker.safetensors、Base/码pin/层名/覆盖/rank更新与版本、设备/峰值显存报告；load_adapter检查绑定/成员/hash/shape/finite | 是adapter候选，不是完整CustomVoice；不保存可恢复optimizer/scheduler/RNG状态，不自动部署聊天，也未Qwen新进程重载试听 |

源码对照固定上游`022e286b98fbec7e1e916cb940cdf532cd9f488e`的finetuning/dataset.py、sft_12hz.py和core/models/modeling_qwen3_tts.py。没有直接运行上游训练脚本；修正T4精度/优化器规模、DDP调用边界与文本投影风险。已验证的只是下面分层证据，实际包/API兼容仍需现场模型运行。

## 3. 准入、资源和退出

- 严格拒绝fixture、legacy-unsealed、非真实编码状态、少于两个样本或没有明确数据审阅/实验确认。审阅是用户声明，不把tokenization_verified等原始未验证标志变true，不替代法律/身份/语义鉴定。
- Base1.7B完整本地内容树固定hash，拒绝pickle/链接/远程代码/不完整或越界分片；Base内speech_tokenizer指纹必须等于所用码的encoder指纹。hash不是官方签名，需操作者可信来源。
- 父进程先固定码并持码租约，再持GPU整组offline-reservation OFD；两rank仅受控继承同一对FD并核对锁、inode/nonce、模式与固定码。码验证可在多rank同时进行，不依赖互相冲突的全局写锁。
- rank在Torch/CUDA前安装Linux PDEATHSIG并核对ppid，启动信号屏蔽窗口后解除SIGTERM/INT；父在Popen+记录PID窗口屏蔽取消，防丢刚启动的孩子。父死且孩子还活着时仍持OFD，最后引用才释放，不能删锁/PID/TTL抢占。
- 正常取消/总超时/单rank失败/第二rank启动失败，父停止并等待直接rank后才退租。timeout约束rank启动/加载/训练阶段，不含父进程前置指纹与收尾核验，并另有终止等待；不是全命令硬截止。DataLoader没有额外进程；不提供任意命令/外部进程训练器，不自动停旧推理或恢复模型。不是跨UID/容器/恶意同UID隔离，也不证明驱动显存已回收。
- request、rank日志/结果与adapter只在本地training_runs；目录0700、文件0600，Git忽略且原profiles-only备份不纳入。私有框架日志可能含路径/错误上下文，不能公开分享。正式CLI只输出控制器收据，不输出私人转写。
- 完成只说明两rank实际运行/覆盖/参数改变并保存adapter，quality_verified与inference_reload_verified仍false。没有checkpoint的双进程退出0明确失败；失败不替换旧推理模型。

## 4. 已执行证据（docs/validation/step10/）

### 真正的张量与算法测试，不只是Mock状态

- 新增25项训练核心/准入/进程测试，另加step9冻结回归；完整Python227×3＝681 PASS，`python-round1/2/3.txt`，没有跳过Torch测试。
- 小网络使用不同文本/talker维度和两级attention，实际计算联合loss、真实autograd/AdamW更新、冻结Base保持、FP16基座/FP32训练梯度、尾部累积、非有限loss/梯度拒绝/跳步、严格adapter保存/重载/hash篡改拒绝。
- 两个实际CPU进程使用torch.distributed/Gloo和DDP、不同样本分片；前后参数摘要改变，两个rank最终摘要完全一致，每epoch全样本覆盖。单元测试每轮都执行，另`trainer_tensor_check.py`独立三轮，完整摘要/loss/步数/分片在`gloo3.json`，不是Qwen权重或CUDA/NCCL结果。
- DDP日志提示find_unused_parameters=True在小网络没有unused，属于额外图遍历开销警告。真实Qwen尚未验证所有分支，暂保留诊断安全配置，不把警告隐去或宣称极致性能。

### 真正的OS进程与文件保护测试

- 实际Popen/pass_fds/OFD两CPU持锁者，父/孩子生死、取消/超时/第二启动失败、一个失败终止另一个、控制器SIGTERM/SIGKILL和pidfd退出观测；错inode/未持有FD拒绝，默认推理模式拒绝offline采用。生命周期测试内部注入CPU角色/绕过训练准入，仅测协议，生产CLI没有fixture训练开关，不能用它证明训练执行。
- 真实CLI fixture训练明确409且无training_runs创建；真实数据/模型依赖缺失返回blocked/拒绝，不产生训练成功。

### 原有功能回归

- Node API30×3、Go28顶层/16子测试race三轮PASS。真实Go→analyst→磁盘HTTP、旧编码CLI/fixture、supervisor受控FD/CPU角色、双CPU Mock流管线各三轮PASS，分别记录；没有GPU/真实音频质量或DeepSeek请求。
- 浏览器110唯一（60 QTTS＋50工作台）×3＝330 PASS（10.4分钟），包含step10完整复制/保留step9；最终复制专项另3 PASS（10.2秒）。均临时项目，不修改正式工作台，不推广成物理设备/Qwen训练/全浏览器验收。
- 原始22hash/当前43资产确定性repack、Python compileall、JS语法、diff检查PASS。最终`verify_delivery.py`核对原始至step9冻结、43资产、24完整内嵌备忘录、9题450建议、300项状态、所有最终日志/Gloo数值及正式15文件全部hash/HEAD，生成final-checks.json和formal-api-readonly.json。
- 沙箱新装Torch2.8.0+cu128、safetensors0.6.2、packaging25.0仅为CPU张量测试，不是Kaggle生产锁或GPU实测；runtime-probe仍blocked/退出2：CUDA不可用、qwen_tts/流式后端/真实权重缺失。没有模型下载/加载、Qwen训练或真实音频输出。

### 原始失败留存

首次17项核心测试中两个错误：夹具把manifest返回值顺序取反、safetensors.torch缺未声明的packaging依赖；修夹具/补可选CPU测试依赖后17 PASS。扩展生命周期时一项夹具reject不支持kwargs，改lambda后完整25项进入最终227三轮均通过。`training-core-initial.txt`、`training-core-expanded-initial.txt`保留对应失败，非伪造生产缺陷或隐藏中止。

## 5. 三轮各100项范围复审

300条状态映射保存review-map.json，依然22/300。这里是完整目标验收清单，不是开发完成度百分比。Q9新增50项建议，累计9题450建议。

- 第一轮100条：训练Core、LoRA目标、文本投影、Base/tokenizer绑定与包许可证有实际实现；但R1-011/018/064等真设备与模型试验仍阻塞，不将CPU结果套进T4项。
- 第二轮100条：R2-011/012/015/021/022/025/031/034等有真实算法/同步/采样/低秩优化与保存实现、CPU层证据；没有真实Qwen/NCCL/显存，R2-040没有新进程Qwen重载试听，均不夸大验收。R2-001/003/004没有自动推理↔训练切换。
- 第三轮100条：保持录音/两视图/编辑保存复制；小网络参数/adapter重载不等于真实音色/训练后聊天，也没有物理麦克风/DeepSeek/首声/RTF或99.5%身份结果。

## 6. 时间回答与接下来的直接核心目标

**何时开始核心开发：本轮已经开始并交付实验性训练代码。何时可以尝试开训：双T4、完整可信模型、授权真实数据及依赖就绪后即可执行当前CLI，不必等另一个基础设施阶段。何时训练成功/声音达标：未有现场数据，不能承诺小时数或日期。**

下一步直接围绕真实首步训练的错误/显存与adapter新进程重载、接入现有推理/聊天。不要再把收据/预约工具排成新的前置阻塞，也不要只增加训练按钮而后台仍做缓存。自动模式切换、可恢复训练状态、完整模型导出、GPU编码、UI进度/取消、真实质量与性能仍待实做。

---

## 内嵌备忘录：KAGGLE_TRAINING_QUICKSTART.md

# 现在怎样真正尝试开训：第十阶段 Kaggle 操作顺序

2026-10-21。**训练核心代码已开发，不需要再等下一轮基础设施；但本沙箱没有执行真实Qwen/T4训练。** 本入口是实验性Base1.7B FP16 LoRA双rank训练，不是完整成品。历史step10不接训练后聊天；当前step11已实现显式原生adapter推理/聊天接入，见KAGGLE_ADAPTER_QUICKSTART.md；仍无网页自动训练。

## 0. 先分清三个状态

| 状态 | 当前结论 |
|---|---|
| 实际loss/反向/优化器/DDP代码 | 已实现；真实CPU小网络/Gloo验证参数更新与跨rank一致 |
| Qwen1.7B在双T4上完成一个训练步 | 尚未运行；需要Kaggle双T4、可信完整本地模型和授权数据 |
| 训练后的声音可在现有网页直接选择聊天 | step11已接入显式选择候选，非自动覆盖；真实重载/试听/质量仍待验 |

不承诺首轮成功、16GB显存够用、训练耗时或音色相似率。首轮以1 epoch、microbatch1、短合法样本开始，记录真实结果后再优化。

## 1. 目标环境与升级

1. 在Kaggle启用双T4，实际运行`nvidia-smi`核对两卡与其他进程。平台开关不是设备证明。
2. 先停止本应用旧GPU服务，再解包当前step11到目标ROOT。仅检查用独立ROOT与`QTTS_UNPACK_ONLY=1`；这不等于实际启动。
3. 保留平台已有、与驱动兼容的PyTorch。**不要在Kaggle照装`requirements-training-test.txt`的Torch2.8/cu128沙箱测试轮子，更不要无条件升级/卸载CUDA库。**
4. 检查Qwen/transformers/safetensors等模型依赖并按可信上游要求准备。训练CLI不自动安装或下载；缺依赖会拒绝。沙箱没有验证完整目标依赖锁。
5. 挂载可信、完整且物化的`Qwen3-TTS-12Hz-1.7B-Base`本地目录，包含文本tokenizer、根safetensors及其索引/分片、generation config与`speech_tokenizer`。禁止pickle、远程Python代码、HF缓存软/硬链接；不能只放空config或假权重。可读README/许可证不代表模型权重可信。

参考实现固定来源：
- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/dataset.py
- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/sft_12hz.py
- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/qwen_tts/core/models/modeling_qwen3_tts.py

没有照搬BF16/标准FA2/全参数AdamW；训练器修正文本嵌入到talker隐藏维度的投影，并把完整联合loss放在DDP.forward内。派生代码保留Apache声明，包内附LICENSE-QWEN-DERIVED.txt。

## 2. 真实数据与声学码

- 在已有命名库/输入准备流程提供自己有权使用的同一说话人音频和逐条匹配转写，完整24kHz mono PCM16 WAV；统一参考≤16秒。首轮至少两个不同样本，建议短样本，不接受fixture或旧未封存码。
- 使用原有`encode_training.py`对实际输入固定manifest hash进行真实CPU声学编码；模型目录应取该Base内`speech_tokenizer`的同一物化内容树。CPU编码可能慢，不能据此保证速度。
- `encode_training.py list/verify`读取实际结果。仅schema2且state=`audio_codes_prepared`的真实编码可进入训练；`test_only_codes`或`legacy-unsealed`明确拒绝。
- 结构一致不证明转写/说话人/内容适合训练。训练前由操作者实际检查这些内容与使用权；CLI显式确认不等于机器语义验证或法律鉴定，源码清单原验证标志不会自动升级。

## 3. Notebook内调用：不填写虚构ID，不在命令写密钥

先在私有Notebook中设置以下**真实非密钥路径/ID**环境变量：
- `QTTS_ROOT`：已解包当前step11源码根目录；
- `QTTS_STATE`：当前本地状态目录；
- `QTTS_BASE_LOCAL`：可信完整Base1.7B物化目录；
- `QTTS_TRAIN_CODES_ID`：从当前list结果选定的真实码版本ID。

下面代码读取真实list并取对应固定hash，不猜第一个版本、不自动选择别人的音频。变量没设置会明确失败；不要将私人转写或密钥粘贴到共享报告。

```python
import json, os, subprocess, sys
from pathlib import Path

ROOT = Path(os.environ['QTTS_ROOT'])
STATE = Path(os.environ['QTTS_STATE'])
BASE = Path(os.environ['QTTS_BASE_LOCAL'])
CODES_ID = os.environ['QTTS_TRAIN_CODES_ID']

def cli(tool, *arguments):
    output = subprocess.check_output(
        [sys.executable, str(ROOT / 'tools' / tool), *map(str, arguments)],
        text=True,
    )
    return json.loads(output)

versions = cli('encode_training.py', 'list', '--state', STATE)['result']
matches = [v for v in versions if v['id'] == CODES_ID]
if len(matches) != 1:
    raise RuntimeError('指定的真实码版本不存在；先检查当前list结果')
selected = matches[0]
if selected['schema'] != 2 or selected['state'] != 'audio_codes_prepared':
    raise RuntimeError('拒绝fixture或未封存历史码；先完成真实声学编码')
CODES_SHA = selected['manifest_sha256']
cli('encode_training.py', 'verify', '--state', STATE,
    '--id', CODES_ID, '--manifest-sha256', CODES_SHA)
BASE_SHA = cli('train_tts.py', 'fingerprint', '--model-dir', BASE)['base_model_sha256']
```

再次检查真实推理服务已停止、合作锁空闲，并用`nvidia-smi`检查显存。锁空闲并不证明显存空闲；不要删除fleet.lock或按旧PID强行抢占，不会自动停推理。

**只有亲自完成数据/权利审阅并接受实验风险后，才执行以下训练调用。** 它会真正尝试加载模型和进行优化，不是无副作用的演示：

```python
command = [
    sys.executable, str(ROOT / 'tools/train_tts.py'), 'train',
    '--state', str(STATE), '--id', CODES_ID, '--manifest-sha256', CODES_SHA,
    '--model-dir', str(BASE), '--model-sha256', BASE_SHA,
    '--epochs', '1', '--accumulation', '4', '--max-sequence', '1024',
    '--lora-rank', '8', '--lora-alpha', '16', '--lr', '0.00002',
    '--timeout', '1800', '--confirm-data-reviewed', '--ack-experimental-training',
]
process = subprocess.Popen(command, text=True, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, start_new_session=True)
try:
    stdout, stderr = process.communicate()
except KeyboardInterrupt:
    process.terminate()  # 向本次持有的控制器对象取消，不查旧PID文件
    stdout, stderr = process.communicate(timeout=15)
    print(stdout)
    raise
print(stdout)  # 仅控制器收据，不输出完整私人转写
if process.returncode != 0:
    raise RuntimeError('训练没有完成；检查本机私有training_runs收据/日志，不要标记成功')
receipt = json.loads(stdout)
```

两rank必须各有实际设备、更新参数且最终adapter摘要相同，全部选中样本覆盖，才会保存adapter；奇数样本采用重复打乱序列前缀补偶数，报告保留重复ID，不drop_last。序列超预算整份拒绝，不裁掉文本/音频。timeout包含rank启动/模型加载/训练，不含父进程前置指纹/收尾核验，终止另有等待；未承诺30分钟足够，也不是全命令硬截止。

## 4. 结果、取消与下一步

- 本地`STATE/training_runs/<job_id>/`有request、每rank私有日志/JSON、result；成功有`adapter/adapter.safetensors`、`speaker.safetensors`、manifest。
- 私有日志可能包含框架路径/错误上下文，不要公开粘贴。请求/音频/文本/adapter不进Git，不自动Dataset备份；删原库不等于删输入/码/训练副本。
- 正常完成返回0，失败/拒绝/总超时2，控制器SIGTERM/INT取消130。Notebook仅中断`subprocess.run`不保证自动向孩子发受控取消；长训练应保留明确的Popen对象，向该控制器发terminate并wait，不按陈旧PID发信号。父SIGKILL也有rank PDEATHSIG与共享FD最后引用保护。
- 不支持恢复optimizer/scheduler/RNG训练状态；当前adapter是推理候选，不是完整可恢复训练检查点或CustomVoice模型。中止/失败不覆盖旧推理模型。
- `tts_training.load_adapter(core, checkpoint, base_directory)`严格检查Base绑定/文件hash/层与张量后挂载LoRA，返回保存的统一参考speaker embedding。须单独加载同一Base、按Base克隆prompt协议接入，并用新进程真实合成/试听；当前没有网页自动部署，不能把CPU小网络重载当Qwen验收。

**多久能开始：代码入口现在已有；真实环境与数据就绪即可尝试，不依赖另一个开发阶段。多久训练成功/达到目标音色：目前没有可靠实测，不能给出保证。** 下一开发重点是现场首步故障修复和训练adapter接入现有推理/聊天，而不是继续追加封存工具。

---

## 内嵌备忘录：KAGGLE_STEP11_PLAN.md

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

---

## 内嵌备忘录：KAGGLE_STEP11_AUDIT.md

# 第十一阶段审查：训练adapter已接入原生推理及现有聊天

2026-10-21。先保存STEP11计划及专业问题10的50建议，再写实现；不向用户重复提问。**这是实际接入代码，不是再做一轮训练准备工具。** 当前无真实Qwen/T4权重、CUDA和外部DeepSeek实验，硬件/音质门禁不升级。

## 1. 交付与选择

- `kaggle/kaggle-fixed-step11.py`：276043字节/46资产，SHA256 `cd5346e8ae34f1e2db327a076a7411996982848f9d4e14236f05d94c626d496e`，`source_manifest_step11.json`对应当前source；repack默认step11。
- 原始至step10冻结；step10仍261429字节/43资产、SHA256 `2bddd6ebad371268f9b3b02315fc29cae588da6c46c7d134476945b50b8a5ac4`。不覆盖旧可运行路径、不改正式满额15文件工作台。
- 不猜faster私有对象/CUDA graph支持动态LoRA。保留默认faster路径；显式`QTTS_TTS_ENGINE=qwen-adapter-buffered`启用官方原生推理，**句级缓冲，不是声学流式**，不混驻两种模型或完整Base副本合并。
- 完整目标审查300条仍22项已验，不是开发完成百分比；10题×50=500建议，不是500项已实施修复。

## 2. 具体代码

| 位置 | 已实现 | 不能推导 |
|---|---|---|
| `trained_profiles.py` | 严格完成run/request/result/manifest交叉核验；固定Base/码pin；两NCCL-shaped rank更新及每epoch样本覆盖记录；限定成员/文件大小/hash/tensor digest/FP32/finite；发布持原码租约，复制统一参考WAV和匹配转写 | 本地记录不是官方签名或同UID恶意造记录的防护；声明不是法律/身份证明 |
| `tools/trained_voice.py` | describe取真实pin，publish要求显式run/pin/自命名与未验收确认；不自动active，不输出私人文本或原始模型路径 | 发布不是训练，不证明声音相似或重载完成；不是GUI训练按钮 |
| `lora_adapter.py` | 全量验证/构造replacement后事务提交，可不同rank切换，提交异常回滚；保持原Base模块，不重复叠挂旧LoRA | CPU输出恢复不是Qwen语音可听一致性或CUDA内存适配 |
| `adapter_engine.py` | 本地Base前后指纹、CUDA单可见卡、Base1.7B FP16/eager；每段核对绑定/adapter，不每句重新hash多GB Base；保存speaker直接生成官方x-vector-only prompt | 实际config的base/1b7/16组及版本/停止条件行为仍须真实权重验证；无模型或T4显存证据 |
| `worker.py` | 显式引擎选择，Mock/默认拒绝trained profile，原生拒绝普通profile；锁内切换/生成，原生单wave转既有PCM帧；取消后丢迟到wave，错误无Base回退 | 停止播放/AR stopping不能中断CUDA kernel/codec decode；错误不等于立即清除GPU任务 |
| Go调度/监督 | 原生无帧/health/supervisor预算180秒；默认60/75/90秒不变。继续有序切段、HTTP/SSE、双worker与原activate门禁 | 预算不是延迟承诺，不保证任意长句180秒可完成 |
| 网页/analyst | 选择器/档案/health标注训练候选、句级缓冲、未验收；参考只读，编辑/校准409；旧普通档案操作及删除保留。修复一致性检测全失败仍可能consistent=true | 比较指标不是人工试听、身份或质量验收；没有新增第三主视图 |
| bootstrap/probe | native检查官方Qwen接口，不要求faster包；固定本地Base，不预下载陌生模型；缺依赖blocked，不自动更换引擎 | API形状通过不是模型运行；Kaggle完整安装/启动路径仍待实机执行 |

## 3. 数据与失败边界

- 新profile仍沿旧profiles私有Dataset备份语义，含一段统一参考WAV及对应文本；run/全体训练数据/完整Base不自动备份。操作说明明确告知，不把音频/权重/私密状态进Git。
- 发布时依赖原码固定版本；运行推理需要同一Base和run/adapter。恢复缺adapter/Base必须明确失败，不用参考缓存或Mock输出冒充训练声音。删原码、原库、profile、run和远程备份是不同操作。
- 训练profile绑定固定版本，不自动修改原有active。两worker均确认才改变active，某卡失败保留active；个别worker可能已加载另一adapter，但下一次请求会按其profile在同一锁内重新选择，不能把一次load当后续永远正确。
- 原生一条文本完整生成后才yield一个wave，要求24kHz mono/有限/非空/非全零/长度预算。后处理、停顿与flush产生多个PCM帧不构成声学流式证据。首个真实语音包时间仍由模型wave返回后计算，不能拿预置停顿冒充TTFA。
- 失败切换保留原adapter对象和prompt，但错误请求不得调用原adapter生成；绑定/文件损坏即报错。Base仅加载期固定指纹，后续内存/文件任意同UID恶意修改不属于隔离保证。

## 4. 本轮已执行的验证

- Python完整252×3=756 PASS，38.129/37.891/36.272秒：包括24项新adapter测试和旧训练/存储/访问控制/包/录音契约。真实CPU LoRA数学证明A/B输出不同、A→B→A精确恢复、不同rank、失败预构造不半写、两worker对象隔离。CPU Gloo小网络训练在三轮完整suite内实际运行，不是Qwen/NCCL。
- `adapter_gateway_check.py`：真实本机Go网关/HTTP/SSE、两个独立worker进程、CPU tiny LoRA+注入官方API形状的生成替身，3轮A→B→A，通过真实聊天切段/帧有序与句级缓冲stats；损坏第二版本后activate 503、原active保留，两worker错误请求无PCM。SSE和wave是本机替身，**不是真实DeepSeek、Qwen声音或NCCL**。
- Go race count=3 PASS；Node30×3 PASS。
- 既有ownership_process_check、training_gateway_check、codes_cli_check、mock_pipeline各调用3次，每次内置3轮，均PASS（各9轮CPU/协议，不是9轮GPU验收）。
- 浏览器112×3=336 PASS（11.0分钟）：新训练候选标注/只读/按钮/现有聊天选择/诊断、全量旧录音/存储/安全/视图及包复制均保留。最终包额外逐字复制3/3 PASS（10.0秒），`final-copy-repeat3.txt`与最终`final-checks.json`留证，不用网页截图冒充目标模型证据。
- native runtime probe **blocked/退出2**，model_loaded/inference_verified/training_verified/performance_verified均false。沙箱Torch2.8+cu128仅CPU测试，CUDA不可用，无qwen_tts或真实权重，不是Kaggle依赖锁。

## 5. 失败记录与修复

1. 新浏览器测试首轮1失败/1通过：默认处于语音对话，测试未进入录制参考视图就用可见role找档案按钮。补显式视图切换，2/2通过；`browser-initial.txt`保留，不删失败。
2. 完整Python首轮248测试1失败：旧探针AST测试仅期望faster调用，新增native接口后不再覆盖两引擎。修正为分别核对两份真实调用关键词集合，并补全native sampling参数探针；`python-initial-failed.txt`保留。扩展后252×3全通过。
3. shell曾用错误工作目录调用仓库相对路径和错误gofmt位置；未更改生产代码，改用仓库根/已安装Go实际路径，最终编译/race通过。不是目标Qwen故障或被隐藏的模型成功。

## 6. 三轮各100项建议复审与后续

`review-map.json`逐条保留300条原始建议/目标、当前证据关联与阶段行动，按源码环境、模型音频、系统交互三组100条审查。新增修复以本报告代码表为准，不把300个范围映射当300个新缺陷或已修复条目。完整目标22/300保持，真实权重/GPU/音质/性能未勾选。

下一项直接到真实Kaggle：先小数据真实首个优化步/峰值显存，完成run后在**新进程**按pin加载、每GPU保存和试听WAV、A/B/A、真实DeepSeek长回答/停止恢复，分别记录句级缓冲首声及默认faster声学流式。按KAGGLE_ADAPTER_QUICKSTART.md执行，不增加另一个工具前置阶段，不承诺成功日期、16GBfit、<3秒、RTF或99.5%身份相似率。

---

## 内嵌备忘录：KAGGLE_ADAPTER_QUICKSTART.md

# 第十一阶段：训练adapter → 命名声音 → 现有聊天

2026-10-21。**接入代码已实现，真实Qwen/T4训练、重载及试听未验收。** 原有faster声学流式路径不改；新后端是官方Qwen原生API，**句级缓冲，不是声学流式**。没有新增第三个主视图或假训练按钮。

## 1. 前提与模式边界

- 使用`kaggle-fixed-step11.py`，先停止旧GPU服务再解包到自己的ROOT；可用`QTTS_UNPACK_ONLY=1`仅解包，不代表启动成功。原始到step10均保留。
- 依照`KAGGLE_TRAINING_QUICKSTART.md`，真实完成一个schema2实际编码输入的双rank训练，取得`result.json`中的**实际job_id**。failed/timeout/cancelled/缺检查点、fixture/旧未封存码不能发布。
- 保留训练run下request/result/adapter三件套和原码版本；发布时会持原码租约验证并读取统一参考。不要猜某个目录名或自动选第一个run。
- Base必须是训练使用的同一可信、物化完整本地Base1.7B，hash固定。禁止pickle、remote code与HF缓存链接。目标依赖仍需自行审查，不把沙箱Torch2.8/cu128测试轮子照装到Kaggle。当前代码严格检查base/1b7/16组契约，真实权重config尚未核验；如不一致应对照真实config修正代码，不能改元数据伪造通过。
- 原生启动要求已有官方`qwen-tts`、`safetensors`及兼容依赖，不自动用未知版本替换引擎。与faster的CUDA graph注入兼容性未验证，所以**不向faster动态注入LoRA，也不离线合并并复制完整Base**。
- 每个worker仅一个可见GPU、一份Base；由既有supervisor分配GPU0/1。CPU接口替身测试不是这两卡已运行的证据。原生模式只接受训练候选，普通参考档案仍保留，但要使用原有faster模式；不在同一个worker里混驻两种模型。

## 2. 显式发布，不自动激活

在私有Notebook中设置自己真实的`QTTS_ROOT`、`QTTS_STATE`和`QTTS_TRAIN_RUN_ID`；最后一个来自本次成功训练收据。下面使用实际记录读取hash，不填写虚构ID。

```python
import json, os, subprocess, sys
from pathlib import Path

ROOT = Path(os.environ['QTTS_ROOT'])
STATE = Path(os.environ['QTTS_STATE'])
RUN_ID = os.environ['QTTS_TRAIN_RUN_ID']

def voice_cli(*args):
    output = subprocess.check_output(
        [sys.executable, str(ROOT / 'tools/trained_voice.py'),
         *map(str, args)], text=True)
    return json.loads(output)['result']

record = voice_cli('describe', '--state', STATE, '--run-id', RUN_ID)
```

亲自确认该run及数据来源、权利和实验风险后，设置自己要显示的`QTTS_TRAINED_VOICE_NAME`，再执行：

```python
published = voice_cli(
    'publish', '--state', STATE, '--run-id', RUN_ID,
    '--adapter-sha256', record['adapter_manifest_sha256'],
    '--name', os.environ['QTTS_TRAINED_VOICE_NAME'],
    '--ack-unverified-adapter')
print(published)
```

输出profile_id、pin和`active_changed=false`；音质/现场重载验收标志仍false。**发布不是训练，不会替你启动模型、证明音色相似或自动启用。** 完成记录与声明只是同UID合作流程记录，不是官方加密签名/法律证明，也不能防同UID恶意伪造整个训练目录。

发布会把一段统一参考WAV及匹配转写复制进现有profiles目录；该目录**沿旧私有Dataset备份语义**，启用原有备份后可能上传这些内容。训练run、所有训练样本和完整模型不会因此自动云备份。删除原库不等于删profile或远程备份；删除profile也不自动删除run。备份恢复若缺少对应run/adapter/Base，新后端必须报错，不会换成原Base或另一声音。推理只读取已固定的adapter记录，原码仅是发布时依赖；删除原码后，已发布profile仍需单独管理。

## 3. 原生后端启动

先按既有所有权协议停止自己旧推理任务并确认相关rank已结束；不要删除锁或拿旧PID盲杀。`nvidia-smi`另查真实显存，合作锁不证明设备空闲。

设置`QTTS_BASE_LOCAL`为同一完整本地Base，并在**新启动进程环境**中选择后端：

```python
runtime_env = {
    **os.environ,
    'QTTS_ROOT': str(ROOT),
    'QTTS_STATE': str(STATE),
    'QTTS_MODEL': str(Path(os.environ['QTTS_BASE_LOCAL'])),
    'QTTS_BASE_SHA256': record['base_model_sha256'],
    'QTTS_TTS_ENGINE': 'qwen-adapter-buffered',
    'QTTS_MOCK': '0',
    'QTTS_DTYPE': 'fp16',
    'QTTS_TUNNEL': 'none',
}
runtime_env.pop('QTTS_UNPACK_ONLY', None)
runtime_env.pop('QTTS_ALLOW_SINGLE_GPU', None)
subprocess.run([sys.executable, str(ROOT / 'py/bootstrap.py')],
               env=runtime_env, check=True)
```

这会真正尝试加载模型及运行既有服务，不是无副作用检查；仍需检查目标环境工具链与启动日志。Secret使用既有私有配置，不在共享命令/报告里输出。先本地验证，再决定是否启用公网隧道。bootstrap的实际依赖/编译安装路径尚无Kaggle现场验收，不承诺启动耗时。

新后端在加载前后核对Base树hash，仅启动时读完整Base；每次声音使用核验profile binding、run状态及adapter成员/hash/张量摘要，不每句重新hash多GB的Base。它加载官方eager/FP16，不复用faster图；使用保存的speaker embedding构造x-vector-only prompt，而不是重算一个无关参考或伪装成完整CustomVoice。

## 4. 现有界面选择与对话

1. 打开原有控制台并解锁；只有“录制参考语音 / 语音对话”两主视图。
2. 声音列表显示“训练候选/句级缓冲/未验收”。在档案卡片点“选择此训练版本（双GPU加载，句级缓冲）”。两worker必须确认加载才改变active；某卡失败不把界面标成启用成功。
3. 训练参考文本只读，保存文本/候选校准禁用，后端同样返回409；要变更训练条件请另做明确训练版本。删除入口保留。
4. 先用直接朗读短句测试，再用现有DeepSeek流式文字与语音聊天。网关仍切段、双worker调度、有序转发及播放停止；声音选择使用当前profile_id。
5. 原生API一段文本生成并解码完成才给出一个wave；Worker后处理的PCM尾部/停顿帧不意味着模型声学流式。诊断health、Worker stats标注`sentence-buffered`。首声可能明显慢于faster，不承诺<3秒/RTF/16GB适配。
6. 取消传入Transformers stopping criteria；取消后丢掉迟到完整wave。停止语音播放不等于立即终止正在执行的CUDA kernel/codec decode；下一请求可能仍需等worker释放锁。
7. 原生无帧等待/健康stall/监督重启预算180秒，旧faster分别保持60/75/90秒；这只是保护预算，不保证任意长句180秒完成。超时不能改成“通过”。

切回原有普通参考声音：先正常停止自己原生服务，再以`QTTS_TTS_ENGINE=faster`启动原有模式。原生模式拒绝普通profile，faster/Mock拒绝训练profile；没有自动卸载再偷偷换引擎的路径。

## 5. 必须现场填写的验收

- 双T4实际设备、每worker唯一GPU与各自一份Base、真实峰值显存；先一个小训练步，检查权重变化与跨rank一致。
- **新进程**按固定pin重载同adapter；每GPU输出真实24kHz WAV，确认非空/有限/非全零，盲听参考与输出，不把CPU oracle或profile文件当试听证据。
- 两个已训练版本A→B→A、同文本同seed及不同文本；损坏/缺失绑定必须明确失败，不能输出原Base冒充训练声音。
- 真实普通路径回归、DeepSeek回答中途切换/取消、长回答有序播放、耳听断句和爆音；测首个真实语音包及完整延迟，明确句级缓冲。
- 没有真实Qwen/T4运行、物理音频及外部模型可用性证据时，上述项保持“待验收”。当前下一步就是这组真实运行，不增加工具前置阶段。

---

## 内嵌备忘录：KAGGLE_STEP12_PLAN.md

# 第十二阶段：依据Kaggle现场日志修复Mimi/RoPE兼容与启动重启风暴

2026-10-21。先保存计划与Q11，再写实现；原始至step11冻结。用户已实际识别两张Tesla T4，Python3.12.13/Torch2.10.0+cu128/faster0.5.4/Transformers5.20.2，模型加载报MimiConfig.rope_theta，尚无加载/推理成功证据。

1. 审查PyPI实际wheel：faster0.5.4要求qwen-tts-hf>=0.1.1.post1和Transformers>=5.15.1，不能只降Transformers到4.x造成依赖冲突。qwen-tts-hf兼容函数仍读取config.rope_theta，现代Mimi使用rope_parameters。
2. 在原实际依赖组合上做最小、可拒绝、不猜theta的兼容桥：仅包装已识别Qwen默认RoPE函数；从现代Mimi配置真实rope_parameters读取theta，对临时config副本提供旧字段，不改模型权重/config文件、不把theta统一硬编码为10000、不改非默认scaled RoPE。
3. Worker/CPU编码/原生推理/训练的Qwen加载前接入；前置探针增加真实MimiConfig+Qwen默认RoPE CPU数值smoke，早于权重加载，不再只验签名。固定faster/hf/transformers已审查三版本，保留平台Torch/CUDA，不盲降/升级。
4. 不兼容异常标fatal，supervisor停止该worker而非反复重启；bootstrap看见fatal及启动失败时清理它自己创建的supervisor，保留合作FD直到子退出。不给旧日志PID发盲杀命令。
5. 两worker继续分别只看GPU0/1，健康报告真实设备/驻留状态；模型加载成功后保持常驻，不自动空闲卸载。验证是假设备/CPU替身时不能说双T4模型成功。Kaggle会话/硬件回收不受应用控制，不承诺永久GPU。
6. 新step12包与浏览器复制页面更新，step11冻结；给用户明确“停止并重启完整Kaggle会话后复制新包”，不是仅刷新网页/重跑旧cell。
7. 真实wheel配置复现与修复数值对照、负面配置、旧接口不变、fatal控制器/双卡分配/源码复制及已有回归三轮；完整Qwen/双T4仍需用户目标再次运行验收。

---

## 内嵌备忘录：KAGGLE_STEP12_AUDIT.md

# 第十二阶段：根据Kaggle实际日志修复MimiConfig.rope_theta

2026-10-21。先保存STEP12计划与Q11的50项建议，再写实现。原始至step11冻结；这次直接修用户已遇到的模型加载故障，不另设训练准备阶段。

## 1. 现场事实与诊断

用户日志显示：Python3.12.13、Torch2.10.0+cu128、faster-qwen3-tts0.5.4、Transformers5.20.2；两张Tesla T4、计算能力7.5、每卡总显存15636037632字节。依赖探针形状通过，Go/Rust编译和模型下载完成；随后两worker均报`AttributeError: 'MimiConfig' object has no attribute 'rope_theta'`并被监督器重启。**这些日志证明到达模型加载并失败，不证明模型已常驻或推理成功。** HF未登录警告不是此次核心异常。

读取实际PyPI wheel与元数据后确认：

- faster0.5.4依赖`qwen-tts-hf>=0.1.1.post1,<0.2`及`transformers>=5.15.1,<6`。不能只把Transformers降到4.x，那个组合违反依赖。
- qwen-tts-hf0.1.1.post1共享`qwen_tts`命名空间，其中`_transformers_compat._default_rope_parameters`仍直接读`config.rope_theta`。
- Transformers5.20.2的实际MimiConfig已使用`rope_parameters`，不存在该旧属性。默认配置及旧`rope_theta=12345`输入都被规范化到现代字典。
- CPU中使用**实际TF5.20.2类+实际Qwen-HF wheel函数**复现同一个AttributeError，修复后检查10000/12345/1000000三个theta的精确频率及原配置不变，通过三次独立进程。未构造完整Qwen、未载权重、未用CUDA。

来源与许可证：
- https://pypi.org/pypi/faster-qwen3-tts/0.5.4/json
- https://pypi.org/pypi/qwen-tts-hf/0.1.1.post1/json
- https://pypi.org/pypi/transformers/5.20.2/json
- Qwen函数来源`qwen_tts/_transformers_compat.py`，Apache-2.0。新桥接调用原函数，不把整份第三方实现混写进新模块；包内原Apache许可保留。
- 实际Qwen-HF wheel SHA256 `ed5b7aae64cf795243369fb5226173f459a45689ea86db1c6d3eb14fc0c2c01d`，所用成员SHA256 `033673335ed7bcb19054cdabc6c8400e443493f4b54340f8f449577d122bf982`。三项完整requires_dist/wheel digest记录在step12证据目录。

## 2. 实际修复

| 部分 | 改动 | 边界 |
|---|---|---|
| `qwen_compat.py` | 仅包装已识别Qwen默认RoPE函数；从真实现代配置读theta/partial factor，用临时config副本传给原函数；重复安装幂等、第三方覆盖/非法值/未知scaled schema拒绝 | 不给所有Mimi硬加property、不写死10000、不修改权重/config文件、不假称修复所有5.x版本 |
| Worker/原生/CPU编码/训练 | 导入Qwen后、加载模型前安装桥；保留原Base/LoRA、现有码/授权与质量标志 | 其他未见过的真实模型错误仍可能出现；实际完整加载须再运行 |
| 预检 | 新`qwen_mimi_rope_cpu`：实际MimiConfig、实际Qwen默认函数的CPU数学smoke，明确NO model/GPU；HF/官方provider检查可区分命名空间 | 解决此前只验签名而漏配置错误的缺口，但不能把smoke当完整模型通过 |
| 依赖 | 固定faster0.5.4 / qwen-tts-hf0.1.1.post1 / TF5.20.2三个直接版本；安装时对已装Torch/torchaudio/torchvision加版本约束；缺平台Torch拒绝替换；官方/HF重叠命名空间拒绝 | 不是完整环境锁，不保证Kaggle所有现有包无冲突；不强制升级/卸载CUDA库或照装沙箱Torch |
| fatal控制 | 已知rope_theta AttributeError及明确兼容异常标fatal；supervisor停止该worker重试，并原子写当前启动nonce绑定的失败记录 | transient错误仍保留有界重试；不按旧日志PID或模糊名称盲杀 |
| bootstrap清理 | 看见fatal健康/当前nonce收据立即结束等待；失败/异常/中断时只停止自己创建的supervisor Popen；等待其正常清理直接children和FD | 45秒未确认会明确要求停止完整Kaggle会话，不删除锁或假称所有GPU已空闲 |
| 会话驻留 | 默认QTTS_RESIDENT=1，保留每worker单GPU0/1映射；不在600次请求或旧13.5GB门槛主动回收模型，显存高只告警；显式0保留旧策略 | CUDA empty_cache不释放活模型权重；OOM、真实错误/服务重启/平台回收仍可打断，不保证永久会话 |
| health | requested_model、model_loaded、cuda_visible_devices、fatal_error、residency_policy | Mock明确不报真实model_loaded，requested_model不是权重内容签名；不把GPU映射配置说成现场模型成功 |

## 3. 交付与验证

- step12：`kaggle/kaggle-fixed-step12.py`，282031字节/47资产，SHA256 `2be33a3a6735639ce32ec8750e9a489abd96e4daa780d068557f2b0156f2de08`，独立包与source_manifest_step12.json。原始至step11冻结。
- 浏览器复制预览3001已换step12，代码和下载来自固定hash的完整包，不动原3000工作台及15文件/HEAD。
- 新14项兼容/控制/驻留/安装约束回归已通过；完整Python267×3=801 PASS，含原有训练/实际CPU小网络Gloo、访问控制、存储、包与adapter回归；Node30×3及Go race count3 PASS。
- 既有所有权真实进程/HTTP输入/本机码CLI/Mock管线/Go+SSE+双worker adapter替身各三轮PASS。新增真实supervisor+CPU fatal-health进程三轮，验证当前nonce收据、bootstrap提前失败、所属supervisor及worker退出、PID运行标记移除；不是GPU实验。均非真实Qwen/NCCL/DeepSeek联网；不把已有CPU链路替身算作GPU重载。
- 真实wheel配置数学三进程PASS；完整浏览器113×3=339 PASS，另最终step12包逐字节复制三轮PASS。真实Chromium复制页三轮剪贴板精确一致、下载文件名/内容哈希一致、拒绝授权时全选/手机375px无横向溢出、正式15文件不变，详见copy-page.json与final-checks.json。
- 三轮各100条建议/目标复审见review-map.json。完整目标仍22/300；11题550建议不等于550实现或300修复。当前只新增用户真实双T4识别/加载失败证据，不升级目标推理/质量项。

## 4. 保留的失败与未执行内容

- 首次独立CPU target环境同时存在旧tokenizers/hub dist-info，TF版本检查拒绝；删除该隔离cache中的旧元数据后，真实CPU复现与修复通过，初始错误日志保留。未修改主测试venv或用户Torch。
- 完整Python初轮267中1失败：旧native探针测试强制要求官方qwen-tts发行包，实际HF provider也可提供命名空间。改为显式provider组门禁及对应断言，随后完整三轮通过；初始失败日志保留。
- 新fatal进程脚本初次漏传子进程PYTHONPATH导致找不到supervisor模块；修正测试环境后实际三轮通过，初始日志保留，不是生产模型故障。
- 沙箱CUDA不可用，没有实际两T4或完整模型权重，完整Qwen导入/加载、warmup、声音、峰值显存和性能仍须用户新包复跑。配置层成功不是整个模型已保证可运行。

## 5. 给用户的直接操作与下一门禁

见KAGGLE_STEP12_QUICKSTART.md。先备份所需私有数据，再停止并重新启动**完整Kaggle会话**，不是只重启内核/刷新网页；默认T4×2/Internet On/非Mock，从浏览器step12完整复制。禁止继续同时运行step11或拿日志PID1589盲杀。

重新运行应先看到配置smoke通过，再两worker完成模型加载/warmup及workers_healthy=2，最后真实短句听音/长文本/打断与显存。下一项是实际目标复跑，不再插入工具准备阶段。

**“永久部署在双卡里面”不能在Kaggle保证。** 能实现并已编码的是健康模型在会话存活期间每卡一份常驻；会话结束/配额到期/机器回收后显存消失，磁盘/私有Dataset权重缓存不是GPU继续运行。长期服务需要可持续双GPU服务器与运维预算，本次未采购/部署外部硬件或绕过平台限制。

- 独立复制检查器首次Chromium启动SIGSEGV，尚未进入页面；保留copy-page-initial-browser-error.txt。随后Playwright最终复制三轮及独立检查器真实剪贴板/下载三轮均PASS；未改生产代码，启动异常根因未确定，不隐去失败记录。

---

## 内嵌备忘录：KAGGLE_STEP12_QUICKSTART.md

# step12：修复你现场的Mimi/RoPE加载错误

这是实际修复包，不是让你继续运行出错的step11。浏览器“复制 Kaggle 修复版完整代码（step12）”已换成`kaggle-fixed-step12.py`。

## 你现在怎么做

1. **先备份自己需要的参考音频、转写、已训练adapter及日志**，不要把API Key/Token发到聊天或共享输出。
2. Kaggle中先停止当前运行，再用平台的**停止会话/重新启动完整会话**操作，确认原监督器与GPU进程已结束。**仅停止一个单元格、刷新网页或重启Python内核不一定停止已分离的旧supervisor。** 不要用日志里的1589盲杀，也不要删除GPU锁来抢占。
3. 新会话选GPU T4 ×2、Internet On；进入浏览器复制页，确认标题/文件名是 **step12**，点击“复制全部代码”，替换旧启动单元格的全部内容再运行。不要同时运行step11。若平台保留了旧工作目录并提示旧supervisor.pid，仍不要盲删或按旧PID杀进程；在确认完整会话已重启后可用全新QTTS_ROOT目录启动，旧数据另行备份/管理。
4. 默认就是Qwen/Qwen3-TTS-12Hz-1.7B-Base，每worker一张GPU。默认`QTTS_RESIDENT=1`为健康模型会话内常驻，不需要另写训练命令或启用adapter模式来解决本次加载错误。环境中若留有`QTTS_MOCK=1`应先去掉/设为0；默认高速后端为`QTTS_TTS_ENGINE=faster`。
5. 依赖阶段审查并固定`faster-qwen3-tts==0.5.4`、`qwen-tts-hf==0.1.1.post1`、`transformers==5.20.2`。若需安装，会用当前Torch/torchaudio/torchvision版本作为约束，避免无条件替换平台CUDA栈。若发生命名空间冲突/安装冲突，会拒绝而不是静默卸载Torch。**不要仅执行pip install transformers<5**，这违反faster0.5.4依赖。
6. 预检应出现`qwen_mimi_rope_cpu`通过；这只是实际配置数学检查，**不是模型加载成功**。然后应看到两个worker完成模型加载及warmup、workers_healthy=2，才进入网页短句合成/实际试听。
7. 如果仍报错，需看本次`worker0.out/worker1.out`末尾的完整异常链及新预检结果。确定性兼容错误现在会停止该worker重试，并让启动流程清理其创建的supervisor，不应继续无意义循环加载。清理45秒未确认时必须按平台停止整个会话，不能认为锁已释放。

## 修了什么

实际Qwen-HF默认RoPE函数仍读取旧`config.rope_theta`，Transformers5.20.2 Mimi已使用`config.rope_parameters['rope_theta']`。新桥接只针对已识别的Qwen默认函数，从实际配置读theta、给临时副本提供旧字段，保持原配置/权重不动。10000、12345、1000000三个theta的真实Mimi配置CPU数值已核对；未知类型/缩放/非法参数不猜值。

默认不再每600次请求重载模型，也不因旧13.5GB门槛主动重启；显存高会告警，空闲缓存清理不释放活模型权重。可显式`QTTS_RESIDENT=0`回到旧周期回收策略。模型异常、OOM、服务重启或平台回收仍可能打断驻留，不承诺16GBfit、质量或时延。

## 不能承诺“永久部署在双卡”

应用能控制的是**会话存活且模型健康时，每张GPU保留一份模型**。Kaggle会话到期、配额用尽、关机或GPU回收后，显存必然丢失；磁盘权重/私有Dataset备份不等于模型继续驻留GPU。

真正长期常驻需要你拥有可持续运行的双GPU服务器和相应运维/预算。本次没有替你采购或部署外部服务器，也不绕过Kaggle限制。

## 现场验收还没完成

你提供的日志已经证明两张T4被识别、编译/下载阶段完成并到达模型加载；同时明确证明当时加载失败。修复已在CPU重现并验证该配置异常，但沙箱没有T4或完整Qwen权重，不能代替你新版本的模型重载、显存/实际声音验收。需要重新运行step12后才能进一步确认。

---

## 内嵌备忘录：KAGGLE_STEP13_PLAN.md

# 第十三阶段计划：修复Faster延迟导入导致RoPE补丁未安装

先计划/问题12的50条建议，再实现；不向用户重复提问。

## 现场事实与根因路径
step12在两T4上再次以同一MimiConfig.rope_theta失败。预检明确显示HF5模块未加载却给warning。真实faster0.5.4顶层只导出包装类，直到from_pretrained内部第194行才导入qwen_tts；step12仅查sys.modules，过早not_applicable。此前真实wheel函数CPU实验验证了桥接数学，却没有验证真实包导入生命周期，此缺口必须修正，不能归因用户操作。

## 实施顺序
1. 冻结原始至step12；新step13整包，不覆盖历史证据。
2. 基于安装发行元数据区分HF与官方legacy。HF先检查受审版本/命名空间冲突，再显式importlib.import_module导入实际compat模块，验证注册并安装补丁；不能用“尚未导入”等同“不适用”。未知/导入失败明确阻断。
3. HF runtime预检必须完成真实Mimi CPU数学smoke；legacy不强行依赖HF5。所有模型入口继续复用同一桥接函数。
4. 新增延迟导入、导入失败、冲突、重入幂等、预检fail-closed测试；真实Faster和完整Qwen包不替换导入函数，CPU构造微型MimiModel走真实_init_weights路径，不下载完整模型/不冒充T4。
5. 三轮Python/Node/Go及协议、完整浏览器，实际包导入+微型Mimi三进程；保留初始失败。三轮各100项范围复核，不把目标22/300改成全部实现。
6. 更新真实复制页/完整交付/33备忘录与12题600建议；验证原始至step12和正式工作台只读不变。

## 验收与边界
HF存在但compat未载入不能再跳过。成功要求step13 CPU真实包导入后桥接installed、实际Mimi实例初始化成功，及既有功能回归通过。真实双T4完整1.7B加载、CUDA graph、显存和声音仍需Kaggle实跑；无法保证平台永久驻留。下一步应直接复跑step13，非要求用户再做准备开发。

---

## 内嵌备忘录：KAGGLE_STEP13_AUDIT.md

# 第十三阶段审查：真实导入生命周期修复

## 结论与责任边界

step12在用户Kaggle两T4上仍失败，不能称已修好。原因不是用户没按步骤，而是我们上一版补丁只查sys.modules，没有覆盖Faster实际延迟导入。此前wheel函数数学通过只说明桥接算法有效，无法证明生产入口安装了补丁。此缺口已明确纳入本阶段回归。

## 实际来源与复现

- 受审真实faster0.5.4 wheel顶层导入model/ggml包装类；model.py第194行在from_pretrained内部才from qwen_tts import Qwen3TTSModel。
- 真实HF0.1.1.post1父包导入时注册旧default RoPE。TF5.20.2 _init_weights的ROPE_INIT_FUNCTIONS会覆盖Mimi自带现代默认计算器，导致读取旧rope_theta。
- 来源哈希/导入行见reviewed-import-sources.json。CPU隔离环境正常导入完整Faster，确认Qwen尚未载入；执行冻结step12实际兼容源，返回not_applicable；再正常导入完整Qwen并构造真实微型Mimi，复现与用户一致AttributeError。见real-import-baseline.json，不伪造第三方导入。

## 实施

1. install_qwen_rope_bridge以发行元数据判别HF/legacy，HF先检查版本/命名空间冲突，再显式正常importlib.import_module加载实际compat（及其父包），随后验证并桥接注册函数。未知组合/导入异常/元数据矛盾拒绝；legacy仍无须HF。
2. 保留窄范围bridge和实际theta临时副本，不改配置/权重，不猜默认值，不盲降TF4，不变更平台Torch/CUDA约束。
3. qwen_configuration_check要求installed且数学smoke明确True；HF存在却跳过或不完整时blocked/required=True。只有真正未安装HF的legacy路径可不适用。
4. Worker/native adapter/CPU编码/训练仍在构造前共用同一桥接；驻留、fatal nonce及所属进程清理保持。不增加导入钩子，不绕过验证来消除报错。
5. 新增6项回归：尚未导入时HF显式导入；导入失败；版本/冲突先行拒绝；已载HF缺发行元数据；HF skipped/incomplete smoke阻断；官方legacy保持可选。旧GPU/API/CPU编码替身测试明确模拟其兼容边界，不能伪造全局发行元数据后误称真实包通过。

## 更强的真实CPU验证（不是完整1.7B模型验收）

lazy_rope_import_check.py不替换第三方导入、不下载模型，禁网且HF离线；从真实Faster未载Qwen状态调用生产安装函数，再正常导入完整Qwen，实际TF MimiModel构造2651参数微型随机模型、本地保存后from_pretrained重载。10000/12345/1000000三theta均校验实际rotary缓冲、配置不变、参数finite；实际初始化进入桥接12次。完整Qwen包导入不等于完整Qwen模型构造/加载。这里GPU执行为False、完整Qwen模型加载为False。

额外正常运行真实backend_probe隔离CLI三轮：HF数学smoke均required=True且pass；沙箱无CUDA，整体报告blocked（符合预期），未把该报告当作目标GPU预检通过。见real-preflight-cpu-round1..3.json。

主venv未装这些第三方包；隔离依赖置/home/user/.cache/qtts-step13-site与既有step12-site，不入Git。SoX二进制缺失有警告，本实验未调用其音频功能，不假称通过SoX音频转换。

## 验证状态

最终三轮：Python273×3=819 PASS，Node30×3=90 PASS，Go race count3 PASS；资源所有权真实进程/HTTP训练输入/本地码CLI/Mock管线四脚本各执行3次（每次内置3轮，共各9轮）、adapter真实Go+SSE+双worker CPU小LoRA替身三轮、fatal真实supervisor+CPU worker三轮PASS。

完整浏览器114×3=342 PASS（11.4分钟），另最终step13整包逐字节复制三轮PASS。3001独立复制页真实Chromium三轮剪贴板/下载完整哈希一致、授权拒绝全选、375px手机无横向溢出、正式15文件不变，见copy-page.json。不是用HTTP读取代码冒充剪贴板验收。

最终交付门禁见docs/validation/step13/final-checks.json；三轮各100项不重复定向开发建议与保留目标ID见review-map.json，完整目标仍22/300；12题600建议不等于600修复。

## 初始失败保留

- 新完整包隔离环境首次缺scipy、随后缺cloudpickle等依赖；仅补隔离验证依赖，未修改主venv/生产版本组合。日志real-import-initial.txt/attempt2/依赖日志留存。
- 微型Mimi首次测试断言误以为TF5旋转模块有rope_init_fn字段；实际是默认静态方法+_init_weights registry。修正验证为实际inv_freq/original_inv_freq和函数profile计数，保留real-import-initial-modelassert.txt；不是以不核对频率的方式忽略错误。
- 完整273测试初轮1错误：CPU编码器旧替身把所有发行元数据伪造成stub-only，触发真实namespace冲突。测试明确隔离模拟legacy兼容路径；生产版本/冲突拒绝未削弱。初始日志python-initial.txt保留。

## 下一现场门禁

发布完整step13、只读复制页，旧原始至12冻结。先备份需要的私有数据，再停止并重启完整Kaggle会话，T4×2/Internet/非Mock默认faster，预检必须通过qwen_mimi_rope_cpu，然后看两worker实际完成加载/预热，再短句试听。当前没有真实T4/完整权重，不能保证下一次必成、显存fit、性能、音质或永久Kaggle；有新异常需按实际链路继续修复，不能报成功掩盖。

## 当前交付完整性

step13：282346字节/47资产，SHA256 dad142d75be94d8efb6567fc1f8755d3f37341a65d5c7fe9454fd36c87770e60；source_manifest逐项校验和repack --check可重现。原始至12包冻结，正式3000工作台HEAD/15文件1043155B不变，33备忘录完整内嵌。

---

## 内嵌备忘录：KAGGLE_STEP13_QUICKSTART.md

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

---

## 内嵌备忘录：KAGGLE_STEP14_REVIEW1.md

# 第十四阶段第1轮审查：100条定向建议

审查覆盖全部源文件的结构/哈希，重点为本轮主题。建议不是已实现清单；实现/保留/待硬件与未完成见STEP14审查处置。

1. [S14-R1-001] 连续录音：将239秒上限与十分钟需求对齐。
2. [S14-R1-002] 连续录音：同时扩大分块数量预算。
3. [S14-R1-003] 连续录音：保留累计字节上限。
4. [S14-R1-004] 连续录音：用虚拟时钟测试十一分钟。
5. [S14-R1-005] 连续录音：停止后才保存有效片段。
6. [S14-R1-006] 连续录音：取消权限晚返回仍关闭设备。
7. [S14-R1-007] 连续录音：禁止空录音提交。
8. [S14-R1-008] 连续录音：保留失败本地片段。
9. [S14-R1-009] 连续录音：显示连续录音最大时长。
10. [S14-R1-010] 连续录音：不把后台计时器当精确音频时钟。
11. [S14-R1-011] 上传预算：同步浏览器与服务端时长。
12. [S14-R1-012] 上传预算：同步客户端与服务端单文件字节。
13. [S14-R1-013] 上传预算：保留整请求总量门禁。
14. [S14-R1-014] 上传预算：保留未知长度流式门禁。
15. [S14-R1-015] 上传预算：原始库独立容量核对。
16. [S14-R1-016] 上传预算：PCM长音频预先计算空间。
17. [S14-R1-017] 上传预算：不把提高秒数等同无限上传。
18. [S14-R1-018] 上传预算：拒绝超过上限而不静默截断。
19. [S14-R1-019] 上传预算：给出明确限额中文提示。
20. [S14-R1-020] 上传预算：加入长WAV完整长度回归。
21. [S14-R1-021] 训练入口：明确参考处理不训练。
22. [S14-R1-022] 训练入口：明确快照不执行优化器。
23. [S14-R1-023] 训练入口：真实训练保留独立确认。
24. [S14-R1-024] 训练入口：不开虚假开始训练按钮。
25. [S14-R1-025] 训练入口：网页训练需独立CPU控制面。
26. [S14-R1-026] 训练入口：训练时停止两GPU推理而非争显存。
27. [S14-R1-027] 训练入口：控制面不能随analyst一起关闭。
28. [S14-R1-028] 训练入口：完成后再恢复原声音服务。
29. [S14-R1-029] 训练入口：取消要等待两个rank退出。
30. [S14-R1-030] 训练入口：未实现端到端入口须明示未完成。
31. [S14-R1-031] 长录音切分：训练不能把十分钟当单条序列。
32. [S14-R1-032] 长录音切分：优先审核ASR时间戳。
33. [S14-R1-033] 长录音切分：不得用均分文本猜对齐。
34. [S14-R1-034] 长录音切分：不得裁去超预算文本。
35. [S14-R1-035] 长录音切分：保留原始音频。
36. [S14-R1-036] 长录音切分：生成独立可审核短WAV。
37. [S14-R1-037] 长录音切分：保留每段来源起止秒。
38. [S14-R1-038] 长录音切分：同一说话人须明确声明。
39. [S14-R1-039] 长录音切分：片段过短需要拒绝或重新切分。
40. [S14-R1-040] 长录音切分：完整语义覆盖要逐项记录。
41. [S14-R1-041] 转写：逐条训练文本对应逐条音频。
42. [S14-R1-042] 转写：ASR提案不能标为人工已核验。
43. [S14-R1-043] 转写：禁止将参考文本套用全部片段。
44. [S14-R1-044] 转写：Unicode转写保持原值。
45. [S14-R1-045] 转写：空转写拒绝。
46. [S14-R1-046] 转写：转写字符总预算保留。
47. [S14-R1-047] 转写：不能凭训练loss证明读音正确。
48. [S14-R1-048] 转写：方言专名需要真实试听。
49. [S14-R1-049] 转写：训练前审核标点断句。
50. [S14-R1-050] 转写：保留来源转写hash。
51. [S14-R1-051] 数据完整性：继续固定manifest hash。
52. [S14-R1-052] 数据完整性：继续拒绝软链接。
53. [S14-R1-053] 数据完整性：继续拒绝硬链接。
54. [S14-R1-054] 数据完整性：样本目录不得路径穿越。
55. [S14-R1-055] 数据完整性：源库删除不等于训练副本删除。
56. [S14-R1-056] 数据完整性：训练时持有读取租约。
57. [S14-R1-057] 数据完整性：保留授权确认。
58. [S14-R1-058] 数据完整性：失败不覆盖旧模型。
59. [S14-R1-059] 数据完整性：保留独立引用参考上限。
60. [S14-R1-060] 数据完整性：不自动上传私人录音到第三方。
61. [S14-R1-061] 格式：浏览器WebM不能改后缀冒充WAV。
62. [S14-R1-062] 格式：真实解码后再重采样。
63. [S14-R1-063] 格式：保持24k单声道PCM16训练契约。
64. [S14-R1-064] 格式：解码时检查完整时长。
65. [S14-R1-065] 格式：解码异常不当成功。
66. [S14-R1-066] 格式：训练长样本切分应在编码前。
67. [S14-R1-067] 格式：统一参考不使用整段十分钟。
68. [S14-R1-068] 格式：不随意降采样谋求提速。
69. [S14-R1-069] 格式：保留nonfinite检测。
70. [S14-R1-070] 格式：输出格式与模型codec契约一致。
71. [S14-R1-071] 并发输入：限制同时解码任务。
72. [S14-R1-072] 并发输入：限制总驻留音频内存。
73. [S14-R1-073] 并发输入：不要每个音频开无限线程。
74. [S14-R1-074] 并发输入：保护ASR共享模型状态。
75. [S14-R1-075] 并发输入：采集线程不承担模型训练。
76. [S14-R1-076] 并发输入：上传回调必须检查当前页面代次。
77. [S14-R1-077] 并发输入：锁定时清空私人转写。
78. [S14-R1-078] 并发输入：晚响应不能恢复已锁定界面。
79. [S14-R1-079] 并发输入：请求取消不等于后台计算结束。
80. [S14-R1-080] 并发输入：并发变更需修订号核对。
81. [S14-R1-081] 浏览器布局：保留两个主要视图。
82. [S14-R1-082] 浏览器布局：训练说明放声音库辅助区。
83. [S14-R1-083] 浏览器布局：长录音状态不能溢出手机宽度。
84. [S14-R1-084] 浏览器布局：保留键盘停止操作。
85. [S14-R1-085] 浏览器布局：录音按钮不能重复启动。
86. [S14-R1-086] 浏览器布局：麦克风波形不能伪造。
87. [S14-R1-087] 浏览器布局：显示准备与实际训练区别。
88. [S14-R1-088] 浏览器布局：为长录音显示时间预算。
89. [S14-R1-089] 浏览器布局：文案不能承诺真人完全一致。
90. [S14-R1-090] 浏览器布局：继续可复制完整Kaggle代码。
91. [S14-R1-091] 验收：保留step13启动成功现场证据。
92. [S14-R1-092] 验收：新包冻结旧版本。
93. [S14-R1-093] 验收：新增十一分钟虚拟录音测试。
94. [S14-R1-094] 验收：物理麦克风仍单独验收。
95. [S14-R1-095] 验收：真实十分钟数据不能用零信号替代质量验收。
96. [S14-R1-096] 验收：保护正式工作台文件。
97. [S14-R1-097] 验收：记录本轮未完成项。
98. [S14-R1-098] 验收：记录训练覆盖而非样本总数猜测。
99. [S14-R1-099] 验收：只有实际执行才标训练通过。
100. [S14-R1-100] 验收：三轮验证证据分开保存。

---

## 内嵌备忘录：KAGGLE_STEP14_REVIEW2.md

# 第十四阶段第2轮审查：100条定向建议

审查覆盖全部源文件的结构/哈希，重点为本轮主题。建议不是已实现清单；实现/保留/待硬件与未完成见STEP14审查处置。

1. [S14-R2-001] 张量准备：找出每epoch重复文本tokenize。
2. [S14-R2-002] 张量准备：缓存必须有字节上限。
3. [S14-R2-003] 张量准备：缓存不改变token顺序。
4. [S14-R2-004] 张量准备：缓存返回值避免被调用者污染。
5. [S14-R2-005] 张量准备：超过缓存上限退回原计算。
6. [S14-R2-006] 张量准备：包含声学码形状校验。
7. [S14-R2-007] 张量准备：不缓存未通过预算的样本。
8. [S14-R2-008] 张量准备：保留统一参考mel。
9. [S14-R2-009] 张量准备：比对缓存前后collate张量。
10. [S14-R2-010] 张量准备：用调用次数而非GPU倍速声称改善。
11. [S14-R2-011] 优化器：保持全部联合loss。
12. [S14-R2-012] 优化器：保持0.3子talker系数。
13. [S14-R2-013] 优化器：保持训练样本顺序。
14. [S14-R2-014] 优化器：保持累积步分母。
15. [S14-R2-015] 优化器：保持不足一组累积的缩放。
16. [S14-R2-016] 优化器：保持AdamW权重衰减。
17. [S14-R2-017] 优化器：保持LoRA可训练参数。
18. [S14-R2-018] 优化器：保持FP32适配器。
19. [S14-R2-019] 优化器：不减少epoch作为无损提速。
20. [S14-R2-020] 优化器：记录真实optimizer step数。
21. [S14-R2-021] 双卡：保持两rank NCCL契约。
22. [S14-R2-022] 双卡：不让两rank同时用同一物理卡。
23. [S14-R2-023] 双卡：保持奇数样本补齐策略。
24. [S14-R2-024] 双卡：保持两rank参数摘要一致。
25. [S14-R2-025] 双卡：每epoch报告实际seen_ids。
26. [S14-R2-026] 双卡：不能把CPU Gloo当NCCL。
27. [S14-R2-027] 双卡：OOM后不得标完成。
28. [S14-R2-028] 双卡：不能用两个Python线程替代DDP。
29. [S14-R2-029] 双卡：显存峰值必须实测。
30. [S14-R2-030] 双卡：完成后保存适配器再报告。
31. [S14-R2-031] 同步开销：审查每参数grad finite读取。
32. [S14-R2-032] 同步开销：合并有限性检查到一次CPU读取。
33. [S14-R2-033] 同步开销：跨rank有限性继续一致。
34. [S14-R2-034] 同步开销：非有限梯度两rank一同跳过。
35. [S14-R2-035] 同步开销：保留梯度范数裁剪。
36. [S14-R2-036] 同步开销：不盲开find_unused_parameters=False。
37. [S14-R2-037] 同步开销：loss统计不删训练计算。
38. [S14-R2-038] 同步开销：不盲开torch.compile。
39. [S14-R2-039] 同步开销：不盲开TF32冒充T4原生支持。
40. [S14-R2-040] 同步开销：CUDA优化需独立目标机基准。
41. [S14-R2-041] 线程预算：按CPU配额而非文件数设置线程。
42. [S14-R2-042] 线程预算：两rank线程总数不能压满宿主。
43. [S14-R2-043] 线程预算：ASR线程与训练线程分开预算。
44. [S14-R2-044] 线程预算：限定预处理并发。
45. [S14-R2-045] 线程预算：避免每个worker再套大线程池。
46. [S14-R2-046] 线程预算：保留取消与超时。
47. [S14-R2-047] 线程预算：记录线程配置。
48. [S14-R2-048] 线程预算：默认不引入DataLoader多进程。
49. [S14-R2-049] 线程预算：小数据先消除重复计算。
50. [S14-R2-050] 线程预算：吞吐测试包含预处理成本。
51. [S14-R2-051] 模型依赖：保留已成功HF导入顺序。
52. [S14-R2-052] 模型依赖：继续执行RoPE强制smoke。
53. [S14-R2-053] 模型依赖：兼容HF发行元数据报告。
54. [S14-R2-054] 模型依赖：不强制卸载平台Torch。
55. [S14-R2-055] 模型依赖：不因训练改变默认推理后端。
56. [S14-R2-056] 模型依赖：T4继续FP16。
57. [S14-R2-057] 模型依赖：不启用仅Ampere支持的BF16。
58. [S14-R2-058] 模型依赖：完整权重来源必须固定。
59. [S14-R2-059] 模型依赖：禁止远程模型代码。
60. [S14-R2-060] 模型依赖：模型物化成本单独记录。
61. [S14-R2-061] 训练发布：不把缓存称adapter。
62. [S14-R2-062] 训练发布：必须真实更新参数。
63. [S14-R2-063] 训练发布：损坏adapter不得回退Base。
64. [S14-R2-064] 训练发布：候选不自动覆盖active。
65. [S14-R2-065] 训练发布：保留保存speaker向量。
66. [S14-R2-066] 训练发布：保留Base绑定。
67. [S14-R2-067] 训练发布：保留训练run来源。
68. [S14-R2-068] 训练发布：新进程重载另行验收。
69. [S14-R2-069] 训练发布：训练后试听不可省略。
70. [S14-R2-070] 训练发布：失败仍保留旧可用档案。
71. [S14-R2-071] 资源所有权：训练前必须排他获取两GPU。
72. [S14-R2-072] 资源所有权：不删除fleet锁抢资源。
73. [S14-R2-073] 资源所有权：不按旧PID杀进程。
74. [S14-R2-074] 资源所有权：保留继承FD证明。
75. [S14-R2-075] 资源所有权：保留nonce校验。
76. [S14-R2-076] 资源所有权：取消只终止所属Popen。
77. [S14-R2-077] 资源所有权：进程退出不等于所有孩子退出。
78. [S14-R2-078] 资源所有权：父进程被杀需释放子进程。
79. [S14-R2-079] 资源所有权：网关与训练控制分离才可网页操作。
80. [S14-R2-080] 资源所有权：不能为一键训练绕过锁。
81. [S14-R2-081] 性能证据：记录端到端训练墙钟。
82. [S14-R2-082] 性能证据：记录加载时间。
83. [S14-R2-083] 性能证据：记录tokenizer调用次数。
84. [S14-R2-084] 性能证据：记录缓存驻留字节。
85. [S14-R2-085] 性能证据：记录优化器更新量。
86. [S14-R2-086] 性能证据：记录CPU线程占用。
87. [S14-R2-087] 性能证据：记录GPU显存峰值。
88. [S14-R2-088] 性能证据：相同数据和seed做A/B。
89. [S14-R2-089] 性能证据：相同loss路径比较参数。
90. [S14-R2-090] 性能证据：无真实基准不写最快。
91. [S14-R2-091] 回归：保留CPU tiny LoRA重载。
92. [S14-R2-092] 回归：保留两进程Gloo测试。
93. [S14-R2-093] 回归：新增缓存等价性测试。
94. [S14-R2-094] 回归：新增缓存淘汰测试。
95. [S14-R2-095] 回归：新增调用者变更隔离测试。
96. [S14-R2-096] 回归：新增HF训练报告发行检查。
97. [S14-R2-097] 回归：新增梯度finite聚合测试。
98. [S14-R2-098] 回归：原CLI拒绝fixture继续有效。
99. [S14-R2-099] 回归：三轮完整Python不是只跑新测试。
100. [S14-R2-100] 回归：逐项登记未实测硬件项。

---

## 内嵌备忘录：KAGGLE_STEP14_REVIEW3.md

# 第十四阶段第3轮审查：100条定向建议

审查覆盖全部源文件的结构/哈希，重点为本轮主题。建议不是已实现清单；实现/保留/待硬件与未完成见STEP14审查处置。

1. [S14-R3-001] 文本链路：定位CleanDelta删除内容。
2. [S14-R3-002] 文本链路：避免每个delta独立清洗URL。
3. [S14-R3-003] 文本链路：朗读路径不补句号。
4. [S14-R3-004] 文本链路：保留中英混合原文。
5. [S14-R3-005] 文本链路：保留数字小数。
6. [S14-R3-006] 文本链路：保留引号。
7. [S14-R3-007] 文本链路：保留专有名词。
8. [S14-R3-008] 文本链路：不添加链接二字。
9. [S14-R3-009] 文本链路：分段连接按规范比较输入。
10. [S14-R3-010] 文本链路：模型声学错字另行核验。
11. [S14-R3-011] 呼吸：默认关闭额外呼吸注入。
12. [S14-R3-012] 呼吸：不以合成噪声冒充真人吸气。
13. [S14-R3-013] 呼吸：保留可选真实参考呼吸。
14. [S14-R3-014] 呼吸：无真实片段时保持安静。
15. [S14-R3-015] 呼吸：不放大短促噪声。
16. [S14-R3-016] 呼吸：保留淡入淡出防爆音。
17. [S14-R3-017] 呼吸：呼吸增益需试听。
18. [S14-R3-018] 呼吸：模型自身呼吸与后加呼吸区分。
19. [S14-R3-019] 呼吸：不盲目滤掉全部气声。
20. [S14-R3-020] 呼吸：去噪不得削掉辅音。
21. [S14-R3-021] 首声：区分模型首块与可听首声。
22. [S14-R3-022] 首声：不把前置静音算有效语音。
23. [S14-R3-023] 首声：修正trimmer前计时。
24. [S14-R3-024] 首声：保留实际首播测量。
25. [S14-R3-025] 首声：分段过短影响韵律须权衡。
26. [S14-R3-026] 首声：小chunk需实机核验。
27. [S14-R3-027] 首声：不要用空PCM刷低首声。
28. [S14-R3-028] 首声：首段优先调度继续保留。
29. [S14-R3-029] 首声：录制到输出完整链路测量。
30. [S14-R3-030] 首声：无真实T4数据不承诺时延。
31. [S14-R3-031] 缓冲：不要无条件降低首播阈值。
32. [S14-R3-032] 缓冲：保留欠载预测。
33. [S14-R3-033] 缓冲：保留迟滞。
34. [S14-R3-034] 缓冲：区分首次启动与恢复。
35. [S14-R3-035] 缓冲：生成慢时继续积累。
36. [S14-R3-036] 缓冲：句级缓冲不能冒称声学流式。
37. [S14-R3-037] 缓冲：记录首PCM和首播放分别。
38. [S14-R3-038] 缓冲：测试短文本尾段可播放。
39. [S14-R3-039] 缓冲：停止后不能漏出迟到PCM。
40. [S14-R3-040] 缓冲：连续朗读不能丢段。
41. [S14-R3-041] 准确朗读：模型可能幻觉不能仅靠输入相等保证。
42. [S14-R3-042] 准确朗读：严格核验需整句缓存。
43. [S14-R3-043] 准确朗读：ASR核验增加首声等待。
44. [S14-R3-044] 准确朗读：ASR也不是绝对真值。
45. [S14-R3-045] 准确朗读：不符应拒绝或请求重试。
46. [S14-R3-046] 准确朗读：重试不改用户文本。
47. [S14-R3-047] 准确朗读：不自动补充解释。
48. [S14-R3-048] 准确朗读：多音字需目标语境测试。
49. [S14-R3-049] 准确朗读：真实试听列为门禁。
50. [S14-R3-050] 准确朗读：不承诺零错字。
51. [S14-R3-051] 调度：保护段索引顺序。
52. [S14-R3-052] 调度：失败只在未输出前重试。
53. [S14-R3-053] 调度：不可重复播放已输出语音。
54. [S14-R3-054] 调度：取消清除队列。
55. [S14-R3-055] 调度：监控两worker健康。
56. [S14-R3-056] 调度：资源锁不因低延迟绕过。
57. [S14-R3-057] 调度：调度公平性回归。
58. [S14-R3-058] 调度：背压不能无限堆积文本。
59. [S14-R3-059] 调度：native超时预算保留。
60. [S14-R3-060] 调度：默认faster启动不退化。
61. [S14-R3-061] 安全：口令只在内存。
62. [S14-R3-062] 安全：不输出密钥到诊断。
63. [S14-R3-063] 安全：预览用相对请求。
64. [S14-R3-064] 安全：只允许可信HTTPS。
65. [S14-R3-065] 安全：训练报告不含转写全文。
66. [S14-R3-066] 安全：不得自动发布私人样本。
67. [S14-R3-067] 安全：上传预算同步Go网关。
68. [S14-R3-068] 安全：锁定终止本地录音。
69. [S14-R3-069] 安全：锁定阻止晚响应。
70. [S14-R3-070] 安全：保留现有访问限制。
71. [S14-R3-071] 包与交付：原始至step13冻结。
72. [S14-R3-072] 包与交付：新step14整包重打。
73. [S14-R3-073] 包与交付：逐资产hash校验。
74. [S14-R3-074] 包与交付：完整剪贴板读回比对。
75. [S14-R3-075] 包与交付：下载内容逐字节比对。
76. [S14-R3-076] 包与交付：手机页面无横向溢出。
77. [S14-R3-077] 包与交付：拒绝剪贴板权限可全选。
78. [S14-R3-078] 包与交付：正式3000工作台不覆盖。
79. [S14-R3-079] 包与交付：复制页固定新hash。
80. [S14-R3-080] 包与交付：文档不把模拟当现场。
81. [S14-R3-081] 语言选择：Python保留模型编排。
82. [S14-R3-082] 语言选择：PyTorch算子执行已编译CUDA。
83. [S14-R3-083] 语言选择：Go保留网关调度。
84. [S14-R3-084] 语言选择：Rust保留DSP。
85. [S14-R3-085] 语言选择：JS保留浏览器采集播放。
86. [S14-R3-086] 语言选择：不为多语言引入额外网络跳转。
87. [S14-R3-087] 语言选择：不无依据重写C++算子。
88. [S14-R3-088] 语言选择：不引入Java服务增加驻留。
89. [S14-R3-089] 语言选择：不引入SQL保存密钥。
90. [S14-R3-090] 语言选择：类型与边界比语言数量重要。
91. [S14-R3-091] 三轮复核：三轮完整Python。
92. [S14-R3-092] 三轮复核：三轮Node文件服务。
93. [S14-R3-093] 三轮复核：Go race count3。
94. [S14-R3-094] 三轮复核：三轮完整浏览器。
95. [S14-R3-095] 三轮复核：三轮协议替身。
96. [S14-R3-096] 三轮复核：真实包Mimi三进程保持。
97. [S14-R3-097] 三轮复核：实际训练质量门禁仍未验。
98. [S14-R3-098] 三轮复核：记录所有初始失败。
99. [S14-R3-099] 三轮复核：汇总300建议处置而非全打勾。
100. [S14-R3-100] 三轮复核：交接提示词完整内嵌新增备忘录。

---

## 内嵌备忘录：KAGGLE_STEP14_PLAN.md

# 第十四阶段方案：长录音、无损训练计算优化、无额外呼吸/文本改写

## 已执行审查与自问自答
三轮审查各100条，见REVIEW1/2/3；全资产结构/哈希与重点链路审查记录见review-before.json，不是全代码无错证明。先问题13，再其50建议，再问题14及50建议，再问题15及50建议，详见DECISIONS。15题750建议，建议不等于已实现。

## 第一性原理与语言职责
录音时长是采集/解码/存储预算问题；训练吞吐是tokenize/数据准备/GPU计算与同步的瓶颈问题；音质取决于数据与模型，不取决于语言种类；准确播放涉及文本源、分段、模型生成、传输顺序与播放器。Python/PyTorch+编译CUDA做模型，Go做调度/传输，Rust/C做已有DSP，浏览器JS做采集播放。没有证据引入C++/Java/C#/SQL/R等重写能提高速度，不为语言数量增加复制和部署风险。

## 完整目标架构（未完成项必须保留）
1. 采集≤20分钟原件并保留，字节/块数/总时长独立门禁；原件不是十分钟单条训练样本。
2. ASR给出时间戳/逐条转写提案，人工审阅、同一说话人及授权确认；切1.5–16秒短样本，保证不猜测对齐、不截去正文，保持来源索引。训练序列超预算拒绝而不裁切。
3. 独立CPU训练控制面保持网页存活；维护态停止双GPU推理及analyst，确认全部孩子退出后才交接排他GPU租约；编码/真实双rank训练/进度/取消/失败收据；结束再恢复推理。当前supervisor退出同时关闭gateway，不能简单在analyst加线程就称网页一键训练完成。
4. 保持loss/优化器/顺序/样本覆盖；有界缓存消除重复tokenize、减少不必要CPU同步；真实T4记录端到端时间与显存后才能确定调参是否提速。
5. 默认不后加呼吸/合成噪声；声音本身的气声不可盲目滤掉。保留可选真实呼吸能力。
6. 默认实际会话不清洗文本、不补句号；输入文本一致不能证明声学无错字。严格逐句ASR核验后播放需要额外延迟，且仍需试听。保留原始低延迟播放并明确尚未自动声学校验。

## 本轮实际执行范围（不是全部目标已经完成）
A. 浏览器与服务端提升为20分钟采集预算、64MiB单文件/128MiB请求、独立块数/本地字节/总量限制，回归十一分钟虚拟时钟和长PCM解码。
B. 实现有界训练输入张量缓存/相同样本序列等价测试；聚合梯度finite检查而不改变联合loss/累积/裁剪；修复HF发行包训练报告版本查询。
C. 会话默认保留原文、不额外补句号；默认禁止后加呼吸（尤其合成噪声），保留显式真实参考呼吸选项；首块计时放在实际可输出语音后。
D. 原始至13冻结，发布14完整可复制包；三轮Python/Node/Go/browser/协议与真实包CPU回归、33+新增备忘录完整交接。

## 本轮不能打勾的目标
网页按钮→长录音自动逐条审校→独立控制面维护态→真实双T4训练→训练后自动部署尚未闭环；不增加只会报成功的假按钮。物理十分钟录音、真实训练质量/速度、首声改善、呼吸主观自然度及逐字声学准确率没有本机证据，不能承诺零错误、真人一样或最快。实际硬件才能解除这些门禁；本轮完成后必须明确报告仍未满足用户全部目标，而非“验收全部成功”。

## 长数据覆盖补充门禁

现有训练快照仍最多16条；若高质量切分产生更多片段，还需扩展受限分片/manifest与完整样本覆盖后才能全部入训，不能只选前16条冒充完整十分钟训练。

---

## 内嵌备忘录：KAGGLE_STEP14_AUDIT.md

# 第十四阶段审查：已实现边界与未完成门禁

## 不能写成“用户全部需求已完成”

| 需求 | 本轮代码/证据 | 尚未完成 |
|---|---|---|
| 连续十多分钟录音 | 约20分钟/8192块/64MiB单文件，服务端1200秒；11分钟虚拟控制与完整合成PCM解码验证 | 物理麦克风、休眠/后台冻结和真实长语音采集 |
| 保质提速 | 冻结step13真实CPU小LoRA A/B，loss/更新/参数逐位一致；重复tokenize从12次到3次 | Qwen/T4吞吐、峰值显存、相同数据训练音质A/B |
| 网页点击真实训练 | 原真实双rank训练CLI保留，快照明确不训练 | 独立CPU控制面、维护态租约交接、网页启动/取消/进度/恢复服务及训练后发布闭环 |
| 自然呼吸 | 默认不后加呼吸，reference模式只有真实片段，无合成噪声回退 | 模型自身气声、呼吸自然度与音色实听 |
| 首声更快 | 区分模型首块与裁边后首个非空PCM；可选首段chunk=2实验 | 未保证首播更快；真实T4端到端首播/欠载A/B |
| 文本完全一致 | 实际会话不再CleanDelta清理正文或补句号；多delta原文连接测试 | 没有逐句ASR核验/拒播闭环，不保证模型无漏字添字；纯标点/纯空白片段仍按旧规则过滤 |

step13用户现场已通过双T4加载/预热/ready门禁；不应再把此前双GPU启动说成完全未知。但上述新增目标仍不能从那次日志推出成功。

## 三轮审查/自问自答

REVIEW1/2/3各100条建议，完整源结构/哈希见review-before.json；重点逐链路审查，不宣称逐行无错或300项全部修复。问题13→50建议→问题14→50建议→问题15→50建议已按顺序记录。共15题750建议。处置表review-disposition.json区分本轮实现、原有回归保留、未闭环/待真实硬件；完整目标清单仍22/300。

## 具体改动

1. recorder默认1199000ms，8192 chunks，64MiB单文件、127MiB本地合计。UploadLimits默认1200秒单段、1800秒合计、128MiB请求、64MiB文件；Go上传上限同步128MiB，浏览器上传检查同步。原始库仍64MiB/库/512MiB总体，其他独立预算仍可先触发；不是无限录音或所有编码格式都能存满20分钟。上传超过限制拒绝，原件不截断。训练快照仍保留短段及序列预算，不能把长参考直接送入SFT。
2. TTSDataset深拷贝输入冻结调用者来源；64MiB有界CPU text/code tensor缓存，超过预算回退旧计算，不裁切不替换样本。返回clone避免缓存被调用者改坏，reference mel只读契约不变。run_rank保留逐样本准入，记录tokenizer_calls/cache_hits/cache_bytes。
3. 训练梯度finite flags在同一设备合并后一次host读取，跨rank collective与loss/accumulation/clipping/AdamW不变。HF/官方训练元数据查询兼容修复，不再在HF成功训练末尾查询不存在的官方发行包而报错。
4. Go实际newSession使用ExactSegCfg；不逐delta清洗markdown/URL/emoji、不合并内部空格、不添加句末标点。DefaultSegCfg/CleanDelta留给显式历史契约测试。不能因此说模型发音与文字已完全相同。
5. Worker默认QTTS_BREATH_MODE=off；reference模式只使用真实bank，空bank返回安静pause，删除合成breath噪声兜底。保留模型原声与淡入淡出，不盲滤气声/辅音。
6. model_first_chunk_ms与first_chunk_ms分别记录；后者从裁边后非空PCM才开始，不把被裁掉的空片段算首声。注意旧EdgeTrimmer在runaway静音时可放行静音并标异常，非空PCM不等于ASR确认的人声/真实首播。前端first_played与欠载保持，acoustic_text_verified=False。QTTS_FIRST_CHUNK_SIZE可选2..8，默认4不变，不通过降低播放器稳定阈值美化延迟。
7. 语言分工仍Python/PyTorch+CUDA、Go、Rust和浏览器JS；没有目标机数据就不引入新语言/自定义C++内核或高风险BF16/FA2/compile开关。

## 实验与证据

- test_step14新增12项：长解码/独立预算、录音≠训练、默认无呼吸、真实呼吸无噪声回退、非空PCM计时、缓存张量/优化器参数等价、字节上限/隔离、梯度finite/HF发行。
- training_cache_check.py加载冻结step13的真实训练与dataset源，不以重写基线代替。三独立CPU进程，每次同数据/seed，三epoch共6次optimizer更新，两路径loss与所有adapter tensor逐位一致；tokenizer调用12→3。只报告减少重复调用，fixture墙钟包含冷启动与执行顺序偏差，不能据此宣称端到端倍速或质量提高。
- 虚拟浏览器11分钟与2640块继续录音/约20分钟自动停止；合成660秒24k PCM解码长度完整。都不是真实麦克风/真人声音实验。
- 保留真实完整Faster/Qwen导入与微型Mimi构造/保存/重载三进程，保护已成功RoPE路径；不是Qwen1.7B训练或T4实验。
- 三轮完整Python285×3=855 PASS，Node30×3=90 PASS，Go race count3 PASS；资源所有权真实进程/输入HTTP/本地码CLI/Mock管线/Go+SSE+双worker adapter替身各三轮、fatal真实supervisor+CPU worker三轮PASS。
- 浏览器117×3=351 PASS（10.4分钟），最终step14整包逐字节复制另3 PASS。独立3001复制页真实Chromium三轮剪贴板/下载精确、授权拒绝全选/375px手机无横向溢出、正式15文件不变PASS。见copy-page.json与final-checks.json。
- 这些通过项仅覆盖实现范围，整体用户需求仍PARTIAL/BLOCKED。

## 初始记录

恢复会话后依赖缓存/venv不在，测试环境按现有测试锁恢复，未写进生产包/未改变Kaggle平台Torch。首个Go测试从仓库根运行找不到go.mod，改在真实go/gateway目录执行后通过；未改源码去适配错误目录。初检记录保留。全量失败若有，必须保留而不是只删测试。

## 下一步必须做而非继续虚报

优先实现网页训练的独立CPU控制面与维护态：网关/状态服务不能随GPU服务退出；停止并确认所有GPU持有者、传递可验证租约、固定实际数据/Base/码版本、真实两rank训练、受控取消/恢复、候选发布/明确切换。需要本地物化Base与审核过的逐段转写，不能猜这些信息或自动拿用户音频权利作假确认。真实首声、质量与声学一致性需相同参考/文本/种子A/B和试听，验收前本阶段整体需求状态为PARTIAL/BLOCKED，不得输出全部成功。

## 长数据覆盖补充门禁

现有训练快照仍最多16条；若高质量切分产生更多片段，还需扩展受限分片/manifest与完整样本覆盖后才能全部入训，不能只选前16条冒充完整十分钟训练。

## 最终交付

step14为285094字节/48资产，SHA256 73a02a95919406c4570ea563f0c0475fdde17535e6ccd16764c32514fce2c369；repack可重现，原始至13冻结，正式15文件/HEAD不变。39完整备忘录、300建议处置、15题750建议均有独立核验；不提升真实质量/性能门禁。

---

## 内嵌备忘录：KAGGLE_STEP14_QUICKSTART.md

# step14 使用与验收边界

这是部分功能修复交付，不是网页一键训练已完成。当前13已有实际双T4 ready日志；14新增功能仍需实机回归。

## 升级
1. 先自行备份需保留的私有原录音/转写/adapter。不要发口令或私人数据给聊天。
2. 在Kaggle停止并重启完整会话（不是只刷新网页/重启内核），避免旧supervisor/GPU进程冲突；不要按旧PID盲杀或删锁。
3. 从3001复制页确认step14，完整替换旧cell，T4×2/Internet/nonMock默认faster运行。仍保留受审HF/TF pins和强制RoPE检查，不需要另改Torch/CUDA。
4. 等两worker加载/预热ready，再解锁网页；仅看到网页不等于模型就绪。

## 长录音
默认约19分59秒自动停止（服务端单段1200秒），最大64MiB/段，16文件、请求128MiB、本地合计127MiB；原始库64MiB/库仍独立生效。块数8192，浏览器后台冻结/休眠仍可能中断，建议前台录制并及时备份。高码率原始WAV可能先达到字节限制，不能保证所有格式录满20分钟。

本地录音在创建档案/添加库前不是服务端持久保存。原始库不自动Dataset备份，清除本地片段/结束会话可能丢失。

## 训练不是“点参考处理”
现有网页的“处理参考”“输入快照”不执行优化器；本轮没有添加假训练按钮。真实训练仍使用train_tts.py双rank CLI，按KAGGLE_TRAINING_QUICKSTART.md准备可信本地Base和逐条对齐短WAV/转写后执行，先停止推理，不并抢双卡。长录音必须先按可信时间戳切短并审核，不可把整段10分钟送入max_sequence1024/2048或均分转写猜对齐。

本轮缓存/finite优化没有减少样本、epoch、联合loss或optimizer步数；CPU小模型逐位等价不代表真实Qwen训练质量/速度已验收。网页训练控制面/取消/恢复/自动部署仍待实现，见STEP14_PLAN/AUDIT。

## 呼吸、正文、首声
- 默认不后加呼吸噪声；模型自身的呼吸仍保留。QTTS_BREATH_MODE=reference可显式使用真实参考片段，无片段不合成噪声。是否更自然需自己试听。
- 实际会话不再清洗正文或补句号，建议直接朗读模式先试多音字/数字/中英混合。并未启用自动ASR核验，模型可能漏字添字，不能保证逐字完全一致。
- 默认首段chunk仍4，保持原稳定策略；可在启动前实验QTTS_FIRST_CHUNK_SIZE=2（有效2..8），但需同参考/同文本测first_played_ms与underruns，变差则恢复4。原生adapter仍句级缓冲，不能冒称声学流式。
- first_chunk_ms为裁边后非空PCM，model_first_chunk_ms是模型首块；真实首播另看first_played_ms。不能把收到前置静音当作已听到人声。

## 必须实测且尚未验收
物理十多分钟录音、真实Qwen/T4训练与音质不降、呼吸自然度、首声实际改善、连续播放准确率和网页一键训练闭环。当前状态PARTIAL/BLOCKED，不是“全部成功”。Kaggle有效会话内健康驻留保留，平台回收/配额不可绕过。

## 长数据覆盖补充门禁

现有训练快照仍最多16条；若高质量切分产生更多片段，还需扩展受限分片/manifest与完整样本覆盖后才能全部入训，不能只选前16条冒充完整十分钟训练。

---

## 内嵌备忘录：KAGGLE_STEP15_REVIEW1.md

# 第十五阶段第1轮专题审查：100条建议

全源文件读取/哈希与Python AST巡检不等于逐行语义正确证明。重点调用链经过人工分析；建议不是100项已修复。处置与实测边界见AUDIT。

1. [S15-R1-001] `worker.RealEngine`：禁止参考码进入解码器。
2. [S15-R1-002] `worker.RealEngine`：仅以说话人向量条件生成。
3. [S15-R1-003] `worker.RealEngine`：生成调用不传参考正文。
4. [S15-R1-004] `worker.RealEngine`：预热采用相同向量模式。
5. [S15-R1-005] `worker.RealEngine`：dtype回退后仍用向量模式。
6. [S15-R1-006] `worker.RealEngine`：不开放环境变量回退ICL。
7. [S15-R1-007] `worker.RealEngine`：明确韵律相似度可能变化。
8. [S15-R1-008] `worker.RealEngine`：核对Faster0.5.4实际源码。
9. [S15-R1-009] `worker.RealEngine`：生成采样率仍严格24k。
10. [S15-R1-010] `worker.RealEngine`：生成器取消时仍close。
11. [S15-R1-011] `worker.lead_audio`：废止reference呼吸拼接开关。
12. [S15-R1-012] `worker.lead_audio`：前置停顿仅零样本。
13. [S15-R1-013] `worker.lead_audio`：旧breath_files不能被读取。
14. [S15-R1-014] `worker.lead_audio`：无参考片段也不造噪声。
15. [S15-R1-015] `worker.lead_audio`：保留模型自身呼吸。
16. [S15-R1-016] `worker.lead_audio`：不把去呼吸等同自然音色。
17. [S15-R1-017] `worker.lead_audio`：暂停最长仍1500ms。
18. [S15-R1-018] `worker.lead_audio`：负暂停仍归零。
19. [S15-R1-019] `worker.lead_audio`：随机种子不能改变静音。
20. [S15-R1-020] `worker.lead_audio`：人工试听仍是门禁。
21. [S15-R1-021] `worker.run_job`：PCM来源只接受模型和零停顿。
22. [S15-R1-022] `worker.run_job`：不因模型失败回放anchor。
23. [S15-R1-023] `worker.run_job`：不因空结果播放参考。
24. [S15-R1-024] `worker.run_job`：保留nonfinite拒绝。
25. [S15-R1-025] `worker.run_job`：保留异常统计。
26. [S15-R1-026] `worker.run_job`：保留裁边。
27. [S15-R1-027] `worker.run_job`：保留尾部淡出。
28. [S15-R1-028] `worker.run_job`：保留取消检查。
29. [S15-R1-029] `worker.run_job`：保留每GPU互斥。
30. [S15-R1-030] `worker.run_job`：日志报告生成隔离模式。
31. [S15-R1-031] `adapter_engine`：核对原生向量模式。
32. [S15-R1-032] `adapter_engine`：不能把训练参考当输出。
33. [S15-R1-033] `adapter_engine`：固定adapter哈希。
34. [S15-R1-034] `adapter_engine`：损坏adapter不能回退Base。
35. [S15-R1-035] `adapter_engine`：不改变句级缓冲标记。
36. [S15-R1-036] `adapter_engine`：不混驻两种引擎。
37. [S15-R1-037] `adapter_engine`：保持取消丢弃迟到wave。
38. [S15-R1-038] `adapter_engine`：训练候选不自动激活。
39. [S15-R1-039] `adapter_engine`：新进程重载仍需实机。
40. [S15-R1-040] `adapter_engine`：无训练证据不称已训练。
41. [S15-R1-041] `朗读内容`：不拼接参考文本。
42. [S15-R1-042] `朗读内容`：不修改目标文本。
43. [S15-R1-043] `朗读内容`：不补额外说明。
44. [S15-R1-044] `朗读内容`：不以字符串一致冒充声学一致。
45. [S15-R1-045] `朗读内容`：不自动删数字。
46. [S15-R1-046] `朗读内容`：不自动删专名。
47. [S15-R1-047] `朗读内容`：不裁词谋求首声。
48. [S15-R1-048] `朗读内容`：短句仍需语言条件。
49. [S15-R1-049] `朗读内容`：模型幻觉单独披露。
50. [S15-R1-050] `朗读内容`：严格ASR拒播仍未实现。
51. [S15-R1-051] `PCM隔离回归`：以非零参考bank诱捕混入。
52. [S15-R1-052] `PCM隔离回归`：旧环境reference模式也应静音。
53. [S15-R1-053] `PCM隔离回归`：断言生成xvec_only为真。
54. [S15-R1-054] `PCM隔离回归`：断言参考正文为空。
55. [S15-R1-055] `PCM隔离回归`：预热断言与生成相同。
56. [S15-R1-056] `PCM隔离回归`：加载不得读取呼吸文件。
57. [S15-R1-057] `PCM隔离回归`：输出频率标记与参考分离。
58. [S15-R1-058] `PCM隔离回归`：完整协议中仅模型PCM。
59. [S15-R1-059] `PCM隔离回归`：失败流不得补参考。
60. [S15-R1-060] `PCM隔离回归`：重复三轮隔离验证。
61. [S15-R1-061] `音量`：新旧档案统一输出目标。
62. [S15-R1-062] `音量`：默认目标从负21到负18dBFS。
63. [S15-R1-063] `音量`：保留可调输出目标。
64. [S15-R1-064] `音量`：合法范围负24到负14。
65. [S15-R1-065] `音量`：非数字回退默认。
66. [S15-R1-066] `音量`：NaN回退默认。
67. [S15-R1-067] `音量`：正无穷回退默认。
68. [S15-R1-068] `音量`：不修改原始录音。
69. [S15-R1-069] `音量`：保持软限幅。
70. [S15-R1-070] `音量`：不承诺所有音量都增加3dB。
71. [S15-R1-071] `DSP质量`：验证低电平正弦增益。
72. [S15-R1-072] `DSP质量`：验证满幅输入不溢出。
73. [S15-R1-073] `DSP质量`：保留DC blocker。
74. [S15-R1-074] `DSP质量`：保留段间淡入。
75. [S15-R1-075] `DSP质量`：保留尾部淡出。
76. [S15-R1-076] `DSP质量`：Rust与NumPy参数相同。
77. [S15-R1-077] `DSP质量`：不新增C++重复实现。
78. [S15-R1-078] `DSP质量`：采样率不降。
79. [S15-R1-079] `DSP质量`：不硬裁削峰。
80. [S15-R1-080] `DSP质量`：测量使用非语音时标明合成。
81. [S15-R1-081] `GPU显存`：1.7B FP16权重估算约3.4GB。
82. [S15-R1-082] `GPU显存`：两模型权重不是全部显存。
83. [S15-R1-083] `GPU显存`：计入codec和speaker。
84. [S15-R1-084] `GPU显存`：计入KV cache。
85. [S15-R1-085] `GPU显存`：计入CUDA graph。
86. [S15-R1-086] `GPU显存`：计入分配器碎片。
87. [S15-R1-087] `GPU显存`：同卡并发争计算带宽。
88. [S15-R1-088] `GPU显存`：不默认每卡两模型。
89. [S15-R1-089] `GPU显存`：以两卡各一模型为基线。
90. [S15-R1-090] `GPU显存`：真双副本收益必须实测。
91. [S15-R1-091] `所有权与安全`：保留单可见GPU契约。
92. [S15-R1-092] `所有权与安全`：不绕过fleet租约。
93. [S15-R1-093] `所有权与安全`：不删除锁。
94. [S15-R1-094] `所有权与安全`：不按旧PID杀。
95. [S15-R1-095] `所有权与安全`：不安装未知CUDA补丁。
96. [S15-R1-096] `所有权与安全`：不输出口令。
97. [S15-R1-097] `所有权与安全`：不保存用户参考到报告。
98. [S15-R1-098] `所有权与安全`：不自动上传录音。
99. [S15-R1-099] `所有权与安全`：不更改已冻结14。
100. [S15-R1-100] `所有权与安全`：保持3000正式工作台。

---

## 内嵌备忘录：KAGGLE_STEP15_REVIEW2.md

# 第十五阶段第2轮专题审查：100条建议

全源文件读取/哈希与Python AST巡检不等于逐行语义正确证明。重点调用链经过人工分析；建议不是100项已修复。处置与实测边界见AUDIT。

1. [S15-R2-001] `首段分段`：识别当前末尾标点等待lookahead。
2. [S15-R2-002] `首段分段`：只为首段新增即时确定边界。
3. [S15-R2-003] `首段分段`：句末中文标点可立即提交。
4. [S15-R2-004] `首段分段`：逗号达到首段预算可提交。
5. [S15-R2-005] `首段分段`：ASCII点仍等lookahead避小数。
6. [S15-R2-006] `首段分段`：保留后续正常分段。
7. [S15-R2-007] `首段分段`：新段保留原文。
8. [S15-R2-008] `首段分段`：不等待LLM全篇完成。
9. [S15-R2-009] `首段分段`：不为每token发TTS。
10. [S15-R2-010] `首段分段`：短于常规阈值完整句可首发。
11. [S15-R2-011] `单位边界`：英文单词不从中间拆开。
12. [S15-R2-012] `单位边界`：小数12.50不拆错。
13. [S15-R2-013] `单位边界`：英文缩写保留。
14. [S15-R2-014] `单位边界`：标点后引号不能丢。
15. [S15-R2-015] `单位边界`：跨delta空格仍保存。
16. [S15-R2-016] `单位边界`：纯标点不能伪成语音。
17. [S15-R2-017] `单位边界`：Unicode原样。
18. [S15-R2-018] `单位边界`：组合emoji不作为词。
19. [S15-R2-019] `单位边界`：无标点长句保持上限。
20. [S15-R2-020] `单位边界`：最后残留仍Flush。
21. [S15-R2-021] `顺序保护`：首段任务优先。
22. [S15-R2-022] `顺序保护`：第二段可用另一GPU。
23. [S15-R2-023] `顺序保护`：已输出失败不重放。
24. [S15-R2-024] `顺序保护`：未输出失败才允许重试。
25. [S15-R2-025] `顺序保护`：保留段索引。
26. [S15-R2-026] `顺序保护`：保留背压高低水位。
27. [S15-R2-027] `顺序保护`：保留迟滞。
28. [S15-R2-028] `顺序保护`：不无限预生成。
29. [S15-R2-029] `顺序保护`：取消移除排队任务。
30. [S15-R2-030] `顺序保护`：健康检查不回放参考。
31. [S15-R2-031] `LLM流`：保留每delta向前端推送。
32. [S15-R2-032] `LLM流`：首句完成即submit。
33. [S15-R2-033] `LLM流`：首token计时保留。
34. [S15-R2-034] `LLM流`：首段提交计时保留。
35. [S15-R2-035] `LLM流`：LLM完成计时保留。
36. [S15-R2-036] `LLM流`：非法JSON报错。
37. [S15-R2-037] `LLM流`：截断finish_reason报错。
38. [S15-R2-038] `LLM流`：取消终止HTTP。
39. [S15-R2-039] `LLM流`：不记录API密钥。
40. [S15-R2-040] `LLM流`：用本地SSE延迟尾巴测试。
41. [S15-R2-041] `首声指标`：区分首token和首段。
42. [S15-R2-042] `首声指标`：区分模型首块和PCM。
43. [S15-R2-043] `首声指标`：区分首PCM和首播。
44. [S15-R2-044] `首声指标`：静音不当作人声。
45. [S15-R2-045] `首声指标`：保留欠载次数。
46. [S15-R2-046] `首声指标`：不以网络替身称DeepSeek实测。
47. [S15-R2-047] `首声指标`：不以MockRTF称QwenRTF。
48. [S15-R2-048] `首声指标`：记录首段早于LLM结束。
49. [S15-R2-049] `首声指标`：没有CUDA不填GPU延迟。
50. [S15-R2-050] `首声指标`：不承诺三秒内。
51. [S15-R2-051] `播放器`：先不盲降全局缓冲。
52. [S15-R2-052] `播放器`：保持starved恢复阈值。
53. [S15-R2-053] `播放器`：保留短尾完成后启动。
54. [S15-R2-054] `播放器`：停止重置ring。
55. [S15-R2-055] `播放器`：迟到PCM不继续播放。
56. [S15-R2-056] `播放器`：初始化失败可重试。
57. [S15-R2-057] `播放器`：保留浏览器重采样。
58. [S15-R2-058] `播放器`：不将gain无限放大。
59. [S15-R2-059] `播放器`：不新增播放参考audio标签。
60. [S15-R2-060] `播放器`：保持手机布局。
61. [S15-R2-061] `首块预算`：保留默认chunk4稳定策略。
62. [S15-R2-062] `首块预算`：允许显式2到8试验。
63. [S15-R2-063] `首块预算`：无效环境回退4。
64. [S15-R2-064] `首块预算`：后段按背压选择。
65. [S15-R2-065] `首块预算`：不把chunk2必然称更快。
66. [S15-R2-066] `首块预算`：重测小chunk欠载。
67. [S15-R2-067] `首块预算`：记录同文同参考条件。
68. [S15-R2-068] `首块预算`：预热成本单列。
69. [S15-R2-069] `首块预算`：不改变max_new_tokens掩盖。
70. [S15-R2-070] `首块预算`：单句质量需真人听。
71. [S15-R2-071] `线程与语言`：Go保留调度路径。
72. [S15-R2-072] `线程与语言`：Python保留模型接口。
73. [S15-R2-073] `线程与语言`：Rust保留DSP。
74. [S15-R2-074] `线程与语言`：JS保留播放。
75. [S15-R2-075] `线程与语言`：不新加Java网络服务。
76. [S15-R2-076] `线程与语言`：不为多语言复制采样器。
77. [S15-R2-077] `线程与语言`：不盲开每卡双进程。
78. [S15-R2-078] `线程与语言`：不启用不支持的BF16。
79. [S15-R2-079] `线程与语言`：不将TF32称T4加速。
80. [S15-R2-080] `线程与语言`：量化质量另实验。
81. [S15-R2-081] `流式测试`：首句单delta即可产生任务。
82. [S15-R2-082] `流式测试`：短中文完整句可首发。
83. [S15-R2-083] `流式测试`：ASCII数字点仍保留。
84. [S15-R2-084] `流式测试`：逗号完整前缀可首发。
85. [S15-R2-085] `流式测试`：相同文本各切片重组。
86. [S15-R2-086] `流式测试`：新特性用应用配置而非旧配置。
87. [S15-R2-087] `流式测试`：晚引号仍完整保留。
88. [S15-R2-088] `流式测试`：SSE未结束worker已收到首段。
89. [S15-R2-089] `流式测试`：最终按索引输出。
90. [S15-R2-090] `流式测试`：Go race三轮。
91. [S15-R2-091] `退化防护`：非首段旧策略不变。
92. [S15-R2-092] `退化防护`：朗读长文不丢段。
93. [S15-R2-093] `退化防护`：URL不清洗。
94. [S15-R2-094] `退化防护`：DeepSeek错误前缀可见。
95. [S15-R2-095] `退化防护`：超时不冒成功。
96. [S15-R2-096] `退化防护`：取消不重复提交。
97. [S15-R2-097] `退化防护`：独立记录早期失败。
98. [S15-R2-098] `退化防护`：浏览器全量回归。
99. [S15-R2-099] `退化防护`：Python全量回归。
100. [S15-R2-100] `退化防护`：无硬件保持部分验收。

---

## 内嵌备忘录：KAGGLE_STEP15_REVIEW3.md

# 第十五阶段第3轮专题审查：100条建议

全源文件读取/哈希与Python AST巡检不等于逐行语义正确证明。重点调用链经过人工分析；建议不是100项已修复。处置与实测边界见AUDIT。

1. [S15-R3-001] `创建默认`：默认关闭可选GPU候选校准。
2. [S15-R3-002] `创建默认`：保留手动校准按钮。
3. [S15-R3-003] `创建默认`：直接创建与库处理默认一致。
4. [S15-R3-004] `创建默认`：后端缺省也关闭校准。
5. [S15-R3-005] `创建默认`：锁定重置默认关闭。
6. [S15-R3-006] `创建默认`：明确不是训练。
7. [S15-R3-007] `创建默认`：不隐藏校准质量代价。
8. [S15-R3-008] `创建默认`：保留两卡预热。
9. [S15-R3-009] `创建默认`：失败不改active。
10. [S15-R3-010] `创建默认`：完成收据不虚报。
11. [S15-R3-011] `ASR成本`：已知单段短文本直接使用。
12. [S15-R3-012] `ASR成本`：不能把长文本套短片。
13. [S15-R3-013] `ASR成本`：保持全量长音频ASR。
14. [S15-R3-014] `ASR成本`：不取前十秒冒充完整。
15. [S15-R3-015] `ASR成本`：CPU Whisper可驻留复用。
16. [S15-R3-016] `ASR成本`：不在GPU常驻ASR。
17. [S15-R3-017] `ASR成本`：保留CPU回退。
18. [S15-R3-018] `ASR成本`：保留识别beam5。
19. [S15-R3-019] `ASR成本`：保留词时间戳。
20. [S15-R3-020] `ASR成本`：记录手动转写绕过ASR。
21. [S15-R3-021] `ASR内存`：仅CPU默认驻留。
22. [S15-R3-022] `ASR内存`：CUDA ASR仍卸载。
23. [S15-R3-023] `ASR内存`：显式开关可禁用驻留。
24. [S15-R3-024] `ASR内存`：同一重模型入口串行。
25. [S15-R3-025] `ASR内存`：不无限缓存音频。
26. [S15-R3-026] `ASR内存`：不缓存每个用户转写。
27. [S15-R3-027] `ASR内存`：不让驻留伪造模型已加载。
28. [S15-R3-028] `ASR内存`：首次下载成本单列。
29. [S15-R3-029] `ASR内存`：CPU内存风险披露。
30. [S15-R3-030] `ASR内存`：不以第二次速度代表冷启动。
31. [S15-R3-031] `重复计算`：档案内部嵌入按内容哈希复用。
32. [S15-R3-032] `重复计算`：嵌入缓存仅本次任务。
33. [S15-R3-033] `重复计算`：返回向量保持只读语义。
34. [S15-R3-034] `重复计算`：不跨档案泄漏用户数据。
35. [S15-R3-035] `重复计算`：记录embed实际调用数。
36. [S15-R3-036] `重复计算`：记录embed命中数。
37. [S15-R3-037] `重复计算`：候选相同波形可复用。
38. [S15-R3-038] `重复计算`：不按文件名猜相同。
39. [S15-R3-039] `重复计算`：不改变候选排序公式。
40. [S15-R3-040] `重复计算`：缓存失败不写半成品。
41. [S15-R3-041] `CPU候选`：保留24候选上限。
42. [S15-R3-042] `CPU候选`：保留前三非重叠。
43. [S15-R3-043] `CPU候选`：保留SNR打分。
44. [S15-R3-044] `CPU候选`：保留典型性中心。
45. [S15-R3-045] `CPU候选`：保留F0打分。
46. [S15-R3-046] `CPU候选`：准确F0仍用于最佳锚点。
47. [S15-R3-047] `CPU候选`：不偷偷换MFCC冒充ECAPA。
48. [S15-R3-048] `CPU候选`：不降采样输入标准。
49. [S15-R3-049] `CPU候选`：不减少可用文件。
50. [S15-R3-050] `CPU候选`：不承诺质量无损提速倍数。
51. [S15-R3-051] `分析阶段计时`：记录speaker加载。
52. [S15-R3-052] `分析阶段计时`：记录解码降噪。
53. [S15-R3-053] `分析阶段计时`：记录ASR。
54. [S15-R3-054] `分析阶段计时`：记录候选评分。
55. [S15-R3-055] `分析阶段计时`：记录呼吸韵律。
56. [S15-R3-056] `分析阶段计时`：记录worker加载。
57. [S15-R3-057] `分析阶段计时`：记录可选校准。
58. [S15-R3-058] `分析阶段计时`：记录总构建时间。
59. [S15-R3-059] `分析阶段计时`：成功后最终写回profile。
60. [S15-R3-060] `分析阶段计时`：旧calibration写回不能覆盖。
61. [S15-R3-061] `候选转写`：长单个ASR段不能截音频保留全文。
62. [S15-R3-062] `候选转写`：长度超界无可信字时间拒绝。
63. [S15-R3-063] `候选转写`：不猜均匀对齐。
64. [S15-R3-064] `候选转写`：提示重录短段或审核切分。
65. [S15-R3-065] `候选转写`：手动16秒整段可不裁。
66. [S15-R3-066] `候选转写`：候选start/end匹配实际波形。
67. [S15-R3-067] `候选转写`：保留多文件来源。
68. [S15-R3-068] `候选转写`：检查负时间。
69. [S15-R3-069] `候选转写`：检查超音频边界。
70. [S15-R3-070] `候选转写`：不静默截断转写。
71. [S15-R3-071] `持久化`：完成前写回quality.build_s。
72. [S15-R3-072] `持久化`：持久化stage_ms。
73. [S15-R3-073] `持久化`：持久化嵌入缓存统计。
74. [S15-R3-074] `持久化`：失败不删除已有档案。
75. [S15-R3-075] `持久化`：新任务失败清理新目录。
76. [S15-R3-076] `持久化`：保持原子JSON。
77. [S15-R3-077] `持久化`：保留worker_load状态。
78. [S15-R3-078] `持久化`：保留校准选择。
79. [S15-R3-079] `持久化`：不把done当两卡加载成功。
80. [S15-R3-080] `持久化`：文件备份范围清楚。
81. [S15-R3-081] `发布交付`：生成新step15不覆盖14。
82. [S15-R3-082] `发布交付`：新增manifest逐文件校验。
83. [S15-R3-083] `发布交付`：复制页固定15哈希。
84. [S15-R3-084] `发布交付`：下载与剪贴板完整一致。
85. [S15-R3-085] `发布交付`：拒绝剪贴板时可全选。
86. [S15-R3-086] `发布交付`：375px无横向溢出。
87. [S15-R3-087] `发布交付`：冻结正式15文件。
88. [S15-R3-088] `发布交付`：交接完整嵌入新增备忘录。
89. [S15-R3-089] `发布交付`：三轮结果分别记录。
90. [S15-R3-090] `发布交付`：未通过项目不得打勾。
91. [S15-R3-091] `现场门禁`：用户截图256.4秒仅作问题证据。
92. [S15-R3-092] `现场门禁`：无原音频不能确定泄漏根因。
93. [S15-R3-093] `现场门禁`：真实Qwen生成必须试听。
94. [S15-R3-094] `现场门禁`：真实T4显存峰值必测。
95. [S15-R3-095] `现场门禁`：同卡双模型不默认试。
96. [S15-R3-096] `现场门禁`：首次和热创建分别测。
97. [S15-R3-097] `现场门禁`：同参考同目标文本比较。
98. [S15-R3-098] `现场门禁`：无额外参考重播需独立检查。
99. [S15-R3-099] `现场门禁`：历史网页训练缺口仍保留。
100. [S15-R3-100] `现场门禁`：不写100%无错误。

---

## 内嵌备忘录：KAGGLE_STEP15_PLAN.md

# 第十五阶段实施方案（产品修改前落盘）

## 优先目标
用户实机截图显示创建档案256.4秒，并报告播放中混入参考录音。截图本身无音频，不能判断确切声学根因。目标是生成路径强隔离、首个完整文字前缀及时调度、更响但不过载、减少可避免的创建等待。

## 三轮研究与顺序自问
已读取全源文件三遍，记录哈希及Python AST；分别分析worker/参考隔离、Go流/浏览器首播、analyst创建/持久化。不是穷尽语义证明。每轮100项建议在REVIEW1–3；问题16→17→18每题回答后50项落实建议已追加DECISIONS。不向用户追问，不承诺100%无错误。

## 分步实施
1. 冻结原始至14、正式工作台15文件。生成独立step15，不改历史包。
2. Faster加载、预热、生成统一x-vector-only，参考正文不参与生成；彻底禁止参考呼吸bank读入/拼接。仅模型输出和零停顿可进入播放。此模式可能改变韵律/音色相似度，不能冒称保质已验。
3. Go仅首段在确定的中文句末/逗号边界及时提交，不等后续delta；英文点仍保留小数lookahead。文本、任务顺序、背压、取消不重写。
4. Worker统一输出目标默认-18dBFS（原-21），覆盖旧档案；QTTS_OUTPUT_DBFS允许-24..-14，非法/非有限回退-18。原始录音不改，保留Rust/NumPy软限幅。
5. 默认关闭可选GPU候选校准，手动入口保留；CPU ASR允许复用（QTTS_ASR_KEEP_CPU=0关闭，CUDA仍卸载）；本次构建嵌入哈希去重；保留全部数据、24候选和评分公式。记录阶段耗时、最终build_s与缓存统计；修正超长ASR单段截音频配全文的危险回退。
6. 增加参考隔离、音量、阶段收据、默认校准与首句SSE尚未结束就开始TTS测试。三轮完整Python/Node/Go race/浏览器，协议与模型接口实验分开记录。
7. 完整重打包、复制下载逐字节验证；汇总审查处置、失败修复记录、快速使用和完整内嵌备忘录交接。

## 双副本结论
1.7B FP16纯参数约3.4GB；双份约6.8GB不含codec、KV、graph、临时张量。两个副本共享同一T4的计算/带宽，不能据此推论单请求更快，OOM风险须实机测。保留每T4一个模型、两T4并行相邻段。未经实测不默认增加副本，不量化/换语言冒充无损提速。

## 验收边界
CPU模型接口/合成信号不是完整Qwen声学实验。本环境无CUDA、真实DeepSeek服务凭据或用户原音频，不能宣布T4速度、音色相似度、零错字、实际256秒降低多少已验收。已有网页训练闭环/长数据全覆盖/严格声学拒播缺口仍未完成。本轮先对可验证工程范围执行三轮，真实硬件项保持BLOCKED并给现场门禁，不能循环空跑到假成功。

---

## 内嵌备忘录：KAGGLE_STEP15_AUDIT.md

# 第十五阶段：参考隔离、首句调度、增响与创建成本审查

日期2026-10-22。**工程实现已完成本轮选定范围，真实Qwen/T4音质与性能仍BLOCKED；不是全部用户需求完成。**

## 用户证据与根因边界
用户提供step14实际网页截图：BZM档案可见、候选6.3/6.4秒、创建日志256.4秒，报告克隆播放中插入原参考录音。截图不包含输出音频、GPU显存与分阶段耗时，所以不能确定这次具体是参考呼吸、ICL串音、模型幻觉或别的声学现象。

查阅实际PyPI Faster0.5.4 wheel的model.py，SHA256 `7d45740b805bb1a4798fbe20ffd580e2a35361e744c4645da106c2b6383d4de2`：ICL模式将ref_codes放入声学解码上下文，再裁去参考部分；上游xvec_only说明明确针对phoneme bleed-through。旧worker三个调用点均xvec_only=False。另有QTTS_BREATH_MODE=reference的显式参考呼吸拼接路径。当前14默认off不能证明该用户开启了reference，不能以存在这条路径就宣布确切根因已证实。

## 本轮实际改动
### 1. 强隔离生成
- worker.RealEngine档案加载、dtype回退预热、正式流式生成统一xvec_only=True、ref_text为空、append_silence=False。参考文件仅用于提取说话人向量，不向Faster ICL提供参考文本/声学码。
- Worker不再读取breath_files，不论旧环境reference设置如何，lead_audio只返回有界零停顿。没有参考音频低延迟占位或失败时回放参考的路径。
- stats使用reference_pcm_splicing=false描述代码策略，acoustic_text_verified仍false。模型自身呼吸不滤除，不能据此保证没有生成幻觉或逐字完全一致。
- 向量模式会改变ICL条件；韵律、口音、音色相似度可能变化，必须真实试听，不称无损切换或已有质量提升。

### 2. 首句调度
- Go新增LiveSegCfg，仅聊天首段使用。完整中文句末、问叹号及达到首段7units的分句不再要求下一delta；短完整句可首发，尾部空格同样处理。
- ASCII点仍等lookahead，避免12.50被拆成12.；未闭合引号/括号保持等待。普通朗读仍ExactSegCfg，后续段和取消、两GPU调度、有序转发、背压、播放器水位不变。
- 没有每token发TTS，LLM尚无确定边界时仍可能积累到FirstMax。纯标点/空白片段仍沿旧过滤，文本分段不是声学ASR核验。
- 实际本地HTTP/SSE实验让LLM尾巴阻塞，观察首段已进入真实scheduler并被HTTP worker fixture接收，再释放LLM尾巴。不是远程DeepSeek或Qwen速度证据。

### 3. 有界增响
- qtts_common.output_target_dbfs共享解析，默认-18dBFS，允许QTTS_OUTPUT_DBFS=-24..-14，非法/非有限回退-18。
- 旧、新档案重新加载时统一使用该输出目标及最大增益12dB（旧9dB），不修改原始录音；保留Rust/NumPy DC blocker、增益平滑、软限幅、淡入淡出。
- 低电平合成正弦验证目标效果及限幅；并非任意语音、静音或硬件音量都会增加恰好3dB，也不是响度LUFS认证。

### 4. 创建成本与正确性
- 网页直建、库处理、后端缺省均关闭可选GPU候选校准；手动按钮和显式勾选保留。不是偷偷删除全部质量模型，不把减少可选校准称质量等价证明。
- CPU Whisper允许跨任务复用同一个模型；QTTS_ASR_KEEP_CPU=0恢复释放；CUDA ASR仍卸载，避免与TTS争VRAM。ASR改RLock保护加载、完整惰性转写及释放；并发回归确认迭代结束前不能释放模型。保留large-v3、beam5、词时间戳与全录音处理，未靠降低识别质量提速。
- 构建局部嵌入缓存按float32样本内容SHA256去重，最多64条、每向量≤16KiB；不持久化录音或向量缓存、不跨声音任务复用。保留24候选、评分公式和最佳锚点准确F0。
- quality.stage_ms记录speaker_load/decode_denoise/asr/candidate_scoring/prosody_analysis/worker_load/optional_calibration；build_s与embedding_cache最终写回profile，页面可以展开查看。重新读取校准后的profile再合并quality，避免覆盖校准选择。
- 修复候选回退截前14秒却配整段文字的问题；仅允许完整2.5–16秒对齐片段，过长不猜切分、明确拒绝。可信手动16秒全文不再被截14秒。这是必要的安全拒绝，不是所有长ASR片段现在都自动可用。
- 首次下载/CPU大模型ASR与ECAPA/F0仍可能很慢；没有拿用户原录音做A/B，不能声称256.4秒已降到某个数值或“大幅提速已实测”。

## 为什么不每张T4放两个1.7B
纯参数1.7e9×2字节约3.4GB/份（十进制），两份约6.8GB；不是整个进程显存。codec、speaker、KV、CUDA graphs、临时张量和碎片另计；同时执行共享同一张T4的计算和带宽。装得下不等于单请求更快，额外副本也可能OOM/恶化首声。当前保持两T4各一模型，用两卡并行相邻段。没有双副本T4实测，不报告可装下或收益。

## 三轮检查与建议处置
REVIEW1/2/3各100项，前置review-before.json记录三次全源文件读取/哈希/Python AST，不是逐行语义正确证明。DECISIONS问题16/17/18顺序展开，每题50建议；累计18题900建议。300条逐项处置见review-disposition.json，区分implemented/preserved/documented-boundary/requires-hardware/not-implemented，不把建议数量当修复数。

## 验证结果（最终计数以final-checks.json为准）
- Python全量301项×3、Node30项×3、Go race count3；新16项隔离/音量/创建成本单测。
- 完整Chromium120项×3=360项在修正等义文案断言后全部通过（10.5分钟），最终完整包剪贴板另3轮通过；独立复制页剪贴板、下载、权限拒绝全选、375px三轮通过。初次357通过/3文案失败日志保留，不隐去。
- 实际Faster0.5.4 resolver→prepare_generation→两阶段streaming控制流三轮，每轮chunk2/4/8，经过生产RealEngine包装；CPU prompt、talker算子与codec为明确注入fixture，40帧/76800样本完整，参考码入decoder为0。不是完整Qwen语音模型。
- 实际完整Faster/Qwen库导入+2651参数tiny Mimi构造/保存/重载三轮通过；强制HF RoPE CPU preflight三轮通过，整体因无CUDA为blocked。
- ownership/input HTTP/codes CLI/mock pipeline/真实本地Go+HTTP+SSE adapter/fatal进程脚本各含三轮，全部三轮通过，结果见收据。
- frozen13与当前实际训练源码CPU tiny LoRA A/B另做三进程×三epoch/6步，loss/全部adapter逐位相同；tokenize12→3。墙钟含冷优化器启动/顺序偏差，不能报告训练倍速或Qwen质量。
- 正式3000项目15文件/revision和原始至14打包件哈希不变。独立3001提供step15完整代码，非Python在线执行器。

## 本轮发现的初始失败，未隐去
1. 验证环境初次启动先重建venv、但日志目录尚未创建，重定向失败exit1；创建目录后安装成功，非产品bug。
2. 初版增响测试发现同一9dB最大增益使很小信号两种目标都饱和于同一上限，无法变响；worker最大增益改为有界12dB，保留软限幅并验证通过。不能只改测试阈值掩盖。
3. 首段HTTP实验最初直接从Session.jobs取任务，早于Scheduler.Submit填写enq，race报错；改为真实scheduler队列锁下pickLocked，避免测试绕过生产同步。最终race三轮通过；此处是新测试夹具错误，没有无依据修改生产锁。
4. 补充首句带尾部空格的边界用例，并同步修复第二处lookahead等待。
5. 初次完整浏览器三轮357通过、3失败，均为旧用例要求“网页训练执行尚未闭环”但新版等义文案为“网页训练尚未闭环”；断言兼容可选“执行”，仍强制展示未闭环，不删除门禁。原日志browser-initial-repeat3.txt保留，完整三轮重跑。
6. CPU驻留复核发现原ASR锁只护加载，惰性转写与释放可能并发；改可重入锁覆盖整个使用周期，并发门禁通过，重新执行三轮全量Python和协议。
7. 交接刷新脚本从39备忘录移植时剩余一个unique数量断言未改，最初assert失败；改为45，完整内嵌及逐篇读回验证，不影响产品包。
8. 首次最终汇总校验器错误地假定协议日志只有3条JSON；输入HTTP含另一组库HTTP收据、adapter含独立损坏拒绝收据。按收据字段/round筛选三轮，并额外强制检查库HTTP与损坏adapter无PCM回退，不删除任何真实失败检查。初始校验器失败日志已保存。

## 保留阻塞
真实Qwen/T4三轮生成、参考重播排查试听、向量模式相似度、真实首播/欠载A/B、首次/热创建同录音A/B、Rust现场DSP和每卡双副本显存/吞吐未验收。没有访问用户GPU和原音频，不可模拟填成功。

历史网页真实训练控制面/维护租约移交/start-cancel-restore-publish、长数据审核对齐/超过16样本完整覆盖、真实训练保质吞吐、严格声学逐字拒播仍未实现/未验收；本轮不是对这些要求的豁免。整体状态PARTIAL/BLOCKED。

---

## 内嵌备忘录：KAGGLE_STEP15_QUICKSTART.md

# step15升级与现场验收

这是参考隔离/首句调度/输出增响/创建成本部分修复，不是全部目标完成，真实Qwen/T4提速和音质尚未验收。

## 升级
1. 下载自己需要保留的私有libraries/profiles及已有training_data/training_codes/training_runs；浏览器待提交录音先保存到库，再备份到自己的设备。不能把Kaggle工作目录当永久备份，不发口令或私人音频给聊天。
2. 停止并重启完整Kaggle会话，不只刷新网页/内核，不按旧PID杀、不删除GPU锁。
3. 选择T4×2、Internet开启；保持平台Torch/CUDA，不自行降级HF/Transformers。
4. 在新启动单元格之前运行下面配置，再将3001复制页的完整kaggle-fixed-step15.py放另一个Code单元格执行。

```python
import os
os.environ['QTTS_MOCK'] = '0'
os.environ['QTTS_TTS_ENGINE'] = 'faster'
os.environ['QTTS_FIRST_CHUNK_SIZE'] = '4'
os.environ['QTTS_OUTPUT_DBFS'] = '-18'
os.environ['QTTS_ASR_KEEP_CPU'] = '1'
os.environ.pop('QTTS_UNPACK_ONLY', None)
```

QTTS_BREATH_MODE=reference在step15已不能启用参考拼接，不必为它删改私有档案。源录音仍保留供音色向量提取、审查和备份，禁止拼接不等于删除源数据。

5. 等required RoPE检查pass、两worker加载/预热ready及QTTS ready后打开网址解锁。SystemExit0正常，不要重复启动。网页应显示“第十五阶段”，旧网页需刷新；若报锁冲突，停止重复启动，不删锁。
6. 可以直接重新启用已有普通参考档案，无需先重新录制。新worker会用向量模式重建缓存，旧档案输出目标也为-18。模型韵律/口音/音色相似度可能变化，不能因网页成功就认为质量已验收。

## 先做直接朗读
选择与参考内容明显不同的短目标句，例如“这次只朗读屏幕上的这句话，现在检查是否有多余内容。”，使用直接朗读模式，听有没有参考里的原话、漏字/添字/重复、断句或爆音。先不用DeepSeek，隔离文字生成变量。随后用中英混合、数字和长段测试。

普通档案参考文本仍用于转写审查/候选评分，当前向量生成不会朗读该文本；保存参考文本不会把它加入目标朗读。目标文字只来自直接朗读输入或DeepSeek正文。

程序禁用的是参考PCM拼接和ICL参考码上下文；没有自动ASR拒播门禁，模型仍可能幻觉，不能承诺零额外内容。

## 首句与增响
- 再切DeepSeek聊天，完整第一句/足够长分句就会提交TTS，不等全篇；不是每个token立即合成。
- 默认chunk4保持稳定播放器水位。先测first_played_ms/underruns，只有同文同档案对照时再试chunk2，变差恢复4。
- 输出默认-18dBFS、最大增益12dB，并保留限幅。音量仍不足可在下一次启动前试QTTS_OUTPUT_DBFS='-16'；合法范围-24..-14，先调耳机到安全音量，避免听力损伤。不会对所有声音精确增大3dB，不保证硬件外放效果。

## 创建档案
默认不勾选较慢的额外GPU校准，手动“候选校准”仍可用。单个≤16秒且有逐字匹配全文的录音可填写已知文本跳过ASR；不要凭空编转写。多段/长录音仍全量转写和评分，不只取前几秒。CPU Whisper模型复用会占用内存，内存紧张可设置QTTS_ASR_KEEP_CPU='0'后完整重启。

创建后在档案“创建阶段耗时”展开看实际分阶段时间。首次模型下载/加载仍可能慢；没有该录音的实测数据，不能给出固定秒数。过长单个ASR段没有可信短段对齐会明确拒绝，不再截14秒却配全文。

## 目标机三轮门禁（目前未执行）
每轮使用同一参考、不同于参考的相同测试文本；区分首次/热创建。记录：
- 两张T4唯一worker、每GPU峰值显存、引擎非Mock。
- 仅生成目标内容且不重播参考的实际试听；保留向量模式与13/14的音色/韵律差异记录。
- 首token/首段/首PCM/first_played_ms/underruns，不能把静音当首声。
- quality.stage_ms和build_s，校准开关一致才比较成本；不能拿关闭校准称同等完整校准快多少。
- 停止、中途取消、切换声音、长回答顺序、物理十多分钟录音和备份。

不默认试每T4双副本。两份权重约6.8GB不含其他显存，同卡共享计算，不保证更快。网页训练执行闭环与声学逐字拒播仍未完成，参考处理/快照不是训练。

---

## 内嵌备忘录：KAGGLE_STEP16_REVIEW1.md

# 第十六阶段第1轮专题审查：100条建议

全源读取/哈希/AST不等于逐行语义无错。重点调用链人工分析，未实测声学或GPU性能不填成功。

1. [S16-R1-001] `参考条件`：重新审视15强制向量模式。
2. [S16-R1-002] `参考条件`：默认恢复匹配转写的ICL条件。
3. [S16-R1-003] `参考条件`：无转写不得静默假设ICL。
4. [S16-R1-004] `参考条件`：向量模式保留为显式选项。
5. [S16-R1-005] `参考条件`：参考文本只作条件不拼目标正文。
6. [S16-R1-006] `参考条件`：解码器不接参考码。
7. [S16-R1-007] `参考条件`：保留原始参考录音。
8. [S16-R1-008] `参考条件`：不把恢复ICL称相似度已验证。
9. [S16-R1-009] `参考条件`：检查参考是否多人。
10. [S16-R1-010] `参考条件`：多人参考必须换干净单人样本。
11. [S16-R1-011] `提示缓存`：核查Faster路径键缓存。
12. [S16-R1-012] `提示缓存`：相同路径换音频必须失效。
13. [S16-R1-013] `提示缓存`：比较参考内容哈希。
14. [S16-R1-014] `提示缓存`：清除该路径旧缓存项。
15. [S16-R1-015] `提示缓存`：不删除模型全局权重。
16. [S16-R1-016] `提示缓存`：不信任仅profile_id相同。
17. [S16-R1-017] `提示缓存`：预热与生成采用同模式。
18. [S16-R1-018] `提示缓存`：dtype重载后重新构建条件。
19. [S16-R1-019] `提示缓存`：不把错误预热当就绪。
20. [S16-R1-020] `提示缓存`：缓存失效增加回归。
21. [S16-R1-021] `会话绑定`：会话开始固定参考内容指纹。
22. [S16-R1-022] `会话绑定`：Go与Python指纹算法一致。
23. [S16-R1-023] `会话绑定`：包含WAV与匹配文本。
24. [S16-R1-024] `会话绑定`：包含语言字段。
25. [S16-R1-025] `会话绑定`：长度前缀避免分隔歧义。
26. [S16-R1-026] `会话绑定`：每个语段携带同一指纹。
27. [S16-R1-027] `会话绑定`：Worker取锁后重新读取档案。
28. [S16-R1-028] `会话绑定`：不同版本先拒绝后输出。
29. [S16-R1-029] `会话绑定`：不重试成另一个声音。
30. [S16-R1-030] `会话绑定`：缺文件不降级原模型。
31. [S16-R1-031] `双卡一致`：保留每T4一个模型。
32. [S16-R1-032] `双卡一致`：比较两卡使用的参考指纹。
33. [S16-R1-033] `双卡一致`：保留同session条件不变。
34. [S16-R1-034] `双卡一致`：候选切换只能影响新会话。
35. [S16-R1-035] `双卡一致`：旧会话版本不符明确失败。
36. [S16-R1-036] `双卡一致`：声音更新与合成共用锁。
37. [S16-R1-037] `双卡一致`：锁后重取profile避免旧引用。
38. [S16-R1-038] `双卡一致`：不要以profile名称证明相同。
39. [S16-R1-039] `双卡一致`：不把RMS一致当同一说话人。
40. [S16-R1-040] `双卡一致`：两张卡实际试听仍必需。
41. [S16-R1-041] `生成稳定`：相邻段使用稳定seed策略。
42. [S16-R1-042] `生成稳定`：不随意每段改变采样条件。
43. [S16-R1-043] `生成稳定`：不以降温保证身份。
44. [S16-R1-044] `生成稳定`：不默认删除情感。
45. [S16-R1-045] `生成稳定`：保留语言参数。
46. [S16-R1-046] `生成稳定`：保留max_new_tokens安全预算。
47. [S16-R1-047] `生成稳定`：保留取消后的生成器close。
48. [S16-R1-048] `生成稳定`：不引入随机参考混合。
49. [S16-R1-049] `生成稳定`：不混用候选锚点。
50. [S16-R1-050] `生成稳定`：不跨用户共享提示。
51. [S16-R1-051] `档案变更`：修正候选更换原路径复用。
52. [S16-R1-052] `档案变更`：文本更改触发提示失效。
53. [S16-R1-053] `档案变更`：手动校准选择不能覆盖回旧。
54. [S16-R1-054] `档案变更`：完成后保存阶段收据。
55. [S16-R1-055] `档案变更`：删除档案不能被旧请求静默复活。
56. [S16-R1-056] `档案变更`：不删除冻结15。
57. [S16-R1-057] `档案变更`：旧档案可重新加载。
58. [S16-R1-058] `档案变更`：参考需审核逐字转写。
59. [S16-R1-059] `档案变更`：ASR提案不是人工真值。
60. [S16-R1-060] `档案变更`：不从短片猜长文。
61. [S16-R1-061] `安全读取`：锚点仅单一安全文件名。
62. [S16-R1-062] `安全读取`：拒绝符号链接。
63. [S16-R1-063] `安全读取`：拒绝目录冒音频。
64. [S16-R1-064] `安全读取`：限制参考读取字节。
65. [S16-R1-065] `安全读取`：路径始终在档案目录。
66. [S16-R1-066] `安全读取`：哈希不输出原音频。
67. [S16-R1-067] `安全读取`：指纹不是授权证明。
68. [S16-R1-068] `安全读取`：不泄漏访问口令。
69. [S16-R1-069] `安全读取`：不自动云传录音。
70. [S16-R1-070] `安全读取`：保持私有备份边界。
71. [S16-R1-071] `原生adapter`：保留训练候选固定binding。
72. [S16-R1-072] `原生adapter`：不向faster注入adapter。
73. [S16-R1-073] `原生adapter`：不修改训练权重。
74. [S16-R1-074] `原生adapter`：缺adapter不回退Base。
75. [S16-R1-075] `原生adapter`：保留句级缓冲标记。
76. [S16-R1-076] `原生adapter`：继续核对Base哈希。
77. [S16-R1-077] `原生adapter`：旧训练功能做回归。
78. [S16-R1-078] `原生adapter`：不要把参考处理叫训练。
79. [S16-R1-079] `原生adapter`：网页真实训练缺口保留。
80. [S16-R1-080] `原生adapter`：真实训练质量仍待验收。
81. [S16-R1-081] `相似度验收`：相似度用真实说话人模型。
82. [S16-R1-082] `相似度验收`：不能伪造99.5百分比。
83. [S16-R1-083] `相似度验收`：文字一致不代表音色一致。
84. [S16-R1-084] `相似度验收`：多段输出分别试听。
85. [S16-R1-085] `相似度验收`：比较两卡相邻段。
86. [S16-R1-086] `相似度验收`：使用与参考不同的目标文字。
87. [S16-R1-087] `相似度验收`：同参考同文同seed对照。
88. [S16-R1-088] `相似度验收`：保留参考与输出独立文件。
89. [S16-R1-089] `相似度验收`：无用户音频不猜根因。
90. [S16-R1-090] `相似度验收`：不承诺100无错。
91. [S16-R1-091] `保护已有功能`：保留原文分段。
92. [S16-R1-092] `保护已有功能`：保留首句及时调度。
93. [S16-R1-093] `保护已有功能`：保留两主视图。
94. [S16-R1-094] `保护已有功能`：保留长录音预算。
95. [S16-R1-095] `保护已有功能`：保留命名空库。
96. [S16-R1-096] `保护已有功能`：保留失败本地片段。
97. [S16-R1-097] `保护已有功能`：保留手动候选校准。
98. [S16-R1-098] `保护已有功能`：保留DeepSeek取消。
99. [S16-R1-099] `保护已有功能`：保留3000正式工作台。
100. [S16-R1-100] `保护已有功能`：保留原始至15整包。

---

## 内嵌备忘录：KAGGLE_STEP16_REVIEW2.md

# 第十六阶段第2轮专题审查：100条建议

全源读取/哈希/AST不等于逐行语义无错。重点调用链人工分析，未实测声学或GPU性能不填成功。

1. [S16-R2-001] `解码路径`：使用实际Faster0.5.4准备接口。
2. [S16-R2-002] `解码路径`：只解码新生成声学码。
3. [S16-R2-003] `解码路径`：禁止参考PCM占位。
4. [S16-R2-004] `解码路径`：不得猜比例裁参考音频。
5. [S16-R2-005] `解码路径`：codec采样率必须24k。
6. [S16-R2-006] `解码路径`：逐帧1920样本契约需检查。
7. [S16-R2-007] `解码路径`：不兼容长度明确失败。
8. [S16-R2-008] `解码路径`：保留码组16列。
9. [S16-R2-009] `解码路径`：不偷改codec权重。
10. [S16-R2-010] `解码路径`：API签名变化明确报错。
11. [S16-R2-011] `有界窗口`：删除每块全历史cat。
12. [S16-R2-012] `有界窗口`：左上下文固定25帧。
13. [S16-R2-013] `有界窗口`：待提交尾部保留2帧。
14. [S16-R2-014] `有界窗口`：窗口随chunk有上限。
15. [S16-R2-015] `有界窗口`：新块仅输出未提交样本。
16. [S16-R2-016] `有界窗口`：提交游标单调。
17. [S16-R2-017] `有界窗口`：末尾只flush一次。
18. [S16-R2-018] `有界窗口`：取消不flush迟到音频。
19. [S16-R2-019] `有界窗口`：新旧窗口无重复样本。
20. [S16-R2-020] `有界窗口`：窗口长度记录便于核验。
21. [S16-R2-021] `块接缝`：未来两帧降低边缘重解码差异。
22. [S16-R2-022] `块接缝`：不对每块单独归一化。
23. [S16-R2-023] `块接缝`：保留时间连续性。
24. [S16-R2-024] `块接缝`：不要对每块强淡入。
25. [S16-R2-025] `块接缝`：短于lookahead暂不输出。
26. [S16-R2-026] `块接缝`：最后短块不能丢。
27. [S16-R2-027] `块接缝`：音频总样本不缩水。
28. [S16-R2-028] `块接缝`：不把重叠输出拼两次。
29. [S16-R2-029] `块接缝`：真实边界爆音仍要听。
30. [S16-R2-030] `块接缝`：增加右边缘不稳定fixture。
31. [S16-R2-031] `沙沙声`：不生成额外呼吸噪声。
32. [S16-R2-032] `沙沙声`：旧breath环境不能启用拼接。
33. [S16-R2-033] `沙沙声`：限制向上增益防底噪变大。
34. [S16-R2-034] `沙沙声`：输出目标仍负18dBFS。
35. [S16-R2-035] `沙沙声`：保留软限幅。
36. [S16-R2-036] `沙沙声`：不默认强低通损坏齿音。
37. [S16-R2-037] `沙沙声`：不抹掉所有清辅音。
38. [S16-R2-038] `沙沙声`：不假装无声就是降噪成功。
39. [S16-R2-039] `沙沙声`：无原音频不确定噪声来源。
40. [S16-R2-040] `沙沙声`：分别检查模型原PCM与后处理。
41. [S16-R2-041] `响度状态`：每任务重建leveler状态。
42. [S16-R2-042] `响度状态`：防双卡历史包络不同。
43. [S16-R2-043] `响度状态`：保留每段淡入淡出。
44. [S16-R2-044] `响度状态`：无语音不flush上段尾巴。
45. [S16-R2-045] `响度状态`：显式配置最大增益。
46. [S16-R2-046] `响度状态`：非法增益回退安全值。
47. [S16-R2-047] `响度状态`：新旧档案一致输出策略。
48. [S16-R2-048] `响度状态`：不能靠过载变响。
49. [S16-R2-049] `响度状态`：用低电平与满幅信号测试。
50. [S16-R2-050] `响度状态`：Rust与NumPy分别标边界。
51. [S16-R2-051] `RTF定义`：标准RTF等于生成墙钟除语音秒数。
52. [S16-R2-052] `RTF定义`：rtf_x是其倒数不是RTF。
53. [S16-R2-053] `RTF定义`：不把双卡速度相加冒单卡RTF。
54. [S16-R2-054] `RTF定义`：排除零停顿分母。
55. [S16-R2-055] `RTF定义`：失败取消样本不能算通过。
56. [S16-R2-056] `RTF定义`：冷预热与热态分开。
57. [S16-R2-057] `RTF定义`：首播与吞吐分开。
58. [S16-R2-058] `RTF定义`：记录每GPU结果。
59. [S16-R2-059] `RTF定义`：目标0.3需每条和汇总检查。
60. [S16-R2-060] `RTF定义`：无T4输出blocked。
61. [S16-R2-061] `计时拆分`：模型prepare单独计时。
62. [S16-R2-062] `计时拆分`：token生成单独计时。
63. [S16-R2-063] `计时拆分`：codec解码单独计时。
64. [S16-R2-064] `计时拆分`：DSP耗时单列。
65. [S16-R2-065] `计时拆分`：总墙钟包括必要同步。
66. [S16-R2-066] `计时拆分`：不拿CPU异步发射当CUDA完成。
67. [S16-R2-067] `计时拆分`：预热不计入热态却单独报告。
68. [S16-R2-068] `计时拆分`：报告first_played与欠载。
69. [S16-R2-069] `计时拆分`：保存原始测量行。
70. [S16-R2-070] `计时拆分`：不删慢样本。
71. [S16-R2-071] `性能选择`：仍用CUDA graph后端。
72. [S16-R2-072] `性能选择`：不盲开torch.compile。
73. [S16-R2-073] `性能选择`：T4继续FP16。
74. [S16-R2-074] `性能选择`：不假称T4原生BF16。
75. [S16-R2-075] `性能选择`：不为语言数量加网络跳转。
76. [S16-R2-076] `性能选择`：不每卡塞两副本。
77. [S16-R2-077] `性能选择`：上下文有界减少复制。
78. [S16-R2-078] `性能选择`：参考prompt按版本复用。
79. [S16-R2-079] `性能选择`：较大后段chunk做可选实测。
80. [S16-R2-080] `性能选择`：质量不降需要真实对照。
81. [S16-R2-081] `实验设计`：同一参考与目标文。
82. [S16-R2-082] `实验设计`：至少三轮独立进程接口实验。
83. [S16-R2-083] `实验设计`：每个chunk2/4/8/12检查。
84. [S16-R2-084] `实验设计`：检查短尾与取消。
85. [S16-R2-085] `实验设计`：参考码标记不能入decoder。
86. [S16-R2-086] `实验设计`：生成总帧对应总样本。
87. [S16-R2-087] `实验设计`：检查窗口峰值上限。
88. [S16-R2-088] `实验设计`：性能fixture不算Qwen性能。
89. [S16-R2-089] `实验设计`：CPU tinyMimi不算完整TTS。
90. [S16-R2-090] `实验设计`：硬件结果不能编造。
91. [S16-R2-091] `降级与边界`：新解码模式不自动回旧混参考路径。
92. [S16-R2-092] `降级与边界`：ICL缺文本给明确提示。
93. [S16-R2-093] `降级与边界`：不要静默改为别的声音。
94. [S16-R2-094] `降级与边界`：不要自动降模型大小。
95. [S16-R2-095] `降级与边界`：不改语速充RTF。
96. [S16-R2-096] `降级与边界`：不删用户正文充速度。
97. [S16-R2-097] `降级与边界`：不缩减训练数据。
98. [S16-R2-098] `降级与边界`：保留故障监督。
99. [S16-R2-099] `降级与边界`：记下每次初始失败。
100. [S16-R2-100] `降级与边界`：整体仍按证据判定。

---

## 内嵌备忘录：KAGGLE_STEP16_REVIEW3.md

# 第十六阶段第3轮专题审查：100条建议

全源读取/哈希/AST不等于逐行语义无错。重点调用链人工分析，未实测声学或GPU性能不填成功。

1. [S16-R3-001] `代码审查`：三轮读全源并记录哈希。
2. [S16-R3-002] `代码审查`：Python AST巡检。
3. [S16-R3-003] `代码审查`：Go格式和race。
4. [S16-R3-004] `代码审查`：浏览器JS语法。
5. [S16-R3-005] `代码审查`：Rust未修改仍说明现场边界。
6. [S16-R3-006] `代码审查`：逐专题审视引用关系。
7. [S16-R3-007] `代码审查`：不把哈希清单当语义证明。
8. [S16-R3-008] `代码审查`：每轮100建议逐项处置。
9. [S16-R3-009] `代码审查`：未实施项明确保留。
10. [S16-R3-010] `代码审查`：别把300建议当300bug。
11. [S16-R3-011] `参考绑定测试`：中英转写跨语言指纹一致。
12. [S16-R3-012] `参考绑定测试`：WAV变更指纹变化。
13. [S16-R3-013] `参考绑定测试`：文本变更指纹变化。
14. [S16-R3-014] `参考绑定测试`：语言变更指纹变化。
15. [S16-R3-015] `参考绑定测试`：质量统计变化不改变声音指纹。
16. [S16-R3-016] `参考绑定测试`：旧Worker缓存不能放行新pin。
17. [S16-R3-017] `参考绑定测试`：任务等待期间换档案需重校验。
18. [S16-R3-018] `参考绑定测试`：错误绑定不能输出PCM。
19. [S16-R3-019] `参考绑定测试`：两卡pin不等必须失败。
20. [S16-R3-020] `参考绑定测试`：取消不触发重加载。
21. [S16-R3-021] `解码测试`：样本总数等于总帧乘1920。
22. [S16-R3-022] `解码测试`：reference marker严格拒绝。
23. [S16-R3-023] `解码测试`：短码块可暂存。
24. [S16-R3-024] `解码测试`：最大窗口有界。
25. [S16-R3-025] `解码测试`：窗口左端超出不可访问。
26. [S16-R3-026] `解码测试`：lookahead尾部完整flush。
27. [S16-R3-027] `解码测试`：flush幂等。
28. [S16-R3-028] `解码测试`：取消丢尾部。
29. [S16-R3-029] `解码测试`：非有限输出不得成功。
30. [S16-R3-030] `解码测试`：错误采样率拒绝。
31. [S16-R3-031] `RTF实验入口`：调用真实worker而非造测量。
32. [S16-R3-032] `RTF实验入口`：用户显式启用目标机测试。
33. [S16-R3-033] `RTF实验入口`：不启动第三模型。
34. [S16-R3-034] `RTF实验入口`：仅读取既有档案。
35. [S16-R3-035] `RTF实验入口`：保存生成WAV供试听。
36. [S16-R3-036] `RTF实验入口`：报告不含口令。
37. [S16-R3-037] `RTF实验入口`：至少三次重复。
38. [S16-R3-038] `RTF实验入口`：测前确认双worker真实引擎。
39. [S16-R3-039] `RTF实验入口`：未达0.3就failed而非pass。
40. [S16-R3-040] `RTF实验入口`：没有CUDA明确blocked。
41. [S16-R3-041] `现有服务`：完整Python三轮。
42. [S16-R3-042] `现有服务`：Node三轮。
43. [S16-R3-043] `现有服务`：Go race count3。
44. [S16-R3-044] `现有服务`：完整Chromium三轮。
45. [S16-R3-045] `现有服务`：协议生命周期三轮。
46. [S16-R3-046] `现有服务`：真实Faster接口三轮。
47. [S16-R3-047] `现有服务`：HF导入tinyMimi三轮。
48. [S16-R3-048] `现有服务`：保留训练CPU等价门禁。
49. [S16-R3-049] `现有服务`：不忽略失败测试。
50. [S16-R3-050] `现有服务`：修复后完整重跑。
51. [S16-R3-051] `浏览器文案`：显示ICL条件不等于回放参考。
52. [S16-R3-052] `浏览器文案`：显示音色尚需试听。
53. [S16-R3-053] `浏览器文案`：显示RTF目标未达证据。
54. [S16-R3-054] `浏览器文案`：保留参考文本编辑。
55. [S16-R3-055] `浏览器文案`：提示转写必须匹配。
56. [S16-R3-056] `浏览器文案`：不新增假训练按钮。
57. [S16-R3-057] `浏览器文案`：不显示100相似度。
58. [S16-R3-058] `浏览器文案`：性能诊断不藏慢行。
59. [S16-R3-059] `浏览器文案`：手机无横向溢出。
60. [S16-R3-060] `浏览器文案`：锁定清空私有文本。
61. [S16-R3-061] `包与版本`：新step16独立文件。
62. [S16-R3-062] `包与版本`：原始至15冻结。
63. [S16-R3-063] `包与版本`：repack逐资产哈希。
64. [S16-R3-064] `包与版本`：内嵌新解码模块。
65. [S16-R3-065] `包与版本`：内嵌新RTF实验入口。
66. [S16-R3-066] `包与版本`：剪贴板全量读回。
67. [S16-R3-067] `包与版本`：下载逐字节核对。
68. [S16-R3-068] `包与版本`：权限拒绝可全选。
69. [S16-R3-069] `包与版本`：复制页固定新hash。
70. [S16-R3-070] `包与版本`：正式工作台不覆盖。
71. [S16-R3-071] `备忘录`：先计划后改产品。
72. [S16-R3-072] `备忘录`：问题19后给50建议。
73. [S16-R3-073] `备忘录`：问题20后给50建议。
74. [S16-R3-074] `备忘录`：问题21后给50建议。
75. [S16-R3-075] `备忘录`：累计问题建议保留。
76. [S16-R3-076] `备忘录`：最终交接完整内嵌。
77. [S16-R3-077] `备忘录`：原失败日志不覆盖。
78. [S16-R3-078] `备忘录`：状态用PARTIAL与BLOCKED。
79. [S16-R3-079] `备忘录`：缺硬件不得改成已达标。
80. [S16-R3-080] `备忘录`：不要求用户提供密钥。
81. [S16-R3-081] `真实声学`：多人参考不是调参可解决。
82. [S16-R3-082] `真实声学`：ICL能改善但非保证。
83. [S16-R3-083] `真实声学`：声纹分数不是听感真值。
84. [S16-R3-084] `真实声学`：模型仍可幻觉添字。
85. [S16-R3-085] `真实声学`：跨语言可能改变口音。
86. [S16-R3-086] `真实声学`：沙沙声需实际音频定位。
87. [S16-R3-087] `真实声学`：不从一张截图断定频谱。
88. [S16-R3-088] `真实声学`：静音延迟不算首声。
89. [S16-R3-089] `真实声学`：质量与速度一起验收。
90. [S16-R3-090] `真实声学`：人声自然度需独立试听。
91. [S16-R3-091] `后续门禁`：优先真实T4不同文本试听。
92. [S16-R3-092] `后续门禁`：逐GPU比较同参考。
93. [S16-R3-093] `后续门禁`：测试候选切换中取消。
94. [S16-R3-094] `后续门禁`：测RTF中位和最慢。
95. [S16-R3-095] `后续门禁`：参考泄漏单独核查。
96. [S16-R3-096] `后续门禁`：新进程重载检查。
97. [S16-R3-097] `后续门禁`：私有音频自行备份。
98. [S16-R3-098] `后续门禁`：历史网页训练闭环未完成。
99. [S16-R3-099] `后续门禁`：长样本全覆盖未完成。
100. [S16-R3-100] `后续门禁`：不把工程通过称全部目标完成。

---

## 内嵌备忘录：KAGGLE_STEP16_PLAN.md

# 第十六阶段计划（产品修改前）

## 目标及证据
用户报告克隆不像/偶尔两种声音/沙沙声，要求RTF≤0.3。当前没有用户输出音频、CUDA/T4或完整模型权重，不能确认声学根因或保证0.3已达标。15向量模式、路径键缓存、缺会话参考pin、流式末端重解码和+12dB增益是本轮需要验证/修复的风险。

已完成三轮专题研究各100建议；全源读取/哈希/Python AST只是巡检，非穷尽语义证明。问题19→20→21各50建议，先记方案再改产品。累计21题1050建议，三轮建议必须逐项处置，不能当300个bug。

## 推荐方案与小步骤
1. 冻结原始–15和正式3000工作台；新建step16，不覆盖历史。
2. 默认ICL匹配参考音频+转写，仅用作talker条件；新生成码专用decoder不接参考码或参考PCM。QTTS_CLONE_MODE=xvector仅显式选择，无转写ICL拒绝，不静默换声音。
3. 参考WAV+匹配文本+语言以长度前缀SHA256指纹绑定；Go会话固定pin，每段携带；worker取锁后复核当前档案和pin，不符在任何PCM前拒绝。替换同路径锚点时清除旧Faster路径缓存；预热与生成条件一致。
4. bounded codec窗口：左25帧、右2帧lookahead，chunk2–16；只提交未输出帧，24k/16码组/每帧1920样本不符拒绝。保留取消，末尾幂等flush。相比15引入约160ms音频前瞻，不承诺首声免费加快。
5. 每任务新leveler避免跨段/双卡历史状态影响；默认最大增益6dB，目标仍-18，QTTS_MAX_GAIN_DB显式0..12。无语音不flush前段尾。没有实际噪声样本，不默认强低通/谱门或声称噪声已清除。
6. 统一同会话生成seed，保留两卡各一模型、真实CUDA graph、FP16、原文分段/取消/长录音/手动校准/训练代码。采样参数先保持，不能把降温说成身份保证。
7. 新增目标机基准入口：仅显式调用已有真实worker，不加载第三模型；逐卡逐条至少三轮保存WAV与RTF(gen_wall/audio)；冷/热、RTF与首播分开。无CUDA必须blocked，0.3未达必须fail，声音质量始终需试听。
8. 三轮完整Python/Node/Go race/Chromium/协议、实际Faster接口fixture及tinyMimi依赖回归；最终完整包复制/下载读回、逐资产哈希、完整备忘录交接。

## 不作的虚假保证
不无依据增加C++/Java/SQL服务，不每卡放两模型，不改语速/删正文/减少数据充RTF，不播放参考片段补相似度，不把Mock或CPU吞吐当T4。真实相似度、单一音色、无沙沙与RTF0.3仍须目标设备三轮测量。历史网页真实训练闭环/长数据完整覆盖/严格声学拒播缺口仍保留；整体PARTIAL/BLOCKED直到有证据。

## 实施中证据驱动修订（保留原方案，未伪装成预先已知）
- 实际HF0.1.1.post1的Qwen12Hz codec是causal attention/causal卷积。真实23813参数tiny decoder随机权重CPU实验，8帧解码与追加到12帧的前缀最大差=0。因此默认前瞻改为0；`QTTS_CODEC_LOOKAHEAD_FRAMES=2`仅显式对照，不凭合成不稳定fixture默认增加160ms。保留通用lookahead回归，不声称真实沙沙根因是右边缘。
- 路径缓存失效之外，保存预计算ICL提示内存快照，合成传入voice_clone_prompt而不重新读取可覆盖的参考文件；dtype重载清空提示快照，后续档案必须重建。避免检查哈希后文件更改的TOCTOU风险。每段还绑定conditioning模式，混合模式先拒绝。
- 候选/文本更新如部分worker失败返回503+reference_saved=true，不宣称已就绪；activation比较两卡pin和模式并再次读当前参考版本。不回滚到另一声音。

---

## 内嵌备忘录：KAGGLE_STEP16_AUDIT.md

# 第十六阶段交付审计

## 状态

**本轮工程修复及最终三轮回归已通过；整体PARTIAL/BLOCKED，绝不声称真实相似度、无沙沙或T4 RTF0.3已经达到。** 最终状态以`validation/step16/final-checks.json`为准。完整目标22/300不因本轮变更自动升级。

最终完整包`kaggle/kaggle-fixed-step16.py`：306580B、52资产，SHA256 `c6ed6c89e6356fc6c7ab554f96a2c3201a8e4690c007ea66626445cc658b4429`。原始–15和正式工作台冻结。

## 实现及原因

1. `clone_stream.py/worker.py`：默认匹配转写ICL，参考文字不拼目标正文；参考声学码只进talker条件，codec仅接新生成码。显式xvector兼容选择，无文本ICL明确拒绝。不会声称ICL必然完全不产生参考音素或文字幻觉。
2. `voice_binding.py/session.go/scheduler.go`：参考WAV、UTF8转写及语言以长度前缀SHA256，Go/Python固定互操作样本；同会话pin/seed固定，每段携带pin与模式。Worker锁内重读档案/复核，版本或模式不符在lead/PCM前拒绝。先前已经播放的段不能撤回，不是整会话事务回滚。
3. 同路径参考变更时清除Faster旧路径键；预计算提示以档案内存快照保存，生成不再读取可覆盖的锚点路径。取prompt前后参考指纹一致才发布；dtype重载清空提示，后续按需重建。无匹配提示不自动回旧参考decoder。
4. 有界25帧左上下文，删除全历史码cat与比例裁参考；16码组/24k/1920样本每帧契约不合即拒绝，样本游标无重复/缺失，尾部幂等、取消不flush。默认前瞻0，实验可选0..2。
5. 最初方案右2帧前瞻被实际因果源码和真实tiny decoder前缀实验推翻：23813随机参数、8帧vs12帧前缀最大差0。故不默认付160ms代价，不把合成不稳定fixture当真实噪声证据。窗口重解码与完整解码在tiny随机参数下相同，不保证训练权重/多层大模型相同。
6. 每任务重置leveler/DC/包络，默认最大增益6dB（0..12显式可调），目标仍-18dBFS、保留软限幅；无生成语音不flush前段尾。降低底噪放大风险，并非真正频谱去噪已验证；很轻的输出可能比15最大12dB稍轻。
7. Analyst文本/候选更新的部分worker失败不再回`ok:true`；返回503并声明reference_saved。Go activation比较pin/模式且重读当前版本；失败保留原active ID，不把不同参考静默混用。
8. 训练adapter档案的sentence-buffered原生模式保持固定，不被gateway的Mock/faster测试标记覆盖；真正不支持训练的Worker仍会拒绝，不绕过adapter来源/权重校验。
9. 新`tools/voice_benchmark.py`明确--run后只调两真实驻留Faster workers，不加载第三模型；至少3轮、逐GPU/文本、无填充speech_samples分母、worker与HTTP wall RTF并列；WAV/JSONL私有保存，慢行保留，0.3未达失败。无硬件不算通过。

## 三轮审查与自问自答

三轮100条专题建议记录于REVIEW1/2/3，逐项处置见validation/step16/review-disposition.json。全源读取/AST/哈希不是穷尽语义无错，也不是300个bug或300项均已实施。问题19→20→21，各50开发建议后才进入下一题，累计21题1050建议；不向用户重复提问，也不声称已理解到100%可保证。

## 最终验证

- Python完整322×3=966项最终通过（37.320/39.911/43.420秒）；原子ready夹具修正后重跑。
- Node30×3=90、Go race count3、六协议脚本各内置3轮通过；完整Chromium121×3=363通过，最终step16完整复制额外3通过，独立复制页剪贴板/下载/拒绝回退/手机3通过；初始360通过/3旧版本文案失败日志保留。
- 实际Faster0.5.4 resolver/prepare与生产generated-only decoder，ICL/xvector、chunk2/4/8/12，CPU注入prompt/talker/kernel/codec：确认参考标记从未入decoder、80帧153600样本、同路径重载提示更新；不是完整模型。
- 实际HF Qwen12Hz tiny随机decoder23813参数：chunk2/4/8/12 ×lookahead0/2，40帧76800样本，固定1920契约/有界窗口/因果前缀；没有训练codec权重或人声音频。
- 保留完整Faster/Qwen导入与2651参数tinyMimi保存重载，CPU tinyLoRA相对冻结13损失/全部adapter张量逐位一致；不把它们称为Qwen训练质量。
- CPU runtime探针真实HF smoke/API签名通过，无CUDA整体仍blocked。真实T4基准本沙箱未运行，target-rtf-not-run.json明确零测量/blocked。

## 初始失败与修正，不隐去

- 初次301项包含旧15纯向量断言、旧stream方法夹具、未重打包、旧probe调用清单失败。保留python-initial/second/third日志，显式向量兼容测试仍在，新增ICL默认隔离测试，没有删除关键检查。
- 新preflight改查实际_prepare_generation/fast_generate_streaming后，旧fake Backend签名需要同步；修正mock声明而非绕过真实API检查。
- 原生adapter HTTP回归首次拒绝：gateway按Mock/faster推断模式而测试实际注入原生adapter。改以发布档案sentence-buffered类型绑定原生模式，加Go回归；A→B→A三轮/损坏adapter拒播重跑通过。初始adapter_gateway_initial.txt保留。
- tiny真实decoder库导入会向stdout打印flash-attn提示，首轮文件不是纯JSON；原文件保留actual-codec-initial-round*.txt，脚本把库输出引到stderr后最终三轮重新生成纯JSON。
- 两次Go命令cwd误用失败（无模块/相对venv路径）；实际竞态检查使用明确绝对Go工具路径与gateway cwd，非把路径错误算通过。

## 未达到/仍需现场验证

没有用户实际噪声音频、训练权重和T4/DeepSeek通路，不能确定报告的两种声音/沙沙全部根因，不能给相似度百分比、真实速度改善倍数或RTF0.3已达结论。ICL转写正确性、多人参考、生成模型幻觉、真实窗口接缝、声纹/自然度与双GPU段间一致性均需真实三轮听测。

没有新增无依据语言重写或每卡第二模型，没有更改语速/删文/加静音充RTF。原文早触发、录音/取消/安全、手动校准、HF/Mimi修复和训练代码保持。历史独立网页真实训练闭环、维护租约切换、长录音完整审核对齐/全样本覆盖、真实训练保质吞吐、严格声学逐字拒播缺口仍未完成。51份完整备忘录已统一内嵌到KAGGLE_HANDOFF_PROMPT.md。
- 最终并行负载下Python第二轮发现既有训练控制器测试夹具ready文件先创建再写PID，父进程读到了空串；这是测试发布竞态而非已证实的生产租约错误。仅改测试夹具临时文件原子rename，并在启动前记录旧run目录，保留python-ready-race-round2.txt后完整重跑三轮；不放宽PID/锁释放断言。
- 首次完整浏览器三轮360通过/3失败，全部为旧step15测试仍断言release-note必须“第十五阶段”；当前确为第十六阶段。只更新版本文案断言并补ICL/真实RTF待测文案检查，原手动校准/默认关闭断言保留；初始日志browser-initial-repeat3.txt保留，完整三轮重跑，不把初始失败算通过。

### 计时解释
`model_stages.prepare_ms/codec_ms/token_decode_ms`与DSP计时是主机观察/后端计数，不是严格CUDA profiler分解；prepare未额外同步，prefill没有独立汇总字段，几项不能简单相加当总GPU耗时。标准gen_ms与HTTP wall包含生成器必要同步、codec CPU取回和实际输出等待；真实RTF门禁使用总墙钟与未填充speech_samples，不用局部计时冒充0.3。

---

## 内嵌备忘录：KAGGLE_STEP16_QUICKSTART.md

# step16 升级与真实双T4验收

## 完整代码

- `kaggle/kaggle-fixed-step16.py`：306580字节，52个完整内嵌资产。
- SHA256：`c6ed6c89e6356fc6c7ab554f96a2c3201a8e4690c007ea66626445cc658b4429`。
- 独立3001复制预览可“复制全部代码”或下载；不改正式3000工作台，不运行Python。
- 原始及step1–15保留，不再把15纯向量模式作为相似度改善的既定答案。

## 升级顺序

1. 先备份需要保留的私有录音、库、档案和adapter；不要删除原录音或手工删除锁文件。
2. 完整停止/重启Kaggle会话，选择T4×2，Internet On。不要让旧15进程与16共用同一GPU/ROOT。
3. 在Code单元格粘贴**完整16代码**运行。默认真实Faster/FP16、每T4一个模型；不要用QTTS_MOCK取得声学结论。保留HF/Mimi正常导入修复，不卸载Kaggle Torch。
4. 可在完整代码之前显式设置：

```python
import os
os.environ['QTTS_CLONE_MODE'] = 'icl'
os.environ['QTTS_MAX_GAIN_DB'] = '6'
os.environ['QTTS_CODEC_LOOKAHEAD_FRAMES'] = '0'
# 紧接着粘贴完整step16，不是只执行这几行。
```

5. 等待双worker ready，再启用已有普通声音档案。**参考音频应只有一个说话人，参考文本必须逐字匹配该锚点**，不是想让它新说的目标文字。选项/档案编辑入口仍在。ICL无转写会明确拒绝，不静默改成另一种声音。
6. 有ASR错字先审核转写。切换候选/修改转写时停止当前会话，再重新启用。若提示reference_saved但worker未全部就绪，保存已发生，需重试启用；不会以旧声音冒充成功。旧会话pin不符会在该段任何PCM前拒绝，已播旧段不能撤回。
7. 首先直接朗读与参考不同的短目标文，再试长文、跨句与两卡交替；最后试DeepSeek第一句及时开始。没有声学逐字拒播器，ICL仍可能产生音素/文字幻觉，不保证无添字或百分百相似。

## 沙沙声的处理边界

- 解码器不接参考码/参考PCM；没有参考呼吸拼接或低延迟占位。
- 只拼未提交生成样本；窗口左25帧有界，默认右前瞻0。真实tiny随机decoder的因果前缀实验通过，故未默认增加160ms前瞻；仅显式实验可设2。
- 每任务重置响度包络，避免上段/双卡历史状态不同；输出目标仍-18dBFS，默认最大向上增益6dB，保留软限幅。需要更响可现场对照9，极限12；底噪也可能被放大，不建议盲开最大值。
- 没有用户实际沙沙样本，不能断定来源是模型、参考噪声、录音环境还是播放链；没有强低通/强谱门掩盖问题，也不声称“已无沙沙”。比较同参考、同文、同seed的独立生成WAV，不把响度变小误判为音质一定变好。

## 真正RTF≤0.3：目标机三轮实验

新工具只调用**已经驻留的两张真实GPU worker**，不启动第三模型。启动完成后可在同Notebook后续Code单元格运行；bootstrap会返回，supervisor在后台。先停止网页合成，确认空闲，填写界面实际档案ID（不是显示名称），输出目录每次用新名称：

```python
import subprocess, sys
subprocess.run([
    sys.executable, '/kaggle/working/qtts/tools/voice_benchmark.py',
    '--run', '--profile', '填写实际档案ID', '--rounds', '3', '--chunk-size', '8',
    '--output', '/kaggle/working/qtts/state/benchmarks/step16-run1/report.json',
], check=False)
```

ROOT或STATE自定义时用实际路径，并让工具继承相同QTTS环境。输出保留在私有state，不能自动上传或共享。

- 两worker必须ready/idle/model_loaded、Faster真实引擎、ICL-generated-only模式、GPU0/1分别独占可见；否则blocked。
- 先单独记录参考提示预热时间，再测3轮×2卡×3段=18条；保存18个生成WAV、逐条原始`measurements.jsonl`与report。后续失败不会删除先前慢行或WAV。
- 标准RTF=`gen_ms/1000/(speech_samples/24000)`，wall RTF包括HTTP/排队/必需等待。分母排除lead/tail/fade填充，失败/取消/anomaly不算成功。`rtf_x`是倒数，不是RTF。
- 任一条worker或wall RTF>0.3均`target-not-met`、退出2；全部满足也只是`measured-speed-only`，**不是音色/无噪声/自然度验收**。
- 不带`--run`时输出blocked、零测量，不会以CPU或Mock替代。这个沙箱当前没有真实T4结果，不能声称0.3已经做到。
- 对比chunk4/8/12请各用新的输出目录、相同参考/文本与seed，保留慢结果；只在试听合格前提下选更快配置。两卡吞吐不能相加冒充单卡RTF，不能改语速/删文/加静音。

## 真正声学验收仍必需

每张卡/每段分别核查：像参考单人、段间一致、自然易懂、无异常沙沙、没有播放参考内容、没有添字漏字；再检查first_played_ms与underruns。声纹余弦分数不能当“99.5%相似”；工程回归与tiny随机权重均不能替代训练权重试听。网页训练闭环、长数据全覆盖、真实双T4训练提速与严格声学拒播等历史缺口仍未完成。

---

## 内嵌备忘录：KAGGLE_STEP17_REVIEW1.md

# 第十七阶段第1轮专题研究：100条建议

本轮前50条针对新问题，后50条复核已成功链路。全源读取/哈希/Python AST不等于逐行语义无错。

1. [S17-R1-001] `截图与根因`：截图是15而非16不能当新包效果。
2. [S17-R1-002] `截图与根因`：录音限额与锚点限额分开。
3. [S17-R1-003] `截图与根因`：重现单个28.7秒ASR段。
4. [S17-R1-004] `截图与根因`：保留16的逐字匹配约束。
5. [S17-R1-005] `截图与根因`：不能将长音频硬截配全文。
6. [S17-R1-006] `截图与根因`：保留ASR词级时间戳。
7. [S17-R1-007] `截图与根因`：按完整词组而非字符比例切分。
8. [S17-R1-008] `截图与根因`：词与原段文本必须核对。
9. [S17-R1-009] `截图与根因`：缺词时间走音频窗口重新ASR。
10. [S17-R1-010] `截图与根因`：不能凭低RMS断定无人声。
11. [S17-R1-011] `词级对齐`：验证时间戳有限。
12. [S17-R1-012] `词级对齐`：验证起止单调。
13. [S17-R1-013] `词级对齐`：验证不越源音频。
14. [S17-R1-014] `词级对齐`：拒绝重叠倒序词。
15. [S17-R1-015] `词级对齐`：Unicode字母数字核对转写。
16. [S17-R1-016] `词级对齐`：不要丢标点后汉字。
17. [S17-R1-017] `词级对齐`：长单词超窗口重新ASR。
18. [S17-R1-018] `词级对齐`：短尾保留在分析收据。
19. [S17-R1-019] `词级对齐`：跨文件绝不合并文字。
20. [S17-R1-020] `词级对齐`：对齐失败有明确中文建议。
21. [S17-R1-021] `长音频重识别`：仅问题长段需要窗口ASR。
22. [S17-R1-022] `长音频重识别`：每窗口音频和转写独立匹配。
23. [S17-R1-023] `长音频重识别`：使用原音频实际切片。
24. [S17-R1-024] `长音频重识别`：偏移恢复绝对时间。
25. [S17-R1-025] `长音频重识别`：边界优先静音。
26. [S17-R1-026] `长音频重识别`：窗口必须前进不死循环。
27. [S17-R1-027] `长音频重识别`：最末窗口不丢。
28. [S17-R1-028] `长音频重识别`：无语音窗口不伪造文字。
29. [S17-R1-029] `长音频重识别`：沿用ASR锁及CPU复用。
30. [S17-R1-030] `长音频重识别`：进度显示窗口计数。
31. [S17-R1-031] `长参考语义`：长录音可以超过15秒。
32. [S17-R1-032] `长参考语义`：不能无限把20分钟塞进ICL。
33. [S17-R1-033] `长参考语义`：提供16与24秒参考窗口。
34. [S17-R1-034] `长参考语义`：默认16保护旧短样本。
35. [S17-R1-035] `长参考语义`：24明确标为实验与较慢。
36. [S17-R1-036] `长参考语义`：手工转写仅单短文件直接采用。
37. [S17-R1-037] `长参考语义`：长手工全文不能按时长分配。
38. [S17-R1-038] `长参考语义`：记录源总时长与选中锚点。
39. [S17-R1-039] `长参考语义`：记录重切分和重识别数量。
40. [S17-R1-040] `长参考语义`：明确建档不是全数据训练。
41. [S17-R1-041] `输入与安全`：窗口值只允许16或24。
42. [S17-R1-042] `输入与安全`：表单和库入口都独立校验。
43. [S17-R1-043] `输入与安全`：失败保留本地录音。
44. [S17-R1-044] `输入与安全`：取消不得删除源音频。
45. [S17-R1-045] `输入与安全`：不自动云传原音。
46. [S17-R1-046] `输入与安全`：拒绝非有限PCM。
47. [S17-R1-047] `输入与安全`：保留20分钟录音预算。
48. [S17-R1-048] `输入与安全`：低电平提示调整设备。
49. [S17-R1-049] `输入与安全`：提示麦克风距离不替人猜设备。
50. [S17-R1-050] `输入与安全`：保留原始至16冻结。
51. [S17-R1-051] `档案变更`：修正候选更换原路径复用。
52. [S17-R1-052] `档案变更`：文本更改触发提示失效。
53. [S17-R1-053] `档案变更`：手动校准选择不能覆盖回旧。
54. [S17-R1-054] `档案变更`：完成后保存阶段收据。
55. [S17-R1-055] `档案变更`：删除档案不能被旧请求静默复活。
56. [S17-R1-056] `档案变更`：不删除冻结15。
57. [S17-R1-057] `档案变更`：旧档案可重新加载。
58. [S17-R1-058] `档案变更`：参考需审核逐字转写。
59. [S17-R1-059] `档案变更`：ASR提案不是人工真值。
60. [S17-R1-060] `档案变更`：不从短片猜长文。
61. [S17-R1-061] `安全读取`：锚点仅单一安全文件名。
62. [S17-R1-062] `安全读取`：拒绝符号链接。
63. [S17-R1-063] `安全读取`：拒绝目录冒音频。
64. [S17-R1-064] `安全读取`：限制参考读取字节。
65. [S17-R1-065] `安全读取`：路径始终在档案目录。
66. [S17-R1-066] `安全读取`：哈希不输出原音频。
67. [S17-R1-067] `安全读取`：指纹不是授权证明。
68. [S17-R1-068] `安全读取`：不泄漏访问口令。
69. [S17-R1-069] `安全读取`：不自动云传录音。
70. [S17-R1-070] `安全读取`：保持私有备份边界。
71. [S17-R1-071] `原生adapter`：保留训练候选固定binding。
72. [S17-R1-072] `原生adapter`：不向faster注入adapter。
73. [S17-R1-073] `原生adapter`：不修改训练权重。
74. [S17-R1-074] `原生adapter`：缺adapter不回退Base。
75. [S17-R1-075] `原生adapter`：保留句级缓冲标记。
76. [S17-R1-076] `原生adapter`：继续核对Base哈希。
77. [S17-R1-077] `原生adapter`：旧训练功能做回归。
78. [S17-R1-078] `原生adapter`：不要把参考处理叫训练。
79. [S17-R1-079] `原生adapter`：网页真实训练缺口保留。
80. [S17-R1-080] `原生adapter`：真实训练质量仍待验收。
81. [S17-R1-081] `相似度验收`：相似度用真实说话人模型。
82. [S17-R1-082] `相似度验收`：不能伪造99.5百分比。
83. [S17-R1-083] `相似度验收`：文字一致不代表音色一致。
84. [S17-R1-084] `相似度验收`：多段输出分别试听。
85. [S17-R1-085] `相似度验收`：比较两卡相邻段。
86. [S17-R1-086] `相似度验收`：使用与参考不同的目标文字。
87. [S17-R1-087] `相似度验收`：同参考同文同seed对照。
88. [S17-R1-088] `相似度验收`：保留参考与输出独立文件。
89. [S17-R1-089] `相似度验收`：无用户音频不猜根因。
90. [S17-R1-090] `相似度验收`：不承诺100无错。
91. [S17-R1-091] `保护已有功能`：保留原文分段。
92. [S17-R1-092] `保护已有功能`：保留首句及时调度。
93. [S17-R1-093] `保护已有功能`：保留两主视图。
94. [S17-R1-094] `保护已有功能`：保留长录音预算。
95. [S17-R1-095] `保护已有功能`：保留命名空库。
96. [S17-R1-096] `保护已有功能`：保留失败本地片段。
97. [S17-R1-097] `保护已有功能`：保留手动候选校准。
98. [S17-R1-098] `保护已有功能`：保留DeepSeek取消。
99. [S17-R1-099] `保护已有功能`：保留3000正式工作台。
100. [S17-R1-100] `保护已有功能`：保留原始至15整包。

---

## 内嵌备忘录：KAGGLE_STEP17_REVIEW2.md

# 第十七阶段第2轮专题研究：100条建议

本轮前50条针对新问题，后50条复核已成功链路。全源读取/哈希/Python AST不等于逐行语义无错。

1. [S17-R2-001] `短参考与音色`：继续使用ICL匹配文本。
2. [S17-R2-002] `短参考与音色`：不退回15纯向量默认。
3. [S17-R2-003] `短参考与音色`：新旧GPU不能混版本。
4. [S17-R2-004] `短参考与音色`：相同参考绑定采样参数。
5. [S17-R2-005] `短参考与音色`：Go和Python浮点编码一致。
6. [S17-R2-006] `短参考与音色`：缺省参数也计入指纹。
7. [S17-R2-007] `短参考与音色`：不接受NaN温度。
8. [S17-R2-008] `短参考与音色`：改温度使旧会话失效。
9. [S17-R2-009] `短参考与音色`：参数相同不是音色绝对相同。
10. [S17-R2-010] `短参考与音色`：真人试听仍是独立门禁。
11. [S17-R2-011] `多卡参数`：绑定temperature。
12. [S17-R2-012] `多卡参数`：绑定top_k。
13. [S17-R2-013] `多卡参数`：绑定top_p。
14. [S17-R2-014] `多卡参数`：绑定repetition_penalty。
15. [S17-R2-015] `多卡参数`：top_k必须整数。
16. [S17-R2-016] `多卡参数`：统一默认参数数值。
17. [S17-R2-017] `多卡参数`：每次合成锁内复核。
18. [S17-R2-018] `多卡参数`：预计算提示快照保留。
19. [S17-R2-019] `多卡参数`：不混用不同条件模式。
20. [S17-R2-020] `多卡参数`：不声称两卡波形逐位相同。
21. [S17-R2-021] `参考质量`：记录原始RMS。
22. [S17-R2-022] `参考质量`：记录原始峰值。
23. [S17-R2-023] `参考质量`：记录SNR估计而非真值。
24. [S17-R2-024] `参考质量`：低电平给风险提示不直接拒绝。
25. [S17-R2-025] `参考质量`：响度归一化不是降噪。
26. [S17-R2-026] `参考质量`：MFCC相似不是可靠声纹真值。
27. [S17-R2-027] `参考质量`：避免强降噪损伤辅音。
28. [S17-R2-028] `参考质量`：参考多人必须审核。
29. [S17-R2-029] `参考质量`：24秒未必比10秒好。
30. [S17-R2-030] `参考质量`：不播放原录音补相似度。
31. [S17-R2-031] `连续朗读`：只调整朗读聚合不延后聊天首句。
32. [S17-R2-032] `连续朗读`：减少过多独立合成语段。
33. [S17-R2-033] `连续朗读`：优先完整句子标点。
34. [S17-R2-034] `连续朗读`：保留原始全文字符。
35. [S17-R2-035] `连续朗读`：不合并不同用户任务。
36. [S17-R2-036] `连续朗读`：保留取消和背压。
37. [S17-R2-037] `连续朗读`：不跨词叠加PCM。
38. [S17-R2-038] `连续朗读`：不删除语音以隐藏接缝。
39. [S17-R2-039] `连续朗读`：保留已有codec有界上下文。
40. [S17-R2-040] `连续朗读`：自然韵律不能仅靠交叉淡化保证。
41. [S17-R2-041] `噪声边界`：继续禁参考呼吸拼接。
42. [S17-R2-042] `噪声边界`：不生成白噪声补停顿。
43. [S17-R2-043] `噪声边界`：保留软限幅。
44. [S17-R2-044] `噪声边界`：保留可控增益。
45. [S17-R2-045] `噪声边界`：不把静音当去噪成功。
46. [S17-R2-046] `噪声边界`：不默认低通抹齿音。
47. [S17-R2-047] `噪声边界`：新统计不得泄漏原文本。
48. [S17-R2-048] `噪声边界`：生成WAV可供独立试听。
49. [S17-R2-049] `噪声边界`：缺真实音频不宣布零噪声。
50. [S17-R2-050] `噪声边界`：不得缩短输出冒RTF达标。
51. [S17-R2-051] `RTF定义`：标准RTF等于生成墙钟除语音秒数。
52. [S17-R2-052] `RTF定义`：rtf_x是其倒数不是RTF。
53. [S17-R2-053] `RTF定义`：不把双卡速度相加冒单卡RTF。
54. [S17-R2-054] `RTF定义`：排除零停顿分母。
55. [S17-R2-055] `RTF定义`：失败取消样本不能算通过。
56. [S17-R2-056] `RTF定义`：冷预热与热态分开。
57. [S17-R2-057] `RTF定义`：首播与吞吐分开。
58. [S17-R2-058] `RTF定义`：记录每GPU结果。
59. [S17-R2-059] `RTF定义`：目标0.3需每条和汇总检查。
60. [S17-R2-060] `RTF定义`：无T4输出blocked。
61. [S17-R2-061] `计时拆分`：模型prepare单独计时。
62. [S17-R2-062] `计时拆分`：token生成单独计时。
63. [S17-R2-063] `计时拆分`：codec解码单独计时。
64. [S17-R2-064] `计时拆分`：DSP耗时单列。
65. [S17-R2-065] `计时拆分`：总墙钟包括必要同步。
66. [S17-R2-066] `计时拆分`：不拿CPU异步发射当CUDA完成。
67. [S17-R2-067] `计时拆分`：预热不计入热态却单独报告。
68. [S17-R2-068] `计时拆分`：报告first_played与欠载。
69. [S17-R2-069] `计时拆分`：保存原始测量行。
70. [S17-R2-070] `计时拆分`：不删慢样本。
71. [S17-R2-071] `性能选择`：仍用CUDA graph后端。
72. [S17-R2-072] `性能选择`：不盲开torch.compile。
73. [S17-R2-073] `性能选择`：T4继续FP16。
74. [S17-R2-074] `性能选择`：不假称T4原生BF16。
75. [S17-R2-075] `性能选择`：不为语言数量加网络跳转。
76. [S17-R2-076] `性能选择`：不每卡塞两副本。
77. [S17-R2-077] `性能选择`：上下文有界减少复制。
78. [S17-R2-078] `性能选择`：参考prompt按版本复用。
79. [S17-R2-079] `性能选择`：较大后段chunk做可选实测。
80. [S17-R2-080] `性能选择`：质量不降需要真实对照。
81. [S17-R2-081] `实验设计`：同一参考与目标文。
82. [S17-R2-082] `实验设计`：至少三轮独立进程接口实验。
83. [S17-R2-083] `实验设计`：每个chunk2/4/8/12检查。
84. [S17-R2-084] `实验设计`：检查短尾与取消。
85. [S17-R2-085] `实验设计`：参考码标记不能入decoder。
86. [S17-R2-086] `实验设计`：生成总帧对应总样本。
87. [S17-R2-087] `实验设计`：检查窗口峰值上限。
88. [S17-R2-088] `实验设计`：性能fixture不算Qwen性能。
89. [S17-R2-089] `实验设计`：CPU tinyMimi不算完整TTS。
90. [S17-R2-090] `实验设计`：硬件结果不能编造。
91. [S17-R2-091] `降级与边界`：新解码模式不自动回旧混参考路径。
92. [S17-R2-092] `降级与边界`：ICL缺文本给明确提示。
93. [S17-R2-093] `降级与边界`：不要静默改为别的声音。
94. [S17-R2-094] `降级与边界`：不要自动降模型大小。
95. [S17-R2-095] `降级与边界`：不改语速充RTF。
96. [S17-R2-096] `降级与边界`：不删用户正文充速度。
97. [S17-R2-097] `降级与边界`：不缩减训练数据。
98. [S17-R2-098] `降级与边界`：保留故障监督。
99. [S17-R2-099] `降级与边界`：记下每次初始失败。
100. [S17-R2-100] `降级与边界`：整体仍按证据判定。

---

## 内嵌备忘录：KAGGLE_STEP17_REVIEW3.md

# 第十七阶段第3轮专题研究：100条建议

本轮前50条针对新问题，后50条复核已成功链路。全源读取/哈希/Python AST不等于逐行语义无错。

1. [S17-R3-001] `重现门禁`：单个28.7秒词级段建档成功。
2. [S17-R3-002] `重现门禁`：单个60秒段词级切分。
3. [S17-R3-003] `重现门禁`：20分钟时间戳规划有界。
4. [S17-R3-004] `重现门禁`：缺词时间戳实际窗口重识别。
5. [S17-R3-005] `重现门禁`：文本不匹配必须回识别。
6. [S17-R3-006] `重现门禁`：长manual全文不错误拼接。
7. [S17-R3-007] `重现门禁`：短manual16秒保持兼容。
8. [S17-R3-008] `重现门禁`：24秒锚点不越界。
9. [S17-R3-009] `重现门禁`：无声和非法时间戳不造成功。
10. [S17-R3-010] `重现门禁`：每项做三轮回归。
11. [S17-R3-011] `接口门禁`：浏览器发送参考窗口字段。
12. [S17-R3-012] `接口门禁`：默认值16可见。
13. [S17-R3-013] `接口门禁`：24选项真实进入后端。
14. [S17-R3-014] `接口门禁`：锁定清除私有转写。
15. [S17-R3-015] `接口门禁`：表单非法值拒绝。
16. [S17-R3-016] `接口门禁`：库处理同样校验。
17. [S17-R3-017] `接口门禁`：服务重启新包版本可识别。
18. [S17-R3-018] `接口门禁`：新包逐字节复制。
19. [S17-R3-019] `接口门禁`：16包哈希冻结。
20. [S17-R3-020] `接口门禁`：正式工作台保持不变。
21. [S17-R3-021] `参数指纹测试`：中英转写跨语言一致。
22. [S17-R3-022] `参数指纹测试`：默认值与显式默认相同。
23. [S17-R3-023] `参数指纹测试`：四参数分别变更使pin变化。
24. [S17-R3-024] `参数指纹测试`：NaN和无穷拒绝。
25. [S17-R3-025] `参数指纹测试`：非整数top_k拒绝。
26. [S17-R3-026] `参数指纹测试`：Worker不输出不符pin的PCM。
27. [S17-R3-027] `参数指纹测试`：Go协议携带固定pin。
28. [S17-R3-028] `参数指纹测试`：不改adapter来源绑定。
29. [S17-R3-029] `参数指纹测试`：新旧包混跑明确重启。
30. [S17-R3-030] `参数指纹测试`：不把指纹当身份认证。
31. [S17-R3-031] `验证与实验`：Python完整三轮。
32. [S17-R3-032] `验证与实验`：Node完整三轮。
33. [S17-R3-033] `验证与实验`：Go race三轮。
34. [S17-R3-034] `验证与实验`：Chromium完整三轮。
35. [S17-R3-035] `验证与实验`：六服务协议各三轮。
36. [S17-R3-036] `验证与实验`：实际Faster控制接口三轮。
37. [S17-R3-037] `验证与实验`：真实tiny codec三轮。
38. [S17-R3-038] `验证与实验`：Mimi导入重载三轮。
39. [S17-R3-039] `验证与实验`：CPU训练等价三轮。
40. [S17-R3-040] `验证与实验`：所有CPU模型明确不是Qwen音质证据。
41. [S17-R3-041] `记录与交付`：问题22回答后给50建议。
42. [S17-R3-042] `记录与交付`：问题23回答后给50建议。
43. [S17-R3-043] `记录与交付`：问题24回答后给50建议。
44. [S17-R3-044] `记录与交付`：方案先于产品修改。
45. [S17-R3-045] `记录与交付`：每次失败日志保留。
46. [S17-R3-046] `记录与交付`：逐条300建议分类。
47. [S17-R3-047] `记录与交付`：无硬件保留BLOCKED。
48. [S17-R3-048] `记录与交付`：真实RTF0.3仍需测量。
49. [S17-R3-049] `记录与交付`：完整57份备忘录内嵌。
50. [S17-R3-050] `记录与交付`：不承诺100相似零噪声。
51. [S17-R3-051] `浏览器文案`：显示ICL条件不等于回放参考。
52. [S17-R3-052] `浏览器文案`：显示音色尚需试听。
53. [S17-R3-053] `浏览器文案`：显示RTF目标未达证据。
54. [S17-R3-054] `浏览器文案`：保留参考文本编辑。
55. [S17-R3-055] `浏览器文案`：提示转写必须匹配。
56. [S17-R3-056] `浏览器文案`：不新增假训练按钮。
57. [S17-R3-057] `浏览器文案`：不显示100相似度。
58. [S17-R3-058] `浏览器文案`：性能诊断不藏慢行。
59. [S17-R3-059] `浏览器文案`：手机无横向溢出。
60. [S17-R3-060] `浏览器文案`：锁定清空私有文本。
61. [S17-R3-061] `包与版本`：新step16独立文件。
62. [S17-R3-062] `包与版本`：原始至15冻结。
63. [S17-R3-063] `包与版本`：repack逐资产哈希。
64. [S17-R3-064] `包与版本`：内嵌新解码模块。
65. [S17-R3-065] `包与版本`：内嵌新RTF实验入口。
66. [S17-R3-066] `包与版本`：剪贴板全量读回。
67. [S17-R3-067] `包与版本`：下载逐字节核对。
68. [S17-R3-068] `包与版本`：权限拒绝可全选。
69. [S17-R3-069] `包与版本`：复制页固定新hash。
70. [S17-R3-070] `包与版本`：正式工作台不覆盖。
71. [S17-R3-071] `备忘录`：先计划后改产品。
72. [S17-R3-072] `备忘录`：问题19后给50建议。
73. [S17-R3-073] `备忘录`：问题20后给50建议。
74. [S17-R3-074] `备忘录`：问题21后给50建议。
75. [S17-R3-075] `备忘录`：累计问题建议保留。
76. [S17-R3-076] `备忘录`：最终交接完整内嵌。
77. [S17-R3-077] `备忘录`：原失败日志不覆盖。
78. [S17-R3-078] `备忘录`：状态用PARTIAL与BLOCKED。
79. [S17-R3-079] `备忘录`：缺硬件不得改成已达标。
80. [S17-R3-080] `备忘录`：不要求用户提供密钥。
81. [S17-R3-081] `真实声学`：多人参考不是调参可解决。
82. [S17-R3-082] `真实声学`：ICL能改善但非保证。
83. [S17-R3-083] `真实声学`：声纹分数不是听感真值。
84. [S17-R3-084] `真实声学`：模型仍可幻觉添字。
85. [S17-R3-085] `真实声学`：跨语言可能改变口音。
86. [S17-R3-086] `真实声学`：沙沙声需实际音频定位。
87. [S17-R3-087] `真实声学`：不从一张截图断定频谱。
88. [S17-R3-088] `真实声学`：静音延迟不算首声。
89. [S17-R3-089] `真实声学`：质量与速度一起验收。
90. [S17-R3-090] `真实声学`：人声自然度需独立试听。
91. [S17-R3-091] `后续门禁`：优先真实T4不同文本试听。
92. [S17-R3-092] `后续门禁`：逐GPU比较同参考。
93. [S17-R3-093] `后续门禁`：测试候选切换中取消。
94. [S17-R3-094] `后续门禁`：测RTF中位和最慢。
95. [S17-R3-095] `后续门禁`：参考泄漏单独核查。
96. [S17-R3-096] `后续门禁`：新进程重载检查。
97. [S17-R3-097] `后续门禁`：私有音频自行备份。
98. [S17-R3-098] `后续门禁`：历史网页训练闭环未完成。
99. [S17-R3-099] `后续门禁`：长样本全覆盖未完成。
100. [S17-R3-100] `后续门禁`：不把工程通过称全部目标完成。

---

## 内嵌备忘录：KAGGLE_STEP17_PLAN.md

# 第十七阶段具体方案（产品修改前）

## 已查明与未知
截图为15，28.7秒录音/RMS约-46.6dBFS/峰0.014，实际报错发生在候选选择，不是录音上传上限。16源码仍忽略ASR已有词级时间戳；单个超过16秒的ASR段无法成为候选。这是可复现的代码缺陷。未收到实际WAV、没有CUDA/训练权重，不能确定沙沙和音色的全部声学根因。

三轮全源读取/AST/哈希及专题审查各100建议已记录；不是穷尽无错证明。问题22→23→24各50建议，累计24题1200建议，记录具体选项/推荐/边界。不询问用户，不承诺100%信心。

## 实施顺序
1. 冻结原始–16和正式工作台，新建17；先复现28.7秒单ASR段失败。
2. 新reference_segments模块：完整保存词级时间，验证词文一致、有限/单调/边界，按完整词切分长段。缺失/不可信的长段对实际音频窗口重新ASR，恢复绝对时间，优先静音边界；不按字数/时长比例分配全文。进度及数量收据；保留ASR全周期锁。
3. 快速建档与库处理均支持16（默认）/24秒（较长参考实验）窗口。长录音仍完整分析并择优，不把20分钟全塞进ICL；单个短文件手工转写直用保持，长manual全文明确自动时间戳转写而非强制对齐。记录源时长、锚点时长、切分/重识别统计。
4. 低输入电平记录RMS/峰值及风险提示，不以小波形认定无声，不强加损音质滤波。保持16 ICL/生成码专用codec/提示快照/禁参考PCM拼接；建档不是训练，更长不保证更像。
5. 参考指纹升级v2，同时绑定四项有效生成参数。Python/Go采用IEEE754小端double规范字节，默认与显式默认一致，拒绝非法/非有限参数。改参数使旧会话失效，避免两卡不同缓存参数；不是声学身份/逐位波形保证。
6. 只朗读模式适度增大自然标点聚合，减少独立合成重启；保留完整正文、取消/背压/顺序和DeepSeek首句早触发。不要跨词叠加PCM或删字掩盖接缝；真实自然度仍须试听。
7. 三轮完整Python/Node/Go race/Chromium/六协议及实际Faster接口、tiny codec/Mimi、CPU训练等价；新增28.7/60/1200秒对齐、缺词重识别、16/24、指纹参数/非法值测试。CPU/Mock不当Qwen声学证明。
8. 更新17完整复制页、全资产校验、下载/剪贴板/手机/权限回退。57份备忘录完整内嵌最终提示词，错误日志与未完成项保留。

## 验收边界
超长采集/对齐修复可工程验证；实际短/长参考相似度、零沙沙、双卡音色完全一致、自然整段韵律和先前RTF≤0.3均需真实双T4与音频。保留硬件BLOCKED，不用合成信号宣布这些目标完成。不无依据新增C++/Java/SQL服务；现有Python/PyTorch/CUDA、Go、Rust、JS分工保持。

## 完成记录（工程范围）

上述8步已落实，原始–16及正式15文件保留。最终Python334×3、Node30×3、Go race3、六协议各三轮、Chromium123×3及完整复制另3通过。冻结16与17相同29秒fixture对照、实际Faster接口/随机tiny codec/完整导入tinyMimi/CPU训练逐位等价各三轮通过。最终全资产逐字节、固定hash复制/下载、57份备忘录、24题各50及冻结文件核对见`validation/step17/final-checks.json`。

工程计划完成不等于所有用户目标完成：没有真实用户录音/完整语音权重/T4证据，仍不签收相似度、零噪声、同卡/跨卡音色、自然完整朗读或RTF≤0.3。历史训练闭环/长数据覆盖/实际吞吐/声学逐字拒播缺口未解决；总体PARTIAL/BLOCKED、目标22/300不变。

---

## 内嵌备忘录：KAGGLE_STEP17_AUDIT.md

# 第十七阶段审计

## 状态与产物

工程修复及最终三轮回归通过；整体**PARTIAL/BLOCKED**。不得称高相似、零噪声、双卡声学完全一致、完整朗读自然度或真实RTF≤0.3已验收。最终收据以validation/step17/final-checks.json为准。

完整包`kaggle/kaggle-fixed-step17.py`，313504B、53资产，SHA256 `6eacaede14f9b5f42ac5c334df5c3f9d1a1c6858fb69b7d3a8ff241ec60427ea`。原始–16与正式工作台冻结。

## 源码确认的缺陷及修复

- 截图是15；现场28.7秒、RMS约-46.6dBFS/peak0.014。上传限额不是15秒；失败处是旧候选仅接受完整2.5–16秒ASR段，忽略words。不能据截图认定无语音或设备故障。
- `reference_segments.py`验证有限/单调/源范围/词文一致，用完整词组切长段；不可信长词时间对实际窗口重ASR，恢复绝对偏移，低能边界优先，短尾留收据，不按字数/时长分全文。短段可保留段级ASR但丢无效可选word元数据，避免后续停顿分析崩溃。ASR依旧不是人工真值。
- `analyst.py/library_api.py/web`都支持16默认/24实验窗口；长manual全文不强配短音频。候选补边不得超窗口，质量记录源总时长、候选时长、切分/重识别计数和非训练声明。默认短manual16秒不回归。
- 原始非有限PCM拒绝；记录归一化前RMS/peak。低于-40dBFS仅给输入距离/增益风险提示，不直接判无声；提示进入现有处理决策显示。没有强滤波损伤辅音或播放参考原音。
- `voice_binding.py/session.go`升级v2：音频/转写/语言加四有效生成参数，规范小端IEEE754 doubles，显式默认与缺省相同，拒绝非法/NaN/Inf/非整数top_k。Worker原有锁内复核/提示快照/模式pin保持；旧会话及混版本须重启。相同条件不保证跨GPU数值或音色完全相同。
- `ReadSegCfg`只朗读增大聚合，FirstMin12/FirstMax24/Min20/Target40/Max80；正文保持、聊天Live首句不变。减少独立重启不是跨段联合建模；可能更慢或降低并行，真实自然度仍待试听。不跨词交叉淡化、不删文。

## 新验证及实验设计

- 最终Python334项×3=1002通过；新增12项覆盖28.7/60/1200秒、缺词重识别实际样本、非法词时间、16/24手工匹配、低输入提示、表单非法值、生成参数pin。
- `long_reference_check.py`从冻结16提取真实build_profile同控制流，对同一29秒合成PCM、28.7秒ASR词段：16复现no aligned，17建档成功并实际读回候选WAV帧数/采样率；缺词实际窗口样本总数完整。ASR/说话人是显式fixture，不是实际Whisper或语音质量。
- 实际Faster resolver/prepare/生成码decoder、真实tiny随机codec、完整Qwen/Mimi导入重载、CPU LoRA对13损失/adapter逐位等价均三轮回归；完整训练权重、GPU、真实人声未执行。
- Node30×3=90、Go race3、六服务协议各三轮、完整Chromium123×3=369、最终整包复制另3、copy页/下载/拒绝回退/手机3均通过。独立3001不改正式3000。

## 初始失败与纠错，保留日志

1. 初次322检查4失败：旧测试to16k替身用24k除2得到12k，新增时长校验正确拒绝伪16k。将测试替身改真实2/3样本比；没有放宽生产时间边界。旧v1固定哈希更新为v2跨语言样本。
2. 旧“长段一律拒绝”断言改为“无可信窗口时间不配全文”；新增旧16失败/17成功对照，不删除拒绝错误对齐的测试。
3. 首次向studio测试写文件的临时编辑脚本误对字符串调用write_text，未写入该文件；后续已正确追加17完整包测试。不是浏览器或产品成功证据。
4. 长参考对照脚本初次stdout混入预期基线失败日志，文件保留long-reference-initial-round*.txt；脚本将库日志导向stderr，三轮重新生成纯JSON。基线错误是预期复现，不是17失败被藏。
5. 低输入提示最初只在API质量字段，最终也合并到已有decision显示，并新增实测合成低电平回归；最终334项重新跑三轮，保留之前333项日志。

## 审查、备忘录与边界

三轮100条见REVIEW1/2/3；全源读取/AST/哈希不等于穷尽语义无错。问题22–24各50建议，累计24题1200建议；处置逐条见review-disposition.json，不将300建议当300bug或全部新功能。最终提示词完整内嵌57份备忘录。

没有用户WAV、Whisper/Qwen训练权重和真实T4，不能保证所有合法录音一定被正确转写，也不能验证声纹/沙沙/自然接缝。长参考可增加重复/噪声和prefill，24实验不能叫质量必提升。参考PCM绝不播放；15向量模式不恢复为默认。先前真实RTF0.3、训练闭环、长数据全覆盖、真实双卡训练吞吐、声学逐字拒播缺口不豁免；完整目标22/300不升级。多语言按实际热路径用，不无证据重写稳定模块。

---

## 内嵌备忘录：KAGGLE_STEP17_QUICKSTART.md

# step17：长录音建档、较长参考与双卡一致性

## 完整代码与升级

`kaggle/kaggle-fixed-step17.py`：313504字节、53个完整内嵌资产。
SHA256：`6eacaede14f9b5f42ac5c334df5c3f9d1a1c6858fb69b7d3a8ff241ec60427ea`。
独立3001预览支持复制全部/下载，不改正式3000工作台。原始–16包均冻结。

**截图标题明确是第十五阶段，不是17。只刷新旧页面不会更新服务端。** 先备份私有录音/档案/adapter，完整停止并重启Kaggle会话，T4×2/Internet On，将完整17粘到Code单元格运行。不要让15/16/17进程混用同一GPU或ROOT；不要删除锁文件或卸载Kaggle Torch。网页应显示“第十七阶段”。指纹已升级v2，旧会话必须停止后重启。

## 超过15秒的现场录音

1. 录音采集/上传上限仍是默认单段1200秒、累计1800秒；不是16秒上限。失败时本地录音保留。
2. 停止采集后打开“选项”。默认模型参考窗口16秒；需要比较较长上下文时选24秒实验选项，再点创建。声音库处理也有16/24秒选择。
3. 17会先使用实际ASR词级时间戳拆长段；词与段文字不一致或缺时间时，对实际音频窗口重新识别，不按字数/时长比例猜转写。长段不再仅因超过16秒就被直接拒绝。
4. 提供手工文本时，单个文件时长≤所选窗口可直接采用，应逐字匹配录音。超过窗口的长全文不会被强行分配给短片段，改用ASR时间戳并留下收据。ASR不是人工真值，仍应审核选中锚点转写。
5. 进度会显示重识别窗口；实际ASR重试可能更慢。若输入无声、重识别仍无有效语音或时间戳不可信，会明确失败而不伪造“成功”。

### 长录音不等于更长模型提示，更不等于训练

长录音用于完整分析、选代表性片段；模型实际用选中的锚点，窗口上限16/24秒，不能把20分钟直接塞进ICL。`quality.reference_context`记录源时长、候选实际时长和`model_trained=false`，`quality.asr[].alignment`记录词切分/重识别窗口。20分钟规划测试不代表已用真实20分钟语音或Whisper权重做质量验收。更长参考可能更慢或增加不必要韵律，不保证比干净10秒更像。

## 短参考不像／沙沙声

- 继续采用16已恢复的匹配转写ICL，codec仅解码新生成码；没有参考PCM/呼吸片段拼接，也没有播放原音充相似度。
- 首先审核实际锚点只有一个人、没有音乐/背景人声、没有削波，转写与该片段逐字对应；录音长不是这几项的替代。
- 截图RMS约-46.6dBFS、峰0.014仅说明输入很轻，不能证明无人声或确定设备原因。17记录原始RMS/峰值，对很轻输入在现有处理决策里提示检查距离和输入增益。归一化也会放大底噪，不是去噪。
- 保留目标-18dBFS、最大增益默认6dB（QTTS_MAX_GAIN_DB可0..12）、软限幅。没有默认强低通/跨词重叠；不把齿音、气声抹掉冒充降噪。
- 没有用户实际WAV和真实权重试听证据，不能声称已经“零噪声”或100%相似；训练模型仍可能幻觉添字。

## 双卡与衔接

参考指纹v2包含音频、转写、语言和有效temperature/top_k/top_p/repetition_penalty；Go/Python使用相同小端IEEE754字节。默认与显式默认一致，参数改变使旧会话失败重启；同会话模式/seed固定、预计算提示快照保留，不能静默混用旧参数。但相同参数和seed不保证不同GPU浮点波形逐位相同，也不保证听感完全一致。

朗读模式适度扩大自然标点聚合（Target40/Max80单位），减少独立合成重启；文字不删改。聊天仍保持第一句及时提交。更大朗读段可能增加等待或降低双卡并行机会，是连续韵律与延迟的取舍，不是已经证明的自然度/提速。保留顺序、背压、取消、有界codec与淡入淡出；不跨词叠加PCM掩接缝。

## 真实验收三轮（仍需目标机）

比较同一个人的干净8–10秒参考、同源16秒/24秒锚点，保持相同目标文、seed、模型与生成参数；每种至少三轮。分别保存GPU0/1同文WAV及完整朗读，审核相似度、单一声音、齿音/沙沙、句间自然度、漏字添字。不要只比较声纹数字或波形幅度。网页音频欠载/first_played与模型RTF分开看。

现有`tools/voice_benchmark.py --run --profile 实际档案ID --rounds 3 --chunk-size 8 --output 新私有目录/report.json`可调用驻留双GPU，保留18条WAV与JSONL，RTF>0.3即不达标；详见STEP16_QUICKSTART。它不代替试听。当前沙箱没有真实T4/Whisper/Qwen语音测量，未运行的结果一律BLOCKED，不用CPU/Mock代替。

网页真实训练闭环、长数据完整审核对齐/训练全覆盖、真实双T4训练提速、严格声学逐字拒播等历史缺口仍未完成。整体仍PARTIAL/BLOCKED。

---

## 内嵌备忘录：KAGGLE_TARGET_ACCEPTANCE.md

# 目标双T4验收门禁（待实际执行）

日期：2026-10-23。此文件是交接操作顺序，不是已有GPU实验结果。当前沙箱虽已装Torch供CPU测试，但没有可用CUDA/训练权重（实际Faster/HF已安装供CPU接口实验，不代表完整模型）、物理麦克风或DeepSeek通路；不得把本地CPU、Mock、界面截图或surface_preflight_passed填进真实实验结果栏。

## G0：保护基线与凭据

保留原始与step1/2/3/4/5/6/7/8/9/10/11包及SHA256。升级前先确认所有旧版本GPU进程停止，再解包到目标ROOT；资源锁只约束本版本合作进程，不能自动迁移旧服务。使用可丢弃的独立Kaggle会话，双T4、Internet On；依赖和模型revision尚未完整锁定，先审查安装流程，不在含无关凭据的环境执行。Kaggle Secret使用QTTS_ACCESS_TOKEN（32–256位非空格ASCII）与按需的HF_TOKEN/DEEPSEEK_API_KEY；不写进命令行、截图、共享日志或交接文件。

仅解包检查可在Notebook子进程中运行（脚本须先上传到当前目录）：

```python
import os, subprocess, sys
subprocess.run([sys.executable, 'kaggle-fixed-step17.py'], check=True,
    env={**os.environ, 'QTTS_UNPACK_ONLY':'1',
         'QTTS_ROOT':'/kaggle/working/qtts-step17-inspect'})
```

这是解包，不安装/下载/加载权重。不要把QTTS_UNPACK_ONLY留在完整启动环境中，避免把仅解包退出0误当模型成功。

## G1：先收集环境，再做表面探针

在目标Notebook记录实际GPU名称/数量、驱动、Python、Torch/CUDA版本、计算能力、总/空闲显存和磁盘。当前探针只记录总显存，不代替空闲显存测量。

完整启动前明确QTTS_MOCK=0、QTTS_DTYPE=fp16、禁用QTTS_ALLOW_SINGLE_GPU；首次建议QTTS_TUNNEL=none，暂不启公网隧道。必须在启动模型进程之前设置，事后在另一个shell里unset不会改变已经运行的Mock进程。

安装流程审查后，真实启动示例（会安装依赖和下载模型，当前沙箱没有执行）：

```python
import os, subprocess, sys
runtime_env={**os.environ, 'QTTS_MOCK':'0', 'QTTS_DTYPE':'fp16', 'QTTS_TUNNEL':'none'}
for key in ('QTTS_UNPACK_ONLY','QTTS_ALLOW_SINGLE_GPU'):
    runtime_env.pop(key,None)
subprocess.run([sys.executable,'kaggle-fixed-step17.py'],env=runtime_env,check=True)
```

默认ROOT=/kaggle/working/qtts；如果自定义QTTS_ROOT或QTTS_STATE，后续路径必须同步。启动失败时先保留STATE/backend_probe.json与脱敏错误类别，不重复安装/重试掩盖失败。

运行时探针独立复现：

```bash
python /kaggle/working/qtts/tools/backend_probe.py --runtime --expected-gpus 2 --dtype fp16 --timeout 120 --output /kaggle/working/qtts/state/backend_probe.json
```

退出2=阻断/仅检查；退出0=设备与API调用形状通过。后者仍没有加载权重，四个model/inference/training/performance验证标志均为false；**kwargs能接收参数不证明内部语义，SDPA/CUDA Graph/精度稳定性还需实际推理。

## G2：证明不是Mock，再做最小真实推理

启动后在Notebook本机用受认证的GET /api/health、/api/workers检查两个worker的健康详情，记录engine=faster-qwen3-tts、dtype=fp16、GPU编号0与1。`ok:true`、HTTP200、两个端口或模拟正弦PCM都不足以证明真实模型。worker /health不应被公网直接暴露。

使用合法同说话人的短WAV参考，自己命名声音库，提供与锚点逐字匹配的文本；没有文本的样本另测真实ASR，不把ASR失败伪装为成功。创建与启用声音档案只准备缓存，**不是训练**。

既有工具的参数已对照源码，声音档案创建后可运行：

```bash
python /kaggle/working/qtts/tools/selftest.py
python /kaggle/working/qtts/tools/e2e_check.py --url http://127.0.0.1:7860 --mode read --min-gpus 2
```

默认读取已启用档案；无档案应跳过并返回非成功，不能计为模型通过。也可用实际档案ID传--profile，不填虚构ID。访问口令由私有环境/认证目录读取，不放命令参数。selftest中的可选Rust检查可能单独失败，逐项记录；--quality会调用真实质量模型，待下载/硬件条件具备后再执行。旧工具个别输出将速度倍率rtf_x标成rtf并带×，应按定义解释，不当作标准RTF。

每卡保存并试听真实PCM/WAV：24kHz、有限值、非空、非全零、无异常幅度/系统性爆音；记录实际流式chunk时间、数量与间隔，排除“整段生成完再切块”伪流式。短句/长句、冷热启动、多段调度和取消恢复分别测量。不通过则回到后端兼容适配，不能静默替换小模型或换预置说话人。

## G3：容器与浏览器链路

分别测试真实浏览器麦克风录制的WebM/Ogg/MP4容器与WAV上传，记录浏览器MIME、解码器/ffmpeg版本、实际采样率、声道、时长、大小和服务端拒绝条件。当前沙箱只有原生Chromium软件输入编码与soundfile小WAV路径，未测物理麦克风或真实ffmpeg。

可信HTTPS浏览器中验证权限拒绝/等待取消、切换主视图、诊断、锁定、麦克风设备结束、超限、上传失败后片段保留。测试虚拟键盘、横屏、缩放、中文字体与屏幕阅读器；当前自动化只覆盖列出的Chromium CSS视口，不能扩展为全设备通过。

## G4：DeepSeek与性能指标

先核对真实模型名、服务端上下文/输出上限与收费额度；Key只用Secret或浏览器内存。测试长流、错误帧、断网、取消、恢复以及切换声音；不自动重试可能重复扣费的请求。

- 分开记录首token、首模型chunk、首PCM、浏览器第一段实际播放；首PCM不是可听首声。
- 标准RTF=生成耗时/音频时长；rtf_x=音频时长/耗时，是倒数速度倍率。分卡与系统聚合指标不可混用。
- 冷/热、短/长文本、两卡调度、浏览器缓冲分别报告，记录足够样本的分布与失败比例，不只展示最好的一次。
- 首声<3秒、RTF≤0.5、无系统性断音是待验收目标。ECAPA余弦或内部fidelity指数不等于99.5%身份一致率；先定义测量/盲听协议和保留集。

## G5：真正双卡训练（实验性核心已实现，Qwen/T4执行未验收）

独立训练作业必须验证world_size=2、两rank实际处理样本、可复现样本覆盖、梯度同步、优化器更新、显存、检查点保存及重载真实试听。当前已有训练输入与声学码准备入口/来源封存/读取租约：逐条文本、统一参考、授权/单说话人声明、完整24kHz mono PCM16 WAV、固定哈希与双rank数学分配计划。真实audio_codes仍blocked；已有FP16 LoRA/DDP/optimizer与adapter代码及CPU小网络梯度/参数更新证据，但未执行Qwen/CUDA训练或自动训练/推理模式切换；不能按创建档案、候选校准或准备输入验收训练。输入副本应先按固定manifest SHA256校验，上游工具必须在快照目录解析相对路径；其他音频格式需受限解码另验，不静默裁剪。

不要将官方BF16/FlashAttention2/全参数AdamW示例直接用于T4，或只加accelerate launch --num_processes 2就称完成。先核对T4支持、模型包装属性、优化器内存和检查点语义；LoRA、ZeRO/FSDP等方案均须实际接口与显存验证，不在缺权重时猜测兼容。训练与推理应隔离，避免每GPU推理实例占满显存时并发训练。

## G5a：声学码准备（入口已有，真实模型未验收）

第七阶段仅本机CPU离线CLI，使用固定输入manifest租约与可信本地12Hz tokenizer模型内容树hash；无自动下载或GPU编码入口。先按KAGGLE_STEP7_AUDIT.md验证真实单条全PCM编码、输出ceil(frames/1920)×16与完整样本覆盖，再实际decode试听、测CPU RAM/耗时。fixture码与stub调用不是该门禁证据；当前真实encode缺qwen_tts/权重且无GPU，仍blocked。

当前已有第八阶段同机同UID整组资源准入协议，但没有自动推理/离线任务模式切换或GPU编码。改为GPU任务前仍需受控作业接入与实际显存测量，不能直接在两模型已占显存时调用cuda:0。输入与码版本租约已实现，码版本已接入实验性双rank训练器并受控共享FD；真实Qwen/T4执行仍未验收，训练器须持有保护直到所有读者退出。语义/解码/训练标志不得因结构检查自动变true。

## G5b：资源准入协议已有，硬件回收尚未验证

按KAGGLE_STEP8_AUDIT.md使用resource_control.py status/reserve；busy=false不代表GPU空闲，预约也不执行模型。真实supervisor/worker/analyst须使用本版本FD协议；父死但孩子持锁时仍busy，不能依PID/TTL强制解锁或删除fleet.lock。多模型进程由supervisor启动，旧版本/外部进程必须另行确认已停。

在目标设备实际记录所有进程停止前后nvidia-smi与CUDA空闲/保留显存，再预约并接入受控GPU任务，验证取消/失败/恢复。此刻有CPU进程/FD与小网络Gloo证据，无实际VRAM回收、自动模式切换或双rank训练证据。bootstrap不再自动按旧PID/pkill停服务；遗留PID标记须人工确认后清理，不能删资源锁。

## G5c：来源封存/读取协议已有，不是训练许可

schema2完整复制输入manifest/JSONL，验证源固定hash、WAV/text/ref/顺序/计划交叉一致；声明只是用户记录。schema1仍legacy-unsealed，禁止凭当前库补写旧授权。list的政策字段不等于完整核验，固定manifest hash verify才返回provenance_verified_now。

hold-read只保持检查租约，第十阶段实验性训练器已接入，但仍须现场验真实编码/语义/权利政策/设备与DDP；首版同版本读取独占，删除/第二读取409，取消/超时/进程退出释放。不能当训练按钮，已有CPU进程/FD接管与小网络参数更新证据，但不能称Qwen/CUDA参数已更新。详见KAGGLE_STEP9_AUDIT.md。

## 待填结果表（当前均未验收）

| 门禁 | 当前真实结果 | 要保存的证据 |
|---|---|---|
| G1 环境/表面探针 | 待目标设备运行；沙箱是blocked | 硬件/版本/报告/空闲显存 |
| G2 双卡真实模型 | 未运行 | 非Mock引擎、每卡真实输出与时间、异常 |
| G3 物理录音/容器 | 未运行 | 浏览器/设备/MIME/ffmpeg/解码与拒绝样本 |
| G4 DeepSeek/性能/音色 | 未运行 | 真实流、分布、取消、听测协议与保留集 |
| G5a 真实声学码/解码 | 未执行；离线CPU入口已有，依赖/权重blocked | 可信模型hash/实际编码/完整覆盖/解码/内存与时间 |
| G5b 资源/显存 | 合作式协议已验证；真实显存/模式切换未验收 | 实际进程/空闲显存/预约与任务取消恢复 |
| G5 双卡训练 | 实验性FP16 LoRA/DDP/adapter代码已实现；真实Qwen/CUDA未运行 | 双rank/样本/梯度/参数更新/检查点重载 |

只有取得对应原始记录后才能改表。秘钥、真实私密语音、完整私人转写和大模型/数据集不进入Git或公开报告。

第十阶段运行入口及具体Notebook取消代码见KAGGLE_TRAINING_QUICKSTART.md；无需等待更多基础设施即可在真实环境尝试。optimizer/adapter执行成功不等于音质通过，不自动替换推理模型，真正Qwen新进程重载/试听与接入聊天仍待执行。


## G11：显式训练adapter后端与聊天（现场待验）

第十一阶段已实现实际接入，不是只写未来工具。按KAGGLE_ADAPTER_QUICKSTART.md从真实completed run取得pin、显式发布命名候选，再使用qwen-adapter-buffered、本地Base及固定hash启动既有supervisor。默认faster保留。两worker加载确认才改变active，错误/缺adapter/Base/错误模式不得回退。

原生API一次生成解码完整段，不接受为G4“声学流式通过”；health/stats/UI必须显示sentence-buffered。只允许称DeepSeek文字/网关段流保留，不能把后处理PCM块或停顿包当模型流式。现场验证保存speaker prompt的真实声音、A/B/A、取消后释放、真实长回答及一份Base/卡的峰值显存。当前CPU数学/本机真实Go+SSE/HTTP是替身系统证据，不是Qwen/T4、新进程试听或外部DeepSeek验收。

固定训练候选拒绝参考文本/候选/校准修改；旧普通档案仍用faster模式，保持删除/认证/两视图。一个参考WAV/转写进入旧profile私有备份范围，run/完整模型不自动备份；恢复缺文件明确失败。源码总目标仍22/300，不因这一开发阶段自动勾满硬件/音质要求。


## G12：现场Mimi/RoPE故障与会话驻留复跑

用户现场已实际识别两T4（各15636037632字节、CC7.5），下载/编译完成；模型加载明确失败，不能保留为“硬件未知”也不能升级成加载成功。step12使用faster0.5.4/qwen-tts-hf0.1.1.post1/TF5.20.2真实现代配置桥接，旧字段异常已在CPU实际wheel函数复现并修复；原配置不变、3个theta验证。CPU数学smoke不是本门禁完成。

目标重新启动完整Kaggle会话后，确认先通过qwen_mimi_rope_cpu，再两个worker各自完成from_pretrained和warmup。检查health的requested_model、model_loaded、单CUDA可见设备与residency_policy，结合实际GPU显存/进程和音频，不能只看这些字段或workers_healthy数字。完成短句/长句/停止与显存记录；配置错误fatal应停止重试并清理本次supervisor，无旧PID盲杀或删锁。

QTTS_RESIDENT=1取消旧600次周期重载和13.5GB主动回收，不自动idle卸载，但错误/OOM/平台回收仍会中断。磁盘权重缓存不等于GPU永久驻留；Kaggle不作永久占用验收。固定三项依赖不是全环境lock，保留平台Torch/CUDA约束后仍需实际安装冲突与模型完整调用验证。

## 第十三阶段现场状态更新（优先于上面历史step12结论）

用户step12仍同错失败，旧CPU函数测试没有覆盖Faster延迟导入。step13显式导入HF后桥接并强制smoke；完整真实包+微型Mimi初始化/重载已在CPU三进程通过，但不是完整Qwen/T4验收。目标22/300不升级，按KAGGLE_STEP13_QUICKSTART.md直接复跑。

## 第十四阶段优先更新

用户step13现场已通过两T4模型加载/预热ready门禁。14仅新增长录音预算/CPU等价缓存/原文分段/默认无后加呼吸。网页一键训练闭环、真实训练提速与质量、首播改善及声学逐字核验未完成/验收，完整目标仍22/300。详见STEP14_AUDIT/QUICKSTART，不能用本轮模拟通过升级真实音质门禁。


## 第十五阶段优先更新

当前step15强隔离参考PCM/ICL上下文，向量模式可能改变音色韵律，不能据CPU证明真实语音完全不串参考。先正常重启会话再运行，按STEP15_QUICKSTART直接朗读与DeepSeek首句分别测试三轮。默认输出-18dBFS、上限12dB增益，校准默认关闭但手动保留，CPU ASR可复用。比较创建耗时时必须区分冷/热、下载和可选校准；比较首声看first_played_ms与underruns。每T4双模型没有实测，不默认开启。旧训练闭环/长数据全覆盖/声学拒播缺口不因本轮交付消失。


## 第十六阶段最新优先门禁（覆盖15纯向量与12dB默认值）

最新包16采用匹配转写ICL条件，codec仅生成码；参考内容及模式pin，默认前瞻0/最大增益6。按STEP16_QUICKSTART先试听不同于参考的目标文本，再做双GPU三轮18条真实基准。tools/voice_benchmark.py不带--run零测量blocked；真实目标0.3任一条不达即失败，达速度也不等于音质合格。旧参考正文继续出声可来自模型幻觉，不能只凭未拼接PCM认为声学逐字已验。历史训练闭环/全覆盖/声学拒播缺口保留，目标22/300仍不升级。


## 第十七阶段最新门禁

先完整重启到17，不用截图15判断17修复。用同源10秒、16秒与24秒对照，长录音按时间戳/真实窗口识别择锚；生成参数也进入v2 pin。核对原文、每卡同文音色/噪声、整段朗读、first_played/underruns与RTF，至少三轮。结构对照16失败17成功不等于实际Whisper识别准确或Qwen质量达标。57份完整备忘录及STEP17_QUICKSTART说明边界，历史训练/覆盖/声学拒播缺口保留。

---

## 内嵌备忘录：KAGGLE_STEP18_PLAN.md

# 第十八阶段：参考条件可追溯、首声、噪声与连续朗读

> 最新优先：S5完成短尾/重采样终点/epoch已实际修复，见KAGGLE_STEP18_S5_PLAYBACK.md；最终610CPU/37VM/173Chromium各三轮以progress-s5.json为准。完整候选app不切正式入口，真实声学与整体仍PARTIAL/BLOCKED。

> 最新优先：S4有界裁剪/worker结束与取消已实际修复，见KAGGLE_STEP18_S4_TRIMMER.md；602×3、21分块×3通过。S3 worker保留，S4入口worker_s4.py未切换正式服务；整体PARTIAL/BLOCKED。

> 最新优先：S3因果 NumPy DSP 与隔离worker实际接入，见 KAGGLE_STEP18_S3_DSP.md；562×3及14分块×3已通过，但Rust/真实声学与完整S3仍PARTIAL/BLOCKED。更早“下一步S3”等均为历史。

> 最新：S2-B有效指标与加载就绪实际实现，见末尾及KAGGLE_STEP18_S2_VALIDITY.md。早期“评分未修”仅历史；完整产品／声音／双T4验收仍未通过。

> 最新：S2-A校准快照实际实现，见末尾及KAGGLE_STEP18_S2_SNAPSHOT.md。S1原28合同保留，完整S2／模型／声学仍未验收；更早“未实现”仅为历史状态。

> 当前优先状态：S1隔离候选实际实现，见本文件末尾和KAGGLE_STEP18_S1_CANDIDATE.md。问题28明确允许未发布候选小步修复，不改冻结17；下文早期“尚无产品修改／不实施”是当时历史，不是本次状态。G0整体与完整S1验收仍PARTIAL/BLOCKED。

## 当前状态（2026-10-23）

当前活动分支`arena/1160bd87-kagglee`，继承已合并的`arena/03d65d8e-kagglee`前两轮记录；历史baseline保留原分支身份不改写。已完成三轮关键路径专题审查各100条、外围入口静态复核、DSP分块/参考状态/播放器边界/裁剪器边界的受控实验。已按顺序完成第25–27题及各50条建议；本批三题已完成，不预填问题28。**三轮专题与库存AST核对不等于所有模块逐行语义审查三遍；该全源覆盖门禁尚未签收。** **没有修改产品源码、没有生成18发布包、没有宣称声学达标。**

截图事实：已是17；41.6秒录音建档成功，耗时142.3秒；RMS约-47.7dBFS、峰0.011；候选#0/#1/#2约9.1/10.5/11.0秒，SNR估计17.1/16.3/17.8dB。没有附件音频，不能由截图听出噪声或确定声学根因。源码说明单锚点用于ICL，候选参与评分与质心，校准逐个试验再择一，不是三参考同时融合。

用户“参数要结果（#0、#1、#2等所有参考）”按要求采用保守、可检验解释：候选应有完整评估/校准依据，生成条件应明确可追溯；是否支持模型原生多参考融合，必须读实际接口后决策，不能用拼接PCM、混转写或平均不兼容提示冒充。所有参考参与质量分析与全部参考同时作为ICL是不同功能。

## 约束

- 中文小步汇报；每轮100条具体建议，不将建议当已证实bug。
- 完成三轮源码审查后，自问自答按一次一题执行，具体选项、推荐理由、待证边界；每题先列50实施建议再下一题；累计决策从问题25开始，不能先批量伪造回答。
- 总方案先于产品修改；不要求100%信心，不承诺零错误/零噪声。缺真实证据保持BLOCKED。
- 原始–17包、manifest和工作台冻结；参考PCM绝不混入生成播放；首声不能用静音占位或参考原音冒充。
- 已有记录、取消、安全、训练、私有数据及复制功能不豁免。绝不上传私有WAV或把模型权重纳入Git。

## 分阶段执行与验收

1. **基线与审查**：核对53内嵌资产、76历史冻结哈希、15正式文件；保留新阶段快照。每轮分开记录实际读过的路径和未覆盖语义，AST/哈希不是全源语义证明。第一轮见REVIEW1。
2. **第二轮：数据与状态语义**：遍历profile/API/缓存/Go会话/前端条件选择，读实际Faster及Qwen提示接口，确认多候选校准与多参考条件是否可实现；检查切换、取消、双卡一致性和过期会话，记录100建议。
3. **第三轮：数值与时间链路**：逐层追踪源录音清理、codec窗口、Rust/NumPy DSP、协议、重采样、Worklet、调度与文本聚合；覆盖启动/欠载/段间停顿，记录100建议。对其他功能逐模块复核，不能只审4个热点就称所有代码已查完。
4. **逐题决策与最终实施细则**：至少覆盖全部候选的作用和实际条件绑定、首包与实际播放测量、DSP分块一致性、噪声与自然度验收；每题50建议后进入下一题。只有实际接口、复现或测量支撑的改动进入产品实施。
5. **小步实现**：优先修复已复现的确定性状态问题；每个修复先保存失败样例，再修复，局部测试通过后完整回归。多参考/降噪/缓冲策略按实验选择，不直接强滤波、不跨词叠加、不删字。
6. **三轮最终工程验证**：在最终源码上运行完整Python、Node、Go race、六协议与浏览器三轮；当前环境依赖需要重建，旧17收据不能当本阶段执行。涵盖取消/锁定/文件路径/长录音/转写/双卡pin/训练来源及正文完整性。
7. **三轮真实模型实验**：实际双T4上同人同文、固定seed和有效参数，比较每候选及推荐策略；保存实际生成WAV、每层耗时、worker与wall RTF、播放欠载与首样本确认。同文两卡与长文交替分开测，结合盲听和转写审核；真实权重/GPU不可用则明确未运行，不拿合成信号或tiny模型代替。
8. **发布与完整备忘录**：冻结18源码后repack、固定hash复制/下载、手机和剪贴板拒绝回退；逐字节校验及全部历史资产冻结检查。所有完成的备忘录完整内嵌提示词，未完成项明确。此阶段进行中的汇总为`KAGGLE_STEP18_HANDOFF_PROMPT.md`；原17最终提示词暂不覆盖。

## 第一轮实测收据

- 新环境仅安装NumPy2.2.6至被忽略`.venv`，无Torch/完整模型/CUDA运行证据。
- `kaggle/tests/dsp_partition_probe.py`对冻结17 NumPy Leveler输入相同半秒双音信号，比较整块与48/64/96/240/1920及不规则分块，每轮12个案例，三轮。
- 隔离增益（target=-6dBFS/max_gain=0）48分块与整块最大差1424 int16单位；1920分块差0。对应淡入跨短块从零重新起算的源码风险。
- 正常增益（target=-18/max_gain=6）1920分块最大差8单位；48分块差1425。AGC分块实现也非严格分块不变。该实验未编译Rust，不称已实测跨后端数值差。
- 所有案例样本数完整、无非有限输出。该收据证明工程分块依赖，不证明噪声听感、用户根因或模型质量。
- `repack.py --check`、JS语法检查、Node30项基线通过；尚未执行本阶段完整334项Python或Go/浏览器回归。

## 第二轮取证与复现（未修复）

- 实际发行版为`faster-qwen3-tts==0.5.4`及`qwen-tts-hf==0.1.1.post1`，wheel SHA256核验通过；`qwen-tts==0.1.1`仅用于对比发行版依赖，未安装。首次误写`qwen-tts==0.1.1.post1`查询失败后按项目pins纠正，未改变产品依赖。
- 实际接口的列表/字典prompt长度必须与目标批次匹配。三参考提示加单目标被拒绝，三提示三目标是独立批次，不是自动融合；单ICL快照仍可用。
- `reference_state_probe.py`对原函数AST每轮执行6项prompt合同、4项校准场景、9项候选参数和1项双卡seed诊断，三轮结果一致。外部模型、ASR、声纹、tokenizer及网络均显式fixtures；没有HTTP或线程压力测试，也没有完整模型运行。
- 复现`index=true`选1、`1.9`截为1、null/容器类型未捕获异常；校准ASR全部失败默认CER0.05；旧转写评分可选中新转写；全合成失败仍chosen0；校准丢弃加载失败回执；同文双卡诊断seed分别100/101。
- 并发案例是确定性交错：模拟候选1编辑后切回候选0并编辑的合法元数据状态。候选WAV不变，但最终采用的候选1转写未在该轮被评估。它不是实际多线程压力或HTTP事务证明。
- 保留已有成功保护：正式播放同会话seed、Go激活并行加载和二次指纹确认/旧active保留、Worker锁内前后核验、文本/候选reload_response的503与reference_saved、前端accessEpoch锁定防迟到回填。
- 第二轮100条及证据见REVIEW2和`validation/step18/reference-state-baseline-round1..3.json`。初始19项探针收据及源码快照保留initial命名，最终扩展到20项并补充明确的被评分转写。

复现命令：先建立含NumPy2.2.6的隔离环境，执行`.venv/bin/python docs/validation/step18/fetch_reviewed_upstream.py`（只解包经哈希核验的两份源码，不安装、无权重），再执行`.venv/bin/python kaggle/tests/reference_state_probe.py --round 1`，依次2、3。

## 第三轮取证与顺序决策（未修复）

- 第三轮100条见REVIEW3；53资产完整读取/hash/所有Python AST核对见review3-inventory.json。生成码窗口、DSP、裁剪、播放器、调度/转发路径作专题语义追踪；训练、资源、持久化和正式工作台仅部分边界复核。不能把库存核对称为所有代码已语义查完三遍。
- 当前新环境只重建NumPy2.2.6；Node可运行，Rust/Go编译器、Torch和目标GPU实验未执行。前两轮收据保留历史，未冒充本分支完整模型回归。
- Node VM执行原Player/Parser/Worklet，每轮22例、三轮一致。完成20/50ms音频在24k/44.1k/48k下滞留buffering，51/100ms可发play；该路径也影响可能的欠载末尾，但本轮未执行真实浏览器/声卡。
- 重采样整块/47样本处分块在容差内一致；终止时缺下一插值端点，需要明确尾样本策略，未证明其有可听损伤。自然结束、欠载恢复一次计数、reset输出为零、overflow计数、逐字节协议帧和超大帧限制均被保护案例覆盖。
- 原EdgeTrimmer每轮8例、三轮一致：64/119样本有声块可被全忽略；跨块35ms预滚比整块少840样本；60样本末尾非零信号可留在held且没有finish接口。小块合同问题不等于当前Faster1920样本倍数生产路径已发生；合成信号不能证明真实辅音被删。
- firstPlayedMs当前在play命令处记录，不是硬件出声；Worklet固定192样本淡入在24k/48k为8/4ms。源码确认Rust flush清DC而NumPy不清，但当前Worker每段重建leveler，不能把跨段复用差异直接称生产噪声根因。Rust未编译，不能声称跨后端实测通过。
- Node30、JS语法与repack基线再次通过，完整Python/Go/Chromium/六协议及完整模型仍未在本阶段最终源码执行；尚无18产品修改。
- 第25题按一次一题完成，详细四选项、推荐C及50建议见KAGGLE_STEP18_DECISIONS.md：全部候选同条件评估与实际ICL/实验融合明确分层；不把列表批量或单锚点说成融合。融合仅研究同模型Qwen嵌入、未验证不启用为默认，不保证提升。问题26已在后续小步中按顺序回答，见下节；第三轮当时的收据保留原状态，不改写历史。

## 问题26：修复次序与首声度量（已完成决策，未实施）

- 先校验第25题选项/回答/50建议未变，再完成第26题四选项、推荐C、具体顺序及50建议；第27题只留下待追问，不批量填答。
- 选择先建立兼容度量和回归合同，再修参考状态可靠性、DSP/裁剪有界状态、完成短尾排空，最后真实同条件测试首块/缓冲。正常流式启动不一律改为零缓冲，默认首段4帧暂不改。
- 新增latency_contract_probe.mjs，原Player代码VM每轮16例、三轮一致：20/50ms完成短尾在buffering与starved均滞留，51ms可发play；未结束短缓冲继续等待、已播放短尾不强停、空结束可结束。显式注入时钟示例300ms首PCM与750ms命令时刻不是实测性能，消费/声学首声仍未测。
- 源码确认Go queue_wait_ms在合成结束计算，包含生成时间，不能当纯队列；Worker queue_ms也含锁/参考准备。下一实现应新增分阶段/分尝试指标，保留旧字段语义，不直接重命名成“真实首声”。
- firstPlayedMs为命令时刻；Worklet确认、非静音阈值、正确人声和声卡出声分别定义，未知保持null。任何实测改善还需正文完整、掉样、欠载、噪声、自然度和RTF联合门禁。
- 以上仅决策与控制流取证；没有性能提速结论，没有产品源码改动。问题25的主体hash及50条已保留核对，当前累积25–26两题100建议；历史24题1200不动。

## 下一执行门禁

第25–27题已按顺序各完成50条，旧主体hash保留。实施细则见`KAGGLE_STEP18_IMPLEMENTATION.md`：先补G0全源三遍语义覆盖与300建议处置/测试映射，再按S1–S8小步修复。全源深审、真实HTTP/线程压力和声学实验不能用建议数或合成案例替代。当前不修改产品、不切复制页到不存在的18；不自动追加问题28。

## 语言与性能原则

PyTorch/CUDA继续承担模型计算，Python组织提示与分析，Go承担调度/协议，Rust承担DSP，JavaScript承担采集/播放。只有实测热路径需要时才增加C/C++等实现；不新增Java/C#/VB/SQL/Fortran服务凑语言。NumPy回退一致性问题应按真实算法合同修复，不用隐藏回退失败冒极致性能。

## 声学验收边界

沙沙声需分别定位原始录音、参考清理、模型生成、codec、后处理及播放欠载；低输入与估计SNR不等于根因。首PCM/发送play命令/Worklet消耗首语音/硬件声学首声不是同一时间。自然度需完整朗读试听与逐字核对。历史真实训练闭环、长数据覆盖及RTF≤0.3缺口继续保留；整体PARTIAL/BLOCKED。

## 问题27：噪声/自然度分层与验收（已完成决策，未实施）

- 四选项、推荐C及50项建议见DECISIONS；参考→ICL→模型PCM→后处理→浏览器→设备分层定位。嘶声、点击、欠载、韵律分别记录，不从截图断定根因。
- noise_metric_probe.py每轮8项、三轮：原estimate_snr为20ms帧RMS的92与8分位差；稳态干净音与两种真实组件SNR不同的等能量重复块均返回0，无噪动态音返回约14.64dB。因此该估计不是噪声真值，不能单独签声学验收。
- 均匀衰减不改善组件SNR；原normalize_speech约14dB增益同时放大信号与噪声。理想FFT低通反例同时损失有用6kHz分量，误差增大；它不是项目降噪器实测，也不是真实辅音试验。
- 合成探针未运行真实降噪/语音模型/GPU/用户WAV；不据此改变降噪阈值或默认算法。声纹、内容、噪声、完整自然朗读及时间指标联合验收，真实声学缺口仍BLOCKED。

## G0补审第一批（未签收）

- 本批实际全文语义读6份/930行，53资产逐项覆盖台账；第二/三遍完整签收0，其余47项及外围仓库继续补，不宣称全源完成。
- 300条建议逐ID初审/批次/测试合同见G0_DISPOSITION；23条关联限定范围缺陷、96保留、89文档/测试合同、55真实条件阻塞、37待证。不是23个独立bug，更不是300已修。
- 84项CPU/进程/进程内HTTP专项三轮均通过；另10项边界三轮复现损坏Base配置未受控异常与恢复中途I/O故障部分提交。没有实际训练/声学/性能验收。
- CPU测试依赖已补入忽略.venv，NumPy仍2.2.6；Torch/完整模型/Go/Rust目标实验未执行。本批详情见KAGGLE_STEP18_G0_AUDIT.md，下一批先补数据/声码/原始库和训练发布链。

## G0补审第二批：训练链（未签收）

- 新读12份/1974行，当前第一遍全文累计18/53、2904行，剩35项；完整第二/三遍仍未签收。当前覆盖台账以g0-training-chain-coverage.json为准，第一批保留历史不改写。
- 135项训练数据/声码/原始库/兼容/安全张量专项×3均通过；新增6项provider元数据合同×3复现HF提供包与旧版本查询不匹配。重型加载为fixture，未执行真实编码/训练。
- 新发现F01单列，不覆盖300原建议；细节见KAGGLE_STEP18_G0_TRAINING_CHAIN.md。下一批优先Go安全/会话/调度及协议，之后完整前端与启动恢复。产品未改，G0仍待补齐。

## G0第三批：Go网关与本地协议（未签收）

新增全文第一遍13份/3527行，累计31/53、6431行，剩22项；完整第二/三遍仍0。原Go主测试40项（含子测试56）×3和新增边界10项×3完成；独立竞争见证三轮均预期非零并报告DATA RACE，不能计为无失败套件。确认快照共享map竞争F02及工作帧校验不足F03，均未修复；queue_wait_ms/健康/慢客户端/SSE问题按证据区分源码观察与待验证。

实际本地Go/Python mock播放链、原始库HTTP、合成训练输入HTTP各内部3轮通过；损坏音频预期处理失败、合成WAV快照不等于真实训练。未重跑全部历史6类协议。详细边界见KAGGLE_STEP18_G0_GATEWAY.md，当前覆盖改以g0-gateway-coverage.json为准，历史台账/300建议/Q25–27均保留。下一步补剩余前端、运行分析、DSP/启动恢复等源码及全源第二/三遍，不跳过G0进入S1，不新增18包，不声称模型/双卡声学或性能验收。

## G0第四批：前端录音与流式播放（未签收）

新增全文第一遍3份/2217行，累计34/53、8648行，剩19项；完整第二/三遍仍0。实际Chromium完整浏览器套件134项×3通过（原123+新增11），失败/跳过/retry/flaky均0；新增8保护+3原缺陷观察，不把观察通过说成修复。第1–17阶段完整包逐字节剪贴板保护通过；真实原始文件按冻结hash核对，浏览器原始文件保留用sentinel，不冒称完整原始文件复制。

F04迟到旧录音error误停新会话、F05协议解析失败未显式取消reader/请求、F06音频模块初始化失败未revoke临时Blob URL，在明确设备/网络故障fixture下各三轮复现，均未修。原Player22项/延迟16项VM各三轮，Node30/JS/repack通过；物理麦克风/声卡/真实模型/双卡声学未测。细节见G0_FRONTEND，当前覆盖以g0-frontend-coverage.json为准。继续剩19项Python运行分析/启动恢复/DSP/工具等及全源第二/三遍，不跳G0，不新增18发布包或Q28。

## G0第五批：Python运行/监督/启动与绑定（未签收）

新增全文第一遍5份/1536行，累计39/53、10184行，剩14项；完整第二/三遍仍0。原84项CPU/安全/租约/可靠性+新10边界=94项×3通过，无失败/错误/跳过；新7保护+3原缺陷观察。真实supervisor/FD租约/进程组与致命健康协议两类各内部3轮通过，模型角色均CPU替身，不是实际GPU/训练或完整Kaggle启动。

F07异步响应队列无容量/反压、F08失败重载遗留与接受pin不匹配的prompt、F09clone模式规范化/报告不一致，均以明确CPU fixture复现，未修。真实文件hash及原Worker/RealEngine.load_profile控制流实际执行，重型提取/生成/GPU清理为fixture；不冒称真实错音色或慢客户端内存压力。Node30/JS/Python AST/repack通过，见G0_RUNTIME。当前覆盖以g0-runtime-coverage.json为准；下一步补剩14项分析/API/参考切分/DSP/工具/说明及全源第二/三遍，不跳G0，不新增18发布或Q28。


## G0第六批：分析/API、参考切分与Python/Rust DSP（2026-10-23）

完整报告见 `docs/KAGGLE_STEP18_G0_ANALYSIS_DSP.md`。全文第一遍新增6份2152行，累计45/53、12336行，剩8份；完整第二/第三遍仍0。172项专项×3轮全通过（旧160+新12，新9保护/3原行为观察），每轮失败/错误/跳过0；另14个分析AST案例与12个NumPy合成DSP案例各三轮，不等于全功能/全模型验收。新F10极短NumPy breath形状、F11窗口重转写词信息漏清洗、F12分析端失败/残缺流被接受，均未修复。F12实际requests+本地TCP；F11为显式ASR metadata fixture。旧校准/候选/诊断及分块依赖仍复现；历史上游cache缺失，本次未重跑6个prompt接口案例，不改写历史20案例收据。Rust两份只完整读源码，缺rustc/cargo，未编译/执行，不冒用NumPy代替。Node30/JS/Python AST/repack检查通过。原300建议、问题25–27各50、53源/94冻结/15正式与本批开始295历史文件hash保持；旧验证器保持历史版本，当前检查用verify_analysis.py。无产品改动、无18包、无真实训练/完整模型/GPU/用户WAV/物理声卡/提速/无沙沙或相似度验收。继续第一遍剩6工具与LICENSE/MEMO，再补全源第二/三遍和失败映射；整体PARTIAL/BLOCKED，不开问题28、不要求Continue。


## G0第七批：工具/LICENSE/MEMO，内嵌53资产第一遍补齐（2026-10-23）

完整报告 `docs/KAGGLE_STEP18_G0_TOOLS.md`。新增全文8份1332行，累计53/53、13668行，第一遍剩0；完整第二/第三遍仍0，G0不签收。197项专项×3轮通过（上批172+既有probe13+新12；新9保护/3原行为见证），每轮失败/错误/跳过0。另每轮4实际CLI合同，backend静态/runtime、默认无--run的benchmark均按预期exit2/BLOCKED；resource status exit0，不冒充模型通过。F13 E2E缺gpu/failed END/奇数PCM/残留误PASS，F14 watermark空HTTP503/ERR/残缺帧的零音频误PASS，F15 selftest failed/cancelled Mock统计流误PASS，均真实本地HTTPfixture三轮确认未修；F15时间是确定性fixture，不是性能实验。D01记录MEMO页头step15/xvector/maxgain12与当前17 ICL/maxgain6漂移，冻结MEMO不改。LICENSE全文读完不等于法律/依赖/权重/语音授权签收，NOTICE来源待证。Node30/JS/全部产品Python AST/repack通过；本批开始329历史文件hash保留，53源/94冻结/15正式不变，当前覆盖g0-tools-coverage.json，检查verify_tools.py。没有Rust/完整模型/GPU/真实训练/声学/提速验收，无产品改动或18包。下一步全源第二遍、第三遍交叉反证与300建议最终映射，不预填Q28，不要求Continue。


## G0全源第二遍第1批：训练执行与资源所有权（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS2_TRAINING.md`。8份重新全文阅读1056行并交叉复核CLI/controller/rank、OFD/码租约、准入/取消/原子产物、dataset/JointLoss/LoRA；第二遍累计8/53、1056行、剩45，第一遍53/53/13668保持，第三遍0。局部查看training_codes/encode_training/supervisor不计第二遍全文。219项×3轮全通过（旧197+另选既有artifact10+新12，新11保护/1原行为见证），失败/错误/跳过0。F16原stop_ranks在leader退出后漏清理忽略SIGTERM的额外后代，实际CPU进程/pidfd/OFD/flock复现，未修；测试finally定向清理并验证锁释放。额外后代为明确fixture，生产run_rank无DataLoader子进程，不声称真实训练出现此故障。AST仅运行纯Python采样、commit赋值回滚、dataset构造/len，无Torch算子模拟，无tensor/optimizer/Gloo/NCCL/完整Qwen/GPU/声学或提速验收。Node30/JS/全产品Python AST/repack通过。382历史文件hash、53源/94冻结/15正式、300建议初审与Q25–27各50保持；当前g0-pass2-training-coverage.json与verify_pass2_training.py。无产品改动/18包，G0仍BLOCKED；继续其余45项第二遍及全源第三遍/最终处置映射，不跳S1/Q28，不要求Continue。


## G0全源第二遍第2批：来源/声码/产物与恢复认证（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS2_STATE.md`。7份重新全文阅读1526行（voice_library/training_data/training_codes/trained_profiles/persist/qtts_common/access_control），第二遍累计15/53、2582行、剩38；第一遍53/53/13668保持，第三遍0。analyst候选函数仅局部，不计全文。324项×3轮全部通过（旧219+另选既有93+新12，新11保护/1原行为观察），各轮失败/错误/跳过0。预检曾因测试提取器保留装饰器报1个NameError，已仅修测试、保留原失败日志，最终预检12通过。F17：原pack目录枚举后切换候选，可收新版profile.json却漏新锚点，本地原解包接受后引用缺失；真实tar/文件与原候选AST函数体执行，worker reload/admission明确fixture，确定性交错非HTTP/线程压力或远端Kaggle。新缺陷未修，F01/F16及旧恢复部分提交等问题仍保留。代码/来源封存、取消/IO回滚/同OFD、隐私scope/auth转发及真实safetensors合成结构专项通过，不是Torch/optimizer/DDP/NCCL/真实编码/长训练/完整模型/GPU/声学/提速验收。Node30/JS/AST38/repack通过；408历史hash、53源/94冻结/15正式、300初审及Q25–27各50不变。当前覆盖g0-pass2-state-coverage.json，当前检查verify_pass2_state.py；完整交接增至73份原文。无产品改动/18包，G0仍PARTIAL/BLOCKED；继续剩38项第二遍及全53第三遍/最终处置，优先provider/binding/worker/分析API版本与取消/失败链，不跳S1/Q28、不要求Continue。


## G0全源第二遍第3批：provider/绑定与推理生命周期（2026-10-23）

完整报告 `docs/KAGGLE_STEP18_G0_PASS2_INFERENCE.md`。qwen_compat/voice_binding/worker/clone_stream/adapter_engine全文5份1071行，第二遍累计20/53、3653行、剩33；第一遍53/53/13668保持，第三遍0。新12（11保护/1观察）加旧324=336项×3通过，失败/错误/跳过0；ASGI2.3独立观察1×3另列。新F18原synth在正文迭代前启动生产线程，响应头阶段断连未进入generator finally，cancel未传给生产；ASGI2.4 send异常和ASGI2.3 receive disconnect两条真实Starlette响应路径三轮确认未修。断连时序/CPU工作负载明确fixture，非TCP/浏览器/模型/GPU证明，finally已定向清理join自有线程。旧F01–F17仍保留。新保护含FIFO/nonblock、绑定/预算、真实锁排队取消、重放迭代器close、RoPE异常/registry、trained磁盘重绑定/删除/链接/预算；最小manual_seed模块替身不是Torch算子或真实codec。临时venv未保留后重建固定关键CPU版本，保存安装日志/freeze，不声称全部传递依赖相同。Node30/JS/AST39/repack通过；435历史hash、53源/94冻结/15正式、300初审与Q25–27各50不变。当前覆盖g0-pass2-inference-coverage.json与verify_pass2_inference.py；交接74份全文。无产品改动/18包/真实训练/模型/双GPU/声学/提速验收，G0仍PARTIAL/BLOCKED。下一批分析/API/参考切分与版本/校准/取消失败链，继续剩33份第二遍和全53第三遍/最终映射，不跳S1/Q28、不要求Continue。


## G0全源第二遍第4批：分析/API、参考切分与校准所有权（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS2_ANALYSIS.md`。analyst/library_api/reference_segments全文3份1480行，第二遍累计23/53、5133行、剩30；第一遍53/53/13668保持，第三遍0。348项（旧336+新12，新10保护/2观察）×3全通过，各轮失败/错误/跳过0。F19两个同档案真实ASGI校准请求经原HEAVY(2)/calibrate，共用临时id；A删除后B原Mock Worker加载缺失，错误结果覆盖成功记录，均200；F20重载期间实际删除档案，原终检跳过None，原reload_response仍200/已保存。两项确认未修；worker transport/合成/ASR/声纹明确fixtures，不是TCP/真实模型/双GPU/删除后播放证明，临时资源/槽位清理通过。参考分析最多24预排/3落盘/单锚点条件区分清楚，不称Qwen融合或训练；新17秒长手工文本/20秒低能量窗口是合成控制流，不是真长数据训练。旧F01–F18及专题问题保留。Node30/JS/AST38/repack通过；470历史hash、53源/94冻结/15正式、300初审/Q25–27各50不变。当前g0-pass2-analysis-coverage.json与verify_pass2_analysis.py；交接75份原文。无产品改动/18包/真实模型/训练/GPU/声学/提速验收。下一批启动/监督/backend preflight，继续剩30份第二遍、全53第三遍及最终映射，G0仍PARTIAL/BLOCKED，不跳S1/Q28、不要求Continue。


## G0全源第二遍第5批：启动、监督与backend preflight（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS2_STARTUP.md`。bootstrap451/supervisor219/backend_probe200全文3份870行，第二遍累计26/53、6003行、剩27；第一遍53/53/13668保持，第三遍0。360项（旧348+新12，新10保护/2观察）×3通过，各轮失败/错误/跳过0。F21原sh在leader退出而后代持stdout时timer跳过killpg，超过请求期限并在外部清理后返回0；真实CPU/pipe/timer/pidfd、观察包装确定性交错，后代退出已验证，非完整bootstrap/性能证明。F22原watch的fatal回执写失败跳过kill/gave_up，HTTP每轮清零使8轮后fail_count仍1；health/IO/process/wait明确fixtures，非真实GPU或磁盘故障。两项未修，F01–F20保留。标准faster启动全部PINS逐项预查/精确安装/constraints0600与清理/Torch变更拒绝、probe先于下载的控制流测试通过；未执行真实pip resolver或GPU，后安装漂移/独立入口/native-adapter仍待证，surface preflight不是质量签收。Node30/JS/AST38/repack通过；497历史hash、53源/94冻结/15正式、300初审与Q25–27各50保持。当前g0-pass2-startup-coverage.json、verify_pass2_startup.py及progress-pass2-startup.json；交接76份原文。无产品修改/18包/真实训练/模型/双GPU/声学/提速验收。继续剩27份第二遍，优先网关调度/流协议/取消/超时及前端排空交叉核对，再全53第三遍/最终映射；G0仍PARTIAL/BLOCKED，不跳S1/Q28、不要求Continue。


## G0全源第二遍第6批：网关调度/流协议/取消与激活终检（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS2_GATEWAY.md`。main/scheduler/session/segmenter/llm全文5份2286行，第二遍累计31/53、8289行、剩22；第一遍53/53/13668保持，第三遍0。每轮Go原40主测/含子测56、旧专项10、新13（11保护/2观察）通过，合计63主测/79含子测×3；Python旧360×3通过，无新增Python测试。通过套件无失败/跳过/race warning；独立F02竞争见证每轮预期非零/DATA RACE，未混入通过数。F23原healthLoop接受HTTP503 ready=true，原网关报告两worker健康；真实本地HTTP，永久循环隔离于自有Go子进程并核对退出。F24原activate期间实际改profile.model_output_mode，最终conditioning改变而binding相同，仍200/提交active；worker回执为HTTP fixture，无真实训练产物/模型/后续合成。两项未修，F01–F22和专题问题保留。实际Go1.23.9新增于忽略venv，安装报告/wheel SHA与可执行hash保存；freeze仅多go-bin==1.23.9，其余依赖保持，不称全部freeze相同。Node30/JS/AST38/repack/原Go及新探针副本vet/gofmt通过；525历史hash、53源/94冻结/15正式、300初审及Q25–27各50不变。当前g0-pass2-gateway-coverage.json、verify_pass2_gateway.py及progress-pass2-gateway.json；交接77份原文。无产品修改/18包/真实DeepSeek/Qwen/训练/双GPU/声学/提速签收。继续剩22份第二遍，优先前端流终止/取消/遥测/完成排空，再DSP/工具/剩余Go安全和测试；全53第三遍及最终映射仍待完成。G0仍PARTIAL/BLOCKED，不跳S1/Q28，不要求Continue。


## G0全源第二遍第7批：前端终态/取消/排空与遥测（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS2_FRONTEND.md`。app1715/recorder358/index144全文3份2217行；HTML首次合并输出截断，已补读全范围，第二遍累计34/53、10506行、剩19；第一遍53/53/13668保持，第三遍0。新增浏览器12（10保护/2观察）预检通过，既有134+新12=146×3全部通过，失败/跳过/flaky/retry0；Player VM22/延迟VM16各三轮、CPU旧360×3通过，无新增Python测试。本批未重跑Go79/独立F02竞争见证或独立ASGI2.3/旧CLI矩阵，不挪用历史数字。F25原完整前端脚本END后仍收PCM/文本且第二END替换首汇总；F26网络EOF先发report并停telemetry，随后play/欠载UI变化不更新报告；真实Chromium原生流/DOM/timer，网络/设备/Worklet状态明确fixtures，非物理播放、真实欠载或声学/提速。两项未修，F01–F24及<=50ms已完成短尾/旧DSP等保留。Node模块按冻结lockfile npm ci恢复，未改lock；venv freeze与上批相同，无新Python依赖。Node30/JS/AST38/repack/前端探针语法检查通过；575历史hash、53源/94冻结/15正式、300初审及Q25–27各50保持。完整交接78份原文；当前g0-pass2-frontend-coverage.json、verify_pass2_frontend.py与progress-pass2-frontend.json。产品未改/18未发/真实DeepSeek/Qwen/训练/双T4/声学/提速未签收。下一批Python/Rust DSP和工具自检，再余Go安全/测试与LICENSE/MEMO；继续剩19份第二遍、全53第三遍/最终映射。G0仍PARTIAL/BLOCKED，不跳S1/Q28、不要求Continue。


## G0全源第二遍第8批：DSP与工具（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS2_DSP.md`。Python/Rust DSP及6工具全文9份1500行，第二遍累计43/53、12006行、剩10份1662行；第一遍53/53/13668保持，第三遍0。CPU372（旧360+新12，新10保护/2观察）×3全部通过，失败/错误/跳过0；NumPy分块12、原EdgeTrimmer AST8各三轮，旧问题未修；4个独立CLI合同×3，backend静态/runtime及默认benchmark按预期exit2/BLOCKED，resource status exit0，阻塞不是模型成功。F27 NumPy flush未清DC状态，常量480→flush192→零240得到240非零/峰6026，fresh为0；Rust源码清DC但未编译执行，正常worker每job重建Leveler，因此不是当前沙沙声根因证明。F28原benchmark/measure两实际HTTP端点health分别GPU0/1、18测量均GPU0，仍real_gpu_verified/speed_target_passed true；health/stats/PCM/clock明确fixtures，报告true是被反证输出，不是硬件/RTF成绩。两项未修。Node30/JS/产品Python AST/新审计语法/repack通过；625历史SHA、53源/94冻结/15正式、300初审及Q25–27各50保持。freeze与前端相同，无新依赖；Rust/Torch/Qwen/实际训练/双GPU/声学/提速未验。本批不重跑浏览器/Player VM/Go/独立F02/ASGI2.3，不挪用历史成绩。完整交接79份；当前g0-pass2-dsp-coverage.json、verify_pass2_dsp.py与progress-pass2-dsp.json。产品未改/18未发；下一批剩余Go安全/测试/go.mod和LICENSE/MEMO共10份，再全53第三遍及300最终映射，G0仍PARTIAL/BLOCKED，不跳S1/Q28，不要求Continue。


## G0全源第二遍第9批：安全与全文收尾（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS2_SECURITY.md`。剩余Go安全/测试/go.mod及LICENSE/MEMO全文10份1662行，第二遍累计53/53、13668行、剩0；第一遍53/53/13668保持，第三遍0。这是冻结包53资产，不是全Git仓库或三遍/全功能完成。每轮Go原40主测/含子测56、旧10、上批13、新12（10保护/2观察），合计75主测/91含子测×3通过；CPU旧372×3通过，无新Python测试；失败/错误/跳过0，通过集合无race warning。独立F02每轮预期非零/DATA RACE，不混入通过数，未修。三轮副本vet通过。F29原guard/decodeJSON/validateSpeak接受孤立高低代理项或非法UTF8，解码成a�b后返回200；实际本地HTTP组合校验handler，非完整合成或认证绕过。F30原授权speak/LLM错误链将HTTP401替身正文回显的配置假密钥带入ERROR/END/metrics；密钥/供应商均synthetic，非真实泄密事件或未授权读取。两项未修。LICENSE全文阅读不等于依赖/模型/数据/NOTICE法律签收；MEMO step15/xvector/maxgain12漂移仍为D01，冻结不改。Node30/JS/产品与新审计Python AST/repack/Go探针gofmt通过；686历史SHA、53源/94冻结/15正式、300初审及Q25–27各50保持。Go沿用、freeze与DSP相同，无新依赖；无Rust/Torch/Qwen/完整模型/真实GPU/训练/声学/提速签收。本批未重跑独立CLI/NumPy与trimmer探针/ASGI2.3/浏览器与Player VM，不挪用旧成绩。完整交接80份；当前g0-pass2-security-coverage.json、verify_pass2_security.py与progress-pass2-security.json。产品未改/18未发；下一步第三遍全源跨层输入/pin/错误、生命周期/取消/播放/训练绑定审查及300最终映射，G0仍PARTIAL/BLOCKED，不跳S1/Q28，不要求Continue。


## G0全源第三遍第1批：输入与内容绑定（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS3_INPUT.md`。main478/security247/session692/qtts_common211/voice_binding60/resource_limits172/access_control70重新全文7份1930行，第三遍7/53、剩46份11738行；第一、第二遍各53/53/13668保持。browser和library_api只局部调用点不计第三遍。新增Go6（5保护/1观察）及Python6（5保护/1观察），预检各6通过；每轮Go81主测/97含子测×3、CPU378（旧372+新6）×3通过，失败/错误/跳过0，通过集合无race warning；独立F02三轮预期非零/DATA RACE不计通过，三轮副本vet通过。实际Go/Python8合法pin与12非法generation向量、两worker ack期间generation变更拒绝、空/错text拒绝、内容pin非身份、上传预算+1、spool清理、原子JSON失败、参考增长拒绝、两认证进程一致性均有明确边界。F31同磁盘top_k:null被Go转0并得pin而Python拒绝；F32认证token FIFO无writer时open先于fstat阻塞，普通文件control通过，外部定向终止并reap自有子进程；两项未修，无真实凭据/模型/错误音色或远程利用证明。原8条建议仅部分证据映射，300与Q25–27各50不改/不签收。739历史SHA、53源/94冻结/15正式保持；Node30/JS/AST/repack/gofmt/vet通过，freeze与第二遍收尾相同，无新依赖。旧S2 F29/F30随套件重跑仍未修；本批未跑浏览器/VM/独立CLI/ASGI2.3/分块裁剪探针，不挪用历史成绩。完整交接81份；当前g0-pass3-input-coverage.json、verify_pass3_input.py及progress-pass3-input.json。产品未改/18未发；无Rust/Torch/Qwen/实际训练/双T4/声学/提速签收。下一批第三遍参考分析/API/档案修改与备份事务，继续剩46份及300最终映射；G0仍PARTIAL/BLOCKED，不跳S1/Q28，不要求Continue。


## G0全源第三遍第2批：参考与档案事务（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS3_REFERENCE.md`。analyst1211/library_api163/persist99/reference_segments106/voice_library351第三遍完整5份1930行，累计12/53、3860行、剩41份9808行；前两遍各53/53/13668保持。新12（10保护/2观察）预检通过，CPU390（旧378+新12）×3全部通过，失败/错误/跳过0。F33真实两CPU线程占满原HEAVY，原text/candidate ASGI先写盘改pin再429，不reload且不报reference_saved；F34原校准评估旧转写，在结束提交前实际text ASGI改pin仍200，随后calibrate保存旧评分到新档案仍200；临时目录/线程/槽清理核对。模型/ASR/speaker/worker ack为fixtures，无真实音质/错误音色证明，两项未修。复制失败旧pin保护、JSON失败仍遗留孤立anchor明确不称全回滚；trained三入口409、原库snapshot异常/顺序/只读与租约、稳定pack/extract字节pin、归档末尾非法成员先拒绝、DELETE重复revision、24秒可信词切分保护通过。原300本批10条部分链接、与前批去重16个ID，均未最终签收；原文/Q25–27各50保持。795历史SHA、53源/94冻结/15正式保持，Node30/JS/AST/repack通过，freeze与前批相同无新依赖。本批未跑Go/F31/独立F02/浏览器VM/独立ASGI2.3/CLI/分块裁剪探针，不挪用历史成绩。交接82份；当前g0-pass3-reference-coverage.json、verify_pass3_reference.py及progress-pass3-reference.json。产品未改/18未发；无Rust/Torch/Qwen/实际训练/双T4/声学/提速签收。下一批第三遍训练输入/码/训练产物绑定与取消/提交，继续余41份及300最终映射；G0仍PARTIAL/BLOCKED，不跳S1/Q28，不要求Continue。


## G0全源第三遍第3批：训练来源与产物提交（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS3_TRAINING.md`。training_data285/training_codes355/training_job227/tts_training200/tts_dataset125/trained_profiles155/encode_training128/trained_voice30全文8份1505行，第三遍累计20/53、5365行、剩33份8303行；前两遍各53/53/13668保持。首组源码输出截断后完整补读。首次测试43项因导入TestCase重复31项，1失败为误判正常.lock；改模块导入与断言，保留首错/说明，预检新12通过。初行数误算1605被信用断言拦住未写错误coverage，逐项纠正1505/5365/8303并留记录。CPU402（旧390+新12，新11保护/1观察）×3全部通过，失败/错误/跳过0。F35原控制器在两个真实CPU替身rank0退出且adapter仅含manifest.json={}时仍completed/optimizer_execution_observed=true，原TrainedArtifacts.inspect409拒绝，信号/租约恢复；训练准入/依赖/tokenizer门禁与rank实现明确替身，原GPU/code OFD adopt实际执行，无Torch/优化器/训练/非法声音发布或正常rank产生坏检查点证明。F35未修，F01–34/D01保留。新保护包括输入BaseException回滚、PCM极值36001帧、codes最终取消、encoder第二样本中断、finish-only pin、adopt最后OFD、cancelled产物拒绝、来源/NaN拒绝、发布末次重核/固定参考文本/active不变及新trained_voice CLI错pin脱敏拒绝；发布codes lease元数据/adapter为fixtures，不能签收真实训练。原300本批7部分链接，与前两批去重22ID，均未最终签收；Q25–27各50保持。825历史SHA、53源/94冻结/15正式保持；Node30/JS/AST38/repack通过，freeze与上批相同无新增依赖。本批未跑Go/F31/独立F02/浏览器VM/独立ASGI2.3/额外四CLI/分块裁剪矩阵，不挪用历史成绩。交接83份；当前g0-pass3-training-coverage.json、verify_pass3_training.py及progress-pass3-training.json。产品未改/18未发，无Rust/Torch/Qwen/实际训练/双T4/声学/提速签收。下一批第三遍adapter/推理/provider兼容与缓存/失败取消，继续余33份及300最终映射，G0仍PARTIAL/BLOCKED，不跳S1/Q28、不要求Continue。


## G0全源第三遍第4批：推理与生成资源清理（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS3_INFERENCE.md`。adapter_engine108/lora_adapter91/qwen_compat97/clone_stream126/gpu_ownership151/worker680/train_tts49重新全文7份1302行，无源输出截断，worker连续四段；第三遍累计27/53、6667行、剩26份7001行；前两遍各53/53/13668保持。新增12（11保护/1观察）预检一次通过；CPU414（旧402+新12）×3全部通过，失败/错误/跳过0。F36原generated_only_stream在consumer关闭已启动生成器时，上游close替身抛异常，后续window.finish被跳过；生成器frame本身关闭，测试捕获的真实window仍closed false/pending1920/合成code标记，最后显式清理完成。准备/predictor/decoder/Torch上下文均控制替身、无tensor模拟，没有证明生产上游会抛错或正常GC后持续GPU内存泄漏/沙沙根因，F36未修。adapter来源不符先拒绝、cached仍核验实际safetensors字节、取消前不选择与取消后丢弃返回PCM、native rate/shape/NaN/长度拒绝与单句输出、回放指标合计、worker部分生成失败解锁/后续成功、同pin缺prompt重载、RoPE重试cause/注册表、真实短pwrite释放OFD均保护通过；LoRA prepare/commit和native模型未执行。F01–35/D01保留，旧ASGI/CLI/信号/CPU持有者见证随集合重跑，不代表真实模型。原300本批7部分链接，累计去重27ID，均未最终签收；Q25–27各50保持。858历史SHA、53源/94冻结/15正式保持；Node30/JS/AST38/repack通过，freeze与上批相同无新依赖。未跑Go/F31/独立F02/浏览器VM/独立ASGI2.3/额外四CLI/分块裁剪矩阵，不挪用历史成绩。完整交接84份；当前g0-pass3-inference-coverage.json、verify_pass3_inference.py及progress-pass3-inference.json。产品未改/18未发，无Rust/Torch/Qwen/实际训练/双T4/声学/提速签收。下一批第三遍启动监督/preflight/资源测量工具与DSP接口，继续余26份及300最终映射，G0仍PARTIAL/BLOCKED，不跳S1/Q28、不要求Continue。

## 第三遍第5批：启动监督、工具与DSP接口

报告 `docs/KAGGLE_STEP18_G0_PASS3_STARTUP.md`。11份2253行全文复读；累计38/53、8920行，剩15份4748行。CPU426（旧414+新12，10保护/2观察）×3全部通过，失败/错误/跳过0；另NumPy分块12、trimmer8、实际CLI4各三轮，CLI中3项每轮期望blocked而非模型成功。首预检12项中1 error为测试误访问UploadRejected.status，纠正为code后12通过，首错/修正留档。F37原preflight父控制器接受真实CPU替身child exit23写出的合法形状成功回执；生产者明确替身，不证明实际GPU误通过。F38已有系统cc编译仅rt_version的C共享库，真实ctypes在ABI3缺rt_leveler_new抛AttributeError中止import，ABI2及显式NO_RUST为NumPy；不是Rust编译/运行或正式Rust库损坏证明。两项未修，产品不改。887历史SHA、53源/94冻结/15正式保持；原300本批7部分链接、累计33unique，Q25–27各50不变，最终处置仍false。Node30/JS/AST38/repack新执行；无新Python/系统依赖，freeze不变。未跑Go/race/vet/浏览器VM/独立ASGI2.3，未跑Torch/Qwen/实际训练/双T4/声学或提速。交接85份；最新coverage/verifier/progress为pass3-startup。继续余Go10/web3/LICENSE/MEMO及300最终映射，G0与整体PARTIAL/BLOCKED，不跳S1/Q28/18发布，不要求Continue。

## 第三遍第6批：网关调度、LLM流与文本保留

报告 `docs/KAGGLE_STEP18_G0_PASS3_GATEWAY.md`。剩余Go10资产2110行全文复读，累计48/53、11030行，剩5份2638行（web3份2217/LICENSE201/MEMO220）；前两遍各53/13668保持。新增Go12（10保护/2观察）race预检通过，首编译错因测试误用submitted，已改为真实字段allSubmitted、首错留档；另一次审计元数据括号SyntaxError解析前阻止全部写入，拆开后纠正留档。Go原40+G0十+P2十三+security十二+input六+新十二＝93顶层/109含子测试×3正常通过，意外fail/skip/race0；独立F02 race×3预期非零、仍未修，vet×3通过。CPU完整继承426×3＝1278 PASS，failure/error/skip0，无本批新增Python合同；另NumPy分块12/trimmer8/实际CLI4各三轮，3项CLI每轮期望blocked非GPU成功。F39原Live PreserveText把你好。!?重连成你好。及丢独立空白/标点尾段，非语词漏读或沙沙根因证明；F40原run在活ctx下接受替身cancelled=true stats＋偶数PCM，served1/failed0，非真实生产取消或GPU漏音证明。两项未修；F01–38/D01保持。chat system/history/预算、SSE CRLF/末行无换行/流内错误脱敏、正常read Unicode保字/seed、retry上限、urgency/FIFO、EMA与chunk2/6/pin转发保护通过，非200正文F30仍在。953历史SHA、53源/94冻结/15正式保持；原300本批7部分链接、累计38unique，Q25–27各50/最终处置不变。Node30/JS/AST38/gofmt/repack新执行，无新Python/系统依赖、freeze不变；CPU继承C ABI故障注入不冒称Rust，无Rust/Torch/Qwen/CUDA/真训练/双T4/声学/提速。本批未跑真实浏览器/VM/独立ASGI2.3，不挪用历史成绩。交接86份，最新pass3-gateway coverage/verifier/progress。产品未改/18未发，下一批web完整阅读与实浏览器、另许可/MEMO及300最终映射；G0与整体PARTIAL/BLOCKED，不跳S1/Q28，不要求Continue。

## 第三遍第7批：web、录音与播放／界面状态

报告 `docs/KAGGLE_STEP18_G0_PASS3_FRONTEND.md`。app1715/index144/recorder358完整复读3份2217行，第三遍累计51/53、13247行，剩LICENSE201/MEMO220共2份421行；前两遍各53/13668保持。浏览器158（原146+新12，10保护/2观察）×3＝474 PASS，失败/flaky/skip/retry0；CPU完整继承426×3＝1278 PASS、failure/error/skip0，无新Python合同；另VM22/16、NumPy分块12/trimmer8/实际CLI4各三轮，三CLI每轮期望blocked不是模型成功。F41停止已abort且hold/reset，注入迟到fixture Worklet st使原player发play/UI playing，不证明真实原生Worklet竞态/物理漏音；F42同accessEpoch、候选mutation0→1、合成profiles响应1→0，使原UI高亮从1回0，不证明实际backend回滚或错声音。两项均未修，旧F01–40/D01保持，每轮保留F04/05/06/25/26观察。新保护含resume中取消、精确File字节/边界、start抛错/权限迟拒绝、policy帧、401锁定、超长帧头、正常完成排空、三份冻结web完整文本原生clipboard且不额外save、最近六完整chat回合；继承真实振荡器/静音录音与完整17包复制/权限回退。浏览器API为fixture，临时E2E workbench不是正式HEAD。首预检11/1为旧recorder-only壳缺charset导致中文乱码，仅新审计壳UTF-8重载后12通过，原断言/旧fixture/产品不改，首错留档。1051历史SHA、53源/94冻结/15正式保持；原300本批7部分链接、累计45unique，Q25–27各50/最终处置false不变。Node30/JS/AST38/repack新执行，freeze/lock不变，无新Python/系统依赖或npm重装；C ABI故障fixture非Rust。本批未跑Go/race/vet/独立ASGI2.3，不挪用历史结果。交接87份，当前pass3-frontend coverage/verifier/progress。产品未改/18未发，物理麦克风/扬声器/真DeepSeek/模型/实际训练/双T4/声学/提速未验。下一步剩2份第三遍及原300最终映射；G0与整体PARTIAL/BLOCKED，不跳S1/Q28，无需Continue。

## 第三遍第8批：许可／MEMO收尾与原300缺口矩阵

报告 `docs/KAGGLE_STEP18_G0_PASS3_CLOSURE.md`。LICENSE201/MEMO220全文复读2份421行，三遍各53/53、13668行，剩0；只关闭53内嵌资产源码阅读子项，不是整个Git仓库或零缺陷验收。原300逐项复核并生成完整gap矩阵，原分类23限定缺陷建议/96保留/89文档合同/55真实条件阻塞/37待证保持；三遍7个链接文件53条记录去重45项，255无该组专用链接不等于无历史证据，最终签收0/300，逐条下一动作／来源／计划合同与边界保存。D01历史MEMO step15/xvector/12dB与冻结17默认ICL/6dB漂移不改；本批AST实际调用原conditioning和output_max_gain_db默认／显式／拒绝路径，不是模型或音量测量。D02新增证据可用性缺口：1139期待历史文件中1136可读SHA匹配、变更0，3份旧.log缺失且匹配*.log忽略规则，预期SHA保留、内容不补造、full_historical_integrity_passed=false。冻结53源/94文件/15正式与HEAD仍保持。旧.venv/node_modules/Go/Rust当前不存在，先期环境／严格历史检查错误留档，改用系统Python标准库、无依赖安装。新12收尾审计合同×3＝36 PASS、Node30×3＝90 PASS，无失败/错误/跳过；JS/repack/AST38各三轮通过。旧158×3浏览器原始JSON只重新解析／核SHA，不是本批重跑；未跑CPU426/Chromium/Go/race/vet/模型/训练/双T4/物理音频／声学／性能，无功能修复、无18包；LICENSE/NOTICE/依赖模型及声音授权未签收。交接88份，当前pass3-closure coverage/verifier/progress。下一步原300逐条最终审查处置及精确测试映射、D02从可信来源找回或有环境后另存新执行收据。G0与整体仍PARTIAL/BLOCKED，不跳S1/Q28，直接继续无需Continue。

## G0第9批：300处置说明与限定失败观察绑定

报告 `docs/KAGGLE_STEP18_G0_DISPOSITION_REVIEW.md`（附录完整300条原建议及逐条说明）。原3轮100项分别补写行动／边界，review_disposition_recorded300/300；原分类23限定修复/96保留/89文档合同/55真条件阻塞/37先调查不变，原final_disposition/test/fix与新functional_acceptance全false，功能及最终签收仍0/300，说明归档不等于G0完成。23原限定缺陷建议手工绑定历史3轮69个JSON Pointer观察（有重复、不算新实验或23新bug），收据／源码／当前相关probe SHA及历史身份是否有记录分别保存；R1-016只相关校准文本交错，NaN未在旧payload，DSP早期未记probe_sha不补造。原45部分链接与23绑定交集3、并集65，235未进入这两组不等于无其他证据。53内嵌资产三遍各13668行保持。D02按3预期SHA搜索当前仓库非.git且<=2MB文件并查git log --all，无同SHA或当前可用提交，未查远端／仓库外；1183历史期待项中1180可读SHA匹配、变更0、3旧.log仍缺，全历史完整性false，不拿新日志充旧字节。新24审计（继承收尾12+新增12）×3＝72 PASS、Node30×3＝90 PASS，JS/repack/AST39各3轮通过，新预检12首次通过，无失败/错误/跳过。系统Python标准库，未装依赖／未重建环境；历史失败仅重读，未跑CPU426/Chromium/Go race/vet/Rust/模型/训练/双T4/物理音频／声学／性能。产品未改，94冻结/15正式及HEAD保持；交接89份，当前g0-disposition-review.json、disposition-failure-bindings.json、verify_disposition.py与progress-disposition.json。下一步按S1非法/缺省/NaN真实HTTP等合同精确映射，补相关而不完整的并发见证，D02从可信源恢复或另存新执行收据。G0与整体PARTIAL/BLOCKED，不跳S1/Q28或18发布，保留全部用户未豁免要求，直接继续无需Continue。

## G0第10批：真实TCP的S1输入边界与CPU继承

报告 `docs/KAGGLE_STEP18_G0_INPUT_HTTP.md`。新Uvicorn原analyst.app+httpx走真实127.0.0.1临时TCP，不是TestClient/AST；生命周期off、worker ACK及合成profile明确fixture，不是Go鉴权或模型。CPU438（原426+新12，7保护/5未修观察组）×3＝1314 PASS，failure/error/skip0；原426逐ID/结果及16旧观察完全继承，新5组后观察21。每轮61请求、合计183；各轮200×19/500×16/400×16/422×6/404×1/409×3，500为未修见证非功能成功。I01 bool/float/string强转；I02容器/非法串/NaN/±Infinity/1e309及顶层非有限500；I03缺省0/重复键最后/未知忽略；I04非字符串转写str化、surrogate500但原文件保留；I05损坏candidates与预装父路径/符号链接file接受，所有字节在自有临时树，不证明公开远程任意文件读取／模型接受。合法候选字节/转写/pin、合法Unicode、越界/缺档、有限非对象422、trained三入口409、library严格JSON400、HEAVY槽恢复保护。新12预检首次通过，探索原JSON保存；检查脚本误用id字段（实际test）的KeyError留档，测试/产品未改、三轮非失败。另NumPy12/trimmer8/实际CLI4各三轮，三CLI期望blocked/resource gpu_verified=false；24审计/Node30/JS/repack/AST39各三轮通过。重建忽略venv并装历史固定Python依赖，freeze精确旧记录去掉故意未装go-bin；NumPy2.2.6非requirements2.4.6，无Go/Rust/npm/Torch/Qwen/模型安装；C ABI fixture非Rust。本批新12建议精确testID/三轮case下标+SHA部分链接，有限证据并集70、230未入这些集合不等于无其他证据，原300/3×100处置/Q25–27各50保持，最终/功能签收0。53资产三遍13668行/94冻结/15正式不动；历史1228期待1225匹配/变更0/3旧.log D02仍缺，不以新日志冒旧内容。无浏览器/Go race/vet/真实模型/训练/双T4/实体音频/声学性能验证，产品未改/18未发。完整交接90份，当前input-http links/verify_input_http.py/progress-input-http.json。G0与整体PARTIAL/BLOCKED，不跳S1/Q28；后续版本冲突与候选/文本/校准组合及剩余逐条映射，不承诺一定成功，直接继续无需Continue。


## G0第11批：版本／校准真实TCP组合（未实施产品优化）

新增12项=8保护/4未修观察，单Uvicorn事件循环真实HTTP、HEAVY线程Event控制交错，原reload/calibrate实际执行，worker/ASR/speaker/synth为替身。首次预检12PASS；CPU450×3PASS、failure/error/skip0，旧438逐ID/结果继承；每轮85TCP、三轮255，其中新增24/轮共72。普通候选/文本重叠旧reload有pin503保护；校准旧评分仍可在真实HTTP编辑之后200保存（新转写未被覆盖）。另满额429前写盘、同名候选bytes变更后未重评、自有profile真实DELETE后校准500而未复活。文件变更非HTTP上传，非声学/实际错声音证明。新12原建议部分链接令并集75/300=25%，仅限定证据覆盖，最终/功能签收0/300。1317历史期待/1314匹配/3旧.log缺失；产品53源/94冻结/15正式保持。复用venv无安装，完整交接91份。附加审计与独立核验以version-http-checks-roundN.json和progress-version-http.json为准；报告KAGGLE_STEP18_G0_VERSION_HTTP.md。G0/整体PARTIAL/BLOCKED，不跳S1/Q28/发布；声音优化未实施，真实模型/双T4/训练/声学/提速未验收。


## S1隔离候选实际实现（问题28流程调整）

不再只增加观察。问题28已独立按四选项、选C及50行动完成，见KAGGLE_STEP18_Q28_S1_CANDIDATE.md；原25–27文件不改、29未开。前置门禁调整为：允许隔离候选修复，不允许未验收候选进入冻结包、默认正式服务／工作台或发布。G0整体仍PARTIAL/BLOCKED，真实模型／硬件门禁未豁免。

新增kaggle/step18的实际候选分析源码，依赖冻结17其余模块；只改候选／文本／删除入口及提交辅助代码，其余命名定义AST相同。实现严格JSON/类型/Unicode、HEAVY先准入后写盘、内容地址锚点和提交失败保旧、短提交锁与删除协调；校准仍原实现不算修复。默认17包与正式HEAD、53源/94冻结/15正式保持。

最终相同28合同，旧版43失败记录/2明确skip/0error，候选28预检全PASS。完整478（旧450冻结对照+新28候选合同）×3PASS，失败／错误／跳过0；每轮159 TCP、三轮477，新候选74/轮共222。15条原建议新限定实现证据加强原75并集，未虚增覆盖，原300最终／功能签收仍0。三轮附加检查与独立封存以s1-candidate-checks-roundN.json及progress-s1-candidate.json为准，完整交接93份。无真实模型／训练／双T4／声音质量／提速验收，18未发布；下一步仅S2校准快照与冲突修复，不能把当前成果称已消沙沙或首声更快。


## S2-A校准快照实际实现

在隔离18候选中实现完整输入捕获、仅用捕获字节评估、提交前同短锁核验；真实HTTP编辑／ABA、候选同名bytes／质心／参数变化、删除／trained变化后409且不应用旧评分。S1变更写修订nonce，相同选择幂等；同档案第二次校准409，临时ID独立且长度安全，自有临时目录与ASR释放finally。最多24候选、64MiB聚合文件，非总内存预算／跨进程事务。改前S1及活跃交接已归档s2-before/index；冻结17不动。新增22合同对改前S1为21失败记录/0error/0skip，候选预检22全PASS。三轮500（450冻结控制+当前候选上S1旧28+新22）及附加检查以progress-s2.json为准，完整交接94份。原300建议最终／功能未全签，证据比例非整体进度。缺失CER默认值、全失败chosen0、非有限／覆盖率评分、最终worker回执等留待S2-B，不提前签完整S2，不跳真实模型／双T4／声学或发布门禁。问题29未开，原三轮100及问题25–28记录保留。


## S2-B有效指标与加载就绪实际实现

Q29选C及50行动先完成，未开30。逐目标缺失null、覆盖率／有限可靠指标门禁，不再默认CER0.05或全失败chosen0。无候选422不写盘保旧，其他完整候选可选；临时worker核验状态和pin，选择保存后最终加载失败503/savedtrue/readyfalse，后改／删版本明确标不当前，不虚构回滚。成功保留磁盘选择报告一致及quality_verified=false；后台可选校准摘要已接入但未完整运行真实创建。S1/S2-A旧方法断言不改。

最终23合同对S2-A为36失败记录（含子用例、非36bug），候选预检PASS。初三轮523通过后复核修正整数PCM abs最小值溢出并补子用例，最终另命名三轮以s2b-final和progress-s2b.json为准，不混算初轮；初源码逆变换重建明确按记录SHA核验、非事前快照，原错日志均保留。旧500加新23，旧450冻结控制／旧50当前候选／新23当前候选，附加检查和封存以实际收据为准。完整交接96份，17／53源／94冻结／15正式不变，18未发布。真实短音、质量、双T4／训练／性能及全局事务仍未签；下一步隔离候选S3分块一致性，不跳声学门禁。

本批12条当前实现限定链接令证据并集81/300（27%仅证据覆盖），不是整体完成率；最终／功能签收仍0。


## S3因果 NumPy DSP 与隔离worker实际接入

Q30四选项选C、50行动和三遍各100专题建议已先归档。新增 step18_audio_rt.py 与隔离 worker.py，唯一模块名接入真实 run_job；所有 worker 命名定义AST保留。固定 RMS 余数、逐样本因果平滑、绝对位置淡入、明确flush/关闭/配置合同；没有PCM整窗缓冲，没有参考PCM拼接。候选只启用 numpy-causal-v1，不装载未测Rust；冻结17/正式工作台不动。旧版30合同44失败记录、候选30 PASS；完整562×3全部PASS，含旧523逐ID/结果保留；14分块矩阵×3差0，601秒合成流×3状态有界和计数通过，CPU实测有短块加速也有大块开销，不是模型RTF或声学提速证明。附加24审计/Node30/AST53等最终结果与两次封存以 progress-s3.json 为准。新venv确实重建、freeze与旧版相同；1768保护/1765匹配/3旧日志缺失仍保留；完整交接101份、18未发布。完整S3含Rust/模型/声学仍未签收。下一步S4裁剪有界状态，不能把DSP样本数守恒当整个原trimmer链已无丢样本；不需要Continue。


## S4有界裁剪与worker结束实际修复

Q31选C及50行动、三遍100建议先写。新增step18_trimmer.py固定120网格残帧/跨块35ms前史/有界尾队列/finish；正常finish保留缓存非零尾，精确零裁掉计数；取消/异常清缓存不排尾；中段静音超限输出不删。新增worker_s4.py实际接入，只更换裁剪器和Worker.run_job，原S3 worker/DSP及旧合同完整保留。30旧版红42失败记录/0error/skip，初41失败+1OverflowError已保留并转明确合同失败；候选30/worker10预检通过。完整602×3全部PASS，旧562逐ID/结果保留；21分块矩阵×3对独立参考逐样本相等，601秒合成流×3达到并守住43200样本尾预算。裁剪CPU约1.10秒/601秒合成音频，正确性有开销不声称提速/模型RTF/首声改善。最终审计24/Node30/AST57及两次封存见progress-s4.json。无新依赖，1905保护/1902匹配/3旧日志仍缺，完整交接106份，17/正式工作台不改、18未发。领先低电平仍可裁，非零尾不是无噪声证明；真实用户音频/双T4/训练/声学及完整S3 native仍未签。下一步S5完成短尾排空，直接继续无需Continue。


## S5完成短尾／重采样／epoch实际修复

Q32选C＋50行动、三遍100建议先归档。新增完整web/app.js，仅改Player及嵌入Worklet，网络解析/预测器/UI后缀逐字节保持；真实完整页面使用新Player。完成任何正pending可play，未完成风险阈值保留；按post−played−dropped计账并等当前epoch endACK，不以旧fill0假装结束。全局整数坐标重采样，正常末样本保持到ceil预算、取消不flush；epoch拒绝旧状态与stop后复活。37VM红28失败/9保留，候选预检37和8源码及15原生浏览器通过。最终610CPU（旧602保留）/37VM/173Chromium（旧158＋新15，含3完整UI原生链）三轮及24审计/Node30/AST58与两次封存见progress-s5.json；不混算重叠VM。实体扬声器与模型声音未验收，firstPlayedMs仍play命令时间。Python沿用无安装，npm ci确实按旧lock安装浏览器依赖，lock/config不改；2049保护/2046匹配/3旧日志缺，完整交接111份，17/正式工作台/S3S4不改、18未发布。下一步S6时序与诊断，真实T4/训练/声学/RTF和完整S3 native仍未签，不要求Continue。

---

## 内嵌备忘录：KAGGLE_STEP18_REVIEW1.md

# 第十八阶段第一轮：参考条件、首声和噪声链路的100条建议

状态：关键路径首轮专题审查；不是全部代码已逐行完成三轮语义审查。产品未修改。建议是后续验证/实现清单，不是100个已证实缺陷。

事实：当前生成使用单个选中锚点；候选参与评分/质心，校准是逐候选试验再择一。播放firstPlayedMs当前是主线程play命令时刻。NumPy/Rust DSP存在需实际验证的分块状态差异。

## 候选真实语义
源码位置：`py/analyst.py:build_profile / calibrate_profile; py/worker.py:FasterEngine.stream`。

1. [S18-R1-001] 将候选参与质心统计与实际ICL锚点分开显示，避免全部片段已融合的误解。
2. [S18-R1-002] 在合成收据记录选中的anchor_candidate，而不是只显示profile ID。
3. [S18-R1-003] 记录实际锚点字节指纹与对应转写指纹；日志不明文写入私有转写。
4. [S18-R1-004] 用不同内容的三个候选验证只选中的音频进入提示提取。
5. [S18-R1-005] 审核“候选校准”文案明确逐个试验后选一个，不称多参考融合。
6. [S18-R1-006] 查验Faster真实接口的多参考能力，未支持时不伪造列表参数。
7. [S18-R1-007] 禁止把三个片段PCM拼成一个提示并配不连续全文。
8. [S18-R1-008] 跨候选声纹中心仅作评分依据，不声称它已替代模型speaker embedding。
9. [S18-R1-009] 为单个合法候选保留最短建档链路，不强迫三候选。
10. [S18-R1-010] 给未来多候选策略保留显式模式与回退边界，不静默改变17默认。

## 候选切换与并发
源码位置：`py/analyst.py:set_candidate; py/worker.py:_load_profile_locked; py/voice_binding.py`。

11. [S18-R1-011] 非法index的布尔、小数、对象与缺省语义分别测试，避免int强转误选或500。
12. [S18-R1-012] 核查切换候选与校准并发时磁盘写入、工作者加载是否形成一致事务。
13. [S18-R1-013] 候选文件复制失败时保留旧profile JSON，不留下半更新锚点。
14. [S18-R1-014] 双卡仅一张加载成功时明确部分失败，不宣称启用完成。
15. [S18-R1-015] 旧会话遇新指纹必须继续拒播，不能热切后拼混音色。
16. [S18-R1-016] 转写编辑与候选选择同时发生时绑定同一版本，防止音文错配。
17. [S18-R1-017] 校准临时profile的anchor_candidate元数据应指向实际试验候选，不能误标0。
18. [S18-R1-018] 候选变更后清理或替换提示快照时保留锁内核验。
19. [S18-R1-019] 为重复点击候选与取消任务增加幂等与状态测试。
20. [S18-R1-020] 训练adapter的固定参考限制保持，不让候选切换绕过来源绑定。

## 首声定义与时钟
源码位置：`py/worker.py:Worker.synth; go/gateway/session.go; web/app.js:tick`。

21. [S18-R1-021] 分别记录请求、首个可用文本、排队、预填充、首PCM、首播放命令。
22. [S18-R1-022] worker t_start在加载提示之后，单独计量冷提示加载而不漏记等待。
23. [S18-R1-023] queue_ms当前覆盖锁等待等前置耗时，拆项后保留旧字段兼容。
24. [S18-R1-024] 浏览器firstPlayedMs当前在发play命令处赋值，标明不是硬件实际出声。
25. [S18-R1-025] 评估AudioWorklet消费首个语音样本的确认消息，区分主线程命令延迟。
26. [S18-R1-026] 跨Python、Go与浏览器仅使用各自单调时间差，不能直接减不同纪元。
27. [S18-R1-027] 显式静音停顿不能计为首个可用人声，保留禁止原音占位。
28. [S18-R1-028] 首包平均之外记录p50/p95与冷暖状态，不用一次幸运值。
29. [S18-R1-029] 将文本长度、参考长度、chunk_size和设备条件写入性能收据。
30. [S18-R1-030] 首声提速必须同时检查缺字与最终音频完整性，不能裁掉开头。

## 浏览器启动缓冲
源码位置：`web/app.js:needToStart / onWorklet / QttsRing`。

31. [S18-R1-031] 对当前0.7秒下限和初始2秒策略建立确定性到达轨迹对照。
32. [S18-R1-032] 分别测试高速稳定、慢速持续、突发包与长网络抖动。
33. [S18-R1-033] 初次启动与欠载恢复分别设计目标，不统一缩到最小。
34. [S18-R1-034] 将预测器无速率样本时的保守回退纳入首次播放测试。
35. [S18-R1-035] 测量AudioWorklet统计消息的刷新间隔对主线程启动判断的影响。
36. [S18-R1-036] 在44.1k及48k上下文验证重采样后的fill计秒正确。
37. [S18-R1-037] 短于启动阈值但已完成的真实语音应及时播放，不等待不可达缓冲。
38. [S18-R1-038] 后台页、暂停恢复、锁定与取消后不得发送迟到play。
39. [S18-R1-039] 记录ring dropped样本；任何丢样不能只显示播放成功。
40. [S18-R1-040] 低延迟策略只能在欠载预算内启用，不能把断续当自然阅读。

## 模型与调度热路径
源码位置：`py/worker.py:FasterEngine; py/clone_stream.py:generated_only_stream; go/gateway/scheduler.go`。

41. [S18-R1-041] 对2/4/8/16帧首块大小做同文本同seed对照，测TTFA及总RTF。
42. [S18-R1-042] 小首块与稳态大块若需不同大小，先确认真实生成器支持，禁止无效传参。
43. [S18-R1-043] 检查decode迭代器首次next含有的预填充时间，不能只测创建生成器。
44. [S18-R1-044] 单独计量token生成、codec解码及CPU拷贝，避免归因全部GPU。
45. [S18-R1-045] 提示快照重用必须与内容指纹一致，不退回仅按路径缓存。
46. [S18-R1-046] 不为首声把ICL换成向量默认，保留相似度条件。
47. [S18-R1-047] 比较首段优先调度与后续并行的队头阻塞，不无证据锁死单卡。
48. [S18-R1-048] 确认Live聊天第一可用前缀触发不被朗读聚合配置覆盖。
49. [S18-R1-049] 保留最大生成token与取消限制，不能为速度删掉输出。
50. [S18-R1-050] 不默认每卡双模型增加显存；只有目标T4实测才接受吞吐结论。

## 输入噪声与参考处理
源码位置：`py/analyst.py:build_profile / denoise / normalize_speech`。

51. [S18-R1-051] 原始RMS约-47.7只作为风险，不推断具体麦克风故障。
52. [S18-R1-052] 分别记录归一化前后语音电平与峰值，注明增益上限14dB。
53. [S18-R1-053] 候选SNR是估计量，不能把17dB阈值当真实噪声声压。
54. [S18-R1-054] 保留raw、strength0.85、strength0.55对照的处理收据。
55. [S18-R1-055] 审查声纹相似0.94与SNR增益2dB门禁是否会误接收失真，不能只看单分数。
56. [S18-R1-056] 验证全零、强直流、很轻语音及背景声输入的处理决策。
57. [S18-R1-057] 对齿音、气声、摩擦音单独测保真，不能以削高频冒无沙沙。
58. [S18-R1-058] 不在用户未授权时保存或上传原始私有WAV作为公共证据。
59. [S18-R1-059] 已存在非平稳降噪不等于生成输出已降噪，明确处理发生阶段。
60. [S18-R1-060] 录音时扬声器回录网页朗读的可能性仅列假设，不能由截图定论。

## 生成输出噪声定位
源码位置：`py/worker.py:Worker.synth; py/clone_stream.py:GeneratedCodecWindow`。

61. [S18-R1-061] 建立模型PCM、后处理PCM、浏览器录回的分层局部诊断，默认关闭私有采集。
62. [S18-R1-062] 将codec窗口起点与边界脉冲位置关联，区分底噪和接缝爆音。
63. [S18-R1-063] 对持续人声与停顿分别计算频谱，但无清洁真值时不称绝对SNR。
64. [S18-R1-064] 继续验证codec只收到生成码，不能回到参考码前缀解码。
65. [S18-R1-065] 真实预训练codec与随机tiny codec的质量证据必须分列。
66. [S18-R1-066] 非有限模型输出当前替换为零，应评估失败拒播而非掩盖异常的策略。
67. [S18-R1-067] 增益提升可能抬噪，记录处理前后噪声地板变化而不自动强门限。
68. [S18-R1-068] 不能用输出全静音或静音段删除作为零噪声验收。
69. [S18-R1-069] 保留模型自然人声呼吸与禁止添加噪声的区别，不自动切除语音气息。
70. [S18-R1-070] 用户全程纯人声目标需真实WAV试听和添字检查，代码指标不替代。

## DSP状态与后端一致
源码位置：`py/audio_rt.py:Leveler; rust/audio_rt/src/lib.rs:Leveler`。

71. [S18-R1-071] 实测同一信号整块与任意分块处理的样本一致性。
72. [S18-R1-072] 重点验证NumPy不足96样本首块时淡入是否在下一块重新从零开始。
73. [S18-R1-073] 核查NumPy按输入块丢弃不足240样本RMS余数与Rust跨块累积差别。
74. [S18-R1-074] 比较Rust逐样本增益平滑与NumPy逐块插值，不能宣称严格等价。
75. [S18-R1-075] 保持输出样本数与输入相等，不能为降噪补偿无记录延迟。
76. [S18-R1-076] 分别测试DC blocker状态、零输入残留与长静音后重新讲话。
77. [S18-R1-077] 测试max_gain_db=0隔离淡入和DC滤波，再开放AGC定位差异。
78. [S18-R1-078] 同卡每段重置与跨卡各自状态不同需测量，不能只凭相同目标响度称一致。
79. [S18-R1-079] flush的192样本衰减不是新生成语音，不能加入RTF语音分母。
80. [S18-R1-080] 若修复NumPy算法须保留Rust接口版本兼容，并添加跨后端容差测试。

## 连续语义与播放接缝
源码位置：`go/gateway/segmenter.go; go/gateway/session.go; web/app.js:QttsRing`。

81. [S18-R1-081] 将独立模型韵律重启、显式停顿、播放欠载三种接缝分类计数。
82. [S18-R1-082] 保留朗读12/24首段、20/40/80稳态配置基线再比较，不盲目扩大。
83. [S18-R1-083] 逐字验证分段重新连接等于原文，保护数字、缩写、引号和标点。
84. [S18-R1-084] 审查PauseBeforeMs与tail_pause_ms是否重复加停顿，先画时序再修改。
85. [S18-R1-085] 禁止跨词PCM重叠掩盖接缝，不牺牲清晰度冒自然度。
86. [S18-R1-086] 段尾8ms衰减及下段淡入需以有声边界实测，不只用零边界波形。
87. [S18-R1-087] 欠载时0.94尾衰减属于播放补偿，不能误标模型本身沙沙。
88. [S18-R1-088] 自然度对照必须同时保存整段朗读，不能只听裁剪后小片段。
89. [S18-R1-089] 不同GPU同文与交替长文分别试听；同seed不等于波形完全相同。
90. [S18-R1-090] 只有真实模型支持的连续条件才能声称跨段联合生成，不换名称包装独立合成。

## 回归、语言和交付门禁
源码位置：`kaggle/repack.py; tests/browser; docs/validation/step17/final-checks.json`。

91. [S18-R1-091] 冻结原始至17包、全部manifest及正式工作台，新增18不得覆盖历史包。
92. [S18-R1-092] 三轮100建议均标已确认问题、待证假设或保留约束，不虚报300个bug。
93. [S18-R1-093] 完成三轮审查后再逐题决策，每题50建议后才进入下一题。
94. [S18-R1-094] 历史334测试不能算18新增验证，依赖缺失需如实记录和重建。
95. [S18-R1-095] 对每个修复保留修复前失败、修复后通过的同输入收据。
96. [S18-R1-096] 三轮Python、Node、Go race、协议和浏览器必须针对最终源码再执行。
97. [S18-R1-097] CPU合成信号实验不代替真实T4语音实验，硬件不足保持BLOCKED。
98. [S18-R1-098] 按实测热路径选择语言；不要新增Java/C#/SQL服务凑多语言。
99. [S18-R1-099] 最终18复制页、下载、剪贴板拒绝回退与手机逐字节校验不可省略。
100. [S18-R1-100] 将全部已完成备忘录内嵌完整提示词；未完成轮次必须明确，不编造结论。


## 第一轮实验补记

S18-R1-081已完成分块对照；S18-R1-082短块淡入问题在三轮冻结17 NumPy路径中复现，隔离增益后48样本分块最大差1424 int16单位。正常AGC1920分块差8。尚未修复，非用户噪声根因证明，非实际模型实验；其他建议不因此自动判为已实施。

---

## 内嵌备忘录：KAGGLE_STEP18_REVIEW2.md

# 第十八阶段第二轮：候选条件、接口合同与并发状态100条建议

状态：第二轮关键路径专题审查完成；第三轮与阶段自问自答未完成。不是全源三轮语义审查完成声明，产品源码未修改。每条建议是待实施/保留合同，不是100个新增已确认bug。

## 取证方法与来源

实际下载并核对faster-qwen3-tts0.5.4与qwen-tts-hf0.1.1.post1的PyPI wheel SHA256；旧qwen-tts0.1.1仅作区别核查，未安装。最初把发行版名写成qwen-tts==0.1.1.post1导致查询失败，纠正为项目真正固定的qwen-tts-hf；不是产品依赖失败。完整URL/hash见`validation/step18/upstream-round2-provenance.json`。

`kaggle/tests/reference_state_probe.py`提取原函数AST执行：真实控制流保留，外部GPU/ASR/tokenizer/说话人/网络为显式fixtures。确定性交错并非线程压力；未跑HTTP、完整模型或GPU，不证明音色或噪声。

## 真实模型接口与批量语义
源码位置：`faster0.5.4:model.py:_resolve_precomputed_voice_clone_prompt; qwen-tts-hf0.1.1.post1:qwen3_tts_model.py`。

1. [S18-R2-001] 保持qwen-tts-hf与旧qwen-tts发行版严格分离，源码同命名空间不等于同版本。
2. [S18-R2-002] 下载源码必须核对PyPI wheel SHA256，收据注明实际提供模型类的发行版。
3. [S18-R2-003] 将三提示单目标被拒绝的实际接口行为加入未来多参考功能合同。
4. [S18-R2-004] 将三提示三目标定义为独立批量任务，界面不能称参考融合。
5. [S18-R2-005] 保留列表prompt每项独立ref_text，不用共享一条文字冒三候选匹配。
6. [S18-R2-006] 字典prompt的批量ref_text共享行为应明确，不直接用于三段不同转写。
7. [S18-R2-007] 引用prompt item中ref_code与speaker embedding的区别，不能用声纹平均替代ICL。
8. [S18-R2-008] 保持单ICL预计算提示的真实接口回归，不能为新模式破坏现有快照。
9. [S18-R2-009] 向量模式继续要求显式选择，不把它作为未实现融合的静默替代。
10. [S18-R2-010] 实际生成器、权重和声学结果未执行时，接口控制流通过不标模型实验通过。

## 候选与生成条件合同
源码位置：`py/analyst.py:build_profile; py/voice_binding.py; py/worker.py:FasterEngine`。

11. [S18-R2-011] 建立全部候选分析清单，逐项列源文件、时间、匹配转写、指纹和有效性。
12. [S18-R2-012] 单锚点模式明确显示被用作ICL的候选及未用作ICL的其他候选。
13. [S18-R2-013] 若后续共享参数来自全部候选评分，记录算法与评分证据而非暗示音频融合。
14. [S18-R2-014] 比较每候选合成时固定同文同seed同采样参数，确保差异确由候选造成。
15. [S18-R2-015] 候选中心与实际Qwen说话人嵌入不同空间时不得直接替换。
16. [S18-R2-016] 实验性的融合嵌入若提出，必须独立模式且真实盲听，不自动作为最佳方案。
17. [S18-R2-017] 不跨候选拼转写或参考码以绕过模型批量长度校验。
18. [S18-R2-018] 候选顺序变化时用内容身份而不只用数组下标定位证据。
19. [S18-R2-019] 候选有效时长按实际WAV而非仅展示start/end计算，避免舍入差。
20. [S18-R2-020] 候选策略、模型模式及参数调整必须使旧会话明确失效。

## 候选入口数据验证
源码位置：`py/analyst.py:set_candidate / set_text; py/library_api.py:body`。

21. [S18-R2-021] index必须严格整数且非bool，拒绝true变1与false变0。
22. [S18-R2-022] 拒绝1.9截断成1，避免非整数JSON静默切换其他参考。
23. [S18-R2-023] 缺失index应明确拒绝还是显式兼容默认0，不让文档与行为矛盾。
24. [S18-R2-024] null、数组、对象及NaN输入转换失败应返回受控4xx而非未捕获异常。
25. [S18-R2-025] 候选入口未知字段与重复字段的策略需与严格library接口一致。
26. [S18-R2-026] 验证candidates为非空合法列表，不能只依赖len和下标访问。
27. [S18-R2-027] 验证候选file为安全单文件名且普通文件，避免损坏profile路径越界。
28. [S18-R2-028] 手工ref_text不接受dict/list被str化，保留严格字符串与Unicode校验。
29. [S18-R2-029] 保留训练档案禁止改候选和转写的409边界，不绕过版本固定。
30. [S18-R2-030] 增加真正HTTP参数与错误码测试；当前AST调用不冒充FastAPI测试。

## 参考版本与并发提交
源码位置：`py/analyst.py:calibrate_profile / set_candidate / set_text; py/qtts_common.py:write_json_atomic`。

31. [S18-R2-031] 校准开始捕获完整候选集合版本，提交时核对未变再采用评分。
32. [S18-R2-032] 禁止用旧候选评分选择重新读取后已更改的同下标候选。
33. [S18-R2-033] 校准期间并发编辑转写不能被结束时静默覆盖，需冲突响应。
34. [S18-R2-034] 候选文件内容更改但文件名不变也要改变校准输入版本。
35. [S18-R2-035] 候选变更、文本变更、校准、删除应协调同一档案锁或乐观版本合同。
36. [S18-R2-036] 进程内线程锁与跨进程文件锁分别评估，不能把一个称全局事务。
37. [S18-R2-037] HEAVY最大2只限制并发数量，不等于每profile串行，不能替代状态锁。
38. [S18-R2-038] 对先写磁盘再等HEAVY被429拒绝的路径核对reference_saved状态。
39. [S18-R2-039] 原子JSON替换只保护单文件，候选复制与JSON提交之间仍需一致性设计。
40. [S18-R2-040] 校准提交前档案已删除或adapter状态已变化时必须停止，不能恢复旧状态。

## 校准缺失指标与失败状态
源码位置：`py/analyst.py:calibrate_profile`。

41. [S18-R2-041] ASR评估全部失败不再用CER0.05冒充实测值，应记录null与失败原因。
42. [S18-R2-042] 部分文本ASR失败时记录覆盖率，不能只对成功样本平均后隐藏缺失。
43. [S18-R2-043] 全部候选合成失败时返回明确未选出有效结果，不能chosen0看似成功。
44. [S18-R2-044] 每候选的有效生成条数和预期条数同时保存，评分先验证完整性。
45. [S18-R2-045] 未测或低可信声纹指标不填高分默认值，应明确阻塞/降级语义。
46. [S18-R2-046] 候选排序排除非有限得分，NaN/Inf不进入max选择。
47. [S18-R2-047] 模型输出空音频、太短、全静音和缺字分别记失败而不只比声纹。
48. [S18-R2-048] 校准报告应保留先前有效结果，失败新校准不覆盖为貌似新最佳。
49. [S18-R2-049] ASR释放与临时目录清理放入覆盖所有异常的finally路径。
50. [S18-R2-050] 错误信息需脱敏且保留阶段，不能把原文和本机私有路径暴露给日志。

## 双卡诊断的可比性
源码位置：`py/analyst.py:consistency; go/gateway/scheduler.go:synthReq`。

51. [S18-R2-051] 同目标文本跨GPU诊断使用相同seed，修复100+17*ti+gi的设备偏移混杂。
52. [S18-R2-052] 将实际seed写入每张卡诊断条目，使测试条件可核验。
53. [S18-R2-053] 会话调度当前各卡同seed的行为应保留，不把诊断偏移引入播放。
54. [S18-R2-054] 两卡同一voice_binding和voice_conditioning都要进诊断收据。
55. [S18-R2-055] 记录实际dtype、模型版本、codec政策与DSP后端，不能仅比profile ID。
56. [S18-R2-056] 相同参数不意味着位级相同；阈值评分和人工听感结论分开。
57. [S18-R2-057] 同文对照与不同文本交替朗读各自设计，不能用同文替代自然衔接。
58. [S18-R2-058] 所有条目失败时speech_db默认0不应参与一致性，明确缺失项。
59. [S18-R2-059] consistent布尔值应附完整性及阈值说明，不能称零噪声或100%同声。
60. [S18-R2-060] 诊断生成在锁定或请求取消后仍进行时保留资源状态，不误报即时停止。

## 双卡加载与启用确认
源码位置：`py/analyst.py:load_on_workers / reload_response; go/gateway/main.go:activate`。

61. [S18-R2-061] 校准结束必须检查load_on_workers回执，不能丢弃失败后正常返回。
62. [S18-R2-062] 保留文本/候选接口已有reference_saved与503部分失败语义。
63. [S18-R2-063] Go激活两卡并行、同绑定同模式核验及旧active保留不得回归。
64. [S18-R2-064] 激活最终再次读磁盘核对指纹的检查必须保留。
65. [S18-R2-065] Python reload最终current为None时应视失败，而不是跳过版本核验。
66. [S18-R2-066] 候选校准只用GPU0的现状须说明；多卡校准需独立计划，不虚报双卡评估。
67. [S18-R2-067] 加载某卡成功某卡失败后，不允许新会话静默只用成功卡冒双卡一致。
68. [S18-R2-068] 冷首次sanity合成耗时应与提示提取耗时分开记录，避免首声归因错误。
69. [S18-R2-069] HTTP断开不等于后台模型加载已停止，未来重试需幂等/状态查询。
70. [S18-R2-070] 不得为降低激活耗时跳过Worker锁内参考前后两次指纹校验。

## 缓存、临时资源与删除
源码位置：`py/worker.py:FasterEngine.load_profile / Worker._load_profile_locked; py/analyst.py:calibrate_profile / delete_profile`。

71. [S18-R2-071] 审查_cal临时profile移除后Worker提示缓存仍驻留的资源生命周期。
72. [S18-R2-072] 重复校准相同临时ID时确保旧提示被替换，不能复用先前参考。
73. [S18-R2-073] 删除档案后清理与它关联的profiles、voice_bindings、levelers和提示快照。
74. [S18-R2-074] 缓存释放必须获取合成同一把锁，不释放正在使用的GPU张量。
75. [S18-R2-075] 缓存容量按可测内存预算管理，而不是只看磁盘profile数量。
76. [S18-R2-076] 临时校准ID与用户可启用ID区分，不能由列表选中临时声音。
77. [S18-R2-077] 备份继续排除_cal档案，不把测试用临时状态持久化为模型。
78. [S18-R2-078] 临时目录清理失败记录状态并可回收，不无声积累数据。
79. [S18-R2-079] 生成器取消仍要close并释放有界codec窗口，不能因缓存修改遗漏。
80. [S18-R2-080] 不要盲目清空CUDA所有缓存导致每段冷启动，资源回收须按作用域。

## 前端状态、认证与用户反馈
源码位置：`web/app.js:apiFetch / m / profile candidate controls; py/access_control.py`。

81. [S18-R2-081] 候选点击期间禁用或序列化同档案变更按钮，避免重复并发写。
82. [S18-R2-082] 响应乱序时按操作版本更新高亮，不让旧响应覆盖新选择。
83. [S18-R2-083] 继续保留accessEpoch和AbortController防锁定后迟到数据回填。
84. [S18-R2-084] 客户端取消只能停止等待时明确提示后台任务可能继续，不伪报服务器取消。
85. [S18-R2-085] 503且reference_saved时显示已保存未全卡就绪，不能笼统当未保存。
86. [S18-R2-086] 校准报告区分逐候选评分、最终提交、双卡加载三个状态。
87. [S18-R2-087] 没有有效候选或指标不全时不显示成功绿标。
88. [S18-R2-088] 参考转写可审阅但日志默认脱敏，token不进URL/localStorage。
89. [S18-R2-089] 新增条件证明信息只放同源授权接口，不能自动上传外部诊断服务。
90. [S18-R2-090] 新增交互保持移动端可操作、录音失败队列保留与锁定清空。

## 保留边界与最终验证
源码位置：`py/voice_library.py; py/trained_profiles.py; py/persist.py; tests/browser`。

91. [S18-R2-091] 原始库已有revision与lease设计可借鉴，但不直接修改其已成功数据格式。
92. [S18-R2-092] 候选处理与真实训练继续分开命名，不把评分或缓存称训练提升。
93. [S18-R2-093] 训练adapter来源hash与固定参考在新条件策略下仍必须核验。
94. [S18-R2-094] 私有原始样本仍排除Dataset自动备份，新增诊断WAV默认不进入归档。
95. [S18-R2-095] 代码、参数和参考版本相同的测试与实际用户WAV声学验收分开报告。
96. [S18-R2-096] 为每个确认缺陷建立独立失败样例，后续修复应让同案例先失败再通过。
97. [S18-R2-097] 受控AST交错不是线程压力测试；实现后补真实并发和HTTP回归。
98. [S18-R2-098] 下载wheel仅源码检查不安装旧qwen-tts，避免命名空间冲突。
99. [S18-R2-099] 本轮100建议与实际实验范围完整入备忘录，不宣称全源三轮完成。
100. [S18-R2-100] 第三轮结束及逐题50建议决策完成后才改产品，继续冻结17包与工作台。

## 三轮受控实验结果

每轮6项上游提示合同、4项校准场景、9项候选输入、1项双卡seed诊断，共20项；三轮结果一致。三提示单目标list/dict均拒绝，三提示三目标是独立批量。ASR全失败产生默认CER0.05、旧评分提交新候选、加载失败未检查、全合成失败仍chosen0、bool/float强转、非法类型异常以及诊断不同seed均复现。它们是控制流/状态问题，不是用户沙沙根因。

保留：Go激活并行加载、指纹/模式确认、最终重读及旧active保留；Python文本/候选reload_response已有503与reference_saved语义；Worker锁内前后核验；前端认证epoch。不能只列缺陷却重写破坏这些成功保护。

---

## 内嵌备忘录：KAGGLE_STEP18_REVIEW3.md

# 第十八阶段第三轮：数值、时序与播放边界100条建议

第三轮专题审查完成，外围模块仅作静态入口/边界复核；不声明所有源码已逐行语义审查三遍。产品未修改，18未发布，自问自答尚未开始。建议不是100个已证实缺陷。

## 实验范围

`playback_boundary_probe.mjs`执行原播放器/协议解析器前缀和Worklet源码，每轮22案例，时钟/端口/AudioWorklet基类受控。没有实体浏览器AudioContext或硬件播放。`trimmer_boundary_probe.py`执行原EdgeTrimmer AST，每轮8案例，输入为显式合成信号。两探针各三轮一致；不是完整语音模型实验。

新复现：生成结束20/50ms剩余音频会滞留buffering；首播放指标在发送命令时已赋值；35ms预滚跨块丢失840样本；小于120样本的语音块可被全丢；不足一帧的非零尾段可留held无finish。小块测试并非当前Faster1920帧倍数路径已发生的证据。

保留成功保护：重采样分块连续性、自然结束不报欠载、欠载只计一次、reset后零输出、ring溢出计数、协议逐字节分包及32MiB限制。末端重采样端点不足只是合同需定义，不宣称已证明有可听损伤。

## 生成码与codec窗口
源码位置：`py/clone_stream.py:GeneratedCodecWindow / generated_only_stream`。

1. [S18-R3-001] 保留16码本、24kHz及1920样本每帧合同，不用未知解码器静默替代。
2. [S18-R3-002] 左上下文25帧只保留有界生成码，参考码继续禁止进入输出解码。
3. [S18-R3-003] 默认右前瞻0与实验1/2帧分别记录延迟与真实质量，不用随机codec推断最优。
4. [S18-R3-004] 为每次提交记录全局帧偏移与已提交区间，定位接缝是否重复或漏帧。
5. [S18-R3-005] 区分有效生成帧、保留上下文和待提交PCM，不能把重复解码时间当新语音。
6. [S18-R3-006] 取消和异常均close生成迭代器并清理pending，禁止取消后尾包泄漏。
7. [S18-R3-007] 实际tokenizer返回错误采样率、非有限值或长度不符继续拒绝。
8. [S18-R3-008] 按首2/4/8帧对照时固定后续策略与文本，不能混入候选或seed变化。
9. [S18-R3-009] 真实codec有限上下文与整段解码差值须用预训练权重另测，不凭因果结构宣布无接缝。
10. [S18-R3-010] prepare_ms不含生成器首次next里的全部预填充，拆分前先验证时钟范围。

## 后处理状态与ABI
源码位置：`py/audio_rt.py:Leveler; rust/audio_rt/src/lib.rs:Leveler`。

11. [S18-R3-011] 将整块与不规则分块输出一致性列为DSP算法合同而非只检查有限和长度。
12. [S18-R3-012] NumPy淡入使用固定总长度及已处理位置，不让每次短块重新从零起算。
13. [S18-R3-013] NumPy RMS统计保留不足10ms余数，避免按来包边界重新分组。
14. [S18-R3-014] Rust逐样本平滑与NumPy插值应先定义相同算法再设合理量化容差。
15. [S18-R3-015] flush后Rust清DC状态而NumPy不清的差别须明确，不能称API语义完全一致。
16. [S18-R3-016] 当前Worker每段重建leveler，不能将跨段复用API问题直接认定为生产根因。
17. [S18-R3-017] 固定目标电平与最大增益仍不保证两段动态响度相同，保留完整语音测量。
18. [S18-R3-018] 纯静音、阶跃和有声转静音须同时检查滤波残留、削波和增益泵动。
19. [S18-R3-019] Rust ABI加载需区分不兼容符号和库缺失，不能失败后不告知回退路径。
20. [S18-R3-020] 缺Rust编译器时记录未执行，不用C++重写参考实现冒Rust实测。

## 首尾裁剪与语音完整性
源码位置：`py/worker.py:EdgeTrimmer / Worker.run_job`。

21. [S18-R3-021] 120样本以下语音块不能因无完整RMS帧就直接丢弃，设计跨块累积。
22. [S18-R3-022] 跨输入块保留35ms有界预滚，而非只在检测到声音的当前块向前取。
23. [S18-R3-023] 候选静音与未发声辅音不能仅凭能量绝对区分，试听门禁保留。
24. [S18-R3-024] 短末块含有非零语音时须有明确finish策略，不能永久留held后销毁。
25. [S18-R3-025] 尾静音裁剪应记录实际删掉时长和阈值，不把删音频冒首声或RTF提速。
26. [S18-R3-026] 900ms超长首静音放行应保留异常说明，不能把放行静音算实际人声。
27. [S18-R3-027] 1800ms held上限必须在长无声生成时仍有界，不引入全句缓冲。
28. [S18-R3-028] 输入codec固定1920样本倍数与泛用小块测试分开，标注生产可达性。
29. [S18-R3-029] 裁剪器发出的样本索引需可追溯至模型原始PCM，便于核对漏音。
30. [S18-R3-030] 输入很轻时不要单纯升高裁剪阈值，应比较失真与背景噪声的权衡。

## 重采样与终止语义
源码位置：`web/app.js:Player.resample / markGenerationDone / beginStream`。

31. [S18-R3-031] 保持流式相位和上一个输入样本跨PCM帧连续，不能每帧独立插值。
32. [S18-R3-032] 24k直通与44.1k/48k转换各自验证输入时长和输出样本预算。
33. [S18-R3-033] 终止时缺下一个插值端点应定义末样本延拓或明确短尾策略并测试。
34. [S18-R3-034] 重采样收尾不能以补充可计入speech的静音改变RTF分母。
35. [S18-R3-035] 每段协议标记不应重置同一朗读流的重采样相位，会制造边界跳变。
36. [S18-R3-036] 锁定、取消和新流begin应清掉上一任务的相位及延迟端点。
37. [S18-R3-037] 分块与整块重采样在数值容差内一致的现有行为应保留。
38. [S18-R3-038] 一输入样本、空块及极短末块需测试，不只测长整秒波形。
39. [S18-R3-039] 扩展至降采样时需考虑抗混叠，不能将线性插值叫任意采样率高保真。
40. [S18-R3-040] 实体浏览器实际采样率与请求24k可能不同，诊断记录两者。

## 短尾启动与播放状态
源码位置：`web/app.js:Player.tick / needToStart / onWorklet`。

41. [S18-R3-041] 生成结束且剩余20ms音频应有播放或明确失败结果，不能永久buffering。
42. [S18-R3-042] 精确50ms边界的严格大于判断需单独测试，不能只测51ms。
43. [S18-R3-043] 欠载恢复时最后短尾同样应可排空，避免截掉最后一个音节。
44. [S18-R3-044] 已结束数据的排空政策与持续生成时风险缓冲分开，不盲降正常启动阈值。
45. [S18-R3-045] 有剩余样本但低于阈值时ended判定须有终止路径，不假装已播完。
46. [S18-R3-046] 一任务只能产生一次最终结束，迟到统计消息不能把ended改回playing。
47. [S18-R3-047] 长网络抖动和低产出速率下测试启动等待与欠载率成对取舍。
48. [S18-R3-048] 暂停恢复必须在用户授权AudioContext状态下执行，不自动规避浏览器策略。
49. [S18-R3-049] 单调时钟中的0值不宜兼任未记录标记，检查极早首包的时间哨兵。
50. [S18-R3-050] 运行原播放器VM只能证明逻辑，不可声称浏览器硬件首声变快。

## Worklet与首声指标
源码位置：`web/app.js:QttsRing / Player.firstPlayedMs; go/gateway/session.go:telemetry`。

51. [S18-R3-051] firstPlayedMs目前是主线程play命令时刻，名称与报表需区分实际消费。
52. [S18-R3-052] 增加首样本消费确认前先定义是否跳过显式停顿和极小淡入样本。
53. [S18-R3-053] Worklet currentFrame与主线程performance属于不同时间轴，使用可解释映射。
54. [S18-R3-054] 保留ring样本计数与自然结束不额外记欠载的已通过行为。
55. [S18-R3-055] 欠载只计一次直至恢复，避免每个渲染量子重复放大统计。
56. [S18-R3-056] 容量溢出dropped必须进入上层状态和失败提示，不能只在底层计数。
57. [S18-R3-057] 固定192样本淡入在24k/48k分别8/4ms，若要求同毫秒则按实际率配置。
58. [S18-R3-058] hold与reset后无旧PCM回放，保留现有重置后精确零输出测试。
59. [S18-R3-059] 环形缓冲溢出属于丢样，不得被统计成已自然连续读完。
60. [S18-R3-060] 声卡/系统输出延迟仍需实体设备测量，Worklet消费也不是声学听到时间。

## 停顿、顺序与重试
源码位置：`go/gateway/segmenter.go:finish; scheduler.go:run; session.go:serve`。

61. [S18-R3-061] 规划器PauseBeforeMs由上一边界生成，逐段记录而不是把所有停顿归模型。
62. [S18-R3-062] Worker默认只加显式lead pause，核实tail默认0后再判断重复停顿。
63. [S18-R3-063] 保留首段零规划停顿，不以参考呼吸或原音占位提前出包。
64. [S18-R3-064] 模型内部停顿与规划停顿叠加需实际WAV分层对照，不能只删规划停顿。
65. [S18-R3-065] 有序转发必须保留，不能为了最快包先播后一GPU导致错序。
66. [S18-R3-066] 已消费部分PCM后禁止跨卡整段重试，保护不重复词句的现有门禁。
67. [S18-R3-067] 未消费重试时正确扣除旧produced样本，维持背压与统计一致。
68. [S18-R3-068] first_worker_audio可能是显式静音包，报表不可直接称人声首包。
69. [S18-R3-069] 第一段4帧与后段6/8/12帧策略保留可追溯，提速不得改变音色条件。
70. [S18-R3-070] 正文保留、引号配对、小数和缩写拆分须有实际Go回归，不靠源码注释。

## 训练、资源与私有边界
源码位置：`py/training_job.py; gpu_ownership.py; supervisor.py; tools/resource_control.py`。

71. [S18-R3-071] 在线推理与离线训练GPU租约保持互斥，不为测试盲停驻留模型。
72. [S18-R3-072] 真实双卡训练、引用缓存与profile建档继续分开报告，避免功能混淆。
73. [S18-R3-073] 子进程继续清除API与认证秘密环境变量，不因性能诊断泄漏。
74. [S18-R3-074] 模型与adapter来源hash及安全权重格式不能为快速加载而跳过。
75. [S18-R3-075] 训练数据审阅/完整覆盖与声学验收是独立缺口，18音频修复不自动解决。
76. [S18-R3-076] 取消训练只终止本次进程组，不根据旧PID文件杀其他进程。
77. [S18-R3-077] 保留离线代码与模型指纹核验，不自动开启远程代码或下载权重。
78. [S18-R3-078] 新增诊断原始WAV默认私有且关闭，不能进入公开Git和自动备份。
79. [S18-R3-079] 资源状态的CPU成功不标CUDA或GPU优化成功，尤其是当前无Torch环境。
80. [S18-R3-080] 剩余复杂训练/恢复路径只有入口边界复核，明确语义深审仍需补齐。

## 交付、前端与安全回归
源码位置：`src/server.js; src/store.js; public/file-rules.js; tools/kaggle-copy-server.mjs`。

81. [S18-R3-081] 正式工作台继续只读核对，不因音频审查改写15文件或HEAD。
82. [S18-R3-082] 自命名空白文件、用户粘贴、并发版本冲突和磁盘持久化需保留。
83. [S18-R3-083] 复制预览与正式工作台分别核对，不能用旧17复制成功冒18完整包成功。
84. [S18-R3-084] 新发布前固定launcher字节数/hash，并校验53以上实际资产完整性。
85. [S18-R3-085] 剪贴板失败回退应选中完整源代码，不能只复制可见窗口。
86. [S18-R3-086] 文件名、路径穿越、脚本/style闭合注入等既有浏览器测试继续执行。
87. [S18-R3-087] 锁定清理、同源token和迟到响应隔离不能被新指标消息绕过。
88. [S18-R3-088] 旧验证脚本固定历史分支属于历史证据，新分支另建验证器而非改旧收据。
89. [S18-R3-089] 新工具依赖留忽略目录，下载源码也不与模型权重混入发布资产。
90. [S18-R3-090] 所有未执行的Go/Rust/真实浏览器/完整模型实验明确标未执行。

## 证据覆盖与最终决策
源码位置：`docs/validation/step18; KAGGLE_STEP18_PLAN.md`。

91. [S18-R3-091] 完整manifest读取/hash/AST只证明库存与语法，不声明全源逐行语义无错。
92. [S18-R3-092] 三轮专题各100完成也不等于所有代码已语义审查三遍，覆盖缺口单列。
93. [S18-R3-093] 每个实验写方法、注入边界、实际源hash及探针hash，避免不同版本混算。
94. [S18-R3-094] 将已复现缺陷、待验证假设与保留保护分别分类，不将300建议全标已修。
95. [S18-R3-095] 重建环境仅NumPy和Node时旧模型实验收据保留历史，不算新执行。
96. [S18-R3-096] 第25题起一次一题，具体选项/推荐/理由/50建议全部记录后再下一题。
97. [S18-R3-097] 实施方案要将首声、条件来源、状态一致、DSP、裁剪、播放排空分成可回滚小步。
98. [S18-R3-098] 产品最终源码冻结后完整三轮回归，当前边界探针不能代替全功能通过。
99. [S18-R3-099] 零噪声/单一音色/自然朗读及RTF0.3仍需真实WAV和双T4，不用绝对承诺替代。
100. [S18-R3-100] 第三轮备忘录和缺口完整内嵌提示词，发布18之前仍使用17并保持PARTIAL。

---

## 内嵌备忘录：KAGGLE_STEP18_DECISIONS.md

# 第十八阶段逐题决策（进行中）

历史问题1–24及1200条建议保留在KAGGLE_DECISIONS.md；这里从25开始，不覆盖历史记录。三轮专题各100建议已记录，不等于所有文件逐行语义审查三遍；覆盖缺口仍保留。当前按顺序完成问题25、26、27及各50项实施建议，不宣称整体需求/声学根因已100%确定。

## 问题25：怎样让全部候选真正参与条件决策，而不把批量提示或单锚点冒充多参考融合？

### 具体选项

- **A：维持选#0/#1/#2其中一个，仅改界面名称为“多参考”。** 不接受：没有新增全部候选证据，也会误导。
- **B：直接将三个prompt传给一个目标文本。** 不接受：真实Faster0.5.4 resolver要求prompt数量与目标批次一致；三提示三目标是三个独立输入，不是同一句参考融合。
- **C：分成明确可核验的两层。** 全部合格候选用相同目标文、seed、生成参数做逐候选评估，记录有效/无效与缺失指标；单锚点ICL保留音频和转写对应，来源/模式/参数一致绑定到两卡。若要同一句同时利用多参考，另开“同模型Qwen说话人嵌入融合”实验，核查真实形状/归一化/内容绑定，并以真实WAV门禁决定是否可用；未运行或未通过时明确未实现融合，不退回单锚点后宣称成功。
- **D：把候选PCM混入播放或把不连续音频配全文。** 禁止：违反原音隔离和音文一致性要求。

### 推荐与理由

选择 **C**。它把“全部候选参与分析/校准”与“同一句实际多参考条件”分开，能够保存17已成功的ICL/生成码隔离路径，同时不给未验证的融合效果背书。真实接口允许预计算prompt字典，但这只证明可注入条件，**不证明融合向量质量一定更好**。ECAPA用于评分，不是Qwen模型的speaker embedding，不能跨空间直接替换。

当前不能确定用户“参数要结果”的文字是否等于要求所有参考码一起参与同一句ICL；不向用户提问，采用保守操作合同：**每个候选的作用必须可追溯；不能把未进入生成的音频说成已融合；任何实际融合未验收就明确BLOCKED。** 最终目标仍是更像、少噪、自然与更快首声，而不是仅完成一个数组接口。

生产默认和融合实验的最终开关、算法、权重、阈值都尚未决定；不能从本题直接跳到默认启用均值嵌入。先修校准的假CER、过期结果、加载确认和种子混杂，才能获得可比较的融合基线。

### 进入下一题前的50项实施建议

1. 建立候选源清单，保留每段源文件身份、实际WAV字节hash与时间范围。
2. 将候选展示下标与内容身份分开，避免排序变化错配旧证据。
3. 对全部候选记录匹配转写身份，不在公共日志明文输出私有转写。
4. 对全部候选记录分析有效性及被排除原因，不能静默丢失败候选。
5. 严格区分原录音、候选分析音频、ICL锚点与生成输出，禁止跨层混放。
6. 保留16/24秒参考窗口合同，不把全部候选时长之和称已用模型上下文。
7. 基线模式明确只用一个锚点ICL，其余候选的评分作用必须写清。
8. 逐候选对照采用相同目标文本，避免文本差异掩盖参考差异。
9. 逐候选对照采用相同seed，不能按候选编号偏移种子。
10. 逐候选对照固定四项有效生成参数，保留实际参数收据。
11. 记录引擎、模型版本、dtype、codec政策与DSP后端，排除环境混杂。
12. 拒绝bool和小数候选索引，不允许强制转换选错参考。
13. 明确缺少index的API语义；推荐受控4xx，不默认误选0。
14. 为null、对象、数组与非有限索引增加受控错误返回。
15. 候选文件验证单文件名、普通文件和字节预算，防路径与损坏状态。
16. 校准开始捕获候选集合与音文版本，不能仅记profile ID。
17. 结束时核对全部候选身份未变，变更则返回冲突且不应用旧评分。
18. 把文本编辑、候选切换、校准提交与删除协调到同一档案状态合同。
19. 阻止校准以旧候选评分覆盖用户新编辑转写。
20. 原子JSON写入不能代替多文件事务，失败时保留一致旧状态。
21. ASR评估缺失时记录null与失败阶段，禁止默认CER0.05冒实测。
22. 部分目标文评估失败时记录覆盖率，不能只平均成功样本。
23. 全部合成失败时不得设置看似成功的chosen候选。
24. 空音频、全静音、过短及非有限输出应独立计失败。
25. speaker相似度无效或非有限时不得参与max排序。
26. 保存每候选全部试验条目与聚合规则，不只保留最高分。
27. 校准结束检查每卡加载回执，失败显示已保存但未全卡就绪。
28. 保留Go激活的指纹/模式核验及失败保留旧active保护。
29. 双卡诊断用同文同seed，正式播放同会话seed行为继续保留。
30. 旧会话遇参考变更继续拒播，不静默切换成另一个候选。
31. 校准临时profile的来源元数据应准确标记被测候选。
32. 临时目录、提示缓存与leveler要有受锁保护的生命周期回收。
33. 将全部候选评估结果与实际ICL来源分开显示，不用“多参考”笼统覆盖。
34. 不将三个prompt列表当融合接口，保留实际resolver拒绝案例。
35. 若研究融合，只使用同一Qwen speaker encoder生成的兼容嵌入。
36. ECAPA质心仅用于评分，禁止不经模型合同替代Qwen嵌入。
37. 先核查真实嵌入维度、dtype、设备和归一化方式，再提出融合公式。
38. 不默认任意加权或归一化策略，公式及权重需进入可复现试验条件。
39. 融合实验仍保留一个匹配音文ICL锚点，不拼接不连续转写。
40. 将融合模式、候选内容身份与有效权重纳入跨卡条件版本核验设计。
41. 若融合条件读取失败必须显式失败，不静默单锚点回退冒融合成功。
42. 融合的提示提取与缓存开销计入冷启动，不漏记到队列时间之外。
43. 分别比较短参考、各候选、单锚点最佳及融合实验，不只挑幸运输出。
44. 真机对照保存同文两卡WAV和完整长文，不以单个声纹数字替代试听。
45. 检查漏字添字、相似度、齿音/沙沙和自然衔接，不能只优化综合分。
46. 相似度改善必须与首声、RTF、欠载及显存代价同时报告。
47. 私有诊断WAV默认本地关闭/按明确权限保存，禁止自动公开。
48. 未有真实权重与双T4证据时融合质量保持BLOCKED，不发布保证。
49. 为单候选与已训练固定参考保留兼容路径，不能强迫至少三个候选。
50. 本题代码实施仍待后续问题和最终方案完成，不将50建议自动标为已实现。

### 顺序追问（历史衔接记录）

第25题50条已在上一步完整列出；下方才继续第26题。原“未开始问题26”状态已结束，不修改上题选项、推荐与50条建议。

## 问题26：如何修复状态和音频边界，同时可靠衡量首声，而不是以丢音或错误指标冒充提速？

### 具体选项

- **A：立即把所有启动缓冲设为零，第一段固定两帧。** 不选：会把生产速率和网络抖动转成欠载；没有实际T4同条件对照，无法证明可用首声变快。末尾排空与正常流式启动不是同一个问题。
- **B：先强滤波、裁去更多静音、交叉叠加各段。** 不选：未定位噪声来源，可能抹辅音、重复/丢字，并掩盖真实模型/播放问题。
- **C：先固定度量与回归合同，再按“参考状态可靠性→DSP/裁剪有界状态→结束后短尾排空→受控缓冲与首块实验”分批修复。** 正常生成阶段保留风险缓冲；生成确实结束后，任何正长度合法PCM应能排空或得到明确错误，不滞留。冷暖、聊天/朗读、命令/消费/声学三类条件分别测。
- **D：先重写为更多语言或再驻留一个模型。** 不选：没有热路径数据支撑，会新增版本、显存和进程风险。

### 推荐与详细回答

选择 **C**。先确保参考校准没有假指标、过期结果和未就绪状态，否则速度对照可能比较不同声音或不完整任务。随后修复有直接复现的数值/边界状态问题；最后才用相同条件决定首块、缓冲或文本聚合调整。**这是一套待实施顺序，不是已修复声明。**

度量首先建立命名合同：

| 事件 | 可证明的含义 | 不能声称的含义 |
|---|---|---|
| Worker收到请求、取得锁、参考准备完成 | 同一进程单调时钟上的等待/准备区间 | 跨进程直接相减或把加载计为纯队列 |
| 首个模型PCM、首个处理后的生成PCM | 模型/后处理阶段产出样本 | 已识别为正确人声、已听到 |
| 浏览器首PCM | 收到可解析PCM，可能含规划静音 | 实际首声 |
| 主线程play命令 | 已要求播放；当前firstPlayedMs属于这里 | Worklet已经消费、扬声器已经发声 |
| Worklet首消费确认 | 渲染线程已读取样本；需明确是否包含规划静音 | 自动证明语音正确或硬件出声 |
| 声学首声 | 实际设备回录/有依据的同步测量与试听 | Node VM或CPU夹具可以替代 |

保留现有`first_played_ms`等兼容字段的旧语义，并另增明确字段/版本说明，不直接改含义让旧报表误读。没有观测到的事件为null/未测，不能填0冒瞬时完成。以幅度阈值判断“非静音”也不是声学人声识别，不能给首噪声抢先记首声。

源代码还确认：Worker的`queue_ms`在锁和参考准备后才结算，涵盖前置工作；Go的`queue_wait_ms`在完整流处理结束时用`time.Since(j.enq)`计算，含合成时间，并且每次Submit重设enq。需要新增每次尝试的入队/派发/结束区间及总任务耗时，而不是直接把这个旧字段当纯排队。

新增`latency_contract_probe.mjs`每轮16项，三轮一致：

- 初始buffering和starved两状态下，完成的20/50ms尾部均可滞留；51ms可发play，空结束可转ended。
- 未结束的20/50ms缓冲继续等待；已在播放的短尾不会被本次tick强行中断，这些应保留。
- 注入时钟/status的轨迹中，首PCM字段为300ms、play命令字段为750ms，而消费样本仍为0。**300/750是设定的实验时间，不是测得的真实性能，也不能据此说优化450ms。**
- 注入稳定快产出估计时，0.69/0.70秒跨越当前启动下限；该夹具只隔离阈值，不证明网络或GPU行为。

正常流式启动阈值暂不全局降低；现有首段4帧与实验2–8帧开关保留，真正的更快首声必须在目标机同参考、同文、同seed、同参数下至少三轮，且字词完整、噪声、自然度、欠载和RTF都不被牺牲。当前没有该声学证据。

### 进入下一题前的50项实施建议

1. 给每个小修复建立独立变更单，写明基线、预期不变量与回滚路径。
2. 先冻结17的缺陷样例与源hash，修复后的回归测试另建，不改写旧失败证据。
3. 对照测试固定参考内容、转写、模式、四生成参数及seed。
4. 把冷模型启动、冷档案提示、暖档案三种准备条件分开测量。
5. 聊天首个可用前缀与朗读首段采用各自配置，不混成一个平均首声。
6. 建立Worker请求接收、锁获得、参考准备结束的本地单调时间点。
7. 保留旧queue_ms字段兼容，同时明确它含参考准备，不只锁等待。
8. 在Go派发开始处记录入队至派发时间，不在合成结束处冒纯等待。
9. 重试时保留每次尝试的enqueue/dispatch/end，另存任务全程耗时。
10. 不对浏览器、Go和Python不同纪元时间戳直接相减。
11. 给首模型PCM与首后处理生成PCM分别打点，区分裁剪/DSP等待。
12. 规划lead pause必须独立标注，不能给静音包记人声首包。
13. 浏览器首次收到PCM与发送play命令分别记录，保留旧字段语义。
14. 新增Worklet消费确认前定义session身份，拒绝上一流的迟到确认。
15. 消费事件明确是否包含规划静音，不能把消费任意样本当可用人声。
16. 硬件声学首声没有真实测量时保持null，不填估计值冒实测。
17. 以非零幅度检测得到的只能叫非静音起点，不叫正确人声起点。
18. 首声分位统计至少附文本长度、参考长度、设备、模型与冷暖标签。
19. 首先修复非法候选参数和过期提交，避免性能对照条件偷偷变化。
20. CER缺失、全部合成失败及双卡未就绪必须有明确状态，不能仍报成功。
21. 将同文两卡诊断seed统一，保留正式播放的会话seed规则。
22. 对NumPy淡入使用连续累计位置，避免短块在第二包重新从零淡入。
23. NumPy RMS块累积保留余数，再与Rust逐样本平滑合同核对。
24. 不为通过分块测试只放宽数值容差；首先确定算法和量化约定。
25. 对低于120样本裁剪块采用有界累积，测试有限样本守恒。
26. 用有界预滚保留跨块35ms上下文，不引入整句缓存延迟。
27. 为裁剪器终止定义带非零末帧的finish行为，不能默认销毁held。
28. 仍允许有依据地去尾静音，但记录删掉区间，不删真实语音来提速。
29. 对泛用短块和Faster1920样本倍数路径分列测试，标明生产可达性。
30. Worker每段重建leveler的现状先保留，不无证据引入跨段共享可变状态。
31. 对生成完成后的任何正长度剩余PCM设计可排空路径。
32. 分别测试20/50/51ms、一个样本、空结束及恰好阈值。
33. 初始buffering与starved恢复都覆盖短尾终止，不只修其中之一。
34. 未生成完成时仍保留风险缓冲，不能把末尾例外推广到所有小包。
35. 已在playing时不得因剩余不足阈值强行暂停或丢尾。
36. 重采样最后缺插值端点时定义可追溯收尾，不偷偷补时长冒语音。
37. 锁定、取消和新流开始后不能排出旧任务尾巴。
38. 对Worklet自然结束、一次欠载计数和reset零输出保留保护测试。
39. 把dropped样本向上层明确报告，不允许丢样后称完整朗读成功。
40. 任何新增时序控制消息需要兼容/版本说明，不改PCM字节布局冒兼容。
41. 保留Live首句早提交、Read正文与标点保留、Go有序转发。
42. 保留已消费PCM不整段重试的保护，避免提速时重复词句。
43. 改动后基线探针应从冻结17取原控制流，修复回归指向新源码，避免混算。
44. 对2/4/8帧首块做真实同条件A/B，未有T4证据前不改默认4帧。
45. 启动缓冲调整需同时报告首声、欠载次数/间隙、掉样与全文完整性。
46. 朗读聚合变化须完整长文试听，不能只看首段变快或单句声纹分数。
47. 不默认强滤波、合成呼吸或跨词PCM叠加，噪声根因另题分层定位。
48. 新增诊断默认不保存私有原音或口令到公开日志，权限边界保持。
49. 最终源码冻结后再做完整三轮Python/Node/Go/协议/浏览器回归，本题VM不替代。
50. 真机声学、全源深审覆盖和问题27仍未完成时，不签收18发布或全部需求。

### 顺序追问（历史衔接记录）

第26题50条在上一步完整列出；下方才进入第27题。原未开始问题27为历史状态，上题主体与50条保持不变。

## 问题27：沙沙声和自然度如何分层取证，哪些改动可以尝试，什么证据才允许验收？

### 具体选项

- **A：提高去噪强度、降低高频，观察SNR变大就验收。** 不接受：现有SNR字段是帧能量分位差，不能当真实噪声SNR；齿音和气声可能一起被抹掉。
- **B：删除低能片段、加长静音或叠加各段来掩盖接缝。** 不接受：可能丢字、延迟、重复或抹平人声；静音输出也能“无噪”，但不满足要求。
- **C：分层留证，先修可复现工程缺陷；降噪/韵律改动仅做明确对照，用语音完整、音色、噪声、整段自然度及真实时序联合门禁验收。** 未取得真实WAV/目标模型/T4证据时，声学与性能项保持BLOCKED，不伪造通过。
- **D：只有相似度综合分高、双卡参数相同就宣布零噪声和自然。** 不接受：评分和参数只证明各自有限合同，不证明听感或完全身份一致。

### 推荐与详细回答

选择 **C**。把四种现象先分开：持续底噪/模型沙沙、codec或DSP边界点击、播放欠载断续、独立语段韵律重启。它们可以同时存在，不能由截图或一个指标选定唯一根因。

诊断链按“原始参考→参考处理后/实际ICL锚点→模型生成PCM→codec/后处理PCM→浏览器队列与消费→实体播放”组织，接口和文件记录每层的来源、样本范围、采样率、条件指纹及操作。私有WAV默认不采集/公开；需要实际诊断时在授权本地范围保存。首声、声学质量、训练结果分别签收。

`noise_metric_probe.py`执行原stage17的frame_rms_db、estimate_snr、speech_rms_dbfs、normalize_speech函数；其余仅为已知干净/噪声分量的合成反例，每轮8项三轮一致：

- 相同能量的重复帧中，真实组成SNR约26.53与0.51dB，现有estimate_snr均为0；无噪声但有强弱变化的样本反而返回约14.64dB。该字段是能量对比代理，非真实SNR真值。
- 同时衰减信号和噪声20dB，真实SNR不变；原normalize_speech对该很轻样本增益约14dB，真实SNR也不变。归一化不是去噪。
- 全部抹为零不能验收。理想低通反例虽消除高频噪声，却删除有用6kHz合成分量，使相对已知干净目标的误差从约-56.05dBFS增至-43.01dBFS。该理想FFT掩码不是项目实际去噪器，也不是真实齿音实验。

因此先纠正指标说明并修已复现的状态、分块、短尾问题；不立即改当前参考清理阈值，不给生成输出默认加新强降噪器。现有参考降噪的声纹/SNR代理门禁不能证明绝对保真或“噪声确实降低”，需原音/处理后真实对照。任何实验失败要保留原因，不静默切算法后称同等质量。

自然度需保留完整长文、每段文本和边界时序：分清模型自然停顿、规划停顿、衰减补偿和欠载；检查漏字/添字/重复、单一声音、齿音/气声、句间韵律。不得将参考PCM/呼吸拼进输出、跨词叠音或删音充当解决办法。固定参数同seed只是控制变量，不保证两卡声学相同。

### 验收与发布门槛

1. 工程修复可独立验证，但不能称用户所有声学目标完成。
2. 最终源码冻结后，完整Python、Node、Go race、协议和浏览器三轮；修复前后同输入、失败日志及保护案例保留。
3. 真实同人参考、完整模型、双T4至少三轮，包含各候选、推荐策略、同文两卡及交替长文；记录原始结果、先后顺序与实测条件，不挑最好一次。
4. 听感验收结合转写/人工逐字审核及盲听：不设未校准的相似度阈值冒100%身份；无清洁真值不报告“真实SNR”；不能证明绝对零噪声。
5. 真实首声及RTF≤0.3分别测，排除静音填充/参考片段，同时检查欠载和掉样。未执行或不达标必须明确。
6. 18工程包可在范围内交付时仍须显著标PARTIAL/BLOCKED；不称完整需求通过。当前全源三遍语义复核也未签收，尚不进入产品实施。

### 进入后续步骤前的50项实施建议

1. 将持续沙沙、点击、断续与韵律重启建立独立问题分类，允许多因共存。
2. 原参考、处理参考、ICL锚点和生成音频使用不同来源标记，防止错比。
3. 每层保存样本数、率与内容hash，时间偏移来自可追溯范围。
4. 未授权的原始WAV默认不落公开日志、Git、诊断链接或备份。
5. 实际采集诊断保持本地私有，原始基线只读保留。
6. 记录录音原始电平，不根据-47.7dBFS猜设备或直接判无声。
7. 将legacy snr_db标明能量分位对比估计，不能直接当真实噪声SNR。
8. 保留旧字段兼容，新增语义说明/版本，不无证据强改排序阈值。
9. 有已知干净分量时才计算真值SNR，并说明合成来源。
10. 无干净参考时把噪声估计与置信/假设分列，不编真实SNR。
11. 将幅度归一化和降噪分成两个处理步骤及收据。
12. 同时衰减信号/噪声不能算降噪改善，保留反例测试。
13. 全静音、极低音量或删完语音必须判无有效语音，不计零噪成功。
14. 不把齿音和气声自动归噪；先以真实样本核对语音成分。
15. 对噪声降低与音色、清晰度、添漏字设联合评价，不只最小化噪声功率。
16. 不默认启用新的输出低通或谱门，先隔离噪声产生层。
17. 当前参考降噪算法的参数、决策与处理时长完整保留。
18. 对不降噪、现有各强度及拟议方案用同源音频做可逆对照。
19. 处理失败或质量未提升时明确原因，不静默假装已经干净。
20. 声纹模型与Qwen条件空间分开，不能以ECAPA高分证明声音无失真。
21. 模型原始输出与后处理输出分别比，识别新增伪影来自哪里。
22. codec边界定位使用全局帧/样本偏移，不仅按网络包边界猜。
23. 继续禁止参考码进入输出解码，保留generated-only合同。
24. 淡入/AGC分块状态先按确定性回归修，不称它必是用户沙沙原因。
25. 裁剪预滚和末尾处理必须有样本范围收据，避免丢辅音或尾音。
26. 低能段如果无法区分停顿与人声，应保守保留并给诊断，不强删冒去噪。
27. 原音和合成呼吸均不得拼入生成播放增加“真人感”。
28. 自然模型人声呼吸不自动删除，区分人声气息与外加噪声。
29. 每段文本、模型内部停顿及规划停顿分别记录以定位不自然。
30. 跨词交叉淡化不作为默认补救，不牺牲字词完整度。
31. 保存完整朗读而非只挑局部片段试听，保留段间上下文。
32. 双卡同文固定相同seed/有效参数，设备差异单独记录。
33. 交替长文另测连续性，不能用同文双卡相似分替代。
34. 欠载事件、间隙、dropped和播放消费计数进诊断，不能只报生成成功。
35. 生成已完成的短尾排空不与正常生成小缓冲政策混同。
36. 锁定和取消后不得回填迟到音频、原文或诊断私有数据。
37. 更大朗读聚合需测首声与韵律取舍，不预先称必然更自然。
38. 每个新处理方案至少三轮同条件对照，记录全部结果与失败。
39. 盲听时随机化展示顺序并保留映射，不给评审暗示推荐版本。
40. 转写检查除CER还列具体漏字/添字/重复，避免平均数掩盖错词。
41. 人工审阅记录范围和人员/方法，不能把ASR当人工真值。
42. 严格100%音色或零噪声不可由有限实验证明，报告可验证范围。
43. 真机首声测量排除命令时间冒出声，保持第26题度量合同。
44. RTF分母仅用定义明确的生成语音，静音、参考拼入和删音不能投机。
45. 每个工程修复冻结前保留修复前失败样例及修复后保护测试。
46. 最终版本完整三轮回归后才生成固定hash的18复制/下载资产。
47. 复制包逐字节、手机和剪贴板失败回退不因音质实验省略。
48. 原始–17、正式工作台、私有边界、训练来源和取消功能继续保护。
49. 未测完整模型/双T4/声学条件必须BLOCKED，不能用本反例实验代替。
50. 汇总25–27题各50建议与300专题建议的处置，不把规划标成已实现。

### 当前决策阶段结论

本批问题25–27已按顺序完成，各50建议；暂不新增问题28凑数量。若后续深审/实验出现新关键选择再逐题记录。下一步是补齐全源语义覆盖、把已知问题映射为可执行小修复及其失败测试；门禁未满足不改产品、不生成18，不虚报所有目标完成。

---

## 内嵌备忘录：KAGGLE_STEP18_IMPLEMENTATION.md

# 第十八阶段本批工程实施细则（前置门禁未签收）

> 最新优先：S5完成短尾/重采样终点/epoch已实际修复，见KAGGLE_STEP18_S5_PLAYBACK.md；最终610CPU/37VM/173Chromium各三轮以progress-s5.json为准。完整候选app不切正式入口，真实声学与整体仍PARTIAL/BLOCKED。

> 最新优先：S4有界裁剪/worker结束与取消已实际修复，见KAGGLE_STEP18_S4_TRIMMER.md；602×3、21分块×3通过。S3 worker保留，S4入口worker_s4.py未切换正式服务；整体PARTIAL/BLOCKED。

> 最新优先：S3因果 NumPy DSP 与隔离worker实际接入，见 KAGGLE_STEP18_S3_DSP.md；562×3及14分块×3已通过，但Rust/真实声学与完整S3仍PARTIAL/BLOCKED。更早“下一步S3”等均为历史。

> 最新：S2-B有效指标与加载就绪实际实现，见末尾及KAGGLE_STEP18_S2_VALIDITY.md。早期“评分未修”仅历史；完整产品／声音／双T4验收仍未通过。

> 最新：S2-A校准快照实际实现，见末尾及KAGGLE_STEP18_S2_SNAPSHOT.md。S1原28合同保留，完整S2／模型／声学仍未验收；更早“未实现”仅为历史状态。

> 当前优先状态：S1隔离候选实际实现，见本文件末尾和KAGGLE_STEP18_S1_CANDIDATE.md。问题28明确允许未发布候选小步修复，不改冻结17；下文早期“尚无产品修改／不实施”是当时历史，不是本次状态。G0整体与完整S1验收仍PARTIAL/BLOCKED。

## 状态与范围

25–27题按顺序完成，各50项建议，专题建议300条。以下是可执行批次，不是已完成修复清单。全源三遍语义覆盖仍有缺口，最终全功能三轮、真实浏览器/HTTP并发、完整模型和双T4声学验收尚未执行。**当前不修改产品源码、不发布18；17复制包继续冻结。**

已知工程复现不等于用户沙沙声全部根因。默认不新增输出强降噪、不混参考PCM、不将实验融合启用为默认。工程交付与整体声学签收分开；后者仍BLOCKED。

## G0：实施前必须补齐

- 以53资产库存为起点逐模块补充三轮语义深审的实际范围、风险、结论及测试映射；不能只读hash/AST或专题热点就标全源三遍完成。
- 固定17源码供缺陷对照，保留现有探针/收据。修复后新增回归指向新源码；旧探针若期望缺陷，不能悄悄改成成功后仍称旧基线。
- 建立300建议处置：确认缺陷、保留保护、待证实验、硬件阻塞、文档边界；每条关联证据，不把300条当300个已修bug。
- 记录完整模型/用户WAV/T4不可用条件。缺依赖时不能用旧17收据或NumPy实验冒本批全功能验证。

## 小步变更单（G0通过后依次执行）

| 批次 | 拟修改位置 | 修复前证据/必备测试 | 实施合同与保留项 |
|---|---|---|---|
| S1 严格候选/文本入口 | analyst profile routes | reference_state_probe bool、float、null等基线；补真实HTTP4xx | 严格类型/范围；受控错误；固定训练参考限制不变；不得先写状态后才发现非法请求 |
| S2 校准状态可靠性 | analyst calibration、档案提交与reload | ASR不可用默认CER、全合成失败chosen0、旧转写评分、新转写提交、丢失败回执；补真实并发 | 缺失指标null/错误及覆盖率；无有效试验不选；快照与提交版本核验；提交短锁不跨GPU长等待；加载失败显式部分状态；保留Go激活旧active/同pin保护 |
| S3 DSP数值状态 | NumPy Leveler及必要ABI测试 | dsp_partition_probe整块/48/1920/不规则分块；补Rust实测 | 固定淡入总长/累计位置、跨块RMS余数、算法合同与舍入容差；输出样本数守恒；保留软限幅/增益预算；不无证据换默认DSP |
| S4 裁剪有界状态 | EdgeTrimmer和Worker终止路径 | 840样本预滚差、短块被丢、held非零尾；另测实际1920倍数 | 有界残帧与预滚、明确finish/取消；真实非零尾不能无声销毁；尾静音处理可追溯；不删语音冒RTF，不引入整句缓冲 |
| S5 播放排空 | Player.tick/结束与重采样收尾 | playback/latency probe完成20/50ms、starved、51ms、空流；补1样本/取消/真浏览器 | 已结束正长度队列可排空或明确错误；未结束风险缓冲保留；已经播放不强停；自然结束/一次欠载/reset零输出保护；取消不排旧尾 |
| S6 度量与诊断 | Go队列、Worker时序、Player/Worklet与诊断 | 源码queue_wait_ms范围、命令前消费0、不同seed诊断；补协议/旧客户端 | 新字段解释本地时间区间与每次重试；旧字段含义兼容；首PCM/命令/消费/声学分列；缺失null；同文两卡同seed；dropped显式报告 |
| S7 条件透明与真实实验入口 | profile/UI/条件收据 | 单ICL与多prompt批次合同、全部候选评估条目 | 显示各候选角色和实际ICL来源；融合单列实验/未验证，不把单锚点回退称融合；语音模式与pin不静默变化 |
| S8 工程候选包与验收 | repack/copy/checks/docs | 最终源码完整三轮及逐资产对比 | 新建18不覆盖原始–17；固定hash/字节数复制下载；手机/剪贴板拒绝回退；完整备忘录；只可签收有证据的工程范围，所有声学缺口继续显著标明 |

## 单步执行规则

1. 每批先保留同输入失败样例，写预期不变量，再做最小改动。
2. 局部回归、保护案例、差异检查通过才进入下一批；失败日志不得删。
3. 撤销失败方案时仅回滚本批，不能覆盖用户改动、冻结包或前批已通过功能。
4. 性能变化需记录测试条件与全部结果，不能通过静音、删音或重播参考投机。
5. 新库/语言仅按实测热路径引入；现有PyTorch/CUDA、Python、Go、Rust、JS分工保留。

## 不能由本批工程测试替代的声学门禁

- 用户实际录音与实际ICL锚点的正确转写、单一说话人及隐私授权。
- 完整权重、实际同文双卡、每候选/策略、交替长文各至少三轮，保留真实生成WAV。
- 逐字审核和完整朗读盲听：音色、沙沙/点击、齿音/气声、漏添重复及跨段韵律。
- 输入/参考处理/模型PCM/后处理/播放分层对照；能量分位差不是噪声真值SNR。
- 冷/暖、聊天/朗读分列，实际首声/欠载/掉样及worker与wall RTF各自测；RTF>0.3仍失败。
- 无法用有限实验证明绝对零噪声、100%身份或所有代码零错误；未测或失败均不得签通过。

## 下一步

不再为凑数量预填问题28；先完成G0的可审计覆盖与测试映射，然后按S1开始小步修复。若深审引出新的关键设计选择，再按一次一题、先50建议规则追加。本文件是明确待执行合同，不宣称G0或S1已经完成。

## G0第一批进度（非门禁通过）

已建立53资产覆盖与300建议初审映射，全文第一遍6份，完整第二/三遍均未签收。84项专项回归×3和10项原缺陷/保护边界×3完成；细节见G0_AUDIT与G0_DISPOSITION。损坏talker_config及恢复部分提交新增为待处置项，当前未修。下一步继续数据/声码/原始库与发布链深审，S1仍待G0通过后执行。

## G0第二批进度（非门禁通过）

第一遍全文累计18/53、2904行；135项专项×3和6项provider合同×3完成，未测真实Torch/Qwen/GPU。F01：CPU声码编码器在HF-only元数据下查询旧qwen-tts版本，前置重型加载成功后会抛PackageNotFoundError；真实元数据+显式重型fixture已复现。后续最小修复必须使用正确提供包身份，不得并装冲突的旧发行版；当前未修。来源、边界和下一批见G0_TRAINING_CHAIN，S1仍不得绕过G0。

## G0第三批：Go网关与本地协议（未签收）

新增全文第一遍13份/3527行，累计31/53、6431行，剩22项；完整第二/三遍仍0。原Go主测试40项（含子测试56）×3和新增边界10项×3完成；独立竞争见证三轮均预期非零并报告DATA RACE，不能计为无失败套件。确认快照共享map竞争F02及工作帧校验不足F03，均未修复；queue_wait_ms/健康/慢客户端/SSE问题按证据区分源码观察与待验证。

实际本地Go/Python mock播放链、原始库HTTP、合成训练输入HTTP各内部3轮通过；损坏音频预期处理失败、合成WAV快照不等于真实训练。未重跑全部历史6类协议。详细边界见KAGGLE_STEP18_G0_GATEWAY.md，当前覆盖改以g0-gateway-coverage.json为准，历史台账/300建议/Q25–27均保留。下一步补剩余前端、运行分析、DSP/启动恢复等源码及全源第二/三遍，不跳过G0进入S1，不新增18包，不声称模型/双卡声学或性能验收。

## G0第四批：前端录音与流式播放（未签收）

新增全文第一遍3份/2217行，累计34/53、8648行，剩19项；完整第二/三遍仍0。实际Chromium完整浏览器套件134项×3通过（原123+新增11），失败/跳过/retry/flaky均0；新增8保护+3原缺陷观察，不把观察通过说成修复。第1–17阶段完整包逐字节剪贴板保护通过；真实原始文件按冻结hash核对，浏览器原始文件保留用sentinel，不冒称完整原始文件复制。

F04迟到旧录音error误停新会话、F05协议解析失败未显式取消reader/请求、F06音频模块初始化失败未revoke临时Blob URL，在明确设备/网络故障fixture下各三轮复现，均未修。原Player22项/延迟16项VM各三轮，Node30/JS/repack通过；物理麦克风/声卡/真实模型/双卡声学未测。细节见G0_FRONTEND，当前覆盖以g0-frontend-coverage.json为准。继续剩19项Python运行分析/启动恢复/DSP/工具等及全源第二/三遍，不跳G0，不新增18发布包或Q28。

## G0第五批：Python运行/监督/启动与绑定（未签收）

新增全文第一遍5份/1536行，累计39/53、10184行，剩14项；完整第二/三遍仍0。原84项CPU/安全/租约/可靠性+新10边界=94项×3通过，无失败/错误/跳过；新7保护+3原缺陷观察。真实supervisor/FD租约/进程组与致命健康协议两类各内部3轮通过，模型角色均CPU替身，不是实际GPU/训练或完整Kaggle启动。

F07异步响应队列无容量/反压、F08失败重载遗留与接受pin不匹配的prompt、F09clone模式规范化/报告不一致，均以明确CPU fixture复现，未修。真实文件hash及原Worker/RealEngine.load_profile控制流实际执行，重型提取/生成/GPU清理为fixture；不冒称真实错音色或慢客户端内存压力。Node30/JS/Python AST/repack通过，见G0_RUNTIME。当前覆盖以g0-runtime-coverage.json为准；下一步补剩14项分析/API/参考切分/DSP/工具/说明及全源第二/三遍，不跳G0，不新增18发布或Q28。


## G0第六批：分析/API、参考切分与Python/Rust DSP（2026-10-23）

完整报告见 `docs/KAGGLE_STEP18_G0_ANALYSIS_DSP.md`。全文第一遍新增6份2152行，累计45/53、12336行，剩8份；完整第二/第三遍仍0。172项专项×3轮全通过（旧160+新12，新9保护/3原行为观察），每轮失败/错误/跳过0；另14个分析AST案例与12个NumPy合成DSP案例各三轮，不等于全功能/全模型验收。新F10极短NumPy breath形状、F11窗口重转写词信息漏清洗、F12分析端失败/残缺流被接受，均未修复。F12实际requests+本地TCP；F11为显式ASR metadata fixture。旧校准/候选/诊断及分块依赖仍复现；历史上游cache缺失，本次未重跑6个prompt接口案例，不改写历史20案例收据。Rust两份只完整读源码，缺rustc/cargo，未编译/执行，不冒用NumPy代替。Node30/JS/Python AST/repack检查通过。原300建议、问题25–27各50、53源/94冻结/15正式与本批开始295历史文件hash保持；旧验证器保持历史版本，当前检查用verify_analysis.py。无产品改动、无18包、无真实训练/完整模型/GPU/用户WAV/物理声卡/提速/无沙沙或相似度验收。继续第一遍剩6工具与LICENSE/MEMO，再补全源第二/三遍和失败映射；整体PARTIAL/BLOCKED，不开问题28、不要求Continue。


## G0第七批：工具/LICENSE/MEMO，内嵌53资产第一遍补齐（2026-10-23）

完整报告 `docs/KAGGLE_STEP18_G0_TOOLS.md`。新增全文8份1332行，累计53/53、13668行，第一遍剩0；完整第二/第三遍仍0，G0不签收。197项专项×3轮通过（上批172+既有probe13+新12；新9保护/3原行为见证），每轮失败/错误/跳过0。另每轮4实际CLI合同，backend静态/runtime、默认无--run的benchmark均按预期exit2/BLOCKED；resource status exit0，不冒充模型通过。F13 E2E缺gpu/failed END/奇数PCM/残留误PASS，F14 watermark空HTTP503/ERR/残缺帧的零音频误PASS，F15 selftest failed/cancelled Mock统计流误PASS，均真实本地HTTPfixture三轮确认未修；F15时间是确定性fixture，不是性能实验。D01记录MEMO页头step15/xvector/maxgain12与当前17 ICL/maxgain6漂移，冻结MEMO不改。LICENSE全文读完不等于法律/依赖/权重/语音授权签收，NOTICE来源待证。Node30/JS/全部产品Python AST/repack通过；本批开始329历史文件hash保留，53源/94冻结/15正式不变，当前覆盖g0-tools-coverage.json，检查verify_tools.py。没有Rust/完整模型/GPU/真实训练/声学/提速验收，无产品改动或18包。下一步全源第二遍、第三遍交叉反证与300建议最终映射，不预填Q28，不要求Continue。


## G0全源第二遍第1批：训练执行与资源所有权（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS2_TRAINING.md`。8份重新全文阅读1056行并交叉复核CLI/controller/rank、OFD/码租约、准入/取消/原子产物、dataset/JointLoss/LoRA；第二遍累计8/53、1056行、剩45，第一遍53/53/13668保持，第三遍0。局部查看training_codes/encode_training/supervisor不计第二遍全文。219项×3轮全通过（旧197+另选既有artifact10+新12，新11保护/1原行为见证），失败/错误/跳过0。F16原stop_ranks在leader退出后漏清理忽略SIGTERM的额外后代，实际CPU进程/pidfd/OFD/flock复现，未修；测试finally定向清理并验证锁释放。额外后代为明确fixture，生产run_rank无DataLoader子进程，不声称真实训练出现此故障。AST仅运行纯Python采样、commit赋值回滚、dataset构造/len，无Torch算子模拟，无tensor/optimizer/Gloo/NCCL/完整Qwen/GPU/声学或提速验收。Node30/JS/全产品Python AST/repack通过。382历史文件hash、53源/94冻结/15正式、300建议初审与Q25–27各50保持；当前g0-pass2-training-coverage.json与verify_pass2_training.py。无产品改动/18包，G0仍BLOCKED；继续其余45项第二遍及全源第三遍/最终处置映射，不跳S1/Q28，不要求Continue。


## G0全源第二遍第2批：来源/声码/产物与恢复认证（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS2_STATE.md`。7份重新全文阅读1526行（voice_library/training_data/training_codes/trained_profiles/persist/qtts_common/access_control），第二遍累计15/53、2582行、剩38；第一遍53/53/13668保持，第三遍0。analyst候选函数仅局部，不计全文。324项×3轮全部通过（旧219+另选既有93+新12，新11保护/1原行为观察），各轮失败/错误/跳过0。预检曾因测试提取器保留装饰器报1个NameError，已仅修测试、保留原失败日志，最终预检12通过。F17：原pack目录枚举后切换候选，可收新版profile.json却漏新锚点，本地原解包接受后引用缺失；真实tar/文件与原候选AST函数体执行，worker reload/admission明确fixture，确定性交错非HTTP/线程压力或远端Kaggle。新缺陷未修，F01/F16及旧恢复部分提交等问题仍保留。代码/来源封存、取消/IO回滚/同OFD、隐私scope/auth转发及真实safetensors合成结构专项通过，不是Torch/optimizer/DDP/NCCL/真实编码/长训练/完整模型/GPU/声学/提速验收。Node30/JS/AST38/repack通过；408历史hash、53源/94冻结/15正式、300初审及Q25–27各50不变。当前覆盖g0-pass2-state-coverage.json，当前检查verify_pass2_state.py；完整交接增至73份原文。无产品改动/18包，G0仍PARTIAL/BLOCKED；继续剩38项第二遍及全53第三遍/最终处置，优先provider/binding/worker/分析API版本与取消/失败链，不跳S1/Q28、不要求Continue。


## G0全源第二遍第3批：provider/绑定与推理生命周期（2026-10-23）

完整报告 `docs/KAGGLE_STEP18_G0_PASS2_INFERENCE.md`。qwen_compat/voice_binding/worker/clone_stream/adapter_engine全文5份1071行，第二遍累计20/53、3653行、剩33；第一遍53/53/13668保持，第三遍0。新12（11保护/1观察）加旧324=336项×3通过，失败/错误/跳过0；ASGI2.3独立观察1×3另列。新F18原synth在正文迭代前启动生产线程，响应头阶段断连未进入generator finally，cancel未传给生产；ASGI2.4 send异常和ASGI2.3 receive disconnect两条真实Starlette响应路径三轮确认未修。断连时序/CPU工作负载明确fixture，非TCP/浏览器/模型/GPU证明，finally已定向清理join自有线程。旧F01–F17仍保留。新保护含FIFO/nonblock、绑定/预算、真实锁排队取消、重放迭代器close、RoPE异常/registry、trained磁盘重绑定/删除/链接/预算；最小manual_seed模块替身不是Torch算子或真实codec。临时venv未保留后重建固定关键CPU版本，保存安装日志/freeze，不声称全部传递依赖相同。Node30/JS/AST39/repack通过；435历史hash、53源/94冻结/15正式、300初审与Q25–27各50不变。当前覆盖g0-pass2-inference-coverage.json与verify_pass2_inference.py；交接74份全文。无产品改动/18包/真实训练/模型/双GPU/声学/提速验收，G0仍PARTIAL/BLOCKED。下一批分析/API/参考切分与版本/校准/取消失败链，继续剩33份第二遍和全53第三遍/最终映射，不跳S1/Q28、不要求Continue。


## G0全源第二遍第4批：分析/API、参考切分与校准所有权（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS2_ANALYSIS.md`。analyst/library_api/reference_segments全文3份1480行，第二遍累计23/53、5133行、剩30；第一遍53/53/13668保持，第三遍0。348项（旧336+新12，新10保护/2观察）×3全通过，各轮失败/错误/跳过0。F19两个同档案真实ASGI校准请求经原HEAVY(2)/calibrate，共用临时id；A删除后B原Mock Worker加载缺失，错误结果覆盖成功记录，均200；F20重载期间实际删除档案，原终检跳过None，原reload_response仍200/已保存。两项确认未修；worker transport/合成/ASR/声纹明确fixtures，不是TCP/真实模型/双GPU/删除后播放证明，临时资源/槽位清理通过。参考分析最多24预排/3落盘/单锚点条件区分清楚，不称Qwen融合或训练；新17秒长手工文本/20秒低能量窗口是合成控制流，不是真长数据训练。旧F01–F18及专题问题保留。Node30/JS/AST38/repack通过；470历史hash、53源/94冻结/15正式、300初审/Q25–27各50不变。当前g0-pass2-analysis-coverage.json与verify_pass2_analysis.py；交接75份原文。无产品改动/18包/真实模型/训练/GPU/声学/提速验收。下一批启动/监督/backend preflight，继续剩30份第二遍、全53第三遍及最终映射，G0仍PARTIAL/BLOCKED，不跳S1/Q28、不要求Continue。


## G0全源第二遍第5批：启动、监督与backend preflight（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS2_STARTUP.md`。bootstrap451/supervisor219/backend_probe200全文3份870行，第二遍累计26/53、6003行、剩27；第一遍53/53/13668保持，第三遍0。360项（旧348+新12，新10保护/2观察）×3通过，各轮失败/错误/跳过0。F21原sh在leader退出而后代持stdout时timer跳过killpg，超过请求期限并在外部清理后返回0；真实CPU/pipe/timer/pidfd、观察包装确定性交错，后代退出已验证，非完整bootstrap/性能证明。F22原watch的fatal回执写失败跳过kill/gave_up，HTTP每轮清零使8轮后fail_count仍1；health/IO/process/wait明确fixtures，非真实GPU或磁盘故障。两项未修，F01–F20保留。标准faster启动全部PINS逐项预查/精确安装/constraints0600与清理/Torch变更拒绝、probe先于下载的控制流测试通过；未执行真实pip resolver或GPU，后安装漂移/独立入口/native-adapter仍待证，surface preflight不是质量签收。Node30/JS/AST38/repack通过；497历史hash、53源/94冻结/15正式、300初审与Q25–27各50保持。当前g0-pass2-startup-coverage.json、verify_pass2_startup.py及progress-pass2-startup.json；交接76份原文。无产品修改/18包/真实训练/模型/双GPU/声学/提速验收。继续剩27份第二遍，优先网关调度/流协议/取消/超时及前端排空交叉核对，再全53第三遍/最终映射；G0仍PARTIAL/BLOCKED，不跳S1/Q28、不要求Continue。


## G0全源第二遍第6批：网关调度/流协议/取消与激活终检（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS2_GATEWAY.md`。main/scheduler/session/segmenter/llm全文5份2286行，第二遍累计31/53、8289行、剩22；第一遍53/53/13668保持，第三遍0。每轮Go原40主测/含子测56、旧专项10、新13（11保护/2观察）通过，合计63主测/79含子测×3；Python旧360×3通过，无新增Python测试。通过套件无失败/跳过/race warning；独立F02竞争见证每轮预期非零/DATA RACE，未混入通过数。F23原healthLoop接受HTTP503 ready=true，原网关报告两worker健康；真实本地HTTP，永久循环隔离于自有Go子进程并核对退出。F24原activate期间实际改profile.model_output_mode，最终conditioning改变而binding相同，仍200/提交active；worker回执为HTTP fixture，无真实训练产物/模型/后续合成。两项未修，F01–F22和专题问题保留。实际Go1.23.9新增于忽略venv，安装报告/wheel SHA与可执行hash保存；freeze仅多go-bin==1.23.9，其余依赖保持，不称全部freeze相同。Node30/JS/AST38/repack/原Go及新探针副本vet/gofmt通过；525历史hash、53源/94冻结/15正式、300初审及Q25–27各50不变。当前g0-pass2-gateway-coverage.json、verify_pass2_gateway.py及progress-pass2-gateway.json；交接77份原文。无产品修改/18包/真实DeepSeek/Qwen/训练/双GPU/声学/提速签收。继续剩22份第二遍，优先前端流终止/取消/遥测/完成排空，再DSP/工具/剩余Go安全和测试；全53第三遍及最终映射仍待完成。G0仍PARTIAL/BLOCKED，不跳S1/Q28，不要求Continue。


## G0全源第二遍第7批：前端终态/取消/排空与遥测（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS2_FRONTEND.md`。app1715/recorder358/index144全文3份2217行；HTML首次合并输出截断，已补读全范围，第二遍累计34/53、10506行、剩19；第一遍53/53/13668保持，第三遍0。新增浏览器12（10保护/2观察）预检通过，既有134+新12=146×3全部通过，失败/跳过/flaky/retry0；Player VM22/延迟VM16各三轮、CPU旧360×3通过，无新增Python测试。本批未重跑Go79/独立F02竞争见证或独立ASGI2.3/旧CLI矩阵，不挪用历史数字。F25原完整前端脚本END后仍收PCM/文本且第二END替换首汇总；F26网络EOF先发report并停telemetry，随后play/欠载UI变化不更新报告；真实Chromium原生流/DOM/timer，网络/设备/Worklet状态明确fixtures，非物理播放、真实欠载或声学/提速。两项未修，F01–F24及<=50ms已完成短尾/旧DSP等保留。Node模块按冻结lockfile npm ci恢复，未改lock；venv freeze与上批相同，无新Python依赖。Node30/JS/AST38/repack/前端探针语法检查通过；575历史hash、53源/94冻结/15正式、300初审及Q25–27各50保持。完整交接78份原文；当前g0-pass2-frontend-coverage.json、verify_pass2_frontend.py与progress-pass2-frontend.json。产品未改/18未发/真实DeepSeek/Qwen/训练/双T4/声学/提速未签收。下一批Python/Rust DSP和工具自检，再余Go安全/测试与LICENSE/MEMO；继续剩19份第二遍、全53第三遍/最终映射。G0仍PARTIAL/BLOCKED，不跳S1/Q28、不要求Continue。


## G0全源第二遍第8批：DSP与工具（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS2_DSP.md`。Python/Rust DSP及6工具全文9份1500行，第二遍累计43/53、12006行、剩10份1662行；第一遍53/53/13668保持，第三遍0。CPU372（旧360+新12，新10保护/2观察）×3全部通过，失败/错误/跳过0；NumPy分块12、原EdgeTrimmer AST8各三轮，旧问题未修；4个独立CLI合同×3，backend静态/runtime及默认benchmark按预期exit2/BLOCKED，resource status exit0，阻塞不是模型成功。F27 NumPy flush未清DC状态，常量480→flush192→零240得到240非零/峰6026，fresh为0；Rust源码清DC但未编译执行，正常worker每job重建Leveler，因此不是当前沙沙声根因证明。F28原benchmark/measure两实际HTTP端点health分别GPU0/1、18测量均GPU0，仍real_gpu_verified/speed_target_passed true；health/stats/PCM/clock明确fixtures，报告true是被反证输出，不是硬件/RTF成绩。两项未修。Node30/JS/产品Python AST/新审计语法/repack通过；625历史SHA、53源/94冻结/15正式、300初审及Q25–27各50保持。freeze与前端相同，无新依赖；Rust/Torch/Qwen/实际训练/双GPU/声学/提速未验。本批不重跑浏览器/Player VM/Go/独立F02/ASGI2.3，不挪用历史成绩。完整交接79份；当前g0-pass2-dsp-coverage.json、verify_pass2_dsp.py与progress-pass2-dsp.json。产品未改/18未发；下一批剩余Go安全/测试/go.mod和LICENSE/MEMO共10份，再全53第三遍及300最终映射，G0仍PARTIAL/BLOCKED，不跳S1/Q28，不要求Continue。


## G0全源第二遍第9批：安全与全文收尾（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS2_SECURITY.md`。剩余Go安全/测试/go.mod及LICENSE/MEMO全文10份1662行，第二遍累计53/53、13668行、剩0；第一遍53/53/13668保持，第三遍0。这是冻结包53资产，不是全Git仓库或三遍/全功能完成。每轮Go原40主测/含子测56、旧10、上批13、新12（10保护/2观察），合计75主测/91含子测×3通过；CPU旧372×3通过，无新Python测试；失败/错误/跳过0，通过集合无race warning。独立F02每轮预期非零/DATA RACE，不混入通过数，未修。三轮副本vet通过。F29原guard/decodeJSON/validateSpeak接受孤立高低代理项或非法UTF8，解码成a�b后返回200；实际本地HTTP组合校验handler，非完整合成或认证绕过。F30原授权speak/LLM错误链将HTTP401替身正文回显的配置假密钥带入ERROR/END/metrics；密钥/供应商均synthetic，非真实泄密事件或未授权读取。两项未修。LICENSE全文阅读不等于依赖/模型/数据/NOTICE法律签收；MEMO step15/xvector/maxgain12漂移仍为D01，冻结不改。Node30/JS/产品与新审计Python AST/repack/Go探针gofmt通过；686历史SHA、53源/94冻结/15正式、300初审及Q25–27各50保持。Go沿用、freeze与DSP相同，无新依赖；无Rust/Torch/Qwen/完整模型/真实GPU/训练/声学/提速签收。本批未重跑独立CLI/NumPy与trimmer探针/ASGI2.3/浏览器与Player VM，不挪用旧成绩。完整交接80份；当前g0-pass2-security-coverage.json、verify_pass2_security.py与progress-pass2-security.json。产品未改/18未发；下一步第三遍全源跨层输入/pin/错误、生命周期/取消/播放/训练绑定审查及300最终映射，G0仍PARTIAL/BLOCKED，不跳S1/Q28，不要求Continue。


## G0全源第三遍第1批：输入与内容绑定（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS3_INPUT.md`。main478/security247/session692/qtts_common211/voice_binding60/resource_limits172/access_control70重新全文7份1930行，第三遍7/53、剩46份11738行；第一、第二遍各53/53/13668保持。browser和library_api只局部调用点不计第三遍。新增Go6（5保护/1观察）及Python6（5保护/1观察），预检各6通过；每轮Go81主测/97含子测×3、CPU378（旧372+新6）×3通过，失败/错误/跳过0，通过集合无race warning；独立F02三轮预期非零/DATA RACE不计通过，三轮副本vet通过。实际Go/Python8合法pin与12非法generation向量、两worker ack期间generation变更拒绝、空/错text拒绝、内容pin非身份、上传预算+1、spool清理、原子JSON失败、参考增长拒绝、两认证进程一致性均有明确边界。F31同磁盘top_k:null被Go转0并得pin而Python拒绝；F32认证token FIFO无writer时open先于fstat阻塞，普通文件control通过，外部定向终止并reap自有子进程；两项未修，无真实凭据/模型/错误音色或远程利用证明。原8条建议仅部分证据映射，300与Q25–27各50不改/不签收。739历史SHA、53源/94冻结/15正式保持；Node30/JS/AST/repack/gofmt/vet通过，freeze与第二遍收尾相同，无新依赖。旧S2 F29/F30随套件重跑仍未修；本批未跑浏览器/VM/独立CLI/ASGI2.3/分块裁剪探针，不挪用历史成绩。完整交接81份；当前g0-pass3-input-coverage.json、verify_pass3_input.py及progress-pass3-input.json。产品未改/18未发；无Rust/Torch/Qwen/实际训练/双T4/声学/提速签收。下一批第三遍参考分析/API/档案修改与备份事务，继续剩46份及300最终映射；G0仍PARTIAL/BLOCKED，不跳S1/Q28，不要求Continue。


## G0全源第三遍第2批：参考与档案事务（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS3_REFERENCE.md`。analyst1211/library_api163/persist99/reference_segments106/voice_library351第三遍完整5份1930行，累计12/53、3860行、剩41份9808行；前两遍各53/53/13668保持。新12（10保护/2观察）预检通过，CPU390（旧378+新12）×3全部通过，失败/错误/跳过0。F33真实两CPU线程占满原HEAVY，原text/candidate ASGI先写盘改pin再429，不reload且不报reference_saved；F34原校准评估旧转写，在结束提交前实际text ASGI改pin仍200，随后calibrate保存旧评分到新档案仍200；临时目录/线程/槽清理核对。模型/ASR/speaker/worker ack为fixtures，无真实音质/错误音色证明，两项未修。复制失败旧pin保护、JSON失败仍遗留孤立anchor明确不称全回滚；trained三入口409、原库snapshot异常/顺序/只读与租约、稳定pack/extract字节pin、归档末尾非法成员先拒绝、DELETE重复revision、24秒可信词切分保护通过。原300本批10条部分链接、与前批去重16个ID，均未最终签收；原文/Q25–27各50保持。795历史SHA、53源/94冻结/15正式保持，Node30/JS/AST/repack通过，freeze与前批相同无新依赖。本批未跑Go/F31/独立F02/浏览器VM/独立ASGI2.3/CLI/分块裁剪探针，不挪用历史成绩。交接82份；当前g0-pass3-reference-coverage.json、verify_pass3_reference.py及progress-pass3-reference.json。产品未改/18未发；无Rust/Torch/Qwen/实际训练/双T4/声学/提速签收。下一批第三遍训练输入/码/训练产物绑定与取消/提交，继续余41份及300最终映射；G0仍PARTIAL/BLOCKED，不跳S1/Q28，不要求Continue。


## G0全源第三遍第3批：训练来源与产物提交（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS3_TRAINING.md`。training_data285/training_codes355/training_job227/tts_training200/tts_dataset125/trained_profiles155/encode_training128/trained_voice30全文8份1505行，第三遍累计20/53、5365行、剩33份8303行；前两遍各53/53/13668保持。首组源码输出截断后完整补读。首次测试43项因导入TestCase重复31项，1失败为误判正常.lock；改模块导入与断言，保留首错/说明，预检新12通过。初行数误算1605被信用断言拦住未写错误coverage，逐项纠正1505/5365/8303并留记录。CPU402（旧390+新12，新11保护/1观察）×3全部通过，失败/错误/跳过0。F35原控制器在两个真实CPU替身rank0退出且adapter仅含manifest.json={}时仍completed/optimizer_execution_observed=true，原TrainedArtifacts.inspect409拒绝，信号/租约恢复；训练准入/依赖/tokenizer门禁与rank实现明确替身，原GPU/code OFD adopt实际执行，无Torch/优化器/训练/非法声音发布或正常rank产生坏检查点证明。F35未修，F01–34/D01保留。新保护包括输入BaseException回滚、PCM极值36001帧、codes最终取消、encoder第二样本中断、finish-only pin、adopt最后OFD、cancelled产物拒绝、来源/NaN拒绝、发布末次重核/固定参考文本/active不变及新trained_voice CLI错pin脱敏拒绝；发布codes lease元数据/adapter为fixtures，不能签收真实训练。原300本批7部分链接，与前两批去重22ID，均未最终签收；Q25–27各50保持。825历史SHA、53源/94冻结/15正式保持；Node30/JS/AST38/repack通过，freeze与上批相同无新增依赖。本批未跑Go/F31/独立F02/浏览器VM/独立ASGI2.3/额外四CLI/分块裁剪矩阵，不挪用历史成绩。交接83份；当前g0-pass3-training-coverage.json、verify_pass3_training.py及progress-pass3-training.json。产品未改/18未发，无Rust/Torch/Qwen/实际训练/双T4/声学/提速签收。下一批第三遍adapter/推理/provider兼容与缓存/失败取消，继续余33份及300最终映射，G0仍PARTIAL/BLOCKED，不跳S1/Q28、不要求Continue。


## G0全源第三遍第4批：推理与生成资源清理（2026-10-23）

报告 `docs/KAGGLE_STEP18_G0_PASS3_INFERENCE.md`。adapter_engine108/lora_adapter91/qwen_compat97/clone_stream126/gpu_ownership151/worker680/train_tts49重新全文7份1302行，无源输出截断，worker连续四段；第三遍累计27/53、6667行、剩26份7001行；前两遍各53/53/13668保持。新增12（11保护/1观察）预检一次通过；CPU414（旧402+新12）×3全部通过，失败/错误/跳过0。F36原generated_only_stream在consumer关闭已启动生成器时，上游close替身抛异常，后续window.finish被跳过；生成器frame本身关闭，测试捕获的真实window仍closed false/pending1920/合成code标记，最后显式清理完成。准备/predictor/decoder/Torch上下文均控制替身、无tensor模拟，没有证明生产上游会抛错或正常GC后持续GPU内存泄漏/沙沙根因，F36未修。adapter来源不符先拒绝、cached仍核验实际safetensors字节、取消前不选择与取消后丢弃返回PCM、native rate/shape/NaN/长度拒绝与单句输出、回放指标合计、worker部分生成失败解锁/后续成功、同pin缺prompt重载、RoPE重试cause/注册表、真实短pwrite释放OFD均保护通过；LoRA prepare/commit和native模型未执行。F01–35/D01保留，旧ASGI/CLI/信号/CPU持有者见证随集合重跑，不代表真实模型。原300本批7部分链接，累计去重27ID，均未最终签收；Q25–27各50保持。858历史SHA、53源/94冻结/15正式保持；Node30/JS/AST38/repack通过，freeze与上批相同无新依赖。未跑Go/F31/独立F02/浏览器VM/独立ASGI2.3/额外四CLI/分块裁剪矩阵，不挪用历史成绩。完整交接84份；当前g0-pass3-inference-coverage.json、verify_pass3_inference.py及progress-pass3-inference.json。产品未改/18未发，无Rust/Torch/Qwen/实际训练/双T4/声学/提速签收。下一批第三遍启动监督/preflight/资源测量工具与DSP接口，继续余26份及300最终映射，G0仍PARTIAL/BLOCKED，不跳S1/Q28、不要求Continue。

## 第三遍第5批：启动监督、工具与DSP接口

报告 `docs/KAGGLE_STEP18_G0_PASS3_STARTUP.md`。11份2253行全文复读；累计38/53、8920行，剩15份4748行。CPU426（旧414+新12，10保护/2观察）×3全部通过，失败/错误/跳过0；另NumPy分块12、trimmer8、实际CLI4各三轮，CLI中3项每轮期望blocked而非模型成功。首预检12项中1 error为测试误访问UploadRejected.status，纠正为code后12通过，首错/修正留档。F37原preflight父控制器接受真实CPU替身child exit23写出的合法形状成功回执；生产者明确替身，不证明实际GPU误通过。F38已有系统cc编译仅rt_version的C共享库，真实ctypes在ABI3缺rt_leveler_new抛AttributeError中止import，ABI2及显式NO_RUST为NumPy；不是Rust编译/运行或正式Rust库损坏证明。两项未修，产品不改。887历史SHA、53源/94冻结/15正式保持；原300本批7部分链接、累计33unique，Q25–27各50不变，最终处置仍false。Node30/JS/AST38/repack新执行；无新Python/系统依赖，freeze不变。未跑Go/race/vet/浏览器VM/独立ASGI2.3，未跑Torch/Qwen/实际训练/双T4/声学或提速。交接85份；最新coverage/verifier/progress为pass3-startup。继续余Go10/web3/LICENSE/MEMO及300最终映射，G0与整体PARTIAL/BLOCKED，不跳S1/Q28/18发布，不要求Continue。

## 第三遍第6批：网关调度、LLM流与文本保留

报告 `docs/KAGGLE_STEP18_G0_PASS3_GATEWAY.md`。剩余Go10资产2110行全文复读，累计48/53、11030行，剩5份2638行（web3份2217/LICENSE201/MEMO220）；前两遍各53/13668保持。新增Go12（10保护/2观察）race预检通过，首编译错因测试误用submitted，已改为真实字段allSubmitted、首错留档；另一次审计元数据括号SyntaxError解析前阻止全部写入，拆开后纠正留档。Go原40+G0十+P2十三+security十二+input六+新十二＝93顶层/109含子测试×3正常通过，意外fail/skip/race0；独立F02 race×3预期非零、仍未修，vet×3通过。CPU完整继承426×3＝1278 PASS，failure/error/skip0，无本批新增Python合同；另NumPy分块12/trimmer8/实际CLI4各三轮，3项CLI每轮期望blocked非GPU成功。F39原Live PreserveText把你好。!?重连成你好。及丢独立空白/标点尾段，非语词漏读或沙沙根因证明；F40原run在活ctx下接受替身cancelled=true stats＋偶数PCM，served1/failed0，非真实生产取消或GPU漏音证明。两项未修；F01–38/D01保持。chat system/history/预算、SSE CRLF/末行无换行/流内错误脱敏、正常read Unicode保字/seed、retry上限、urgency/FIFO、EMA与chunk2/6/pin转发保护通过，非200正文F30仍在。953历史SHA、53源/94冻结/15正式保持；原300本批7部分链接、累计38unique，Q25–27各50/最终处置不变。Node30/JS/AST38/gofmt/repack新执行，无新Python/系统依赖、freeze不变；CPU继承C ABI故障注入不冒称Rust，无Rust/Torch/Qwen/CUDA/真训练/双T4/声学/提速。本批未跑真实浏览器/VM/独立ASGI2.3，不挪用历史成绩。交接86份，最新pass3-gateway coverage/verifier/progress。产品未改/18未发，下一批web完整阅读与实浏览器、另许可/MEMO及300最终映射；G0与整体PARTIAL/BLOCKED，不跳S1/Q28，不要求Continue。

## 第三遍第7批：web、录音与播放／界面状态

报告 `docs/KAGGLE_STEP18_G0_PASS3_FRONTEND.md`。app1715/index144/recorder358完整复读3份2217行，第三遍累计51/53、13247行，剩LICENSE201/MEMO220共2份421行；前两遍各53/13668保持。浏览器158（原146+新12，10保护/2观察）×3＝474 PASS，失败/flaky/skip/retry0；CPU完整继承426×3＝1278 PASS、failure/error/skip0，无新Python合同；另VM22/16、NumPy分块12/trimmer8/实际CLI4各三轮，三CLI每轮期望blocked不是模型成功。F41停止已abort且hold/reset，注入迟到fixture Worklet st使原player发play/UI playing，不证明真实原生Worklet竞态/物理漏音；F42同accessEpoch、候选mutation0→1、合成profiles响应1→0，使原UI高亮从1回0，不证明实际backend回滚或错声音。两项均未修，旧F01–40/D01保持，每轮保留F04/05/06/25/26观察。新保护含resume中取消、精确File字节/边界、start抛错/权限迟拒绝、policy帧、401锁定、超长帧头、正常完成排空、三份冻结web完整文本原生clipboard且不额外save、最近六完整chat回合；继承真实振荡器/静音录音与完整17包复制/权限回退。浏览器API为fixture，临时E2E workbench不是正式HEAD。首预检11/1为旧recorder-only壳缺charset导致中文乱码，仅新审计壳UTF-8重载后12通过，原断言/旧fixture/产品不改，首错留档。1051历史SHA、53源/94冻结/15正式保持；原300本批7部分链接、累计45unique，Q25–27各50/最终处置false不变。Node30/JS/AST38/repack新执行，freeze/lock不变，无新Python/系统依赖或npm重装；C ABI故障fixture非Rust。本批未跑Go/race/vet/独立ASGI2.3，不挪用历史结果。交接87份，当前pass3-frontend coverage/verifier/progress。产品未改/18未发，物理麦克风/扬声器/真DeepSeek/模型/实际训练/双T4/声学/提速未验。下一步剩2份第三遍及原300最终映射；G0与整体PARTIAL/BLOCKED，不跳S1/Q28，无需Continue。

## 第三遍第8批：许可／MEMO收尾与原300缺口矩阵

报告 `docs/KAGGLE_STEP18_G0_PASS3_CLOSURE.md`。LICENSE201/MEMO220全文复读2份421行，三遍各53/53、13668行，剩0；只关闭53内嵌资产源码阅读子项，不是整个Git仓库或零缺陷验收。原300逐项复核并生成完整gap矩阵，原分类23限定缺陷建议/96保留/89文档合同/55真实条件阻塞/37待证保持；三遍7个链接文件53条记录去重45项，255无该组专用链接不等于无历史证据，最终签收0/300，逐条下一动作／来源／计划合同与边界保存。D01历史MEMO step15/xvector/12dB与冻结17默认ICL/6dB漂移不改；本批AST实际调用原conditioning和output_max_gain_db默认／显式／拒绝路径，不是模型或音量测量。D02新增证据可用性缺口：1139期待历史文件中1136可读SHA匹配、变更0，3份旧.log缺失且匹配*.log忽略规则，预期SHA保留、内容不补造、full_historical_integrity_passed=false。冻结53源/94文件/15正式与HEAD仍保持。旧.venv/node_modules/Go/Rust当前不存在，先期环境／严格历史检查错误留档，改用系统Python标准库、无依赖安装。新12收尾审计合同×3＝36 PASS、Node30×3＝90 PASS，无失败/错误/跳过；JS/repack/AST38各三轮通过。旧158×3浏览器原始JSON只重新解析／核SHA，不是本批重跑；未跑CPU426/Chromium/Go/race/vet/模型/训练/双T4/物理音频／声学／性能，无功能修复、无18包；LICENSE/NOTICE/依赖模型及声音授权未签收。交接88份，当前pass3-closure coverage/verifier/progress。下一步原300逐条最终审查处置及精确测试映射、D02从可信来源找回或有环境后另存新执行收据。G0与整体仍PARTIAL/BLOCKED，不跳S1/Q28，直接继续无需Continue。

## G0第9批：300处置说明与限定失败观察绑定

报告 `docs/KAGGLE_STEP18_G0_DISPOSITION_REVIEW.md`（附录完整300条原建议及逐条说明）。原3轮100项分别补写行动／边界，review_disposition_recorded300/300；原分类23限定修复/96保留/89文档合同/55真条件阻塞/37先调查不变，原final_disposition/test/fix与新functional_acceptance全false，功能及最终签收仍0/300，说明归档不等于G0完成。23原限定缺陷建议手工绑定历史3轮69个JSON Pointer观察（有重复、不算新实验或23新bug），收据／源码／当前相关probe SHA及历史身份是否有记录分别保存；R1-016只相关校准文本交错，NaN未在旧payload，DSP早期未记probe_sha不补造。原45部分链接与23绑定交集3、并集65，235未进入这两组不等于无其他证据。53内嵌资产三遍各13668行保持。D02按3预期SHA搜索当前仓库非.git且<=2MB文件并查git log --all，无同SHA或当前可用提交，未查远端／仓库外；1183历史期待项中1180可读SHA匹配、变更0、3旧.log仍缺，全历史完整性false，不拿新日志充旧字节。新24审计（继承收尾12+新增12）×3＝72 PASS、Node30×3＝90 PASS，JS/repack/AST39各3轮通过，新预检12首次通过，无失败/错误/跳过。系统Python标准库，未装依赖／未重建环境；历史失败仅重读，未跑CPU426/Chromium/Go race/vet/Rust/模型/训练/双T4/物理音频／声学／性能。产品未改，94冻结/15正式及HEAD保持；交接89份，当前g0-disposition-review.json、disposition-failure-bindings.json、verify_disposition.py与progress-disposition.json。下一步按S1非法/缺省/NaN真实HTTP等合同精确映射，补相关而不完整的并发见证，D02从可信源恢复或另存新执行收据。G0与整体PARTIAL/BLOCKED，不跳S1/Q28或18发布，保留全部用户未豁免要求，直接继续无需Continue。

## G0第10批：真实TCP的S1输入边界与CPU继承

报告 `docs/KAGGLE_STEP18_G0_INPUT_HTTP.md`。新Uvicorn原analyst.app+httpx走真实127.0.0.1临时TCP，不是TestClient/AST；生命周期off、worker ACK及合成profile明确fixture，不是Go鉴权或模型。CPU438（原426+新12，7保护/5未修观察组）×3＝1314 PASS，failure/error/skip0；原426逐ID/结果及16旧观察完全继承，新5组后观察21。每轮61请求、合计183；各轮200×19/500×16/400×16/422×6/404×1/409×3，500为未修见证非功能成功。I01 bool/float/string强转；I02容器/非法串/NaN/±Infinity/1e309及顶层非有限500；I03缺省0/重复键最后/未知忽略；I04非字符串转写str化、surrogate500但原文件保留；I05损坏candidates与预装父路径/符号链接file接受，所有字节在自有临时树，不证明公开远程任意文件读取／模型接受。合法候选字节/转写/pin、合法Unicode、越界/缺档、有限非对象422、trained三入口409、library严格JSON400、HEAVY槽恢复保护。新12预检首次通过，探索原JSON保存；检查脚本误用id字段（实际test）的KeyError留档，测试/产品未改、三轮非失败。另NumPy12/trimmer8/实际CLI4各三轮，三CLI期望blocked/resource gpu_verified=false；24审计/Node30/JS/repack/AST39各三轮通过。重建忽略venv并装历史固定Python依赖，freeze精确旧记录去掉故意未装go-bin；NumPy2.2.6非requirements2.4.6，无Go/Rust/npm/Torch/Qwen/模型安装；C ABI fixture非Rust。本批新12建议精确testID/三轮case下标+SHA部分链接，有限证据并集70、230未入这些集合不等于无其他证据，原300/3×100处置/Q25–27各50保持，最终/功能签收0。53资产三遍13668行/94冻结/15正式不动；历史1228期待1225匹配/变更0/3旧.log D02仍缺，不以新日志冒旧内容。无浏览器/Go race/vet/真实模型/训练/双T4/实体音频/声学性能验证，产品未改/18未发。完整交接90份，当前input-http links/verify_input_http.py/progress-input-http.json。G0与整体PARTIAL/BLOCKED，不跳S1/Q28；后续版本冲突与候选/文本/校准组合及剩余逐条映射，不承诺一定成功，直接继续无需Continue。


## G0第11批：版本／校准真实TCP组合（未实施产品优化）

新增12项=8保护/4未修观察，单Uvicorn事件循环真实HTTP、HEAVY线程Event控制交错，原reload/calibrate实际执行，worker/ASR/speaker/synth为替身。首次预检12PASS；CPU450×3PASS、failure/error/skip0，旧438逐ID/结果继承；每轮85TCP、三轮255，其中新增24/轮共72。普通候选/文本重叠旧reload有pin503保护；校准旧评分仍可在真实HTTP编辑之后200保存（新转写未被覆盖）。另满额429前写盘、同名候选bytes变更后未重评、自有profile真实DELETE后校准500而未复活。文件变更非HTTP上传，非声学/实际错声音证明。新12原建议部分链接令并集75/300=25%，仅限定证据覆盖，最终/功能签收0/300。1317历史期待/1314匹配/3旧.log缺失；产品53源/94冻结/15正式保持。复用venv无安装，完整交接91份。附加审计与独立核验以version-http-checks-roundN.json和progress-version-http.json为准；报告KAGGLE_STEP18_G0_VERSION_HTTP.md。G0/整体PARTIAL/BLOCKED，不跳S1/Q28/发布；声音优化未实施，真实模型/双T4/训练/声学/提速未验收。


## S1隔离候选实际实现（问题28流程调整）

不再只增加观察。问题28已独立按四选项、选C及50行动完成，见KAGGLE_STEP18_Q28_S1_CANDIDATE.md；原25–27文件不改、29未开。前置门禁调整为：允许隔离候选修复，不允许未验收候选进入冻结包、默认正式服务／工作台或发布。G0整体仍PARTIAL/BLOCKED，真实模型／硬件门禁未豁免。

新增kaggle/step18的实际候选分析源码，依赖冻结17其余模块；只改候选／文本／删除入口及提交辅助代码，其余命名定义AST相同。实现严格JSON/类型/Unicode、HEAVY先准入后写盘、内容地址锚点和提交失败保旧、短提交锁与删除协调；校准仍原实现不算修复。默认17包与正式HEAD、53源/94冻结/15正式保持。

最终相同28合同，旧版43失败记录/2明确skip/0error，候选28预检全PASS。完整478（旧450冻结对照+新28候选合同）×3PASS，失败／错误／跳过0；每轮159 TCP、三轮477，新候选74/轮共222。15条原建议新限定实现证据加强原75并集，未虚增覆盖，原300最终／功能签收仍0。三轮附加检查与独立封存以s1-candidate-checks-roundN.json及progress-s1-candidate.json为准，完整交接93份。无真实模型／训练／双T4／声音质量／提速验收，18未发布；下一步仅S2校准快照与冲突修复，不能把当前成果称已消沙沙或首声更快。


## S2-A校准快照实际实现

在隔离18候选中实现完整输入捕获、仅用捕获字节评估、提交前同短锁核验；真实HTTP编辑／ABA、候选同名bytes／质心／参数变化、删除／trained变化后409且不应用旧评分。S1变更写修订nonce，相同选择幂等；同档案第二次校准409，临时ID独立且长度安全，自有临时目录与ASR释放finally。最多24候选、64MiB聚合文件，非总内存预算／跨进程事务。改前S1及活跃交接已归档s2-before/index；冻结17不动。新增22合同对改前S1为21失败记录/0error/0skip，候选预检22全PASS。三轮500（450冻结控制+当前候选上S1旧28+新22）及附加检查以progress-s2.json为准，完整交接94份。原300建议最终／功能未全签，证据比例非整体进度。缺失CER默认值、全失败chosen0、非有限／覆盖率评分、最终worker回执等留待S2-B，不提前签完整S2，不跳真实模型／双T4／声学或发布门禁。问题29未开，原三轮100及问题25–28记录保留。


## S2-B有效指标与加载就绪实际实现

Q29选C及50行动先完成，未开30。逐目标缺失null、覆盖率／有限可靠指标门禁，不再默认CER0.05或全失败chosen0。无候选422不写盘保旧，其他完整候选可选；临时worker核验状态和pin，选择保存后最终加载失败503/savedtrue/readyfalse，后改／删版本明确标不当前，不虚构回滚。成功保留磁盘选择报告一致及quality_verified=false；后台可选校准摘要已接入但未完整运行真实创建。S1/S2-A旧方法断言不改。

最终23合同对S2-A为36失败记录（含子用例、非36bug），候选预检PASS。初三轮523通过后复核修正整数PCM abs最小值溢出并补子用例，最终另命名三轮以s2b-final和progress-s2b.json为准，不混算初轮；初源码逆变换重建明确按记录SHA核验、非事前快照，原错日志均保留。旧500加新23，旧450冻结控制／旧50当前候选／新23当前候选，附加检查和封存以实际收据为准。完整交接96份，17／53源／94冻结／15正式不变，18未发布。真实短音、质量、双T4／训练／性能及全局事务仍未签；下一步隔离候选S3分块一致性，不跳声学门禁。

本批12条当前实现限定链接令证据并集81/300（27%仅证据覆盖），不是整体完成率；最终／功能签收仍0。


## S3因果 NumPy DSP 与隔离worker实际接入

Q30四选项选C、50行动和三遍各100专题建议已先归档。新增 step18_audio_rt.py 与隔离 worker.py，唯一模块名接入真实 run_job；所有 worker 命名定义AST保留。固定 RMS 余数、逐样本因果平滑、绝对位置淡入、明确flush/关闭/配置合同；没有PCM整窗缓冲，没有参考PCM拼接。候选只启用 numpy-causal-v1，不装载未测Rust；冻结17/正式工作台不动。旧版30合同44失败记录、候选30 PASS；完整562×3全部PASS，含旧523逐ID/结果保留；14分块矩阵×3差0，601秒合成流×3状态有界和计数通过，CPU实测有短块加速也有大块开销，不是模型RTF或声学提速证明。附加24审计/Node30/AST53等最终结果与两次封存以 progress-s3.json 为准。新venv确实重建、freeze与旧版相同；1768保护/1765匹配/3旧日志缺失仍保留；完整交接101份、18未发布。完整S3含Rust/模型/声学仍未签收。下一步S4裁剪有界状态，不能把DSP样本数守恒当整个原trimmer链已无丢样本；不需要Continue。


## S4有界裁剪与worker结束实际修复

Q31选C及50行动、三遍100建议先写。新增step18_trimmer.py固定120网格残帧/跨块35ms前史/有界尾队列/finish；正常finish保留缓存非零尾，精确零裁掉计数；取消/异常清缓存不排尾；中段静音超限输出不删。新增worker_s4.py实际接入，只更换裁剪器和Worker.run_job，原S3 worker/DSP及旧合同完整保留。30旧版红42失败记录/0error/skip，初41失败+1OverflowError已保留并转明确合同失败；候选30/worker10预检通过。完整602×3全部PASS，旧562逐ID/结果保留；21分块矩阵×3对独立参考逐样本相等，601秒合成流×3达到并守住43200样本尾预算。裁剪CPU约1.10秒/601秒合成音频，正确性有开销不声称提速/模型RTF/首声改善。最终审计24/Node30/AST57及两次封存见progress-s4.json。无新依赖，1905保护/1902匹配/3旧日志仍缺，完整交接106份，17/正式工作台不改、18未发。领先低电平仍可裁，非零尾不是无噪声证明；真实用户音频/双T4/训练/声学及完整S3 native仍未签。下一步S5完成短尾排空，直接继续无需Continue。


## S5完成短尾／重采样／epoch实际修复

Q32选C＋50行动、三遍100建议先归档。新增完整web/app.js，仅改Player及嵌入Worklet，网络解析/预测器/UI后缀逐字节保持；真实完整页面使用新Player。完成任何正pending可play，未完成风险阈值保留；按post−played−dropped计账并等当前epoch endACK，不以旧fill0假装结束。全局整数坐标重采样，正常末样本保持到ceil预算、取消不flush；epoch拒绝旧状态与stop后复活。37VM红28失败/9保留，候选预检37和8源码及15原生浏览器通过。最终610CPU（旧602保留）/37VM/173Chromium（旧158＋新15，含3完整UI原生链）三轮及24审计/Node30/AST58与两次封存见progress-s5.json；不混算重叠VM。实体扬声器与模型声音未验收，firstPlayedMs仍play命令时间。Python沿用无安装，npm ci确实按旧lock安装浏览器依赖，lock/config不改；2049保护/2046匹配/3旧日志缺，完整交接111份，17/正式工作台/S3S4不改、18未发布。下一步S6时序与诊断，真实T4/训练/声学/RTF和完整S3 native仍未签，不要求Continue。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_AUDIT.md

# 第十八阶段G0补审与建议处置（第一批，未签收）

## 本批实际完成

- 活动分支`arena/1160bd87-kagglee`。产品源码、原始–17发布资产与正式工作台不改。
- 读取300条原建议，逐ID初审分类、关联批次和待执行测试合同。完整表见`KAGGLE_STEP18_G0_DISPOSITION.md`，机器记录见`validation/step18/g0-recommendation-disposition.json`。**分类不代表全部建议已实现、逐项已测或最终签收。**
- 对此前较浅的六份源码完成本批第一遍完整文件语义阅读，共930行：training_job.py、gpu_ownership.py、persist.py、access_control.py、resource_limits.py、qtts_common.py。第二遍仅做部分调用方/边界交叉核对，第三遍未完成，不把三种观察角度伪称全源三遍。
- `g0-source-coverage.json`逐资产记录53项的hash、行数、三遍状态与历史范围。本批第一遍完整阅读6项，其余47项不新增完整覆盖信用；第二/三遍完整签收均0。53资产之外的仓库服务、生成器、测试、复制页和正式工作台仍需单独覆盖，不能从这张表推导全仓已审完。

## 300条初审结果

| 分类 | 条数 | 解释 |
|---|---:|---|
| 限定范围内已复现缺陷建议 | 23 | 与历史受控收据关联；多条可指向同一缺陷，不是23个独立bug |
| 保留约束/保护 | 96 | 不应被音频优化破坏；并不表示96条本批逐项测试通过 |
| 文档/度量/测试合同 | 89 | 语义说明、计划或证据边界，不能冒充产品修复 |
| 真实模型/设备等阻塞 | 55 | 含真实WAV、浏览器/设备、目标后端及双T4；仍未执行 |
| 待进一步证据 | 37 | 保留未知，不猜成bug或直接删除需求 |
| 合计 | 300 | 全部有初审映射，全部最终处置签收仍为false |

每行保留原ID、原建议/来源和原review引用；测试家族是拟执行的不变量，不把共享测试家族等同每行都有独立覆盖。已复现类只称各收据所述范围，例如AST交错不代表真实线程并发、小块泛用合同不代表生产1920倍数必达。

## 六模块第一遍语义结论

### training_job.py（1–227）

- 28–70检查本地文件树、硬链接/软链接、预算、远程代码元数据、必备文件和Base1.7B/16码本，使用内容hash；这不是加载或验证真实权重质量。
- 73–86拒绝fixture/legacy训练来源，要求审阅及实验确认；整数预算拒bool。80–86浮点选项/内部调用类型边界还需后续深审，不能认为当前所有类型已严密覆盖。
- 99–105训练子进程清除列举的认证/API变量及PYTHONPATH，开启离线；仅证明列举键，不证明所有可能的凭证别名已清除。
- 153–210持代码租约与离线GPU租约；创建子进程前屏蔽取消信号，登记PID后恢复；停止实际创建的独立进程组，不读旧PID杀进程；结束后复核输入与模型。退出0但没有checkpoint不算优化器成功。
- 125–150检查rank集合、样本集合及参数变化，保存安全格式checkpoint但明确质量/推理未验证。其报告可信性、逐epoch完整覆盖、训练恢复等仍需tts_training/数据链完整深审和真实执行。
- **新复现G0-B02–04**：config.json合法对象但talker_config为null/列表/字符串时，68行链式.get产生AttributeError；不是受控UploadRejected。仅本地材料化配置错误合同，未证明远程利用、GPU训练发生或声学损害。后续先修错误分类，再补CLI回执；当前未修改。

### gpu_ownership.py（1–151）

- 固定同主机同UID命名空间不随STATE/设备别名变化。文件类型/owner/nlink/权限及nonce检查阻止误采纳；adopt核对inode、活锁和共享描述符。
- close只关FD不LOCK_UN，保证父子共享的最后描述符关闭前租约仍有效；不unlink锁文件。状态记录PID/时间只诊断，不据“过期PID”抢锁。
- 这是合作式CPU flock协议，外部UID/容器/非参与进程不在合同内，`gpu_verified=false`保留。不能称测到实际CUDA占用。

### persist.py（1–99）与qtts_common.py（1–211）

- _pack仅打包profiles与active，跳过_cal；原始libraries/training_data/training_codes/training_runs不被该遍历纳入。profile的参考锚点和转写本来就属于显式配置快照，不能误称“备份不含任何私有音频”。未调用Kaggle网络服务验证私有可见性。
- 恢复先检查整个归档成员范围，再由通用extract_tar_safely拒绝绝对路径、..、特殊成员和现存逃逸链接；逐文件临时写再replace。合法路径与不安全成员预检查已有保护继续通过。
- **新边界G0-B08**：在合法归档第二成员replace处注入OSError，第一成员已提交，第二仍旧；临时文件清理成功，但没有包级回滚。是本地故障注入下的恢复一致性缺口，不是已发生的数据损坏或声音串档；后续设计需考虑暂存、提交、启动顺序和指纹保护，不能直接把所有文件一次replace称全事务。
- common的JSON写入是单文件原子替换；默认json.dump接受非有限数，不能借training_job.write_json的allow_nan=False推断所有写入相同。来源、预算、日志与恢复原子性都需第二/三遍复核。

### access_control.py（1–70）

- 默认认证目录在临时目录，状态路径hash隔离；环境值与生成token长度/ASCII检查，文件采用NOFOLLOW、owner/类型/长度核验，落盘fsync和600权限；并发生成有flock。
- gateway_headers仅对指定本地HTTP网关附token，不向worker或远端发送；这是内部探针行为，不让浏览器向localhost取服务。
- 对目录祖先/本地同UID篡改、锁文件和文件打开时序的完整威胁覆盖未签收；不把现有测试通过称认证无漏洞。未显示或持久化实际凭证。

### resource_limits.py（1–172）

- BodyBudgetMiddleware先有界spool再交multipart解析；未知Content-Length也逐块计量，断开不继续调用应用；JSON与multipart预算分开。
- BuildAdmission.start本身不获取slot；核对analyst.py 987–1033的调用方先非阻塞获取，未成功start时finally释放；线程内finally释放。不能只看片段就误报“未获取却释放”。
- HeavyAdmission用shield使HTTP取消不释放实际仍运行任务的槽；提交失败通过事件门阻止队列残留重复执行/重复释放。它不是按profile串行事务，不能替代S2版本/锁。
- 实际限流、ASGI/HTTP错误、启动失败及取消保护在本批84项子集中验证；真实高并发长稳压测尚未执行。

## 实际执行与收据

### 现有专项回归：84项×3轮

`run_g0_regressions.py`明确选择test_gpu_ownership、test_security、test_reliability及test_tts_training中的AdmissionTests/ControllerLifetimeTests。每轮84项、失败0、错误0、跳过0。包含真实CPU子进程、FD/flock、SIGTERM/SIGKILL生命周期；HTTP部分是FastAPI TestClient进程内请求，不是网络服务压力或用户浏览器。

训练控制器部分明确注入fixture代码、模拟模型/子进程；绝不是完整Qwen训练。未纳入Torch TensorTests，因此0跳过也不能说已跑张量/Gloo实验。未执行Go/Rust/完整浏览器/六协议最终三轮。

收据：`g0-regression-round1..3.json/.txt`，每项测试ID及状态、53源资产/测试/runner hash和主要依赖版本均记录。第一次执行84×3也通过，但源清单rglob误纳入24个__pycache__文件；保留为`*-initial`，修正为baseline的53资产后重新执行84×3，以无initial后缀为当前收据。这是收据库存错误，不是产品回归失败。

### 新边界实验：10项×3轮

`g0_boundary_probe.py`直接导入原函数，使用临时本地合成文件，无权重、无外网、无用户WAV。G0-B01..10涵盖假文件树指纹、三种损坏talker_config、auto_map拒绝、NaN单文件写保护、坏归档预检、恢复中途I/O失败、备份范围、列举秘密清除/离线策略。三轮结果一致。**捕捉到原有缺陷的案例退出0表示成功复现，不是修复后通过。**

收据：`g0-boundary-round1..3.json`。NumPy保持2.2.6；为实际CPU/HTTP测试在忽略.venv补安装requirements-test中FastAPI/Uvicorn/multipart/httpx/soundfile/requests固定版本，未安装Torch/Go，未修改生产依赖。首次安装命令因.cache目录不存在在重定向前失败，创建忽略目录后成功。

## 覆盖和下一步门禁

- **G0仍未完成**：6份第一遍全文不能代替全部53资产，更不能代替全仓三遍。300映射初审不能代替逐条最终签收。
- 下一批先读training_data/training_codes/voice_library的完整事务、租约及训练采样/发布链，再覆盖Go会话、安全、全前端和外围服务；逐遍记录实际范围，不自动补成完成。
- 新恢复一致性问题暂留设计待证，不在本步默认决定重写恢复。若后续需要新的关键设计选择，再按一题/50建议追加；不机械填问题28。
- 完成覆盖/映射后才按实施细则S1起小步修改。最终完整回归与真实模型三轮仍分别必需；首声、无沙沙、同声自然朗读、RTF≤0.3、真实长数据训练全部未由本批证明。
- 整体PARTIAL/BLOCKED，产品未改、18未生成，原始–17及正式工作台继续冻结。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_DISPOSITION.md

# 第十八阶段300条建议处置映射（初审，未签收）

每条保留原ID/建议；测试家族是待执行合同，不等于每条已有独立测试。确证缺陷仅限收据所述范围。三遍全源未完成，G0未通过。

| ID | 初审分类 | 批次 | 建议 | 测试家族 |
|---|---|---|---|---|
| S18-R1-001 | documentation-or-test-contract | S7 | 将候选参与质心统计与实际ICL锚点分开显示，避免全部片段已融合的误解 | 候选条件来源 |
| S18-R1-002 | pending-evidence | S7 | 在合成收据记录选中的anchor_candidate，而不是只显示profile ID | 候选条件来源 |
| S18-R1-003 | pending-evidence | S7 | 记录实际锚点字节指纹与对应转写指纹；日志不明文写入私有转写 | 候选条件来源 |
| S18-R1-004 | pending-evidence | S7 | 用不同内容的三个候选验证只选中的音频进入提示提取 | 候选条件来源 |
| S18-R1-005 | documentation-or-test-contract | S7 | 审核“候选校准”文案明确逐个试验后选一个，不称多参考融合 | 候选条件来源 |
| S18-R1-006 | pending-evidence | S7 | 查验Faster真实接口的多参考能力，未支持时不伪造列表参数 | 候选条件来源 |
| S18-R1-007 | preservation | S7 | 禁止把三个片段PCM拼成一个提示并配不连续全文 | 候选条件来源 |
| S18-R1-008 | preservation | S7 | 跨候选声纹中心仅作评分依据，不声称它已替代模型speaker embedding | 候选条件来源 |
| S18-R1-009 | preservation | S7 | 为单个合法候选保留最短建档链路，不强迫三候选 | 候选条件来源 |
| S18-R1-010 | documentation-or-test-contract | S7 | 给未来多候选策略保留显式模式与回退边界，不静默改变17默认 | 候选条件来源 |
| S18-R1-011 | confirmed-defect-in-stated-scope | S1/S2 | 非法index的布尔、小数、对象与缺省语义分别测试，避免int强转误选或500 | 候选状态事务 |
| S18-R1-012 | pending-evidence | S1/S2 | 核查切换候选与校准并发时磁盘写入、工作者加载是否形成一致事务 | 候选状态事务 |
| S18-R1-013 | pending-evidence | S1/S2 | 候选文件复制失败时保留旧profile JSON，不留下半更新锚点 | 候选状态事务 |
| S18-R1-014 | pending-evidence | S1/S2 | 双卡仅一张加载成功时明确部分失败，不宣称启用完成 | 候选状态事务 |
| S18-R1-015 | preservation | S1/S2 | 旧会话遇新指纹必须继续拒播，不能热切后拼混音色 | 候选状态事务 |
| S18-R1-016 | confirmed-defect-in-stated-scope | S1/S2 | 转写编辑与候选选择同时发生时绑定同一版本，防止音文错配 | 候选状态事务 |
| S18-R1-017 | pending-evidence | S1/S2 | 校准临时profile的anchor_candidate元数据应指向实际试验候选，不能误标0 | 候选状态事务 |
| S18-R1-018 | preservation | S1/S2 | 候选变更后清理或替换提示快照时保留锁内核验 | 候选状态事务 |
| S18-R1-019 | pending-evidence | S1/S2 | 为重复点击候选与取消任务增加幂等与状态测试 | 候选状态事务 |
| S18-R1-020 | preservation | S1/S2 | 训练adapter的固定参考限制保持，不让候选切换绕过来源绑定 | 候选状态事务 |
| S18-R1-021 | documentation-or-test-contract | S6 | 分别记录请求、首个可用文本、排队、预填充、首PCM、首播放命令 | 分阶段首声度量 |
| S18-R1-022 | documentation-or-test-contract | S6 | worker t_start在加载提示之后，单独计量冷提示加载而不漏记等待 | 分阶段首声度量 |
| S18-R1-023 | documentation-or-test-contract | S6 | queue_ms当前覆盖锁等待等前置耗时，拆项后保留旧字段兼容 | 分阶段首声度量 |
| S18-R1-024 | documentation-or-test-contract | S6 | 浏览器firstPlayedMs当前在发play命令处赋值，标明不是硬件实际出声 | 分阶段首声度量 |
| S18-R1-025 | pending-evidence | S6 | 评估AudioWorklet消费首个语音样本的确认消息，区分主线程命令延迟 | 分阶段首声度量 |
| S18-R1-026 | preservation | S6 | 跨Python、Go与浏览器仅使用各自单调时间差，不能直接减不同纪元 | 分阶段首声度量 |
| S18-R1-027 | preservation | S6 | 显式静音停顿不能计为首个可用人声，保留禁止原音占位 | 分阶段首声度量 |
| S18-R1-028 | hardware-or-real-model-blocked | S6 | 首包平均之外记录p50/p95与冷暖状态，不用一次幸运值 | 分阶段首声度量 |
| S18-R1-029 | hardware-or-real-model-blocked | S6 | 将文本长度、参考长度、chunk_size和设备条件写入性能收据 | 分阶段首声度量 |
| S18-R1-030 | documentation-or-test-contract | S6 | 首声提速必须同时检查缺字与最终音频完整性，不能裁掉开头 | 分阶段首声度量 |
| S18-R1-031 | pending-evidence | S5/S6 | 对当前0.7秒下限和初始2秒策略建立确定性到达轨迹对照 | 播放启动 |
| S18-R1-032 | pending-evidence | S5/S6 | 分别测试高速稳定、慢速持续、突发包与长网络抖动 | 播放启动 |
| S18-R1-033 | pending-evidence | S5/S6 | 初次启动与欠载恢复分别设计目标，不统一缩到最小 | 播放启动 |
| S18-R1-034 | pending-evidence | S5/S6 | 将预测器无速率样本时的保守回退纳入首次播放测试 | 播放启动 |
| S18-R1-035 | pending-evidence | S5/S6 | 测量AudioWorklet统计消息的刷新间隔对主线程启动判断的影响 | 播放启动 |
| S18-R1-036 | pending-evidence | S5/S6 | 在44.1k及48k上下文验证重采样后的fill计秒正确 | 播放启动 |
| S18-R1-037 | confirmed-defect-in-stated-scope | S5/S6 | 短于启动阈值但已完成的真实语音应及时播放，不等待不可达缓冲 | 播放启动 |
| S18-R1-038 | pending-evidence | S5/S6 | 后台页、暂停恢复、锁定与取消后不得发送迟到play | 播放启动 |
| S18-R1-039 | pending-evidence | S5/S6 | 记录ring dropped样本；任何丢样不能只显示播放成功 | 播放启动 |
| S18-R1-040 | hardware-or-real-model-blocked | S5/S6 | 低延迟策略只能在欠载预算内启用，不能把断续当自然阅读 | 播放启动 |
| S18-R1-041 | hardware-or-real-model-blocked | S6/S7 | 对2/4/8/16帧首块大小做同文本同seed对照，测TTFA及总RTF | 模型与调度热路径 |
| S18-R1-042 | hardware-or-real-model-blocked | S6/S7 | 小首块与稳态大块若需不同大小，先确认真实生成器支持，禁止无效传参 | 模型与调度热路径 |
| S18-R1-043 | hardware-or-real-model-blocked | S6/S7 | 检查decode迭代器首次next含有的预填充时间，不能只测创建生成器 | 模型与调度热路径 |
| S18-R1-044 | hardware-or-real-model-blocked | S6/S7 | 单独计量token生成、codec解码及CPU拷贝，避免归因全部GPU | 模型与调度热路径 |
| S18-R1-045 | preservation | S6/S7 | 提示快照重用必须与内容指纹一致，不退回仅按路径缓存 | 模型与调度热路径 |
| S18-R1-046 | preservation | S6/S7 | 不为首声把ICL换成向量默认，保留相似度条件 | 模型与调度热路径 |
| S18-R1-047 | hardware-or-real-model-blocked | S6/S7 | 比较首段优先调度与后续并行的队头阻塞，不无证据锁死单卡 | 模型与调度热路径 |
| S18-R1-048 | preservation | S6/S7 | 确认Live聊天第一可用前缀触发不被朗读聚合配置覆盖 | 模型与调度热路径 |
| S18-R1-049 | preservation | S6/S7 | 保留最大生成token与取消限制，不能为速度删掉输出 | 模型与调度热路径 |
| S18-R1-050 | hardware-or-real-model-blocked | S6/S7 | 不默认每卡双模型增加显存；只有目标T4实测才接受吞吐结论 | 模型与调度热路径 |
| S18-R1-051 | documentation-or-test-contract | S7/acoustic | 原始RMS约-47.7只作为风险，不推断具体麦克风故障 | 参考清理 |
| S18-R1-052 | documentation-or-test-contract | S7/acoustic | 分别记录归一化前后语音电平与峰值，注明增益上限14dB | 参考清理 |
| S18-R1-053 | documentation-or-test-contract | S7/acoustic | 候选SNR是估计量，不能把17dB阈值当真实噪声声压 | 参考清理 |
| S18-R1-054 | hardware-or-real-model-blocked | S7/acoustic | 保留raw、strength0.85、strength0.55对照的处理收据 | 参考清理 |
| S18-R1-055 | hardware-or-real-model-blocked | S7/acoustic | 审查声纹相似0.94与SNR增益2dB门禁是否会误接收失真，不能只看单分数 | 参考清理 |
| S18-R1-056 | pending-evidence | S7/acoustic | 验证全零、强直流、很轻语音及背景声输入的处理决策 | 参考清理 |
| S18-R1-057 | hardware-or-real-model-blocked | S7/acoustic | 对齿音、气声、摩擦音单独测保真，不能以削高频冒无沙沙 | 参考清理 |
| S18-R1-058 | preservation | S7/acoustic | 不在用户未授权时保存或上传原始私有WAV作为公共证据 | 参考清理 |
| S18-R1-059 | documentation-or-test-contract | S7/acoustic | 已存在非平稳降噪不等于生成输出已降噪，明确处理发生阶段 | 参考清理 |
| S18-R1-060 | hardware-or-real-model-blocked | S7/acoustic | 录音时扬声器回录网页朗读的可能性仅列假设，不能由截图定论 | 参考清理 |
| S18-R1-061 | hardware-or-real-model-blocked | S3/S7/acoustic | 建立模型PCM、后处理PCM、浏览器录回的分层局部诊断，默认关闭私有采集 | 输出噪声定位 |
| S18-R1-062 | hardware-or-real-model-blocked | S3/S7/acoustic | 将codec窗口起点与边界脉冲位置关联，区分底噪和接缝爆音 | 输出噪声定位 |
| S18-R1-063 | hardware-or-real-model-blocked | S3/S7/acoustic | 对持续人声与停顿分别计算频谱，但无清洁真值时不称绝对SNR | 输出噪声定位 |
| S18-R1-064 | preservation | S3/S7/acoustic | 继续验证codec只收到生成码，不能回到参考码前缀解码 | 输出噪声定位 |
| S18-R1-065 | hardware-or-real-model-blocked | S3/S7/acoustic | 真实预训练codec与随机tiny codec的质量证据必须分列 | 输出噪声定位 |
| S18-R1-066 | pending-evidence | S3/S7/acoustic | 非有限模型输出当前替换为零，应评估失败拒播而非掩盖异常的策略 | 输出噪声定位 |
| S18-R1-067 | hardware-or-real-model-blocked | S3/S7/acoustic | 增益提升可能抬噪，记录处理前后噪声地板变化而不自动强门限 | 输出噪声定位 |
| S18-R1-068 | preservation | S3/S7/acoustic | 不能用输出全静音或静音段删除作为零噪声验收 | 输出噪声定位 |
| S18-R1-069 | preservation | S3/S7/acoustic | 保留模型自然人声呼吸与禁止添加噪声的区别，不自动切除语音气息 | 输出噪声定位 |
| S18-R1-070 | hardware-or-real-model-blocked | S3/S7/acoustic | 用户全程纯人声目标需真实WAV试听和添字检查，代码指标不替代 | 输出噪声定位 |
| S18-R1-071 | confirmed-defect-in-stated-scope | S3 | 实测同一信号整块与任意分块处理的样本一致性 | DSP状态 |
| S18-R1-072 | confirmed-defect-in-stated-scope | S3 | 重点验证NumPy不足96样本首块时淡入是否在下一块重新从零开始 | DSP状态 |
| S18-R1-073 | pending-evidence | S3 | 核查NumPy按输入块丢弃不足240样本RMS余数与Rust跨块累积差别 | DSP状态 |
| S18-R1-074 | pending-evidence | S3 | 比较Rust逐样本增益平滑与NumPy逐块插值，不能宣称严格等价 | DSP状态 |
| S18-R1-075 | preservation | S3 | 保持输出样本数与输入相等，不能为降噪补偿无记录延迟 | DSP状态 |
| S18-R1-076 | pending-evidence | S3 | 分别测试DC blocker状态、零输入残留与长静音后重新讲话 | DSP状态 |
| S18-R1-077 | pending-evidence | S3 | 测试max_gain_db=0隔离淡入和DC滤波，再开放AGC定位差异 | DSP状态 |
| S18-R1-078 | hardware-or-real-model-blocked | S3 | 同卡每段重置与跨卡各自状态不同需测量，不能只凭相同目标响度称一致 | DSP状态 |
| S18-R1-079 | preservation | S3 | flush的192样本衰减不是新生成语音，不能加入RTF语音分母 | DSP状态 |
| S18-R1-080 | documentation-or-test-contract | S3 | 若修复NumPy算法须保留Rust接口版本兼容，并添加跨后端容差测试 | DSP状态 |
| S18-R1-081 | hardware-or-real-model-blocked | S4/S5/acoustic | 将独立模型韵律重启、显式停顿、播放欠载三种接缝分类计数 | 连续朗读 |
| S18-R1-082 | hardware-or-real-model-blocked | S4/S5/acoustic | 保留朗读12/24首段、20/40/80稳态配置基线再比较，不盲目扩大 | 连续朗读 |
| S18-R1-083 | preservation | S4/S5/acoustic | 逐字验证分段重新连接等于原文，保护数字、缩写、引号和标点 | 连续朗读 |
| S18-R1-084 | documentation-or-test-contract | S4/S5/acoustic | 审查PauseBeforeMs与tail_pause_ms是否重复加停顿，先画时序再修改 | 连续朗读 |
| S18-R1-085 | preservation | S4/S5/acoustic | 禁止跨词PCM重叠掩盖接缝，不牺牲清晰度冒自然度 | 连续朗读 |
| S18-R1-086 | hardware-or-real-model-blocked | S4/S5/acoustic | 段尾8ms衰减及下段淡入需以有声边界实测，不只用零边界波形 | 连续朗读 |
| S18-R1-087 | hardware-or-real-model-blocked | S4/S5/acoustic | 欠载时0.94尾衰减属于播放补偿，不能误标模型本身沙沙 | 连续朗读 |
| S18-R1-088 | hardware-or-real-model-blocked | S4/S5/acoustic | 自然度对照必须同时保存整段朗读，不能只听裁剪后小片段 | 连续朗读 |
| S18-R1-089 | hardware-or-real-model-blocked | S4/S5/acoustic | 不同GPU同文与交替长文分别试听；同seed不等于波形完全相同 | 连续朗读 |
| S18-R1-090 | hardware-or-real-model-blocked | S4/S5/acoustic | 只有真实模型支持的连续条件才能声称跨段联合生成，不换名称包装独立合成 | 连续朗读 |
| S18-R1-091 | preservation | G0/S8 | 冻结原始至17包、全部manifest及正式工作台，新增18不得覆盖历史包 | 回归交付 |
| S18-R1-092 | documentation-or-test-contract | G0/S8 | 三轮100建议均标已确认问题、待证假设或保留约束，不虚报300个bug | 回归交付 |
| S18-R1-093 | documentation-or-test-contract | G0/S8 | 完成三轮审查后再逐题决策，每题50建议后才进入下一题 | 回归交付 |
| S18-R1-094 | documentation-or-test-contract | G0/S8 | 历史334测试不能算18新增验证，依赖缺失需如实记录和重建 | 回归交付 |
| S18-R1-095 | documentation-or-test-contract | G0/S8 | 对每个修复保留修复前失败、修复后通过的同输入收据 | 回归交付 |
| S18-R1-096 | documentation-or-test-contract | G0/S8 | 三轮Python、Node、Go race、协议和浏览器必须针对最终源码再执行 | 回归交付 |
| S18-R1-097 | hardware-or-real-model-blocked | G0/S8 | CPU合成信号实验不代替真实T4语音实验，硬件不足保持BLOCKED | 回归交付 |
| S18-R1-098 | preservation | G0/S8 | 按实测热路径选择语言；不要新增Java/C#/SQL服务凑多语言 | 回归交付 |
| S18-R1-099 | documentation-or-test-contract | G0/S8 | 最终18复制页、下载、剪贴板拒绝回退与手机逐字节校验不可省略 | 回归交付 |
| S18-R1-100 | documentation-or-test-contract | G0/S8 | 将全部已完成备忘录内嵌完整提示词；未完成轮次必须明确，不编造结论 | 回归交付 |
| S18-R2-001 | preservation | S7 | 保持qwen-tts-hf与旧qwen-tts发行版严格分离，源码同命名空间不等于同版本 | 实际模型接口 |
| S18-R2-002 | preservation | S7 | 下载源码必须核对PyPI wheel SHA256，收据注明实际提供模型类的发行版 | 实际模型接口 |
| S18-R2-003 | pending-evidence | S7 | 将三提示单目标被拒绝的实际接口行为加入未来多参考功能合同 | 实际模型接口 |
| S18-R2-004 | documentation-or-test-contract | S7 | 将三提示三目标定义为独立批量任务，界面不能称参考融合 | 实际模型接口 |
| S18-R2-005 | preservation | S7 | 保留列表prompt每项独立ref_text，不用共享一条文字冒三候选匹配 | 实际模型接口 |
| S18-R2-006 | documentation-or-test-contract | S7 | 字典prompt的批量ref_text共享行为应明确，不直接用于三段不同转写 | 实际模型接口 |
| S18-R2-007 | preservation | S7 | 引用prompt item中ref_code与speaker embedding的区别，不能用声纹平均替代ICL | 实际模型接口 |
| S18-R2-008 | preservation | S7 | 保持单ICL预计算提示的真实接口回归，不能为新模式破坏现有快照 | 实际模型接口 |
| S18-R2-009 | preservation | S7 | 向量模式继续要求显式选择，不把它作为未实现融合的静默替代 | 实际模型接口 |
| S18-R2-010 | hardware-or-real-model-blocked | S7 | 实际生成器、权重和声学结果未执行时，接口控制流通过不标模型实验通过 | 实际模型接口 |
| S18-R2-011 | documentation-or-test-contract | S7 | 建立全部候选分析清单，逐项列源文件、时间、匹配转写、指纹和有效性 | 候选条件合同 |
| S18-R2-012 | documentation-or-test-contract | S7 | 单锚点模式明确显示被用作ICL的候选及未用作ICL的其他候选 | 候选条件合同 |
| S18-R2-013 | documentation-or-test-contract | S7 | 若后续共享参数来自全部候选评分，记录算法与评分证据而非暗示音频融合 | 候选条件合同 |
| S18-R2-014 | hardware-or-real-model-blocked | S7 | 比较每候选合成时固定同文同seed同采样参数，确保差异确由候选造成 | 候选条件合同 |
| S18-R2-015 | preservation | S7 | 候选中心与实际Qwen说话人嵌入不同空间时不得直接替换 | 候选条件合同 |
| S18-R2-016 | hardware-or-real-model-blocked | S7 | 实验性的融合嵌入若提出，必须独立模式且真实盲听，不自动作为最佳方案 | 候选条件合同 |
| S18-R2-017 | preservation | S7 | 不跨候选拼转写或参考码以绕过模型批量长度校验 | 候选条件合同 |
| S18-R2-018 | documentation-or-test-contract | S7 | 候选顺序变化时用内容身份而不只用数组下标定位证据 | 候选条件合同 |
| S18-R2-019 | documentation-or-test-contract | S7 | 候选有效时长按实际WAV而非仅展示start/end计算，避免舍入差 | 候选条件合同 |
| S18-R2-020 | preservation | S7 | 候选策略、模型模式及参数调整必须使旧会话明确失效 | 候选条件合同 |
| S18-R2-021 | confirmed-defect-in-stated-scope | S1 | index必须严格整数且非bool，拒绝true变1与false变0 | 入口验证 |
| S18-R2-022 | confirmed-defect-in-stated-scope | S1 | 拒绝1.9截断成1，避免非整数JSON静默切换其他参考 | 入口验证 |
| S18-R2-023 | documentation-or-test-contract | S1 | 缺失index应明确拒绝还是显式兼容默认0，不让文档与行为矛盾 | 入口验证 |
| S18-R2-024 | confirmed-defect-in-stated-scope | S1 | null、数组、对象及NaN输入转换失败应返回受控4xx而非未捕获异常 | 入口验证 |
| S18-R2-025 | documentation-or-test-contract | S1 | 候选入口未知字段与重复字段的策略需与严格library接口一致 | 入口验证 |
| S18-R2-026 | pending-evidence | S1 | 验证candidates为非空合法列表，不能只依赖len和下标访问 | 入口验证 |
| S18-R2-027 | pending-evidence | S1 | 验证候选file为安全单文件名且普通文件，避免损坏profile路径越界 | 入口验证 |
| S18-R2-028 | pending-evidence | S1 | 手工ref_text不接受dict/list被str化，保留严格字符串与Unicode校验 | 入口验证 |
| S18-R2-029 | preservation | S1 | 保留训练档案禁止改候选和转写的409边界，不绕过版本固定 | 入口验证 |
| S18-R2-030 | documentation-or-test-contract | S1 | 增加真正HTTP参数与错误码测试；当前AST调用不冒充FastAPI测试 | 入口验证 |
| S18-R2-031 | confirmed-defect-in-stated-scope | S2 | 校准开始捕获完整候选集合版本，提交时核对未变再采用评分 | 校准版本提交 |
| S18-R2-032 | confirmed-defect-in-stated-scope | S2 | 禁止用旧候选评分选择重新读取后已更改的同下标候选 | 校准版本提交 |
| S18-R2-033 | confirmed-defect-in-stated-scope | S2 | 校准期间并发编辑转写不能被结束时静默覆盖，需冲突响应 | 校准版本提交 |
| S18-R2-034 | pending-evidence | S2 | 候选文件内容更改但文件名不变也要改变校准输入版本 | 校准版本提交 |
| S18-R2-035 | pending-evidence | S2 | 候选变更、文本变更、校准、删除应协调同一档案锁或乐观版本合同 | 校准版本提交 |
| S18-R2-036 | documentation-or-test-contract | S2 | 进程内线程锁与跨进程文件锁分别评估，不能把一个称全局事务 | 校准版本提交 |
| S18-R2-037 | documentation-or-test-contract | S2 | HEAVY最大2只限制并发数量，不等于每profile串行，不能替代状态锁 | 校准版本提交 |
| S18-R2-038 | documentation-or-test-contract | S2 | 对先写磁盘再等HEAVY被429拒绝的路径核对reference_saved状态 | 校准版本提交 |
| S18-R2-039 | documentation-or-test-contract | S2 | 原子JSON替换只保护单文件，候选复制与JSON提交之间仍需一致性设计 | 校准版本提交 |
| S18-R2-040 | pending-evidence | S2 | 校准提交前档案已删除或adapter状态已变化时必须停止，不能恢复旧状态 | 校准版本提交 |
| S18-R2-041 | confirmed-defect-in-stated-scope | S2 | ASR评估全部失败不再用CER0.05冒充实测值，应记录null与失败原因 | 校准缺失与失败 |
| S18-R2-042 | documentation-or-test-contract | S2 | 部分文本ASR失败时记录覆盖率，不能只对成功样本平均后隐藏缺失 | 校准缺失与失败 |
| S18-R2-043 | confirmed-defect-in-stated-scope | S2 | 全部候选合成失败时返回明确未选出有效结果，不能chosen0看似成功 | 校准缺失与失败 |
| S18-R2-044 | documentation-or-test-contract | S2 | 每候选的有效生成条数和预期条数同时保存，评分先验证完整性 | 校准缺失与失败 |
| S18-R2-045 | documentation-or-test-contract | S2 | 未测或低可信声纹指标不填高分默认值，应明确阻塞/降级语义 | 校准缺失与失败 |
| S18-R2-046 | pending-evidence | S2 | 候选排序排除非有限得分，NaN/Inf不进入max选择 | 校准缺失与失败 |
| S18-R2-047 | documentation-or-test-contract | S2 | 模型输出空音频、太短、全静音和缺字分别记失败而不只比声纹 | 校准缺失与失败 |
| S18-R2-048 | pending-evidence | S2 | 校准报告应保留先前有效结果，失败新校准不覆盖为貌似新最佳 | 校准缺失与失败 |
| S18-R2-049 | documentation-or-test-contract | S2 | ASR释放与临时目录清理放入覆盖所有异常的finally路径 | 校准缺失与失败 |
| S18-R2-050 | documentation-or-test-contract | S2 | 错误信息需脱敏且保留阶段，不能把原文和本机私有路径暴露给日志 | 校准缺失与失败 |
| S18-R2-051 | confirmed-defect-in-stated-scope | S6/acoustic | 同目标文本跨GPU诊断使用相同seed，修复100+17*ti+gi的设备偏移混杂 | 双卡诊断 |
| S18-R2-052 | documentation-or-test-contract | S6/acoustic | 将实际seed写入每张卡诊断条目，使测试条件可核验 | 双卡诊断 |
| S18-R2-053 | preservation | S6/acoustic | 会话调度当前各卡同seed的行为应保留，不把诊断偏移引入播放 | 双卡诊断 |
| S18-R2-054 | documentation-or-test-contract | S6/acoustic | 两卡同一voice_binding和voice_conditioning都要进诊断收据 | 双卡诊断 |
| S18-R2-055 | hardware-or-real-model-blocked | S6/acoustic | 记录实际dtype、模型版本、codec政策与DSP后端，不能仅比profile ID | 双卡诊断 |
| S18-R2-056 | hardware-or-real-model-blocked | S6/acoustic | 相同参数不意味着位级相同；阈值评分和人工听感结论分开 | 双卡诊断 |
| S18-R2-057 | hardware-or-real-model-blocked | S6/acoustic | 同文对照与不同文本交替朗读各自设计，不能用同文替代自然衔接 | 双卡诊断 |
| S18-R2-058 | documentation-or-test-contract | S6/acoustic | 所有条目失败时speech_db默认0不应参与一致性，明确缺失项 | 双卡诊断 |
| S18-R2-059 | documentation-or-test-contract | S6/acoustic | consistent布尔值应附完整性及阈值说明，不能称零噪声或100%同声 | 双卡诊断 |
| S18-R2-060 | documentation-or-test-contract | S6/acoustic | 诊断生成在锁定或请求取消后仍进行时保留资源状态，不误报即时停止 | 双卡诊断 |
| S18-R2-061 | confirmed-defect-in-stated-scope | S2/S6 | 校准结束必须检查load_on_workers回执，不能丢弃失败后正常返回 | 加载确认 |
| S18-R2-062 | preservation | S2/S6 | 保留文本/候选接口已有reference_saved与503部分失败语义 | 加载确认 |
| S18-R2-063 | preservation | S2/S6 | Go激活两卡并行、同绑定同模式核验及旧active保留不得回归 | 加载确认 |
| S18-R2-064 | preservation | S2/S6 | 激活最终再次读磁盘核对指纹的检查必须保留 | 加载确认 |
| S18-R2-065 | pending-evidence | S2/S6 | Python reload最终current为None时应视失败，而不是跳过版本核验 | 加载确认 |
| S18-R2-066 | hardware-or-real-model-blocked | S2/S6 | 候选校准只用GPU0的现状须说明；多卡校准需独立计划，不虚报双卡评估 | 加载确认 |
| S18-R2-067 | documentation-or-test-contract | S2/S6 | 加载某卡成功某卡失败后，不允许新会话静默只用成功卡冒双卡一致 | 加载确认 |
| S18-R2-068 | hardware-or-real-model-blocked | S2/S6 | 冷首次sanity合成耗时应与提示提取耗时分开记录，避免首声归因错误 | 加载确认 |
| S18-R2-069 | documentation-or-test-contract | S2/S6 | HTTP断开不等于后台模型加载已停止，未来重试需幂等/状态查询 | 加载确认 |
| S18-R2-070 | preservation | S2/S6 | 不得为降低激活耗时跳过Worker锁内参考前后两次指纹校验 | 加载确认 |
| S18-R2-071 | documentation-or-test-contract | S2/resource | 审查_cal临时profile移除后Worker提示缓存仍驻留的资源生命周期 | 缓存生命周期 |
| S18-R2-072 | documentation-or-test-contract | S2/resource | 重复校准相同临时ID时确保旧提示被替换，不能复用先前参考 | 缓存生命周期 |
| S18-R2-073 | documentation-or-test-contract | S2/resource | 删除档案后清理与它关联的profiles、voice_bindings、levelers和提示快照 | 缓存生命周期 |
| S18-R2-074 | preservation | S2/resource | 缓存释放必须获取合成同一把锁，不释放正在使用的GPU张量 | 缓存生命周期 |
| S18-R2-075 | hardware-or-real-model-blocked | S2/resource | 缓存容量按可测内存预算管理，而不是只看磁盘profile数量 | 缓存生命周期 |
| S18-R2-076 | documentation-or-test-contract | S2/resource | 临时校准ID与用户可启用ID区分，不能由列表选中临时声音 | 缓存生命周期 |
| S18-R2-077 | preservation | S2/resource | 备份继续排除_cal档案，不把测试用临时状态持久化为模型 | 缓存生命周期 |
| S18-R2-078 | documentation-or-test-contract | S2/resource | 临时目录清理失败记录状态并可回收，不无声积累数据 | 缓存生命周期 |
| S18-R2-079 | preservation | S2/resource | 生成器取消仍要close并释放有界codec窗口，不能因缓存修改遗漏 | 缓存生命周期 |
| S18-R2-080 | preservation | S2/resource | 不要盲目清空CUDA所有缓存导致每段冷启动，资源回收须按作用域 | 缓存生命周期 |
| S18-R2-081 | documentation-or-test-contract | S1/S2/UI | 候选点击期间禁用或序列化同档案变更按钮，避免重复并发写 | 前端迟到状态 |
| S18-R2-082 | documentation-or-test-contract | S1/S2/UI | 响应乱序时按操作版本更新高亮，不让旧响应覆盖新选择 | 前端迟到状态 |
| S18-R2-083 | preservation | S1/S2/UI | 继续保留accessEpoch和AbortController防锁定后迟到数据回填 | 前端迟到状态 |
| S18-R2-084 | documentation-or-test-contract | S1/S2/UI | 客户端取消只能停止等待时明确提示后台任务可能继续，不伪报服务器取消 | 前端迟到状态 |
| S18-R2-085 | documentation-or-test-contract | S1/S2/UI | 503且reference_saved时显示已保存未全卡就绪，不能笼统当未保存 | 前端迟到状态 |
| S18-R2-086 | documentation-or-test-contract | S1/S2/UI | 校准报告区分逐候选评分、最终提交、双卡加载三个状态 | 前端迟到状态 |
| S18-R2-087 | documentation-or-test-contract | S1/S2/UI | 没有有效候选或指标不全时不显示成功绿标 | 前端迟到状态 |
| S18-R2-088 | preservation | S1/S2/UI | 参考转写可审阅但日志默认脱敏，token不进URL/localStorage | 前端迟到状态 |
| S18-R2-089 | preservation | S1/S2/UI | 新增条件证明信息只放同源授权接口，不能自动上传外部诊断服务 | 前端迟到状态 |
| S18-R2-090 | preservation | S1/S2/UI | 新增交互保持移动端可操作、录音失败队列保留与锁定清空 | 前端迟到状态 |
| S18-R2-091 | preservation | G0/S8 | 原始库已有revision与lease设计可借鉴，但不直接修改其已成功数据格式 | 来源与保留 |
| S18-R2-092 | preservation | G0/S8 | 候选处理与真实训练继续分开命名，不把评分或缓存称训练提升 | 来源与保留 |
| S18-R2-093 | preservation | G0/S8 | 训练adapter来源hash与固定参考在新条件策略下仍必须核验 | 来源与保留 |
| S18-R2-094 | preservation | G0/S8 | 私有原始样本仍排除Dataset自动备份，新增诊断WAV默认不进入归档 | 来源与保留 |
| S18-R2-095 | hardware-or-real-model-blocked | G0/S8 | 代码、参数和参考版本相同的测试与实际用户WAV声学验收分开报告 | 来源与保留 |
| S18-R2-096 | documentation-or-test-contract | G0/S8 | 为每个确认缺陷建立独立失败样例，后续修复应让同案例先失败再通过 | 来源与保留 |
| S18-R2-097 | documentation-or-test-contract | G0/S8 | 受控AST交错不是线程压力测试；实现后补真实并发和HTTP回归 | 来源与保留 |
| S18-R2-098 | preservation | G0/S8 | 下载wheel仅源码检查不安装旧qwen-tts，避免命名空间冲突 | 来源与保留 |
| S18-R2-099 | documentation-or-test-contract | G0/S8 | 本轮100建议与实际实验范围完整入备忘录，不宣称全源三轮完成 | 来源与保留 |
| S18-R2-100 | preservation | G0/S8 | 第三轮结束及逐题50建议决策完成后才改产品，继续冻结17包与工作台 | 来源与保留 |
| S18-R3-001 | preservation | S6/S7 | 保留16码本、24kHz及1920样本每帧合同，不用未知解码器静默替代 | 生成码窗口 |
| S18-R3-002 | preservation | S6/S7 | 左上下文25帧只保留有界生成码，参考码继续禁止进入输出解码 | 生成码窗口 |
| S18-R3-003 | hardware-or-real-model-blocked | S6/S7 | 默认右前瞻0与实验1/2帧分别记录延迟与真实质量，不用随机codec推断最优 | 生成码窗口 |
| S18-R3-004 | documentation-or-test-contract | S6/S7 | 为每次提交记录全局帧偏移与已提交区间，定位接缝是否重复或漏帧 | 生成码窗口 |
| S18-R3-005 | documentation-or-test-contract | S6/S7 | 区分有效生成帧、保留上下文和待提交PCM，不能把重复解码时间当新语音 | 生成码窗口 |
| S18-R3-006 | preservation | S6/S7 | 取消和异常均close生成迭代器并清理pending，禁止取消后尾包泄漏 | 生成码窗口 |
| S18-R3-007 | preservation | S6/S7 | 实际tokenizer返回错误采样率、非有限值或长度不符继续拒绝 | 生成码窗口 |
| S18-R3-008 | hardware-or-real-model-blocked | S6/S7 | 按首2/4/8帧对照时固定后续策略与文本，不能混入候选或seed变化 | 生成码窗口 |
| S18-R3-009 | hardware-or-real-model-blocked | S6/S7 | 真实codec有限上下文与整段解码差值须用预训练权重另测，不凭因果结构宣布无接缝 | 生成码窗口 |
| S18-R3-010 | documentation-or-test-contract | S6/S7 | prepare_ms不含生成器首次next里的全部预填充，拆分前先验证时钟范围 | 生成码窗口 |
| S18-R3-011 | confirmed-defect-in-stated-scope | S3 | 将整块与不规则分块输出一致性列为DSP算法合同而非只检查有限和长度 | DSP ABI |
| S18-R3-012 | confirmed-defect-in-stated-scope | S3 | NumPy淡入使用固定总长度及已处理位置，不让每次短块重新从零起算 | DSP ABI |
| S18-R3-013 | pending-evidence | S3 | NumPy RMS统计保留不足10ms余数，避免按来包边界重新分组 | DSP ABI |
| S18-R3-014 | pending-evidence | S3 | Rust逐样本平滑与NumPy插值应先定义相同算法再设合理量化容差 | DSP ABI |
| S18-R3-015 | documentation-or-test-contract | S3 | flush后Rust清DC状态而NumPy不清的差别须明确，不能称API语义完全一致 | DSP ABI |
| S18-R3-016 | preservation | S3 | 当前Worker每段重建leveler，不能将跨段复用API问题直接认定为生产根因 | DSP ABI |
| S18-R3-017 | hardware-or-real-model-blocked | S3 | 固定目标电平与最大增益仍不保证两段动态响度相同，保留完整语音测量 | DSP ABI |
| S18-R3-018 | pending-evidence | S3 | 纯静音、阶跃和有声转静音须同时检查滤波残留、削波和增益泵动 | DSP ABI |
| S18-R3-019 | documentation-or-test-contract | S3 | Rust ABI加载需区分不兼容符号和库缺失，不能失败后不告知回退路径 | DSP ABI |
| S18-R3-020 | preservation | S3 | 缺Rust编译器时记录未执行，不用C++重写参考实现冒Rust实测 | DSP ABI |
| S18-R3-021 | confirmed-defect-in-stated-scope | S4 | 120样本以下语音块不能因无完整RMS帧就直接丢弃，设计跨块累积 | 裁剪终止 |
| S18-R3-022 | confirmed-defect-in-stated-scope | S4 | 跨输入块保留35ms有界预滚，而非只在检测到声音的当前块向前取 | 裁剪终止 |
| S18-R3-023 | preservation | S4 | 候选静音与未发声辅音不能仅凭能量绝对区分，试听门禁保留 | 裁剪终止 |
| S18-R3-024 | confirmed-defect-in-stated-scope | S4 | 短末块含有非零语音时须有明确finish策略，不能永久留held后销毁 | 裁剪终止 |
| S18-R3-025 | documentation-or-test-contract | S4 | 尾静音裁剪应记录实际删掉时长和阈值，不把删音频冒首声或RTF提速 | 裁剪终止 |
| S18-R3-026 | documentation-or-test-contract | S4 | 900ms超长首静音放行应保留异常说明，不能把放行静音算实际人声 | 裁剪终止 |
| S18-R3-027 | preservation | S4 | 1800ms held上限必须在长无声生成时仍有界，不引入全句缓冲 | 裁剪终止 |
| S18-R3-028 | preservation | S4 | 输入codec固定1920样本倍数与泛用小块测试分开，标注生产可达性 | 裁剪终止 |
| S18-R3-029 | documentation-or-test-contract | S4 | 裁剪器发出的样本索引需可追溯至模型原始PCM，便于核对漏音 | 裁剪终止 |
| S18-R3-030 | hardware-or-real-model-blocked | S4 | 输入很轻时不要单纯升高裁剪阈值，应比较失真与背景噪声的权衡 | 裁剪终止 |
| S18-R3-031 | preservation | S5 | 保持流式相位和上一个输入样本跨PCM帧连续，不能每帧独立插值 | 重采样收尾 |
| S18-R3-032 | documentation-or-test-contract | S5 | 24k直通与44.1k/48k转换各自验证输入时长和输出样本预算 | 重采样收尾 |
| S18-R3-033 | documentation-or-test-contract | S5 | 终止时缺下一个插值端点应定义末样本延拓或明确短尾策略并测试 | 重采样收尾 |
| S18-R3-034 | preservation | S5 | 重采样收尾不能以补充可计入speech的静音改变RTF分母 | 重采样收尾 |
| S18-R3-035 | preservation | S5 | 每段协议标记不应重置同一朗读流的重采样相位，会制造边界跳变 | 重采样收尾 |
| S18-R3-036 | preservation | S5 | 锁定、取消和新流begin应清掉上一任务的相位及延迟端点 | 重采样收尾 |
| S18-R3-037 | preservation | S5 | 分块与整块重采样在数值容差内一致的现有行为应保留 | 重采样收尾 |
| S18-R3-038 | documentation-or-test-contract | S5 | 一输入样本、空块及极短末块需测试，不只测长整秒波形 | 重采样收尾 |
| S18-R3-039 | hardware-or-real-model-blocked | S5 | 扩展至降采样时需考虑抗混叠，不能将线性插值叫任意采样率高保真 | 重采样收尾 |
| S18-R3-040 | hardware-or-real-model-blocked | S5 | 实体浏览器实际采样率与请求24k可能不同，诊断记录两者 | 重采样收尾 |
| S18-R3-041 | confirmed-defect-in-stated-scope | S5 | 生成结束且剩余20ms音频应有播放或明确失败结果，不能永久buffering | 完成短尾状态 |
| S18-R3-042 | confirmed-defect-in-stated-scope | S5 | 精确50ms边界的严格大于判断需单独测试，不能只测51ms | 完成短尾状态 |
| S18-R3-043 | confirmed-defect-in-stated-scope | S5 | 欠载恢复时最后短尾同样应可排空，避免截掉最后一个音节 | 完成短尾状态 |
| S18-R3-044 | preservation | S5 | 已结束数据的排空政策与持续生成时风险缓冲分开，不盲降正常启动阈值 | 完成短尾状态 |
| S18-R3-045 | documentation-or-test-contract | S5 | 有剩余样本但低于阈值时ended判定须有终止路径，不假装已播完 | 完成短尾状态 |
| S18-R3-046 | documentation-or-test-contract | S5 | 一任务只能产生一次最终结束，迟到统计消息不能把ended改回playing | 完成短尾状态 |
| S18-R3-047 | hardware-or-real-model-blocked | S5 | 长网络抖动和低产出速率下测试启动等待与欠载率成对取舍 | 完成短尾状态 |
| S18-R3-048 | hardware-or-real-model-blocked | S5 | 暂停恢复必须在用户授权AudioContext状态下执行，不自动规避浏览器策略 | 完成短尾状态 |
| S18-R3-049 | documentation-or-test-contract | S5 | 单调时钟中的0值不宜兼任未记录标记，检查极早首包的时间哨兵 | 完成短尾状态 |
| S18-R3-050 | preservation | S5 | 运行原播放器VM只能证明逻辑，不可声称浏览器硬件首声变快 | 完成短尾状态 |
| S18-R3-051 | documentation-or-test-contract | S5/S6 | firstPlayedMs目前是主线程play命令时刻，名称与报表需区分实际消费 | Worklet时钟 |
| S18-R3-052 | hardware-or-real-model-blocked | S5/S6 | 增加首样本消费确认前先定义是否跳过显式停顿和极小淡入样本 | Worklet时钟 |
| S18-R3-053 | hardware-or-real-model-blocked | S5/S6 | Worklet currentFrame与主线程performance属于不同时间轴，使用可解释映射 | Worklet时钟 |
| S18-R3-054 | preservation | S5/S6 | 保留ring样本计数与自然结束不额外记欠载的已通过行为 | Worklet时钟 |
| S18-R3-055 | preservation | S5/S6 | 欠载只计一次直至恢复，避免每个渲染量子重复放大统计 | Worklet时钟 |
| S18-R3-056 | documentation-or-test-contract | S5/S6 | 容量溢出dropped必须进入上层状态和失败提示，不能只在底层计数 | Worklet时钟 |
| S18-R3-057 | hardware-or-real-model-blocked | S5/S6 | 固定192样本淡入在24k/48k分别8/4ms，若要求同毫秒则按实际率配置 | Worklet时钟 |
| S18-R3-058 | preservation | S5/S6 | hold与reset后无旧PCM回放，保留现有重置后精确零输出测试 | Worklet时钟 |
| S18-R3-059 | documentation-or-test-contract | S5/S6 | 环形缓冲溢出属于丢样，不得被统计成已自然连续读完 | Worklet时钟 |
| S18-R3-060 | preservation | S5/S6 | 声卡/系统输出延迟仍需实体设备测量，Worklet消费也不是声学听到时间 | Worklet时钟 |
| S18-R3-061 | documentation-or-test-contract | S6 | 规划器PauseBeforeMs由上一边界生成，逐段记录而不是把所有停顿归模型 | 停顿顺序重试 |
| S18-R3-062 | documentation-or-test-contract | S6 | Worker默认只加显式lead pause，核实tail默认0后再判断重复停顿 | 停顿顺序重试 |
| S18-R3-063 | preservation | S6 | 保留首段零规划停顿，不以参考呼吸或原音占位提前出包 | 停顿顺序重试 |
| S18-R3-064 | hardware-or-real-model-blocked | S6 | 模型内部停顿与规划停顿叠加需实际WAV分层对照，不能只删规划停顿 | 停顿顺序重试 |
| S18-R3-065 | preservation | S6 | 有序转发必须保留，不能为了最快包先播后一GPU导致错序 | 停顿顺序重试 |
| S18-R3-066 | preservation | S6 | 已消费部分PCM后禁止跨卡整段重试，保护不重复词句的现有门禁 | 停顿顺序重试 |
| S18-R3-067 | documentation-or-test-contract | S6 | 未消费重试时正确扣除旧produced样本，维持背压与统计一致 | 停顿顺序重试 |
| S18-R3-068 | hardware-or-real-model-blocked | S6 | first_worker_audio可能是显式静音包，报表不可直接称人声首包 | 停顿顺序重试 |
| S18-R3-069 | hardware-or-real-model-blocked | S6 | 第一段4帧与后段6/8/12帧策略保留可追溯，提速不得改变音色条件 | 停顿顺序重试 |
| S18-R3-070 | documentation-or-test-contract | S6 | 正文保留、引号配对、小数和缩写拆分须有实际Go回归，不靠源码注释 | 停顿顺序重试 |
| S18-R3-071 | preservation | G0/resource/acoustic | 在线推理与离线训练GPU租约保持互斥，不为测试盲停驻留模型 | 训练资源安全 |
| S18-R3-072 | hardware-or-real-model-blocked | G0/resource/acoustic | 真实双卡训练、引用缓存与profile建档继续分开报告，避免功能混淆 | 训练资源安全 |
| S18-R3-073 | preservation | G0/resource/acoustic | 子进程继续清除API与认证秘密环境变量，不因性能诊断泄漏 | 训练资源安全 |
| S18-R3-074 | preservation | G0/resource/acoustic | 模型与adapter来源hash及安全权重格式不能为快速加载而跳过 | 训练资源安全 |
| S18-R3-075 | hardware-or-real-model-blocked | G0/resource/acoustic | 训练数据审阅/完整覆盖与声学验收是独立缺口，18音频修复不自动解决 | 训练资源安全 |
| S18-R3-076 | preservation | G0/resource/acoustic | 取消训练只终止本次进程组，不根据旧PID文件杀其他进程 | 训练资源安全 |
| S18-R3-077 | preservation | G0/resource/acoustic | 保留离线代码与模型指纹核验，不自动开启远程代码或下载权重 | 训练资源安全 |
| S18-R3-078 | preservation | G0/resource/acoustic | 新增诊断原始WAV默认私有且关闭，不能进入公开Git和自动备份 | 训练资源安全 |
| S18-R3-079 | preservation | G0/resource/acoustic | 资源状态的CPU成功不标CUDA或GPU优化成功，尤其是当前无Torch环境 | 训练资源安全 |
| S18-R3-080 | documentation-or-test-contract | G0/resource/acoustic | 剩余复杂训练/恢复路径只有入口边界复核，明确语义深审仍需补齐 | 训练资源安全 |
| S18-R3-081 | preservation | G0/S8 | 正式工作台继续只读核对，不因音频审查改写15文件或HEAD | 交付安全 |
| S18-R3-082 | preservation | G0/S8 | 自命名空白文件、用户粘贴、并发版本冲突和磁盘持久化需保留 | 交付安全 |
| S18-R3-083 | documentation-or-test-contract | G0/S8 | 复制预览与正式工作台分别核对，不能用旧17复制成功冒18完整包成功 | 交付安全 |
| S18-R3-084 | documentation-or-test-contract | G0/S8 | 新发布前固定launcher字节数/hash，并校验53以上实际资产完整性 | 交付安全 |
| S18-R3-085 | preservation | G0/S8 | 剪贴板失败回退应选中完整源代码，不能只复制可见窗口 | 交付安全 |
| S18-R3-086 | preservation | G0/S8 | 文件名、路径穿越、脚本/style闭合注入等既有浏览器测试继续执行 | 交付安全 |
| S18-R3-087 | preservation | G0/S8 | 锁定清理、同源token和迟到响应隔离不能被新指标消息绕过 | 交付安全 |
| S18-R3-088 | preservation | G0/S8 | 旧验证脚本固定历史分支属于历史证据，新分支另建验证器而非改旧收据 | 交付安全 |
| S18-R3-089 | preservation | G0/S8 | 新工具依赖留忽略目录，下载源码也不与模型权重混入发布资产 | 交付安全 |
| S18-R3-090 | preservation | G0/S8 | 所有未执行的Go/Rust/真实浏览器/完整模型实验明确标未执行 | 交付安全 |
| S18-R3-091 | preservation | G0/S8 | 完整manifest读取/hash/AST只证明库存与语法，不声明全源逐行语义无错 | 证据与决策 |
| S18-R3-092 | preservation | G0/S8 | 三轮专题各100完成也不等于所有代码已语义审查三遍，覆盖缺口单列 | 证据与决策 |
| S18-R3-093 | documentation-or-test-contract | G0/S8 | 每个实验写方法、注入边界、实际源hash及探针hash，避免不同版本混算 | 证据与决策 |
| S18-R3-094 | documentation-or-test-contract | G0/S8 | 将已复现缺陷、待验证假设与保留保护分别分类，不将300建议全标已修 | 证据与决策 |
| S18-R3-095 | preservation | G0/S8 | 重建环境仅NumPy和Node时旧模型实验收据保留历史，不算新执行 | 证据与决策 |
| S18-R3-096 | preservation | G0/S8 | 第25题起一次一题，具体选项/推荐/理由/50建议全部记录后再下一题 | 证据与决策 |
| S18-R3-097 | documentation-or-test-contract | G0/S8 | 实施方案要将首声、条件来源、状态一致、DSP、裁剪、播放排空分成可回滚小步 | 证据与决策 |
| S18-R3-098 | preservation | G0/S8 | 产品最终源码冻结后完整三轮回归，当前边界探针不能代替全功能通过 | 证据与决策 |
| S18-R3-099 | preservation | G0/S8 | 零噪声/单一音色/自然朗读及RTF0.3仍需真实WAV和双T4，不用绝对承诺替代 | 证据与决策 |
| S18-R3-100 | preservation | G0/S8 | 第三轮备忘录和缺口完整内嵌提示词，发布18之前仍使用17并保持PARTIAL | 证据与决策 |

详见`validation/step18/g0-recommendation-disposition.json`中的原来源、处置理由、已有关联证据和待执行测试合同。无条目标记修复完成或最终签收。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_TRAINING_CHAIN.md

# 第十八阶段G0第二批：训练数据、声码、原始库与发布链

## 当前结论

本批对12份、1974行源码完成第一遍全文语义阅读。加上第一批6份/930行，当前53资产中第一遍完整覆盖18份/2904行，剩35份尚未获得第一遍全文信用；完整第二/三遍签收仍为0。**这不是全源三遍完成，G0仍未通过。** 53资产外的仓库服务、生成器、测试与工作台也不能遗漏。

实际新增执行：135项CPU/文件/租约/进程内HTTP/安全张量格式专项，每轮失败0、错误0、跳过0，三轮一致；其中125项现有测试、10项新增artifact边界测试。另6项提供包元数据/构造器合同案例，各三轮。未执行完整Torch训练、完整Qwen、GPU、真实用户WAV、实际双T4、浏览器声卡或性能比较。

**新确证项：CPU声码编码器查询了不匹配的发行版名。** `training_codes.py:99`查询`qwen-tts`；项目固定运行栈则为`qwen-tts-hf==0.1.1.post1`，两者共享模块名但不是同一发行版。在HF元数据存在、旧发行版不存在且前置加载步骤成功的条件下，会抛PackageNotFoundError。重型加载步骤由显式fixture代替，版本查询来自真实wheel元数据；因此这是受控的提供包收据合同复现，不宣称完整编码器已经在目标环境运行。

产品源码/冻结包/正式工作台未改，未创建18。25–27题、300条原建议与第一批收据保留。此次新增发现另存`g0-training-chain-findings.json`，只关联原建议，不把300条历史建议重写成已修。

## 第一遍全文范围及语义结果

### 1. training_data.py：1–285

- canonical_wav先审RIFF总长、fmt/data唯一性、完整chunk和PCM16单声道24k，再作预算及常量拒绝；只规范容器，不自动重采样、截断或把强弱变化识别为语音。
- prepare要求权益/单人声明严格为true、逐样本转写、唯一ID和选中的参考；全局存储锁内获取原始库revision/lease，临时目录完整写入/verify后rename；异常BaseException清理。
- 单样本上限min(240秒,配置)，总输入min(900秒,配置)，参考≤16秒。长录音上传能力不等于可直接把一条20分钟音频训练；长数据拆分仍需正确逐段音文与用户数据审阅，不能按比例编造转写。
- manifest/jsonl/音频/分配计划独立hash，确切成员及租约保护；lease不长持全局锁，但阻止合作式删除。它证明内容/结构和来源声明，**不证明转写、权益、身份或训练质量**。
- rank_plan是数学分配说明；tts_training.epoch_indices才是运行时采样。两种算法不同不自动是错，但报告不能把前者当后者的执行轨迹。

### 2. training_codes.py：1–355

- 材料化本地tokenizer目录拒symlink/hardlink/pickle/auto_map和不安全shard映射；CPU/FP32/eager/offline加载，加载后检查24k、1920、16码本及2048词表。hash与结构不是权重质量证明。
- 每条声码帧数ceil(frames/1920)、16个严格整数、0..2047；处理每样本前后查取消，来源租约和全局代码锁内准备，临时目录异常清理，发布前复核输入/hash和取消。
- schema2封存原始manifest/jsonl，核对去掉audio_codes后的行、参考、逐样本hash；不是只有一个外部source_id。fixture始终test_only_codes，不能以“结构正确”升级为真实tokenization。
- lease/adopt用同inode/实际flock/共享描述符保护跨进程读；与训练admit及真实语义审核分开，不能把拿到FD当训练授权。
- **F01**：99行旧发行版版本查询不匹配HF栈；原测试`test_adapter_loader_contract_with_stub_imports_no_real_model`把所有metadata.version替换为stub-only，因此测试通过不能反驳此缺陷。`tts_training.provider_version`已有HF优先的轻量函数体可用于对照，但本步不修改或跨模块导入Torch来“快速修”。

### 3. voice_library.py：1–351

- 原始库与建档/训练分开；私有目录、普通文件/owner/nlink/NOFOLLOW/NONBLOCK、revision、字节预算、独立构建lease保留。重复字节内容去重不等于单说话人或音频语义去重。
- add先写独立样本，再原子JSON提交，失败移除新增文件；remove_sample先更新索引再清孤儿。_sweep只清允许的孤儿/临时文件，不递归删除独立profile。
- snapshot检查选中集合、revision、文件大小/hash，持续持有库lease；begin/finish另外维护reference_prepared/processing_failed；不能把这个状态称训练完成。
- list/get的busy只是合作锁观察，不是GPU占用。目录祖先/恶意同UID改动、跨进程崩溃一致性仍需后续第二/三遍与威胁边界复核，不能称文件系统绝对安全。

### 4. trained_profiles.py：1–155

- inspect核对完成记录、Base/codes/sample/LoRA绑定、两rank每epoch集合与更新记录；再校验真实safetensors字节hash、键/shape/float32/有限值及adapter摘要。
- 这些是**可信本地文件中的记录一致性**，没有硬件签名/执行证明。本批手写rank报告只用于验证拒绝/解析路径；即使describe返回training_execution_recorded，也不能拿它证明本批真的执行NCCL或优化器。
- publish需显式ack、来源代码租约、schema2真实编码状态、样本集合及唯一对应参考转写；临时目录完整写入并再次inspect后rename。它不会自动改变active，质量/推理重载继续false。
- 输出profile包含一份参考锚点和转写，属于现有profile备份范围；CLI确认说明此点。原始库、完整训练数据和adapter不因此进入自动Dataset备份。
- trained binding只允许显式trained后端，禁止Base/Mock静默回退；artifact pin是内容一致性，不是用户认证或声学评分。

### 5. tts_dataset.py：1–125；tts_training.py：1–200

- dataset深拷贝行、严格声码布局/范围、text token布局及max_sequence预算；超长样本报错而非截断。有界cache返回token/code克隆，参考mel共享；完整真实tokenizer与长数据适配仍需模型实验。
- collate保持独立text/codec mask、16码本与EOS标签；JointLoss在DDP.forward内部执行文本投影及talker/subtalker损失，不绕过DDP对参数的追踪。
- epoch_indices使两rank步数一致，奇数数量显式重复前缀而不drop_last；它不意味着绝不重复样本。梯度累积最后不足一组按实际group_size归一；跨rank有限值共识、溢出跳更新及摘要一致性检查。
- run_rank要求恰好两CUDA设备/NCCL，加载本地安全格式模型与固定speaker，所有样本长度先查后更新；训练结束核验参数变化/两rank摘要与模型来源。优化器/权重更新/保存的真实执行本批均未测。
- load_adapter不等于部署；不保存optimizer恢复状态，不能叫可精确断点续训。FP32 LoRA、FP16基础模型、真实吞吐/显存/质量权衡都不能由源码或CPU格式测试签收。

### 6. lora_adapter.py：1–91；adapter_engine.py：1–108

- 只选择talker及其code_predictor attention的q/v线性层，基础参数冻结，FP32 A/B；restore先全量校验再copy。prepare先构造全部替换，commit异常回滚，切换和生成必须由Worker同锁串行。
- trained引擎显式sentence-buffered；它传入保存speaker向量而不是ICL参考码，不能把它称Faster流式或默认单锚点ICL，也不能承诺改善首声。
- 每次_select重新读档案与固定artifact/来源；正确构建prompt后再提交adapter；输出检查24k/一条完整一维有限非零音频，取消会丢弃整句结果但不能抢占正在执行的CUDA kernel。
- Worker调用锁、两卡有效条件和真实输出仍须后续跨模块完整复核。源码相同/seed相同不证明两GPU声学同声。

### 7. qwen_compat.py：1–97；CLI三文件共207行

- 固定Faster0.5.4/HF0.1.1.post1/Transformers5.20.2；共享模块命名空间不能据此允许旧发行版并装。RoPE桥只认具体registry与default schema，不猜theta；配置smoke不是完整模型实验。
- encode_training.py 1–128：子进程离线CPU/清列举秘密；Linux父死SIGKILL及arming后ppid复查，bounded private报告，超时/取消只停本次进程组。SIGTERM/创建子进程竞态等完整生命周期还需后续第二/三遍覆盖，不能只凭注释签收。
- train_tts.py 1–49：参数预算与内部rank入口分离，公开错误脱敏；fingerprint不加载模型，未完成返回非成功。
- trained_voice.py 1–30：显式发布未验证候选，ack含参考锚点进入profile备份的说明；错误pin/来源不得静默替换。脚本可达不等于已经有UI真实训练按钮或实际训练数据。

## 本批执行方法与边界

### 135项专项×3轮

`run_training_chain_regressions.py`选择test_training_data、test_training_codes、test_code_provenance、test_libraries、test_qwen_compat与新增test_training_artifact_boundaries。每轮135通过、失败0/错误0/跳过0；这是子集，不是本阶段最终全功能三轮。

新增10项使用真实NumPy/safetensors序列化/解析：合成artifact合法解析、错误manifest pin、张量篡改、更新hash后仍拒非有限值、拒float64、每epoch覆盖缺失、无ack不inspect、fixture代码不能发布、禁止未训练后端回退、错误绑定ID/hash。rank报告明确手写fixture；未运行torch/LoRA计算/Gloo/NCCL/声学生成。

### 6项provider合同×3轮

`fetch_chain_metadata.py`从PyPI下载HF0.1.1.post1 wheel，SHA256固定`ed5b7aae64cf795243369fb5226173f459a45689ea86db1c6d3eb14fc0c2c01d`；仅提取METADATA至忽略.cache，不安装HF/旧Qwen，不导入其代码、不取权重。来源URL与METADATA hash见chain-provider-provenance.json。

`training_provider_probe.py`在独立进程限定sys.path，使metadata读取真实HF METADATA，确认旧发行版不存在；原编码器仅重型加载/桥接用fixture，随后真实版本查询按原码抛错。另证明宽泛版本stub会隐藏问题、错误模型pin在loader前拒绝、原训练provider_version函数体能识别HF，以及仅有元数据不满足运行栈门禁。**退出0表示复现到预期旧行为，不是编码器已修复。**

新增依赖只有忽略.venv中的safetensors0.6.2，用于真实NumPy格式测试；NumPy保持2.2.6。未安装Torch、Qwen发行版、模型权重或替换生产依赖。缺失.cache时按fetch工具重新获取经固定hash核验的元数据，不改历史round2收据。

## 后续门禁

1. 当前18/53仅是第一遍全文，另35资产及外围仓库、完整第二/三遍继续推进；不因本批测试数较多就通过G0。
2. 下一批优先Go安全/会话/调度及对应协议链，随后覆盖完整前端与启动恢复；跨链的Worker锁、训练CLI进程竞态也需复查。
3. F01加入后续最小修复/失败测试清单；不能安装旧qwen-tts来消除异常，不能使同模块命名空间冲突，不借修收据启用新模型或更改默认声音模式。
4. 300建议仍是初审映射、未逐条最终签收。全功能三轮、真实长数据训练、同文双卡及自然长文/无沙沙/首声/RTF≤0.3仍独立BLOCKED。
5. 25–27题不变，不机械追加问题28；若后续发现必须选择的新方案，再按一次一题、50建议规则记录。当前产品未改、18未生成，整体PARTIAL/BLOCKED。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_GATEWAY.md

# G0第三批：Go安全、会话、调度及协议链补审（未签收）

## 结论与范围

本批全文语义第一遍新增13份、3527行；累计31/53资产、6431行，尚有22项未完成第一遍。完整第二、第三遍仍为0。三轮测试不是三遍全文语义审查，更不是完整产品功能/声学验收。G0仍未通过，S1未开始，产品与原始–17冻结包、正式15文件工作台均不修改。

实际执行Go 1.23.9，启用CGO与race detector，不下载Go模块。测试副本逐文件核验与53资产基线一致；新增探针放在kaggle/tests，仅临时复制到忽略目录与原包一同编译，不把审计代码写入冻结网关。

## 全文阅读覆盖及语义记录

下表范围均为1至所列末行，含实现、注释和测试。精确源哈希与逐文件状态见g0-gateway-coverage.json；不把目录清单、测试执行或局部交叉查阅计为第二/三遍完成。

| 文件（kaggle/source/go/gateway/） | 末行 | 全文语义核对重点 |
|---|---:|---|
| security.go | 247 | Bearer鉴权、访问令牌、浏览器origin、JSON与上传预算、安全代理和出错路径；既有鉴权功能保留 |
| llm.go | 137 | DeepSeek流式HTTP、SSE增量、前缀文本、取消传播；未连接真实上游 |
| main.go | 478 | 路由与代理、profile激活、预检、私有字段与状态、请求上下文及流式响应；不将HTTP测试称浏览器验证 |
| scheduler.go | 490 | 健康与负载分配、任务租约、最大三次尝试、PCM消费后禁止重试、相同会话seed/绑定、帧校验与完成统计 |
| session.go | 692 | 分段按序转发、背压、取消/生产量、会话指标与快照；已复现快照别名竞争 |
| segmenter.go | 489 | UTF-8与标点边界、单位/时长估计、首段与尾段、原文拼接、聊天增量与朗读；测试不证明自然韵律 |
| fidelity_test.go | 187 | 文本保真、UTF-8与原文拼接既有断言的覆盖边界 |
| preflight_test.go | 67 | 已有预检与profile合同，失败不静默绕过 |
| reliability_test.go | 159 | 截断、有限重试、取消与顺序既有断言；缺失异常帧组合另增探针 |
| security_test.go | 342 | 认证、origin、预算、代理与私密状态既有保护案例 |
| segmenter_test.go | 123 | 中英文、尾段与不同切分策略；不是模型内容质量测试 |
| voice_binding_test.go | 113 | profile/绑定/conditioning固定、训练模式拒绝边界；相同参数不等于双GPU音色相同 |
| go.mod | 3 | module qtts/gateway；Go 1.21声明；本环境执行1.23.9，非目标Kaggle工具链实测 |

## 三轮独立执行与失败分流

每轮分别调用原包与哈希匹配副本，均使用`go test -race -json -count=1`，未依赖缓存测试结果。编译缓存只缓存编译产物。

| 类别 | 第1轮 | 第2轮 | 第3轮 | 能说明什么 |
|---|---:|---:|---:|---|
| 原网关主测试 | 40通过 | 40通过 | 40通过 | 含子测试各56通过、0失败/跳过 |
| 新增边界探针 | 10通过 | 10通过 | 10通过 | 5个保护合同+5个原缺陷观察；观察通过≠修复 |
| 独立竞争见证 | 非零退出且DATA RACE | 同左 | 同左 | **预期失败**，不得并入无失败的回归统计 |

`go vet ./...`退出0。原始、合同和竞争日志分别保存在gateway-{original,contract,race-witness}-round1..3.jsonl，机器收据为gateway-audit-round1..3.json。不是全仓三轮完整功能验收。

新增5个保护合同：已消费PCM禁止重试；未消费重试清空与样本计数一致；取消使实际本地HTTP工作请求停止且busy释放；两个本地worker请求保持同seed/voice_binding/conditioning；大于32MiB帧在分配前拒绝。它们不执行模型，也不证明两个真实GPU输出相同。

## 新增确认问题（均未修复）

### S18-G0-GO-F02：指标快照共享run map产生编码竞争

session.go:659–689：snapshot只复制slice，未复制每个run map；mergeClient稍后在锁内写同一map，快照的JSON编码在锁外。顺序探针先取snapshot再merge，证实先前快照内容改变；独立并发见证对原Metrics同时mergeClient与json.Marshal(snapshot)，三轮race detector均报告encoding/json/reflect读取与session.go:664写入竞争。

这是实际执行原方法的合成并发，不是线上压测/外网利用证明。潜在后果包括不一致与map并发读写故障，不能把本见证称线上崩溃复现。未来修复要明确快照所有权、嵌套对象不可变/深拷贝合同与锁范围，再保留无竞争验证；当前不改产品。

### S18-G0-GO-F03：工作进程帧合同校验不足

scheduler.go:351–407，真实本地HTTP fixture每轮复现四项：

1. 3字节PCM16负载被转发，样本计数以n/2取整为1。
2. 没有PCM、仅声明audio_s=0.01的stats仍被标记served。
3. 非法JSON错误帧`{`被忽略，后接合法stats仍成功。
4. 合法stats后仅2字节的下一帧头被忽略，仍成功。

本地工作进程是受信任边界；这不等于外部攻击入口。探针没有修复这些问题，也没有证明当前模型正常输出会触发它们。未来应规定PCM16对齐、统计与实收PCM一致、错误JSON与截断流失败策略，且不能让已消费PCM重试产生重复语音。

## 仅源码观察/待验证，不升级为已确认运行缺陷

- W01：scheduler.go:428的queue_wait_ms在完成时赋值，含生成耗时；Q26已记录该含义。没有用延迟fixture测出真实排队时间，不宣称性能改善。
- W02：healthLoop忽略HTTP状态及JSON解码错误；本批未增加有界健康循环故障fixture，仍待验证，不能宣称已复现错误健康判定。
- 上游SSE行预算、慢客户端写阻塞/超时为后续评估问题，未运行针对性压力实验。

## 真实本地协议链：仅选择3类，各内部3轮

1. mock_pipeline.py：实际Go→两个Python mock worker，鉴权、按序原文拼接、生成fixture帧、两worker被使用、关闭流后恢复；播放欠载为事件模拟，非声卡试听。
2. library_gateway_check.py：实际Go→analyst→文件系统，空库、超JSON预算上传、重启恢复、CAS/删除、原始hash；损坏音频处理**预期失败**，不称解码成功。
3. training_gateway_check.py：同链及合成PCM16训练输入快照、样本转写、hash篡改拒绝、租约禁止删除、源删除后副本仍在；未执行tokenizer/优化器/训练rank。

gateway-protocol-receipt.json记录脚本/hash/日志与每轮实际输出。没有重跑全部历史6类：adapter_gateway_check需要当前缺失Torch；codes_cli_check与ownership_process_check本批未选，不借历史通过冒充重新执行。

## 保持与下一步

新F02/F03另列g0-gateway-findings.json，不改原300条处置映射和训练链F01。Q25–27及各50建议文件保持hash不变，不为此自动新增Q28。历史各批覆盖、收据与验证器保留；新验证器只验证本批证据边界，不把旧验证器硬编码数量改成当前数。

继续G0剩余22项的前端、Python运行/分析、DSP/启动与恢复源码第一遍及外围脚本；之后完成全源第二、第三遍和建议映射更新，才可通过G0并进入S1。真实用户WAV、完整模型、实际训练、双T4同条件声学、物理首声/RTF≤0.3、无沙沙和自然完整朗读仍未验收，整体PARTIAL/BLOCKED。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_FRONTEND.md

# G0第四批：前端录音、流式播放与隐私生命周期补审（未签收）

## 当前结论

本批新增完整语义第一遍3份、2217行；累计34/53资产、8648行，剩19项未完成第一遍。完整第二、第三遍仍为0。三轮浏览器运行不是三遍源码语义审查，也不是全功能/完整模型验收。G0未通过，S1未开始，产品与原始–17包、正式工作台均未修改。

实际Chromium执行三轮，每轮134项（原123项+新11项）通过，失败/跳过/重试/波动均0。新增11项中8项为保护合同、3项为原缺陷观察；后者通过表示旧行为复现，**不表示修复**。另对原Player/Parser/Worklet运行22项边界及16项延迟合同VM探针，各三轮；Node30、JS语法与只读repack一致性检查通过。

## 全文语义覆盖

所有行均按编号全文读取，精确hash与覆盖见g0-frontend-coverage.json。历史台账保留，不将此前局部VM抽取或本次执行次数补记为完整第二/三遍。

| 文件 | 范围 | 本批全文核对 |
|---|---|---|
| kaggle/source/web/app.js | 1–1715 | 1–35帧拼接/大小限制与JSON；36–92 Worklet环形队列；93–381速率预测/音频初始化/有界启动/重采样/尾部/指标；382–584同源鉴权/epoch/解锁/诊断/视图；585–860流式turn/取消/错误/报告；861–1069档案/转写/候选/校准/一致性展示；1070–1208录音列表与创建任务；1209–1316诊断轮询；1317–1535库管理/修订/取消；1537–1630训练输入文本、声明、固定hash验证/删除；1632–1715初始化/键盘/pagehide |
| kaggle/source/web/recorder.js | 1–358 | 会话epoch与权限等待、输入约束、原生录音与分析器连接、字节/块数/时长预算、真实输入波形读数、停止与封装超时、最终文件/取消清理；发现error回调遗漏会话所有权核对 |
| kaggle/source/web/index.html | 1–144 | DOM ID/脚本顺序、默认锁定与密码字段、两主视图/对话框/焦点/响应式与短屏降级、16/24秒参考选择、训练输入而非训练按钮、未验收说明；静态措辞不证明真实声学 |

剩19项包括analyst/worker/bootstrap/supervisor、音频DSP与Rust、参考/库API/绑定、工具及LICENSE/MEMO；外围仓库也不能由53资产清单替代完整审查。

## 三轮执行和原功能保护

运行器：docs/validation/step18/run_frontend_audit.py。每轮独立启动测试服务器/Chromium测试进程，retries=0；临时工作区由原tests/e2e-server.js创建和清理，不操作正式workspace。原qtts.spec.js、studio.spec.js与Playwright配置均保持hash不变；新增tests/browser/g0-frontend.spec.js只提供审计测试。

| 类别 | 每轮数量 | 轮数 | 结果与边界 |
|---|---:|---:|---|
| 原浏览器回归 | 123 | 3 | 共369通过；鉴权/迟到响应/录音容器/预算/库与输入/布局/键盘/工作台编辑及剪贴板 |
| 新保护合同 | 8 | 3 | 共24通过；详见下列保护点 |
| 新原缺陷观察 | 3 | 3 | 共9次一致复现；均未修复 |
| 原Player边界VM | 22 | 3 | 合同与已知缺陷观察各三轮；短尾滞留仍存在 |
| 原延迟合同VM | 16 | 3 | 指标/完成短尾/恢复阈值；注入时钟不是测得性能 |

每轮浏览器总134、三轮402通过；不将VM案例另加到浏览器测试数。原始JSON报告frontend-browser-round1..3.json，退出码/原始报告hash/逐项结果/测试源hash/观察附件见frontend-audit-round1..3.json。所有轮次无失败、跳过、retry或flaky；并不等于全部用户要求通过。

新增8个保护点：
1. 字节级分片的PCM帧重组，-32768/0/32767保持正确有符号缩放，只有收到的生成PCM帧进入Player；这是fixture数据，不证明真实模型未加词。
2. 有结束汇总但尾帧截断时显示明确错误，不静默成功。
3. 缺结束汇总时报错。
4. 明确停止能中止待处理语音请求signal。
5. 旧录音data事件不能污染新会话。
6. 旧录音stop事件不能清理新会话/设备。
7. 录音字节溢出丢弃块与片段，不保存部分超限录音。
8. 权限等待取消后，迟到stream被停止，不保存片段，等待期间不累积设备请求。

原工作台回归在隔离临时工作区验证自命名空文件、用户粘贴/保存/恢复、剪贴板权限拒绝与逐字节复制；包括第1–17阶段完整源码包的逐字节剪贴板测试；原始kaggle文件在浏览器用sentinel验证保留，真实原始文件另外按冻结hash核对，不能把sentinel测试称完整原始文件复制。本批没有创建第18阶段包，也没有更改正式工作台。

## 三处新增确认行为：均未修复

### S18-G0-WEB-F04：迟到录音error回调会停止新会话

recorder.js:182–184的onerror没有像ondataavailable、track-ended一样检查owns(session)。在实际Chromium内加载原完整recorder.js，用明确的MediaRecorder/设备fixture：旧会话epoch1取消后启动新会话epoch3，再调用旧onerror；新会话从recording变为stopping，新track被停止。三轮一致。对照保护证明旧data和stop不会破坏新会话。

这是原回调的确定性交错复现，不证明真实设备在任何一次录音必然触发迟到error。未来最小修复需补所有权检查并保留原生自动停止、断线保存、预算丢弃与隐私清理合同；本批不改产品。

### S18-G0-WEB-F05：流协议解析失败未立即取消reader/请求

app.js:721–790，JSON.parse或parser异常进入catch/finally时，只标记generationDone并恢复按钮；未取消局部reader或中止当前controller。Chromium内用浏览器原生Response/ReadableStream对象构造不闭合的HTTP流fixture，发送完整type2帧但JSON为`{`：错误显示后，cancelCount=0、signalAborted=false、streamLocked=true，且报告已发送。三轮一致；之后明确停止会使signalAborted=true。

证明的是协议异常路径缺少显式取消，不是对真实Go/worker连接或GPU资源泄漏的压力实测；浏览器GC/连接回收与后台工作时长没有测量。未来须在当前turn仍拥有请求时取消reader/abort，并避免旧turn误停新turn，保留正常生成后已缓冲PCM的完成策略。

### S18-G0-WEB-F06：addModule失败留下未撤销Blob URL

app.js:210–224只在await addModule成功后revokeObjectURL，init.catch关闭context但未撤销该URL。Chromium原生Blob URL创建/撤销调用被计数，addModule显式注入拒绝后created=1、revoked=0、speak请求=0，三轮一致。浏览器页面离开可回收相关资源；本批没有测量堆增长/真实设备失败频率，不能宣称测得内存泄漏大小。

未来应保证失败/成功路径都回收临时URL，同时保留可重试init、并发共享初始化与取消后不迟发HTTP的已有合同；本批未修。

## 已知问题与仅源码观察

- 已有20/50ms完成短尾滞留、命令时间被标作firstPlayedMs、重采样终端flush政策仍未修；本批VM重新执行，不包装成新发现或提速。
- app.js:784–818在生成结束时停止活跃遥测并发送报告，可能早于实际缓冲排空；本批未增加“晚发生欠载/最终报告覆盖”专用实机实验，仍是源码观察，后续需按Q26度量合同验证。
- Candidate选择及profile异步动作的重叠顺序、Worklet状态跨turn的迟到消息预算等仍需专门故障注入；本批未实证，不签不存在。
- SNR/一致性/校准页面字段来自后端估计和条件测试，不能由UI标签签真实音质或推断用户沙沙根因。

## 环境和不能越过的证据边界

本轮起初浏览器测试依赖未安装，按现有package-lock执行npm ci --ignore-scripts补齐忽略node_modules；package.json、package-lock及产品依赖未改。浏览器由现有npm内置Chromium配置运行，不下载外部CDN浏览器。版本信息见frontend-environment.txt。

原套件部分用**原生Web Audio/MediaRecorder API**，但输入来自振荡器或静音MediaStream fixture；11分钟/2640块案例为虚拟时间，不是物理长录音。新11项使用明确模拟的AudioContext/MediaRecorder/权限与HTTP，完整冻结脚本和DOM在实际Chromium执行。VM探针没有浏览器设备。API返回为测试fixture，不是本批真实Go/DeepSeek/完整Qwen/GPU。物理麦克风、声卡首声、用户WAV、听感、相似度、自然连续朗读、无沙沙、同条件双T4及RTF≤0.3均未验收。

## 保持与下一步

新F04–F06单列g0-frontend-findings.json；原300建议初审、Q25–27各50建议、前批F01–F03与全部历史收据保持不变。当前覆盖以g0-frontend-coverage.json为准；交接提示词完整内嵌本备忘录。下一批先补Python运行/分析/启动恢复链及DSP/工具等剩19项，再完成全源第二/三遍与建议处置更新；不预填Q28、不跳过G0先实施S1。整体PARTIAL/BLOCKED。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_RUNTIME.md

# G0第五批：Python启动、监督、工作进程与绑定链（未签收）

## 结论与实际覆盖

本批全文语义第一遍新增5份、1536行；累计39/53资产、10184行，尚有14项未完成第一遍。完整第二、第三遍仍为0；专项测试三轮不是全源三遍语义审查。G0未通过、S1未开始，产品/原始–17包/正式工作台不改。

| 文件 | 本批完整范围 | 语义核对重点 |
|---|---|---|
| kaggle/source/py/bootstrap.py | 1–451 | 导入副作用与状态目录；有界子进程与进程组超时；平台Torch保护/发行包身份；工具与模型获取；GPU门禁；恢复；supervisor当前startup_id故障收据；只停止本次创建进程；隧道认证与失败路径 |
| kaggle/source/py/supervisor.py | 1–219 | 子进程角色环境最小化；租约FD/nonce继承；仅自身进程组终止；退避/崩溃循环；健康/致命配置；缓存重载；周期快照；信号、PID与lease清理 |
| kaggle/source/py/worker.py | 1–680 | 模型加载前设备/租约；T4 dtype策略；参考缓存/绑定；生成码适配器调用；锁/取消/静音停顿；逐段DSP/裁剪；统计/错误帧；重启；异步响应队列与HTTP生命周期 |
| kaggle/source/py/clone_stream.py | 1–126 | ICL/xvector输入；生成码窗口/左上下文/可选右看；有限样本率与长度；取消/尾部/生成器关闭；参考码只作conditioning，不传codec。未运行真实Torch窗口或完整生成 |
| kaggle/source/py/voice_binding.py | 1–60 | 文件名/类型/大小/O_NOFOLLOW；UTF-8与长度前缀跨语言hash；gen默认值、数值/布尔/非有限校验。它是内容绑定，不是身份认证/声学分数 |

精确hash及逐文件范围见g0-runtime-coverage.json。当前剩14项：analyst.py、audio_rt.py、library_api.py、reference_segments.py、Rust Cargo.toml/lib.rs、6个工具、LICENSE及MEMO；外围仓库仍有独立审查范围，不由53项台账替代。

## 三轮专项回归与进程协议

每轮独立Python进程执行原G0的84项CPU/安全/租约/可靠性专项，再加10项新运行边界，合计94项；三轮均0失败/错误/跳过，共282通过。新10项为7保护+3原行为观察；捕捉旧缺陷通过不等于已修。

运行器run_runtime_audit.py，逐项结果、源与测试hash、三份观察见runtime-audit-round1..3.json；unittest日志为runtime-regression-round1..3.txt，stdout/stderr另存runtime-round1..3-console.txt。既有测试未修改，历史G0/训练/Go/前端收据不重写。NumPy回退被明确强制，未编译或执行Rust。

新增7个保护：
1. 关闭实际synth异步响应迭代器会设置生产者cancel Event，CPU替身生产线程能退出。
2. 错误voice_binding在任何静音/生成PCM之前失败，不启动engine.stream，并释放锁/busy。
3. 原RealEngine.load_profile只清除同路径prompt缓存，保留其他路径；不启用参考静音增强或参考PCM拼接。
4. 真实文件hash复核既有跨语言字面值17f55c…；采样参数变化改变绑定；bool/小数top_k/非有限值拒绝；符号链接不接受。
5. 即使breath_bank含非零参考数组，原lead_audio仍只输出有界全零计划停顿，不拼接参考音频。
6. 无效clone模式与缺失ICL转写拒绝，不静默回退。
7. 工作帧5字节小端长度头与Unicode统计JSON一致。

另实际执行两个现有协议脚本，各内部3轮，由run_runtime_protocols.py串行调用：

- ownership_process_check.py：真实supervisor、POSIX FD继承/租约、worker/analyst角色继承、gateway不继承、离线争用409、停止后可重新预约、PID清理。**模型角色是CPU stand-in**，没有真实GPU/VRAM或训练。
- fatal_startup_check.py：真实supervisor与本地HTTP致命健康替身，当前startup_id故障收据、bootstrap.wait_ready快速停止、仅本次Popen关闭、子进程退出及PID清理。没有实际触发真实模型MimiConfig加载错误。

脚本hash、实际退出码与每轮JSON输出见runtime-protocol-receipt.json及runtime-protocol-*.txt。不是重跑全部历史6类协议，也不是完整启动Kaggle模型/隧道/下载链。

## 新确认行为：均未修复

### S18-G0-RUNTIME-F07：异步响应队列没有容量与生产反压

worker.py:650–673：asyncio.Queue()默认maxsize=0，emit仅call_soon_threadsafe(q.put_nowait,item)，不等待消费者。直接执行原synth，使用有界CPU生产替身排入512个小PCM帧及终止哨兵；未消费时观察maxsize=0、队列513项，随后正常消费并清空。三轮一致。

这是应用层容量/反压缺口，不是测得无限内存增长或外部DoS。fixture不是TCP慢客户端压力；真实模型token上限、Go单worker并发、ASGI/socket缓冲和取消共同影响实际占用，尚未测量。后续策略需在有界排队、跨线程投递、断连取消、终止哨兵和阻塞退出间建立合同，不能直接塞一个会抛QueueFull的put_nowait后声称修复。

### S18-G0-RUNTIME-F08：重载失败后engine prompt缓存与已接受绑定不原子一致

worker.py:257–275、396–409、452–466：RealEngine.load_profile先更新_prompts，再由Worker复核文件绑定。已缓存成功参考A；把文件改成B并重载，显式resolver替身读取B、随后把磁盘恢复A，Worker正确检测重载中变更而抛异常。但engine._prompts已是B，Worker旧profiles/voice_bindings仍是A；下一任务以当前A的正确pin进入，缓存存在判定不触发重建，原run_job调用的生成替身拿到B prompt。

三轮观察：failed_reload_rejected=true，当前文件与接受pin匹配=true，缓存prompt与当前文件匹配=false；初次+失败重载resolver共2次，下一job未重建且未标failed。

实际执行原Worker和RealEngine.load_profile及真实文件hash；重型resolver/prompt/stream和GPU清理明确为fixture。没有执行真实ICL提取、Qwen/codec或听到错误声音。这是确定性失败原子性控制流复现，不冒称线上并发HTTP或音色混淆已声学复现。后续应设计准备/验证/提交与失败回滚或缓存失效合同，并与Q25的候选/绑定版本一致性一起保留测试；当前不改产品。

### S18-G0-RUNTIME-F09：模式规范化与报告/会话检查不一致

clone_stream.py:13–22用strip().lower()接受` XVECTOR `，返回xvector=true、空ref_text；worker.py:65–70对原环境值做精确比较，反而报告icl-generated-only-codec。三轮直接调用原函数一致复现；未运行模型。

这会使被接受的有效条件与报告字段不一致；不等于证明真实双GPU声音不一致。后续需统一规范化/拒绝政策并保证请求pin、加载回执、health和实际生成条件相同；不能通过更换UI标签掩盖实际条件。当前未修。

## 仅源码观察或仍阻塞的验证

- bootstrap的后台模型下载join没有总体期限；Go/cloudflared获取未见固定版本内容hash校验、Rust引导运行远端脚本。此批未访问/执行这些下载或安装路径，不能称验证了供应链/可用性故障。
- 子进程启动OSError后gave_up、非worker健康失效、全部关键进程退出时的总退出政策，仍需专用故障矩阵；现有致命健康用例不涵盖所有启动失败。
- Worker after_job在锁释放后执行、重启与忙状态交错、长生成/慢客户端真实资源峰值，仍需压力/生命周期补验，不将源码疑点写成实证缺陷。
- 原trimmer预滚/短尾、NumPy分块依赖、指标语义等历史问题仍未修；本批不是DSP新实现。
- GeneratedCodecWindow和fast_generate_streaming的真实Torch/完整模型路径未执行；没有靠安装假Torch把它们签为真实codec测试。源码生成码隔离意图/文件pin/fixture调用不等于真实声纹、无额外语音或同条件双卡声学证明。

## 保持、归档与下一步

新F07–F09另列g0-runtime-findings.json，原300建议初审映射/Q25–27各50项/F01–F06和各历史验证器保持hash不变。新台账不把本批测试当成全源第二/第三遍。Node30、JS/新测试语法、5份Python AST及只读repack/冻结一致性检查均通过；正式15文件工作台未动，没有18发布包。

下一步补剩14项的分析/API/参考切分与DSP/工具/说明全文，再完成全源第二/第三遍和建议处置更新，不跳G0先实施S1，不预填Q28。用户录音、完整权重/真实训练、双T4同条件输出、自然连续朗读、首声/RTF≤0.3及无沙沙仍未验收；整体PARTIAL/BLOCKED。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_ANALYSIS_DSP.md

# 第十八阶段 G0 第六批：分析/API、参考切分、Python/Rust DSP

## 1. 本批结论与边界

2026-10-23，活动分支 `arena/1160bd87-kagglee`。延续已完成第五批，不改冻结产品，不重开 PR2、不预填问题28、不生成第18阶段发布包。本批是**全文第一遍补审与限定范围执行验证**，不是已实施首声/声质优化，也不是完整三轮全功能/模型验收。

- 本批新增全文第一遍 **6份、2152行**；累计 **45/53、12336行，剩8份**。
- 完整第二遍、第三遍仍均为 **0**。三轮专题各100建议及问题25–27各50建议保留，不冒充全源三遍语义审查。
- **172项×3轮=516项通过**，每轮失败/错误/跳过均0。其中旧测试160项，新12项：9保护、3 `OBSERVED_NOT_FIXED` 原行为见证。旧测试中也含已知缺陷见证，不能将总通过数解释为没有缺陷。
- 另行 **14个分析端AST控制流案例×3轮**、**12个NumPy合成DSP案例×3轮**。与单元测试存在行为重叠，不相加冒充独立完整功能覆盖。
- 新确认 F10–F12 三类边界，**均未修复**。历史校准/候选缺陷、NumPy分块依赖也仍复现。
- 实际执行：原Python函数、NumPy DSP、requests/TCP本地HTTP、库进程内ASGI与本地文件操作。重型ASR/embedding/模型生成使用明确fixtures。
- 未找到 `rustc`/`cargo`；Rust两份文件**只完成源码审查**，未编译、未跑内置Rust测试、未加载实际Rust库。不用NumPy结果替代Rust运行证明，不为完成语言数量安装来源不明编译器。
- 无Torch/Qwen完整权重/CUDA、真实DeepSeek、用户WAV、物理声卡及双T4；没有证明相似度、无沙沙、自然连续朗读、RTF≤0.3或真实提速。

冻结基线继续为53资产、94冻结hash与15正式文件；本批保存295个既有文档/收据/脚本hash，旧证据不改写。NumPy为实际2.2.6，不是需求文件中的2.4.6。Starlette/httpx的弃用警告保留在控制台，未为消除警告擅改产品依赖。

## 2. 全文第一遍范围

全文阅读分段进行；analyst最初只读到1050行，补完1051–1211后才计入覆盖，不把部分阅读提前记全文。其余5份也均完整读完。阅读区间不是运行覆盖率。

| 资产 | 行数与完整区间 | 本次重点 |
|---|---:|---|
| `kaggle/source/py/analyst.py` | 1211，1–1211 | 解码/上传限额、ASR/speaker生命周期、指标、worker帧协议、候选评分/重叠选择、校准、旧API、consistency |
| `kaggle/source/py/audio_rt.py` | 222，1–222 | ctypes符号与参数、NumPy DC/AGC/淡入/尾部、转换、极短breath |
| `kaggle/source/py/library_api.py` | 163，1–163 | 严格JSON、multipart、修订CAS、租约、共享准入、后台任务提交/失败/清理、错误脱敏 |
| `kaggle/source/py/reference_segments.py` | 106，1–106 | 有效时间戳、词级校验、长段窗口重转写、短尾收据、原文不可按比例切割 |
| `kaggle/source/rust/audio_rt/Cargo.toml` | 17，1–17 | cdylib/rlib、无第三方依赖、2021 edition、release LTO/abort，未实际编译 |
| `kaggle/source/rust/audio_rt/src/lib.rs` | 433，1–433 | Leveler跨块状态、DC/AGC/淡入/flush、noise、unsafe C入口、内置测试；只读源码 |

覆盖台账：`docs/validation/step18/g0-analysis-dsp-coverage.json`。旧 `g0-runtime-coverage.json` 等保持为历史检查点。

## 3. 按模块的语义结论

### 3.1 分析、候选、校准与指标

1. build内embedding缓存按规范化float32内容hash；命中返回copy，build之间不共享。新保护验证float64/非连续输入规范化及调用者修改不污染缓存。它是缓存，不是训练。
2. 全参考参与分析/统计与centroid，最终至多三候选按评分和同文件重叠规则选择；实际ICL仍用选中锚点。保留“全部音频参与统计不等于全部同时进入模型prompt”的透明边界。
3. 评分涉及长度、帧能量分位差、ASR logprob、speaker相对centroid、F0离散度及语速。分数不是人声相似度真值；低RMS截图不能定位沙沙声来源。
4. `synth_full`用于离线校准/诊断，不能继承浏览器/Go已做的协议校验来假定安全。其HTTP状态、终结与残留校验不足独立记录F12。
5. 本次14项AST重跑保留：ASR不可用仍CER0.05、旧评分提交期间更改后的转写、重载失败回执被忽略、全合成失败仍chosen0；均是确定性交错/依赖fixture，不是线程压力测试。
6. 旧 `/candidate` 存在bool/小数强转及null/容器未捕获异常；本次9个输入案例重新执行。不能用该结果推断严格库JSON路由也同样接受。
7. `consistency`同文调用seed100/101不同的旧诊断行为再次验证。正式播放同会话seed一致的功能不得被这条诊断观察反向改坏。fixture返回相同speaker值不是真实双卡等效参数或声学一致性证明。
8. 建档两个worker加载失败后任务是否仍done、旧修改/删除接口与校准并发、实际HTTP竞争、缺CER/proxy值是否进入质量门禁，继续列为待证/待设计，不把本轮14个AST例说成覆盖全部。

### 3.2 原始参考库API

完整读取库路由及其依赖的既有32项测试：严格请求体、CAS/lease、选择检查、后台任务、共享准入、失败释放、提交顺序、去重、完整性与私有错误脱敏。重跑实际本地文件与进程内HTTP；后台语音处理为fixture。

保护“成功状态晚于元数据提交”“失败保留原样本及上一成功profile”“请求取消不能丢租约”“executor提交失败不能稍后执行排队修改”“库样本不自动成为可播放模型”。这些是现成功能保护，不是新增了真实训练按钮/训练闭环或验证语音质量。

### 3.3 参考切分

- 合法短段直接用段级文本与时间戳；可选词信息不可信时短段分支清空，不能按字符比例把全文分给不同音频。
- 长段优先使用与词全文一致且时间合法的词分区，否则对**真实对应音频窗口**重转写。新增保护验证32秒由两个16秒窗口产生自己的文本，第二窗口词时间平移16秒。
- 小于1.5秒尾段记录 `short_tail_s`，不与上一段全文拼成伪对齐。17秒fixture实际仅对前16秒重转写，尾1秒不生成候选文本；保护的是“明确报告而非伪造对齐”，不宣称最后1秒已被ASR转写或完整训练覆盖。
- 重转写结果词信息的清洗弱于直接短段分支，详见F11。坏词元数据是明确注入；真实Whisper在用户录音中是否产生相同数据仍未测。

### 3.4 NumPy与Rust DSP

NumPy原函数实际执行；Rust源码显示持有跨调用能量累计与完整淡入位置，flush重置DC状态。NumPy的分块RMS/增益插值、剩余长度重启淡入以及flush保留DC状态需独立同信号同分块对照。当前Worker每段新建leveler这一调用约束必须保留；不能把复用同一个leveler的潜在差异直接当作当前用户播放故障。

本次重跑既有半秒24kHz双音实验12组合：

| 设置 | 分块 | 对整块最大int16差（三轮一致） |
|---|---:|---:|
| target−6 / maxgain0，隔离淡入与DC | 48样本 | 1424 |
| 同上 | 1920样本 | 0 |
| target−18 / maxgain6，正常AGC | 48样本 | 1425 |
| 同上 | 1920样本 | 8 |

这是**工程分块依赖**，不是经过主观试听的接缝损伤、噪声根因或GPU路径对照。没有修正数值，也没有测得质量/性能改善。

新保护还覆盖正常长度breath确定性/长度/有限值、非连续float转连续布局、空输入meter、PCM饱和不回绕、Leveler空/非有限值输入、热信号限幅及尾部归零、close幂等。非有限输入清洗仅验证NumPy路径，不扩展到未执行Rust。

Rust的C入口空指针保护、slice长度/所有权、调用方串行化、版本门槛与符号完备、错误返回值处理仍须真实ABI验证；Python只捕获装载OSError、不检查每个DSP返回码等是**源码待测观察**，不在本轮虚报ABI故障复现。Cargo内置测试未运行，未生成或签收 `.so`。

## 4. 新确认但未修的三个边界

### S18-G0-ANALYSIS-F10：NumPy极短breath形状

`audio_rt.py:86–102`，24kHz卷积核6，`same`输出长度为输入与卷积核长度最大值：
- 请求1样本，实际返回6样本；
- 请求2/3/4/5样本，分别抛ValueError（包络广播不兼容）；
- 请求6样本，返回6；常规64/1920/24000长度保护通过。

直接原函数/真实NumPy执行。只是合成helper边界，**没有播放参考PCM**，未证明当前worker正常分块会触发，更未证明用户沙沙根因。后续修复必须保证长度且不重新启用参考呼吸拼接。

### S18-G0-ANALYSIS-F11：窗口重识别的可选words漏清洗

`reference_segments.py:96–103`，注入合法段时间与字符串text，但可选words为四元组，重识别分支列表推导解包直接ValueError；同样metadata在短段分支被清空。三元组的text=None可被保留进输出。

原helper实际执行，ASR结果显式fixture；未运行真实Whisper，也没有声称实际端到端build崩溃已执行。后续pause/prosody路径依赖word字符串，仅作为需保护的下游风险说明，不能将潜在AttributeError当作本次新跑出的证据。

### S18-G0-ANALYSIS-F12：分析端不完整/失败流被当作正常返回

`analyst.py:361–385`，使用真正requests + ThreadingHTTPServer本地TCP，原 `synth_full` 实际解析：
1. HTTP503携带PCM/空stats：正常返回2样本；
2. PCM后残留2字节header：正常返回2样本、空stats；
3. PCM后未完整到达的stats payload：正常返回2样本、空stats；
4. stats为 `failed:true`：正常返回音频与failed字段，未抛错；
5. HTTP200空体：正常返回0样本、空stats。

同时保护完整分片UTF-8 stats/PCM，以及显式ERR帧正确抛RuntimeError。这证明分析端协议验证缺口，**不是实际worker模型故障已发生，也不是公开网关利用验证**。没有运行HTTP慢客户端/无上限payload压力或资源泄漏测量。

三条状态均 `confirmed...not_fixed`，新见证通过只意味着原失败行为稳定复现。机器台账：`g0-analysis-dsp-findings.json`。原300建议初审不改写，新观察单列。

## 5. 三轮执行与证据链

每轮运行：

```bash
.venv/bin/python docs/validation/step18/run_analysis_audit.py --round 1
# --round 2 / --round 3 相同目标、独立进程执行
```

172项构成：原G0 84 + runtime 10 + RecordingTests 6 + step15 16 + step17 12 + libraries 32 + 新analysis 12。明确不选需要Torch的 `test_step14.CacheTests`；没有把跳过训练测试算成通过。本轮选中项实际skip为0。

每轮另执行：
- `reference_state_probe.py` 中4校准+9候选输入+1consistency，直接调用旧probe函数，共14。**本地旧upstream解包cache不存在**，因此未跑历史6个prompt接口案例，没有偷偷重建/重签旧wheel收据。旧20案例历史收据保持不变。
- 原 `dsp_partition_probe.py --round N`，12个真实NumPy合成分块组合，保存原始stdout与JSON。

| 轮次 | unittest | 分析AST案例 | 合成DSP案例 | 失败/错误/跳过 |
|---|---:|---:|---:|---:|
| 1 | 172 PASS | 14完成 | 12完成 | 0/0/0 |
| 2 | 172 PASS | 14完成 | 12完成 | 0/0/0 |
| 3 | 172 PASS | 14完成 | 12完成 | 0/0/0 |

主要文件均位于 `docs/validation/step18/`：
- `analysis-audit-roundN.json`：逐测试ID、结果、新观察、53源码hash、测试/runner/support hash、依赖、原log hash、真实性标记。
- `analysis-regression-roundN.txt` / `analysis-roundN-console.txt`：原始测试及console；模拟失败异常与无GPU门禁输出属于预期测试输入，不能据console中ERROR字样误判成功收据，也不能将自检工具的内部SKIP展示当成执行了模型测试。
- `analysis-contracts-roundN.json`：4+9+1 AST函数控制流细项、原probe/source hash。
- `analysis-dsp-roundN.json` / `.txt`：原12组合数值、probe/source/hash与原stdout。
- `analysis-preserved.json`：本批开始时295个既有历史文档/收据/脚本hash，旧签收不因新handoff自动变更。
- `analysis-toolchecks.json` 与对应日志：Node30、JS检查、Python AST、repack一致性检查。
- `analysis-environment.txt`：本机依赖、Rust/模型环境边界。
- `verify_analysis.py` / `analysis-progress-verification.txt` / `progress-analysis.json`：本批独立一致性验证；`progress-checks.json`指向当前检查点，旧验证器和旧收据原样留存。

独立验证器必须确认53源码/94冻结/正式资产、历史295份、原300建议及问题25–27、45/53/12336、三轮目标一致、观察稳定、所有log/test/probe hash、handoff逐memo原文一致。不能以“写出JSON”替代实际断言。

## 6. 后续精确顺序

本批不另开关键设计题；问题25–27各50建议、推荐C保持。仍按G0→S1–S8门禁执行，不跳至DSP产品修复。第一遍剩8份：6个工具 `backend_probe/e2e_check/resource_control/selftest/voice_benchmark/watermark_check` 与 `LICENSE-QWEN-DERIVED.txt`、`MEMO.md`。先读完并补各自执行边界，再补全源第二/第三遍、300建议最终处置与失败见证映射。

Rust真实编译/内置测试/ctypes同信号对照、实际HTTP并发更新、完整模型/双卡/用户录音/长数据真实训练仍是显式缺口；如环境缺失继续标BLOCKED，不把source read变成runtime PASS。必要设计问题继续逐题≥50建议，不提前问用户，不要求点击Continue。

所有性能和声学不变要求仍在：真实首可用DeepSeek prefix立即生成、生成PCM-only、更响且受保护、更低创建延迟、>10分钟录音与真实训练的区分、<10秒参考相似度、双GPU同等参数/声音、自然连续朗读、无沙沙及真实RTF≤0.3。当前没有真实新优化或声学验收，整体 **PARTIAL/BLOCKED**。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_TOOLS.md

# 第十八阶段 G0 第七批：工具、LICENSE 与历史 MEMO

## 1. 结论：53项内嵌资产第一遍完成，G0尚未完成

2026-10-23，活动分支 `arena/1160bd87-kagglee`。本批新增8份全文第一遍、1332行；累计 **53/53、13668行、第一遍剩0项**。这是53项内嵌资产的覆盖口径，不是整个Git仓库全部文件或全源三遍语义审查完成。完整第二遍/第三遍仍 **0/0**，G0与发布验收仍 **PARTIAL/BLOCKED**。

- **197项专项×3轮=591通过**：每轮失败/错误/跳过均0。
- 构成：上批172 + 既有probe 13 + 本批新12。新12为 **9项保护、3项OBSERVED_NOT_FIXED见证**。既有项中也有已知缺陷见证，总通过数不意味着产品无缺陷或已修复。
- 三轮各独立执行4个CLI：backend静态/隔离runtime、benchmark默认无`--run`均返回预期exit2/BLOCKED；resource status返回exit0。**预期阻塞合同通过不等于GPU/模型成功。**
- 新确认工具误报通过 F13–F15，均未修复；另记录MEMO文档漂移 D01，不混成第四个运行缺陷。
- 53源码、94冻结hash、15正式工作台文件保持不变；本批开始封存329份历史文档/脚本/收据hash，旧报告不随最新handoff重签。
- 本批没有产品改动、没有18发布包、没有实际训练/完整模型/GPU/Rust编译/物理声卡/真实DeepSeek/用户WAV或质量/提速验收。

## 2. 全文第一遍范围

所有文件按行分段读完，输出截断处另行补读；只在全文读完后计入台账。

| 文件（相对kaggle/source） | 全文区间 | 重点 |
|---|---:|---|
| `tools/backend_probe.py` | 1–200 | 元数据/精度/API surface、隔离子进程、deadline、进程组终止、报告权限/原子提交、exit语义 |
| `tools/e2e_check.py` | 1–180 | 9字节网关帧、文本/统计/END/ERR、顺序、GPU计数、模拟播放与退出门禁 |
| `tools/resource_control.py` | 1–41 | 只读status、1..3600秒预约、租约、信号恢复、拒绝/取消/失败exit |
| `tools/selftest.py` | 1–177 | 各检查的PASS/SKIP/FAIL、NumPy/Rust标签、worker健康/流、e2e/quality调用、报告写入 |
| `tools/voice_benchmark.py` | 1–168 | 显式运行门禁、双worker健康/pin、严格帧与样本数/RTF、私有WAV/ledger、不覆盖证据 |
| `tools/watermark_check.py` | 1–145 | 消费与telemetry线程、水位/饥饿/排空、帧校验、chatter指标与退出判断 |
| `LICENSE-QWEN-DERIVED.txt` | 1–201 | Apache2授权/专利终止/分发条件/变更与归属通知/NOTICE/商标/免责声明，末尾Alibaba Cloud版权 |
| `MEMO.md` | 1–220 | 当前页头与历史阶段混排、数据/训练/隐私/真实验收边界、与当前17源码策略核对 |

本批覆盖：`docs/validation/step18/g0-tools-coverage.json`；保留此前各批覆盖JSON原样。全源第一遍补齐不能解除第二/第三遍或300建议最终处置/失败映射门禁。

## 3. 模块结论与现成功能保护

### backend_probe

默认只查metadata，不安装/下载模型。runtime在有界子进程内检查CUDA及实际调用形状；surface pass也明确不表示模型加载、推理、训练、性能通过。保留T4 BF16/未经批准FP32阻断、签名bind与额外必需参数检查、导入异常脱敏、子进程deadline、原子0600报告。

既有13项probe测试本轮独立重跑三次，虚拟GPU和兼容smoke仅是显式fixtures。新测试及独立CLI又实际启动隔离runtime子进程：本环境缺Torch/Faster，输出blocked、devices空，model_loaded/inference_verified/training_verified/performance_verified均false，exit2，不冒充CUDA成功。真实超时后的全部后代退出与child退出码/报告一致性仍需更完整故障矩阵；现有timeout测试为受控Popen/killpg fixture，不宣称本批真实杀过挂起模型导入树。

### resource_control

仅本机status/预约，不接任意命令、不强制解锁、不运行GPU任务。状态与诊断记录不是显存空闲证明。新保护验证私有临时namespace下fresh status/非法时长不创建锁文件，竞争拒绝后原holder仍busy、SIGINT/SIGTERM处理器还原。既有32项ownership相关测试还包括真实子进程/OFD/flock/信号及预约生命周期；该历史套件本轮实际重跑，不能将CPU锁实验叫GPU工作。

### voice_benchmark

默认无`--run`直接blocked，既不合成也不把CPU/Mock当双卡证明。新CLI保护实际保存0600报告，并验证第二次相同路径拒绝覆盖；该拒绝目前会产生FileExistsError/非零而非结构化重试收据，未改产品。

`measure`已有比另三个诊断工具更严格的HTTP状态、16MiB帧界限、64MiB PCM预算、终结后禁止数据、残留/失败/取消/未知引擎/pin/anomaly/样本数/RTF一致性检查。新本地HTTP测试保护15个协议/统计拒绝分支及HTTP503拒绝；只通过header声明超大帧，不分配16MiB或64MiB攻击体，未做大包内存压力。

合法fixture为240 speech samples+192 tail，fake worker元数据及全零PCM，仅验证解析/分母排除padding。该fixture中的engine字符串/统计数字不是真实Faster、可听语音或RTF成绩；本批没有调用benchmark的真实`run=True`，也没有生成用于声学验收的WAV。真实双worker身份、dtype/参数同等、私有pin与听感仍须目标设备验证。

### e2e_check / selftest / watermark_check

三者是运维工具，不应继承浏览器或网关的协议保证来替代自身验证。既有空E2E失败保护保留；新测试同时保护显式ERR、HTTP非200失败、SKIP/FAIL/PASS区分、模拟短尾排空与已知欠载。

`e2e_check.simulate_player`在所有到达后可立即排短尾；不代表实际浏览器Player的已知完成短尾问题已修复。watermark消费线程不是浏览器Worklet，也没有实体音频输出；source注释“exactly like browser”不构成等价证据。selftest的 `t_rust`即使NumPy回退也可执行，其名字不能证明Rust已编译；本批不运行完整selftest.main或quality网络链，不访问真实worker/analysis/gateway。

## 4. 新确认且未修复的三个误报通过边界

### S18-G0-TOOLS-F13：E2E硬门禁仍接受无效证据

原 `run`/二进制parser/`main`，真实requests+有限本地HTTP fixture，4种输入各三轮：

| case | 实际行为 |
|---|---|
| stats缺gpu字段 | `{None}`长度为1，默认min-gpus1竟通过；输出展示过滤None后仍看不到设备 |
| END含failed/cancelled=true | 只要求END存在，不拒绝失败字段，RESULT PASS/exit0 |
| PCM payload为3字节 | `ln//2`静默向下取整，RESULT PASS/exit0 |
| 合法流后残留2字节下个header | EOF残留未校验，RESULT PASS/exit0 |

fixture有segment/PCM/stats/END，不是历史空流例。**没有实际Go网关、模型或GPU**。这说明工具的验收可信性不足，不说明真实双卡已失败、公开网关已被利用或正常音频已受损。

### S18-G0-TOOLS-F14：watermark零音频也PASS

原 `main`、player/telemetry线程实际执行，本地HTTP三类：空503、显式网关ERR帧、残缺header。各自均 audio=0、first play=None、starvations=0，最后RESULT PASS/exit0；高水位分支仅提示文本太短，不使结果失败。

没有验证HTTP状态/有效PCM/END/ERR/残留，因此“未播放无欠载”可变成通过。测试捕获并等待工具两个daemon线程退出，避免线程污染后续轮次；这不等于产品已新增finally/join，也不覆盖网络/JSON异常时线程清理。没有证明真实调度水位或chatter性能正常。

### S18-G0-TOOLS-F15：selftest失败/取消Mock流仍报stream通过

原 `stream_once`与装饰后的 `t_stream` 实际调用本地HTTP，送3帧各12000样本以及 `failed:true,cancelled:true,engine:mock` 的stats。原检查仅依据分块数、到达/总时间、audio>1秒、无anomalies字段，返回True且status passed。

时间为显式确定性fixture，端口列表只有一个本地fixture worker，**不是测得首声/吞吐或双GPU结果**。不推断整个selftest.main会退出0，因为其他检查没有在这条见证中一起执行。stream_once的HTTP/终结校验弱项也列后续统一修复合同，不重复计成其他新bug。

三条状态均 `confirmed_with_explicit_local_http_fixtures_not_fixed`。197 PASS中的见证是“仍可复现”而非“已修复”。机器台账 `g0-tools-findings.json`，原300建议处置文件不改写。

## 5. LICENSE与MEMO结论

### 许可证：保留文本，不作法律认证

读完Apache2各条及附录，特别保留分发附许可证、修改文件显著说明、来源归属/版权保留以及**若上游分发含NOTICE则按条件携带**。专利授权/诉讼终止与商标权限不同，AS IS不等于无需遵守条件。文本末尾有2026 Alibaba Cloud版权；这一存在性不证明所有依赖、模型权重、音频和再分发许可已完整核验。

本地source未发现NOTICE文件，不能据此推断上游原发行版必定没有NOTICE或已违规。旧upstream解包cache缺失，未在本批重下载所有依赖或重新认证其许可证。后续发布仍需来源/修改标记/NOTICE与依赖及权重许可清单；用户语音授权另行核对，许可证不自动授予他人声音权。当前不修改冻结许可证，不出具法律合规签收。

### 文档漂移 D01（不是第四个运行缺陷）

`MEMO.md`页头称当前step15，写vector-only、不回退ICL、maxgain12；当前冻结17源码为默认ICL、generated-only codec、默认maxgain6。旧历史段落还混有14/11/10“当前”字样、已过时录音预算/训练入口边界，以及第83行短呼吸不再广播异常的笼统说法（F10已在极短2..5样本复现）。

新旧阶段曾经的推荐不等于最新策略；不能据MEMO重启参考PCM拼接、改回纯向量、认定网页训练已完成或把历史TorchCPU证据当本机现有依赖。bootstrap诊断会摘出旧“当前版本修复”段，原始console也可见历史14文字，应以manifest/最新阶段报告为准。这里只做本地源码对照，不额外执行安装器，也不篡改历史MEMO；未来新发布包应在新版本说明中消歧，保留旧包hash。

## 6. 执行、证据和环境

运行命令：

```bash
.venv/bin/python docs/validation/step18/run_tools_audit.py --round 1
# --round 2、--round 3，独立进程、同一197项目标
```

| 轮次 | unittest | fail/error/skip | 独立CLI | 其中预期BLOCKED |
|---|---:|---:|---:|---:|
| 1 | 197 PASS | 0/0/0 | 4合同符合 | 3 |
| 2 | 197 PASS | 0/0/0 | 4合同符合 | 3 |
| 3 | 197 PASS | 0/0/0 | 4合同符合 | 3 |

新12预检也全部通过，原始日志 `tools-preflight.txt` 保留，不另计第四轮。没有为凑数把unittest中的内部工具SKIP输出计成模型执行；选中的unittest层级skip实际0。没有重跑上批另行14AST/12DSP或历史Chromium/Go race全协议，旧收据继续有效为历史证据，不称本轮全量重跑。

主要证据位于 `docs/validation/step18/`：
- `tools-audit-roundN.json`、`tools-regression-roundN.txt`、`tools-roundN-console.txt`：197逐ID/观察、53源hash、测试/runner/support hash、原日志与依赖。
- `tools-cli-roundN.json`及 `tools-{backend-static,backend-runtime,benchmark-default,resource-status}-roundN.{json,txt}`：实际CLI命令、预期/实际exit与原始报告/log hash；exit2按阻塞保存。
- `tools-preserved.json`：329既有历史文件hash；旧验证器/收据保持检查点版本，不随新handoff改写。
- `g0-tools-coverage.json` / `g0-tools-findings.json`：53项第一遍覆盖、F13–15与D01。
- `tools-toolchecks.json`、对应Node/JS/Python AST/repack日志，`tools-environment.txt`。
- `verify_tools.py` / `tools-progress-verification.txt` / `progress-tools.json` / `tools-run-manifest.json`：独立检查源码/冻结/正式文件、历史、300建议/QA、三轮一致性、逐log/测试hash、handoff原文；`progress-checks.json`更新指向本批。

实际Python3.11、NumPy2.2.6，不冒充requirements NumPy2.4.6。没有Torch/Qwen/CUDA/rustc/cargo；HTTP为有限本地fixtures，音频为零PCM/合成信号，设备/API smoke含显式虚拟对象。没有实际训练数据/声纹外传，无GitHub凭据或访问口令写进报告，所用token仅固定本地fixture字符串。

## 7. 下一步与未解除门禁

第一遍已无剩余项。下一步转入**全源第二遍**，以53资产完整台账逐份做调用链、失败传播、并发/版本提交和度量语义交叉复核；第三遍再独立反证/回归映射。现有专项重复执行不能自动给某文件第二遍完整阅读计分，也不能把3×100专题建议当作这两遍已完成。

保留300建议原ID与初审，后续补到最终处置/失败见证；F01–F15及D01均按真实边界处理，不将15编号直接解释成15个互不重叠根因。只有需要重大设计选择才按顺序开启新题并给≥50行动建议，本批不预填问题28，不向用户索要Continue。

在G0完成前不跳到S1/Q28/18包。真实首可用DeepSeek prefix触发、更低创建延迟、更响受保护输出、generated-only PCM、自然连续朗读、<10秒参考相似度、>10分钟录音与真实长数据训练、双GPU同等参数/声音、无沙沙与真实RTF≤0.3全部仍未豁免；当前只是工程审查第一遍里程碑，非产品/模型/声学发布签收。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_PASS2_TRAINING.md

# 第十八阶段 G0：全源第二遍第1批——训练执行与资源所有权

## 1. 进度与结论

2026-10-23，活动分支 `arena/1160bd87-kagglee`。承接第一遍53/53、13668行检查点，本批**重新逐行读完8份、1056行**并交叉复核调用/失败/租约链，正式第二遍为 **8/53、1056行，剩45份**；第三遍0。不是重复跑测试就给第二遍阅读计分，也不是全源第二遍已经完成。

- **219项×3轮=657通过**，各轮失败/错误/跳过0。旧197 + 另选现有artifact10 + 新12；新12为11保护、1个 `OBSERVED_NOT_FIXED` 见证。
- 新确认 F16：原 `stop_ranks` 对忽略SIGTERM的额外后代存在清理缺口。实际CPU子进程、pidfd、继承OFD及flock执行；未修复。测试最后定向清理所有fixture后代并验证锁释放。
- 正常生产 `run_rank` 没有DataLoader子进程，本次额外后代明确构造；**未证明正常Qwen训练发生了这条故障**，未运行真正训练rank。
- 没有Torch，不执行任何张量/optimizer/Gloo/NCCL测试。AST只抽出纯Python采样、赋值提交回滚及dataset构造/len，不模拟Torch算子，不将其称为训练成功。
- 53源/94冻结hash/15正式文件不变；开始时382个历史文档/脚本/收据hash封存。旧300建议初审和问题25–27各50条保留。
- 无产品改动、无18包、无完整模型/GPU/Rust/物理声卡/真实训练/用户录音/提速或声学验收。G0仍 **PARTIAL/BLOCKED**。

## 2. 本次重新完整阅读与不计分的局部阅读

| 文件 | 第二遍重新阅读区间 | 复核重点 |
|---|---:|---|
| `py/training_job.py` | 1–227 | 内容pin、预算、两类租约、准入、子进程环境、信号屏蔽/启动登记、停止/结果、原子checkpoint |
| `py/gpu_ownership.py` | 1–151 | 固定namespace、inode/OFD/nonce/模式、继承/duplicate关闭、诊断非权威、最后引用释放 |
| `py/resource_limits.py` | 1–172 | multipart预预算/重放、构建记录与准入所有权、HTTP取消与执行器提交失败门闩 |
| `py/tts_training.py` | 1–200 | JointLoss/DDP.forward、codec/text位置、采样/累积、全rank finite、更新/digest/保存与退出 |
| `py/tts_dataset.py` | 1–125 | 文本格式/裁尾假设、16组codes、序列拒绝非截断、cache复制、mask/label/index与单batch布局 |
| `py/lora_adapter.py` | 1–91 | q/v目标、Base冻结、FP32 A/B存储、严格restore、prepare-before-commit、BaseException回滚 |
| `tools/train_tts.py` | 1–49 | public参数、内部受控rank路径、结构化退出、私有rank日志与公开错误 |
| `tools/resource_control.py` | 1–41 | status/预约预算、GPU工作标记false、取消/拒绝/信号还原 |

共8份1056行。第二遍计分证据为当前报告与 `g0-pass2-training-coverage.json`，各份第一遍信息原样保留。

另交叉查看 `training_codes.py` 的lease_with_fd/adopt_lease、`encode_training.py` 的arm_parent_death、`supervisor.py` 的Proc生命周期，以及现有控制器/所有权/产物测试。这些是**局部调用点/测试阅读**，不把对应依赖文件记成全文第二遍。

## 3. 跨文件语义复核记录

### 3.1 CLI→controller→rank→训练核心

1. public `train` 参数由argparse设类型；实验确认/数据审阅与schema2真实编码准入不可由fixture bypass进入正式CLI。既有Admission8项中实际CLI拒绝fixture的合同本轮继续执行。
2. controller先持码读取OFD核验固定manifest，核验Base及speech tokenizer内容pin，再查训练依赖，最后获取offline-reservation。拒绝时不自动停推理、不下载模型、不替换默认引擎。
3. GPU整组租约与码读取租约通过pass_fds分别传给两个受控rank；信号在Popen到登记process之间屏蔽，避免取消丢PID。父进程保存自己的引用，rank接管duplicates后关闭原继承FD，不使用LOCK_UN释放共享OFD。
4. rank在Torch/CUDA导入前设置Linux PDEATHSIG并重核ppid；随后解除继承信号屏蔽、检查rank和请求，再接管offline及码租约。码接管再次验证目录/内容/manifest，并不绕过正式训练admit。
5. 已有六项ControllerLifetime测试在CPU替身下运行真实Popen/lease/PDEATHSIG，覆盖无checkpoint的双exit0不能成功、timeout、单rank失败、第二次spawn失败、offline显式接管、控制器SIGTERM/SIGKILL。其内部注入admit/dependency/模型fingerprint，不是真实模型rank或优化器。
6. controller完成后在父租约仍持有时再verify码、Base及checkpoint manifest存在。这里只是父端完成检查；完整产物语义还依赖受控rank写出合同及后续TrainedArtifacts验证，不把manifest存在当作独立优化器或质量证明。父端语义复核加固仍是待测/待设计项，本轮未用恶意假rank伪造“真实训练成功”证据。

### 3.2 OFD与资源准入

- fresh打开同一inode不等于持有同一个open file description；新保护用实际fresh FD验证adopt拒绝，原holder保持busy。
- inference_guard默认只接管inference；offline FD不能作为启动推理的默认许可。新测试失败后原holder仍持有，最后close后释放。
- child_environment只清理列出的凭据键/旧lease/PYTHONPATH，设置离线与线程限制，保留CUDA可见性；它不是任意名称凭据的全面沙箱。新保护用固定fixture值验证枚举清理和真实私有lease导出，不在证据中保存token/nonce值。
- BodyBudgetMiddleware先spool再解析，含unknown-length独立实际字节限制，重放完才透传receive。HeavyAdmission在HTTP取消后仍等执行真正结束才释放；run_in_executor提交可能先排队后启动失败，submitted门闩阻止拒绝任务迟执行。相关既有安全/库API测试均包含在组合中；不是OS内存/CPU隔离或全部ASGI事件矩阵证明。
- BuildAdmission.start的slot预先获取由调用方负责，start不再次acquire，线程启动失败由调用方释放；不把单个文件的finally读成整个链已完整。原调用点部分查阅不能算analyst/library_api全文第二遍。

### 3.3 dataset / JointLoss / LoRA（源码结论，张量运行仍阻塞）

- dataset深复制rows，缓存tokens/codes并在命中返回clone；reference_mel仍共享，不将cache当作训练/新增参考融合。新AST构造测试只验证深复制/预算/计数，不运行tokenizer或collate。
- 文本token布局包含固定格式与末5 token裁尾假设；codes要求非空16列、0..2047；tokens+codes+8超预算拒绝而非截断。mask、speaker固定位置6、BOS/EOS和label移位重新按源码推导；仍须实际固定Qwen tokenizer/张量验证，不能把AST构造当作mask数值一致。
- JointLoss把参数相关路径放在DDP.forward内部，包含text_projection、speaker条件、16-codebook嵌入与subtalker loss。源码布局复核不证明实际provider API/hidden_states结构在完整模型上可用。
- epoch_indices确定性打乱、前缀padding补齐两rank等步数，不drop最后样本。原函数AST执行检查world2/3/4、count从world到32：全覆盖、等长、padding次数正确；另验证跨epoch变化、同seed复现与too-few拒绝。这是纯Python采样数学，不是DDP执行。
- optimize_epoch按实际尾部group_size缩放、边界才同步/更新，全rank finite失败策略与GradScaler/clip顺序重新审查。没有Torch，**未重新运行反向、混合精度、nonfinite梯度、Gloo/NCCL或参数一致性**。旧CPU证据仍是历史，不据此给本轮数值验收。
- LoRA A/B存储FP32与实际autocast算子执行精度不是同一命题；没有声称所有matmul以FP32计算、T4无溢出或快于原方案。
- prepare先构造/检查全部替换，commit遇BaseException逆序恢复。新AST测试用普通Python对象/setter注入KeyboardInterrupt验证赋值回滚，不伪装nn.Module、CUDA、真实adapter切换或推理声音保持。
- run_rank先逐条检查tokenized长度后建optimizer，内容pin复核、adapter digest跨rank汇聚、全部更新/一致才保存；checkpoint原子发布与产物加载仍需真实Torch/权重。F01旧provider metadata缺口仍未修，是训练链阻塞因素之一，不把依赖缺失单说成只有GPU问题。

## 4. 新确认 F16：停止直接rank不等于清空整个进程组

位置：`training_job.py:108–122`。原helper先SIGTERM进程组，等待直接leader，再仅在 `process.poll() is None` 时对组SIGKILL；leader退出后，额外忽略SIGTERM的后代会被跳过。

实际CPU/OFD见证步骤（三轮相同）：
1. 在独立临时root取得offline-reservation，创建本测试拥有的新session leader。
2. leader显式派生一个忽略SIGTERM的额外CPU后代，传同一租约FD；通过ready握手确保handler已安装，用pidfd观察。
3. 调原 `stop_ranks`：直接leader确已回收，但后代pidfd未退出。
4. 关闭测试父进程租约引用，实际status仍busy，证实后代仍持OFD。
5. **测试finally只向自己创建的group定向SIGKILL**，确认后代退出、close全部引用、status变非busy。没有留下fixture进程/租约，也没有按旧PID/名字杀外部进程。

状态 `confirmed_with_explicit_cpu_descendant_fixture_not_fixed`。新见证PASS代表缺口仍复现，不代表产品已增加组清理。当前run_rank无DataLoader子进程，PDEATHSIG用于受控直接rank；本次额外后代并不是实际Qwen/第三方组件产生。因此这是停止helper在明确额外后代场景下的不足，**不能声称真实训练曾泄漏显存、用户进程被锁住、父死正常路径已失效或构成公开攻击**。

正常单个直接CPU子进程的停止/回收保护也通过。未来修复须与supervisor已考虑leader死亡后组后代的策略交叉核对，不能破坏最后引用才释放、仅停止本次进程、取消/故障时不发布成功等保证；当前G0下不改冻结helper。

## 5. 三轮执行与证据

```bash
.venv/bin/python docs/validation/step18/run_pass2_training.py --round 1
# --round 2 / --round 3 同目标、独立进程
```

| 轮次 | unittest | fail/error/skip | 新保护/原行为见证 |
|---|---:|---:|---:|
| 1 | 219 PASS | 0/0/0 | 11/1 |
| 2 | 219 PASS | 0/0/0 | 11/1 |
| 3 | 219 PASS | 0/0/0 | 11/1 |

另选现有10个artifact边界，真实NumPy/safetensors解析、本地文件、手工rank报告；**手工报告不是实际NCCL/训练**。新12项预检日志保留，不计额外完整轮。组合包含旧诊断误PASS等观察，不能将219通过解释为旧缺陷消失。原先单独CLI四项矩阵、14个分析AST、12个DSP分块及Chromium/Go race全协议没有以独立矩阵重跑，不改写旧收据。

主要文件均在 `docs/validation/step18/`：
- `pass2-training-roundN.json` / `pass2-training-regression-roundN.txt` / `pass2-training-roundN-console.txt`：逐ID、源/测试/runner/support/hash、依赖、F16和执行边界。
- `pass2-training-preflight.txt`：新12项预检。
- `pass2-training-preserved.json`：382既有历史文件hash。
- `g0-pass2-training-coverage.json` / `g0-pass2-training-findings.json`：8份第二遍及F16，局部依赖阅读不冒充全文。
- `pass2-training-toolchecks.json`及Node/JS/Python AST/repack日志、`pass2-training-environment.txt`。
- `verify_pass2_training.py` / `pass2-training-progress-verification.txt` / `progress-pass2-training.json` / `pass2-training-run-manifest.json`：独立一致性检查；`progress-checks.json`更新当前检查点。

所有产品Python源码AST解析是语法检查，不是Torch导入/执行。实际NumPy2.2.6、safetensors0.6.2，无Torch/Qwen/CUDA/rustc/cargo；没有扩大实际环境成绩至需求文件版本。

## 6. 后续顺序

全源第一遍53/53保持；第二遍现8/53，尚45份；第三遍仍0。下一批沿码/输入/产物/恢复链逐份重新全文读，再到分析/worker/网关/前端/工具/说明的跨层失败传播，不以局部grep或新增测试自动填满第二遍。

原300建议最终处置/失败见证映射尚未签收。只有真正关键设计选择才按既定顺序另开题并给≥50行动建议，不预填Q28、不向用户索要Continue。G0未完成前不跳S1/发布；首可用DeepSeek prefix、更响受保护输出、更快真实首声/建档、generated-only PCM、自然连续、短参考相似度、双卡同等参数与声音、真实长数据训练、无沙沙及RTF≤0.3仍全部保留，当前未取得新的声学/性能证据。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_PASS2_STATE.md

# 第十八阶段 G0：全源第二遍第2批——数据、产物、恢复与认证

日期：2026-10-23。分支：`arena/1160bd87-kagglee`。状态：**限定审计/回归完成，G0仍PARTIAL/BLOCKED；产品未改，缺陷未修，18包未发布。**

## 1. 本批范围与真实覆盖

沿已确定的G0计划继续，不重开问题、不新增问题28，不以测试通过代替源码三遍审查。新增第二遍全文语义阅读7份、1526行，读至各文件末尾；按分段输出核对首尾，无截断。登记脚本只依据该阅读事实、基线hash/行数更新台账，不从测试数量推导阅读覆盖。

| 全文文件（`kaggle/source/py/`） | 行数 | 本次交叉复核重点 |
|---|---:|---|
| `voice_library.py` | 351 | 私有普通文件/no-follow、全局/库租约、revision与原始字节hash、snapshot/begin/finish、元数据原子替换及失败清理 |
| `training_data.py` | 285 | 严格24k mono PCM16 RIFF边界、每样本文本与权利声明、不可变输入快照、manifest/audio/jsonl/rank_plan绑定、staging发布、读租约与删除 |
| `training_codes.py` | 355 | 本地模型树fingerprint/安全JSON、CPU encoder提供包身份、schema2来源封存、逐row/code/audio验证、发布前复验、同OFD继承/adopt与失败关闭 |
| `trained_profiles.py` | 155 | request/result/rank报告交叉核对、真实safetensors NumPy结构与hash、fixture/legacy声码拒绝发布、参考文本绑定、发布前二次pin验证、禁止Base/Mock静默回退 |
| `persist.py` | 99 | profiles/active备份范围、上传与恢复分支、scope预检、候选切换与归档一致性、远端操作证据边界 |
| `qtts_common.py` | 211 | JSON/日志、profile定位、tar路径预检与逐文件替换、输出增益配置边界 |
| `access_control.py` | 70 | 默认认证目录不进入Notebook输出、token格式/权限/本地锁、仅本地同端口HTTP gateway转发 |
| **合计** | **1526** | **7份第二遍全文** |

另局部复查 `analyst.set_candidate` 原函数及既有测试fixture；**不计analyst第二遍全文**。测试文件的局部读取也不计产品源码覆盖。

- 第一遍：53/53内嵌资产，13668行，保持不变；不是整个Git仓库全部文件已审。
- 第二遍：上批8/1056 + 本批7/1526 = **15/53、2582行；剩38份**。
- 第三遍：0/53。
- 当前台账：`docs/validation/step18/g0-pass2-state-coverage.json`；历史台账和已发收据不重写。

## 2. 依赖链、边界与保留合同

1. 原始库保留原始字节与revision；训练输入按明确样本id/独立文本/显式权利确认生成新快照，不把库的建档记录当训练成绩。
2. `canonical_wav`要求完整24kHz、单声道PCM16，至少1.5秒；训练路径每文件/累计上限还受`min(240, limits.seconds)`与`min(900, limits.total_seconds)`约束。可忽略合法非fmt/data chunk并重封装，但PCM不得被截短、重采样或悄悄换声。该严格入口**不是已经支持任意>10分钟单条录音训练**，分段、文本对齐与真实长数据训练仍未验收。
3. 输入manifest pin、JSONL、逐WAV与rank_plan建立一致绑定；rank_plan只是数学分配计划，不是双GPU采样或优化器实际执行轨迹。
4. 声码构建持输入租约，封存来源manifest/原始JSONL、独立复制PCM，逐条验证`ceil(frames/1920) × 16`个0..2047普通整数，完成后复验输入与整个staging，再rename发布。取消/IO失败必须清staging且释放输入租约，原库与输入不应被改写。
5. schema2声码可脱离已删除原库/输入继续校验封存来源；这只证明本地来源/结构绑定。`test_fixture`即使完整封存、能取得读租约，也始终`test_only_codes`，tokenization/training/inference标记仍false；**租约不是训练准入许可**。
6. `adopt_lease`要求继承同一个开放文件描述而非仅同inode；校验失败须关自己的dup，不能关调用方FD，也不能遗留额外OFD阻塞删除。本批实际flock/FD故障回路验证这一点。
7. 训练产物检查会读取真实safetensors容器及NumPy数组、交叉检查rank报告/成员/摘要；本批使用合成权重与手工报告。**JSON里写了NCCL/optimizer已执行，不等于实际跑过NCCL/优化器**。发布还要求真实已准备声码、来源一致、显式未验收确认；无fallback合同必须保持。
8. `_pack`只遍历profiles及active，不自动保存raw libraries/training_data/training_codes/training_runs或默认认证目录，也排除`_cal_`临时profile。因此当前Dataset备份**不是完整训练工程/权重恢复方案**；不能许诺跨Kaggle会话完整恢复训练。profiles内参考/转写本身仍属敏感数据；不能把“排除训练目录”说成备份无隐私内容。
9. tar scope/path/type预检拒绝越界与链接；实际落盘是逐文件临时文件+replace，**不是整个状态目录事务**。第一批已记录第二成员IO失败部分提交；本批未修，不能冒称恢复原子性已验收。
10. 默认auth目录以state路径摘要隔离、位于临时目录；重复provision保留同一token、目录0700/文件0600。只向精确本地gateway端口HTTP附加token，不传给不同端口worker、外部host或userinfo伪装host。测试只用临时生成token/固定合成token，不向远端发请求、不输出token值。

F01（旧`qwen-tts`元数据查询与HF提供包不符）和F16（额外后代持OFD退出清理）仍未修。此次完整复读不改变其既有证据边界。特别是未重新运行已缺失upstream cache依赖的独立真实wheel-provider六案例，不用当前fixture替代该历史证据。

## 3. 新实证 F17：备份与候选切换交错，恢复后引用缺失锚点

**确认未修；不是猜测、不是修复后的绿色测试。**

源位置：`persist.py:27–36`、`analyst.py:1067–1082`，以及`qtts_common.extract_tar_safely`的逐文件恢复。`_pack`递归`tarfile.add`没有与profile候选切换共享一致性屏障/不可变版本快照。

确定性步骤（每轮均重建独立临时状态）：

1. 准备合成PCM WAV候选0/1，当前profile指向`anchor_0.wav`，尚无`anchor_1.wav`。
2. 原`_pack`递归归档profile，tarfile已经枚举该目录的现有文件名。
3. 在已打入`anchor_0.wav`、尚未读取后面的`profile.json`时，由serializer hook运行**原`set_candidate`函数体**，切换index=1：真实`shutil.copy`生成新锚点，真实原子JSON替换更新anchor/ref_text。只有admission/worker reload是明确fixture；不执行模型。
4. live profile及其新锚点完整存在，且锚点字节等于候选1。
5. tar按先前枚举的文件名继续打包，读到新的`profile.json`，却不会追加刚创建的`anchor_1.wav`。
6. 用原`extract_state_members`和`extract_tar_safely`实际解包不抛异常；恢复的profile指向`anchor_1.wav`，文件不存在。

这证明本地并发可达的备份一致性缺口；并未调用远端Kaggle snapshot/restore、未跑完整HTTP竞争/线程压力、未证明用户现有Dataset损坏、未运行Worker模型加载，也不把它当用户沙沙/低响度根因。测试不是修改产品来制造失败，只在原函数间控制交错时机。

三轮观察收据均包含F17的live-anchor-present与restored-anchor-missing真值；旧F16亦保留在本轮观察收据中。新增finding只登记F17，不重编号、覆盖历史问题或300条原始建议。

后续修复方向（**尚未实施/未作新设计签收**）：需在G0完成后比较与候选变更共享profile级锁、从不可变版本打包、以及发布前自校验/重试；恢复要验证profile引用/版本，并明确整体事务与失败回滚政策。不能仅补齐这次漏掉的文件名或忽略缺失锚点。

## 4. 新增12项边界：11保护 + 1原缺陷观察

文件：`kaggle/tests/test_pass2_state_boundaries.py`。

| # | 检查 | 结果含义 |
|---:|---|---|
| 1 | 封存第二文件写失败，清staging、释放输入租约、原库/输入不变且可重试 | 保护 |
| 2 | 最终发布rename失败，回滚staging且可再次构建 | 保护 |
| 3 | encoder返回后立即取消，只执行一条fixture编码且不发布 | 保护 |
| 4 | adopt校验期间封存来源损坏，失败关dup而不关parent FD，parent释放后可删除 | 真实FD/flock保护 |
| 5 | 原库和输入删除后，封存来源仍可验证；所有fixture执行/训练标记仍false | 保护，不是训练 |
| 6 | 38400/38401帧按20/21码帧、0/2047边界，拒bool/浮点/字符串/越界及少帧 | 结构保护，不是编码精度 |
| 7 | 合法odd-sized JUNK chunk重封装，全部36000个PCM样本逐字节不变 | 合成WAV保护 |
| 8 | pack只收profiles/active，排除校准临时目录、raw库/数据/训练/认证目录，不运行远端命令 | 备份范围保护 |
| 9 | 目标已有指向恢复根外的symlink，完整预检后拒绝，前面合法成员也不写入 | 安全预检保护，不是IO故障整体回滚 |
| 10 | 默认auth按state隔离、位于state外、稳定token与0700/0600权限 | 本地临时认证保护 |
| 11 | 仅local gateway同端口HTTP附header，异端口/外部host/https/userinfo伪装不附 | 转发保护，无网络请求 |
| 12 | 打包与原候选切换确定性交错后，解包profile引用缺失锚点 | **F17观察通过=确认缺陷，不是已修** |

预检首次1项error来自**测试提取器保留了HTTP注册装饰器**导致`app`未定义；11项已过。修正测试提取为只去装饰器、原函数体不变后12/12通过。保留`pass2-state-preflight-attempt1.txt`失败原日志及最终`pass2-state-preflight.txt`；未修改产品以绕过预检，不隐去失败。

## 5. 三独立轮专项回归

runner：`docs/validation/step18/run_pass2_state.py --round N`，N=1、2、3；独立Python进程，依次执行，临时状态隔离。

组成：上批219项 + 本批另选既有`test_training_data`19、`test_training_codes`33、`test_code_provenance`21、`test_qwen_compat`20（共93）+ 新12 = **324项/轮**。按逐测试ID去重、保留顺序与hash。

| 轮次 | tests | failures | errors | skipped | 结果 |
|---|---:|---:|---:|---:|---|
| 1 | 324 | 0 | 0 | 0 | PASS |
| 2 | 324 | 0 | 0 | 0 | PASS |
| 3 | 324 | 0 | 0 | 0 | PASS |
| **合计** | **972** | **0** | **0** | **0** | **专项通过，非产品验收** |

覆盖包含原始库、合成PCM/JSONL、来源封存、CPU真实子进程/取消/租约、显式HTTP/模型替身、实际本地HTTP、真实NumPy/safetensors解析，以及本批实际tar/文件操作。套件中已有故障注入会打印预期异常；正式结果以逐ID收据为准，不把console出现的fixture traceback当未捕获套件错误。

保存每轮`pass2-state-roundN.json`、`pass2-state-regression-roundN.txt`、`pass2-state-console-roundN.txt`，含53源、测试/runner/support hash、依赖版本、逐ID结果、观察和真实性标记。

**不包含**实际Torch算子/optimizer/GradScaler/Gloo/NCCL、真实Qwen声码、权重训练、GPU/双T4、用户WAV/相似度/去沙沙/自然连续朗读/物理声卡、DeepSeek真实prefix首声或提速测量。NumPy2.2.6不等于生产requirements2.4.6；Rust缺工具链，未编译或执行。此次未重跑独立旧CLI四矩阵、Go race/完整Go协议、Chromium全量、14分析AST/12 DSP独立矩阵或缺缓存的provider六案例，不挪用历史数字充本轮成绩。

## 6. 工具、冻结、证据与交接

- 本批`npm test`：Node30/30；`npm run check`：PASS。
- Python AST：全部产品Python及本批test/runner/advance/verifier/refresh共38份：PASS。
- `kaggle/repack.py --check`：PASS，确定性包内容一致。
- 新校验器：`docs/validation/step18/verify_pass2_state.py`，检查当前覆盖、324×3逐ID/观察/hash、原300建议与Q25–27各50、冻结与完整交接内嵌；不重签旧检查点。
- 原53源、94冻结hash、正式15文件和正式revision保持，历史handoff保持；本批开始408份历史证据hash保留；上批382清单及其后产物仍在。
- 新run manifest冻结本批输入/报告/收据/日志/校验器/交接hash；进度输出为`progress-pass2-state.json`和当前`progress-checks.json`，自引用输出不纳入自身manifest。
- 新完整报告加入交接，累计**73份备忘录全文**。`handoff-progress.json`记录实际字节数与SHA256；嵌入原文逐份核对，不在本报告预填循环依赖hash。
- `git diff --check`须通过；不提交或推送也能保存当前分支工作。

## 7. 下一步与未签收门禁

继续剩38份第二遍，优先模型provider/voice binding/worker/分析API间的版本、失败、取消与参考贡献链；补齐全53份第三遍、300条建议的最终处置/失败见证映射，再按既定S1–S8顺序实施。当前已确认F01–F17及旧边界/专题问题按各自证据保留，不能因专项绿色而消除阻塞。

不改冻结17/正式工作台/空白文件与浏览器复制行为，不发布18包，不默认融合prompt列表、添加参考PCM、切向量策略或强滤波；不提前打开Q28，不要求用户点击Continue。>15秒/极长录音、<10秒相似度、>10分钟真实训练、双GPU等效参数、generated-only播放、DeepSeek首可用prefix即生成、更响受保护输出、更低创建/首声延迟、安全/取消/隐私/冻结版本等要求均未撤销，仍需分层实证。整体保持**PARTIAL/BLOCKED**。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_PASS2_INFERENCE.md

# 第十八阶段 G0：全源第二遍第3批——provider、参考绑定与推理生命周期

日期：2026-10-23。分支：`arena/1160bd87-kagglee`。

**本批限定审计完成；产品未改、缺陷未修、G0仍PARTIAL/BLOCKED，无18发布包。** 专项通过不是完整功能、真实模型、训练或声学验收。

## 1. 全文阅读和进度

| 文件（`kaggle/source/py/`） | 全文行数 | 第二遍复核重点 |
|---|---:|---|
| `qwen_compat.py` | 97 | HF/旧发行包命名空间、现代/旧RoPE配置、registry身份与幂等、失败分类和smoke边界 |
| `voice_binding.py` | 60 | 跨语言domain与长度前缀、生成参数规范化、参考文件类型/预算/no-follow、绑定的能力边界 |
| `worker.py` | 680 | GPU准入、模型/提示缓存、版本检查与锁、取消/错误/终态、generated-only播放、统计和ASGI生命周期 |
| `clone_stream.py` | 126 | 条件模式、生成码与参考码隔离、有限左上下文/右lookahead、提交位置、finish与生成器清理 |
| `adapter_engine.py` | 108 | Base/adapter绑定、磁盘profile重读、适配器选择提交、真实句缓冲语义、取消与PCM验证 |
| **新增合计** | **1071** | **5份重新全文语义阅读** |

worker按1–170、171–340、341–510、511–680逐段完整复读；其余四份完整输出。上述源输出无截断。测试/调用点的局部查看不计其他产品文件第二遍；分析API全文留在下一批，不以测试经过API路径代替全文覆盖。

- 第一遍：53/53内嵌资产、13668行，保持；不是整个Git仓库所有文件已审。
- 第二遍：上批15/2582 + 本批5/1071 = **20/53、3653行，剩33份**。
- 第三遍：0/53。
- 当前覆盖：`docs/validation/step18/g0-pass2-inference-coverage.json`。既往台账/报告/收据保持历史意义，不重签。

## 2. 语义链与必须保持的合同

### 2.1 provider / RoPE / 实际运行边界

桥先根据发行包元数据选择HF路径，拒旧`qwen-tts`与`qwen-tts-hf`同命名空间并存，以及已加载兼容模块却无HF元数据的状态。对现代default配置，从实际`rope_parameters`取theta/partial factor，复制config后委托已识别的原initializer，不猜默认theta、不修改权重、不全局覆盖其他registry项；未知schema、非法范围、registry漂移必须拒绝。

桥强制比较HF/Transformers组合；Faster版本虽收集进versions，桥本身未逐项对照其PINS。**此处仅记录源码观察，尚需完整启动/安装/preflight政策链反证，不升级为已证生产故障。** 新registry保护使用明确上游函数fixture，不是实际Transformers/Mimi数值运算；旧真正wheel/config实验保留历史证据，当前未重跑。

`RealEngine.load`要求单可见CUDA设备和允许的dtype；T4不能把软件BF16支持当原生能力，FP32只可显式准入。warmup/sanity是运行门禁，不是声纹、逐字正确或质量验收。新测试不执行这些模型步骤，不把`model_loaded`字段或mock health当GPU证明。

### 2.2 绑定、缓存与加载

reference pin由domain、参考原始字节、参考文本、语言与四个规范化生成参数组成；显示名称、quality和未选候选不纳入这个内容pin。它**不是认证、候选贡献评分，也不单独绑定trained adapter权重**。训练后端另有binding/manifest/Base交叉检查，不能拿普通参考pin代替适配器绑定。

文件打开含no-follow/nonblock，先fstat确认普通文件与1..64MiB，再有界读取。空/超预算/FIFO拒绝；本批FIFO在真实短子进程中验证，超时会由subprocess.run定向清理，不依赖“当前没卡住”的猜测。

Worker持同一锁读取磁盘profile、验证session模式/内容pin、提取prompt后二次检查，再提交worker profile/binding；不得在锁外先抓旧快照，不得先发静音或参考PCM掩盖错误。新测试验证初次提取期间参考变化会拒绝且不登记worker绑定，**不宣称engine内部prompt已事务回滚**：F08仍未修。

### 2.3 生成、generated-only与指标

Faster路径把参考码仅用于talker conditioning，GeneratedCodecWindow只接生成码；16组、24kHz、1920样本/帧、25帧左上下文与默认0右lookahead合同不变。窗口保留/提交/finish需要真Torch与实际codec进一步证明；本批全文复核不等于执行了Torch张量或预训练codec。

RealEngine迭代器在消费方close或采样率错误时应调用下游close；新检查使用有限PCM重放迭代器及仅`manual_seed`的显式模块fixture，不安装Torch、不模拟Tensor/算子，不测生成性能。实际目标text与参考text分离、参考PCM不拼接的既有保护继续回归。

Worker只产生规划静音，不插入参考呼吸；trimmer/leveler旧短块/短尾问题保留。`model_first_chunk_ms`是引擎首数组到达，`first_chunk_ms`是DSP后首PCM，不是浏览器或声卡首声。speech_samples、flush、规划暂停与端到端首声不得混算；EMA、rtf_target字段不证明RTF≤0.3。

排队取消验证只覆盖未读取profile、未启动引擎、未释放他人持锁以及唯一stats/None收尾。**锁等待/刚取得锁时的提前返回目前缺少cancelled标志**，不以这项所有权保护签收取消终态语义；列为后续矩阵观察。

### 2.4 训练后端

AdapterEngine每次选择重读受预算/no-follow保护的磁盘profile，比较trained binding，检查Base/adapter/codes pin与speaker维度，准备并提交adapter。不得静默回退到Base/Mock。新测试执行真实文件访问与原`_profile_now`，拒重绑定、删除、symlink和超预算，失败不改变key/prompt；没有执行模型加载、adapter张量提交或真实推理。

该后端明确**整句缓冲**：官方generate返回完整单条波形后才yield，取消只能通过StoppingCriteria/返回后检查配合，不能抢占CUDA kernel或codec。不能把它的一个yield切成假块就宣称原生声学流式、真实首声提速或双GPU一致。

## 3. 新实证 F18：正文开始前断连，没有传递取消到已启动生产线程

**确认未修。** 源位置`worker.py:650–674`：`synth`在返回StreamingResponse前启动生产线程；cancel只在内部async generator的finally中设置。若正文生成器尚未第一次进入，关闭这个未启动的生成器不会执行其finally。

两条真实Starlette响应控制流，各独立三轮：

1. **ASGI 2.4**（纳入每轮336项）：真实原`synth`启动明确CPU生产线程；真实StreamingResponse发送`http.response.start`时，send fixture抛断连OSError。原响应抛ClientDisconnect，正文未开始。再显式aclose body iterator，生产cancel仍未设置，线程仍等待。
2. **ASGI 2.3**（独立companion probe）：真实响应在发送响应头的await期间暂停；receive fixture随即返回`http.disconnect`。真实响应task group退出/取消header发送任务，正文仍未开始；生产cancel仍未设置，线程仍等待。

所有实验finally只设置自己创建的cancel并join自己创建的生产线程，验证其退出；没有留下后台等待线程。使用实际安装的Starlette1.9.0，收据包含版本和responses模块hash。ASGI send/receive时机与生产工作负载明确fixture；**没有实际TCP/浏览器断连、模型生成、显存增长或Kaggle线上故障证据**。不把它认作用户噪声根因，也不保证所有服务器版本都走相同分支。

它补足旧测试“已取到首PCM再aclose”的盲区：旧测试仍通过，但不能覆盖首次迭代前断连。与F07无界队列不同，本项证据是**取消所有权缺失**，不以有限CPU实验声称测出了无限内存或GPU泄漏。

F18登记在`g0-pass2-inference-findings.json`；F01–F17与其他历史边界/专题发现保留，不被绿色观察测试消除。后续方向需比较响应全生命周期清理、生产者启动时机、取消令牌和有界队列的联合所有权；**尚未实现或作新设计定案**，不能只补测试里的断连分支。

## 4. 新12项边界：11保护 + 1原缺陷观察

文件：`kaggle/tests/test_pass2_inference_boundaries.py`。预检12/12通过，无失败/错误/跳过。

| # | 检查 | 证据边界 |
|---:|---|---|
| 1 | generation默认值等价、合法int/float规范化、无关元数据排除及非法边界拒绝 | 原Python pin/编码函数 |
| 2 | 空参考与64MiB+1稀疏文件拒绝 | 真实fstat/文件，不分配大数组 |
| 3 | FIFO无writer仍能及时拒绝 | 真实CPU子进程/系统FIFO，有超时清理 |
| 4 | 排队取消不读profile/调用engine，不释放他人持锁，仅一次stats/None | 真实锁/线程；不验收cancelled标志 |
| 5 | 初次提取中参考改变，拒绝并不登记worker profile/pin | 原Worker + 文件；提取回调fixture，不代表F08修复 |
| 6 | RealEngine采样率错误仍关闭重放迭代器一次 | 原stream + 明确manual_seed/PCM重放fixture |
| 7 | 消费方关闭时下游close一次、seed掩码保持 | 同上；不执行真实codec |
| 8 | 无prompt时不创建生成迭代器 | 同上；无模型 |
| 9 | RoPE桥不改其他registry/原config，原异常和参数传递保持 | 原桥 + 明确initializer fixture |
| 10 | trained磁盘binding变化/删除拒绝，恢复原文件后可读 | 原AdapterEngine._profile_now + 文件 |
| 11 | trained profile symlink/超预算拒绝，key/prompt未变 | 同上；无adapter加载 |
| 12 | ASGI2.4响应头阶段断连后取消未传给生产线程 | **F18观察通过=确认缺陷，非修复** |

ASGI2.3补充脚本：`docs/validation/step18/probe_pass2_inference_asgi23.py --round N`，不塞进336项、也不冒充另一轮完整回归。

## 5. 三独立轮与真实性

runner：`docs/validation/step18/run_pass2_inference.py --round N`，独立Python进程、独立临时状态，完整专项轮依次执行。组成：上批324 + 新12 = **336项/轮**，逐ID去重、原324顺序保持。

| 轮次 | tests | failures | errors | skipped | 结果 |
|---|---:|---:|---:|---:|---|
| 1 | 336 | 0 | 0 | 0 | PASS |
| 2 | 336 | 0 | 0 | 0 | PASS |
| 3 | 336 | 0 | 0 | 0 | PASS |
| **合计** | **1008** | **0** | **0** | **0** | **限定专项，不是全功能验收** |

另ASGI2.3 companion独立三轮，各1项观察通过；不计入1008。每轮正式收据保留逐ID、53源/测试/runner/support hash、依赖版本、F16/F17/F18观察真值和真实性标记。历史F16额外后代最后定向清理/锁释放、本批F18生产线程退出均实际检查。console里的故障注入异常不是未捕获套件错误，结果以逐ID收据为准。

既有真实本地HTTP/文件/flock/子进程、NumPy与合成safetensors测试本轮重跑；新ASGI断连是进程内事件，不冒充socket断连。没有真实Torch算子、optimizer、GradScaler、DDP/Gloo/NCCL、Qwen/Faster模型/编码、训练、双T4、Rust编译/执行、用户音频、声纹/沙沙/自然连续听感、DeepSeek真实prefix或物理声卡/性能测量。

## 6. 环境、工具与冻结

本轮开始发现`.venv`及其CPU依赖未保留。首次探测命令出现`.venv/bin/python: No such file or directory`，**不是测试失败或产品缺陷**；随后重建隔离venv，固定NumPy2.2.6、safetensors0.6.2、FastAPI0.156.4、Starlette1.9.0、httpx0.28.1、requests2.34.2、soundfile0.14.0、uvicorn0.34.0、python-multipart0.0.20。安装日志与完整pip freeze保留；未承诺全部传递依赖与旧环境完全相同，以当前environment/freeze为准。没有安装Torch/Qwen、Rust或Go；NumPy版本仍不等于生产requirements的2.4.6。

- Node30项、JS check、产品Python与本批test/runner/advance/verifier/probe/refresh共39份AST、repack一致性：检查日志单列。
- 本批开始435份历史证据hash保留，53源/94冻结/15正式文件及正式revision不变，旧handoff保持。没有18包。
- 新校验器`verify_pass2_inference.py`核对当前20/53覆盖、336×3逐ID/观察/hash、ASGI2.3 companion三轮、旧300建议/Q25–27各50、冻结和完整内嵌交接。
- 当前`progress-pass2-inference.json`与`progress-checks.json`保存结果；新manifest覆盖本批输入/日志/收据/报告/校验器/交接，排除自引用进度输出。
- 交接新增此完整报告，累计**74份备忘录全文**，实际字节/SHA在`handoff-progress.json`，逐份内嵌原文核对，不在报告预填自引用hash。
- `git diff --check`作为最终检查；本轮未重跑独立旧CLI四矩阵、完整Go/race/协议、Chromium全量、14分析AST/12DSP或需要缺失upstream cache的真实provider六案例，不挪用历史数字。

## 7. 下一步与未签收门禁

下一批复读分析/API及参考切分，核对provider版本政策与启动/worker/会话间失败、取消、参考贡献和校准版本链；继续剩33份第二遍、全53份第三遍和300条建议最终处置/失败见证映射，再按既定G0→S1–S8实施。新发现不等于已有纠正，当前不绕过G0修产品、不新增问题28、不要求Continue。

保持冻结17、正式工作台空白文件/用户粘贴/完整浏览器复制；不盲目prompt列表融合、改向量策略、强滤波或拼入参考PCM。>15秒/极长录音、<10秒相似度、>10分钟真实训练、双GPU等效参数、generated-only、DeepSeek首可用prefix即生成、更响受保护输出、更低创建与实际首声延迟、安全/取消/隐私/版本冻结等要求均未撤销，仍须真实分层证据。整体**PARTIAL/BLOCKED**。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_PASS2_ANALYSIS.md

# 第十八阶段 G0：全源第二遍第4批——分析/API、参考切分与校准所有权

日期：2026-10-23；分支：`arena/1160bd87-kagglee`。

**本批限定审计完成，产品未改、缺陷未修；G0仍PARTIAL/BLOCKED，无18包。** 三轮专项通过不等于全功能、真实训练/模型/双GPU或声学验收。

## 1. 本批全文与累计覆盖

| 文件（`kaggle/source/py/`） | 全文行数 | 第二遍语义重点 |
|---|---:|---|
| `analyst.py` | 1211 | decode/清洗/ASR/候选/质检/建档/校准/重载/一致性/HTTP；版本和失败记录、临时资源与准入所有权 |
| `library_api.py` | 163 | 严格JSON/上传校验、共享admission、库租约与线程handoff、最终结果提交和错误脱敏 |
| `reference_segments.py` | 106 | 可信词级分区、实际PCM窗口重识别、时间戳偏移、低能量边界、短尾与可选词信息 |
| **合计** | **1480** | **新增3份重新全文语义阅读** |

analyst逐段1–200、201–400、401–600、601–800、801–1000、1001–1211完整复读，另两份完整输出，各源输出无截断。测试和resource_limits局部调用点复查不新增源码全文信用；不把经过函数的测试计作第三遍阅读。

- 第一遍：53/53内嵌资产、13668行，保持；不是整个Git仓库所有文件已审。
- 第二遍：上批20/3653 + 本批3/1480 = **23/53、5133行，剩30份**。
- 第三遍：0/53。
- 当前台账：`docs/validation/step18/g0-pass2-analysis-coverage.json`，旧台账/收据作为历史保留。

## 2. 原始参考实际贡献：统计、候选、conditioning不可混为一谈

复读确认的现有路径，不是新增融合算法或最终需求签收：

| 阶段 | 实际使用/记录 | 不能声称 |
|---|---|---|
| 输入/清洗 | 按文件解码、有限时长/总量/有限数值检查，记录原始RMS/peak、估计SNR、清洗决策与低输入警告 | 截图能定噪声根因；归一化等于去噪 |
| ASR/对齐 | 单文件不超anchor limit的手工文本可直配；长手工文本不强行配给短候选，依时间戳/实际窗口ASR | ASR文字是人工真值；长录音全部作为模型prompt |
| 候选评分 | 从可信片段组合窗口，预排后最多24个候选做embedding/评分，再选最多3个非近重复候选落盘 | 每个可能窗口都已评估；每个输入在最终prompt中的贡献都有独立可追溯权重 |
| centroid | 分析说话人空间中候选embedding均值用于典型性/质量评价，存centroid.npy | 这是Qwen条件嵌入融合，或ECAPA/MFCC可直接代替Qwen向量 |
| conditioning | 实际选定一个anchor与匹配ref_text供Worker加载；其余候选可切换/校准 | prompt列表自动融合三参考；统计参与等于模型conditioning参与 |
| 韵律/呼吸 | 全部可用clips/words参与部分韵律统计并保存候选呼吸文件；Worker参考呼吸播放仍禁用 | 可以拼入参考PCM来改善相似度或提前首声 |
| 校准 | 遍历已保存候选，在worker0用固定目标文本/seed合成后评分，最后重载 | 已测全部输入/全部窗口；双卡声学等效；质量/RTF已达标 |

`quality.reference_context`明确`all_audio_used_as_model_prompt=False`、`model_trained=False`，必须保留。默认16秒/24秒实验入口不变。上传配置允许长录音与训练数据入口每文件240秒的上限不是同一合同；本批17秒合成建档和既有20分钟时间戳规划测试**不是>10分钟真实音频转写、实际训练或全数据覆盖验收**。

`estimate_snr`仍是帧能量分位差，不是真值SNR；SpeakerModel可降级MFCC代理，ASR可降级CPU small，必须保留实际方法/能力披露，不把代理分数当声纹认证。`fidelity_index`是内部加权指标而非相似度百分比。ASR失败默认CER0.05、校准旧版本覆盖/失败重载/全合成失败选择、consistency按GPU使用不同seed等既有专题问题仍保留，未修、未重编号为新发现。

## 3. 新实证 F19：同一档案并发校准争用临时目录，并覆盖成功记录

源：`analyst.py:886–936、1085–1096`。**确认未修。**

校准临时id为`_cal_{pid}_{candidate_index}`，没有每调用独立标识或同档案互斥；共享HEAVY默认可接受两个操作。测试用两个真实进程内ASGI POST `/profiles/voice/calibrate`、原HEAVY(2)、原calibrate_profile、实际文件复制/JSON/rmtree，以及原Mock Worker.load_profile控制流，安排如下交错：

1. A创建`_cal_voice_0`，真实Mock Worker完成加载，A停在明确的合成替身回调。
2. B也为同一档案创建/写入`_cal_voice_0`，进入重载回调等待A完成。
3. A继续完成合成替身评分，在原finally中删除共享临时目录，提交成功的校准记录并返回。
4. B随后通过原Worker.load_profile读取该临时档案，真实文件已经不存在，返回找不到档案的错误；B得到score=-9的候选错误结果。
5. B把自己的错误校准记录覆盖A的成功记录。两个ASGI请求都返回HTTP200；最终记录是后来的失败结果。

每轮核对A的成功分数、B的缺失档案错误、仅A进入合成替身、最终记录等于B结果、临时目录清空和两个HEAVY槽位均释放。A/B按事件建立确定性交错，非概率压力测试；HTTP是ASGITransport进程内调用，worker transport、合成、ASR、说话人模型明确fixtures，仅一个Mock Worker角色，不是真双卡/真实网络/模型/音色实验。fixture分数不作为成绩。

F19不是“任意陌生用户可攻击”证明；它确认已准入的同档案校准操作缺少隔离与结果版本归属。全失败候选仍返回chosen等现象已有历史专题证据，这次新增裁决的核心是**两个原校准请求共享临时资源并相互清理/覆盖结果**，不是重复报旧问题。

## 4. 新实证 F20：档案在重载期间删除，最终仍报告成功/已保存

源：`analyst.py:388–412`。**确认未修。**

`load_on_workers`先取profile和expected pin，再收各worker回执；最终仅在`current`存在且pin变化时拒绝。如果目录在重载回调期间删除，`load_profile`返回None，最终复核条件被跳过，旧的成功回执原样返回；原reload_response据此生成HTTP200、`ok=True`、`reference_saved=True`。

测试真实创建/删除临时档案、执行原helper与JSONResponse；worker成功回执明确fixture，没有合成。每轮验证目录实际不存在、回执仍全部ok、响应仍200/已保存。

**没有验证删除后可继续播放旧声，也不是激活或认证绕过证明。** 非Mock Worker后续合成仍有缺失profile拒绝门禁；本项是重载最终状态与事实不符，不能拿此成功回执作为已删除档案可用/已保存的签收。

F19/F20分别单列新finding，原F01–F18及原始300建议/历史专题不覆盖。后续方向需比较同档案操作串行化、不可变版本/CAS提交、临时资源单调用所有权，以及重载终检把不存在视为失效；**尚未实施或作新的设计定案**。不能只换临时目录名而忽略最终结果归属、取消、删除与版本事务。

## 5. 新增12项：10保护 + 2原缺陷观察

文件：`kaggle/tests/test_pass2_analysis_boundaries.py`。预检12/12通过，失败/错误/跳过0。

| # | 检查 | 真实性/限制 |
|---:|---|---|
| 1 | 重载拒503、非布尔ok、错误pin、错误回执形状 | 原load helper；worker回执fixture |
| 2 | 重载终检参考文本版本变化，所有回执改为失败 | 原helper、实际JSON/内容pin |
| 3 | training-data嵌套重复JSON字段在准备前拒绝 | 真实FastAPI/TestClient；不执行训练 |
| 4 | 库处理非法Unicode/非bool校准标记/16.0上下文在租约前拒绝 | 真实路由与校验；begin未调用 |
| 5 | CPU ASR惰性迭代错误向上抛出，不默默变成功或重试模型 | 原ASR控制流，明确metadata iterator fixture，无Whisper |
| 6 | 超16384字节embedding结果不进入构建缓存，不虚报hit | 原缓存、NumPy与speaker fixture |
| 7 | 低能量边界切到15.3秒，实际PCM两窗口无重叠/遗漏、语言与时间戳正确 | 合成20秒PCM，ASR回调fixture |
| 8 | 进度回调异常在窗口ASR前传播，源段/PCM保持不变 | 原prepare_segments；不等于有公开建档取消API |
| 9 | 17秒长手工文本不覆盖短候选ASR文本，保留来源策略与非训练标记 | 原build函数/真实WAV/JSON；模型/信号分析明确fixtures |
| 10 | 后台build声称done却给不安全profile id时不得提交库成功；原始样本保留、租约可再编辑 | 真实库/路由/BuildAdmission；build callback fixture |
| 11 | 两个同档案ASGI校准共享临时目录，成功结果被错误结果覆盖 | **F19观察通过=确认缺陷，非修复** |
| 12 | 重载期间真实删除档案，仍得到200/已保存 | **F20观察通过=确认缺陷，非修复** |

library_api的begin+线程handoff同executor准入、后台结果有效profile检查、store.finish异常脱敏/租约清理仍需保持。HeavyAdmission用shield使HTTP等待取消不等于底层计算已取消；本批未把等待结束当ASR/合成停止，也未改其资源政策。既有F11窗口可选words清洗不一致、F12失败/残缺流被接受，三轮原测试仍复现未修。

## 6. 三独立轮专项回归

runner：`docs/validation/step18/run_pass2_analysis.py --round N`，N=1–3。组成：上批336 + 新12 = **348项/轮**；独立Python进程与临时状态，逐轮执行，按测试ID核对无重复且原336顺序保持。

| 轮次 | tests | failures | errors | skipped | 结果 |
|---|---:|---:|---:|---:|---|
| 1 | 348 | 0 | 0 | 0 | PASS |
| 2 | 348 | 0 | 0 | 0 | PASS |
| 3 | 348 | 0 | 0 | 0 | PASS |
| **合计** | **1044** | **0** | **0** | **0** | **专项通过，不是全功能验收** |

每轮`pass2-analysis-roundN.json`及regression/console日志保存逐ID、53源/测试/runner/support hash、依赖版本、F16–F20观察和真实性字段。沿用测试中的F16额外后代退出/锁释放、F18自有生产线程退出，以及本批F19准入槽/临时资源清理均有断言；不是保存PID后向无关进程发信号。

继承实际本地HTTP、CPU子进程/锁、NumPy/safetensors、WAV/文件/归档测试；F19新HTTP请求为进程内ASGI而非TCP。没有Torch真实算子、optimizer/GradScaler/DDP/Gloo/NCCL、真实Qwen/Whisper/ECAPA/Faster/codec、训练或双T4、Rust编译/执行、用户WAV、声纹/沙沙/自然连续听感、DeepSeek真实prefix、物理声卡或提速成绩。

本轮未重跑独立ASGI2.3 companion（348中保留的是F18 ASGI2.4）；也未重跑独立旧CLI四矩阵、完整Go/race/协议、Chromium全量、14分析AST/12DSP及缺缓存的真实provider六案例。不挪用历史数字充本轮成绩。

## 7. 工具、冻结、环境与完整交接

- 本轮venv存在，未重新安装依赖；保存当前environment与pip freeze，核对freeze等于上批快照。不把版本列表一致泛化为全部运行环境/二进制绝对相同。NumPy仍2.2.6，与生产requirements2.4.6不同；无Torch/Qwen/Rust/Go运行证据。
- Node30项、JS检查、全部产品Python加本批test/runner/advance/verifier/refresh共38份AST、repack一致性均检查并单列日志；最终`git diff --check`。
- 本批开始470份历史证据hash保留；53源/94冻结hash/15正式文件、正式revision和历史handoff不变。无产品改动/18包。
- 当前校验器`verify_pass2_analysis.py`核对23/53覆盖、348×3逐ID/hash/旧观察/两新finding、300原建议/Q25–27各50、冻结与完整内嵌交接，不重签旧检查点。
- 当前结果`progress-pass2-analysis.json`、`progress-checks.json`；本批manifest封存输入/报告/日志/收据/校验器/交接，排除自引用进度输出。
- 新报告加入交接，累计**75份备忘录全文**；实际字节/SHA在`handoff-progress.json`，逐份原文核对，不预填循环hash。

## 8. 下一步与未签收要求

继续剩30份第二遍，下一批优先完整启动/监督和backend preflight，核对provider版本、健康、启动失败/取消与进程所有权；随后其余前端、Go、DSP/工具/说明。再补齐全53份第三遍、300条建议最终处置/失败见证映射，按G0→S1–S8顺序实施，不以本批绿色越过G0。

冻结17、正式工作台空白文件/用户粘贴/完整浏览器复制保持；不默认融合prompt列表、改向量策略、强滤波或拼入参考PCM。>15秒/极长录音、<10秒相似度、>10分钟真实训练、双GPU等效参数、generated-only、首个可用DeepSeek prefix即生成、更响受保护输出、更低创建/实际首声延迟、安全/取消/隐私/版本冻结等要求均未撤销，仍待真实分层验证。不新增问题28，不要求Continue。整体**PARTIAL/BLOCKED**。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_PASS2_STARTUP.md

# 第十八阶段 G0：全源第二遍第5批——启动、监督与 backend preflight

日期：2026-10-23；活动分支：`arena/1160bd87-kagglee`。

**本批限定审计完成，产品代码仍冻结，新增两项缺陷确认未修；G0仍为PARTIAL/BLOCKED。** 三轮专项通过不是全功能、真实模型/训练、双GPU、声学或性能签收，无18发布包。

## 1. 全文阅读和真实进度

| 文件（`kaggle/source/`） | 行数 | 第二遍语义重点 |
|---|---:|---|
| `py/bootstrap.py` | 451 | 所有权准入、版本安装、runtime probe先后顺序、命令超时/后代、下载与编译、监督启动与失败取消、访问控制/隧道 |
| `py/supervisor.py` | 219 | GPU lease/FD、进程组、日志句柄、重试预算、健康/致命回执、停机、快照与标记所有权 |
| `tools/backend_probe.py` | 200 | 静态与runtime surface区分、CUDA/API检查、隔离子进程/超时、报告预算/结构、原子写入与退出码 |
| **合计** | **870** | **新增3份完整第二遍语义阅读** |

bootstrap按1–155/156–310/311–451，supervisor按1–115/116–219，probe按1–105/106–200输出并全文复读，所有这些源文件输出无截断。之后相关函数、旧测试与provider控制流的局部核对不另增全文信用。

- 第一遍保持：53/53内嵌资产、13668行；并非整个Git仓库全部文件。
- 第二遍：23/5133 + 3/870 = **26/53、6003行，剩27份**。
- 第三遍：**0/53**，不能把测试执行或局部复查计作第三遍。
- 当前台账：`docs/validation/step18/g0-pass2-startup-coverage.json`；前四批台账/日志保持历史原样。

## 2. 版本准入裁决：已验证的控制流与仍未签收的范围

标准 `QTTS_TTS_ENGINE=faster` 启动链：

1. 所有权检查在依赖安装与GPU启动前进行；默认必须看见两张GPU，显式单卡测试不等于双卡验收。
2. 拒绝旧 `qwen-tts` 与HF同命名空间冲突。
3. 对 `PINS` **每一项**检查metadata：Faster `0.5.4`、HF `0.1.1.post1`、Transformers `5.20.2`。已有任一漂移时调用精确pin安装，不是只检查模块能否import。
4. `install_reviewed_faster` 要求平台Torch已存在，以临时constraints约束Torch及已存在的torchaudio/torchvision；传给pip时文件权限0600，退出后删除；安装后Torch版本改变会抛错。
5. 运行隔离runtime preflight之后才进入后台模型下载、Go/Rust构建和监督启动。preflight失败不能当模型已加载。

新增测试对“全部匹配”与“逐一漂移”分别运行原main至probe哨兵：应否调用精确安装均符合预期；下载未启动。安装测试实际创建/读取/清理constraints，核对精确命令与Torch改变后的拒绝。

**限制：** metadata、pip、GPU数量、import和probe调用为明确fixtures；没有执行真实pip resolver、下载或GPU启动。因此只能确认上述控制流，不能说真实部署的所有版本已准入成功。通用/可选依赖安装后的resolver漂移、安装结果的完整再核对、独立入口和native-adapter路径仍待查。`qwen_compat`未单独拒绝Faster漂移，不能脱离标准bootstrap已有全pin预查直接定为标准启动缺陷；反过来也不能把预查测试当所有入口的终态版本证明。

独立probe的成功仅为 `surface_preflight_passed`：metadata/API/CUDA形状检查，不是模型权重、prompt/codec、声学、RTF或双卡等效证明。没有因表面检查通过改变任何冻结版本。

## 3. F21：leader退出而后代持有stdout时，命令超时失效

源：`py/bootstrap.py:62–96`。**实际CPU进程/管道/计时器复现，确认未修。**

`sh`逐行读取合并stdout，在读流结束后才wait；timer回调仅在直接子进程 `poll() is None` 时设置超时并killpg。leader已退出却有同组后代持有stdout时，回调跳过整组清理，读循环不能收到EOF，也不能抵达后面的超时判断。

确定性实验，而非启动耗时或正常部署证明：

1. 私有临时目录中的真实CPU leader启动一个睡眠后代，后代写出自己的pid/pgid并继承stdout。
2. 自有wrapper用原Popen启动leader，并在返回原sh前等待leader退出；这是明确的Popen观察/调度包装，确保timer装好时leader已经退出，**不是完全未包装的自然竞态压力实验**。
3. wrapper验证后代pgid属于该leader，并持有其pidfd；原sh使用0.1秒期限。
4. 外部0.35秒等待仍超时，wrapper还在原sh读流中，后代pidfd尚未退出。证明该交错下请求的期限没有终止命令。
5. 只通过自有后代pidfd发送KILL；退出可读断言通过，管道EOF后原sh返回0，未报告超时。
6. finally定向终止/回收自有wrapper，后代pidfd退出验证并关闭。无按进程名/任意旧PID杀进程。

这是独立于训练 `stop_ranks` 的F16调用点与行为：本项针对bootstrap命令的超时和管道EOF；没有声称正常run_rank、真实安装/模型下载已发生该问题，更不是显存泄漏证据。后续修复需要把进程组生命周期与leader退出状态解耦，并定义超时/取消/读流的有界清理；本批未实施。

## 4. F22：致命回执写失败会跳过停机，失败计数每轮又清零

源：`py/supervisor.py:147–170`。**原watch控制流复现，确认未修。**

每次HTTP读取成功先把fail_count清零；worker报告fatal_error时，代码先写 `startup-failure.json`，再kill并设gave_up。如果写入抛OSError，直接进入通用except，未执行kill/gave_up，fail_count变为1；下次HTTP成功又归零。同样的致命错误与回执写失败持续存在，也达不到8次健康失败的重启门槛。

测试执行原watch，使用真实STOP事件、8轮受控无睡眠wait；HTTP fatal健康、进程句柄和回执OSError均为fixtures，不制造真实磁盘故障，也不启动工作进程/GPU。started_at置于宽限期之外以排除宽限期影响。结果：

- 8次回执写入尝试/异常；8轮循环。
- kill=0、restart=0、gave_up=False、最终fail_count=1。
- 没有成功落盘的startup-failure.json。

本项不是“GPU实际无法停止”或磁盘故障概率证明，而是**持久化错误能阻断安全停机、并被错误计数策略掩盖**的原控制流证据。后续需比较独立停机与尽力写回执、不同错误计数归属等方案；尚未修改产品。

## 5. 新增12项：10保护 + 2未修观察

测试：`kaggle/tests/test_pass2_startup_boundaries.py`。预检12/12通过，未发生测试失败；日志 `pass2-startup-preflight.log`。

| # | 合同 | 执行范围/限制 |
|---:|---|---|
| 1 | 每项冻结pin漂移触发精确安装；runtime probe先于模型下载 | 原main至哨兵；metadata/安装/设备/导入替身 |
| 2 | 精确pip参数、平台Torch/audio/vision constraints、0600与清理 | 真实临时文件，pip替身 |
| 3 | 安装后Torch改变拒绝，constraints仍清理 | metadata/pip替身；无真实Torch |
| 4 | probe原子替换失败保留原报告并移除临时文件 | 原write_report，真实文件；replace OSError替身 |
| 5 | 子报告超256KiB、坏JSON、checks坏形状均阻塞 | 原isolated_runtime、真实临时报告；子进程替身 |
| 6 | 旧startup nonce失败记录不遮蔽当前活监督与健康回执 | 真实旧JSON；process/HTTP替身 |
| 7 | 已关闭GPU lease不能启动模型角色 | 真实lease/锁；Popen未调用 |
| 8 | Popen OSError关闭日志且不擅自释放监督拥有的lease | 原Proc.start、真实文件/锁；spawn异常替身 |
| 9 | 丢弃过期重试，第7次近期重试give up、不再start | 原restart；kill/start替身 |
| 10 | 流式90秒与句缓冲180秒严格越界才按停滞重启 | 原watch；health/restart与单轮wait替身，非真实等待 |
| 11 | leader退出、后代持stdout导致超时失效 | **F21观察通过=缺陷存在**；真实CPU/pipe/pidfd，确定性交错 |
| 12 | fatal回执I/O失败跳过kill且计数停留1 | **F22观察通过=缺陷存在**；原watch与明确fixtures |

既有13项probe与监督/所有权保护继续纳入累计回归，不把已有正常killpg、旧标记或停止不重启用例重复报为新发现。F01–F20和原专题问题均保留。

## 6. 三独立轮累计专项回归

runner：`docs/validation/step18/run_pass2_startup.py --round N`；每轮独立Python进程/临时状态。上批348 + 新12 = **360项/轮**，逐ID不重复，原348顺序保持。

| 轮次 | tests | failures | errors | skipped | 结果 |
|---|---:|---:|---:|---:|---|
| 1 | 360 | 0 | 0 | 0 | PASS |
| 2 | 360 | 0 | 0 | 0 | PASS |
| 3 | 360 | 0 | 0 | 0 | PASS |
| **合计** | **1080** | **0** | **0** | **0** | **限定专项，不是全功能验收** |

逐轮JSON/regression/console日志保留测试ID、源/测试/runner/support哈希、依赖、F16–F22观察及真实性字段。F21自有进程/pidfd、旧F16后代/锁、F18线程、F19临时资源/槽位均执行清理断言。日志中预期fatal/spawn等ERROR为故障注入，不能单凭日志级别当作测试失败。

继承真实CPU进程/锁、本地HTTP、ASGI、NumPy/safetensors、WAV/文件/归档合同；没有执行完整bootstrap安装/下载/编译/启动、真实Torch算子/optimizer/Gloo/NCCL、真实Qwen/Faster/Whisper/ECAPA/codec、训练或双T4。本批未重跑独立ASGI2.3 companion、旧CLI四矩阵、全Go/race/协议、Chromium全量、旧14分析AST/12DSP或缺cache的provider六案例，不重签历史成绩。

## 7. 封存、工具与交接

- 沿用现存venv，无新依赖安装；environment与完整pip freeze已保存，freeze与第4批相同，不称所有二进制/运行环境绝对一致。NumPy2.2.6仍不同于生产requirements2.4.6；无Torch/Qwen/rustc/cargo/go。
- Node30、JS检查、33份产品Python加本批测试及4个审计脚本共38份AST、repack检查通过，各有独立日志；最终diff检查不替代运行验证。
- 497份历史文件逐SHA保留；53资产/94冻结哈希/15正式文件、原300建议初审、Q25–27各50项保持。未改原包、工作台、浏览器复制实现、安全/录音/取消或私有数据合同。
- 封存验证器首次把两条新观察的追加顺序误认作编号顺序；unittest按测试名称执行，实际为F22再F21。仅修验证器按唯一ID核对，未改测试或产品、未重写三轮收据，原断言失败日志保存在 `pass2-startup-progress-verification-initial-failed.txt`；重验通过。
- 当前验证器 `verify_pass2_startup.py`；当前覆盖/发现为 `g0-pass2-startup-{coverage,findings}.json`；`progress-pass2-startup.json`经验证后同步 `progress-checks.json`。本批run manifest绑定测试、审计脚本、日志、报告、PLAN/IMPLEMENTATION/交接等文件，不循环哈希进度输出。
- `KAGGLE_STEP18_HANDOFF_PROMPT.md`更新为**76份完整备忘录**；具体字节数/SHA由 `handoff-progress.json`与当前progress收据校验，不把旧75份摘要冒充当前原文。

## 8. 下一步和未签收需求

继续第二遍剩27份，优先网关调度/流协议/取消/超时与前端完成排空跨语言交叉核对；随后补全全53份第三遍和300建议最终处置/失败映射。发现仍按原行为反证，不为凑数量另开问题28，不跳过G0实施S1–S8或发布18包，不要求点击Continue。

相似度、无沙沙、自然连续、双卡同条件声学、真实首声/RTF≤0.3、更响且受保护输出、首个可用DeepSeek prefix立即生成、长录音真实训练/提速、全部候选贡献与generated-only PCM等要求均未撤销、未签收。没有用户WAV/真实模型/双T4/物理声卡实验，不能从截图归因或宣称已解决。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_PASS2_GATEWAY.md

# 第十八阶段 G0：全源第二遍第6批——网关调度、流协议、取消与激活终检

日期：2026-10-23；活动分支：`arena/1160bd87-kagglee`。

**本批限定审计完成，产品代码未改，新增F23/F24确认未修。G0仍PARTIAL/BLOCKED，无18包。** 专项测试通过不等于全功能、真实DeepSeek/Qwen、双GPU、训练、听感或提速签收。

## 1. 全文与累计覆盖

本批全文均位于 `kaggle/source/go/gateway/`：

| 文件 | 行数 | 第二遍语义重点 |
|---|---:|---|
| main.go | 478 | speak生命周期、上下文/注册、激活回执与最终状态、代理脱敏、路由/健康/预检 |
| scheduler.go | 490 | 队列优先级、取消清理、重试与已消费PCM、worker帧、停滞watchdog、健康与RTF估计 |
| session.go | 692 | binding/条件、遥测与水位、逐delta生产/结束flush、顺序转发/END、失败与指标 |
| segmenter.go | 489 | exact/live/read策略、首prefix、词/小数/引号边界、段间暂停和呼吸元数据 |
| llm.go | 137 | 请求参数/认证、逐行SSE、完成/错误判定、上下文取消 |
| **合计** | **2286** | **新增5份完整第二遍语义阅读** |

scheduler先完整1–240、再241–490；session分1–240/241–480/481–692；main分1–155/156–320/321–478；segmenter分1–245/246–489；llm完整1–137。以上产品源输出无截断。旧测试/安全函数等调用点仅局部核对，不记额外全文信用；编译全部Go文件也不等于其余测试文件已完成第二遍。

- 第一遍保持53/53内嵌资产、13668行；不是整个Git仓库所有文件。
- 第二遍：26/6003 + 5/2286 = **31/53、8289行，剩22份**。
- 第三遍：**0/53**，测试经过不补第三遍信用。
- 当前台账：`docs/validation/step18/g0-pass2-gateway-coverage.json`。

## 2. F23：HTTP503的健康响应被计为可用，网关回执报告两节点健康

源：`scheduler.go:434–455`、`main.go:225–238`。**原Go实际编译、本地HTTP复现，确认未修。**

healthLoop只看请求是否返回transport error，未检查HTTP状态码；503响应也继续decode JSON。只要其中ready为true、stalled_s小于阈值，就标记healthy=true。原网关health再按这些标记计数。

实验用真实本地HTTP服务固定返回503及 `{"ready":true,"stalled_s":0}`；为scheduler配置两个fixture worker引用，运行原healthLoop，随后调用原网关health。结果：HTTP200的网关回执中 `workers_healthy=2`、`ok=true`。

原healthLoop没有停止接口，因此实验放在**自有Go测试子进程**，父进程设置15秒保底期限，核对子进程成功退出和观察标记；不把永久goroutine留在外层累计套件中。子进程中的HTTP服务清理后整体退出。这里是两个协议fixture引用同一本地服务，**不是两张GPU或两个真实模型**。没有执行完整bootstrap，也不声称线上worker确实返回过这种状态组合。

结论限定为健康准入未校验HTTP状态，不能用这个回执签收模型可用性。生命周期停止接口、JSON结构/预算与过期健康记录等仍需完整矩阵，本批不一并宣称已解决。

## 3. F24：激活期间条件模式改变，参考binding不变，最终仍提交成功

源：`main.go:281–348`、`session.go:73–82、100–136`。**原激活/文件/哈希与真实本地HTTP复现，确认未修。**

初始loadProfileInfo得到ICL条件和reference binding；收到worker回执时检查初始binding/conditioning。最后重新loadProfileInfo，但只比较binding，未同时复核最终conditioning。binding包含参考字节、ref_text、language、generation参数，不包含model_output_mode；将该元数据改为sentence-buffered会使读取出的conditioning变成trained-speaker-vector，但binding相同。

确定性交错：

1. 创建真实私有临时profile和参考哈希输入，保留 `active.json={"id":"previous"}`。参考文件刻意只是哈希fixture，不是可解码音频。
2. 调用原activate。原代码发送真实本地HTTP `/profile/load`。
3. handler在回执前实际改写profile.json，把model_output_mode改为sentence-buffered；返回初始ICL条件与初始binding的成功回执。
4. 原激活终检读取到新的trained-speaker-vector条件，但binding未变，仍提交active.json并返回HTTP200。
5. 验证当前档案条件与回执条件不同、binding相同、活动档案已变成fixture。

worker load回执明确为fixture；**没有创建/验证真实训练产物，没有运行模型、后续合成或播放，不能说已绕过worker训练产物准入或听到错误声音。** 本项是激活成功回执与最终条件版本不一致。与F20的Python重载删除假成功不同；本批另设Go最终删除拒绝保护，原Go删除终检确实会503并保留旧活动档案。

后续需把有效模型/条件/绑定/档案版本纳入一致性终检或事务比较；这只是待实施方向，不在本批修改产品或另开设计问题。

## 4. 新增13项：11保护 + 2未修观察

`kaggle/tests/pass2_gateway_boundaries_test.go`只复制到忽略目录，与逐SHA匹配的原Go包编译，不写入冻结网关。预检13项全部通过，启用race detector。

| # | 合同 | 真实性与限制 |
|---:|---|---|
| 1 | 首次失败丢弃未消费PCM、撤回produced计数、优先另一健康节点，重试回执attempts=2 | 原scheduler、两个本地HTTP协议fixture，无模型 |
| 2 | 已消费PCM后出现worker错误，不重试/重放、不重复计数 | 原run/SegBuf；HTTP流与事件建立确定性交错 |
| 3 | 已取消排队job在健康调度前移除并标记cancelled | 原队列/上下文，无实际合成请求 |
| 4 | 后段先完成仍按段0→1转发PCM，END一次，指标记录一次 | 原serve和实际二进制帧；预填生成PCM fixture、内存ResponseRecorder |
| 5 | PCM Write失败令serve取消上下文，不记录成功END/完整run | 原serve；明确ErrClosedPipe writer fixture，非慢TCP写阻塞实验 |
| 6 | LLM读流取消传播到本地HTTP handler上下文，handler和调用返回 | 真HTTP/SSE头/原StreamLLM，无真实DeepSeek |
| 7 | LLM length截断保留原prefix并上报LLM错误，END仍含错误而非静默成功 | 原produce/serve；真实本地SSE，TTS只注入失败回执 |
| 8 | 100段中英日韩/小数/原始格式文本的read生产不访问LLM、不改写文本 | 原read生产与原分段；文本测试不等于自然连续声学 |
| 9 | 水位高阈值/回滞/恢复及过期遥测的现有放行政策保持 | 原telemetry/allowDispatch；受控时间戳，无真实播放或内存峰值保证 |
| 10 | stats前空EOF、残header、截断PCM负载不能计served | 原scheduler、真实本地HTTP坏流；不同于旧F03的stats后残header |
| 11 | 激活期间档案删除，503且旧active保留、无活动临时文件 | 原activate/真实删除/原子提交；HTTP成功回执fixture |
| 12 | HTTP503仍计入两健康worker | **F23观察通过=确认缺陷**；健康循环在自有子进程 |
| 13 | 条件模式改变但binding不变，激活仍200 | **F24观察通过=确认缺陷**；实际文件变更/HTTP回执fixture |

保留原默认首块4、2–8实验边界、相同session seed/pin、generated-only PCM，不启用参考音拼接或新融合。旧 `TestFirstTTSRequestBeforeLLMTailArrives`本批实际重跑：本地SSE首prefix在LLM尾部放行前到达worker协议端；不是实际DeepSeek/声卡首声成绩。

## 5. 三轮交叉回归：Go与Python分开计数

总runner：`docs/validation/step18/run_pass2_gateway.py --round N`。每轮Go `-race -count=1`，测试副本逐文件hash核对；Go模块网络下载禁用。原包40主测含子测56；旧G0专项10；新专项13。Python companion沿用全部360项，**本批无新增Python测试**。

| 轮次 | Go原主测 / 含子测 | 旧专项 | 新专项 | Go通过主测 / 含子测 | Python通过 | F02独立竞争见证 |
|---|---:|---:|---:|---:|---:|---|
| 1 | 40 / 56 | 10 | 13 | 63 / 79 | 360 | 预期非零、DATA RACE |
| 2 | 40 / 56 | 10 | 13 | 63 / 79 | 360 | 预期非零、DATA RACE |
| 3 | 40 / 56 | 10 | 13 | 63 / 79 | 360 | 预期非零、DATA RACE |

通过套件每轮失败/错误/跳过0，没有race warning；Go含子测试合计237通过，Python合计1080通过。主测试/子测试、不同语言不揉成一个“全功能通过”分母。

旧F02 map alias竞争见证是**独立预期失败**：每轮非零并检出 `WARNING: DATA RACE`，不加入通过套件。旧F03奇数PCM、stats-only、坏error JSON与stats后残header仍复现未修。F16–F22在360项中也重新观察、验证自有资源清理。

Go的实际LLM HTTP取消测试不同于F18用户合成响应断连：本批未做浏览器→Go→真实worker的TCP断连或慢TCP客户端实验。F18仍是进程内ASGI2.4观察，独立ASGI2.3 companion未重跑。也未重跑旧三类网关协议脚本/完整历史六矩阵、Chromium全量、独立旧CLI四矩阵、14分析AST/12DSP或缺cache的provider六案例。

## 6. 工具、环境和封存

- 原有Go不可用，审计venv新增 `go-bin==1.23.9`（历史同版），`--no-deps`安装。保存安装日志、pip安装报告（含wheel URL/SHA）、Go可执行哈希、版本、完整freeze；对比上批freeze，**只新增这一发行包**，其余依赖保持，不称freeze完全相同或全部二进制环境等同。未安装Torch/Qwen/Rust或模型。
- Node30、JS、全部33份产品Python加本批5个审计脚本共38份AST、repack、原Go及含新增探针副本的go vet、gofmt检查通过。gofmt未提供venv顶层wrapper，最初该路径不可用，已按实际GOROOT/bin/gofmt格式化并检查；三轮正式收据在格式化之后生成。
- 525份历史文件逐SHA保持，53资产/94冻结哈希/15正式文件及原300建议、Q25–27各50未改；旧checkpoint不重签。冻结代码、原包、正式工作台、浏览器复制实现和隐私/录音/取消功能未改。
- 当前 `g0-pass2-gateway-{coverage,findings}.json`、`verify_pass2_gateway.py`、`progress-pass2-gateway.json`；验证后同步progress-checks。run manifest绑定本批代码、报告、日志、环境、检查和交接，排除自身及可变进度输出。
- 完整交接更新至**77份原文备忘录**；字节数/SHA由handoff-progress和当前progress收据核对。产品未修改、问题未修复，不能把观察通过当成发布可用。

## 7. 下一步与未撤销需求

继续剩22份第二遍，优先前端app/recorder/index的流终止、取消、遥测与完成排空，再DSP/工具及剩余Go安全/测试文件；随后完成全部53份第三遍及300建议最终处置/失败映射。G0未完成前不跳S1–S8或问题28，不发18包，不要求点击Continue。

更快真实首声、首个可用DeepSeek prefix立即生成、更响受保护输出、全部参考候选贡献可追踪、generated-only PCM、无沙沙、自然连续、短参考相似度、双卡同条件声学、RTF≤0.3、>10分钟录音与真实训练/提速等要求均未撤销或签收。无用户真实WAV/完整模型/双T4/物理声卡证据，不能从截图确定噪声根因，也不宣称已完成所有功能/语音质量验证。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_PASS2_FRONTEND.md

# 第十八阶段 G0：全源第二遍第7批——前端终态、取消、排空与遥测

日期：2026-10-23；活动分支：`arena/1160bd87-kagglee`。

**本批限定审计完成，产品代码继续冻结；新增F25/F26确认未修，G0仍PARTIAL/BLOCKED。** 浏览器/CPU/VM专项通过不是全功能、真实DeepSeek/Qwen、训练、双GPU、声学或提速验收，没有18发布包。

## 1. 全文阅读与累计覆盖

| 文件（`kaggle/source/web/`） | 行数 | 第二遍语义重点 |
|---|---:|---|
| app.js | 1715 | Parser/Player/Worklet、流终态与错误、访问/turn epoch、停止/锁定、播放排空、遥测/报告、库/参考/训练输入与诊断 |
| recorder.js | 358 | 权限等待、session所有权、设备/上下文/计时器、字节/数量/时长预算、原生封装、停止/取消与回调 |
| index.html | 144 | 脚本加载顺序、空白自命名/训练声明、视图/对话框、锁定与公开静态界面、限额和未验收说明 |
| **合计** | **2217** | **新增3份完整第二遍语义阅读** |

app按1–280/281–560/561–840/841–1120/1121–1400/1401–1715完整分段复读；recorder按1–185/186–358完整复读。index首次合并读取被工具截断，随后补读1–80及81–144，并再单独补齐31–80；最终全144行均已可见并复读，**不把截断输出算已读**。旧测试与VM局部核对不新增源码全文信用，运行测试也不计作第三遍。

- 第一遍保持53/53内嵌资产、13668行；不是整个Git仓库所有文件。
- 第二遍：31/8289 + 3/2217 = **34/53、10506行，剩19份**。
- 第三遍：**0/53**。
- 当前台账：`docs/validation/step18/g0-pass2-frontend-coverage.json`；旧台账/日志保留历史原样。

## 2. F25：END不是解析终态，后续PCM/文本继续处理，第二份汇总替换第一份

源：`app.js:729–776`。**完整冻结前端脚本在Chromium中复现，确认未修。**

case5只把解析出的汇总赋给d，未关闭协议状态或拒绝后续帧；读取继续到网络EOF。因此一条流依次含有效END、PCM、文本、另一份END时，后续PCM仍进入Player，文本仍进入回答区域，最终采用第二份汇总，且没有协议错误。

实验使用原网页及完整app/recorder脚本，不提取或改写产品函数；Chromium原生Response/ReadableStream承载明确wire fixture：

1. 第一份有效END，空timeline/per_gpu。
2. PCM16样本1的帧；Player端收到float32值1/32768。
3. 文本 `after terminal`；回答区域确实显示。
4. 第二份END带 `replacement_summary=7`；最终timeline确实采用它。
5. 网络关闭；只发送一次client report，errbox为空。

这是终态/顺序合同的缺口，**不是线上网关确实发送过这条坏流或外部攻击已成功的证明**。AudioContext/AudioWorkletNode为明确设备替身，只确认PCM传到播放器消息端，没有实际播放/声卡或真实生成模型。该PCM仍是生成流fixture，不拼参考音；不能从本项推断用户听到额外话语的根因。

旧F03是Go worker帧接受问题，本项是浏览器client帧END之后的状态机行为，不重复编号旧奇数PCM/stats后残header。后续需定义终态、重复END、后续帧、读流取消与有效汇总校验；尚未实施产品修复。

## 3. F26：网络EOF时先发报告，后续播放/欠载状态不再更新到报告

源：`app.js:625–644、784–818`。**原前端与真实浏览器计时器/序列化路径复现，确认未修。**

B的finally在网络读取结束后调用markGenerationDone，并把w清为false；随后立刻读取Player状态，发一次 `/api/report`。250ms循环仍刷新本地UI，但 `!x || !w` 后不再发送telemetry。声音可能还未开始或未排空，此时不能视为完整播放结果。

确定性实验：原应用接收0.2秒PCM fixture及有效END，立即网络EOF；设备替身暂不提供Worklet状态。第一次report为 `first_played_ms=0、underruns=0`。收到这份report后才注入：

- Worklet缓冲状态fill=4800，应用发送play命令、UI变为“播放中”。
- 一条延迟状态含underruns=1，真实UI刷新到欠载1。

核对最终仍只有一份report、内容与最初逐字段相同，期间telemetry数量也不增加。**延迟状态与设备均为fixtures，数值1不是实际物理欠载；play命令不是扬声器出声，不构成延迟/提速成绩。** 实验不主张正常Worklet在已经接收end后必然新增欠载，而是确认迟到状态和实际播放阶段不能进入当前“结束报告”。

第一遍“report before drain”原先仅源观察，本批补成完整网页事件链实证，首次正式登记F26。旧 `firstPlayedMs`在play命令处赋值的问题继续保留；本项额外是报告生命周期与后续更新缺口，不能只改字段名称就认为解决。

跨语言复核：Go在speak/serve返回后注销session，旧网络EOF后继续发telemetry也可能没有活动session。因此后续需区分生成结束、播放排空、取消与最终client-report合并，设计有界的状态/报告归属；不能简单把w永远保持true。Go调用点是上批已读源码的局部复核，不增本批全文信用，也没有修改任何端点。

## 4. 新增12项：10保护 + 2未修观察

文件：`tests/browser/pass2-frontend.spec.js`及专用fixture helper。预检12通过，失败/跳过/flaky/retry为0。HTTP/音频/设备故障明确替身，完整冻结脚本由浏览器实际执行。

| # | 合同 | 执行边界 |
|---:|---|---|
| 1 | 网络EOF后锁定仍abort旧session、hold/reset播放并清空聊天；重新解锁下一请求history为空 | 真DOM/turn/access epoch，fetch和音频替身 |
| 2 | pagehide在未结束body中锁定，迟到END经旧turn检查取消reader，不产生旧report/私密输出 | 原生流、真实事件与取消回调；非实际页面导航/远端Go |
| 3 | HTTP503 JSON错误可见，按钮释放，无PCM/无成功client report | 原B错误路径；HTTP响应fixture |
| 4 | body.read拒绝可见并释放按钮，不把等待状态永久卡住 | 原生流error；不声称旧F05取消/报告政策已修 |
| 5 | 坏END JSON不生成成功timeline，错误可见、无PCM | 原parser/JSON路径；保留既有错误处理 |
| 6 | 逐字节碎片化UTF8中英日韩/emoji与HTML字面文本正确合并，以textContent显示、不执行HTML | 原帧解析与浏览器DOM，无模型 |
| 7 | 录制中另增文件耗尽数量预算，finish再次核对后丢弃当前片段 | 原recorder、受控duration=1700ms/数据Blob，非真实1.7秒录音 |
| 8 | 重复stop回调只提交一次File，块清空、设备释放 | 原recorder、明确MediaRecorder/track替身 |
| 9 | 旧track-ended不能停止新owned recorder | 原owns检查与事件回调，不能当F04旧onerror已修 |
| 10 | 首次addModule失败后第二次可重新初始化并发请求，旧context关闭 | 音频替身；失败Blob仍未revoke，旧F06保留 |
| 11 | END后PCM/文本/替换汇总仍被接受 | **F25观察通过=缺陷存在**，不是修复 |
| 12 | EOF先发report，随后play/欠载UI变化不更新报告 | **F26观察通过=缺陷存在**，非物理音频测量 |

旧F04旧录音error影响新session、F05解析失败未cancel/abort、F06失败Blob URL不回收仍在旧11项中复现，未修。取消与权限、容器封装、空库/训练输入、安全/访问、正式工作台/复制等旧浏览器合同也全部重跑；没有把“准备训练输入”改说成真正训练按钮或训练闭环。

## 5. 三轮浏览器、VM与CPU回归，分别计数

runner：`docs/validation/step18/run_pass2_frontend.py --round N`。每轮独立Playwright进程，`--retries=0`；既有134 + 新12 = **146项/轮**。真实Chromium中的旧原生录制用振荡器/静音输入替换getUserMedia，不是实体麦克风。新12全部是明确网络/音频设备/事件fixtures。

| 轮次 | 浏览器 | 失败 / 跳过 / flaky / retry | Player VM | 延迟合同VM | Python CPU |
|---|---:|---|---:|---:|---:|
| 1 | 146通过 | 0 / 0 / 0 / 0 | 22通过 | 16通过 | 360通过 |
| 2 | 146通过 | 0 / 0 / 0 / 0 | 22通过 | 16通过 | 360通过 |
| 3 | 146通过 | 0 / 0 / 0 / 0 | 22通过 | 16通过 | 360通过 |

浏览器合计**438通过**；CPU合计**1080通过**，CPU每轮失败/错误/跳过0。本批无新增Python用例。两种VM分别22×3/16×3，原Player/Worklet代码和明确时钟/端口/status替身，不能把它们合并成实体播放成绩。

旧VM中已完成20/50ms短尾卡buffering/starved的观察继续通过，51ms可发play；这意味着旧缺陷仍存在，不是排空修好。重采样结束flush、首块时间/消费/声卡出声区别与Rust/DSP/trimmer分块问题也未修。默认首块4、2–8实验边界、generated-only与参考PCM禁播不变。

浏览器代码复制保护重跑：原始文件使用真实hash及浏览器sentinel保护，1–17完整包复制合同仍保持；不把sentinel声称为原始整文件浏览器复制。正式空白文件/用户粘贴和不强制预填流程保持。

每轮保留原始Playwright JSON/stderr、逐用例状态/单次执行、5份未修观察（F04–06/F25–26）、两种VM JSON、CPU逐ID日志/JSON、源/测试/support哈希。CPU继续F16–F22自有进程/锁/线程/临时资源清理，不重签旧收据。

**本批未重跑Go79项/独立F02竞争见证、独立ASGI2.3 companion、旧独立CLI/协议矩阵、14分析AST/12DSP或缺cache的provider案例。** 这些保留上批/历史成绩，不列作本轮执行。也没有真实DeepSeek、完整模型/codec、双T4、实际训练、远程Kaggle、物理声卡、用户WAV或声学/提速成绩。

## 6. 环境、检查、封存与交接

- node_modules未保留，按冻结package-lock执行 `npm ci --ignore-scripts`恢复；保存日志与依赖树，未改package-lock/产品依赖。预检及三轮使用实际Chromium。审计venv沿用，完整pip freeze与上批相同，没有新增Python发行包；Go1.23.9仍可用但本批未重跑其套件，无Torch/Qwen/Rust运行。
- Node30、JS检查、33份产品Python加本批5个审计脚本共38份AST、repack，以及前端/新探针/VM的JS语法检查通过。最终diff检查和manifest验证不替代模型验收。
- 575份历史文件、53资产/94冻结哈希/15正式文件、原300建议初审及Q25–27各50保持；原包/工作台/安全/录音/复制产品代码未改。
- 当前 `g0-pass2-frontend-{coverage,findings}.json`、`verify_pass2_frontend.py`、`progress-pass2-frontend.json`；验证后同步progress-checks。manifest绑定本批报告/测试/helper/runner/收据/日志/环境/交接，排除自身与可变进度输出。
- 完整交接更新为**78份原文备忘录**，以handoff-progress及当前progress核对具体字节数/SHA。

## 7. 下一步与全部未撤销要求

继续第二遍剩19份：优先Python/Rust DSP、音频边界与工具自检，再补剩余Go安全/测试和LICENSE/MEMO；随后全53份第三遍及300建议最终处置/失败映射。G0未完成前不跳S1–S8/问题28、不发18包、不要求点击Continue。

更快真实首声、首个可用DeepSeek prefix立即生成、更响受保护输出、全部候选贡献可追踪、generated-only、无沙沙、自然连续、短参考相似度、双GPU同条件声学、RTF≤0.3、>10分钟录音和真实长数据训练/提速等均未撤销或签收。截图不能证明噪声根因，fixture不能冒充真模型/实机/试听，整体仍PARTIAL/BLOCKED。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_PASS2_DSP.md

# G0 全源第二遍第8批：Python/Rust DSP 与音频工具

日期：2026-10-23；分支 `arena/1160bd87-kagglee`。**专项三轮完成，G0 仍 PARTIAL/BLOCKED；产品未修改，未发布18包。**

## 1. 全文阅读信用

本批重新完整阅读9份1500行，不将测试执行、局部调用点检查计作全文：

| 文件（均位于 kaggle/source/） | 行数 |
|---|---:|
| py/audio_rt.py | 222 |
| rust/audio_rt/Cargo.toml | 17 |
| rust/audio_rt/src/lib.rs | 433 |
| tools/e2e_check.py | 180 |
| tools/encode_training.py | 128 |
| tools/selftest.py | 177 |
| tools/trained_voice.py | 30 |
| tools/voice_benchmark.py | 168 |
| tools/watermark_check.py | 145 |

第一遍保持53/53、13668行；第二遍由34/53、10506行推进至 **43/53、12006行，剩10份1662行**；完整第三遍仍0。Rust全文分段读完；旧测试组合输出曾截断，仅补读相关范围，不给旧测试全文信用。范围是冻结包内53资产，不是整个 Git 仓库。

## 2. 新增合同：10保护＋2未修观察

`kaggle/tests/test_pass2_dsp_boundaries.py`：

1. 非有限输入等价于零替换、不修改调用方数组。
2. 关闭淡入/动态增益后的单纯 DC 过滤跨调用连续；**不是一般分块不变性声明**。
3. 门限下信号不学习语音包络、不改变增益。
4. 禁用 Rust 时不调用动态库加载。
5. ABI2 跳过、ABI3 ctypes 签名设置；符号与库对象为 fixture，未 dlopen Rust。
6. 原 benchmark/measure 的18次请求同文同 seed/同 pin、warmup 独立、私有 WAV/ledger 保留。
7. 后续请求失败仍保留先前慢行、WAV、ledger，最终报告 BLOCKED 且不泄漏异常详情。
8. encoder 控制器移除凭据/租约变量、固定离线 CPU 环境、恢复信号处理器；Popen/回执是显式 fixture。
9. 缺失或超过1MiB回执拒绝，不打印其内容；fixture 子进程角色，不冒称真实编码。
10. trained_voice CLI 非预期错误脱敏、503保留 blocked 状态。
11. F27 NumPy flush DC残留观察。
12. F28 benchmark逐条 GPU 身份观察。

### F27：flush 尾音归零，但 NumPy DC 记忆未归零

实际 NumPy：480样本常量0.2→flush(192)→240样本零输入，尾音最后为0，但后续零输入240样本全部非零，峰值 **6026 int16**；fresh Leveler 同长零输入全零。NumPy仅清 `_last`，Rust源码的非空 flush 还清 `dc_x1/dc_y1`。

**已核对影响范围：** worker `run_job` 每次调用 `_reset_leveler(pid)`，关闭旧对象并创建新对象；这次反证是复用同一 Leveler 的 API/后端一致性缺口，不证明正常跨请求路径复用该残留，更不证明截图里的沙沙声根因。Rust没有编译/执行，不能把源码差异说成已实测双后端等价或不等价。

### F28：benchmark 接受两端点全部测量都声明 GPU0

执行原 `run()`/`measure()`、两实际本地 HTTP 端点、真实 profile/pin/WAV/ledger 文件。health fixture 分别声明 GPU0/1、CUDA_VISIBLE_DEVICES=0/1；18条合成统计却全部声明 GPU0。报告仍为 `measured-speed-only`，`real_gpu_verified=true`、`speed_target_passed=true`，而行内 worker索引仍含0/1。

**证据边界：** health/模型/PCM/计时均为 fixture，报告中的上述 true 是被反证的工具输出，绝不是本批真实GPU验证或RTF成绩。端点身份与逐条实际合成身份缺少一致性校验；不能由此证明部署时真的两端共享GPU，也不能用两个健康回执替代运行期硬件与等效参数证据。两个缺陷均未修复。

## 3. 三轮实际执行

| 范围 | 第1轮 | 第2轮 | 第3轮 |
|---|---:|---:|---:|
| CPU合同，原360＋新12 | 372 PASS | 372 PASS | 372 PASS |
| NumPy DSP分块合成信号案例 | 12 | 12 | 12 |
| 原EdgeTrimmer AST合成信号案例 | 8 | 8 | 8 |
| 独立真实CLI合同 | 4 | 4 | 4 |
| CPU失败/错误/跳过 | 0/0/0 | 0/0/0 | 0/0/0 |

CPU共1116通过；新增36包含30保护和6次未修观察，不能解释为全部功能修复。分块/裁剪器保留既有问题，不重复编号。CLI每轮backend-static、backend-runtime、benchmark-default均按预期exit2/BLOCKED；resource-status exit0但GPU未验证，**预期阻塞不计模型成功**。脚本 `run_pass2_dsp.py` 和 `run_pass2_dsp_cpu.py`；后台执行已正常exit0、无监听端口。

本批没有重跑浏览器146、Player VM22/latency VM16、Go79/独立F02竞争或独立ASGI2.3 companion；这些只保留历史记录，不挪作本批新成绩。CPU合集含原ASGI/进程/文件合同，模型、ASR、声纹及特定调度角色仍为显式fixture。没有Torch tensor/optimizer/Gloo/NCCL、完整模型、GPU、物理麦克风/播放器或声学验收。

## 4. 完整性与未完成项

- 新测试预检12/12通过；三轮测试身份及F27/F28观测一致。
- Node30、JS检查、产品Python AST及新审计脚本语法、repack check通过；不改冻结产品/lockfile。
- 625份历史文件SHA保留；53源资产、94冻结哈希、正式HEAD15文件、300建议原文/处置及Q25–27各50条校验不变。
- 依赖沿用，pip freeze与前端检查点完全相同；没有新增安装。Rust/rustc/cargo、Torch/Qwen不可用；Go可用但本批未跑Go。
- `g0-pass2-dsp-coverage.json`、`g0-pass2-dsp-findings.json`、三轮原始收据、manifest及 `verify_pass2_dsp.py`为当前证据；交接完整内嵌增至79份。
- F01–F26及原DSP分块、短breath、校准/裁剪/播放器短尾问题继续未修，不将合成信号当真实语音。
- 后续仍待：encoder回执内容/退出码一致性、各工具语义终态/样本预算的完整失败矩阵、ABI空指针/长度/返回码与Rust真实工具链验证、两worker版本/参数及测量身份持续一致、真音频听测和端到端首声。

下一批完整复读剩余 Go security 及测试/go.mod、LICENSE/MEMO，共10份1662行；再进行全53份第三遍与300条最终处置/测试映射。真实长录音训练、参考贡献追踪、DeepSeek首prefix、双T4等效参数、自然连续朗读、无沙沙、真实RTF≤0.3等要求均未豁免、尚未签收。**不越过G0先改DSP，不跳S1或另开Q28，不要求用户点击Continue。**

---

## 内嵌备忘录：KAGGLE_STEP18_G0_PASS2_SECURITY.md

# G0 全源第二遍第9批：Go安全／测试与文档收尾

日期：2026-10-23；分支 `arena/1160bd87-kagglee`。

**第二遍53项全文复读已完成；完整第三遍仍0，G0仍PARTIAL/BLOCKED。产品未改，未生成18发布包。**

## 1. 阅读范围与进度

以下均重新全文阅读，工具输出未截断；不把测试执行计作源码阅读。

| 文件（相对 kaggle/source/） | 行数 |
|---|---:|
| LICENSE-QWEN-DERIVED.txt | 201 |
| MEMO.md | 220 |
| go/gateway/fidelity_test.go | 187 |
| go/gateway/go.mod | 3 |
| go/gateway/preflight_test.go | 67 |
| go/gateway/reliability_test.go | 159 |
| go/gateway/security.go | 247 |
| go/gateway/security_test.go | 342 |
| go/gateway/segmenter_test.go | 123 |
| go/gateway/voice_binding_test.go | 113 |
| **本批合计** | **1662** |

第一遍53/53、13668行保持；第二遍由43/53、12006行推进至 **53/53、13668行，剩0**。此范围是冻结包内53资产，不等于整个Git仓库所有文件，更不等于三遍全文或所有功能验收。

## 2. 安全与既有测试的交叉核对

本批检查认证失败/owner预算隔离、令牌桶锁、并发名额与panic/取消清理、已知/未知Content-Length、JSON单值与Unicode、代理凭据剥离/请求取消、CORS、首prefix调度与原文保留测试、档案绑定和preflight只读行为。

`kaggle/tests/pass2_security_boundaries_test.go`新增12主测试，**10保护＋2未修观察**，只在SHA匹配的产品副本旁编译，不把探针放进冻结源码：

1. 失败认证只耗失败桶，不消耗owner通用/语音预算或占名额。
2. 1000个真实goroutine竞争容量7令牌桶，恰好7次通过；启用race。
3. 8项预算环境变量的上下边界、越界、非整数和整数溢出拒绝。
4. 重操作限额独立于语音名额，取消至handler退出后释放。
5. handler panic展开defer后不泄漏语音名额，后续合法请求仍可进入。
6. Unicode JSON字节预算在精确边界通过、少1字节拒绝；已知和未知长度两种路径。
7. CORS预检不等于API认证：跨host拒绝、合法预检不调用业务、未认证POST仍拒绝。
8. 代理删除全部凭据header值，保留有界请求内容和目标路径。
9. 原反向代理取消传到实际本地HTTP上游，错误不包含上游地址，名额释放。
10. 混合BMP/补充平面Unicode字符预算、history/system边界和非法角色；直接非法UTF-8字符串被validator拒绝。
11. F29：wire畸形Unicode在解码后被替换并接受。
12. F30：供应商HTTP错误正文可把假配置密钥带入客户端帧与指标。

### F29：解码先替换畸形Unicode，后续UTF-8检查失效

实际本地HTTP→原Guard→原decodeJSON→原validateSpeak：孤立高代理项、孤立低代理项、原始非法UTF-8字节三类输入，均HTTP200，输入字符串变为 `a�b`。直接将非法UTF-8交给validator会拒绝，但JSON解码已完成替换，后续 `utf8.ValidString` 只能检查替换后的字符串。

这是**严格输入与原文保真边界缺口**，不是认证绕过。见证使用组合校验handler，不执行完整speak、TTS或实际读音；没有声称正常浏览器JSON.stringify会产生这些畸形输入。修复阶段仍需统一非法编码、代理项、重复键等策略及兼容范围，不能直接删除或改写合法正文。

### F30：未脱敏上游HTTP错误进入客户端ERROR／END与metrics

实际授权网关 `/api/speak`→原Session.produce→原StreamLLM→本地HTTP401替身。请求未提供X-DeepSeek-Key，使用配置的**合成假密钥**。替身错误正文回显Authorization和私有详情；原StreamLLM把前800字节拼入错误，客户端ERROR、END和metrics记录均包含假密钥。

这是第三方错误内容未脱敏的传播路径；**不是未授权访问证明，也不是某真实供应商已泄密的证明**。API仍需要有效共享Bearer；供应商、错误正文与配置密钥全部是fixture，没有读取真实凭据、调用真实DeepSeek或生成PCM。后续应采用稳定公开错误码/安全消息，保留受保护诊断，不把截800字节误当脱敏。

两项均三轮复现，**尚未修复**。此前F01–F28及其他专题观察保持，不重复编号或宣称解决。

## 3. 三轮验证结果

| 每轮范围 | 第1轮 | 第2轮 | 第3轮 |
|---|---:|---:|---:|
| 原Go主测试／含子测试 | 40／56 PASS | 40／56 PASS | 40／56 PASS |
| 第一遍Go专项 | 10 PASS | 10 PASS | 10 PASS |
| 上批Go专项 | 13 PASS | 13 PASS | 13 PASS |
| 本批Go专项 | 12 PASS | 12 PASS | 12 PASS |
| **Go合计主测试／含子测试** | **75／91** | **75／91** | **75／91** |
| CPU既有合同 | 372 PASS | 372 PASS | 372 PASS |
| 副本go vet | PASS | PASS | PASS |
| 独立F02竞争见证 | 预期非零＋DATA RACE | 同左 | 同左 |

Go通过集合含子测试共273，CPU共1116；新保护30次、新未修观察6次。通过集合失败/跳过/race warning均0，CPU失败/错误/跳过均0。**独立F02故意失败见证不混入通过数字，F02仍未修。** 各轮使用 `-race -count=1`；第三方服务仅自有loopback HTTP。旧F23无限健康循环仍隔离在自有测试子进程并核对退出；测试服务器/处理goroutine正常清理。后台验证已exit0，无监听端口。

本批继承CPU372并实际重跑，包含原进程/锁/ASGI/NumPy/文件合同及F27/F28 fixture反证。没有新增Python测试；没有重跑独立CLI四项矩阵、NumPy分块/裁剪器探针、独立ASGI2.3、浏览器146和Player/latency VM，不挪用其历史成绩。原Go首prefix→本地worker请求测试重跑，不是实际DeepSeek/模型首声或速度成绩。

## 4. LICENSE与MEMO裁决

- LICENSE已全文读完：许可副本、修改声明、来源归属、条件性的NOTICE保留、商标限制及免责声明等条款已记录。**阅读文件不等于项目依赖、模型、训练数据或再分发法律合规签收**；实际适用范围、依赖许可/NOTICE清单与发布材料仍待核对，不出具法律结论。
- MEMO顶层仍为历史step15、xvector-only及maxgain12等表述；冻结产品当前17 ICL/maxgain6，已有D01文档漂移继续保留，不改冻结MEMO、不重复登记为新缺陷。其部分历史“短breath已修”等说法也不能覆盖后续F10实证。
- 测试通过证明断言成立，不证明断言覆盖全部协议/真实模型/听感；segmenter内部breath标记不等于worker会播放参考片段。generated-only、参考PCM不拼接要求保持。

## 5. 封存与下一步门禁

- 686份历史文件SHA、53源资产、94冻结哈希及正式HEAD15文件保持；原300建议与Q25–27每题50条不变。
- Node30、JS、产品Python与新审计脚本AST、repack、Go探针gofmt以及三轮副本vet通过。
- Go1.23.9沿用，无新安装；pip freeze与DSP批完全相同。Rust/rustc/cargo、Torch/Qwen仍不可用；无完整模型、真实GPU、训练、物理音频或声学/性能签收。
- 封存校验首跑错误地要求F02在 `halt_on_error=1` 下仍发出逐测试fail事件；实际是立即退出并发出包级fail。已保留首错日志，改为同时核对非零退出、DATA RACE、指定见证run与包级fail；不修改产品/测试，不重跑或抹除三轮记录。
- 当前检查点：`g0-pass2-security-coverage.json`、`g0-pass2-security-findings.json`、`progress-pass2-security.json`、`verify_pass2_security.py`；完整交接80份。

**下一步进入第三遍全源交叉审查，不实施S1：**

1. 先按API→Go→Python→文件快照追踪输入、pin、档案修订和错误脱敏；每份必须重新全文阅读，局部跟踪不计信用。
2. 然后核对生成/网络/播放生命周期、取消所有权、GPU租约及训练产物绑定；已知问题建立修复顺序和回归映射，不只重复通过测试。
3. 全53份第三遍和300条最终处置/失败见证映射完成前，G0保持未签收；缺真实硬件/音频的项目继续BLOCKED。
4. 不新增伪训练按钮，不用fixture替代双T4、长录音训练、无沙沙/音色/连续朗读、DeepSeek首prefix和真实RTF≤0.3验收，不要求用户点击Continue。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_PASS3_INPUT.md

# G0 全源第三遍第1批：输入、档案内容绑定与认证文件

日期：2026-10-23；分支 `arena/1160bd87-kagglee`。

**第三遍7/53份、1930行；剩46份11738行。第一、第二遍均53/53、13668行。G0仍PARTIAL/BLOCKED，产品与冻结发布包未修改。**

## 1. 本批第三遍全文信用

| 文件（相对 kaggle/source/） | 行数 | 本遍交叉核对 |
|---|---:|---|
| go/gateway/main.go | 478 | speak验证/trim、profile加载、激活重检、错误/代理、路由与认证 |
| go/gateway/security.go | 247 | Unicode解码边界、body预算、令牌桶、名额/取消与期限 |
| go/gateway/session.go | 692 | profile JSON类型、pin序列化、generation默认值/范围、队列/播放遥测、错误与metrics |
| py/qtts_common.py | 211 | 档案路径/读取、原子JSON、归档提取、配置和音量目标 |
| py/voice_binding.py | 60 | 实际跨语言内容hash、类型/范围、NOFOLLOW/NONBLOCK、文件大小变化 |
| py/resource_limits.py | 172 | 上传预算、暂存/replay清理、后台准入与取消所有权 |
| py/access_control.py | 70 | 私有口令文件/锁、文件类型检查时机、转发目标 |
| **合计** | **1930** | **7份全范围重新阅读，无截断** |

浏览器app.js只局部复看660–720请求构造，library_api.py只局部查看严格JSON入口，llm等其他调用点也没有本批第三遍全文信用。没有把第二遍阅读、测试运行或AST扫描当作第三遍全文。7份的all_three_complete仅表示三遍阅读记录齐全，**不表示其缺陷已修或产品验收通过**。

## 2. 新证据与原有建议映射

新增6项Go合同（5保护/1观察）与6项Python合同（5保护/1观察）：

- 实际Go/Python代码比较8个合法pin向量：UTF-8/NUL、缺省与显式gen、gen整体null、metadata排除、top_k负零和0、Unicode不同码点序列、边界参数与长度前缀。
- 12个非法generation类型/范围向量两端均拒绝；不是用另一份hash实现代替产品代码。
- 两本地worker ack fixture期间实际改变generation参数，原activate最终pin重检503，旧active保留。
- 原完整speak对null/空/错误text类型/尾随JSON拒绝，无session/worker调用。
- 两个不同合法profile ID、相同内容的pin相同：pin是内容标识，**不是身份、授权或声学相似度**。
- 上传读取最多预算+1字节即拒绝，不截断冒充完整音频；精确预算保留全部字节。
- body暂存在溢出、断连、下游异常三种路径关闭，不进入不该执行的解析/业务。
- 原子JSON替换失败保留旧私有文件、清临时文件，后续重试可用；不是多文件事务证明。
- 参考文件fstat后长度增长被原binding拒绝；不是同长度恶意改写/同UID隔离保证。
- 两实际认证CPU进程取得同一私有口令，仅输出摘要供临时比较；口令不进日志，临时目录清理。
- F31、F32未修观察，详见下节。

`pass3-input-recommendation-links.json`将8条**原有**建议逐项链接到实际测试身份或未修见证：R1-013/016/020/083、R2-028/039/050/063。每条明确覆盖不足；原300条不改，specific_row_test_signoff/final_disposition_signed_off/product_fix_implemented均false。相邻generation类型保护不能冒充完整ref_text schema签收；单文件replace不能冒充候选/JSON事务；旧训练metadata fixture不能冒充真实训练或原生模型。

## 3. 两项新确认的未修问题

### F31：同一JSON的top_k:null跨语言含义不同

实际磁盘profile包含 `gen:{"top_k":null}`：Go JSON解为map[string]float64时将null变成0，`loadProfileInfo`接受并产生非空pin；同目录/同JSON交给实际Python `reference_binding`，因None不是数值而抛ValueError。合法的gen整体null两端均按缺省处理，不能把两种null混为一谈。

本批Go测试通过受控CPU子进程调用当前Python文件，校验ABI字节和内容pin，不调用模型。参考文件是明确的hash字节fixture、不是可播放WAV。**不证明正常建档会写入该非法字段，也不证明已成功激活或生成错误音色。** 这是配置schema/内容绑定接受域不一致；两端应在计算pin前统一严格类型语义。

### F32：认证文件若为FIFO，无写入方时先阻塞再谈类型校验

实际原 `ensure_access_token`：自有0700认证目录下，既有`.access-token`是0600 FIFO且无writer，子进程在调用前发送握手，之后不能返回，测试外部强制终止并reap；同脚本的普通文件control正常返回。`_read_file`用NOFOLLOW但没有NONBLOCK，open在fstat确认普通文件之前阻塞。

**边界：** 没有真实口令、用户目录、真实bootstrap、远端请求或GPU工作。攻击者是否能写私有目录不是此测试结论，不能称远程认证绕过。0.25秒是测试收容边界，不是产品性能成绩；自有子进程已清理。后续应在安全打开且不被特殊文件阻塞的前提下检查类型/属主/大小，保留有效私有token及并发锁语义。

F01–F30、D01及旧DSP/播放/训练/校准观察继续未修。本批不靠新编号掩盖既有问题。

## 4. 三轮实际回归

| 每轮范围 | 第1轮 | 第2轮 | 第3轮 |
|---|---:|---:|---:|
| 原Go主测/含子测 | 40/56 PASS | 40/56 PASS | 40/56 PASS |
| 既有Go专项10+13+12 | 35 PASS | 35 PASS | 35 PASS |
| 新Go专项 | 6 PASS | 6 PASS | 6 PASS |
| **Go主测/含子测合计** | **81/97** | **81/97** | **81/97** |
| CPU旧372+新6 | 378 PASS | 378 PASS | 378 PASS |
| 副本go vet | PASS | PASS | PASS |
| 独立F02竞争见证 | 预期非零/DATA RACE | 同左 | 同左 |

Go含子测共291通过，CPU共1134通过。新保护共30次、未修观察共6次。通过集合失败/错误/跳过/race warning均0；F02独立故意失败不混入通过数，仍未修。所有Go回归启用-race/-count=1，产品源码未插入新探针。F29/F30随原S2套件实际重跑，仍未修；F23无限health循环继续隔离于自有子进程，正常退出已核对。

Go/Python预检各6通过。后台三轮正常exit0，无监听端口；CPU进程/FIFO/认证并发进程已清理。没有重跑浏览器146、Player/latency VM、独立ASGI2.3、独立CLI矩阵、分块/裁剪器探针，不挪用历史成绩。原CPU套件包含实际ASGI/进程/锁/NumPy/文件测试及明确模型角色fixture，不是全功能或模型验收。

## 5. 后续实施建议与门禁（尚未修改产品）

1. 为generation建立跨语言schema，区分缺省字段、gen整体null与成员null，禁止无声强制转换。
2. 将本批8合法/12非法向量固化成修复后的公共合同，并增加成员null、额外键和大数策略。
3. 严格检查原始JSON UTF-8和代理项，保留合法码点序列，不用替换字符假装原文保真。
4. 统一重复键、未知字段、浮点/布尔/字符串接受策略，不能仅修改Go而让worker域更宽。
5. 保留生成参数进入pin的属性；不要通过忽略gen来“修复”两端不一致。
6. 激活最终核对同时包含内容pin与conditioning模式，覆盖尚未修复的F24。
7. 准确区分单文件replace与候选/转写/profile多文件事务，保留旧成功档案与失败证据。
8. 认证读取不得在确认文件类型前无限等FIFO；新增特殊文件/目录/链接/权限矩阵。
9. 保留认证目录0700、文件0600、锁与两进程一致性，不把拒绝异常文件改成静默重建口令。
10. 上游错误使用安全公开码和阶段，私有诊断不直接回显HTTP正文/密钥，覆盖未修F30。
11. 首prefix、文本保真与播放终态分别测试；当前browser/API trim并不受producer原文拼接测试完整保护。
12. 将这些证据作为300建议的部分映射，待第三遍全覆盖后才做最终处置，不把本批8行当全300签收。

## 6. 封存与下一步

739份历史证据SHA、53源资产/94冻结哈希、正式HEAD15文件及原300/Q25–27各50保持。Node30/JS/产品与新审计Python AST/repack/Go探针gofmt通过，三轮副本vet通过；pip freeze与第二遍收尾相同，无新依赖。Go沿用1.23.9；无Rust/Torch/Qwen/实际模型/双GPU/训练/物理音频/音质/提速签收。完整交接81份。

当前 `g0-pass3-input-coverage.json`、`g0-pass3-input-findings.json`、`progress-pass3-input.json`、`verify_pass3_input.py`；各轮原始日志、manifest与建议映射保留。

下一批继续第三遍参考分析/API/档案修改与备份事务的完整复读，优先检查候选/转写/pin/模式切换及取消所有权，再依次完成剩46份、300最终映射和真实目标环境门禁。不跳S1/Q28，不实施未获G0签收的DSP修复，不要求用户点击Continue。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_PASS3_REFERENCE.md

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

---

## 内嵌备忘录：KAGGLE_STEP18_G0_PASS3_TRAINING.md

# G0 全源第三遍第3批：训练输入、声学码与产物提交

日期：2026-10-23；分支 `arena/1160bd87-kagglee`。

**第三遍累计20/53份、5365行，剩33份8303行。前两遍各53/53份、13668行保持。产品冻结，G0仍PARTIAL/BLOCKED。** 这是冻结包53源资产，不是整个Git仓库全审/全功能/目标模型验收。

## 1. 本批全文复读：8份1505行

| 文件（相对 kaggle/source/） | 行数 | 复核重点 |
|---|---:|---|
| py/training_data.py | 285 | WAV全部帧、文本/声明、选中来源/revision、预备目录/发布、只读租约 |
| py/training_codes.py | 355 | 模型指纹/结构、schema2封存来源、逐样本完整码、取消末门、继承OFD |
| py/training_job.py | 227 | 严格准入/参数、双rank进程、FD/密钥、checkpoint发布与最终回执 |
| py/tts_training.py | 200 | JointLoss/DDP/累积/溢出、采样覆盖、实际优化入口、rank报告/保存；仅源码语义 |
| py/tts_dataset.py | 125 | 完整文本/16码本序列预算、缓存克隆、collate偏移/标签/掩码；仅源码语义 |
| py/trained_profiles.py | 155 | 完成记录/hash/实际safetensors解析、绑定、固定参考文本、发布前重核 |
| tools/encode_training.py | 128 | 离线CPU子进程、parent-death、私有回执、超时/取消与提交提示 |
| tools/trained_voice.py | 30 | 显式未验adapter声明、describe/publish参数与脱敏错误 |
| **合计** | **1505** | **8份重新完整阅读** |

初次三组拼接输出被截断，不计那次为全文；随后逐组完整补读，training_codes分1–180/181–355，其余完整范围均无截断。tts_training与tts_dataset的张量/优化语义是源码审查，不冒充Torch执行。adapter_engine/lora_adapter/qwen_compat及train_tts等剩余文件不因调用或旧辅助测试阅读获得本批全文信用。

**计数纠正：**进度曾手算为1605行，信用生成器断言失败，未写错误覆盖文件；逐项求和为1505。已保存`pass3-training-credit-correction.json`，校正为3860+1505=5365、13668−5365=8303。没有加文件/测试或修改源代码抵消错误。

## 2. 新增12项：11保护＋1未修观察

`kaggle/tests/test_pass3_training_boundaries.py`实际执行文件、PCM、flock/OFD、原控制器与受控CPU子进程、原产物检查/发布事务及CLI。明确不导入Torch算子，不进行优化器/Gloo/NCCL/模型/实际训练。

| 项目 | 已验证及边界 |
|---|---|
| raw输入准备遇KeyboardInterrupt | audio/JSONL已写后中断，清pending，保留已有snapshot/原库，释放租约后可重试 |
| PCM极值/奇数帧数 | −32768/+32767和36001帧完整保留，带奇数长度JUNK元数据被移除；总帧预算少1明确413，不裁切 |
| acoustic codes最终取消 | 原完整_verify已经通过后置取消，最后rename前409、清pending；原输入保持，可重新prepare |
| 第二样本encoder遇BaseException | 第一份已编码/落盘后KeyboardInterrupt，全部本次pending清理，源租约释放，后续重试成功 |
| Qwen finish指纹 | 只构造无tokenizer对象执行原finish，materialized字节变更409；**未执行构造器/编码，不绕过F01** |
| code OFD最后引用 | 原adopt_lease保留dup，父上下文先关后删除仍409；最后adopt上下文关后才可删。进程内FD试验，不是此项执行双rank |
| cancelled结果拒绝 | 即使有可解析的合成adapter，结果改cancelled仍409、不创建profile |
| request/epoch拒绝 | request样本顺序不一致、rank loss NaN各自409；未穷尽所有rank/类型/报告矛盾 |
| publish第二次检查 | 写完候选JSON后更改speaker tensor，原最终inspect拒绝、清临时档案、保留active；profiles正常.lock保留 |
| 固定参考匹配 | 非首行的真实参考WAV配其自身文本、保存pin，不改active/不声称quality/reload；code lease元数据及adapter均为fixture |
| trained_voice CLI | 错pin返回rejected/409/exit2、不创建档案、不带私有路径或Traceback；无模型加载 |
| F35 | 原控制器空检查点仍报告优化器执行，产物检查器会拒绝，详见下节 |

### 首次预检失败及修正

首次收集43项，其中31项是直接导入TestCase类带来的既有重复项；新增断言有1失败：误将正常留下的`.lock`视为发布残留。原事务正确清理了`.trained-profile-*`且没有新profile。改用模块导入避免重复收集，断言明确仅`.lock`保留。产品/旧fixture未改；首次原始日志和`pass3-training-precheck-correction.json`保留。最终预检仅新增12项、12通过；三轮累计不计那31项重复。

## 3. F35：子进程成功＋manifest存在，不足以声称优化器执行

原`run_controller`在两个rank exit0后，核验code pin、Base指纹及`adapter/manifest.json`文件存在，即把最终结果标为`completed`/`optimizer_execution_observed=true`，未在该阶段解析检查点内容或核对完整rank报告。

受控见证：

1. 使用真实本地raw/code fixture快照；仅训练准入、依赖存在与tokenizer一致门禁为显式测试替换，无生产CLI开关。
2. 两个真正自有CPU子进程执行原GpuLease/code OFD adopt与parent-death握手，随后正常exit0，不执行rank_worker/run_rank/优化器。
3. rank0只创建`adapter/manifest.json`，内容为`{}`；没有adapter/speaker tensor。
4. 原控制器仍生成`completed`、rank_exit_codes=[0,0]、optimizer_execution_observed=true；磁盘result与回执一致。
5. 原`TrainedArtifacts.inspect`409拒绝该产物；信号处理恢复，code与GPU租约可再次获取，没有发布非法声音。

**结论仅为控制器回执的证据不足**，不是实际训练成功、真实rank会生成坏检查点、模型错误或发布绕过的证明。正常源码run_rank/save_checkpoint还有完整报告/权重保存与rank同步；本见证有意替换它们，不能用结果否认真实优化代码存在。与F13–15工具自检、F16后代清理及F01包版本元数据不同，不重复编号。F35三轮稳定复现，未修。

后续修正宜抽取**不依赖最终result.json**的检查点/来源/rank验证器，在最终completed回执前使用；不能直接把现有inspect插入控制器造成“inspect先要求completed结果、结果又等inspect”的先决条件环。应区分processes_exited_ok、checkpoint_validated、optimizer_execution_recorded和quality_verified；结构自洽仍非真实硬件/优化器独立证明。

## 4. 三轮执行与独立完整性核验

| 项目 | 第1轮 | 第2轮 | 第3轮 |
|---|---:|---:|---:|
| 累计CPU/ASGI/文件/进程合同，旧390＋新12 | 402 PASS | 402 PASS | 402 PASS |
| 新保护／未修观察 | 11／1 | 11／1 | 11／1 |
| 失败／错误／跳过 | 0／0／0 | 0／0／0 | 0／0／0 |

共1206通过；新保护33次、F35见证3次。三轮测试ID/观察一致，旧390逐项继承；原控制器CPU子进程正常回收，后台进程exit0。旧F16后代与F32认证FIFO等见证随CPU集合重跑，仍未修。

本批新增独立trained_voice CLI拒绝合同；原CPU合集已有encode CLI/parent-death/真实信号等也执行。**未重跑额外四项专项CLI矩阵、Go/F31/独立F02、浏览器/Player/latency VM、独立ASGI2.3、NumPy分块/trimmer单独矩阵**，不挪用旧成绩。标准Node30/JS/38份Python AST（33产品库存＋新测试＋4审计脚本）/repack通过。

825份历史文件SHA逐项保持，53源资产/94冻结哈希/正式HEAD15文件不变；原300与Q25–27每题50行动保持。pip freeze与上批相同，无安装新依赖。Go存在但本批未跑其套件；无Rust/Torch/Qwen/CUDA/真实双T4/物理音频。NumPy/safetensors/合成WAV为格式/文件证据，不是预训练模型/训练或声学质量证据。

独立封存首次准备也有审计脚本错误：交接生成器的f-string标题中新增空manifest字面量`{}`未转义，AST/manifest准备未完成，首次verifier报缺manifest。已仅将生成器字面量转义为`{{}}`，保留首错与correction说明，重新生成交接/AST/manifest后再校验；原始三轮收据与产品/测试/runner未改、未重跑回归。

## 5. 原建议部分证据与实施前待办

本批链接原7条：R1-020、R2-093、R3-071/072/075/076/080；含本轮真实重跑的旧信号合同。与之前去重22个原ID有暂定证据，**不是22条已完成**。原建议文本和初始处置不改；specific_row_test_signoff/final_disposition_signed_off/product_fix_implemented均false。

1. 训练输入格式完整、声明与内容语义审阅分列，不将declaration当版权/身份自动验证。
2. 长录音接收、样本分段、全部选择覆盖、实际训练迭代和参考prompt使用继续区分；现有每文件240秒/总900秒门禁不等于真实长数据已训练。
3. 保持sealed-source-v1及内容hash，训练前/提交前核验Base、tokenizer与codes来源版本。
4. 保留fixture/legacy拒绝训练和发布；不得为模型测试便利加生产绕过开关。
5. 统一实际provider distribution元数据；F01仍未修，finish-only保护不能掩盖constructor版本入口。
6. 明确final-cancel相对原子rename的线性化点；提交后取消回执必须指引list/verify，不误称从未提交。
7. 取消/失败只清理自有本次pending，保留旧成功版本；继续解决F16已退出leader的额外后代，不根据历史PID乱杀。
8. 校验每rank逐epoch覆盖、padding、步数/溢出与实际代码报告一致；union覆盖不足以穷尽所有矛盾报告。
9. 在真实Torch环境验证DDP forward、变长序列、累积尾组/共同溢出、FP16/FP32 adapter与两rank digest，不靠AST/tiny替代目标模型。
10. 区分受控CPU lease互斥和真实在线推理/离线双GPU资源隔离；不得为测试盲停驻留模型。
11. 发布前重核tensor/hash/固定参考；成功发布仍只是显式未验候选，保持trained无Base/Mock回退。
12. 将控制器进程退出、检查点完整性、优化记录、reload、音质与加速分别出证；F35先修回执合同，不能新增一项true就声称真实训练已验证。

## 6. 当前检查点与下一步

当前证据：`g0-pass3-training-coverage.json`、`g0-pass3-training-findings.json`、三轮原始log/receipt、manifest、`verify_pass3_training.py`和`progress-pass3-training.json`。完整交接83份，顶层PLAN/IMPLEMENTATION已同步。

下一批继续第三遍adapter/推理入口、provider兼容及训练/推理绑定，复核加载失败、取消、缓存版本与原样生成输出；继续剩33份/8303行及300最终处置。无产品修改、不发18包、不跳S1/Q28、不要求Continue。

长录音真实训练、全部参考贡献追踪、<10秒相似度、首可用DeepSeek prefix立即生成、更响受保护输出、更低建档延迟、自然连续朗读/去沙沙/无接缝、generated-only PCM、双GPU等效参数与真实RTF≤0.3等均未豁免，均不由本批替身签收。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_PASS3_INFERENCE.md

# G0 全源第三遍第4批：adapter、推理与生成资源清理

日期：2026-10-23；分支 `arena/1160bd87-kagglee`。

**第三遍累计27/53份、6667行，剩26份7001行。前两遍各53/53份、13668行保持。产品未改，G0仍PARTIAL/BLOCKED。** 全文阅读齐全与问题已修/功能已验不是同一状态，53资产也不等于整个Git仓库。

## 1. 新增7份完整复读：1302行

| 文件（相对 kaggle/source/） | 行数 | 重点 |
|---|---:|---|
| py/adapter_engine.py | 108 | 本地Base固定、磁盘trained绑定、cached选择仍检查产物、原子模块切换、整句输出及取消 |
| py/lora_adapter.py | 91 | 冻结Base/FP32 A-B、全部替换前校验、commit回滚与张量设备；仅源码语义 |
| py/qwen_compat.py | 97 | provider分布元数据/命名空间冲突、RoPE schema/代理/注册表与失败重试 |
| py/clone_stream.py | 126 | generated-only条件与解码分离、有限窗口、pending与close/取消 |
| py/gpu_ownership.py | 151 | 固定同UID命名空间、FD类型/nonce/OFD、短写失败释放、观察状态非授权 |
| py/worker.py | 680 | boot/profile事务、pin/缓存/锁、生成/DSP/指标、HTTP和断连/排空 |
| tools/train_tts.py | 49 | CLI准入与退出码、rank私有错误日志、原控制器分支 |
| **合计** | **1302** | **7份完整重新阅读，无源输出截断** |

worker分1–170/171–340/341–510/511–680连续读完，其余完整全文。辅助旧测试组合输出一次截断，不计测试全文信用。结合上一批5365+1302=6667，13668−6667=7001；机器断言逐项核算。未复读的DSP/监督/Go/浏览器/工具/许可文件不因调用或继承测试获得本批第三遍信用。

## 2. 新增12项：11保护＋1未修观察

`kaggle/tests/test_pass3_inference_boundaries.py`执行原AdapterEngine/RealEngine/Worker/RoPE/租约方法与真实文件、NumPy、safetensors、flock/OFD。Torch只替换最小导入/seed记录/空inference上下文，**没有模拟tensor算子**；实际LoRA prepare/commit、native generation、predictor/codec decode均未执行。合成完成记录不是实际训练证据。

| 新合同 | 结果与覆盖边界 |
|---|---|
| adapter Base绑定不符 | inspect/prepare/commit前409；旧key/prompt保持；不声明全部失败切换回滚 |
| adapter缓存命中 | 仍真实重读并解析合成产物；第二次实际改变safetensors字节即409，不调prepare/commit |
| adapter codes绑定不符 | manifest与profile声明不一致409，不调张量替换，key/prompt不提交 |
| 生成前取消 | 不select、不seed、不调用生成；最小依赖导入仍会先发生，不宣称零成本取消 |
| 生成后取消 | 整句native替身已返回的4800 PCM全部丢弃；不能据此声称可以抢占CUDA核/codec |
| native PCM严格边界 | 空列表、错误采样率/容器/维度、全零、NaN、超token对应长度拒绝；合法4800帧只yield一次float32整句，不伪造声学流 |
| RealEngine度量/关闭 | 两个回放包prepare取max、codec/decode求和、窗口峰值取max；回放iterator耗尽关闭一次，seed记录正确；不是RTF测量 |
| worker部分失败恢复 | 先出一包后生成器异常，1 error/1 stats/1 sentinel、解锁并after_job；后续job可成功，failed/served各1；不解决F07无界队列/F18早断连 |
| 同pin但prompt缺失 | 原worker重新resolve/cache后才生成；resolver/音频为替身，实际hash/pin/锁流程执行，不修复F08旧prompt回滚 |
| RoPE失败重试 | 原错误cause保留且失败未改注册表；重试安装单一bridge，不改变其他registry项；不是实际MimiConfig/Torch smoke |
| GPU记录短写 | 真pwrite少2字节触发异常，FD关闭、busy false、非法记录无诊断值，锁文件仍0600，后续owner可获得；仅同UID合作协议，非GPU测量 |
| F36 | 上游close异常导致窗口finish跳过，详见下节 |

预检12/12一次通过，未跳过。worker错误恢复测试预期记录synthetic异常日志，不能把日志中的ERROR误算为测试失败；原始日志完整保留。

## 3. F36：上游close失败，窗口最终清理未受独立finally保护

原`generated_only_stream`的退出顺序：

```python
finally:
    it.close()
    window.finish(cancelled=True)
```

本批通过原函数实际启动、yield一包后由消费者close；把上游iterator.close设为抛synthetic RuntimeError，原finally第二行即被跳过。

- 上游close调用1次，异常传播；原生成器frame本身已经关闭。
- 被测试显式捕获的真实GeneratedCodecWindow仍closed=False，pending为1920个NumPy样本、codes为合成标记。
- 最后由测试所有者显式finish(cancelled=True)，closed=True、pending空、codes=None，全部本次资源清理。

**结论仅是异常安全的清理顺序缺口，未修。** 准备/predictor/decoder/Torch上下文为明确控制替身；测试为观察状态主动保留window引用。没有证明生产上游close实际会抛异常，也没有证明正常生成器引用释放后仍有持续内存占用、真实GPU泄漏、错误声音或沙沙声根因。建议嵌套try/finally保证窗口清理不依赖上游close成功，同时明确原错误与清理错误优先级；不能仅吞掉异常再伪报成功。

F36三轮稳定见证，与F08加载失败的prompt/pin不一致、F18未开始body迭代的取消丢失不同；不重复登记旧问题。F01–F35/D01及原DSP/trimmer/播放器/校准问题继续保留，未因本批通过而关闭。

## 4. 三轮验证与证据完整性

| 项目 | 第1轮 | 第2轮 | 第3轮 |
|---|---:|---:|---:|
| 累计CPU/ASGI/文件/进程合同：旧402＋新12 | 414 PASS | 414 PASS | 414 PASS |
| 新保护／新未修观察 | 11／1 | 11／1 | 11／1 |
| 失败／错误／跳过 | 0／0／0 | 0／0／0 | 0／0／0 |

共1242通过；新保护33次、F36见证3次，三轮测试ID与观察一致、旧402逐项保留。三轮后台正常exit0、无监听端口；已有实际CPU子进程/信号/OFD、原ASGI与CLI合同随合集运行，F35等旧见证仍未修。本批新增部分没有HTTP浏览器或原生tensor运行，不把方法调用冒充HTTP。

Node30、JS检查、38份Python AST（33产品库存＋新测试＋4审计脚本）、repack通过。858份历史SHA、53源资产/94冻结哈希、正式HEAD15文件保持；原300与Q25–27各50行动不变。pip freeze与上一批一致，无新依赖。完整交接84份、当前manifest/独立verifier/progress均已建立。

**本批未重跑Go/F31/独立F02、浏览器/Player/latency VM、独立ASGI2.3、额外四CLI、NumPy分块/trimmer单独矩阵；不挪用历史成绩。** 沿用Go工具但本批未执行该套件；无Rust/Torch/Qwen/完整权重/CUDA/真实训练/双T4/物理音频，实际音质与提速未签收。

## 5. 原建议部分证据与待实施事项

本批映射原7条R1-045、R2-060/079/093、R3-006/007/071；累计去重27个原ID有暂定链接，**不是27条已完成**。原文/初始处置不改，specific_row_test_signoff/final_disposition_signed_off/product_fix_implemented全部false。没有因本批另开新问题，原300及既有逐题行动保持。

1. 生成器拥有的窗口finish置于独立finally，覆盖上游close本身出错、消费者close与模型异常。
2. 明确close错误不覆盖原生成错误，独立记录阶段与清理完成事实，错误脱敏不吞真失败。
3. bounded window/no reference decode要在真实预训练codec复测，不用本批解码替身或源码因果性签收音质。
4. adapter冷选择与缓存命中都保持Base/manifest/codes来源检查，缓存key不能替代实际tensor文件核验。
5. prepare全部通过再commit，commit异常需原子恢复所有模块；本批只检查不进入prepare的拒绝分支，真实CPU张量/不同rank adapter和CUDA设备路径仍待证。
6. F08需协调engine prompt与worker已接受pin的事务提交/回滚；补一个缺prompt重载保护不能当作已修。
7. F09需统一conditioning规范化与对外mode，同内容pin仍不能签收不同backend/mode一致性。
8. 保留adapter整句缓冲声明和取消后丢弃返回PCM；不要将cooperative stop写成GPU立刻停或首声已提速。
9. F07队列背压和F18早断连需要独立所有权合同；worker解锁后可再服务不代表网络/生产者已取消。
10. 汇总prepare/codec/decode只反映定义中的阶段，不能用生成完成或虚拟播放时间替代真实首声/消费/RTF。
11. GPU锁只约束同版本/同UID合作进程；OFD/nonce/短写保护不是容器/外部进程或真实两卡隔离保证。
12. 继续严格provider元数据/bridge入口，真实依赖环境安装与实际configuration smoke要另证，不强降TF4或临时替换模型。

## 6. 当前检查点与下一步

`g0-pass3-inference-coverage.json`、`g0-pass3-inference-findings.json`、三轮原始log/receipt、manifest、`verify_pass3_inference.py`、`progress-pass3-inference.json`为当前证据；PLAN/IMPLEMENTATION与84份全文交接已同步。

下一批第三遍启动/监督、backend preflight、资源/测量工具与DSP接口，继续核对超时/退出/失败回执与真实测量定义；随后剩余Go/前端/许可等，完成余26份7001行及300最终处置。产品不改、不发18包、不跳S1/Q28、不要求用户点击Continue。

长录音真实训练、全部参考贡献追踪、短录音相似度、首可用DeepSeek prefix立即生成、更响且受保护输出、更低建档延迟、自然连续朗读/无沙沙/接缝、generated-only PCM、双GPU等效参数与真实RTF≤0.3仍未豁免，不由本批fixture签收。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_PASS3_STARTUP.md

# G0 全源第三遍第5批：启动、监督、preflight、资源测量与 DSP 接口

日期：2026-10-23；活动分支 `arena/1160bd87-kagglee`。

**第三遍累计38/53份、8920行，剩15份4748行；前两遍各53/53份、13668行保持。产品冻结未改，G0及整体仍PARTIAL/BLOCKED。** 本批是阅读与故障边界核验，不是完整功能、真实训练、声学或提速签收。

## 1. 全文重新阅读11份2253行

| 文件（相对 kaggle/source/） | 行数 | 审查重点 |
|---|---:|---|
| py/bootstrap.py | 451 | 自有进程组、超时/后代管道、冻结依赖、preflight/nonce、旧标记不盲杀、启动回收 |
| py/supervisor.py | 219 | 秘密环境最小化、子进程组与OFD、重试/STOP、fatal回执、退出释放与信号恢复 |
| py/audio_rt.py | 222 | ctypes ABI/符号、加载降级、NumPy状态/有限值、淡入/flush/限幅 |
| rust/audio_rt/Cargo.toml | 17 | cdylib、构建与依赖、接口版本 |
| rust/audio_rt/src/lib.rs | 433 | ABI3及全部导出、指针/长度、DC/RMS/平滑/呼吸/flush；仅源码，未运行Rust |
| tools/backend_probe.py | 200 | 静态/运行时区分、callshape非语义、子进程限时与回执、退出码与成功状态 |
| tools/e2e_check.py | 180 | health/生成/终端统计的成功定义、原F13及错误流边界 |
| tools/resource_control.py | 41 | 合作OFD状态/等待/占用，不将CPU状态冒充GPU运行 |
| tools/selftest.py | 177 | 原F15、fixture/真实服务与自检失败含义，不提升为全功能验收 |
| tools/voice_benchmark.py | 168 | 明确--run、双卡health/实际stats绑定、terminal/计数/RTF、私有O_EXCL产物 |
| tools/watermark_check.py | 145 | 原F14、PCM/统计及真实听感界限 |
| **合计** | **2253** | **11份全文，无产品源输出截断** |

bootstrap连续1–225/226–451，Rust lib连续1–215/216–433，其他全文。辅助旧测试组合输出曾截断，不计辅助测试完整阅读。6667+2253=8920，13668−8920=4748。余15份是LICENSE 201、MEMO 220、Go gateway10份2110行、web3份2217行；调用/继承测试不自动给予这些文件第三遍信用，LICENSE阅读也不等于法律签收。

## 2. 新合同12项：10保护＋2未修观察

测试：`kaggle/tests/test_pass3_startup_boundaries.py`。执行原启动/监督/探针/benchmark/DSP Python代码，真实自有CPU进程、线程、文件和OFD；C ABI 测试库仅用于符号故障注入，不重写DSP，不是Rust实测或多语言性能成果。

| 新保护 | 证据与明确边界 |
|---|---|
| bootstrap活跃直属子进程超时 | 原sh以真实Timer终止自有会话组，直属child为SIGKILL退出且stdout关闭；不修F21“leader已退出、后代仍持管道”路径 |
| bootstrap资源忙/旧PID标记 | 真OFD忙409；释放后旧marker仍409且不更改，去掉本测试marker后才允许通过，killpg未调用 |
| supervisor已退出leader的后代 | 自有leader先exit0，后代忽略TERM并继承真fleet FD；原Proc.kill仍发送组KILL，pidfd确认后代退出、OFD busy恢复false；不是CUDA测量，不修训练F16 |
| supervisor停止优先于重启 | 真线程/Event在重试流程发STOP，原restart退出且start不调用；kill/start为控制替身，不作为重启时延性能测量 |
| supervisor认证准入失败 | 真OFD先取得，认证替身抛UploadRejected；原main返回2，未build子服务，清本次PID、还OFD并恢复SIGTERM/INT处理器；未完整启动服务 |
| preflight超时 | 原isolated_runtime控制器终止/回收真实自有睡眠CPU child，返回blocked与runtime_timeout，模型/推理/训练/性能标志均false |
| callshape不执行模型 | classmethod、实例方法只inspect不调用；额外必填参数阻塞；即便callshape接受也保留behavior untested，非实际provider语义签收 |
| benchmark流及分母 | 分裂header/payload可重组；拒绝终端后数据、重复stats、残帧、超16MiB声明、缺stats、bool/错误sample数、错误pin/engine、cancel/failed/anomaly、NaN/不一致RTF；HTTP、PCM、stats、clock均fixtures，.1/.2不是实测性能 |
| benchmark不覆盖历史报告 | 不带--run时不联网；既存0600报告导致FileExistsError且字节/权限不变，无ledger/WAV创建；只证明拒绝覆盖，不签收友好CLI错误呈现 |
| NumPy有限值边界 | 非连续float64/NaN/±Inf/±1e6输入，经原Leveler得到同长度有界int16，空输入零长、flush192/末端0及再次flush0、close幂等；不声明分块不变/DC状态复位/真实听感 |

### 首错记录（不隐藏）

首次新预检12项中11通过、1 error：测试误访问不存在的`UploadRejected.status`，实际字段为`code`；产品已按预期拒绝。仅改两处测试断言字段，保留`pass3-startup-precheck-first.txt`与`pass3-startup-precheck-correction.json`，修正后12项通过。没有以产品改动消除该测试错误。

## 3. F37：子进程非零退出，但原父控制器仍接受成功回执（未修）

原`backend_probe.isolated_runtime`先wait，随后只按报告文件大小与部分JSON形状接受回执，没有先检查returncode。测试替换的**报告生产者**是自有真实CPU child：写相同schema1/status=surface_preflight_passed/checks=[]、全部模型验证标志false的合成报告，然后分别exit0与exit23。原父控制器均原样返回该报告，真实child均已回收。

三轮新CPU见证一致。确认的是**非零child退出状态没有参与回执准入**；不是实际GPU preflight误通过，不是Torch/provider实际先成功后崩溃的证明。报告生产者明确替身，不能据此宣称有真实GPU/模型。未来修复还需组合returncode、必要checks/报告完整性和状态，不能只看宽松JSON。

## 4. F38：缺必需符号的ABI3库令ctypes导入中止，而非回退（未修）

使用已有`/usr/bin/cc`在自有临时目录真实编译极小C共享库，仅导出`unsigned int rt_version(void)`，以编译宏分别返回2/3；在独立真实Python child中导入原`audio_rt`，实际ctypes加载该库：

1. ABI2：版本太旧，原加载器跳过，结果NumPy；
2. ABI3：访问首个必需符号`rt_leveler_new`时抛`AttributeError`，原except只捕获`OSError`，import以非零码中止；
3. 同ABI3但`QTTS_NO_RUST=1`：显式绕过native加载，结果NumPy。

三轮均一致，回执保存C源码SHA及实际编译器版本。库/源/child临时文件不入Git。**这是实际C ABI 故障注入＋ctypes执行，不是Rust编译或Rust DSP执行；没有证明正式Rust库损坏，也没有声学、跨后端等价或性能结论。** 加载策略应先明确“明确失败关闭”还是“可观察、明确标注的NumPy回退”，不能掩盖native缺失；本阶段没有修改产品实现。

## 5. 三轮重新运行的结果与未执行项

| 实际执行 | 第1轮 | 第2轮 | 第3轮 |
|---|---:|---:|---:|
| CPU继承集合＋新合同 | 426 PASS | 426 PASS | 426 PASS |
| failure/error/skip | 0/0/0 | 0/0/0 | 0/0/0 |
| 独立NumPy分块探针 | 12 case | 12 case | 12 case |
| 独立trimmer探针 | 8 case | 8 case | 8 case |
| 实际CLI期望合同 | 4 | 4 | 4 |

CPU **426×3＝1278 PASS**，每轮完整保留前批414项并新增12项；新增保护30次、观察见证6次。比较逐项测试ID与结果，不以总数替代继承核验。原F01–36/D01保留，观察通过不是bug修复。独立分块探针仍观察到48样本切块差1424 int16等已知分块依赖，实验完成不是算法通过容差/去沙沙成功；裁剪探针也是合成信号，不是真实逐字听感签收。

每轮真实CLI：backend静态、backend --runtime、benchmark默认均期望exit2/blocked，resource status期望exit0但gpu_verified=false；合计12次CLI，其中9次预期阻塞。benchmark未加--run、无模型加载或WAV生成。不能把“预期阻塞符合合同”写成GPU/性能成功。CPU集合本来包含的本地HTTP/ASGI/CLI/租约/信号等继续实际重跑，但模型/health/decoder/ASR等明确替身的部分不会升级证据。

另单次新执行Node30、JS语法（工作台及产品web）、Python AST38、repack --check；没有本批Go/race/vet、真实浏览器/VM、独立ASGI2.3 companion。旧历史成绩不挪作本批成绩。沿用现有.venv，无新Python或系统依赖安装；freeze与前批相同（NumPy2.2.6，不冒称requirements2.4.6）。无Torch/Qwen/CUDA/rustc/cargo。C测试库由已有系统cc编译；**Rust未编译、未执行**。

## 6. 完整性、原300建议与交接

- 887份历史文件SHA在本批前保存，历史收据/测试/报告不得改写；53源、94冻结、15正式工作台文件及原17包保持。
- `advance_pass3_startup.py`逐文件核对SHA/行数，新增11/2253；coverage第一/二遍保持，第三遍38/53，未把剩15份涂绿。
- 本批7条原建议仅部分证据链接：R1-075/079/080、R3-019/020/076/079；与前批去重累计33个ID，原300逐字与Q25–27各50项保持。没有新增重大方案选择题，没有跳Q28；所有最终处置/逐条签收仍false。
- 独立`verify_pass3_startup.py`复核历史SHA、冻结、逐项CPU继承、F37/38、探针/CLI原始日志及SHA、manifest、建议映射、环境与完整交接。
- 完整交接85份备忘录逐份嵌入匹配；本报告、PLAN/IMPLEMENTATION及交接优先状态同步。manifest不自哈希，也不嵌入可变交接/进度，避免循环；这些由独立核验器另验。

主要收据：`docs/validation/step18/pass3-startup-cpu-round1..3.json`、`pass3-startup-companions-round1..3.json`、`g0-pass3-startup-{coverage,findings}.json`、`pass3-startup-recommendation-links.json`、`pass3-startup-run-manifest.json`、`progress-pass3-startup.json`；终态以独立核验成功日志为准。

## 7. 后续精确动作（待实施，不冒充修复）

1. 下一批完整复读Go gateway10份2110行；保存历史SHA，新增严格输入/取消/终端协议与私密错误边界合同。
2. 另批完整复读web3份2217行，实浏览器重验录音/复制/排空/取消，不能用Node代替浏览器。
3. 阅读剩LICENSE/MEMO 421行并分开记录技术与法律边界；完成53资产第三遍后仍不自动签收300处置。
4. 对F37规划child exit0必要条件，再验证合法形状但缺checks/错误mode/自相矛盾flags的拒绝政策。
5. 对F38规划明确native加载诊断，测试缺rt_version/各必需符号/损坏ELF/错误ABI；不能静默称Rust已启动。
6. 保留C库仅为符号故障fixture；真正Rust编译、ABI导出、数值与生命周期检查必须在具备Rust环境独立执行。
7. 继续修前完成F21/F22/F16退出与fatal回执设计，不因本批监督器保护成功覆盖另一路缺陷。
8. benchmark将health GPU和每次stats GPU/engine/binding关联校验，F28仍未修；fixture RTF不得签收0.3目标。
9. 对F13–15分别闭合终端统计/错误JSON/早EOF/奇数PCM等失败语义，不把工具自检绿标当全功能证明。
10. NumPy/Rust先统一状态/分块/flush语义再测容差，保留generated-only，禁止拼参考PCM提相似。
11. 后续按G0→S1顺序实施，不碰冻结17与正式工作台，不提前生成18发布包。
12. 真模型、双T4、长录音/真实训练、真实参考与生成WAV、声学/自然连贯/相似度/首声与RTF缺口继续列BLOCKED，具备条件后再真实三轮验收。

**结论：阅读与故障边界证据推进，F37/F38正式登记但未修。不是全功能通过、不是真实声音改善；G0与整体仍PARTIAL/BLOCKED。直接继续下一批，无需用户点击Continue。**

---

## 内嵌备忘录：KAGGLE_STEP18_G0_PASS3_GATEWAY.md

# G0 全源第三遍第6批：网关调度、LLM 流与文本保留

日期：2026-10-23；活动分支 `arena/1160bd87-kagglee`。

**第三遍累计48/53份、11030行，剩5份2638行。前两遍各53/53份、13668行保持；产品未改，G0与整体仍PARTIAL/BLOCKED。** 全文语义阅读、原建议最终处置、功能修复和真模型/声学验收是不同门禁；53资产不代表整个Git仓库审计。

## 1. 新增完整复读10份2110行

| 文件（相对 kaggle/source/go/gateway/） | 行数 | 重点 |
|---|---:|---|
| fidelity_test.go | 187 | 原文/复制相关源文字合同、首块预算、即时首前缀、真实本地SSE→首worker请求先于尾部 |
| go.mod | 3 | 无额外模块依赖；兼容版本与实际Go工具链分开记录 |
| llm.go | 137 | 请求/认证/预算、SSE增量与结束、EOF/错误/取消、非200正文隐私F30 |
| preflight_test.go | 67 | 已授权只读报告、大小/JSON边界、公开recorder静态白名单 |
| reliability_test.go | 159 | profile身份、激活后确认、LLM完整性、token预算、同源 |
| scheduler.go | 490 | FIFO/优先级、watermark、重试/已消费PCM、请求取消、帧终端/统计、health与EMA |
| security_test.go | 342 | token/重复header、已知/分块body预算、并发槽、截止/取消、proxy去秘密 |
| segmenter.go | 489 | exact/read/live策略、Unicode/小数/闭合引号、文本分组、暂停/seed/flush |
| segmenter_test.go | 123 | 分段稳定、保字/长度/小数/呼吸/清理旧合同的实际边界 |
| voice_binding_test.go | 113 | 内容pin/文本/语言/生成参数跨语言、trained模式与read/chat分离 |
| **合计** | **2110** | **10份全文，无本批源阅读截断** |

scheduler连续1–245/246–490，segmenter连续1–245/246–489，其余全文。辅助旧测试一次组合输出截断，不计辅助测试完整阅读。Go main/security/session三份已在第三遍输入批计信用，本批虽编译/调用及读取必要上下文，不重复加信用。8920+2110=11030；13668−11030=2638。余5份是web/app.js1715、index.html144、recorder.js358、LICENSE201、MEMO220。LICENSE未来阅读不代表法律签收。

## 2. 新增12个Go合同：10保护＋2未修观察

文件：`kaggle/tests/pass3_gateway_boundaries_test.go`。只复制到忽略缓存的SHA匹配Go源树编译；产品目录不加入测试、不改产品。使用原Go方法、真实本地HTTP和控制流；LLM/provider、worker、PCM、stats、认证材料明确是合成fixture，不调用真实DeepSeek、不生成真实人声。

| 新保护 | 实际检查与边界 |
|---|---|
| chat请求完整性 | 原Session.produce→StreamLLM保留自定义system、两条history及当前user顺序，传model/8192/stream/合成Bearer；原前缀形成job，提交完成；不是真provider输出预算/质量证据 |
| 缺LLM key | 原StreamLLM在任何HTTP与delta前返回错误；fixture服务调用0，不要求用户提供秘密 |
| SSE边界 | 心跳/comment/非data行、role-only delta、CRLF、Unicode、最后无换行的DONE/stop均按预期解析；不签收所有SSE扩展/任意代理行为 |
| SSE错误脱敏 | 合成error.message或坏JSON不进入错误文本，已收到原始前缀不改写；仅流内错误，不修非200正文F30 |
| 多语种read原文 | 中文/组合字符/astral emoji/URL/双空格/换行/12.50，1/2/7/4096 rune切块后逐字相等，索引连续，重复Flush空；特意不含独立无词尾段，F39另列 |
| pause/seed | profile pause超界正确钳制；同seed17的read分组/暂停/元数据在1与4096切块下相同；不是自然韵律或跨GPU音色相同证明 |
| retry预算 | 真HTTP429正文限400字节，attempts=2时不再排队，failed1/served0、busy恢复、错误有界、healthy不盲改；不解决原frame/状态缺口 |
| urgency/FIFO | 原Submit/pickLocked跨会话优先urgent/first，平级按seq稳定FIFO；未Start无限health/ticker，不作吞吐测量 |
| 统计EMA | 原run对合成正数统计更新rtf2→2.6、first100→130、audio3→5，增加attempts/queue_wait并计2个PCM样本；合成audio_s与PCM长度并不对应，不称RTF一致性已验 |
| synth参数转发 | 原run首块opt-in2、后续6，保留seed91/pin/conditioning/语言/原字/停顿/呼吸字段；只是请求转发，不能证明真实首声提速或允许拼参考PCM |

### 首错与纠正均留档

首次Go预检在编译阶段失败：测试误写`session.submitted`，实际字段为`allSubmitted`；未执行任何测试。仅改该测试断言字段后，12项race预检通过，无产品修改。`pass3-gateway-precheck-first.txt`、`precheck-correction.json`、`precheck-final.txt`保留。

另一次内联审计元数据命令因findings字典括号混写而SyntaxError，整段解析失败、没有写文件或推进coverage，不影响后台回归。已拆成显式credit脚本和字典构造，记录在`pass3-gateway-metadata-correction.json`；不改写历史。

## 3. F39：PreserveText仍丢独立标点/空白尾段（未修）

原`Segmenter.finish`无论PreserveText是否true，都会以hasWord=false丢弃无词组。实际LiveSegCfg、逐rune馈入、原Flush下四个稳定见证：

| 输入 | 重连全部seg.Text |
|---|---|
| `你好。!?` | `你好。` |
| `你好。\n\n` | `你好。` |
| `\t\n` | 空 |
| `!?` | 空 |

前两例即时首前缀已发后，剩余独立无词尾段被丢；普通带词内容内的标点并非全部被删除。确认的是“PreserveText/重连逐字相等”合同缺口，**不是漏读语词、沙沙、接缝或真实声音质量下降的证明**。本批没有修改分段算法。未来需明确无损展示文本与可朗读分组的关系，不能用丢标点后的重连声称原文完全保留，也不能为了保字随意增加模型朗读内容。

## 4. F40：cancelled worker统计在活ctx下仍计served（未修）

真实本地HTTP worker替身返回一个合法偶数字节PCM帧（2个合成样本），随后stats包含failed=false/cancelled=true。原`Scheduler.run`只拒绝failed=true，没有拒绝cancelled=true：会话ctx仍有效、buffer done=true/error为空、worker served=1/failed=0、busy恢复false。新测试直接断言这些原始状态，三轮一致。

**worker、PCM和stats为fixture，不是生产worker真实取消、CUDA仍运行、漏音或成功播报取消任务的证明。** 本批继承的实际请求ctx取消→worker取消保护仍通过；该保护不覆盖worker自己报告cancelled但请求ctx仍有效的状态组合。未来应校验终端状态一致性，连同F03奇数PCM/空stats/非法错误JSON/残帧等统一考虑，不靠“served计数变绿”验收生成。

## 5. 三轮完整执行矩阵

| 每轮Go race集合 | 顶层通过 | 含子测试通过 |
|---|---:|---:|
| 原产品测试 | 40 | 56 |
| 原G0合同 | 10 | 10 |
| 第二遍gateway合同 | 13 | 13 |
| 第二遍security合同 | 12 | 12 |
| 第三遍input合同 | 6 | 6 |
| 本批新gateway合同 | 12 | 12 |
| **每轮合计** | **93** | **109** |

三轮均 **93/109 PASS**，合计顶层279次、含子测试327次，正常集合意外失败/skip/race为0。比对前第三遍input批81/97逐项测试ID，确保原前缀先发、原文、消费后不重试、pin/同seed、认证/取消等既有合同实际继承，不只比较总数。新10保护×3＝30次，2观察×3＝6次；观察通过表示缺陷仍可见，不是修复成功。

- **F02故意race见证独立执行三次，均预期非零并出现DATA RACE。** 不混进正常通过数，也不隐藏为“全无race”；map alias race仍未修。
- Go vet三轮exit0；实际Go1.23.9，GOTOOLCHAIN=local/GOPROXY=off，不下载新工具链或模块。SHA核对13份复制原Go文件与6个外置探针；本批阅读新增仅10份。
- CPU完整继承集合每轮426、共 **1278 PASS**，失败/错误/skip0；**本批没有新增Python合同**，原414+12来自前批。包括F31–38等CPU观察/自有进程/OFD/C ABI故障fixture，但不是模型训练或Rust实测。
- 每轮另NumPy分块12、trimmer8、实际CLI4；三个CLI期望blocked/exit2，resource status exit0但gpu_verified=false。合成分块差异观察没有变成去沙沙或跨后端容差通过。
- 单次新执行Node30、工作台及产品web JS语法、Python AST38、新Go测试gofmt、repack --check。没有本批真实浏览器/VM或独立ASGI2.3 companion；Node不代替浏览器复制/录音/排空验收，冻结网页字节保持不等于浏览器重新测试。
- .venv/系统无新依赖，freeze与前批相同，NumPy2.2.6不冒称requirements2.4.6。继承CPU集确实再次编译并加载微型C ABI故障库；无cargo/rustc/Torch/Qwen/CUDA、Rust编译/运行、真训练、真实音频播放或提速测量。

## 6. 完整性、建议处置和交接

- 批前保存953份历史SHA；原53源/94冻结/15正式工作台、原17包及先前收据保持。产品diff为空，不生成18包。
- coverage以逐文件SHA/行数核对新增10/2110，48/53/11030，剩5份2638；前两遍不改。未全三遍，不提前签收G0。
- 原300本批7部分链接：R1-048/083、R2-050/053/084、R3-008/066；累计去重38个ID。链接含本批与明确重新执行的旧Go合同，不冒充7个新发现；原文、Q25–27各50项保持，逐条/最终处置均false。
- 独立`verify_pass3_gateway.py`验证历史SHA/冻结、逐文件信用、Go JSON事件与ID继承、两新观察、F02预期race、vet、426项CPU逐项继承、探针/CLI、环境/manifest、原建议及全部交接嵌入。
- 完整交接86份备忘录逐份匹配，PLAN/IMPLEMENTATION与最新状态同步。manifest排除自身/可变handoff与progress，后者由独立核验另验，避免循环哈希。

主要收据：`docs/validation/step18/pass3-gateway-round1..3.json`、`pass3-gateway-cpu-round1..3.json`、`pass3-gateway-companions-round1..3.json`、`g0-pass3-gateway-{coverage,findings}.json`、`pass3-gateway-recommendation-links.json`、`pass3-gateway-run-manifest.json`、`progress-pass3-gateway.json`。最终封存以独立核验成功日志为准。

## 7. 下一步精确行动（待实施）

1. 全文复读web三资产2217行，分段读app.js不得以语法检查代替语义阅读。
2. 在SHA匹配fixture环境重新跑真实浏览器录音/取消/复制/排空/迟到响应合同，不挪用历史成绩。
3. 对F39明确原文展示/模型分组分层政策，构建纯标点/纯空白/尾段/即时首句组合合同；不得无依据加读字符。
4. 对F40明确ctx取消、worker cancelled、failed和正常终端的优先级与错误语义，避免重试已消费声音。
5. 继续保留F02/F03/F23/F24/F29/F30等旧缺口，修复时不能因本批其他保护通过而删除观察。
6. 保留第一可用DeepSeek前缀立即发worker请求的原保护；实际首可用人声仍需模型/浏览器测量。
7. 保留相同seed/pin与generated-only路径，不用合成stats或参考PCM证明双GPU等效音色。
8. 全文复读LICENSE/MEMO 421行并分别记录许可/技术限制；完成53资产也不自动完成原300逐条最终映射。
9. 原300和Q25–27建议按实际发现闭环，重大设计选择才开下一问题，不为编号制造问题。
10. 全部G0门禁通过后才进入S1，保持原17/正式工作台冻结，不提前发布18。
11. 真训练、长录音/完整数据覆盖、双T4、相似度、自然连续声音和无沙沙等用户要求继续列缺口。
12. 真实首声/建档延迟/RTF0.3须在固定条件下三轮真实模型和听感验收，当前不承诺结果。

**结论：第三遍阅读与Go边界核验推进；F39/F40未修，F02等旧缺陷保留。G0与整体仍PARTIAL/BLOCKED，非全功能或声学签收。直接继续下一批，无需Continue。**

---

## 内嵌备忘录：KAGGLE_STEP18_G0_PASS3_FRONTEND.md

# G0 全源第三遍第7批：web、录音生命周期与播放／界面状态

日期：2026-10-23；分支 `arena/1160bd87-kagglee`。

**第三遍累计51/53份、13247行，剩2份421行。前两遍各53/53份、13668行保持。产品未改；G0与整体仍PARTIAL/BLOCKED。** 本报告仅在三轮与独立核验完成后封存；全文阅读、功能修复、原300最终处置、声学与发布验收分别计算。

## 1. 重新全文复读3份2217行

| kaggle/source/web/文件 | 行数 | 重点 |
|---|---:|---|
| app.js | 1715 | 帧解析、Worklet/ring/player、重采样/缓冲/排空、access/turn/diagnostic/library epoch、录音与档案、快照非训练、UI私密内容清理 |
| index.html | 144 | UTF-8、默认锁定、自命名/不预填、两个主视图、键盘/移动端、录音/参考/训练明确区分、隐私与未验收提示 |
| recorder.js | 358 | 权限/AudioContext异步边界、会话归属、字节/时长/分块预算、最终File、停止/取消/设备结束/回调清理 |
| **合计** | **2217** | **3份完整读完** |

app连续1–350/351–700/701–1050/1051–1400/1401–1715，recorder连续1–180/181–358。初始HTML与recorder合并输出截断，单独HTML输出也截断，最终index连续1–40/41–90/91–144全部无截断补读后才计信用。辅助测试阅读不是源资产信用。11030+2217=13247，13668−13247=421；剩LICENSE201/MEMO220，没有自动标已读，更不将许可阅读冒法律签收。

## 2. 新增12项浏览器合同：10保护＋2未修观察

`tests/browser/pass3-frontend.spec.js`在实际Chromium执行完整冻结脚本，不修改产品或旧fixture。新录音／音频／fetch／Worklet状态／时钟为明确控制替身；剪贴板通过真实原生API及临时E2E工作台执行。原146项含真实Web Audio/MediaRecorder的振荡器／静音输入案例，但没有物理麦克风或扬声器验收。

| 新保护 | 结果与边界 |
|---|---|
| cancel与AudioContext.resume交错 | 原录音器在resume等待中cancel，晚resume不安装录音；ctx关闭、track stopped、session空、clip0；音频设备为fixture |
| 精确预算与File字节 | 5字节/2块/1500ms恰好边界接受，空块忽略，原File内容[0,255,1,2,3]逐字节一致，chunks清空；这是合成字节，不是有效原生录音容器 |
| MediaRecorder.start异常 | 原catch清本次context/track/session，回idle、clip0；start抛错由fixture注入 |
| 取消后的迟到权限拒绝 | 不覆盖取消提示，不建context、不留pending；新录音测试页明确UTF-8，原产品不变 |
| 当前policy帧 | 原完整播放器实际接收policy，网络EOF前按新阈值发play；不是首声／RTF测量或策略优化 |
| 当前HTTP401 | 原apiFetch立即锁定／abort，清text/key/err、不把私密错误JSON回填页面，无PCM/report |
| 超32MiB帧头 | 原浏览器parser先拒绝，不向player发PCM，恢复发送按钮；不签收F05读流取消或异常report语义 |
| 正常完成后排空 | 0.2秒合成PCM＋受控worklet状态／时钟，从playing到ended，无新增play；不代表≤50ms短尾已解决，也不修F26报告过早 |
| 三web资产原生剪贴板 | 临时工作台导入三份完整冻结文本，切换选中文件、读代码及原生clipboard逐字一致，复制不额外保存、项目revision与files不变；不是正式HEAD写入或18包复制验收 |
| chat历史上限 | 10个合成回合逐轮检查请求只带最近六个完整user/assistant对，无错序或过期历史；不调用真实DeepSeek |

### 首错保留与修正

首次新预检11通过、1失败，唯一差异是取消提示中文变成乱码：旧recorder-only测试HTML没有charset，脚本继承legacy文档编码；真实产品index已有UTF-8声明。仅在新审计spec增加UTF-8录音测试壳并重载原recorder，保留原断言／旧fixture／产品字节，随后12/12通过。`pass3-frontend-precheck-first.json`、stderr、`precheck-correction.json`与`precheck-final.json`均保存，不以产品修改掩盖测试环境错误。

## 3. F41：停止后迟到Worklet统计可重新发play（未修）

实际完整浏览器脚本执行显式停止：请求signal已abort，原player发hold、reset并显示idle。随后注入一个“reset前已产生、但晚到主线程”的合成st：fill240000、underruns1、starved=true。原onWorklet先切starved，tick又按旧fill满足阈值发play、UI显示playing，命令尾部为hold→reset→play；请求仍为aborted。

确认的是**迟到状态缺少流世代／停止状态门禁，可以改变原UI和命令序列**。AudioWorkletNode、st与设备均为fixture，**没有证明真实原生port必然发生该竞态、旧PCM实际恢复、物理漏音或模型继续生成**。未来需把stop/reset/begin与状态消息关联，同时保留真实ring reset精确零输出保护，不能只隐藏UI状态。

## 4. F42：同accessEpoch乱序档案刷新会回滚高亮（未修）

原候选按钮按0→1点击，各自成功后调用原v刷新。两个受控profiles请求处于同accessEpoch：先回复较新的snapshot1，页面高亮#1；后回复旧snapshot0，原v再次重绘并高亮#0。测试直接检查mutation=[0,1]与可见高亮先1后0。

确认的是**只有accessEpoch、没有当前刷新／操作顺序门禁**；不是实际后端参考回滚或错误音色证明，responses都是合成快照。声音库dialog的独立libraryEpoch与训练输入保护仍存在且重跑通过，不能混为已修。未来需统一“最新操作”与刷新结果归属，而非移除原access/turn/library隔离。

## 5. 三轮执行与证据边界

| 实际集合 | 第1轮 | 第2轮 | 第3轮 |
|---|---:|---:|---:|
| Chromium全部浏览器测试 | 158 PASS | 158 PASS | 158 PASS |
| 其中继承／本批新增 | 146／12 | 146／12 | 146／12 |
| 浏览器失败／flaky／skip | 0／0／0 | 0／0／0 | 0／0／0 |
| 完整继承CPU集合 | 426 PASS | 426 PASS | 426 PASS |
| CPU failure／error／skip | 0／0／0 | 0／0／0 | 0／0／0 |
| 原播放器VM合同 | 22 | 22 | 22 |
| 原首声策略VM合同 | 16 | 16 | 16 |
| 独立NumPy分块／trimmer | 12／8 | 12／8 | 12／8 |
| 实际CLI期望合同 | 4 | 4 | 4 |

浏览器 **158×3＝474 PASS**、CPU **426×3＝1278 PASS**。每轮12新合同中10保护／2观察，三轮分别30／6次；本批无新Python合同。浏览器146项按file+title逐项与旧批核对，CPU426项按测试ID／结果与前批逐项核对，不用总数冒完整继承；重试0。

- 实际重跑的旧浏览器合同包含原生录音振荡器／静音、权限／设备结束、长虚拟录音与分块预算、锁定／迟到HTTP、库管理／训练快照、移动端／键盘／XSS，以及完整17包原生剪贴板、拒绝回退。冻结正式工作台15文件另以SHA核对；临时E2E workspace不是用户正式HEAD。
- 七份浏览器观察附件包含F04/05/06/25/26及新F41/42，每轮均可见；“观察通过”不等于修复。F04旧录音错误、F05读流未取消、F06失败Blob URL、F25 END后帧、F26报告在EOF过早等均保留。
- VM确实执行冻结播放器prefix/ring源码，仍记录≤50ms尾缓冲可能搁置、插值尾端未flush等已知观察；VM不是硬件，不能因此称声学排空、首声或去沙沙已通过。
- 每轮三项CLI预期exit2/blocked，resource status exit0但gpu_verified=false；没有--run benchmark或WAV生成。NumPy分块差异实验完成也不等于算法容差通过。
- Node30、工作台／产品／新spec的JS语法、Python AST38、repack单次新执行。无本批Go/race/vet或独立ASGI2.3 companion，不挪用上批93/109／F02结果。浏览器API为fixture，不是真Go后端链路。
- 沿用既有npm／Chromium分发与.venv；无npm ci／新Python或系统依赖安装，lock与freeze保持。NumPy2.2.6不是requirements2.4.6；继承CPU集合再次运行C ABI故障fixture，不是Rust编译／执行。无Torch/Qwen/CUDA、真训练、双T4、真实声纹／听感或提速验证。

## 6. 完整性、原建议与交接

1051份历史SHA、53源／94冻结／15正式工作台文件保持，产品diff为空。`advance_pass3_frontend.py`逐资产SHA／行数核对，信用51/53/13247，剩2份421，不提前签收全三遍。

原300本批7项仅部分链接：R1-038、R2-082/083、R3-044/046/083/085，累计去重45个ID；其中剪贴板失败回退明确链接实际重跑的旧浏览器合同，不冒称本批新增。原文／Q25–27各50项保持，逐条测试及最终处置均false。本批未开新重大方案题，不跳Q28。

独立`verify_pass3_frontend.py`递归解析原始Playwright JSON、核对158逐项状态／重试／146继承、7观察、VM、426CPU继承、probe/CLI、源码／环境／manifest、原建议与交接。完整交接87份逐份内嵌匹配，PLAN／IMPLEMENTATION与最新进度同步。manifest排除自身和可变handoff／progress，由核验器另验避免循环。

主要收据：`docs/validation/step18/pass3-frontend-audit-round1..3.json`、`pass3-frontend-browser-round1..3.json`、`pass3-frontend-cpu-round1..3.json`、`g0-pass3-frontend-{coverage,findings}.json`、`pass3-frontend-recommendation-links.json`、`pass3-frontend-run-manifest.json`、`progress-pass3-frontend.json`。终态以独立核验成功日志为准。

## 7. 后续精准动作（待实施，不冒充修复）

1. 完整复读剩LICENSE201与MEMO220，按技术／许可分别列限制，法律问题不由测试涂绿。
2. 完成53资产第三遍后，仍逐条闭合原300建议最终映射及测试证据，而非自动签收G0。
3. 为F41设计流世代／停机门禁及真实原生Worklet跨方向消息交错实验，区分命令、处理与物理出声。
4. 保留ring reset精确零输出、显式取消和新流begin清相位，防修迟到状态时造成旧数据重播。
5. 为F42设计最新操作／刷新版本，保留access/turn/library/diagnostic epoch及AbortController。
6. 单独处理F04旧录音error与现session归属，保留晚data/stop/track-ended不能影响新session的现有保护。
7. 单独处理F05/06异常读流与Blob资源清理，不能通过“catch不报错”遮蔽仍运行的后台请求。
8. 统一END终端／后续帧、EOF／播放排空与最终report生命周期，F25/26及短尾政策仍待修。
9. 继续区分自命名空库、参考处理、训练输入、真实训练、trained加载与声学验收，不增加伪训练绿标。
10. G0通过后才进入S1，保持冻结17和正式工作台，不提前生成18发布包。
11. 长录音／长数据真实训练、双GPU等效参数、generated-only、首可用前缀、输出音量／创建时延等未豁免要求继续保留。
12. 真实首可用人声、无沙沙／自然连续朗读／相似度／RTF≤0.3须真实音频和双T4三轮验证，当前不承诺结果。

**结论：web语义阅读与真实浏览器边界核验推进，F41/F42未修；非完整模型、全功能或声学签收。G0与整体仍PARTIAL/BLOCKED，直接继续，无需Continue。**

---

## 内嵌备忘录：KAGGLE_STEP18_G0_PASS3_CLOSURE.md

# G0 全源第三遍第8批：许可／历史备忘录收尾与300项缺口矩阵

日期：2026-10-23；活动分支 `arena/1160bd87-kagglee`。

**53份内嵌资产三遍全文语义阅读已完成，每遍53/53、13668行。本批2份421行。只关闭源码阅读子项，不代表所有Git文件、原300项最终处置、功能、法律或声学验收。G0与整体仍PARTIAL/BLOCKED。**

## 1. 最后2份完整复读及覆盖信用

- `kaggle/source/LICENSE-QWEN-DERIVED.txt`：连续1–105、106–201，201行；无工具截断。
- `kaggle/source/MEMO.md`：连续1–110、111–220，220行；无工具截断。
- 13247+421=13668，51+2=53，剩0。只变更这两项pass3记录，pass1/pass2与前51项pass3不动，逐文件SHA／行数均核对。
- 当前范围是冻结17启动包所含53资产，不是整个仓库所有源码、文档、测试、历史包的三遍逐行审查。三遍阅读也不证明零缺陷。
- `g0-pass3-closure-coverage.json`是新台账；第7批及更早覆盖JSON保留，不回写历史“未完成”。

## 2. LICENSE：文本阅读完成，法律发布未签收

这是Apache License Version2.0/January2004文本，末尾Copyright2026 Alibaba Cloud。以下是工程发布检查清单，不是所有组件可商用／授权完备的法律结论：

1. 第1节定义Source/Object/Derivative Works/Contribution等；接口链接分离条款不能由一次文本扫描推导整个工程的法律关系。
2. 第2节版权授权适用于其覆盖的Work与Contributor，不自动证明所有依赖、模型权重、训练数据和声音授权。
3. 第3节专利授权范围及相关专利诉讼终止条件单独核对。
4. 第4(a)节分发许可副本；第4(b)节修改文件的显著变更声明；第4(c)节保留相关来源署名等通知。
5. 第4(d)节在上游分发含NOTICE时，按许可允许的位置保留适用署名。当前53资产没有名为NOTICE的项，不证明上游无NOTICE义务，也不直接判当前侵权。
6. 第5节贡献默认许可与独立协议；第6节不授予一般商标使用权。
7. 第7–9节AS IS、责任限制、额外担保由自己承担，不可转写成软件正确／身份一致／无噪声保证。
8. 附录版权行是现有文本，不是逐文件派生来源或许可一致性已鉴定的证据。
9. 待发布时按实际上游版本、派生文件、依赖与模型逐项核对LICENSE/NOTICE/修改声明，另核授权语音与隐私，不混入声学评分。
10. 本批不改冻结许可、不新建虚假NOTICE、不声称已完成法律或模型权重许可审查。

## 3. MEMO：既有D01保留，不改历史

顶部标题仍称step15优先，3–5行称当前step15、xvec_only=True且不能回退ICL；8行称最大增益12dB。冻结17实际：

- `clone_stream.conditioning`默认QTTS_CLONE_MODE=icl，要求匹配转写；显式xvector返回空转写/True，非法模式拒绝。
- `worker.output_max_gain_db`默认6dB；12是可配置上限，13或NaN回落6，不把“上限12”误判为“12已删除”。
- 本批通过只抽取原函数体的AST测试实际调用这些默认／显式／拒绝路径，不导入整个worker、不加载NumPy/Torch/Qwen/GPU，不证明当前用户实际环境变量／音色／音量。
- 旧文中step14允许reference呼吸、早期239秒／64MiB预算、早期未实现训练按钮、step10训练核心等均为不同历史阶段。旧文自己已说明历史分节，并反复限制真实Qwen/T4验收；不能跨节拼成当前功能承诺。
- 第17阶段代码优先，MEMO SHA保持；D01既有文档漂移不重新编号为新产品bug。未来18文档应另写当前事实，不覆写历史制造一致。

## 4. 原300项：重新逐项复核与缺口矩阵

本批完整重读R1-001..100、R2-001..100、R3-001..100的原建议和初始分类／工作包。它是对原三轮各100建议的继续复核，不新增300个缺陷或重写旧建议。

| 原始初审类别（保持） | 条数 |
|---|---:|
| 限定范围确认缺陷建议 | 23 |
| 保留保护 | 96 |
| 文档／测试合同 | 89 |
| 真实硬件／模型阻塞 | 55 |
| 待证 | 37 |
| 合计 | 300 |

23条建议有重复，不是当前缺陷总数，也没有自动改为已修。`g0-pass3-closure-recommendation-gaps.json`保存每一条原ID／原文／source／分类／工作包／test_family／计划合同／原证据，增加：

- 原三遍专用链接文件及SHA、准确row_index、合同标题、覆盖边界；7文件53条链接记录，去重45个原建议ID。
- 45条仅有部分第三遍链接；255条未进入这组专用链接，**不等于没有任何历史证据**。
- 每行下一动作保留其原source、工作包、原建议和所需测试合同，要求精确测试ID、源码／探针SHA、执行结果与注入／硬件边界；不能用大类测试数替代逐条映射。
- 300条specific_row_test_signoff、final_disposition_signed_off、product_fix_implemented保持false；最终签收0，未闭环300。
- 工作包计数汇总以真实原字段计算，不靠关键词生成假缺陷／伪造已执行测试；原300 JSON与Q25–27各50建议SHA保持。

## 5. D02：三份历史日志目前不可读，禁止冒充全部历史完整

本批拟检查1139份历史路径／预期SHA：**1136份可读取且SHA匹配，变更0；另3份缺失**：

- `docs/validation/step18/pass2-gateway-go-install.log`
- `docs/validation/step18/pass2-gateway-preflight.log`
- `docs/validation/step18/pass2-startup-preflight.log`

三份均匹配仓库既有`*.log`忽略规则；这里只确认当前缺失与忽略规则匹配，不推断确切丢失时间或过程。预期SHA仍保存在新旧preserved JSON，不重建虚构内容，不删掉期待项来让完整性涂绿。

因此full_historical_integrity_passed=false，D02是审计证据可用性缺口，不是新产品缺陷。当前工作区可读的冻结53资产／94文件／正式15文件与正式HEAD均保持。前批“当时1051全通过”的历史收据不被改写，但不能当作现在全部文件仍在的证明。新日志均使用.txt，不复用这些缺失路径。

第一次环境查询发现旧.venv和猜测的LICENSE路径不存在；转用系统Python及台账给出的准确文件名。随后首次严格历史检查因缺第一份.log停止、未写错误的“全完整”声明；全面盘点才登记上述三份。两次先期错误及处理均在`pass3-closure-precheck-observations.json`留档。

## 6. 本批实际执行范围

三轮实际完成（每项原始日志与SHA分别留存）：

| 本批新执行 | 第1轮 | 第2轮 | 第3轮 |
|---|---:|---:|---:|
| 收尾审计合同 | 12 PASS | 12 PASS | 12 PASS |
| Node工作台测试 | 30 PASS | 30 PASS | 30 PASS |
| 工作台／web／原浏览器spec JS语法 | PASS | PASS | PASS |
| 冻结17 repack --check | PASS | PASS | PASS |
| Python AST | 38文件 | 38文件 | 38文件 |

审计12×3＝36 PASS，Node30×3＝90 PASS，均无失败／错误／跳过。预检12/12首次通过。AST38为33份产品Python加5份本批测试／脚本，未导入完整运行时。

新`test_pass3_closure_contracts.py`有12个审计合同：覆盖与精确增量、分支／冻结／正式工作台、原300身份、分类／去重、链接出处、下一动作与不自动签收、许可边界、原conditioning AST、原增益AST、缺失历史明确暴露、旧浏览器原始JSON可读性、既有逐题50行动完整性。

第10项合同通过只表示准确报告1136匹配+3缺失，不表示1139完整；第11项只重新解析上批158×3原始Playwright收据，不是浏览器新执行。原浏览器每项只一次passed与SHA重核，不能用来签新产品。

本批没有.venv/node_modules/Go/Rust工具链；不安装新依赖，不跑完整CPU426、Chromium、Go/race/vet、Torch/Qwen、真实训练／双T4／物理录音／扬声器、真实DeepSeek或声学／性能实验。未执行项不算通过。无新功能修复，无18包；新的审计／工作台检查不能代替用户要求的最终全功能／真实模型三轮验证。

## 7. 门禁状态与直接后续

| 子项 | 当前结论 |
|---|---|
| 53内嵌资产三遍全文阅读 | 完成，各13668行 |
| 原300逐条最终处置／测试签收 | 仍未闭环，0/300最终签收 |
| 历史证据全量可用性 | 阻塞，D02三份缺失日志 |
| 限定缺陷修复及相同输入前后见证 | 未完成，F01–42及先前DSP／播放器等观察保留 |
| LICENSE/NOTICE/模型与数据授权 | 未签收 |
| 真实模型／双T4训练／听感／首声／RTF | 未验收 |
| G0／整体 | PARTIAL/BLOCKED |
| S1／Q28／18发布 | 未开始／未开启／未发布 |

下一步先补原300逐条“最终审查处置”（与产品修复验收分开），将可由现存证据判定的保留／缺陷／待证／真实条件阻塞明确归档；对D02从原始可信来源找回日志或在有依赖环境按原命令另存新收据，不能伪称重建了旧内容。随后按原建议精确测试ID逐行闭合，不用又一轮总数回归替代映射。G0通过前不跳S1或Q28。

## 8. 交接与独立核验

本报告、PLAN、IMPLEMENTATION同步进入88份完整交接；旧57份与本阶段已完成文件逐份原文内嵌。独立`verify_pass3_closure.py`用系统Python标准库再核对覆盖、冻结／正式文件、1139期待项的1136匹配+3缺失、300身份／53链接记录、三轮真实日志、环境边界、manifest及交接。

主要文件：`g0-pass3-closure-{coverage,recommendation-gaps,boundaries}.json`、`pass3-closure-history-availability.json`、`pass3-closure-audit-round1..3.json`、`pass3-closure-run-manifest.json`、`progress-pass3-closure.json`。审计核验通过只签本批记录准确，full_historical_integrity、G0、功能／法律／声学／发布仍false。

**继续直接推进，不要求Continue。源码阅读子项完成；不把阅读、部分证据、历史成功或缺陷观察当作修复和整体验收。**

---

## 内嵌备忘录：KAGGLE_STEP18_G0_DISPOSITION_REVIEW.md

# G0第9批：300项审查处置记录与限定失败观察映射

日期2026-10-23，分支 `arena/1160bd87-kagglee`。

**本批将300/300条审查处置说明归档，23条原限定缺陷建议绑定到历史三轮的69份逐行观察引用；不是23个新缺陷或69次新运行。功能验收／原final_disposition签收仍0/300；G0与整体PARTIAL/BLOCKED。** 产品、原始至17及正式工作台冻结，不启动S1/Q28或18发布。

## 1. 处置说明和最终验收分开

原3轮各100条逐条补写source相应的行动、限制和推荐处理，不自动用关键词生成结论。三个TSV各100条，当前JSON保存原ID／原文／source／工作包／原计划合同、单独review_note与行动。本文附录完整内嵌300条原建议及本批说明。

| 推荐处置 | 数量 | 不代表 |
|---|---:|---|
| 限定范围修复 | 23 | 不代表23独立bug或已修 |
| 保留不变量 | 96 | 不代表该保护已逐条功能签收 |
| 实现文档／测试合同 | 89 | 不代表只改文案即可验收 |
| 等真实硬件／模型证据 | 55 | 不代表豁免或删除用户要求 |
| 先调查再设计 | 37 | 不代表猜测已证实 |

review_disposition_recorded=true仅表示本批处置说明已记录。原specific_row_test_signoff／final_disposition_signed_off／product_fix_implemented及新functional_acceptance全部false，旧300与第8批矩阵不回写。不能用新的字段名把旧功能门禁涂绿。

## 2. 23条限定失败观察精确绑定

`disposition-failure-bindings.json`按原建议ID手工选择历史收据及JSON Pointer，存观察片段、收据SHA、产品源码SHA、当前相关probe SHA与历史记录能否证明probe身份。每条绑定三轮，共69引用；这些引用有重复，不能当作69独立实验。

- R1-011、R2-021/022/024：候选bool、1.9及null/dict/list的AST观察。缺省语义与容器异常分别保存；NaN不在历史payload快照中，不冒充已覆盖真实HTTP NaN。
- R1-016、R2-031/032/033：旧评分提交到新转写的确定性交错。R1-016仅为相关校准／文本证据，不覆盖完整set_text/set_candidate并发组合，也不是线程压力。
- R2-041/043/051/061：ASR缺失却CER0.05、全合成失败chosen0、同文诊断seed100/101、reload失败仍正常返回的历史观察。模型与网络为fixture。
- R1-071/072、R3-011/012：NumPy分块最大差1424与正常1920块差8等合成观察；该早期DSP JSON没有probe_sha256，当前相关probe的SHA不能补成历史身份已验证。不是Rust、真实音频、用户沙沙根因。
- R3-021/022/024：小于120样本丢输出、跨块预滚差840、末端held含60非零样本。当前codec1920倍数的生产可达性另列，不声称真实辅音已丢。
- R1-037、R3-041/042/043：原Player VM在完成20/50ms短尾仍buffering/starved、51ms可发play。合成PCM／时钟／端口不是实际用户语音／实体播放。

本批重新读取这些已保存JSON并逐Pointer核对，不导入重型模型重跑旧实验。观察测试的通过不等于行为正确，绑定也不是整条功能验收。

## 3. 部分证据覆盖：并集65，不是签收65

第8批原第三遍专用链接45个建议ID，与本批23限定缺陷建议交集只有R1-016/R2-031/R2-032三项，所以45+23−3=65；剩235条没有进入这两组限定引用。235不等于无任何历史证据，也不能直接签成失败。需继续按每行计划合同核对准确test ID、输入版本和覆盖边界。

当前53内嵌资产三遍各53/53、13668行的阅读结果保持。这不是整个Git仓库所有文件，也不证明代码无错。300条建议与F01–42命名发现不是一一对应关系。

## 4. D02可信恢复搜索

仅对当前仓库中非.git、文件大小≤2,000,000字节的可读文件比较三份缺失日志的预期SHA，并对每个原路径执行git log --all。没有同SHA副本，当前可用Git历史无提交记录；未搜索远端、仓库外备份或不可用提交，不能声称全球无副本。

三份仍缺失：pass2-gateway-go-install.log、pass2-gateway-preflight.log、pass2-startup-preflight.log。新preserved共有1183个历史期待项，1180可读SHA匹配，变更0，缺失3；完整历史完整性false。保留预期SHA，不伪造内容、不把重跑输出命名成找回旧日志。

后续只能从可信旧状态找回并验证SHA，或有依赖环境后按原命令另存带新身份的收据；后者解决可复现性但不冒充原文件恢复。搜索范围／命令／结果在disposition-history-recovery.json留档。

## 5. 本批验证范围

三轮本批新执行已完成：

| 实际新执行集合 | 第1轮 | 第2轮 | 第3轮 |
|---|---:|---:|---:|
| 审计合同（继承12＋新增12） | 24 PASS | 24 PASS | 24 PASS |
| Node工作台测试 | 30 PASS | 30 PASS | 30 PASS |
| 工作台／web／旧浏览器spec JS语法 | PASS | PASS | PASS |
| 冻结17 repack --check | PASS | PASS | PASS |
| Python AST | 39文件 | 39文件 | 39文件 |

审计24×3＝72 PASS，Node30×3＝90 PASS，无失败／错误／跳过；新12预检首次通过。AST39为33份产品Python与6份当前脚本／测试；没有执行GPU／完整worker导入。历史实验仅核读，不以这些72个审计通过替代功能验收。

测试包含原第8批12项收尾合同及新12项处置／Pointer合同，使用系统Python标准库；其中旧conditioning/gain AST原函数仍真实调用，但不是完整CPU426。新合同覆盖300身份与300条手写说明、分类及65并集、23/69逐行引用、payload类型、校准/seed、DSP/短尾/裁剪边界、不自动验收、D02不伪恢复。

没有旧venv/node_modules，不安装依赖；未运行CPU426／Chromium／Go race/vet／Rust／Torch/Qwen／GPU／真实训练／DeepSeek／物理麦克风或扬声器／真实声学及速度实验。旧浏览器158×3和CPU426×3仍是历史。没有新增产品修复，法律/NOTICE/权重与语音授权未签收。

## 6. 下一精确门禁

1. 对未完整绑定的合同按行匹配实际测试ID，不再用总测试数作逐条验收。优先S1非法输入与缺省/未知/重复字段政策；R2-024另补真实HTTP NaN解析、null/容器返回码。
2. 对R1-016补完整候选/文本并发组合，S2提交政策必须保留trained409、pin与双卡部分加载语义。
3. 已绑定23条保留相同输入修复前失败与修复后通过，不用另一个更容易样例替换原反例。
4. 扩大候选、DSP、短尾等真实证据前，先逐项保留现有成功保护；不以新指标绕过取消／隐私／生成码专用。
5. D02恢复保持独立阻塞；无环境不虚构旧Go安装/预检重跑。
6. 300处置说明归档不等于G0放行；新决策只在重大设计歧义出现时按既有逐题50行动流程开启，不为了数量开Q28。
7. 真双T4训练、长数据覆盖、全部参考贡献透明、实际首声／输出音量／创建时延／无沙沙／自然朗读／RTF0.3继续未豁免。

## 7. 封存与交接

独立verify_disposition.py核对原300身份、300处置说明、69Pointer／SHA／缺失probe身份、65并集、1183历史期待项、三轮真实审计日志、冻结94及正式15、manifest和89份完整内嵌交接。核验成功只表示本批记录准确，不表示历史全完整或G0通过。

当前主JSON：g0-disposition-review.json；限定引用：disposition-failure-bindings.json；进度：progress-disposition.json。原推荐及Q25–27各50建议保持，不覆盖任何历史审查报告。继续直接操作，无需Continue。

## 附录：三轮各100条完整处置记录

### 原审查第1轮100条

| ID | 原建议 | 本批逐条处置说明 |
|---|---|---|
| S18-R1-001 | 将候选参与质心统计与实际ICL锚点分开显示，避免全部片段已融合的误解 | 在S7分别展示分析参与与实际conditioning；不把质心改名为融合。 |
| S18-R1-002 | 在合成收据记录选中的anchor_candidate，而不是只显示profile ID | 新增实际anchor_candidate收据；缺失时显示未知而非默认0。 |
| S18-R1-003 | 记录实际锚点字节指纹与对应转写指纹；日志不明文写入私有转写 | 仅记录锚点及转写hash；不把私人转写写入诊断日志。 |
| S18-R1-004 | 用不同内容的三个候选验证只选中的音频进入提示提取 | 三段不同转写用受控调用捕获选中锚点，再另做真实模型试验。 |
| S18-R1-005 | 审核“候选校准”文案明确逐个试验后选一个，不称多参考融合 | 候选校准文案写明逐个评估后选一个；不许以列表暗示融合。 |
| S18-R1-006 | 查验Faster真实接口的多参考能力，未支持时不伪造列表参数 | 沿用已检查接口的批量长度拒绝；模型融合能力仍需另证。 |
| S18-R1-007 | 禁止把三个片段PCM拼成一个提示并配不连续全文 | 保留禁止拼参考PCM与不连续全文的约束，测试中也不得绕过。 |
| S18-R1-008 | 跨候选声纹中心仅作评分依据，不声称它已替代模型speaker embedding | 声纹中心保持分析代理身份；不可直接替换不同空间模型嵌入。 |
| S18-R1-009 | 为单个合法候选保留最短建档链路，不强迫三候选 | 单候选仍走合法最短链路，加入不强迫三候选的回归。 |
| S18-R1-010 | 给未来多候选策略保留显式模式与回退边界，不静默改变17默认 | 未来策略另设模式和版本，不更改冻结17默认。 |
| S18-R1-011 | 非法index的布尔、小数、对象与缺省语义分别测试，避免int强转误选或500 | S1分别拒绝bool/float/容器并定义缺省；历史AST见证不是HTTP验收。 |
| S18-R1-012 | 核查切换候选与校准并发时磁盘写入、工作者加载是否形成一致事务 | 候选/校准写入与worker加载需要同版本提交；部分链接不等于事务完成。 |
| S18-R1-013 | 候选文件复制失败时保留旧profile JSON，不留下半更新锚点 | 保留旧JSON回滚保护，另检查复制成功后JSON失败的孤立文件。 |
| S18-R1-014 | 双卡仅一张加载成功时明确部分失败，不宣称启用完成 | 一张卡失败必须暴露部分失败；不能仅数成功worker。 |
| S18-R1-015 | 旧会话遇新指纹必须继续拒播，不能热切后拼混音色 | 保留旧会话pin不一致拒播，并覆盖热切途中后续片段。 |
| S18-R1-016 | 转写编辑与候选选择同时发生时绑定同一版本，防止音文错配 | 校准旧转写见证只相关覆盖；须补文本与候选同时提交的独立交错。 |
| S18-R1-017 | 校准临时profile的anchor_candidate元数据应指向实际试验候选，不能误标0 | 临时校准档案元数据随试验候选更新，不能依赖chosen默认值。 |
| S18-R1-018 | 候选变更后清理或替换提示快照时保留锁内核验 | 保留提示快照锁内核验，增加替换/删除交错而不解锁重载。 |
| S18-R1-019 | 为重复点击候选与取消任务增加幂等与状态测试 | 重复点击与取消分别定义操作身份及提交后状态，不称浏览器abort即撤销。 |
| S18-R1-020 | 训练adapter的固定参考限制保持，不让候选切换绕过来源绑定 | trained固定参考三入口拒绝继续保留，不能开放普通候选路径。 |
| S18-R1-021 | 分别记录请求、首个可用文本、排队、预填充、首PCM、首播放命令 | 指标阶段拆分并保留旧字段含义，未实测阶段使用null。 |
| S18-R1-022 | worker t_start在加载提示之后，单独计量冷提示加载而不漏记等待 | 把冷提示提取计入独立阶段，避免t_start以后才计时漏掉准备。 |
| S18-R1-023 | queue_ms当前覆盖锁等待等前置耗时，拆项后保留旧字段兼容 | 兼容保留queue_ms，新增锁等待与准备耗时而不偷偷改分母。 |
| S18-R1-024 | 浏览器firstPlayedMs当前在发play命令处赋值，标明不是硬件实际出声 | 把firstPlayedMs定义为主线程命令时刻，不升级为实体首声。 |
| S18-R1-025 | 评估AudioWorklet消费首个语音样本的确认消息，区分主线程命令延迟 | 设计消费确认时先明确首样本还是首语音；不由消息时间推声卡出声。 |
| S18-R1-026 | 跨Python、Go与浏览器仅使用各自单调时间差，不能直接减不同纪元 | 各进程仅比较本地单调时间差，跨时钟采用可解释的映射。 |
| S18-R1-027 | 显式静音停顿不能计为首个可用人声，保留禁止原音占位 | 显式停顿不能充首人声，参考原音也不能作占位首包。 |
| S18-R1-028 | 首包平均之外记录p50/p95与冷暖状态，不用一次幸运值 | 冷暖分层重复采样再算p50/p95，当前无目标设备故保持阻塞。 |
| S18-R1-029 | 将文本长度、参考长度、chunk_size和设备条件写入性能收据 | 性能收据固定文本/参考/chunk/device参数，不能复用截图数值。 |
| S18-R1-030 | 首声提速必须同时检查缺字与最终音频完整性，不能裁掉开头 | 首声对照同时核对首尾完整和添字，不以裁掉语音换快。 |
| S18-R1-031 | 对当前0.7秒下限和初始2秒策略建立确定性到达轨迹对照 | 0.7秒/初始策略先以VM轨迹对照，不把策略仿真当真实提速。 |
| S18-R1-032 | 分别测试高速稳定、慢速持续、突发包与长网络抖动 | 补稳定/慢速/突发/抖动轨迹，记录欠载和等待成对结果。 |
| S18-R1-033 | 初次启动与欠载恢复分别设计目标，不统一缩到最小 | 初播与starved恢复分开策略；先覆盖终端短尾而非全局降阈值。 |
| S18-R1-034 | 将预测器无速率样本时的保守回退纳入首次播放测试 | 保留无估计样本的保守回退，并单测预测器初始化。 |
| S18-R1-035 | 测量AudioWorklet统计消息的刷新间隔对主线程启动判断的影响 | 测Worklet状态刷新间隔及消息晚到；fixture不能证明真实port竞态。 |
| S18-R1-036 | 在44.1k及48k上下文验证重采样后的fill计秒正确 | 按实际上下文率换算fill秒数，单测44.1k/48k边界。 |
| S18-R1-037 | 短于启动阈值但已完成的真实语音应及时播放，不等待不可达缓冲 | 20/50ms完成短尾见证为VM合成输入；修播放政策后另测真实语音。 |
| S18-R1-038 | 后台页、暂停恢复、锁定与取消后不得发送迟到play | F41仅覆盖stop后迟到统计；锁定/后台/暂停恢复仍要分别验证。 |
| S18-R1-039 | 记录ring dropped样本；任何丢样不能只显示播放成功 | dropped进入失败/完整性状态，不能只保留底层计数。 |
| S18-R1-040 | 低延迟策略只能在欠载预算内启用，不能把断续当自然阅读 | 低延迟与欠载预算联合门禁，真实连续朗读不合格即不能发布。 |
| S18-R1-041 | 对2/4/8/16帧首块大小做同文本同seed对照，测TTFA及总RTF | 16帧超出当前首块2..8配置范围；不得强塞无效参数，合法对照先做2/4/8。 |
| S18-R1-042 | 小首块与稳态大块若需不同大小，先确认真实生成器支持，禁止无效传参 | 首块/稳态分离须真实后端支持；禁止界面参数有值但生成器忽略。 |
| S18-R1-043 | 检查decode迭代器首次next含有的预填充时间，不能只测创建生成器 | 首次next的预填充必须实测，创建生成器用时不是首chunk。 |
| S18-R1-044 | 单独计量token生成、codec解码及CPU拷贝，避免归因全部GPU | 分离token/codec/拷贝时间，目标设备缺失不填估算GPU成绩。 |
| S18-R1-045 | 提示快照重用必须与内容指纹一致，不退回仅按路径缓存 | 保留内容pin缓存身份，路径相同但字节变化必须失效。 |
| S18-R1-046 | 不为首声把ICL换成向量默认，保留相似度条件 | 不为提速默认退向量模式，ICL条件和相似度门禁保持。 |
| S18-R1-047 | 比较首段优先调度与后续并行的队头阻塞，不无证据锁死单卡 | 首段优先与后段并行以真实排队分布比较，不凭单卡直觉重排。 |
| S18-R1-048 | 确认Live聊天第一可用前缀触发不被朗读聚合配置覆盖 | 保留聊天Live首可用前缀触发，朗读聚合不得覆盖该配置。 |
| S18-R1-049 | 保留最大生成token与取消限制，不能为速度删掉输出 | 生成token上限及取消保护保持，不能以少生成冒速度提升。 |
| S18-R1-050 | 不默认每卡双模型增加显存；只有目标T4实测才接受吞吐结论 | 每卡双模型只允许目标T4测量后讨论，不先改副本数。 |
| S18-R1-051 | 原始RMS约-47.7只作为风险，不推断具体麦克风故障 | 截图RMS仅提示输入轻，不当作麦克风或噪声根因诊断。 |
| S18-R1-052 | 分别记录归一化前后语音电平与峰值，注明增益上限14dB | 输入归一化14dB上限与输出默认6dB分开，避免两个增益概念混用。 |
| S18-R1-053 | 候选SNR是估计量，不能把17dB阈值当真实噪声声压 | 17dB估计门限不当真实SNR，报告算法与未校准限制。 |
| S18-R1-054 | 保留raw、strength0.85、strength0.55对照的处理收据 | 授权真WAV做raw/0.85/0.55并列对照，保留每次处理来源。 |
| S18-R1-055 | 审查声纹相似0.94与SNR增益2dB门禁是否会误接收失真，不能只看单分数 | 声纹/SNR门限与失真共同评估，无清洁真值不直接签听感。 |
| S18-R1-056 | 验证全零、强直流、很轻语音及背景声输入的处理决策 | 全零/DC/轻语音/背景分别测决策，不把拒绝样本都当降噪成功。 |
| S18-R1-057 | 对齿音、气声、摩擦音单独测保真，不能以削高频冒无沙沙 | 真实齿音/气声/摩擦音须盲听，不能只用频谱高频下降。 |
| S18-R1-058 | 不在用户未授权时保存或上传原始私有WAV作为公共证据 | 私有WAV不进公共仓库；收集需授权且默认关闭。 |
| S18-R1-059 | 已存在非平稳降噪不等于生成输出已降噪，明确处理发生阶段 | 说明降噪发生在参考分析，不暗示生成PCM已被消噪。 |
| S18-R1-060 | 录音时扬声器回录网页朗读的可能性仅列假设，不能由截图定论 | 扬声器回录只是待证假设，截图不足以确诊。 |
| S18-R1-061 | 建立模型PCM、后处理PCM、浏览器录回的分层局部诊断，默认关闭私有采集 | 分层PCM诊断默认私有且关闭，输出层级不能混成同一测量。 |
| S18-R1-062 | 将codec窗口起点与边界脉冲位置关联，区分底噪和接缝爆音 | 真实codec窗口偏移与脉冲位置对齐后才归因接缝。 |
| S18-R1-063 | 对持续人声与停顿分别计算频谱，但无清洁真值时不称绝对SNR | 无清洁真值只报相对度量，不给绝对SNR标签。 |
| S18-R1-064 | 继续验证codec只收到生成码，不能回到参考码前缀解码 | 保留生成码专用窗口，参考码从所有输出解码入口排除。 |
| S18-R1-065 | 真实预训练codec与随机tiny codec的质量证据必须分列 | 随机tiny codec只作控制流证据，不能替代预训练codec听感。 |
| S18-R1-066 | 非有限模型输出当前替换为零，应评估失败拒播而非掩盖异常的策略 | 非有限输出是待决失败策略，先保留见证而非擅自改零替换语义。 |
| S18-R1-067 | 增益提升可能抬噪，记录处理前后噪声地板变化而不自动强门限 | 增响同时量噪声地板，不能默认强门限掩盖抬噪。 |
| S18-R1-068 | 不能用输出全静音或静音段删除作为零噪声验收 | 全静音/删静音都不能签无沙沙或音质成功。 |
| S18-R1-069 | 保留模型自然人声呼吸与禁止添加噪声的区别，不自动切除语音气息 | 保留自然模型气息与禁后加参考噪声的区别，避免误删辅音。 |
| S18-R1-070 | 用户全程纯人声目标需真实WAV试听和添字检查，代码指标不替代 | 真实整段WAV对照添字/漏字与听感，当前无音频不能签纯人声。 |
| S18-R1-071 | 实测同一信号整块与任意分块处理的样本一致性 | 分块差异1424/8来自NumPy历史合成实验，不当用户噪声根因。 |
| S18-R1-072 | 重点验证NumPy不足96样本首块时淡入是否在下一块重新从零开始 | 不足96样本淡入重启应在S3修固定进度，保留整块及短块同输入见证。 |
| S18-R1-073 | 核查NumPy按输入块丢弃不足240样本RMS余数与Rust跨块累积差别 | 核查不足240样本RMS余数跨包累积，不能只比较输出长度。 |
| S18-R1-074 | 比较Rust逐样本增益平滑与NumPy逐块插值，不能宣称严格等价 | 先定Rust/NumPy算法差别与容差，不能以接口相同称等价。 |
| S18-R1-075 | 保持输出样本数与输入相等，不能为降噪补偿无记录延迟 | 保留输入输出样本预算；新增延迟必须单独记账。 |
| S18-R1-076 | 分别测试DC blocker状态、零输入残留与长静音后重新讲话 | DC残留、零输入与长静音后恢复分别测，flush问题不直接归声学根因。 |
| S18-R1-077 | 测试max_gain_db=0隔离淡入和DC滤波，再开放AGC定位差异 | 用max_gain0隔离淡入/DC，再逐步开放AGC定位。 |
| S18-R1-078 | 同卡每段重置与跨卡各自状态不同需测量，不能只凭相同目标响度称一致 | 同卡重置与跨卡独立DSP状态用真实音频测，不以同目标dB签一致。 |
| S18-R1-079 | flush的192样本衰减不是新生成语音，不能加入RTF语音分母 | flush192样本不算新语音时长，保持RTF分母真实。 |
| S18-R1-080 | 若修复NumPy算法须保留Rust接口版本兼容，并添加跨后端容差测试 | 修NumPy时保留Rust ABI兼容并明确降级，C fixture不是Rust执行。 |
| S18-R1-081 | 将独立模型韵律重启、显式停顿、播放欠载三种接缝分类计数 | 独立合成重启/规划停顿/播放欠载分三类记账，不一律叫沙沙。 |
| S18-R1-082 | 保留朗读12/24首段、20/40/80稳态配置基线再比较，不盲目扩大 | 先保留12/24及20/40/80历史配置基线，扩大段长须真声学对照。 |
| S18-R1-083 | 逐字验证分段重新连接等于原文，保护数字、缩写、引号和标点 | F39限定字词外标点尾段丢失；保留原文重连合同，不夸大成所有词漏读。 |
| S18-R1-084 | 审查PauseBeforeMs与tail_pause_ms是否重复加停顿，先画时序再修改 | 画PauseBefore与tail_pause时序，不能未经核对就删停顿。 |
| S18-R1-085 | 禁止跨词PCM重叠掩盖接缝，不牺牲清晰度冒自然度 | 不以跨词PCM重叠隐藏接缝，语义与清晰度优先。 |
| S18-R1-086 | 段尾8ms衰减及下段淡入需以有声边界实测，不只用零边界波形 | 8ms有声边界对照须真WAV，不用零边界单音替代。 |
| S18-R1-087 | 欠载时0.94尾衰减属于播放补偿，不能误标模型本身沙沙 | Worklet欠载补偿与模型底噪分开归因，0.94尾衰减不是模型结论。 |
| S18-R1-088 | 自然度对照必须同时保存整段朗读，不能只听裁剪后小片段 | 整段自然朗读盲听与局部片段同时保留，不能只挑好片段。 |
| S18-R1-089 | 不同GPU同文与交替长文分别试听；同seed不等于波形完全相同 | 同文双卡及交替长文两套测试，同seed不保证位级相同。 |
| S18-R1-090 | 只有真实模型支持的连续条件才能声称跨段联合生成，不换名称包装独立合成 | 无连续条件接口证据时保持独立段合成描述，不包装联合生成。 |
| S18-R1-091 | 冻结原始至17包、全部manifest及正式工作台，新增18不得覆盖历史包 | 冻结原始至17包与正式HEAD不动，18另建包及清单。 |
| S18-R1-092 | 三轮100建议均标已确认问题、待证假设或保留约束，不虚报300个bug | 保留问题/假设/约束三分法，300建议不是300已确认bug。 |
| S18-R1-093 | 完成三轮审查后再逐题决策，每题50建议后才进入下一题 | Q25–27各50行动保持；没有新重大方案不为计数开Q28。 |
| S18-R1-094 | 历史334测试不能算18新增验证，依赖缺失需如实记录和重建 | 当前无旧venv/node_modules，应记录缺依赖；历史334不是本批新执行。 |
| S18-R1-095 | 对每个修复保留修复前失败、修复后通过的同输入收据 | 修复前后必须相同输入，观察测试成功不等于故障修复。 |
| S18-R1-096 | 三轮Python、Node、Go race、协议和浏览器必须针对最终源码再执行 | 最终产品源码冻结后再完整三轮，当前审计/Node不能替代。 |
| S18-R1-097 | CPU合成信号实验不代替真实T4语音实验，硬件不足保持BLOCKED | CPU合成信号不能替代真实T4语音，硬件缺失保持BLOCKED。 |
| S18-R1-098 | 按实测热路径选择语言；不要新增Java/C#/SQL服务凑多语言 | 仅以热路径测量决定语言，不新增服务凑语言数量。 |
| S18-R1-099 | 最终18复制页、下载、剪贴板拒绝回退与手机逐字节校验不可省略 | 18未生成，当前17复制证据不能签18下载/剪贴板/手机完整性。 |
| S18-R1-100 | 将全部已完成备忘录内嵌完整提示词；未完成轮次必须明确，不编造结论 | 全部已完成memo内嵌交接；历史完成表述按当时范围解释。 |

### 原审查第2轮100条

| ID | 原建议 | 本批逐条处置说明 |
|---|---|---|
| S18-R2-001 | 保持qwen-tts-hf与旧qwen-tts发行版严格分离，源码同命名空间不等于同版本 | HF与旧发行版分离，不能因命名空间相同替换依赖。 |
| S18-R2-002 | 下载源码必须核对PyPI wheel SHA256，收据注明实际提供模型类的发行版 | 保留wheel SHA与发行版身份；缺缓存时只能核收据而非重跑模型接口。 |
| S18-R2-003 | 将三提示单目标被拒绝的实际接口行为加入未来多参考功能合同 | 三提示一目标拒绝作为接口边界，不构造未实现融合参数。 |
| S18-R2-004 | 将三提示三目标定义为独立批量任务，界面不能称参考融合 | 三提示三目标标独立批量任务，与一句融合明确分开。 |
| S18-R2-005 | 保留列表prompt每项独立ref_text，不用共享一条文字冒三候选匹配 | 保留逐prompt ref_text匹配，拒绝跨候选共享错误转写。 |
| S18-R2-006 | 字典prompt的批量ref_text共享行为应明确，不直接用于三段不同转写 | 字典批量共享文本限制须明示，不给不同音频拼全文。 |
| S18-R2-007 | 引用prompt item中ref_code与speaker embedding的区别，不能用声纹平均替代ICL | ref_code与speaker embedding分属不同角色，不由ECAPA均值替换。 |
| S18-R2-008 | 保持单ICL预计算提示的真实接口回归，不能为新模式破坏现有快照 | 单ICL快照接口保护保留，新增策略不可破坏。 |
| S18-R2-009 | 向量模式继续要求显式选择，不把它作为未实现融合的静默替代 | 向量模式只能显式选，不能作为未实现融合的静默成功回退。 |
| S18-R2-010 | 实际生成器、权重和声学结果未执行时，接口控制流通过不标模型实验通过 | 真实生成器/权重未跑，接口控制流不算完整模型实验。 |
| S18-R2-011 | 建立全部候选分析清单，逐项列源文件、时间、匹配转写、指纹和有效性 | 候选清单按来源/时间/转写/hash/有效性列出，不只显示编号。 |
| S18-R2-012 | 单锚点模式明确显示被用作ICL的候选及未用作ICL的其他候选 | UI明确实际单ICL锚点，其他候选分析贡献另列。 |
| S18-R2-013 | 若后续共享参数来自全部候选评分，记录算法与评分证据而非暗示音频融合 | 来自全部候选的评分需算法来源，不暗示全部音频进入Qwen。 |
| S18-R2-014 | 比较每候选合成时固定同文同seed同采样参数，确保差异确由候选造成 | 每候选固定同文同seed同采样再盲听，目前真实条件缺失。 |
| S18-R2-015 | 候选中心与实际Qwen说话人嵌入不同空间时不得直接替换 | 不同嵌入空间严禁直接平均替换，需同模型实验另证。 |
| S18-R2-016 | 实验性的融合嵌入若提出，必须独立模式且真实盲听，不自动作为最佳方案 | 任何融合必须独立实验模式，未验证不得设默认。 |
| S18-R2-017 | 不跨候选拼转写或参考码以绕过模型批量长度校验 | 不拼参考码或转写绕过批量长度约束。 |
| S18-R2-018 | 候选顺序变化时用内容身份而不只用数组下标定位证据 | 候选顺序变动以内容身份重定位，数组index不是永久证据ID。 |
| S18-R2-019 | 候选有效时长按实际WAV而非仅展示start/end计算，避免舍入差 | 用实际WAV帧数算时长，展示四舍五入不能作门禁。 |
| S18-R2-020 | 候选策略、模型模式及参数调整必须使旧会话明确失效 | 模式/策略/参数改变须使旧会话明确失效，不能混旧pin。 |
| S18-R2-021 | index必须严格整数且非bool，拒绝true变1与false变0 | S1 bool先于整数检查，true/false拒绝不能按1/0。 |
| S18-R2-022 | 拒绝1.9截断成1，避免非整数JSON静默切换其他参考 | 1.9拒绝而非int截断，保留已有合法整数行为。 |
| S18-R2-023 | 缺失index应明确拒绝还是显式兼容默认0，不让文档与行为矛盾 | 缺省index政策先显式定为受控合同，不在修bool时顺带猜兼容。 |
| S18-R2-024 | null、数组、对象及NaN输入转换失败应返回受控4xx而非未捕获异常 | 旧AST证实null/容器未捕获；NaN真实HTTP编码行为需另测，不扩张覆盖。 |
| S18-R2-025 | 候选入口未知字段与重复字段的策略需与严格library接口一致 | 未知/重复字段与library严格接口协调，勿只改一个入口。 |
| S18-R2-026 | 验证candidates为非空合法列表，不能只依赖len和下标访问 | 损坏candidates类型/空列表先拒绝，不只用len和下标。 |
| S18-R2-027 | 验证候选file为安全单文件名且普通文件，避免损坏profile路径越界 | 候选文件限定安全单文件名/普通文件，拒绝损坏路径与链接。 |
| S18-R2-028 | 手工ref_text不接受dict/list被str化，保留严格字符串与Unicode校验 | ref_text严格字符串/Unicode，dict/list不被str化接受。 |
| S18-R2-029 | 保留训练档案禁止改候选和转写的409边界，不绕过版本固定 | trained候选/文本409保护保持，来源绑定不能被新策略绕过。 |
| S18-R2-030 | 增加真正HTTP参数与错误码测试；当前AST调用不冒充FastAPI测试 | AST测试不是HTTP；补原ASGI状态码和返回体脱敏。 |
| S18-R2-031 | 校准开始捕获完整候选集合版本，提交时核对未变再采用评分 | 校准开始固定完整输入版本，提交重核后才能采用旧评分。 |
| S18-R2-032 | 禁止用旧候选评分选择重新读取后已更改的同下标候选 | 旧快照按候选内容身份提交，不把新同下标当原对象。 |
| S18-R2-033 | 校准期间并发编辑转写不能被结束时静默覆盖，需冲突响应 | 并发文本更新必须冲突而非旧结果覆盖；原AST见证不当线程压力。 |
| S18-R2-034 | 候选文件内容更改但文件名不变也要改变校准输入版本 | 文件名不变字节变化也进入版本核验，不能只比JSON时间。 |
| S18-R2-035 | 候选变更、文本变更、校准、删除应协调同一档案锁或乐观版本合同 | 候选/文本/校准/删除使用统一提交合同，不拿HEAVY当档案锁。 |
| S18-R2-036 | 进程内线程锁与跨进程文件锁分别评估，不能把一个称全局事务 | 线程锁与文件锁保护范围分别记录，不声称单进程锁全局事务。 |
| S18-R2-037 | HEAVY最大2只限制并发数量，不等于每profile串行，不能替代状态锁 | HEAVY2只管名额，不能证明同档案顺序和一致性。 |
| S18-R2-038 | 对先写磁盘再等HEAVY被429拒绝的路径核对reference_saved状态 | F33满HEAVY前已写盘见证保留；429必须清楚reference_saved语义。 |
| S18-R2-039 | 原子JSON替换只保护单文件，候选复制与JSON提交之间仍需一致性设计 | 单文件atomic replace不保证锚点+JSON跨文件事务，失败点逐个测。 |
| S18-R2-040 | 校准提交前档案已删除或adapter状态已变化时必须停止，不能恢复旧状态 | 提交前删除/变trained都应重新核对，禁止恢复已删除旧档案。 |
| S18-R2-041 | ASR评估全部失败不再用CER0.05冒充实测值，应记录null与失败原因 | ASR缺失不能CER0.05；修为缺失/失败与覆盖率，不填优分。 |
| S18-R2-042 | 部分文本ASR失败时记录覆盖率，不能只对成功样本平均后隐藏缺失 | 部分ASR失败保存分子分母，不能只平均成功样本。 |
| S18-R2-043 | 全部候选合成失败时返回明确未选出有效结果，不能chosen0看似成功 | 全合成失败不能chosen0，记录无有效选择并保留上次有效状态。 |
| S18-R2-044 | 每候选的有效生成条数和预期条数同时保存，评分先验证完整性 | 每候选预期与成功条数都入收据，先完整性后评分。 |
| S18-R2-045 | 未测或低可信声纹指标不填高分默认值，应明确阻塞/降级语义 | 未测声纹不填高分默认，明确阻塞或降级。 |
| S18-R2-046 | 候选排序排除非有限得分，NaN/Inf不进入max选择 | NaN/Inf在排序前拒绝，不靠max偶然顺序选候选。 |
| S18-R2-047 | 模型输出空音频、太短、全静音和缺字分别记失败而不只比声纹 | 空/太短/静音/缺字分别标失败，声纹高不代表有效语音。 |
| S18-R2-048 | 校准报告应保留先前有效结果，失败新校准不覆盖为貌似新最佳 | 失败校准保留旧有效结果，不能覆盖成看似新最佳。 |
| S18-R2-049 | ASR释放与临时目录清理放入覆盖所有异常的finally路径 | ASR/临时目录全异常finally清理，取消和生成异常都需覆盖。 |
| S18-R2-050 | 错误信息需脱敏且保留阶段，不能把原文和本机私有路径暴露给日志 | 错误按阶段脱敏，不回显私人全文/本地路径。 |
| S18-R2-051 | 同目标文本跨GPU诊断使用相同seed，修复100+17*ti+gi的设备偏移混杂 | 诊断跨GPU同文用同seed，100/101旧见证只说明诊断混杂。 |
| S18-R2-052 | 将实际seed写入每张卡诊断条目，使测试条件可核验 | 每卡真实seed进诊断收据，禁止只在总配置声明。 |
| S18-R2-053 | 会话调度当前各卡同seed的行为应保留，不把诊断偏移引入播放 | 正式会话同seed调度保持，不把诊断设备偏移带入播放。 |
| S18-R2-054 | 两卡同一voice_binding和voice_conditioning都要进诊断收据 | 每卡同时列binding和conditioning，profile ID不够。 |
| S18-R2-055 | 记录实际dtype、模型版本、codec政策与DSP后端，不能仅比profile ID | dtype/版本/codec/DSP在目标机实录，当前不能填测量完成。 |
| S18-R2-056 | 相同参数不意味着位级相同；阈值评分和人工听感结论分开 | 同参数不保证波形位同，评分阈值与盲听结论分列。 |
| S18-R2-057 | 同文对照与不同文本交替朗读各自设计，不能用同文替代自然衔接 | 同文对照不能替代不同文本交替朗读，两者分别验收。 |
| S18-R2-058 | 所有条目失败时speech_db默认0不应参与一致性，明确缺失项 | 全失败speech_db0是缺失占位，不参与一致性统计。 |
| S18-R2-059 | consistent布尔值应附完整性及阈值说明，不能称零噪声或100%同声 | consistent必须附覆盖与阈值，不是100%同声或零噪声承诺。 |
| S18-R2-060 | 诊断生成在锁定或请求取消后仍进行时保留资源状态，不误报即时停止 | 取消诊断后后台资源未必停，UI停止等待与真实停止分开。 |
| S18-R2-061 | 校准结束必须检查load_on_workers回执，不能丢弃失败后正常返回 | 校准必须检查worker回执，不能reload失败仍正常选定。 |
| S18-R2-062 | 保留文本/候选接口已有reference_saved与503部分失败语义 | 已有reference_saved/503部分失败语义保持，避免误称磁盘没提交。 |
| S18-R2-063 | Go激活两卡并行、同绑定同模式核验及旧active保留不得回归 | Go双卡同pin同模式激活保护保持，失败旧active不动。 |
| S18-R2-064 | 激活最终再次读磁盘核对指纹的检查必须保留 | 激活提交前再次读盘核pin保留，不以提速删掉。 |
| S18-R2-065 | Python reload最终current为None时应视失败，而不是跳过版本核验 | reload最终current=None必须失败；已有F20相关见证不等于修复。 |
| S18-R2-066 | 候选校准只用GPU0的现状须说明；多卡校准需独立计划，不虚报双卡评估 | 当前校准GPU0事实需说明，多卡评估不能由双worker推断。 |
| S18-R2-067 | 加载某卡成功某卡失败后，不允许新会话静默只用成功卡冒双卡一致 | 单卡加载成功不能称双卡就绪，新会话行为要显式失败。 |
| S18-R2-068 | 冷首次sanity合成耗时应与提示提取耗时分开记录，避免首声归因错误 | 冷sanity合成与提示提取分别计时，当前无目标设备不归因。 |
| S18-R2-069 | HTTP断开不等于后台模型加载已停止，未来重试需幂等/状态查询 | HTTP断开不等于加载停止，重试须先状态查询/操作身份。 |
| S18-R2-070 | 不得为降低激活耗时跳过Worker锁内参考前后两次指纹校验 | 参考前后两次锁内指纹核验保留，不因激活加速省略。 |
| S18-R2-071 | 审查_cal临时profile移除后Worker提示缓存仍驻留的资源生命周期 | 临时_cal删除后提示缓存生命周期需独立检查，不把删目录当释放GPU。 |
| S18-R2-072 | 重复校准相同临时ID时确保旧提示被替换，不能复用先前参考 | 重复临时ID也须按内容pin替换旧提示，不按路径命中。 |
| S18-R2-073 | 删除档案后清理与它关联的profiles、voice_bindings、levelers和提示快照 | 删除档案需按作用域清profile/binding/leveler/prompt，不能漏在用引用。 |
| S18-R2-074 | 缓存释放必须获取合成同一把锁，不释放正在使用的GPU张量 | 缓存释放用同合成锁，不释放正在使用的张量。 |
| S18-R2-075 | 缓存容量按可测内存预算管理，而不是只看磁盘profile数量 | 缓存容量须真实内存测量，磁盘profile数量不是显存预算。 |
| S18-R2-076 | 临时校准ID与用户可启用ID区分，不能由列表选中临时声音 | _cal不在可激活列表中，临时身份与用户档案分开。 |
| S18-R2-077 | 备份继续排除_cal档案，不把测试用临时状态持久化为模型 | 备份继续排除_cal，不把校准临时数据持久化为模型。 |
| S18-R2-078 | 临时目录清理失败记录状态并可回收，不无声积累数据 | 临时清理失败要可见/可回收，不无声积累私有数据。 |
| S18-R2-079 | 生成器取消仍要close并释放有界codec窗口，不能因缓存修改遗漏 | F36上游close异常会跳finish，需保留finally清窗口的原取消保护。 |
| S18-R2-080 | 不要盲目清空CUDA所有缓存导致每段冷启动，资源回收须按作用域 | 不要全局清CUDA缓存制造每段冷启动，释放应有作用域。 |
| S18-R2-081 | 候选点击期间禁用或序列化同档案变更按钮，避免重复并发写 | 候选/校准变更按钮串行或操作身份保护，不仅防双击样式。 |
| S18-R2-082 | 响应乱序时按操作版本更新高亮，不让旧响应覆盖新选择 | F42已证同epoch合成响应回滚高亮；只修UI排序不声称后端回滚。 |
| S18-R2-083 | 继续保留accessEpoch和AbortController防锁定后迟到数据回填 | accessEpoch/abort锁定清理保持，不能用新操作版本替换旧安全门禁。 |
| S18-R2-084 | 客户端取消只能停止等待时明确提示后台任务可能继续，不伪报服务器取消 | 取消等待明确后台可能继续，不能显示已撤销服务端提交。 |
| S18-R2-085 | 503且reference_saved时显示已保存未全卡就绪，不能笼统当未保存 | 503且reference_saved显示保存成功/加载失败两个状态。 |
| S18-R2-086 | 校准报告区分逐候选评分、最终提交、双卡加载三个状态 | 报告分别标逐候选评估、磁盘提交、双卡加载，不能一个绿标覆盖。 |
| S18-R2-087 | 没有有效候选或指标不全时不显示成功绿标 | 无有效候选/指标不完整时不显示成功；错误不伪造评分。 |
| S18-R2-088 | 参考转写可审阅但日志默认脱敏，token不进URL/localStorage | 参考转写只在授权视图审阅，token不入URL/localStorage。 |
| S18-R2-089 | 新增条件证明信息只放同源授权接口，不能自动上传外部诊断服务 | 条件来源收据走同源授权接口，不自动发外部诊断。 |
| S18-R2-090 | 新增交互保持移动端可操作、录音失败队列保留与锁定清空 | 移动端录音失败队列/锁定清空保持，新增控件不能遮停止按钮。 |
| S18-R2-091 | 原始库已有revision与lease设计可借鉴，但不直接修改其已成功数据格式 | 借鉴revision/lease但不改已成功库格式，迁移需单独合同。 |
| S18-R2-092 | 候选处理与真实训练继续分开命名，不把评分或缓存称训练提升 | 参考缓存/评分不叫训练提升，真实优化器执行独立验收。 |
| S18-R2-093 | 训练adapter来源hash与固定参考在新条件策略下仍必须核验 | trained来源hash及固定参考持续核验，条件策略不豁免。 |
| S18-R2-094 | 私有原始样本仍排除Dataset自动备份，新增诊断WAV默认不进入归档 | 私有原始样本与新WAV诊断不自动Dataset备份。 |
| S18-R2-095 | 代码、参数和参考版本相同的测试与实际用户WAV声学验收分开报告 | 同版本代码/参数仅是实验条件，不是用户WAV声学通过。 |
| S18-R2-096 | 为每个确认缺陷建立独立失败样例，后续修复应让同案例先失败再通过 | 每缺陷定位独立见证，23建议可复用相关见证但不能当23独立bug。 |
| S18-R2-097 | 受控AST交错不是线程压力测试；实现后补真实并发和HTTP回归 | AST确定性交错不等于真实并发，修复后补HTTP和线程压力。 |
| S18-R2-098 | 下载wheel仅源码检查不安装旧qwen-tts，避免命名空间冲突 | wheel只下载检查，不安装旧qwen-tts污染HF命名空间。 |
| S18-R2-099 | 本轮100建议与实际实验范围完整入备忘录，不宣称全源三轮完成 | 旧轮100建议不能倒写为当时全源三遍；当前53三遍另有新台账。 |
| S18-R2-100 | 第三轮结束及逐题50建议决策完成后才改产品，继续冻结17包与工作台 | 原先顺序决策及17冻结保持，源码三遍完成不自动开工S1。 |

### 原审查第3轮100条

| ID | 原建议 | 本批逐条处置说明 |
|---|---|---|
| S18-R3-001 | 保留16码本、24kHz及1920样本每帧合同，不用未知解码器静默替代 | 保持16码本/24k/1920合同，不允许未知解码器静默回退。 |
| S18-R3-002 | 左上下文25帧只保留有界生成码，参考码继续禁止进入输出解码 | 25帧左上下文只保留生成码，参考码不能进入输出窗口。 |
| S18-R3-003 | 默认右前瞻0与实验1/2帧分别记录延迟与真实质量，不用随机codec推断最优 | 右前瞻0/1/2需预训练codec真实对照，不以随机模型选最佳。 |
| S18-R3-004 | 为每次提交记录全局帧偏移与已提交区间，定位接缝是否重复或漏帧 | 提交帧偏移/区间用于追重复漏帧，先明确坐标语义。 |
| S18-R3-005 | 区分有效生成帧、保留上下文和待提交PCM，不能把重复解码时间当新语音 | 重复解码上下文不能算有效语音，pending与已提交分开计。 |
| S18-R3-006 | 取消和异常均close生成迭代器并清理pending，禁止取消后尾包泄漏 | 取消/异常都须close并清pending；F36说明异常路径仍缺保护。 |
| S18-R3-007 | 实际tokenizer返回错误采样率、非有限值或长度不符继续拒绝 | 原采样率/shape/NaN/长度拒绝行为保持，不静默修成可播。 |
| S18-R3-008 | 按首2/4/8帧对照时固定后续策略与文本，不能混入候选或seed变化 | 首2/4/8对照固定后续文本/seed/候选，真实模型缺失则阻塞。 |
| S18-R3-009 | 真实codec有限上下文与整段解码差值须用预训练权重另测，不凭因果结构宣布无接缝 | 有限上下文与整段差须预训练权重，因果结构不是无接缝证明。 |
| S18-R3-010 | prepare_ms不含生成器首次next里的全部预填充，拆分前先验证时钟范围 | prepare_ms与first next预填充边界明确，不能重命名即算测量。 |
| S18-R3-011 | 将整块与不规则分块输出一致性列为DSP算法合同而非只检查有限和长度 | 整块/不规则分块建立数值合同，旧分块差异是修复前证据。 |
| S18-R3-012 | NumPy淡入使用固定总长度及已处理位置，不让每次短块重新从零起算 | 淡入用固定总进度而非按每块重置，短块/正常块同输入回归。 |
| S18-R3-013 | NumPy RMS统计保留不足10ms余数，避免按来包边界重新分组 | 10ms RMS余数跨块保存，不能重分组造成包依赖。 |
| S18-R3-014 | Rust逐样本平滑与NumPy插值应先定义相同算法再设合理量化容差 | Rust/NumPy先统一所需算法和量化容差，再称跨后端等效。 |
| S18-R3-015 | flush后Rust清DC状态而NumPy不清的差别须明确，不能称API语义完全一致 | flush DC状态差异明确记录；F27不证明用户沙沙原因。 |
| S18-R3-016 | 当前Worker每段重建leveler，不能将跨段复用API问题直接认定为生产根因 | Worker每段重建leveler的事实保持，跨段API差异不直接算生产根因。 |
| S18-R3-017 | 固定目标电平与最大增益仍不保证两段动态响度相同，保留完整语音测量 | 目标dB与最大增益不保证动态响度相同，需整段实际测量。 |
| S18-R3-018 | 纯静音、阶跃和有声转静音须同时检查滤波残留、削波和增益泵动 | 静音/阶跃/有声转静音同时测DC/削波/泵动，不只检查finite。 |
| S18-R3-019 | Rust ABI加载需区分不兼容符号和库缺失，不能失败后不告知回退路径 | ABI缺符号和库缺失分开；F38是C故障fixture，不是实际Rust库验收。 |
| S18-R3-020 | 缺Rust编译器时记录未执行，不用C++重写参考实现冒Rust实测 | 无Rust工具链记未执行，C/C++参考不算Rust测量。 |
| S18-R3-021 | 120样本以下语音块不能因无完整RMS帧就直接丢弃，设计跨块累积 | 不足120样本见证是泛用helper；当前codec1920倍数可达性另列。 |
| S18-R3-022 | 跨输入块保留35ms有界预滚，而非只在检测到声音的当前块向前取 | 跨块预滚840样本差是合成边界见证，不直接称真实辅音丢失。 |
| S18-R3-023 | 候选静音与未发声辅音不能仅凭能量绝对区分，试听门禁保留 | 轻辅音与静音不能只靠能量分开，保留真实听感门禁。 |
| S18-R3-024 | 短末块含有非零语音时须有明确finish策略，不能永久留held后销毁 | 60非零样本留held需finish政策；未定义前不能声称末音完整。 |
| S18-R3-025 | 尾静音裁剪应记录实际删掉时长和阈值，不把删音频冒首声或RTF提速 | 裁掉时长及阈值入收据，删除音频不能算提速收益。 |
| S18-R3-026 | 900ms超长首静音放行应保留异常说明，不能把放行静音算实际人声 | 900ms放行首静音是异常政策，不能作为实际首人声。 |
| S18-R3-027 | 1800ms held上限必须在长无声生成时仍有界，不引入全句缓冲 | 1800ms held上限保持，禁止修尾端引入全句无界缓存。 |
| S18-R3-028 | 输入codec固定1920样本倍数与泛用小块测试分开，标注生产可达性 | 1920倍数生产合同与小块泛用反例分开，修复目标范围写明。 |
| S18-R3-029 | 裁剪器发出的样本索引需可追溯至模型原始PCM，便于核对漏音 | 输出样本坐标追溯原PCM，便于审查裁剪是否漏音。 |
| S18-R3-030 | 输入很轻时不要单纯升高裁剪阈值，应比较失真与背景噪声的权衡 | 轻语音不能盲抬阈值，真WAV比较失真/噪声权衡。 |
| S18-R3-031 | 保持流式相位和上一个输入样本跨PCM帧连续，不能每帧独立插值 | 保留跨包相位与上一样本，不能逐帧独立重采样。 |
| S18-R3-032 | 24k直通与44.1k/48k转换各自验证输入时长和输出样本预算 | 24k直通和44.1k/48k分别核时长与预算，不沿用名义帧数。 |
| S18-R3-033 | 终止时缺下一个插值端点应定义末样本延拓或明确短尾策略并测试 | 末端插值缺端点须明确延拓/短尾政策，不由1样本差宣布声学损伤。 |
| S18-R3-034 | 重采样收尾不能以补充可计入speech的静音改变RTF分母 | 不补可计speech静音扩大RTF分母，flush单独记账。 |
| S18-R3-035 | 每段协议标记不应重置同一朗读流的重采样相位，会制造边界跳变 | 同朗读流跨段相位连续，协议分段不重置重采样器。 |
| S18-R3-036 | 锁定、取消和新流begin应清掉上一任务的相位及延迟端点 | 锁定/cancel/new begin清旧相位端点保持，防旧数据串新轮。 |
| S18-R3-037 | 分块与整块重采样在数值容差内一致的现有行为应保留 | 分块/整块重采样已有相同容差保护保持，尾端修复不得破坏。 |
| S18-R3-038 | 一输入样本、空块及极短末块需测试，不只测长整秒波形 | 空块/一输入样本/极短末块单测，不只覆盖整秒。 |
| S18-R3-039 | 扩展至降采样时需考虑抗混叠，不能将线性插值叫任意采样率高保真 | 若支持降采样需抗混叠设计，线性插值不称任意率高保真。 |
| S18-R3-040 | 实体浏览器实际采样率与请求24k可能不同，诊断记录两者 | 实体设备实际采样率需记录，ctx请求24k不是硬件率保证。 |
| S18-R3-041 | 生成结束且剩余20ms音频应有播放或明确失败结果，不能永久buffering | 20ms合成完成短尾仍buffering，须播放或显式失败而不是永久等。 |
| S18-R3-042 | 精确50ms边界的严格大于判断需单独测试，不能只测51ms | 50与51ms分别断言，严格大于边界不能靠大缓冲用例覆盖。 |
| S18-R3-043 | 欠载恢复时最后短尾同样应可排空，避免截掉最后一个音节 | starved最后短尾与初播一样有终止策略，不能截最后音节。 |
| S18-R3-044 | 已结束数据的排空政策与持续生成时风险缓冲分开，不盲降正常启动阈值 | 完成短尾与live风险缓冲分开，不把修尾端变成全局降阈值。 |
| S18-R3-045 | 有剩余样本但低于阈值时ended判定须有终止路径，不假装已播完 | 低于阈值但仍有样本必须可终止，不能提前ended报自然完成。 |
| S18-R3-046 | 一任务只能产生一次最终结束，迟到统计消息不能把ended改回playing | F41证明stop后状态晚到，不等于所有ended路径；须单测一次最终结束。 |
| S18-R3-047 | 长网络抖动和低产出速率下测试启动等待与欠载率成对取舍 | 真实抖动/低产出需联合等待与欠载统计，VM不签自然朗读。 |
| S18-R3-048 | 暂停恢复必须在用户授权AudioContext状态下执行，不自动规避浏览器策略 | 暂停恢复受AudioContext用户授权约束，不自动绕过浏览器策略。 |
| S18-R3-049 | 单调时钟中的0值不宜兼任未记录标记，检查极早首包的时间哨兵 | 零时钟与未记录标记分开，先补极早包哨兵测试。 |
| S18-R3-050 | 运行原播放器VM只能证明逻辑，不可声称浏览器硬件首声变快 | VM只能签逻辑，不能签浏览器硬件首声变快。 |
| S18-R3-051 | firstPlayedMs目前是主线程play命令时刻，名称与报表需区分实际消费 | firstPlayedMs是命令时刻，消费/出声另起指标且未测null。 |
| S18-R3-052 | 增加首样本消费确认前先定义是否跳过显式停顿和极小淡入样本 | 首消费确认需先定义跳过停顿/微小淡入样本规则。 |
| S18-R3-053 | Worklet currentFrame与主线程performance属于不同时间轴，使用可解释映射 | currentFrame与performance时间轴映射须可解释，不能直接相减。 |
| S18-R3-054 | 保留ring样本计数与自然结束不额外记欠载的已通过行为 | ring样本计数与自然结束不额外欠载的现有保护保持。 |
| S18-R3-055 | 欠载只计一次直至恢复，避免每个渲染量子重复放大统计 | 欠载只记一次直到恢复，不能渲染量子重复放大。 |
| S18-R3-056 | 容量溢出dropped必须进入上层状态和失败提示，不能只在底层计数 | dropped从底层进上层失败提示，不能只显示正常结束。 |
| S18-R3-057 | 固定192样本淡入在24k/48k分别8/4ms，若要求同毫秒则按实际率配置 | 192样本对应24k8ms/48k4ms；是否固定毫秒需先定义真声学目标。 |
| S18-R3-058 | hold与reset后无旧PCM回放，保留现有重置后精确零输出测试 | 保留reset后精确零输出；F41命令状态漏洞不证明旧PCM真实重播。 |
| S18-R3-059 | 环形缓冲溢出属于丢样，不得被统计成已自然连续读完 | 容量溢出属于丢样，完整性门禁必须失败而非自然读完。 |
| S18-R3-060 | 声卡/系统输出延迟仍需实体设备测量，Worklet消费也不是声学听到时间 | Worklet消费仍不是声卡出声，实体延迟测量独立阻塞。 |
| S18-R3-061 | 规划器PauseBeforeMs由上一边界生成，逐段记录而不是把所有停顿归模型 | 逐段记录PauseBefore来源，不把全部停顿归模型。 |
| S18-R3-062 | Worker默认只加显式lead pause，核实tail默认0后再判断重复停顿 | 先核tail默认0与lead pause，再判断重复加停顿。 |
| S18-R3-063 | 保留首段零规划停顿，不以参考呼吸或原音占位提前出包 | 首段零规划停顿保持，禁止参考呼吸/原音抢首包。 |
| S18-R3-064 | 模型内部停顿与规划停顿叠加需实际WAV分层对照，不能只删规划停顿 | 模型内停顿与规划停顿需真实分层WAV，不能先删规划停顿。 |
| S18-R3-065 | 有序转发必须保留，不能为了最快包先播后一GPU导致错序 | 有序转发不改为最快worker先播，保留正文顺序。 |
| S18-R3-066 | 已消费部分PCM后禁止跨卡整段重试，保护不重复词句的现有门禁 | 已消费PCM禁止跨卡整段重试，避免词句重复。 |
| S18-R3-067 | 未消费重试时正确扣除旧produced样本，维持背压与统计一致 | 未消费重试需扣旧produced，背压和统计不可双记。 |
| S18-R3-068 | first_worker_audio可能是显式静音包，报表不可直接称人声首包 | first_worker_audio可能静音，不能直接报人声首包。 |
| S18-R3-069 | 第一段4帧与后段6/8/12帧策略保留可追溯，提速不得改变音色条件 | 首4与后段6/8/12策略保留来源，不让性能实验暗改条件。 |
| S18-R3-070 | 正文保留、引号配对、小数和缩写拆分须有实际Go回归，不靠源码注释 | 实际Go正文/数字/缩写/引号回归必需，注释和AST都不能替代。 |
| S18-R3-071 | 在线推理与离线训练GPU租约保持互斥，不为测试盲停驻留模型 | 在线/离线整组GPU互斥保持，不为审计停真实驻留模型。 |
| S18-R3-072 | 真实双卡训练、引用缓存与profile建档继续分开报告，避免功能混淆 | 真双卡训练与建档/缓存分开报告，CPUrank替身不算训练成功。 |
| S18-R3-073 | 子进程继续清除API与认证秘密环境变量，不因性能诊断泄漏 | 子进程凭据清理保持，性能探针不得继承认证/模型私钥。 |
| S18-R3-074 | 模型与adapter来源hash及安全权重格式不能为快速加载而跳过 | 模型/adapter hash与安全格式不为快加载豁免。 |
| S18-R3-075 | 训练数据审阅/完整覆盖与声学验收是独立缺口，18音频修复不自动解决 | 长训练数据覆盖/审阅与声学是独立缺口，音频修复不会自动完成。 |
| S18-R3-076 | 取消训练只终止本次进程组，不根据旧PID文件杀其他进程 | 仅终止本次进程组，不能用旧PID误杀其他服务。 |
| S18-R3-077 | 保留离线代码与模型指纹核验，不自动开启远程代码或下载权重 | 离线指纹/不信任remote code保持，不自动下载权重补缺口。 |
| S18-R3-078 | 新增诊断原始WAV默认私有且关闭，不能进入公开Git和自动备份 | 诊断WAV默认私有关闭，不进Git或自动备份。 |
| S18-R3-079 | 资源状态的CPU成功不标CUDA或GPU优化成功，尤其是当前无Torch环境 | CPU资源status成功不算GPU优化，现环境尤其不能偷换。 |
| S18-R3-080 | 剩余复杂训练/恢复路径只有入口边界复核，明确语义深审仍需补齐 | 原文“尚需语义深审”属历史；当前53三遍完成，但训练恢复功能签收仍缺。 |
| S18-R3-081 | 正式工作台继续只读核对，不因音频审查改写15文件或HEAD | 正式15文件和HEAD只读核对，审计不得改用户工作台。 |
| S18-R3-082 | 自命名空白文件、用户粘贴、并发版本冲突和磁盘持久化需保留 | 自命名空白/用户粘贴/CAS/持久化继续保留，新功能不强制预填。 |
| S18-R3-083 | 复制预览与正式工作台分别核对，不能用旧17复制成功冒18完整包成功 | 17和三web源码复制保护不等于18复制页，发布前独立验收。 |
| S18-R3-084 | 新发布前固定launcher字节数/hash，并校验53以上实际资产完整性 | 18未生成，未来固定launcher bytes/hash与实际资产清单再发布。 |
| S18-R3-085 | 剪贴板失败回退应选中完整源代码，不能只复制可见窗口 | 剪贴板拒绝回退必须选完整源，不只选可见窗口。 |
| S18-R3-086 | 文件名、路径穿越、脚本/style闭合注入等既有浏览器测试继续执行 | 文件名/穿越/闭合注入保护继续跑，不因新文案弱化。 |
| S18-R3-087 | 锁定清理、同源token和迟到响应隔离不能被新指标消息绕过 | 锁定/同源token/迟到数据隔离不能被新指标旁路。 |
| S18-R3-088 | 旧验证脚本固定历史分支属于历史证据，新分支另建验证器而非改旧收据 | 历史验证脚本分支固定不改，新分支另建核验器。 |
| S18-R3-089 | 新工具依赖留忽略目录，下载源码也不与模型权重混入发布资产 | 工具/下载/依赖留忽略目录，不混进模型资产或正式包。 |
| S18-R3-090 | 所有未执行的Go/Rust/真实浏览器/完整模型实验明确标未执行 | 未执行Go/Rust/浏览器/模型明确false，不能由历史收据推本批运行。 |
| S18-R3-091 | 完整manifest读取/hash/AST只证明库存与语法，不声明全源逐行语义无错 | manifest/hash/AST仅签库存与语法，不签语义无错。 |
| S18-R3-092 | 三轮专题各100完成也不等于所有代码已语义审查三遍，覆盖缺口单列 | 专题3×100与全源3遍分开；当前阅读完成仍不是300功能签收。 |
| S18-R3-093 | 每个实验写方法、注入边界、实际源hash及探针hash，避免不同版本混算 | 每证据写方法/注入/源码与探针hash，避免版本混算。 |
| S18-R3-094 | 将已复现缺陷、待验证假设与保留保护分别分类，不将300建议全标已修 | 缺陷/待证/保留分别处置，不能300全部标已修。 |
| S18-R3-095 | 重建环境仅NumPy和Node时旧模型实验收据保留历史，不算新执行 | 缺环境保留旧结果为历史；新审计12和Node30不冒CPU426。 |
| S18-R3-096 | 第25题起一次一题，具体选项/推荐/理由/50建议全部记录后再下一题 | 逐题50行动与推荐/理由全部保持，本批不新增重大方案题。 |
| S18-R3-097 | 实施方案要将首声、条件来源、状态一致、DSP、裁剪、播放排空分成可回滚小步 | S1输入→S2版本→S3DSP→S4裁剪→S5排空→S6度量→S7透明→S8发布分小步。 |
| S18-R3-098 | 产品最终源码冻结后完整三轮回归，当前边界探针不能代替全功能通过 | 最终产品源码需完整三轮功能回归，当前审计三轮不代替。 |
| S18-R3-099 | 零噪声/单一音色/自然朗读及RTF0.3仍需真实WAV和双T4，不用绝对承诺替代 | 无沙沙/同一音色/自然连续/RTF0.3需真WAV双T4，不作绝对保证。 |
| S18-R3-100 | 第三轮备忘录和缺口完整内嵌提示词，发布18之前仍使用17并保持PARTIAL | 本轮处置全文入交接，18未发仍用17并保持PARTIAL/BLOCKED。 |

---

## 内嵌备忘录：KAGGLE_STEP18_G0_INPUT_HTTP.md

# G0第10批：S1输入边界的真实TCP/HTTP见证

日期2026-10-23；活动分支 `arena/1160bd87-kagglee`。

**本批完成438项CPU/HTTP合同三轮，438×3＝1314 PASS，无失败／错误／跳过。其中继承原426、新增12（7保护＋5未修观察组）。新增每轮实际61个TCP/HTTP请求，合计183个。测试通过不表示所有请求应当成功：每轮16个500是准确捕获的未修行为，不能当作功能验收。G0与整体仍PARTIAL/BLOCKED。**

用户要求确保成功：本批以同输入断言、真实请求、失败留档和独立核验控制可验证结果，不预先承诺产品／完整模型／训练或声学一定成功。产品未修改，未跳S1实施、Q28或18发布。

## 1. 环境恢复与范围

本次工作区开始没有旧venv或node_modules。重新创建忽略目录.venv，从允许的PyPI下载并安装历史Python固定依赖，完整freeze逐行等于第7批记录去掉go-bin==1.23.9；Go不在本批范围，未安装。NumPy2.2.6保持，与产品requirements2.4.6不同，不称目标依赖门禁完成。没有安装Torch/Qwen/模型、Rust、Go或npm依赖，没有执行产品bootstrap安装器。

安装首次成功，保存input-http-dependency-install-first.txt及完整freeze；不声称与历史所有系统库／二进制绝对等同，venv恢复不是语音运行环境验收。

## 2. 是真实TCP，不是TestClient或AST冒充HTTP

新 `input_http_fixture.py` 将完整原始analyst.app交给Uvicorn，在已绑定的127.0.0.1临时端口监听，httpx通过真实socket请求。使用启动事件而非sleep轮询，客户端关闭后设置退出标志、限时join并确认自有server线程停止；服务器退出时清理其事件循环执行器。临时目录和合成WAV／档案均由测试独占并删除，不读用户私有数据。

FastAPI、JSON解析／验证、BodyBudgetMiddleware、原路由、原文件提交与HEAVY执行。生命周期事件明确off，不冒称完整服务启动；路径／profile读取位置切到自有临时目录，worker重载回执是明确fixture，仅返回两项ok。不是完整模型worker、真实训练、声音生成、Go鉴权代理、远端利用或实体音频实验。环回端口仅测试用途，不是面向用户的预览服务。

## 3. 新12项：7保护、5未修观察组

| 合同 | 实测与边界 |
|---|---|
| 合法整数候选 | 0/1正常200，锚点字节／转写／pin匹配；只证明fixture worker回执下原路由提交 |
| 越界／缺档案 | -1/2/999返回400，缺档案404，不改盘、不reload |
| 有限非对象／破JSON | null/list/bool/number/string及不完整JSON返回422，不改盘；不将非有限值混入该保护 |
| trained保护 | candidate/text/calibrate均409，在IO/reload/校准前拒绝；trained元数据为fixture，不是训练产物验证 |
| library严格JSON | NaN/Infinity/-Infinity、重复键、未知／缺少字段、非对象和破JSON均400，不调store.create |
| 合法Unicode文本 | 中文／希腊字母／emoji完整保存并同步候选转写，空／缺省文本400；不涉及ASR正确性 |
| 错误index与满HEAVY | 两槽占满时，越界仍400、null仍500且不进入reload；释放后两槽可复用 |
| I01：index强转未修 | true→1、false→0、1.9→1、字符串1→1、1.0→1，均200并reload |
| I02：非有限与容器未修 | null/list/dict/非法数字串、NaN/±Infinity/1e309及顶层非有限值返回500，不改盘、不reload |
| I03：旧字段策略未改 | 缺省index回0，重复键最后一个生效，未知字段忽略；记录兼容现状，不擅自签未来政策 |
| I04：文本类型／Unicode未修 | dict/list/null/bool/float经str保存并200；孤立surrogate返回500，原文件不变且临时文件清掉 |
| I05：损坏档案边界未修 | 空candidates400；null/dict/null-entry500；预装的父路径／符号链接file可复制自有档案目录外WAV并200 |

I05所有“目录外”内容仍在自有临时测试树，损坏profile预先写入，不是HTTP请求体直接控制file字段；不证明公开远程任意文件读取或实际模型接受该档案。没有访问真实私密路径。

I02顶层NaN等不等于内部index的int转换：有限非对象是422，顶层非有限触发框架错误响应的实际500。保留真实原始请求字符串与响应，不用httpx的json参数拒绝NaN来假装服务端已拒绝。错误响应500为Internal Server Error，不回显源异常；未做完整错误隐私签收。

这些I01–I05细化原建议的边界，不按数量宣称新增5个独立产品bug。旧F01–42与先前DSP／播放器观察没有修复。

## 4. 三轮结果与继承核对

| 本批实际集合 | 第1轮 | 第2轮 | 第3轮 |
|---|---:|---:|---:|
| CPU＋HTTP合同 | 438 PASS | 438 PASS | 438 PASS |
| 原集合／本批新增 | 426／12 | 426／12 | 426／12 |
| failure／error／skip | 0／0／0 | 0／0／0 | 0／0／0 |
| 新真实TCP请求 | 61 | 61 | 61 |
| 独立NumPy分块／trimmer | 12／8 | 12／8 | 12／8 |
| 实际CLI期望合同 | 4 | 4 | 4 |

每轮61请求的状态分布相同：200×19、500×16、400×16、422×6、404×1、409×3；183请求不是183个单元测试。7新保护三轮21次、5观察组三轮15次，不能与每组多个请求重复计算。

原426逐test ID及结果与前批核对完全继承，原16份CPU观察与前批逐项一致；加新5组为21份观察，不把观察PASS当已修。新三轮原始请求／响应／观察片段一致，fixture地址与临时路径不混入稳定数据。

每轮三CLI按预期exit2/BLOCKED，resource status exit0但gpu_verified=false，不把阻塞当模型成功。C ABI故障库再次由系统cc编译／ctypes加载，是C故障fixture而非Rust执行；旧CPU rank／模型角色依旧替身，没有真实优化器／GPU训练。

新12预检首次12/12通过；探索原始HTTP矩阵的JSON与stdout保留。一次结果检查脚本误读ReceiptResult的id字段（实际字段test），仅检查脚本KeyError，未改测试或产品、未导致三轮失败，纠正记录在input-http-metadata-correction.json。

附加新执行三轮均通过：原24项审计合同×3＝72 PASS，Node工作台30×3＝90 PASS；工作台／产品web／旧浏览器spec JS语法、repack --check、Python AST39各三轮通过。AST39包含33份产品Python及6份当前测试／脚本。无失败／错误／跳过。这些检查不算浏览器执行或完整功能验收。

## 5. 逐建议映射，不涂绿原300

12条原建议新增精确test ID及三轮HTTP case下标／收据SHA：R1-011/020、R2-021/022/023/024/025/026/027/028/029/030。R2-024现在有真实后端HTTP NaN/Infinity见证，补足上批“旧payload没有NaN”的缺口；不是修成4xx。

input-http-recommendation-links.json每行保留原文和注入／鉴权／模型边界。原有限证据并集65加新链接后为70个ID，另230未进入这些限定集合，不等于无其他历史证据。原300、3×100处置说明、Q25–27各50行动原文保持；逐条最终／功能签收仍0，product_fix_implemented=false。

## 6. 冻结与D02

53内嵌资产三遍各13668行保持，不新增阅读信用，也不称整个Git仓库三遍审完。94冻结文件、正式15文件及HEAD保持，产品diff为空。

历史期待1228项中1225可读SHA匹配、变更0，三份D02旧.log仍缺失：pass2-gateway-go-install.log、pass2-gateway-preflight.log、pass2-startup-preflight.log。新环境安装日志不改名冒充旧安装日志，full_historical_integrity_passed仍false。D02不是靠新的438通过自动消除。

## 7. 门禁与下一步

本批证明真实原分析HTTP输入边界和原CPU保护可重复；没有证明严格输入已修、完整鉴权链／浏览器／Go race/vet通过，更无模型／双T4训练／长数据／音色／去沙沙／自然朗读／首声／RTF或创建加速验收。不承诺一定无错或一定达标。

下一步先补其他未绑定建议的精确测试证据，尤其候选／文本／校准版本冲突与旧评分提交组合；对S1将合法输入、缺省兼容、重复／未知字段、非有限JSON、损坏档案与trained限制整理为修复前失败／成功保护合同。G0门禁未签收前不直接修改冻结产品，不用反复总数回归替代逐条映射。需要重大方案选择才按逐题50行动开新题，不预填Q28。

本报告及PLAN／IMPLEMENTATION进入90份完整交接。独立verify_input_http.py再次从原始日志／JSON核438继承426、61请求／5观察、链接／SHA／环境／冻结／manifest与交接，成功只签本批记录准确。最新progress-input-http.json。直接继续，无需Continue。

---

## 内嵌备忘录：KAGGLE_STEP18_G0_VERSION_HTTP.md

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

---

## 内嵌备忘录：KAGGLE_STEP18_Q28_S1_CANDIDATE.md

# 问题28：怎样真正开始修复，同时不改冻结17、不把未完成G0说成通过？

## 选项与决定

- A：直接修改kaggle/source及17包。拒绝，破坏冻结、历史缺陷对照与正式复制。
- B：继续只加缺陷观察直到全部声音／硬件要求通过。拒绝，缺陷不修就无法做可信后续实验，观察数不是实现进度。
- C：新增明确隔离、可运行但未发布的18候选源码。保留全部17源码、旧探针与收据；先修已复现的S1输入及HEAVY先写后拒，执行同合同旧版失败对照和候选三轮验证。G0整体仍PARTIAL/BLOCKED，候选小步实现不等于放行默认、全S1或发布。
- D：一次复制和重写全部53资产、所有模型／DSP／浏览器层。拒绝，差异过大、难归因，也无法补足真实模型证据。

**选择C。** 这是本次明确的流程调整：先前“G0通过前不实施”的绝对实现禁令，收窄为“不让未通过的候选进入冻结包／正式工作台／发布或整体验收”。全源三遍和300处置说明已有；未覆盖合同、D02历史日志、真实模型／双T4／声学继续阻塞整体签收。修复候选可以开始，不能为此伪造G0通过。此决定落实用户要求真正推进，未豁免冻结和真实验收要求。

候选文件放在`kaggle/step18`，显式依赖冻结17的其余Python模块，不复制全部项目、不改默认入口。一个分析服务进程的候选／转写短提交用有界条带锁；HEAVY准入在任何写盘前，executor实际完成前不归还槽位。校准函数在本批不改，过期评分等问题继续未修；候选输入更严格不表示整个服务JSON或状态事务已严格。

## 进入下一题之前的50项行动

1. 核对活动分支固定arena/1160bd87-kagglee。
2. 对第11批及更早历史建立SHA保存清单。
3. 保留3旧日志缺失，不降低历史完整性要求。
4. 不修改冻结kaggle/source。
5. 不修改原始–17包及manifest。
6. 不改正式HEAD及工作台文件。
7. 明确新候选入口，不将默认服务自动切换。
8. 记录analyst候选的冻结来源SHA。
9. 复用其余冻结模块，避免复制全部53资产。
10. 明确候选不是独立完整18安装／发布包。
11. 保留25–27题及各50行动原文。
12. 将本题流程调整记录到PLAN和IMPLEMENTATION。
13. 实现候选入口严格UTF-8 JSON解析。
14. 非对象JSON返回受控400。
15. 拒绝NaN和正负Infinity。
16. 拒绝解析后溢出的非有限浮点数。
17. 重复JSON键返回400而不是静默取最后一个。
18. 明确未知字段拒绝策略，不让拼写错误被忽略。
19. 输入流设置独立有界预算，超限返回413。
20. index必须是整数，不接受bool。
21. 小数和整值float都不作为index接受。
22. 不接受字符串index隐式转换。
23. 缺少index返回400，不默认选0。
24. 对负数／越界索引返回400。
25. ref_text必须为字符串。
26. 去空白后长度限定1..20000字符。
27. 拒绝无法编码成UTF-8的代理项。
28. 保留合法Unicode、中英文和空白修剪。
29. 维护trained参考三个入口的409限制。
30. 缺档案维持404且不创建目录。
31. HEAVY获准之后才执行磁盘修改。
32. 不把准入和实际工作分开提前释放槽位。
33. executor入队前提交失败不能执行写盘。
34. 等待HTTP被取消时实际线程结束前不释放槽位。
35. 工作线程内重新核验档案存在与trained状态。
36. 候选／转写短提交使用有界锁，不持锁跨worker网络等待。
37. 候选文件名限定为单个安全文件名。
38. 拒绝候选符号链接、FIFO和目录。
39. 对候选文件字节读取设限并核对读取长度。
40. 校验候选文本类型与编码后再复制字节。
41. 候选新anchor用唯一名字，避免覆盖旧anchor后JSON失败。
42. JSON提交失败清理本次未提交的新anchor并保留旧状态。
43. 不将复制候选音频作为生成输出或播放。
44. 保留worker错误pin的503/reference_saved部分失败语义。
45. 不在本批顺便改校准／DSP／缓冲或声学默认参数。
46. 同一预期合同先在冻结17上执行失败对照，保留原stdout。
47. 再在候选上执行同合同，失败不修改为宽松期望。
48. 三轮运行旧450项和新候选测试，明确旧集合仍指向冻结17。
49. 三轮Node／语法／repack与冻结核对，保存全部失败和修正记录。
50. 报告精确修复范围、剩余校准缺陷、无真实模型／声学验收，更新完整交接后再进入下一题。

本题50条完成后才实施下述小步，不开启问题29。数量是行动清单，不是50项已实现声明；实际结果见S1候选报告和收据。

---

## 内嵌备忘录：KAGGLE_STEP18_S1_CANDIDATE.md

# S1隔离候选：首次实际修复与三轮工程回归

## 当前结论

**本批已有实际候选产品代码修改，不再只是增加观察。** 代码在`kaggle/step18/analyst.py`和`step18_profile_inputs.py`，来源和启动边界见同目录`origin.json`及README。

**候选未发布、未部署到默认服务，冻结17包和正式工作台未改。G0整体／完整S1／真实声音验收仍PARTIAL/BLOCKED。** 这不是完整18包，也不声称已改善沙沙、相似度或真实首声。

本批问题28按顺序完成选项、推荐C与50条行动，见`KAGGLE_STEP18_Q28_S1_CANDIDATE.md`；原问题25–27及各50条不改，问题29未开。明确调整过去的绝对实施禁令：可做隔离候选修复，不能将其冒充G0通过或放入冻结包／默认入口／发布。这保留真实模型与声学门禁，不再因未修缺陷而无限只做观察。

## 1. 实际实现了什么

| 代码改动 | 已验证的限定效果 | 边界 |
|---|---|---|
| candidate/text严格JSON及输入类型 | 拒绝bool/float/字符串索引、缺省index、非法容器、非有限值、重复／未知键、非对象及非法UTF-8 | 仅这两个新候选入口，不是全服务JSON改造 |
| 转写校验 | 严格字符串、有效Unicode、去空白后1..20000字符；正常中英文／emoji和边界长度可保存 | 请求另限128KiB，转义表示过大仍可413 |
| HEAVY先准入后写盘 | 静态满槽及真实两个在途编辑后，额外候选／转写429均不再改变磁盘 | 未将HEAVY当成每profile锁；未改其实际线程结束后才释放槽位语义 |
| 候选文件安全读取 | 拒绝父路径、符号链接、FIFO、目录和列举损坏元数据；普通文件no-follow/nonblocking有界读取 | 仅自有临时树测试，不是远程利用证明或音频可解码签收 |
| 内容地址锚点及JSON提交 | 不覆盖旧锚点；注入JSON提交失败时旧文件／元数据保持，本次未提交锚点被清理；相同选择复用文件 | 非完整跨文件／跨进程事务，不保证所有IO故障；旧锚点GC尚未实施 |
| 候选／转写／删除提交协调 | 新工作线程内重核档案／trained状态；有界进程内锁，worker网络等待不持锁；删除等待提交后不复活档案 | 新删除也经HEAVY，满额可429；原校准不参与本锁合同 |
| 兼容保护 | 合法候选字节、转写对应、trained三入口409、缺档404、原worker pin及503/reference_saved保留 | worker传输和模型是fixture，未证明真实双卡加载 |

只改原分析服务的`set_text`、`set_candidate`、`delete_profile`三个命名定义，新增4个提交辅助函数；其余原命名函数／类AST相同。尤其`calibrate_profile`和`load_on_workers`原实现未变。候选显式复用冻结17其余Python模块，不大规模复制53资产、不修改bootstrap、模型、DSP、训练或播放器。

## 2. 先失败对照、后候选通过

同一最终`test_step18_profile_inputs.py`文件的28项合同：

- 冻结17对照：43条失败记录、0 error、2明确skip。失败记录包含参数化子用例，**不是43个独立缺陷或43个失败方法**。两项skip分别为可能阻塞旧事件循环的FIFO复制路径，以及仅新executor提交架构需要的删除协调合同。
- 候选最终预检：28/28 PASS，failure/error/skip均0。FIFO和删除协调均实际执行，没有在候选上跳过。
- 两组收据记录相同最终测试文件SHA；不以修改断言或只挑通过项制造修复结论。

原始记录：`s1-candidate-frozen-red-final.{txt,json}`、`s1-candidate-precheck-final.{txt,json}`。

首次26项旧版对照超时，诊断栈显示卡在unittest对大WAV bytes的差异格式化（difflib），不是服务线程死锁。定向终止自有进程后，仅把文件快照改为SHA256＋长度，仍要求全部文件集合／内容相同；合法候选还直接比较字节。首次stdout、faulthandler栈、修正后26项及最终28项记录全部保留，没有覆盖。见`execution-notes`与`red-io-debug-first`。

复核先后修正两处候选设计：候选文本规范化必须同步两处元数据；写盘移到executor后，删除必须加入相同短提交协调。均在最终28合同及三轮执行前完成。

## 3. 三轮完整工程回归

`run_s1_candidate_cpu.py`实际执行三轮：

- **478×3＝1434 PASS**，每轮failure/error/skip均0。
- 每轮旧450项仍指向冻结17，逐ID／结果保留；新增28项指向隔离18候选。不能将合计说成478项全在新运行时验证所有功能。
- 旧25组未修观察照常保留，不把冻结缺陷观察改成候选“成功”。
- 每轮159次真实Uvicorn环回TCP＝旧85＋新候选74；三轮477，其中候选222次。
- 候选每轮实际状态：200×12、503×3、429×4、500×1、400×48、413×1、409×3、404×2。500是注入JSON提交失败的保护合同；错误码不都表示产品功能成功。
- 删除与reload的完成先后可以影响该候选请求的200/503，测试仅签两请求完成后档案不复活，不冒充删除期间所有pin路径都已修复。封存器对此场景不强制逐字节时序一致，其余候选HTTP内容三轮核对。
- 每轮companion仍为NumPy partition12、trimmer8及CLI4。三个CLI期望blocked，resource gpu_verified=false。C ABI fixture不是Rust编译／执行。

附加审计／Node／语法／冻结核对及独立封存的实际结果在末尾记录，不能借用旧批次通过数。

## 4. 三遍增量复核与原建议映射

原全源53资产三遍各13668行、原3×100建议与300处置说明不改。本批不是重新生成300条建议，而是在同一任务内按输入合同、生命周期／IO并发、冻结／安全／证据三条路线复核变更，结果见`s1-candidate-delta-review.json`。

本批15条原建议获得候选实现或保护的直接证据：R1-011/020、R2-021–030、R2-037/038/039；均有测试全ID、三轮收据SHA和HTTP数组下标，边界逐条保留。

**部分证据并集仍为75/300，没有增加。真正进展是从旧版失败见证推进到候选实现及验证，而不是提高映射数字。** 元数据脚本曾预计76，发现R2-039早已在并集中；断言失败单独留档后按真实集合纠正，不是产品／测试失败，也没有改原验收条件。

原300条最终／功能签收仍0。候选限定合同已验证不等于整条建议跨部署、模型、浏览器和发布边界全部验收。

## 5. 冻结、历史、环境和交接

- 原53资产、94冻结哈希、17包、正式HEAD及15文件保持。只使用`repack --check`，未运行旧生成器，未产出18发布包。
- 保存清单1402期待历史路径，其中1399已有文件SHA匹配、0变更、3旧.log依然缺失；D02未关闭，full_historical_integrity仍false。
- 现有venv复用，无新安装，pip freeze与前批逐字节相同。NumPy仍2.2.6，非产品requirements2.4.6。
- 未运行Go/race/vet、实际浏览器／剪贴板、DeepSeek、Torch/Qwen、完整权重、真实训练、双T4、麦克风／扬声器、声学或提速验收。旧浏览器／复制证据继续保存，不冒充本批执行。
- 完整交接为93份，包含本题28和本报告；冻结17的原交接不覆盖。

## 6. 下一步

下一步继续隔离18候选的S2：把校准输入快照、内容身份和提交冲突做成实际代码修复；保留旧版失败样例及新候选回归，再三轮验证。校准过期评分、缺失CER默认值、全失败chosen0、临时profile冲突、加载失败回执、删除／adapter版本变化等不能因本批S1成果而标为已修。

S3–S8、全部候选conditioning透明、真实首声、无沙沙、自然朗读、generated-only PCM、长录音真训练、双卡等效参数、RTF≤0.3依然未完成。不能承诺一定成功；本批只确保修复范围和证据能够复核，不隐瞒失败或改变冻结版本。


## 7. 附加核验与封存记录

附加检查已实际执行三轮：每轮24项审计、Node30项、JS语法、repack检查通过，43份Python AST解析通过。封存前独立核验首次通过，已核对同测试SHA的旧版失败／候选通过对照、三轮478项及旧450继承、候选TCP内容、所有引用日志／SHA、原建议映射和冻结／历史／环境；原stdout保存于`s1-candidate-seal-preflight-first.txt`。

本批清单`s1-candidate-run-manifest.json`覆盖102文件，包括实际候选源码。完整交接93份逐份内嵌核对。最终封存判据为`verify_s1_candidate.py`连续两次执行通过，输出逐字节一致；实际输出分别保存在`s1-candidate-verification-first.txt`与`second.txt`，结果以`progress-s1-candidate.json`为准并同步`progress-checks.json`。这些检查不签完整产品／模型／声学验收，不把隔离候选变成已发布18。

---

## 内嵌备忘录：KAGGLE_STEP18_S2_SNAPSHOT.md

# S2-A：校准输入快照与提交冲突的实际修复

## 当前进度：两个限定工程子批次已有代码

| 范围 | 当前状态 |
|---|---|
| 全源53资产三遍、每遍13668行；原3×100建议与300处置说明 | 已完成并保留 |
| S1入口／准入／锚点提交 | 已实现隔离候选；原28项合同本批在当前S2运行时重跑 |
| S2-A快照／冲突／同档案校准互斥 | **本批实际实现，新增22项合同三轮通过** |
| S2-B有效评分、全失败拒选、最终加载回执 | 尚未修复 |
| S3–S8、真实声音与双T4／训练／首声／RTF验收 | 未完成 |
| 默认服务／工作台／复制、18发布 | 仍17；18候选未发布、未部署 |

**整体仍PARTIAL/BLOCKED，不能计算可信整体百分比。** 75/300＝25%仍仅部分证据覆盖，不是修复率或整体完成率；本批没有提高这个数字，而是把已有失败见证推进到候选代码修复。不能把两个限定工程批次说成2/8或25%总进度。原300条最终／功能签收仍0，不表示本批限定代码合同没有实现，而是完整建议跨发布／模型／设备边界尚未签收。

## 1. 实际代码与修复范围

新增`kaggle/step18/step18_calibration_state.py`；相对归档S1，分析服务仅修改`calibrate_profile`、`commit_text`、`commit_candidate`。其余命名函数／类AST相同，S1入口、删除协调及原reload逻辑保持。冻结`kaggle/source`、原始–17包、正式HEAD与15文件不改。

实现合同：

1. **开始时捕获输入**：在现有短档案锁内捕获完整规范化JSON、全部候选WAV、当前锚点、可选质心字节及目录身份。最多24候选，聚合文件64MiB；这是逻辑文件预算，不是总RSS，副本／重新核验另占内存。
2. **评估只使用捕获内容**：每个临时profile的anchor由捕获字节建立，不在后续评分时重新读取可能已变化的候选路径。
3. **提交前检查**：同一短锁内重新捕获并核对输入，再写入校准／锚点。真实HTTP候选／转写编辑、候选同名bytes变化、参数／质心变化、删除或trained状态变化后返回409，旧评分不被保存，不复活已删除档案。
4. **ABA版本**：候选／转写实际发生变化时写修订nonce，改回相同内容仍可检测。完全相同的重复选择不改变修订，保持幂等，不制造假冲突。
5. **校准互斥**：同档案只允许一个在途校准，第二个409；不同档案可推进。互斥范围只是本分析服务进程，不冒充跨进程锁或真实GPU／ASR线程安全。
6. **临时资源**：每次运行独立随机ID，长度不超过40；700目录，内容地址临时anchor；只删除自己成功创建的目录，设置／评估异常也走清理，ASR释放置于finally。临时ID隔离与同档案互斥共同消除已测组合的目录复用问题。
7. **提交失败**：沿用S1内容地址锚点，注入JSON提交失败时保留旧元数据／字节，清理本次未提交锚点，校准占用可释放并重试。
8. **可追溯**：成功校准回执增加`input_version`内容摘要。它不是身份认证、相似度或声音质量分数；nonce也不是模型条件融合。

不持档案锁跨合成、ASR或worker网络等待。当前协作入口可保证检查和提交协调，但外部／跨进程／其他不遵守本锁的写入仍可能在终检后改状态；原创建过程末尾质量合并等未全纳入本合同，不称完整全局事务。目录身份不是对恶意文件系统ABA的绝对保证。

## 2. 同合同修复前后对照

在改代码前，将S1实际源码、README、origin及旧活跃交接等逐字节保存至`docs/validation/step18/s2-before/`，原路径／档案／SHA见`s2-before-index.json`。不是把冻结17当成S1，也不是从修复后代码伪造旧版本。

同一份最终`test_step18_calibration_state.py`：

- 归档S1：22方法，21条失败记录，0 error，0 skip。失败记录含临时清理的tearDown断言，不是21个独立缺陷。
- 当前S2候选首次预检：22/22 PASS，failure/error/skip均0。
- 两份JSON记录相同测试文件SHA，以及各自目标源码SHA。旧stdout和结构化结果保留，不覆盖。

具体合同涵盖：稳定成功；真实候选＋文本编辑；单独候选／文本编辑；两类ABA；同名候选bytes、质心与生成参数变化；真实DELETE；自有trained元数据变化；同档案第二校准拒绝；多次运行独立临时ID；评估途中改变活文件而试验仍用旧捕获字节；JSON提交失败／ASR释放失败后的状态和重试；临时设置失败清理；两项预算；不安全候选路径；幂等选择；不同档案受控并行。

所有场景经单Uvicorn事件循环、httpx真实环回TCP。HEAVY执行器中的Event控制交错，事件循环继续接收编辑／删除，不是阻塞事件循环后伪造并发，也不是多server压力。worker传输、合成、ASR与说话人分数明确fixture。文件bytes／参数／质心／trained变化为自有文件测试，不是HTTP上传、真实adapter发布或远程利用证明。

## 3. 三轮工程回归实际结果

- **500×3＝1500 PASS**，每轮failure/error/skip均0。
- 组成：旧450项仍指向冻结17；S1旧28项在当前S2候选上重跑；新增22项指向当前S2候选。不能把500项合计当完整新运行时／模型全功能验证。
- 旧478逐ID／结果保留，冻结缺陷25组观察继续保留；不悄悄改旧缺陷期望为“已修”。
- 每轮198真实TCP＝旧159＋S2新39，三轮594；其中S2新增117。
- 新39／轮状态：200×22、409×12、500×2、400×1、413×2。两个500来自注入提交／ASR释放失败；200中包含只验证清理的全错误场景，**不表示有效校准**。
- 比较三轮响应时，只对内容摘要`input_version`做格式验证并归一化；修订nonce导致摘要不同是预期。继承S1的删除／reload先后场景不强求固定响应顺序，其余语义／内容核对；不是忽略错误码或放宽合同。
- companions每轮NumPy partition12、trimmer8、CLI4；三项CLI期望blocked，resource gpu_verified=false，不是模型成功。C ABI fixture不是Rust运行。

附加审计／Node／语法／repack与最终独立核验的实际结果见末尾记录，不借用旧批次成绩。

## 4. 明确没有修复的S2事项

**不能把S2-A叫完整S2。** 本批保留原评分公式及以下已知问题，下一步S2-B处理：

- ASR全失败仍可能使用默认CER0.05；部分失败覆盖率不足未显式记录。
- 全候选失败仍可能200/chosen0；失败新校准可能覆盖先前有效报告。
- 非有限得分、空／短／静音生成和各指标有效性尚未完整门禁。
- 临时worker ACK与最终`load_on_workers`回执未完整签收；最终回执仍未决定校准HTTP是否就绪。
- 所有异常／清理IO失败没有穷举；同进程不同profile下实际ASR／模型并发安全未验证。

22项测试通过仅说明列出的状态合同和保护满足；不证明真实评分、同声、无沙沙、首声或T4速度。不得把fixture分数当实测声学指标。

## 5. 建议、历史、环境和交接

原三轮100建议及问题25–28／各50行动保留；本批执行既定S2方案，无新关键选择，不开启问题29。三遍增量复核实际范围见`s2-delta-review.json`：输入快照／提交版本、资源生命周期、回归及验收边界。

11条原建议得到当前候选的直接证据：R1-012/016，R2-031/032/033/034/035/037/039/040/049。测试全ID、三轮收据SHA、HTTP数组下标和限定边界见`s2-recommendation-links.json`。均加强已有75条并集，不重复算新增，不改变原最终／功能签收false。

受保护历史路径1509，1506已有文件SHA匹配、3旧.log仍缺失D02。允许改变的候选及活跃交接先归档再修改，不伪称活源码未变。旧S1封存输出及改前源码仍可核验；旧S1验证器针对当时活源码的限制不被改写。

现有venv复用、无安装，pip freeze与上批逐字节相同；NumPy2.2.6仍非产品要求2.4.6。无Go/race/vet、实际浏览器／clipboard、完整模型、Torch/Qwen、真实训练、双T4、实体麦克风／扬声器、声学或提速新验收。完整交接94份，原17最终交接不覆盖。

## 6. 下一步

直接实现S2-B：缺失指标显式化、有效／完整试验门禁、全失败不选择且保留旧有效状态、最终worker回执的已保存／未就绪语义，然后再跑修复前后对照及三轮回归。未完成前不跳DSP或声学优化，不启用未经验证的多参考融合，不发布18。

可以确保失败对照、实际代码和验证结果可追溯；不能承诺所有模型／声学效果一定成功，也不能用审计通过数计算整体完成率。


## 7. 附加检查与封存记录

附加检查已实际三轮完成：每轮24项审计、Node30项、JS语法与repack检查全部通过，45份Python AST解析通过。封存前独立核验首次通过，核对了归档S1来源、同测试SHA的修复前后对照、三轮500项／旧478继承、当前候选S1／S2的TCP语义、所有引用日志和SHA、建议下标及冻结／历史／环境；原stdout为`s2-seal-preflight-first.txt`。

本批独立清单`s2-run-manifest.json`覆盖104文件（含当前源码和归档S1／交接来源）。完整交接94份逐份内嵌核对。最终封存判据是`verify_s2.py`连续两次实际执行通过且stdout逐字节一致；输出分别保存为`s2-verification-first.txt`与`second.txt`，最终结果以`progress-s2.json`为准，并同步`progress-checks.json`。这些检查只签限定工程证据，不签完整S2、整体G0、模型或声学验收，也不将未发布候选切换为正式18。

---

## 内嵌备忘录：KAGGLE_STEP18_Q29_CALIBRATION_VALIDITY.md

# 问题29：怎样定义可选校准与已保存／未就绪，而不再用缺省分数制造成功？

## 选项、推荐与边界

A：保留CER0.05、只平均成功试验、全错chosen0。拒绝，会把缺失当实测。

B：补一个武断相似度／时长阈值，或以MFCC代理默认高分选最好。拒绝，当前没有真实声音实验支持主观质量阈值，不能靠猜测验收。

C：**完整性门禁与声音质量分开。** 保留已有sim−1.5×CER排序公式，但候选只有全部既定目标试验成功、指标有限且来源合格时才有可排序score。逐试验记录缺失null、阶段错误码、预期／有效数；ECAPA不可用或质心缺失时不以代理当可靠声纹。无完整候选则422、chosen=null、reference_saved=false，不写档案、不覆盖旧有效结果。可选时保存选择证据，再检查临时及最终worker同pin确认；最终失败503、reference_saved=true、ready=false，不回滚已提交的锚点。200仅表示本次工程加载确认通过，不是声学达标。

D：任何失败都回滚磁盘和各卡提示。拒绝，网络加载可能部分完成，不能伪装成可原子回滚的分布式事务。

**选择C。** 这是本批新的关键API／有效性决定，按顺序先完成本题50行动，再实施，不询问用户、不预填问题30。沿用原Q25–28、3×100建议和S2-A快照／冲突合同。相对排序没有质量最低线；短时长策略、漏添字／真实听感阈值仍需实验，不自行填数。仅拒绝空、非有限、非法形状／幅度及全零PCM；不把这个数值检查叫“有效人声”或“自然朗读”。

成功响应继续是已保存的选择报告，兼容旧S2-A的报告结构和磁盘／HTTP一致断言。就绪是本次加载检查结果，不提前写进选择报告冒持久就绪；失败响应显式附未就绪与已保存标记。后台可选校准记录精简状态，不把创建成功称校准成功。

## 进入下一题前的50项行动

1. 核对固定活动分支。
2. 改前逐字节归档S2-A源码及交接。
3. 保留S2-A全部收据和3缺失日志期待。
4. 不改冻结17／正式HEAD／复制页。
5. 新测试使用同一合同对照归档S2-A和新候选。
6. 保留原500项方法及断言。
7. 继续在当前候选重跑S1与S2-A合同。
8. 为每个CAL_TEXTS目标建立独立试验条目。
9. 记录目标索引和实际seed，不公开私有转写。
10. 保存预期试验数和实际有效数。
11. 缺失speaker指标为null。
12. 缺失CER为null，不填0.05。
13. ASR失败记录固定阶段码，不输出异常原文。
14. 空假设不能冒充一次成功ASR。
15. 非有限CER不参与选择。
16. 非有限声纹不参与选择。
17. 声纹方法明确记录，不把MFCC代理当ECAPA。
18. 质心缺失／损坏不填相似度0当实测。
19. 部分试验缺失仍保留已测指标及覆盖率。
20. 不完整候选score=null，排除max。
21. 全部目标完整才计算原排序公式。
22. 没有合格候选时chosen=null。
23. 无候选时HTTP422并明确reference_saved=false。
24. 无候选时不写新锚点或calibration字段。
25. 保留以前有效的选择／校准证据。
26. 某候选失败不阻止其他完整候选参与排序。
27. 空PCM失败并记录synthesis阶段。
28. NaN／Infinity PCM失败。
29. 非一维或非实数PCM失败。
30. 全零PCM失败，但不声称已测噪声或语音质量。
31. 不武断加入未经声学验证的最短时长阈值。
32. 每个临时worker加载检查HTTP状态。
33. 临时worker必须ok严格true并确认匹配pin。
34. 临时加载失败不执行该候选合成。
35. 设置失败为所有预期试验记录固定错误。
36. 继续ASR finally及仅清理自有临时目录。
37. 评分有效性不绕过S2-A提交冲突409。
38. 提交后不持档案锁等待worker网络。
39. 检查最终worker数量和每项确认。
40. 最终回执错误／空／异常时明确未就绪。
41. 对外worker错误采用固定码，不回显供应商正文。
42. 最终重核已提交版本仍存在且未被修改。
43. 保存后加载失败返回503和reference_saved=true。
44. 不虚构把各卡提示和磁盘一起回滚。
45. 成功报告加quality_verified=false避免质量误读。
46. 后台可选校准记录状态，不静默吞掉未选出结果。
47. 公共校准500响应不泄露异常原文。
48. 三条路线复核：数值完整性、状态／就绪、兼容／隐私。
49. 三轮完整工程回归及独立两次封存，不覆盖失败日志。
50. 更新完整交接并明确剩余真实模型／设备／声学与短时长门禁，再考虑问题30。

50条是实施清单，不自动意味着全部验收。实际实现和限定验证以S2-B报告为准；未发布、未部署、真实模型与声音仍PARTIAL/BLOCKED。

---

## 内嵌备忘录：KAGGLE_STEP18_S2_VALIDITY.md

# S2-B：有效校准指标、无候选保旧与加载就绪的实际修复

## 本批结论

**隔离18候选已有实际S1、S2-A及本批S2-B代码，不只是增加观察。** 新增`step18_calibration_metrics.py`，相对归档S2-A的分析服务仅修改`build_profile`、`calibrate_profile`、`calibrate`；其余命名定义AST相同。冻结17、正式工作台与默认复制入口保持，候选未发布、未部署。

**整体仍PARTIAL/BLOCKED。** 完整产品、真实模型／双T4、训练、声学、首声和RTF未验收；不能承诺一定成功。S2主要预定状态／评分合同已在限定候选中实现，但全局并发写者、任意IO故障、真实短音与质量门禁等仍在，不称完整S2或全功能通过。

Q29在实施前按顺序完成四选项、推荐C及50行动，完整见`KAGGLE_STEP18_Q29_CALIBRATION_VALIDITY.md`。原Q25–28及原3×100保留，问题30未开。

## 1. 实际改正的行为

| 以前行为 | 当前候选合同 |
|---|---|
| ASR缺失仍填CER0.05 | 缺失为null，逐目标固定阶段码、预期／有效数、speaker／ASR覆盖率明确保存 |
| 只平均成功试验、隐藏缺失 | 只有全部目标完整且指标有限才可排序；不完整候选score=null |
| 代理或缺质心仍给相似度默认值 | ECAPA未确认、无／坏质心时不冒可靠声纹指标；质量仍未验证 |
| 全部失败仍200/chosen0、覆盖旧报告 | 422、chosen=null、reference_saved=false，不写新锚点／档案，保留旧证据 |
| 临时worker只看truthy ok | 检查HTTP状态、严格ok=true、匹配参考pin后才执行合成 |
| 丢弃最终加载失败回执 | 选择先提交，再核对两worker与已保存输入版本；失败503、已保存但未就绪 |
| 保存后再被改／删仍可能正常返回 | 503并给saved_version_current=false；reference_saved表示历史曾提交，不表示当前文件仍存在 |
| 校准错误可能回显异常正文 | 对外固定阶段错误码、worker状态和泛化500，不回显私有异常／供应商正文 |
| 后台可选校准返回未被区分 | 记录精简状态摘要；创建成功不等于校准有效／两卡已就绪 |

保持原`sim−1.5×CER`相对排序公式，不新增未经真实实验支持的相似度最低线或最短音阈值。数值检查拒绝空、非一维、非实数、非有限、全零及幅度非法PCM，但**不能把通过这些检查叫正确人声、无漏字或自然朗读**。部分候选失败不阻止其他完整候选。

成功HTTP200只在本次两卡工程回执及保存版本确认后返回；成功body仍等于磁盘选择报告，包含`quality_verified=false`。选择报告不提前持久化ready=true来冒后续永久就绪。503不伪造分布式回滚；用户后续需显式重试激活，不能混会话。

后台摘要接入按源码／辅助逻辑复核，**本批没有完整执行真实建档流程**。公共校准错误脱敏不等于全产品日志／全部入口隐私已验收。

## 2. 同合同修复前后对照

S2-A改动前的源码、README、origin及活跃交接等已逐字节归档至`s2b-before`，路径与SHA见`s2b-before-index.json`。这是真实改前来源，不是拿冻结17冒充S2-A。

最终同一份`test_step18_calibration_validity.py`的23项方法：

- 归档S2-A：**36条失败记录、0 error、0 skip**。含参数化子用例，不是36个独立缺陷。
- 当前候选预检：**23/23 PASS，failure/error/skip均0**。
- 两份JSON记录相同测试SHA和各自目标源码SHA，最终对照为`s2b-red-final2`与`s2b-precheck-final2`。

23项覆盖完整选择、全ASR失败、部分ASR覆盖率、缺失高分不能压过完整候选、空／坏ASR假设、全合成失败保旧、单候选失败、NaN/Inf指标、代理／坏质心、非法PCM、临时HTTP／错pin、最终失败／空回执／异常、最终加载中真实HTTP编辑／删除、公共异常脱敏、可恢复重试与JSON提交失败保旧。

全走单Uvicorn事件循环及真实环回TCP；worker网络、合成、ASR、声纹均明确fixture，非Go鉴权代理／浏览器／真实模型。旧有效报告是自有fixture，不冒真声音证据；私有字符串也是合成sentinel，没有真实凭据。

## 3. 失败记录与最终重跑，不覆盖历史

1. 首红对照34失败＋1 KeyError，因为旧报告不存在新合同字段；增加`assertIn`使缺字段成为明确断言失败，不降低合同。原stdout／JSON留档；随后35失败、0 error。
2. 初三轮523项均通过后，增量复核用受控int16最小值发现`abs(-32768)`溢出会错误通过幅度检查。该路径为自有数值fixture，不证明实际provider输出了整数PCM。
3. 改为min/max范围比较并加入整数边界子用例，最终旧版对照36失败、候选23通过。**重新执行最终源码完整三轮**，使用`s2b-final-*`新名字；初轮不覆盖、不与最终通过数混算。
4. 初S2-B的helper／测试源码副本按已记录SHA进行确定性逆变换重建，严格核对初轮收据，并明确不是事前快照。真正事前S2-A档案不受影响。见`s2b-initial-source`、`s2b-integer-pcm-exploration.txt`与`execution-notes`。
5. README更新曾因预期空格边界不匹配而断言失败，代码／测试未失败；精确替换后完成，元数据记录保留。

## 4. 最终三轮工程验证

- **523×3＝1569 PASS**，每轮failure/error/skip均0。
- 组成：450冻结17控制；S1旧28＋S2-A旧22在当前S2-B候选重跑；新增23当前候选合同。不能把523合计冒完整新产品验收。
- 原500方法／结果逐ID继承，旧25组冻结缺陷观察保留，不改旧方法或断言。
- S2-A成功校准报告新增有效性字段，临时设置全错由200改422，这是本批有意修复；不声称旧响应字节完全一致。成功磁盘／HTTP一致和其他原合同保持。
- 最终每轮237 TCP，三轮711；其中S2-B新39/轮、合计117。新39状态为422×26、200×6、503×5、500×2；错误码多为预期拒绝／故障注入，不是39次产品功能成功。
- 比较三轮时只归一化格式验证过的内容版本摘要，并保留继承S1删除／reload先后的已声明不确定性，其余内容核对；不忽略状态差异。
- 每轮companion：NumPy partition12、trimmer8、CLI4，三项CLI期望blocked，resource gpu_verified=false；C ABI fixture不是Rust运行。

附加审计／Node／语法／冻结与独立封存的实际结果见末尾，不借用旧批次成绩。

## 5. 原建议、进度与冻结边界

本批12条原建议有当前实现限定链接：R2-041–050、061/062。每条有原文、精确测试ID、三轮收据SHA、HTTP下标和边界。

部分证据并集75→81，新增进入集合的是R2-042/044/045/046/047/048。**81/300＝27%仅证据覆盖，不是整体完成率。** R2-047只补数值非法PCM，不签真实极短／漏字策略；R2-050只补校准公共错误，不签全日志。原300条最终／功能签收仍0；这与本批限定候选代码已实现不矛盾。

受保护历史路径1609、已有1606 SHA匹配、3旧.log仍缺，D02未关闭。允许变化的候选及活跃交接先归档，冻结53源／94文件／正式15文件／HEAD／17包不动。不运行旧生成器，只repack --check。

现有venv复用，无依赖安装，freeze与前批逐字节相同，NumPy仍2.2.6非目标2.4.6。本批无Go/race/vet、实浏览器／clipboard、Torch/Qwen／权重、真实训练／双T4、实体音频、声音质量或速度实测。完整交接96份，默认仍17，18未发布。

## 6. 下一步

进入隔离候选S3的可复现数值修复：先修NumPy分块淡入／RMS状态一致性，保留样本数、限幅及增益预算，Rust对照需要实际编译和独立证据。不得以数值修复推断用户沙沙根因。

S2跨进程／不合作创建写者、短音／质量阈值及真实模型载入门禁继续保留。自然朗读、全部候选conditioning透明、generated-only PCM、真实长训练、更快真实首声、双T4等效参数与RTF≤0.3仍未豁免；不能承诺一定成功或用工程通过数代替这些验收。


## 7. 附加检查与封存记录

最终附加检查已实际三轮完成：每轮24项审计、Node30、JS语法与repack全部通过，47份Python AST解析通过。封存前独立复核首次通过，核对真实改前来源、同测试SHA红绿对照、最终三轮523／旧500继承、新无候选和就绪响应语义、所有引用日志／SHA、原建议下标、冻结／历史／环境；stdout保存在`s2b-seal-preflight-first.txt`。

独立清单`s2b-run-manifest.json`覆盖163文件，包含初轮和最终日志、当前代码、真实S2-A档案及明确标识的初S2-B重建源码。完整交接96份逐份内嵌核对。最终封存判据为`verify_s2b.py`连续两次执行通过且stdout逐字节一致；实际输出分别保存为`s2b-verification-first.txt`与`second.txt`，最终状态以`progress-s2b.json`为准并同步`progress-checks.json`。审计通过不签完整产品／模型／声学，也不把未发布候选切换为正式18。

---

## 内嵌备忘录：KAGGLE_STEP18_Q30_DSP_PARTITION.md

# Q30：如何真正修复 S3 分块状态，而不改冻结 17？

## 顺序专业自问自答
本问题承接已封存 Q29。下个问题必须等待本题至少 50 项可操作建议写完；不向用户索要 Continue。

- A：仅补淡入计数。改动少，但 RMS 余数丢失和非因果增益仍在，拒绝。
- B：要求模型固定输出大块。掩盖分块依赖并可能拖慢首声，拒绝。
- **C（采用）**：独立 18 候选采用逐样本因果状态，明确连接隔离 worker；先测实际 CPU 开销再决定是否需要额外加速语言，不引入未测 JIT 编译延迟。
- D：只换 Rust 并宣称等效。当前没有 Rust 工具链且 f32/量化/参数语义不同，没有实测依据，拒绝。

## 合同与修正理由
保持冻结代码与正式工作台不变。新模块的 process 不缓存 PCM，输出长度严格等于输入；DC、固定网格 RMS、逐样本增益和淡入坐标跨调用保存。采用与冻结 Rust 因果设计相近的 10ms RMS／30ms attack／600ms release／-46dB 门限，但 Python float64 状态和 ties-to-even 量化不等于 Rust f32 位级一致，绝不借 ABI fixture 宣称 Rust 验收。有效配置保持既有默认值；非法/非有限配置、负长度明确拒绝。flush(0) 无副作用，正 flush 清 DC/last，保留 RMS/gain/env/fade。淡入首样本为零，最后一个淡入样本仍小于 1，随后恢复 1；重启段显式重新淡入。新增关闭生命周期保护。

这是隔离候选的行为纠正，会改变旧 NumPy 整段结果；旧 NumPy 不是正确输出 oracle。不把分块一致性等同于去沙沙、自然朗读或相似度改善。完整 TTS 产品、双 T4、真实训练和发布仍 blocked。

## 本题 50 项行动
1. 核验当前 arena 分支，禁止换支。
2. 归档会变化的 S2-B 文档和交接。
3. 保存冻结 DSP/worker/Rust 的改前 SHA。
4. 串联旧保护表并保留三条历史缺件，不补造。
5. 重建已消失的 venv，保存安装日志。
6. 比较新旧 pip freeze，记录 Python/工具可用性。
7. 冻结 17 和正式工作台零修改。
8. 把 18 DSP 置于独立模块名，避免 sys.modules 污染。
9. 提供隔离 worker 文件而不改冻结 worker。
10. 为候选 worker 加冻结公共依赖搜索路径。
11. 把淡入总长和剩余位置分开保存。
12. 用绝对已消耗位置计算余弦淡入。
13. 支持跨 1 样本调用完成淡入。
14. 定义 start_segment(0) 和重复 start_segment。
15. 按采样率四舍五入计算 10ms 窗长。
16. 持久化 RMS 平方和及样本计数。
17. 只在完整固定网格窗口结束学习。
18. 禁用基于整次调用未来数据的增益插值。
19. 保留 DC 前样本与前输出。
20. 采用逐样本 30ms attack/600ms release。
21. 显式记录 -46dB 门限和与旧 NumPy 的差异。
22. 夹限期望增益并验证当前增益预算。
23. 使用 float64 标量状态，float32 输入，int16 输出。
24. 定义 ties-to-even 量化，不声称 Rust 位等同。
25. 对非有限样本等价置零。
26. 不修改只读或步进输入。
27. 逐块返回相同数量 PCM，无输出缓存等待窗口。
28. 严格限定 soft limiter 的幅度预算。
29. 定义正 flush 仅输出显式尾长。
30. 正 flush 清 DC/last、保留学习态。
31. 零 flush 不推进状态。
32. 负 flush 明确拒绝。
33. 关闭后拒绝处理，close 幂等。
34. 构造器拒绝非有限与超界配置而不是隐式放行。
35. 修正实现边界：冻结 ABI bridge 保持原样；新隔离 DSP 只启用明确标识的 NumPy 因果实现，不自动装载未验收的 Rust 库。
36. 以改前 DSP 执行相同数值合同，保存红结果。
37. 以独立参考递推验证指定波形输出。
38. 逐样本、固定短块、不规则与随机切分严格比较。
39. 比较整段与分块最终 gain/env/内部状态。
40. 验证相同前缀面对不同未来输出不变。
41. 通过实际候选 worker run_job 发出 PCM 帧。
42. 验证 worker 关闭并替换旧 leveler。
43. 验证取消、错误与 generated-only 控制仍保留。
44. 用冻结 DSP 与候选同机测 CPU 成本。
45. 记录基准仅为合成 DSP 而非模型 RTF。
46. 保留全部 523 旧合同并跑三轮最终组合。
47. 三轮执行审计、Node、JS、repack 与语法检查。
48. 新增独立封存 verifier 并连续两次核验。
49. 更新计划、报告、交接并保存最终整合提示。
50. 按证据报告进展；真实听感、训练、T4、首声和完整发布仍未验收。

## 实施前边界修正
当前没有 Rust 工具链，因此候选不复制 ABI 自动选择代码。新 worker 明确使用 `numpy-causal-v1`，冻结 Rust bridge 原样保留但不接入本候选。避免使用新 NumPy 合同为未测 native 分支背书；与原计划“保留 bridge”相比，缩小发布面更可靠。

---

## 内嵌备忘录：KAGGLE_STEP18_S3_REVIEW_R1.md

# S3 R1：状态与因果复核（100 条建议）

这些是实施前检查与建议，不是 100 项通过收据。合成输入与替身引擎不代表真实声音、训练、GPU 或 Rust 验收。

1. **S3-R1-001｜淡入绝对位置／单次处理**：条件：剩余不足一段淡入时继续处理；操作：保存 fade_total/left，禁止每次调用从零重启；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
2. **S3-R1-002｜淡入绝对位置／固定短块**：条件：剩余不足一段淡入时继续处理；操作：保存 fade_total/left，禁止每次调用从零重启；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
3. **S3-R1-003｜淡入绝对位置／不规则余数**：条件：剩余不足一段淡入时继续处理；操作：保存 fade_total/left，禁止每次调用从零重启；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
4. **S3-R1-004｜淡入绝对位置／空块交错**：条件：剩余不足一段淡入时继续处理；操作：保存 fade_total/left，禁止每次调用从零重启；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
5. **S3-R1-005｜淡入零长度／单次处理**：条件：start_segment(0) 后处理非零样本；操作：不加包络、不除零；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
6. **S3-R1-006｜淡入零长度／固定短块**：条件：start_segment(0) 后处理非零样本；操作：不加包络、不除零；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
7. **S3-R1-007｜淡入零长度／不规则余数**：条件：start_segment(0) 后处理非零样本；操作：不加包络、不除零；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
8. **S3-R1-008｜淡入零长度／空块交错**：条件：start_segment(0) 后处理非零样本；操作：不加包络、不除零；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
9. **S3-R1-009｜淡入单样本／单次处理**：条件：淡入总长为一时；操作：按约定首样本零、随后恢复，不延长样本流；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
10. **S3-R1-010｜淡入单样本／固定短块**：条件：淡入总长为一时；操作：按约定首样本零、随后恢复，不延长样本流；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
11. **S3-R1-011｜淡入单样本／不规则余数**：条件：淡入总长为一时；操作：按约定首样本零、随后恢复，不延长样本流；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
12. **S3-R1-012｜淡入单样本／空块交错**：条件：淡入总长为一时；操作：按约定首样本零、随后恢复，不延长样本流；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
13. **S3-R1-013｜重复段开始／单次处理**：条件：未完成淡入再次 start_segment；操作：显式重新开始淡入，保留已学习增益和 RMS；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
14. **S3-R1-014｜重复段开始／固定短块**：条件：未完成淡入再次 start_segment；操作：显式重新开始淡入，保留已学习增益和 RMS；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
15. **S3-R1-015｜重复段开始／不规则余数**：条件：未完成淡入再次 start_segment；操作：显式重新开始淡入，保留已学习增益和 RMS；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
16. **S3-R1-016｜重复段开始／空块交错**：条件：未完成淡入再次 start_segment；操作：显式重新开始淡入，保留已学习增益和 RMS；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
17. **S3-R1-017｜RMS 余数／单次处理**：条件：每次调用少于 10ms；操作：跨调用保留平方和与计数，窗口结束才学习；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
18. **S3-R1-018｜RMS 余数／固定短块**：条件：每次调用少于 10ms；操作：跨调用保留平方和与计数，窗口结束才学习；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
19. **S3-R1-019｜RMS 余数／不规则余数**：条件：每次调用少于 10ms；操作：跨调用保留平方和与计数，窗口结束才学习；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
20. **S3-R1-020｜RMS 余数／空块交错**：条件：每次调用少于 10ms；操作：跨调用保留平方和与计数，窗口结束才学习；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
21. **S3-R1-021｜RMS 边界／单次处理**：条件：长度等于窗口及窗口±1；操作：使用固定样本网格，不按调用重置窗口；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
22. **S3-R1-022｜RMS 边界／固定短块**：条件：长度等于窗口及窗口±1；操作：使用固定样本网格，不按调用重置窗口；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
23. **S3-R1-023｜RMS 边界／不规则余数**：条件：长度等于窗口及窗口±1；操作：使用固定样本网格，不按调用重置窗口；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
24. **S3-R1-024｜RMS 边界／空块交错**：条件：长度等于窗口及窗口±1；操作：使用固定样本网格，不按调用重置窗口；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
25. **S3-R1-025｜因果前缀／单次处理**：条件：相同前缀接不同未来信号；操作：前缀 PCM 和前缀状态相同，不用 np.interp 未来信息；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
26. **S3-R1-026｜因果前缀／固定短块**：条件：相同前缀接不同未来信号；操作：前缀 PCM 和前缀状态相同，不用 np.interp 未来信息；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
27. **S3-R1-027｜因果前缀／不规则余数**：条件：相同前缀接不同未来信号；操作：前缀 PCM 和前缀状态相同，不用 np.interp 未来信息；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
28. **S3-R1-028｜因果前缀／空块交错**：条件：相同前缀接不同未来信号；操作：前缀 PCM 和前缀状态相同，不用 np.interp 未来信息；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
29. **S3-R1-029｜增益攻击／单次处理**：条件：大于所需增益的前态；操作：逐样本使用 30ms 系数；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
30. **S3-R1-030｜增益攻击／固定短块**：条件：大于所需增益的前态；操作：逐样本使用 30ms 系数；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
31. **S3-R1-031｜增益攻击／不规则余数**：条件：大于所需增益的前态；操作：逐样本使用 30ms 系数；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
32. **S3-R1-032｜增益攻击／空块交错**：条件：大于所需增益的前态；操作：逐样本使用 30ms 系数；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
33. **S3-R1-033｜增益释放／单次处理**：条件：小于所需增益的前态；操作：逐样本使用 600ms 系数；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
34. **S3-R1-034｜增益释放／固定短块**：条件：小于所需增益的前态；操作：逐样本使用 600ms 系数；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
35. **S3-R1-035｜增益释放／不规则余数**：条件：小于所需增益的前态；操作：逐样本使用 600ms 系数；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
36. **S3-R1-036｜增益释放／空块交错**：条件：小于所需增益的前态；操作：逐样本使用 600ms 系数；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
37. **S3-R1-037｜增益预算／单次处理**：条件：很小且通过门限的信号；操作：期望增益与当前增益均在明确上下限内；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
38. **S3-R1-038｜增益预算／固定短块**：条件：很小且通过门限的信号；操作：期望增益与当前增益均在明确上下限内；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
39. **S3-R1-039｜增益预算／不规则余数**：条件：很小且通过门限的信号；操作：期望增益与当前增益均在明确上下限内；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
40. **S3-R1-040｜增益预算／空块交错**：条件：很小且通过门限的信号；操作：期望增益与当前增益均在明确上下限内；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
41. **S3-R1-041｜静音门限／单次处理**：条件：零、低于门限、超过门限；操作：低于门限不学习噪声，使用 -46dB RMS 门限；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
42. **S3-R1-042｜静音门限／固定短块**：条件：零、低于门限、超过门限；操作：低于门限不学习噪声，使用 -46dB RMS 门限；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
43. **S3-R1-043｜静音门限／不规则余数**：条件：零、低于门限、超过门限；操作：低于门限不学习噪声，使用 -46dB RMS 门限；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
44. **S3-R1-044｜静音门限／空块交错**：条件：零、低于门限、超过门限；操作：低于门限不学习噪声，使用 -46dB RMS 门限；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
45. **S3-R1-045｜DC 连续性／单次处理**：条件：常量偏置在任意点切开；操作：保存上一输入/输出，不在 process 边界重置；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
46. **S3-R1-046｜DC 连续性／固定短块**：条件：常量偏置在任意点切开；操作：保存上一输入/输出，不在 process 边界重置；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
47. **S3-R1-047｜DC 连续性／不规则余数**：条件：常量偏置在任意点切开；操作：保存上一输入/输出，不在 process 边界重置；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
48. **S3-R1-048｜DC 连续性／空块交错**：条件：常量偏置在任意点切开；操作：保存上一输入/输出，不在 process 边界重置；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
49. **S3-R1-049｜非有限输入／单次处理**：条件：NaN、正负无穷混入；操作：等价于对应样本置零，不传播非有限状态；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
50. **S3-R1-050｜非有限输入／固定短块**：条件：NaN、正负无穷混入；操作：等价于对应样本置零，不传播非有限状态；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
51. **S3-R1-051｜非有限输入／不规则余数**：条件：NaN、正负无穷混入；操作：等价于对应样本置零，不传播非有限状态；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
52. **S3-R1-052｜非有限输入／空块交错**：条件：NaN、正负无穷混入；操作：等价于对应样本置零，不传播非有限状态；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
53. **S3-R1-053｜空块／单次处理**：条件：任意处理间插入空块；操作：返回零样本且不推进任何状态；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
54. **S3-R1-054｜空块／固定短块**：条件：任意处理间插入空块；操作：返回零样本且不推进任何状态；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
55. **S3-R1-055｜空块／不规则余数**：条件：任意处理间插入空块；操作：返回零样本且不推进任何状态；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
56. **S3-R1-056｜空块／空块交错**：条件：任意处理间插入空块；操作：返回零样本且不推进任何状态；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
57. **S3-R1-057｜非连续输入／单次处理**：条件：步进视图与连续副本；操作：结果一致且不修改输入；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
58. **S3-R1-058｜非连续输入／固定短块**：条件：步进视图与连续副本；操作：结果一致且不修改输入；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
59. **S3-R1-059｜非连续输入／不规则余数**：条件：步进视图与连续副本；操作：结果一致且不修改输入；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
60. **S3-R1-060｜非连续输入／空块交错**：条件：步进视图与连续副本；操作：结果一致且不修改输入；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
61. **S3-R1-061｜采样率／单次处理**：条件：8k、24k、44.1k、48k；操作：依采样率计算固定 RMS 网格与时间常数；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
62. **S3-R1-062｜采样率／固定短块**：条件：8k、24k、44.1k、48k；操作：依采样率计算固定 RMS 网格与时间常数；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
63. **S3-R1-063｜采样率／不规则余数**：条件：8k、24k、44.1k、48k；操作：依采样率计算固定 RMS 网格与时间常数；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
64. **S3-R1-064｜采样率／空块交错**：条件：8k、24k、44.1k、48k；操作：依采样率计算固定 RMS 网格与时间常数；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
65. **S3-R1-065｜正尾刷新／单次处理**：条件：flush(192) 后再次处理；操作：输出明确尾长，清 DC/last，保留其他学习态；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
66. **S3-R1-066｜正尾刷新／固定短块**：条件：flush(192) 后再次处理；操作：输出明确尾长，清 DC/last，保留其他学习态；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
67. **S3-R1-067｜正尾刷新／不规则余数**：条件：flush(192) 后再次处理；操作：输出明确尾长，清 DC/last，保留其他学习态；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
68. **S3-R1-068｜正尾刷新／空块交错**：条件：flush(192) 后再次处理；操作：输出明确尾长，清 DC/last，保留其他学习态；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
69. **S3-R1-069｜零尾刷新／单次处理**：条件：flush(0) 在流中间；操作：无输出且不改状态；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
70. **S3-R1-070｜零尾刷新／固定短块**：条件：flush(0) 在流中间；操作：无输出且不改状态；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
71. **S3-R1-071｜零尾刷新／不规则余数**：条件：flush(0) 在流中间；操作：无输出且不改状态；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
72. **S3-R1-072｜零尾刷新／空块交错**：条件：flush(0) 在流中间；操作：无输出且不改状态；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
73. **S3-R1-073｜负尾刷新／单次处理**：条件：flush(-1)；操作：明确 ValueError，不以空数组掩盖调用错误；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
74. **S3-R1-074｜负尾刷新／固定短块**：条件：flush(-1)；操作：明确 ValueError，不以空数组掩盖调用错误；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
75. **S3-R1-075｜负尾刷新／不规则余数**：条件：flush(-1)；操作：明确 ValueError，不以空数组掩盖调用错误；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
76. **S3-R1-076｜负尾刷新／空块交错**：条件：flush(-1)；操作：明确 ValueError，不以空数组掩盖调用错误；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
77. **S3-R1-077｜尾部限幅／单次处理**：条件：最后样本接近限幅；操作：尾样本也保持安全幅度，无参考 PCM 拼接；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
78. **S3-R1-078｜尾部限幅／固定短块**：条件：最后样本接近限幅；操作：尾样本也保持安全幅度，无参考 PCM 拼接；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
79. **S3-R1-079｜尾部限幅／不规则余数**：条件：最后样本接近限幅；操作：尾样本也保持安全幅度，无参考 PCM 拼接；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
80. **S3-R1-080｜尾部限幅／空块交错**：条件：最后样本接近限幅；操作：尾样本也保持安全幅度，无参考 PCM 拼接；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
81. **S3-R1-081｜关闭生命周期／单次处理**：条件：重复 close 或已关闭后调用；操作：close 幂等，其他操作明确拒绝；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
82. **S3-R1-082｜关闭生命周期／固定短块**：条件：重复 close 或已关闭后调用；操作：close 幂等，其他操作明确拒绝；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
83. **S3-R1-083｜关闭生命周期／不规则余数**：条件：重复 close 或已关闭后调用；操作：close 幂等，其他操作明确拒绝；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
84. **S3-R1-084｜关闭生命周期／空块交错**：条件：重复 close 或已关闭后调用；操作：close 幂等，其他操作明确拒绝；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
85. **S3-R1-085｜worker 模块绑定／单次处理**：条件：冻结 audio_rt 已在 sys.modules；操作：候选显式导入 step18_audio_rt，禁止导入缓存劫持；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
86. **S3-R1-086｜worker 模块绑定／固定短块**：条件：冻结 audio_rt 已在 sys.modules；操作：候选显式导入 step18_audio_rt，禁止导入缓存劫持；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
87. **S3-R1-087｜worker 模块绑定／不规则余数**：条件：冻结 audio_rt 已在 sys.modules；操作：候选显式导入 step18_audio_rt，禁止导入缓存劫持；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
88. **S3-R1-088｜worker 模块绑定／空块交错**：条件：冻结 audio_rt 已在 sys.modules；操作：候选显式导入 step18_audio_rt，禁止导入缓存劫持；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
89. **S3-R1-089｜worker 实际调用／单次处理**：条件：真实 run_job 接合成 engine；操作：捕获实际 Leveler.process/flush 返回的 PCM 与帧计数；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
90. **S3-R1-090｜worker 实际调用／固定短块**：条件：真实 run_job 接合成 engine；操作：捕获实际 Leveler.process/flush 返回的 PCM 与帧计数；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
91. **S3-R1-091｜worker 实际调用／不规则余数**：条件：真实 run_job 接合成 engine；操作：捕获实际 Leveler.process/flush 返回的 PCM 与帧计数；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
92. **S3-R1-092｜worker 实际调用／空块交错**：条件：真实 run_job 接合成 engine；操作：捕获实际 Leveler.process/flush 返回的 PCM 与帧计数；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
93. **S3-R1-093｜性能边界／单次处理**：条件：1 样本、240 样本、整段调用；操作：记录 CPU 秒与样本数，禁止作为首声或模型 RTF 证据；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
94. **S3-R1-094｜性能边界／固定短块**：条件：1 样本、240 样本、整段调用；操作：记录 CPU 秒与样本数，禁止作为首声或模型 RTF 证据；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
95. **S3-R1-095｜性能边界／不规则余数**：条件：1 样本、240 样本、整段调用；操作：记录 CPU 秒与样本数，禁止作为首声或模型 RTF 证据；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
96. **S3-R1-096｜性能边界／空块交错**：条件：1 样本、240 样本、整段调用；操作：记录 CPU 秒与样本数，禁止作为首声或模型 RTF 证据；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
97. **S3-R1-097｜封存边界／单次处理**：条件：旧收据绑定活动文档；操作：事前复制可变文档，旧源码和收据只读保留；在“单次处理”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
98. **S3-R1-098｜封存边界／固定短块**：条件：旧收据绑定活动文档；操作：事前复制可变文档，旧源码和收据只读保留；在“固定短块”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
99. **S3-R1-099｜封存边界／不规则余数**：条件：旧收据绑定活动文档；操作：事前复制可变文档，旧源码和收据只读保留；在“不规则余数”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
100. **S3-R1-100｜封存边界／空块交错**：条件：旧收据绑定活动文档；操作：事前复制可变文档，旧源码和收据只读保留；在“空块交错”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。

---

## 内嵌备忘录：KAGGLE_STEP18_S3_REVIEW_R2.md

# S3 R2：数值与防护复核（100 条建议）

这些是实施前检查与建议，不是 100 项通过收据。合成输入与替身引擎不代表真实声音、训练、GPU 或 Rust 验收。

1. **S3-R2-001｜淡入绝对位置／零和极小输入**：条件：剩余不足一段淡入时继续处理；操作：保存 fade_total/left，禁止每次调用从零重启；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
2. **S3-R2-002｜淡入绝对位置／正常合成波形**：条件：剩余不足一段淡入时继续处理；操作：保存 fade_total/left，禁止每次调用从零重启；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
3. **S3-R2-003｜淡入绝对位置／极值与非有限输入**：条件：剩余不足一段淡入时继续处理；操作：保存 fade_total/left，禁止每次调用从零重启；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
4. **S3-R2-004｜淡入绝对位置／非连续与边界输入**：条件：剩余不足一段淡入时继续处理；操作：保存 fade_total/left，禁止每次调用从零重启；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
5. **S3-R2-005｜淡入零长度／零和极小输入**：条件：start_segment(0) 后处理非零样本；操作：不加包络、不除零；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
6. **S3-R2-006｜淡入零长度／正常合成波形**：条件：start_segment(0) 后处理非零样本；操作：不加包络、不除零；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
7. **S3-R2-007｜淡入零长度／极值与非有限输入**：条件：start_segment(0) 后处理非零样本；操作：不加包络、不除零；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
8. **S3-R2-008｜淡入零长度／非连续与边界输入**：条件：start_segment(0) 后处理非零样本；操作：不加包络、不除零；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
9. **S3-R2-009｜淡入单样本／零和极小输入**：条件：淡入总长为一时；操作：按约定首样本零、随后恢复，不延长样本流；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
10. **S3-R2-010｜淡入单样本／正常合成波形**：条件：淡入总长为一时；操作：按约定首样本零、随后恢复，不延长样本流；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
11. **S3-R2-011｜淡入单样本／极值与非有限输入**：条件：淡入总长为一时；操作：按约定首样本零、随后恢复，不延长样本流；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
12. **S3-R2-012｜淡入单样本／非连续与边界输入**：条件：淡入总长为一时；操作：按约定首样本零、随后恢复，不延长样本流；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
13. **S3-R2-013｜重复段开始／零和极小输入**：条件：未完成淡入再次 start_segment；操作：显式重新开始淡入，保留已学习增益和 RMS；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
14. **S3-R2-014｜重复段开始／正常合成波形**：条件：未完成淡入再次 start_segment；操作：显式重新开始淡入，保留已学习增益和 RMS；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
15. **S3-R2-015｜重复段开始／极值与非有限输入**：条件：未完成淡入再次 start_segment；操作：显式重新开始淡入，保留已学习增益和 RMS；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
16. **S3-R2-016｜重复段开始／非连续与边界输入**：条件：未完成淡入再次 start_segment；操作：显式重新开始淡入，保留已学习增益和 RMS；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
17. **S3-R2-017｜RMS 余数／零和极小输入**：条件：每次调用少于 10ms；操作：跨调用保留平方和与计数，窗口结束才学习；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
18. **S3-R2-018｜RMS 余数／正常合成波形**：条件：每次调用少于 10ms；操作：跨调用保留平方和与计数，窗口结束才学习；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
19. **S3-R2-019｜RMS 余数／极值与非有限输入**：条件：每次调用少于 10ms；操作：跨调用保留平方和与计数，窗口结束才学习；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
20. **S3-R2-020｜RMS 余数／非连续与边界输入**：条件：每次调用少于 10ms；操作：跨调用保留平方和与计数，窗口结束才学习；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
21. **S3-R2-021｜RMS 边界／零和极小输入**：条件：长度等于窗口及窗口±1；操作：使用固定样本网格，不按调用重置窗口；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
22. **S3-R2-022｜RMS 边界／正常合成波形**：条件：长度等于窗口及窗口±1；操作：使用固定样本网格，不按调用重置窗口；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
23. **S3-R2-023｜RMS 边界／极值与非有限输入**：条件：长度等于窗口及窗口±1；操作：使用固定样本网格，不按调用重置窗口；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
24. **S3-R2-024｜RMS 边界／非连续与边界输入**：条件：长度等于窗口及窗口±1；操作：使用固定样本网格，不按调用重置窗口；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
25. **S3-R2-025｜因果前缀／零和极小输入**：条件：相同前缀接不同未来信号；操作：前缀 PCM 和前缀状态相同，不用 np.interp 未来信息；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
26. **S3-R2-026｜因果前缀／正常合成波形**：条件：相同前缀接不同未来信号；操作：前缀 PCM 和前缀状态相同，不用 np.interp 未来信息；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
27. **S3-R2-027｜因果前缀／极值与非有限输入**：条件：相同前缀接不同未来信号；操作：前缀 PCM 和前缀状态相同，不用 np.interp 未来信息；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
28. **S3-R2-028｜因果前缀／非连续与边界输入**：条件：相同前缀接不同未来信号；操作：前缀 PCM 和前缀状态相同，不用 np.interp 未来信息；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
29. **S3-R2-029｜增益攻击／零和极小输入**：条件：大于所需增益的前态；操作：逐样本使用 30ms 系数；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
30. **S3-R2-030｜增益攻击／正常合成波形**：条件：大于所需增益的前态；操作：逐样本使用 30ms 系数；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
31. **S3-R2-031｜增益攻击／极值与非有限输入**：条件：大于所需增益的前态；操作：逐样本使用 30ms 系数；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
32. **S3-R2-032｜增益攻击／非连续与边界输入**：条件：大于所需增益的前态；操作：逐样本使用 30ms 系数；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
33. **S3-R2-033｜增益释放／零和极小输入**：条件：小于所需增益的前态；操作：逐样本使用 600ms 系数；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
34. **S3-R2-034｜增益释放／正常合成波形**：条件：小于所需增益的前态；操作：逐样本使用 600ms 系数；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
35. **S3-R2-035｜增益释放／极值与非有限输入**：条件：小于所需增益的前态；操作：逐样本使用 600ms 系数；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
36. **S3-R2-036｜增益释放／非连续与边界输入**：条件：小于所需增益的前态；操作：逐样本使用 600ms 系数；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
37. **S3-R2-037｜增益预算／零和极小输入**：条件：很小且通过门限的信号；操作：期望增益与当前增益均在明确上下限内；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
38. **S3-R2-038｜增益预算／正常合成波形**：条件：很小且通过门限的信号；操作：期望增益与当前增益均在明确上下限内；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
39. **S3-R2-039｜增益预算／极值与非有限输入**：条件：很小且通过门限的信号；操作：期望增益与当前增益均在明确上下限内；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
40. **S3-R2-040｜增益预算／非连续与边界输入**：条件：很小且通过门限的信号；操作：期望增益与当前增益均在明确上下限内；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
41. **S3-R2-041｜静音门限／零和极小输入**：条件：零、低于门限、超过门限；操作：低于门限不学习噪声，使用 -46dB RMS 门限；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
42. **S3-R2-042｜静音门限／正常合成波形**：条件：零、低于门限、超过门限；操作：低于门限不学习噪声，使用 -46dB RMS 门限；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
43. **S3-R2-043｜静音门限／极值与非有限输入**：条件：零、低于门限、超过门限；操作：低于门限不学习噪声，使用 -46dB RMS 门限；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
44. **S3-R2-044｜静音门限／非连续与边界输入**：条件：零、低于门限、超过门限；操作：低于门限不学习噪声，使用 -46dB RMS 门限；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
45. **S3-R2-045｜DC 连续性／零和极小输入**：条件：常量偏置在任意点切开；操作：保存上一输入/输出，不在 process 边界重置；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
46. **S3-R2-046｜DC 连续性／正常合成波形**：条件：常量偏置在任意点切开；操作：保存上一输入/输出，不在 process 边界重置；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
47. **S3-R2-047｜DC 连续性／极值与非有限输入**：条件：常量偏置在任意点切开；操作：保存上一输入/输出，不在 process 边界重置；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
48. **S3-R2-048｜DC 连续性／非连续与边界输入**：条件：常量偏置在任意点切开；操作：保存上一输入/输出，不在 process 边界重置；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
49. **S3-R2-049｜非有限输入／零和极小输入**：条件：NaN、正负无穷混入；操作：等价于对应样本置零，不传播非有限状态；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
50. **S3-R2-050｜非有限输入／正常合成波形**：条件：NaN、正负无穷混入；操作：等价于对应样本置零，不传播非有限状态；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
51. **S3-R2-051｜非有限输入／极值与非有限输入**：条件：NaN、正负无穷混入；操作：等价于对应样本置零，不传播非有限状态；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
52. **S3-R2-052｜非有限输入／非连续与边界输入**：条件：NaN、正负无穷混入；操作：等价于对应样本置零，不传播非有限状态；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
53. **S3-R2-053｜空块／零和极小输入**：条件：任意处理间插入空块；操作：返回零样本且不推进任何状态；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
54. **S3-R2-054｜空块／正常合成波形**：条件：任意处理间插入空块；操作：返回零样本且不推进任何状态；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
55. **S3-R2-055｜空块／极值与非有限输入**：条件：任意处理间插入空块；操作：返回零样本且不推进任何状态；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
56. **S3-R2-056｜空块／非连续与边界输入**：条件：任意处理间插入空块；操作：返回零样本且不推进任何状态；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
57. **S3-R2-057｜非连续输入／零和极小输入**：条件：步进视图与连续副本；操作：结果一致且不修改输入；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
58. **S3-R2-058｜非连续输入／正常合成波形**：条件：步进视图与连续副本；操作：结果一致且不修改输入；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
59. **S3-R2-059｜非连续输入／极值与非有限输入**：条件：步进视图与连续副本；操作：结果一致且不修改输入；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
60. **S3-R2-060｜非连续输入／非连续与边界输入**：条件：步进视图与连续副本；操作：结果一致且不修改输入；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
61. **S3-R2-061｜采样率／零和极小输入**：条件：8k、24k、44.1k、48k；操作：依采样率计算固定 RMS 网格与时间常数；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
62. **S3-R2-062｜采样率／正常合成波形**：条件：8k、24k、44.1k、48k；操作：依采样率计算固定 RMS 网格与时间常数；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
63. **S3-R2-063｜采样率／极值与非有限输入**：条件：8k、24k、44.1k、48k；操作：依采样率计算固定 RMS 网格与时间常数；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
64. **S3-R2-064｜采样率／非连续与边界输入**：条件：8k、24k、44.1k、48k；操作：依采样率计算固定 RMS 网格与时间常数；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
65. **S3-R2-065｜正尾刷新／零和极小输入**：条件：flush(192) 后再次处理；操作：输出明确尾长，清 DC/last，保留其他学习态；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
66. **S3-R2-066｜正尾刷新／正常合成波形**：条件：flush(192) 后再次处理；操作：输出明确尾长，清 DC/last，保留其他学习态；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
67. **S3-R2-067｜正尾刷新／极值与非有限输入**：条件：flush(192) 后再次处理；操作：输出明确尾长，清 DC/last，保留其他学习态；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
68. **S3-R2-068｜正尾刷新／非连续与边界输入**：条件：flush(192) 后再次处理；操作：输出明确尾长，清 DC/last，保留其他学习态；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
69. **S3-R2-069｜零尾刷新／零和极小输入**：条件：flush(0) 在流中间；操作：无输出且不改状态；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
70. **S3-R2-070｜零尾刷新／正常合成波形**：条件：flush(0) 在流中间；操作：无输出且不改状态；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
71. **S3-R2-071｜零尾刷新／极值与非有限输入**：条件：flush(0) 在流中间；操作：无输出且不改状态；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
72. **S3-R2-072｜零尾刷新／非连续与边界输入**：条件：flush(0) 在流中间；操作：无输出且不改状态；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
73. **S3-R2-073｜负尾刷新／零和极小输入**：条件：flush(-1)；操作：明确 ValueError，不以空数组掩盖调用错误；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
74. **S3-R2-074｜负尾刷新／正常合成波形**：条件：flush(-1)；操作：明确 ValueError，不以空数组掩盖调用错误；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
75. **S3-R2-075｜负尾刷新／极值与非有限输入**：条件：flush(-1)；操作：明确 ValueError，不以空数组掩盖调用错误；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
76. **S3-R2-076｜负尾刷新／非连续与边界输入**：条件：flush(-1)；操作：明确 ValueError，不以空数组掩盖调用错误；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
77. **S3-R2-077｜尾部限幅／零和极小输入**：条件：最后样本接近限幅；操作：尾样本也保持安全幅度，无参考 PCM 拼接；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
78. **S3-R2-078｜尾部限幅／正常合成波形**：条件：最后样本接近限幅；操作：尾样本也保持安全幅度，无参考 PCM 拼接；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
79. **S3-R2-079｜尾部限幅／极值与非有限输入**：条件：最后样本接近限幅；操作：尾样本也保持安全幅度，无参考 PCM 拼接；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
80. **S3-R2-080｜尾部限幅／非连续与边界输入**：条件：最后样本接近限幅；操作：尾样本也保持安全幅度，无参考 PCM 拼接；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
81. **S3-R2-081｜关闭生命周期／零和极小输入**：条件：重复 close 或已关闭后调用；操作：close 幂等，其他操作明确拒绝；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
82. **S3-R2-082｜关闭生命周期／正常合成波形**：条件：重复 close 或已关闭后调用；操作：close 幂等，其他操作明确拒绝；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
83. **S3-R2-083｜关闭生命周期／极值与非有限输入**：条件：重复 close 或已关闭后调用；操作：close 幂等，其他操作明确拒绝；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
84. **S3-R2-084｜关闭生命周期／非连续与边界输入**：条件：重复 close 或已关闭后调用；操作：close 幂等，其他操作明确拒绝；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
85. **S3-R2-085｜worker 模块绑定／零和极小输入**：条件：冻结 audio_rt 已在 sys.modules；操作：候选显式导入 step18_audio_rt，禁止导入缓存劫持；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
86. **S3-R2-086｜worker 模块绑定／正常合成波形**：条件：冻结 audio_rt 已在 sys.modules；操作：候选显式导入 step18_audio_rt，禁止导入缓存劫持；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
87. **S3-R2-087｜worker 模块绑定／极值与非有限输入**：条件：冻结 audio_rt 已在 sys.modules；操作：候选显式导入 step18_audio_rt，禁止导入缓存劫持；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
88. **S3-R2-088｜worker 模块绑定／非连续与边界输入**：条件：冻结 audio_rt 已在 sys.modules；操作：候选显式导入 step18_audio_rt，禁止导入缓存劫持；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
89. **S3-R2-089｜worker 实际调用／零和极小输入**：条件：真实 run_job 接合成 engine；操作：捕获实际 Leveler.process/flush 返回的 PCM 与帧计数；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
90. **S3-R2-090｜worker 实际调用／正常合成波形**：条件：真实 run_job 接合成 engine；操作：捕获实际 Leveler.process/flush 返回的 PCM 与帧计数；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
91. **S3-R2-091｜worker 实际调用／极值与非有限输入**：条件：真实 run_job 接合成 engine；操作：捕获实际 Leveler.process/flush 返回的 PCM 与帧计数；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
92. **S3-R2-092｜worker 实际调用／非连续与边界输入**：条件：真实 run_job 接合成 engine；操作：捕获实际 Leveler.process/flush 返回的 PCM 与帧计数；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
93. **S3-R2-093｜性能边界／零和极小输入**：条件：1 样本、240 样本、整段调用；操作：记录 CPU 秒与样本数，禁止作为首声或模型 RTF 证据；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
94. **S3-R2-094｜性能边界／正常合成波形**：条件：1 样本、240 样本、整段调用；操作：记录 CPU 秒与样本数，禁止作为首声或模型 RTF 证据；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
95. **S3-R2-095｜性能边界／极值与非有限输入**：条件：1 样本、240 样本、整段调用；操作：记录 CPU 秒与样本数，禁止作为首声或模型 RTF 证据；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
96. **S3-R2-096｜性能边界／非连续与边界输入**：条件：1 样本、240 样本、整段调用；操作：记录 CPU 秒与样本数，禁止作为首声或模型 RTF 证据；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
97. **S3-R2-097｜封存边界／零和极小输入**：条件：旧收据绑定活动文档；操作：事前复制可变文档，旧源码和收据只读保留；在“零和极小输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
98. **S3-R2-098｜封存边界／正常合成波形**：条件：旧收据绑定活动文档；操作：事前复制可变文档，旧源码和收据只读保留；在“正常合成波形”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
99. **S3-R2-099｜封存边界／极值与非有限输入**：条件：旧收据绑定活动文档；操作：事前复制可变文档，旧源码和收据只读保留；在“极值与非有限输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
100. **S3-R2-100｜封存边界／非连续与边界输入**：条件：旧收据绑定活动文档；操作：事前复制可变文档，旧源码和收据只读保留；在“非连续与边界输入”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。

---

## 内嵌备忘录：KAGGLE_STEP18_S3_REVIEW_R3.md

# S3 R3：接入与证据复核（100 条建议）

这些是实施前检查与建议，不是 100 项通过收据。合成输入与替身引擎不代表真实声音、训练、GPU 或 Rust 验收。

1. **S3-R3-001｜淡入绝对位置／直接候选调用**：条件：剩余不足一段淡入时继续处理；操作：保存 fade_total/left，禁止每次调用从零重启；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
2. **S3-R3-002｜淡入绝对位置／冻结前态对照**：条件：剩余不足一段淡入时继续处理；操作：保存 fade_total/left，禁止每次调用从零重启；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
3. **S3-R3-003｜淡入绝对位置／实际 worker 替身引擎**：条件：剩余不足一段淡入时继续处理；操作：保存 fade_total/left，禁止每次调用从零重启；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
4. **S3-R3-004｜淡入绝对位置／独立封存与回归**：条件：剩余不足一段淡入时继续处理；操作：保存 fade_total/left，禁止每次调用从零重启；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
5. **S3-R3-005｜淡入零长度／直接候选调用**：条件：start_segment(0) 后处理非零样本；操作：不加包络、不除零；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
6. **S3-R3-006｜淡入零长度／冻结前态对照**：条件：start_segment(0) 后处理非零样本；操作：不加包络、不除零；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
7. **S3-R3-007｜淡入零长度／实际 worker 替身引擎**：条件：start_segment(0) 后处理非零样本；操作：不加包络、不除零；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
8. **S3-R3-008｜淡入零长度／独立封存与回归**：条件：start_segment(0) 后处理非零样本；操作：不加包络、不除零；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
9. **S3-R3-009｜淡入单样本／直接候选调用**：条件：淡入总长为一时；操作：按约定首样本零、随后恢复，不延长样本流；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
10. **S3-R3-010｜淡入单样本／冻结前态对照**：条件：淡入总长为一时；操作：按约定首样本零、随后恢复，不延长样本流；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
11. **S3-R3-011｜淡入单样本／实际 worker 替身引擎**：条件：淡入总长为一时；操作：按约定首样本零、随后恢复，不延长样本流；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
12. **S3-R3-012｜淡入单样本／独立封存与回归**：条件：淡入总长为一时；操作：按约定首样本零、随后恢复，不延长样本流；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
13. **S3-R3-013｜重复段开始／直接候选调用**：条件：未完成淡入再次 start_segment；操作：显式重新开始淡入，保留已学习增益和 RMS；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
14. **S3-R3-014｜重复段开始／冻结前态对照**：条件：未完成淡入再次 start_segment；操作：显式重新开始淡入，保留已学习增益和 RMS；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
15. **S3-R3-015｜重复段开始／实际 worker 替身引擎**：条件：未完成淡入再次 start_segment；操作：显式重新开始淡入，保留已学习增益和 RMS；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
16. **S3-R3-016｜重复段开始／独立封存与回归**：条件：未完成淡入再次 start_segment；操作：显式重新开始淡入，保留已学习增益和 RMS；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
17. **S3-R3-017｜RMS 余数／直接候选调用**：条件：每次调用少于 10ms；操作：跨调用保留平方和与计数，窗口结束才学习；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
18. **S3-R3-018｜RMS 余数／冻结前态对照**：条件：每次调用少于 10ms；操作：跨调用保留平方和与计数，窗口结束才学习；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
19. **S3-R3-019｜RMS 余数／实际 worker 替身引擎**：条件：每次调用少于 10ms；操作：跨调用保留平方和与计数，窗口结束才学习；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
20. **S3-R3-020｜RMS 余数／独立封存与回归**：条件：每次调用少于 10ms；操作：跨调用保留平方和与计数，窗口结束才学习；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
21. **S3-R3-021｜RMS 边界／直接候选调用**：条件：长度等于窗口及窗口±1；操作：使用固定样本网格，不按调用重置窗口；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
22. **S3-R3-022｜RMS 边界／冻结前态对照**：条件：长度等于窗口及窗口±1；操作：使用固定样本网格，不按调用重置窗口；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
23. **S3-R3-023｜RMS 边界／实际 worker 替身引擎**：条件：长度等于窗口及窗口±1；操作：使用固定样本网格，不按调用重置窗口；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
24. **S3-R3-024｜RMS 边界／独立封存与回归**：条件：长度等于窗口及窗口±1；操作：使用固定样本网格，不按调用重置窗口；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
25. **S3-R3-025｜因果前缀／直接候选调用**：条件：相同前缀接不同未来信号；操作：前缀 PCM 和前缀状态相同，不用 np.interp 未来信息；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
26. **S3-R3-026｜因果前缀／冻结前态对照**：条件：相同前缀接不同未来信号；操作：前缀 PCM 和前缀状态相同，不用 np.interp 未来信息；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
27. **S3-R3-027｜因果前缀／实际 worker 替身引擎**：条件：相同前缀接不同未来信号；操作：前缀 PCM 和前缀状态相同，不用 np.interp 未来信息；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
28. **S3-R3-028｜因果前缀／独立封存与回归**：条件：相同前缀接不同未来信号；操作：前缀 PCM 和前缀状态相同，不用 np.interp 未来信息；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
29. **S3-R3-029｜增益攻击／直接候选调用**：条件：大于所需增益的前态；操作：逐样本使用 30ms 系数；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
30. **S3-R3-030｜增益攻击／冻结前态对照**：条件：大于所需增益的前态；操作：逐样本使用 30ms 系数；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
31. **S3-R3-031｜增益攻击／实际 worker 替身引擎**：条件：大于所需增益的前态；操作：逐样本使用 30ms 系数；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
32. **S3-R3-032｜增益攻击／独立封存与回归**：条件：大于所需增益的前态；操作：逐样本使用 30ms 系数；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
33. **S3-R3-033｜增益释放／直接候选调用**：条件：小于所需增益的前态；操作：逐样本使用 600ms 系数；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
34. **S3-R3-034｜增益释放／冻结前态对照**：条件：小于所需增益的前态；操作：逐样本使用 600ms 系数；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
35. **S3-R3-035｜增益释放／实际 worker 替身引擎**：条件：小于所需增益的前态；操作：逐样本使用 600ms 系数；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
36. **S3-R3-036｜增益释放／独立封存与回归**：条件：小于所需增益的前态；操作：逐样本使用 600ms 系数；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
37. **S3-R3-037｜增益预算／直接候选调用**：条件：很小且通过门限的信号；操作：期望增益与当前增益均在明确上下限内；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
38. **S3-R3-038｜增益预算／冻结前态对照**：条件：很小且通过门限的信号；操作：期望增益与当前增益均在明确上下限内；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
39. **S3-R3-039｜增益预算／实际 worker 替身引擎**：条件：很小且通过门限的信号；操作：期望增益与当前增益均在明确上下限内；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
40. **S3-R3-040｜增益预算／独立封存与回归**：条件：很小且通过门限的信号；操作：期望增益与当前增益均在明确上下限内；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
41. **S3-R3-041｜静音门限／直接候选调用**：条件：零、低于门限、超过门限；操作：低于门限不学习噪声，使用 -46dB RMS 门限；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
42. **S3-R3-042｜静音门限／冻结前态对照**：条件：零、低于门限、超过门限；操作：低于门限不学习噪声，使用 -46dB RMS 门限；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
43. **S3-R3-043｜静音门限／实际 worker 替身引擎**：条件：零、低于门限、超过门限；操作：低于门限不学习噪声，使用 -46dB RMS 门限；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
44. **S3-R3-044｜静音门限／独立封存与回归**：条件：零、低于门限、超过门限；操作：低于门限不学习噪声，使用 -46dB RMS 门限；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
45. **S3-R3-045｜DC 连续性／直接候选调用**：条件：常量偏置在任意点切开；操作：保存上一输入/输出，不在 process 边界重置；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
46. **S3-R3-046｜DC 连续性／冻结前态对照**：条件：常量偏置在任意点切开；操作：保存上一输入/输出，不在 process 边界重置；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
47. **S3-R3-047｜DC 连续性／实际 worker 替身引擎**：条件：常量偏置在任意点切开；操作：保存上一输入/输出，不在 process 边界重置；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
48. **S3-R3-048｜DC 连续性／独立封存与回归**：条件：常量偏置在任意点切开；操作：保存上一输入/输出，不在 process 边界重置；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
49. **S3-R3-049｜非有限输入／直接候选调用**：条件：NaN、正负无穷混入；操作：等价于对应样本置零，不传播非有限状态；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
50. **S3-R3-050｜非有限输入／冻结前态对照**：条件：NaN、正负无穷混入；操作：等价于对应样本置零，不传播非有限状态；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
51. **S3-R3-051｜非有限输入／实际 worker 替身引擎**：条件：NaN、正负无穷混入；操作：等价于对应样本置零，不传播非有限状态；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
52. **S3-R3-052｜非有限输入／独立封存与回归**：条件：NaN、正负无穷混入；操作：等价于对应样本置零，不传播非有限状态；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
53. **S3-R3-053｜空块／直接候选调用**：条件：任意处理间插入空块；操作：返回零样本且不推进任何状态；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
54. **S3-R3-054｜空块／冻结前态对照**：条件：任意处理间插入空块；操作：返回零样本且不推进任何状态；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
55. **S3-R3-055｜空块／实际 worker 替身引擎**：条件：任意处理间插入空块；操作：返回零样本且不推进任何状态；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
56. **S3-R3-056｜空块／独立封存与回归**：条件：任意处理间插入空块；操作：返回零样本且不推进任何状态；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
57. **S3-R3-057｜非连续输入／直接候选调用**：条件：步进视图与连续副本；操作：结果一致且不修改输入；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
58. **S3-R3-058｜非连续输入／冻结前态对照**：条件：步进视图与连续副本；操作：结果一致且不修改输入；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
59. **S3-R3-059｜非连续输入／实际 worker 替身引擎**：条件：步进视图与连续副本；操作：结果一致且不修改输入；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
60. **S3-R3-060｜非连续输入／独立封存与回归**：条件：步进视图与连续副本；操作：结果一致且不修改输入；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
61. **S3-R3-061｜采样率／直接候选调用**：条件：8k、24k、44.1k、48k；操作：依采样率计算固定 RMS 网格与时间常数；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
62. **S3-R3-062｜采样率／冻结前态对照**：条件：8k、24k、44.1k、48k；操作：依采样率计算固定 RMS 网格与时间常数；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
63. **S3-R3-063｜采样率／实际 worker 替身引擎**：条件：8k、24k、44.1k、48k；操作：依采样率计算固定 RMS 网格与时间常数；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
64. **S3-R3-064｜采样率／独立封存与回归**：条件：8k、24k、44.1k、48k；操作：依采样率计算固定 RMS 网格与时间常数；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
65. **S3-R3-065｜正尾刷新／直接候选调用**：条件：flush(192) 后再次处理；操作：输出明确尾长，清 DC/last，保留其他学习态；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
66. **S3-R3-066｜正尾刷新／冻结前态对照**：条件：flush(192) 后再次处理；操作：输出明确尾长，清 DC/last，保留其他学习态；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
67. **S3-R3-067｜正尾刷新／实际 worker 替身引擎**：条件：flush(192) 后再次处理；操作：输出明确尾长，清 DC/last，保留其他学习态；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
68. **S3-R3-068｜正尾刷新／独立封存与回归**：条件：flush(192) 后再次处理；操作：输出明确尾长，清 DC/last，保留其他学习态；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
69. **S3-R3-069｜零尾刷新／直接候选调用**：条件：flush(0) 在流中间；操作：无输出且不改状态；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
70. **S3-R3-070｜零尾刷新／冻结前态对照**：条件：flush(0) 在流中间；操作：无输出且不改状态；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
71. **S3-R3-071｜零尾刷新／实际 worker 替身引擎**：条件：flush(0) 在流中间；操作：无输出且不改状态；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
72. **S3-R3-072｜零尾刷新／独立封存与回归**：条件：flush(0) 在流中间；操作：无输出且不改状态；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
73. **S3-R3-073｜负尾刷新／直接候选调用**：条件：flush(-1)；操作：明确 ValueError，不以空数组掩盖调用错误；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
74. **S3-R3-074｜负尾刷新／冻结前态对照**：条件：flush(-1)；操作：明确 ValueError，不以空数组掩盖调用错误；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
75. **S3-R3-075｜负尾刷新／实际 worker 替身引擎**：条件：flush(-1)；操作：明确 ValueError，不以空数组掩盖调用错误；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
76. **S3-R3-076｜负尾刷新／独立封存与回归**：条件：flush(-1)；操作：明确 ValueError，不以空数组掩盖调用错误；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
77. **S3-R3-077｜尾部限幅／直接候选调用**：条件：最后样本接近限幅；操作：尾样本也保持安全幅度，无参考 PCM 拼接；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
78. **S3-R3-078｜尾部限幅／冻结前态对照**：条件：最后样本接近限幅；操作：尾样本也保持安全幅度，无参考 PCM 拼接；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
79. **S3-R3-079｜尾部限幅／实际 worker 替身引擎**：条件：最后样本接近限幅；操作：尾样本也保持安全幅度，无参考 PCM 拼接；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
80. **S3-R3-080｜尾部限幅／独立封存与回归**：条件：最后样本接近限幅；操作：尾样本也保持安全幅度，无参考 PCM 拼接；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
81. **S3-R3-081｜关闭生命周期／直接候选调用**：条件：重复 close 或已关闭后调用；操作：close 幂等，其他操作明确拒绝；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
82. **S3-R3-082｜关闭生命周期／冻结前态对照**：条件：重复 close 或已关闭后调用；操作：close 幂等，其他操作明确拒绝；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
83. **S3-R3-083｜关闭生命周期／实际 worker 替身引擎**：条件：重复 close 或已关闭后调用；操作：close 幂等，其他操作明确拒绝；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
84. **S3-R3-084｜关闭生命周期／独立封存与回归**：条件：重复 close 或已关闭后调用；操作：close 幂等，其他操作明确拒绝；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
85. **S3-R3-085｜worker 模块绑定／直接候选调用**：条件：冻结 audio_rt 已在 sys.modules；操作：候选显式导入 step18_audio_rt，禁止导入缓存劫持；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
86. **S3-R3-086｜worker 模块绑定／冻结前态对照**：条件：冻结 audio_rt 已在 sys.modules；操作：候选显式导入 step18_audio_rt，禁止导入缓存劫持；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
87. **S3-R3-087｜worker 模块绑定／实际 worker 替身引擎**：条件：冻结 audio_rt 已在 sys.modules；操作：候选显式导入 step18_audio_rt，禁止导入缓存劫持；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
88. **S3-R3-088｜worker 模块绑定／独立封存与回归**：条件：冻结 audio_rt 已在 sys.modules；操作：候选显式导入 step18_audio_rt，禁止导入缓存劫持；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
89. **S3-R3-089｜worker 实际调用／直接候选调用**：条件：真实 run_job 接合成 engine；操作：捕获实际 Leveler.process/flush 返回的 PCM 与帧计数；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
90. **S3-R3-090｜worker 实际调用／冻结前态对照**：条件：真实 run_job 接合成 engine；操作：捕获实际 Leveler.process/flush 返回的 PCM 与帧计数；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
91. **S3-R3-091｜worker 实际调用／实际 worker 替身引擎**：条件：真实 run_job 接合成 engine；操作：捕获实际 Leveler.process/flush 返回的 PCM 与帧计数；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
92. **S3-R3-092｜worker 实际调用／独立封存与回归**：条件：真实 run_job 接合成 engine；操作：捕获实际 Leveler.process/flush 返回的 PCM 与帧计数；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
93. **S3-R3-093｜性能边界／直接候选调用**：条件：1 样本、240 样本、整段调用；操作：记录 CPU 秒与样本数，禁止作为首声或模型 RTF 证据；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
94. **S3-R3-094｜性能边界／冻结前态对照**：条件：1 样本、240 样本、整段调用；操作：记录 CPU 秒与样本数，禁止作为首声或模型 RTF 证据；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
95. **S3-R3-095｜性能边界／实际 worker 替身引擎**：条件：1 样本、240 样本、整段调用；操作：记录 CPU 秒与样本数，禁止作为首声或模型 RTF 证据；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
96. **S3-R3-096｜性能边界／独立封存与回归**：条件：1 样本、240 样本、整段调用；操作：记录 CPU 秒与样本数，禁止作为首声或模型 RTF 证据；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
97. **S3-R3-097｜封存边界／直接候选调用**：条件：旧收据绑定活动文档；操作：事前复制可变文档，旧源码和收据只读保留；在“直接候选调用”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
98. **S3-R3-098｜封存边界／冻结前态对照**：条件：旧收据绑定活动文档；操作：事前复制可变文档，旧源码和收据只读保留；在“冻结前态对照”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
99. **S3-R3-099｜封存边界／实际 worker 替身引擎**：条件：旧收据绑定活动文档；操作：事前复制可变文档，旧源码和收据只读保留；在“实际 worker 替身引擎”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。
100. **S3-R3-100｜封存边界／独立封存与回归**：条件：旧收据绑定活动文档；操作：事前复制可变文档，旧源码和收据只读保留；在“独立封存与回归”路径保留输入、输出长度及状态证据；无法执行必须标未验收，不能用邻近路径代替。

---

## 内嵌备忘录：KAGGLE_STEP18_S3_DSP.md

# S3：因果 NumPy DSP 与隔离 worker 实际接入

**结论：本步数值修复已落地并通过限定回归；完整 S3／产品／模型／声学仍 PARTIAL/BLOCKED，18 未发布、未部署。**

## 实际代码进展

- 新增 `kaggle/step18/step18_audio_rt.py`，不是仅加观察或测试替身。
- RMS 平方和/计数按固定 10ms 网格跨块累计；不足窗口的 process 仍立即发出同数量 PCM，不等待未来。
- 增益按逐样本 30ms attack／600ms release 更新，不再依赖本次调用内部未来 RMS 的插值。淡入按固定总长与已消耗位置计算，不在每个短块重新从零开始。
- 保留 DC 连续性、门控学习、上下限和软限幅。float32 输入／float64 标量状态／ties-to-even int16 量化；-46dB gate 使用精确幅度阈值，与旧 NumPy 0.005 不完全相同。旧整段输出不是正确性 oracle，修复会改变旧整段增益曲线。
- 定义空块、0/1样本淡入、重复段、flush、非法参数和关闭行为。正 flush 清 DC/last，保留 RMS/gain/env/fade；flush(0) 不改状态。显式合成衰减尾不算额外参考语音。
- 新增隔离 `kaggle/step18/worker.py`，唯一模块名显式绑定候选 DSP。所有命名函数/类 AST 与冻结 worker 相同；真实 run_job、原 trimmer 和帧编码已执行，engine 与 pin 明确为替身。没有改默认启动入口、17 包或正式工作台。
- 候选明确仅启用 `numpy-causal-v1`，不自动装载 Rust。冻结 Rust 和 ABI bridge 完全保留；没有工具链，不声称跨后端位等同或已验收完整 S3。

## 三轮真实执行收据

| 项目 | 每轮结果 | 范围 |
|---|---:|---|
| 完整 CPU 组合 | **562 PASS ×3** | 450 冻结控制＋73 旧候选＋30 新 DSP＋9 新 worker；合计1686 PASS |
| 失败／错误／跳过 | **0／0／0** | 三轮均如此；注入错误的预期处理也是合同，不代表所有业务请求都成功 |
| 同套 DSP 合同旧版红对照 | 30项，44失败记录，0error/skip | 含子用例，不是44独立bug；与事前封存旧源码 SHA 相同 |
| 同套候选绿对照 | 30 PASS | 独立递推、因果前缀、状态、样本数、幅度与生命周期 |
| 分块矩阵 | **14组×3，最大差0 int16** | fade隔离／正常AGC，各含整段、1、17、48、240、1920、不规则分块；最终gain/env也相等 |
| 长流压力 | **601秒合成流×3** | 每轮14424000样本；固定标量状态，不保留 PCM 历史；不是实际录音或训练 |
| 继承真实环回 TCP | 237/轮，共711 | 仍为旧 S1/S2 端点；新 S3 不新增 TCP 请求，engine/ACK 等仍替身 |
| 审计／Node／AST | 24／30／53 ×3 | 另 JS语法与 repack --check；未重跑真实浏览器或 Go/Rust |

原旧523测试逐ID和结果完整继承，HTTP状态组合保留；旧冻结 DSP/trimmer 缺陷观察仍在，未改旧探针使其看似已修。`s3-final-cpu-roundN.json`、`s3-final-checks-roundN.json`、`s3-dsp-benchmark-roundN.json` 是最终证据；初次预检/附加检查另保留不混算。

## 实测性能：有改善也有代价

同机顺序处理24037样本（约1.002秒）正常AGC的 CPU 时间，三轮范围：

| 调用方式 | 旧版 CPU ms | 候选 CPU ms | 解释 |
|---|---:|---:|---|
| 整段 | 4.99–5.18 | 8.93–9.05 | 较慢；逐样本因果控制的实际开销 |
| 单样本 | 654.89–674.72 | 70.48–105.58 | 较快；减少短调用 NumPy 临时数组成本 |
| 17样本 | 43.68–71.41 | 13.24–14.00 | 较快；减少短调用 NumPy 临时数组成本 |
| 240样本 | 10.72–15.83 | 9.07–12.54 | 较慢；逐样本因果控制的实际开销 |
| 1920样本 | 6.15–6.85 | 9.00–9.05 | 较慢；逐样本因果控制的实际开销 |
| 不规则 | 7.29–8.07 | 9.04–9.19 | 较慢；逐样本因果控制的实际开销 |

601秒合成流的候选 CPU 耗时分别为 6.415 / 6.339 / 5.868 秒，合成 DSP CPU时间/音频时长约 0.00976–0.01067。这只度量 DSP，不是完整模型RTF≤0.3、首声<3秒、声卡实际出声或听感改善证明。**不声称全面加速**；当前不为几毫秒纯数值开销盲目引入 JIT 或多语言重写，真实 T4 集成后仍需完整预算。

## 复核、留错与封存

- 本题 Q30 先完成四选项选择 C＋50行动，再实施；新增三遍专题复核各100建议。它们是复核建议，不是300已修缺陷或完整验证。
- S2-B可变文档/交接与冻结 DSP/worker/Rust 事前归档 `s3-before/`；后续覆盖 progress-checks 前也归档旧进度。历史保护1768路径，1765匹配，3份旧日志仍缺，不补造。完整历史完整性仍false。
- 首次 worker 预检9项中4error，原因是测试 engine fixture 缺少原 run_job 要求的 dtype_name；只补 fixture 后9 PASS，未改产品来迁就替身。首错完整保留。
- 红对照极端 float32 输入触发旧临时数组溢出警告；最终结构化红对照原始日志捕获 stderr。不能把此合成极值当用户沙沙根因。
- 新环境的 .venv 原已消失，本次确实重建并安装；pip freeze 与 S2-B 字节一致，不冒同一运行环境，无 Rust/Go/Torch/Qwen 安装或实际模型执行。
- 8条原始建议按具体测试ID和三轮收据 SHA 建立限定链接；原300建议最终/功能签收仍0，不以覆盖率宣称整体完成。
- 独立 `verify_s3.py` 核验来源、旧523继承、对照、三轮、幅度/状态/长度、历史保护及完整交接；最终进度见 `progress-s3.json`。完整交接101份；两次独立核验的实际结果以封存stdout文件为准。

## 尚未签收／下一步

真实用户音频、自然朗读、无沙沙、相似度、首声、双T4和长录音真训练均未验收。分块一致性不能证明噪声消失。Rust编译/跨后端容差仍缺条件，完整S3不签收；正式18包未构建/发布。

下一步按计划推进 **S4 裁剪有界状态**：原 EdgeTrimmer 的短于120样本丢弃、跨块预滚、非零held尾部与finish/取消路径。当前候选 worker 保留原 trimmer，因此 DSP 的样本数守恒只从实际送入 DSP 的输入开始，不能冒称整个生成/播放链已无丢样本。不询问 Continue，不跳过冻结保护和真实声学门禁。

---

## 内嵌备忘录：KAGGLE_STEP18_Q31_TRIMMER.md

# Q31：怎样修复S4裁剪状态而不破坏S3？

顺序自问自答，承接已完成Q30；不向用户提问，不预填Q32。

- A：只在结束拼接held。仍丢短块和跨块预滚，拒绝。
- B：禁用裁剪／强制大块。改变暂停政策或掩盖问题，拒绝。
- **C（采用）**：固定网格残帧＋有界前史/尾队列＋显式finish/取消，并新增worker_s4真正接入，保留S3 worker及其旧合同。按数值合同而非听感猜测实施。
- D：攒整句再离线裁剪。损害首声且无界缓存，拒绝。

## 政策先定义

120样本网格从流开始对齐，与调用边界无关。在worker固定24kHz下最多等待不足5ms残帧；35ms前史跨调用。正常结束按实际残帧长度检测，保留仍缓存的全部非零尾，只能删除精确零；领先低于门限的历史仍可按前史预算裁掉，计数并承认可能包含低电平声音，不能宣称全部语音守恒。中段静音超过尾预算要输出而非丢弃。取消/异常清空缓存，不排旧尾。输入总数=裁剪返回+领先丢弃+精确零尾丢弃+取消丢弃+当前缓存；裁剪返回不等于已播放样本。固定标量/队列预算，不加整句缓冲。保留旧worker.py，使旧结构性AST合同仍真实有效；新worker_s4.py为本步可运行候选，不切换正式入口。

## 50行动（下一题前先完成）
1. 确认活动分支不换支。
2. 归档S3可变交接文档。
3. 保存S3 worker/DSP和旧进度字节。
4. 扩展旧保护表保留三缺日志。
5. 复核环境而不冒新安装。
6. 三遍各100建议先写明非通过收据。
7. 独立worker_s4保留旧worker和39项合同。
8. 唯一模块名导入新裁剪器。
9. 固定120样本检测网格。
10. 跨调用保存不足网格余数。
11. 残帧只拷贝少于120样本避免大数组引用。
12. 使用实际残帧长度检测不补零稀释。
13. 跨块保留35ms前史。
14. 前史淘汰按精确样本计数。
15. 记录实际前端丢弃与扫描数的区别。
16. 长前静音按固定网格越限启动。
17. 独立标记lead_limit_reached。
18. 语音帧释放中间静音不剪内部停顿。
19. 尾部先放行keep窗口。
20. 只保留有界尾队列。
21. 超过尾预算按顺序输出而非删音。
22. deque避免每帧复制全部尾缓存。
23. 队列切片不持有整段输入。
24. 保持输入只读与float32输出。
25. 空push无状态推进。
26. 正常finish检查不足120样本残帧。
27. 正常finish保留全部缓存非零样本。
28. 仅精确零尾可删除且计数。
29. 无语音低电平结束保留当前非零前史。
30. 定义keep=0的显式政策。
31. finish幂等。
32. finish后push明确拒绝。
33. 取消finish不输出任何缓存。
34. 异常路径也取消并清空裁剪状态。
35. 在worker结束前真正调用finish。
36. 结束残帧走同一DSP和PCM计数路径。
37. 短音首帧可在finish时发出且时序如实。
38. 取消后不flush192衰减尾。
39. 取消后不追加显式尾暂停。
40. 输出裁剪诊断不称声学验证。
41. 区分trimmer返回样本和wire样本。
42. 测试finish与取消交错屏障。
43. 独立批处理oracle不拿旧版当正确值。
44. whole/single/119/120/1920/不规则严格对照。
45. 旧代码运行同套修复合同保存红对照。
46. 所有旧562合同保留再加新合同三轮。
47. 三轮Node审计JSrepack语法核验。
48. 测CPU和长流缓存上界不冒训练或RTF。
49. 独立两次封存与完整交接。
50. 如实保留真实模型听感T4发布门禁。

---

## 内嵌备忘录：KAGGLE_STEP18_S4_REVIEW_R1.md

# S4 R1：状态复核100建议

建议不是执行成绩；不代表声学、完整模型、真实训练验收。

1. **S4-R1-001｜短块/一次输入**：在1..119样本调用时，保存残帧直到固定网格或finish；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
2. **S4-R1-002｜短块/单样本分块**：在1..119样本调用时，保存残帧直到固定网格或finish；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
3. **S4-R1-003｜短块/不规则分块**：在1..119样本调用时，保存残帧直到固定网格或finish；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
4. **S4-R1-004｜短块/结束边界**：在1..119样本调用时，保存残帧直到固定网格或finish；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
5. **S4-R1-005｜网格边缘/一次输入**：在119/120/121样本时，不按调用重置检测网格；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
6. **S4-R1-006｜网格边缘/单样本分块**：在119/120/121样本时，不按调用重置检测网格；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
7. **S4-R1-007｜网格边缘/不规则分块**：在119/120/121样本时，不按调用重置检测网格；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
8. **S4-R1-008｜网格边缘/结束边界**：在119/120/121样本时，不按调用重置检测网格；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
9. **S4-R1-009｜前史/一次输入**：在960低电平后2400有声时，保留跨块840前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
10. **S4-R1-010｜前史/单样本分块**：在960低电平后2400有声时，保留跨块840前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
11. **S4-R1-011｜前史/不规则分块**：在960低电平后2400有声时，保留跨块840前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
12. **S4-R1-012｜前史/结束边界**：在960低电平后2400有声时，保留跨块840前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
13. **S4-R1-013｜零前史/一次输入**：在keep=0时，明确允许丢领先静音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
14. **S4-R1-014｜零前史/单样本分块**：在keep=0时，明确允许丢领先静音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
15. **S4-R1-015｜零前史/不规则分块**：在keep=0时，明确允许丢领先静音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
16. **S4-R1-016｜零前史/结束边界**：在keep=0时，明确允许丢领先静音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
17. **S4-R1-017｜尾残帧/一次输入**：在末尾60非零时，实际长度检测并输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
18. **S4-R1-018｜尾残帧/单样本分块**：在末尾60非零时，实际长度检测并输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
19. **S4-R1-019｜尾残帧/不规则分块**：在末尾60非零时，实际长度检测并输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
20. **S4-R1-020｜尾残帧/结束边界**：在末尾60非零时，实际长度检测并输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
21. **S4-R1-021｜低电平尾/一次输入**：在已开始后低于阈值非零时，finish不按门限删非零尾；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
22. **S4-R1-022｜低电平尾/单样本分块**：在已开始后低于阈值非零时，finish不按门限删非零尾；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
23. **S4-R1-023｜低电平尾/不规则分块**：在已开始后低于阈值非零时，finish不按门限删非零尾；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
24. **S4-R1-024｜低电平尾/结束边界**：在已开始后低于阈值非零时，finish不按门限删非零尾；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
25. **S4-R1-025｜精确零尾/一次输入**：在连续全零结束时，只删可计数精确零；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
26. **S4-R1-026｜精确零尾/单样本分块**：在连续全零结束时，只删可计数精确零；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
27. **S4-R1-027｜精确零尾/不规则分块**：在连续全零结束时，只删可计数精确零；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
28. **S4-R1-028｜精确零尾/结束边界**：在连续全零结束时，只删可计数精确零；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
29. **S4-R1-029｜中间停顿/一次输入**：在两有声段间静音时，按原序释放不缩句中停顿；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
30. **S4-R1-030｜中间停顿/单样本分块**：在两有声段间静音时，按原序释放不缩句中停顿；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
31. **S4-R1-031｜中间停顿/不规则分块**：在两有声段间静音时，按原序释放不缩句中停顿；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
32. **S4-R1-032｜中间停顿/结束边界**：在两有声段间静音时，按原序释放不缩句中停顿；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
33. **S4-R1-033｜长尾队列/一次输入**：在超过max_held时，超额输出不删音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
34. **S4-R1-034｜长尾队列/单样本分块**：在超过max_held时，超额输出不删音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
35. **S4-R1-035｜长尾队列/不规则分块**：在超过max_held时，超额输出不删音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
36. **S4-R1-036｜长尾队列/结束边界**：在超过max_held时，超额输出不删音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
37. **S4-R1-037｜长前静音/一次输入**：在超过max_lead时，固定网格触发并记录越限；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
38. **S4-R1-038｜长前静音/单样本分块**：在超过max_lead时，固定网格触发并记录越限；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
39. **S4-R1-039｜长前静音/不规则分块**：在超过max_lead时，固定网格触发并记录越限；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
40. **S4-R1-040｜长前静音/结束边界**：在超过max_lead时，固定网格触发并记录越限；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
41. **S4-R1-041｜纯短语音/一次输入**：在全段不足120时，finish必须可输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
42. **S4-R1-042｜纯短语音/单样本分块**：在全段不足120时，finish必须可输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
43. **S4-R1-043｜纯短语音/不规则分块**：在全段不足120时，finish必须可输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
44. **S4-R1-044｜纯短语音/结束边界**：在全段不足120时，finish必须可输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
45. **S4-R1-045｜纯低电平/一次输入**：在一直未过门限时，保留结束仍缓存非零前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
46. **S4-R1-046｜纯低电平/单样本分块**：在一直未过门限时，保留结束仍缓存非零前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
47. **S4-R1-047｜纯低电平/不规则分块**：在一直未过门限时，保留结束仍缓存非零前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
48. **S4-R1-048｜纯低电平/结束边界**：在一直未过门限时，保留结束仍缓存非零前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
49. **S4-R1-049｜空流/一次输入**：在无push结束时，空输出且幂等；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
50. **S4-R1-050｜空流/单样本分块**：在无push结束时，空输出且幂等；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
51. **S4-R1-051｜空流/不规则分块**：在无push结束时，空输出且幂等；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
52. **S4-R1-052｜空流/结束边界**：在无push结束时，空输出且幂等；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
53. **S4-R1-053｜空块/一次输入**：在流中插空时，状态不推进；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
54. **S4-R1-054｜空块/单样本分块**：在流中插空时，状态不推进；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
55. **S4-R1-055｜空块/不规则分块**：在流中插空时，状态不推进；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
56. **S4-R1-056｜空块/结束边界**：在流中插空时，状态不推进；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
57. **S4-R1-057｜finish重复/一次输入**：在结束调用两次时，第二次空输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
58. **S4-R1-058｜finish重复/单样本分块**：在结束调用两次时，第二次空输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
59. **S4-R1-059｜finish重复/不规则分块**：在结束调用两次时，第二次空输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
60. **S4-R1-060｜finish重复/结束边界**：在结束调用两次时，第二次空输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
61. **S4-R1-061｜终止后push/一次输入**：在已结束后输入时，明确拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
62. **S4-R1-062｜终止后push/单样本分块**：在已结束后输入时，明确拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
63. **S4-R1-063｜终止后push/不规则分块**：在已结束后输入时，明确拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
64. **S4-R1-064｜终止后push/结束边界**：在已结束后输入时，明确拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
65. **S4-R1-065｜取消/一次输入**：在持有残帧和尾时，清空不输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
66. **S4-R1-066｜取消/单样本分块**：在持有残帧和尾时，清空不输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
67. **S4-R1-067｜取消/不规则分块**：在持有残帧和尾时，清空不输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
68. **S4-R1-068｜取消/结束边界**：在持有残帧和尾时，清空不输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
69. **S4-R1-069｜异常/一次输入**：在engine抛错时，保留错误并清理；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
70. **S4-R1-070｜异常/单样本分块**：在engine抛错时，保留错误并清理；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
71. **S4-R1-071｜异常/不规则分块**：在engine抛错时，保留错误并清理；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
72. **S4-R1-072｜异常/结束边界**：在engine抛错时，保留错误并清理；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
73. **S4-R1-073｜只读输入/一次输入**：在非连续数组时，不修改不保留大数组；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
74. **S4-R1-074｜只读输入/单样本分块**：在非连续数组时，不修改不保留大数组；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
75. **S4-R1-075｜只读输入/不规则分块**：在非连续数组时，不修改不保留大数组；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
76. **S4-R1-076｜只读输入/结束边界**：在非连续数组时，不修改不保留大数组；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
77. **S4-R1-077｜参数/一次输入**：在负长度非有限配置时，显式拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
78. **S4-R1-078｜参数/单样本分块**：在负长度非有限配置时，显式拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
79. **S4-R1-079｜参数/不规则分块**：在负长度非有限配置时，显式拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
80. **S4-R1-080｜参数/结束边界**：在负长度非有限配置时，显式拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
81. **S4-R1-081｜计数/一次输入**：在正常与取消结束时，逐项守恒区分wire；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
82. **S4-R1-082｜计数/单样本分块**：在正常与取消结束时，逐项守恒区分wire；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
83. **S4-R1-083｜计数/不规则分块**：在正常与取消结束时，逐项守恒区分wire；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
84. **S4-R1-084｜计数/结束边界**：在正常与取消结束时，逐项守恒区分wire；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
85. **S4-R1-085｜worker首帧/一次输入**：在finish才得到短音时，走实际DSP和帧编码；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
86. **S4-R1-086｜worker首帧/单样本分块**：在finish才得到短音时，走实际DSP和帧编码；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
87. **S4-R1-087｜worker首帧/不规则分块**：在finish才得到短音时，走实际DSP和帧编码；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
88. **S4-R1-088｜worker首帧/结束边界**：在finish才得到短音时，走实际DSP和帧编码；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
89. **S4-R1-089｜取消交错/一次输入**：在drain返回后cancel时，最终emit前重查；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
90. **S4-R1-090｜取消交错/单样本分块**：在drain返回后cancel时，最终emit前重查；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
91. **S4-R1-091｜取消交错/不规则分块**：在drain返回后cancel时，最终emit前重查；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
92. **S4-R1-092｜取消交错/结束边界**：在drain返回后cancel时，最终emit前重查；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
93. **S4-R1-093｜性能/一次输入**：在1920及大块时，测CPU不冒首声；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
94. **S4-R1-094｜性能/单样本分块**：在1920及大块时，测CPU不冒首声；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
95. **S4-R1-095｜性能/不规则分块**：在1920及大块时，测CPU不冒首声；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
96. **S4-R1-096｜性能/结束边界**：在1920及大块时，测CPU不冒首声；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
97. **S4-R1-097｜冻结封存/一次输入**：在旧探针和562合同时，不改期望缺陷来伪造修复；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
98. **S4-R1-098｜冻结封存/单样本分块**：在旧探针和562合同时，不改期望缺陷来伪造修复；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
99. **S4-R1-099｜冻结封存/不规则分块**：在旧探针和562合同时，不改期望缺陷来伪造修复；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
100. **S4-R1-100｜冻结封存/结束边界**：在旧探针和562合同时，不改期望缺陷来伪造修复；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。

---

## 内嵌备忘录：KAGGLE_STEP18_S4_REVIEW_R2.md

# S4 R2：数值复核100建议

建议不是执行成绩；不代表声学、完整模型、真实训练验收。

1. **S4-R2-001｜短块/零输入**：在1..119样本调用时，保存残帧直到固定网格或finish；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
2. **S4-R2-002｜短块/有声合成波形**：在1..119样本调用时，保存残帧直到固定网格或finish；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
3. **S4-R2-003｜短块/门限附近输入**：在1..119样本调用时，保存残帧直到固定网格或finish；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
4. **S4-R2-004｜短块/只读与极值输入**：在1..119样本调用时，保存残帧直到固定网格或finish；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
5. **S4-R2-005｜网格边缘/零输入**：在119/120/121样本时，不按调用重置检测网格；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
6. **S4-R2-006｜网格边缘/有声合成波形**：在119/120/121样本时，不按调用重置检测网格；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
7. **S4-R2-007｜网格边缘/门限附近输入**：在119/120/121样本时，不按调用重置检测网格；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
8. **S4-R2-008｜网格边缘/只读与极值输入**：在119/120/121样本时，不按调用重置检测网格；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
9. **S4-R2-009｜前史/零输入**：在960低电平后2400有声时，保留跨块840前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
10. **S4-R2-010｜前史/有声合成波形**：在960低电平后2400有声时，保留跨块840前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
11. **S4-R2-011｜前史/门限附近输入**：在960低电平后2400有声时，保留跨块840前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
12. **S4-R2-012｜前史/只读与极值输入**：在960低电平后2400有声时，保留跨块840前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
13. **S4-R2-013｜零前史/零输入**：在keep=0时，明确允许丢领先静音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
14. **S4-R2-014｜零前史/有声合成波形**：在keep=0时，明确允许丢领先静音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
15. **S4-R2-015｜零前史/门限附近输入**：在keep=0时，明确允许丢领先静音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
16. **S4-R2-016｜零前史/只读与极值输入**：在keep=0时，明确允许丢领先静音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
17. **S4-R2-017｜尾残帧/零输入**：在末尾60非零时，实际长度检测并输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
18. **S4-R2-018｜尾残帧/有声合成波形**：在末尾60非零时，实际长度检测并输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
19. **S4-R2-019｜尾残帧/门限附近输入**：在末尾60非零时，实际长度检测并输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
20. **S4-R2-020｜尾残帧/只读与极值输入**：在末尾60非零时，实际长度检测并输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
21. **S4-R2-021｜低电平尾/零输入**：在已开始后低于阈值非零时，finish不按门限删非零尾；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
22. **S4-R2-022｜低电平尾/有声合成波形**：在已开始后低于阈值非零时，finish不按门限删非零尾；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
23. **S4-R2-023｜低电平尾/门限附近输入**：在已开始后低于阈值非零时，finish不按门限删非零尾；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
24. **S4-R2-024｜低电平尾/只读与极值输入**：在已开始后低于阈值非零时，finish不按门限删非零尾；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
25. **S4-R2-025｜精确零尾/零输入**：在连续全零结束时，只删可计数精确零；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
26. **S4-R2-026｜精确零尾/有声合成波形**：在连续全零结束时，只删可计数精确零；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
27. **S4-R2-027｜精确零尾/门限附近输入**：在连续全零结束时，只删可计数精确零；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
28. **S4-R2-028｜精确零尾/只读与极值输入**：在连续全零结束时，只删可计数精确零；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
29. **S4-R2-029｜中间停顿/零输入**：在两有声段间静音时，按原序释放不缩句中停顿；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
30. **S4-R2-030｜中间停顿/有声合成波形**：在两有声段间静音时，按原序释放不缩句中停顿；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
31. **S4-R2-031｜中间停顿/门限附近输入**：在两有声段间静音时，按原序释放不缩句中停顿；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
32. **S4-R2-032｜中间停顿/只读与极值输入**：在两有声段间静音时，按原序释放不缩句中停顿；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
33. **S4-R2-033｜长尾队列/零输入**：在超过max_held时，超额输出不删音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
34. **S4-R2-034｜长尾队列/有声合成波形**：在超过max_held时，超额输出不删音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
35. **S4-R2-035｜长尾队列/门限附近输入**：在超过max_held时，超额输出不删音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
36. **S4-R2-036｜长尾队列/只读与极值输入**：在超过max_held时，超额输出不删音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
37. **S4-R2-037｜长前静音/零输入**：在超过max_lead时，固定网格触发并记录越限；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
38. **S4-R2-038｜长前静音/有声合成波形**：在超过max_lead时，固定网格触发并记录越限；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
39. **S4-R2-039｜长前静音/门限附近输入**：在超过max_lead时，固定网格触发并记录越限；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
40. **S4-R2-040｜长前静音/只读与极值输入**：在超过max_lead时，固定网格触发并记录越限；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
41. **S4-R2-041｜纯短语音/零输入**：在全段不足120时，finish必须可输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
42. **S4-R2-042｜纯短语音/有声合成波形**：在全段不足120时，finish必须可输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
43. **S4-R2-043｜纯短语音/门限附近输入**：在全段不足120时，finish必须可输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
44. **S4-R2-044｜纯短语音/只读与极值输入**：在全段不足120时，finish必须可输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
45. **S4-R2-045｜纯低电平/零输入**：在一直未过门限时，保留结束仍缓存非零前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
46. **S4-R2-046｜纯低电平/有声合成波形**：在一直未过门限时，保留结束仍缓存非零前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
47. **S4-R2-047｜纯低电平/门限附近输入**：在一直未过门限时，保留结束仍缓存非零前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
48. **S4-R2-048｜纯低电平/只读与极值输入**：在一直未过门限时，保留结束仍缓存非零前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
49. **S4-R2-049｜空流/零输入**：在无push结束时，空输出且幂等；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
50. **S4-R2-050｜空流/有声合成波形**：在无push结束时，空输出且幂等；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
51. **S4-R2-051｜空流/门限附近输入**：在无push结束时，空输出且幂等；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
52. **S4-R2-052｜空流/只读与极值输入**：在无push结束时，空输出且幂等；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
53. **S4-R2-053｜空块/零输入**：在流中插空时，状态不推进；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
54. **S4-R2-054｜空块/有声合成波形**：在流中插空时，状态不推进；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
55. **S4-R2-055｜空块/门限附近输入**：在流中插空时，状态不推进；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
56. **S4-R2-056｜空块/只读与极值输入**：在流中插空时，状态不推进；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
57. **S4-R2-057｜finish重复/零输入**：在结束调用两次时，第二次空输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
58. **S4-R2-058｜finish重复/有声合成波形**：在结束调用两次时，第二次空输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
59. **S4-R2-059｜finish重复/门限附近输入**：在结束调用两次时，第二次空输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
60. **S4-R2-060｜finish重复/只读与极值输入**：在结束调用两次时，第二次空输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
61. **S4-R2-061｜终止后push/零输入**：在已结束后输入时，明确拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
62. **S4-R2-062｜终止后push/有声合成波形**：在已结束后输入时，明确拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
63. **S4-R2-063｜终止后push/门限附近输入**：在已结束后输入时，明确拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
64. **S4-R2-064｜终止后push/只读与极值输入**：在已结束后输入时，明确拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
65. **S4-R2-065｜取消/零输入**：在持有残帧和尾时，清空不输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
66. **S4-R2-066｜取消/有声合成波形**：在持有残帧和尾时，清空不输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
67. **S4-R2-067｜取消/门限附近输入**：在持有残帧和尾时，清空不输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
68. **S4-R2-068｜取消/只读与极值输入**：在持有残帧和尾时，清空不输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
69. **S4-R2-069｜异常/零输入**：在engine抛错时，保留错误并清理；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
70. **S4-R2-070｜异常/有声合成波形**：在engine抛错时，保留错误并清理；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
71. **S4-R2-071｜异常/门限附近输入**：在engine抛错时，保留错误并清理；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
72. **S4-R2-072｜异常/只读与极值输入**：在engine抛错时，保留错误并清理；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
73. **S4-R2-073｜只读输入/零输入**：在非连续数组时，不修改不保留大数组；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
74. **S4-R2-074｜只读输入/有声合成波形**：在非连续数组时，不修改不保留大数组；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
75. **S4-R2-075｜只读输入/门限附近输入**：在非连续数组时，不修改不保留大数组；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
76. **S4-R2-076｜只读输入/只读与极值输入**：在非连续数组时，不修改不保留大数组；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
77. **S4-R2-077｜参数/零输入**：在负长度非有限配置时，显式拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
78. **S4-R2-078｜参数/有声合成波形**：在负长度非有限配置时，显式拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
79. **S4-R2-079｜参数/门限附近输入**：在负长度非有限配置时，显式拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
80. **S4-R2-080｜参数/只读与极值输入**：在负长度非有限配置时，显式拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
81. **S4-R2-081｜计数/零输入**：在正常与取消结束时，逐项守恒区分wire；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
82. **S4-R2-082｜计数/有声合成波形**：在正常与取消结束时，逐项守恒区分wire；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
83. **S4-R2-083｜计数/门限附近输入**：在正常与取消结束时，逐项守恒区分wire；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
84. **S4-R2-084｜计数/只读与极值输入**：在正常与取消结束时，逐项守恒区分wire；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
85. **S4-R2-085｜worker首帧/零输入**：在finish才得到短音时，走实际DSP和帧编码；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
86. **S4-R2-086｜worker首帧/有声合成波形**：在finish才得到短音时，走实际DSP和帧编码；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
87. **S4-R2-087｜worker首帧/门限附近输入**：在finish才得到短音时，走实际DSP和帧编码；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
88. **S4-R2-088｜worker首帧/只读与极值输入**：在finish才得到短音时，走实际DSP和帧编码；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
89. **S4-R2-089｜取消交错/零输入**：在drain返回后cancel时，最终emit前重查；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
90. **S4-R2-090｜取消交错/有声合成波形**：在drain返回后cancel时，最终emit前重查；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
91. **S4-R2-091｜取消交错/门限附近输入**：在drain返回后cancel时，最终emit前重查；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
92. **S4-R2-092｜取消交错/只读与极值输入**：在drain返回后cancel时，最终emit前重查；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
93. **S4-R2-093｜性能/零输入**：在1920及大块时，测CPU不冒首声；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
94. **S4-R2-094｜性能/有声合成波形**：在1920及大块时，测CPU不冒首声；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
95. **S4-R2-095｜性能/门限附近输入**：在1920及大块时，测CPU不冒首声；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
96. **S4-R2-096｜性能/只读与极值输入**：在1920及大块时，测CPU不冒首声；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
97. **S4-R2-097｜冻结封存/零输入**：在旧探针和562合同时，不改期望缺陷来伪造修复；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
98. **S4-R2-098｜冻结封存/有声合成波形**：在旧探针和562合同时，不改期望缺陷来伪造修复；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
99. **S4-R2-099｜冻结封存/门限附近输入**：在旧探针和562合同时，不改期望缺陷来伪造修复；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
100. **S4-R2-100｜冻结封存/只读与极值输入**：在旧探针和562合同时，不改期望缺陷来伪造修复；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。

---

## 内嵌备忘录：KAGGLE_STEP18_S4_REVIEW_R3.md

# S4 R3：集成复核100建议

建议不是执行成绩；不代表声学、完整模型、真实训练验收。

1. **S4-R3-001｜短块/直接调用**：在1..119样本调用时，保存残帧直到固定网格或finish；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
2. **S4-R3-002｜短块/旧版失败对照**：在1..119样本调用时，保存残帧直到固定网格或finish；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
3. **S4-R3-003｜短块/真实worker替身引擎**：在1..119样本调用时，保存残帧直到固定网格或finish；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
4. **S4-R3-004｜短块/独立回归封存**：在1..119样本调用时，保存残帧直到固定网格或finish；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
5. **S4-R3-005｜网格边缘/直接调用**：在119/120/121样本时，不按调用重置检测网格；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
6. **S4-R3-006｜网格边缘/旧版失败对照**：在119/120/121样本时，不按调用重置检测网格；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
7. **S4-R3-007｜网格边缘/真实worker替身引擎**：在119/120/121样本时，不按调用重置检测网格；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
8. **S4-R3-008｜网格边缘/独立回归封存**：在119/120/121样本时，不按调用重置检测网格；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
9. **S4-R3-009｜前史/直接调用**：在960低电平后2400有声时，保留跨块840前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
10. **S4-R3-010｜前史/旧版失败对照**：在960低电平后2400有声时，保留跨块840前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
11. **S4-R3-011｜前史/真实worker替身引擎**：在960低电平后2400有声时，保留跨块840前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
12. **S4-R3-012｜前史/独立回归封存**：在960低电平后2400有声时，保留跨块840前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
13. **S4-R3-013｜零前史/直接调用**：在keep=0时，明确允许丢领先静音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
14. **S4-R3-014｜零前史/旧版失败对照**：在keep=0时，明确允许丢领先静音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
15. **S4-R3-015｜零前史/真实worker替身引擎**：在keep=0时，明确允许丢领先静音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
16. **S4-R3-016｜零前史/独立回归封存**：在keep=0时，明确允许丢领先静音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
17. **S4-R3-017｜尾残帧/直接调用**：在末尾60非零时，实际长度检测并输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
18. **S4-R3-018｜尾残帧/旧版失败对照**：在末尾60非零时，实际长度检测并输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
19. **S4-R3-019｜尾残帧/真实worker替身引擎**：在末尾60非零时，实际长度检测并输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
20. **S4-R3-020｜尾残帧/独立回归封存**：在末尾60非零时，实际长度检测并输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
21. **S4-R3-021｜低电平尾/直接调用**：在已开始后低于阈值非零时，finish不按门限删非零尾；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
22. **S4-R3-022｜低电平尾/旧版失败对照**：在已开始后低于阈值非零时，finish不按门限删非零尾；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
23. **S4-R3-023｜低电平尾/真实worker替身引擎**：在已开始后低于阈值非零时，finish不按门限删非零尾；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
24. **S4-R3-024｜低电平尾/独立回归封存**：在已开始后低于阈值非零时，finish不按门限删非零尾；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
25. **S4-R3-025｜精确零尾/直接调用**：在连续全零结束时，只删可计数精确零；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
26. **S4-R3-026｜精确零尾/旧版失败对照**：在连续全零结束时，只删可计数精确零；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
27. **S4-R3-027｜精确零尾/真实worker替身引擎**：在连续全零结束时，只删可计数精确零；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
28. **S4-R3-028｜精确零尾/独立回归封存**：在连续全零结束时，只删可计数精确零；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
29. **S4-R3-029｜中间停顿/直接调用**：在两有声段间静音时，按原序释放不缩句中停顿；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
30. **S4-R3-030｜中间停顿/旧版失败对照**：在两有声段间静音时，按原序释放不缩句中停顿；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
31. **S4-R3-031｜中间停顿/真实worker替身引擎**：在两有声段间静音时，按原序释放不缩句中停顿；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
32. **S4-R3-032｜中间停顿/独立回归封存**：在两有声段间静音时，按原序释放不缩句中停顿；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
33. **S4-R3-033｜长尾队列/直接调用**：在超过max_held时，超额输出不删音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
34. **S4-R3-034｜长尾队列/旧版失败对照**：在超过max_held时，超额输出不删音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
35. **S4-R3-035｜长尾队列/真实worker替身引擎**：在超过max_held时，超额输出不删音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
36. **S4-R3-036｜长尾队列/独立回归封存**：在超过max_held时，超额输出不删音；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
37. **S4-R3-037｜长前静音/直接调用**：在超过max_lead时，固定网格触发并记录越限；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
38. **S4-R3-038｜长前静音/旧版失败对照**：在超过max_lead时，固定网格触发并记录越限；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
39. **S4-R3-039｜长前静音/真实worker替身引擎**：在超过max_lead时，固定网格触发并记录越限；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
40. **S4-R3-040｜长前静音/独立回归封存**：在超过max_lead时，固定网格触发并记录越限；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
41. **S4-R3-041｜纯短语音/直接调用**：在全段不足120时，finish必须可输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
42. **S4-R3-042｜纯短语音/旧版失败对照**：在全段不足120时，finish必须可输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
43. **S4-R3-043｜纯短语音/真实worker替身引擎**：在全段不足120时，finish必须可输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
44. **S4-R3-044｜纯短语音/独立回归封存**：在全段不足120时，finish必须可输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
45. **S4-R3-045｜纯低电平/直接调用**：在一直未过门限时，保留结束仍缓存非零前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
46. **S4-R3-046｜纯低电平/旧版失败对照**：在一直未过门限时，保留结束仍缓存非零前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
47. **S4-R3-047｜纯低电平/真实worker替身引擎**：在一直未过门限时，保留结束仍缓存非零前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
48. **S4-R3-048｜纯低电平/独立回归封存**：在一直未过门限时，保留结束仍缓存非零前史；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
49. **S4-R3-049｜空流/直接调用**：在无push结束时，空输出且幂等；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
50. **S4-R3-050｜空流/旧版失败对照**：在无push结束时，空输出且幂等；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
51. **S4-R3-051｜空流/真实worker替身引擎**：在无push结束时，空输出且幂等；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
52. **S4-R3-052｜空流/独立回归封存**：在无push结束时，空输出且幂等；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
53. **S4-R3-053｜空块/直接调用**：在流中插空时，状态不推进；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
54. **S4-R3-054｜空块/旧版失败对照**：在流中插空时，状态不推进；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
55. **S4-R3-055｜空块/真实worker替身引擎**：在流中插空时，状态不推进；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
56. **S4-R3-056｜空块/独立回归封存**：在流中插空时，状态不推进；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
57. **S4-R3-057｜finish重复/直接调用**：在结束调用两次时，第二次空输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
58. **S4-R3-058｜finish重复/旧版失败对照**：在结束调用两次时，第二次空输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
59. **S4-R3-059｜finish重复/真实worker替身引擎**：在结束调用两次时，第二次空输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
60. **S4-R3-060｜finish重复/独立回归封存**：在结束调用两次时，第二次空输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
61. **S4-R3-061｜终止后push/直接调用**：在已结束后输入时，明确拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
62. **S4-R3-062｜终止后push/旧版失败对照**：在已结束后输入时，明确拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
63. **S4-R3-063｜终止后push/真实worker替身引擎**：在已结束后输入时，明确拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
64. **S4-R3-064｜终止后push/独立回归封存**：在已结束后输入时，明确拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
65. **S4-R3-065｜取消/直接调用**：在持有残帧和尾时，清空不输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
66. **S4-R3-066｜取消/旧版失败对照**：在持有残帧和尾时，清空不输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
67. **S4-R3-067｜取消/真实worker替身引擎**：在持有残帧和尾时，清空不输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
68. **S4-R3-068｜取消/独立回归封存**：在持有残帧和尾时，清空不输出；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
69. **S4-R3-069｜异常/直接调用**：在engine抛错时，保留错误并清理；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
70. **S4-R3-070｜异常/旧版失败对照**：在engine抛错时，保留错误并清理；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
71. **S4-R3-071｜异常/真实worker替身引擎**：在engine抛错时，保留错误并清理；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
72. **S4-R3-072｜异常/独立回归封存**：在engine抛错时，保留错误并清理；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
73. **S4-R3-073｜只读输入/直接调用**：在非连续数组时，不修改不保留大数组；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
74. **S4-R3-074｜只读输入/旧版失败对照**：在非连续数组时，不修改不保留大数组；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
75. **S4-R3-075｜只读输入/真实worker替身引擎**：在非连续数组时，不修改不保留大数组；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
76. **S4-R3-076｜只读输入/独立回归封存**：在非连续数组时，不修改不保留大数组；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
77. **S4-R3-077｜参数/直接调用**：在负长度非有限配置时，显式拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
78. **S4-R3-078｜参数/旧版失败对照**：在负长度非有限配置时，显式拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
79. **S4-R3-079｜参数/真实worker替身引擎**：在负长度非有限配置时，显式拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
80. **S4-R3-080｜参数/独立回归封存**：在负长度非有限配置时，显式拒绝；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
81. **S4-R3-081｜计数/直接调用**：在正常与取消结束时，逐项守恒区分wire；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
82. **S4-R3-082｜计数/旧版失败对照**：在正常与取消结束时，逐项守恒区分wire；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
83. **S4-R3-083｜计数/真实worker替身引擎**：在正常与取消结束时，逐项守恒区分wire；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
84. **S4-R3-084｜计数/独立回归封存**：在正常与取消结束时，逐项守恒区分wire；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
85. **S4-R3-085｜worker首帧/直接调用**：在finish才得到短音时，走实际DSP和帧编码；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
86. **S4-R3-086｜worker首帧/旧版失败对照**：在finish才得到短音时，走实际DSP和帧编码；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
87. **S4-R3-087｜worker首帧/真实worker替身引擎**：在finish才得到短音时，走实际DSP和帧编码；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
88. **S4-R3-088｜worker首帧/独立回归封存**：在finish才得到短音时，走实际DSP和帧编码；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
89. **S4-R3-089｜取消交错/直接调用**：在drain返回后cancel时，最终emit前重查；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
90. **S4-R3-090｜取消交错/旧版失败对照**：在drain返回后cancel时，最终emit前重查；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
91. **S4-R3-091｜取消交错/真实worker替身引擎**：在drain返回后cancel时，最终emit前重查；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
92. **S4-R3-092｜取消交错/独立回归封存**：在drain返回后cancel时，最终emit前重查；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
93. **S4-R3-093｜性能/直接调用**：在1920及大块时，测CPU不冒首声；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
94. **S4-R3-094｜性能/旧版失败对照**：在1920及大块时，测CPU不冒首声；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
95. **S4-R3-095｜性能/真实worker替身引擎**：在1920及大块时，测CPU不冒首声；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
96. **S4-R3-096｜性能/独立回归封存**：在1920及大块时，测CPU不冒首声；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
97. **S4-R3-097｜冻结封存/直接调用**：在旧探针和562合同时，不改期望缺陷来伪造修复；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
98. **S4-R3-098｜冻结封存/旧版失败对照**：在旧探针和562合同时，不改期望缺陷来伪造修复；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
99. **S4-R3-099｜冻结封存/真实worker替身引擎**：在旧探针和562合同时，不改期望缺陷来伪造修复；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。
100. **S4-R3-100｜冻结封存/独立回归封存**：在旧探针和562合同时，不改期望缺陷来伪造修复；记录该路径输入/返回/缓存/丢弃数与顺序；未执行必须保留未验收，不能用其他路径代替。

---

## 内嵌备忘录：KAGGLE_STEP18_S4_TRIMMER.md

# S4：有界裁剪与 worker 正常/取消收尾实际修复

**已完成隔离候选的限定工程修复，整体仍 PARTIAL/BLOCKED；18 未发布、未部署。不能保证一定成功或声音已无沙沙。**

## 代码与接入

新增 `kaggle/step18/step18_trimmer.py` 和可运行的 `worker_s4.py`，不是仅加测试替身。保留S3的 `worker.py`/DSP和原合同；新worker仅替换裁剪器导入和 `Worker.run_job`，其他命名函数/方法AST保持。

- 固定120样本RMS网格跨调用累计，残帧不足一格仍保留，正常finish按实际残帧长度检测。worker固定24kHz下最多增加不足5ms检测等待，不引入整句缓冲。
- 35ms前史跨块保留；不是只在当前检测块内回看。领先历史的实际丢弃数量单独计数。
- 有声后先保留keep窗口，尾队列最多1800ms；超出预算按顺序输出而非删除内部停顿。deque分块复制，不持有整段输入数组。
- 正常finish保留当前仍缓存的全部非零尾（含低于阈值的弱信号），只允许裁掉可计数的精确零尾。finish幂等，关闭后拒绝push。
- worker结束时真正调用finish，余数走相同DSP和PCM计数/帧编码；不足120样本的整个短段也可在结束时输出。取消/异常清缓存，不排旧尾、不补192样本衰减尾。
- 输出 `stats.trim`：输入/返回/领先丢弃/精确零尾丢弃/取消丢弃/缓存和守恒。返回样本不等于已播放样本；finish返回后取消的样本另记 `cancelled_after_trim_samples`。最终发帧前重查取消，但不宣称线程事件与声卡播放原子化。
- 输入只读、非连续、非有限样本和float32极值有明确测试；阈值平方采用float64，非有限等价置零。

## 最终三轮结果

| 项目 | 结果 | 证据边界 |
|---|---:|---|
| 完整CPU组合 | **602 PASS ×3 =1806 PASS** | 450冻结控制＋112旧候选＋30新裁剪＋10新worker |
| 失败／错误／跳过 | **0／0／0，三轮均如此** | 包含错误注入的预期处理，不是全部业务请求都200 |
| 同套旧版红对照 | 30项，42失败记录，0error/skip | 事前归档S3真实EdgeTrimmer AST；含新增finish/snapshot合同，非42独立bug |
| 同套候选绿对照 | 30 PASS | 固定网格、独立批处理索引oracle、前史、非零尾、取消和计数 |
| 实际worker集成 | 10 PASS/轮 | 原run_job派生、真实裁剪/DSP/frame，engine和pin明确替身 |
| 分块矩阵 | **21组×3，逐样本等于独立参考** | 全有声、跨块预滚、非零尾，各含整段/1/64/119/120/1920/不规则 |
| 长流压力 | **601秒合成流×3** | 每轮14424000样本；4秒周期有声+长静音，确实达到43200样本尾预算，且不超限 |
| 继承真实环回TCP | 237/轮，共711 | 旧S1/S2端点，新S4不新增TCP；不冒真实模型或Go链 |
| 附加检查 | 审计24／Node30／AST57 ×3 | 另JS/repack --check；真实浏览器、Go/Rust未重跑 |

旧562合同逐ID和结果完整继承；其中S3的9项worker合同仍针对保留的S3 worker，新10项针对S4 worker。不能把旧562全称成S4端到端验收。旧DSP/trimmer探针继续保留缺陷观察，没有修改期望来伪造旧版通过。

### 具体缺陷前后

- 60样本完整有声段：旧版可全丢，新候选finish输出60样本，worker再输出明确192样本衰减尾；统计speech_samples仍为60。
- 960样本低电平＋2400有声，按两块输入：新候选保留840样本前史，输出3240；不是删前史换首声。
- 有声后长静音再60样本低电平非零尾：新候选把尾样本送入真实DSP，不永久留在held后销毁。
- 240有声＋4000精确零：输出1080（含840保留上下文），精确零尾裁掉3160并计数；不拿缩短音频冒RTF提升。
- 残帧取消/引擎错误不drain；finish返回后注入取消时无新PCM/衰减尾，区分trim返回60与wire发送0。

## CPU成本与内存边界

下面是12037样本全有声合成输入（约0.502秒）的CPU耗时三轮范围；旧版无finish，部分分块产出不同，因此**不是等价工作量的提速比较**。

| 调用 | S3旧裁剪CPU ms | S4 CPU ms | 输出说明 |
| 整段 | 0.223–0.353 | 1.102–4.901 | 均12037，但新版提供完整状态/结束合同 |
| 单样本 | 61.105–63.582 | 66.871–111.522 | 旧版0，新版12037 |
| 1920样本 | 0.154–0.405 | 0.724–1.349 | 均12037，但新版提供完整状态/结束合同 |

601秒合成流三轮CPU耗时分别为 1.129/1.097/1.097 秒，裁剪CPU时间/音频时长约 0.001825–0.001878。**本步增加正确性开销，不声称更快**；无模型、声卡或T4数据，不能据此签完整RTF≤0.3或首声。暂不为低绝对开销盲目加多语言/JIT，真实集成预算仍需测量。

压力流没有保留PCM历史；队列逻辑上限为keep前史＋max_held尾＋不足120残帧，处理中至多额外一个检测格的队列插入。push的输入/输出本身随本次调用大小占内存，因此不把逻辑缓存预算冒总进程RSS。601秒只是合成状态压力，不是实际>10分钟录音、全部音频训练或真实模型长文。

## 流程与留错

Q31四选项选C及50行动先完成，三遍专题复核各100建议归档；建议不是300已修bug。最初候选30/10预检均通过。初次旧版红对照41失败＋1error，旧构造器对无限keep_ms抛OverflowError；保持严格ValueError合同，只把该旧异常转成明确断言失败，最终42失败/0error/skip，未改候选迁就测试。初日志、初测试和控制runner源码保留，最终另名control-final。

本步沿用现有venv、无新依赖安装，freeze与S3字节相同。历史1905路径保护，1902匹配，3旧日志缺失仍显式保留，完整历史完整性false。S3可变文档/交接改前归档；原17／53源／94冻结／15正式资产不改。

5条原建议有具体测试ID和三轮收据SHA限定链接，原300最终/功能签收仍0。独立verify_s4核验源码、旧562继承、对照、三轮、缓存/计数与完整交接；最终状态见progress-s4.json，两次核验以stdout文件为准。完整交接106份。

## 封存预检的限定修正（非产品或测试失败）

首次独立封存把所有历史HTTP状态强制逐项相同，因旧S1删除/提交交错测试在本轮1返回200、历史503而被拦。原测试第134行本来明确允许200或503（reload与delete在解锁后谁先完成），三个602套件均通过。已保存初verifier、日志及初manifest；只对这一精确测试ID、POST候选路径将既有{200,503}合同正规化，其余状态仍严格比较，未放宽产品测试或改写CPU/HTTP收据。最终附加检查另命名 `s4-seal-final-checks-roundN.json`，最终独立两次封存以对应stdout为准；初附加检查仍保留但不混算。

## 保留限制与下一步

- 阈值不是真正语音检测器：低于阈值的领先历史仍可能裁掉，只保留35ms前史；不保证弱辅音/全部低电平语音都保留。
- 保留非零尾也可能保留噪声，不能据此宣称无沙沙、相似度或自然度提高；需要用户真实音频和完整模型盲听。
- 双T4、实际训练、首声、完整模型RTF、真实浏览器/物理播放以及Rust等效门禁均未豁免；S3完整native/声学仍未签。
- 正式入口/包/工作台未切换，18未发布。接下来推进 **S5播放器完成后短尾排空**；当前工程修复不代表播放链已排净，也不要求点击Continue。

---

## 内嵌备忘录：KAGGLE_STEP18_Q32_PLAYBACK_DRAIN.md

# Q32：怎样排净完成短尾而不破坏实时缓冲和取消？

顺序自问自答，承接Q31；不向用户提问，不预填Q33。

- A：把所有启动阈值降到0。破坏未完成流欠载保护，拒绝。
- B：结束时直接标ended。只是隐藏滞留、实际删尾，拒绝。
- **C（采用）**：完成流任何正pending可启动；按post总量/消费/dropped计账，等待当前epoch end ACK；显式重采样尾政策。只改隔离完整app候选。
- D：等待整段再播放。损害首声和流式，拒绝。

## 先定义合同

24k源PCM，输出目标Nout=ceil(Nin*contextRate/24000)。线性插值使用固定全局整数坐标；精确端点可立即输出，缺右邻时只保留一输入样本，正常完成末样本保持补足时间；不凭空新增源语音，取消不flush。Worklet内部消息加入epoch，不改网络协议。完成播放需已收到当前流end标记并消费/明确计数丢弃全部post样本；陈旧fill0不能签完成。stop后忽略迟到状态/PCM，新begin不接受旧epoch状态。firstPlayedMs仍为play命令时间，不冒实际可听首声。溢出dropped不是无损排空，必须单列。浏览器测试不等于实体扬声器或真实模型声音。

## 50行动
1. 确认活动分支不换支。
2. 归档S4文档交接和完整app基线。
3. 保护旧源码收据及三份缺日志。
4. 保存npm锁与配置改前SHA。
5. 记录Python环境和npm安装事实。
6. Q32四选项先决策。
7. 三遍各100建议明确非已通过成绩。
8. 新增完整app候选不改冻结17。
9. 固定三个目标采样率合同。
10. 结束后任何正队列可发play。
11. 未结束仍沿用缓冲阈值。
12. 已播放状态不重复发play。
13. 初始短尾和starved恢复都覆盖。
14. 结束空流等待当前Worklet确认。
15. 记录已postPCM样本总数。
16. 用queued减played减dropped计算未消费。
17. 不以陈旧fill0提前结束。
18. 完成需endACK和pending0。
19. stop立即禁用当前流。
20. begin与stop递增内部epoch。
21. 每条内部消息带epoch。
22. Worklet拒绝旧epoch控制。
23. Player拒绝旧epoch状态。
24. 不复用旧流resampler状态。
25. 完成后拒绝新PCM避免越过end。
26. markDone幂等。
27. 重采样用整数全局输出坐标。
28. 精确端点无需等待下一输入。
29. 分数端点只等待一个邻样本。
30. 结束以末样本保持补足时长。
31. 目标输出长度为ceil(N*rate/24000)。
32. 同一重采样政策覆盖一到多样本。
33. 结束补点先PCM再end再play。
34. 取消不补重采样尾。
35. 清空流无额外全零PCM。
36. 只接受完整int16字节不静默吞奇数尾。
37. 保留旧firstPlayedMs含义并不冒声卡计时。
38. VM执行实际Player和Worklet串接。
39. 直接计数Worklet消费不只看play命令。
40. 测超容量dropped而不冒无损。
41. 保留正常欠载一次计数。
42. 测试stop后迟到st不复活。
43. 测试旧流状态不串新流。
44. 同合同旧版红对照并留原错误。
45. 运行602旧CPU组合三轮。
46. Node审计JSrepack三轮。
47. 安装锁定浏览器依赖不改lock。
48. 真实Chromium三轮含旧复制保护。
49. 核对独立封存两次和完整交接。
50. 保留物理扬声器模型T4训练声学门禁。

---

## 内嵌备忘录：KAGGLE_STEP18_S5_REVIEW_R1.md

# S5 R1：状态复核100建议

建议不是执行成绩；未执行项目不得签收，不代表真实声学。

1. **S5-R1-001｜完成20ms/初始路径**：在初始buffering时，正pending触发play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
2. **S5-R1-002｜完成20ms/短块路径**：在初始buffering时，正pending触发play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
3. **S5-R1-003｜完成20ms/结束边界**：在初始buffering时，正pending触发play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
4. **S5-R1-004｜完成20ms/取消边界**：在初始buffering时，正pending触发play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
5. **S5-R1-005｜完成50ms/初始路径**：在正好旧阈值时，不能永久滞留；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
6. **S5-R1-006｜完成50ms/短块路径**：在正好旧阈值时，不能永久滞留；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
7. **S5-R1-007｜完成50ms/结束边界**：在正好旧阈值时，不能永久滞留；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
8. **S5-R1-008｜完成50ms/取消边界**：在正好旧阈值时，不能永久滞留；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
9. **S5-R1-009｜单样本尾/初始路径**：在1源样本时，按目标率计数消费；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
10. **S5-R1-010｜单样本尾/短块路径**：在1源样本时，按目标率计数消费；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
11. **S5-R1-011｜单样本尾/结束边界**：在1源样本时，按目标率计数消费；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
12. **S5-R1-012｜单样本尾/取消边界**：在1源样本时，按目标率计数消费；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
13. **S5-R1-013｜恢复短尾/初始路径**：在starved后完成时，恢复而非等大块；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
14. **S5-R1-014｜恢复短尾/短块路径**：在starved后完成时，恢复而非等大块；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
15. **S5-R1-015｜恢复短尾/结束边界**：在starved后完成时，恢复而非等大块；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
16. **S5-R1-016｜恢复短尾/取消边界**：在starved后完成时，恢复而非等大块；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
17. **S5-R1-017｜实时缓冲/初始路径**：在generationDone=false时，保留原need阈值；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
18. **S5-R1-018｜实时缓冲/短块路径**：在generationDone=false时，保留原need阈值；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
19. **S5-R1-019｜实时缓冲/结束边界**：在generationDone=false时，保留原need阈值；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
20. **S5-R1-020｜实时缓冲/取消边界**：在generationDone=false时，保留原need阈值；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
21. **S5-R1-021｜已播放/初始路径**：在playing时finish时，不重复play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
22. **S5-R1-022｜已播放/短块路径**：在playing时finish时，不重复play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
23. **S5-R1-023｜已播放/结束边界**：在playing时finish时，不重复play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
24. **S5-R1-024｜已播放/取消边界**：在playing时finish时，不重复play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
25. **S5-R1-025｜空流/初始路径**：在0个输入样本时，不合成PCM且等endACK；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
26. **S5-R1-026｜空流/短块路径**：在0个输入样本时，不合成PCM且等endACK；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
27. **S5-R1-027｜空流/结束边界**：在0个输入样本时，不合成PCM且等endACK；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
28. **S5-R1-028｜空流/取消边界**：在0个输入样本时，不合成PCM且等endACK；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
29. **S5-R1-029｜陈旧零fill/初始路径**：在PCM尚未ack时，不提前ended；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
30. **S5-R1-030｜陈旧零fill/短块路径**：在PCM尚未ack时，不提前ended；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
31. **S5-R1-031｜陈旧零fill/结束边界**：在PCM尚未ack时，不提前ended；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
32. **S5-R1-032｜陈旧零fill/取消边界**：在PCM尚未ack时，不提前ended；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
33. **S5-R1-033｜消费ACK/初始路径**：在played追上queued时，只在endACK后结束；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
34. **S5-R1-034｜消费ACK/短块路径**：在played追上queued时，只在endACK后结束；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
35. **S5-R1-035｜消费ACK/结束边界**：在played追上queued时，只在endACK后结束；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
36. **S5-R1-036｜消费ACK/取消边界**：在played追上queued时，只在endACK后结束；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
37. **S5-R1-037｜reset/初始路径**：在stop后旧st时，不复活播放；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
38. **S5-R1-038｜reset/短块路径**：在stop后旧st时，不复活播放；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
39. **S5-R1-039｜reset/结束边界**：在stop后旧st时，不复活播放；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
40. **S5-R1-040｜reset/取消边界**：在stop后旧st时，不复活播放；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
41. **S5-R1-041｜流epoch/初始路径**：在新begin收到旧流状态时，拒绝跨流污染；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
42. **S5-R1-042｜流epoch/短块路径**：在新begin收到旧流状态时，拒绝跨流污染；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
43. **S5-R1-043｜流epoch/结束边界**：在新begin收到旧流状态时，拒绝跨流污染；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
44. **S5-R1-044｜流epoch/取消边界**：在新begin收到旧流状态时，拒绝跨流污染；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
45. **S5-R1-045｜晚PCM/初始路径**：在已结束后再到时，明确拒绝或取消后忽略；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
46. **S5-R1-046｜晚PCM/短块路径**：在已结束后再到时，明确拒绝或取消后忽略；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
47. **S5-R1-047｜晚PCM/结束边界**：在已结束后再到时，明确拒绝或取消后忽略；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
48. **S5-R1-048｜晚PCM/取消边界**：在已结束后再到时，明确拒绝或取消后忽略；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
49. **S5-R1-049｜重复完成/初始路径**：在markDone两次时，不重复补点；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
50. **S5-R1-050｜重复完成/短块路径**：在markDone两次时，不重复补点；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
51. **S5-R1-051｜重复完成/结束边界**：在markDone两次时，不重复补点；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
52. **S5-R1-052｜重复完成/取消边界**：在markDone两次时，不重复补点；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
53. **S5-R1-053｜重采样长度/初始路径**：在24/44.1/48k时，ceil精确时长政策；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
54. **S5-R1-054｜重采样长度/短块路径**：在24/44.1/48k时，ceil精确时长政策；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
55. **S5-R1-055｜重采样长度/结束边界**：在24/44.1/48k时，ceil精确时长政策；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
56. **S5-R1-056｜重采样长度/取消边界**：在24/44.1/48k时，ceil精确时长政策；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
57. **S5-R1-057｜插值边界/初始路径**：在分数位置缺右邻时，仅保留一邻样本；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
58. **S5-R1-058｜插值边界/短块路径**：在分数位置缺右邻时，仅保留一邻样本；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
59. **S5-R1-059｜插值边界/结束边界**：在分数位置缺右邻时，仅保留一邻样本；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
60. **S5-R1-060｜插值边界/取消边界**：在分数位置缺右邻时，仅保留一邻样本；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
61. **S5-R1-061｜端点/初始路径**：在恰好整数采样位置时，不等待无用未来；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
62. **S5-R1-062｜端点/短块路径**：在恰好整数采样位置时，不等待无用未来；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
63. **S5-R1-063｜端点/结束边界**：在恰好整数采样位置时，不等待无用未来；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
64. **S5-R1-064｜端点/取消边界**：在恰好整数采样位置时，不等待无用未来；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
65. **S5-R1-065｜多块插值/初始路径**：在任意切分时，与整段逐样本一致；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
66. **S5-R1-066｜多块插值/短块路径**：在任意切分时，与整段逐样本一致；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
67. **S5-R1-067｜多块插值/结束边界**：在任意切分时，与整段逐样本一致；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
68. **S5-R1-068｜多块插值/取消边界**：在任意切分时，与整段逐样本一致；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
69. **S5-R1-069｜取消插值/初始路径**：在保留终端邻样本时，不补尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
70. **S5-R1-070｜取消插值/短块路径**：在保留终端邻样本时，不补尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
71. **S5-R1-071｜取消插值/结束边界**：在保留终端邻样本时，不补尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
72. **S5-R1-072｜取消插值/取消边界**：在保留终端邻样本时，不补尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
73. **S5-R1-073｜奇数字节/初始路径**：在坏PCM帧时，不静默吞尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
74. **S5-R1-074｜奇数字节/短块路径**：在坏PCM帧时，不静默吞尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
75. **S5-R1-075｜奇数字节/结束边界**：在坏PCM帧时，不静默吞尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
76. **S5-R1-076｜奇数字节/取消边界**：在坏PCM帧时，不静默吞尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
77. **S5-R1-077｜欠载/初始路径**：在未完成时耗尽时，一次计数并可恢复；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
78. **S5-R1-078｜欠载/短块路径**：在未完成时耗尽时，一次计数并可恢复；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
79. **S5-R1-079｜欠载/结束边界**：在未完成时耗尽时，一次计数并可恢复；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
80. **S5-R1-080｜欠载/取消边界**：在未完成时耗尽时，一次计数并可恢复；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
81. **S5-R1-081｜溢出/初始路径**：在cap缩小的合成测试时，dropped显式不是无损；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
82. **S5-R1-082｜溢出/短块路径**：在cap缩小的合成测试时，dropped显式不是无损；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
83. **S5-R1-083｜溢出/结束边界**：在cap缩小的合成测试时，dropped显式不是无损；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
84. **S5-R1-084｜溢出/取消边界**：在cap缩小的合成测试时，dropped显式不是无损；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
85. **S5-R1-085｜实际Worklet/初始路径**：在真实Chromium合成PCM时，计数消费而非声卡保证；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
86. **S5-R1-086｜实际Worklet/短块路径**：在真实Chromium合成PCM时，计数消费而非声卡保证；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
87. **S5-R1-087｜实际Worklet/结束边界**：在真实Chromium合成PCM时，计数消费而非声卡保证；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
88. **S5-R1-088｜实际Worklet/取消边界**：在真实Chromium合成PCM时，计数消费而非声卡保证；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
89. **S5-R1-089｜完整UI接入/初始路径**：在完整app候选时，保持正式入口和旧功能；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
90. **S5-R1-090｜完整UI接入/短块路径**：在完整app候选时，保持正式入口和旧功能；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
91. **S5-R1-091｜完整UI接入/结束边界**：在完整app候选时，保持正式入口和旧功能；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
92. **S5-R1-092｜完整UI接入/取消边界**：在完整app候选时，保持正式入口和旧功能；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
93. **S5-R1-093｜复制保护/初始路径**：在旧浏览器套件时，完整文本字节与录音保护；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
94. **S5-R1-094｜复制保护/短块路径**：在旧浏览器套件时，完整文本字节与录音保护；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
95. **S5-R1-095｜复制保护/结束边界**：在旧浏览器套件时，完整文本字节与录音保护；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
96. **S5-R1-096｜复制保护/取消边界**：在旧浏览器套件时，完整文本字节与录音保护；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
97. **S5-R1-097｜封存/初始路径**：在独立SHA/双验证时，不改旧失败探针；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
98. **S5-R1-098｜封存/短块路径**：在独立SHA/双验证时，不改旧失败探针；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
99. **S5-R1-099｜封存/结束边界**：在独立SHA/双验证时，不改旧失败探针；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
100. **S5-R1-100｜封存/取消边界**：在独立SHA/双验证时，不改旧失败探针；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。

---

## 内嵌备忘录：KAGGLE_STEP18_S5_REVIEW_R2.md

# S5 R2：数值复核100建议

建议不是执行成绩；未执行项目不得签收，不代表真实声学。

1. **S5-R2-001｜完成20ms/单样本**：在初始buffering时，正pending触发play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
2. **S5-R2-002｜完成20ms/正常合成PCM**：在初始buffering时，正pending触发play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
3. **S5-R2-003｜完成20ms/跨采样率**：在初始buffering时，正pending触发play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
4. **S5-R2-004｜完成20ms/分块和空块**：在初始buffering时，正pending触发play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
5. **S5-R2-005｜完成50ms/单样本**：在正好旧阈值时，不能永久滞留；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
6. **S5-R2-006｜完成50ms/正常合成PCM**：在正好旧阈值时，不能永久滞留；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
7. **S5-R2-007｜完成50ms/跨采样率**：在正好旧阈值时，不能永久滞留；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
8. **S5-R2-008｜完成50ms/分块和空块**：在正好旧阈值时，不能永久滞留；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
9. **S5-R2-009｜单样本尾/单样本**：在1源样本时，按目标率计数消费；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
10. **S5-R2-010｜单样本尾/正常合成PCM**：在1源样本时，按目标率计数消费；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
11. **S5-R2-011｜单样本尾/跨采样率**：在1源样本时，按目标率计数消费；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
12. **S5-R2-012｜单样本尾/分块和空块**：在1源样本时，按目标率计数消费；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
13. **S5-R2-013｜恢复短尾/单样本**：在starved后完成时，恢复而非等大块；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
14. **S5-R2-014｜恢复短尾/正常合成PCM**：在starved后完成时，恢复而非等大块；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
15. **S5-R2-015｜恢复短尾/跨采样率**：在starved后完成时，恢复而非等大块；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
16. **S5-R2-016｜恢复短尾/分块和空块**：在starved后完成时，恢复而非等大块；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
17. **S5-R2-017｜实时缓冲/单样本**：在generationDone=false时，保留原need阈值；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
18. **S5-R2-018｜实时缓冲/正常合成PCM**：在generationDone=false时，保留原need阈值；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
19. **S5-R2-019｜实时缓冲/跨采样率**：在generationDone=false时，保留原need阈值；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
20. **S5-R2-020｜实时缓冲/分块和空块**：在generationDone=false时，保留原need阈值；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
21. **S5-R2-021｜已播放/单样本**：在playing时finish时，不重复play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
22. **S5-R2-022｜已播放/正常合成PCM**：在playing时finish时，不重复play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
23. **S5-R2-023｜已播放/跨采样率**：在playing时finish时，不重复play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
24. **S5-R2-024｜已播放/分块和空块**：在playing时finish时，不重复play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
25. **S5-R2-025｜空流/单样本**：在0个输入样本时，不合成PCM且等endACK；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
26. **S5-R2-026｜空流/正常合成PCM**：在0个输入样本时，不合成PCM且等endACK；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
27. **S5-R2-027｜空流/跨采样率**：在0个输入样本时，不合成PCM且等endACK；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
28. **S5-R2-028｜空流/分块和空块**：在0个输入样本时，不合成PCM且等endACK；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
29. **S5-R2-029｜陈旧零fill/单样本**：在PCM尚未ack时，不提前ended；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
30. **S5-R2-030｜陈旧零fill/正常合成PCM**：在PCM尚未ack时，不提前ended；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
31. **S5-R2-031｜陈旧零fill/跨采样率**：在PCM尚未ack时，不提前ended；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
32. **S5-R2-032｜陈旧零fill/分块和空块**：在PCM尚未ack时，不提前ended；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
33. **S5-R2-033｜消费ACK/单样本**：在played追上queued时，只在endACK后结束；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
34. **S5-R2-034｜消费ACK/正常合成PCM**：在played追上queued时，只在endACK后结束；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
35. **S5-R2-035｜消费ACK/跨采样率**：在played追上queued时，只在endACK后结束；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
36. **S5-R2-036｜消费ACK/分块和空块**：在played追上queued时，只在endACK后结束；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
37. **S5-R2-037｜reset/单样本**：在stop后旧st时，不复活播放；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
38. **S5-R2-038｜reset/正常合成PCM**：在stop后旧st时，不复活播放；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
39. **S5-R2-039｜reset/跨采样率**：在stop后旧st时，不复活播放；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
40. **S5-R2-040｜reset/分块和空块**：在stop后旧st时，不复活播放；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
41. **S5-R2-041｜流epoch/单样本**：在新begin收到旧流状态时，拒绝跨流污染；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
42. **S5-R2-042｜流epoch/正常合成PCM**：在新begin收到旧流状态时，拒绝跨流污染；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
43. **S5-R2-043｜流epoch/跨采样率**：在新begin收到旧流状态时，拒绝跨流污染；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
44. **S5-R2-044｜流epoch/分块和空块**：在新begin收到旧流状态时，拒绝跨流污染；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
45. **S5-R2-045｜晚PCM/单样本**：在已结束后再到时，明确拒绝或取消后忽略；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
46. **S5-R2-046｜晚PCM/正常合成PCM**：在已结束后再到时，明确拒绝或取消后忽略；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
47. **S5-R2-047｜晚PCM/跨采样率**：在已结束后再到时，明确拒绝或取消后忽略；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
48. **S5-R2-048｜晚PCM/分块和空块**：在已结束后再到时，明确拒绝或取消后忽略；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
49. **S5-R2-049｜重复完成/单样本**：在markDone两次时，不重复补点；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
50. **S5-R2-050｜重复完成/正常合成PCM**：在markDone两次时，不重复补点；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
51. **S5-R2-051｜重复完成/跨采样率**：在markDone两次时，不重复补点；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
52. **S5-R2-052｜重复完成/分块和空块**：在markDone两次时，不重复补点；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
53. **S5-R2-053｜重采样长度/单样本**：在24/44.1/48k时，ceil精确时长政策；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
54. **S5-R2-054｜重采样长度/正常合成PCM**：在24/44.1/48k时，ceil精确时长政策；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
55. **S5-R2-055｜重采样长度/跨采样率**：在24/44.1/48k时，ceil精确时长政策；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
56. **S5-R2-056｜重采样长度/分块和空块**：在24/44.1/48k时，ceil精确时长政策；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
57. **S5-R2-057｜插值边界/单样本**：在分数位置缺右邻时，仅保留一邻样本；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
58. **S5-R2-058｜插值边界/正常合成PCM**：在分数位置缺右邻时，仅保留一邻样本；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
59. **S5-R2-059｜插值边界/跨采样率**：在分数位置缺右邻时，仅保留一邻样本；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
60. **S5-R2-060｜插值边界/分块和空块**：在分数位置缺右邻时，仅保留一邻样本；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
61. **S5-R2-061｜端点/单样本**：在恰好整数采样位置时，不等待无用未来；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
62. **S5-R2-062｜端点/正常合成PCM**：在恰好整数采样位置时，不等待无用未来；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
63. **S5-R2-063｜端点/跨采样率**：在恰好整数采样位置时，不等待无用未来；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
64. **S5-R2-064｜端点/分块和空块**：在恰好整数采样位置时，不等待无用未来；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
65. **S5-R2-065｜多块插值/单样本**：在任意切分时，与整段逐样本一致；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
66. **S5-R2-066｜多块插值/正常合成PCM**：在任意切分时，与整段逐样本一致；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
67. **S5-R2-067｜多块插值/跨采样率**：在任意切分时，与整段逐样本一致；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
68. **S5-R2-068｜多块插值/分块和空块**：在任意切分时，与整段逐样本一致；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
69. **S5-R2-069｜取消插值/单样本**：在保留终端邻样本时，不补尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
70. **S5-R2-070｜取消插值/正常合成PCM**：在保留终端邻样本时，不补尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
71. **S5-R2-071｜取消插值/跨采样率**：在保留终端邻样本时，不补尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
72. **S5-R2-072｜取消插值/分块和空块**：在保留终端邻样本时，不补尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
73. **S5-R2-073｜奇数字节/单样本**：在坏PCM帧时，不静默吞尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
74. **S5-R2-074｜奇数字节/正常合成PCM**：在坏PCM帧时，不静默吞尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
75. **S5-R2-075｜奇数字节/跨采样率**：在坏PCM帧时，不静默吞尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
76. **S5-R2-076｜奇数字节/分块和空块**：在坏PCM帧时，不静默吞尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
77. **S5-R2-077｜欠载/单样本**：在未完成时耗尽时，一次计数并可恢复；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
78. **S5-R2-078｜欠载/正常合成PCM**：在未完成时耗尽时，一次计数并可恢复；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
79. **S5-R2-079｜欠载/跨采样率**：在未完成时耗尽时，一次计数并可恢复；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
80. **S5-R2-080｜欠载/分块和空块**：在未完成时耗尽时，一次计数并可恢复；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
81. **S5-R2-081｜溢出/单样本**：在cap缩小的合成测试时，dropped显式不是无损；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
82. **S5-R2-082｜溢出/正常合成PCM**：在cap缩小的合成测试时，dropped显式不是无损；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
83. **S5-R2-083｜溢出/跨采样率**：在cap缩小的合成测试时，dropped显式不是无损；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
84. **S5-R2-084｜溢出/分块和空块**：在cap缩小的合成测试时，dropped显式不是无损；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
85. **S5-R2-085｜实际Worklet/单样本**：在真实Chromium合成PCM时，计数消费而非声卡保证；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
86. **S5-R2-086｜实际Worklet/正常合成PCM**：在真实Chromium合成PCM时，计数消费而非声卡保证；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
87. **S5-R2-087｜实际Worklet/跨采样率**：在真实Chromium合成PCM时，计数消费而非声卡保证；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
88. **S5-R2-088｜实际Worklet/分块和空块**：在真实Chromium合成PCM时，计数消费而非声卡保证；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
89. **S5-R2-089｜完整UI接入/单样本**：在完整app候选时，保持正式入口和旧功能；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
90. **S5-R2-090｜完整UI接入/正常合成PCM**：在完整app候选时，保持正式入口和旧功能；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
91. **S5-R2-091｜完整UI接入/跨采样率**：在完整app候选时，保持正式入口和旧功能；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
92. **S5-R2-092｜完整UI接入/分块和空块**：在完整app候选时，保持正式入口和旧功能；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
93. **S5-R2-093｜复制保护/单样本**：在旧浏览器套件时，完整文本字节与录音保护；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
94. **S5-R2-094｜复制保护/正常合成PCM**：在旧浏览器套件时，完整文本字节与录音保护；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
95. **S5-R2-095｜复制保护/跨采样率**：在旧浏览器套件时，完整文本字节与录音保护；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
96. **S5-R2-096｜复制保护/分块和空块**：在旧浏览器套件时，完整文本字节与录音保护；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
97. **S5-R2-097｜封存/单样本**：在独立SHA/双验证时，不改旧失败探针；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
98. **S5-R2-098｜封存/正常合成PCM**：在独立SHA/双验证时，不改旧失败探针；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
99. **S5-R2-099｜封存/跨采样率**：在独立SHA/双验证时，不改旧失败探针；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
100. **S5-R2-100｜封存/分块和空块**：在独立SHA/双验证时，不改旧失败探针；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。

---

## 内嵌备忘录：KAGGLE_STEP18_S5_REVIEW_R3.md

# S5 R3：接入复核100建议

建议不是执行成绩；未执行项目不得签收，不代表真实声学。

1. **S5-R3-001｜完成20ms/Node VM**：在初始buffering时，正pending触发play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
2. **S5-R3-002｜完成20ms/真实Chromium**：在初始buffering时，正pending触发play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
3. **S5-R3-003｜完成20ms/完整UI与旧控制**：在初始buffering时，正pending触发play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
4. **S5-R3-004｜完成20ms/独立封存**：在初始buffering时，正pending触发play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
5. **S5-R3-005｜完成50ms/Node VM**：在正好旧阈值时，不能永久滞留；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
6. **S5-R3-006｜完成50ms/真实Chromium**：在正好旧阈值时，不能永久滞留；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
7. **S5-R3-007｜完成50ms/完整UI与旧控制**：在正好旧阈值时，不能永久滞留；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
8. **S5-R3-008｜完成50ms/独立封存**：在正好旧阈值时，不能永久滞留；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
9. **S5-R3-009｜单样本尾/Node VM**：在1源样本时，按目标率计数消费；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
10. **S5-R3-010｜单样本尾/真实Chromium**：在1源样本时，按目标率计数消费；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
11. **S5-R3-011｜单样本尾/完整UI与旧控制**：在1源样本时，按目标率计数消费；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
12. **S5-R3-012｜单样本尾/独立封存**：在1源样本时，按目标率计数消费；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
13. **S5-R3-013｜恢复短尾/Node VM**：在starved后完成时，恢复而非等大块；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
14. **S5-R3-014｜恢复短尾/真实Chromium**：在starved后完成时，恢复而非等大块；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
15. **S5-R3-015｜恢复短尾/完整UI与旧控制**：在starved后完成时，恢复而非等大块；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
16. **S5-R3-016｜恢复短尾/独立封存**：在starved后完成时，恢复而非等大块；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
17. **S5-R3-017｜实时缓冲/Node VM**：在generationDone=false时，保留原need阈值；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
18. **S5-R3-018｜实时缓冲/真实Chromium**：在generationDone=false时，保留原need阈值；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
19. **S5-R3-019｜实时缓冲/完整UI与旧控制**：在generationDone=false时，保留原need阈值；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
20. **S5-R3-020｜实时缓冲/独立封存**：在generationDone=false时，保留原need阈值；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
21. **S5-R3-021｜已播放/Node VM**：在playing时finish时，不重复play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
22. **S5-R3-022｜已播放/真实Chromium**：在playing时finish时，不重复play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
23. **S5-R3-023｜已播放/完整UI与旧控制**：在playing时finish时，不重复play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
24. **S5-R3-024｜已播放/独立封存**：在playing时finish时，不重复play；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
25. **S5-R3-025｜空流/Node VM**：在0个输入样本时，不合成PCM且等endACK；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
26. **S5-R3-026｜空流/真实Chromium**：在0个输入样本时，不合成PCM且等endACK；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
27. **S5-R3-027｜空流/完整UI与旧控制**：在0个输入样本时，不合成PCM且等endACK；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
28. **S5-R3-028｜空流/独立封存**：在0个输入样本时，不合成PCM且等endACK；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
29. **S5-R3-029｜陈旧零fill/Node VM**：在PCM尚未ack时，不提前ended；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
30. **S5-R3-030｜陈旧零fill/真实Chromium**：在PCM尚未ack时，不提前ended；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
31. **S5-R3-031｜陈旧零fill/完整UI与旧控制**：在PCM尚未ack时，不提前ended；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
32. **S5-R3-032｜陈旧零fill/独立封存**：在PCM尚未ack时，不提前ended；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
33. **S5-R3-033｜消费ACK/Node VM**：在played追上queued时，只在endACK后结束；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
34. **S5-R3-034｜消费ACK/真实Chromium**：在played追上queued时，只在endACK后结束；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
35. **S5-R3-035｜消费ACK/完整UI与旧控制**：在played追上queued时，只在endACK后结束；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
36. **S5-R3-036｜消费ACK/独立封存**：在played追上queued时，只在endACK后结束；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
37. **S5-R3-037｜reset/Node VM**：在stop后旧st时，不复活播放；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
38. **S5-R3-038｜reset/真实Chromium**：在stop后旧st时，不复活播放；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
39. **S5-R3-039｜reset/完整UI与旧控制**：在stop后旧st时，不复活播放；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
40. **S5-R3-040｜reset/独立封存**：在stop后旧st时，不复活播放；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
41. **S5-R3-041｜流epoch/Node VM**：在新begin收到旧流状态时，拒绝跨流污染；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
42. **S5-R3-042｜流epoch/真实Chromium**：在新begin收到旧流状态时，拒绝跨流污染；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
43. **S5-R3-043｜流epoch/完整UI与旧控制**：在新begin收到旧流状态时，拒绝跨流污染；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
44. **S5-R3-044｜流epoch/独立封存**：在新begin收到旧流状态时，拒绝跨流污染；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
45. **S5-R3-045｜晚PCM/Node VM**：在已结束后再到时，明确拒绝或取消后忽略；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
46. **S5-R3-046｜晚PCM/真实Chromium**：在已结束后再到时，明确拒绝或取消后忽略；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
47. **S5-R3-047｜晚PCM/完整UI与旧控制**：在已结束后再到时，明确拒绝或取消后忽略；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
48. **S5-R3-048｜晚PCM/独立封存**：在已结束后再到时，明确拒绝或取消后忽略；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
49. **S5-R3-049｜重复完成/Node VM**：在markDone两次时，不重复补点；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
50. **S5-R3-050｜重复完成/真实Chromium**：在markDone两次时，不重复补点；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
51. **S5-R3-051｜重复完成/完整UI与旧控制**：在markDone两次时，不重复补点；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
52. **S5-R3-052｜重复完成/独立封存**：在markDone两次时，不重复补点；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
53. **S5-R3-053｜重采样长度/Node VM**：在24/44.1/48k时，ceil精确时长政策；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
54. **S5-R3-054｜重采样长度/真实Chromium**：在24/44.1/48k时，ceil精确时长政策；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
55. **S5-R3-055｜重采样长度/完整UI与旧控制**：在24/44.1/48k时，ceil精确时长政策；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
56. **S5-R3-056｜重采样长度/独立封存**：在24/44.1/48k时，ceil精确时长政策；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
57. **S5-R3-057｜插值边界/Node VM**：在分数位置缺右邻时，仅保留一邻样本；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
58. **S5-R3-058｜插值边界/真实Chromium**：在分数位置缺右邻时，仅保留一邻样本；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
59. **S5-R3-059｜插值边界/完整UI与旧控制**：在分数位置缺右邻时，仅保留一邻样本；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
60. **S5-R3-060｜插值边界/独立封存**：在分数位置缺右邻时，仅保留一邻样本；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
61. **S5-R3-061｜端点/Node VM**：在恰好整数采样位置时，不等待无用未来；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
62. **S5-R3-062｜端点/真实Chromium**：在恰好整数采样位置时，不等待无用未来；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
63. **S5-R3-063｜端点/完整UI与旧控制**：在恰好整数采样位置时，不等待无用未来；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
64. **S5-R3-064｜端点/独立封存**：在恰好整数采样位置时，不等待无用未来；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
65. **S5-R3-065｜多块插值/Node VM**：在任意切分时，与整段逐样本一致；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
66. **S5-R3-066｜多块插值/真实Chromium**：在任意切分时，与整段逐样本一致；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
67. **S5-R3-067｜多块插值/完整UI与旧控制**：在任意切分时，与整段逐样本一致；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
68. **S5-R3-068｜多块插值/独立封存**：在任意切分时，与整段逐样本一致；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
69. **S5-R3-069｜取消插值/Node VM**：在保留终端邻样本时，不补尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
70. **S5-R3-070｜取消插值/真实Chromium**：在保留终端邻样本时，不补尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
71. **S5-R3-071｜取消插值/完整UI与旧控制**：在保留终端邻样本时，不补尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
72. **S5-R3-072｜取消插值/独立封存**：在保留终端邻样本时，不补尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
73. **S5-R3-073｜奇数字节/Node VM**：在坏PCM帧时，不静默吞尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
74. **S5-R3-074｜奇数字节/真实Chromium**：在坏PCM帧时，不静默吞尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
75. **S5-R3-075｜奇数字节/完整UI与旧控制**：在坏PCM帧时，不静默吞尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
76. **S5-R3-076｜奇数字节/独立封存**：在坏PCM帧时，不静默吞尾；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
77. **S5-R3-077｜欠载/Node VM**：在未完成时耗尽时，一次计数并可恢复；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
78. **S5-R3-078｜欠载/真实Chromium**：在未完成时耗尽时，一次计数并可恢复；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
79. **S5-R3-079｜欠载/完整UI与旧控制**：在未完成时耗尽时，一次计数并可恢复；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
80. **S5-R3-080｜欠载/独立封存**：在未完成时耗尽时，一次计数并可恢复；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
81. **S5-R3-081｜溢出/Node VM**：在cap缩小的合成测试时，dropped显式不是无损；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
82. **S5-R3-082｜溢出/真实Chromium**：在cap缩小的合成测试时，dropped显式不是无损；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
83. **S5-R3-083｜溢出/完整UI与旧控制**：在cap缩小的合成测试时，dropped显式不是无损；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
84. **S5-R3-084｜溢出/独立封存**：在cap缩小的合成测试时，dropped显式不是无损；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
85. **S5-R3-085｜实际Worklet/Node VM**：在真实Chromium合成PCM时，计数消费而非声卡保证；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
86. **S5-R3-086｜实际Worklet/真实Chromium**：在真实Chromium合成PCM时，计数消费而非声卡保证；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
87. **S5-R3-087｜实际Worklet/完整UI与旧控制**：在真实Chromium合成PCM时，计数消费而非声卡保证；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
88. **S5-R3-088｜实际Worklet/独立封存**：在真实Chromium合成PCM时，计数消费而非声卡保证；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
89. **S5-R3-089｜完整UI接入/Node VM**：在完整app候选时，保持正式入口和旧功能；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
90. **S5-R3-090｜完整UI接入/真实Chromium**：在完整app候选时，保持正式入口和旧功能；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
91. **S5-R3-091｜完整UI接入/完整UI与旧控制**：在完整app候选时，保持正式入口和旧功能；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
92. **S5-R3-092｜完整UI接入/独立封存**：在完整app候选时，保持正式入口和旧功能；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
93. **S5-R3-093｜复制保护/Node VM**：在旧浏览器套件时，完整文本字节与录音保护；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
94. **S5-R3-094｜复制保护/真实Chromium**：在旧浏览器套件时，完整文本字节与录音保护；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
95. **S5-R3-095｜复制保护/完整UI与旧控制**：在旧浏览器套件时，完整文本字节与录音保护；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
96. **S5-R3-096｜复制保护/独立封存**：在旧浏览器套件时，完整文本字节与录音保护；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
97. **S5-R3-097｜封存/Node VM**：在独立SHA/双验证时，不改旧失败探针；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
98. **S5-R3-098｜封存/真实Chromium**：在独立SHA/双验证时，不改旧失败探针；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
99. **S5-R3-099｜封存/完整UI与旧控制**：在独立SHA/双验证时，不改旧失败探针；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。
100. **S5-R3-100｜封存/独立封存**：在独立SHA/双验证时，不改旧失败探针；记录队列、命令、消费、epoch或长度的该路径证据，未执行不得用邻近路径替代。

---

## 内嵌备忘录：KAGGLE_STEP18_S5_PLAYBACK.md

# S5：播放器完成短尾排空、重采样终点与流隔离实际修复

**限定工程修复已实现；整体 PARTIAL/BLOCKED，18 未发布、未部署。不能保证整个产品一定成功或声音已经无沙沙。**

## 实际修改与完整接入

新增完整 `kaggle/step18/web/app.js`，从冻结17 app派生，只修改Player P及嵌入Worklet V。网络帧解析器、到达预测器、整个UI后缀逐字节不变；新Player由完整页面原路径实际实例化，不是测试内helper。S3/S4候选、冻结17及正式工作台不动，默认前端/包未切换。

1. **完成短尾**：生成已结束且pending>0即可play，包含初始20/50ms、一输入样本及starved恢复；未结束仍使用原风险缓冲阈值，不盲降启动预算。
2. **不假装排空**：记录已post目标样本总数，以queued−played−dropped计算pending，不因陈旧fill0提前结束。需当前流endACK且pending=0才ended；消费与明确丢弃分列，不能把溢出叫无损。
3. **重采样收尾**：全局整数输出坐标、精确端点立即输出、分数端点只等一个邻样本；正常结束用末样本保持，输出长度ceil(Nin*contextRate/24000)，取消不补点。测试覆盖24k/44.1k/48k，不宣称任意采样率抗混叠高保真。
4. **取消／换流隔离**：内部epoch覆盖控制与状态，stop后迟到消息不复活，新begin拒绝旧状态；取消不排旧尾或旧插值端点。不改网络协议。
5. **错误与指标边界**：奇数PCM字节拒绝，重复markDone不重复补点；firstPlayedMs仍为发送play命令时间，未冒Worklet或扬声器实际首声。新status列出queued/pending/dropped/epoch/endACK，未完成S6全链时序设计。

末样本保持不会追加参考PCM，不添加worker speech样本或改变其RTF分母。极短1样本虽会被Worklet计数消费，也可能被既有淡入归零，**不是可听人声**；不能把单样本消费证明冒自然朗读或可用首声验收。

## 最终三轮证据

| 项目 | 每轮结果 | 范围 |
|---|---:|---|
| 完整CPU组合 | **610 PASS ×3＝1830 PASS** | 450冻结控制＋152旧候选＋8新源码/实际VM集成 |
| CPU失败／错误／跳过 | **0／0／0** | 旧602逐ID和结果完整继承 |
| 专项Node VM | **37 PASS ×3** | 真实Player与Worklet串接；时钟、port及processor基类明确替身 |
| 同套冻结红对照 | **37中28失败、9保留通过** | 不是28独立bug；旧短尾/端点/取消等合同失败，未改旧probe |
| 完整Chromium | **173 PASS ×3＝519 PASS** | 原158＋新15；0失败/flaky/skip/retry |
| 新原生浏览器测试 | **15/轮** | 9种真实Worklet消费＋3种空/取消/换流＋3种完整UI原生链 |
| 完整候选UI链 | **3/轮** | 合成HTTP PCM/参考状态，真实浏览器AudioContext/Worklet；不是Go/模型 |
| 继承环回TCP | 237/轮，共711 | 旧S1/S2端点；S5没有新增实际后端TCP请求，浏览器HTTP数据明确fixture |
| 审计／Node服务／AST | **24／30／58 ×3** | 另JS语法、候选/测试语法和repack --check |

CPU的第8新合同内部也会执行37项Node VM；专项37三轮另存收据，**不把重叠运行相加当独立功能数量**。旧158浏览器保护仍针对冻结脚本/正式工作台，含完整包文本复制与录音/权限/取消保护；新15才验证S5候选，不能把173全部说成新候选全功能。

### 原生消费具体检查

- 24k上下文：1／480／1200源样本分别消费1／480／1200；44.1k及48k按ceil目标预算消费。
- 每项核对queued=played、pending=0、dropped=0、当前epoch endACK和最终ended，不止断言发送了play。
- 完整候选页面从原speak入口、帧解析、完成标记到真实Worklet消费1／480／1200源样本，并显示播放完毕。
- 未完成20ms仍buffering；欠载恢复只计原一次underrun；已playing不重复play；旧epoch状态/PCM被拒绝。
- 小cap合成overflow场景明确记录8消费/12丢弃，不把“队列终止”冒全部收到样本无损。

真实Chromium采用原配置headless、mute-audio，原生AudioWorklet确实执行，但没有实体扬声器/耳机声压、DAC时延或盲听证据。记录消费不等于正确语音、可听首声或用户沙沙根因。

## 流程、环境与封存

Q32先按四选项选C并列50行动，三遍专题各100建议归档；不是300修复/验收。首轮37VM、8源码、15原生浏览器预检均通过；旧红37中28失败，同套保留9保护通过。最终源码和测试在三轮CPU/浏览器启动后未改。

Python venv沿用，无新Python依赖，freeze与S4字节相同。node_modules原不存在，本步确实执行npm ci --ignore-scripts，按原lock安装；package.json/lock和既有Playwright配置不改。具体版本与安装日志见s5-environment.json/s5-npm-install.txt，不冒“无安装”。无Rust/Go/Torch/Qwen/权重/训练/T4执行。

历史保护2049路径，2046匹配，3份旧日志缺失仍保留，不补造；完整历史完整性false。S4可变文档/交接及冻结app改前归档，原53资产/94冻结/15正式不动。8条原建议有具体VM测试名、三轮收据SHA限定链接；原300最终/功能签收仍0，不用覆盖率冒整体进度。

独立verify_s5核验旧602继承、VM红绿、三轮原生浏览器及附件消费数据、原完整UI后缀、冻结保护和完整交接。两次核验以stdout为准，进度见progress-s5.json；完整交接111份。浏览器完整回归单轮需数分钟，按原进程顺序完成，不因等待超时重启/重跑或覆盖日志。

## 仍未签收／下一步

真实用户音频、自然朗读、同声/无沙沙、可听首声<3秒、双T4、长录音真实训练、模型RTF≤0.3、完整鉴权网络/候选包发布均未验收。S3 Rust等效仍阻塞；S4领先低电平可能裁掉的限制未消失。播放队列上限、设备挂起/后台调度及抗混叠等仍需真实条件验证，不承诺普遍零漏音或永久Kaggle可用。

下一步按计划进入 **S6时序与诊断**：区分排队/模型首块/首PCM/play命令/Worklet消费/实体可听时间，保留旧字段含义，不把旧firstPlayedMs当实际出声。Q33未开，不预填；直接继续无需Continue。
