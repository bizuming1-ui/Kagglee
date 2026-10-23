"""Run once, before product edits: topical reviews, sequential decisions, frozen inventory."""
from pathlib import Path
import ast,json,hashlib
R=Path(__file__).resolve().parents[3];D=R/'docs';H=Path(__file__).resolve().parent
prior=ast.literal_eval(next(n.value for n in ast.parse((D/'validation/step16/prepare_reviews.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='groups' for t in n.targets)))
new=[[
('截图与根因','截图是15而非16不能当新包效果；录音限额与锚点限额分开；重现单个28.7秒ASR段；保留16的逐字匹配约束；不能将长音频硬截配全文；保留ASR词级时间戳；按完整词组而非字符比例切分；词与原段文本必须核对；缺词时间走音频窗口重新ASR；不能凭低RMS断定无人声'),
('词级对齐','验证时间戳有限；验证起止单调；验证不越源音频；拒绝重叠倒序词；Unicode字母数字核对转写；不要丢标点后汉字；长单词超窗口重新ASR；短尾保留在分析收据；跨文件绝不合并文字；对齐失败有明确中文建议'),
('长音频重识别','仅问题长段需要窗口ASR；每窗口音频和转写独立匹配；使用原音频实际切片；偏移恢复绝对时间；边界优先静音；窗口必须前进不死循环；最末窗口不丢；无语音窗口不伪造文字；沿用ASR锁及CPU复用；进度显示窗口计数'),
('长参考语义','长录音可以超过15秒；不能无限把20分钟塞进ICL；提供16与24秒参考窗口；默认16保护旧短样本；24明确标为实验与较慢；手工转写仅单短文件直接采用；长手工全文不能按时长分配；记录源总时长与选中锚点；记录重切分和重识别数量；明确建档不是全数据训练'),
('输入与安全','窗口值只允许16或24；表单和库入口都独立校验；失败保留本地录音；取消不得删除源音频；不自动云传原音；拒绝非有限PCM；保留20分钟录音预算；低电平提示调整设备；提示麦克风距离不替人猜设备；保留原始至16冻结')
],[
('短参考与音色','继续使用ICL匹配文本；不退回15纯向量默认；新旧GPU不能混版本；相同参考绑定采样参数；Go和Python浮点编码一致；缺省参数也计入指纹；不接受NaN温度；改温度使旧会话失效；参数相同不是音色绝对相同；真人试听仍是独立门禁'),
('多卡参数','绑定temperature；绑定top_k；绑定top_p；绑定repetition_penalty；top_k必须整数；统一默认参数数值；每次合成锁内复核；预计算提示快照保留；不混用不同条件模式；不声称两卡波形逐位相同'),
('参考质量','记录原始RMS；记录原始峰值；记录SNR估计而非真值；低电平给风险提示不直接拒绝；响度归一化不是降噪；MFCC相似不是可靠声纹真值；避免强降噪损伤辅音；参考多人必须审核；24秒未必比10秒好；不播放原录音补相似度'),
('连续朗读','只调整朗读聚合不延后聊天首句；减少过多独立合成语段；优先完整句子标点；保留原始全文字符；不合并不同用户任务；保留取消和背压；不跨词叠加PCM；不删除语音以隐藏接缝；保留已有codec有界上下文；自然韵律不能仅靠交叉淡化保证'),
('噪声边界','继续禁参考呼吸拼接；不生成白噪声补停顿；保留软限幅；保留可控增益；不把静音当去噪成功；不默认低通抹齿音；新统计不得泄漏原文本；生成WAV可供独立试听；缺真实音频不宣布零噪声；不得缩短输出冒RTF达标')
],[
('重现门禁','单个28.7秒词级段建档成功；单个60秒段词级切分；20分钟时间戳规划有界；缺词时间戳实际窗口重识别；文本不匹配必须回识别；长manual全文不错误拼接；短manual16秒保持兼容；24秒锚点不越界；无声和非法时间戳不造成功；每项做三轮回归'),
('接口门禁','浏览器发送参考窗口字段；默认值16可见；24选项真实进入后端；锁定清除私有转写；表单非法值拒绝；库处理同样校验；服务重启新包版本可识别；新包逐字节复制；16包哈希冻结；正式工作台保持不变'),
('参数指纹测试','中英转写跨语言一致；默认值与显式默认相同；四参数分别变更使pin变化；NaN和无穷拒绝；非整数top_k拒绝；Worker不输出不符pin的PCM；Go协议携带固定pin；不改adapter来源绑定；新旧包混跑明确重启；不把指纹当身份认证'),
('验证与实验','Python完整三轮；Node完整三轮；Go race三轮；Chromium完整三轮；六服务协议各三轮；实际Faster控制接口三轮；真实tiny codec三轮；Mimi导入重载三轮；CPU训练等价三轮；所有CPU模型明确不是Qwen音质证据'),
('记录与交付','问题22回答后给50建议；问题23回答后给50建议；问题24回答后给50建议；方案先于产品修改；每次失败日志保留；逐条300建议分类；无硬件保留BLOCKED；真实RTF0.3仍需测量；完整57份备忘录内嵌；不承诺100相似零噪声')
]]
records=[]
for r in range(3):
 groups=new[r]+prior[r][5:]
 rows=[];lines=[f'# 第十七阶段第{r+1}轮专题研究：100条建议','','本轮前50条针对新问题，后50条复核已成功链路。全源读取/哈希/Python AST不等于逐行语义无错。','']
 for topic,raw in groups:
  items=raw.split('；');assert len(items)==10,(topic,len(items))
  for item in items:
   ident=f'S17-R{r+1}-{len(rows)+1:03}';rows.append([ident,topic,item]);lines.append(f'{len(rows)}. [{ident}] `{topic}`：{item}。')
 assert len(rows)==100
 (D/f'KAGGLE_STEP17_REVIEW{r+1}.md').write_text('\n'.join(lines)+'\n')
 inventory=[]
 for p in sorted((R/'kaggle/source').rglob('*')):
  if not p.is_file() or any(x in p.parts for x in ('state','target','__pycache__')) or p.name=='gateway':continue
  b=p.read_bytes()
  if p.suffix=='.py':ast.parse(b)
  inventory.append({'path':str(p.relative_to(R/'kaggle/source')),'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)})
 records.append({'round':r+1,'entries':rows,'source_inventory':inventory})
(H/'review-before.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
qs=[('22','超过15秒录音为什么建档失败，如何修复且不伪造对齐？','A删16秒限制后配整段全文；B保留音频/转写匹配，使用词级时间戳切分，缺失则短音频窗口真实重识别；C按字数比例分全文。','B','源码接收长录音，但候选仅取完整2.5–16秒ASR段，忽略已有words。一个28秒段因此无候选。B按完整词切分并验证词文一致；缺词时间不猜，重新ASR实际窗口。保留长音频完整分析，长manual全文不冒充逐字对齐。',0),('23','超长参考是否一定更像，怎样保证短参考与双卡条件一致？','A无限参考整段进模型；B可选16/24秒锚点，长录音用于选择代表片段，指纹同时绑定四项采样参数；C混入参考原音增加相似。','B','更多同说话人干净录音有助选样，但参考上下文不是训练，不能保证长于短。默认ICL与匹配转写保持；新增24秒明确实验和延迟代价。四生成参数及参考内容共同绑定，防两卡不同修订；同条件也不保证硬件波形相同或100%音色。',1),('24','如何自然连续朗读、排查沙沙声并诚实验收？','A强低通加跨词重叠；B适度增大只读文本聚合、保留正文/取消/codec，参考质量提示与真实双卡WAV验收；C静音或删字冒无噪声。','B','减少独立语段可降低重启韵律次数，但不声称等同整段联合生成。保留聊天第一句早提交，不跨词叠加PCM。记录低输入电平而不从截图猜设备；强降噪会损伤音色，不无证据默认开启。三轮工程/实际库控制实验外，训练权重试听和T4 RTF仍需真实硬件。',2)]
p=D/'KAGGLE_DECISIONS.md';value=p.read_text();assert '## 问题22：' not in value
for n,q,opts,choice,answer,r in qs:
 value+=f'\n\n## 问题{n}：{q}\n\n具体选项：{opts}\n\n推荐：{choice}。\n\n详细回答：{answer}\n\n进入下一题之前的50项实施建议：\n\n'
 for i,(ident,topic,item) in enumerate(records[r]['entries'][:50],1):value+=f'{i}. [{ident}] `{topic}`：{item}；以代码/测试收据或明确真实硬件门禁核查。\n'
 value+='\n追问结论：方案边界明确，不向用户提问；未知的真实声学结果保留未知，不声称100%。\n'
p.write_text(value)
frozen={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [*sorted((R/'kaggle').glob('kaggle*.py')),R/'workspace/HEAD.json',*sorted((R/'workspace/revisions').rglob('*'))] if p.is_file()}
(H/'frozen-before.json').write_text(json.dumps(frozen,indent=2)+'\n')
print('3x100 recommendations; Q22-24 each50; original–16 + formal files frozen')
