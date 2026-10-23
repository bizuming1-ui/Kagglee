import { defineConfig } from '@playwright/test';
import chromium from '@sparticuz/chromium';
import { readFile, mkdir, writeFile } from 'node:fs/promises';
import { brotliDecompressSync } from 'node:zlib';
import { execFileSync } from 'node:child_process';
import path from 'node:path';

// The npm-distributed browser works without a CDN download. Its bundled NSS
// libraries also support this minimal Linux environment. All binaries stay in node_modules.
const libraryDir = path.resolve('node_modules/.cache/kagglee-chromium');
await mkdir(libraryDir, { recursive: true });
const archive = path.join(libraryDir, 'al2023.tar');
await writeFile(archive, brotliDecompressSync(await readFile('node_modules/@sparticuz/chromium/bin/al2023.tar.br')));
execFileSync('tar', ['-xf', archive, '-C', libraryDir]);
const args = chromium.args.filter(arg => ![
  '--single-process', '--disable-web-security', '--allow-running-insecure-content',
  '--disable-site-isolation-trials'
].includes(arg) && !arg.includes('IsolateOrigins'));
export default defineConfig({
  testDir: './tests/browser', fullyParallel: false, workers: 1, timeout: 30000,
  use: {
    baseURL: 'http://127.0.0.1:3100', viewport: { width: 1440, height: 900 },
    launchOptions: {
      executablePath: await chromium.executablePath(), args,
      env: { ...process.env, LD_LIBRARY_PATH: `${libraryDir}/lib:${process.env.LD_LIBRARY_PATH || ''}` }
    },
    trace: 'retain-on-failure'
  },
  webServer: { command: 'node tests/e2e-server.js', url: 'http://127.0.0.1:3100', reuseExistingServer: false },
  reporter: [['list']]
});
