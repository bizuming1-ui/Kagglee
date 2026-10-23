"""Record second topical review; no product edits and no fabricated full-source completion."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[3];D=R/'docs';H=Path(__file__).resolve().parent
assert not (D/'KAGGLE_STEP18_REVIEW2.md').exists(), 'Do not overwrite a completed review'
groups=[
('真实模型接口与批量语义','faster0.5.4:model.py:_resolve_precomputed_voice_clone_prompt; qwen-tts-hf0.1.1.post1:qwen3_tts_model.py',[
'保持qwen-tts-hf与旧qwen-tts发行版严格分离，源码同命名空间不等于同版本',
'下载源码必须核对PyPI wheel SHA256，收据注明实际提供模型类的发行版',
'将三提示单目标被拒绝的实际接口行为加入未来多参考功能合同',
'将三提示三目标定义为独立批量任务，界面不能称参考融合',
'保留列表prompt每项独立ref_text，不用共享一条文字冒三候选匹配',
'字典prompt的批量ref_text共享行为应明确，不直接用于三段不同转写',
'引用prompt item中ref_code与speaker embedding的区别，不能用声纹平均替代ICL',
'保持单ICL预计算提示的真实接口回归，不能为新模式破坏现有快照',
'向量模式继续要求显式选择，不把它作为未实现融合的静默替代',
'实际生成器、权重和声学结果未执行时，接口控制流通过不标模型实验通过']),
('候选与生成条件合同','py/analyst.py:build_profile; py/voice_binding.py; py/worker.py:FasterEngine',[
'建立全部候选分析清单，逐项列源文件、时间、匹配转写、指纹和有效性',
'单锚点模式明确显示被用作ICL的候选及未用作ICL的其他候选',
'若后续共享参数来自全部候选评分，记录算法与评分证据而非暗示音频融合',
'比较每候选合成时固定同文同seed同采样参数，确保差异确由候选造成',
'候选中心与实际Qwen说话人嵌入不同空间时不得直接替换',
'实验性的融合嵌入若提出，必须独立模式且真实盲听，不自动作为最佳方案',
'不跨候选拼转写或参考码以绕过模型批量长度校验',
'候选顺序变化时用内容身份而不只用数组下标定位证据',
'候选有效时长按实际WAV而非仅展示start/end计算，避免舍入差',
'候选策略、模型模式及参数调整必须使旧会话明确失效']),
('候选入口数据验证','py/analyst.py:set_candidate / set_text; py/library_api.py:body',[
'index必须严格整数且非bool，拒绝true变1与false变0',
'拒绝1.9截断成1，避免非整数JSON静默切换其他参考',
'缺失index应明确拒绝还是显式兼容默认0，不让文档与行为矛盾',
'null、数组、对象及NaN输入转换失败应返回受控4xx而非未捕获异常',
'候选入口未知字段与重复字段的策略需与严格library接口一致',
'验证candidates为非空合法列表，不能只依赖len和下标访问',
'验证候选file为安全单文件名且普通文件，避免损坏profile路径越界',
'手工ref_text不接受dict/list被str化，保留严格字符串与Unicode校验',
'保留训练档案禁止改候选和转写的409边界，不绕过版本固定',
'增加真正HTTP参数与错误码测试；当前AST调用不冒充FastAPI测试']),
('参考版本与并发提交','py/analyst.py:calibrate_profile / set_candidate / set_text; py/qtts_common.py:write_json_atomic',[
'校准开始捕获完整候选集合版本，提交时核对未变再采用评分',
'禁止用旧候选评分选择重新读取后已更改的同下标候选',
'校准期间并发编辑转写不能被结束时静默覆盖，需冲突响应',
'候选文件内容更改但文件名不变也要改变校准输入版本',
'候选变更、文本变更、校准、删除应协调同一档案锁或乐观版本合同',
'进程内线程锁与跨进程文件锁分别评估，不能把一个称全局事务',
'HEAVY最大2只限制并发数量，不等于每profile串行，不能替代状态锁',
'对先写磁盘再等HEAVY被429拒绝的路径核对reference_saved状态',
'原子JSON替换只保护单文件，候选复制与JSON提交之间仍需一致性设计',
'校准提交前档案已删除或adapter状态已变化时必须停止，不能恢复旧状态']),
('校准缺失指标与失败状态','py/analyst.py:calibrate_profile',[
'ASR评估全部失败不再用CER0.05冒充实测值，应记录null与失败原因',
'部分文本ASR失败时记录覆盖率，不能只对成功样本平均后隐藏缺失',
'全部候选合成失败时返回明确未选出有效结果，不能chosen0看似成功',
'每候选的有效生成条数和预期条数同时保存，评分先验证完整性',
'未测或低可信声纹指标不填高分默认值，应明确阻塞/降级语义',
'候选排序排除非有限得分，NaN/Inf不进入max选择',
'模型输出空音频、太短、全静音和缺字分别记失败而不只比声纹',
'校准报告应保留先前有效结果，失败新校准不覆盖为貌似新最佳',
'ASR释放与临时目录清理放入覆盖所有异常的finally路径',
'错误信息需脱敏且保留阶段，不能把原文和本机私有路径暴露给日志']),
('双卡诊断的可比性','py/analyst.py:consistency; go/gateway/scheduler.go:synthReq',[
'同目标文本跨GPU诊断使用相同seed，修复100+17*ti+gi的设备偏移混杂',
'将实际seed写入每张卡诊断条目，使测试条件可核验',
'会话调度当前各卡同seed的行为应保留，不把诊断偏移引入播放',
'两卡同一voice_binding和voice_conditioning都要进诊断收据',
'记录实际dtype、模型版本、codec政策与DSP后端，不能仅比profile ID',
'相同参数不意味着位级相同；阈值评分和人工听感结论分开',
'同文对照与不同文本交替朗读各自设计，不能用同文替代自然衔接',
'所有条目失败时speech_db默认0不应参与一致性，明确缺失项',
'consistent布尔值应附完整性及阈值说明，不能称零噪声或100%同声',
'诊断生成在锁定或请求取消后仍进行时保留资源状态，不误报即时停止']),
('双卡加载与启用确认','py/analyst.py:load_on_workers / reload_response; go/gateway/main.go:activate',[
'校准结束必须检查load_on_workers回执，不能丢弃失败后正常返回',
'保留文本/候选接口已有reference_saved与503部分失败语义',
'Go激活两卡并行、同绑定同模式核验及旧active保留不得回归',
'激活最终再次读磁盘核对指纹的检查必须保留',
'Python reload最终current为None时应视失败，而不是跳过版本核验',
'候选校准只用GPU0的现状须说明；多卡校准需独立计划，不虚报双卡评估',
'加载某卡成功某卡失败后，不允许新会话静默只用成功卡冒双卡一致',
'冷首次sanity合成耗时应与提示提取耗时分开记录，避免首声归因错误',
'HTTP断开不等于后台模型加载已停止，未来重试需幂等/状态查询',
'不得为降低激活耗时跳过Worker锁内参考前后两次指纹校验']),
('缓存、临时资源与删除','py/worker.py:FasterEngine.load_profile / Worker._load_profile_locked; py/analyst.py:calibrate_profile / delete_profile',[
'审查_cal临时profile移除后Worker提示缓存仍驻留的资源生命周期',
'重复校准相同临时ID时确保旧提示被替换，不能复用先前参考',
'删除档案后清理与它关联的profiles、voice_bindings、levelers和提示快照',
'缓存释放必须获取合成同一把锁，不释放正在使用的GPU张量',
'缓存容量按可测内存预算管理，而不是只看磁盘profile数量',
'临时校准ID与用户可启用ID区分，不能由列表选中临时声音',
'备份继续排除_cal档案，不把测试用临时状态持久化为模型',
'临时目录清理失败记录状态并可回收，不无声积累数据',
'生成器取消仍要close并释放有界codec窗口，不能因缓存修改遗漏',
'不要盲目清空CUDA所有缓存导致每段冷启动，资源回收须按作用域']),
('前端状态、认证与用户反馈','web/app.js:apiFetch / m / profile candidate controls; py/access_control.py',[
'候选点击期间禁用或序列化同档案变更按钮，避免重复并发写',
'响应乱序时按操作版本更新高亮，不让旧响应覆盖新选择',
'继续保留accessEpoch和AbortController防锁定后迟到数据回填',
'客户端取消只能停止等待时明确提示后台任务可能继续，不伪报服务器取消',
'503且reference_saved时显示已保存未全卡就绪，不能笼统当未保存',
'校准报告区分逐候选评分、最终提交、双卡加载三个状态',
'没有有效候选或指标不全时不显示成功绿标',
'参考转写可审阅但日志默认脱敏，token不进URL/localStorage',
'新增条件证明信息只放同源授权接口，不能自动上传外部诊断服务',
'新增交互保持移动端可操作、录音失败队列保留与锁定清空']),
('保留边界与最终验证','py/voice_library.py; py/trained_profiles.py; py/persist.py; tests/browser',[
'原始库已有revision与lease设计可借鉴，但不直接修改其已成功数据格式',
'候选处理与真实训练继续分开命名，不把评分或缓存称训练提升',
'训练adapter来源hash与固定参考在新条件策略下仍必须核验',
'私有原始样本仍排除Dataset自动备份，新增诊断WAV默认不进入归档',
'代码、参数和参考版本相同的测试与实际用户WAV声学验收分开报告',
'为每个确认缺陷建立独立失败样例，后续修复应让同案例先失败再通过',
'受控AST交错不是线程压力测试；实现后补真实并发和HTTP回归',
'下载wheel仅源码检查不安装旧qwen-tts，避免命名空间冲突',
'本轮100建议与实际实验范围完整入备忘录，不宣称全源三轮完成',
'第三轮结束及逐题50建议决策完成后才改产品，继续冻结17包与工作台'])
]
rows=[];lines=['# 第十八阶段第二轮：候选条件、接口合同与并发状态100条建议','','状态：第二轮关键路径专题审查完成；第三轮与阶段自问自答未完成。不是全源三轮语义审查完成声明，产品源码未修改。每条建议是待实施/保留合同，不是100个新增已确认bug。','','## 取证方法与来源','','实际下载并核对faster-qwen3-tts0.5.4与qwen-tts-hf0.1.1.post1的PyPI wheel SHA256；旧qwen-tts0.1.1仅作区别核查，未安装。最初把发行版名写成qwen-tts==0.1.1.post1导致查询失败，纠正为项目真正固定的qwen-tts-hf；不是产品依赖失败。完整URL/hash见`validation/step18/upstream-round2-provenance.json`。','','`kaggle/tests/reference_state_probe.py`提取原函数AST执行：真实控制流保留，外部GPU/ASR/tokenizer/说话人/网络为显式fixtures。确定性交错并非线程压力；未跑HTTP、完整模型或GPU，不证明音色或噪声。','']
confirmed={21:'candidate_payload_cases bool coercion',22:'candidate_payload_cases fractional truncation',24:'candidate_payload_cases uncaught TypeError',32:'calibration_cases concurrent-candidate-edit',33:'calibration_cases concurrent-candidate-edit overwrites concurrent text',41:'calibration_cases ASR-unavailable -> CER0.05',43:'calibration_cases all-synth-failed -> chosen0',51:'consistency_case seeds100/101',61:'calibration_cases reload-failed ignored'}
for topic,source,items in groups:
 assert len(items)==10
 lines.extend([f'## {topic}',f'源码位置：`{source}`。',''])
 for item in items:
  i=len(rows)+1;ident=f'S18-R2-{i:03}';row={'id':ident,'topic':topic,'source':source,'recommendation':item,'status':'pending-evidence-or-preservation'}
  if i in confirmed:row.update(status='controlled-baseline-issue-reproduced-not-fixed',evidence=confirmed[i])
  rows.append(row);lines.append(f'{i}. [{ident}] {item}。')
 lines.append('')
assert len(rows)==100
lines+=['## 三轮受控实验结果','','每轮6项上游提示合同、4项校准场景、9项候选输入、1项双卡seed诊断，共20项；三轮结果一致。三提示单目标list/dict均拒绝，三提示三目标是独立批量。ASR全失败产生默认CER0.05、旧评分提交新候选、加载失败未检查、全合成失败仍chosen0、bool/float强转、非法类型异常以及诊断不同seed均复现。它们是控制流/状态问题，不是用户沙沙根因。','','保留：Go激活并行加载、指纹/模式确认、最终重读及旧active保留；Python文本/候选reload_response已有503与reference_saved语义；Worker锁内前后核验；前端认证epoch。不能只列缺陷却重写破坏这些成功保护。','']
(D/'KAGGLE_STEP18_REVIEW2.md').write_text('\n'.join(lines).rstrip()+'\n')
(H/'review2.json').write_text(json.dumps({'count':100,'all_source_semantic_review_complete':False,'recommendations':rows},ensure_ascii=False,indent=2)+'\n')
print('Second topical review: 100 recommendations; product unchanged')
