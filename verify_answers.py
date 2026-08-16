"""公式解答PDFから解答を抽出し JSON に書き出す（verify_answers.js が読む）"""
import pypdfium2 as pdfium
import json, re, os

base = os.path.dirname(os.path.abspath(__file__))

# 年度キー -> 公式解答PDF
PDFS = {
    'r1kami':       '20190602_co_second_a01.pdf',
    'r1shimo':      '20191006_co_second_a01.pdf',
    'r2shimo':      '20201004_co_second_a01.pdf',
    'r2shimo_gogo': '20201004_co_second_a02.pdf',
    'r3kami':       '20210530_co_second_a01.pdf',
    'r3kami_gogo':  '20210530_co_second_a02.pdf',
    'r3shimo':      '220211024_co_second_a01.pdf',
    'r3shimo_gogo': '220211024_co_second_a02.pdf',
    'r4kami':       '20220529_co_second_a01.pdf',
    'r4kami_gogo':  '20220529_co_second_a02.pdf',
    'r4shimo':      '20221030_co_second_a01.pdf',
    'r4shimo_gogo': '20221030_co_second_a02.pdf',
    'r5kami':       '20230528_co_second_a01.pdf',
    'r5shimo':      '20231029_co_second_a01.pdf',
    'r5shimo_gogo': '20231029_co_second_a02.pdf',
    'r6kami':       '20240526_co_second_a01.pdf',
    'r6shimo':      '20241027_co_second_a01.pdf',
    'r7kami':       '20250525_co_second_a01.pdf',
    'r7shimo':      '20251026_co_second_a01.pdf',
    'r8kami':       '20260524_co_second_a01.pdf',
}

IDX = {'イ': 0, 'ロ': 1, 'ハ': 2, 'ニ': 3}

result = {}
for key, fname in PDFS.items():
    path = os.path.join(base, 'list', fname)
    if not os.path.exists(path):
        print(f'{key}: PDFなし ({fname})')
        continue
    pdf = pdfium.PdfDocument(path)
    text = pdf[0].get_textpage().get_text_range()
    # 「番号 解答」のペアを全て拾う
    pairs = re.findall(r'(\d{1,2})\s*([イロハニ])', text)
    answers = {}
    for num, ch in pairs:
        n = int(num)
        if 1 <= n <= 50:
            answers[n] = IDX[ch]
    missing = [n for n in range(1, 51) if n not in answers]
    if missing:
        print(f'{key}: 抽出できなかった問 -> {missing}')
    result[key] = {str(n): answers[n] for n in sorted(answers)}
    print(f'{key}: {len(answers)}問 抽出')

out = os.path.join(base, 'official_answers.json')
with open(out, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=1)
print('\n->', out)
