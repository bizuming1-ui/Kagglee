import { mkdir, readFile, writeFile, rename, rm, readdir } from 'node:fs/promises';
import path from 'node:path';
import { randomUUID } from 'node:crypto';
import { CORE_FILES, MAX_FILES, fileNameError } from '../public/file-rules.js';

export const FILE_NAMES = CORE_FILES;
export const MAX_BYTES = 1024 * 1024;
export class HttpError extends Error {
  constructor(status, message) { super(message); this.status = status; }
}
export const starterFiles = {
  'index.html': `<main class="card">\n  <div class="badge">YOUR IDEAS, IN MOTION</div>\n  <div class="orb">✦</div>\n  <h1>Hello, possibilities.</h1>\n  <p>A little HTML. A touch of CSS. A spark of JavaScript.<br>Make something that feels like you.</p>\n  <button id="hello">Make a little magic <span>↗</span></button>\n  <div id="message" aria-live="polite">Your next great idea starts here.</div>\n</main>`,
  'style.css': `* { box-sizing: border-box; }\nbody { margin: 0; min-height: 100vh; display: grid; place-items: center; background: #f7f8fc; font-family: system-ui, sans-serif; color: #202334; padding: 24px; }\n.card { width: 100%; max-width: 580px; text-align: center; padding: 48px 24px; }\n.badge { font-size: 10px; font-weight: 700; letter-spacing: 2px; color: #7e79a4; }\n.orb { margin: 32px auto; width: 92px; height: 92px; display: grid; place-items: center; border-radius: 28px; font-size: 54px; color: white; background: linear-gradient(135deg, #b9a4ff, #7862e8); box-shadow: 0 16px 40px #8b75e83a; transform: rotate(-8deg); }\nh1 { font-size: clamp(27px, 4vw, 40px); letter-spacing: -1.7px; margin: 0 0 16px; }\np { font-size: 14px; line-height: 1.9; color: #8b8d9e; }\nbutton { margin: 20px 0 24px; border: none; border-radius: 9px; padding: 14px 22px; background: #7760df; color: white; font: 600 13px system-ui; cursor: pointer; box-shadow: 0 5px 12px #7760df25; }\nbutton:hover { background: #644bce; }\nbutton span { margin-left: 16px; }\n#message { color: #9697a7; font-size: 11px; }`,
  'script.js': `const button = document.querySelector('#hello');\n\nbutton?.addEventListener('click', () => {\n  document.querySelector('#message').textContent = 'You made it happen. Keep creating! ✨';\n  console.log('A little magic, made by you.');\n});\n\nconsole.log('Ready when you are. ✨');`
};

export function validateFiles(files) {
  if (!files || typeof files !== 'object' || Array.isArray(files) ||
      FILE_NAMES.some(name => !Object.hasOwn(files, name) || typeof files[name] !== 'string')) {
    throw new HttpError(400, '必须保留 index.html、style.css、script.js 三个字符串文件。');
  }
  const names = Object.keys(files);
  if (names.length > MAX_FILES) throw new HttpError(400, `最多保存 ${MAX_FILES} 个文件。`);
  for (const name of names) {
    const error = fileNameError(name, names, name);
    if (error) throw new HttpError(400, error);
    if (typeof files[name] !== 'string') throw new HttpError(400, '文件内容必须为字符串。');
  }
  if (names.reduce((n, name) => n + Buffer.byteLength(files[name]), 0) > MAX_BYTES) {
    throw new HttpError(413, '代码总大小不能超过 1 MiB。');
  }
}

export class ProjectStore {
  constructor(root) { this.root = path.resolve(root); this.queue = Promise.resolve(); }
  async init() {
    await mkdir(path.join(this.root, 'revisions'), { recursive: true });
    try { await this.load(); }
    catch (error) {
      // Only a missing HEAD means a new project. A corrupt existing project must not be overwritten.
      if (error.code !== 'ENOENT' || error.path !== path.join(this.root, 'HEAD.json')) throw error;
      await this.write(starterFiles);
    }
  }
  async load() {
    const head = JSON.parse(await readFile(path.join(this.root, 'HEAD.json'), 'utf8'));
    if (typeof head.revision !== 'string' || !/^[a-f0-9-]{36}$/.test(head.revision) ||
        typeof head.savedAt !== 'string' || !Number.isFinite(Date.parse(head.savedAt))) {
      throw new Error('Invalid project HEAD');
    }
    const dir = path.join(this.root, 'revisions', head.revision);
    const entries = await readdir(dir, { withFileTypes: true });
    if (entries.some(entry => !entry.isFile()) || entries.length > MAX_FILES) throw new Error('Invalid project files');
    const names = entries.map(entry => entry.name);
    const values = await Promise.all(names.map(name => readFile(path.join(dir, name), 'utf8')));
    const files = Object.fromEntries(names.map((name, i) => [name, values[i]]));
    validateFiles(files);
    return { ...head, files, storagePath: path.relative(process.cwd(), dir) || dir };
  }
  save(files, baseRevision) {
    validateFiles(files);
    if (typeof baseRevision !== 'string') throw new HttpError(400, '缺少基础版本，请先加载项目。');
    const result = this.queue.then(async () => {
      const current = await this.load();
      if (current.revision !== baseRevision) throw new HttpError(409, '项目已被其他窗口修改。请先备份当前代码，再重新加载磁盘版本。');
      return this.write(files);
    });
    this.queue = result.catch(() => {});
    return result;
  }
  async write(files) {
    validateFiles(files);
    const revision = randomUUID();
    const savedAt = new Date().toISOString();
    const dir = path.join(this.root, 'revisions', revision);
    const tempHead = path.join(this.root, `.HEAD-${revision}.tmp`);
    try {
      await mkdir(dir);
      await Promise.all(Object.keys(files).map(name => writeFile(path.join(dir, name), files[name], { flag: 'wx' })));
      await writeFile(tempHead, JSON.stringify({ revision, savedAt }, null, 2) + '\n', { flag: 'wx' });
      await rename(tempHead, path.join(this.root, 'HEAD.json'));
    } catch (error) {
      await Promise.all([rm(dir, { recursive: true, force: true }), rm(tempHead, { force: true })]);
      throw error;
    }
    return { revision, savedAt, files: { ...files }, storagePath: path.relative(process.cwd(), dir) || dir };
  }
}
