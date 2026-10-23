import { test, expect } from '@playwright/test';
import { starterFiles } from '../../src/store.js';
import { readFile } from 'node:fs/promises';
import path from 'node:path';

async function edit(page, name, value) {
  await page.getByRole('tab', { name, exact: true }).click();
  await page.getByRole('textbox', { name: `${name} 代码`, exact: true }).fill(value);
}
async function saved(page) { await expect(page.locator('#save-status')).toHaveText('已保存到项目'); }
async function apiProject(request) { return (await request.get('/api/project')).json(); }

test.beforeEach(async ({ page, request }) => {
  const current = await apiProject(request);
  const result = await request.put('/api/project', { data: { files: starterFiles, baseRevision: current.revision } });
  expect(result.status()).toBe(200);
  await page.goto('/');
  await saved(page);
});

test.describe('第一轮：正常编辑、预览与持久化', () => {
  test('loads all files, sandbox preview and initial logs', async ({ page }) => {
    await expect(page.locator('#code')).toHaveValue(starterFiles['index.html']);
    await expect(page.frameLocator('#preview').getByRole('heading')).toHaveText('Hello, possibilities.');
    await expect(page.locator('#console-output')).toContainText('Ready when you are.');
    await expect(page.locator('#preview')).toHaveAttribute('sandbox', 'allow-scripts');
    await page.screenshot({ path: 'test-results/studio-desktop.png', fullPage: true });
  });
  test('switches files without losing unsaved changes', async ({ page }) => {
    await edit(page, 'index.html', '<h1>保留 HTML</h1>');
    await edit(page, 'style.css', 'body { color: red; }');
    await edit(page, 'script.js', 'console.log("保留 JS")');
    await page.getByRole('tab', { name: 'index.html', exact: true }).click();
    await expect(page.locator('#code')).toHaveValue('<h1>保留 HTML</h1>');
    await expect(page.locator('.file-modified.visible')).toHaveCount(3);
    await expect(page.locator('#save-status')).toHaveText('有未保存的更改');
  });
  test('run renders HTML CSS JS without saving', async ({ page, request }) => {
    const original = await apiProject(request);
    await edit(page, 'index.html', '<h1 id="test">运行成功</h1>');
    await edit(page, 'style.css', 'h1 { color: rgb(255, 0, 0); }');
    await edit(page, 'script.js', 'console.log("浏览器执行成功");');
    await page.locator('#run').click();
    await expect(page.frameLocator('#preview').locator('h1')).toHaveCSS('color', 'rgb(255, 0, 0)');
    await expect(page.locator('#console-output')).toContainText('浏览器执行成功');
    expect((await apiProject(request)).revision).toBe(original.revision);
  });
  test('save writes actual project files and survives page reload', async ({ page, request }) => {
    const expected = { 'index.html': '<h1>真正保存 你好 🌍</h1>', 'style.css': 'h1 { color: purple; }', 'script.js': 'console.log("persisted")' };
    for (const [name, value] of Object.entries(expected)) await edit(page, name, value);
    await page.locator('#save').click();
    await saved(page);
    const data = await apiProject(request);
    expect(data.files).toEqual(expected);
    for (const name of Object.keys(expected)) expect(await readFile(path.resolve(data.storagePath, name), 'utf8')).toBe(expected[name]);
    await page.reload();
    await saved(page);
    await expect(page.locator('#code')).toHaveValue(expected['index.html']);
    await expect(page.frameLocator('#preview').locator('h1')).toHaveText('真正保存 你好 🌍');
  });
  test('preview button events run and console clear/filter work', async ({ page }) => {
    await page.frameLocator('#preview').getByRole('button').click();
    await expect(page.frameLocator('#preview').locator('#message')).toContainText('You made it happen.');
    await expect(page.locator('#console-output')).toContainText('A little magic');
    await page.locator('#log-filter').selectOption('error');
    await expect(page.locator('#console-output')).toContainText('没有符合');
    await page.locator('#clear-console').click();
    await expect(page.locator('#console-count')).toHaveText('0');
  });
  test('keyboard save, run and indentation work', async ({ page }) => {
    await edit(page, 'index.html', '<h1>快捷键</h1>');
    await page.locator('#code').press('Control+Home');
    await page.locator('#code').press('Tab');
    await expect(page.locator('#code')).toHaveValue('  <h1>快捷键</h1>');
    await page.locator('#code').press('Shift+Tab');
    await expect(page.locator('#code')).toHaveValue('<h1>快捷键</h1>');
    await page.keyboard.press('Control+s');
    await saved(page);
    await page.keyboard.press('Control+Enter');
    await expect(page.frameLocator('#preview').locator('h1')).toHaveText('快捷键');
  });
  test('backup contains current unsaved code', async ({ page }) => {
    await edit(page, 'index.html', '备份未保存内容');
    const downloadPromise = page.waitForEvent('download');
    await page.locator('#download').click();
    const download = await downloadPromise;
    const backup = JSON.parse(await readFile(await download.path(), 'utf8'));
    expect(backup.files['index.html']).toBe('备份未保存内容');
    await expect(page.locator('#save-status')).toHaveText('有未保存的更改');
  });
  test('storage dialog exposes real directory and help opens', async ({ page, request }) => {
    await page.locator('#disk-path').click();
    await expect(page.getByRole('dialog')).toContainText((await apiProject(request)).storagePath);
    await page.locator('#dialog-done').click();
    await page.locator('#help').click();
    await expect(page.getByRole('dialog')).toContainText('运行不会自动保存');
  });
});

