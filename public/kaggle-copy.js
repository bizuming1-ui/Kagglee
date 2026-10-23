const $=id=>document.getElementById(id);
let source='';
const expected='6eacaede14f9b5f42ac5c334df5c3f9d1a1c6858fb69b7d3a8ff241ec60427ea';
function selectAll(){ $('code').focus();$('code').select();$('code').setSelectionRange(0,source.length); }
$('select').addEventListener('click',()=>{selectAll();$('status').textContent='已选中全部代码，请按 Ctrl+C（Mac：⌘C）复制。';});
$('copy').addEventListener('click',async()=>{
  if(!source)return;
  $('copy').disabled=true;
  try{await navigator.clipboard.writeText(source);$('status').textContent='已复制全部代码 ✓ 请粘贴到 Kaggle 的一个 Code 单元格。';}
  catch{selectAll();$('status').textContent='浏览器未允许自动复制。已选中全部代码，请按 Ctrl+C（Mac：⌘C）。';}
  finally{$('copy').disabled=false;}
});
(async()=>{
  try{
    const response=await fetch('/api/code',{cache:'no-store'});if(!response.ok)throw new Error('load');
    const data=await response.json();
    if(typeof data.code!=='string'||data.filename!=='kaggle-fixed-step17.py'||data.sha256!==expected||data.bytes!==313504)throw new Error('metadata');
    const bytes=new TextEncoder().encode(data.code);
    const digest=Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',bytes)),b=>b.toString(16).padStart(2,'0')).join('');
    if(bytes.length!==data.bytes||digest!==expected)throw new Error('integrity');
    source=data.code;$('code').value=source;$('size').textContent=`${data.bytes.toLocaleString()} 字节 · 完整代码`;
    $('hash').textContent=digest;$('copy').disabled=false;$('select').disabled=false;
    $('status').textContent='完整性校验通过。点击“复制全部代码”，不用手动逐段复制。';
  }catch{$('status').textContent='完整代码加载或校验失败，复制已禁用。请刷新重试，或下载 .py 文件。';}
})();
