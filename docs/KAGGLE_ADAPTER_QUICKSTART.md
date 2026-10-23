# 第十一阶段：训练adapter → 命名声音 → 现有聊天

2026-10-21。**接入代码已实现，真实Qwen/T4训练、重载及试听未验收。** 原有faster声学流式路径不改；新后端是官方Qwen原生API，**句级缓冲，不是声学流式**。没有新增第三个主视图或假训练按钮。

## 1. 前提与模式边界

- 使用`kaggle-fixed-step11.py`，先停止旧GPU服务再解包到自己的ROOT；可用`QTTS_UNPACK_ONLY=1`仅解包，不代表启动成功。原始到step10均保留。
- 依照`KAGGLE_TRAINING_QUICKSTART.md`，真实完成一个schema2实际编码输入的双rank训练，取得`result.json`中的**实际job_id**。failed/timeout/cancelled/缺检查点、fixture/旧未封存码不能发布。
- 保留训练run下request/result/adapter三件套和原码版本；发布时会持原码租约验证并读取统一参考。不要猜某个目录名或自动选第一个run。
- Base必须是训练使用的同一可信、物化完整本地Base1.7B，hash固定。禁止pickle、remote code与HF缓存链接。目标依赖仍需自行审查，不把沙箱Torch2.8/cu128测试轮子照装到Kaggle。当前代码严格检查base/1b7/16组契约，真实权重config尚未核验；如不一致应对照真实config修正代码，不能改元数据伪造通过。
- 原生启动要求已有官方`qwen-tts`、`safetensors`及兼容依赖，不自动用未知版本替换引擎。与faster的CUDA graph注入兼容性未验证，所以**不向faster动态注入LoRA，也不离线合并并复制完整Base**。
- 每个worker仅一个可见GPU、一份Base；由既有supervisor分配GPU0/1。CPU接口替身测试不是这两卡已运行的证据。原生模式只接受训练候选，普通参考档案仍保留，但要使用原有faster模式；不在同一个worker里混驻两种模型。

## 2. 显式发布，不自动激活

在私有Notebook中设置自己真实的`QTTS_ROOT`、`QTTS_STATE`和`QTTS_TRAIN_RUN_ID`；最后一个来自本次成功训练收据。下面使用实际记录读取hash，不填写虚构ID。

```python
import json, os, subprocess, sys
from pathlib import Path

ROOT = Path(os.environ['QTTS_ROOT'])
STATE = Path(os.environ['QTTS_STATE'])
RUN_ID = os.environ['QTTS_TRAIN_RUN_ID']

def voice_cli(*args):
    output = subprocess.check_output(
        [sys.executable, str(ROOT / 'tools/trained_voice.py'),
         *map(str, args)], text=True)
    return json.loads(output)['result']

record = voice_cli('describe', '--state', STATE, '--run-id', RUN_ID)
```

亲自确认该run及数据来源、权利和实验风险后，设置自己要显示的`QTTS_TRAINED_VOICE_NAME`，再执行：

```python
published = voice_cli(
    'publish', '--state', STATE, '--run-id', RUN_ID,
    '--adapter-sha256', record['adapter_manifest_sha256'],
    '--name', os.environ['QTTS_TRAINED_VOICE_NAME'],
    '--ack-unverified-adapter')
print(published)
```

输出profile_id、pin和`active_changed=false`；音质/现场重载验收标志仍false。**发布不是训练，不会替你启动模型、证明音色相似或自动启用。** 完成记录与声明只是同UID合作流程记录，不是官方加密签名/法律证明，也不能防同UID恶意伪造整个训练目录。

发布会把一段统一参考WAV及匹配转写复制进现有profiles目录；该目录**沿旧私有Dataset备份语义**，启用原有备份后可能上传这些内容。训练run、所有训练样本和完整模型不会因此自动云备份。删除原库不等于删profile或远程备份；删除profile也不自动删除run。备份恢复若缺少对应run/adapter/Base，新后端必须报错，不会换成原Base或另一声音。推理只读取已固定的adapter记录，原码仅是发布时依赖；删除原码后，已发布profile仍需单独管理。

## 3. 原生后端启动

