# 第七阶段审查：离线声学码事务与真实编码门禁

> 第七阶段冻结证据；当前源码/打包入口为step10，见KAGGLE_STEP10_AUDIT.md。以下统计保留当时结果，不代表实际GPU/编码/训练已验收。

2026-10-21。先保存KAGGLE_STEP7_PLAN.md与Q6的50条行动建议，再增量编码。**实现了调用真实Qwen tokenizer的本机入口与安全事务，但真实编码仍blocked；没有运行真实权重，没有训练。**

## 交付与已保留内容

- 独立`kaggle/kaggle-fixed-step7.py`：222808字节、35资产，SHA256 `3fe57769560c076d6d288a87cae6150b0a9404597eb0ea3997ab26de596f4cd0`。清单source_manifest_step7.json；repack.py默认生成step7。原始与step1–6冻结。
- 新增`py/training_codes.py`和`tools/encode_training.py`；`py/training_data.py`只增固定版本读取租约与删除互斥，既有准备/校验语义不变。没有新增HTTP路由/网页训练按钮；两主视图、命名库、逐条转写、授权隔离、旧快捷参考处理与全部工作台功能保留。
- 正式工作台仍15文件1043155字节/1MiB余5421字节，HEAD不变；独立交付，不提高容量、不删除历史、不直接改HEAD。复制测试仅在隔离临时项目。

## 实现与边界

| 范围 | 本次实现 | 不扩大解释 |
|---|---|---|
| 输入使用租约 | 先固定manifest SHA256并全量校验，再持有目录外`.use-{id}`文件锁；编码期间HTTP删除409，其他输入列表可读 | 合作式Linux flock，不是同UID恶意进程隔离；不修改快照文件集合 |
| 进程死亡 | SIGINT/SIGTERM/总期限停止worker进程组并必要SIGKILL；Linux PDEATHSIG与ppid握手覆盖控制器被强杀 | 生产编码器是单进程CPU线程；不是任意第三方外部进程的系统级沙箱 |
| 真实适配入口 | 懒加载Qwen3TTSTokenizer，CPU/FP32/eager/两线程、单条numpy float32/24kHz全波形 | 当前无Torch/qwen_tts/权重，真实适配只测了stub调用契约，未执行真实编码 |
| 模型固定 | 本地物化JSON/safetensors全文件内容树SHA256，≤512文件/128目录/4GiB/JSON每份≤1MiB；拒绝软硬链接、pickle、auto_map和越界分片索引 | 需可信来源预先固定hash；不是官方签名或权重真实性证明，不能防同UID恶意竞争写入 |
| 加载约束 | local_files_only/offline/trust_remote_code=false/use_safetensors，CPU与实际dtype/配置/特征采样率复核；加载前后及发布前重算模型hash | HF离线参数不是OS断网沙箱；运行时包版本仅记录，不宣称已校验其源码与上游提交完全一致 |
| 结果契约 | 恰好一个返回，ceil(输入帧/1920)行、16列、严格整数0..2047；全部样本顺序/逐条text/统一ref_audio保留 | 结构检查不证明声学码语义、还原音质或训练可用性 |
| 独立输出 | STATE/training_codes/{UUID}/复制全部WAV、rank_plan，写train_with_codes.jsonl和manifest；源输入可随后删除 | 复制会另占磁盘，删除源输入不删除码副本；没有外部训练读取租约 |
| 事务和预算 | 0700/0600，staging全核对后rename发布、失败回滚、下一写操作清理被杀遗留暂存；32份/64MiB单份/256MiB总量/256MiB余量 | 应用预算非OS配额；保守预留原输入大小+8MiB可能提前拒绝，不裁样本绕过限制；无断电耐久保证 |
| 状态 | 真实适配执行返回才可audio_codes_prepared/tokenization_executed=true；注入测试编码器强制test_only_codes/false | tokenization_verified/training/two_rank/inference始终false；不是文本tokenizer/优化器/检查点 |
| 隐私 | 不自动Dataset备份；公开收据不含私人转写或底层异常；子进程剥离已知HF/DeepSeek/Kaggle/访问凭据 | 原始输入/码JSONL确实含转写；本地可信操作员仍可读，临时操作目录并非安全擦除 |