test.describe('第二轮：异常、冲突与编辑安全', () => {
  test('two tabs conflict without losing current code', async ({ page, context }) => {
    const other = await context.newPage();
    await other.goto('/');
    await saved(other);
    await edit(page, 'index.html', '<h1>第一个窗口</h1>');
    await page.locator('#save').click();
    await saved(page);
    await edit(other, 'index.html', '<h1>第二个窗口未保存</h1>');
    await other.locator('#save').click();
    await expect(other.locator('#toast')).toContainText('其他窗口');
    await expect(other.locator('#code')).toHaveValue('<h1>第二个窗口未保存</h1>');
    await expect(other.locator('#save-status')).toHaveText('保存未完成');
  });
  test('edits made while saving remain dirty', async ({ page }) => {
    let release;
    const gate = new Promise(resolve => { release = resolve; });
    await page.route('**/api/project', async route => {
      if (route.request().method() !== 'PUT') return route.continue();
      await gate;
      await route.continue();
    });
    await edit(page, 'index.html', '<h1>保存快照</h1>');
    await page.locator('#save').click();
    await expect(page.locator('#save-status')).toHaveText('正在写入项目…');
    await page.locator('#code').fill('<h1>保存期间继续编辑</h1>');
    release();
    await expect(page.locator('#save-status')).toHaveText('有未保存的更改');
    await expect(page.locator('#code')).toHaveValue('<h1>保存期间继续编辑</h1>');
    await page.locator('#save').click();
    await saved(page);
  });
  test('network failure preserves code and retry succeeds', async ({ page }) => {
    await edit(page, 'index.html', '<h1>不能丢失</h1>');
    await page.route('**/api/project', route => route.request().method() === 'PUT' ? route.abort('failed') : route.continue());
    await page.locator('#save').click();
    await expect(page.locator('#save-status')).toHaveText('保存未完成');
    await expect(page.locator('#code')).toHaveValue('<h1>不能丢失</h1>');
    await page.unroute('**/api/project');
    await page.locator('#save').click();
    await saved(page);
  });
  test('reload cancel retains changes; accept restores disk', async ({ page }) => {
    await edit(page, 'index.html', '临时内容');
    page.once('dialog', dialog => dialog.dismiss());
    await page.locator('#reload-project').click();
    await expect(page.locator('#code')).toHaveValue('临时内容');
    page.once('dialog', dialog => dialog.accept());
    await page.locator('#reload-project').click();
    await saved(page);
    await expect(page.locator('#code')).toHaveValue(starterFiles['index.html']);
  });
  test('synchronous errors and promise rejections reach console', async ({ page }) => {
    await edit(page, 'script.js', 'console.warn("警告测试"); Promise.reject(new Error("Promise 测试")); setTimeout(() => { throw new Error("运行异常测试"); }, 0);');
    await page.locator('#run').click();
    await expect(page.locator('#console-output')).toContainText('Promise 测试');
    await expect(page.locator('#console-output')).toContainText('运行异常测试');
    await page.locator('#log-filter').selectOption('warn');
    await expect(page.locator('#console-output')).toContainText('警告测试');
    await expect(page.locator('#console-output')).not.toContainText('Promise 测试');
  });
  test('closing script and style tags inside source do not break injection', async ({ page }) => {
    await edit(page, 'style.css', '/* </style><div>unsafe</div> */ body { color: rgb(0, 128, 0); }');
    await edit(page, 'script.js', 'console.log("</script><h1>不是HTML</h1>");');
    await page.locator('#run').click();
    await expect(page.locator('#console-output')).toContainText('</script><h1>不是HTML</h1>');
    await expect(page.frameLocator('#preview').locator('h1')).toHaveCount(1);
    await expect(page.locator('#console-output h1')).toHaveCount(0);
  });
  test('reset example modifies editor only until saved', async ({ page, request }) => {
    await edit(page, 'index.html', '<h1>磁盘原版</h1>');
    await page.locator('#save').click();
    await saved(page);
    page.once('dialog', dialog => dialog.accept());
    await page.locator('#reset-example').click();
    await expect(page.locator('#code')).toHaveValue(starterFiles['index.html']);
    await expect(page.locator('#save-status')).toHaveText('有未保存的更改');
    expect((await apiProject(request)).files['index.html']).toBe('<h1>磁盘原版</h1>');
  });
  test('initial load failure presents retry and recovers', async ({ page }) => {
    await page.route('**/api/project', route => route.fulfill({ status: 500, contentType: 'application/json', body: '{"error":"读取失败测试"}' }));
    await page.reload();
    await expect(page.locator('#loading')).toContainText('项目读取失败');
    await expect(page.locator('#save')).toBeDisabled();
    await page.unroute('**/api/project');
    await page.getByRole('button', { name: '点击重试' }).click();
    await saved(page);
    await expect(page.locator('#loading')).toBeHidden();
  });
});

