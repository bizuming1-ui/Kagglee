import { createHash, randomUUID } from 'node:crypto';
import { mkdir, open, readFile, rename, lstat, readdir, unlink } from 'node:fs/promises';
import path from 'node:path';

const SESSION_RE = /^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
const SLOT = {
  code: { label: '完整Kaggle代码', max: 20 * 1024 * 1024, ext: new Set(['.py', '.ipynb', '.zip']) },
  reference_audio: { label: '参考语音', max: 64 * 1024 * 1024, ext: new Set(['.wav', '.webm', '.ogg', '.oga', '.m4a', '.mp4', '.aac', '.mp3']) },
  generated_wav: { label: '本次合成WAV', max: 64 * 1024 * 1024, ext: new Set(['.wav']) },
  diagnostics_json: { label: '脱敏诊断JSON', max: 4 * 1024 * 1024, ext: new Set(['.json']) },
};
const jsonBytes = value => Buffer.from(JSON.stringify(value, null, 2) + '\n');
const sha = bytes => createHash('sha256').update(bytes).digest('hex');
const isDir = async p => { const s = await lstat(p); return s.isDirectory() && !s.isSymbolicLink(); };

export class UploadError extends Error { constructor(status, message) { super(message); this.status = status; } }

export class KaggleUploadStore {
  constructor(workspace) { this.workspace = path.resolve(workspace); this.root = path.join(this.workspace, 'kaggle-evidence'); this.queues = new Map(); }
  async init() {
    await mkdir(this.workspace, { recursive: true });
    if (!(await isDir(this.workspace))) throw new Error('workspace directory is unsafe');
    await mkdir(this.root, { recursive: true, mode: 0o700 });
    if (!(await isDir(this.root))) throw new Error('upload directory is unsafe');
    await chmodDir(this.root);
  }
  sessionDir(id) {
    if (!SESSION_RE.test(id)) throw new UploadError(404, '上传批次不存在。');
    return path.join(this.root, id);
  }
  async readSession(id) {
    const dir = this.sessionDir(id);
    if (!(await isDir(dir))) throw new UploadError(404, '上传批次不存在。');
    let record;
    try { record = JSON.parse(await readFile(path.join(dir, 'manifest.json'), 'utf8')); }
    catch { throw new UploadError(500, '上传批次清单损坏。'); }
    return { dir, record };
  }
  async list() {
    const out = [];
    for (const name of await readdir(this.root)) {
      if (!SESSION_RE.test(name)) continue;
      try { const { record } = await this.readSession(name); out.push(record); } catch {}
    }
    return out.sort((a, b) => b.created_at.localeCompare(a.created_at));
  }
  async create(name) {
    if (typeof name !== 'string' || !name.trim() || [...name.trim()].length > 80 || /[\u0000-\u001f\u007f]/u.test(name))
      throw new UploadError(400, '请自行填写批次名称（1–80字符）。');
    const id = randomUUID(), dir = this.sessionDir(id);
    await mkdir(dir, { mode: 0o700 });
    const record = { id, name: name.trim(), created_at: new Date().toISOString(), storage: `workspace/kaggle-evidence/${id}`, files: {} };
    await this.writeManifest(dir, record);
    return record;
  }
  async writeManifest(dir, record) {
    const tmp = path.join(dir, `.manifest-${randomUUID()}.tmp`);
    const f = await open(tmp, 'wx', 0o600);
    try { await f.writeFile(jsonBytes(record)); await f.sync(); } finally { await f.close(); }
    await rename(tmp, path.join(dir, 'manifest.json'));
    const d = await open(dir, 'r'); try { await d.sync(); } finally { await d.close(); }
  }
  async readRequest(req, max) {
    const chunks = []; let n = 0;
    for await (const chunk of req) { n += chunk.length; if (n > max) throw new UploadError(413, '文件超过该类型上传上限。'); chunks.push(chunk); }
    if (!n) throw new UploadError(400, '文件为空。');
    return Buffer.concat(chunks, n);
  }
  validate(slot, filename, bytes) {
    const spec = SLOT[slot]; if (!spec) throw new UploadError(404, '未知文件类型。');
    if (typeof filename !== 'string' || filename.length > 180 || filename !== path.basename(filename) || /[\u0000-\u001f\u007f/\\]/u.test(filename))
      throw new UploadError(400, '文件名无效；请直接选择本地文件。');
    const ext = path.extname(filename).toLowerCase();
    if (!spec.ext.has(ext)) throw new UploadError(415, `${spec.label}文件扩展名不受支持。`);
    if (slot === 'generated_wav' || (slot === 'reference_audio' && ext === '.wav')) {
      if (bytes.length < 44 || bytes.toString('ascii', 0, 4) !== 'RIFF' || bytes.toString('ascii', 8, 12) !== 'WAVE')
        throw new UploadError(415, 'WAV文件签名无效。');
    } else if (slot === 'reference_audio') {
      const wav = bytes.length >= 12 && bytes.toString('ascii', 0, 4) === 'RIFF' && bytes.toString('ascii', 8, 12) === 'WAVE';
      const webm = bytes.length >= 4 && bytes.subarray(0, 4).equals(Buffer.from([0x1a, 0x45, 0xdf, 0xa3]));
      const ogg = bytes.length >= 4 && bytes.toString('ascii', 0, 4) === 'OggS';
      const mp4 = bytes.length >= 12 && bytes.toString('ascii', 4, 8) === 'ftyp';
      const mp3 = bytes.length >= 3 && (bytes.toString('ascii', 0, 3) === 'ID3' || (bytes[0] === 0xff && (bytes[1] & 0xe0) === 0xe0));
      const aac = bytes.length >= 2 && bytes[0] === 0xff && (bytes[1] & 0xf6) === 0xf0;
      if (!(wav || webm || ogg || mp4 || mp3 || aac)) throw new UploadError(415, '参考音频容器签名无法识别；未保存文件。');
    } else if (slot === 'diagnostics_json') {
      let obj; try { obj = JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(bytes)); } catch { throw new UploadError(400, '诊断JSON无效或不是UTF-8。'); }
      if (!obj || typeof obj !== 'object' || Array.isArray(obj)) throw new UploadError(400, '诊断JSON应为对象。');
    } else if (slot === 'code' && ext !== '.zip') {
      try { new TextDecoder('utf-8', { fatal: true }).decode(bytes); } catch { throw new UploadError(400, '代码文件必须是有效UTF-8文本。'); }
    } else if (slot === 'code' && ext === '.zip' && !(bytes[0] === 0x50 && bytes[1] === 0x4b)) throw new UploadError(415, 'ZIP文件签名无效。');
    return spec;
  }
  async upload(id, slot, filename, req) {
    const spec = SLOT[slot]; if (!spec) throw new UploadError(404, '未知文件类型。');
    const bytes = await this.readRequest(req, spec.max);
    const checked = this.validate(slot, filename, bytes);
    const previous = this.queues.get(id) || Promise.resolve();
    const operation = previous.then(async () => {
      const { dir, record } = await this.readSession(id);
      if (record.files[slot]) throw new UploadError(409, '此批次已收到该类型文件；如需替换，请新建一个批次，原文件不会覆盖。');
      const stored = `${slot}${path.extname(filename).toLowerCase()}`;
      const target = path.join(dir, stored), tmp = path.join(dir, `.${randomUUID()}.tmp`);
      const f = await open(tmp, 'wx', 0o600);
      try { await f.writeFile(bytes); await f.sync(); } finally { await f.close(); }
      try { await rename(tmp, target); } catch (e) { await unlink(tmp).catch(() => {}); throw e; }
      record.files[slot] = { label: checked.label, filename, stored, bytes: bytes.length, sha256: sha(bytes), content_type: req.headers['x-file-content-type'] || 'application/octet-stream', uploaded_at: new Date().toISOString() };
      try { await this.writeManifest(dir, record); } catch (e) { await unlink(target).catch(() => {}); throw e; }
      return record;
    });
    this.queues.set(id, operation.catch(() => {}));
    return operation;
  }
  async getFile(id, slot) {
    if (!SLOT[slot]) throw new UploadError(404, '未知文件类型。');
    const { dir, record } = await this.readSession(id), info = record.files[slot];
    if (!info) throw new UploadError(404, '此批次尚未上传该文件。');
    const bytes = await readFile(path.join(dir, info.stored));
    if (bytes.length !== info.bytes || sha(bytes) !== info.sha256) throw new UploadError(409, '文件完整性校验失败。');
    return { bytes, info };
  }
  async detail(id) { return (await this.readSession(id)).record; }
}
async function chmodDir(dir) { const { chmod } = await import('node:fs/promises'); await chmod(dir, 0o700); }
