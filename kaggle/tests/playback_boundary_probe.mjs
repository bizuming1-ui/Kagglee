// Read-only execution of the actual stage17 player prefix/worklet in Node VM.
// No browser AudioContext/device, network, trained model or listening acceptance.
import fs from 'node:fs';
import vm from 'node:vm';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
const path = new URL('../source/web/app.js', import.meta.url);
const source = fs.readFileSync(path, 'utf8');
const start = source.indexOf('  var M = class');
const end = source.indexOf('  var r = (t) =>');
assert(start >= 0 && end > start);
let clock = 1250;
const context = vm.createContext({TextDecoder, Float32Array, Uint8Array, ArrayBuffer, DataView,
  performance:{now:()=>clock}});
vm.runInContext(`(() => { ${source.slice(start,end)}; globalThis.extracted = {Player:P, Parser:M, worklet:V}; })()`, context);
const {Player, Parser, worklet} = context.extracted;
const cases=[];
for(const rate of [24000,44100,48000]) {
  for(const milliseconds of [20,50,51,100]) {
    clock=1250;
    const p=new Player(), commands=[];
    p.ctxRate=rate;p.node={port:{postMessage:m=>commands.push(m)}};p.beginStream(1000);
    p.st.fill=Math.round(rate*milliseconds/1000);p.lastPcmAt=clock;p.generationDone=true;
    p.tick();clock+=2000;p.tick();
    const played=commands.some(m=>m.t==='play');
    if(milliseconds<=50) assert.equal(played,false); else assert.equal(played,true);
    cases.push({case:'completed-short-tail',context_rate:rate,buffer_ms:milliseconds,play_command:played,
      final_state:p.state,remaining_samples:p.st.fill,stranded:!played&&p.st.fill>0,
      command_timestamp_before_any_audio_processing:p.firstPlayedMs||null});
  }
  const p=new Player();p.ctxRate=rate;
  const input=Float32Array.from({length:240},(_,i)=>i/1000);
  if(rate!==24000){
    const whole=p.resample(input);
    const splitPlayer=new Player();splitPlayer.ctxRate=rate;
    const a=splitPlayer.resample(input.slice(0,47)),b=splitPlayer.resample(input.slice(47));
    const joined=Float32Array.from([...a,...b]);
    assert.equal(whole.length,joined.length);
    let max=0;for(let i=0;i<whole.length;i++)max=Math.max(max,Math.abs(whole[i]-joined[i]));
    assert(max<1e-6);
    cases.push({case:'resampling-terminal-lookbehind',context_rate:rate,input_samples:240,output_samples:whole.length,
      nominal_ten_ms_samples:Math.round(rate*.01),partition_max_abs_difference:max,
      end_flush_present:false,note:'Interpolation requires next endpoint; terminal flush policy needs explicit design, not proof of audible damage.'});
  }
}
function makeRing(rate){
  let Ring;
  const reports=[];
  const c=vm.createContext({sampleRate:rate,Float32Array,
    AudioWorkletProcessor:class{constructor(){this.port={postMessage:m=>reports.push(m)};}},
    registerProcessor:(name,ctor)=>{assert.equal(name,'qtts-ring');Ring=ctor;}});
  vm.runInContext(worklet,c);
  const ring=new Ring();
  const send=m=>ring.port.onmessage({data:m});
  const process=n=>{const out=new Float32Array(n);ring.process([],[[out]]);assert(out.every(Number.isFinite));return out;};
  return {ring,send,process,reports};
}
for(const rate of [24000,48000]){
  {
    const {ring,send,process}=makeRing(rate);
    send({t:'pcm',d:new Float32Array(256).fill(.2)});send({t:'end'});send({t:'play'});
    assert.equal(ring.played,0);process(384);
    assert.equal(ring.played,256);assert.equal(ring.underruns,0);assert.equal(ring.fill,0);
    send({t:'reset'});assert(process(128).every(x=>x===0));
    cases.push({case:'worklet-natural-end-and-reset',context_rate:rate,played_samples:256,underruns:0,reset_output_exact_zero:true,
      fade_duration_ms:192/rate*1000,hardware_audio_executed:false});
  }
  {
    const {ring,send,process}=makeRing(rate);
    send({t:'pcm',d:new Float32Array(128).fill(.2)});send({t:'play'});process(256);
    assert.equal(ring.underruns,1);assert.equal(ring.playing,false);
    send({t:'pcm',d:new Float32Array(128).fill(.2)});send({t:'play'});send({t:'end'});process(256);
    assert.equal(ring.played,256);assert.equal(ring.underruns,1);
    cases.push({case:'worklet-starvation-and-resume',context_rate:rate,underruns:1,total_consumed_samples:256});
  }
  {
    const {ring,send}=makeRing(rate);ring.cap=8;ring.buf=new Float32Array(8);
    send({t:'pcm',d:new Float32Array(20).fill(.2)});
    assert.equal(ring.fill,8);assert.equal(ring.dropped,12);
    cases.push({case:'worklet-overflow-counting',context_rate:rate,received_samples:20,queued:8,dropped:12});
  }
}
{
  const bytes=new Uint8Array(13);const dv=new DataView(bytes.buffer);
  dv.setUint8(0,1);dv.setUint32(1,7,true);dv.setUint32(5,4,true);bytes.set([1,2,3,4],9);
  const parser=new Parser();let frames=[];
  for(const x of bytes)frames.push(...parser.push(new Uint8Array([x])));
  assert.equal(frames.length,1);assert.equal(frames[0].seg,7);assert.deepEqual(Array.from(frames[0].payload),[1,2,3,4]);
  cases.push({case:'fragmented-frame-byte-by-byte',frames:1,payload_preserved:true});
  const oversized=new Uint8Array(9);new DataView(oversized.buffer).setUint32(5,32*1024*1024+1,true);
  assert.throws(()=>new Parser().push(oversized),/32MiB/);
  cases.push({case:'oversized-frame-header',rejected:true});
}
assert.equal(cases.length,22);
console.log(JSON.stringify({round:Number(process.argv[2]||1),experiment_completed:true,
 source_sha256:crypto.createHash('sha256').update(source).digest('hex'),
 probe_sha256:crypto.createHash('sha256').update(fs.readFileSync(new URL(import.meta.url))).digest('hex'),
 cases,method:'actual player/parser prefix and AudioWorklet source evaluated in Node VM; mocked clock/ports/processor base',
 browser_device_executed:false,full_model_executed:false,gpu_executed:false,user_hiss_root_cause_proven:false,product_modified:false},null,2));
