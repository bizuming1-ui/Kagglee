import assert from 'node:assert/strict';
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {chromium} from '@playwright/test';
import config from '../playwright.config.js';
const expected=await readFile('kaggle/kaggle-fixed-step17.py','utf8');
const hash=value=>createHash('sha256').update(value).digest('hex');
const project=await (await fetch('http://127.0.0.1:3000/api/project')).json();
const browser=await chromium.launch(config.use.launchOptions);
const results=[];
try{
 for(let round=1;round<=3;round++){
  const context=await browser.newContext({permissions:['clipboard-read','clipboard-write'],viewport:round===3?{width:375,height:667}:{width:1440,height:900}});
  const page=await context.newPage();await page.goto('http://127.0.0.1:3001');
  await page.locator('#copy').waitFor({state:'visible'});
  await page.waitForFunction(()=>!document.getElementById('copy').disabled);
  assert.equal(await page.locator('#code').inputValue(),expected);
  await page.locator('#copy').click();
  assert.equal(await page.evaluate(()=>navigator.clipboard.readText()),expected);
  assert.match(await page.locator('#status').textContent(),/已复制全部/);
  const downloadEvent=page.waitForEvent('download');await page.getByText('下载 .py 文件',{exact:true}).click();
  const download=await downloadEvent;assert.equal(download.suggestedFilename(),'kaggle-fixed-step17.py');
  assert.equal(hash(await readFile(await download.path())),hash(expected));
  await page.evaluate(()=>Object.defineProperty(navigator.clipboard,'writeText',{configurable:true,value:async()=>{throw new Error('test denied')}}));
  await page.locator('#copy').click();await page.waitForFunction(()=>document.getElementById('status').textContent.includes('未允许自动复制'));
  assert.equal(await page.locator('#code').evaluate(e=>e.selectionEnd-e.selectionStart),expected.length);
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  results.push({round,bytes:Buffer.byteLength(expected),sha256:hash(expected),clipboard_exact:true,download_exact:true,denied_clipboard_selects_all:true,mobile:round===3});
  await context.close();
 }
 const after=await (await fetch('http://127.0.0.1:3000/api/project')).json();assert.deepEqual(after,project);
 const result={passed:true,rounds:results,formal_project_unchanged:true,formal_files:Object.keys(after.files).length};
 await writeFile('docs/validation/step17/copy-page.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result,null,2));
}finally{await browser.close();}