test.describe('第三轮：隔离、边界与设备模拟', () => {
  test('sandbox cannot read parent DOM or silently save to project', async ({ page, request }) => {
    const before = await apiProject(request);
    await edit(page, 'script.js', `try { parent.document.body.innerHTML = 'hacked'; } catch { console.log('父页面隔离成功'); } fetch('/api/project', {method:'PUT', headers:{'Content-Type':'application/json'}, body:'{}'}).then(r=>console.log('写入状态',r.status)).catch(()=>console.log('网络隔离成功'));`);
    await page.locator('#run').click();
    await expect(page.locator('#console-output')).toContainText('父页面隔离成功');
    await expect(page.locator('.brand')).toBeVisible();
    expect((await apiProject(request)).revision).toBe(before.revision);
  });
  test('console handles circular objects and caps message count', async ({ page }) => {
    await edit(page, 'script.js', 'const a={};a.self=a;console.log(a);for(let i=0;i<250;i++) console.log("日志",i);');
    await page.locator('#run').click();
    await expect(page.locator('#console-count')).toHaveText('200');
    await expect(page.locator('#console-output')).toContainText('249');
    await expect(page.locator('.console-row')).toHaveCount(200);
  });
  test('device dimensions persist on rerun', async ({ page }) => {
    await page.getByRole('button', { name: '手机预览', exact: true }).click();
    await expect(page.locator('#preview')).toHaveCSS('width', '375px');
    await page.locator('#run').click();
    await expect(page.locator('#preview')).toHaveCSS('width', '375px');
    await page.getByRole('button', { name: '平板预览', exact: true }).click();
    await expect(page.locator('#preview')).toHaveCSS('width', '768px');
    await page.getByRole('button', { name: '桌面预览', exact: true }).click();
    await expect(page.locator('#preview')).toHaveAttribute('style', /100%/);
  });
  test('mobile layout has no page-level horizontal overflow', async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await expect(page.locator('#save')).toBeVisible();
    await expect(page.locator('#code')).toBeVisible();
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
    await page.screenshot({ path: 'test-results/studio-mobile.png', fullPage: true });
  });
  test('full HTML documents and empty files render', async ({ page }) => {
    await edit(page, 'index.html', '<!doctype html><html><head><title>完整文档</title></head><body><h1>完整页面</h1></body></html>');
    await edit(page, 'style.css', '');
    await edit(page, 'script.js', '');
    await page.locator('#run').click();
    await expect(page.frameLocator('#preview').locator('h1')).toHaveText('完整页面');
    await edit(page, 'index.html', '');
    await page.locator('#run').click();
    await expect(page.frameLocator('#preview').locator('h1')).toHaveCount(0);
    await page.locator('#save').click();
    await saved(page);
  });
  test('tab keyboard navigation and panel toggles work', async ({ page }) => {
    await page.getByRole('tab', { name: 'index.html', exact: true }).focus();
    await page.keyboard.press('ArrowRight');
    await expect(page.getByRole('tab', { name: 'style.css', exact: true })).toHaveAttribute('aria-selected', 'true');
    await expect(page.locator('#code')).toHaveValue(starterFiles['style.css']);
    await page.locator('#toggle-sidebar').click();
    await expect(page.locator('.studio')).toHaveClass(/sidebar-hidden/);
    await page.locator('#toggle-console').click();
    await expect(page.locator('#console-output')).toBeHidden();
    await page.locator('#toggle-console').click();
    await expect(page.locator('#console-output')).toBeVisible();
  });
  test('beforeunload prompts only when changes are unsaved', async ({ page }) => {
    await edit(page, 'index.html', '需要保存');
    const dialogPromise = page.waitForEvent('dialog');
    const navigation = page.reload();
    const dialog = await dialogPromise;
    expect(dialog.type()).toBe('beforeunload');
    await dialog.accept();
    await navigation;
    await saved(page);
    await expect(page.locator('#code')).toHaveValue(starterFiles['index.html']);
  });
  test('oversized save fails visibly without changing disk', async ({ page, request }) => {
    const before = await apiProject(request);
    await edit(page, 'index.html', 'a'.repeat(1024 * 1024 + 1));
    await page.locator('#save').click();
    await expect(page.locator('#toast')).toContainText('1 MiB');
    await expect(page.locator('#save-status')).toHaveText('保存未完成');
    expect((await apiProject(request)).revision).toBe(before.revision);
  });
});

test.describe('最终复核补充', () => {
  test('local companion file links use editor code exactly once', async ({ page }) => {
    await edit(page, 'index.html', '<!doctype html><html lang="zh-CN"><head><link rel="stylesheet" href="./style.css?v=1"></head><body><h1>本地文件引用</h1><script src="script.js"></script></body></html>');
    await edit(page, 'style.css', 'h1 { color: rgb(12, 34, 56); }');
    await edit(page, 'script.js', 'console.log("只执行一次");');
    await page.locator('#run').click();
    await expect(page.frameLocator('#preview').locator('h1')).toHaveCSS('color', 'rgb(12, 34, 56)');
    await expect(page.locator('.console-row .log-text')).toHaveText(['只执行一次']);
    await expect(page.frameLocator('#preview').locator('html')).toHaveAttribute('lang', 'zh-CN');
    await expect(page.frameLocator('#preview').locator('link[href*="style.css"]')).toHaveCount(0);
  });
  test('bundled Chinese font loads and app has no startup script errors', async ({ page }) => {
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.reload();
    await saved(page);
    await page.evaluate(() => document.fonts.ready);
    expect(await page.evaluate(() => document.fonts.check('12px "Noto Sans SC"', '保存项目代码'))).toBe(true);
    expect(errors).toEqual([]);
    await page.screenshot({ path: 'test-results/studio-desktop.png', fullPage: true });
  });
});

