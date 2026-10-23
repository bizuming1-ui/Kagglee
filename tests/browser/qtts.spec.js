import { test, expect } from '@playwright/test';
import { readFile } from 'node:fs/promises';

// Browser/protocol regressions with explicitly mocked Web Audio and HTTP streams.
// These tests cannot measure audibility, voice similarity, GPU throughput or DeepSeek.
async function openQTTS(page, { failAudio = false, deferAudio = false, locked = false, realAudio = false, denyMedia = false, deferMedia = false, silence = false, failUpload = false, failPreflight = false, manyProfiles = false, trainedProfile = false } = {}) {
  await page.route('**/qtts-regression', async route => route.fulfill({ contentType: 'text/html', body: await readFile('kaggle/source/web/index.html', 'utf8') }));
  await page.route('**/recorder.js', async route => route.fulfill({ contentType: 'text/javascript', body: await readFile('kaggle/source/web/recorder.js', 'utf8') }));
  await page.route('**/app.js', async route => route.fulfill({ contentType: 'text/javascript', body: await readFile('kaggle/source/web/app.js', 'utf8') }));
  await page.addInitScript(({ failAudio, deferAudio, realAudio, denyMedia, deferMedia, silence, failUpload, failPreflight, manyProfiles, trainedProfile }) => {
    localStorage.setItem('qtts_dskey', 'obsolete-secret');
    window.apiRequests=[];window.audioMessages = []; window.turns = []; window.moduleLoads = 0; window.reports = [];
    if(realAudio) {
      const NativeContext=window.AudioContext,NativeFile=window.File;
      window.micStreams=[];window.captureContexts=[];window.mediaRequests=0;window.madeFiles=[];
      window.File=class extends NativeFile {constructor(...args){super(...args);window.madeFiles.push(this)}};
      window.AudioContext=class extends NativeContext {createMediaStreamSource(stream){window.captureContexts.push(this);return super.createMediaStreamSource(stream)}};
      const makeStream=async()=>{
        const context=new NativeContext(), source=context.createOscillator(),gain=context.createGain(),output=context.createMediaStreamDestination();
        source.frequency.value=440;gain.gain.value=silence?0:.1;source.connect(gain).connect(output);source.start();await context.resume();
        window.micStreams.push(output.stream);return output.stream;
      };
      Object.defineProperty(navigator.mediaDevices,'getUserMedia',{value:async()=>{
        window.mediaRequests++;
        if(denyMedia)throw new DOMException('Denied for test','NotAllowedError');
        if(deferMedia)return new Promise(resolve=>{window.releaseMic=async()=>resolve(await makeStream())});
        return makeStream();
      }});
    } else window.AudioContext = class {
      constructor() { this.state = 'running'; this.sampleRate = 24000; this.destination = {}; this.audioWorklet = { addModule: async () => {
        window.moduleLoads++;
        if (failAudio) throw new Error('Audio unavailable');
        if (deferAudio) await new Promise(resolve => window.releaseAudio = resolve);
      } }; }
      createGain() { return { connect() { return this; } }; }
      async close() {} async resume() {}
    };
    window.AudioWorkletNode = class {
      constructor() { this.port = { postMessage(message) { window.audioMessages.push(message.t); } }; }
      connect() { return { connect() {} }; }
    };
    const nativeFetch = window.fetch;
    window.fetch = async (url, options = {}) => {
      const name = new URL(url, location.href).pathname;
      if(name.startsWith('/api/'))window.apiRequests.push({path:name,method:options.method||'GET'});
      const headers=Object.fromEntries(new Headers(options.headers));
      if(name.startsWith('/api/') && headers.authorization!=='Bearer browser-test-token-01234567890123456789012345')return Response.json({error:'invalid token'},{status:401});
      if(name==='/api/prep/profiles' && failUpload)return Response.json({error:'test upload unavailable'},{status:503});
      if(name==='/api/preflight'&&failPreflight)return Response.json({error:'test report unavailable'},{status:503});
      if(name==='/api/preflight')return Response.json({status:'not_run',model_loaded:false,performance_verified:false});
      if (name === '/api/health') return Response.json({ ok: true, workers:trainedProfile?[{id:0,healthy:true,worker:{engine:'qwen-adapter-buffered',model_output_mode:'sentence-buffered',dtype:'fp16'}}]:[] });
      if (name === '/api/profiles') return Response.json({ active: 'voice', profiles: Array.from({length:manyProfiles?40:1},(_,index)=>({trained_adapter:trainedProfile?{run_id:'fixture-ui-only'}:undefined,id:index?'voice_'+index:'voice',name:manyProfiles?'档案'+index+'超长声音库名称'.repeat(45):'回归测试声音',ref_text:'你好',breath_files:[],candidates:manyProfiles?[{score:.8,snr_db:20,asr_conf:.9,start:0,end:3,text:'测试候选'}]:[]})) });
      if (name === '/api/telemetry') return Response.json({ ok: true });
      if (name === '/api/report') { window.reports.push(JSON.parse(options.body)); return Response.json({ ok: true }); }
      if (name === '/api/speak') {
        // Deliberately ignore AbortSignal: emulate a late server/proxy response.
        return new Promise(resolve => window.turns.push({ resolve, body: JSON.parse(options.body), headers, signal:options.signal }));
      }
      if (name.startsWith('/api/')) return Response.json({ ok: true });
      return nativeFetch(url, options);
    };
    window.finishTurn = (index, text, hold = false) => {
      const frame = (type, object) => {
        const payload = new TextEncoder().encode(JSON.stringify(object));
        const bytes = new Uint8Array(9 + payload.length); const view = new DataView(bytes.buffer);
        view.setUint8(0, type); view.setUint32(1, 0, true); view.setUint32(5, payload.length, true); bytes.set(payload, 9); return bytes;
      };
      window.turns[index].resolve(new Response(new ReadableStream({ start(controller) {
        controller.enqueue(frame(3, { t: text }));
        if (hold) { window.turns[index].finish = () => { controller.enqueue(frame(5, { timeline_ms: {}, per_gpu: {} })); controller.close(); }; window.finishHeld = window.turns[index].finish; }
        else { controller.enqueue(frame(5, { timeline_ms: {}, per_gpu: {} })); controller.close(); }
      } }), { headers: { 'X-Session-Id': 'test-' + index } }));
    };
  }, { failAudio, deferAudio, realAudio, denyMedia, deferMedia, silence, failUpload, failPreflight, manyProfiles, trainedProfile });
  await page.goto('/qtts-regression');
  // Chromium in this sandbox has no installed CJK fonts. Reuse the repository's
  // licensed local test font, without adding external font requests to the Kaggle bundle.
  await page.addStyleTag({content:'@font-face{font-family:"Noto Sans SC";src:url("/fonts/noto-sans-sc.woff2") format("woff2");font-weight:100 900;font-display:swap}'});
  await page.evaluate(()=>document.fonts.load('14px "Noto Sans SC"','声音台录制参考语音'));
  if(locked)return;
  await page.locator('#access-token').fill('browser-test-token-01234567890123456789012345');
  await page.locator('#btn-unlock').click();
  await expect(page.locator('#profile')).toHaveValue('voice');
  await page.locator('#text').fill('本次请求');
}

test('QTTS key migration clears persisted secrets and new keys stay in memory', async ({ page }) => {
  await openQTTS(page);
  await expect(page.locator('#dskey')).toHaveValue('');
  expect(await page.evaluate(() => localStorage.getItem('qtts_dskey'))).toBeNull();
  await page.locator('#dskey').fill('new-in-memory-key');
  await page.locator('#btn-speak').click();
  await expect.poll(() => page.evaluate(() => window.turns.length)).toBe(1);
  expect(await page.evaluate(() => window.turns[0].headers['x-deepseek-key'])).toBe('new-in-memory-key');
  expect(await page.evaluate(() => localStorage.getItem('qtts_dskey'))).toBeNull();
});

test('QTTS late old response cannot end, overwrite or report the current stream', async ({ page }) => {
  await openQTTS(page);
  await page.locator('#btn-speak').click();
  await expect.poll(() => page.evaluate(() => window.turns.length)).toBe(1);
  await page.locator('#text').press('Control+Enter');
  await expect.poll(() => page.evaluate(() => window.turns.length)).toBe(2);
  await page.evaluate(() => window.finishTurn(1, '新回答', true));
  await expect(page.locator('#llmout')).toHaveText('新回答');
  const ends = await page.evaluate(() => window.audioMessages.filter(x => x === 'end').length);
  await page.evaluate(() => window.finishTurn(0, '过期回答'));
  // Drain pending promises/stream cancellation through a browser task boundary.
  await page.evaluate(() => new Promise(resolve => setTimeout(resolve, 20)));
  await expect(page.locator('#btn-speak')).toBeDisabled();
  await expect(page.locator('#llmout')).toHaveText('新回答');
  expect(await page.evaluate(() => window.audioMessages.filter(x => x === 'end').length)).toBe(ends);
  expect(await page.evaluate(() => window.reports.length)).toBe(0);
  await page.evaluate(() => window.finishHeld());
  await expect(page.locator('#btn-speak')).toBeEnabled();
});

