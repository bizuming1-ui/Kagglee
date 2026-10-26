import { chromium as playwrightChromium } from 'playwright';
import config from '../playwright.config.js';
import { readFile, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import assert from 'node:assert/strict';
const source=await readFile(new URL('../kaggle/delivery18/artifacts-startup-return-fix/kaggle-step18-candidate.py',import.meta.url));
const sha=b=>createHash('sha256').update(b).digest('hex');
const browser=await playwrightChromium.launch({...config.use.launchOptions,headless:true});
try{
 for(let round=1;round<=3;round++){
  const context=await browser.newContext();await context.grantPermissions(['clipboard-read','clipboard-write'],{origin:'http://127.0.0.1:8082'});
  const page=await context.newPage();await page.goto('http://127.0.0.1:8082/');await page.waitForFunction(()=>!document.querySelector('#copy').disabled);
  const value=await page.locator('#code').inputValue();assert.equal(sha(Buffer.from(value)),sha(source));
  await page.locator('#copy').click();const copied=await page.evaluate(()=>navigator.clipboard.readText());assert.equal(sha(Buffer.from(copied)),sha(source));
  const pending=page.waitForEvent('download');await page.getByText('下载完整 .py',{exact:true}).click();const download=await pending;assert.equal(sha(await readFile(await download.path())),sha(source));
  await page.evaluate(()=>Object.defineProperty(navigator,'clipboard',{configurable:true,value:{writeText:async()=>{throw new Error('controlled permission denial');}}}));
  await page.locator('#copy').click();assert.deepEqual(await page.locator('#code').evaluate(e=>[e.selectionStart,e.selectionEnd]),[0,value.length]);
  assert.match(await page.locator('#status').textContent(),/浏览器未允许/);
  const result={round,passed:true,full_textarea_sha256:sha(source),bytes:source.length,native_clipboard_exact:true,native_download_exact:true,clipboard_denied_select_all_fallback:true,local_chromium_not_remote_colab:true};
  await writeFile(new URL(`../docs/validation/step18/startup-return-fix/browser-round${round}.json`,import.meta.url),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));await context.close();
 }
}finally{await browser.close();}
