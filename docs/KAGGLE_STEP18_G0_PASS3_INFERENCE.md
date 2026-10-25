# G0 全源第三遍第4批：adapter、推理与生成资源清理

日期：2026-10-23；分支 `arena/1160bd87-kagglee`。

**第三遍累计27/53份、6667行，剩26份7001行。前两遍各53/53份、13668行保持。产品未改，G0仍PARTIAL/BLOCKED。** 全文阅读齐全与问题已修/功能已验不是同一状态，53资产也不等于整个Git仓库。

## 1. 新增7份完整复读：1302行

| 文件（相对 kaggle/source/） | 行数 | 重点 |
|---|---:|---|
| py/adapter_engine.py | 108 | 本地Base固定、磁盘trained绑定、cached选择仍检查产物、原子模块切换、整句输出及取消 |
| py/lora_adapter.py | 91 | 冻结Base/FP32 A-B、全部替换前校验、commit回滚与张量设备；仅源码语义 |
| py/qwen_compat.py | 97 | provider分布元数据/命名空间冲突、RoPE schema/代理/注册表与失败重试 |
| py/clone_stream.py | 126 | generated-only条件与解码分离、有限窗口、pending与close/取消 |
| py/gpu_ownership.py | 151 | 固定同UID命名空间、FD类型/nonce/OFD、短写失败释放、观察状态非授权 |
| py/worker.py | 680 | boot/profile事务、pin/缓存/锁、生成/DSP/指标、HTTP和断连/排空 |
| tools/train_tts.py | 49 | CLI准入与退出码、rank私有错误日志、原控制器分支 |
| **合计** | **1302** | **7份完整重新阅读，无源输出截断** |

worker分1–170/171–340/341–510/511–680连续读完，其余完整全文。辅助旧测试组合输出一次截断，不计测试全文信用。结合上一批5365+1302=6667，13668−6667=7001；机器断言逐项核算。未复读的DSP/监督/Go/浏览器/工具/许可文件不因调用或继承测试获得本批第三遍信用。

## 2. 新增12项：11保护＋1未修观察

`kaggle/tests/test_pass3_inference_boundaries.py`执行原AdapterEngine/RealEngine/Worker/RoPE/租约方法与真实文件、NumPy、safetensors、flock/OFD。Torch只替换最小导入/seed记录/空inference上下文，**没有模拟tensor算子**；实际LoRA prepare/commit、native generation、predictor/codec decode均未执行。合成完成记录不是实际训练证据。

| 新合同 | 结果与覆盖边界 |
|---|---|
| adapter Base绑定不符 | inspect/prepare/commit前409；旧key/prompt保持；不声明全部失败切换回滚 |
| adapter缓存命中 | 仍真实重读并解析合成产物；第二次实际改变safetensors字节即409，不调prepare/commit |
| adapter codes绑定不符 | manifest与profile声明不一致409，不调张量替换，key/prompt不提交 |
| 生成前取消 | 不select、不seed、不调用生成；最小依赖导入仍会先发生，不宣称零成本取消 |
| 生成后取消 | 整句native替身已返回的4800 PCM全部丢弃；不能据此声称可以抢占CUDA核/codec |
| native PCM严格边界 | 空列表、错误采样率/容器/维度、全零、NaN、超token对应长度拒绝；合法4800帧只yield一次float32整句，不伪造声学流 |
| RealEngine度量/关闭 | 两个回放包prepare取max、codec/decode求和、窗口峰值取max；回放iterator耗尽关闭一次，seed记录正确；不是RTF测量 |
| worker部分失败恢复 | 先出一包后生成器异常，1 error/1 stats/1 sentinel、解锁并after_job；后续job可成功，failed/served各1；不解决F07无界队列/F18早断连 |
| 同pin但prompt缺失 | 原worker重新resolve/cache后才生成；resolver/音频为替身，实际hash/pin/锁流程执行，不修复F08旧prompt回滚 |
| RoPE失败重试 | 原错误cause保留且失败未改注册表；重试安装单一bridge，不改变其他registry项；不是实际MimiConfig/Torch smoke |
| GPU记录短写 | 真pwrite少2字节触发异常，FD关闭、busy false、非法记录无诊断值，锁文件仍0600，后续owner可获得；仅同UID合作协议，非GPU测量 |
| F36 | 上游close异常导致窗口finish跳过，详见下节 |

预检12/12一次通过，未跳过。worker错误恢复测试预期记录synthetic异常日志，不能把日志中的ERROR误算为测试失败；原始日志完整保留。

## 3. F36：上游close失败，窗口最终清理未受独立finally保护

原`generated_only_stream`的退出顺序：

```python
finally:
    it.close()
    window.finish(cancelled=True)
```

本批通过原函数实际启动、yield一包后由消费者close；把上游iterator.close设为抛synthetic RuntimeError，原finally第二行即被跳过。

- 上游close调用1次，异常传播；原生成器frame本身已经关闭。
- 被测试显式捕获的真实GeneratedCodecWindow仍closed=False，pending为1920个NumPy样本、codes为合成标记。
- 最后由测试所有者显式finish(cancelled=True)，closed=True、pending空、codes=None，全部本次资源清理。

