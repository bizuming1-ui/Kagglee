import { test, expect } from '@playwright/test';
import { readFile } from 'node:fs/promises';

// Full frozen scripts in Chromium; HTTP, microphone and audio devices below are
// EXPLICIT FIXTURES. OBSERVED_NOT_FIXED assertions prove old behavior, not fixes.
async function openFixture(page, { recorderOnly = false, failAudio = false, deferMedia = false } = {}) {
  await page.route('**/g0-frontend', async route => route.fulfill({contentType:'text/html',body:
    recorderOnly ? '<script src="/recorder.js"></script>' : await readFile('kaggle/source/web/index.html','utf8')}));
  for (const name of ['app.js','recorder.js']) await page.route(`**/${name}`, async route =>
    route.fulfill({contentType:'text/javascript',body:await readFile(`kaggle/source/web/${name}`,'utf8')}));
  await page.addInitScript(({failAudio,deferMedia}) => {
    window.g0={tracks:[],messages:[],turns:[],reports:[],created:[],revoked:[],permissionCalls:0};
    const makeStream=()=>{
      const track={stopped:false,stop(){this.stopped=true;},addEventListener(){}};
      window.g0.tracks.push(track);return {getTracks:()=>[track]};
    };
    Object.defineProperty(navigator.mediaDevices,'getUserMedia',{value:async()=>{
      window.g0.permissionCalls++;
      if(deferMedia)return new Promise(resolve=>window.g0.releasePermission=()=>resolve(makeStream()));
      return makeStream();
    }});
    window.MediaRecorder=class {
      static isTypeSupported(){return true;}
      constructor(){this.state='inactive';this.mimeType='audio/webm;codecs=opus';}
      start(){this.state='recording';} stop(){this.state='inactive';} // tests control late events
    };
    window.AudioContext=class {
      constructor(){this.state='running';this.sampleRate=24000;this.destination={};this.audioWorklet={addModule:async()=>{
        if(failAudio)throw new Error('g0 synthetic addModule rejection');
      }};}
      async resume(){} async close(){this.state='closed';}
      createGain(){return {connect(){return this;}};}
      createMediaStreamSource(){return {connect(){},disconnect(){}};}
      createAnalyser(){return {fftSize:2048,getFloatTimeDomainData(a){a.fill(.01);},disconnect(){}};}
    };
    window.AudioWorkletNode=class {
      constructor(){this.port={postMessage:m=>window.g0.messages.push({t:m.t,d:m.d?Array.from(m.d):null})};}
      connect(){return {connect(){}};}
    };
    const create=URL.createObjectURL.bind(URL),revoke=URL.revokeObjectURL.bind(URL);
    URL.createObjectURL=blob=>{const url=create(blob);window.g0.created.push(url);return url;};
    URL.revokeObjectURL=url=>{window.g0.revoked.push(url);revoke(url);};
    window.g0.frame=(type,payload)=>{
      if(!(payload instanceof Uint8Array))payload=new TextEncoder().encode(JSON.stringify(payload));
      const out=new Uint8Array(9+payload.length),view=new DataView(out.buffer);
      view.setUint8(0,type);view.setUint32(1,0,true);view.setUint32(5,payload.length,true);out.set(payload,9);return out;
    };
    window.g0.respond=(chunks,close=true)=>{
      const turn=window.g0.turns.at(-1);turn.cancelCount=0;
      turn.stream=new ReadableStream({start(controller){turn.controller=controller;for(const chunk of chunks)controller.enqueue(new Uint8Array(chunk));if(close)controller.close();},cancel(){turn.cancelCount++;}});
      turn.resolve(new Response(turn.stream,{headers:{'X-Session-Id':'synthetic-g0'}}));
    };
    const native=fetch;
    window.fetch=async(url,options={})=>{
      const path=new URL(url,location.href).pathname;
      if(path==='/api/health')return Response.json({ok:true,workers:[]});
      if(path==='/api/profiles')return Response.json({active:'voice',profiles:[{id:'voice',name:'Synthetic only',ref_text:'fixture',breath_files:[],candidates:[]}]});
      if(path==='/api/speak')return new Promise(resolve=>window.g0.turns.push({resolve,signal:options.signal}));
      if(path==='/api/report'){window.g0.reports.push(JSON.parse(options.body));return Response.json({ok:true});}
      if(path.startsWith('/api/'))return Response.json({ok:true});
      return native(url,options);
    };
    window.g0.newRecorder=()=>new window.QttsMicrophoneRecorder({onClip:()=>window.g0.clips++,getFiles:()=>[],onStatus(){}});
    window.g0.clips=0;
  },{failAudio,deferMedia});
  await page.goto('/g0-frontend');
  if(!recorderOnly){
    await page.locator('#access-token').fill('synthetic-g0-token-012345678901234567890123');
    await page.locator('#btn-unlock').click();await expect(page.locator('#profile')).toHaveValue('voice');
    await page.locator('#mode').selectOption('read');await page.locator('#text').fill('fixture only');
  }
}
async function speak(page){await page.locator('#btn-speak').click();await expect.poll(()=>page.evaluate(()=>window.g0.turns.length)).toBe(1);}
async function evidence(info,value){await info.attach('g0-observation',{contentType:'application/json',body:Buffer.from(JSON.stringify(value))});}