test('QTTS overlapping clicks share audio initialization and only latest starts', async ({ page }) => {
  await openQTTS(page, { deferAudio: true });
  await page.locator('#btn-speak').click();
  await expect.poll(() => page.evaluate(() => typeof window.releaseAudio)).toBe('function');
  await page.locator('#text').fill('较新请求');
  await page.locator('#text').press('Control+Enter');
  await page.evaluate(() => window.releaseAudio());
  await expect.poll(() => page.evaluate(() => window.turns.length)).toBe(1);
  expect(await page.evaluate(() => window.moduleLoads)).toBe(1);
  expect(await page.evaluate(() => window.turns[0].body.text)).toBe('较新请求');
});

test('QTTS audio initialization error stays actionable instead of unhandled rejection', async ({ page }) => {
  const errors = []; page.on('pageerror', error => errors.push(error.message));
  await openQTTS(page, { failAudio: true });
  await page.locator('#btn-speak').click();
  await expect(page.locator('#errbox')).toContainText('Audio unavailable');
  await expect(page.locator('#btn-speak')).toBeEnabled();
  expect(errors).toEqual([]);
});


test('QTTS late old body frame cannot finalize a newer active stream', async ({ page }) => {
  await openQTTS(page);
  await page.locator('#btn-speak').click();
  await expect.poll(() => page.evaluate(() => window.turns.length)).toBe(1);
  await page.evaluate(() => window.finishTurn(0, '旧回答前缀', true));
  await expect(page.locator('#llmout')).toHaveText('旧回答前缀');
  await page.locator('#text').press('Control+Enter');
  await expect.poll(() => page.evaluate(() => window.turns.length)).toBe(2);
  await page.evaluate(() => window.finishTurn(1, '当前回答', true));
  await expect(page.locator('#llmout')).toHaveText('当前回答');
  const ends = await page.evaluate(() => window.audioMessages.filter(x => x === 'end').length);
  await page.evaluate(() => window.turns[0].finish());
  await page.evaluate(() => new Promise(resolve => setTimeout(resolve, 20)));
  await expect(page.locator('#btn-speak')).toBeDisabled();
  await expect(page.locator('#llmout')).toHaveText('当前回答');
  expect(await page.evaluate(() => window.audioMessages.filter(x => x === 'end').length)).toBe(ends);
  await page.evaluate(() => window.turns[1].finish());
  await expect(page.locator('#btn-speak')).toBeEnabled();
});

test('QTTS stop during pending audio initialization prevents a late HTTP request', async ({ page }) => {
  await openQTTS(page, { deferAudio: true });
  await page.locator('#btn-speak').click();
  await expect.poll(() => page.evaluate(() => typeof window.releaseAudio)).toBe('function');
  await page.locator('#btn-stop').click();
  await page.evaluate(() => window.releaseAudio());
  await page.evaluate(() => new Promise(resolve => setTimeout(resolve, 20)));
  expect(await page.evaluate(() => window.turns.length)).toBe(0);
  await expect(page.locator('#btn-speak')).toBeEnabled();
});

test('QTTS starts locked without API calls and rejects incorrect access tokens', async ({ page }) => {
  let calls = 0; page.on('request', request => { if (new URL(request.url()).pathname.startsWith('/api/')) calls++; });
  await openQTTS(page, { locked: true });
  await expect(page.locator('#protected-controls')).toBeHidden();
  await expect(page.locator('#access-status')).toContainText('已锁定');
  expect(calls).toBe(0);
  await page.locator('#access-token').fill('wrong-token-012345678901234567890123456789');
  await page.locator('#btn-unlock').click();
  await expect(page.locator('#access-status')).toContainText('口令无效');
  await expect(page.locator('#protected-controls')).toBeHidden();
});

test('QTTS access token is attached only to same-origin headers and never stored', async ({ page }) => {
  await openQTTS(page);
  await page.locator('#btn-speak').click();
  await expect.poll(() => page.evaluate(() => window.turns.length)).toBe(1);
  expect(await page.evaluate(() => window.turns[0].headers.authorization)).toBe('Bearer browser-test-token-01234567890123456789012345');
  await expect(page.locator('#baseurl')).toHaveAttribute('readonly', '');
  await expect(page.locator('#access-token')).toHaveValue('');
  const stored=await page.evaluate(() => JSON.stringify({local:{...localStorage},session:{...sessionStorage},url:location.href}));
  expect(stored).not.toContain('browser-test-token');
  await page.reload();
  await expect(page.locator('#protected-controls')).toBeHidden();
});

test('QTTS locking aborts the request, hides private data and rejects late frames', async ({ page }) => {
  await openQTTS(page);
  await page.locator('#nav-lab').click();
  await page.locator('#reference-options summary').click();await page.locator('#preftext').fill('私密参考转写');
  await page.locator('#nav-speak').click();
  await page.locator('#dskey').fill('private-provider-key');
  await page.locator('#btn-speak').click();
  await expect.poll(() => page.evaluate(() => window.turns.length)).toBe(1);
  await page.evaluate(() => window.finishTurn(0, '私密回答', true));
  await expect(page.locator('#llmout')).toHaveText('私密回答');
  await page.locator('#btn-lock').click();
  await expect(page.locator('#protected-controls')).toBeHidden();
  expect(await page.evaluate(() => window.turns[0].signal.aborted)).toBe(true);
  await expect(page.locator('#llmout')).toBeEmpty();
  await expect(page.locator('#profile')).toBeEmpty();
  await expect(page.locator('#preftext')).toHaveValue('');
  await expect(page.locator('#dskey')).toHaveValue('');
  await page.evaluate(() => window.turns[0].finish());
  await page.evaluate(() => new Promise(resolve => setTimeout(resolve, 20)));
  await expect(page.locator('#llmout')).toBeEmpty();
});

// Native Chromium analyser/MediaRecorder + oscillator-backed MediaStream input.
// This exercises real browser PCM/container handling, NOT a physical microphone or TTS quality.
test('QTTS native input draws measured waveform, records a container, retains failed uploads and removes local clips', async ({ page }) => {
  await openQTTS(page, { realAudio:true, failUpload:true });
  await page.locator('#nav-lab').click();await page.locator('#btn-rec').click();
  await expect(page.locator('#rec-status')).toContainText('正在采集真实');
  await expect(page.locator('#rec-meter')).toContainText('峰值 0.100');
  const painted=await page.locator('#rec-wave').evaluate(canvas=>[...canvas.getContext('2d').getImageData(0,0,canvas.width,canvas.height).data].some((value,i)=>i%4===3&&value>0));
  expect(painted).toBe(true);
  await page.waitForTimeout(1650);await page.locator('#btn-rec').click();
  await expect(page.locator('#rec-clips')).toContainText('rec_1.webm');
  const file=await page.evaluate(async()=>({size:window.madeFiles[0].size,type:window.madeFiles[0].type,header:[...new Uint8Array(await window.madeFiles[0].slice(0,4).arrayBuffer())],ended:window.micStreams[0].getTracks().every(track=>track.readyState==='ended'),closed:window.captureContexts.every(context=>context.state==='closed')}));
  expect(file.size).toBeGreaterThan(100);expect(file.type).toContain('audio/webm');expect(file.header).toEqual([26,69,223,163]);expect(file.ended&&file.closed).toBe(true);
  await page.locator('#pname').fill('本地录音测试');await page.locator('#btn-create').click();await expect(page.locator('#jobinfo')).toContainText('test upload unavailable');
  await expect(page.locator('#rec-clips')).toContainText('rec_1.webm');
  await page.locator('#rec-clips button').click();await expect(page.locator('#rec-clips')).toBeEmpty();
});

test('QTTS denied microphone permission stays actionable and keeps file upload available',async({page})=>{
  await openQTTS(page,{realAudio:true,denyMedia:true});await page.locator('#nav-lab').click();await page.locator('#btn-rec').click();
  await expect(page.locator('#rec-status')).toContainText('权限被拒绝');await expect(page.locator('#files')).toBeEnabled();
  expect(await page.evaluate(()=>window.captureContexts.length)).toBe(0);
});

test('QTTS lock during pending permission stops a late stream without saving or creating an analyser',async({page})=>{
  await openQTTS(page,{realAudio:true,deferMedia:true});await page.locator('#nav-lab').click();await page.locator('#btn-rec').click();
  await expect(page.locator('#rec-status')).toContainText('等待麦克风权限');await page.locator('#btn-lock').click();
  await page.evaluate(()=>window.releaseMic());
  await expect.poll(()=>page.evaluate(()=>window.micStreams.length===1&&window.micStreams[0].getTracks().every(track=>track.readyState==='ended'))).toBe(true);
  expect(await page.evaluate(()=>window.captureContexts.length)).toBe(0);expect(await page.evaluate(()=>window.madeFiles.length)).toBe(0);
});

