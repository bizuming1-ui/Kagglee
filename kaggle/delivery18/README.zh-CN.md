# 完整 Kaggle 源码候选（从现存 S5 接线，非正式发布）

## 下载哪个

- `kaggle-step18-candidate.py`：完整单文件，内嵌全部运行源码，不是网络下载器或零散补丁。
- `kaggle-step18-full-source.zip`：同一入口＋全部可读 Python/Go/JS/Rust/训练源码＋MANIFEST；不含模型权重、编译器、依赖wheel、用户音频、状态、token或日志，不是离线安装包。

重要：本次工作区实际只保留到 S5。会话曾述 S6–S8-C 文件及 alpha ZIP 当前缺失，原因未知。本包不冒称恢复它们，也不包含其时序/检查点/配对控制器/收据overlay。原17、现存S1–S5和旧证据保持不变。

## Kaggle 使用：先校验，再显式运行

1. 新建 Notebook，Settings 选择 **GPU T4 x2**，**Internet On**。准备足够存储，模型/编译会占时间；未测得总耗时承诺。
2. 把完整 `.py` 文件上传为私有 Kaggle Dataset 并 Attach，或保存到 `/kaggle/working/kaggle-step18-candidate.py`。下面命令中的文件路径应改为你实际文件位置；`/kaggle/input/...` 是只读输入，不在其中创建runtime。
3. 单元格1（无安装、无模型、无Secrets读取）：

```python
%run /kaggle/working/kaggle-step18-candidate.py --check
```

4. 单元格2（显式允许真实安装/模型下载/启动）：

```python
%run /kaggle/working/kaggle-step18-candidate.py --run --destination /kaggle/working/qtts18-new
```

目标目录必须不存在；重复运行不能覆盖旧目录，不自动删旧数据。需要先正常停止旧服务；有旧进程/显存占用时，继承的ownership门禁会拒绝。不要仅删锁文件强行重开。重启session或确认停止后选择新的目录。

整段代码直接粘贴进Notebook时默认只校验，不会偷偷下载模型。仍需上述显式run，或同一内核中调用：

```python
main(["--run", "--destination", "/kaggle/working/qtts18-new"])
```

无GPU、不是两块独立T4、设置了MOCK/单GPU豁免时返回blocked，不自动切MOCK。硬件可见不证明CUDA/模型可用，后续还要通过原bootstrap的运行时探测。当前沙箱不能访问Kaggle真实双T4，不能保证本命令已在Kaggle成功。

Kaggle Secrets 可选 `DEEPSEEK_API_KEY`（聊天）、`HF_TOKEN`（模型下载）、`QTTS_ACCESS_TOKEN`（网关访问）；仅run时读取，不打印值。缺token时原鉴权模块生成私有token。打开启动输出的URL，在原界面解锁；不要公开token/日志或Notebook输出。声音初始为空，不强制预填。

## 新入口实际接了哪些修改

- 原 `py/analyst.py` 替换为当前隔离18分析服务，附profile输入/校准快照/有效度量三个依赖。
- 原 `py/worker.py` 替换为S4 worker，附因果NumPy DSP和有界trimmer两个依赖。
- `web/app.js` 使用S5完整Player/Worklet，非只有测试helper。
- 新包内bootstrap只关闭Rust安装/编译分支，明确使用numpy-causal-v1；其他原安装、模型、Go、supervisor、录音、鉴权、训练功能保留。冻结源码本身不改。
- 原MEMO历史首页改为本候选范围说明；原53资产其余部分保持，清单记录每项来源/变化。

## 训练/备份源码在哪

可读ZIP `source/py/tts_training.py`、`training_job.py`、`lora_adapter.py` 等含实际训练实现；`source/tools/train_tts.py`、`trained_voice.py` 为命令入口；`source/py/persist.py` 与 `source/tools/*` 保留备份/恢复等代码。启动后声音库/录音/合成界面沿用原页面；**不能把这些源码存在说成“训练按钮闭环、超10分钟录音、同质量加速已经验证”**。建档/参考缓存不等于训练，默认克隆不自动训练adapter。

当前仍沿用原bootstrap下载工具链策略和部分非固定依赖，不是经过全供应链签名验证的锁包；继承LICENSE不是所有模型/依赖和声音授权已清关。训练、恢复、真实两模型、DeepSeek首前缀、音色自然无嘶声逐字、实体首声<3秒/RTF≤0.3都仍需实际验证。参考PCM不得混入生成播放。

## 可离线做的事

```bash
python kaggle-step18-candidate.py --check
python kaggle-step18-candidate.py --extract-only --destination NEW_DIRECTORY
python kaggle-step18-candidate.py --doctor
```

前两项不安装、不读Secrets、不启动服务；doctor只读取nvidia-smi硬件库存，不加载模型，CPU环境预期退出2。解包IO失败可能留下自己的不完整新目录，非掉电事务回滚。

包装SHA/CRC只检查一致性，不是身份认证或可信供应链。已有旧日志/旧成功证据不覆盖。本轮CPU/MOCK联通与模型门禁必须分开阅读；源代码交付完成不等于整体产品完成。
