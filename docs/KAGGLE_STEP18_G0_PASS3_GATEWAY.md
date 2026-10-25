# G0 全源第三遍第6批：网关调度、LLM 流与文本保留

日期：2026-10-23；活动分支 `arena/1160bd87-kagglee`。

**第三遍累计48/53份、11030行，剩5份2638行。前两遍各53/53份、13668行保持；产品未改，G0与整体仍PARTIAL/BLOCKED。** 全文语义阅读、原建议最终处置、功能修复和真模型/声学验收是不同门禁；53资产不代表整个Git仓库审计。

## 1. 新增完整复读10份2110行

| 文件（相对 kaggle/source/go/gateway/） | 行数 | 重点 |
|---|---:|---|
| fidelity_test.go | 187 | 原文/复制相关源文字合同、首块预算、即时首前缀、真实本地SSE→首worker请求先于尾部 |
| go.mod | 3 | 无额外模块依赖；兼容版本与实际Go工具链分开记录 |
| llm.go | 137 | 请求/认证/预算、SSE增量与结束、EOF/错误/取消、非200正文隐私F30 |
| preflight_test.go | 67 | 已授权只读报告、大小/JSON边界、公开recorder静态白名单 |
| reliability_test.go | 159 | profile身份、激活后确认、LLM完整性、token预算、同源 |
| scheduler.go | 490 | FIFO/优先级、watermark、重试/已消费PCM、请求取消、帧终端/统计、health与EMA |
| security_test.go | 342 | token/重复header、已知/分块body预算、并发槽、截止/取消、proxy去秘密 |
| segmenter.go | 489 | exact/read/live策略、Unicode/小数/闭合引号、文本分组、暂停/seed/flush |
| segmenter_test.go | 123 | 分段稳定、保字/长度/小数/呼吸/清理旧合同的实际边界 |
| voice_binding_test.go | 113 | 内容pin/文本/语言/生成参数跨语言、trained模式与read/chat分离 |
| **合计** | **2110** | **10份全文，无本批源阅读截断** |

scheduler连续1–245/246–490，segmenter连续1–245/246–489，其余全文。辅助旧测试一次组合输出截断，不计辅助测试完整阅读。Go main/security/session三份已在第三遍输入批计信用，本批虽编译/调用及读取必要上下文，不重复加信用。8920+2110=11030；13668−11030=2638。余5份是web/app.js1715、index.html144、recorder.js358、LICENSE201、MEMO220。LICENSE未来阅读不代表法律签收。

## 2. 新增12个Go合同：10保护＋2未修观察

文件：`kaggle/tests/pass3_gateway_boundaries_test.go`。只复制到忽略缓存的SHA匹配Go源树编译；产品目录不加入测试、不改产品。使用原Go方法、真实本地HTTP和控制流；LLM/provider、worker、PCM、stats、认证材料明确是合成fixture，不调用真实DeepSeek、不生成真实人声。

| 新保护 | 实际检查与边界 |
|---|---|
| chat请求完整性 | 原Session.produce→StreamLLM保留自定义system、两条history及当前user顺序，传model/8192/stream/合成Bearer；原前缀形成job，提交完成；不是真provider输出预算/质量证据 |
| 缺LLM key | 原StreamLLM在任何HTTP与delta前返回错误；fixture服务调用0，不要求用户提供秘密 |
| SSE边界 | 心跳/comment/非data行、role-only delta、CRLF、Unicode、最后无换行的DONE/stop均按预期解析；不签收所有SSE扩展/任意代理行为 |
| SSE错误脱敏 | 合成error.message或坏JSON不进入错误文本，已收到原始前缀不改写；仅流内错误，不修非200正文F30 |
| 多语种read原文 | 中文/组合字符/astral emoji/URL/双空格/换行/12.50，1/2/7/4096 rune切块后逐字相等，索引连续，重复Flush空；特意不含独立无词尾段，F39另列 |
| pause/seed | profile pause超界正确钳制；同seed17的read分组/暂停/元数据在1与4096切块下相同；不是自然韵律或跨GPU音色相同证明 |
| retry预算 | 真HTTP429正文限400字节，attempts=2时不再排队，failed1/served0、busy恢复、错误有界、healthy不盲改；不解决原frame/状态缺口 |
| urgency/FIFO | 原Submit/pickLocked跨会话优先urgent/first，平级按seq稳定FIFO；未Start无限health/ticker，不作吞吐测量 |
| 统计EMA | 原run对合成正数统计更新rtf2→2.6、first100→130、audio3→5，增加attempts/queue_wait并计2个PCM样本；合成audio_s与PCM长度并不对应，不称RTF一致性已验 |
| synth参数转发 | 原run首块opt-in2、后续6，保留seed91/pin/conditioning/语言/原字/停顿/呼吸字段；只是请求转发，不能证明真实首声提速或允许拼参考PCM |