test('QTTS lock releases active recording resources and stale stop events cannot restore private clips',async({page})=>{
  await openQTTS(page,{realAudio:true});await page.locator('#nav-lab').click();await page.locator('#btn-rec').click();
  await expect(page.locator('#rec-status')).toContainText('正在采集真实');await page.locator('#btn-lock').click();
  await expect.poll(()=>page.evaluate(()=>window.micStreams[0].getTracks().every(track=>track.readyState==='ended')&&window.captureContexts.every(context=>context.state==='closed'))).toBe(true);
  await page.locator('#access-token').fill('browser-test-token-01234567890123456789012345');await page.locator('#btn-unlock').click();await expect(page.locator('#profile')).toHaveValue('voice');await page.locator('#nav-lab').click();await expect(page.locator('#rec-clips')).toBeEmpty();
  expect(await page.evaluate(()=>window.madeFiles.length)).toBe(0);
  await expect(page.locator('#rec-meter')).toHaveText('未采集');
});

test('QTTS native silent input reports zero peak instead of a simulated waveform',async({page})=>{
  await openQTTS(page,{realAudio:true,silence:true});await page.locator('#nav-lab').click();await page.locator('#btn-rec').click();
  await expect(page.locator('#rec-meter')).toContainText('RMS -120.0 dBFS · 峰值 0.000');
  await page.locator('#btn-rec').click();await expect(page.locator('#btn-rec')).toHaveText('● 录音');expect(await page.evaluate(()=>window.captureContexts.every(context=>context.state==='closed'))).toBe(true);
});

test('QTTS native recorder enforces byte and time budgets and releases resources',async({page})=>{
  await openQTTS(page,{realAudio:true});
  for(const byteLimit of [1,20*1024*1024]) {
    await page.evaluate(async limit=>{
      window.budgetClips=[];window.budgetStatuses=[];
      window.budgetRecorder=new window.QttsMicrophoneRecorder({maxClipBytes:limit,maxDurationMs:600,minDurationMs:0,onClip:file=>window.budgetClips.push(file),onStatus:(state,message)=>window.budgetStatuses.push({state,message})});
      await window.budgetRecorder.start();
    },byteLimit);
    await expect.poll(()=>page.evaluate(()=>window.budgetRecorder.state)).toBe('idle');
    const result=await page.evaluate(()=>({clips:window.budgetClips.length,messages:window.budgetStatuses.map(s=>s.message).join('|'),closed:window.captureContexts.every(context=>context.state==='closed'),ended:window.micStreams.every(stream=>stream.getTracks().every(track=>track.readyState==='ended'))}));
    expect(result.closed&&result.ended).toBe(true);expect(result.clips).toBe(byteLimit===1?0:1);expect(result.messages).toContain(byteLimit===1?'字节预算':'时长预算');
  }
});

test('QTTS recording count budget rejects extra input without opening a microphone',async({page})=>{
  await openQTTS(page,{realAudio:true});await page.locator('#nav-lab').click();
  await page.locator('#files').setInputFiles(Array.from({length:16},(_,i)=>({name:`ref${i}.wav`,mimeType:'audio/wav',buffer:Buffer.from('test-only')})));
  await page.locator('#btn-rec').click();await expect(page.locator('#rec-status')).toContainText('预算已满');expect(await page.evaluate(()=>window.mediaRequests)).toBe(0);
});

test('QTTS compatibility report is read-only monitor data and never implies model readiness',async({page})=>{
  await openQTTS(page);await page.locator('#nav-mon').click();
  await expect(page.locator('#preflight-output')).toContainText('not_run');await expect(page.locator('#preflight-output')).toContainText('不代表模型、训练或性能通过');
  const calls=await page.evaluate(()=>window.apiRequests.filter(r=>r.path==='/api/preflight'));
  expect(calls.length).toBeGreaterThan(0);expect(calls.every(call=>call.method==='GET')).toBe(true);
});

test('QTTS cancelled pending permission does not accumulate concurrent device requests',async({page})=>{
  await openQTTS(page,{realAudio:true,deferMedia:true});await page.locator('#nav-lab').click();await page.locator('#btn-rec').click();
  await expect(page.locator('#rec-status')).toContainText('等待麦克风权限');await page.locator('#btn-rec').click();await page.locator('#btn-rec').click();
  await expect(page.locator('#rec-status')).toContainText('上一次麦克风权限请求尚未返回');
  expect(await page.evaluate(()=>window.mediaRequests)).toBe(1);await page.evaluate(()=>window.releaseMic());
  await expect.poll(()=>page.evaluate(()=>window.micStreams[0]?.getTracks().every(track=>track.readyState==='ended'))).toBe(true);
});

test('QTTS device-ended lifecycle stops native capture and releases the context',async({page})=>{
  await openQTTS(page,{realAudio:true});await page.locator('#nav-lab').click();await page.locator('#btn-rec').click();
  await expect(page.locator('#rec-status')).toContainText('正在采集真实');
  await page.waitForTimeout(1600);
  // Software dispatch tests the ended handler; no claim of unplugging physical hardware.
  await page.evaluate(()=>{const track=window.micStreams[0].getAudioTracks()[0];track.stop();track.dispatchEvent(new Event('ended'))});
  await expect.poll(()=>page.evaluate(()=>window.captureContexts.every(context=>context.state==='closed'))).toBe(true);
  await expect(page.locator('#btn-rec')).toHaveText('● 录音');await expect(page.locator('#rec-clips')).toContainText('rec_1.webm');
});

test('QTTS pagehide cancels native capture without preserving private audio',async({page})=>{
  await openQTTS(page,{realAudio:true});await page.locator('#nav-lab').click();await page.locator('#btn-rec').click();
  await expect(page.locator('#rec-status')).toContainText('正在采集真实');await page.evaluate(()=>window.dispatchEvent(new Event('pagehide')));
  await expect.poll(()=>page.evaluate(()=>window.micStreams[0].getTracks().every(track=>track.readyState==='ended')&&window.captureContexts.every(context=>context.state==='closed'))).toBe(true);
  await expect(page.locator('#rec-clips')).toBeEmpty();
});

test('QTTS unavailable preflight report does not break the existing health monitor',async({page})=>{
  await openQTTS(page,{failPreflight:true});await page.locator('#nav-mon').click();
  await expect(page.locator('#preflight-output')).toContainText('test report unavailable');expect(await page.evaluate(()=>window.apiRequests.some(call=>call.path==='/api/metrics'))).toBe(true);await expect(page.locator('#mon-agg')).toContainText('系统聚合速度');
});

test('QTTS native recorder bounds retained data chunk count independently of bytes',async({page})=>{
  await openQTTS(page,{realAudio:true});
  await page.evaluate(async()=>{
    window.chunkClips=[];window.chunkMessage='';
    window.chunkRecorder=new window.QttsMicrophoneRecorder({maxChunks:0,maxDurationMs:3000,onClip:file=>window.chunkClips.push(file),onStatus:(_state,message)=>{window.chunkMessage=message}});
    await window.chunkRecorder.start();
  });
  await expect.poll(()=>page.evaluate(()=>window.chunkRecorder.state)).toBe('idle');
  expect(await page.evaluate(()=>window.chunkMessage)).toContain('分块数量超过预算');expect(await page.evaluate(()=>window.chunkClips.length)).toBe(0);
});

test('QTTS missing native recorder stop callback has a bounded discard and cleanup path',async({page})=>{
  await openQTTS(page,{realAudio:true});
  await page.evaluate(async()=>{
    const Native=window.MediaRecorder;
    window.MediaRecorder=class extends Native{stop(){this.onstop=null;super.stop()}};
    window.fallbackClips=[];window.fallbackMessage='';
    window.fallbackRecorder=new window.QttsMicrophoneRecorder({maxDurationMs:300,minDurationMs:0,onClip:file=>window.fallbackClips.push(file),onStatus:(_state,message)=>{window.fallbackMessage=message}});
    await window.fallbackRecorder.start();
  });
  await expect.poll(()=>page.evaluate(()=>window.fallbackRecorder.state)).toBe('idle');
  expect(await page.evaluate(()=>window.fallbackMessage)).toContain('封装超时');expect(await page.evaluate(()=>window.fallbackClips.length)).toBe(0);
  expect(await page.evaluate(()=>window.captureContexts.every(context=>context.state==='closed')&&window.micStreams.every(stream=>stream.getTracks().every(track=>track.readyState==='ended')))).toBe(true);
});