test('G0 OBSERVED_NOT_FIXED old recorder error stops a newer owned session',async({page},info)=>{
  await openFixture(page,{recorderOnly:true});
  const observed=await page.evaluate(async()=>{
    const recorder=window.g0.newRecorder();await recorder.start();const old=recorder.session;
    recorder.cancel();await recorder.start();const current=recorder.session,before=recorder.state;
    old.recorder.onerror();
    const result={before,after:recorder.state,newTrackStopped:current.stream.getTracks()[0].stopped,oldEpoch:old.epoch,newEpoch:current.epoch};
    recorder.cancel();return result;
  });
  expect(observed.before).toBe('recording');expect(observed.after).toBe('stopping');expect(observed.newTrackStopped).toBe(true);
  await evidence(info,{id:'S18-G0-WEB-F04',...observed,fixed:false,injectedLateEvent:true});
});

test('G0 OBSERVED_NOT_FIXED protocol JSON error leaves reader open and request un-aborted',async({page},info)=>{
  await openFixture(page);await speak(page);
  await page.evaluate(()=>window.g0.respond([window.g0.frame(2,new TextEncoder().encode('{'))],false));
  await expect(page.locator('#errbox')).not.toBeEmpty();await expect.poll(()=>page.evaluate(()=>window.g0.reports.length)).toBe(1);
  const observed=await page.evaluate(()=>({cancelCount:window.g0.turns[0].cancelCount,signalAborted:window.g0.turns[0].signal.aborted,streamLocked:window.g0.turns[0].stream.locked}));
  expect(observed).toEqual({cancelCount:0,signalAborted:false,streamLocked:true});
  await evidence(info,{id:'S18-G0-WEB-F05',...observed,fixed:false,networkStreamIsFixture:true});
  await page.locator('#btn-stop').click();expect(await page.evaluate(()=>window.g0.turns[0].signal.aborted)).toBe(true);
});

test('G0 OBSERVED_NOT_FIXED failed audio module initialization does not revoke its blob URL',async({page},info)=>{
  await openFixture(page,{failAudio:true});await page.locator('#btn-speak').click();
  await expect(page.locator('#errbox')).toContainText('synthetic addModule rejection');
  const observed=await page.evaluate(()=>({created:window.g0.created.length,revoked:window.g0.revoked.length,requests:window.g0.turns.length}));
  expect(observed).toEqual({created:1,revoked:0,requests:0});
  await evidence(info,{id:'S18-G0-WEB-F06',...observed,fixed:false,injectedModuleFailure:true});
});

