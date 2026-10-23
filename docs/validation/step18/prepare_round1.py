"""Stage18 pre-product snapshot and explicit first topical review. Not a semantic all-code proof."""
from pathlib import Path
import ast, hashlib, json, subprocess
R=Path(__file__).resolve().parents[3];D=R/'docs';H=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
assert subprocess.check_output(['git','branch','--show-current'],cwd=R,text=True).strip()=='arena/03d65d8e-kagglee'
assert not (H/'baseline.json').exists(), 'Baseline already exists; do not replace historical evidence'
m=json.loads((R/'kaggle/source_manifest_step17.json').read_text())
raw=(R/'kaggle/kaggle-fixed-step17.py').read_bytes()
assert len(raw)==313504 and sha(raw)==m['launcher_sha256']=='6eacaede14f9b5f42ac5c334df5c3f9d1a1c6858fb69b7d3a8ff241ec60427ea'
files=ast.literal_eval(next(n.value for n in ast.parse(raw).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='FILES' for t in n.targets)))
import base64,zlib
inventory=[]
for row in m['assets']:
 p=R/'kaggle/source'/row['path'];b=p.read_bytes()
 assert sha(b)==row['sha256']==files[row['path']][0] and zlib.decompress(base64.b64decode(files[row['path']][1],validate=True))==b
 if p.suffix=='.py':ast.parse(b)
 inventory.append({'path':str(p.relative_to(R)),'bytes':len(b),'sha256':sha(b)})
