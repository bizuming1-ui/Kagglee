# 第十三阶段审查：真实导入生命周期修复

## 结论与责任边界

step12在用户Kaggle两T4上仍失败，不能称已修好。原因不是用户没按步骤，而是我们上一版补丁只查sys.modules，没有覆盖Faster实际延迟导入。此前wheel函数数学通过只说明桥接算法有效，无法证明生产入口安装了补丁。此缺口已明确纳入本阶段回归。

## 实际来源与复现

- 受审真实faster0.5.4 wheel顶层导入model/ggml包装类；model.py第194行在from_pretrained内部才from qwen_tts import Qwen3TTSModel。
- 真实HF0.1.1.post1父包导入时注册旧default RoPE。TF5.20.2 _init_weights的ROPE_INIT_FUNCTIONS会覆盖Mimi自带现代默认计算器，导致读取旧rope_theta。
- 来源哈希/导入行见reviewed-import-sources.json。CPU隔离环境正常导入完整Faster，确认Qwen尚未载入；执行冻结step12实际兼容源，返回not_applicable；再正常导入完整Qwen并构造真实微型Mimi，复现与用户一致AttributeError。见real-import-baseline.json，不伪造第三方导入。

## 实施

1. install_qwen_rope_bridge以发行元数据判别HF/legacy，HF先检查版本/命名空间冲突，再显式正常importlib.import_module加载实际compat（及其父包），随后验证并桥接注册函数。未知组合/导入异常/元数据矛盾拒绝；legacy仍无须HF。
2. 保留窄范围bridge和实际theta临时副本，不改配置/权重，不猜默认值，不盲降TF4，不变更平台Torch/CUDA约束。
3. qwen_configuration_check要求installed且数学smoke明确True；HF存在却跳过或不完整时blocked/required=True。只有真正未安装HF的legacy路径可不适用。
4. Worker/native adapter/CPU编码/训练仍在构造前共用同一桥接；驻留、fatal nonce及所属进程清理保持。不增加导入钩子，不绕过验证来消除报错。
5. 新增6项回归：尚未导入时HF显式导入；导入失败；版本/冲突先行拒绝；已载HF缺发行元数据；HF skipped/incomplete smoke阻断；官方legacy保持可选。旧GPU/API/CPU编码替身测试明确模拟其兼容边界，不能伪造全局发行元数据后误称真实包通过。

## 更强的真实CPU验证（不是完整1.7B模型验收）

lazy_rope_import_check.py不替换第三方导入、不下载模型，禁网且HF离线；从真实Faster未载Qwen状态调用生产安装函数，再正常导入完整Qwen，实际TF MimiModel构造2651参数微型随机模型、本地保存后from_pretrained重载。10000/12345/1000000三theta均校验实际rotary缓冲、配置不变、参数finite；实际初始化进入桥接12次。完整Qwen包导入不等于完整Qwen模型构造/加载。这里GPU执行为False、完整Qwen模型加载为False。

额外正常运行真实backend_probe隔离CLI三轮：HF数学smoke均required=True且pass；沙箱无CUDA，整体报告blocked（符合预期），未把该报告当作目标GPU预检通过。见real-preflight-cpu-round1..3.json。

主venv未装这些第三方包；隔离依赖置/home/user/.cache/qtts-step13-site与既有step12-site，不入Git。SoX二进制缺失有警告，本实验未调用其音频功能，不假称通过SoX音频转换。

## 验证状态

最终三轮：Python273×3=819 PASS，Node30×3=90 PASS，Go race count3 PASS；资源所有权真实进程/HTTP训练输入/本地码CLI/Mock管线四脚本各执行3次（每次内置3轮，共各9轮）、adapter真实Go+SSE+双worker CPU小LoRA替身三轮、fatal真实supervisor+CPU worker三轮PASS。

完整浏览器114×3=342 PASS（11.4分钟），另最终step13整包逐字节复制三轮PASS。3001独立复制页真实Chromium三轮剪贴板/下载完整哈希一致、授权拒绝全选、375px手机无横向溢出、正式15文件不变，见copy-page.json。不是用HTTP读取代码冒充剪贴板验收。

最终交付门禁见docs/validation/step13/final-checks.json；三轮各100项不重复定向开发建议与保留目标ID见review-map.json，完整目标仍22/300；12题600建议不等于600修复。

## 初始失败保留

- 新完整包隔离环境首次缺scipy、随后缺cloudpickle等依赖；仅补隔离验证依赖，未修改主venv/生产版本组合。日志real-import-initial.txt/attempt2/依赖日志留存。
- 微型Mimi首次测试断言误以为TF5旋转模块有rope_init_fn字段；实际是默认静态方法+_init_weights registry。修正验证为实际inv_freq/original_inv_freq和函数profile计数，保留real-import-initial-modelassert.txt；不是以不核对频率的方式忽略错误。
- 完整273测试初轮1错误：CPU编码器旧替身把所有发行元数据伪造成stub-only，触发真实namespace冲突。测试明确隔离模拟legacy兼容路径；生产版本/冲突拒绝未削弱。初始日志python-initial.txt保留。

## 下一现场门禁

发布完整step13、只读复制页，旧原始至12冻结。先备份需要的私有数据，再停止并重启完整Kaggle会话，T4×2/Internet/非Mock默认faster，预检必须通过qwen_mimi_rope_cpu，然后看两worker实际完成加载/预热，再短句试听。当前没有真实T4/完整权重，不能保证下一次必成、显存fit、性能、音质或永久Kaggle；有新异常需按实际链路继续修复，不能报成功掩盖。

## 当前交付完整性

step13：282346字节/47资产，SHA256 dad142d75be94d8efb6567fc1f8755d3f37341a65d5c7fe9454fd36c87770e60；source_manifest逐项校验和repack --check可重现。原始至12包冻结，正式3000工作台HEAD/15文件1043155B不变，33备忘录完整内嵌。
