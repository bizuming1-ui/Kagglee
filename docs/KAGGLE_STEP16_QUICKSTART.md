# step16 升级与真实双T4验收

## 完整代码

- `kaggle/kaggle-fixed-step16.py`：306580字节，52个完整内嵌资产。
- SHA256：`c6ed6c89e6356fc6c7ab554f96a2c3201a8e4690c007ea66626445cc658b4429`。
- 独立3001复制预览可“复制全部代码”或下载；不改正式3000工作台，不运行Python。
- 原始及step1–15保留，不再把15纯向量模式作为相似度改善的既定答案。

## 升级顺序

1. 先备份需要保留的私有录音、库、档案和adapter；不要删除原录音或手工删除锁文件。
2. 完整停止/重启Kaggle会话，选择T4×2，Internet On。不要让旧15进程与16共用同一GPU/ROOT。
3. 在Code单元格粘贴**完整16代码**运行。默认真实Faster/FP16、每T4一个模型；不要用QTTS_MOCK取得声学结论。保留HF/Mimi正常导入修复，不卸载Kaggle Torch。
4. 可在完整代码之前显式设置：

```python
import os
os.environ['QTTS_CLONE_MODE'] = 'icl'
os.environ['QTTS_MAX_GAIN_DB'] = '6'
os.environ['QTTS_CODEC_LOOKAHEAD_FRAMES'] = '0'
# 紧接着粘贴完整step16，不是只执行这几行。
```

5. 等待双worker ready，再启用已有普通声音档案。**参考音频应只有一个说话人，参考文本必须逐字匹配该锚点**，不是想让它新说的目标文字。选项/档案编辑入口仍在。ICL无转写会明确拒绝，不静默改成另一种声音。
6. 有ASR错字先审核转写。切换候选/修改转写时停止当前会话，再重新启用。若提示reference_saved但worker未全部就绪，保存已发生，需重试启用；不会以旧声音冒充成功。旧会话pin不符会在该段任何PCM前拒绝，已播旧段不能撤回。
7. 首先直接朗读与参考不同的短目标文，再试长文、跨句与两卡交替；最后试DeepSeek第一句及时开始。没有声学逐字拒播器，ICL仍可能产生音素/文字幻觉，不保证无添字或百分百相似。

## 沙沙声的处理边界

- 解码器不接参考码/参考PCM；没有参考呼吸拼接或低延迟占位。
- 只拼未提交生成样本；窗口左25帧有界，默认右前瞻0。真实tiny随机decoder的因果前缀实验通过，故未默认增加160ms前瞻；仅显式实验可设2。
- 每任务重置响度包络，避免上段/双卡历史状态不同；输出目标仍-18dBFS，默认最大向上增益6dB，保留软限幅。需要更响可现场对照9，极限12；底噪也可能被放大，不建议盲开最大值。
- 没有用户实际沙沙样本，不能断定来源是模型、参考噪声、录音环境还是播放链；没有强低通/强谱门掩盖问题，也不声称“已无沙沙”。比较同参考、同文、同seed的独立生成WAV，不把响度变小误判为音质一定变好。

## 真正RTF≤0.3：目标机三轮实验

新工具只调用**已经驻留的两张真实GPU worker**，不启动第三模型。启动完成后可在同Notebook后续Code单元格运行；bootstrap会返回，supervisor在后台。先停止网页合成，确认空闲，填写界面实际档案ID（不是显示名称），输出目录每次用新名称：

```python
import subprocess, sys
subprocess.run([
    sys.executable, '/kaggle/working/qtts/tools/voice_benchmark.py',
    '--run', '--profile', '填写实际档案ID', '--rounds', '3', '--chunk-size', '8',
    '--output', '/kaggle/working/qtts/state/benchmarks/step16-run1/report.json',
], check=False)
```

ROOT或STATE自定义时用实际路径，并让工具继承相同QTTS环境。输出保留在私有state，不能自动上传或共享。

- 两worker必须ready/idle/model_loaded、Faster真实引擎、ICL-generated-only模式、GPU0/1分别独占可见；否则blocked。
- 先单独记录参考提示预热时间，再测3轮×2卡×3段=18条；保存18个生成WAV、逐条原始`measurements.jsonl`与report。后续失败不会删除先前慢行或WAV。
- 标准RTF=`gen_ms/1000/(speech_samples/24000)`，wall RTF包括HTTP/排队/必需等待。分母排除lead/tail/fade填充，失败/取消/anomaly不算成功。`rtf_x`是倒数，不是RTF。
- 任一条worker或wall RTF>0.3均`target-not-met`、退出2；全部满足也只是`measured-speed-only`，**不是音色/无噪声/自然度验收**。
- 不带`--run`时输出blocked、零测量，不会以CPU或Mock替代。这个沙箱当前没有真实T4结果，不能声称0.3已经做到。
- 对比chunk4/8/12请各用新的输出目录、相同参考/文本与seed，保留慢结果；只在试听合格前提下选更快配置。两卡吞吐不能相加冒充单卡RTF，不能改语速/删文/加静音。

## 真正声学验收仍必需

每张卡/每段分别核查：像参考单人、段间一致、自然易懂、无异常沙沙、没有播放参考内容、没有添字漏字；再检查first_played_ms与underruns。声纹余弦分数不能当“99.5%相似”；工程回归与tiny随机权重均不能替代训练权重试听。网页训练闭环、长数据全覆盖、真实双T4训练提速与严格声学拒播等历史缺口仍未完成。
