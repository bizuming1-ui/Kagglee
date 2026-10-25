import { test, expect } from '@playwright/test';
import { readFile } from 'node:fs/promises';

// Full frozen scripts in Chromium; HTTP, microphone and audio devices below are
// EXPLICIT FIXTURES. OBSERVED_NOT_FIXED assertions prove old behavior, not fixes.
export async function openFixture(page, { recorderOnly = false, failAudio = false, deferMedia = false } = {}) {
  await page.route('**/p2-frontend', async route => route.fulfill({contentType:'text/html',body:
    recorderOnly ? '<script src="/recorder.js"></script>' : await readFile('kaggle/source/web/index.html','utf8')}));
  for (const name of ['app.js','recorder.js']) await page.route(`**/${name}`, async route =>
    route.fulfill({contentType:'text/javascript',body:await readFile(`kaggle/source/web/${name}`,'utf8')}));
  await page.addInitScript(({failAudio,deferMedia}) => {
    window.p2={tracks:[],nodes:[],contexts:[],messages:[],turns:[],reports:[],telemetry:[],created:[],revoked:[],permissionCalls:0,moduleCalls:0,files:[]};
    const makeStream=()=>{
      const track={stopped:false,handlers:{},stop(){this.stopped=true;},addEventListener(name,fn){this.handlers[name]=fn;}};
      window.p2.tracks.push(track);return {getTracks:()=>[track]};
    };
    Object.defineProperty(navigator.mediaDevices,'getUserMedia',{value:async()=>{
      window.p2.permissionCalls++;
      if(deferMedia)return new Promise(resolve=>window.p2.releasePermission=()=>resolve(makeStream()));
      return makeStream();
    }});
    window.MediaRecorder=class {
      static isTypeSupported(){return true;}
      constructor(){this.state='inactive';this.mimeType='audio/webm;codecs=opus';}
      start(){this.state='recording';} stop(){this.state='inactive';} // tests control late events
    };
    window.AudioContext=class {
      constructor(){window.p2.contexts.push(this);this.state='running';this.sampleRate=24000;this.destination={};this.audioWorklet={addModule:async()=>{
        if(failAudio && window.p2.moduleCalls++===0)throw new Error('p2 synthetic addModule rejection');
      }};}
      async resume(){} async close(){this.state='closed';}
      createGain(){return {connect(){return this;}};}
      createMediaStreamSource(){return {connect(){},disconnect(){}};}
      createAnalyser(){return {fftSize:2048,getFloatTimeDomainData(a){a.fill(.01);},disconnect(){}};}
    };
    window.AudioWorkletNode=class {
      constructor(){window.p2.nodes.push(this);this.port={postMessage:m=>window.p2.messages.push({t:m.t,d:m.d?Array.from(m.d):null})};}
      connect(){return {connect(){}};}
    };
    const create=URL.createObjectURL.bind(URL),revoke=URL.revokeObjectURL.bind(URL);
    URL.createObjectURL=blob=>{const url=create(blob);window.p2.created.push(url);return url;};
    URL.revokeObjectURL=url=>{window.p2.revoked.push(url);revoke(url);};
    window.p2.frame=(type,payload)=>{
      if(!(payload instanceof Uint8Array))payload=new TextEncoder().encode(JSON.stringify(payload));
      const out=new Uint8Array(9+payload.length),view=new DataView(out.buffer);
      view.setUint8(0,type);view.setUint32(1,0,true);view.setUint32(5,payload.length,true);out.set(payload,9);return out;
    };
    window.p2.respond=(chunks,close=true,index=window.p2.turns.length-1)=>{
      const turn=window.p2.turns[index];turn.cancelCount=0;
      turn.stream=new ReadableStream({start(controller){turn.controller=controller;for(const chunk of chunks)controller.enqueue(new Uint8Array(chunk));if(close)controller.close();},cancel(){turn.cancelCount++;}});
      turn.resolve(new Response(turn.stream,{headers:{'X-Session-Id':'synthetic-p2'}}));
    };
    const native=fetch;
    window.fetch=async(url,options={})=>{
      const path=new URL(url,location.href).pathname;
      if(path==='/api/health')return Response.json({ok:true,workers:[]});
      if(path==='/api/profiles')return Response.json({active:'voice',profiles:[{id:'voice',name:'Synthetic only',ref_text:'fixture',breath_files:[],candidates:[]}]});
      if(path==='/api/speak')return new Promise(resolve=>window.p2.turns.push({resolve,signal:options.signal,request:JSON.parse(options.body)}));
      if(path==='/api/telemetry'){window.p2.telemetry.push(JSON.parse(options.body));return Response.json({ok:true});}
      if(path==='/api/report'){window.p2.reports.push(JSON.parse(options.body));return Response.json({ok:true});}
      if(path.startsWith('/api/'))return Response.json({ok:true});
      return native(url,options);
    };
    window.p2.newRecorder=()=>new window.QttsMicrophoneRecorder({onClip:file=>{window.p2.clips++;window.p2.lastClip=file;},getFiles:()=>window.p2.files,onStatus(){}});
    window.p2.clips=0;
  },{failAudio,deferMedia});
  await page.goto('/p2-frontend');
  if(!recorderOnly){
    await page.locator('#access-token').fill('synthetic-p2-token-012345678901234567890123');
    await page.locator('#btn-unlock').click();await expect(page.locator('#profile')).toHaveValue('voice');
    await page.locator('#mode').selectOption('read');await page.locator('#text').fill('fixture only');
  }
}
export async function speak(page){await page.locator('#btn-speak').click();await expect.poll(()=>page.evaluate(()=>window.p2.turns.length)).toBe(1);}
export async function evidence(info,value){await info.attach('g0-observation',{contentType:'application/json',body:Buffer.from(JSON.stringify(value))});}
