import { test, expect } from '@playwright/test';
import { readFile } from 'node:fs/promises';
import { openFixture, speak, evidence } from './pass2-frontend-fixture.js';

// Real Chromium running complete frozen scripts. p2 audio/media/fetch/status are
// explicit fixtures; clipboard test uses native clipboard + ephemeral workbench.
const end={timeline_ms:{},per_gpu:{}};
const done=async(page,n=1)=>expect.poll(()=>page.evaluate(()=>window.p2.reports.length)).toBe(n);

async function recorderFixture(page){
 await openFixture(page,{recorderOnly:true});
 // The old recorder-only helper has no document charset. Declare UTF-8 in the
 // audit-only shell so original script literals are decoded as in product HTML.
 await page.route('**/p2-frontend',route=>route.fulfill({contentType:'text/html; charset=utf-8',body:'<!doctype html><meta charset="utf-8"><script src="/recorder.js"></script>'}));
 await page.reload();
}


test('P3 protection cancelled recorder audio resume cannot install a late recording',async({page})=>{
 await recorderFixture(page);
 const value=await page.evaluate(async()=>{
  window.AudioContext.prototype.resume=function(){return new Promise(resolve=>window.releaseResume=resolve);};
  const recorder=window.p2.newRecorder();const pending=recorder.start();
  await Promise.resolve();const context=window.p2.contexts[0];recorder.cancel();window.releaseResume();await pending;
  return {state:recorder.state,session:recorder.session,stopped:window.p2.tracks[0].stopped,context:context.state,clips:window.p2.clips};
 });
 expect(value).toEqual({state:'idle',session:null,stopped:true,context:'closed',clips:0});
});

test('P3 protection recorder exact byte and duration boundary preserves actual File bytes',async({page})=>{
 await recorderFixture(page);
 const value=await page.evaluate(async()=>{
  const recorder=window.p2.newRecorder();recorder.maxClipBytes=5;recorder.maxTotalBytes=5;recorder.maxChunks=2;
  await recorder.start();const s=recorder.session;
  s.recorder.ondataavailable({data:new Blob([])});
  s.recorder.ondataavailable({data:new Blob([new Uint8Array([0,255])])});
  s.recorder.ondataavailable({data:new Blob([new Uint8Array([1,2,3])])});
  s.durationMs=1500;s.recorder.onstop();
  const value={clips:window.p2.clips,bytes:Array.from(new Uint8Array(await window.p2.lastClip.arrayBuffer())),state:recorder.state,chunks:s.chunks.length,stopped:s.stream.getTracks()[0].stopped};recorder.cancel();return value;
 });
 expect(value).toEqual({clips:1,bytes:[0,255,1,2,3],state:'idle',chunks:0,stopped:true});
});

test('P3 protection MediaRecorder start rejection cleans owned context and tracks',async({page})=>{
 await recorderFixture(page);
 const value=await page.evaluate(async()=>{
  window.MediaRecorder.prototype.start=function(){throw new DOMException('synthetic start failure','InvalidStateError');};
  const recorder=window.p2.newRecorder();await recorder.start();
  return {state:recorder.state,session:recorder.session,stopped:window.p2.tracks[0].stopped,context:window.p2.contexts[0].state,clips:window.p2.clips};
 });
 expect(value).toEqual({state:'idle',session:null,stopped:true,context:'closed',clips:0});
});

test('P3 protection late permission rejection after cancel cannot replace cancel state',async({page})=>{
 await recorderFixture(page);
 const value=await page.evaluate(async()=>{
  Object.defineProperty(navigator,'mediaDevices',{configurable:true,value:{getUserMedia:()=>new Promise((_,reject)=>window.rejectPermission=reject)}});
  const recorder=window.p2.newRecorder();const statuses=[];recorder.onStatus=(state,message)=>statuses.push({state,message});
  const pending=recorder.start();recorder.cancel();window.rejectPermission(new DOMException('synthetic deny','NotAllowedError'));await pending;
  return {state:recorder.state,session:recorder.session,pending:recorder.pendingPermission,last:statuses.at(-1).message,contexts:window.p2.contexts.length,clips:window.p2.clips};
 });
 expect(value).toEqual({state:'idle',session:null,pending:false,last:'未采集；录音已取消并释放设备',contexts:0,clips:0});
});

