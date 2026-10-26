import http from 'node:http';
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { fileURLToPath } from 'node:url';
const path=fileURLToPath(new URL('../kaggle/delivery18/artifacts/kaggle-step18-candidate.py',import.meta.url));
const code=readFileSync(path);
const digest=createHash('sha256').update(code).digest('hex');
if(digest!=='f54346e232b44750f77c506bc9cefd155edd809c0f7444092621fc7b0bb4fab7')throw new Error('Delivered code SHA mismatch');
const page=String.raw`<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>完整 Kaggle 代码输出框</title>
<style>*{box-sizing:border-box}body{margin:0;background:#10151d;color:#e6edf5;font:15px/1.6 system-ui,sans-serif}main{max-width:1500px;margin:auto;padding:24px}h1{font-size:24px;margin:0 0 10px}.note{color:#b4c0d0;margin:8px 0}.bar{display:flex;flex-wrap:wrap;align-items:center;gap:12px;margin:18px 0}button,a{font:inherit;border:1px solid #40516b;border-radius:7px;padding:9px 18px;background:#24334a;color:#fff;text-decoration:none;cursor:pointer}button.primary{background:#297bdf;border-color:#297bdf}button:disabled{opacity:.5;cursor:wait}#status{color:#91d6ba}textarea{display:block;width:100%;height:68vh;min-height:360px;background:#0b1017;color:#dce8f5;border:1px solid #40516b;border-radius:8px;padding:16px;font:13px/1.6 ui-monospace,Consolas,monospace;tab-size:4;resize:vertical;white-space:pre;overflow:auto}details{margin-top:16px;color:#b4c0d0}code{overflow-wrap:anywhere}</style></head>
<body><main><h1>完整 Kaggle 代码输出框</h1>
<p class="note">当前可核验 S5 基线的完整候选 · 内嵌 58 个源码资产 · 不是补丁或省略版。</p>
<p class="note">S6–S8-C 文件当前缺失，未冒称合入。真实双 T4、训练、音质和速度尚未签收。完整代码粘贴到 Kaggle 后默认只校验，不自动安装或启动。</p>
<div class="bar"><button id="copy" class="primary" disabled>复制全部代码</button><button id="select" disabled>全选代码</button><a href="./download">下载完整 .py</a><span id="status" role="status" aria-live="polite">正在加载并校验完整代码…</span></div>
<textarea id="code" readonly wrap="off" spellcheck="false" aria-label="完整 Kaggle Python 代码"></textarea>
<details><summary>完整性与运行说明</summary><p>文件：kaggle-step18-candidate.py · 286135 字节。输出框不做格式化、不省略、不替换源码。</p><p>SHA256：<code>f54346e232b44750f77c506bc9cefd155edd809c0f7444092621fc7b0bb4fab7</code></p><p>在 Kaggle 选择 GPU T4×2、Internet On。完整粘贴并校验通过后，在下一单元格执行：</p><pre>main(["--run", "--destination", "/kaggle/working/qtts18-new"])</pre><p>目标目录必须不存在；不要覆盖旧目录或强删旧进程锁。浏览器若禁止剪贴板，请点“全选代码”后按 Ctrl+C / Command+C，或下载文件。</p></details>
</main><script>
const box=document.getElementById('code'),copy=document.getElementById('copy'),select=document.getElementById('select'),status=document.getElementById('status');
let source='';
function selectAll(){box.focus();box.select();box.setSelectionRange(0,box.value.length);}
select.onclick=()=>{selectAll();status.textContent='已选中全部代码，请按 Ctrl+C / Command+C。';};
copy.onclick=async()=>{try{if(box.value!==source)throw new Error('内容变化，请重新加载');await navigator.clipboard.writeText(source);status.textContent='已复制全部 '+new TextEncoder().encode(source).length+' 字节代码。';}catch(e){selectAll();status.textContent='浏览器未允许一键复制；已全选，请按 Ctrl+C / Command+C。';}};
(async()=>{try{const response=await fetch('./code',{cache:'no-store'});if(!response.ok)throw new Error('加载失败');const bytes=await response.arrayBuffer();if(bytes.byteLength!==286135)throw new Error('字节数不一致');const hash=Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',bytes)),b=>b.toString(16).padStart(2,'0')).join('');if(hash!=='f54346e232b44750f77c506bc9cefd155edd809c0f7444092621fc7b0bb4fab7')throw new Error('SHA256 不一致');source=new TextDecoder('utf-8',{fatal:true}).decode(bytes);box.value=source;copy.disabled=false;select.disabled=false;status.textContent='完整代码已加载 · 286135 字节 · SHA256 校验通过';}catch(e){status.textContent='未显示不完整代码：'+e.message+'。请使用下载文件或刷新重试。';}})();
</script></body></html>`;
http.createServer((req,res)=>{
 const route=new URL(req.url,'http://output.local').pathname;
 res.setHeader('Cache-Control','no-store');res.setHeader('X-Content-Type-Options','nosniff');
 if(req.method!=='GET'&&req.method!=='HEAD'){res.writeHead(405);return res.end();}
 let body;
 if(route==='/'||route==='/index.html'){res.setHeader('Content-Type','text/html; charset=utf-8');body=Buffer.from(page);}
 else if(route==='/code'||route==='/download'){res.setHeader('Content-Type','text/plain; charset=utf-8');if(route==='/download')res.setHeader('Content-Disposition','attachment; filename="kaggle-step18-candidate.py"');body=code;}
 else{res.writeHead(404);return res.end('Not found');}
 res.setHeader('Content-Length',body.length);res.writeHead(200);res.end(req.method==='HEAD'?undefined:body);
}).listen(8080,'0.0.0.0',()=>console.log('完整代码输出框已就绪，端口 8080；286135 字节，源码 SHA256 已核对。'));
