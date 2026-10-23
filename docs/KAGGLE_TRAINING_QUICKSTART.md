# 现在怎样真正尝试开训：第十阶段 Kaggle 操作顺序

2026-10-21。**训练核心代码已开发，不需要再等下一轮基础设施；但本沙箱没有执行真实Qwen/T4训练。** 本入口是实验性Base1.7B FP16 LoRA双rank训练，不是完整成品。历史step10不接训练后聊天；当前step11已实现显式原生adapter推理/聊天接入，见KAGGLE_ADAPTER_QUICKSTART.md；仍无网页自动训练。

## 0. 先分清三个状态

| 状态 | 当前结论 |
|---|---|
| 实际loss/反向/优化器/DDP代码 | 已实现；真实CPU小网络/Gloo验证参数更新与跨rank一致 |
| Qwen1.7B在双T4上完成一个训练步 | 尚未运行；需要Kaggle双T4、可信完整本地模型和授权数据 |
| 训练后的声音可在现有网页直接选择聊天 | step11已接入显式选择候选，非自动覆盖；真实重载/试听/质量仍待验 |

不承诺首轮成功、16GB显存够用、训练耗时或音色相似率。首轮以1 epoch、microbatch1、短合法样本开始，记录真实结果后再优化。

## 1. 目标环境与升级

1. 在Kaggle启用双T4，实际运行`nvidia-smi`核对两卡与其他进程。平台开关不是设备证明。
2. 先停止本应用旧GPU服务，再解包当前step11到目标ROOT。仅检查用独立ROOT与`QTTS_UNPACK_ONLY=1`；这不等于实际启动。
3. 保留平台已有、与驱动兼容的PyTorch。**不要在Kaggle照装`requirements-training-test.txt`的Torch2.8/cu128沙箱测试轮子，更不要无条件升级/卸载CUDA库。**
4. 检查Qwen/transformers/safetensors等模型依赖并按可信上游要求准备。训练CLI不自动安装或下载；缺依赖会拒绝。沙箱没有验证完整目标依赖锁。
5. 挂载可信、完整且物化的`Qwen3-TTS-12Hz-1.7B-Base`本地目录，包含文本tokenizer、根safetensors及其索引/分片、generation config与`speech_tokenizer`。禁止pickle、远程Python代码、HF缓存软/硬链接；不能只放空config或假权重。可读README/许可证不代表模型权重可信。

参考实现固定来源：
- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/dataset.py
- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/sft_12hz.py
- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/qwen_tts/core/models/modeling_qwen3_tts.py

没有照搬BF16/标准FA2/全参数AdamW；训练器修正文本嵌入到talker隐藏维度的投影，并把完整联合loss放在DDP.forward内。派生代码保留Apache声明，包内附LICENSE-QWEN-DERIVED.txt。

## 2. 真实数据与声学码

- 在已有命名库/输入准备流程提供自己有权使用的同一说话人音频和逐条匹配转写，完整24kHz mono PCM16 WAV；统一参考≤16秒。首轮至少两个不同样本，建议短样本，不接受fixture或旧未封存码。
- 使用原有`encode_training.py`对实际输入固定manifest hash进行真实CPU声学编码；模型目录应取该Base内`speech_tokenizer`的同一物化内容树。CPU编码可能慢，不能据此保证速度。
- `encode_training.py list/verify`读取实际结果。仅schema2且state=`audio_codes_prepared`的真实编码可进入训练；`test_only_codes`或`legacy-unsealed`明确拒绝。
- 结构一致不证明转写/说话人/内容适合训练。训练前由操作者实际检查这些内容与使用权；CLI显式确认不等于机器语义验证或法律鉴定，源码清单原验证标志不会自动升级。

## 3. Notebook内调用：不填写虚构ID，不在命令写密钥

先在私有Notebook中设置以下**真实非密钥路径/ID**环境变量：
- `QTTS_ROOT`：已解包当前step11源码根目录；
- `QTTS_STATE`：当前本地状态目录；
- `QTTS_BASE_LOCAL`：可信完整Base1.7B物化目录；
- `QTTS_TRAIN_CODES_ID`：从当前list结果选定的真实码版本ID。

下面代码读取真实list并取对应固定hash，不猜第一个版本、不自动选择别人的音频。变量没设置会明确失败；不要将私人转写或密钥粘贴到共享报告。

