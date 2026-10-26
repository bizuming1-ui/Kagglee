# 完整 Kaggle 候选源码交付：现存 S5 的实际接线与独立打包

## 交付结论

已生成完整可运行入口源码，而非零散补丁或只有报告：

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `kaggle/delivery18/artifacts/kaggle-step18-candidate.py` | 286135 | `f54346e232b44750f77c506bc9cefd155edd809c0f7444092621fc7b0bb4fab7` |
| `kaggle/delivery18/artifacts/kaggle-step18-full-source.zip` | 432569 | `1559b70d7451736fef4d288539dadf465d15e8a266864167612e0fd628970243` |

ZIP有61成员：58个可读源码资产＋同一完整单文件入口＋中文README＋MANIFEST。单文件内嵌全部58资产（611276B未压缩），不依赖GitHub在线拉源码，不包含模型/依赖wheel/用户数据，不是离线安装包。SHA只检查一致性，非身份认证。

本批 **源码交付/CPU-MOCK接线范围完成；完整产品仍 PARTIAL/BLOCKED**。不承诺一定在未测的Kaggle双T4环境成功，不签收实际训练、音色、噪声、首声或RTF。

## 必须纠正的实际工作区状态

开工实查：当前可读文件只到S5，现存完整交接111份、SHA `3f8f70f0001b956b876bd32c781cc8f5b8b81da40d231554498a0e14411887c5`。会话中提到的S6–S8-C相关代码、alpha ZIP及收据现在不在磁盘，原因未确定。不能继续声称它们已在当前交付中，也不能把凭记忆重建称作原封存文件。

`docs/validation/step18/delivery/baseline.json`逐项记录已确认缺失的关键路径及会话中的旧alpha预期SHA，**不补造其字节或验证收据**。这次明确从可核验S5创建新候选，不叫“S8-C恢复版”，不包含缺失的S6时序、S6D检查点、S7配对器或S8C终态收据overlay。

现存S5独立verifier开工、收尾均成功且输出一致；开工3071现存文件逐项SHA保持，没有删除旧证据、改写正式17/工作台或覆盖现存候选源码。此前说过的完整历史保护数不能用作本次当前文件数。

## 实际修改与接线

新 `kaggle/delivery18/build.py` 是确定性构建器，读取冻结17 FILES和清单但不执行其旧启动器。原53资产保持完整，增加5个候选依赖，共58：

1. 包内 `py/analyst.py` 真正采用当前S1/S2分析服务；输入、校准快照、有效指标三个模块同目录附带。
2. 包内 `py/worker.py` 真正采用S4 worker；因果NumPy DSP与有界trimmer两个模块同目录附带。
3. 包内 `web/app.js` 真正采用S5完整Player/Worklet；录音器、UI后缀、鉴权和网络接线保留。
4. 只在新包bootstrap中替换 `build_rust()`，不再安装/编译未验收Rust，使用已验证的numpy-causal-v1；其他函数AST与冻结bootstrap保持。
5. 新包MEMO替换陈旧历史首页，明确本候选范围；训练、录音、profile、Go、备份等原源码仍在。

原文件全部不改；新入口默认只check，--extract-only不安装/读取Secrets，--doctor只查硬件库存。只有显式--run在两个独立物理T4库存门禁通过后才创建全新目录、读取Secrets并进入原bootstrap。MOCK/单GPU豁免环境拒绝，不偷偷降级。完整JSON长度/SHA/有限解压预算校验在创建目标前；新目录排他写、700/600，不覆盖已有或符号链接目标。

新入口不声称已有S8C的失败终态能力；仍继承bootstrap/supervisor的未修限制。bootstrap返回ready也不是训练成功或四服务已停止。完全不可写、取消、掉电、输出丢失、部分解包失败和新目录残留未承诺完整事务恢复。

## 本轮三轮正式实测

| 类别 | 第一轮 | 第二轮 | 第三轮 | 边界 |
|---|---:|---:|---:|---|
| 新完整包装/入口单位合同 | 36 | 36 | 36 | 同版完整单文件与ZIP |
| 继承S5完整CPU合同 | 610 | 610 | 610 | 冻结/候选混合原目标，不是610项新功能 |
| Player/Worklet VM专项 | 37 | 37 | 37 | 合成时钟/端口，已被CPU源合同调用，不相加 |
| Node服务回归 | 30 | 30 | 30 | 原工作台服务 |
| 包内实际Go正常测试顶层 | 40 | 40 | 40 | 含子例56 pass事件，非额外56项；未跑race |
| 包内Python AST | 38 | 38 | 38 | 其余含Go/JS/Rust/许可证等 |
| 独立新解包＋实际四程序联通 | 通过 | 通过 | 通过 | 真实Go＋两个CPU MOCK worker＋Analyst |
| doctor / 显式run硬件门禁 | 2 / 2 | 2 / 2 | 2 / 2 | 缺nvidia库存，未建runtime，预期blocked |

失败/错误/skip均为0（上述正式类别），模型实际运行次数0。本轮完整CPU610确实重新执行，输出另名，不挪用或覆盖原S5日志。原173浏览器本批**没有重跑**，只保持旧源码和封存证据；本轮37是Node VM，不是原生声卡/浏览器或物理音频测试。

