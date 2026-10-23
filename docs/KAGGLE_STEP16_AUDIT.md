# 第十六阶段交付审计

## 状态

**本轮工程修复及最终三轮回归已通过；整体PARTIAL/BLOCKED，绝不声称真实相似度、无沙沙或T4 RTF0.3已经达到。** 最终状态以`validation/step16/final-checks.json`为准。完整目标22/300不因本轮变更自动升级。

最终完整包`kaggle/kaggle-fixed-step16.py`：306580B、52资产，SHA256 `c6ed6c89e6356fc6c7ab554f96a2c3201a8e4690c007ea66626445cc658b4429`。原始–15和正式工作台冻结。

## 实现及原因

1. `clone_stream.py/worker.py`：默认匹配转写ICL，参考文字不拼目标正文；参考声学码只进talker条件，codec仅接新生成码。显式xvector兼容选择，无文本ICL明确拒绝。不会声称ICL必然完全不产生参考音素或文字幻觉。
2. `voice_binding.py/session.go/scheduler.go`：参考WAV、UTF8转写及语言以长度前缀SHA256，Go/Python固定互操作样本；同会话pin/seed固定，每段携带pin与模式。Worker锁内重读档案/复核，版本或模式不符在lead/PCM前拒绝。先前已经播放的段不能撤回，不是整会话事务回滚。
3. 同路径参考变更时清除Faster旧路径键；预计算提示以档案内存快照保存，生成不再读取可覆盖的锚点路径。取prompt前后参考指纹一致才发布；dtype重载清空提示，后续按需重建。无匹配提示不自动回旧参考decoder。
4. 有界25帧左上下文，删除全历史码cat与比例裁参考；16码组/24k/1920样本每帧契约不合即拒绝，样本游标无重复/缺失，尾部幂等、取消不flush。默认前瞻0，实验可选0..2。
5. 最初方案右2帧前瞻被实际因果源码和真实tiny decoder前缀实验推翻：23813随机参数、8帧vs12帧前缀最大差0。故不默认付160ms代价，不把合成不稳定fixture当真实噪声证据。窗口重解码与完整解码在tiny随机参数下相同，不保证训练权重/多层大模型相同。
6. 每任务重置leveler/DC/包络，默认最大增益6dB（0..12显式可调），目标仍-18dBFS、保留软限幅；无生成语音不flush前段尾。降低底噪放大风险，并非真正频谱去噪已验证；很轻的输出可能比15最大12dB稍轻。
7. Analyst文本/候选更新的部分worker失败不再回`ok:true`；返回503并声明reference_saved。Go activation比较pin/模式且重读当前版本；失败保留原active ID，不把不同参考静默混用。
8. 训练adapter档案的sentence-buffered原生模式保持固定，不被gateway的Mock/faster测试标记覆盖；真正不支持训练的Worker仍会拒绝，不绕过adapter来源/权重校验。
9. 新`tools/voice_benchmark.py`明确--run后只调两真实驻留Faster workers，不加载第三模型；至少3轮、逐GPU/文本、无填充speech_samples分母、worker与HTTP wall RTF并列；WAV/JSONL私有保存，慢行保留，0.3未达失败。无硬件不算通过。

## 三轮审查与自问自答

三轮100条专题建议记录于REVIEW1/2/3，逐项处置见validation/step16/review-disposition.json。全源读取/AST/哈希不是穷尽语义无错，也不是300个bug或300项均已实施。问题19→20→21，各50开发建议后才进入下一题，累计21题1050建议；不向用户重复提问，也不声称已理解到100%可保证。

## 最终验证

