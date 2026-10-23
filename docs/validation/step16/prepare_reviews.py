"""Pre-edit topical review, decision trail and inventories. Not an exhaustive proof."""
from pathlib import Path
import ast,hashlib,json
R=Path(__file__).resolve().parents[3];D=R/'docs';S=R/'kaggle/source'
groups=[[
('参考条件','重新审视15强制向量模式；默认恢复匹配转写的ICL条件；无转写不得静默假设ICL；向量模式保留为显式选项；参考文本只作条件不拼目标正文；解码器不接参考码；保留原始参考录音；不把恢复ICL称相似度已验证；检查参考是否多人；多人参考必须换干净单人样本'),
('提示缓存','核查Faster路径键缓存；相同路径换音频必须失效；比较参考内容哈希；清除该路径旧缓存项；不删除模型全局权重；不信任仅profile_id相同；预热与生成采用同模式；dtype重载后重新构建条件；不把错误预热当就绪；缓存失效增加回归'),
('会话绑定','会话开始固定参考内容指纹；Go与Python指纹算法一致；包含WAV与匹配文本；包含语言字段；长度前缀避免分隔歧义；每个语段携带同一指纹；Worker取锁后重新读取档案；不同版本先拒绝后输出；不重试成另一个声音；缺文件不降级原模型'),
('双卡一致','保留每T4一个模型；比较两卡使用的参考指纹；保留同session条件不变；候选切换只能影响新会话；旧会话版本不符明确失败；声音更新与合成共用锁；锁后重取profile避免旧引用；不要以profile名称证明相同；不把RMS一致当同一说话人；两张卡实际试听仍必需'),
('生成稳定','相邻段使用稳定seed策略；不随意每段改变采样条件；不以降温保证身份；不默认删除情感；保留语言参数；保留max_new_tokens安全预算；保留取消后的生成器close；不引入随机参考混合；不混用候选锚点；不跨用户共享提示'),
('档案变更','修正候选更换原路径复用；文本更改触发提示失效；手动校准选择不能覆盖回旧；完成后保存阶段收据；删除档案不能被旧请求静默复活；不删除冻结15；旧档案可重新加载；参考需审核逐字转写；ASR提案不是人工真值；不从短片猜长文'),
('安全读取','锚点仅单一安全文件名；拒绝符号链接；拒绝目录冒音频；限制参考读取字节；路径始终在档案目录；哈希不输出原音频；指纹不是授权证明；不泄漏访问口令；不自动云传录音；保持私有备份边界'),
('原生adapter','保留训练候选固定binding；不向faster注入adapter；不修改训练权重；缺adapter不回退Base；保留句级缓冲标记；继续核对Base哈希；旧训练功能做回归；不要把参考处理叫训练；网页真实训练缺口保留；真实训练质量仍待验收'),
('相似度验收','相似度用真实说话人模型；不能伪造99.5百分比；文字一致不代表音色一致；多段输出分别试听；比较两卡相邻段；使用与参考不同的目标文字；同参考同文同seed对照；保留参考与输出独立文件；无用户音频不猜根因；不承诺100无错'),
('保护已有功能','保留原文分段；保留首句及时调度；保留两主视图；保留长录音预算；保留命名空库；保留失败本地片段；保留手动候选校准；保留DeepSeek取消；保留3000正式工作台；保留原始至15整包')
],[
('解码路径','使用实际Faster0.5.4准备接口；只解码新生成声学码；禁止参考PCM占位；不得猜比例裁参考音频；codec采样率必须24k；逐帧1920样本契约需检查；不兼容长度明确失败；保留码组16列；不偷改codec权重；API签名变化明确报错'),
('有界窗口','删除每块全历史cat；左上下文固定25帧；待提交尾部保留2帧；窗口随chunk有上限；新块仅输出未提交样本；提交游标单调；末尾只flush一次；取消不flush迟到音频；新旧窗口无重复样本；窗口长度记录便于核验'),
('块接缝','未来两帧降低边缘重解码差异；不对每块单独归一化；保留时间连续性；不要对每块强淡入；短于lookahead暂不输出；最后短块不能丢；音频总样本不缩水；不把重叠输出拼两次；真实边界爆音仍要听；增加右边缘不稳定fixture'),
('沙沙声','不生成额外呼吸噪声；旧breath环境不能启用拼接；限制向上增益防底噪变大；输出目标仍负18dBFS；保留软限幅；不默认强低通损坏齿音；不抹掉所有清辅音；不假装无声就是降噪成功；无原音频不确定噪声来源；分别检查模型原PCM与后处理'),
('响度状态','每任务重建leveler状态；防双卡历史包络不同；保留每段淡入淡出；无语音不flush上段尾巴；显式配置最大增益；非法增益回退安全值；新旧档案一致输出策略；不能靠过载变响；用低电平与满幅信号测试；Rust与NumPy分别标边界'),
('RTF定义','标准RTF等于生成墙钟除语音秒数；rtf_x是其倒数不是RTF；不把双卡速度相加冒单卡RTF；排除零停顿分母；失败取消样本不能算通过；冷预热与热态分开；首播与吞吐分开；记录每GPU结果；目标0.3需每条和汇总检查；无T4输出blocked'),
('计时拆分','模型prepare单独计时；token生成单独计时；codec解码单独计时；DSP耗时单列；总墙钟包括必要同步；不拿CPU异步发射当CUDA完成；预热不计入热态却单独报告；报告first_played与欠载；保存原始测量行；不删慢样本'),
('性能选择','仍用CUDA graph后端；不盲开torch.compile；T4继续FP16；不假称T4原生BF16；不为语言数量加网络跳转；不每卡塞两副本；上下文有界减少复制；参考prompt按版本复用；较大后段chunk做可选实测；质量不降需要真实对照'),
('实验设计','同一参考与目标文；至少三轮独立进程接口实验；每个chunk2/4/8/12检查；检查短尾与取消；参考码标记不能入decoder；生成总帧对应总样本；检查窗口峰值上限；性能fixture不算Qwen性能；CPU tinyMimi不算完整TTS；硬件结果不能编造'),
('降级与边界','新解码模式不自动回旧混参考路径；ICL缺文本给明确提示；不要静默改为别的声音；不要自动降模型大小；不改语速充RTF；不删用户正文充速度；不缩减训练数据；保留故障监督；记下每次初始失败；整体仍按证据判定')
],[
('代码审查','三轮读全源并记录哈希；Python AST巡检；Go格式和race；浏览器JS语法；Rust未修改仍说明现场边界；逐专题审视引用关系；不把哈希清单当语义证明；每轮100建议逐项处置；未实施项明确保留；别把300建议当300bug'),
('参考绑定测试','中英转写跨语言指纹一致；WAV变更指纹变化；文本变更指纹变化；语言变更指纹变化；质量统计变化不改变声音指纹；旧Worker缓存不能放行新pin；任务等待期间换档案需重校验；错误绑定不能输出PCM；两卡pin不等必须失败；取消不触发重加载'),
('解码测试','样本总数等于总帧乘1920；reference marker严格拒绝；短码块可暂存；最大窗口有界；窗口左端超出不可访问；lookahead尾部完整flush；flush幂等；取消丢尾部；非有限输出不得成功；错误采样率拒绝'),
('RTF实验入口','调用真实worker而非造测量；用户显式启用目标机测试；不启动第三模型；仅读取既有档案；保存生成WAV供试听；报告不含口令；至少三次重复；测前确认双worker真实引擎；未达0.3就failed而非pass；没有CUDA明确blocked'),
('现有服务','完整Python三轮；Node三轮；Go race count3；完整Chromium三轮；协议生命周期三轮；真实Faster接口三轮；HF导入tinyMimi三轮；保留训练CPU等价门禁；不忽略失败测试；修复后完整重跑'),
('浏览器文案','显示ICL条件不等于回放参考；显示音色尚需试听；显示RTF目标未达证据；保留参考文本编辑；提示转写必须匹配；不新增假训练按钮；不显示100相似度；性能诊断不藏慢行；手机无横向溢出；锁定清空私有文本'),
('包与版本','新step16独立文件；原始至15冻结；repack逐资产哈希；内嵌新解码模块；内嵌新RTF实验入口；剪贴板全量读回；下载逐字节核对；权限拒绝可全选；复制页固定新hash；正式工作台不覆盖'),
('备忘录','先计划后改产品；问题19后给50建议；问题20后给50建议；问题21后给50建议；累计问题建议保留；最终交接完整内嵌；原失败日志不覆盖；状态用PARTIAL与BLOCKED；缺硬件不得改成已达标；不要求用户提供密钥'),
('真实声学','多人参考不是调参可解决；ICL能改善但非保证；声纹分数不是听感真值；模型仍可幻觉添字；跨语言可能改变口音；沙沙声需实际音频定位；不从一张截图断定频谱；静音延迟不算首声；质量与速度一起验收；人声自然度需独立试听'),
('后续门禁','优先真实T4不同文本试听；逐GPU比较同参考；测试候选切换中取消；测RTF中位和最慢；参考泄漏单独核查；新进程重载检查；私有音频自行备份；历史网页训练闭环未完成；长样本全覆盖未完成；不把工程通过称全部目标完成')
]]
records=[]
for r,sections in enumerate(groups,1):
 inventory=[]
 for p in sorted(S.rglob('*')):
  if not p.is_file() or any(t in p.parts for t in ('state','target','__pycache__')) or p.name=='gateway':continue
  b=p.read_bytes()
  if p.suffix=='.py':ast.parse(b)
  inventory.append({'path':str(p.relative_to(S)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
 entries=[];lines=[f'# 第十六阶段第{r}轮专题审查：100条建议','','全源读取/哈希/AST不等于逐行语义无错。重点调用链人工分析，未实测声学或GPU性能不填成功。','']
 for anchor,raw in sections:
  vs=raw.split('；');assert len(vs)==10,(anchor,len(vs))
  for v in vs:
   ident=f'S16-R{r}-{len(entries)+1:03}';entries.append((ident,anchor,v));lines.append(f'{len(entries)}. [{ident}] `{anchor}`：{v}。')
 assert len(entries)==100
 (D/f'KAGGLE_STEP16_REVIEW{r}.md').write_text('\n'.join(lines)+'\n')
 records.append({'round':r,'entries':entries,'source_inventory':inventory})
(R/'docs/validation/step16/review-before.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
questions=[('19','音色不像与两种声音，应如何修复且不重新播放参考？','A保持15纯向量；B恢复有转写ICL条件、只解码生成码、参考内容固定绑定；C把参考原音混回输出。','B','15向量模式可能弱化相似度；B保留声学/转写条件但参考码绝不进codec，新增内容指纹和路径缓存失效。C明确违反用户先前要求。ICL不能保证无幻觉或绝对相似，用户原音频未提供，实际听感仍待验。',0),('20','沙沙声和RTF0.3能否靠换语言、加副本或提高增益解决？','A强降噪/多副本；B有界生成码上下文、两帧lookahead、限制噪声增益、分阶段测量；C缩短或加速音频冒充RTF下降。','B','删除全历史cat，窗口25帧上下文+chunk+2帧待提交，禁止参考码解码；留160ms未来上下文减少块末不稳定。每任务重置响度状态、默认最大增益从12回到6dB，目标仍-18，显式可调。会增加约160ms音频lookahead，不能称免费低延迟或真实去噪已验。',1),('21','如何验证相似、单一声音、无沙沙与RTF≤0.3而不造硬件结果？','A用Mock吞吐宣布达标；B三轮工程/真实库接口实验，提供实际双worker基准入口并保留声学与T4门禁；C只比较文件哈希。','B','工程测试确认绑定、边界、样本完整、取消；真实Faster控制流用明确注入CPU模型fixture，tinyMimi仅保护依赖。目标机基准调用已驻留真实worker、输出逐GPU墙钟RTF与WAV，0.3未达就失败；没有CUDA则blocked。听感与参考单人性仍需真人审核，不称100%信心。',2)]
p=D/'KAGGLE_DECISIONS.md';v=p.read_text()
for num,q,options,pick,answer,r in questions:
 v+=f'\n\n## 问题{num}：{q}\n\n具体选项：{options}\n\n推荐选择：{pick}。\n\n详细回答：{answer}\n\n本题回答后、进入下一题前的50项开发建议：\n\n'
 for i,(ident,anchor,text) in enumerate(records[r]['entries'][:50],1):v+=f'{i}. [{ident}] 在`{anchor}`落实：{text}；以对应代码测试或明确硬件门禁核验，不以建议数量代替实现。\n'
 v+='\n追问结论：工程取舍已明确，不向用户重复提问；未提供真实音频与T4不能对声学或速度声称100%。\n'
p.write_text(v)
frozen={}
for p in [*sorted((R/'kaggle').glob('kaggle*.py')),R/'workspace/HEAD.json',*sorted((R/'workspace/revisions').rglob('*'))]:
 if p.is_file():frozen[str(p.relative_to(R))]=hashlib.sha256(p.read_bytes()).hexdigest()
(R/'docs/validation/step16/frozen-before.json').write_text(json.dumps(frozen,indent=2)+'\n')
print('3x100 review recommendations; Q19-21 each50; frozen original–15/formal inventory')
