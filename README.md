# Kagglee Studio

一个可粘贴、编辑和运行 **HTML / CSS / JavaScript** 的浏览器工作台。点击“保存到项目”会通过 Node.js 服务端写入仓库内的真实源码文件，**不是 localStorage / IndexedDB 保存**。

## 运行

需要 Node.js 22+。生产运行无第三方运行时依赖。

```bash
npm ci
npm start
# 访问 http://localhost:3000
```

服务监听 `0.0.0.0`，支持 Arena 同源反向代理预览。浏览器只请求相对 API 路径，不连接浏览器自己的 localhost。

可配置：

```bash
PORT=3000 WORKSPACE_DIR=/absolute/path/to/workspace npm start
```

## 使用

1. 点击顶部工具栏 **“＋ 新建文件”**，自行输入文件名（例如 `我的内容.txt`、`我的页面.html`），创建后内容为空，由你自行粘贴。也可继续编辑预设的三个文件。
2. 点击 **运行**（Ctrl/Cmd + Enter）刷新沙箱预览。运行不代表保存。
3. 点击 **保存到项目**（Ctrl/Cmd + S），保存所有文件，包括你新建的自命名文件。只有服务端写入成功后才显示“已保存到项目”。
   自命名文件可点击 **“重命名”** 修改名称，内容保持不变，需再次保存才会写入磁盘。三个预设文件是原有预览的基础，保留其名称。
4. 刷新页面或重启服务，从磁盘恢复最近保存的版本。
5. 顶部 **“复制当前代码”** 原样复制所选文件的当前内容（包括未保存更改）。浏览器拒绝剪贴板权限时提供选中原文的手动复制窗口。复制不等于保存，也不代表代码经过Kaggle运行验证。Python代码应在Kaggle等实际Python环境运行。
6. 底栏的 `workspace/` 可查看当前真实路径。“备份代码”下载当前编辑内容的 JSON，包括未保存更改，不替代保存。
7. 多窗口冲突时，先备份编辑内容，再选择“从磁盘重载”。不自动覆盖其他窗口的保存。

支持完整 HTML 文档，也支持 HTML 片段。选中自命名的 `.html` / `.htm` 文件后点击运行，可预览你自己的页面，默认不注入示例样式和脚本；仅在页面明确引用 `style.css` / `script.js` 时使用这两个伴随文件。其他自命名文本文件仅提供编辑保存，不增加后端代码执行能力。原有 `index.html` 预览继续自动注入 CSS、JavaScript；HTML 中指向 `style.css` / `script.js` 的本地引用（含 `./`、`/` 前缀及查询参数）由编辑区对应文件统一提供，避免加载工作台资源或重复执行。直接用其他工具打开保存的 HTML 片段时，需要自行补充完整文档及 CSS/JS 引用。

其他功能：文件修改标记、行号、Tab/Shift+Tab 缩进、光标位置、日志筛选和清空、异常与 Promise 拒绝捕获、200条日志上限、375px/768px/自适应预览、手机响应式界面、离开未保存页面提醒、需确认的示例恢复。

## 真实保存结构

```text
workspace/
├── HEAD.json                    # 当前版本号及保存时间
└── revisions/
    └── <服务端生成的 UUID>/
        ├── index.html           # 用户原始 HTML
        ├── style.css            # 用户原始 CSS
        ├── script.js            # 用户原始 JavaScript
        └── 我的内容.txt          # 自命名文件，名称与内容由你决定
```

每次保存所有文件组成一个完整快照，完成写入后原子替换 HEAD。历史版本不会被覆盖。失败时不更新当前指针；非法或损坏的存储不会被静默重建。

- 保留三个预设文件，可添加自命名文件；最多32个文件，总 UTF-8 内容上限 1 MiB。文件名最多100字符/240字节，允许中文、字母、数字、空格、下划线、短横线、圆括号与扩展名，拒绝路径、系统保留名和不区分大小写的重名。
- 新建、重命名和粘贴不会自动写盘；保存按钮统一落盘。恢复示例只重置三个预设文件，不会清空自命名文件。
- 版本号冲突返回 HTTP 409；同一服务进程中的写入串行处理。
- **同一工作区只运行一个服务进程**，不提供跨进程/分布式文件锁。
- 请勿在服务运行时直接修改 HEAD 或快照；外部改动不在版本冲突检测范围内。
- 原子替换保证正常进程运行中的版本一致性；没有承诺断电级 fsync 持久化或文件系统损坏恢复。
- 历史版本保留，不自动清理；长期使用应自行备份并在停止服务后清理非当前版本。
- 保存到磁盘不等于自动 git commit / push。源码不被 `.gitignore` 排除，但测试文件和浏览器二进制不会进入 Git。

## 安全边界

**本地、单用户开发工具，不是完整浏览器或恶意代码执行平台。**

