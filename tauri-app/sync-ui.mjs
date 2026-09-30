/**
 * 把 web/index.html 同步为 Tauri 的静态 UI（tauri-app/ui/）
 * - importmap 的 three.js 改为本地 ./three.module.js（完全离线）
 * 用法：node tauri-app/sync-ui.mjs
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, '..');
const src = fs.readFileSync(path.join(root, 'web/index.html'), 'utf8');

const CDN = 'https://cdn.jsdelivr.net/npm/three@0.161.0/build/three.module.js';
if (!src.includes(CDN)) throw new Error('web/index.html 中未找到 three.js CDN importmap，请检查 sync-ui.mjs');

const out = src.replace(CDN, './three.module.js');
const uiDir = path.join(here, 'ui');
fs.mkdirSync(uiDir, { recursive: true });
fs.writeFileSync(path.join(uiDir, 'index.html'), out);
fs.copyFileSync(path.join(here, 'vendor/three.module.js'), path.join(uiDir, 'three.module.js'));
console.log('[sync-ui] 已生成 ui/index.html（' + (out.length / 1024).toFixed(1) + ' KB）+ three.module.js');