test('G0 protection fragmented wire PCM preserves signed samples and only generated frames reach player',async({page})=>{
  await openFixture(page);await speak(page);
  await page.evaluate(()=>{
    const audio=window.g0.frame(1,new Uint8Array([0,128,0,0,255,127]));
    const end=window.g0.frame(5,{timeline_ms:{},per_gpu:{}});
    window.g0.respond([...audio,...end].map(byte=>[byte]));
  });
  await expect.poll(()=>page.evaluate(()=>window.g0.reports.length)).toBe(1);
  expect(await page.evaluate(()=>window.g0.messages.filter(m=>m.t==='pcm').map(m=>m.d))).toEqual([[-1,0,32767/32768]]);
  await expect(page.locator('#errbox')).toBeEmpty();
});

test('G0 protection truncated trailing frame is displayed as a protocol error',async({page})=>{
  await openFixture(page);await speak(page);
  await page.evaluate(()=>window.g0.respond([window.g0.frame(5,{timeline_ms:{},per_gpu:{}}),[1,0]]));
  await expect(page.locator('#errbox')).toContainText('音频协议帧被截断');await expect(page.locator('#btn-speak')).toBeEnabled();
});

test('G0 protection missing final summary is not silently reported as a complete stream',async({page})=>{
  await openFixture(page);await speak(page);
  await page.evaluate(()=>window.g0.respond([window.g0.frame(3,{t:'fixture'})]));
  await expect(page.locator('#errbox')).toContainText('音频流未返回结束汇总');
});

test('G0 protection explicit stop aborts the pending speech request',async({page})=>{
  await openFixture(page);await speak(page);await page.locator('#btn-stop').click();
  expect(await page.evaluate(()=>window.g0.turns[0].signal.aborted)).toBe(true);await expect(page.locator('#btn-speak')).toBeEnabled();
});

test('G0 protection old recorder data does not enter a newer recording',async({page})=>{
  await openFixture(page,{recorderOnly:true});
  expect(await page.evaluate(async()=>{
    const recorder=window.g0.newRecorder();await recorder.start();const old=recorder.session;
    recorder.cancel();await recorder.start();old.recorder.ondataavailable({data:new Blob(['late'])});
    const result={bytes:recorder.session.bytes,chunks:recorder.session.chunks.length,state:recorder.state};recorder.cancel();return result;
  })).toEqual({bytes:0,chunks:0,state:'recording'});
});

test('G0 protection old recorder stop cannot clean up a new session',async({page})=>{
  await openFixture(page,{recorderOnly:true});
  expect(await page.evaluate(async()=>{
    const recorder=window.g0.newRecorder();await recorder.start();const old=recorder.session;
    recorder.cancel();await recorder.start();const current=recorder.session;old.recorder.onstop();
    const result={stillOwned:recorder.owns(current),newTrackStopped:current.stream.getTracks()[0].stopped,state:recorder.state};recorder.cancel();return result;
  })).toEqual({stillOwned:true,newTrackStopped:false,state:'recording'});
});

test('G0 protection recording byte overflow discards chunks instead of saving a partial clip',async({page})=>{
  await openFixture(page,{recorderOnly:true});
  expect(await page.evaluate(async()=>{
    const recorder=window.g0.newRecorder();recorder.maxClipBytes=2;await recorder.start();const session=recorder.session;
    session.recorder.ondataavailable({data:new Blob(['123'])});session.recorder.onstop();
    return {chunks:session.chunks.length,clips:window.g0.clips,discard:session.discard,state:recorder.state,stopped:session.stream.getTracks()[0].stopped};
  })).toEqual({chunks:0,clips:0,discard:true,state:'idle',stopped:true});
});

test('G0 protection cancel during permission wait releases the late stream without a clip',async({page})=>{
  await openFixture(page,{recorderOnly:true,deferMedia:true});
  expect(await page.evaluate(async()=>{
    const recorder=window.g0.newRecorder();const pending=recorder.start();recorder.cancel();
    await recorder.start();const calls=window.g0.permissionCalls;window.g0.releasePermission();await pending;
    return {calls,stopped:window.g0.tracks[0].stopped,session:recorder.session,clips:window.g0.clips,state:recorder.state};
  })).toEqual({calls:1,stopped:true,session:null,clips:0,state:'idle'});
});