```python
import json, os, subprocess, sys
from pathlib import Path

ROOT = Path(os.environ['QTTS_ROOT'])
STATE = Path(os.environ['QTTS_STATE'])
BASE = Path(os.environ['QTTS_BASE_LOCAL'])
CODES_ID = os.environ['QTTS_TRAIN_CODES_ID']

def cli(tool, *arguments):
    output = subprocess.check_output(
        [sys.executable, str(ROOT / 'tools' / tool), *map(str, arguments)],
        text=True,
    )
    return json.loads(output)

versions = cli('encode_training.py', 'list', '--state', STATE)['result']
matches = [v for v in versions if v['id'] == CODES_ID]
if len(matches) != 1:
    raise RuntimeError('指定的真实码版本不存在；先检查当前list结果')
selected = matches[0]
if selected['schema'] != 2 or selected['state'] != 'audio_codes_prepared':
    raise RuntimeError('拒绝fixture或未封存历史码；先完成真实声学编码')
CODES_SHA = selected['manifest_sha256']
cli('encode_training.py', 'verify', '--state', STATE,
    '--id', CODES_ID, '--manifest-sha256', CODES_SHA)
BASE_SHA = cli('train_tts.py', 'fingerprint', '--model-dir', BASE)['base_model_sha256']
```

再次检查真实推理服务已停止、合作锁空闲，并用`nvidia-smi`检查显存。锁空闲并不证明显存空闲；不要删除fleet.lock或按旧PID强行抢占，不会自动停推理。

**只有亲自完成数据/权利审阅并接受实验风险后，才执行以下训练调用。** 它会真正尝试加载模型和进行优化，不是无副作用的演示：

```python
command = [
    sys.executable, str(ROOT / 'tools/train_tts.py'), 'train',
    '--state', str(STATE), '--id', CODES_ID, '--manifest-sha256', CODES_SHA,
    '--model-dir', str(BASE), '--model-sha256', BASE_SHA,
    '--epochs', '1', '--accumulation', '4', '--max-sequence', '1024',
    '--lora-rank', '8', '--lora-alpha', '16', '--lr', '0.00002',
    '--timeout', '1800', '--confirm-data-reviewed', '--ack-experimental-training',
]
process = subprocess.Popen(command, text=True, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, start_new_session=True)
try:
    stdout, stderr = process.communicate()
except KeyboardInterrupt:
    process.terminate()  # 向本次持有的控制器对象取消，不查旧PID文件
    stdout, stderr = process.communicate(timeout=15)
    print(stdout)
    raise
print(stdout)  # 仅控制器收据，不输出完整私人转写
if process.returncode != 0:
    raise RuntimeError('训练没有完成；检查本机私有training_runs收据/日志，不要标记成功')
receipt = json.loads(stdout)
```

两rank必须各有实际设备、更新参数且最终adapter摘要相同，全部选中样本覆盖，才会保存adapter；奇数样本采用重复打乱序列前缀补偶数，报告保留重复ID，不drop_last。序列超预算整份拒绝，不裁掉文本/音频。timeout包含rank启动/模型加载/训练，不含父进程前置指纹/收尾核验，终止另有等待；未承诺30分钟足够，也不是全命令硬截止。

## 4. 结果、取消与下一步

- 本地`STATE/training_runs/<job_id>/`有request、每rank私有日志/JSON、result；成功有`adapter/adapter.safetensors`、`speaker.safetensors`、manifest。
- 私有日志可能包含框架路径/错误上下文，不要公开粘贴。请求/音频/文本/adapter不进Git，不自动Dataset备份；删原库不等于删输入/码/训练副本。
- 正常完成返回0，失败/拒绝/总超时2，控制器SIGTERM/INT取消130。Notebook仅中断`subprocess.run`不保证自动向孩子发受控取消；长训练应保留明确的Popen对象，向该控制器发terminate并wait，不按陈旧PID发信号。父SIGKILL也有rank PDEATHSIG与共享FD最后引用保护。
- 不支持恢复optimizer/scheduler/RNG训练状态；当前adapter是推理候选，不是完整可恢复训练检查点或CustomVoice模型。中止/失败不覆盖旧推理模型。
- `tts_training.load_adapter(core, checkpoint, base_directory)`严格检查Base绑定/文件hash/层与张量后挂载LoRA，返回保存的统一参考speaker embedding。须单独加载同一Base、按Base克隆prompt协议接入，并用新进程真实合成/试听；当前没有网页自动部署，不能把CPU小网络重载当Qwen验收。

**多久能开始：代码入口现在已有；真实环境与数据就绪即可尝试，不依赖另一个开发阶段。多久训练成功/达到目标音色：目前没有可靠实测，不能给出保证。** 下一开发重点是现场首步故障修复和训练adapter接入现有推理/聊天，而不是继续追加封存工具。