- iframe 只启用 `allow-scripts`，不启用同源、表单、弹窗、下载或顶层导航权限。控制台通过独立 MessageChannel 传输，日志作为纯文本显示。
- 服务端拒绝跨站及 `Origin: null` 写入；API 不启用 CORS；静态资源严格白名单；不提供任意路径读写或服务端代码执行。
- CSP 限制资源及连接来源；为 srcdoc 中的用户脚本和样式保留 inline 支持，因此不将 CSP 当作主页面完整 XSS 防护。API 数据不使用 innerHTML。
- 不支持 Python/C++/Rust 等服务端语言、npm 模块导入、多文件构建或任意外部网络资源。默认网络资源策略也可能限制用户代码中的图片、字体或外链。
- 沙箱不隔离 CPU/内存消耗，死循环及日志洪泛仍可能卡住浏览器；只运行可信代码。资源加载错误、语法错误等按浏览器提供的信息输出，部分跨域异常只有通用提示。
- **没有应用级用户认证，不应直接暴露到公网。** 对远程访问必须使用可信环境的访问控制或带认证的反向代理。只检查 Origin 无法替代身份认证或防范 DNS rebinding。
- 未保存的内容不做后台缓存，关闭页面可能丢失；请保存或下载备份。JSON 备份可手动提取三个文件，目前不提供导入按钮。

## 验证

```bash
npm run check      # JavaScript 语法检查
npm test           # Node HTTP/API/文件系统测试
npm run test:e2e    # 三轮 Playwright Chromium 浏览器模拟 + 最终补充
npm run test:e2e -- --repeat-each=3  # 整套浏览器用例重复3遍
npm audit --audit-level=high
```

