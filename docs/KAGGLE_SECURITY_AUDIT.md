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