async function expectInsideViewport(page,selector){
  const result=await page.locator(selector).evaluate(element=>{
    const box=element.getBoundingClientRect();
    const center=document.elementFromPoint(box.x+box.width/2,box.y+box.height/2);
    let unclipped=true;
    for(let parent=element.parentElement;parent;parent=parent.parentElement){
      const style=getComputedStyle(parent),clip=parent.getBoundingClientRect();
      if(['auto','hidden','scroll'].includes(style.overflowY)&& (box.top<clip.top+parent.clientTop-1||box.bottom>clip.top+parent.clientTop+parent.clientHeight+1))unclipped=false;
      if(['auto','hidden','scroll'].includes(style.overflowX)&& (box.left<clip.left+parent.clientLeft-1||box.right>clip.left+parent.clientLeft+parent.clientWidth+1))unclipped=false;
    }
    return {visible:unclipped&&box.width>0&&box.height>0&&box.x>=0&&box.y>=0&&box.right<=innerWidth+1&&box.bottom<=innerHeight+1,hit:center===element||element.contains(center)};
  });
  expect(result,selector).toEqual({visible:true,hit:true});
}
for(const [width,height] of [[1440,900],[1024,768],[768,1024],[390,844],[375,667]]){
  test(`QTTS two primary views keep essential actions inside ${width}x${height}`,async({page})=>{
    await page.setViewportSize({width,height});await openQTTS(page);
    await expect(page.getByRole('navigation',{name:'主要视图'}).getByRole('button')).toHaveCount(2);
    await expect(page.locator('#nav-speak')).toHaveAttribute('aria-pressed','true');await expect(page.locator('#tab-lab')).toBeHidden();
    for(const selector of ['#mode','#profile','#text','#btn-speak','#btn-stop','#nav-mon','#btn-lock'])await expectInsideViewport(page,selector);
    expect(await page.evaluate(()=>document.documentElement.scrollHeight<=innerHeight+1&&document.documentElement.scrollWidth<=innerWidth+1)).toBe(true);
    if(width===1440||width===375)await page.screenshot({path:`docs/validation/step6/chat-${width}x${height}.png`});
    await page.locator('#nav-lab').click();await expect(page.locator('#nav-lab')).toHaveAttribute('aria-pressed','true');await expect(page.locator('#tab-speak')).toBeHidden();
    for(const selector of ['#pname','#files','#btn-rec','#btn-create','#rec-wave','#btn-reference-options'])await expectInsideViewport(page,selector);
    expect(await page.locator('#profiles').evaluate(element=>element.clientHeight)).toBeGreaterThan(40);
    if(width===1440||width===375)await page.screenshot({path:`docs/validation/step6/reference-${width}x${height}.png`});
    expect(await page.evaluate(()=>document.documentElement.scrollHeight<=innerHeight+1&&document.documentElement.scrollWidth<=innerWidth+1)).toBe(true);
  });
}

test('QTTS diagnostic modal closes with Escape, restores focus and preserves selected main view',async({page})=>{
  await openQTTS(page);await page.locator('#nav-lab').click();await page.locator('#nav-mon').click();
  await expect(page.getByRole('dialog',{name:'诊断与高级信息'})).toBeVisible();await expect(page.locator('#btn-close-diagnostics')).toBeFocused();
  await page.keyboard.press('Escape');await expect(page.locator('#diagnostics')).not.toBeVisible();await expect(page.locator('#nav-mon')).toBeFocused();
  await expect(page.locator('#nav-lab')).toHaveAttribute('aria-pressed','true');await expect(page.locator('#tab-lab')).toBeVisible();
  await page.locator('#nav-mon').click();await page.locator('#btn-close-diagnostics').click();await expect(page.locator('#nav-mon')).toBeFocused();
});

test('QTTS keyboard navigation selects two primary views and hidden panels are not focusable',async({page})=>{
  await openQTTS(page);await page.locator('#nav-speak').focus();await page.keyboard.press('ArrowLeft');
  await expect(page.locator('#nav-lab')).toBeFocused();await expect(page.locator('#nav-lab')).toHaveAttribute('aria-pressed','true');
  expect(await page.locator('#text').evaluate(element=>{element.focus();return document.activeElement===element})).toBe(false);
  await page.keyboard.press('End');await expect(page.locator('#nav-speak')).toBeFocused();await expect(page.locator('#nav-speak')).toHaveAttribute('aria-pressed','true');
  await page.keyboard.press('Home');await expect(page.locator('#nav-lab')).toBeFocused();
});

test('QTTS diagnostic lock closes modal, clears private results and restores accessible login',async({page})=>{
  await openQTTS(page);await page.locator('#nav-mon').click();await expect(page.locator('#preflight-output')).toContainText('not_run');
  await page.locator('#btn-lock-dialog').click();await expect(page.locator('#diagnostics')).not.toBeVisible();await expect(page.locator('#protected-controls')).toBeHidden();
  await expect(page.locator('#preflight-output')).toBeEmpty();await expect(page.locator('#access-token')).toBeVisible();await expect(page.locator('#access-token')).toBeFocused();await expect(page.locator('#nav-mon')).toBeDisabled();
});

test('QTTS switching to recording stops pending speech initialization and late HTTP requests',async({page})=>{
  await openQTTS(page,{deferAudio:true});await page.locator('#btn-speak').click();await expect.poll(()=>page.evaluate(()=>typeof window.releaseAudio)).toBe('function');
  await page.locator('#nav-lab').click();await page.evaluate(()=>window.releaseAudio());
  await page.evaluate(()=>new Promise(resolve=>setTimeout(resolve,20)));expect(await page.evaluate(()=>window.turns.length)).toBe(0);
});

test('QTTS switching away from recording stops native capture but keeps a valid local clip',async({page})=>{
  await openQTTS(page,{realAudio:true});await page.locator('#nav-lab').click();await page.locator('#btn-rec').click();await expect(page.locator('#rec-status')).toContainText('正在采集真实');
  await page.waitForTimeout(1600);await page.locator('#nav-speak').click();
  await expect.poll(()=>page.evaluate(()=>window.micStreams[0].getTracks().every(track=>track.readyState==='ended')&&window.captureContexts.every(context=>context.state==='closed'))).toBe(true);
  await page.locator('#nav-lab').click();await expect(page.locator('#rec-clips')).toContainText('rec_1.webm');
});

test('QTTS short CSS viewport degrades to scrollable content without losing primary actions',async({page})=>{
  await page.setViewportSize({width:375,height:480});await openQTTS(page);await page.locator('#btn-stop').scrollIntoViewIfNeeded();await expectInsideViewport(page,'#btn-stop');
  await page.locator('#nav-lab').click();await page.locator('#btn-create').scrollIntoViewIfNeeded();await expectInsideViewport(page,'#btn-create');
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1)).toBe(true);
});

test('QTTS long text and many long-named profiles scroll locally without moving essential actions',async({page})=>{
  await page.setViewportSize({width:375,height:667});await openQTTS(page,{manyProfiles:true});await page.locator('#btn-speak').click();await expect.poll(()=>page.evaluate(()=>window.turns.length)).toBe(1);
  await page.evaluate(()=>window.finishTurn(0,'长回答与连续文字'.repeat(1600),true));
  await expect.poll(()=>page.locator('#llmout').evaluate(element=>element.scrollHeight>element.clientHeight)).toBe(true);
  await page.locator('#llmout').focus();await page.keyboard.press('End');await expect.poll(()=>page.locator('#llmout').evaluate(element=>element.scrollTop)).toBeGreaterThan(0);
  await expectInsideViewport(page,'#btn-stop');await page.locator('#nav-lab').click();await expect(page.locator('#profiles .card')).toHaveCount(40);
  await page.locator('#profiles .card').last().getByRole('button',{name:'删除',exact:true}).scrollIntoViewIfNeeded();
  for(const selector of ['#btn-rec','#btn-create','#nav-speak'])await expectInsideViewport(page,selector);
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1&&document.documentElement.scrollHeight<=innerHeight+1)).toBe(true);
});

test('QTTS existing voice text, candidate, activation and calibration actions remain reachable',async({page})=>{
  await openQTTS(page,{manyProfiles:true});await page.locator('#nav-lab').click();await expect(page.locator('#profiles .card')).toHaveCount(40);
  await page.locator('#profiles .reftext').first().fill('更新参考文本');await page.locator('#profiles .card').first().getByRole('button',{name:'保存文本并重载',exact:true}).click();
  await expect.poll(()=>page.evaluate(()=>window.apiRequests.some(call=>call.path==='/api/prep/profiles/voice/text'&&call.method==='POST'))).toBe(true);
  await page.locator('#profiles .card').first().locator('.cand').click();
  await expect.poll(()=>page.evaluate(()=>window.apiRequests.some(call=>call.path==='/api/prep/profiles/voice/candidate'))).toBe(true);
  await page.locator('#profiles .card').first().getByRole('button',{name:/启用此声音/}).click();
  await expect.poll(()=>page.evaluate(()=>window.apiRequests.some(call=>call.path==='/api/profiles/activate'))).toBe(true);
  await page.locator('#profiles .card').first().getByRole('button',{name:/候选校准/}).click();
  await expect.poll(()=>page.evaluate(()=>window.apiRequests.some(call=>call.path==='/api/prep/profiles/voice/calibrate'))).toBe(true);
  // HTTP handlers are fixtures: checking reachable operations, never actual GPU calibration.
});

