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
