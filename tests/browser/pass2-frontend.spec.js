import { test, expect } from '@playwright/test';
import { openFixture, speak, evidence } from './pass2-frontend-fixture.js';

// Execute entire frozen scripts in Chromium. Audio/HTTP/status events remain
// explicit fixtures; no true model/backend, microphone, sound card or timing claim.
const end = {timeline_ms:{},per_gpu:{}};
async function done(page){await expect.poll(()=>page.evaluate(()=>window.p2.reports.length)).toBe(1);}

test('P2 protection lock after network EOF cancels session clears chat and resets playback',async({page})=>{
  await openFixture(page);await page.locator('#mode').selectOption('chat');await speak(page);
  await page.evaluate(end=>window.p2.respond([window.p2.frame(3,{t:'private fixture answer'}),window.p2.frame(1,new Uint8Array(4800)),window.p2.frame(5,end)]),end);
  await done(page);await page.locator('#btn-lock').click();
  await expect(page.locator('#text')).toHaveValue('');await expect(page.locator('#llmout')).toHaveText('');
  expect(await page.evaluate(()=>({aborted:window.p2.turns[0].signal.aborted,last:window.p2.messages.slice(-2).map(m=>m.t)}))).toEqual({aborted:true,last:['hold','reset']});
  await page.locator('#access-token').fill('synthetic-pass2-token-01234567890123456789');await page.locator('#btn-unlock').click();await expect(page.locator('#profile')).toHaveValue('voice');
  await page.locator('#text').fill('new access session');await page.locator('#btn-speak').click();
  await expect.poll(()=>page.evaluate(()=>window.p2.turns.length)).toBe(2);
  expect(await page.evaluate(()=>window.p2.turns[1].request.history)).toEqual([]);
  await page.locator('#btn-stop').click();
  await page.evaluate(end=>window.p2.respond([window.p2.frame(5,end)]),end);
});

test('P2 protection pagehide during an open body aborts late data without a report',async({page})=>{
  await openFixture(page);await speak(page);
  await page.evaluate(()=>window.p2.respond([window.p2.frame(3,{t:'private prefix'})],false));
  await expect(page.locator('#llmout')).toHaveText('private prefix');
  await page.evaluate(()=>window.dispatchEvent(new Event('pagehide')));
  expect(await page.evaluate(()=>window.p2.turns[0].signal.aborted)).toBe(true);
  await page.evaluate(end=>{window.p2.turns[0].controller.enqueue(window.p2.frame(5,end));},end);
  await expect(page.locator('#llmout')).toHaveText('');
  await expect.poll(()=>page.evaluate(()=>window.p2.turns[0].cancelCount)).toBe(1);
  expect(await page.evaluate(()=>window.p2.reports.length)).toBe(0);
});

test('P2 protection HTTP503 JSON error ends UI wait without PCM or client success report',async({page})=>{
  await openFixture(page);await speak(page);
  await page.evaluate(()=>window.p2.turns[0].resolve(Response.json({error:'fixture HTTP503'},{status:503})));
  await expect(page.locator('#errbox')).toContainText('fixture HTTP503');await expect(page.locator('#btn-speak')).toBeEnabled();
  expect(await page.evaluate(()=>({pcm:window.p2.messages.filter(m=>m.t==='pcm').length,reports:window.p2.reports.length,end:window.p2.messages.filter(m=>m.t==='end').length}))).toEqual({pcm:0,reports:0,end:1});
});

test('P2 protection stream read rejection is visible and releases the send button',async({page})=>{
  await openFixture(page);await speak(page);
  await page.evaluate(()=>window.p2.respond([window.p2.frame(3,{t:'prefix before read error'})],false));
  await expect(page.locator('#llmout')).toHaveText('prefix before read error');
  await page.evaluate(()=>window.p2.turns[0].controller.error(new Error('fixture read rejection')));
  await expect(page.locator('#errbox')).toContainText('fixture read rejection');await expect(page.locator('#btn-speak')).toBeEnabled();
  // Existing catch/report behavior is retained, NOT a cancellation/complete-stream success assertion.
  await done(page);await page.locator('#btn-stop').click();
});

