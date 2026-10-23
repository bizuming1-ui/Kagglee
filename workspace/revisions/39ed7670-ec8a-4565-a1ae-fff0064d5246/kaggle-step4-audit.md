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