test('QTTS diagnostic polling is sequential, aborts on close, and ignores late reports across reopening',async({page})=>{
  await openQTTS(page);await page.clock.install();
  await page.evaluate(()=>{
    const original=window.fetch;window.probeRequests=[];
    window.fetch=async(url,options={})=>{
      if(new URL(url,location.href).pathname==='/api/preflight')return new Promise(resolve=>window.probeRequests.push({resolve,signal:options.signal}));
      return original(url,options);
    };
  });
  await page.locator('#nav-mon').click();await expect.poll(()=>page.evaluate(()=>window.probeRequests.length)).toBe(1);
  await page.clock.fastForward(6000);expect(await page.evaluate(()=>window.probeRequests.length)).toBe(1);
  // Close/reopen in one task exercises late native `close` events as well.
  await page.evaluate(()=>{document.getElementById('btn-close-diagnostics').click();document.getElementById('nav-mon').click()});
  await expect.poll(()=>page.evaluate(()=>window.probeRequests.length)).toBe(2);expect(await page.evaluate(()=>window.probeRequests[0].signal.aborted)).toBe(true);
  await page.evaluate(()=>window.probeRequests[1].resolve(Response.json({status:'CURRENT_TEST_REPORT',model_loaded:false})));
  await expect(page.locator('#preflight-output')).toContainText('CURRENT_TEST_REPORT');
  await page.evaluate(()=>window.probeRequests[0].resolve(Response.json({status:'STALE_TEST_REPORT',model_loaded:false})));
  await page.evaluate(()=>new Promise(resolve=>queueMicrotask(resolve)));await expect(page.locator('#preflight-output')).not.toContainText('STALE_TEST_REPORT');
  await page.locator('#btn-close-diagnostics').click();await page.clock.fastForward(10000);expect(await page.evaluate(()=>window.probeRequests.length)).toBe(2);expect(await page.evaluate(()=>window.probeRequests[1].signal.aborted)).toBe(true);
});

test('QTTS diagnostics stop native microphone capture rather than hide it behind a modal',async({page})=>{
  await openQTTS(page,{realAudio:true});await page.locator('#nav-lab').click();await page.locator('#btn-rec').click();await expect(page.locator('#rec-status')).toContainText('正在采集真实');
  await page.waitForTimeout(1600);await page.locator('#nav-mon').click();
  await expect.poll(()=>page.evaluate(()=>window.micStreams[0].getTracks().every(track=>track.readyState==='ended')&&window.captureContexts.every(context=>context.state==='closed'))).toBe(true);
  await page.locator('#btn-close-diagnostics').click();await expect(page.locator('#rec-clips')).toContainText('rec_1.webm');
});

test('QTTS voice library needs a custom name and never uploads unnamed references',async({page})=>{
  await openQTTS(page,{failUpload:true});await page.locator('#nav-lab').click();
  await expect(page.locator('#pname')).toHaveValue('');await page.locator('#files').setInputFiles({name:'local.wav',mimeType:'audio/wav',buffer:Buffer.from('fixture-only')});
  await page.locator('#btn-create').click();await expect(page.locator('#jobinfo')).toContainText('自行填写1至64字符');
  expect(await page.evaluate(()=>window.apiRequests.filter(call=>call.path==='/api/prep/profiles').length)).toBe(0);
  expect(await page.locator('#files').evaluate(element=>element.files.length)).toBe(1);
  await page.locator('#pname').fill('界'.repeat(65));await page.locator('#btn-create').click();
  expect(await page.evaluate(()=>window.apiRequests.filter(call=>call.path==='/api/prep/profiles').length)).toBe(0);
  await page.locator('#pname').fill('自己的声音库');await page.locator('#btn-create').click();await expect(page.locator('#jobinfo')).toContainText('test upload unavailable');
  expect(await page.locator('#files').evaluate(element=>element.files.length)).toBe(1);
});

test('QTTS mobile optional reference settings have a visible explicit entry and remain keyboard reachable',async({page})=>{
  await page.setViewportSize({width:375,height:667});await openQTTS(page);await page.locator('#nav-lab').click();await expectInsideViewport(page,'#btn-reference-options');
  await page.locator('#btn-reference-options').click();await expect(page.locator('#btn-reference-options')).toHaveAttribute('aria-expanded','true');
  await expect(page.locator('#reference-options summary')).toBeFocused();await page.keyboard.press('Tab');await expect(page.locator('#preftext')).toBeFocused();
  await page.locator('#preftext').fill('自己的参考转写');await page.locator('#pcal').uncheck();
  await page.locator('#btn-reference-options').click();await expect(page.locator('#btn-reference-options')).toHaveAttribute('aria-expanded','false');await expectInsideViewport(page,'#files');
  expect(await page.evaluate(()=>document.documentElement.scrollHeight<=innerHeight+1)).toBe(true);
});

for(const withEnded of [true,false]){
  test(`QTTS native auto-stop preserves a valid clip with ended handler=${withEnded}`,async({page})=>{
    await openQTTS(page,{realAudio:true});
    await page.evaluate(()=>{
      const Native=window.MediaRecorder;
      window.MediaRecorder=class extends Native{constructor(...args){super(...args);window.lastNativeRecorder=this}};
    });
    await page.locator('#nav-lab').click();await page.locator('#btn-rec').click();await expect(page.locator('#rec-status')).toContainText('正在采集真实');await page.waitForTimeout(1600);
    await page.evaluate(ended=>{
      window.lastNativeRecorder.stop(); // synchronously sets inactive, queues final events
      if(ended){const track=window.micStreams[0].getAudioTracks()[0];track.stop();track.dispatchEvent(new Event('ended'))}
    },withEnded);
    await expect(page.locator('#rec-clips')).toContainText('rec_1.webm');await expect(page.locator('#btn-rec')).toHaveText('● 录音');
    expect(await page.evaluate(()=>window.captureContexts.every(context=>context.state==='closed')&&window.micStreams[0].getTracks().every(track=>track.readyState==='ended'))).toBe(true);
  });
}

test('QTTS minimum duration gate rejects a clock-injected 100ms clip without wall-clock timing assumptions',async({page})=>{
  await openQTTS(page,{realAudio:true});
  await page.evaluate(async()=>{
    window.shortClips=[];window.shortMessage='';window.shortRecorder=new window.QttsMicrophoneRecorder({maxDurationMs:10000,onClip:file=>window.shortClips.push(file),onStatus:(_state,message)=>{window.shortMessage=message}});
    await window.shortRecorder.start();window.shortSession=window.shortRecorder.session;
  });
  await page.waitForTimeout(350);
  expect(await page.evaluate(()=>window.shortRecorder.minDurationMs)).toBe(1500);
  await page.evaluate(()=>{
    const descriptor=Object.getOwnPropertyDescriptor(performance,'now');
    Object.defineProperty(performance,'now',{configurable:true,value:()=>window.shortSession.startedAt+100});
    try{window.shortRecorder.stop()}finally{if(descriptor)Object.defineProperty(performance,'now',descriptor);else delete performance.now}
  });
  await expect.poll(()=>page.evaluate(()=>window.shortRecorder.state)).toBe('idle');
  expect(await page.evaluate(()=>window.shortClips.length)).toBe(0);expect(await page.evaluate(()=>window.shortMessage)).toContain('不足1.5秒');
  expect(await page.evaluate(()=>window.shortSession.durationMs)).toBe(100);
  expect(await page.evaluate(()=>window.shortSession.bytes)).toBeGreaterThan(0);
});

