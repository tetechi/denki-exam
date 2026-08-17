// 選択肢が「イ．」のみで中身が空の問題に、表示用の注記を入れる。
// 対象はいずれも選択肢が写真・図で示される問題（PDF本文にも文字の選択肢は無い）。
const fs = require('fs');
const path = require('path');

const KEYS = {
  r7kami: 'R7KAMI', r7shimo: 'R7SHIMO', r6shimo: 'R6SHIMO',
  r4shimo: 'R4SHIMO', r4shimo_gogo: 'R4SHIMO_GOGO',
  r3shimo_gogo: 'R3SHIMO_GOGO', r5shimo_gogo: 'R5SHIMO_GOGO',
};

const LETTERS = ['イ', 'ロ', 'ハ', 'ニ'];
// 空の選択肢配列にマッチ（'イ．' 形式と 'イ' 形式の両方）
const EMPTY_RE = /choices:\s*\[\s*'イ．?'\s*,\s*'ロ．?'\s*,\s*'ハ．?'\s*,\s*'ニ．?'\s*\]/g;

let grand = 0;
for (const [file, key] of Object.entries(KEYS)) {
  const p = path.join(__dirname, file + '_data.js');
  let src = fs.readFileSync(p, 'utf8');

  // どの問題が空かを事前に把握し、問題文から写真/図を判定する
  global.window = {};
  delete require.cache[require.resolve('./' + file + '_data.js')];
  require('./' + file + '_data.js');
  const qs = window[key].questions;
  const emptyIds = qs
    .filter(q => q.choices.every(c => /^[イロハニ]．?\s*$/.test(c)))
    .map(q => q.id);

  // 出現順に「写真参照 / 図参照」を割り当てる（空の配列は出現順＝ID順）
  const labels = emptyIds.map(id => {
    const q = qs.find(x => x.id === id);
    return /写真/.test(q.q) ? '（写真参照）' : '（図参照）';
  });

  let i = 0;
  src = src.replace(EMPTY_RE, (m) => {
    const label = labels[i] || '（図参照）';
    const sep = m.includes('イ．') ? '．' : '';
    i++;
    return `choices: [${LETTERS.map(L => `'${L}${sep}${label}'`).join(', ')}]`;
  });

  if (i !== emptyIds.length) {
    console.log(`${file}: 置換数 ${i} が 空選択肢数 ${emptyIds.length} と一致しません。スキップします。`);
    continue;
  }

  fs.writeFileSync(p, src);
  console.log(`${file}: ${i} 問を補完 -> ${emptyIds.join(',')}`);
  grand += i;
}
console.log(`\n合計 ${grand} 問`);