async function createFile(page, name) {
  await page.getByRole('button', { name: '＋ 新建文件', exact: true }).click();
  await page.getByRole('textbox', { name: '文件名（可自行命名）', exact: true }).fill(name);
  await page.getByRole('button', { name: '创建空白文件', exact: true }).click();
}
test.describe('自命名空白文件', () => {
  test('create blank, paste own content, save real file and restore', async ({ page, request }) => {
    await createFile(page, '我的内容.txt');
    await expect(page.locator('#code')).toHaveValue('');
    await expect(page.locator('#code')).toHaveAttribute('aria-label', '我的内容.txt 代码');
    await expect(page.locator('#save-status')).toHaveText('有未保存的更改');
    const text = '这是我自己粘贴的内容\n<script>只保存，不在服务端执行</script>\n你好 🌍';
    await page.locator('#code').fill(text);
    await page.locator('#save').click();
    await saved(page);
    const project = await apiProject(request);
    expect(await readFile(path.resolve(project.storagePath, '我的内容.txt'), 'utf8')).toBe(text);
    await page.reload();
    await saved(page);
    await page.getByRole('tab', { name: '我的内容.txt', exact: true }).click();
    await expect(page.locator('#code')).toHaveValue(text);
  });
  test('duplicate, case duplicate and traversal are visibly rejected', async ({ page }) => {
    await page.locator('#new-file').click();
    for (const [name, message] of [['index.html', '同名'], ['INDEX.HTML', '同名'], ['../outside.txt', '路径']]) {
      await page.locator('#file-name').fill(name);
      await page.locator('#confirm-file').click();
      await expect(page.locator('#file-name-error')).toContainText(message);
      await expect(page.locator('#file-dialog')).toBeVisible();
    }
    await page.locator('#cancel-file').click();
    await expect(page.getByRole('tab')).toHaveCount(3);
  });
  test('rename keeps content, save removes previous current name', async ({ page, request }) => {
    await createFile(page, '原名称.txt');
    await page.locator('#code').fill('重命名后也不能丢失');
    await page.locator('#save').click();
    await saved(page);
    await page.locator('#rename-file').click();
    await page.locator('#file-name').fill('新的名称.txt');
    await page.locator('#confirm-file').click();
    await expect(page.locator('#code')).toHaveValue('重命名后也不能丢失');
    await expect(page.getByRole('tab', { name: '原名称.txt', exact: true })).toHaveCount(0);
    await page.locator('#save').click();
    await saved(page);
    const project = await apiProject(request);
    expect(project.files['新的名称.txt']).toBe('重命名后也不能丢失');
    expect(Object.hasOwn(project.files, '原名称.txt')).toBe(false);
  });
  test('empty file itself can be saved and survives reload', async ({ page, request }) => {
    await createFile(page, '空白文档.md');
    await page.locator('#save').click();
    await saved(page);
    expect((await apiProject(request)).files['空白文档.md']).toBe('');
    await page.reload();
    await saved(page);
    await page.getByRole('tab', { name: '空白文档.md', exact: true }).click();
    await expect(page.locator('#code')).toHaveValue('');
  });
  test('named HTML previews own content without starter CSS or JS', async ({ page }) => {
    await createFile(page, '我的页面.html');
    await page.locator('#code').fill('<style>body{background:rgb(1, 2, 3)}</style><h1>我自己的页面</h1><script>console.log("我自己的代码")</script>');
    await page.locator('#run').click();
    await expect(page.frameLocator('#preview').locator('h1')).toHaveText('我自己的页面');
    await expect(page.frameLocator('#preview').locator('body')).toHaveCSS('background-color', 'rgb(1, 2, 3)');
    await expect(page.locator('#console-output')).toContainText('我自己的代码');
    await expect(page.locator('#console-output')).not.toContainText('Ready when you are.');
    await expect(page.locator('#preview-file')).toHaveText('我的页面.html');
  });
  test('example reset retains custom file and original preview still works', async ({ page }) => {
    await createFile(page, '保留我.txt');
    await page.locator('#code').fill('不要删除我的内容');
    page.once('dialog', dialog => dialog.accept());
    await page.locator('#reset-example').click();
    await expect(page.locator('#code')).toHaveValue('不要删除我的内容');
    await page.getByRole('tab', { name: 'index.html', exact: true }).click();
    await page.locator('#run').click();
    await expect(page.frameLocator('#preview').locator('h1')).toHaveText('Hello, possibilities.');
    await expect(page.locator('#rename-file')).toBeDisabled();
  });
  test('mobile can name and paste without page horizontal overflow', async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    await createFile(page, '手机上命名的文件.txt');
    await page.locator('#code').fill('手机上粘贴的内容');
    await page.locator('#save').click();
    await saved(page);
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
  });
});