// Library browser tests deliberately use a protocol fixture. Real disk/CAS/flock
// and multipart checks live in test_libraries.py; this is NOT GPU/model evidence.
async function installLibraryFixture(page) {
  await page.evaluate(() => {
    const previous = window.fetch;
    window.libraryStore = []; window.libraryRequests = []; window.libraryProcess = null;
    window.trainingDatasets = [];window.trainingRequests = [];
    let sequence = 0, sampleSequence = 0;
    const snapshot = row => JSON.parse(JSON.stringify(row));
    window.finishLibrary = (failed = false) => {
      const row=window.libraryStore.find(row=>row.busy);if(!row)return;
      row.busy=false;row.state=failed?'processing_failed':'reference_prepared';
      row.last_build.state=row.state;row.prepared_profile=failed?null:'prepared-voice';
    };
    window.fetch = async (url, options = {}) => {
      const path = new URL(url, location.href).pathname;
      if(path.startsWith('/api/prep/training-data')){
        const method=options.method||'GET';window.trainingRequests.push({path,method});
        if(new Headers(options.headers).get('Authorization')!=='Bearer browser-test-token-01234567890123456789012345')return Response.json({error:'invalid token'},{status:401});
        const parts=path.slice('/api/prep/training-data'.length).split('/').filter(Boolean);
        if(method==='GET')return Response.json({datasets:JSON.parse(JSON.stringify(window.trainingDatasets))});
        const body=JSON.parse(options.body);
        if(method==='POST'&&!parts.length){
          window.trainingLastBody=body;
          if(window.trainingRejectWav)return Response.json({error:'only mono 24kHz PCM16 WAV accepted'},{status:400});
          const source=window.libraryStore.find(row=>row.id===body.library_id);
          const dataset={id:String(window.trainingDatasets.length+1).padStart(32,'d'),state:'input_snapshot_ready',library_id:source.id,library_name:source.name,sample_count:body.samples.length,manifest_sha256:'a'.repeat(64),integrity_verified_now:true,checks:{training_verified:false,two_rank_execution_verified:false,tokenization_verified:false}};
          window.trainingDatasets.unshift(dataset);const response=Response.json({dataset});
          if(window.trainingDeferPrepare)return new Promise(resolve=>window.releaseTrainingPrepare=()=>resolve(response));
          return response;
        }
        const row=window.trainingDatasets.find(row=>row.id===parts[0]);
        if(!row)return Response.json({error:'missing dataset'},{status:404});
        if(method==='POST'&&parts[1]==='verify'){
          if(window.trainingTampered)return Response.json({error:'training input hash changed'},{status:409});
          return Response.json({dataset:{...row,integrity_verified_now:true}});
        }
        if(method==='DELETE'){window.trainingDatasets=window.trainingDatasets.filter(item=>item!==row);return Response.json({deleted:row.id});}
      }
      if(!path.startsWith('/api/prep/libraries'))return previous(url,options);
      const method=options.method||'GET';
      window.apiRequests.push({path,method});window.libraryRequests.push({path,method});
      if(new Headers(options.headers).get('Authorization')!=='Bearer browser-test-token-01234567890123456789012345')return Response.json({error:'invalid token'},{status:401});
      const parts=path.slice('/api/prep/libraries'.length).split('/').filter(Boolean);
      if(method==='GET'&&!parts.length)return Response.json({libraries:snapshot(window.libraryStore)});
      if(method==='POST'&&!parts.length){
        const body=JSON.parse(options.body);
        if(window.libraryStore.some(row=>row.name===body.name))return Response.json({error:'duplicate name'},{status:409});
        const row={id:String(++sequence).padStart(32,'0'),name:body.name,language:body.language,revision:1,samples:[],bytes:0,state:'empty',busy:false,last_build:null,prepared_profile:null,training_verified:false,inference_verified:false};
        window.libraryStore.unshift(row);const response=Response.json({library:snapshot(row)});
        if(window.libraryDeferCreate)return new Promise(resolve=>window.releaseLibraryCreate=()=>resolve(response));
        return response;
      }
      const row=window.libraryStore.find(row=>row.id===parts[0]);
      if(!row)return Response.json({error:'no library'},{status:404});
      if(method==='GET'){
        const response=Response.json({library:snapshot(row)});
        if(window.libraryDeferPoll)return new Promise(resolve=>window.releaseLibraryPoll=()=>resolve(response));
        return response;
      }
      if(method==='POST'&&parts[1]==='samples'){
        if(window.libraryFailUpload)return Response.json({error:'upload unavailable'},{status:503});
        if(Number(options.body.get('revision'))!==row.revision)return Response.json({error:'library changed; refresh'},{status:409});
        for(const file of options.body.getAll('files')){
          const digest=Array.from(new Uint8Array(await file.arrayBuffer())).join(',');
          if(!row.samples.some(sample=>sample.sha256===digest))row.samples.push({id:(++sampleSequence).toString(16).padStart(32,'0'),name:file.name,bytes:file.size,sha256:digest});
        }
        row.bytes=row.samples.reduce((sum,sample)=>sum+sample.bytes,0);row.revision++;row.state='samples_unverified';
        return Response.json({library:snapshot(row)});
      }
      const data=JSON.parse(options.body);
      if(data.revision!==row.revision)return Response.json({error:'library changed; refresh'},{status:409});
      if(method==='POST'&&parts[1]==='process'){
        window.libraryProcess={...data,library:row.id};row.busy=true;row.state='processing';row.last_build={job:'library-job',state:'running'};
        return Response.json({job:'library-job',library:row.id,operation:'reference_processing_not_training'});
      }
      if(method==='DELETE'&&parts[1]==='samples'){
        row.samples=row.samples.filter(sample=>sample.id!==parts[2]);row.revision++;row.bytes=row.samples.reduce((sum,sample)=>sum+sample.bytes,0);
        row.state=row.samples.length?'samples_unverified':'empty';const response=Response.json({library:snapshot(row)});
        if(window.libraryDeferRemove)return new Promise(resolve=>window.releaseLibraryRemove=()=>resolve(response));
        return response;
      }
      if(method==='DELETE'){
        window.libraryStore=window.libraryStore.filter(item=>item!==row);return Response.json({deleted:row.id,prepared_profiles_deleted:false});
      }
      return Response.json({error:'fixture route missing'},{status:404});
    };
  });
}
async function openLibraries(page, options) {
  await openQTTS(page, options); await installLibraryFixture(page);
  await page.locator('#nav-lab').click();await page.locator('#btn-libraries').click();
  await expect(page.locator('#btn-library-refresh')).toBeEnabled();
}
async function createLibrary(page, name='用户自己的库') {
  await page.locator('#library-name').fill(name);await page.locator('#btn-library-create').click();
  await expect(page.locator('#library-message')).toContainText('命名空库已保存');
}
async function uploadLibrary(page) {
  await page.locator('#library-files').setInputFiles([{name:'one.wav',mimeType:'audio/wav',buffer:Buffer.from('first')},{name:'two.wav',mimeType:'audio/wav',buffer:Buffer.from('second')}]);
  await page.locator('#btn-library-upload').click();await expect(page.locator('#library-message')).toContainText('原始样本已保存');
}

test('QTTS library named empty first, upload, select one and process without claiming training', async ({page})=>{
  await openLibraries(page);await expect(page.locator('#library-name')).toHaveValue('');await expect(page.locator('#btn-library-upload')).toBeDisabled();
  await createLibrary(page);await expect(page.locator('#library-state')).toContainText('命名空库');await expect(page.locator('#profile option')).toHaveCount(1);
  await uploadLibrary(page);await expect(page.locator('#library-samples input')).toHaveCount(2);await expect(page.locator('#btn-library-process')).toBeDisabled();
  await page.getByRole('checkbox',{name:'选择样本 two.wav',exact:true}).check();await page.locator('#library-reftext').fill('自己填写的参考');await page.locator('#library-calibrate').uncheck();
  await page.locator('#btn-library-process').click();await expect(page.locator('#library-message')).toContainText('任务已受理');
  const process=await page.evaluate(()=>window.libraryProcess);expect(process.sample_ids).toHaveLength(1);expect(process.ref_text).toBe('自己填写的参考');expect(process.calibrate).toBe(false);
  await page.evaluate(()=>window.finishLibrary());await expect(page.locator('#library-state')).toContainText('参考已处理');await expect(page.locator('#library-state')).toContainText('未训练');
});

test('QTTS library blank name is not defaulted and empty file does not submit',async({page})=>{
  await openLibraries(page);await page.locator('#btn-library-create').click();await expect(page.locator('#library-message')).toContainText('1–64');
  expect(await page.evaluate(()=>window.libraryRequests.filter(r=>r.method==='POST').length)).toBe(0);
  await createLibrary(page);await page.locator('#library-files').setInputFiles({name:'empty.wav',mimeType:'audio/wav',buffer:Buffer.alloc(0)});
  await page.locator('#btn-library-upload').click();await expect(page.locator('#library-message')).toContainText('空文件');
  expect(await page.evaluate(()=>window.libraryRequests.some(r=>r.path.endsWith('/samples')))).toBe(false);
});

test('QTTS library upload failure preserves selected files for retry and never advances state',async({page})=>{
  await openLibraries(page);await createLibrary(page);await page.evaluate(()=>window.libraryFailUpload=true);
  await page.locator('#library-files').setInputFiles({name:'keep.wav',mimeType:'audio/wav',buffer:Buffer.from('keep')});
  await page.locator('#btn-library-upload').click();await expect(page.locator('#library-message')).toContainText('upload unavailable');
  expect(await page.locator('#library-files').evaluate(input=>input.files.length)).toBe(1);await expect(page.locator('#library-state')).toContainText('命名空库');
  await page.evaluate(()=>window.libraryFailUpload=false);await page.locator('#btn-library-upload').click();await expect(page.locator('#library-message')).toContainText('原始样本已保存');
  expect(await page.locator('#library-files').evaluate(input=>input.files.length)).toBe(0);
});

test('QTTS library stale revision retains local data and refresh allows deliberate retry',async({page})=>{
  await openLibraries(page);await createLibrary(page);await page.locator('#library-files').setInputFiles({name:'keep.wav',mimeType:'audio/wav',buffer:Buffer.from('keep')});
  await page.evaluate(()=>window.libraryStore[0].revision++);await page.locator('#btn-library-upload').click();await expect(page.locator('#library-message')).toContainText('library changed');
  expect(await page.locator('#library-files').evaluate(input=>input.files.length)).toBe(1);await page.locator('#btn-library-refresh').click();await expect(page.locator('#btn-library-refresh')).toBeEnabled();
  await page.locator('#btn-library-upload').click();await expect(page.locator('#library-message')).toContainText('原始样本已保存');
});

test('QTTS library sample removal and confirmed whole-library deletion leave processed profiles alone',async({page})=>{
  await openLibraries(page);await createLibrary(page);await uploadLibrary(page);
  await page.getByRole('button',{name:'移除样本 one.wav',exact:true}).click();await expect(page.locator('#library-samples input')).toHaveCount(1);
  await page.locator('#library-delete-options summary').click();await page.locator('#btn-library-delete').click();await expect(page.locator('#library-message')).toContainText('独立声音档案未删除');
  await expect(page.locator('#library-select option')).toHaveCount(0);await page.locator('#btn-library-close').click();await expect(page.locator('#profiles')).toContainText('回归测试声音');
});