## 本机使用约定

CLI没有Mock编码参数，不提供远程路径执行或下载/安装模式。请使用目标环境Python；以下是操作说明，**并非本沙箱已经执行的真实编码命令**。

1. 通过原有声音库窗口生成第六阶段输入，取得真实`id`和`manifest_sha256`。输入窗口状态仍是input_snapshot_ready，不因另有离线副本而修改其状态。
2. 准备可信来源的Qwen3-TTS-Tokenizer-12Hz本地完整模型，必须物化JSON/safetensors，不直接使用HF缓存软链接或包含README/其他文件的未整理目录。当前没有自动下载器或GPU依赖锁文件。
3. 对选定目录取树指纹，人工核对可信来源后固定；指纹只是变化检测，不证明这个模型属于官方。

```bash
ROOT=${QTTS_ROOT:-/kaggle/working/qtts}
STATE=${QTTS_STATE:-"$ROOT/state"}
python "$ROOT/tools/encode_training.py" fingerprint --model-dir "${MODEL_DIR:?设置可信本地模型目录}"
# 根据真实结果设置INPUT_ID、INPUT_MANIFEST_SHA256、MODEL_TREE_SHA256，不填虚构UUID或示例hash。
python "$ROOT/tools/encode_training.py" encode --state "$STATE" \
  --id "${INPUT_ID:?设置真实输入ID}" --manifest-sha256 "${INPUT_MANIFEST_SHA256:?设置固定输入hash}" \
  --model-dir "$MODEL_DIR" --model-sha256 "${MODEL_TREE_SHA256:?设置预先固定模型hash}" --timeout 1800
python "$ROOT/tools/encode_training.py" list --state "$STATE"
# 以下两个变量应来自本次真正输出，不能拿输入ID/hash替代。
python "$ROOT/tools/encode_training.py" verify --state "$STATE" \
  --id "${CODES_ID:?设置真实码副本ID}" --manifest-sha256 "${CODES_MANIFEST_SHA256:?设置码清单hash}"
# 确定没有手动训练读取后，才删除这个独立副本。
python "$ROOT/tools/encode_training.py" delete --state "$STATE" \
  --id "$CODES_ID" --manifest-sha256 "$CODES_MANIFEST_SHA256"
```

CLI超时允许1..3600秒，正常0，拒绝/blocked/失败/超时2，常规取消130。公开错误不包含库名/转写/原始异常。超时或取消恰逢rename之后、收据之前时，结果可能已经原子提交：先list及固定hash verify，不盲目重跑。父进程被SIGKILL可能来不及给收据；worker自动死亡释放租约，孤立staging在下次写入清理。

码输出JSONL仍使用audio/text/ref_audio及audio_codes；路径必须按**码副本目录作为cwd**解析，不能按原输入或启动命令cwd猜测。rank_plan仍是数学分配，不是两个rank实际运行。默认配置环境变量QTTS_MAX_CODE_DATASETS/QTTS_MAX_CODE_DATASET_BYTES/QTTS_MAX_ALL_CODE_DATA_BYTES；沿用既有上传音频边界。

输入租约并非训练器使用租约：未来真正训练还需阻止删除码副本，接入显存所有权/推理与训练模式、文本tokenizer/实际两rank/梯度/optimizer/checkpoint及重载试听。当前不自动停在线服务，不允许GPU编码参数。

## 分层验证（docs/validation/step7/）