test.describe('新建入口可发现性', () => {
  test('full-sized new-file button is in the top toolbar and opens the name dialog', async ({ page }) => {
    const button = page.locator('.topbar').getByRole('button', { name: '＋ 新建文件', exact: true });
    await expect(button).toBeVisible();
    await expect(button).toBeEnabled();
    const box = await button.boundingBox();
    expect(box.width).toBeGreaterThanOrEqual(100);
    expect(box.height).toBeGreaterThanOrEqual(32);
    await button.click();
    await expect(page.getByRole('dialog', { name: '新建空白文件' })).toBeVisible();
    await expect(page.locator('#file-name')).toBeFocused();
    await page.screenshot({ path: 'test-results/new-file-dialog.png', fullPage: true });
  });
  test('mobile keeps new, run, save buttons visible without horizontal overflow', async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    for (const id of ['new-file', 'run', 'save']) await expect(page.locator(`.topbar #${id}`)).toBeVisible();
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
    await page.locator('#new-file').click();
    await expect(page.getByRole('dialog', { name: '新建空白文件' })).toBeVisible();
  });
});

test.describe('复制当前代码', () => {
  test('native clipboard copies exact current content without saving or modifying it', async ({ page, context, request }) => {
    await context.grantPermissions(['clipboard-read', 'clipboard-write']);
    const previous = await apiProject(request);
    await createFile(page, 'kaggle.py');
    const code = '# 用户提供的代码\nprint("你好 </script> 🌍")\n';
    await page.locator('#code').fill(code);
    await page.locator('#copy-code').click();
    await expect(page.locator('#toast')).toContainText('已复制 kaggle.py');
    expect(await page.evaluate(() => navigator.clipboard.readText())).toBe(code);
    await expect(page.locator('#code')).toHaveValue(code);
    await expect(page.locator('#save-status')).toHaveText('有未保存的更改');
    expect((await apiProject(request)).revision).toBe(previous.revision);
  });
  test('switching files copies the selected file, not a stale buffer', async ({ page, context }) => {
    await context.grantPermissions(['clipboard-read', 'clipboard-write']);
    await edit(page, 'script.js', 'console.log("selected script");');
    await page.locator('#copy-code').click();
    await expect(page.locator('#toast')).toContainText('已复制 script.js');
    expect(await page.evaluate(() => navigator.clipboard.readText())).toBe('console.log("selected script");');
    await page.getByRole('tab', { name: 'index.html', exact: true }).click();
    await page.locator('#copy-code').click();
    await expect(page.locator('#toast')).toContainText('已复制 index.html');
    expect(await page.evaluate(() => navigator.clipboard.readText())).toBe(starterFiles['index.html']);
  });
  test('permission denial offers selected read-only original text, not a false success', async ({ page }) => {
    await page.evaluate(() => Object.defineProperty(navigator, 'clipboard', { configurable: true, value: { writeText: async () => { throw new Error('denied'); } } }));
    await createFile(page, 'kaggle.py');
    const code = '# 粘贴代码\nprint("<img src=x onerror=alert(1)>")\n';
    await page.locator('#code').fill(code);
    await page.locator('#copy-code').click();
    await expect(page.getByRole('dialog')).toContainText('浏览器未允许自动复制');
    await expect(page.locator('#copy-fallback')).toHaveValue(code);
    expect(await page.locator('#copy-fallback').evaluate(node => node.readOnly && node.selectionStart === 0 && node.selectionEnd === node.value.length)).toBe(true);
    await expect(page.locator('#dialog-content img')).toHaveCount(0);
    await page.locator('#dialog-done').click();
    await expect(page.locator('#code')).toHaveValue(code);
  });
  test('empty custom file explains that code must be pasted first', async ({ page }) => {
    await createFile(page, 'kaggle.py');
    await page.locator('#copy-code').click();
    await expect(page.locator('#toast')).toContainText('当前文件为空');
    await expect(page.locator('#code')).toHaveValue('');
  });
  test('mobile exposes four toolbar buttons without horizontal overflow', async ({ page }) => {
    await page.setViewportSize({ width: 390, height: 844 });
    for (const id of ['new-file', 'copy-code', 'run', 'save']) await expect(page.locator(`.topbar #${id}`)).toBeVisible();
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth)).toBe(true);
  });
});


test('首轮修复包可从工作台复制完整启动源码，原始 kaggle 保留', async ({ page, request }) => {
  const source = await readFile('kaggle/kaggle-fixed-step1.py', 'utf8');
  const current = await apiProject(request);
  const response = await request.put('/api/project', { data: { files: { ...current.files, 'kaggle': 'original sentinel', 'kaggle-fixed-step1.py': source }, baseRevision: current.revision } });
  expect(response.status()).toBe(200);
  await page.reload(); await saved(page);
  await page.getByRole('tab', { name: 'kaggle-fixed-step1.py', exact: true }).click();
  await expect(page.locator('#code')).toHaveValue(source);
  await page.context().grantPermissions(['clipboard-read', 'clipboard-write']);
  await page.locator('#copy-code').click();
  expect(await page.evaluate(() => navigator.clipboard.readText())).toBe(source);
  expect((await apiProject(request)).files.kaggle).toBe('original sentinel');
});


