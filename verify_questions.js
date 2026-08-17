// 各年度の *_data.js の問題文が、実際の問題PDF本文に存在するか照合する。
// テキスト層のあるPDF（令和4年度以降）のみ判定可能。
const fs = require('fs');
const path = require('path');

const pdfText = JSON.parse(fs.readFileSync(path.join(__dirname, 'pdf_text.json'), 'utf8'));

const KEYS = {
  r1kami: 'R1KAMI', r1shimo: 'R1SHIMO',
  r2shimo: 'R2SHIMO', r2shimo_gogo: 'R2SHIMO_GOGO',
  r3kami: 'R3KAMI', r3kami_gogo: 'R3KAMI_GOGO',
  r3shimo: 'R3SHIMO', r3shimo_gogo: 'R3SHIMO_GOGO',
  r4kami: 'R4KAMI', r4kami_gogo: 'R4KAMI_GOGO',
  r4shimo: 'R4SHIMO', r4shimo_gogo: 'R4SHIMO_GOGO',
  r5kami: 'R5KAMI', r5shimo: 'R5SHIMO', r5shimo_gogo: 'R5SHIMO_GOGO',
  r6kami: 'R6KAMI', r6shimo: 'R6SHIMO',
  r7kami: 'R7KAMI', r7shimo: 'R7SHIMO',
  r8kami: 'R8KAMI',
};

// アプリ側で付け足した案内文はPDFに存在しないので、比較前に取り除く
function stripNotes(s) {
  return String(s || '')
    .replace(/[\n\r]*[（(]\s*PDF[^）)]*[）)]/g, '')
    .replace(/[\n\r]*[（(][^）)]*参照すること[^）)]*[）)]/g, '')
    .replace(/[\n\r]*[（(][^）)]*配線図を参照[^）)]*[）)]/g, '');
}

// 比較用に正規化：記号・空白・全半角ゆれを落として文字だけ残す
function norm(s) {
  return stripNotes(s)
    .replace(/<[^>]+>/g, '')
    .normalize('NFKC')
    .replace(/[\s　]/g, '')
    .replace(/[，、。．・「」『』（）()［］\[\]〔〕【】:：;；,\.\-−–—~〜"'"']/g, '')
    .toLowerCase();
}

// n-gram の一致率で「PDFに実在するか」を測る
function coverage(needle, hay, n = 6) {
  if (needle.length < n) return 1;
  let hit = 0, total = 0;
  for (let i = 0; i + n <= needle.length; i += 2) {
    total++;
    if (hay.includes(needle.slice(i, i + n))) hit++;
  }
  return total ? hit / total : 1;
}

const THRESHOLD = 0.5; // これ未満なら「PDFに見当たらない」と判定

// PDF側のテキスト層が壊れているため誤検出になる問題（目視でPDFと一致を確認済み）
const KNOWN_FALSE_POSITIVES = {
  // 材料表面の型式表示がPDF内で特殊フォント化けしており抽出できない
  r5kami: [16],
};

console.log('年度'.padEnd(15) + '判定  疑わしい問題');
console.log('-'.repeat(78));

const summary = [];
for (const [file, key] of Object.entries(KEYS)) {
  const raw = pdfText[file] || '';
  const hay = norm(raw);
  if (hay.length < 3000) {
    console.log(file.padEnd(15) + '判定不可（スキャンPDFでテキスト層なし）');
    summary.push([file, null]);
    continue;
  }
  global.window = {};
  const p = './' + file + '_data.js';
  delete require.cache[require.resolve(p)];
  require(p);
  const qs = window[key].questions;

  const skip = new Set(KNOWN_FALSE_POSITIVES[file] || []);
  const bad = [];
  for (const q of qs) {
    if (skip.has(q.id)) continue;
    const body = norm(String(q.q).replace(/^【問\d+】/, ''));
    const cov = coverage(body, hay);
    if (cov < THRESHOLD) bad.push(q.id);
  }
  summary.push([file, bad]);
  console.log(file.padEnd(15) + String(bad.length).padStart(3) + '件  ' + (bad.length ? bad.join(',') : 'OK'));
}

console.log('-'.repeat(78));
const checked = summary.filter(([, b]) => b !== null);
const totalBad = checked.reduce((a, [, b]) => a + b.length, 0);
console.log(`判定できた ${checked.length} 年度で 疑わしい問題文 合計 ${totalBad} 件`);
