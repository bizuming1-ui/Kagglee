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