test('P3 protection current policy frame reaches original player before EOF',async({page})=>{
 await openFixture(page);await speak(page);
 await page.evaluate(()=>window.p2.respond([window.p2.frame(7,{low_s:.5,high_s:2,start_s:.1,agg_rtf:1})],false));
 await expect(page.locator('#m-pol')).toContainText('低 0.5');
 await page.evaluate(()=>window.p2.nodes[0].port.onmessage({data:{t:'st',fill:4800,played:0,underruns:0,playing:false,starved:false,dropped:0}}));
 await expect(page.locator('#pstate')).toHaveText('播放中');
 expect(await page.evaluate(()=>({play:window.p2.messages.filter(m=>m.t==='play').length,reports:window.p2.reports.length}))).toEqual({play:1,reports:0});
 await page.locator('#btn-stop').click();
 await page.evaluate(end=>window.p2.turns[0].controller.enqueue(window.p2.frame(5,end)),end);
 await expect.poll(()=>page.evaluate(()=>window.p2.turns[0].cancelCount)).toBe(1);
});

test('P3 protection current HTTP401 locks before private error can populate the page',async({page})=>{
 await openFixture(page);await page.locator('#dskey').fill('synthetic-ds-key');await speak(page);
 await page.evaluate(()=>window.p2.turns[0].resolve(Response.json({error:'synthetic-private-error'},{status:401})));
 await expect(page.locator('#protected-controls')).toBeHidden();await expect(page.locator('#access-status')).toContainText('访问口令无效');
 await expect(page.locator('#text')).toHaveValue('');await expect(page.locator('#dskey')).toHaveValue('');await expect(page.locator('#errbox')).toHaveText('');
 expect(await page.evaluate(()=>({aborted:window.p2.turns[0].signal.aborted,reports:window.p2.reports.length,pcm:window.p2.messages.filter(m=>m.t==='pcm').length}))).toEqual({aborted:true,reports:0,pcm:0});
});

test('P3 protection browser rejects oversized wire header before PCM admission',async({page})=>{
 await openFixture(page);await speak(page);
 await page.evaluate(()=>{const header=new Uint8Array(9);header[0]=1;new DataView(header.buffer).setUint32(5,32*1024*1024+1,true);window.p2.respond([header]);});
 await expect(page.locator('#errbox')).toContainText('超过32MiB限制');await expect(page.locator('#btn-speak')).toBeEnabled();
 expect(await page.evaluate(()=>window.p2.messages.filter(m=>m.t==='pcm').length)).toBe(0);
 // Existing F05/F26 catch/report and cleanup semantics are not signed off here.
 await page.locator('#btn-stop').click();
});

test('P3 protection completed nonempty playback can drain to ended without synthetic underrun',async({page})=>{
 await openFixture(page);await speak(page);
 await page.evaluate(end=>window.p2.respond([window.p2.frame(1,new Uint8Array(9600)),window.p2.frame(5,end)]),end);await done(page);
 await page.evaluate(()=>window.p2.nodes[0].port.onmessage({data:{t:'st',fill:4800,played:0,underruns:0,playing:false,starved:false,dropped:0}}));
 await expect(page.locator('#pstate')).toHaveText('播放中');
 await page.evaluate(()=>{
  const now=performance.now.bind(performance);Object.defineProperty(performance,'now',{value:()=>now()+1000});
  window.p2.nodes[0].port.onmessage({data:{t:'st',fill:0,played:4800,underruns:0,playing:false,starved:false,dropped:0}});
 });
 await expect(page.locator('#pstate')).toHaveText('播放完毕');
 expect(await page.evaluate(()=>({play:window.p2.messages.filter(m=>m.t==='play').length,pcm:window.p2.messages.filter(m=>m.t==='pcm').length}))).toEqual({play:1,pcm:1});
 // Controlled status/clock, not actual audio rendering, TTFA or final-report F26 fix.
});

test('P3 protection native clipboard copies each complete frozen web source without another save',async({page,request,context})=>{
 const current=await (await request.get('/api/project')).json();const files={...current.files};const expected={};
 for(const name of ['app.js','recorder.js','index.html']){const key='audit-web-'+name;expected[key]=await readFile('kaggle/source/web/'+name,'utf8');files[key]=expected[key];}
 const response=await request.put('/api/project',{data:{files,baseRevision:current.revision}});expect(response.status()).toBe(200);
 const before=await (await request.get('/api/project')).json();await page.goto('/');await expect(page.locator('#save-status')).toHaveText('已保存到项目');
 await context.grantPermissions(['clipboard-read','clipboard-write']);
 for(const [name,source] of Object.entries(expected)){
  await page.getByRole('tab',{name,exact:true}).click();await expect(page.locator('#code')).toHaveValue(source);
  await page.locator('#copy-code').click();await expect(page.locator('#toast')).toContainText('已复制 '+name);
  expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(source);await expect(page.locator('#code')).toHaveValue(source);
 }
 const after=await (await request.get('/api/project')).json();expect(after.revision).toBe(before.revision);expect(after.files).toEqual(before.files);
 // Isolated ephemeral E2E workspace, never the formal workspace/HEAD revision.
});