先按既有所有权协议停止自己旧推理任务并确认相关rank已结束；不要删除锁或拿旧PID盲杀。`nvidia-smi`另查真实显存，合作锁不证明设备空闲。

设置`QTTS_BASE_LOCAL`为同一完整本地Base，并在**新启动进程环境**中选择后端：

```python
runtime_env = {
    **os.environ,
    'QTTS_ROOT': str(ROOT),
    'QTTS_STATE': str(STATE),
    'QTTS_MODEL': str(Path(os.environ['QTTS_BASE_LOCAL'])),
    'QTTS_BASE_SHA256': record['base_model_sha256'],
    'QTTS_TTS_ENGINE': 'qwen-adapter-buffered',
    'QTTS_MOCK': '0',
    'QTTS_DTYPE': 'fp16',
    'QTTS_TUNNEL': 'none',
}
runtime_env.pop('QTTS_UNPACK_ONLY', None)
runtime_env.pop('QTTS_ALLOW_SINGLE_GPU', None)
subprocess.run([sys.executable, str(ROOT / 'py/bootstrap.py')],
               env=runtime_env, check=True)
```

这会真正尝试加载模型及运行既有服务，不是无副作用检查；仍需检查目标环境工具链与启动日志。Secret使用既有私有配置，不在共享命令/报告里输出。先本地验证，再决定是否启用公网隧道。bootstrap的实际依赖/编译安装路径尚无Kaggle现场验收，不承诺启动耗时。

新后端在加载前后核对Base树hash，仅启动时读完整Base；每次声音使用核验profile binding、run状态及adapter成员/hash/张量摘要，不每句重新hash多GB的Base。它加载官方eager/FP16，不复用faster图；使用保存的speaker embedding构造x-vector-only prompt，而不是重算一个无关参考或伪装成完整CustomVoice。

## 4. 现有界面选择与对话

1. 打开原有控制台并解锁；只有“录制参考语音 / 语音对话”两主视图。
2. 声音列表显示“训练候选/句级缓冲/未验收”。在档案卡片点“选择此训练版本（双GPU加载，句级缓冲）”。两worker必须确认加载才改变active；某卡失败不把界面标成启用成功。
3. 训练参考文本只读，保存文本/候选校准禁用，后端同样返回409；要变更训练条件请另做明确训练版本。删除入口保留。
4. 先用直接朗读短句测试，再用现有DeepSeek流式文字与语音聊天。网关仍切段、双worker调度、有序转发及播放停止；声音选择使用当前profile_id。
5. 原生API一段文本生成并解码完成才给出一个wave；Worker后处理的PCM尾部/停顿帧不意味着模型声学流式。诊断health、Worker stats标注`sentence-buffered`。首声可能明显慢于faster，不承诺<3秒/RTF/16GB适配。
6. 取消传入Transformers stopping criteria；取消后丢掉迟到完整wave。停止语音播放不等于立即终止正在执行的CUDA kernel/codec decode；下一请求可能仍需等worker释放锁。
7. 原生无帧等待/健康stall/监督重启预算180秒，旧faster分别保持60/75/90秒；这只是保护预算，不保证任意长句180秒完成。超时不能改成“通过”。

切回原有普通参考声音：先正常停止自己原生服务，再以`QTTS_TTS_ENGINE=faster`启动原有模式。原生模式拒绝普通profile，faster/Mock拒绝训练profile；没有自动卸载再偷偷换引擎的路径。

## 5. 必须现场填写的验收

- 双T4实际设备、每worker唯一GPU与各自一份Base、真实峰值显存；先一个小训练步，检查权重变化与跨rank一致。
- **新进程**按固定pin重载同adapter；每GPU输出真实24kHz WAV，确认非空/有限/非全零，盲听参考与输出，不把CPU oracle或profile文件当试听证据。
- 两个已训练版本A→B→A、同文本同seed及不同文本；损坏/缺失绑定必须明确失败，不能输出原Base冒充训练声音。
- 真实普通路径回归、DeepSeek回答中途切换/取消、长回答有序播放、耳听断句和爆音；测首个真实语音包及完整延迟，明确句级缓冲。
- 没有真实Qwen/T4运行、物理音频及外部模型可用性证据时，上述项保持“待验收”。当前下一步就是这组真实运行，不增加工具前置阶段。