test('P2 protection malformed END JSON cannot populate a success timeline',async({page})=>{
  await openFixture(page);await speak(page);
  await page.evaluate(()=>window.p2.respond([window.p2.frame(5,new TextEncoder().encode('{'))]));
  await expect(page.locator('#errbox')).not.toBeEmpty();await expect(page.locator('#btn-speak')).toBeEnabled();await expect(page.locator('#timeline')).toHaveText('');
  expect(await page.evaluate(()=>window.p2.messages.filter(m=>m.t==='pcm').length)).toBe(0);await page.locator('#btn-stop').click();
});

test('P2 protection byte fragmented multilingual text renders as text not HTML',async({page})=>{
  await openFixture(page);await speak(page);
  const text='你好🙂「日本語」 한국어 <img src=x onerror="window.injected=true"> **literal**';
  await page.evaluate(({text,end})=>{
    const bytes=[...window.p2.frame(3,{t:text}),...window.p2.frame(5,end)];window.p2.respond(bytes.map(b=>[b]));
  },{text,end});
  await done(page);await expect(page.locator('#llmout')).toHaveText(text);expect(await page.locator('#llmout img').count()).toBe(0);
  expect(await page.evaluate(()=>window.injected)).toBeUndefined();await expect(page.locator('#errbox')).toHaveText('');
});

test('P2 protection recorder rechecks file budget at finish after another file is added',async({page})=>{
  await openFixture(page,{recorderOnly:true});
  const result=await page.evaluate(async()=>{
    const recorder=window.p2.newRecorder();recorder.maxFiles=1;await recorder.start();const s=recorder.session;
    s.recorder.ondataavailable({data:new Blob(['fixture'])});s.durationMs=1700;
    window.p2.files.push(new File(['other'],'other.webm'));s.recorder.onstop();
    const result={clips:window.p2.clips,discard:s.discard,chunks:s.chunks.length,state:recorder.state,stopped:s.stream.getTracks()[0].stopped};recorder.cancel();return result;
  });
  expect(result).toEqual({clips:0,discard:true,chunks:0,state:'idle',stopped:true});
});

test('P2 protection duplicate recorder stop callback commits the clip only once',async({page})=>{
  await openFixture(page,{recorderOnly:true});
  const result=await page.evaluate(async()=>{
    const recorder=window.p2.newRecorder();await recorder.start();const s=recorder.session;
    s.recorder.ondataavailable({data:new Blob(['fixture'],{type:'audio/webm'})});s.durationMs=1700;
    s.recorder.onstop();s.recorder.onstop();
    const result={clips:window.p2.clips,size:window.p2.lastClip.size,session:recorder.session,chunks:s.chunks.length,state:recorder.state,stopped:s.stream.getTracks()[0].stopped};recorder.cancel();return result;
  });
  expect(result).toEqual({clips:1,size:7,session:null,chunks:0,state:'idle',stopped:true});
});

test('P2 protection stale track ended event cannot stop the current recorder',async({page})=>{
  await openFixture(page,{recorderOnly:true});
  const result=await page.evaluate(async()=>{
    const recorder=window.p2.newRecorder();await recorder.start();const old=recorder.session;
    recorder.cancel();await recorder.start();const current=recorder.session;
    old.stream.getTracks()[0].handlers.ended();
    const result={owned:recorder.owns(current),stopped:current.stream.getTracks()[0].stopped,state:recorder.state,clips:window.p2.clips};recorder.cancel();return result;
  });
  expect(result).toEqual({owned:true,stopped:false,state:'recording',clips:0});
});

