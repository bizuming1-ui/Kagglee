# 第十二阶段：依据Kaggle现场日志修复Mimi/RoPE兼容与启动重启风暴

2026-10-21。先保存计划与Q11，再写实现；原始至step11冻结。用户已实际识别两张Tesla T4，Python3.12.13/Torch2.10.0+cu128/faster0.5.4/Transformers5.20.2，模型加载报MimiConfig.rope_theta，尚无加载/推理成功证据。

1. 审查PyPI实际wheel：faster0.5.4要求qwen-tts-hf>=0.1.1.post1和Transformers>=5.15.1，不能只降Transformers到4.x造成依赖冲突。qwen-tts-hf兼容函数仍读取config.rope_theta，现代Mimi使用rope_parameters。
2. 在原实际依赖组合上做最小、可拒绝、不猜theta的兼容桥：仅包装已识别Qwen默认RoPE函数；从现代Mimi配置真实rope_parameters读取theta，对临时config副本提供旧字段，不改模型权重/config文件、不把theta统一硬编码为10000、不改非默认scaled RoPE。
3. Worker/CPU编码/原生推理/训练的Qwen加载前接入；前置探针增加真实MimiConfig+Qwen默认RoPE CPU数值smoke，早于权重加载，不再只验签名。固定faster/hf/transformers已审查三版本，保留平台Torch/CUDA，不盲降/升级。
4. 不兼容异常标fatal，supervisor停止该worker而非反复重启；bootstrap看见fatal及启动失败时清理它自己创建的supervisor，保留合作FD直到子退出。不给旧日志PID发盲杀命令。
5. 两worker继续分别只看GPU0/1，健康报告真实设备/驻留状态；模型加载成功后保持常驻，不自动空闲卸载。验证是假设备/CPU替身时不能说双T4模型成功。Kaggle会话/硬件回收不受应用控制，不承诺永久GPU。
6. 新step12包与浏览器复制页面更新，step11冻结；给用户明确“停止并重启完整Kaggle会话后复制新包”，不是仅刷新网页/重跑旧cell。
7. 真实wheel配置复现与修复数值对照、负面配置、旧接口不变、fatal控制器/双卡分配/源码复制及已有回归三轮；完整Qwen/双T4仍需用户目标再次运行验收。
