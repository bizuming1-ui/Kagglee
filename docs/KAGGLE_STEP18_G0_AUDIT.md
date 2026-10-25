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