test('第二阶段修复包可完整复制且保留首轮与原始文件', async ({ page, request }) => {
  const source = await readFile('kaggle/kaggle-fixed-step2.py', 'utf8');
  const first = await readFile('kaggle/kaggle-fixed-step1.py', 'utf8');
  const current = await apiProject(request);
  const response = await request.put('/api/project', { data: { files: { ...current.files, 'kaggle': 'original sentinel', 'kaggle-fixed-step1.py': first, 'kaggle-fixed-step2.py': source }, baseRevision: current.revision } });
  expect(response.status()).toBe(200);
  await page.reload(); await saved(page);
  await page.getByRole('tab', { name: 'kaggle-fixed-step2.py', exact: true }).click();
  await expect(page.locator('#code')).toHaveValue(source);
  await page.context().grantPermissions(['clipboard-read', 'clipboard-write']);
  await page.locator('#copy-code').click();
  expect(await page.evaluate(() => navigator.clipboard.readText())).toBe(source);
  const data=await apiProject(request);
  expect(data.files.kaggle).toBe('original sentinel');
  expect(data.files['kaggle-fixed-step1.py']).toBe(first);
});

test('第三阶段完整源码可原样复制且保留第二阶段包', async ({ page, request }) => {
  const source = await readFile('kaggle/kaggle-fixed-step3.py', 'utf8');
  const second = await readFile('kaggle/kaggle-fixed-step2.py', 'utf8');
  const current = await apiProject(request);
  const response=await request.put('/api/project',{data:{files:{...current.files,'kaggle-fixed-step2.py':second,'kaggle-fixed-step3.py':source},baseRevision:current.revision}});
  expect(response.status()).toBe(200);await page.reload();await saved(page);
  await page.getByRole('tab',{name:'kaggle-fixed-step3.py',exact:true}).click();await expect(page.locator('#code')).toHaveValue(source);
  await page.context().grantPermissions(['clipboard-read','clipboard-write']);await page.locator('#copy-code').click();
  expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(source);
  expect((await apiProject(request)).files['kaggle-fixed-step2.py']).toBe(second);
});

test('第四阶段完整源码可原样复制且保留历史包', async ({ page, request }) => {
  const source=await readFile('kaggle/kaggle-fixed-step4.py','utf8');
  const history=await readFile('kaggle/kaggle-fixed-step3.py','utf8');
  const current=await apiProject(request);
  const response=await request.put('/api/project',{data:{files:{...current.files,'kaggle-fixed-step3.py':history,'kaggle-fixed-step4.py':source},baseRevision:current.revision}});
  expect(response.status()).toBe(200);await page.reload();await saved(page);
  await page.getByRole('tab',{name:'kaggle-fixed-step4.py',exact:true}).click();await expect(page.locator('#code')).toHaveValue(source);
  await page.context().grantPermissions(['clipboard-read','clipboard-write']);await page.locator('#copy-code').click();
  expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(source);
  expect((await apiProject(request)).files['kaggle-fixed-step3.py']).toBe(history);
});

test('第五阶段完整源码可原样复制且保留第四阶段包（隔离工作区）', async ({ page, request }) => {
  const source=await readFile('kaggle/kaggle-fixed-step5.py','utf8');
  const frozen=await readFile('kaggle/kaggle-fixed-step4.py','utf8');
  const current=await apiProject(request);
  const response=await request.put('/api/project',{data:{files:{...current.files,'kaggle-fixed-step4.py':frozen,'kaggle-fixed-step5.py':source},baseRevision:current.revision}});
  expect(response.status()).toBe(200);await page.reload();await saved(page);
  await page.getByRole('tab',{name:'kaggle-fixed-step5.py',exact:true}).click();await expect(page.locator('#code')).toHaveValue(source);
  await page.context().grantPermissions(['clipboard-read','clipboard-write']);await page.locator('#copy-code').click();
  expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(source);
  expect((await apiProject(request)).files['kaggle-fixed-step4.py']).toBe(frozen);
});

test('第六阶段完整Python包可逐字节复制并保留第五阶段包',async({page,request})=>{
  const source=await readFile('kaggle/kaggle-fixed-step6.py','utf8'),frozen=await readFile('kaggle/kaggle-fixed-step5.py','utf8');
  const current=await apiProject(request);const response=await request.put('/api/project',{data:{files:{...current.files,'kaggle-fixed-step5.py':frozen,'kaggle-fixed-step6.py':source},baseRevision:current.revision}});
  expect(response.status()).toBe(200);await page.reload();await saved(page);await page.getByRole('tab',{name:'kaggle-fixed-step6.py',exact:true}).click();await expect(page.locator('#code')).toHaveValue(source);
  await page.context().grantPermissions(['clipboard-read','clipboard-write']);await page.locator('#copy-code').click();expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(source);expect((await apiProject(request)).files['kaggle-fixed-step5.py']).toBe(frozen);
});


