import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
export function sourcePath(target='candidate') {
  return new URL(target==='candidate'?'../step18/web/app.js':'../source/web/app.js',import.meta.url);
}
export function extract(source){
  const a=source.indexOf('  var M = class'),b=source.indexOf('  var r = (t) =>');
  assert(a>=0&&b>a);return source.slice(a,b);
}
export function load(target='candidate'){
  const source=fs.readFileSync(sourcePath(target),'utf8');let clock=1000;
  const ctx=vm.createContext({Float32Array,Uint8Array,DataView,ArrayBuffer,TextDecoder,performance:{now:()=>clock}});
  vm.runInContext(`(()=>{${extract(source)};globalThis.s5={Player:P,worklet:V};})()`,ctx);
  return {...ctx.s5,source,advance(ms=10){clock+=ms;}};
}
export function pcm(n,value=5000){
  const a=new Uint8Array(n*2),v=new DataView(a.buffer);
  for(let i=0;i<n;i++)v.setInt16(i*2,typeof value==='function'?value(i):value,true);
  return a;
}
export function wire(target='candidate',rate=24000){
  const api=load(target);let Ring;const reports=[],messages=[],queue=[];
  vm.runInNewContext(api.worklet,{sampleRate:rate,Float32Array,
    AudioWorkletProcessor:class{constructor(){this.port={postMessage:m=>reports.push(m)};}},
    registerProcessor:(name,ctor)=>{assert.equal(name,'qtts-ring');Ring=ctor;}});
  const ring=new Ring(),p=new api.Player();p.ctxRate=rate;
  p.node={port:{postMessage:m=>{messages.push(m);queue.push(m);}}};p.beginStream(900);
  function deliver(){while(queue.length)ring.port.onmessage({data:queue.shift()});}
  function step(n=128){deliver();const out=new Float32Array(n);ring.process([],[[out]]);api.advance(n*1000/rate);while(reports.length)p.onWorklet(reports.shift());p.tick();return out;}
  function drain(max=3000){for(let i=0;i<max;i++){step();if(p.state==='ended')return;}assert.fail(`drain timeout state=${p.state}, fill=${ring.fill}, played=${ring.played}`);}
  return {p,ring,messages,queue,reports,deliver,step,drain,...api};
}