- Python完整322×3=966项最终通过（37.320/39.911/43.420秒）；原子ready夹具修正后重跑。
- Node30×3=90、Go race count3、六协议脚本各内置3轮通过；完整Chromium121×3=363通过，最终step16完整复制额外3通过，独立复制页剪贴板/下载/拒绝回退/手机3通过；初始360通过/3旧版本文案失败日志保留。
- 实际Faster0.5.4 resolver/prepare与生产generated-only decoder，ICL/xvector、chunk2/4/8/12，CPU注入prompt/talker/kernel/codec：确认参考标记从未入decoder、80帧153600样本、同路径重载提示更新；不是完整模型。
- 实际HF Qwen12Hz tiny随机decoder23813参数：chunk2/4/8/12 ×lookahead0/2，40帧76800样本，固定1920契约/有界窗口/因果前缀；没有训练codec权重或人声音频。
- 保留完整Faster/Qwen导入与2651参数tinyMimi保存重载，CPU tinyLoRA相对冻结13损失/全部adapter张量逐位一致；不把它们称为Qwen训练质量。
- CPU runtime探针真实HF smoke/API签名通过，无CUDA整体仍blocked。真实T4基准本沙箱未运行，target-rtf-not-run.json明确零测量/blocked。

## 初始失败与修正，不隐去

- 初次301项包含旧15纯向量断言、旧stream方法夹具、未重打包、旧probe调用清单失败。保留python-initial/second/third日志，显式向量兼容测试仍在，新增ICL默认隔离测试，没有删除关键检查。
- 新preflight改查实际_prepare_generation/fast_generate_streaming后，旧fake Backend签名需要同步；修正mock声明而非绕过真实API检查。
- 原生adapter HTTP回归首次拒绝：gateway按Mock/faster推断模式而测试实际注入原生adapter。改以发布档案sentence-buffered类型绑定原生模式，加Go回归；A→B→A三轮/损坏adapter拒播重跑通过。初始adapter_gateway_initial.txt保留。
- tiny真实decoder库导入会向stdout打印flash-attn提示，首轮文件不是纯JSON；原文件保留actual-codec-initial-round*.txt，脚本把库输出引到stderr后最终三轮重新生成纯JSON。
- 两次Go命令cwd误用失败（无模块/相对venv路径）；实际竞态检查使用明确绝对Go工具路径与gateway cwd，非把路径错误算通过。

## 未达到/仍需现场验证

没有用户实际噪声音频、训练权重和T4/DeepSeek通路，不能确定报告的两种声音/沙沙全部根因，不能给相似度百分比、真实速度改善倍数或RTF0.3已达结论。ICL转写正确性、多人参考、生成模型幻觉、真实窗口接缝、声纹/自然度与双GPU段间一致性均需真实三轮听测。

没有新增无依据语言重写或每卡第二模型，没有更改语速/删文/加静音充RTF。原文早触发、录音/取消/安全、手动校准、HF/Mimi修复和训练代码保持。历史独立网页真实训练闭环、维护租约切换、长录音完整审核对齐/全样本覆盖、真实训练保质吞吐、严格声学逐字拒播缺口仍未完成。51份完整备忘录已统一内嵌到KAGGLE_HANDOFF_PROMPT.md。
- 最终并行负载下Python第二轮发现既有训练控制器测试夹具ready文件先创建再写PID，父进程读到了空串；这是测试发布竞态而非已证实的生产租约错误。仅改测试夹具临时文件原子rename，并在启动前记录旧run目录，保留python-ready-race-round2.txt后完整重跑三轮；不放宽PID/锁释放断言。
- 首次完整浏览器三轮360通过/3失败，全部为旧step15测试仍断言release-note必须“第十五阶段”；当前确为第十六阶段。只更新版本文案断言并补ICL/真实RTF待测文案检查，原手动校准/默认关闭断言保留；初始日志browser-initial-repeat3.txt保留，完整三轮重跑，不把初始失败算通过。

### 计时解释
`model_stages.prepare_ms/codec_ms/token_decode_ms`与DSP计时是主机观察/后端计数，不是严格CUDA profiler分解；prepare未额外同步，prefill没有独立汇总字段，几项不能简单相加当总GPU耗时。标准gen_ms与HTTP wall包含生成器必要同步、codec CPU取回和实际输出等待；真实RTF门禁使用总墙钟与未填充speech_samples，不用局部计时冒充0.3。
