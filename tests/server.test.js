import { test, before, after } from 'node:test';
import assert from 'node:assert/strict';
import { mkdtemp, readFile, rm, writeFile, mkdir, readdir } from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import { once } from 'node:events';
import { createApp } from '../src/server.js';
import { ProjectStore, starterFiles, MAX_BYTES } from '../src/store.js';

let server, store, root, base;
before(async () => {
  root = await mkdtemp(path.join(os.tmpdir(), 'kagglee-api-'));
  ({ server, store } = await createApp({ workspace: root }));
  server.listen(0, '127.0.0.1');
  await once(server, 'listening');
  base = `http://127.0.0.1:${server.address().port}`;
});
after(async () => {
  await new Promise(resolve => server.close(resolve));
  await rm(root, { recursive: true, force: true });
});
const get = async () => (await fetch(`${base}/api/project`)).json();
const put = async (files, baseRevision, headers = {}) => fetch(`${base}/api/project`, {
  method: 'PUT', headers: { 'Content-Type': 'application/json', ...headers }, body: JSON.stringify({ files, baseRevision })
});

test('initial project contains all three real files', async () => {
  const data = await get();
  assert.deepEqual(data.files, starterFiles);
  for (const name of Object.keys(starterFiles)) assert.equal(await readFile(path.join(root, 'revisions', data.revision, name), 'utf8'), data.files[name]);
});
test('save persists exact unicode and closing-tag contents', async () => {
  const old = await get();
  const files = { 'index.html': '<h1>你好 🌍</h1>', 'style.css': '/* </style> */', 'script.js': 'console.log("</script>");' };
  const response = await put(files, old.revision);
  assert.equal(response.status, 200);
  const saved = await response.json();
  assert.notEqual(saved.revision, old.revision);
  assert.deepEqual((await get()).files, files);
  assert.equal((JSON.parse(await readFile(path.join(root, 'HEAD.json')))).revision, saved.revision);
  for (const name of Object.keys(files)) assert.equal(await readFile(path.join(root, 'revisions', saved.revision, name), 'utf8'), files[name]);
});
test('new store instance restores persisted version', async () => {
  const next = new ProjectStore(root);
  await next.init();
  assert.deepEqual(await next.load(), await store.load());
});
test('historical revision is not overwritten', async () => {
  const current = await get();
  await put(starterFiles, current.revision);
  assert.equal(await readFile(path.join(root, 'revisions', current.revision, 'index.html'), 'utf8'), current.files['index.html']);
});
test('stale revisions return 409 and preserve disk', async () => {
  const current = await get();
  assert.equal((await put(starterFiles, 'stale')).status, 409);
  assert.equal((await get()).revision, current.revision);
});
test('concurrent saves admit exactly one winner', async () => {
  const current = await get();
  const results = await Promise.all([put(starterFiles, current.revision), put(starterFiles, current.revision)]);
  assert.deepEqual(results.map(r => r.status).sort(), [200, 409]);
});
test('empty source files are valid', async () => {
  const current = await get();
  const files = { 'index.html': '', 'style.css': '', 'script.js': '' };
  assert.equal((await put(files, current.revision)).status, 200);
  assert.deepEqual((await get()).files, files);
});
test('rejects missing, extra, traversal and non-string files', async () => {
  const current = await get();
  for (const files of [null, [], {}, { ...starterFiles, '../escape': 'bad' }, { ...starterFiles, 'script.js': 42 }, { ...starterFiles, 'script.js': null }]) {
    assert.equal((await put(files, current.revision)).status, 400);
  }
  assert.equal((await get()).revision, current.revision);
});
test('requires baseRevision string', async () => {
  assert.equal((await put(starterFiles, undefined)).status, 400);
  assert.equal((await put(starterFiles, null)).status, 400);
});
test('rejects malformed JSON and unsupported content type', async () => {
  assert.equal((await fetch(`${base}/api/project`, { method: 'PUT', headers: { 'Content-Type': 'application/json' }, body: '{' })).status, 400);
  assert.equal((await fetch(`${base}/api/project`, { method: 'PUT', body: '{}' })).status, 415);
});
test('rejects extra request fields and array bodies', async () => {
  for (const body of ['[]', '{"files":{},"baseRevision":"x","extra":true}', 'null']) {
    assert.equal((await fetch(`${base}/api/project`, { method: 'PUT', headers: { 'Content-Type': 'application/json' }, body })).status, 400);
  }
});
test('1 MiB limit counts UTF-8 bytes, not characters', async () => {
  const current = await get();
  assert.equal((await put({ 'index.html': '界'.repeat(Math.ceil(MAX_BYTES / 3)), 'style.css': '', 'script.js': '' }, current.revision)).status, 413);
  assert.equal((await get()).revision, current.revision);
});
test('accepts exactly 1 MiB and JSON-escaped control characters', async () => {
  const current = await get();
  const files = { 'index.html': '\u0000'.repeat(MAX_BYTES), 'style.css': '', 'script.js': '' };
  assert.equal((await put(files, current.revision)).status, 200);
  assert.equal((await get()).files['index.html'].length, MAX_BYTES);
});
test('rejects oversized raw request', async () => {
  const result = await fetch(`${base}/api/project`, { method: 'PUT', headers: { 'Content-Type': 'application/json' }, body: 'x'.repeat(MAX_BYTES * 6 + 4097) });
  assert.equal(result.status, 413);
});
test('rejects cross-origin, opaque-origin and cross-site writes', async () => {
  const current = await get();
  for (const headers of [{ Origin: 'https://evil.example' }, { Origin: 'null' }, { 'Sec-Fetch-Site': 'cross-site' }]) {
    assert.equal((await put(starterFiles, current.revision, headers)).status, 403);
  }
});
test('allows same-origin write and does not enable CORS', async () => {
  const current = await get();
  const response = await put(starterFiles, current.revision, { Origin: base });
  assert.equal(response.status, 200);
  assert.equal(response.headers.get('access-control-allow-origin'), null);
});
test('static asset whitelist does not expose storage or source', async () => {
  for (const url of ['/workspace/HEAD.json', '/src/server.js', '/.git/config', '/%2e%2e/README.md']) {
    assert.equal((await fetch(`${base}${url}`)).status, 404);
  }
});
test('assets support HEAD and security headers', async () => {
  const result = await fetch(base, { method: 'HEAD' });
  assert.equal(result.status, 200);
  assert.equal(await result.text(), '');
  assert.equal(result.headers.get('x-content-type-options'), 'nosniff');
  assert.match(result.headers.get('content-security-policy'), /connect-src 'self'/);
  assert.equal((await fetch(`${base}/app.js`)).status, 200);
  assert.equal((await fetch(`${base}/styles.css`)).status, 200);
});
test('API is uncached and methods are restricted', async () => {
  assert.equal((await fetch(`${base}/api/project`)).headers.get('cache-control'), 'no-store');
  const result = await fetch(`${base}/api/project`, { method: 'POST' });
  assert.equal(result.status, 405);
  assert.equal(result.headers.get('allow'), 'GET, PUT');
});
test('example endpoint does not mutate saved project', async () => {
  const current = await get();
  assert.deepEqual((await (await fetch(`${base}/api/example`)).json()).files, starterFiles);
  assert.equal((await get()).revision, current.revision);
});
test('write failure does not change HEAD; subsequent saves recover', async () => {
  const current = await get();
  const original = store.write;
  store.write = async () => { throw new Error('simulated disk failure'); };
  try { assert.equal((await put(starterFiles, current.revision)).status, 500); }
  finally { store.write = original; }
  assert.equal((await get()).revision, current.revision);
  assert.equal((await put(starterFiles, current.revision)).status, 200);
});
test('failed real atomic rename cleans up incomplete revision', async () => {
  const dir = await mkdtemp(path.join(os.tmpdir(), 'kagglee-failure-'));
  try {
    const isolated = new ProjectStore(dir);
    await mkdir(path.join(dir, 'revisions'));
    await mkdir(path.join(dir, 'HEAD.json'));
    await assert.rejects(isolated.write(starterFiles));
    assert.deepEqual(await readdir(path.join(dir, 'revisions')), []);
    assert.deepEqual((await readdir(dir)).sort(), ['HEAD.json', 'revisions']);
  } finally { await rm(dir, { recursive: true, force: true }); }
});
test('corrupt HEAD is not silently replaced', async () => {
  const dir = await mkdtemp(path.join(os.tmpdir(), 'kagglee-corrupt-'));
  try {
    await writeFile(path.join(dir, 'HEAD.json'), 'broken');
    await assert.rejects(new ProjectStore(dir).init());
    assert.equal(await readFile(path.join(dir, 'HEAD.json'), 'utf8'), 'broken');
  } finally { await rm(dir, { recursive: true, force: true }); }
});
test('missing revision file and invalid HEAD path do not reset project', async () => {
  const dir = await mkdtemp(path.join(os.tmpdir(), 'kagglee-missing-'));
  try {
    const isolated = new ProjectStore(dir);
    await isolated.init();
    const current = await isolated.load();
    await rm(path.join(dir, 'revisions', current.revision, 'style.css'));
    await assert.rejects(new ProjectStore(dir).init());
    assert.equal(JSON.parse(await readFile(path.join(dir, 'HEAD.json'))).revision, current.revision);
    await writeFile(path.join(dir, 'HEAD.json'), JSON.stringify({ revision: '../../secret', savedAt: new Date().toISOString() }));
    await assert.rejects(new ProjectStore(dir).init(), /Invalid project HEAD/);
  } finally { await rm(dir, { recursive: true, force: true }); }
});
test('full HTTP server restart restores latest saved source from disk', async () => {
  const current = await get();
  const files = { ...starterFiles, 'index.html': '<h1>重启仍存在</h1>' };
  assert.equal((await put(files, current.revision)).status, 200);
  const expected = await get();
  await new Promise(resolve => server.close(resolve));
  ({ server, store } = await createApp({ workspace: root }));
  server.listen(0, '127.0.0.1');
  await once(server, 'listening');
  base = `http://127.0.0.1:${server.address().port}`;
  assert.deepEqual(await get(), expected);
});

