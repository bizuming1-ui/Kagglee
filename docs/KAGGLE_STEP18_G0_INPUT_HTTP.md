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
