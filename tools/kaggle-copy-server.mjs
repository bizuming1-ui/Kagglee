// Dedicated read-only delivery preview. Never writes the user's workbench.
import http from 'node:http';
import { readFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const filename='kaggle-fixed-step17.py';
const expected='6eacaede14f9b5f42ac5c334df5c3f9d1a1c6858fb69b7d3a8ff241ec60427ea';
const raw=await readFile(path.join(root,'kaggle',filename));
if(createHash('sha256').update(raw).digest('hex')!==expected)throw new Error('Frozen step17 hash mismatch');
const payload=JSON.stringify({filename,sha256:expected,bytes:raw.length,code:raw.toString('utf8')});
const assets=new Map([['/',['kaggle-copy.html','text/html; charset=utf-8']],['/copy.js',['kaggle-copy.js','text/javascript; charset=utf-8']],['/copy.css',['kaggle-copy.css','text/css; charset=utf-8']]]);
const server=http.createServer(async(req,res)=>{
  res.setHeader('X-Content-Type-Options','nosniff');res.setHeader('Cache-Control','no-store');
  res.setHeader('Content-Security-Policy',"default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'none'");
  if(req.method!=='GET'&&req.method!=='HEAD'){res.writeHead(405);res.end();return;}
  const route=new URL(req.url,'http://internal').pathname;
  if(route==='/api/code'){res.setHeader('Content-Type','application/json; charset=utf-8');res.end(req.method==='HEAD'?undefined:payload);return;}
  if(route==='/kaggle-fixed-step17.py'){
    res.setHeader('Content-Type','text/x-python; charset=utf-8');res.setHeader('Content-Disposition',`attachment; filename="${filename}"`);res.end(req.method==='HEAD'?undefined:raw);return;
  }
  const asset=assets.get(route);
  if(!asset){res.writeHead(404);res.end('Not found');return;}
  try{const content=await readFile(path.join(root,'public',asset[0]));res.setHeader('Content-Type',asset[1]);res.end(req.method==='HEAD'?undefined:content);}
  catch{res.writeHead(500);res.end('Delivery page unavailable');}
});
server.listen(Number(process.env.PORT||3001),'0.0.0.0',()=>console.log('Kaggle code copy page ready'));
for(const signal of ['SIGINT','SIGTERM'])process.on(signal,()=>server.close(()=>process.exit(0)));