test('QTTS library failed processing retains selected raw samples and does not claim success',async({page})=>{
  await openLibraries(page);await createLibrary(page);await uploadLibrary(page);await page.getByRole('checkbox',{name:'选择样本 one.wav',exact:true}).check();
  await page.locator('#btn-library-process').click();await expect(page.locator('#library-message')).toContainText('任务已受理');
  await expect(page.locator('#btn-library-delete')).toBeDisabled();await page.evaluate(()=>window.finishLibrary(true));
  await expect(page.locator('#library-state')).toContainText('处理失败');await expect(page.locator('#library-samples input')).toHaveCount(2);await expect(page.locator('#btn-library-process')).toBeEnabled();
});

test('QTTS library lock clears private form, sample names and ignores late creation response',async({page})=>{
  await openLibraries(page);await page.evaluate(()=>window.libraryDeferCreate=true);await page.locator('#library-name').fill('私密迟到库');await page.locator('#btn-library-create').click();
  await expect.poll(()=>page.evaluate(()=>typeof window.releaseLibraryCreate)).toBe('function');await page.locator('#btn-library-lock').click();
  await page.evaluate(()=>window.releaseLibraryCreate());await page.evaluate(()=>new Promise(resolve=>setTimeout(resolve,20)));
  await expect(page.locator('#library-dialog')).not.toBeVisible();await expect(page.locator('#library-select')).toHaveText('');await expect(page.locator('#library-name')).toHaveValue('');
  await expect(page.locator('#library-samples')).toHaveText('');await expect(page.locator('#access-token')).toBeFocused();
});

test('QTTS library late sample removal cannot overwrite a reopened different selection',async({page})=>{
  await openLibraries(page);await createLibrary(page,'旧库');await uploadLibrary(page);await page.evaluate(()=>window.libraryDeferRemove=true);
  await page.getByRole('button',{name:'移除样本 one.wav',exact:true}).click();await expect.poll(()=>page.evaluate(()=>typeof window.releaseLibraryRemove)).toBe('function');
  await page.locator('#btn-library-close').click();await page.locator('#btn-libraries').click();await expect(page.locator('#btn-library-refresh')).toBeEnabled();await createLibrary(page,'新库');
  const id=await page.locator('#library-select').inputValue();await page.evaluate(()=>window.releaseLibraryRemove());await page.evaluate(()=>new Promise(resolve=>setTimeout(resolve,20)));
  await expect(page.locator('#library-select')).toHaveValue(id);await expect(page.locator('#library-state')).toContainText('命名空库');await expect(page.locator('#library-samples input')).toHaveCount(0);
});

test('QTTS library progress polls are sequential and stop after closing even with ignored abort',async({page})=>{
  await openLibraries(page);await createLibrary(page);await uploadLibrary(page);await page.getByRole('checkbox',{name:'选择样本 one.wav',exact:true}).check();
  await page.evaluate(()=>window.libraryDeferPoll=true);await page.locator('#btn-library-process').click();await expect.poll(()=>page.evaluate(()=>typeof window.releaseLibraryPoll)).toBe('function');
  const before=await page.evaluate(()=>window.libraryRequests.filter(r=>r.method==='GET'&&r.path.endsWith(window.libraryStore[0].id)).length);
  await page.waitForTimeout(2300);expect(await page.evaluate(()=>window.libraryRequests.filter(r=>r.method==='GET'&&r.path.endsWith(window.libraryStore[0].id)).length)).toBe(before);
  await page.locator('#btn-library-close').click();await page.evaluate(()=>window.releaseLibraryPoll());await page.waitForTimeout(2300);
  expect(await page.evaluate(()=>window.libraryRequests.filter(r=>r.method==='GET'&&r.path.endsWith(window.libraryStore[0].id)).length)).toBe(before);await expect(page.locator('#library-message')).toHaveText('');
});

test('QTTS library native recording is stopped by opening, then saved to the named library',async({page})=>{
  await openLibraries(page,{realAudio:true});await createLibrary(page);await page.locator('#btn-library-close').click();
  await page.locator('#btn-rec').click();await expect(page.locator('#btn-rec')).toHaveText('■ 停止录音');await page.waitForTimeout(1600);
  await page.locator('#btn-libraries').click();await expect(page.locator('#rec-clips .row')).toHaveCount(1);await expect(page.locator('#btn-library-clips')).toBeEnabled();
  expect(await page.evaluate(()=>window.micStreams.every(stream=>stream.getTracks().every(track=>track.readyState==='ended')))).toBe(true);
  await page.locator('#btn-library-clips').click();await expect(page.locator('#library-message')).toContainText('原始样本已保存');await expect(page.locator('#rec-clips .row')).toHaveCount(0);await expect(page.locator('#library-samples input')).toHaveCount(1);
});

for(const [width,height] of [[1440,900],[375,667]])test(`QTTS library dialog bounded keyboard and XSS-safe content ${width}x${height}`,async({page})=>{
  await page.setViewportSize({width,height});await openLibraries(page);await expect(page.locator('#btn-library-close')).toBeFocused();
  await createLibrary(page,'<img src=x onerror=alert(1)>');await expect(page.locator('#library-dialog img')).toHaveCount(0);await uploadLibrary(page);
  await page.locator('#btn-library-process').scrollIntoViewIfNeeded();await expectInsideViewport(page,'#btn-library-process');await expectInsideViewport(page,'#btn-library-close');
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
  await page.screenshot({path:`docs/validation/step6/library-${width}x${height}.png`});await page.keyboard.press('Escape');await expect(page.locator('#library-dialog')).not.toBeVisible();await expect(page.locator('#btn-libraries')).toBeFocused();
  await expect(page.locator('nav[aria-label="主要视图"] button')).toHaveCount(2);
});

async function fillTrainingInputs(page) {
  await page.getByRole('checkbox',{name:'选择样本 one.wav',exact:true}).check();await page.getByRole('checkbox',{name:'选择样本 two.wav',exact:true}).check();
  await page.locator('#training-options summary').first().click();
  await page.getByRole('textbox',{name:'训练转写 one.wav',exact:true}).fill('第一段独立转写');await page.getByRole('textbox',{name:'训练转写 two.wav',exact:true}).fill('第二段不同转写');
  await page.getByRole('radio',{name:'统一参考 one.wav',exact:true}).check();await page.locator('#training-rights').check();await page.locator('#training-single-speaker').check();
}

test('QTTS training input explicit texts and declarations prepare, verify, delete without running training',async({page})=>{
  await openLibraries(page);await createLibrary(page);await uploadLibrary(page);
  await expect(page.locator('#btn-training-prepare')).toBeDisabled();await fillTrainingInputs(page);await page.locator('#btn-training-prepare').click();
  await expect(page.locator('#training-result')).toContainText('训练输入快照已生成');
  const body=await page.evaluate(()=>window.trainingLastBody);expect(body.samples.map(row=>row.text)).toEqual(['第一段独立转写','第二段不同转写']);expect(body.voice_rights_confirmed).toBe(true);expect(body.reference_sample_id).toBe(body.samples[0].id);
  expect(await page.evaluate(()=>window.libraryProcess)).toBeNull();await expect(page.locator('#training-result')).toContainText('"training_verified": false');
  await page.locator('#btn-training-verify').click();await expect(page.locator('#training-result')).toContainText('本次内容哈希');
  await page.locator('#training-delete-options summary').click();await page.locator('#btn-training-delete').click();await expect(page.locator('#training-result')).toContainText('原始库和声音档案未删除');await expect(page.locator('#library-samples input')).toHaveCount(2);
});

test('QTTS training input rejects unsupported format and retains user transcripts and raw selection',async({page})=>{
  await openLibraries(page);await createLibrary(page);await uploadLibrary(page);await fillTrainingInputs(page);await page.evaluate(()=>window.trainingRejectWav=true);
  await page.locator('#btn-training-prepare').click();await expect(page.locator('#library-message')).toContainText('PCM16 WAV accepted');
  await expect(page.getByRole('textbox',{name:'训练转写 one.wav',exact:true})).toHaveValue('第一段独立转写');await expect(page.locator('#training-datasets option')).toHaveCount(0);await expect(page.locator('#library-samples input:checked')).toHaveCount(2);
  await expect(page.locator('#training-result')).not.toContainText('已生成');expect(await page.evaluate(()=>window.libraryProcess)).toBeNull();
});

test('QTTS training input lock clears private transcripts and ignores late committed snapshot response',async({page})=>{
  await openLibraries(page);await createLibrary(page);await uploadLibrary(page);await fillTrainingInputs(page);await page.evaluate(()=>window.trainingDeferPrepare=true);await page.locator('#btn-training-prepare').click();
  await expect.poll(()=>page.evaluate(()=>typeof window.releaseTrainingPrepare)).toBe('function');await page.locator('#btn-library-lock').click();await page.evaluate(()=>window.releaseTrainingPrepare());await page.evaluate(()=>new Promise(resolve=>setTimeout(resolve,20)));
  await expect(page.locator('#training-transcripts')).toHaveText('');await expect(page.locator('#training-result')).toHaveText('');await expect(page.locator('#training-datasets')).toHaveText('');await expect(page.locator('#training-rights')).not.toBeChecked();await expect(page.locator('#access-token')).toBeFocused();
});