### 首错与纠正均留档

首次Go预检在编译阶段失败：测试误写`session.submitted`，实际字段为`allSubmitted`；未执行任何测试。仅改该测试断言字段后，12项race预检通过，无产品修改。`pass3-gateway-precheck-first.txt`、`precheck-correction.json`、`precheck-final.txt`保留。

另一次内联审计元数据命令因findings字典括号混写而SyntaxError，整段解析失败、没有写文件或推进coverage，不影响后台回归。已拆成显式credit脚本和字典构造，记录在`pass3-gateway-metadata-correction.json`；不改写历史。

## 3. F39：PreserveText仍丢独立标点/空白尾段（未修）

原`Segmenter.finish`无论PreserveText是否true，都会以hasWord=false丢弃无词组。实际LiveSegCfg、逐rune馈入、原Flush下四个稳定见证：

| 输入 | 重连全部seg.Text |
|---|---|
| `你好。!?` | `你好。` |
| `你好。\n\n` | `你好。` |
| `\t\n` | 空 |
| `!?` | 空 |

前两例即时首前缀已发后，剩余独立无词尾段被丢；普通带词内容内的标点并非全部被删除。确认的是“PreserveText/重连逐字相等”合同缺口，**不是漏读语词、沙沙、接缝或真实声音质量下降的证明**。本批没有修改分段算法。未来需明确无损展示文本与可朗读分组的关系，不能用丢标点后的重连声称原文完全保留，也不能为了保字随意增加模型朗读内容。

## 4. F40：cancelled worker统计在活ctx下仍计served（未修）

真实本地HTTP worker替身返回一个合法偶数字节PCM帧（2个合成样本），随后stats包含failed=false/cancelled=true。原`Scheduler.run`只拒绝failed=true，没有拒绝cancelled=true：会话ctx仍有效、buffer done=true/error为空、worker served=1/failed=0、busy恢复false。新测试直接断言这些原始状态，三轮一致。

**worker、PCM和stats为fixture，不是生产worker真实取消、CUDA仍运行、漏音或成功播报取消任务的证明。** 本批继承的实际请求ctx取消→worker取消保护仍通过；该保护不覆盖worker自己报告cancelled但请求ctx仍有效的状态组合。未来应校验终端状态一致性，连同F03奇数PCM/空stats/非法错误JSON/残帧等统一考虑，不靠“served计数变绿”验收生成。

## 5. 三轮完整执行矩阵

| 每轮Go race集合 | 顶层通过 | 含子测试通过 |
|---|---:|---:|
| 原产品测试 | 40 | 56 |
| 原G0合同 | 10 | 10 |
| 第二遍gateway合同 | 13 | 13 |
| 第二遍security合同 | 12 | 12 |
| 第三遍input合同 | 6 | 6 |
| 本批新gateway合同 | 12 | 12 |
| **每轮合计** | **93** | **109** |

三轮均 **93/109 PASS**，合计顶层279次、含子测试327次，正常集合意外失败/skip/race为0。比对前第三遍input批81/97逐项测试ID，确保原前缀先发、原文、消费后不重试、pin/同seed、认证/取消等既有合同实际继承，不只比较总数。新10保护×3＝30次，2观察×3＝6次；观察通过表示缺陷仍可见，不是修复成功。

