# 启动已ready但Notebook显示SystemExit:0：精准返回码修正

## 本次远端日志意味着什么

用户提供的Kaggle日志显示两块不同物理T4、Python3.12.13、Torch2.10.0+cu128；依赖安装和runtime_surface预检通过，模型下载/缓存、真实Go网关编译完成，supervisor启动，wait_ready通过后打印约195秒ready并建立隧道。

这是**用户提供的真实双T4启动进展证据**，不能再说真实启动完全没尝试。尚未收到启动后两worker的直接health响应、实际生成音频/性能测量或训练收据，不能把ready推成训练/音质/首声/RTF已签收。日志含公开访问链接与私有token文件位置，本报告不复制其链接/UUID/token路径。

最后SystemExit:0是bootstrap的 `sys.exit(main())` 成功返回被runpy.run_path原样抛到IPython；它不是启动失败。旧入口在CPU显式替身中精确复现了成功退出仍抛异常，见original-red.json。替身没有执行真实bootstrap、Secrets、模型或启动服务。

**不要为了这个提示重跑--run。当前已ready的服务无需重启。** HF匿名下载警告没有阻止本次下载；Rust不构建是候选因果NumPy设计，不是此次错误。qwen-tts未安装在日志中是非必需warning，当前使用qwen-tts-hf，不应为此盲装冲突namespace或更换平台Torch。

## 独立新修正版

`kaggle/delivery18/artifacts-startup-return-fix/`：

| 文件 | 字节 | SHA256 |
|---|---:|---|
| kaggle-step18-candidate.py | 287168 | `d701f79cda10c7673c09ba0b70204021599057fee36abed8253793d56cff871c` |
| kaggle-step18-full-source.zip | 433606 | `985dba2fc85492c3ddce32ecb47800392ef8e2cd8e9f96d54c66923032f7457e` |

新增_run_bootstrap，只有SystemExit被规范化：None/0为返回0；整数非零保留，布尔按Python标准语义False→0/True→1，字符串（包括字符串"0"）为失败1，不回显任意私有字符串。正常函数返回也为0。KeyboardInterrupt/RuntimeError等不被该helper吞掉。

main仅把原runpy调用替换为返回helper结果；保留上一版Colab/Jupyter连接参数修复、严格CLI、双T4门禁、解包安全。原所有其他命名函数AST保持，58运行源码资产与ZIP source/*逐字节不变，仍61个ZIP成员。未修改已运行Kaggle机器或服务，也没有远程执行停止/启动命令。旧两份交付原样保留。

## 验证与边界

- 新24个返回/集成/包保护合同＋继承30个Notebook/CLI/IPython合同，**54×3**均通过。继承原36中与新wrapper有关的30项，排除旧版包/特定AST断言，由本批包一致性与AST断言替代；不是暗改旧测试。
- 本地真实IPython中main成功后实际执行下一条语句、不再SystemExit警告；失败仍返回3。独立Python子进程成功退出0/失败退出3，避免只验证函数返回。
- 取消/意外异常保持可见，成功路径不会发kill；bootstrap/硬件/Secrets是明确CPU替身，不冒称实机重跑或验证全部取消清理。
- 三轮真实本地Chromium：全文287168B、原生剪贴板、实际下载均同SHA；权限拒绝时全选范围完整。
- 双旧seal再次只读通过：上版28项与原54项交付范围不改，原3071保护仍通过。原610CPU/Go40/173浏览器等本批没有整套重跑，运行资产未改而保留旧证据，不拼接为本轮成绩。
- 新增health_readonly.py仅GET两个既有loopback worker，禁用代理/重定向，限定响应预算，不读token、不启动或安装、不写状态。健康聚合的正向测试是明确合成HTTP响应，不是远端模型证据。
- 仅本次返回处理已修；没有证明全部运行异常、持久化、Kaggle恢复或真实声学已解决。本地Python3.11/IPython9.17测试，不冒称新wrapper已在用户远端3.12运行。

Q44选B＋50，三审各100复核建议存同名Q44文档和startup-return-fix/reviews.json；为修正后复核，不是300修复。十上下文×十维度分别绑定SystemExit/异常测试01–09、main/CLI/IPython测试10–16、包保护17–23、健康24及三轮浏览器。旧源码不覆盖，失败码不吞。

## 当前用户只做只读检查

已有服务不要重启。直接在当前Notebook新单元格请求 `http://127.0.0.1:7001/health` 和7002对应路径，仅输出ready/engine/model_loaded/dtype/rt字段，不输出完整profiles或token。期望两个worker均ready=true、engine=faster-qwen3-tts、model_loaded=true，才补足“两worker报告真实模型已加载”的响应证据。它仍不是实际生成/训练/音质/速度证明。

新输出框在本地预览8082，只替换代码复制预览服务，不是停止用户Kaggle服务。已启动用户可继续现有会话，不需要为清除历史输出中的SystemExit:0重装或重启；新完整单文件用于以后启动。下次调用main([...])成功会正常返回0，非零必须保留为失败。

## 继续交接提示词

当前基础仍是可核验S5接线包，缺失S6–S8C未恢复。已收到用户双T4真实启动ready日志，下一步先收集直接health及实际生成证据，不再笼统说实机启动从未执行。新wrapper版本为d701f79c…，原58运行源码不变，保留Colab参数修复。禁止重新--run干扰现有服务。独立封存见docs/validation/step18/startup-return-fix；整体PARTIAL/BLOCKED，原300最终0，不能保证声音或性能一定成功。
