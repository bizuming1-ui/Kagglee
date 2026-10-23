export const MAX_FILES = 32;
export const CORE_FILES = ['index.html', 'style.css', 'script.js'];

// Shared by the editor and server. Names are single path components, never paths.
export function fileNameError(name, existing = [], except = null) {
  if (typeof name !== 'string' || !name || name.length > 100 || new TextEncoder().encode(name).length > 240) return '文件名不能为空，最多100个字符且不超过240字节。';
  if (name !== name.normalize('NFC') || !/^[\p{L}\p{N}_][\p{L}\p{N}_. ()-]*$/u.test(name) || name.includes('..') || /[. ]$/.test(name)) return '文件名请使用中文、字母、数字、空格、下划线、短横线和扩展名，不能包含路径或连续的点。';
  if (['__proto__', 'prototype', ...Object.getOwnPropertyNames(Object.prototype)].includes(name) || /^(?:CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\.|$)/i.test(name)) return '此文件名被系统保留，请换一个名称。';
  if (existing.some(other => other !== except && other.toLocaleLowerCase('en-US') === name.toLocaleLowerCase('en-US'))) return '同名文件已存在（不区分大小写），请换一个名称。';
  return '';
}