- **F02故意race见证独立执行三次，均预期非零并出现DATA RACE。** 不混进正常通过数，也不隐藏为“全无race”；map alias race仍未修。
- Go vet三轮exit0；实际Go1.23.9，GOTOOLCHAIN=local/GOPROXY=off，不下载新工具链或模块。SHA核对13份复制原Go文件与6个外置探针；本批阅读新增仅10份。
- CPU完整继承集合每轮426、共 **1278 PASS**，失败/错误/skip0；**本批没有新增Python合同**，原414+12来自前批。包括F31–38等CPU观察/自有进程/OFD/C ABI故障fixture，但不是模型训练或Rust实测。
- 每轮另NumPy分块12、trimmer8、实际CLI4；三个CLI期望blocked/exit2，resource status exit0但gpu_verified=false。合成分块差异观察没有变成去沙沙或跨后端容差通过。
- 单次新执行Node30、工作台及产品web JS语法、Python AST38、新Go测试gofmt、repack --check。没有本批真实浏览器/VM或独立ASGI2.3 companion；Node不代替浏览器复制/录音/排空验收，冻结网页字节保持不等于浏览器重新测试。
- .venv/系统无新依赖，freeze与前批相同，NumPy2.2.6不冒称requirements2.4.6。继承CPU集确实再次编译并加载微型C ABI故障库；无cargo/rustc/Torch/Qwen/CUDA、Rust编译/运行、真训练、真实音频播放或提速测量。

## 6. 完整性、建议处置和交接

- 批前保存953份历史SHA；原53源/94冻结/15正式工作台、原17包及先前收据保持。产品diff为空，不生成18包。
- coverage以逐文件SHA/行数核对新增10/2110，48/53/11030，剩5份2638；前两遍不改。未全三遍，不提前签收G0。
- 原300本批7部分链接：R1-048/083、R2-050/053/084、R3-008/066；累计去重38个ID。链接含本批与明确重新执行的旧Go合同，不冒充7个新发现；原文、Q25–27各50项保持，逐条/最终处置均false。
- 独立`verify_pass3_gateway.py`验证历史SHA/冻结、逐文件信用、Go JSON事件与ID继承、两新观察、F02预期race、vet、426项CPU逐项继承、探针/CLI、环境/manifest、原建议及全部交接嵌入。
- 完整交接86份备忘录逐份匹配，PLAN/IMPLEMENTATION与最新状态同步。manifest排除自身/可变handoff与progress，后者由独立核验另验，避免循环哈希。

主要收据：`docs/validation/step18/pass3-gateway-round1..3.json`、`pass3-gateway-cpu-round1..3.json`、`pass3-gateway-companions-round1..3.json`、`g0-pass3-gateway-{coverage,findings}.json`、`pass3-gateway-recommendation-links.json`、`pass3-gateway-run-manifest.json`、`progress-pass3-gateway.json`。最终封存以独立核验成功日志为准。

## 7. 下一步精确行动（待实施）

1. 全文复读web三资产2217行，分段读app.js不得以语法检查代替语义阅读。
2. 在SHA匹配fixture环境重新跑真实浏览器录音/取消/复制/排空/迟到响应合同，不挪用历史成绩。
3. 对F39明确原文展示/模型分组分层政策，构建纯标点/纯空白/尾段/即时首句组合合同；不得无依据加读字符。
4. 对F40明确ctx取消、worker cancelled、failed和正常终端的优先级与错误语义，避免重试已消费声音。
5. 继续保留F02/F03/F23/F24/F29/F30等旧缺口，修复时不能因本批其他保护通过而删除观察。
6. 保留第一可用DeepSeek前缀立即发worker请求的原保护；实际首可用人声仍需模型/浏览器测量。
7. 保留相同seed/pin与generated-only路径，不用合成stats或参考PCM证明双GPU等效音色。
8. 全文复读LICENSE/MEMO 421行并分别记录许可/技术限制；完成53资产也不自动完成原300逐条最终映射。
9. 原300和Q25–27建议按实际发现闭环，重大设计选择才开下一问题，不为编号制造问题。
10. 全部G0门禁通过后才进入S1，保持原17/正式工作台冻结，不提前发布18。
11. 真训练、长录音/完整数据覆盖、双T4、相似度、自然连续声音和无沙沙等用户要求继续列缺口。
12. 真实首声/建档延迟/RTF0.3须在固定条件下三轮真实模型和听感验收，当前不承诺结果。

**结论：第三遍阅读与Go边界核验推进；F39/F40未修，F02等旧缺陷保留。G0与整体仍PARTIAL/BLOCKED，非全功能或声学签收。直接继续下一批，无需Continue。**
