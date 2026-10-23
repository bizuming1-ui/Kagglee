# 第十三阶段计划：修复Faster延迟导入导致RoPE补丁未安装

先计划/问题12的50条建议，再实现；不向用户重复提问。

## 现场事实与根因路径
step12在两T4上再次以同一MimiConfig.rope_theta失败。预检明确显示HF5模块未加载却给warning。真实faster0.5.4顶层只导出包装类，直到from_pretrained内部第194行才导入qwen_tts；step12仅查sys.modules，过早not_applicable。此前真实wheel函数CPU实验验证了桥接数学，却没有验证真实包导入生命周期，此缺口必须修正，不能归因用户操作。

## 实施顺序
1. 冻结原始至step12；新step13整包，不覆盖历史证据。
2. 基于安装发行元数据区分HF与官方legacy。HF先检查受审版本/命名空间冲突，再显式importlib.import_module导入实际compat模块，验证注册并安装补丁；不能用“尚未导入”等同“不适用”。未知/导入失败明确阻断。
3. HF runtime预检必须完成真实Mimi CPU数学smoke；legacy不强行依赖HF5。所有模型入口继续复用同一桥接函数。
4. 新增延迟导入、导入失败、冲突、重入幂等、预检fail-closed测试；真实Faster和完整Qwen包不替换导入函数，CPU构造微型MimiModel走真实_init_weights路径，不下载完整模型/不冒充T4。
5. 三轮Python/Node/Go及协议、完整浏览器，实际包导入+微型Mimi三进程；保留初始失败。三轮各100项范围复核，不把目标22/300改成全部实现。
6. 更新真实复制页/完整交付/33备忘录与12题600建议；验证原始至step12和正式工作台只读不变。

## 验收与边界
HF存在但compat未载入不能再跳过。成功要求step13 CPU真实包导入后桥接installed、实际Mimi实例初始化成功，及既有功能回归通过。真实双T4完整1.7B加载、CUDA graph、显存和声音仍需Kaggle实跑；无法保证平台永久驻留。下一步应直接复跑step13，非要求用户再做准备开发。
