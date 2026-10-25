# Notebook 参数精准修正：Colab / Jupyter 的 -f 连接文件

## 根因与改动

用户日志入口为 `colab_kernel_launcher.py`，带 `-f ...kernel.json`。旧入口只识别ipykernel_launcher两个名称，导致Notebook整段粘贴走普通CLI，argparse实际报unrecognized arguments并退出2。已在修改前用同形状合成路径复现，留存 `notebook-fix/original-colab-red.txt`；未读取用户连接文件。

新文件位于 `kaggle/delivery18/artifacts-notebook-fix/`，**不覆盖原交付**：

| 文件 | 字节 | SHA256 |
|---|---:|---|
| kaggle-step18-candidate.py | 286755 | `95b8130bf8761eafef66dd0bb29068f97186d3088fbc6fe5aefa7f41b9820214` |
| kaggle-step18-full-source.zip | 433190 | `bad31f102ab57d0fce6fcad49eda8f0022b4966c190d97267707534f969a1879` |

新增 `_is_notebook_kernel_argv(argv)`：只认Colab/Jupyter各带.py或不带.py的四个精确入口名，以及无参数、`-f PATH.json`、`-f=PATH.json`三种形状。只有完整代码直接粘贴的内核调用默认check，且不抛SystemExit(0)产生退出提示。

**不清空全局sys.argv，不用parse_known_args，不无条件忽略-f。** 普通CLI、IPython `%run`、显式main参数继续严格校验；未知/额外参数仍退出2。比如内核形状后再加--run不会被偷偷执行。IPython `%run script.py --extract-only ...`不被误识别为内核，正常解包。

旧所有命名函数（包括main）AST不变；嵌入的58个运行源码资产与ZIP source/*逐字节不变。只增加内核调用识别并修改最末入口分流，ZIP说明/清单同步。原54项交付清单、原3071保护文件及旧完整seal保持通过，原单文件SHA仍为f54346e232b44750f77c506bc9cefd155edd809c0f7444092621fc7b0bb4fab7。

## 新验证

- 新入口36合同 ×3 全通过：四种内核入口、完整文件exec、严格CLI、实际解包、真实CPU环境doctor/run阻塞、AST/58资产一致性、确定性ZIP和旧54项保护。
- 每轮包含**实际IPython 9.17.1**执行Colab/Jupyter形状整段粘贴，以及实际 `%run --check`、`%run --extract-only`；不是只给检测函数喂名字。测试运行时Python3.11.2，不冒称已在远程Colab Python3.12运行；3.12目录名的用例只是argv路径形状。
- 本地真实Chromium三轮：输出框完整286755B SHA一致、原生剪贴板完整文本一致、实际下载一致、模拟剪贴板权限拒绝时全选范围完整。
- 首次浏览器预检因缺libnspr4等NSS库未启动，失败日志/当时测试源码gzip保留。复用已有playwright.config.js附带库/启动参数后完成三轮，不修改产品或放宽复制断言。
- 实际运行入口与doctor每轮在当前无GPU环境退出2/blocked，未创建runtime、不读Secrets或模型。此次模型验证为门禁，不是模型运行。
- 原610CPU/Go40/173浏览器本批未整套重跑；其旧证据保持，不能算成本轮新成绩。新增测试不等于完整语音产品验收。

测试依赖只新增IPython到忽略的venv；npm ci按旧lock恢复浏览器测试依赖，未改package/lock。新输出框服务器绑定0.0.0.0:8081，浏览器API使用相对URL。旧8080输出框停止以避免继续复制有缺陷版本；旧服务器源码/原代码文件保留。

## 复核与交接

Q43选C、50行动及三审各100建议在 `docs/KAGGLE_STEP18_Q43_NOTEBOOK_ARGV.md`、`docs/validation/step18/notebook-fix/reviews.json`。这些是首修预检后的复核，不冒称事前审查，也不是300个bug或测试。

各份建议按10个上下文（Colab/Jupyter四名、-f=、CLI、实际IPython和门禁）×10检查维度映射至36合同；源码一致性对应27–32，四种整段exec对应16–20，真实IPython对应33–36，CLI拒绝/副作用对应13–15/21–26。输出框额外三轮证明全文复制，无远程Colab或物理音频证明。

证据位于 `docs/validation/step18/notebook-fix/`，新清单与双核验绑定修正版、测试、原54项保护及浏览器输出。旧交付seal不重写。

继续提示词：仅本次Notebook参数修正完成；后续工作应从新修正版文件与本报告继续，不覆盖旧交付。可读基线仍S5，缺失S6–S8C未恢复，实际训练/双T4/音质/实体首声RTF/Kaggle或Colab实机运行均未验。此次修复不放松双T4门禁；Colab常见单GPU环境仍会blocked，不能把它误当同一个-f解析问题。整体仍PARTIAL/BLOCKED。

## 用户操作

使用新的“Notebook修正版·完整Kaggle代码输出框”复制整份代码，**完整替换旧单元格后重跑**，而不是只在报错后重复执行旧单元格。默认先出现source_verified_not_started；需要启动时另格明确调用：

```python
main(["--run", "--destination", "/kaggle/working/qtts18-new"])
```

该目录及GPU要求针对Kaggle；Colab实际目录布局可能不同，运行前需选择已存在的可写父目录。无两块T4仍会被门禁拒绝，不能用此兼容修正承诺完整运行成功。