API 测试使用临时目录和随机端口；浏览器测试使用临时工作区及独立 3100 端口，**不会修改正式 workspace/**。E2E 测试通过 npm 提供的 `@sparticuz/chromium` 获取 Linux x64 浏览器，附带的 NSS 库解压在 `node_modules/.cache`。不需要访问 Playwright CDN。系统需要 Linux x64、`tar` 和 Chromium 的常规基础库；其他平台需要调整 `playwright.config.js` 的浏览器配置。测试只在启动参数中关闭系统沙箱（容器所需），不关闭 Web Security 或站点隔离。此依赖仅用于开发测试。

实现与审查记录见 [docs/AUDIT.md](docs/AUDIT.md)。中文字体来自 Noto Sans SC，随项目本地提供，无外部字体请求；许可证见 `public/fonts/OFL.txt`。

## Kaggle语音系统需求备忘录

现已收到原始 `kaggle`，22项压缩资产校验通过，可读源码在 `kaggle/source/`。

- 最新：[第十七阶段长参考修复包](kaggle/kaggle-fixed-step17.py)：长ASR段词级切分／实际窗口重识别，16/24秒参考窗口、生成参数指纹及较长朗读聚合。**真实相似度、零噪声、双卡声学完全一致、自然度与T4 RTF0.3仍待实机验收，整体PARTIAL/BLOCKED。** [方案](docs/KAGGLE_STEP17_PLAN.md)／[升级操作](docs/KAGGLE_STEP17_QUICKSTART.md)／[审计](docs/KAGGLE_STEP17_AUDIT.md)。
- 历史16：[第十六阶段部分修复包](kaggle/kaggle-fixed-step16.py)：匹配转写ICL＋仅生成码解码、参考内容/模式绑定、提示快照、有界codec窗口与每任务6dB最大增益。**真实音色相似、单一声音、无沙沙与T4 RTF≤0.3尚未验收，整体PARTIAL/BLOCKED。** 见[完整方案](docs/KAGGLE_STEP16_PLAN.md)、[升级与真实基准](docs/KAGGLE_STEP16_QUICKSTART.md)、[审计](docs/KAGGLE_STEP16_AUDIT.md)。
- 历史15：[第十五阶段部分修复包](kaggle/kaggle-fixed-step15.py)：仅说话人向量生成、禁用参考片段拼接、首句及时提交、限幅增响、创建默认延后额外GPU校准/CPU ASR复用。**向量模式可能改变韵律相似度；真实T4试听、首播与创建提速仍未验收。网页训练闭环和声学逐字拒播仍缺，整体PARTIAL/BLOCKED。** 见[方案](docs/KAGGLE_STEP15_PLAN.md)、[升级操作](docs/KAGGLE_STEP15_QUICKSTART.md)、[审查](docs/KAGGLE_STEP15_AUDIT.md)。
- 历史：[第十四阶段部分修复包](kaggle/kaggle-fixed-step14.py)冻结保留，长录音/等价训练缓存证据见STEP14_AUDIT。
- 当前审查：[第十阶段证据与操作说明](docs/KAGGLE_STEP10_AUDIT.md)，Python227×3、Go竞态×3、API30×3、真实输入HTTP与本机CLI/fixture及双CPU Mock各三轮通过；浏览器110唯一×3＝330 PASS（10.4分钟），完整复制另3 PASS，三轮用例通过不等于300清单全验收，中止/复审记录保留。真实设备下一步见[目标验收门禁](docs/KAGGLE_TARGET_ACCEPTANCE.md)，不把CPU/软件音频流当作GPU/物理麦克风验收。
- 冻结保留：[首轮包](kaggle/kaggle-fixed-step1.py)、[第二阶段包](kaggle/kaggle-fixed-step2.py)、[第三阶段包](kaggle/kaggle-fixed-step3.py)、[第四阶段包](kaggle/kaggle-fixed-step4.py)、[第五阶段包](kaggle/kaggle-fixed-step5.py)、[第六阶段包](kaggle/kaggle-fixed-step6.py)、[第七阶段包](kaggle/kaggle-fixed-step7.py)、[第八阶段包](kaggle/kaggle-fixed-step8.py)、[第九阶段包](kaggle/kaggle-fixed-step9.py)、[第十阶段包](kaggle/kaggle-fixed-step10.py)、[第十一阶段包](kaggle/kaggle-fixed-step11.py)、[第十二阶段包](kaggle/kaggle-fixed-step12.py)、[第十三阶段包](kaggle/kaggle-fixed-step13.py)与[历史首轮审查](docs/KAGGLE_SOURCE_AUDIT.md)。原始kaggle未覆盖；`repack.py --check`当前检查step17。
- 访问口令与DeepSeek Key分离，仅当前网页内存使用；默认自动口令放在/tmp私有目录，不在声音库导出中。应通过可信HTTPS代理访问。
- **实验性训练代码已实现，但没有运行真实Qwen训练，也未经双T4/音质/性能验收；不是多租户安全平台，GPU依赖、OS级隔离和真实解码器兼容仍待完善。**

完整方案、边界、15×50专业建议及三轮300项清单汇总在 [KAGGLE_HANDOFF_PROMPT.md](docs/KAGGLE_HANDOFF_PROMPT.md)；当前仅22项清单有据勾选，不能当作300项验收完成。上述Kaggle网关与本地Node代码工作台是两个不同运行单元；工作台本身仍遵守前面的本地单用户安全边界。

第五至十阶段均为独立文件交付：正式工作台15文件1043155字节，距1MiB只余5421字节，不强塞新包、不提高限制或删除旧文件。原始库仅在本次工作目录保存，未自动加入Dataset；处理后档案的锚点/转写仍沿用既有备份设置。

第六阶段训练输入格式门禁：仅完整24kHz单声道PCM16 WAV，逐条转写，统一参考≤16秒。浏览器默认Opus等格式会被明确拒绝，既有参考处理不受此限制。训练输入副本不自动云备份，删除原库后仍需单独删除副本；没有真正训练或GPU资源切换。

第七阶段离线CLI：仅本机CPU/FP32/eager、本地物化JSON/safetensors模型、固定模型目录hash；不提供GPU/HTTP编码或自动下载。测试码强制test_only_codes，不冒充真实Qwen编码；真实执行和解码/训练验收分开。操作见第七阶段报告。

第八阶段资源预约：`tools/resource_control.py status` / `reserve --seconds 5`仅观察或预约合作式整组锁，不测显存、不运行训练。升级前先停所有旧GPU服务；bootstrap不再按旧PID/pkill自动杀进程，busy/遗留PID标记会明确阻断。多真实模型进程由supervisor统一持锁启动，父死但孩子仍持锁时不能强制解锁。详情见第八阶段报告。


第九阶段来源/读取检查：新schema2原样保存source/manifest.json与source/train_raw.jsonl，包括原库/修订/样本/声明，不代表权利鉴定；列表只描述封存政策，全核验才声明provenance_verified_now。schema1继续可读核验/删除且不改旧hash。`tools/encode_training.py hold-read --state "$QTTS_STATE" --id "$CODES_ID" --manifest-sha256 "$CODES_SHA256" --seconds 5 --timeout 15`仅保持约定只读租约，同版本删除/第二读取409；不调用训练器，training_allowed=false。变量必须取实际list/verify结果，不填虚构ID。未自动接入DDP多rank生命周期或Dataset备份。


第十阶段现在可开发/尝试训练，不再等待额外基础设施。目标环境就绪即可执行`tools/train_tts.py train`；[Kaggle开训步骤与可取消Notebook代码](docs/KAGGLE_TRAINING_QUICKSTART.md)说明真实输入、模型固定hash、显式审阅及失败处理。输出是adapter候选而非完整CustomVoice，尚未自动接入现有语音聊天、恢复训练状态或完成真实Qwen重载试听；不能把核心代码实现与产品验收混为一谈。

第十一阶段保留实验性训练核心，新增固定run/manifest/Base/码绑定、事务式LoRA切换与保存speaker prompt。现有两主视图/普通档案/命名库/录音/访问控制/DeepSeek协议及源码复制保留；训练候选固定参考，不自动active或伪造音质验收。CPU三轮回归与本机Go/SSE/双worker接口替身证据不等于真实Qwen或DeepSeek联网验收。10题500建议，22/300仍为完整目标验收统计。

第十七阶段的浏览器复制预览使用`node tools/kaggle-copy-server.mjs`（默认3001），与正式3000工作台隔离；页面只展示固定hash的step17整包并支持原样复制/下载，不执行Python。目标双卡实际识别见用户日志，模型修复后的重载/听音待复跑。