**结论仅是异常安全的清理顺序缺口，未修。** 准备/predictor/decoder/Torch上下文为明确控制替身；测试为观察状态主动保留window引用。没有证明生产上游close实际会抛异常，也没有证明正常生成器引用释放后仍有持续内存占用、真实GPU泄漏、错误声音或沙沙声根因。建议嵌套try/finally保证窗口清理不依赖上游close成功，同时明确原错误与清理错误优先级；不能仅吞掉异常再伪报成功。

F36三轮稳定见证，与F08加载失败的prompt/pin不一致、F18未开始body迭代的取消丢失不同；不重复登记旧问题。F01–F35/D01及原DSP/trimmer/播放器/校准问题继续保留，未因本批通过而关闭。

## 4. 三轮验证与证据完整性

| 项目 | 第1轮 | 第2轮 | 第3轮 |
|---|---:|---:|---:|
| 累计CPU/ASGI/文件/进程合同：旧402＋新12 | 414 PASS | 414 PASS | 414 PASS |
| 新保护／新未修观察 | 11／1 | 11／1 | 11／1 |
| 失败／错误／跳过 | 0／0／0 | 0／0／0 | 0／0／0 |

共1242通过；新保护33次、F36见证3次，三轮测试ID与观察一致、旧402逐项保留。三轮后台正常exit0、无监听端口；已有实际CPU子进程/信号/OFD、原ASGI与CLI合同随合集运行，F35等旧见证仍未修。本批新增部分没有HTTP浏览器或原生tensor运行，不把方法调用冒充HTTP。

Node30、JS检查、38份Python AST（33产品库存＋新测试＋4审计脚本）、repack通过。858份历史SHA、53源资产/94冻结哈希、正式HEAD15文件保持；原300与Q25–27各50行动不变。pip freeze与上一批一致，无新依赖。完整交接84份、当前manifest/独立verifier/progress均已建立。

**本批未重跑Go/F31/独立F02、浏览器/Player/latency VM、独立ASGI2.3、额外四CLI、NumPy分块/trimmer单独矩阵；不挪用历史成绩。** 沿用Go工具但本批未执行该套件；无Rust/Torch/Qwen/完整权重/CUDA/真实训练/双T4/物理音频，实际音质与提速未签收。

## 5. 原建议部分证据与待实施事项

本批映射原7条R1-045、R2-060/079/093、R3-006/007/071；累计去重27个原ID有暂定链接，**不是27条已完成**。原文/初始处置不改，specific_row_test_signoff/final_disposition_signed_off/product_fix_implemented全部false。没有因本批另开新问题，原300及既有逐题行动保持。

1. 生成器拥有的窗口finish置于独立finally，覆盖上游close本身出错、消费者close与模型异常。
2. 明确close错误不覆盖原生成错误，独立记录阶段与清理完成事实，错误脱敏不吞真失败。
3. bounded window/no reference decode要在真实预训练codec复测，不用本批解码替身或源码因果性签收音质。
4. adapter冷选择与缓存命中都保持Base/manifest/codes来源检查，缓存key不能替代实际tensor文件核验。
5. prepare全部通过再commit，commit异常需原子恢复所有模块；本批只检查不进入prepare的拒绝分支，真实CPU张量/不同rank adapter和CUDA设备路径仍待证。
6. F08需协调engine prompt与worker已接受pin的事务提交/回滚；补一个缺prompt重载保护不能当作已修。
7. F09需统一conditioning规范化与对外mode，同内容pin仍不能签收不同backend/mode一致性。
8. 保留adapter整句缓冲声明和取消后丢弃返回PCM；不要将cooperative stop写成GPU立刻停或首声已提速。
9. F07队列背压和F18早断连需要独立所有权合同；worker解锁后可再服务不代表网络/生产者已取消。
10. 汇总prepare/codec/decode只反映定义中的阶段，不能用生成完成或虚拟播放时间替代真实首声/消费/RTF。
11. GPU锁只约束同版本/同UID合作进程；OFD/nonce/短写保护不是容器/外部进程或真实两卡隔离保证。
12. 继续严格provider元数据/bridge入口，真实依赖环境安装与实际configuration smoke要另证，不强降TF4或临时替换模型。

## 6. 当前检查点与下一步

`g0-pass3-inference-coverage.json`、`g0-pass3-inference-findings.json`、三轮原始log/receipt、manifest、`verify_pass3_inference.py`、`progress-pass3-inference.json`为当前证据；PLAN/IMPLEMENTATION与84份全文交接已同步。

下一批第三遍启动/监督、backend preflight、资源/测量工具与DSP接口，继续核对超时/退出/失败回执与真实测量定义；随后剩余Go/前端/许可等，完成余26份7001行及300最终处置。产品不改、不发18包、不跳S1/Q28、不要求用户点击Continue。

长录音真实训练、全部参考贡献追踪、短录音相似度、首可用DeepSeek prefix立即生成、更响且受保护输出、更低建档延迟、自然连续朗读/无沙沙/接缝、generated-only PCM、双GPU等效参数与真实RTF≤0.3仍未豁免，不由本批fixture签收。
