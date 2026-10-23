import { mkdtemp, rm } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { createApp } from '../src/server.js';
const dir = await mkdtemp(path.join(os.tmpdir(), 'kagglee-e2e-'));
const { server } = await createApp({ workspace: dir });
server.listen(3100, '0.0.0.0', () => console.log('E2E server ready'));
for (const signal of ['SIGTERM', 'SIGINT']) process.on(signal, () => server.close(async () => {
  await rm(dir, { recursive: true, force: true });
  process.exit(0);
}));