test('QTTS training input phone controls bounded and hash failure does not display stale success',async({page})=>{
  await page.setViewportSize({width:375,height:667});await openLibraries(page);await createLibrary(page);await uploadLibrary(page);await fillTrainingInputs(page);await page.locator('#btn-training-prepare').scrollIntoViewIfNeeded();await expectInsideViewport(page,'#btn-training-prepare');await page.locator('#btn-training-prepare').click();await expect(page.locator('#training-result')).toContainText('快照已生成');
  await page.evaluate(()=>window.trainingTampered=true);await page.locator('#btn-training-verify').click();await expect(page.locator('#library-message')).toContainText('hash changed');await expect(page.locator('#training-result')).not.toContainText('快照已生成');await expect(page.locator('#training-result')).not.toContainText('校验通过（');
  await page.screenshot({path:'docs/validation/step6/training-input-375x667.png'});await expect(page.locator('nav[aria-label="主要视图"] button')).toHaveCount(2);
});

test('QTTS training declarations are invalidated on selection, new library and deletion transitions',async({page})=>{
  await openLibraries(page);await createLibrary(page);await uploadLibrary(page);await fillTrainingInputs(page);await expect(page.locator('#btn-training-prepare')).toBeEnabled();
  await page.getByRole('checkbox',{name:'选择样本 two.wav',exact:true}).uncheck();await expect(page.locator('#training-rights')).not.toBeChecked();await expect(page.locator('#training-single-speaker')).not.toBeChecked();await expect(page.locator('#btn-training-prepare')).toBeDisabled();
  await page.locator('#training-rights').check();await page.locator('#training-single-speaker').check();await createLibrary(page,'另一个新库');
  await page.locator('#training-options summary').first().click();await expect(page.locator('#training-rights')).not.toBeChecked();await expect(page.locator('#training-transcripts textarea')).toHaveCount(0);
  await page.locator('#training-rights').check();await page.locator('#training-single-speaker').check();await page.locator('#library-delete-options summary').click();await page.locator('#btn-library-delete').click();
  await page.locator('#training-options summary').first().click();await expect(page.locator('#training-rights')).not.toBeChecked();await expect(page.locator('#training-single-speaker')).not.toBeChecked();
});


test('QTTS trained voice is explicitly labeled buffered unverified and immutable without a third view',async({page})=>{
  await openQTTS(page,{trainedProfile:true});await page.locator('#nav-lab').click();
  await expect(page.locator('#profile option')).toContainText('训练候选/句级缓冲/未验收');
  const card=page.locator('#profiles .card').first();await expect(card).toContainText('非声学流式');
  await expect(card.locator('textarea')).toHaveAttribute('readonly','');
  await expect(card.getByRole('button',{name:'保存文本并重载',exact:true})).toBeDisabled();
  await expect(card.getByRole('button',{name:/候选校准/})).toBeDisabled();
  await expect(card.getByRole('button',{name:/选择此训练版本/})).toBeEnabled();
  await expect(page.locator('nav[aria-label="主要视图"] button')).toHaveCount(2);
  await card.getByRole('button',{name:/选择此训练版本/}).click();
  expect(await page.evaluate(()=>window.apiRequests.some(call=>call.path==='/api/profiles/activate'))).toBe(true);
  await page.locator('#nav-speak').click();await page.locator('#btn-speak').click();
  await expect.poll(()=>page.evaluate(()=>window.turns.length)).toBe(1);
  expect(await page.evaluate(()=>window.turns[0].body.profile)).toBe('voice');
  await page.evaluate(()=>window.finishTurn(0,'候选聊天接口替身，不是Qwen音质证据'));
  await expect(page.locator('#llmout')).toContainText('不是Qwen音质证据');
  await page.locator('#nav-mon').click();await expect(page.locator('#workers')).toContainText('句级缓冲，非声学流式');
});

test('QTTS twenty-minute recorder keeps 11-minute virtual session and more than 2048 bounded chunks',async({page})=>{
  // Virtual duration/control test only: no claim of 11 minutes physical audio capture.
  await page.clock.install();
  await page.route('**/long-recorder-fixture',route=>route.fulfill({contentType:'text/html',body:'<script src="/recorder.js"></script>'}));
  await page.route('**/recorder.js',async route=>route.fulfill({contentType:'text/javascript',body:await readFile('kaggle/source/web/recorder.js','utf8')}));
  await page.goto('/long-recorder-fixture');
  await page.evaluate(async()=>{
    window.testTrack={ended:false,stop(){this.ended=true},addEventListener(){}};
    Object.defineProperty(navigator.mediaDevices,'getUserMedia',{value:async()=>({getTracks:()=>[window.testTrack]})});
    window.AudioContext=class {async resume(){} async close(){window.testContextClosed=true}createMediaStreamSource(){return {connect(){},disconnect(){}}}createAnalyser(){return {fftSize:2048,getFloatTimeDomainData(a){a.fill(.01)},disconnect(){}}}};
    window.MediaRecorder=class {static isTypeSupported(){return true}constructor(){this.state='inactive';this.mimeType='audio/webm'}start(){this.state='recording'}stop(){this.state='inactive';this.onstop()}};
    window.longClips=[];window.longRecorder=new window.QttsMicrophoneRecorder({onClip:(file,ms)=>window.longClips.push({size:file.size,ms})});
    await window.longRecorder.start();
    for(let i=0;i<2640;i++)window.longRecorder.session.recorder.ondataavailable({data:new Blob(['data'])});
  });
  await page.clock.fastForward('11:00');
  expect(await page.evaluate(()=>window.longRecorder.state)).toBe('recording');
  expect(await page.evaluate(()=>window.longRecorder.session.chunks.length)).toBe(2640);
  await page.clock.fastForward('10:00');
  expect(await page.evaluate(()=>window.longRecorder.state)).toBe('idle');
  expect(await page.evaluate(()=>window.longClips.length)).toBe(1);
  expect(await page.evaluate(()=>window.testTrack.ended&&window.testContextClosed)).toBe(true);
});

test('QTTS long capture is honestly separate from actual training and acoustic verification',async({page})=>{
  await openQTTS(page);await page.locator('#nav-lab').click();await page.locator('#btn-reference-options').click();
  await expect(page.locator('#reference-options')).toContainText('1200秒');
  await expect(page.locator('#reference-options')).toContainText('128MiB');
  await expect(page.locator('.release-note')).toContainText(/网页训练(?:执行)?尚未闭环/);
  await page.locator('#btn-libraries').click();await page.locator('#training-options').evaluate(e=>e.open=true);
  await expect(page.locator('#training-options')).toContainText('长录音不能直接作为单条训练序列');
});


test('QTTS step15 creation defers optional GPU calibration by default without removing manual controls', async ({page})=>{
  await openQTTS(page);
  await page.locator('#nav-lab').click();
  await expect(page.locator('.release-note')).toContainText('第十七阶段');
  await expect(page.locator('.release-note')).toContainText('双卡参考及生成参数绑定');
  await expect(page.locator('.release-note')).toContainText('RTF≤0.3尚须试听实测');
  await page.locator('#btn-reference-options').click();
  await expect(page.locator('#pcal')).not.toBeChecked();
  await expect(page.locator('#reference-options')).toContainText('默认关闭');
  await page.locator('#pcal').check();await expect(page.locator('#pcal')).toBeChecked();
  await expect(page.locator('#profiles').getByRole('button',{name:/候选校准/})).toBeVisible();
});

test('QTTS step15 library calibration default and lock reset stay off',async({page})=>{
  await openLibraries(page);
  await expect(page.locator('#library-calibrate')).not.toBeChecked();
  await page.locator('#btn-library-close').click();
  await page.locator('#btn-lock').click();
  await page.locator('#access-token').fill('browser-test-token-01234567890123456789012345');
  await page.locator('#btn-unlock').click();
  await page.locator('#btn-libraries').click();
  await expect(page.locator('#library-calibrate')).not.toBeChecked();
});


test('QTTS step17 long-reference context is explicit, submitted and reset on lock',async({page})=>{
  await openQTTS(page);await page.locator('#nav-lab').click();await page.locator('#btn-reference-options').click();
  await expect(page.locator('#pcontext')).toHaveValue('16');await page.locator('#pcontext').selectOption('24');
  await expect(page.locator('#reference-options')).toContainText('长录音可超过15秒');
  await expect(page.locator('#reference-options')).toContainText('更长不保证更像');
  await page.evaluate(()=>{const original=window.fetch;window.fetch=async(url,options={})=>{
    const p=new URL(url,location.href).pathname;
    if(p==='/api/prep/profiles'&&options.method==='POST'){window.submittedContext=options.body.get('anchor_seconds');return Response.json({job:'long-reference-test'});}
    if(p==='/api/prep/jobs/long-reference-test')return Response.json({state:'done',pct:100,profile:'voice',log:[]});
    return original(url,options);
  }});
  await page.locator('#pname').fill('长参考');await page.locator('#files').setInputFiles({name:'long.wav',mimeType:'audio/wav',buffer:Buffer.from('fixture-not-real-audio')});
  await page.locator('#btn-create').click();await expect.poll(()=>page.evaluate(()=>window.submittedContext)).toBe('24');
  await page.locator('#btn-lock').click();await expect(page.locator('#pcontext')).toHaveValue('16');
});
