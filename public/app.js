import { CORE_FILES, MAX_FILES, fileNameError } from './file-rules.js';
const $ = selector => document.querySelector(selector);
const $$ = selector => [...document.querySelectorAll(selector)];
let names = [...CORE_FILES];
const languages = { 'index.html': 'HTML', 'style.css': 'CSS', 'script.js': 'JavaScript' };
const tabIds = { 'index.html': 'tab-html', 'style.css': 'tab-css', 'script.js': 'tab-js' };
const editor = $('#code');
let files = Object.fromEntries(names.map(name => [name, '']));
let savedFiles = { ...files };
let revision = null;
let savedAt = null;
let storagePath = '';
let activeFile = 'index.html';
let loading = true;
let saving = false;
let saveError = '';
let toastTimer;
let port;
let logs = [];
let runNumber = 0;
const cursors = {};

const dirty = () => [...new Set([...Object.keys(files), ...Object.keys(savedFiles)])].some(name => files[name] !== savedFiles[name]);
function toast(message, error = false) {
  const node = $('#toast');
  clearTimeout(toastTimer);
  node.textContent = message;
  node.classList.toggle('error', error);
  node.hidden = false;
  toastTimer = setTimeout(() => { node.hidden = true; }, error ? 9000 : 4000);
}
function renderFiles() {
  names = [...CORE_FILES, ...Object.keys(files).filter(name => !CORE_FILES.includes(name)).sort()];
  const list = $('.file-list');
  const tabs = $('.editor-tabs');
  const toggle = $('#toggle-sidebar');
  list.replaceChildren();
  tabs.replaceChildren();
  names.forEach((name, index) => {
    const extension = name.split('.').at(-1).toLowerCase();
    const kind = ['html', 'htm'].includes(extension) ? 'html' : extension === 'css' ? 'css' : extension === 'js' ? 'js' : 'text';
    const symbol = { html: '◇', css: '#', js: 'JS', text: '≡' }[kind];
    tabIds[name] = `tab-file-${index}`;
    for (const isTab of [false, true]) {
      const button = document.createElement('button');
      button.className = isTab ? 'editor-tab' : 'file-item';
      button.dataset[isTab ? 'tab' : 'file'] = name;
      button.setAttribute('aria-label', name);
      button.title = name;
      if (isTab) {
        button.id = tabIds[name];
        button.setAttribute('role', 'tab');
        button.setAttribute('aria-controls', 'code-panel');
      }
      const icon = document.createElement('span');
      icon.className = `file-icon ${kind}`;
      icon.setAttribute('aria-hidden', 'true');
      icon.textContent = symbol;
      const label = document.createElement('span');
      label.className = 'filename-label';
      label.textContent = name;
      const dot = document.createElement('span');
      dot.className = isTab ? 'tab-dot' : 'file-modified';
      dot.dataset[isTab ? 'tabDot' : 'dot'] = name;
      button.append(icon, label, dot);
      (isTab ? tabs : list).append(button);
    }
  });
  tabs.append(toggle);
  $('.file-count').textContent = names.length;
}
function updateStatus() {
  const status = $('#save-status');
  const modified = dirty();
  status.className = `save-status${saveError ? ' error' : modified ? ' dirty' : ''}`;
  status.textContent = loading ? '正在连接项目…' : saving ? '正在写入项目…' : saveError ? '保存未完成' : modified ? '有未保存的更改' : '已保存到项目';
  status.title = saveError || (savedAt ? `最近保存：${new Date(savedAt).toLocaleString('zh-CN')}` : '');
  $('#save').disabled = loading || saving || !revision;
  $('#save-label').textContent = saving ? '保存中…' : '保存到项目';
  $('#run').disabled = loading || !revision;
  $('#refresh-preview').disabled = loading || !revision;
  $('#reload-project').disabled = loading || saving;
  $('#reset-example').disabled = loading || saving || !revision;
  $('#download').disabled = loading || !revision;
  $('#copy-code').disabled = loading || !revision;
  $('#new-file').disabled = loading || saving || !revision || names.length >= MAX_FILES;
  $('#rename-file').disabled = loading || saving || !revision || CORE_FILES.includes(activeFile);
  editor.disabled = loading || !revision;
  names.forEach(name => {
    const changed = files[name] !== savedFiles[name];
    $(`[data-dot="${name}"]`).classList.toggle('visible', changed);
    $(`[data-tab-dot="${name}"]`).classList.toggle('visible', changed);
  });
}
function updateEditorMetadata() {
  const position = editor.selectionStart;
  const lines = editor.value.slice(0, position).split('\n');
  $('#cursor-position').textContent = `行 ${lines.length}, 列 ${lines.at(-1).length + 1}`;
  const size = new TextEncoder().encode(editor.value).length;
  $('#code-size').textContent = size < 1024 ? `${size} B` : `${(size / 1024).toFixed(1)} KB`;
  const lineCount = editor.value.split('\n').length;
  $('#line-numbers').textContent = Array.from({ length: lineCount }, (_, index) => index + 1).join('\n');
  $('#line-numbers').scrollTop = editor.scrollTop;
}
function selectFile(name) {
  if (!names.includes(name)) return;
  if (names.includes(activeFile)) cursors[activeFile] = { start: editor.selectionStart, end: editor.selectionEnd, scroll: editor.scrollTop, left: editor.scrollLeft };
  activeFile = name;
  editor.value = files[name];
  editor.setAttribute('aria-label', `${name} 代码`);
  editor.placeholder = '在此粘贴你自己的内容…';
  $('#breadcrumb-file').textContent = name;
  $('#language-name').textContent = languages[name] || ({ html: 'HTML', htm: 'HTML', css: 'CSS', js: 'JavaScript', json: 'JSON', md: 'Markdown' }[name.split('.').at(-1).toLowerCase()] || '纯文本');
  $('#code-panel').setAttribute('aria-labelledby', tabIds[name]);
  $$('[data-file]').forEach(button => {
    const selected = button.dataset.file === name;
    button.classList.toggle('active', selected);
    if (selected) button.setAttribute('aria-current', 'true');
    else button.removeAttribute('aria-current');
  });
  $$('[data-tab]').forEach(button => {
    const selected = button.dataset.tab === name;
    button.classList.toggle('active', selected);
    button.setAttribute('aria-selected', String(selected));
    button.tabIndex = selected ? 0 : -1;
  });
  const cursor = cursors[name] || { start: 0, end: 0, scroll: 0, left: 0 };
  editor.setSelectionRange(cursor.start, cursor.end);
  editor.scrollTop = cursor.scroll;
  editor.scrollLeft = cursor.left;
  updateEditorMetadata();
  $('#rename-file').disabled = loading || saving || !revision || CORE_FILES.includes(activeFile);
}
async function request(url, options = {}) {
  const response = await fetch(url, { ...options, signal: AbortSignal.timeout(15000) });
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || `请求失败 (${response.status})`);
  return data;
}
async function loadProject(initial = false) {
  if (saving || (dirty() && !initial && !confirm('从磁盘重载会丢弃未保存更改。建议先点击“备份代码”。确定继续？'))) return;
  loading = true;
  const overlay = $('#loading');
  overlay.hidden = false;
  overlay.textContent = '正在读取项目文件…';
  updateStatus();
  try {
    const data = await request('/api/project');
    if (!data.revision || CORE_FILES.some(name => typeof data.files?.[name] !== 'string')) throw new Error('服务端项目数据无效。');
    files = { ...data.files };
    savedFiles = { ...data.files };
    revision = data.revision;
    savedAt = data.savedAt;
    storagePath = data.storagePath;
    saveError = '';
    for (const key of Object.keys(cursors)) delete cursors[key];
    renderFiles();
    selectFile(Object.hasOwn(files, activeFile) ? activeFile : 'index.html');
    overlay.hidden = true;
    $('#connection-status').textContent = '项目已连接';
    $('#disk-path').textContent = 'workspace/';
    $('#disk-path').title = storagePath;
    runPreview();
    if (!initial) toast('已从项目文件重新加载');
  } catch (error) {
    $('#connection-status').textContent = '项目连接失败';
    overlay.textContent = '项目读取失败。';
    const retry = document.createElement('button');
    retry.textContent = '点击重试';
    retry.addEventListener('click', () => loadProject(initial));
    overlay.append(retry);
    saveError = error.message;
    toast(error.message, true);
  } finally { loading = false; updateStatus(); }
}
async function saveProject() {
  if (loading || saving || !revision) return;
  const snapshot = { ...files };
  saving = true;
  saveError = '';
  updateStatus();
  try {
    const result = await request('/api/project', {
      method: 'PUT', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ baseRevision: revision, files: snapshot })
    });
    revision = result.revision;
    savedAt = result.savedAt;
    storagePath = result.storagePath;
    savedFiles = snapshot;
    $('#disk-path').title = storagePath;
    toast(dirty() ? '已保存刚才的版本；新的编辑内容尚未保存。' : `保存成功 · ${Object.keys(snapshot).length} 个文件已写入项目`);
  } catch (error) {
    saveError = error.name === 'TimeoutError' ? '保存请求超时，结果暂不确定。请备份代码并从磁盘重载核对。' : error.message;
    toast(saveError, true);
  } finally { saving = false; updateStatus(); }
}
function previewBridge() {
  let logPort;
  let pending = [];
  const emit = (level, args) => {
    const text = args.map(value => {
      try {
        if (typeof value === 'string') return value;
        if (value instanceof Error) return `${value.name}: ${value.message}`;
        if (typeof value === 'undefined') return 'undefined';
        return JSON.stringify(value) ?? String(value);
      } catch { return '[无法序列化的对象]'; }
    }).join(' ').slice(0, 8000);
    const entry = { level, text };
    if (logPort) logPort.postMessage(entry);
    else { pending.push(entry); if (pending.length > 200) pending.shift(); }
  };
  for (const level of ['log', 'info', 'warn', 'error', 'debug']) {
    const original = console[level].bind(console);
    console[level] = (...args) => { emit(level, args); original(...args); };
  }
  window.addEventListener('error', event => emit('error', [event.message || '资源加载失败']));
  window.addEventListener('unhandledrejection', event => emit('error', ['Unhandled rejection:', event.reason]));
  const receive = event => {
    if (event.source !== parent || event.data !== 'kagglee:connect' || !event.ports[0]) return;
    logPort = event.ports[0];
    pending.forEach(entry => logPort.postMessage(entry));
    pending = [];
    window.removeEventListener('message', receive);
  };
  window.addEventListener('message', receive);
}
const scriptJSON = value => JSON.stringify(value).replace(/</g, '\\u003c').replace(/\u2028/g, '\\u2028').replace(/\u2029/g, '\\u2029');
function runPreview() {
  if (!revision) return;
  const currentRun = ++runNumber;
  port?.close();
  logs = [];
  renderLogs();
  const previousFrame = $('#preview');
  const frame = document.createElement('iframe');
  frame.id = 'preview';
  frame.title = '代码运行结果';
  frame.setAttribute('sandbox', 'allow-scripts');
  frame.referrerPolicy = 'no-referrer';
  frame.style.width = previousFrame.style.width;
  const bootstrap = `(${previewBridge.toString()})();`;
  const previewName = /\.html?$/i.test(activeFile) ? activeFile : 'index.html';
  $('#preview-file').textContent = previewName;
  const doc = new DOMParser().parseFromString(files[previewName], 'text/html');
  let useCSS = previewName === 'index.html';
  let useJS = previewName === 'index.html';
  doc.querySelectorAll('link[rel="stylesheet"][href], script[src]').forEach(node => {
    const target = (node.getAttribute('href') || node.getAttribute('src') || '').split(/[?#]/)[0].replace(/^(?:\.\/|\/)/, '');
    if (node.tagName === 'LINK' && target === 'style.css') { useCSS = true; node.remove(); }
    if (node.tagName === 'SCRIPT' && target === 'script.js') { useJS = true; node.remove(); }
  });
  // Named HTML is self-contained unless it explicitly references the companion files.
  const inject = `const kaggleeStyle=document.createElement('style');kaggleeStyle.textContent=${scriptJSON(useCSS ? files['style.css'] : '')};document.head.append(kaggleeStyle);const kaggleeScript=document.createElement('script');kaggleeScript.textContent=${scriptJSON(useJS ? files['script.js'] : '')};document.body.append(kaggleeScript);`;
  const bridgeScript = doc.createElement('script');
  bridgeScript.textContent = bootstrap;
  doc.head.prepend(bridgeScript);
  const charset = doc.createElement('meta');
  charset.setAttribute('charset', 'utf-8');
  doc.head.prepend(charset);
  if (!doc.querySelector('meta[name="viewport"]')) {
    const viewport = doc.createElement('meta');
    viewport.name = 'viewport';
    viewport.content = 'width=device-width,initial-scale=1';
    doc.head.append(viewport);
  }
  const codeScript = doc.createElement('script');
  codeScript.textContent = inject;
  doc.body.append(codeScript);
  frame.srcdoc = '<!doctype html>' + doc.documentElement.outerHTML;
  frame.addEventListener('load', () => {
    if (currentRun !== runNumber) return;
    const channel = new MessageChannel();
    port = channel.port1;
    port.onmessage = event => {
      const data = event.data;
      if (!data || !['log', 'info', 'debug', 'warn', 'error'].includes(data.level) || typeof data.text !== 'string') return;
      addLog(data.level, data.text.slice(0, 8000));
    };
    frame.contentWindow.postMessage('kagglee:connect', '*', [channel.port2]);
    $('#preview-status').textContent = '预览已更新';
  }, { once: true });
  previousFrame.replaceWith(frame);
  $('#preview-empty').hidden = true;
  $('#preview-status').textContent = '正在运行…';
}
function addLog(level, text) {
  logs.push({ level, text, time: new Date().toLocaleTimeString('zh-CN', { hour12: false }) });
  if (logs.length > 200) logs.shift();
  scheduleLogs();
}
let logFrame = false;
function scheduleLogs() {
  if (logFrame) return;
  logFrame = true;
  requestAnimationFrame(() => { logFrame = false; renderLogs(); });
}
function renderLogs() {
  const output = $('#console-output');
  const filter = $('#log-filter').value;
  $('#console-count').textContent = logs.length;
  const visible = logs.filter(entry => filter === 'all' || (filter === 'log' ? ['log', 'info', 'debug'].includes(entry.level) : entry.level === filter));
  const fragment = document.createDocumentFragment();
  for (const entry of visible) {
    const row = document.createElement('div');
    row.className = `console-row ${entry.level}`;
    for (const [className, text] of [['log-time', entry.time], ['log-symbol', entry.level === 'error' ? '×' : entry.level === 'warn' ? '△' : '›'], ['log-text', entry.text]]) {
      const cell = document.createElement('span');
      cell.className = className;
      cell.textContent = text;
      row.append(cell);
    }
    fragment.append(row);
  }
  if (!visible.length) {
    const placeholder = document.createElement('div');
    placeholder.className = 'console-placeholder';
    placeholder.textContent = logs.length ? '没有符合筛选条件的日志' : '运行输出会显示在这里';
    fragment.append(placeholder);
  }
  output.replaceChildren(fragment);
  output.scrollTop = output.scrollHeight;
}
function showDialog(title, paragraphs, code = '') {
  $('#dialog-title').textContent = title;
  const content = $('#dialog-content');
  content.replaceChildren();
  paragraphs.forEach(text => { const p = document.createElement('p'); p.textContent = text; content.append(p); });
  if (code) { const node = document.createElement('code'); node.textContent = code; content.append(node); }
  $('#info-dialog').showModal();
}
function showStorage() {
  showDialog('代码真正保存在哪里？', [
    '“保存到项目”通过服务端创建一个包含所有编辑文件的完整版本（包括你的自命名文件）。workspace/HEAD.json 指向当前版本；刷新页面和重启服务都会读取这个版本。',
    '当前版本路径如下（包含预设文件及所有已保存的自命名文件）。历史版本保留在 revisions/ 中。未保存的输入只存在本页，离开前请保存或备份。'
  ], storagePath || '尚未连接项目');
}
editor.addEventListener('input', () => { files[activeFile] = editor.value; saveError = ''; updateEditorMetadata(); updateStatus(); });
editor.addEventListener('scroll', () => { $('#line-numbers').scrollTop = editor.scrollTop; });
for (const event of ['click', 'keyup', 'select']) editor.addEventListener(event, updateEditorMetadata);
editor.addEventListener('keydown', event => {
  if (event.key !== 'Tab') return;
  event.preventDefault();
  const start = editor.selectionStart;
  const end = editor.selectionEnd;
  if (event.shiftKey) {
    const lineStart = editor.value.lastIndexOf('\n', start - 1) + 1;
    const remove = editor.value.slice(lineStart).match(/^ {1,2}/)?.[0].length || 0;
    editor.setRangeText('', lineStart, lineStart + remove, 'preserve');
  } else editor.setRangeText('  ', start, end, 'end');
  editor.dispatchEvent(new Event('input'));
});
$('.file-list').addEventListener('click', event => {
  const button = event.target.closest('[data-file]');
  if (button) selectFile(button.dataset.file);
});
$('.editor-tabs').addEventListener('click', event => {
  const button = event.target.closest('[data-tab]');
  if (button) selectFile(button.dataset.tab);
});
$('.editor-tabs').addEventListener('keydown', event => {
  if (!event.target.closest('[data-tab]') || !['ArrowRight', 'ArrowLeft', 'Home', 'End'].includes(event.key)) return;
  event.preventDefault();
  const current = names.indexOf(activeFile);
  const index = event.key === 'Home' ? 0 : event.key === 'End' ? names.length - 1 : (current + (event.key === 'ArrowRight' ? 1 : -1) + names.length) % names.length;
  selectFile(names[index]);
  $(`[data-tab="${names[index]}"]`).focus();
});
let renameTarget = null;
function openFileDialog(rename = false) {
  if (loading || saving || !revision) return;
  renameTarget = rename ? activeFile : null;
  if (renameTarget && CORE_FILES.includes(renameTarget)) return;
  $('#file-dialog-title').textContent = rename ? '重命名文件' : '新建空白文件';
  $('#confirm-file').textContent = rename ? '确认重命名' : '创建空白文件';
  $('#file-name').value = rename ? activeFile : '';
  $('#file-name-error').textContent = '';
  $('#file-name').setAttribute('aria-invalid', 'false');
  $('#file-dialog').showModal();
  $('#file-name').focus();
  $('#file-name').select();
}
$('#new-file').addEventListener('click', () => openFileDialog());
$('#rename-file').addEventListener('click', () => openFileDialog(true));
for (const id of ['cancel-file', 'cancel-file-x']) $(`#${id}`).addEventListener('click', () => $('#file-dialog').close());
$('#file-form').addEventListener('submit', event => {
  event.preventDefault();
  if (loading || saving || !revision) return;
  const name = $('#file-name').value.trim().normalize('NFC');
  const error = fileNameError(name, names, renameTarget) || (!renameTarget && names.length >= MAX_FILES ? `最多创建 ${MAX_FILES} 个文件。` : '');
  $('#file-name-error').textContent = error;
  $('#file-name').setAttribute('aria-invalid', String(Boolean(error)));
  if (error) { $('#file-name').focus(); return; }
  if (renameTarget) {
    files[name] = files[renameTarget];
    if (name !== renameTarget) { delete files[renameTarget]; cursors[name] = cursors[renameTarget]; delete cursors[renameTarget]; }
  } else files[name] = '';
  renderFiles();
  selectFile(name);
  saveError = '';
  updateStatus();
  $('#file-dialog').close();
  editor.focus();
  toast(renameTarget ? '文件已重命名，点击“保存到项目”后生效。' : '空白文件已创建，请粘贴你的内容，再点击“保存到项目”。');
});
$('#copy-code').addEventListener('click', async () => {
  if (loading || !revision) return;
  const name = activeFile;
  const content = files[name];
  if (!content) { toast('当前文件为空，请先粘贴你的代码。', true); return; }
  try {
    if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
    await navigator.clipboard.writeText(content);
    toast(`已复制 ${name} 的当前内容（复制不等于保存或运行验证）`);
  } catch {
    showDialog('手动复制当前文件', [
      `浏览器未允许自动复制。下方是 ${name} 的完整原始内容，已选中；请按 Ctrl / ⌘ + C 复制。不会修改或保存你的文件。`
    ]);
    const fallback = document.createElement('textarea');
    fallback.id = 'copy-fallback';
    fallback.readOnly = true;
    fallback.spellcheck = false;
    fallback.setAttribute('aria-label', '待复制的完整代码');
    fallback.value = content;
    $('#dialog-content').append(fallback);
    fallback.focus();
    fallback.select();
  }
});
$('#save').addEventListener('click', saveProject);
$('#run').addEventListener('click', runPreview);
$('#refresh-preview').addEventListener('click', runPreview);
$('#reload-project').addEventListener('click', () => loadProject());
$('#storage-info').addEventListener('click', showStorage);
$('#disk-path').addEventListener('click', showStorage);
$('#help').addEventListener('click', () => showDialog('欢迎来到 Kagglee Studio', [
  '在左侧选择 HTML、CSS 或 JavaScript 文件，粘贴代码后点击“运行”。Ctrl / ⌘ + Enter 也可运行。运行不会自动保存。',
  '点击“保存到项目”或按 Ctrl / ⌘ + S，把所有文件真正写入项目。保存冲突时先备份，再从磁盘重载。备份会下载当前代码的 JSON 文件。',
  '顶部“复制当前代码”原样复制所选文件（含未保存的编辑），不会修改项目；浏览器禁止剪贴板时会显示选中的原文供手动复制。Python代码需粘贴到Kaggle运行，网页工作台不会在服务器执行它。',
  '点击顶部工具栏的“＋ 新建文件”，自行输入文件名，再粘贴自己的内容。自命名文件可重命名；HTML文件选中后可独立预览，其他文本文件只编辑和保存。三个预设文件为运行基础，不能重命名。',
  '预览在不含同源权限的沙箱中执行，控制台会显示 console 输出、异常与未处理的 Promise。桌面、平板、手机按钮可切换预览宽度。',
  '这是本地开发工作台，不是完整浏览器、后端代码执行器或恶意代码安全平台。不支持 npm 导入、服务端语言或任意网络资源；请勿运行不可信的死循环代码。'
]));
$('#close-dialog').addEventListener('click', () => $('#info-dialog').close());
$('#dialog-done').addEventListener('click', () => $('#info-dialog').close());
$('#toggle-sidebar').addEventListener('click', () => { const hidden = $('.studio').classList.toggle('sidebar-hidden'); $('#toggle-sidebar').setAttribute('aria-expanded', String(!hidden)); });
$('#toggle-console').addEventListener('click', () => { const hidden = $('.console-panel').classList.toggle('collapsed'); $('#toggle-console').setAttribute('aria-expanded', String(!hidden)); });
$('#clear-console').addEventListener('click', () => { logs = []; renderLogs(); });
$('#log-filter').addEventListener('change', renderLogs);
$$('[data-device]').forEach(button => button.addEventListener('click', () => {
  const device = button.dataset.device;
  const width = device === 'mobile' ? '375px' : device === 'tablet' ? '768px' : '100%';
  $('#preview').style.width = width;
  $('#viewport-label').textContent = device === 'desktop' ? '自适应' : width;
  $$('[data-device]').forEach(node => { node.classList.toggle('selected', node === button); node.setAttribute('aria-pressed', String(node === button)); });
}));
$('#download').addEventListener('click', () => {
  const blob = new Blob([JSON.stringify({ files, exportedAt: new Date().toISOString() }, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = 'kagglee-project-backup.json';
  link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
  toast('已导出当前编辑内容（这不会替代项目保存）');
});
$('#reset-example').addEventListener('click', async () => {
  if (!confirm('将三个预设文件替换为初始示例？自命名文件会保留；预设文件的未保存内容会丢失，磁盘文件不会改变，直到你点击保存。')) return;
  try {
    const data = await request('/api/example');
    files = { ...files, ...data.files };
    renderFiles();
    selectFile(activeFile);
    updateStatus();
    runPreview();
    toast('已恢复示例，点击“保存到项目”才会写入磁盘');
  } catch (error) { toast(error.message, true); }
});
document.addEventListener('keydown', event => {
  if (!(event.ctrlKey || event.metaKey)) return;
  if (event.key.toLowerCase() === 's') { event.preventDefault(); saveProject(); }
  if (event.key === 'Enter') { event.preventDefault(); if (!loading) runPreview(); }
});
window.addEventListener('beforeunload', event => { if (dirty() || saving) { event.preventDefault(); event.returnValue = ''; } });
await loadProject(true);