test('第七阶段完整Python包可逐字节复制并保留第六阶段包',async({page,request})=>{
  const source=await readFile('kaggle/kaggle-fixed-step7.py','utf8'),frozen=await readFile('kaggle/kaggle-fixed-step6.py','utf8');
  const current=await apiProject(request);const response=await request.put('/api/project',{data:{files:{...current.files,'kaggle-fixed-step6.py':frozen,'kaggle-fixed-step7.py':source},baseRevision:current.revision}});
  expect(response.status()).toBe(200);await page.reload();await saved(page);await page.getByRole('tab',{name:'kaggle-fixed-step7.py',exact:true}).click();await expect(page.locator('#code')).toHaveValue(source);
  await page.context().grantPermissions(['clipboard-read','clipboard-write']);await page.locator('#copy-code').click();expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(source);expect((await apiProject(request)).files['kaggle-fixed-step6.py']).toBe(frozen);
});


test('第八阶段完整Python包可逐字节复制并保留第七阶段包',async({page,request})=>{
  const source=await readFile('kaggle/kaggle-fixed-step8.py','utf8'),frozen=await readFile('kaggle/kaggle-fixed-step7.py','utf8');
  const current=await apiProject(request);const response=await request.put('/api/project',{data:{files:{...current.files,'kaggle-fixed-step7.py':frozen,'kaggle-fixed-step8.py':source},baseRevision:current.revision}});
  expect(response.status()).toBe(200);await page.reload();await saved(page);await page.getByRole('tab',{name:'kaggle-fixed-step8.py',exact:true}).click();await expect(page.locator('#code')).toHaveValue(source);
  await page.context().grantPermissions(['clipboard-read','clipboard-write']);await page.locator('#copy-code').click();expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(source);expect((await apiProject(request)).files['kaggle-fixed-step7.py']).toBe(frozen);
});


test('第九阶段完整Python包可逐字节复制并保留第八阶段包',async({page,request})=>{
  const source=await readFile('kaggle/kaggle-fixed-step9.py','utf8'),frozen=await readFile('kaggle/kaggle-fixed-step8.py','utf8');
  const current=await apiProject(request);const response=await request.put('/api/project',{data:{files:{...current.files,'kaggle-fixed-step8.py':frozen,'kaggle-fixed-step9.py':source},baseRevision:current.revision}});
  expect(response.status()).toBe(200);await page.reload();await saved(page);await page.getByRole('tab',{name:'kaggle-fixed-step9.py',exact:true}).click();await expect(page.locator('#code')).toHaveValue(source);
  await page.context().grantPermissions(['clipboard-read','clipboard-write']);await page.locator('#copy-code').click();expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(source);expect((await apiProject(request)).files['kaggle-fixed-step8.py']).toBe(frozen);
});


test('第十阶段训练器完整Python包可逐字节复制并保留第九阶段包',async({page,request})=>{
  const source=await readFile('kaggle/kaggle-fixed-step10.py','utf8'),frozen=await readFile('kaggle/kaggle-fixed-step9.py','utf8');
  const current=await apiProject(request);const response=await request.put('/api/project',{data:{files:{...current.files,'kaggle-fixed-step9.py':frozen,'kaggle-fixed-step10.py':source},baseRevision:current.revision}});
  expect(response.status()).toBe(200);await page.reload();await saved(page);await page.getByRole('tab',{name:'kaggle-fixed-step10.py',exact:true}).click();await expect(page.locator('#code')).toHaveValue(source);
  await page.context().grantPermissions(['clipboard-read','clipboard-write']);await page.locator('#copy-code').click();expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(source);expect((await apiProject(request)).files['kaggle-fixed-step9.py']).toBe(frozen);
});

test('第十一阶段adapter聊天完整Python包可逐字节复制并保留第十阶段包',async({page,request})=>{
  const source=await readFile('kaggle/kaggle-fixed-step11.py','utf8'),frozen=await readFile('kaggle/kaggle-fixed-step10.py','utf8');
  const current=await apiProject(request);const response=await request.put('/api/project',{data:{files:{...current.files,'kaggle-fixed-step10.py':frozen,'kaggle-fixed-step11.py':source},baseRevision:current.revision}});
  expect(response.status()).toBe(200);await page.reload();await saved(page);await page.getByRole('tab',{name:'kaggle-fixed-step11.py',exact:true}).click();await expect(page.locator('#code')).toHaveValue(source);
  await page.context().grantPermissions(['clipboard-read','clipboard-write']);await page.locator('#copy-code').click();expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(source);expect((await apiProject(request)).files['kaggle-fixed-step10.py']).toBe(frozen);
});

test('第十二阶段Mimi修复完整Python包可逐字节复制并保留第十一阶段包',async({page,request})=>{
  const source=await readFile('kaggle/kaggle-fixed-step12.py','utf8'),frozen=await readFile('kaggle/kaggle-fixed-step11.py','utf8');
  const current=await apiProject(request);const response=await request.put('/api/project',{data:{files:{...current.files,'kaggle-fixed-step11.py':frozen,'kaggle-fixed-step12.py':source},baseRevision:current.revision}});
  expect(response.status()).toBe(200);await page.reload();await saved(page);await page.getByRole('tab',{name:'kaggle-fixed-step12.py',exact:true}).click();await expect(page.locator('#code')).toHaveValue(source);
  await page.context().grantPermissions(['clipboard-read','clipboard-write']);await page.locator('#copy-code').click();expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(source);expect((await apiProject(request)).files['kaggle-fixed-step11.py']).toBe(frozen);
});