test('P2 protection audio initialization can recover after a first module rejection',async({page})=>{
  await openFixture(page,{failAudio:true});await page.locator('#btn-speak').click();
  await expect(page.locator('#errbox')).toContainText('p2 synthetic addModule rejection');
  expect(await page.evaluate(()=>window.p2.turns.length)).toBe(0);
  await page.locator('#btn-speak').click();await expect.poll(()=>page.evaluate(()=>window.p2.turns.length)).toBe(1);
  await page.evaluate(end=>window.p2.respond([window.p2.frame(5,end)]),end);await done(page);
  expect(await page.evaluate(()=>({contexts:window.p2.contexts.length,oldClosed:window.p2.contexts[0].state,newRunning:window.p2.contexts[1].state,created:window.p2.created.length,revoked:window.p2.revoked.length}))).toEqual({contexts:2,oldClosed:'closed',newRunning:'running',created:2,revoked:1});
  await expect(page.locator('#errbox')).toHaveText(''); // old failed-module Blob URL still unreclaimed: F06 NOT fixed
});

test('P2 OBSERVED_NOT_FIXED terminal END does not prevent later PCM text or replacement summary',async({page},info)=>{
  await openFixture(page);await speak(page);
  await page.evaluate(end=>window.p2.respond([
    window.p2.frame(5,end),window.p2.frame(1,new Uint8Array([1,0])),window.p2.frame(3,{t:'after terminal'}),
    window.p2.frame(5,{timeline_ms:{replacement_summary:7},per_gpu:{}})
  ]),end);
  await done(page);await expect(page.locator('#llmout')).toHaveText('after terminal');await expect(page.locator('#timeline')).toContainText('replacement_summary');await expect(page.locator('#errbox')).toHaveText('');
  const result=await page.evaluate(()=>({latePCM:window.p2.messages.filter(m=>m.t==='pcm').map(m=>m.d),reportCount:window.p2.reports.length}));
  expect(result).toEqual({latePCM:[[1/32768]],reportCount:1});
  await evidence(info,{id:'S18-G0-PASS2-F25',fixed:false,endFrames:2,postEndPCMForwarded:true,postEndTextDisplayed:true,laterSummaryReplacesFirst:true,fullFrozenBrowserScript:true,wireAndAudioDevicesAreFixtures:true,actualModelExecuted:false});
  await page.locator('#btn-stop').click();
});

test('P2 OBSERVED_NOT_FIXED report sent at EOF misses subsequent playback and underrun status',async({page},info)=>{
  await openFixture(page);await speak(page);
  await page.evaluate(end=>window.p2.respond([window.p2.frame(1,new Uint8Array(9600)),window.p2.frame(5,end)]),end);await done(page);
  const before=await page.evaluate(()=>({report:{...window.p2.reports[0]},telemetry:window.p2.telemetry.length}));
  expect(before.report.first_played_ms).toBe(0);expect(before.report.underruns).toBe(0);
  await page.evaluate(()=>window.p2.nodes[0].port.onmessage({data:{t:'st',fill:4800,played:0,underruns:0,playing:false,starved:false,dropped:0}}));
  await expect(page.locator('#pstate')).toHaveText('播放中');
  await page.evaluate(()=>window.p2.nodes[0].port.onmessage({data:{t:'st',fill:0,played:4800,underruns:1,playing:false,starved:true,dropped:0}}));
  // Give the actual 250ms UI/telemetry interval a task window, NOT a latency benchmark.
  await expect(page.locator('#m-under')).toHaveText('1');
  const after=await page.evaluate(()=>({reports:window.p2.reports.length,report:window.p2.reports[0],telemetry:window.p2.telemetry.length,play:window.p2.messages.filter(m=>m.t==='play').length}));
  expect(after.reports).toBe(1);expect(after.report).toEqual(before.report);expect(after.telemetry).toBe(before.telemetry);expect(after.play).toBe(1);
  await evidence(info,{id:'S18-G0-PASS2-F26',fixed:false,reportCount:1,reportSentBeforePlayCommand:true,reportedFirstPlayedMs:0,reportedUnderruns:0,laterUIUnderruns:1,noFinalReportRefresh:true,telemetryStopsAtNetworkEOF:true,workletStatusAndDevicesAreFixtures:true,physicalAudibleStartMeasured:false,actualModelExecuted:false});
  await page.locator('#btn-stop').click();
});