### 最终包内四程序真实接线做了什么

每轮从最终单文件独立解出完整树，使用第三方PyPI go-bin1.25.3实际离线编译其中Go源码（GOPROXY/GOSUMDB关闭），启动两个实际worker.py、实际Analyst、真实网关，验证：

- worker明确engine=mock、model_loaded=false、rt=numpy-causal-v1；Analyst明确mock。
- 无token API为401；初始profiles为空，没有强制声音预填。
- 网关实际返回的整个app.js与S5候选逐字节一致。
- 在自有临时树创建明确的合成profile/WAV，真实网关调用两worker加载；两个实际worker各输出有限非空偶数字节PCM及stats；Go /api/speak真实协议有PCM/结束帧、无错误帧。
- 所有音频为MOCK合成数据，不是用户语音、不是模型、不是训练；不保存这些PCM或私有状态。
- 四角色唯一PID，审计实际wait回收并以pidfd观察退出。退出-15是审计主动TERM，不是产品崩溃或真实停止UI验收。只处理自有进程组，没杀任何按名称猜测的外部进程。

预检36与一次四程序预检均通过，原样保留；没有失败通过放宽断言藏掉。一次工具定位使用 `import go_bin` 得ModuleNotFoundError，已改用实际已发现的Go二进制路径；这不是包装或回归失败，不把该包当Python运行依赖。CPU依赖按现存S5 freeze重装，新增go-bin1.25.3并保存当前freeze；Go来源为第三方PyPI，仅记录版本/执行证据，未独立验证官方签名。没有安装Torch/Qwen模型或运行真实GPU。

## 三审100×3的处置

Q42选择独立完整包，50行动已保存；三审不是300个修复或原300综合签收。各份同编号组：

- 001–010：S5 seal＋3071保护；后期缺失明确记录，不冒恢复。
- 011–020：58资产来源清单、三入口实际替换；训练/备份代码保留，许可证不是完整授权清关。
- 021–030：单位01–16验证完整性、确定性、坏编码/截断/尾随/解压预算；默认check无副作用。
- 031–040：单位17–22，新目录/符号链接/权限/已有内容保护；无掉电事务承诺。
- 041–050：单位23–30和真实CPU门禁三轮；物理库存正向只做定点模拟，不能冒称真正T4。
- 051–060：bootstrap仅Rust函数改变（单位33），继承平台Torch策略；CPU freeze明确非GPU锁；签名/安装供应链不签收。
- 061–070：三次最终包实际Go＋四程序联通与合成协议；actual model字段false。
- 071–080：36/610/37/30/40分别三轮，旧日志不覆盖、四进程wait/pidfd；没有将VM/MOCK冒声学。
- 081–090：完整单文件和可读ZIP、MANIFEST、确定性SHA、中文Kaggle命令、训练备份源码路径；非离线安装、非远程部署。
- 091–100：三审建议与原300区分，真实门禁保留；双独立seal后交付，不承诺必成。

## 直接使用

详见 `kaggle/delivery18/README.zh-CN.md`（ZIP内也有）。将单文件放到Kaggle实际可读路径，Settings选GPU T4 x2、Internet On；示例文件位置为 `/kaggle/working/`：

```python
%run /kaggle/working/kaggle-step18-candidate.py --check
%run /kaggle/working/kaggle-step18-candidate.py --run --destination /kaggle/working/qtts18-new
```

如来自 `/kaggle/input/...`，改前半文件路径即可；目标仍在可写working中。目标必须全新；不要删旧锁强行启动，不覆盖旧声音数据。整段粘贴默认只检查，需要同一单元格/下一格 `main(["--run", "--destination", "/kaggle/working/qtts18-new"])` 才实际启动。

原UI鉴权和私有token政策保留，Secrets只在显式run读取，值不打印。不要分享token/原始私有日志。训练代码存在≠默认建档就是训练；不拼参考PCM增加相似。

## 未完成、下一步和完整交接

真正双T4与两个模型、超过10分钟实际录音/训练按钮/优化器/同质量加速、自然音色无嘶声逐字、真实DeepSeek首前缀、实体首声<3秒/RTF≤0.3、Kaggle安装/许可/备份恢复和历史缺口/原300最终签收仍未完成。原300最终仍0，没有可信总体百分比或完工日期。

本次包可供用户实际尝试，不是假装已完成远程Kaggle运行。下一步应收集本候选在真实双T4的受控启动/生成证据，再判断具体失败点；不能由截图猜噪声根因，也不能用CPU图表许诺声音一定相同。

新证据在 `docs/validation/step18/delivery/`，新进度 `progress.json`、双seal `verification-first.json`/`verification-second.json`、清单 `manifest.json`；旧progress-checks仍保留S5，不伪写历史。独立完整交接 `docs/KAGGLE_STEP18_DELIVERY_HANDOFF.md` 保留旧111备忘录全部原文，再附本批Q42、三审与本报告，共116备忘录；不是恢复缺失的156交接。