test('第十三阶段延迟导入修复完整Python包可逐字节复制并保留第十二阶段包',async({page,request})=>{
  const source=await readFile('kaggle/kaggle-fixed-step13.py','utf8'),frozen=await readFile('kaggle/kaggle-fixed-step12.py','utf8');
  const current=await apiProject(request);const response=await request.put('/api/project',{data:{files:{...current.files,'kaggle-fixed-step12.py':frozen,'kaggle-fixed-step13.py':source},baseRevision:current.revision}});
  expect(response.status()).toBe(200);await page.reload();await saved(page);await page.getByRole('tab',{name:'kaggle-fixed-step13.py',exact:true}).click();await expect(page.locator('#code')).toHaveValue(source);
  await page.context().grantPermissions(['clipboard-read','clipboard-write']);await page.locator('#copy-code').click();expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(source);expect((await apiProject(request)).files['kaggle-fixed-step12.py']).toBe(frozen);
});

test('第十四阶段长录音原文修复完整Python包可逐字节复制并保留第十三阶段包',async({page,request})=>{
  const source=await readFile('kaggle/kaggle-fixed-step14.py','utf8'),frozen=await readFile('kaggle/kaggle-fixed-step13.py','utf8');
  const current=await apiProject(request);const response=await request.put('/api/project',{data:{files:{...current.files,'kaggle-fixed-step13.py':frozen,'kaggle-fixed-step14.py':source},baseRevision:current.revision}});
  expect(response.status()).toBe(200);await page.reload();await saved(page);await page.getByRole('tab',{name:'kaggle-fixed-step14.py',exact:true}).click();await expect(page.locator('#code')).toHaveValue(source);
  await page.context().grantPermissions(['clipboard-read','clipboard-write']);await page.locator('#copy-code').click();expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(source);expect((await apiProject(request)).files['kaggle-fixed-step13.py']).toBe(frozen);
});

test('第十五阶段参考隔离首句优化完整Python包可逐字节复制并保留第十四阶段包',async({page,request})=>{
  const source=await readFile('kaggle/kaggle-fixed-step15.py','utf8'),frozen=await readFile('kaggle/kaggle-fixed-step14.py','utf8');
  const current=await apiProject(request);const response=await request.put('/api/project',{data:{files:{...current.files,'kaggle-fixed-step14.py':frozen,'kaggle-fixed-step15.py':source},baseRevision:current.revision}});
  expect(response.status()).toBe(200);await page.reload();await saved(page);await page.getByRole('tab',{name:'kaggle-fixed-step15.py',exact:true}).click();await expect(page.locator('#code')).toHaveValue(source);
  await page.context().grantPermissions(['clipboard-read','clipboard-write']);await page.locator('#copy-code').click();expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(source);expect((await apiProject(request)).files['kaggle-fixed-step14.py']).toBe(frozen);
});

test('第十六阶段ICL绑定有界解码完整Python包可逐字节复制并保留第十五阶段包',async({page,request})=>{
  const source=await readFile('kaggle/kaggle-fixed-step16.py','utf8'),frozen=await readFile('kaggle/kaggle-fixed-step15.py','utf8');
  const current=await apiProject(request);const response=await request.put('/api/project',{data:{files:{...current.files,'kaggle-fixed-step15.py':frozen,'kaggle-fixed-step16.py':source},baseRevision:current.revision}});
  expect(response.status()).toBe(200);await page.reload();await saved(page);await page.getByRole('tab',{name:'kaggle-fixed-step16.py',exact:true}).click();await expect(page.locator('#code')).toHaveValue(source);
  await page.context().grantPermissions(['clipboard-read','clipboard-write']);await page.locator('#copy-code').click();expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(source);expect((await apiProject(request)).files['kaggle-fixed-step15.py']).toBe(frozen);
});

test('第十七阶段长参考对齐参数绑定完整Python包可逐字节复制并保留第十六阶段包',async({page,request})=>{
  const source=await readFile('kaggle/kaggle-fixed-step17.py','utf8'),frozen=await readFile('kaggle/kaggle-fixed-step16.py','utf8');
  const current=await apiProject(request);const response=await request.put('/api/project',{data:{files:{...current.files,'kaggle-fixed-step16.py':frozen,'kaggle-fixed-step17.py':source},baseRevision:current.revision}});
  expect(response.status()).toBe(200);await page.reload();await saved(page);await page.getByRole('tab',{name:'kaggle-fixed-step17.py',exact:true}).click();await expect(page.locator('#code')).toHaveValue(source);
  await page.context().grantPermissions(['clipboard-read','clipboard-write']);await page.locator('#copy-code').click();expect(await page.evaluate(()=>navigator.clipboard.readText())).toBe(source);expect((await apiProject(request)).files['kaggle-fixed-step16.py']).toBe(frozen);
});
