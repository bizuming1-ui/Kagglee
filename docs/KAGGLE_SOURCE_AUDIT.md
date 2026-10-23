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