old=json.loads((D/'validation/step17/frozen-before.json').read_text())
assert all(sha((R/name).read_bytes())==digest for name,digest in old.items())
frozen={str(p.relative_to(R)):sha(p.read_bytes()) for p in [*sorted((R/'kaggle').glob('kaggle*.py')),*sorted((R/'kaggle').glob('source_manifest*.json')),R/'workspace/HEAD.json',*sorted((R/'workspace/revisions').rglob('*'))] if p.is_file()}
head=json.loads((R/'workspace/HEAD.json').read_text());formal=json.loads((D/'validation/step17/formal-api-readonly.json').read_text())
assert head['revision']==formal['revision']
for name,digest in formal['hashes'].items():assert sha((R/'workspace/revisions'/head['revision']/name).read_bytes())==digest
baseline={'branch':'arena/03d65d8e-kagglee','base_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),'stage17_bytes':len(raw),'stage17_sha256':sha(raw),'assets_verified':len(inventory),'source_inventory':inventory,'frozen_hashes':frozen,'prior_frozen_hashes_verified':len(old),'formal_revision':head['revision'],'formal_files_verified':len(formal['hashes']),'historical_handoff_sha256':sha((D/'KAGGLE_HANDOFF_PROMPT.md').read_bytes()),'all_code_semantically_reviewed':False,'reviews_completed':1,'product_modified':False,'real_gpu_executed':False,'voice_quality_verified':False}
(H/'baseline.json').write_text(json.dumps(baseline,ensure_ascii=False,indent=2)+'\n')
groups=[
('候选真实语义','py/analyst.py:build_profile / calibrate_profile; py/worker.py:FasterEngine.stream',[
'将候选参与质心统计与实际ICL锚点分开显示，避免全部片段已融合的误解',
'在合成收据记录选中的anchor_candidate，而不是只显示profile ID',
'记录实际锚点字节指纹与对应转写指纹；日志不明文写入私有转写',
'用不同内容的三个候选验证只选中的音频进入提示提取',
'审核“候选校准”文案明确逐个试验后选一个，不称多参考融合',
'查验Faster真实接口的多参考能力，未支持时不伪造列表参数',
'禁止把三个片段PCM拼成一个提示并配不连续全文',
'跨候选声纹中心仅作评分依据，不声称它已替代模型speaker embedding',
'为单个合法候选保留最短建档链路，不强迫三候选',
'给未来多候选策略保留显式模式与回退边界，不静默改变17默认']),
('候选切换与并发','py/analyst.py:set_candidate; py/worker.py:_load_profile_locked; py/voice_binding.py',[
'非法index的布尔、小数、对象与缺省语义分别测试，避免int强转误选或500',
'核查切换候选与校准并发时磁盘写入、工作者加载是否形成一致事务',
'候选文件复制失败时保留旧profile JSON，不留下半更新锚点',
'双卡仅一张加载成功时明确部分失败，不宣称启用完成',
'旧会话遇新指纹必须继续拒播，不能热切后拼混音色',
'转写编辑与候选选择同时发生时绑定同一版本，防止音文错配',
'校准临时profile的anchor_candidate元数据应指向实际试验候选，不能误标0',
'候选变更后清理或替换提示快照时保留锁内核验',
'为重复点击候选与取消任务增加幂等与状态测试',
'训练adapter的固定参考限制保持，不让候选切换绕过来源绑定']),
('首声定义与时钟','py/worker.py:Worker.synth; go/gateway/session.go; web/app.js:tick',[
'分别记录请求、首个可用文本、排队、预填充、首PCM、首播放命令',
'worker t_start在加载提示之后，单独计量冷提示加载而不漏记等待',
'queue_ms当前覆盖锁等待等前置耗时，拆项后保留旧字段兼容',
'浏览器firstPlayedMs当前在发play命令处赋值，标明不是硬件实际出声',
'评估AudioWorklet消费首个语音样本的确认消息，区分主线程命令延迟',
'跨Python、Go与浏览器仅使用各自单调时间差，不能直接减不同纪元',
'显式静音停顿不能计为首个可用人声，保留禁止原音占位',
'首包平均之外记录p50/p95与冷暖状态，不用一次幸运值',
'将文本长度、参考长度、chunk_size和设备条件写入性能收据',
'首声提速必须同时检查缺字与最终音频完整性，不能裁掉开头']),
('浏览器启动缓冲','web/app.js:needToStart / onWorklet / QttsRing',[
'对当前0.7秒下限和初始2秒策略建立确定性到达轨迹对照',
'分别测试高速稳定、慢速持续、突发包与长网络抖动',
'初次启动与欠载恢复分别设计目标，不统一缩到最小',
'将预测器无速率样本时的保守回退纳入首次播放测试',
'测量AudioWorklet统计消息的刷新间隔对主线程启动判断的影响',
'在44.1k及48k上下文验证重采样后的fill计秒正确',
'短于启动阈值但已完成的真实语音应及时播放，不等待不可达缓冲',
'后台页、暂停恢复、锁定与取消后不得发送迟到play',
'记录ring dropped样本；任何丢样不能只显示播放成功',
'低延迟策略只能在欠载预算内启用，不能把断续当自然阅读']),
('模型与调度热路径','py/worker.py:FasterEngine; py/clone_stream.py:generated_only_stream; go/gateway/scheduler.go',[
'对2/4/8/16帧首块大小做同文本同seed对照，测TTFA及总RTF',
'小首块与稳态大块若需不同大小，先确认真实生成器支持，禁止无效传参',
'检查decode迭代器首次next含有的预填充时间，不能只测创建生成器',
'单独计量token生成、codec解码及CPU拷贝，避免归因全部GPU',
'提示快照重用必须与内容指纹一致，不退回仅按路径缓存',
'不为首声把ICL换成向量默认，保留相似度条件',
'比较首段优先调度与后续并行的队头阻塞，不无证据锁死单卡',
'确认Live聊天第一可用前缀触发不被朗读聚合配置覆盖',
'保留最大生成token与取消限制，不能为速度删掉输出',
'不默认每卡双模型增加显存；只有目标T4实测才接受吞吐结论']),
('输入噪声与参考处理','py/analyst.py:build_profile / denoise / normalize_speech',[
'原始RMS约-47.7只作为风险，不推断具体麦克风故障',
'分别记录归一化前后语音电平与峰值，注明增益上限14dB',
'候选SNR是估计量，不能把17dB阈值当真实噪声声压',
'保留raw、strength0.85、strength0.55对照的处理收据',
'审查声纹相似0.94与SNR增益2dB门禁是否会误接收失真，不能只看单分数',
'验证全零、强直流、很轻语音及背景声输入的处理决策',
'对齿音、气声、摩擦音单独测保真，不能以削高频冒无沙沙',
'不在用户未授权时保存或上传原始私有WAV作为公共证据',
'已存在非平稳降噪不等于生成输出已降噪，明确处理发生阶段',
'录音时扬声器回录网页朗读的可能性仅列假设，不能由截图定论']),
('生成输出噪声定位','py/worker.py:Worker.synth; py/clone_stream.py:GeneratedCodecWindow',[
'建立模型PCM、后处理PCM、浏览器录回的分层局部诊断，默认关闭私有采集',
'将codec窗口起点与边界脉冲位置关联，区分底噪和接缝爆音',
'对持续人声与停顿分别计算频谱，但无清洁真值时不称绝对SNR',
'继续验证codec只收到生成码，不能回到参考码前缀解码',
'真实预训练codec与随机tiny codec的质量证据必须分列',
'非有限模型输出当前替换为零，应评估失败拒播而非掩盖异常的策略',
'增益提升可能抬噪，记录处理前后噪声地板变化而不自动强门限',
'不能用输出全静音或静音段删除作为零噪声验收',
'保留模型自然人声呼吸与禁止添加噪声的区别，不自动切除语音气息',
'用户全程纯人声目标需真实WAV试听和添字检查，代码指标不替代']),
('DSP状态与后端一致','py/audio_rt.py:Leveler; rust/audio_rt/src/lib.rs:Leveler',[
'实测同一信号整块与任意分块处理的样本一致性',
'重点验证NumPy不足96样本首块时淡入是否在下一块重新从零开始',
'核查NumPy按输入块丢弃不足240样本RMS余数与Rust跨块累积差别',
'比较Rust逐样本增益平滑与NumPy逐块插值，不能宣称严格等价',
'保持输出样本数与输入相等，不能为降噪补偿无记录延迟',
'分别测试DC blocker状态、零输入残留与长静音后重新讲话',
'测试max_gain_db=0隔离淡入和DC滤波，再开放AGC定位差异',
'同卡每段重置与跨卡各自状态不同需测量，不能只凭相同目标响度称一致',
'flush的192样本衰减不是新生成语音，不能加入RTF语音分母',
'若修复NumPy算法须保留Rust接口版本兼容，并添加跨后端容差测试']),
('连续语义与播放接缝','go/gateway/segmenter.go; go/gateway/session.go; web/app.js:QttsRing',[
'将独立模型韵律重启、显式停顿、播放欠载三种接缝分类计数',
'保留朗读12/24首段、20/40/80稳态配置基线再比较，不盲目扩大',
'逐字验证分段重新连接等于原文，保护数字、缩写、引号和标点',
'审查PauseBeforeMs与tail_pause_ms是否重复加停顿，先画时序再修改',
'禁止跨词PCM重叠掩盖接缝，不牺牲清晰度冒自然度',
'段尾8ms衰减及下段淡入需以有声边界实测，不只用零边界波形',
'欠载时0.94尾衰减属于播放补偿，不能误标模型本身沙沙',
'自然度对照必须同时保存整段朗读，不能只听裁剪后小片段',
'不同GPU同文与交替长文分别试听；同seed不等于波形完全相同',
'只有真实模型支持的连续条件才能声称跨段联合生成，不换名称包装独立合成']),
('回归、语言和交付门禁','kaggle/repack.py; tests/browser; docs/validation/step17/final-checks.json',[
'冻结原始至17包、全部manifest及正式工作台，新增18不得覆盖历史包',
'三轮100建议均标已确认问题、待证假设或保留约束，不虚报300个bug',
'完成三轮审查后再逐题决策，每题50建议后才进入下一题',
'历史334测试不能算18新增验证，依赖缺失需如实记录和重建',
'对每个修复保留修复前失败、修复后通过的同输入收据',
'三轮Python、Node、Go race、协议和浏览器必须针对最终源码再执行',
'CPU合成信号实验不代替真实T4语音实验，硬件不足保持BLOCKED',
'按实测热路径选择语言；不要新增Java/C#/SQL服务凑多语言',
'最终18复制页、下载、剪贴板拒绝回退与手机逐字节校验不可省略',
'将全部已完成备忘录内嵌完整提示词；未完成轮次必须明确，不编造结论'])
]
rows=[];out=['# 第十八阶段第一轮：参考条件、首声和噪声链路的100条建议','','状态：关键路径首轮专题审查；不是全部代码已逐行完成三轮语义审查。产品未修改。建议是后续验证/实现清单，不是100个已证实缺陷。','','事实：当前生成使用单个选中锚点；候选参与评分/质心，校准是逐候选试验再择一。播放firstPlayedMs当前是主线程play命令时刻。NumPy/Rust DSP存在需实际验证的分块状态差异。','']
for topic,source,items in groups:
 assert len(items)==10
 out.extend([f'## {topic}',f'源码位置：`{source}`。',''])
 for item in items:
  i=len(rows)+1;ident=f'S18-R1-{i:03}'
  rows.append({'id':ident,'topic':topic,'source':source,'recommendation':item,'status':'pending-evidence-or-preservation'})
  out.append(f'{i}. [{ident}] {item}。')
 out.append('')
assert len(rows)==100
(D/'KAGGLE_STEP18_REVIEW1.md').write_text('\n'.join(out)+'\n')
(H/'review1.json').write_text(json.dumps({'count':100,'full_semantic_source_review_complete':False,'recommendations':rows},ensure_ascii=False,indent=2)+'\n')
print('Stage17 assets verified:',len(inventory),'prior frozen verified:',len(old),'recommendations:',len(rows))