test('P3 protection chat request history remains bounded to last six complete fixture turns',async({page})=>{
 await openFixture(page);await page.locator('#mode').selectOption('chat');
 for(let i=0;i<10;i++){
  await page.locator('#text').fill('question-'+i);await page.locator('#btn-speak').click();await expect.poll(()=>page.evaluate(()=>window.p2.turns.length)).toBe(i+1);
  const history=await page.evaluate(i=>window.p2.turns[i].request.history,i);const expected=[];
  for(let j=Math.max(0,i-6);j<i;j++)expected.push({role:'user',content:'question-'+j},{role:'assistant',content:'answer-'+j});
  expect(history).toEqual(expected);
  await page.evaluate(({i,end})=>window.p2.respond([window.p2.frame(3,{t:'answer-'+i}),window.p2.frame(5,end)]),{i,end});await done(page,i+1);
 }
});

test('P3 OBSERVED_NOT_FIXED late pre-reset worklet status restarts stopped player commands',async({page},info)=>{
 await openFixture(page);await speak(page);await page.locator('#btn-stop').click();await expect(page.locator('#pstate')).toHaveText('空闲');
 await page.evaluate(()=>window.p2.nodes[0].port.onmessage({data:{t:'st',fill:240000,played:0,underruns:1,playing:false,starved:true,dropped:0}}));
 await expect(page.locator('#pstate')).toHaveText('播放中');
 const value=await page.evaluate(()=>({aborted:window.p2.turns[0].signal.aborted,last:window.p2.messages.slice(-3).map(m=>m.t),play:window.p2.messages.filter(m=>m.t==='play').length}));
 expect(value).toEqual({aborted:true,last:['hold','reset','play'],play:1});
 await evidence(info,{id:'S18-G0-PASS3-F41',fixed:false,originalFullScriptExecuted:true,afterExplicitStop:true,requestAborted:true,lateWorkletStatusIsFixture:true,commandSequence:['hold','reset','play'],uiState:'playing',actualWorkletRaceOrPhysicalPlaybackProven:false,actualModelExecuted:false});
 await page.locator('#btn-stop').click();await page.evaluate(end=>window.p2.respond([window.p2.frame(5,end)]),end);
});

test('P3 OBSERVED_NOT_FIXED same access epoch profile reloads can roll back newer candidate highlight',async({page},info)=>{
 await openFixture(page);
 await page.evaluate(()=>{
  const native=window.fetch;
  window.p3={reloads:[],mutations:[],defer:false};
  window.p3.profile=index=>({id:'voice',name:'Synthetic only',ref_text:'fixture',breath_files:[],anchor_candidate:index,candidates:[0,1].map(i=>({score:.8,snr_db:20,asr_conf:.9,start:0,end:3,text:'candidate '+i}))});
  window.fetch=async(url,options={})=>{
   const path=new URL(url,location.href).pathname;
   if(path==='/api/profiles'){
    if(window.p3.defer)return new Promise(resolve=>window.p3.reloads.push(resolve));
    return Response.json({active:'voice',profiles:[window.p3.profile(0)]});
   }
   if(path.endsWith('/candidate')){window.p3.mutations.push(JSON.parse(options.body).index);return Response.json({ok:true});}
   return native(url,options);
  };
 });
 await page.locator('#nav-lab').click();await expect(page.locator('.cand')).toHaveCount(2);
 await page.evaluate(()=>window.p3.defer=true);await page.locator('.cand').nth(0).click();await page.locator('.cand').nth(1).click();
 await expect.poll(()=>page.evaluate(()=>window.p3.reloads.length)).toBe(2);
 await page.evaluate(()=>window.p3.reloads[1](Response.json({active:'voice',profiles:[window.p3.profile(1)]})));
 await expect(page.locator('.cand.on')).toContainText('#1');
 await page.evaluate(()=>window.p3.reloads[0](Response.json({active:'voice',profiles:[window.p3.profile(0)]})));
 await expect(page.locator('.cand.on')).toContainText('#0');
 expect(await page.evaluate(()=>window.p3.mutations)).toEqual([0,1]);
 await evidence(info,{id:'S18-G0-PASS3-F42',fixed:false,originalFullScriptExecuted:true,sameAccessEpoch:true,candidateMutationOrder:[0,1],profileResponseOrder:[1,0],observedHighlightOrder:[1,0],profileResponsesAreSyntheticSnapshots:true,actualBackendRollbackOrWrongVoiceProven:false,actualModelExecuted:false});
});
