import {test,expect} from '@playwright/test';
import {readFile} from 'node:fs/promises';
import {extract} from '../../kaggle/tests/step18_playback_fixture.mjs';
const source=await readFile('kaggle/step18/web/app.js','utf8');
async function nativePage(page,rate=24000){
 await page.route('**/s5-native',r=>r.fulfill({contentType:'text/html; charset=utf-8',body:'<!doctype html><button id="go">start</button><script>'+`(()=>{${extract(source)};window.S5Player=P;})();`+'</script>'}));
 await page.goto('/s5-native');
 await page.evaluate(rate=>{
  const Native=window.AudioContext;
  window.AudioContext=class extends Native{constructor(options){super({...options,sampleRate:rate});}};
  window.s5={states:[],reports:[]};
  document.querySelector('#go').onclick=async()=>{
   const p=window.s5.player=new window.S5Player();await p.init(s=>window.s5.states.push(s));
   p.node.port.addEventListener('message',e=>window.s5.reports.push(e.data));p.node.port.start();p.beginStream(performance.now());window.s5.ready=true;
  };
 },rate);
 await page.click('#go');await expect.poll(()=>page.evaluate(()=>window.s5.ready)).toBe(true);
 expect(await page.evaluate(()=>window.s5.player.ctx.sampleRate)).toBe(rate);
}
for(const rate of [24000,44100,48000])for(const n of [1,480,1200]){
 test(`S5 native AudioWorklet consumes completed ${n} source samples at ${rate}`,async({page},info)=>{
  await nativePage(page,rate);
  await page.evaluate(n=>{const a=new Uint8Array(n*2),v=new DataView(a.buffer);for(let i=0;i<n;i++)v.setInt16(i*2,5000,true);const p=window.s5.player;p.pushPcm(a);p.markGenerationDone();},n);
  await expect.poll(()=>page.evaluate(()=>window.s5.player.state)).toBe('ended');
  const evidence=await page.evaluate(()=>{const p=window.s5.player;return {rate:p.ctxRate,state:p.state,queued:p.queuedSamples,played:p.st.played,dropped:p.st.dropped,endAck:p.st.endAck,pending:p.pendingSamples(),reports:window.s5.reports.length};});
  expect(evidence.played).toBe(Math.ceil(n*rate/24000));expect(evidence.queued).toBe(evidence.played);expect(evidence.pending).toBe(0);expect(evidence.dropped).toBe(0);expect(evidence.endAck).toBe(true);
  await info.attach('s5-native-consumption',{contentType:'application/json',body:Buffer.from(JSON.stringify({...evidence,physical_speaker_verified:false,model_executed:false}))});
  await page.evaluate(()=>window.s5.player.ctx.close());
 });
}
test('S5 native empty generation acknowledges end without adding PCM',async({page})=>{
 await nativePage(page);await page.evaluate(()=>window.s5.player.markGenerationDone());await expect.poll(()=>page.evaluate(()=>window.s5.player.state)).toBe('ended');expect(await page.evaluate(()=>window.s5.player.st.played)).toBe(0);await page.evaluate(()=>window.s5.player.ctx.close());
});
test('S5 native stop rejects delayed same-stream status and does not play buffered PCM',async({page})=>{
 await nativePage(page,48000);await page.evaluate(()=>{const p=window.s5.player;const e=p.streamEpoch;p.pushPcm(new Uint8Array(960));p.stop();p.onWorklet({epoch:e,fill:96000,played:0,dropped:0,underruns:0,endAck:false});p.tick();});
 await expect.poll(()=>page.evaluate(()=>window.s5.reports.some(x=>x.epoch===window.s5.player.streamEpoch))).toBe(true);
 expect(await page.evaluate(()=>({state:window.s5.player.state,played:window.s5.reports.at(-1).played}))).toEqual({state:'idle',played:0});await page.evaluate(()=>window.s5.player.ctx.close());
});
test('S5 native replacement stream ignores stale old epoch and drains new short tail',async({page})=>{
 await nativePage(page);await page.evaluate(()=>{const p=window.s5.player;const e=p.streamEpoch;p.stop();p.beginStream(performance.now());p.onWorklet({epoch:e,fill:96000,played:999,dropped:0,underruns:0,endAck:true});p.pushPcm(new Uint8Array(960));p.markGenerationDone();});
 await expect.poll(()=>page.evaluate(()=>window.s5.player.state)).toBe('ended');expect(await page.evaluate(()=>window.s5.player.st.played)).toBe(480);await page.evaluate(()=>window.s5.player.ctx.close());
});
async function fullUI(page){
 await page.route('**/s5-full',async r=>r.fulfill({contentType:'text/html; charset=utf-8',body:await readFile('kaggle/source/web/index.html','utf8')}));
 for(const name of ['app.js','recorder.js'])await page.route(`**/${name}`,async r=>r.fulfill({contentType:'text/javascript',body:name==='app.js'?source:await readFile('kaggle/source/web/recorder.js','utf8')}));
 await page.addInitScript(()=>{
  window.s5ui={reports:[],messages:[],turns:[]};const NativeNode=window.AudioWorkletNode;
  window.AudioWorkletNode=class extends NativeNode{constructor(...args){super(...args);this.port.addEventListener('message',e=>window.s5ui.reports.push(e.data));this.port.start();const post=this.port.postMessage.bind(this.port);this.port.postMessage=(m,...args)=>{window.s5ui.messages.push({t:m.t,epoch:m.epoch,length:m.d?.length||0});post(m,...args);};}};
  const native=window.fetch;window.fetch=async(url,options={})=>{
   const path=new URL(url,location.href).pathname;
   if(path==='/api/health')return Response.json({ok:true,workers:[]});
   if(path==='/api/profiles')return Response.json({active:'voice',profiles:[{id:'voice',name:'Synthetic S5',ref_text:'fixture',breath_files:[],candidates:[]}]});
   if(path==='/api/speak')return new Promise(resolve=>window.s5ui.turns.push(resolve));
   if(path.startsWith('/api/'))return Response.json({ok:true});return native(url,options);
  };
  window.s5ui.frame=(type,payload)=>{const a=payload instanceof Uint8Array?payload:new TextEncoder().encode(JSON.stringify(payload));const out=new Uint8Array(9+a.length),v=new DataView(out.buffer);v.setUint8(0,type);v.setUint32(1,0,true);v.setUint32(5,a.length,true);out.set(a,9);return out;};
  window.s5ui.respond=n=>{const pcm=new Uint8Array(n*2),v=new DataView(pcm.buffer);for(let i=0;i<n;i++)v.setInt16(i*2,5000,true);const chunks=[window.s5ui.frame(1,pcm),window.s5ui.frame(5,{timeline_ms:{},per_gpu:{}})];window.s5ui.turns.at(-1)(new Response(new ReadableStream({start(c){for(const a of chunks)c.enqueue(a);c.close();}})));};
 });
 await page.goto('/s5-full');await page.locator('#access-token').fill('synthetic-s5-token-01234567890123456789');await page.locator('#btn-unlock').click();await expect(page.locator('#profile')).toHaveValue('voice');await page.locator('#mode').selectOption('read');await page.locator('#text').fill('fixture only');
}
for(const n of [1,480,1200])test(`S5 complete candidate UI drives native end-to-end short ${n}`,async({page},info)=>{
 await fullUI(page);await page.locator('#btn-speak').click();await expect.poll(()=>page.evaluate(()=>window.s5ui.turns.length)).toBe(1);await page.evaluate(n=>window.s5ui.respond(n),n);
 await expect(page.locator('#pstate')).toHaveText('播放完毕');
 await expect.poll(()=>page.evaluate(()=>window.s5ui.reports.at(-1)?.played)).toBe(n);
 const ev=await page.evaluate(()=>window.s5ui);await info.attach('s5-full-native-ui',{contentType:'application/json',body:Buffer.from(JSON.stringify({messages:ev.messages,reports:ev.reports,synthetic_http:true,physical_speaker_verified:false}))});
 expect(ev.messages.filter(x=>x.t==='end')).toHaveLength(1);expect(ev.messages.some(x=>x.t==='play')).toBe(true);
});