test('custom named blank and unicode files are written exactly and restored', async () => {
  const current = await get();
  const files = { ...starterFiles, '我的文件.txt': '我自己粘贴的内容\n第二行 🌍', '空白.html': '' };
  const response = await put(files, current.revision);
  assert.equal(response.status, 200);
  const saved = await response.json();
  assert.deepEqual((await get()).files, files);
  assert.equal(await readFile(path.join(root, 'revisions', saved.revision, '我的文件.txt'), 'utf8'), files['我的文件.txt']);
  assert.equal(await readFile(path.join(root, 'revisions', saved.revision, '空白.html'), 'utf8'), '');
  const restarted = new ProjectStore(root);
  await restarted.init();
  assert.deepEqual((await restarted.load()).files, files);
});
test('rename preserves content and leaves historical names untouched', async () => {
  const old = await get();
  const files = { ...old.files, '重新命名.txt': old.files['我的文件.txt'] };
  delete files['我的文件.txt'];
  assert.equal((await put(files, old.revision)).status, 200);
  const saved = await get();
  assert.equal(saved.files['重新命名.txt'], '我自己粘贴的内容\n第二行 🌍');
  assert.equal(Object.hasOwn(saved.files, '我的文件.txt'), false);
  assert.equal(await readFile(path.join(root, 'revisions', old.revision, '我的文件.txt'), 'utf8'), files['重新命名.txt']);
});
test('rejects unsafe, reserved, excessively long and case-colliding custom names', async () => {
  const current = await get();
  for (const name of ['../escape.txt', '/absolute.txt', 'dir/file.txt', 'dir\\file.txt', '.env', 'a..b', 'bad.txt.', 'CON.txt', 'a'.repeat(101), '界'.repeat(90), 'INDEX.HTML', 'toString', '__proto__']) {
    const files = Object.fromEntries([...Object.entries(starterFiles), [name, 'bad']]);
    assert.equal((await put(files, current.revision)).status, 400, name);
  }
  assert.equal((await get()).revision, current.revision);
});
test('permits 32 files and rejects 33 without changing disk', async () => {
  const current = await get();
  const files = { ...starterFiles, ...Object.fromEntries(Array.from({ length: 29 }, (_, i) => [`note-${i}.txt`, ''])) };
  assert.equal((await put(files, current.revision)).status, 200);
  const saved = await get();
  assert.equal(Object.keys(saved.files).length, 32);
  assert.equal((await put({ ...files, 'overflow.txt': '' }, saved.revision)).status, 400);
  assert.equal((await get()).revision, saved.revision);
});
test('size limit includes all custom file contents', async () => {
  const current = await get();
  assert.equal((await put({ ...starterFiles, 'large.txt': 'a'.repeat(MAX_BYTES) }, current.revision)).status, 413);
  assert.equal((await get()).revision, current.revision);
});
