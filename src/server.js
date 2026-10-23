import http from 'node:http';
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { ProjectStore, HttpError, MAX_BYTES, starterFiles } from './store.js';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const assets = new Map([
  ['/', ['index.html', 'text/html; charset=utf-8']],
  ['/app.js', ['app.js', 'text/javascript; charset=utf-8']],
  ['/file-rules.js', ['file-rules.js', 'text/javascript; charset=utf-8']],
  ['/styles.css', ['styles.css', 'text/css; charset=utf-8']],
  ['/fonts/noto-sans-sc.woff2', ['fonts/noto-sans-sc.woff2', 'font/woff2']],
]);
function json(res, status, data) {
  res.writeHead(status, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' });
  res.end(JSON.stringify(data));
}
async function parseBody(req) {
  if (!/^application\/json(?:\s*;|$)/i.test(req.headers['content-type'] || '')) throw new HttpError(415, '请求必须使用 application/json。');
  const chunks = [];
  let size = 0;
  // JSON escaping can make a valid 1 MiB source up to six times larger.
  for await (const chunk of req) {
    size += chunk.length;
    if (size > MAX_BYTES * 6 + 4096) throw new HttpError(413, '请求过大。');
    chunks.push(chunk);
  }
  try { return JSON.parse(Buffer.concat(chunks).toString('utf8')); }
  catch { throw new HttpError(400, 'JSON 格式无效。'); }
}
export async function createApp({ workspace = process.env.WORKSPACE_DIR || path.join(ROOT, 'workspace') } = {}) {
  const store = new ProjectStore(workspace);
  await store.init();
  const server = http.createServer(async (req, res) => {
    res.setHeader('X-Content-Type-Options', 'nosniff');
    res.setHeader('Referrer-Policy', 'no-referrer');
    try {
      const url = new URL(req.url, 'http://internal');
      if (url.pathname === '/api/example' && req.method === 'GET') return json(res, 200, { files: starterFiles });
      if (url.pathname === '/api/project') {
        if (req.method === 'GET') return json(res, 200, await store.load());
        if (req.method === 'PUT') {
          // Preview runs in an opaque sandbox origin. Null and cross-site origins cannot write.
          const origin = req.headers.origin;
          let originHost;
          try { if (origin) originHost = new URL(origin).host; } catch { throw new HttpError(403, '不允许此来源保存项目。'); }
          if (req.headers['sec-fetch-site'] === 'cross-site' || (origin && originHost !== req.headers.host)) {
            throw new HttpError(403, '不允许跨站保存项目。');
          }
          const body = await parseBody(req);
          if (!body || typeof body !== 'object' || Array.isArray(body) ||
              Object.keys(body).sort().join(',') !== 'baseRevision,files') throw new HttpError(400, '保存请求结构无效。');
          return json(res, 200, await store.save(body.files, body.baseRevision));
        }
        res.setHeader('Allow', 'GET, PUT');
        return json(res, 405, { error: '此接口不支持该请求方法。' });
      }
      if (req.method !== 'GET' && req.method !== 'HEAD') return json(res, 405, { error: '不支持的请求方法。' });
      const asset = assets.get(url.pathname);
      if (!asset) return json(res, 404, { error: '未找到资源。' });
      const content = await readFile(path.join(ROOT, 'public', asset[0]));
      res.writeHead(200, {
        'Content-Type': asset[1], 'Cache-Control': 'no-cache',
        'Content-Security-Policy': "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; frame-src 'self' about:; connect-src 'self'; object-src 'none'; base-uri 'none'"
      });
      res.end(req.method === 'HEAD' ? undefined : content);
    } catch (error) {
      if (!res.headersSent) {
        if (!error.status) console.error('Request failed:', error.message);
        json(res, error.status || 500, { error: error.status ? error.message : '项目读写失败，请检查磁盘权限和服务日志。' });
      } else res.end();
    }
  });
  server.requestTimeout = 15000;
  server.headersTimeout = 10000;
  return { server, store };
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const { server } = await createApp();
  const port = Number(process.env.PORT || 3000);
  server.listen(port, '0.0.0.0', () => console.log(`Kagglee Studio listening on 0.0.0.0:${server.address().port}`));
  for (const signal of ['SIGINT', 'SIGTERM']) process.on(signal, () => server.close(() => process.exit(0)));
}
