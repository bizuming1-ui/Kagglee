// Actual Player/Worklet VM contracts, synthetic PCM/ports/clocks. Not a sound device.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import crypto from 'node:crypto';
import {wire,load,pcm,sourcePath} from './step18_playback_fixture.mjs';
const target=process.argv.includes('--frozen')?'frozen17':'candidate';
const round=Number(process.argv.find(x=>x.startsWith('--round='))?.split('=')[1]||0);
const cases=[];
function test(name,fn){try{const evidence=fn();cases.push({name,status:'pass',evidence:evidence??null});}catch(e){cases.push({name,status:'fail',error:String(e.stack)});}}
for(const rate of [24000,44100,48000]){
 for(const n of [1,480,1200])test(`drain-${rate}-${n}`,()=>{
  const w=wire(target,rate);w.p.pushPcm(pcm(n));w.p.markGenerationDone();w.drain();
  const expected=Math.ceil(n*rate/24000);assert.equal(w.ring.played,expected);assert.equal(w.ring.dropped,0);assert.equal(w.ring.fill,0);assert.equal(w.p.state,'ended');
  return {input:n,consumed:w.ring.played,rate,device:false};
 });
 test(`starved-recovery-${rate}`,()=>{
  const w=wire(target,rate);w.p.state='starved';w.p.pushPcm(pcm(480));w.p.markGenerationDone();w.drain();assert.equal(w.ring.played,Math.ceil(480*rate/24000));
 });
 test(`live-short-must-wait-${rate}`,()=>{
  const w=wire(target,rate);w.p.pushPcm(pcm(480));for(let i=0;i<20;i++)w.step();assert.equal(w.ring.played,0);assert.equal(w.p.state,'buffering');
 });
 test(`resample-partition-${rate}`,()=>{
  const n=1703,input=pcm(n,i=>Math.round(Math.sin(i*.13)*5000));
  function run(sizes){const w=wire(target,rate);let at=0,j=0;while(at<n){let end=Math.min(n,at+sizes[j++%sizes.length]);w.p.pushPcm(input.slice(at*2,end*2));at=end;}w.p.markGenerationDone();return w.messages.filter(x=>x.t==='pcm').flatMap(x=>Array.from(x.d));}
  const a=run([n]),b=run([1,17,47,120,3]);assert.equal(a.length,Math.ceil(n*rate/24000));assert.deepEqual(a,b);
  const floats=Array.from({length:n},(_,i)=>new DataView(input.buffer).getInt16(i*2,true)/32768);
  const expected=Array.from({length:a.length},(_,k)=>{const q=k*24000;const i=Math.floor(q/rate);const f=(q%rate)/rate;return Math.fround(floats[i]+((floats[i+1]??floats[n-1])-floats[i])*f);});assert.deepEqual(a,expected);
 });
 test(`stop-late-status-${rate}`,()=>{
  const w=wire(target,rate),epoch=w.p.streamEpoch;w.p.pushPcm(pcm(480));w.p.stop();w.p.onWorklet({t:'st',epoch,fill:rate*4,played:0,underruns:0,dropped:0,playing:false,starved:false,endAck:false});w.p.tick();assert.equal(w.p.state,'idle');
 });
}
test('stale-empty-status-cannot-end-posted-audio',()=>{const w=wire(target);w.p.pushPcm(pcm(1));w.p.markGenerationDone();w.advance(3000);w.p.tick();assert.notEqual(w.p.state,'ended');w.drain();assert.equal(w.ring.played,1);});
test('old-epoch-cannot-start-new-stream',()=>{const w=wire(target);const old=w.p.streamEpoch;w.p.stop();w.p.beginStream(1000);w.p.onWorklet({epoch:old,fill:96000,played:0,dropped:0,underruns:0,endAck:true});assert.equal(w.p.state,'buffering');assert.equal(w.p.st.played,0);});
test('empty-stream-no-added-pcm',()=>{const w=wire(target);w.p.markGenerationDone();assert.equal(w.messages.filter(x=>x.t==='pcm').length,0);w.drain();assert.equal(w.ring.played,0);});
test('mark-done-idempotent',()=>{const w=wire(target,48000);w.p.pushPcm(pcm(1));w.p.markGenerationDone();const n=w.messages.length;w.p.markGenerationDone();assert.equal(w.messages.length,n);w.drain();assert.equal(w.ring.played,2);});
test('no-pcm-after-end-marker',()=>{const w=wire(target);w.p.pushPcm(pcm(1));w.p.markGenerationDone();assert.throws(()=>w.p.pushPcm(pcm(1)),/after generation end/);});
test('odd-pcm-rejected',()=>{const w=wire(target);assert.throws(()=>w.p.pushPcm(new Uint8Array(3)),/int16/);});
test('cancel-does-not-flush-endpoint',()=>{const w=wire(target,48000);w.p.pushPcm(pcm(1));w.p.stop();const n=w.messages.filter(x=>x.t==='pcm').reduce((n,m)=>n+m.d.length,0);w.p.markGenerationDone();w.p.pushPcm(pcm(100));assert.equal(w.messages.filter(x=>x.t==='pcm').reduce((n,m)=>n+m.d.length,0),n);w.step();assert.equal(w.ring.played,0);});
test('end-ack-required',()=>{const w=wire(target);w.p.markGenerationDone();w.advance(3000);w.p.tick();assert.notEqual(w.p.state,'ended');w.drain();assert.equal(w.p.state,'ended');});
test('already-playing-no-duplicate-play',()=>{const w=wire(target);w.p.pred.stats=()=>({rate:2,sigma:0});w.p.pred.deficit=()=>0;w.p.pushPcm(pcm(24000));const n=w.messages.filter(x=>x.t==='play').length;assert.equal(n,1);w.p.markGenerationDone();w.p.tick();assert.equal(w.messages.filter(x=>x.t==='play').length,n);w.drain();});
test('one-underrun-and-recovery',()=>{const w=wire(target);w.p.pred.stats=()=>({rate:2,sigma:0});w.p.pred.deficit=()=>0;w.p.pushPcm(pcm(24000));for(let i=0;i<230;i++)w.step();assert.equal(w.ring.underruns,1);w.p.pushPcm(pcm(480));w.p.markGenerationDone();w.drain();assert.equal(w.ring.played,24480);assert.equal(w.ring.underruns,1);});
test('overflow-accounted-not-lossless',()=>{const w=wire(target);w.ring.cap=8;w.ring.buf=new Float32Array(8);w.p.pushPcm(pcm(20));w.p.markGenerationDone();w.drain();assert.equal(w.ring.played,8);assert.equal(w.ring.dropped,12);assert.equal(w.p.status().droppedSamples,12);});
test('begin-clears-resampler-history',()=>{const w=wire(target,44100);w.p.pushPcm(pcm(7));w.p.stop();w.p.beginStream(1000);const at=w.messages.length;w.p.pushPcm(pcm(1,7000));w.p.markGenerationDone();const out=w.messages.slice(at).filter(m=>m.t==='pcm').flatMap(m=>Array.from(m.d));assert.equal(out.length,2);assert(out.every(x=>x===7000/32768));});
test('old-epoch-pcm-rejected-by-ring',()=>{const w=wire(target);const old=w.p.streamEpoch;w.p.stop();w.p.beginStream(1000);w.deliver();w.ring.port.onmessage({data:{t:'pcm',epoch:old,d:new Float32Array([.2])}});assert.equal(w.ring.fill,0);});
test('reset-output-exact-zero',()=>{const w=wire(target);w.p.pushPcm(pcm(20000));w.step();w.p.stop();assert(w.step().every(x=>x===0));});
test('zero-pcm-is-consumed-not-claimed-audible',()=>{const w=wire(target);w.p.pushPcm(pcm(480,0));w.p.markGenerationDone();w.drain();assert.equal(w.ring.played,480);});
test('rational-resampler-rate-validation',()=>{const {Player}=load(target);const p=new Player();p.ctxRate=0;assert.throws(()=>p.resample(new Float32Array([.1])),/rate/);});
const sha=s=>crypto.createHash('sha256').update(s).digest('hex');
const result={target,round,tests:cases.length,passed:cases.filter(x=>x.status==='pass').length,failures:cases.filter(x=>x.status==='fail').length,cases,source_sha256:sha(fs.readFileSync(sourcePath(target))),test_sha256:sha(fs.readFileSync(new URL(import.meta.url))),fixture_sha256:sha(fs.readFileSync(new URL('./step18_playback_fixture.mjs',import.meta.url))),actual_player_and_worklet_vm:true,physical_audio_device:false,model_gpu_or_acoustic_validation:false};
console.log(JSON.stringify(result,null,2));if(result.failures)process.exitCode=1;
