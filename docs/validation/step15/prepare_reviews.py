"""Record three topical reviews before product edits. Inventories are not semantic proof."""
from pathlib import Path
import ast, hashlib, json
R=Path(__file__).resolve().parents[3];D=R/'docs';S=R/'kaggle/source'
rounds=[[
('worker.RealEngine', '禁止参考码进入解码器；仅以说话人向量条件生成；生成调用不传参考正文；预热采用相同向量模式；dtype回退后仍用向量模式；不开放环境变量回退ICL；明确韵律相似度可能变化；核对Faster0.5.4实际源码；生成采样率仍严格24k；生成器取消时仍close'),
('worker.lead_audio','废止reference呼吸拼接开关；前置停顿仅零样本；旧breath_files不能被读取；无参考片段也不造噪声；保留模型自身呼吸；不把去呼吸等同自然音色；暂停最长仍1500ms；负暂停仍归零；随机种子不能改变静音；人工试听仍是门禁'),
('worker.run_job','PCM来源只接受模型和零停顿；不因模型失败回放anchor；不因空结果播放参考；保留nonfinite拒绝；保留异常统计；保留裁边；保留尾部淡出；保留取消检查；保留每GPU互斥；日志报告生成隔离模式'),
('adapter_engine','核对原生向量模式；不能把训练参考当输出；固定adapter哈希；损坏adapter不能回退Base；不改变句级缓冲标记；不混驻两种引擎；保持取消丢弃迟到wave；训练候选不自动激活；新进程重载仍需实机；无训练证据不称已训练'),
('朗读内容','不拼接参考文本；不修改目标文本；不补额外说明；不以字符串一致冒充声学一致；不自动删数字；不自动删专名；不裁词谋求首声；短句仍需语言条件；模型幻觉单独披露；严格ASR拒播仍未实现'),
('PCM隔离回归','以非零参考bank诱捕混入；旧环境reference模式也应静音；断言生成xvec_only为真；断言参考正文为空；预热断言与生成相同；加载不得读取呼吸文件；输出频率标记与参考分离；完整协议中仅模型PCM；失败流不得补参考；重复三轮隔离验证'),
('音量','新旧档案统一输出目标；默认目标从负21到负18dBFS；保留可调输出目标；合法范围负24到负14；非数字回退默认；NaN回退默认；正无穷回退默认；不修改原始录音；保持软限幅；不承诺所有音量都增加3dB'),
('DSP质量','验证低电平正弦增益；验证满幅输入不溢出；保留DC blocker；保留段间淡入；保留尾部淡出；Rust与NumPy参数相同；不新增C++重复实现；采样率不降；不硬裁削峰；测量使用非语音时标明合成'),
('GPU显存','1.7B FP16权重估算约3.4GB；两模型权重不是全部显存；计入codec和speaker；计入KV cache；计入CUDA graph；计入分配器碎片；同卡并发争计算带宽；不默认每卡两模型；以两卡各一模型为基线；真双副本收益必须实测'),
('所有权与安全','保留单可见GPU契约；不绕过fleet租约；不删除锁；不按旧PID杀；不安装未知CUDA补丁；不输出口令；不保存用户参考到报告；不自动上传录音；不更改已冻结14；保持3000正式工作台')
],[
('首段分段','识别当前末尾标点等待lookahead；只为首段新增即时确定边界；句末中文标点可立即提交；逗号达到首段预算可提交；ASCII点仍等lookahead避小数；保留后续正常分段；新段保留原文；不等待LLM全篇完成；不为每token发TTS；短于常规阈值完整句可首发'),
('单位边界','英文单词不从中间拆开；小数12.50不拆错；英文缩写保留；标点后引号不能丢；跨delta空格仍保存；纯标点不能伪成语音；Unicode原样；组合emoji不作为词；无标点长句保持上限；最后残留仍Flush'),
('顺序保护','首段任务优先；第二段可用另一GPU；已输出失败不重放；未输出失败才允许重试；保留段索引；保留背压高低水位；保留迟滞；不无限预生成；取消移除排队任务；健康检查不回放参考'),
('LLM流','保留每delta向前端推送；首句完成即submit；首token计时保留；首段提交计时保留；LLM完成计时保留；非法JSON报错；截断finish_reason报错；取消终止HTTP；不记录API密钥；用本地SSE延迟尾巴测试'),
('首声指标','区分首token和首段；区分模型首块和PCM；区分首PCM和首播；静音不当作人声；保留欠载次数；不以网络替身称DeepSeek实测；不以MockRTF称QwenRTF；记录首段早于LLM结束；没有CUDA不填GPU延迟；不承诺三秒内'),
('播放器','先不盲降全局缓冲；保持starved恢复阈值；保留短尾完成后启动；停止重置ring；迟到PCM不继续播放；初始化失败可重试；保留浏览器重采样；不将gain无限放大；不新增播放参考audio标签；保持手机布局'),
('首块预算','保留默认chunk4稳定策略；允许显式2到8试验；无效环境回退4；后段按背压选择；不把chunk2必然称更快；重测小chunk欠载；记录同文同参考条件；预热成本单列；不改变max_new_tokens掩盖；单句质量需真人听'),
('线程与语言','Go保留调度路径；Python保留模型接口；Rust保留DSP；JS保留播放；不新加Java网络服务；不为多语言复制采样器；不盲开每卡双进程；不启用不支持的BF16；不将TF32称T4加速；量化质量另实验'),
('流式测试','首句单delta即可产生任务；短中文完整句可首发；ASCII数字点仍保留；逗号完整前缀可首发；相同文本各切片重组；新特性用应用配置而非旧配置；晚引号仍完整保留；SSE未结束worker已收到首段；最终按索引输出；Go race三轮'),
('退化防护','非首段旧策略不变；朗读长文不丢段；URL不清洗；DeepSeek错误前缀可见；超时不冒成功；取消不重复提交；独立记录早期失败；浏览器全量回归；Python全量回归；无硬件保持部分验收')
],[
('创建默认','默认关闭可选GPU候选校准；保留手动校准按钮；直接创建与库处理默认一致；后端缺省也关闭校准；锁定重置默认关闭；明确不是训练；不隐藏校准质量代价；保留两卡预热；失败不改active；完成收据不虚报'),
('ASR成本','已知单段短文本直接使用；不能把长文本套短片；保持全量长音频ASR；不取前十秒冒充完整；CPU Whisper可驻留复用；不在GPU常驻ASR；保留CPU回退；保留识别beam5；保留词时间戳；记录手动转写绕过ASR'),
('ASR内存','仅CPU默认驻留；CUDA ASR仍卸载；显式开关可禁用驻留；同一重模型入口串行；不无限缓存音频；不缓存每个用户转写；不让驻留伪造模型已加载；首次下载成本单列；CPU内存风险披露；不以第二次速度代表冷启动'),
('重复计算','档案内部嵌入按内容哈希复用；嵌入缓存仅本次任务；返回向量保持只读语义；不跨档案泄漏用户数据；记录embed实际调用数；记录embed命中数；候选相同波形可复用；不按文件名猜相同；不改变候选排序公式；缓存失败不写半成品'),
('CPU候选','保留24候选上限；保留前三非重叠；保留SNR打分；保留典型性中心；保留F0打分；准确F0仍用于最佳锚点；不偷偷换MFCC冒充ECAPA；不降采样输入标准；不减少可用文件；不承诺质量无损提速倍数'),
('分析阶段计时','记录speaker加载；记录解码降噪；记录ASR；记录候选评分；记录呼吸韵律；记录worker加载；记录可选校准；记录总构建时间；成功后最终写回profile；旧calibration写回不能覆盖'),
('候选转写','长单个ASR段不能截音频保留全文；长度超界无可信字时间拒绝；不猜均匀对齐；提示重录短段或审核切分；手动16秒整段可不裁；候选start/end匹配实际波形；保留多文件来源；检查负时间；检查超音频边界；不静默截断转写'),
('持久化','完成前写回quality.build_s；持久化stage_ms；持久化嵌入缓存统计；失败不删除已有档案；新任务失败清理新目录；保持原子JSON；保留worker_load状态；保留校准选择；不把done当两卡加载成功；文件备份范围清楚'),
('发布交付','生成新step15不覆盖14；新增manifest逐文件校验；复制页固定15哈希；下载与剪贴板完整一致；拒绝剪贴板时可全选；375px无横向溢出；冻结正式15文件；交接完整嵌入新增备忘录；三轮结果分别记录；未通过项目不得打勾'),
('现场门禁','用户截图256.4秒仅作问题证据；无原音频不能确定泄漏根因；真实Qwen生成必须试听；真实T4显存峰值必测；同卡双模型不默认试；首次和热创建分别测；同参考同目标文本比较；无额外参考重播需独立检查；历史网页训练缺口仍保留；不写100%无错误')
]]
manifest=[]
for i,groups in enumerate(rounds,1):
 records=[]
 # Read every current source file in each pass; compile syntax, inventory all languages.
 for p in sorted(S.rglob('*')):
  if not p.is_file() or any(x in p.parts for x in ('state','__pycache__','target')) or p.name=='gateway':continue
  b=p.read_bytes()
  if p.suffix=='.py':ast.parse(b)
  records.append({'path':str(p.relative_to(S)),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
 lines=[f'# 第十五阶段第{i}轮专题审查：100条建议','', '全源文件读取/哈希与Python AST巡检不等于逐行语义正确证明。重点调用链经过人工分析；建议不是100项已修复。处置与实测边界见AUDIT。','']
 entries=[]
 for anchor,raw in groups:
  values=raw.split('；');assert len(values)==10,(anchor,len(values))
  for v in values:
   ident=f'S15-R{i}-{len(entries)+1:03}';entries.append((ident,anchor,v));lines.append(f'{len(entries)}. [{ident}] `{anchor}`：{v}。')
 assert len(entries)==100
 (D/f'KAGGLE_STEP15_REVIEW{i}.md').write_text('\n'.join(lines)+'\n')
 manifest.append({'round':i,'files':records,'recommendations':100,'entries':entries})
(R/'docs/validation/step15/review-before.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
# Sequential professional questions; each has a choice, concrete rationale and 50 actions before next.
questions=[
('16','怎样让参考录音只能提供音色，不能进入输出波形？','A 继续ICL并裁参考波形；B 仅说话人向量且停顿纯静音；C 先生成后整句ASR拒播。','B','先取说话人向量，生成与预热均xvec_only=True，ref_text为空；禁止参考呼吸拼接和旧环境开关。A依赖裁切且参考码参与解码，不满足强隔离；C延迟更高且ASR不是真值。B会改变韵律/相似度，必须实机试听，不承诺模型不幻觉。',0),
('17','能否通过每T4放两个1.7B来降低首声？如何在不破坏朗读内容时早发第一段？','A 每卡双副本；B 每卡一模型，首个确定语义边界即提交；C 每token一个TTS任务。','B','FP16纯参数约3.4GB/份，双份约6.8GB不是峰值显存；codec、KV、graph及临时张量另占内存。同卡副本共享同一计算资源，单请求不自动变快。保留两卡两模型并行相邻段；首个完整中文句或足够长逗号前缀无需等下一delta，英文点仍保留lookahead。保留播放器抗欠载策略。',1),
('18','创建档案怎样提速而不偷偷减数据或伪造训练？','A 默认省掉所有质量模型；B 默认延后可选GPU校准，复用CPU ASR及本任务重复嵌入，分阶段计时；C 只处理前十秒。','B','保留完整数据ASR、24候选评分和准确最佳锚点F0。可选校准移至用户显式调用；CPU Whisper可复用，CUDA ASR仍卸载；同任务嵌入内容去重。首建仍可能受下载和CPU大模型限制，不预设提速倍数。阶段收据必须最终持久化，长ASR段无可信对齐不能截音频配全文。',2)]
p=D/'KAGGLE_DECISIONS.md';text=p.read_text()
for number,q,opts,chosen,answer,r in questions:
 text+=f'\n\n## 问题{number}：{q}\n\n具体选项：{opts}\n\n最推荐：{chosen}。\n\n回答及追问结论：{answer}\n\n落实到后续代码的50项建议（本题结清后再进入下一题）：\n\n'
 for n,(ident,anchor,v) in enumerate(manifest[r]['entries'][:50],1):text+=f'{n}. [{ident}] 在`{anchor}`落实：{v}；用相应自动回归或明确现场门禁检查，不以建议数量当修复数量。\n'
 text+='\n结论：已足够确定本轮工程取舍，无需向用户追问；真实声学质量和T4性能只能保留待测，不声称100%信心。\n'
p.write_text(text)
print('3 reviews x100; Q16-18 each50; pre-edit inventories recorded')
