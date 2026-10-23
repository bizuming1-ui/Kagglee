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
