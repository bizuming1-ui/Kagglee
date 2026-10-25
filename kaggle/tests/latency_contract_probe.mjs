// Q26 baseline state/metric contracts; actual Player code in Node VM, no audio device.
import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import crypto from 'node:crypto';
const source=fs.readFileSync(new URL('../source/web/app.js',import.meta.url),'utf8');
const lo=source.indexOf('  var M = class'),hi=source.indexOf('  var r = (t) =>');
assert(lo>=0&&hi>lo);
let clock=1250;
const ctx=vm.createContext({Float32Array,Uint8Array,DataView,ArrayBuffer,TextDecoder,performance:{now:()=>clock}});
vm.runInContext(`(() => { ${source.slice(lo,hi)};globalThis.Player=P; })()`,ctx);
const cases=[];
function player(state){
  clock=1250;const p=new ctx.Player(),commands=[];p.ctxRate=24000;
  p.node={port:{postMessage:m=>commands.push(m)}};p.beginStream(1000);p.state=state;p.lastPcmAt=clock;
  return {p,commands};
}
for(const state of ['buffering','starved']){
  for(const [done,ms] of [[false,20],[false,50],[true,20],[true,50],[true,51],[true,0]]){
    const {p,commands}=player(state);p.st.fill=Math.round(24*ms);p.generationDone=done;
    p.tick();clock=3250;p.tick();
    const played=commands.some(c=>c.t==='play');
    if(done&&ms===0)assert.equal(p.state,'ended');
    else if(done&&ms===51)assert.equal(played,true);
    else {assert.equal(played,false);assert.equal(p.state,state);}
    cases.push({case:'end-vs-live-buffer-policy',initial_state:state,generation_done:done,buffer_ms:ms,
      play_command:played,final_state:p.state,remaining_samples:p.st.fill,
      stranded_finished_tail:done&&ms>0&&!played});
  }
}
{
  const {p,commands}=player('playing');p.st.fill=480;p.generationDone=true;p.tick();
  assert.equal(p.state,'playing');assert(!commands.some(c=>c.t==='play'));
  cases.push({case:'already-playing-short-tail','playing_state_preserved':true,'duplicate_play_commands':0});
}
{
  const {p,commands}=player('buffering');
  const pcm=new Uint8Array(24000*2*2);const view=new DataView(pcm.buffer);
  for(let i=0;i<pcm.length;i+=2)view.setInt16(i,3277,true);
  clock=1300;p.pushPcm(pcm);assert.equal(p.firstPcmMs,300);assert.equal(p.firstPlayedMs,0);
  // A synthetic delayed status update, not real Worklet processing or device time.
  clock=1750;p.onWorklet({t:'st',fill:48000,played:0,underruns:0,playing:false,starved:false,dropped:0});
  assert.equal(p.firstPlayedMs,750);assert(commands.some(c=>c.t==='play'));assert.equal(p.st.played,0);
  cases.push({case:'pcm-command-consumption-distinction',synthetic_first_pcm_ms:p.firstPcmMs,
    legacy_firstPlayedMs:p.firstPlayedMs,worklet_consumed_samples:p.st.played,
    worklet_first_consumption_ms:null,hardware_audible_start_ms:null,
    observation:'legacy field is assigned before consumption; the synthetic 300/750ms values are NOT measured performance'});
}
for(const seconds of [.69,.70]){
  const {p,commands}=player('buffering');
  // Deliberately injected stable fast-arrival estimate isolates the threshold, not a network simulation.
  p.pred.stats=()=>({rate:2,sigma:0});p.pred.deficit=()=>0;p.st.fill=Math.round(seconds*24000);
  p.tick();assert.equal(commands.some(c=>c.t==='play'),seconds===.70);
  cases.push({case:'stable-fast-estimator-start-threshold',injected_estimator:true,buffer_seconds:seconds,
    need_seconds:p.needToStart(clock,false),play_command:commands.some(c=>c.t==='play')});
}
assert.equal(cases.length,16);
console.log(JSON.stringify({round:Number(process.argv[2]||1),experiment_completed:true,cases,
 source_sha256:crypto.createHash('sha256').update(source).digest('hex'),
 probe_sha256:crypto.createHash('sha256').update(fs.readFileSync(new URL(import.meta.url))).digest('hex'),
 method:'actual stage17 Player prefix in Node VM; injected monotonic clock, ports, status updates and two explicit estimator stubs',
 product_modified:false,performance_improvement_measured:false,browser_device_executed:false,
 full_model_executed:false,gpu_executed:false,user_hiss_root_cause_proven:false},null,2));
