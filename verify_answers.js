// official_answers.json と各年度の *_data.js の answer を照合する
const fs = require('fs');
const path = require('path');

const base = __dirname;
const official = JSON.parse(fs.readFileSync(path.join(base, 'official_answers.json'), 'utf8'));

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

const L = ['イ', 'ロ', 'ハ', 'ニ'];
let totalBad = 0;

console.log('年度'.padEnd(15) + ' 不一致  内訳');
console.log('-'.repeat(70));

for (const [file, key] of Object.entries(KEYS)) {
  const p = './' + file + '_data.js';
  global.window = {};
  delete require.cache[require.resolve(p)];
  require(p);
  const qs = window[key].questions;
  const off = official[file];
  if (!off) { console.log(file.padEnd(15) + ' 公式解答なし'); continue; }

  const bad = [];
  for (const q of qs) {
    const exp = off[String(q.id)];
    if (exp === undefined) { bad.push(`問${q.id}:公式なし`); continue; }
    if (q.answer !== exp) bad.push(`問${q.id}(data:${L[q.answer]}/公式:${L[exp]})`);
  }
  totalBad += bad.length;
  const head = file.padEnd(15) + String(bad.length).padStart(5) + '  ';
  console.log(head + (bad.length ? bad.join(' ') : 'OK'));
}

console.log('-'.repeat(70));
console.log(totalBad === 0 ? '全年度 全50問 解答一致' : `解答の不一致 合計 ${totalBad} 件`);