- Python新增33项码事务/模型门禁/CLI/进程测试，加step6冻结回归，总146项。最终146×3＝438通过，python-round1/2/3.txt。包含真实fork租约、控制器SIGKILL、SIGTERM、超时、SIGTERM忽略的后代SIGKILL及pidfd死亡确认；没有真实模型执行。
- Go28顶层/16子测试race三轮；Node工作台API30×3通过。
- training-http3-final.txt：真实Go→analyst→磁盘三轮，新增本机租约阻止HTTP删除且列表可读，保留原输入篡改/独立副本/单独删除与原始库负向解码回归；不增加模型作业。
- codes-cli3.txt：真实本地CLI list/verify/delete与文件事务三轮，**码全为fixture**；原输入删除后码副本仍可校验。另用明确标注的无效fixture权重目录仅触发缺依赖门禁，三次blocked，未加载任何真实模型。
- mock-pipeline.txt：两CPU Mock worker三轮有序分段/取消恢复，非真实双T4。
- browser-repeat3.txt：60 QTTS＋47工作台＝107唯一×3＝321通过（11.5分钟）。包含第七阶段222808字节完整Python系统剪贴板逐字节一致三次且step6保持；final-copy-repeat3.txt另专项3/3通过。均为隔离临时项目。生产JS/HTML未改，不新增主视图。
- 确定性repack当前35资产/原始22哈希、语法/compileall/diff检查通过。runtime-probe.json仍blocked/退出2，Torch/流式后端/ffmpeg缺失，没有模型/GPU验收。

## 初检、复审和失败记录

1. python-initial.txt保留3个测试辅助错误：两处Fixture.reject不接关键字参数、Mock.poll始终活跃使二次清理消耗完预设wait序列。修正测试调用与真实退出顺序，不放宽业务断言。
2. python-review.txt保留一次异步SIGKILL尚未完成时立即读取/proc的竞态；改用pidfd有限等待确认实际死亡。
3. python-proc-reap-race-failure.txt保留最终第三轮一次/proc在exists与read之间被OS回收的ESRCH。仍必须pidfd死亡确认，然后接受已消失或Z/X；没有把活进程当成功。修正后全146项重新跑三轮。
4. 复审发现控制器被SIGKILL会使原独立会话worker继续执行，补Linux PDEATHSIG/ppid握手及实际强杀回归。初版浏览器已75次通过后中止，browser-interrupted-parent-review.txt保留，绝不计最终三轮；修正后重跑。
5. codes-cli-initial-helper-error.txt保留新增测试脚本误用LibraryStore.delete；核对实际remove接口后修正并重新完成三轮。仅测试助手错误，未改生产删库接口。

## 未通过项与下一步

- 码清单固定源输入ID/hash，但不复制原输入完整manifest；删除原输入后仍能核验码副本，却不能从中恢复完整的原库来源/声明资料。需要溯源时保留原输入清单；真正训练接入前须补完整来源/授权封存策略。
- 当前没有真实audio_codes产物、真实Qwen编码/解码/音质证据；本机入口不是模型验收。CPU速度、RAM峰值与目标依赖组合未实测。
- 仍无真实双T4训练、GPU资源模式、文本tokenizer、梯度/优化器更新、loss、检查点或训练后推理。CPU路径是保守前置，不是最终双卡性能方案。
- DeepSeek、物理麦克风、真实ffmpeg压缩容器、首声<3秒/RTF≤0.5/99.5%音色目标仍未验收，不用协议/fixture代替。
- 清单继续21/300，本阶段不增加GPU/编码真实执行勾选。专业自问自答6×50＝300建议，不等于300项修复。
- 下一步先实现可审计GPU资源所有权/推理与离线任务互斥，再在可用目标设备以可信模型完成单条真实编码/解码、完整覆盖、内存与耗时；之后才接文本tokenizer及真正两rank优化器和检查点。

## 固定上游依据

本轮通过GitHub API再次读取以下固定文件，仅核对源码未执行：

- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/finetuning/prepare_data.py
- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/qwen_tts/inference/qwen3_tts_tokenizer.py
- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/qwen_tts/core/tokenizer_12hz/configuration_qwen3_tts_tokenizer_v2.py
- https://github.com/QwenLM/Qwen3-TTS/blob/022e286b98fbec7e1e916cb940cdf532cd9f488e/qwen_tts/core/tokenizer_12hz/modeling_qwen3_tts_tokenizer_v2.py

这里记录的是契约参考提交，不是当前尚未安装的运行时包源码身份校验。
